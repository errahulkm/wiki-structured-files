# Universal Multi-MCU Architectural DNA & Dynamic Graph Blueprint

This document defines the dynamic architectural DNA specification for the STMicroelectronics Karpathy-Wiki Generator. It supersedes static single-MCU blueprints by establishing dynamic runtime extraction across any ST microcontroller family.

---

## 1. Universal Architectural DNA Principles

1. **Silicon Truth Extracted from Source**:
   - The reference manual PDF provided by the user is the sole ground truth.
   - Chapter count, chapter titles, page ranges, and peripheral allocations are extracted dynamically at runtime.
   - Fixed lists of chapters (e.g. 65 chapters) and hardcoded peripheral catalogs (e.g. 43 IPs from RM0468) are prohibited.

2. **Heterogeneous Family DNA Profiles**:
   Each ST microcontroller family possesses a distinct hardware DNA:

| MCU Series | Typical Reference Manual | Core Architecture | Typical Chapters | Bus Interconnect | Peripheral Distinctions | Security Profile |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **STM32F1** | **RM0008** | **ARM Cortex-M3 (72 MHz)** | **32 Chapters** | AHB/APB Matrix | FSMC, bxCAN, USB FS, SDIO, ETH, TIM1-14 | No TrustZone, No CRYP/HASH |
| **STM32F4** | **RM0090** | **ARM Cortex-M4 (168-180 MHz)** | **38-42 Chapters** | Multi-Layer AHB Matrix | FMC, CAN, USB OTG, DCMI, RNG | Optional CRYP/HASH |
| **STM32H7** | **RM0468** | **ARM Cortex-M7 (480-550 MHz)** | **65 Chapters** | 64-bit AXI + Multi-AHB | SAI, LTDC, DCMI, DMA2D, OCTOSPI, FDCAN | High-Density CRYP, HASH, OTFDEC |
| **STM32U3/U5**| **RM0487/RM0456** | **ARM Cortex-M33 (ARMv8-M)** | **55-60 Chapters** | Low-Power AXI/AHB | LPBAM, MDF, ADF, OCTOSPI, USB Type-C | Full ARM TrustZone, GTZC, SAU |

---

## 2. Dynamic Topographic Layers in Knowledge Graph

The Knowledge Graph topology dynamically adjusts its layers based on the detected `MCUDNA`:

1. **Master Index Layer (`Master Index`)**: Entry MOC (`index.md`) dashboard.
2. **Memory Layer (`Memory`)**: Master system memory map (`memory/memory_map.md`) defining the physical bus attachment for this specific chip.
3. **System Infrastructure Layer (`System`)**: Only the active system controllers (e.g. `RCC`, `PWR`, `BKP` for F1; `RCC`, `PWR`, `SYSCFG`, `GTZC` for H7/U3).
4. **Dynamic CPU Core Layer (`Core`)**: Labeled dynamically with the real silicon core (e.g., `Cortex-M3 Core`, `Cortex-M4 Core`, `Cortex-M7 Core`, `Cortex-M33 Core`).
5. **Peripherals Layer (`Peripherals`)**: Only contains hardware IPs that physically exist in the active reference manual.
6. **Security Architecture Layer (`Security`)**: Included **ONLY** if the MCU features hardware security (e.g., TrustZone, CRYP, HASH, RNG, OTFDEC). Hidden/omitted for standard microcontrollers like STM32F1.
7. **Hardware Register Layer (`Registers`)**: Isolated 32-bit register JSON schemas parsed directly from the active manual.

---

## 3. Dynamic Chapter-Driven Ingestion Protocol

1. **Outline & TOC Extraction**:
   - `extract_mcu_dna(pdf_path)` scans PDF outlines and Table of Contents to discover:
     - Exact chapter index $1..N$
     - Chapter titles and physical page numbers $[start\_page, end\_page]$
     - Category classification (`memory`, `system`, `core`, `peripherals`, `security`, `chapters`)
2. **Deterministic Virtual Directory Generation**:
   - Exactly $N$ chapter markdown files are created under `/chapters/` (`chapter_01.md` ... `chapter_N.md`).
   - Chapter raw text is extracted from the active reference manual PDF across the exact page boundaries.
   - Corresponding IP module pages are generated only for discovered active IPs.
3. **Register Map Isolation**:
   - Hardware register JSONs are extracted dynamically from the manual text.
   - Pre-populated static register dictionaries from other chip families are strictly forbidden.
