# Embedded Flash Memory

## 1. Overview & Key Features
The Embedded Flash Memory block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 6](../chapters/chapter_06.md) (Pages 73 - 112).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: MEMORY
* **Reference Chapter**: [Chapter 6](../chapters/chapter_06.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Embedded Flash Memory Architectural Block Diagram](../figures/flash_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Embedded Flash Memory Configuration & Parameter Matrix](../tables/flash_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `FLASH_ACR` | `0x00` | Flash access control register (FLASH_ACR) | [FLASH_ACR.json](../registers_json/FLASH_ACR.json) |
| `FLASH_CR` | `0x10` | Embedded Flash Memory FLASH_CR Register | [FLASH_CR.json](../registers_json/FLASH_CR.json) |
| `FLASH_KEYR` | `0x04` | Flash key register (FLASH_KEYR) | [FLASH_KEYR.json](../registers_json/FLASH_KEYR.json) |
| `FLASH_OPT` | `0x08` | Embedded Flash Memory FLASH_OPT Register | [FLASH_OPT.json](../registers_json/FLASH_OPT.json) |
| `FLASH_OPTCR` | `0x14` | Flash option contro l register (FLASH_OPTCR) | [FLASH_OPTCR.json](../registers_json/FLASH_OPTCR.json) |
| `FLASH_OPTCR1` | `0x00` | Flash option contro l register (FLASH_OPTCR1) | [FLASH_OPTCR1.json](../registers_json/FLASH_OPTCR1.json) |
| `FLASH_OPTKEYR` | `0x00` | Flash option key regi ster (FLASH_OPTKEYR) | [FLASH_OPTKEYR.json](../registers_json/FLASH_OPTKEYR.json) |
| `FLASH_SR` | `0x0C` | Embedded Flash Memory FLASH_SR Register | [FLASH_SR.json](../registers_json/FLASH_SR.json) |