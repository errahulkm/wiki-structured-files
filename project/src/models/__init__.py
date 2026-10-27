"""
Models package for STM32 Karpathy-Wiki Generator.
Defines Pydantic data schemas for registers, memory maps, per-file status, and execution state.
"""

from .register_model import RegisterBitField, RegisterModel, RegisterIndex
from .memory_map_model import MemoryMapRegion, SystemMemoryMap
from .state_model import IngestionStateModel, FileStatusModel, ProcessingStatus

__all__ = [
    "RegisterBitField",
    "RegisterModel",
    "RegisterIndex",
    "MemoryMapRegion",
    "SystemMemoryMap",
    "IngestionStateModel",
    "FileStatusModel",
    "ProcessingStatus",
]
