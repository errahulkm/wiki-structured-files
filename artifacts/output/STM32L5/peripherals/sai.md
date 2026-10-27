# Serial Audio Interface (SAI)

## 1. Overview & Key Features
The Serial Audio Interface (SAI) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 47](../chapters/chapter_47.md) (Pages 1723 - 1790).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 47](../chapters/chapter_47.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Serial Audio Interface (SAI) Architectural Block Diagram](../figures/sai_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Serial Audio Interface (SAI) Configuration & Parameter Matrix](../tables/sai_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `SAI_` | `0x40` | Serial Audio Interface (SAI) SAI_ Register | [SAI_.json](../registers_json/SAI_.json) |
| `SAI_ACLRFR` | `0x1C` | SAI clear flag register (SAI_ACLRFR) | [SAI_ACLRFR.json](../registers_json/SAI_ACLRFR.json) |
| `SAI_ACR1` | `0x04` | SAI configuration register 1 (SAI_ACR1) | [SAI_ACR1.json](../registers_json/SAI_ACR1.json) |
| `SAI_ACR2` | `0x08` | SAI configuration register 2 (SAI_ACR2) | [SAI_ACR2.json](../registers_json/SAI_ACR2.json) |
| `SAI_AFRCR` | `0x0C` | SAI frame configurat ion register (SAI_AFRCR) | [SAI_AFRCR.json](../registers_json/SAI_AFRCR.json) |
| `SAI_AIM` | `0x14` | SAI interrupt m ask register (SAI_AIM) | [SAI_AIM.json](../registers_json/SAI_AIM.json) |
| `SAI_ASLOTR` | `0x10` | SAI slot register (SAI_ASLOTR) | [SAI_ASLOTR.json](../registers_json/SAI_ASLOTR.json) |
| `SAI_BCLRFR` | `0x3C` | SAI clear flag register (SAI_BCLRFR) | [SAI_BCLRFR.json](../registers_json/SAI_BCLRFR.json) |
| `SAI_BCR1` | `0x24` | SAI configuration register 1 (SAI_BCR1) | [SAI_BCR1.json](../registers_json/SAI_BCR1.json) |
| `SAI_BCR2` | `0x28` | SAI configuratio n register 2 (SAI_BCR2) | [SAI_BCR2.json](../registers_json/SAI_BCR2.json) |
| `SAI_BFRCR` | `0x2C` | SAI frame configurat ion register (SAI_BFRCR) | [SAI_BFRCR.json](../registers_json/SAI_BFRCR.json) |
| `SAI_BIM` | `0x34` | SAI interrupt m ask register (SAI_BIM) | [SAI_BIM.json](../registers_json/SAI_BIM.json) |
| `SAI_BSLOTR` | `0x30` | SAI slot register (SAI_BSLOTR) | [SAI_BSLOTR.json](../registers_json/SAI_BSLOTR.json) |
| `SAI_BSR` | `0x38` | SAI status register (SAI_BSR) | [SAI_BSR.json](../registers_json/SAI_BSR.json) |
| `SAI_GCR` | `0x0000` | SAI global configur ation register (SAI_GCR) | [SAI_GCR.json](../registers_json/SAI_GCR.json) |
| `SAI_PDMCR` | `0x44` | SAI PDM control register (SAI_PDMCR) | [SAI_PDMCR.json](../registers_json/SAI_PDMCR.json) |
| `SAI_PDMDLY` | `0x48` | SAI PDM delay register (SAI_PDMDLY) | [SAI_PDMDLY.json](../registers_json/SAI_PDMDLY.json) |