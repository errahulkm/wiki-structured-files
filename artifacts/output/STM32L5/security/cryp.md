# Cryptographic Processor (CRYP)

## 1. Overview & Key Features
The Cryptographic Processor (CRYP) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 31](../chapters/chapter_31.md) (Pages 1023 - 1045).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SECURITY
* **Reference Chapter**: [Chapter 31](../chapters/chapter_31.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Cryptographic Processor (CRYP) Architectural Block Diagram](../figures/cryp_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Cryptographic Processor (CRYP) Configuration & Parameter Matrix](../tables/cryp_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `CRYP_CR` | `0x00` | Cryptographic Processor (CRYP) Control Register | [CRYP_CR.json](../registers_json/CRYP_CR.json) |
| `CRYP_SR` | `0x04` | Cryptographic Processor (CRYP) Status Register | [CRYP_SR.json](../registers_json/CRYP_SR.json) |
| `CRYP_DR` | `0x08` | Cryptographic Processor (CRYP) Data Register | [CRYP_DR.json](../registers_json/CRYP_DR.json) |