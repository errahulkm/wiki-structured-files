# Master System Memory Map

## 1. Overview & Key Features
The Master System Memory Map block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 2](../chapters/chapter_02.md) (Pages 79 - 93).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: MEMORY
* **Reference Chapter**: [Chapter 2](../chapters/chapter_02.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Master System Memory Map Architectural Block Diagram](../figures/memory_map_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Master System Memory Map Configuration & Parameter Matrix](../tables/memory_map_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `MEMORY_MAP_CR` | `0x00` | Master System Memory Map Control Register | [MEMORY_MAP_CR.json](../registers_json/MEMORY_MAP_CR.json) |
| `MEMORY_MAP_SR` | `0x04` | Master System Memory Map Status Register | [MEMORY_MAP_SR.json](../registers_json/MEMORY_MAP_SR.json) |
| `MEMORY_MAP_DR` | `0x08` | Master System Memory Map Data Register | [MEMORY_MAP_DR.json](../registers_json/MEMORY_MAP_DR.json) |