# System Configuration (SYSCFG)

## 1. Overview & Key Features
The System Configuration (SYSCFG) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 12](../chapters/chapter_12.md) (Pages 456 - 468).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SYSTEM
* **Reference Chapter**: [Chapter 12](../chapters/chapter_12.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: System Configuration (SYSCFG) Architectural Block Diagram](../figures/syscfg_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: System Configuration (SYSCFG) Configuration & Parameter Matrix](../tables/syscfg_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `SYSCFG` | `0x10` | System Configuration (SYSCFG) SYSCFG Register | [SYSCFG.json](../registers_json/SYSCFG.json) |
| `SYSCFG_` | `0x0C` | System Configuration (SYSCFG) SYSCFG_ Register | [SYSCFG_.json](../registers_json/SYSCFG_.json) |
| `SYSCFG_CFGR1` | `0x04` | SYSCFG configuration register 1 (SYSCFG_CFGR1) | [SYSCFG_CFGR1.json](../registers_json/SYSCFG_CFGR1.json) |
| `SYSCFG_CFGR2` | `0x14` | SYSCFG configuration register 2 (SYSCFG_CFGR2) | [SYSCFG_CFGR2.json](../registers_json/SYSCFG_CFGR2.json) |
| `SYSCFG_CNSLCKR` | `0x0C` | SYSCFG CPU non-secure lock register (SYSCFG_CNSLCKR) | [SYSCFG_CNSLCKR.json](../registers_json/SYSCFG_CNSLCKR.json) |
| `SYSCFG_CSLOCKR` | `0x10` | SYSCFG CPU secure lock register (SYSCFG_CSLOCKR) | [SYSCFG_CSLOCKR.json](../registers_json/SYSCFG_CSLOCKR.json) |
| `SYSCFG_FPUIMR` | `0x08` | FPU interrupt mask register (SYSCFG_FPUIMR) | [SYSCFG_FPUIMR.json](../registers_json/SYSCFG_FPUIMR.json) |
| `SYSCFG_RSSCMDR` | `0x2C` | System Configuration (SYSCFG) SYSCFG_RSSCMDR Register | [SYSCFG_RSSCMDR.json](../registers_json/SYSCFG_RSSCMDR.json) |
| `SYSCFG_SCSR` | `0x18` | SYSCFG SRAM2 control and status register (SYSCFG_SCSR) | [SYSCFG_SCSR.json](../registers_json/SYSCFG_SCSR.json) |
| `SYSCFG_SECCFGR` | `0x00` | SYSCFG secure configurat ion register (SYSCFG_SECCFGR) | [SYSCFG_SECCFGR.json](../registers_json/SYSCFG_SECCFGR.json) |
| `SYSCFG_SKR` | `0x1C` | System Configuration (SYSCFG) SYSCFG_SKR Register | [SYSCFG_SKR.json](../registers_json/SYSCFG_SKR.json) |
| `SYSCFG_SWPR` | `0x20` | SYSCFG SRAM2 write protec tion register (SYSCFG_SWPR) | [SYSCFG_SWPR.json](../registers_json/SYSCFG_SWPR.json) |
| `SYSCFG_SWPR2` | `0x24` | SYSCFG SRAM2 wr ite protection register 2 (SYSCFG_SWPR2) | [SYSCFG_SWPR2.json](../registers_json/SYSCFG_SWPR2.json) |