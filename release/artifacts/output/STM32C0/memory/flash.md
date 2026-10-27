# Embedded Flash Memory

## 1. Overview & Key Features
The Embedded Flash Memory block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 4](../chapters/chapter_04.md) (Pages 56 - 91).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: MEMORY
* **Reference Chapter**: [Chapter 4](../chapters/chapter_04.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Embedded Flash Memory Architectural Block Diagram](../figures/flash_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Embedded Flash Memory Configuration & Parameter Matrix](../tables/flash_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `FLASH_ACR` | `0x000` | FLASH access control register (FLASH_ACR) | [FLASH_ACR.json](../registers_json/FLASH_ACR.json) |
| `FLASH_CR` | `0x014` | FLASH control register (FLASH_CR) | [FLASH_CR.json](../registers_json/FLASH_CR.json) |
| `FLASH_KEYR` | `0x008` | FLASH key regi ster (FLASH_KEYR) | [FLASH_KEYR.json](../registers_json/FLASH_KEYR.json) |
| `FLASH_OPT` | `0x00C` | Embedded Flash Memory FLASH_OPT Register | [FLASH_OPT.json](../registers_json/FLASH_OPT.json) |
| `FLASH_OPTKEYR` | `0x00C` | FLASH option key regi ster (FLASH_OPTKEYR) | [FLASH_OPTKEYR.json](../registers_json/FLASH_OPTKEYR.json) |
| `FLASH_OPTR` | `0x020` | FLASH option register (FLASH_OPTR) | [FLASH_OPTR.json](../registers_json/FLASH_OPTR.json) |
| `FLASH_PCROP1AER` | `0x028` | FLASH PCROP area A end address register (FLASH_PCROP1AER) | [FLASH_PCROP1AER.json](../registers_json/FLASH_PCROP1AER.json) |
| `FLASH_PCROP1ASR` | `0x024` | FLASH PCROP area A start address register (FLASH_PCROP1ASR) | [FLASH_PCROP1ASR.json](../registers_json/FLASH_PCROP1ASR.json) |
| `FLASH_PCROP1BER` | `0x038` | FLASH PCROP area B end address register (FLASH_PCROP1BER) | [FLASH_PCROP1BER.json](../registers_json/FLASH_PCROP1BER.json) |
| `FLASH_PCROP1BSR` | `0x034` | FLASH PCROP area B start address register (FLASH_PCROP1BSR) | [FLASH_PCROP1BSR.json](../registers_json/FLASH_PCROP1BSR.json) |
| `FLASH_SECR` | `0x080` | FLASH security register (FLASH_SECR) | [FLASH_SECR.json](../registers_json/FLASH_SECR.json) |
| `FLASH_SR` | `0x010` | access This register must not be modified when CFGBSY in FLASH status register (FLASH_SR) | [FLASH_SR.json](../registers_json/FLASH_SR.json) |
| `FLASH_WRP1AR` | `0x02C` | FLASH WRP area A address register (FLASH_WRP1AR) | [FLASH_WRP1AR.json](../registers_json/FLASH_WRP1AR.json) |
| `FLASH_WRP1BR` | `0x030` | FLASH WRP area B addr ess register (FLASH_WRP1BR) | [FLASH_WRP1BR.json](../registers_json/FLASH_WRP1BR.json) |