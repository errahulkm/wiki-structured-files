# Reset and Clock Control (RCC)

## 1. Overview & Key Features
The Reset and Clock Control (RCC) block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 7](../chapters/chapter_07.md) (Pages 270 - 333).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SYSTEM
* **Reference Chapter**: [Chapter 7](../chapters/chapter_07.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Reset and Clock Control (RCC) Architectural Block Diagram](../figures/rcc_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Reset and Clock Control (RCC) Configuration & Parameter Matrix](../tables/rcc_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `RCC` | `0x00` | Offset Register 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0440 Rev 9 333/2140 RM0440 Reset and clock control (RCC) | [RCC.json](../registers_json/RCC.json) |
| `RCC_` | `0x80` | Reset and Clock Control (RCC) RCC_ Register | [RCC_.json](../registers_json/RCC_.json) |
| `RCC_AHB1ENR` | `0x48` | AHB1 periphera l clock enable register (RCC_AHB1ENR) | [RCC_AHB1ENR.json](../registers_json/RCC_AHB1ENR.json) |
| `RCC_AHB1RSTR` | `0x28` | AHB1 peripheral reset register (RCC_AHB1RSTR) | [RCC_AHB1RSTR.json](../registers_json/RCC_AHB1RSTR.json) |
| `RCC_AHB1SMENR` | `0x68` | AHB1 peripheral clocks enable in Sleep and Stop modes register (RCC_AHB1SMENR) | [RCC_AHB1SMENR.json](../registers_json/RCC_AHB1SMENR.json) |
| `RCC_AHB2ENR` | `0x4C` | AHB2 periphera l clock enable register (RCC_AHB2ENR) | [RCC_AHB2ENR.json](../registers_json/RCC_AHB2ENR.json) |
| `RCC_AHB2RSTR` | `0x2C` | AHB2 peripheral reset register (RCC_AHB2RSTR) | [RCC_AHB2RSTR.json](../registers_json/RCC_AHB2RSTR.json) |
| `RCC_AHB2SMENR` | `0x6C` | AHB2 peripheral clocks enable in Sleep and Stop modes register (RCC_AHB2SMENR) | [RCC_AHB2SMENR.json](../registers_json/RCC_AHB2SMENR.json) |
| `RCC_AHB3ENR` | `0x50` | AHB3 periphera l clock enable register (RCC_AHB3ENR) | [RCC_AHB3ENR.json](../registers_json/RCC_AHB3ENR.json) |
| `RCC_AHB3RSTR` | `0x30` | AHB3 peripheral rese t register (RCC_AHB3RSTR) | [RCC_AHB3RSTR.json](../registers_json/RCC_AHB3RSTR.json) |
| `RCC_AHB3SMENR` | `0x70` | AHB3 peripheral clocks enable in Sleep and Stop modes register (RCC_AHB3SMENR) | [RCC_AHB3SMENR.json](../registers_json/RCC_AHB3SMENR.json) |
| `RCC_AHBXENR` | `0x00` | Peripheral clock enable register (RCC_AHBXENR) | [RCC_AHBXENR.json](../registers_json/RCC_AHBXENR.json) |
| `RCC_APB1ENR1` | `0x00` | APB1 peripheral clock en able register 1 (RCC_APB1ENR1) | [RCC_APB1ENR1.json](../registers_json/RCC_APB1ENR1.json) |
| `RCC_APB1ENR2` | `0x5C` | APB1 peripheral clock en able register 2 (RCC_APB1ENR2) | [RCC_APB1ENR2.json](../registers_json/RCC_APB1ENR2.json) |
| `RCC_APB1RSTR1` | `0x38` | APB1 peripheral reset register 1 (RCC_APB1RSTR1) | [RCC_APB1RSTR1.json](../registers_json/RCC_APB1RSTR1.json) |
| `RCC_APB1RSTR2` | `0x3C` | APB1 peripheral reset register 2 (RCC_APB1RSTR2) | [RCC_APB1RSTR2.json](../registers_json/RCC_APB1RSTR2.json) |
| `RCC_APB1SMENR1` | `0x00` | APB1 peripheral clocks enable in Sleep and Stop modes register 1 (RCC_APB1SMENR1) | [RCC_APB1SMENR1.json](../registers_json/RCC_APB1SMENR1.json) |
| `RCC_APB1SMENR2` | `0x7C` | APB1 peripheral clocks enable in Sleep and Stop modes register 2 (RCC_APB1SMENR2) | [RCC_APB1SMENR2.json](../registers_json/RCC_APB1SMENR2.json) |
| `RCC_APB2ENR` | `0x00` | APB2 peripheral clock enable register (RCC_APB2ENR) | [RCC_APB2ENR.json](../registers_json/RCC_APB2ENR.json) |
| `RCC_APB2RSTR` | `0x40` | APB2 peripheral rese t register (RCC_APB2RSTR) | [RCC_APB2RSTR.json](../registers_json/RCC_APB2RSTR.json) |
| `RCC_APB2SMENR` | `0x00` | APB2 peripheral clocks enable in Sleep and Stop modes register (RCC_APB2SMENR) | [RCC_APB2SMENR.json](../registers_json/RCC_APB2SMENR.json) |
| `RCC_APBXENRY` | `0x00` | Peripheral clock enable register (RCC_APBXENRY) | [RCC_APBXENRY.json](../registers_json/RCC_APBXENRY.json) |
| `RCC_BDCR` | `0x90` | RTC domain contro l register (RCC_BDCR) | [RCC_BDCR.json](../registers_json/RCC_BDCR.json) |
| `RCC_CCIPR` | `0x88` | Peripherals independent clock configuration register (RCC_CCIPR) | [RCC_CCIPR.json](../registers_json/RCC_CCIPR.json) |
| `RCC_CCIPR2` | `0x9C` | Peripherals independent clock configuration register (RCC_CCIPR2) | [RCC_CCIPR2.json](../registers_json/RCC_CCIPR2.json) |
| `RCC_CFGR` | `0x08` | Clock configurati on register (RCC_CFGR) | [RCC_CFGR.json](../registers_json/RCC_CFGR.json) |
| `RCC_CICR` | `0x20` | Clock interrupt cl ear register (RCC_CICR) | [RCC_CICR.json](../registers_json/RCC_CICR.json) |
| `RCC_CIER` | `0x18` | Clock interrupt enable register (RCC_CIER) | [RCC_CIER.json](../registers_json/RCC_CIER.json) |
| `RCC_CIFR` | `0x1C` | Clock interrupt flag register (RCC_CIFR) | [RCC_CIFR.json](../registers_json/RCC_CIFR.json) |
| `RCC_CR` | `0x00` | Clock control register (RCC_CR) | [RCC_CR.json](../registers_json/RCC_CR.json) |
| `RCC_CRRCR` | `0x98` | Clock recovery RC register (RCC_CRRCR) | [RCC_CRRCR.json](../registers_json/RCC_CRRCR.json) |
| `RCC_CSR` | `0x94` | Control/status register (RCC_CSR) | [RCC_CSR.json](../registers_json/RCC_CSR.json) |
| `RCC_ICSCR` | `0x04` | Internal clock sources ca libration register (RCC_ICSCR) | [RCC_ICSCR.json](../registers_json/RCC_ICSCR.json) |
| `RCC_PLLCFGR` | `0x0C` | PLL configuration register (RCC_PLLCFGR) | [RCC_PLLCFGR.json](../registers_json/RCC_PLLCFGR.json) |