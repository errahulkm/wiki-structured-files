"""
Append-Only Wiki Logger.
Writes timestamped UTC operational logs to log.md and stdout.
"""

import os
from datetime import datetime, timezone


class WikiLogger:
    """Thread-safe append-only logger writing structured Markdown logs to wiki/log.md."""

    def __init__(self, log_file_path: str = "artifacts/output/structured-wiki/wiki/log.md") -> None:
        """Initializes logger with destination log.md path."""
        self.log_file_path = os.path.abspath(log_file_path)
        os.makedirs(os.path.dirname(self.log_file_path), exist_ok=True)
        self._ensure_log_header()

    def _ensure_log_header(self) -> None:
        """Writes Markdown header if file does not exist."""
        if not os.path.exists(self.log_file_path):
            with open(self.log_file_path, "w", encoding="utf-8") as f:
                f.write("# STM32 Structured Wiki Ingestion Log\n\n")
                f.write("| Timestamp (UTC) | Level | Operational Message |\n")
                f.write("|---|---|---|\n")

    def get_timestamp(self) -> str:
        """Returns UTC ISO timestamp."""
        return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    def log(self, level: str, message: str) -> None:
        """Appends log entry to log.md and prints to stdout."""
        timestamp = self.get_timestamp()
        os.makedirs(os.path.dirname(self.log_file_path), exist_ok=True)
        self._ensure_log_header()
        
        log_entry = f"| {timestamp} | {level.upper()} | {message} |\n"

        try:
            with open(self.log_file_path, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            print(f"[LOGGER ERROR] Failed to write log entry: {e}")

        print(f"[{timestamp}] [{level.upper()}] {message}")

    def info(self, message: str) -> None:
        """Logs info-level message."""
        self.log("INFO", message)

    def warning(self, message: str) -> None:
        """Logs warning-level message."""
        self.log("WARNING", message)

    def error(self, message: str) -> None:
        """Logs error-level message."""
        self.log("ERROR", message)

    def checkpoint(self, message: str) -> None:
        """Logs state checkpoint message."""
        self.log("CHECKPOINT", message)
