# Debug Support (DBG)

## 1. Overview & Key Features
The Debug Support (DBG) block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 47](../chapters/chapter_47.md) (Pages 2088 - 2120).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: CORE
* **Reference Chapter**: [Chapter 47](../chapters/chapter_47.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Debug Support (DBG) Architectural Block Diagram](../figures/debug_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Debug Support (DBG) Configuration & Parameter Matrix](../tables/debug_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `DEBUG_CR` | `0x00` | Debug Support (DBG) Control Register | [DEBUG_CR.json](../registers_json/DEBUG_CR.json) |
| `DEBUG_SR` | `0x04` | Debug Support (DBG) Status Register | [DEBUG_SR.json](../registers_json/DEBUG_SR.json) |
| `DEBUG_DR` | `0x08` | Debug Support (DBG) Data Register | [DEBUG_DR.json](../registers_json/DEBUG_DR.json) |