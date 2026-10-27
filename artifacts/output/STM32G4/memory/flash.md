# Embedded Flash Memory

## 1. Overview & Key Features
The Embedded Flash Memory block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 3](../chapters/chapter_03.md), [Chapter 4](../chapters/chapter_04.md), [Chapter 5](../chapters/chapter_05.md) (Pages 94 - 148).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: MEMORY
* **Reference Chapter**: [Chapter 3](../chapters/chapter_03.md), [Chapter 4](../chapters/chapter_04.md), [Chapter 5](../chapters/chapter_05.md)
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
| `FLASH_` | `0x70` | Embedded Flash Memory FLASH_ Register | [FLASH_.json](../registers_json/FLASH_.json) |
| `FLASH_ACR` | `0x00` | Flash access control register (FLASH_ACR) | [FLASH_ACR.json](../registers_json/FLASH_ACR.json) |
| `FLASH_CR` | `0x14` | Flash control register (FLASH_CR) | [FLASH_CR.json](../registers_json/FLASH_CR.json) |
| `FLASH_ECCR` | `0x18` | Flash ECC regi ster (FLASH_ECCR) | [FLASH_ECCR.json](../registers_json/FLASH_ECCR.json) |
| `FLASH_KEYR` | `0x08` | Flash key register (FLASH_KEYR) | [FLASH_KEYR.json](../registers_json/FLASH_KEYR.json) |
| `FLASH_OPT` | `0x0C` | Embedded Flash Memory FLASH_OPT Register | [FLASH_OPT.json](../registers_json/FLASH_OPT.json) |
| `FLASH_OPTKEYR` | `0x0C` | Flash option key regi ster (FLASH_OPTKEYR) | [FLASH_OPTKEYR.json](../registers_json/FLASH_OPTKEYR.json) |
| `FLASH_OPTR` | `0x20` | Embedded Flash Memory FLASH_OPTR Register | [FLASH_OPTR.json](../registers_json/FLASH_OPTR.json) |
| `FLASH_PCROP1ER` | `0x28` | Flash PCROP1 End addr ess register (FLASH_PCROP1ER) | [FLASH_PCROP1ER.json](../registers_json/FLASH_PCROP1ER.json) |
| `FLASH_PCROP1SR` | `0x24` | Flash PCROP1 Start addr ess register (FLASH_PCROP1SR) | [FLASH_PCROP1SR.json](../registers_json/FLASH_PCROP1SR.json) |
| `FLASH_PCROP2ER` | `0x48` | Flash PCROP2 End addr ess register (FLASH_PCROP2ER) | [FLASH_PCROP2ER.json](../registers_json/FLASH_PCROP2ER.json) |
| `FLASH_PCROP2SR` | `0x44` | Flash PCROP2 Start address register (FLASH_PCROP2SR) | [FLASH_PCROP2SR.json](../registers_json/FLASH_PCROP2SR.json) |
| `FLASH_PDKEYR` | `0x04` | Flash Power-down key register (FLASH_PDKEYR) | [FLASH_PDKEYR.json](../registers_json/FLASH_PDKEYR.json) |
| `FLASH_SEC1R` | `0x70` | Flash securable area register (FLASH_SEC1R) | [FLASH_SEC1R.json](../registers_json/FLASH_SEC1R.json) |
| `FLASH_SEC2R` | `0x74` | Flash securable area bank2 register (FLASH_SEC2R) | [FLASH_SEC2R.json](../registers_json/FLASH_SEC2R.json) |
| `FLASH_SR` | `0x10` | Flash status register (FLASH_SR) | [FLASH_SR.json](../registers_json/FLASH_SR.json) |
| `FLASH_WRP1AR` | `0x2C` | Flash WRP area A addr ess register (FLASH_WRP1AR) | [FLASH_WRP1AR.json](../registers_json/FLASH_WRP1AR.json) |
| `FLASH_WRP1BR` | `0x30` | Flash WRP area B addr ess register (FLASH_WRP1BR) | [FLASH_WRP1BR.json](../registers_json/FLASH_WRP1BR.json) |
| `FLASH_WRP2AR` | `0x4C` | Flash Bank 2 WRP area A address register (FLASH_WRP2AR) | [FLASH_WRP2AR.json](../registers_json/FLASH_WRP2AR.json) |
| `FLASH_WRP2BR` | `0x50` | Flash Bank 2 WRP area B address register (FLASH_WRP2BR) | [FLASH_WRP2BR.json](../registers_json/FLASH_WRP2BR.json) |