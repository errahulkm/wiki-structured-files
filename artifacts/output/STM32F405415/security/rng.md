# Random Number Generator (RNG)

## 1. Overview & Key Features
The Random Number Generator (RNG) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 27](../chapters/chapter_27.md) (Pages 763 - 767).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SECURITY
* **Reference Chapter**: [Chapter 27](../chapters/chapter_27.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Random Number Generator (RNG) Architectural Block Diagram](../figures/rng_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Random Number Generator (RNG) Configuration & Parameter Matrix](../tables/rng_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `RNG_CR` | `0x00` | RNG control register (RNG_CR) | [RNG_CR.json](../registers_json/RNG_CR.json) |
| `RNG_DR` | `0x08` | RNG data register (RNG_DR) | [RNG_DR.json](../registers_json/RNG_DR.json) |
| `RNG_SR` | `0x04` | RNG status register (RNG_SR) | [RNG_SR.json](../registers_json/RNG_SR.json) |