# Embedded Flash Memory

## 1. Overview & Key Features
The Embedded Flash Memory block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 6](../chapters/chapter_06.md) (Pages 174 - 241).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: MEMORY
* **Reference Chapter**: [Chapter 6](../chapters/chapter_06.md)
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
| `FLASH` | `0x00` | Offset Register 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0438 Rev 8 241/2187 RM0438 Embedded flash memory (FLASH) | [FLASH.json](../registers_json/FLASH.json) |
| `FLASH_` | `0xC4` | Embedded Flash Memory FLASH_ Register | [FLASH_.json](../registers_json/FLASH_.json) |
| `FLASH_ACR` | `0x00` | Flash access control register (FLASH_ACR) | [FLASH_ACR.json](../registers_json/FLASH_ACR.json) |
| `FLASH_ECCR` | `0x30` | Embedded Flash Memory FLASH_ECCR Register | [FLASH_ECCR.json](../registers_json/FLASH_ECCR.json) |
| `FLASH_LVEKEYR` | `0x14` | Flash low voltage key register (FLASH_LVEKEYR) | [FLASH_LVEKEYR.json](../registers_json/FLASH_LVEKEYR.json) |
| `FLASH_NSBOOTA` | `0x44` | Embedded Flash Memory FLASH_NSBOOTA Register | [FLASH_NSBOOTA.json](../registers_json/FLASH_NSBOOTA.json) |
| `FLASH_NSBOOTADD0R` | `0x00` | Flash non-secure boot address 0 register (FLASH_NSBOOTADD0R) | [FLASH_NSBOOTADD0R.json](../registers_json/FLASH_NSBOOTADD0R.json) |
| `FLASH_NSBOOTADD1R` | `0x00` | Flash non-secure boot address 1 register (FLASH_NSBOOTADD1R) | [FLASH_NSBOOTADD1R.json](../registers_json/FLASH_NSBOOTADD1R.json) |
| `FLASH_NSCR` | `0x28` | Flash non-secure cont rol register (FLASH_NSCR) | [FLASH_NSCR.json](../registers_json/FLASH_NSCR.json) |
| `FLASH_NSKEYR` | `0x08` | Flash non-secure k ey register (FLASH_NSKEYR) | [FLASH_NSKEYR.json](../registers_json/FLASH_NSKEYR.json) |
| `FLASH_NSSR` | `0x20` | Embedded Flash Memory FLASH_NSSR Register | [FLASH_NSSR.json](../registers_json/FLASH_NSSR.json) |
| `FLASH_OPTKEYR` | `0x10` | Flash option key regi ster (FLASH_OPTKEYR) | [FLASH_OPTKEYR.json](../registers_json/FLASH_OPTKEYR.json) |
| `FLASH_OPTR` | `0x40` | Embedded Flash Memory FLASH_OPTR Register | [FLASH_OPTR.json](../registers_json/FLASH_OPTR.json) |
| `FLASH_PDKEYR` | `0x04` | Flash power-down key register (FLASH_PDKEYR) | [FLASH_PDKEYR.json](../registers_json/FLASH_PDKEYR.json) |
| `FLASH_PRIVCFGR` | `0x00` | FLASH privilege configur ation register (FLASH_PRIVCFGR) | [FLASH_PRIVCFGR.json](../registers_json/FLASH_PRIVCFGR.json) |
| `FLASH_SECBB1RX` | `0x00` | FLASH secure block based ba nk 1 register (FLASH_SECBB1RX) | [FLASH_SECBB1RX.json](../registers_json/FLASH_SECBB1RX.json) |
| `FLASH_SECBB2RX` | `0x00` | FLASH secure block based ba nk 2 register (FLASH_SECBB2RX) | [FLASH_SECBB2RX.json](../registers_json/FLASH_SECBB2RX.json) |
| `FLASH_SECBOOT` | `0x4C` | Embedded Flash Memory FLASH_SECBOOT Register | [FLASH_SECBOOT.json](../registers_json/FLASH_SECBOOT.json) |
| `FLASH_SECBOOTADD0R` | `0x00` | Flash secure boot address 0 register (FLASH_SECBOOTADD0R) | [FLASH_SECBOOTADD0R.json](../registers_json/FLASH_SECBOOTADD0R.json) |
| `FLASH_SECCR` | `0x2C` | Flash secure contro l register (FLASH_SECCR) | [FLASH_SECCR.json](../registers_json/FLASH_SECCR.json) |
| `FLASH_SECHDPCR` | `0x00` | FLASH secure HDP contro l register (FLASH_SECHDPCR) | [FLASH_SECHDPCR.json](../registers_json/FLASH_SECHDPCR.json) |
| `FLASH_SECKEYR` | `0x0C` | Embedded Flash Memory FLASH_SECKEYR Register | [FLASH_SECKEYR.json](../registers_json/FLASH_SECKEYR.json) |
| `FLASH_SECSR` | `0x24` | Embedded Flash Memory FLASH_SECSR Register | [FLASH_SECSR.json](../registers_json/FLASH_SECSR.json) |
| `FLASH_SECWM1R1` | `0x00` | Flash bank 1 secure wate rmak1 register (FLASH_SECWM1R1) | [FLASH_SECWM1R1.json](../registers_json/FLASH_SECWM1R1.json) |
| `FLASH_SECWM1R2` | `0x00` | Flash secure watermak 1 register 2 (FLASH_SECWM1R2) | [FLASH_SECWM1R2.json](../registers_json/FLASH_SECWM1R2.json) |
| `FLASH_SECWM2R1` | `0x00` | Flash secure watermak 2 register (FLASH_SECWM2R1) | [FLASH_SECWM2R1.json](../registers_json/FLASH_SECWM2R1.json) |
| `FLASH_SECWM2R2` | `0x00` | Flash secure watermak 2 register 2 (FLASH_SECWM2R2) | [FLASH_SECWM2R2.json](../registers_json/FLASH_SECWM2R2.json) |
| `FLASH_WRP1AR` | `0x58` | Flash WPR1 area A a ddress register (FLASH_WRP1AR) | [FLASH_WRP1AR.json](../registers_json/FLASH_WRP1AR.json) |
| `FLASH_WRP1BR` | `0x5C` | Flash WPR1 area B ad dress register (FLASH_WRP1BR) | [FLASH_WRP1BR.json](../registers_json/FLASH_WRP1BR.json) |
| `FLASH_WRP2AR` | `0x68` | Flash WPR2 area A a ddress register (FLASH_WRP2AR) | [FLASH_WRP2AR.json](../registers_json/FLASH_WRP2AR.json) |
| `FLASH_WRP2BR` | `0x6C` | Flash WPR2 area B ad dress register (FLASH_WRP2BR) | [FLASH_WRP2BR.json](../registers_json/FLASH_WRP2BR.json) |