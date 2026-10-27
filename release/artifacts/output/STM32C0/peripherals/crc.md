# CRC Calculation Unit

## 1. Overview & Key Features
The CRC Calculation Unit block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 15](../chapters/chapter_15.md) (Pages 280 - 286).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 15](../chapters/chapter_15.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: CRC Calculation Unit Architectural Block Diagram](../figures/crc_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: CRC Calculation Unit Configuration & Parameter Matrix](../tables/crc_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `CRC_CR` | `0x08` | CRC control register (CRC_CR) | [CRC_CR.json](../registers_json/CRC_CR.json) |
| `CRC_DR` | `0x00` | CRC data register (CRC_DR) | [CRC_DR.json](../registers_json/CRC_DR.json) |
| `CRC_IDR` | `0x04` | CRC independent da ta register (CRC_IDR) | [CRC_IDR.json](../registers_json/CRC_IDR.json) |
| `CRC_INIT` | `0x10` | CRC Calculation Unit CRC_INIT Register | [CRC_INIT.json](../registers_json/CRC_INIT.json) |
| `CRC_POL` | `0x14` | CRC Calculation Unit CRC_POL Register | [CRC_POL.json](../registers_json/CRC_POL.json) |