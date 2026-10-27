"""
Persistent State Checkpoint Manager.
Handles atomic reads/writes to memory/state.json for warm booting, per-file progress, speed, and ETA calculation.
"""

import os
import json
import time
import shutil
from datetime import datetime, timezone
from typing import Optional, Dict, Any

from ..models.state_model import IngestionStateModel, FileStatusModel, ProcessingStatus
from .hardware_detector import detect_hardware_device
from .logger import WikiLogger


class CheckpointManager:
    """Atomic state manager tracking per-file status, overall percentage, elapsed time, and ETA."""

    def __init__(self, output_root: str = "artifacts/output/karpathy-wiki",
                 logger: Optional[WikiLogger] = None) -> None:
        """Initializes checkpoint manager with output directory root."""
        self.output_root = os.path.abspath(output_root)
        self.state_file_path = os.path.join(self.output_root, "memory", "state.json")
        self.logger = logger or WikiLogger(os.path.join(self.output_root, "wiki", "log.md"))
        self.hw_info = detect_hardware_device()
        self.start_epoch = time.time()
        
        # Ensure memory directory exists
        os.makedirs(os.path.dirname(self.state_file_path), exist_ok=True)
        self.state = self.load_or_create_state()

    def get_timestamp(self) -> str:
        """Returns UTC ISO timestamp."""
        return datetime.now(timezone.utc).isoformat()

    def load_or_create_state(self, pdf_filename: str = "RM0468.pdf") -> IngestionStateModel:
        """Loads state from memory/state.json if present (warm boot), else creates initial state."""
        if os.path.exists(self.state_file_path):
            try:
                with open(self.state_file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                state = IngestionStateModel(**data)
                self.logger.info(f"Warm Boot Triggered: Loaded state for {state.active_file}. Resume overall={state.overall_progress_percentage:.1f}%")
                return state
            except Exception as e:
                self.logger.error(f"Failed to read existing state file: {e}. Re-initializing state.")
        
        # Default fresh state
        initial_state = IngestionStateModel(
            active_file=pdf_filename,
            total_pages=0,
            last_processed_page=0,
            chunk_size=20,
            status=ProcessingStatus.NOT_STARTED,
            hardware_device=self.hw_info["device"],
            hardware_name=self.hw_info["device_name"],
            start_time_iso=self.get_timestamp(),
            last_checkpoint_timestamp=self.get_timestamp()
        )
        return initial_state

    def save_state(self) -> None:
        """Atomically saves state model to memory/state.json."""
        self.state.last_checkpoint_timestamp = self.get_timestamp()
        dir_name = os.path.dirname(self.state_file_path)
        os.makedirs(dir_name, exist_ok=True)

        temp_path = os.path.join(dir_name, f".tmp_state_{int(time.time() * 1000)}.json")
        try:
            with open(temp_path, "w", encoding="utf-8") as f:
                f.write(self.state.model_dump_json(indent=2))
            os.replace(temp_path, self.state_file_path)
            self.logger.checkpoint(f"State saved atomically: Progress {self.state.overall_progress_percentage:.1f}% (Device: {self.state.hardware_name})")
        except Exception as e:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            self.logger.error(f"Failed to write state file: {e}")

    def update_file_status(self, file_key: str, file_type: str, file_path: str,
                           current_page: int, total_pages: int,
                           status: ProcessingStatus = ProcessingStatus.IN_PROGRESS) -> None:
        """Updates separate progress status for a specific input file."""
        file_name = os.path.basename(file_path) if file_path else "Not Selected"
        pct = round((current_page / total_pages * 100.0), 1) if total_pages > 0 else 0.0

        if file_key not in self.state.file_statuses:
            self.state.file_statuses[file_key] = FileStatusModel(
                file_type=file_type,
                file_path=file_path,
                file_name=file_name,
                status=status,
                progress_percentage=pct,
                current_page=current_page,
                total_pages=total_pages
            )
        else:
            fs = self.state.file_statuses[file_key]
            fs.file_path = file_path
            fs.file_name = file_name
            fs.status = status
            fs.progress_percentage = pct
            fs.current_page = current_page
            fs.total_pages = total_pages

        self.recalculate_overall_progress()

    def recalculate_overall_progress(self) -> None:
        """Recalculates cumulative percentage, elapsed runtime, pages/sec speed, and ETA."""
        elapsed = max(1.0, time.time() - self.start_epoch)
        self.state.elapsed_time_seconds = round(elapsed, 1)

        total_pages_sum = sum(f.total_pages for f in self.state.file_statuses.values())
        processed_pages_sum = sum(f.current_page for f in self.state.file_statuses.values())

        if total_pages_sum > 0:
            self.state.total_pages = total_pages_sum
            self.state.last_processed_page = processed_pages_sum
            self.state.overall_progress_percentage = round((processed_pages_sum / total_pages_sum * 100.0), 1)
            
            speed = processed_pages_sum / elapsed
            self.state.pages_per_second = round(speed, 2)
            
            remaining_pages = max(0, total_pages_sum - processed_pages_sum)
            if speed > 0:
                self.state.estimated_time_remaining_seconds = round(remaining_pages / speed, 1)
            else:
                self.state.estimated_time_remaining_seconds = 0.0
        
        self.save_state()

    def format_eta_str(self) -> str:
        """Formats estimated time remaining as HH:MM:SS string."""
        eta_sec = int(self.state.estimated_time_remaining_seconds)
        mins, secs = divmod(eta_sec, 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02d}:{mins:02d}:{secs:02d}"

    def format_elapsed_str(self) -> str:
        """Formats elapsed duration as HH:MM:SS string."""
        elapsed_sec = int(self.state.elapsed_time_seconds)
        mins, secs = divmod(elapsed_sec, 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02d}:{mins:02d}:{secs:02d}"

    def mark_completed(self) -> None:
        """Marks task as completely finished."""
        self.state.status = ProcessingStatus.COMPLETED
        self.state.overall_progress_percentage = 100.0
        self.state.estimated_time_remaining_seconds = 0.0
        for f in self.state.file_statuses.values():
            f.status = ProcessingStatus.COMPLETED
            f.progress_percentage = 100.0
        self.save_state()
        self.logger.info(f"Ingestion Completed in {self.format_elapsed_str()}.")
