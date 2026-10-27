# Reset and Clock Control (RCC)

## 1. Overview & Key Features
The Reset and Clock Control (RCC) block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 6](../chapters/chapter_06.md) (Pages 118 - 165).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SYSTEM
* **Reference Chapter**: [Chapter 6](../chapters/chapter_06.md)
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
| `RCC_AHBENR` | `0x38` | RCC AHB peripheral cloc k enable register (RCC_AHBENR) | [RCC_AHBENR.json](../registers_json/RCC_AHBENR.json) |
| `RCC_AHBRSTR` | `0x28` | RCC AHB peripheral re set register (RCC_AHBRSTR) | [RCC_AHBRSTR.json](../registers_json/RCC_AHBRSTR.json) |
| `RCC_AHBSMENR` | `0x48` | RCC AHB periphera l clock enable in Sleep/Stop mode register (RCC_AHBSMENR) | [RCC_AHBSMENR.json](../registers_json/RCC_AHBSMENR.json) |
| `RCC_APBENR1` | `0x3C` | RCC APB periphe ral clock enable register 1 (RCC_APBENR1) | [RCC_APBENR1.json](../registers_json/RCC_APBENR1.json) |
| `RCC_APBENR2` | `0x40` | RCC APB periphe ral clock enable register 2 (RCC_APBENR2) | [RCC_APBENR2.json](../registers_json/RCC_APBENR2.json) |
| `RCC_APBRSTR1` | `0x2C` | RCC APB peripheral rese t register 1 (RCC_APBRSTR1) | [RCC_APBRSTR1.json](../registers_json/RCC_APBRSTR1.json) |
| `RCC_APBRSTR2` | `0x30` | RCC APB peripheral rese t register 2 (RCC_APBRSTR2) | [RCC_APBRSTR2.json](../registers_json/RCC_APBRSTR2.json) |
| `RCC_APBSMENR1` | `0x4C` | RCC APB periphera l clock enable in Sleep/Stop mode register 1 (RCC_APBSMENR1) | [RCC_APBSMENR1.json](../registers_json/RCC_APBSMENR1.json) |
| `RCC_APBSMENR2` | `0x50` | RCC APB periphera l clock enable in Sleep/Stop mode register 2 (RCC_APBSMENR2) | [RCC_APBSMENR2.json](../registers_json/RCC_APBSMENR2.json) |
| `RCC_CCIPR` | `0x54` | RCC peripherals independent clock configuration register 1 (RCC_CCIPR) | [RCC_CCIPR.json](../registers_json/RCC_CCIPR.json) |
| `RCC_CCIPR2` | `0x58` | RCC peripherals independent clock configuration register 2 (RCC_CCIPR2) | [RCC_CCIPR2.json](../registers_json/RCC_CCIPR2.json) |
| `RCC_CFGR` | `0x08` | RCC clock configurat ion register (RCC_CFGR) | [RCC_CFGR.json](../registers_json/RCC_CFGR.json) |
| `RCC_CICR` | `0x20` | RCC clock interrupt clear register (RCC_CICR) | [RCC_CICR.json](../registers_json/RCC_CICR.json) |
| `RCC_CIER` | `0x18` | RCC clock interrupt en able register (RCC_CIER) | [RCC_CIER.json](../registers_json/RCC_CIER.json) |
| `RCC_CIFR` | `0x1C` | RCC clock interrupt flag register (RCC_CIFR) | [RCC_CIFR.json](../registers_json/RCC_CIFR.json) |
| `RCC_CR` | `0x00` | RCC clock cont rol register (RCC_CR) | [RCC_CR.json](../registers_json/RCC_CR.json) |
| `RCC_CRRCR` | `0x14` | RCC clock recovery RC register (RCC_CRRCR) | [RCC_CRRCR.json](../registers_json/RCC_CRRCR.json) |
| `RCC_CSR1` | `0x5C` | RCC control/status register 1 (RCC_CSR1) | [RCC_CSR1.json](../registers_json/RCC_CSR1.json) |
| `RCC_CSR2` | `0x60` | RCC control/status register 2 (RCC_CSR2) | [RCC_CSR2.json](../registers_json/RCC_CSR2.json) |
| `RCC_ICSCR` | `0x04` | RCC internal clock source calibration register (RCC_ICSCR) | [RCC_ICSCR.json](../registers_json/RCC_ICSCR.json) |
| `RCC_IOPENR` | `0x34` | RCC I/O port clock en able register (RCC_IOPENR) | [RCC_IOPENR.json](../registers_json/RCC_IOPENR.json) |
| `RCC_IOPRSTR` | `0x24` | RCC I/O port reset register (RCC_IOPRSTR) | [RCC_IOPRSTR.json](../registers_json/RCC_IOPRSTR.json) |
| `RCC_IOPSMENR` | `0x44` | RCC I/O port in Sleep mode clock enable register (RCC_IOPSMENR) | [RCC_IOPSMENR.json](../registers_json/RCC_IOPSMENR.json) |