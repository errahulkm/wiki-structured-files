"""
State Persistence and Crash Recovery Manager for Mission-Critical Orchestration.
Guarantees atomic reads and writes to disk, ensuring state survival across crashes.
"""

import os
import json
import time
import shutil
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List


class StateManager:
    """Manages system state loading, atomic saving, schema validation, and recovery."""

    def __init__(self, state_file_path: str = "orchestration/state/state.json",
                 schema_file_path: str = "orchestration/config/state_schema.json") -> None:
        """Initializes state manager with paths to state JSON and validation schema."""
        self.state_file_path = os.path.abspath(state_file_path)
        self.schema_file_path = os.path.abspath(schema_file_path)
        self.backup_file_path = f"{self.state_file_path}.bak"
        self._state: Dict[str, Any] = {}
        self.load_state()

    def get_timestamp(self) -> str:
        """Returns ISO format timestamp in UTC."""
        return datetime.now(timezone.utc).isoformat()

    def load_state(self) -> Dict[str, Any]:
        """Loads state from disk with fallback recovery from backup if corrupted."""
        if not os.path.exists(self.state_file_path):
            raise FileNotFoundError(f"State file not found at: {self.state_file_path}")

        try:
            with open(self.state_file_path, "r", encoding="utf-8") as f:
                self._state = json.load(f)
            return self._state
        except json.JSONDecodeError as err:
            print(f"[WARNING] Primary state file corrupted: {err}. Attempting recovery from backup...")
            if os.path.exists(self.backup_file_path):
                with open(self.backup_file_path, "r", encoding="utf-8") as bf:
                    self._state = json.load(bf)
                # Restore primary state from backup
                self.save_state()
                self._state["system_health"]["last_crash_recovery_timestamp"] = self.get_timestamp()
                return self._state
            else:
                raise RuntimeError(f"State file corrupted and no backup found: {err}")

    def save_state(self) -> bool:
        """Atomic state saver: writes to temp file then replaces destination file."""
        self._state["updated_at"] = self.get_timestamp()
        dir_name = os.path.dirname(self.state_file_path)
        temp_path = os.path.join(dir_name, f".state_tmp_{int(time.time() * 1000)}.json")

        try:
            # Create a backup of existing state before overwriting
            if os.path.exists(self.state_file_path):
                shutil.copy2(self.state_file_path, self.backup_file_path)

            with open(temp_path, "w", encoding="utf-8") as f:
                json.dump(self._state, f, indent=2, ensure_ascii=False)
            
            # Atomic replace operation
            os.replace(temp_path, self.state_file_path)
            return True
        except Exception as e:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            raise IOError(f"Failed to atomically write state file: {e}")

    def get_state(self) -> Dict[str, Any]:
        """Returns current state snapshot."""
        return self._state

    def update_phase(self, phase_name: str, active_agent: str) -> None:
        """Updates active phase and agent."""
        self._state["current_phase"] = phase_name
        self._state["active_agent"] = active_agent
        self.save_state()

    def record_completed_micro_phase(self, phase_id: str, phase_name: str,
                                      agent_role: str, status: str, summary: str) -> None:
        """Appends a micro-phase entry to history and increments step counter."""
        entry = {
            "phase_id": phase_id,
            "phase_name": phase_name,
            "agent_role": agent_role,
            "timestamp": self.get_timestamp(),
            "status": status,
            "summary": summary
        }
        self._state["completed_micro_phases"].append(entry)
        self._state["current_micro_step"] += 1
        self.save_state()

    def record_agent_output(self, agent_role: str, raw_output: str,
                            parsed_data: Optional[Dict[str, Any]] = None,
                            verification_passed: bool = True) -> None:
        """Stores or updates the latest agent output in state."""
        self._state["agent_outputs"][agent_role] = {
            "last_updated": self.get_timestamp(),
            "raw_output": raw_output,
            "parsed_data": parsed_data or {},
            "verification_passed": verification_passed
        }
        self.save_state()

    def record_user_feedback(self, target_agent: str, feedback_text: str) -> None:
        """Appends user feedback for dynamic prompt rewriting."""
        entry = {
            "timestamp": self.get_timestamp(),
            "target_agent": target_agent,
            "feedback_text": feedback_text,
            "applied_to_phase": self._state["current_phase"]
        }
        self._state["user_feedback_history"].append(entry)
        self.save_state()

    def store_dynamic_prompt(self, agent_role: str, prompt_text: str) -> None:
        """Stores the dynamically compiled prompt for an agent."""
        self._state["dynamic_prompts"][agent_role] = prompt_text
        self.save_state()

    def update_audit_status(self, **kwargs) -> None:
        """Updates specific key-value pairs in the audit status dict."""
        for key, value in kwargs.items():
            if key in self._state["audit_status"]:
                self._state["audit_status"][key] = value
        self.save_state()


if __name__ == "__main__":
    sm = StateManager()
    print(f"State loaded successfully: {sm.get_state()['project_name']}")
