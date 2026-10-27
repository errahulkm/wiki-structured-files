# Digital Camera Interface (DCMI)

## 1. Overview & Key Features
The Digital Camera Interface (DCMI) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 18](../chapters/chapter_18.md) (Pages 457 - 479).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 18](../chapters/chapter_18.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Digital Camera Interface (DCMI) Architectural Block Diagram](../figures/dcmi_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Digital Camera Interface (DCMI) Configuration & Parameter Matrix](../tables/dcmi_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `DCMI_CR` | `0x00` | Digital Camera Interface (DCMI) DCMI_CR Register | [DCMI_CR.json](../registers_json/DCMI_CR.json) |
| `DCMI_CWSIZ` | `0x24` | Digital Camera Interface (DCMI) DCMI_CWSIZ Register | [DCMI_CWSIZ.json](../registers_json/DCMI_CWSIZ.json) |
| `DCMI_CWSTR` | `0x20` | Digital Camera Interface (DCMI) DCMI_CWSTR Register | [DCMI_CWSTR.json](../registers_json/DCMI_CWSTR.json) |
| `DCMI_DR` | `0x28` | DCMI data register (DCMI_DR) | [DCMI_DR.json](../registers_json/DCMI_DR.json) |
| `DCMI_ESCR` | `0x18` | DCMI embedded synchronizati on code register (DCMI_ESCR) | [DCMI_ESCR.json](../registers_json/DCMI_ESCR.json) |
| `DCMI_ESUR` | `0x1C` | DCMI embedded synchroniza tion unmask register (DCMI_ESUR) | [DCMI_ESUR.json](../registers_json/DCMI_ESUR.json) |
| `DCMI_ICR` | `0x14` | DCMI interrupt clear register (DCMI_ICR) | [DCMI_ICR.json](../registers_json/DCMI_ICR.json) |
| `DCMI_IER` | `0x0C` | DCMI interrupt enable register (DCMI_IER) | [DCMI_IER.json](../registers_json/DCMI_IER.json) |
| `DCMI_MIS` | `0x10` | DCMI masked interrupt st atus register (DCMI_MIS) | [DCMI_MIS.json](../registers_json/DCMI_MIS.json) |
| `DCMI_RIS` | `0x08` | DCMI raw interrupt st atus register (DCMI_RIS) | [DCMI_RIS.json](../registers_json/DCMI_RIS.json) |
| `DCMI_SR` | `0x04` | Digital Camera Interface (DCMI) DCMI_SR Register | [DCMI_SR.json](../registers_json/DCMI_SR.json) |