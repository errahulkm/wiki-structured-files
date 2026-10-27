"""
Pydantic Schema for Memory Map Regions and Base Address Mapping.
Strictly validates hexadecimal physical memory addresses for STM32 architectures.
"""

import re
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator


class MemoryMapRegion(BaseModel):
    """Specific memory region mapping (e.g., Flash, SRAM, AHB1, APB1)."""
    region_name: str = Field(..., description="Name of memory block (e.g. D1 Domain AXI SRAM)")
    bus_architecture: str = Field(..., description="Bus interface (e.g. AXI, AHB3, APB1)")
    base_address: str = Field(..., description="32-bit hexadecimal base address (e.g. 0x40021000)")
    end_address: str = Field(..., description="32-bit hexadecimal end address (e.g. 0x400213FF)")
    size_bytes: int = Field(..., ge=0, description="Size of block in bytes")
    trustzone_security: str = Field("SECURE_AND_NONSECURE", description="TrustZone security attribute")

    @field_validator("base_address", "end_address")
    @classmethod
    def validate_hex_address(cls, v: str) -> str:
        clean = v.strip()
        if not re.match(r'^0x[0-9A-Fa-f]{8}$', clean) and not re.match(r'^0x[0-9A-Fa-f]+$', clean):
            raise ValueError(f"Invalid memory address format: {v}")
        return clean


class SystemMemoryMap(BaseModel):
    """Complete device system memory map containing all mapped regions."""
    target_device: str = Field(..., description="Microcontroller device family (e.g. STM32H723)")
    regions: List[MemoryMapRegion] = Field(default_factory=list)
