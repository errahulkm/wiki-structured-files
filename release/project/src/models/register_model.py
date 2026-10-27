"""
Pydantic Schema for Hardware Registers and Bitfields.
Strictly maps STM32 peripheral register attributes into JSON format.
"""

import re
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, field_validator


class ErrataNote(BaseModel):
    """Note appended when an Errata Sheet modifies or flags a register behavior."""
    errata_id: str = Field(..., description="Errata document identifier (e.g. ES0491)")
    description: str = Field(..., description="Description of register anomaly or workaround")
    date_added: str = Field(..., description="Timestamp when note was ingested")


class RegisterBitField(BaseModel):
    """Bit-field specification within a 32-bit hardware register."""
    name: str = Field(..., description="Bit-field name (e.g. HSION, PLL1ON)")
    bit_offset: int = Field(..., ge=0, le=31, description="Starting bit position (0 to 31)")
    bit_width: int = Field(..., ge=1, le=32, description="Bit field width in bits")
    access: str = Field(..., description="Access permission (R/W, RO, WO, R/W1C)")
    reset_value: str = Field(..., description="Reset state value (e.g. 0b0, 0x0)")
    description: str = Field(..., description="Functional description of bit field")

    @field_validator("bit_offset")
    @classmethod
    def validate_bit_offset(cls, v: int) -> int:
        if not (0 <= v <= 31):
            raise ValueError(f"Bit offset must be between 0 and 31 inclusive, got {v}")
        return v

    @field_validator("access")
    @classmethod
    def validate_access(cls, v: str) -> str:
        clean = v.strip().upper()
        allowed = {"R/W", "RO", "WO", "W1C", "R/W1C", "RC_W0", "RS", "NONE"}
        if not any(a in clean for a in allowed):
            # Keep raw string if non-standard, but normalize whitespace
            return clean
        return clean


class RegisterModel(BaseModel):
    """Complete specification for a single 32-bit hardware register."""
    peripheral: str = Field(..., description="Peripheral acronym (e.g. RCC, GPIOA, DMA1)")
    register_name: str = Field(..., description="Short register name (e.g. RCC_CR, GPIOA_MODER)")
    long_name: str = Field(..., description="Full descriptive name of the register")
    address_offset: str = Field(..., description="Hexadecimal offset from peripheral base (e.g. 0x00)")
    reset_value: str = Field(..., description="32-bit hex reset value (e.g. 0x00000001)")
    description: str = Field(..., description="High-level register purpose")
    bit_fields: List[RegisterBitField] = Field(default_factory=list, description="Array of bit-fields")
    errata_notes: List[ErrataNote] = Field(default_factory=list, description="Appended errata Sheet notes")

    @field_validator("address_offset")
    @classmethod
    def validate_hex_offset(cls, v: str) -> str:
        v_clean = v.strip()
        if not re.match(r'^0x[0-9A-Fa-f]+$', v_clean):
            raise ValueError(f"Invalid hex address offset: {v}")
        return v_clean


class RegisterIndex(BaseModel):
    """Index catalog mapping all register names to their respective JSON files."""
    total_registers: int
    peripherals: List[str]
    register_files: Dict[str, str]
