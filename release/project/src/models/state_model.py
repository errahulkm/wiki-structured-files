"""
Pydantic Schema for State Checkpointing and Warm Boot Resume Engine.
Maintains persistent ingestion status, per-file metrics, GPU execution state, and ETA tracking.
"""

from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class ProcessingStatus(str, Enum):
    """Execution status enum for ingestion state."""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    PAUSED_DUE_TO_TOKEN_LIMIT = "paused_due_to_token_limit"
    COMPLETED = "completed"
    ERROR = "error"
    SKIPPED = "skipped"


class FileStatusModel(BaseModel):
    """Per-input-file separate status and progress tracking payload."""
    file_type: str = Field(..., description="File category (e.g. Reference Manual, Datasheet)")
    file_path: str = Field("", description="File system path to source PDF")
    file_name: str = Field("", description="Basename of target file")
    status: ProcessingStatus = Field(ProcessingStatus.NOT_STARTED, description="Current file status")
    progress_percentage: float = Field(0.0, ge=0.0, le=100.0, description="Individual file percentage")
    current_page: int = Field(0, ge=0, description="Processed page index")
    total_pages: int = Field(0, ge=0, description="Total pages in target PDF")
    elapsed_seconds: float = Field(0.0, ge=0.0, description="Processing duration in seconds")


class IngestionStateModel(BaseModel):
    """State tracking payload saved to memory/state.json for warm booting and telemetry."""
    active_file: str = Field(..., description="Currently ingested PDF source file")
    total_pages: int = Field(0, ge=0, description="Total cumulative pages across active files")
    last_processed_page: int = Field(0, ge=0, description="Last page successfully processed")
    overall_progress_percentage: float = Field(0.0, ge=0.0, le=100.0, description="Overall task completion percentage")
    chunk_size: int = Field(20, ge=1, description="Page block chunk size")
    status: ProcessingStatus = Field(ProcessingStatus.NOT_STARTED, description="Current execution state")
    
    # GPU Acceleration info
    hardware_device: str = Field("cpu", description="Execution device ('cuda' or 'cpu')")
    hardware_name: str = Field("CPU Fallback", description="GPU device name or CPU")
    
    # Time Tracking & Speed
    start_time_iso: Optional[str] = Field(None, description="ISO timestamp when task started")
    elapsed_time_seconds: float = Field(0.0, ge=0.0, description="Total elapsed runtime in seconds")
    pages_per_second: float = Field(0.0, ge=0.0, description="Current processing speed")
    estimated_time_remaining_seconds: float = Field(0.0, ge=0.0, description="Estimated time remaining (ETA)")
    
    # Granular per-file status dictionary
    file_statuses: Dict[str, FileStatusModel] = Field(default_factory=dict, description="Status map for each input PDF")
    
    extracted_register_count: int = Field(0, ge=0, description="Total register JSON files produced")
    extracted_markdown_count: int = Field(0, ge=0, description="Total Markdown theory files generated")
    completed_chapters: List[str] = Field(default_factory=list, description="List of processed chapter names")
    last_checkpoint_timestamp: Optional[str] = Field(None, description="ISO timestamp of last save")
    error_log: Optional[str] = Field(None, description="Latest error message if status is ERROR")
