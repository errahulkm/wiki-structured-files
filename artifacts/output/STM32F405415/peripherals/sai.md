# Serial Audio Interface (SAI)

## 1. Overview & Key Features
The Serial Audio Interface (SAI) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 32](../chapters/chapter_32.md) (Pages 921 - 959).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 32](../chapters/chapter_32.md)
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
| `SAI_ACLRFR` | `0x01C` | SAI x clear flag register (SAI_ACLRFR) | [SAI_ACLRFR.json](../registers_json/SAI_ACLRFR.json) |
| `SAI_ACR1` | `0x004` | SAI x configuration register 1 (SAI_ACR1) | [SAI_ACR1.json](../registers_json/SAI_ACR1.json) |
| `SAI_ACR2` | `0x008` | SAI x configuration register 2 (SAI_ACR2) | [SAI_ACR2.json](../registers_json/SAI_ACR2.json) |
| `SAI_ADR` | `0x020` | SAI x data register (SAI_ADR) | [SAI_ADR.json](../registers_json/SAI_ADR.json) |
| `SAI_AFRCR` | `0x00C` | SAI x frame configuration regist er (SAI_AFRCR) | [SAI_AFRCR.json](../registers_json/SAI_AFRCR.json) |
| `SAI_AIM` | `0x014` | SAI x interrupt mask regist er (SAI_AIM) | [SAI_AIM.json](../registers_json/SAI_AIM.json) |
| `SAI_ASLOTR` | `0x010` | SAI x slot register (SAI_ASLOTR) | [SAI_ASLOTR.json](../registers_json/SAI_ASLOTR.json) |
| `SAI_ASR` | `0x018` | SAI x status register (SAI_ASR) | [SAI_ASR.json](../registers_json/SAI_ASR.json) |
| `SAI_BCLRFR` | `0x03C` | SAI x clear flag register (SAI_BCLRFR) | [SAI_BCLRFR.json](../registers_json/SAI_BCLRFR.json) |
| `SAI_BCR1` | `0x024` | SAI x configuration register 1 (SAI_BCR1) | [SAI_BCR1.json](../registers_json/SAI_BCR1.json) |
| `SAI_BCR2` | `0x028` | SAI x configuration register 2 (SAI_BCR2) | [SAI_BCR2.json](../registers_json/SAI_BCR2.json) |
| `SAI_BDR` | `0x040` | SAI x data register (SAI_BDR) | [SAI_BDR.json](../registers_json/SAI_BDR.json) |
| `SAI_BFRCR` | `0x02C` | SAI x frame configuration regist er (SAI_BFRCR) | [SAI_BFRCR.json](../registers_json/SAI_BFRCR.json) |
| `SAI_BIM` | `0x034` | SAI x interrupt mask regist er (SAI_BIM) | [SAI_BIM.json](../registers_json/SAI_BIM.json) |
| `SAI_BSLOTR` | `0x030` | SAI x slot register (SAI_BSLOTR) | [SAI_BSLOTR.json](../registers_json/SAI_BSLOTR.json) |
| `SAI_BSR` | `0x038` | SAI x status register (SAI_BSR) | [SAI_BSR.json](../registers_json/SAI_BSR.json) |
