# Comparator (COMP)

## 1. Overview & Key Features
The Comparator (COMP) block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 24](../chapters/chapter_24.md) (Pages 768 - 775).

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
| `COMP_C1CSR` | `0x00` | Comparator (COMP) COMP_C1CSR Register | [COMP_C1CSR.json](../registers_json/COMP_C1CSR.json) |
| `COMP_C2CSR` | `0x04` | Comparator (COMP) COMP_C2CSR Register | [COMP_C2CSR.json](../registers_json/COMP_C2CSR.json) |
| `COMP_C3CSR` | `0x08` | Comparator (COMP) COMP_C3CSR Register | [COMP_C3CSR.json](../registers_json/COMP_C3CSR.json) |
| `COMP_C4CSR` | `0x0C` | Comparator (COMP) COMP_C4CSR Register | [COMP_C4CSR.json](../registers_json/COMP_C4CSR.json) |
| `COMP_C5CSR` | `0x10` | Comparator (COMP) COMP_C5CSR Register | [COMP_C5CSR.json](../registers_json/COMP_C5CSR.json) |
| `COMP_C6CSR` | `0x14` | Comparator (COMP) COMP_C6CSR Register | [COMP_C6CSR.json](../registers_json/COMP_C6CSR.json) |
| `COMP_C7CSR` | `0x18` | Comparator (COMP) COMP_C7CSR Register | [COMP_C7CSR.json](../registers_json/COMP_C7CSR.json) |
| `COMP_CXCSR` | `0x00` | Comparator x control a nd status register (COMP_CXCSR) | [COMP_CXCSR.json](../registers_json/COMP_CXCSR.json) |