"""
Dynamic MCU and Reference Manual Metadata Detector.
Extracts MCU family, Reference Manual number, and device titles from PDF paths, filenames, or directory names.
"""

import os
import re
from typing import Dict, Any, Optional, Tuple


def detect_mcu_metadata(source_hint: Optional[str] = None, wiki_root: Optional[str] = None) -> Dict[str, str]:
    """
    Detects MCU family, RM number, and human-friendly display titles.
    
    Args:
        source_hint: Path to PDF, filename, or device string.
        wiki_root: Output directory path where files or raw PDFs reside.
        
    Returns:
        Dictionary with keys:
            - mcu_family: e.g. "STM32U3", "STM32H7", "STM32F4"
            - rm_number: e.g. "RM0487", "RM0468", "RM0090"
            - target_device: e.g. "STM32U3C5ZI", "STM32H723VE"
            - display_title: e.g. "STM32U3 Series (RM0487)"
            - graph_title: e.g. "STM32U3 Knowledge Graph"
            - audit_title: e.g. "STM32U3 Karpathy Wiki Corpus Independent Audit"
            - audit_subtitle: e.g. "Multi-Algorithmic Cross-Verification against STMicroelectronics RM0487 PDF"
    """
    # 1. Gather all clues
    clues = []
    if wiki_root:
        dna_path = os.path.join(wiki_root, "mcu_dna.json")
        if os.path.exists(dna_path):
            try:
                import json
                with open(dna_path, "r", encoding="utf-8") as f:
                    dna_data = json.load(f)
                mcu_fam = dna_data.get("mcu_family") or "STM32"
                rm_num = dna_data.get("rm_number") or "RM"
                tgt_dev = dna_data.get("target_device") or mcu_fam
                return {
                    "mcu_family": mcu_fam,
                    "rm_number": rm_num,
                    "target_device": tgt_dev,
                    "display_title": f"{mcu_fam} Series ({rm_num})",
                    "graph_title": f"{mcu_fam} Knowledge Graph",
                    "audit_title": f"{mcu_fam} Karpathy Wiki Corpus Independent Audit",
                    "audit_subtitle": f"Multi-Algorithmic Cross-Verification against STMicroelectronics {rm_num} PDF"
                }
            except Exception:
                pass

    if source_hint:
        if str(source_hint).lower().endswith(".pdf"):
            clues.append(os.path.basename(str(source_hint)))
        clues.append(str(source_hint))
    if wiki_root:
        clues.append(str(wiki_root))
        raw_dir = os.path.join(wiki_root, "raw")
        if os.path.exists(raw_dir):
            for f in os.listdir(raw_dir):
                if f.lower().endswith(".pdf"):
                    clues.append(f)

    combined_text = " ".join(clues)

    # 2. Extract MCU Family (e.g. STM32H7, STM32U3, STM32F4, STM32G4, STM32L4, STM32WB, STM32WL, etc.)
    mcu_match = re.search(r'\b(STM32[A-Z0-9]{2,8})\b', combined_text, re.IGNORECASE)
    if mcu_match:
        raw_mcu = mcu_match.group(1).upper()
        # Normalize to family (e.g. STM32U3C5ZI -> STM32U3, STM32H723VE -> STM32H7)
        fam_match = re.match(r'^(STM32[A-Z][0-9])', raw_mcu)
        mcu_family = fam_match.group(1) if fam_match else raw_mcu[:7]
        target_device = raw_mcu
    else:
        # Check for generic U3 / H7 / F4
        if re.search(r'\b(u3|stm32u3)\b', combined_text, re.IGNORECASE):
            mcu_family = "STM32U3"
            target_device = "STM32U3 Series"
        elif re.search(r'\b(h7|stm32h7)\b', combined_text, re.IGNORECASE):
            mcu_family = "STM32H7"
            target_device = "STM32H7 Series"
        elif re.search(r'\b(f4|stm32f4)\b', combined_text, re.IGNORECASE):
            mcu_family = "STM32F4"
            target_device = "STM32F4 Series"
        elif re.search(r'\b(g4|stm32g4)\b', combined_text, re.IGNORECASE):
            mcu_family = "STM32G4"
            target_device = "STM32G4 Series"
        elif re.search(r'\b(l4|stm32l4)\b', combined_text, re.IGNORECASE):
            mcu_family = "STM32L4"
            target_device = "STM32L4 Series"
        else:
            mcu_family = "STM32"
            target_device = "STM32 Microcontroller"

    # 3. Extract RM Number (e.g. RM0487, RM0468, RM0090, RM0399)
    rm_match = re.search(r'\b(RM[0-9]{4})\b', combined_text, re.IGNORECASE)
    if rm_match:
        rm_number = rm_match.group(1).upper()
    else:
        if mcu_family == "STM32U3":
            rm_number = "RM0487"
        elif mcu_family == "STM32H7":
            rm_number = "RM0468"
        elif mcu_family == "STM32F4":
            rm_number = "RM0090"
        else:
            rm_number = "Reference Manual"

    # 4. Construct human-readable titles
    display_title = f"{mcu_family} Series ({rm_number})" if rm_number != "Reference Manual" else f"{mcu_family} Series Reference Manual"
    graph_title = f"{mcu_family} Knowledge Graph"
    audit_title = f"{mcu_family} Karpathy Wiki Corpus Independent Audit"
    audit_subtitle = f"Multi-Algorithmic Cross-Verification against STMicroelectronics {rm_number} PDF"

    return {
        "mcu_family": mcu_family,
        "rm_number": rm_number,
        "target_device": target_device,
        "display_title": display_title,
        "graph_title": graph_title,
        "audit_title": audit_title,
        "audit_subtitle": audit_subtitle
    }


def classify_st_document(file_path: str) -> Dict[str, Any]:
    """
    Classifies an ST document into REFERENCE_MANUAL, DATASHEET, ERRATA_SHEET,
    PROGRAMMING_MANUAL, APPLICATION_NOTE, or UNKNOWN.
    """
    if not file_path:
        return {"doc_type": "UNKNOWN", "is_reference_manual": False, "doc_code": "UNKNOWN", "file_name": "", "description": "Empty path"}

    fname = os.path.basename(file_path).lower()

    # 1. Reference Manual check (RMxxxx or reference-manual)
    rm_match = re.search(r'\b(rm[0-9]{4})\b', fname)
    if rm_match or "reference-manual" in fname or "reference_manual" in fname or "reference manual" in fname:
        doc_code = rm_match.group(1).upper() if rm_match else "RM"
        return {
            "doc_type": "REFERENCE_MANUAL",
            "is_reference_manual": True,
            "doc_code": doc_code,
            "file_name": os.path.basename(file_path),
            "description": f"Official Reference Manual ({doc_code}) containing peripheral registers and hardware architecture."
        }

    # 2. Errata Sheet check (ESxxxx or errata)
    es_match = re.search(r'\b(es[0-9]{4})\b', fname)
    if es_match or "errata" in fname or "device-errata" in fname:
        doc_code = es_match.group(1).upper() if es_match else "ES"
        return {
            "doc_type": "ERRATA_SHEET",
            "is_reference_manual": False,
            "doc_code": doc_code,
            "file_name": os.path.basename(file_path),
            "description": f"Silicon Errata Sheet ({doc_code}) describing known chip limitations and workarounds. Not a Reference Manual."
        }

    # 3. Programming Manual check (PMxxxx or programming-manual)
    pm_match = re.search(r'\b(pm[0-9]{4})\b', fname)
    if pm_match or "programming-manual" in fname or "programming_manual" in fname:
        doc_code = pm_match.group(1).upper() if pm_match else "PM"
        return {
            "doc_type": "PROGRAMMING_MANUAL",
            "is_reference_manual": False,
            "doc_code": doc_code,
            "file_name": os.path.basename(file_path),
            "description": f"Programming Manual ({doc_code}) detailing CPU core instruction set and NVIC registers. Not a Reference Manual."
        }

    # 4. Application Note check (ANxxxx or application-note)
    an_match = re.search(r'\b(an[0-9]{4})\b', fname)
    if an_match or "application-note" in fname or "application_note" in fname:
        doc_code = an_match.group(1).upper() if an_match else "AN"
        return {
            "doc_type": "APPLICATION_NOTE",
            "is_reference_manual": False,
            "doc_code": doc_code,
            "file_name": os.path.basename(file_path),
            "description": f"Application Note ({doc_code}). Not a Reference Manual."
        }

    # 5. Datasheet check (DSxxxx, ds_*, datasheet, or bare stm32part.pdf)
    ds_match = re.search(r'\b(ds[0-9]{3,6})\b', fname)
    if ds_match or fname.startswith("ds_") or "datasheet" in fname or re.match(r'^stm32[a-z0-9]+\.pdf$', fname):
        doc_code = ds_match.group(1).upper() if ds_match else "DS"
        return {
            "doc_type": "DATASHEET",
            "is_reference_manual": False,
            "doc_code": doc_code,
            "file_name": os.path.basename(file_path),
            "description": f"Device Datasheet ({doc_code}) containing pinout diagrams and electrical characteristics. Not a Reference Manual."
        }

    return {
        "doc_type": "UNKNOWN",
        "is_reference_manual": False,
        "doc_code": "UNKNOWN",
        "file_name": os.path.basename(file_path),
        "description": "Unrecognized document format. A Reference Manual (RMxxxx) is required."
    }


def find_reference_manual_in_directory(dir_path: str) -> Optional[str]:
    """Scans a directory for a legitimate ST Reference Manual PDF (rm*.pdf)."""
    if not os.path.isdir(dir_path):
        return None

    # Priority 1: Check rm*.pdf
    for f in sorted(os.listdir(dir_path)):
        if f.lower().endswith(".pdf"):
            full = os.path.join(dir_path, f)
            c = classify_st_document(full)
            if c["is_reference_manual"]:
                return full

    return None


def validate_reference_manual(file_path: str) -> Tuple[bool, str, Optional[str]]:
    """
    Validates whether the provided file path is an authentic Reference Manual.
    If a Datasheet or Errata sheet was selected but a Reference Manual exists in the same directory,
    returns (False, warning_message, resolved_rm_path).
    """
    if not file_path or not os.path.exists(file_path):
        return False, f"File does not exist: {file_path}", None

    if os.path.isdir(file_path):
        rm_in_dir = find_reference_manual_in_directory(file_path)
        if rm_in_dir:
            return True, f"Found Reference Manual in directory: {os.path.basename(rm_in_dir)}", rm_in_dir
        return False, f"Directory '{file_path}' does not contain any ST Reference Manual (RMxxxx PDF).", None

    classification = classify_st_document(file_path)
    if classification["is_reference_manual"]:
        return True, "Valid ST Reference Manual.", file_path

    # Check if a sibling RM exists in the same parent folder
    parent_dir = os.path.dirname(os.path.abspath(file_path))
    sibling_rm = find_reference_manual_in_directory(parent_dir)

    msg = f"Rejected: '{os.path.basename(file_path)}' is classified as an ST {classification['doc_type']} ({classification['description']}). Karpathy Wiki requires an official Reference Manual (RMxxxx) with complete peripheral register maps."
    return False, msg, sibling_rm

