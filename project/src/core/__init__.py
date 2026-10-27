"""
Core infrastructure package for STM32 Structured Wiki Generator.
Contains persistent state checkpoint manager and multi-verbose append-only logger.
"""

from .checkpoint_manager import CheckpointManager
from .logger import WikiLogger
from .mcu_detector import detect_mcu_metadata
from .gpu_runtime import (
    detect_system_gpu_architecture,
    get_optimal_gpu_env,
    get_adaptive_chromium_flags,
    sanitize_process_env,
    run_gpu_diagnostics,
    GpuArchitecture,
)

__all__ = [
    "CheckpointManager",
    "WikiLogger",
    "detect_mcu_metadata",
    "detect_system_gpu_architecture",
    "get_optimal_gpu_env",
    "get_adaptive_chromium_flags",
    "sanitize_process_env",
    "run_gpu_diagnostics",
    "GpuArchitecture",
]
