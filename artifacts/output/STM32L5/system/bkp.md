# Backup Registers (BKP)

## 1. Overview & Key Features
The Backup Registers (BKP) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 42](../chapters/chapter_42.md) (Pages 1447 - 1482).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SYSTEM
* **Reference Chapter**: [Chapter 42](../chapters/chapter_42.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Backup Registers (BKP) Architectural Block Diagram](../figures/bkp_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Backup Registers (BKP) Configuration & Parameter Matrix](../tables/bkp_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `BKP_CR` | `0x00` | Backup Registers (BKP) Control Register | [BKP_CR.json](../registers_json/BKP_CR.json) |
| `BKP_SR` | `0x04` | Backup Registers (BKP) Status Register | [BKP_SR.json](../registers_json/BKP_SR.json) |
| `BKP_DR` | `0x08` | Backup Registers (BKP) Data Register | [BKP_DR.json](../registers_json/BKP_DR.json) |