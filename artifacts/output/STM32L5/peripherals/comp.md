# Comparator (COMP)

## 1. Overview & Key Features
The Comparator (COMP) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 24](../chapters/chapter_24.md) (Pages 837 - 848).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 24](../chapters/chapter_24.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Comparator (COMP) Architectural Block Diagram](../figures/comp_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Comparator (COMP) Configuration & Parameter Matrix](../tables/comp_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `COMP1_CSR` | `0x00` | Comparator 1 control a nd status register (COMP1_CSR) | [COMP1_CSR.json](../registers_json/COMP1_CSR.json) |
| `COMP2_CSR` | `0x04` | Comparator 2 control and status register (COMP2_CSR) | [COMP2_CSR.json](../registers_json/COMP2_CSR.json) |