# System Configuration (SYSCFG)

## 1. Overview & Key Features
The System Configuration (SYSCFG) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 12](../chapters/chapter_12.md) (Pages 291 - 303).

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
| `SYSCFG_CMPCR` | `0x20` | Compensation cell contro l register (SYSCFG_CMPCR) | [SYSCFG_CMPCR.json](../registers_json/SYSCFG_CMPCR.json) |
| `SYSCFG_EXTICR1` | `0x08` | SYSCFG external interrup t configuration register 1 (SYSCFG_EXTICR1) | [SYSCFG_EXTICR1.json](../registers_json/SYSCFG_EXTICR1.json) |
| `SYSCFG_EXTICR2` | `0x0C` | SYSCFG external interrup t configuration register 2 (SYSCFG_EXTICR2) | [SYSCFG_EXTICR2.json](../registers_json/SYSCFG_EXTICR2.json) |
| `SYSCFG_EXTICR3` | `0x10` | SYSCFG external interrup t configuration register 3 (SYSCFG_EXTICR3) | [SYSCFG_EXTICR3.json](../registers_json/SYSCFG_EXTICR3.json) |
| `SYSCFG_EXTICR4` | `0x14` | SYSCFG external interrup t configuration register 4 (SYSCFG_EXTICR4) | [SYSCFG_EXTICR4.json](../registers_json/SYSCFG_EXTICR4.json) |
| `SYSCFG_MEMRMP` | `0x00` | SYSCFG memory remap register (SYSCFG_MEMRMP) | [SYSCFG_MEMRMP.json](../registers_json/SYSCFG_MEMRMP.json) |
| `SYSCFG_PMC` | `0x04` | SYSCFG peripheral mode conf iguration register (SYSCFG_PMC) | [SYSCFG_PMC.json](../registers_json/SYSCFG_PMC.json) |