"""
Parsers package for STM32 Karpathy-Wiki Generator.
Contains Docling PDF document loader and hardware register bitfield extractor.
"""

from .docling_extractor import DoclingPDFExtractor
from .register_parser import RegisterParser

__all__ = ["DoclingPDFExtractor", "RegisterParser"]
