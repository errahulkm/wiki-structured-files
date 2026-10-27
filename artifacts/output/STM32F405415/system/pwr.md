# Power Control (PWR)

## 1. Overview & Key Features
The Power Control (PWR) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 8](../chapters/chapter_08.md) (Pages 116 - 150).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SYSTEM
* **Reference Chapter**: [Chapter 8](../chapters/chapter_08.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Power Control (PWR) Architectural Block Diagram](../figures/pwr_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Power Control (PWR) Configuration & Parameter Matrix](../tables/pwr_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `PWR_CR` | `0x000` | PWR power control register (PWR_CR) | [PWR_CR.json](../registers_json/PWR_CR.json) |
| `PWR_CSR` | `0x004` | PWR power control/st atus register (PWR_CSR) | [PWR_CSR.json](../registers_json/PWR_CSR.json) |