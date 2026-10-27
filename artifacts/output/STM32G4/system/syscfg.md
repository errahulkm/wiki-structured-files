# System Configuration (SYSCFG)

## 1. Overview & Key Features
The System Configuration (SYSCFG) block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 10](../chapters/chapter_10.md) (Pages 364 - 375).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SYSTEM
* **Reference Chapter**: [Chapter 10](../chapters/chapter_10.md)
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
| `SYSCFG_` | `0x00` | System Configuration (SYSCFG) SYSCFG_ Register | [SYSCFG_.json](../registers_json/SYSCFG_.json) |
| `SYSCFG_CFGR1` | `0x04` | SYSCFG configuration register 1 (SYSCFG_CFGR1) | [SYSCFG_CFGR1.json](../registers_json/SYSCFG_CFGR1.json) |
| `SYSCFG_CFGR2` | `0x1C` | SYSCFG configuration register 2 (SYSCFG_CFGR2) | [SYSCFG_CFGR2.json](../registers_json/SYSCFG_CFGR2.json) |
| `SYSCFG_EXTICR1` | `0x08` | SYSCFG external interrup t configuration register 1 (SYSCFG_EXTICR1) | [SYSCFG_EXTICR1.json](../registers_json/SYSCFG_EXTICR1.json) |
| `SYSCFG_EXTICR2` | `0x0C` | SYSCFG external interrup t configuration register 2 (SYSCFG_EXTICR2) | [SYSCFG_EXTICR2.json](../registers_json/SYSCFG_EXTICR2.json) |
| `SYSCFG_EXTICR3` | `0x10` | SYSCFG external interrup t configuration register 3 (SYSCFG_EXTICR3) | [SYSCFG_EXTICR3.json](../registers_json/SYSCFG_EXTICR3.json) |
| `SYSCFG_EXTICR4` | `0x14` | SYSCFG external interrup t configuration register 4 (SYSCFG_EXTICR4) | [SYSCFG_EXTICR4.json](../registers_json/SYSCFG_EXTICR4.json) |
| `SYSCFG_MEMRMP` | `0x00` | SYSCFG memory remap register (SYSCFG_MEMRMP) | [SYSCFG_MEMRMP.json](../registers_json/SYSCFG_MEMRMP.json) |
| `SYSCFG_SCSR` | `0x18` | SYSCFG CCM SRAM control and status register (SYSCFG_SCSR) | [SYSCFG_SCSR.json](../registers_json/SYSCFG_SCSR.json) |
| `SYSCFG_SKR` | `0x24` | SYSCFG CCM SRAM key register (SYSCFG_SKR) | [SYSCFG_SKR.json](../registers_json/SYSCFG_SKR.json) |
| `SYSCFG_SWPR` | `0x20` | SYSCFG CCM SRAM write pr otection register (SYSCFG_SWPR) | [SYSCFG_SWPR.json](../registers_json/SYSCFG_SWPR.json) |