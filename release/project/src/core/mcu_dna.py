"""
Dynamic MCU Architectural DNA & Table-of-Contents (TOC) Extraction Engine.
Extracts hardware core architecture, runtime chapter boundaries, peripheral inventory,
and system topology directly from any STMicroelectronics Reference Manual PDF.
"""

import os
import re
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Any, Optional, Tuple, Set


@dataclass
class ChapterInfo:
    chapter_num: int
    title: str
    clean_title: str
    start_page: int
    end_page: int
    category: str  # memory, system, core, peripherals, security, chapters
    ip_key: str
    ip_name: str
    rel_path: str


@dataclass
class MCUDNA:
    mcu_family: str
    target_device: str
    rm_number: str
    core_architecture: str
    core_layer_label: str
    total_pages: int
    has_security: bool
    chapters: List[Dict[str, Any]] = field(default_factory=list)
    active_ips: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    topology_layers: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def classify_chapter_title(title: str) -> Tuple[str, str, str, str]:
    """
    Classifies chapter title into (category, ip_key, rel_path, ip_name).
    Categories: memory, system, core, peripherals, security, chapters.
    """
    t = title.lower()
    clean_title = re.sub(r'^\d+[\.\s]+', '', title).strip()

    # 1. Specialized Communication Protocols & High-Priority IPs
    if any(k in t for k in ['ethernet', 'eth']):
        return 'peripherals', 'eth', 'peripherals/eth.md', 'Ethernet MAC (ETH)'
    elif any(k in t for k in ['timer', 'tim1', 'tim2', 'tim3', 'tim4', 'tim5', 'tim6', 'tim7', 'tim8', 'tim9', 'tim10', 'tim11', 'tim12', 'tim13', 'tim14', 'timx', 'lptim', 'hrtim']):
        return 'peripherals', 'timers', 'peripherals/timers.md', 'Timers (TIM)'
    elif any(k in t for k in ['gpio', 'afio', 'alternate-function']) or ('i/o' in t and 'port' in t):
        return 'peripherals', 'gpio', 'peripherals/gpio.md', 'General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs)'
    elif any(k in t for k in ['memory and bus', 'memory organization', 'memory map', 'system and memory', 'memory overview', 'memory mapping', 'memory architecture', 'bus matrix']):
        return 'memory', 'memory_map', 'memory/memory_map.md', 'Master System Memory Map'
    elif 'flash' in t:
        return 'memory', 'flash', 'memory/flash.md', 'Embedded Flash Memory'
    elif 'fsmc' in t:
        return 'peripherals', 'fsmc', 'peripherals/fsmc.md', 'Flexible Static Memory Controller (FSMC)'
    elif 'fmc' in t:
        return 'peripherals', 'fmc', 'peripherals/fmc.md', 'Flexible Memory Controller (FMC)'
    elif any(k in t for k in ['power control', 'pwr']):
        return 'system', 'pwr', 'system/pwr.md', 'Power Control (PWR)'
    elif any(k in t for k in ['backup register', 'bkp']):
        return 'system', 'bkp', 'system/bkp.md', 'Backup Registers (BKP)'
    elif any(k in t for k in ['reset and clock', 'rcc']):
        return 'system', 'rcc', 'system/rcc.md', 'Reset and Clock Control (RCC)'
    elif any(k in t for k in ['system config', 'syscfg']):
        return 'system', 'syscfg', 'system/syscfg.md', 'System Configuration (SYSCFG)'
    elif any(k in t for k in ['nested vectored interrupt', 'interrupts and events', 'exti', 'nvic']):
        return 'core', 'interrupts', 'core/interrupts.md', 'Interrupts and Events (NVIC/EXTI)'
    elif any(k in t for k in ['analog-to-digital', 'adc']):
        return 'peripherals', 'adc', 'peripherals/adc.md', 'Analog-to-Digital Converter (ADC)'
    elif any(k in t for k in ['digital-to-analog', 'dac']):
        return 'peripherals', 'dac', 'peripherals/dac.md', 'Digital-to-Analog Converter (DAC)'
    elif any(k in t for k in ['direct memory access', 'dma', 'dmamux', 'bdma', 'mdma']):
        return 'peripherals', 'dma', 'peripherals/dma.md', 'Direct Memory Access Controller (DMA)'
    elif any(k in t for k in ['real-time clock', 'rtc']):
        return 'peripherals', 'rtc', 'peripherals/rtc.md', 'Real-Time Clock (RTC)'
    elif 'iwdg' in t or 'independent watchdog' in t:
        return 'peripherals', 'iwdg', 'peripherals/iwdg.md', 'Independent Watchdog (IWDG)'
    elif 'wwdg' in t or 'window watchdog' in t:
        return 'peripherals', 'wwdg', 'peripherals/wwdg.md', 'Window Watchdog (WWDG)'
    elif 'sdio' in t:
        return 'peripherals', 'sdio', 'peripherals/sdio.md', 'Secure Digital Input/Output (SDIO)'
    elif 'sdmmc' in t:
        return 'peripherals', 'sdmmc', 'peripherals/sdmmc.md', 'SDMMC Interface'
    elif 'otg_fs' in t:
        return 'peripherals', 'otg_fs', 'peripherals/otg_fs.md', 'USB On-The-Go Full-Speed (OTG_FS)'
    elif 'otg_hs' in t:
        return 'peripherals', 'otg_hs', 'peripherals/otg_hs.md', 'USB On-The-Go High-Speed (OTG_HS)'
    elif 'universal serial bus' in t or 'usb' in t:
        return 'peripherals', 'usb', 'peripherals/usb.md', 'Universal Serial Bus (USB)'
    elif 'bxcan' in t:
        return 'peripherals', 'can', 'peripherals/can.md', 'Controller Area Network (bxCAN)'
    elif 'fdcan' in t:
        return 'peripherals', 'fdcan', 'peripherals/fdcan.md', 'FDCAN Interface'
    elif 'can' in t:
        return 'peripherals', 'can', 'peripherals/can.md', 'Controller Area Network (CAN)'
    elif 'spi' in t or 'serial peripheral' in t:
        return 'peripherals', 'spi', 'peripherals/spi.md', 'Serial Peripheral Interface (SPI)'
    elif 'i2c' in t or 'inter-integrated' in t:
        return 'peripherals', 'i2c', 'peripherals/i2c.md', 'Inter-Integrated Circuit (I2C)'
    elif 'usart' in t or 'uart' in t:
        return 'peripherals', 'usart', 'peripherals/usart.md', 'Universal Synchronous Asynchronous Receiver Transmitter (USART)'
    elif 'crc' in t:
        return 'peripherals', 'crc', 'peripherals/crc.md', 'CRC Calculation Unit'
    elif 'debug' in t or 'dbg' in t:
        return 'core', 'debug', 'core/debug.md', 'Debug Support (DBG)'
    # Security Features
    elif any(k in t for k in ['cryp', 'crypt']):
        return 'security', 'cryp', 'security/cryp.md', 'Cryptographic Processor (CRYP)'
    elif 'hash' in t:
        return 'security', 'hash', 'security/hash.md', 'Hash Processor (HASH)'
    elif 'rng' in t:
        return 'security', 'rng', 'security/rng.md', 'Random Number Generator (RNG)'
    elif 'otfdec' in t:
        return 'security', 'otfdec', 'security/otfdec.md', 'On-The-Fly Decryption (OTFDEC)'
    elif 'trustzone' in t or 'tzsc' in t or 'gtzc' in t:
        return 'security', 'trustzone', 'security/trustzone.md', 'Global TrustZone Security Controller'
    # Media & Specialized Audio/Video
    elif 'octospi' in t or 'ospi' in t:
        return 'peripherals', 'octospi', 'peripherals/octospi.md', 'Octo-SPI Interface (OCTOSPI)'
    elif 'sai' in t or 'serial audio' in t:
        return 'peripherals', 'sai', 'peripherals/sai.md', 'Serial Audio Interface (SAI)'
    elif 'spdif' in t:
        return 'peripherals', 'spdifrx', 'peripherals/spdifrx.md', 'SPDIF Receiver (SPDIFRX)'
    elif 'ltdc' in t or 'lcd-tft' in t:
        return 'peripherals', 'ltdc', 'peripherals/ltdc.md', 'LCD-TFT Display Controller (LTDC)'
    elif 'dma2d' in t or 'chrom-art' in t:
        return 'peripherals', 'dma2d', 'peripherals/dma2d.md', 'Chrom-ART Accelerator (DMA2D)'
    elif 'dcmi' in t or 'camera' in t:
        return 'peripherals', 'dcmi', 'peripherals/dcmi.md', 'Digital Camera Interface (DCMI)'
    elif 'opamp' in t:
        return 'peripherals', 'opamp', 'peripherals/opamp.md', 'Operational Amplifier (OPAMP)'
    elif 'comp' in t or 'comparator' in t:
        return 'peripherals', 'comp', 'peripherals/comp.md', 'Comparator (COMP)'
    else:
        # General documentation, introduction, revision history
        return 'chapters', f'chapter_{t[:10]}', 'chapters/chapter.md', clean_title


def extract_mcu_dna(pdf_path: str, wiki_root: Optional[str] = None) -> MCUDNA:
    """
    Inspects any reference manual PDF at runtime and extracts its dynamic architectural DNA,
    including exact chapter count, page boundaries, peripheral taxonomy, and CPU core.
    """
    import pypdf
    try:
        from .mcu_detector import detect_mcu_metadata
    except ImportError:
        from src.core.mcu_detector import detect_mcu_metadata

    pdf_path = os.path.abspath(pdf_path)
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Reference manual PDF not found at: {pdf_path}")

    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)

    # Base metadata
    meta = detect_mcu_metadata(source_hint=pdf_path, wiki_root=wiki_root)
    mcu_family = meta["mcu_family"]
    target_device = meta["target_device"]
    rm_number = meta["rm_number"]

    # 1. Detect CPU Core Architecture dynamically
    core_architecture = "ARM 32-bit Cortex"
    first_pages_text = ""
    for p_idx in range(min(15, total_pages)):
        first_pages_text += (reader.pages[p_idx].extract_text() or "") + "\n"

    core_match = re.search(r'Cortex[\s®\*\™\-]*M\s*([0-9]+(?:\+)?|33|55|85)', first_pages_text, re.IGNORECASE)
    if core_match:
        c_num = core_match.group(1).upper()
        if c_num == "33":
            core_architecture = "ARM 32-bit Cortex-M33"
            core_layer_label = "Cortex-M33 Core"
        elif c_num == "4":
            core_architecture = "ARM 32-bit Cortex-M4"
            core_layer_label = "Cortex-M4 Core"
        elif c_num == "7":
            core_architecture = "ARM 32-bit Cortex-M7"
            core_layer_label = "Cortex-M7 Core"
        elif c_num == "3":
            core_architecture = "ARM 32-bit Cortex-M3"
            core_layer_label = "Cortex-M3 Core"
        elif c_num in ["0", "0+"]:
            core_architecture = "ARM 32-bit Cortex-M0/M0+"
            core_layer_label = "Cortex-M0 Core"
        elif c_num == "55":
            core_architecture = "ARM 32-bit Cortex-M55"
            core_layer_label = "Cortex-M55 Core"
        elif c_num == "85":
            core_architecture = "ARM 32-bit Cortex-M85"
            core_layer_label = "Cortex-M85 Core"
        else:
            core_architecture = f"ARM Cortex-M{c_num}"
            core_layer_label = f"Cortex-M{c_num} Core"
    else:
        # Fallback based on MCU family
        if "F1" in mcu_family or "L1" in mcu_family:
            core_architecture = "ARM 32-bit Cortex-M3"
            core_layer_label = "Cortex-M3 Core"
        elif "H7" in mcu_family or "F7" in mcu_family:
            core_architecture = "ARM 32-bit Cortex-M7"
            core_layer_label = "Cortex-M7 Core"
        elif "U3" in mcu_family or "U5" in mcu_family or "H5" in mcu_family:
            core_architecture = "ARM 32-bit Cortex-M33"
            core_layer_label = "Cortex-M33 Core"
        elif "F4" in mcu_family or "G4" in mcu_family or "L4" in mcu_family:
            core_architecture = "ARM 32-bit Cortex-M4"
            core_layer_label = "Cortex-M4 Core"
        else:
            core_architecture = "ARM 32-bit Cortex Processor"
            core_layer_label = "Cortex Core"

    # Fast O(1) page mapping
    page_map = {}
    for i, page in enumerate(reader.pages):
        if hasattr(page, 'indirect_reference') and page.indirect_reference:
            page_map[page.indirect_reference.idnum] = i + 1

    # 2. Extract Chapters from PDF Outlines
    outline_items = []
    if reader.outline:
        for item in reader.outline:
            if not isinstance(item, list):
                outline_items.append(item)

    raw_chapters = []
    if outline_items:
        for i, item in enumerate(outline_items):
            title = getattr(item, 'title', str(item)).strip()
            p_start = None
            if hasattr(item, 'page') and hasattr(item.page, 'idnum'):
                p_start = page_map.get(item.page.idnum)
            if p_start is None:
                try:
                    p_start = reader.get_destination_page_number(item) + 1
                except Exception:
                    p_start = 1

            p_end = total_pages + 1
            if i + 1 < len(outline_items):
                next_item = outline_items[i + 1]
                if hasattr(next_item, 'page') and hasattr(next_item.page, 'idnum'):
                    next_p = page_map.get(next_item.page.idnum)
                    if next_p:
                        p_end = next_p
                if p_end == total_pages + 1:
                    try:
                        p_end = reader.get_destination_page_number(next_item) + 1
                    except Exception:
                        pass
            
            p_end = max(p_start + 1, min(p_end, total_pages + 1))
            raw_chapters.append({
                "index": i + 1,
                "title": title,
                "start_page": p_start,
                "end_page": p_end
            })
    else:
        # Fallback: scan table of contents in first 35 pages
        toc_lines = [l.strip() for l in first_pages_text.split('\n') if l.strip()]
        toc_pattern = re.compile(r'^(?:Chapter\s+)?(\d+)\s+([A-Za-z0-9_\-\s\(\)\/,\.]+?)\s*\.{2,}\s*(\d+)$')
        found_toc = []
        for line in toc_lines:
            m = toc_pattern.match(line)
            if m:
                c_num = int(m.group(1))
                c_title = m.group(2).strip()
                c_page = int(m.group(3))
                found_toc.append((c_num, c_title, c_page))
        
        if found_toc:
            for i, (c_num, c_title, c_page) in enumerate(found_toc):
                next_page = found_toc[i + 1][2] if i + 1 < len(found_toc) else (total_pages + 1)
                raw_chapters.append({
                    "index": c_num,
                    "title": f"{c_num} {c_title}",
                    "start_page": c_page,
                    "end_page": next_page
                })
        else:
            # Emergency single-chapter fallback
            raw_chapters.append({
                "index": 1,
                "title": f"1 {target_device} Complete Architecture",
                "start_page": 1,
                "end_page": total_pages + 1
            })

    # 3. Classify and map chapters to Structured Wiki architecture
    processed_chapters: List[Dict[str, Any]] = []
    active_ips: Dict[str, Dict[str, Any]] = {}
    has_security = False

    for c in raw_chapters:
        c_num = c["index"]
        c_title = c["title"]
        start_p = c["start_page"]
        end_p = c["end_page"]

        cat, ip_key, rel_path, ip_name = classify_chapter_title(c_title)
        clean_title = re.sub(r'^\d+[\.\s]+', '', c_title).strip()
        if cat == 'chapters':
            rel_path = f"chapters/chapter_{c_num:02d}.md"

        chap_dict = {
            "chapter_num": c_num,
            "chapter_id": f"chapter_{c_num:02d}",
            "file": f"chapter_{c_num:02d}.md",
            "title": f"Chapter {c_num}: {clean_title}",
            "raw_title": c_title,
            "clean_title": clean_title,
            "start_page": start_p,
            "end_page": end_p,
            "category": cat,
            "ip_key": ip_key,
            "ip_name": ip_name,
            "rel_path": rel_path
        }
        processed_chapters.append(chap_dict)

        if cat == "security":
            has_security = True

        if cat in ["memory", "system", "core", "peripherals", "security"]:
            if ip_key not in active_ips:
                active_ips[ip_key] = {
                    "key": ip_key,
                    "rel_path": rel_path,
                    "name": ip_name,
                    "category": cat,
                    "chapter_refs": [c_num],
                    "clean_title": clean_title,
                    "start_page": start_p,
                    "end_page": end_p
                }
            else:
                active_ips[ip_key]["chapter_refs"].append(c_num)

    # Guarantee Master System Memory Map exists as an active IP block
    if "memory_map" not in active_ips:
        mem_chap = 2 if len(processed_chapters) >= 2 else 1
        for c in processed_chapters:
            if "memory" in c["clean_title"].lower():
                mem_chap = c["chapter_num"]
                break
        active_ips["memory_map"] = {
            "key": "memory_map",
            "rel_path": "memory/memory_map.md",
            "name": "Master System Memory Map",
            "category": "memory",
            "chapter_refs": [mem_chap],
            "clean_title": "Master System Memory Map",
            "start_page": 1,
            "end_page": 30
        }

    # 4. Define dynamic topology layers based on what actually exists
    topology_layers = [
        "Master Index",
        "Memory Layer",
        "System Infrastructure",
        core_layer_label,
        "Peripherals"
    ]
    if has_security:
        topology_layers.append("Security Architecture")
    topology_layers.append("Hardware Registers")

    return MCUDNA(
        mcu_family=mcu_family,
        target_device=target_device,
        rm_number=rm_number,
        core_architecture=core_architecture,
        core_layer_label=core_layer_label,
        total_pages=total_pages,
        has_security=has_security,
        chapters=processed_chapters,
        active_ips=active_ips,
        topology_layers=topology_layers
    )
