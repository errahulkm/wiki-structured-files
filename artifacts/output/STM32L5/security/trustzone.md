# Global TrustZone Security Controller

## 1. Overview & Key Features
The Global TrustZone Security Controller block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 5](../chapters/chapter_05.md) (Pages 130 - 173).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SECURITY
* **Reference Chapter**: [Chapter 5](../chapters/chapter_05.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Global TrustZone Security Controller Architectural Block Diagram](../figures/trustzone_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Global TrustZone Security Controller Configuration & Parameter Matrix](../tables/trustzone_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `TRUSTZONE_CR` | `0x00` | Global TrustZone Security Controller Control Register | [TRUSTZONE_CR.json](../registers_json/TRUSTZONE_CR.json) |
| `TRUSTZONE_SR` | `0x04` | Global TrustZone Security Controller Status Register | [TRUSTZONE_SR.json](../registers_json/TRUSTZONE_SR.json) |
| `TRUSTZONE_DR` | `0x08` | Global TrustZone Security Controller Data Register | [TRUSTZONE_DR.json](../registers_json/TRUSTZONE_DR.json) |