# Flexible Static Memory Controller (FSMC)

## 1. Overview & Key Features
The Flexible Static Memory Controller (FSMC) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 19](../chapters/chapter_19.md) (Pages 570 - 625).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 19](../chapters/chapter_19.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Flexible Static Memory Controller (FSMC) Architectural Block Diagram](../figures/fsmc_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Flexible Static Memory Controller (FSMC) Configuration & Parameter Matrix](../tables/fsmc_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `FSMC_BCR1` | `0x00` | FSMC SRAM/NOR-Flash Chip-Select Control Register 1 | [FSMC_BCR1.json](../registers_json/FSMC_BCR1.json) |
| `FSMC_BTR1` | `0x04` | FSMC SRAM/NOR-Flash Chip-Select Timing Register 1 | [FSMC_BTR1.json](../registers_json/FSMC_BTR1.json) |
| `FSMC_BCR2` | `0x08` | FSMC SRAM/NOR-Flash Chip-Select Control Register 2 | [FSMC_BCR2.json](../registers_json/FSMC_BCR2.json) |
| `FSMC_BTR2` | `0x0C` | FSMC SRAM/NOR-Flash Chip-Select Timing Register 2 | [FSMC_BTR2.json](../registers_json/FSMC_BTR2.json) |
| `FSMC_BCR3` | `0x10` | FSMC SRAM/NOR-Flash Chip-Select Control Register 3 | [FSMC_BCR3.json](../registers_json/FSMC_BCR3.json) |
| `FSMC_BTR3` | `0x14` | FSMC SRAM/NOR-Flash Chip-Select Timing Register 3 | [FSMC_BTR3.json](../registers_json/FSMC_BTR3.json) |
| `FSMC_BCR4` | `0x18` | FSMC SRAM/NOR-Flash Chip-Select Control Register 4 | [FSMC_BCR4.json](../registers_json/FSMC_BCR4.json) |
| `FSMC_BTR4` | `0x1C` | FSMC SRAM/NOR-Flash Chip-Select Timing Register 4 | [FSMC_BTR4.json](../registers_json/FSMC_BTR4.json) |
| `FSMC_PCR2` | `0x60` | FSMC NAND Flash/PC Card Control Register 2 | [FSMC_PCR2.json](../registers_json/FSMC_PCR2.json) |
| `FSMC_SR2` | `0x64` | FSMC FIFO Status and Interrupt Register 2 | [FSMC_SR2.json](../registers_json/FSMC_SR2.json) |
| `FSMC_BWTR1` | `0x104` | FSMC SRAM/NOR-Flash Write Timing Register 1 | [FSMC_BWTR1.json](../registers_json/FSMC_BWTR1.json) |