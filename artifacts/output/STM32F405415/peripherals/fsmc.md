# Flexible Static Memory Controller (FSMC)

## 1. Overview & Key Features
The Flexible Static Memory Controller (FSMC) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 39](../chapters/chapter_39.md) (Pages 1532 - 1589).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 39](../chapters/chapter_39.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Flexible Static Memory Controller (FSMC) Architectural Block Diagram](../figures/fsmc_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Flexible Static Memory Controller (FSMC) Configuration & Parameter Matrix](../tables/fsmc_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `FSMC_BCR1` | `0x0000` | Flexible Static Memory Controller (FSMC) FSMC_BCR1 Register | [FSMC_BCR1.json](../registers_json/FSMC_BCR1.json) |
| `FSMC_BCR2` | `0x0008` | Flexible Static Memory Controller (FSMC) FSMC_BCR2 Register | [FSMC_BCR2.json](../registers_json/FSMC_BCR2.json) |
| `FSMC_BCR3` | `0x0010` | Flexible Static Memory Controller (FSMC) FSMC_BCR3 Register | [FSMC_BCR3.json](../registers_json/FSMC_BCR3.json) |
| `FSMC_BCR4` | `0x0018` | Flexible Static Memory Controller (FSMC) FSMC_BCR4 Register | [FSMC_BCR4.json](../registers_json/FSMC_BCR4.json) |
| `FSMC_BTR1` | `0x0004` | Flexible Static Memory Controller (FSMC) FSMC_BTR1 Register | [FSMC_BTR1.json](../registers_json/FSMC_BTR1.json) |
| `FSMC_BTR2` | `0x000C` | Flexible Static Memory Controller (FSMC) FSMC_BTR2 Register | [FSMC_BTR2.json](../registers_json/FSMC_BTR2.json) |
| `FSMC_BTR3` | `0x0014` | Flexible Static Memory Controller (FSMC) FSMC_BTR3 Register | [FSMC_BTR3.json](../registers_json/FSMC_BTR3.json) |
| `FSMC_BTR4` | `0x001C` | Flexible Static Memory Controller (FSMC) FSMC_BTR4 Register | [FSMC_BTR4.json](../registers_json/FSMC_BTR4.json) |
| `FSMC_BWTR` | `0x0104` | Flexible Static Memory Controller (FSMC) FSMC_BWTR Register | [FSMC_BWTR.json](../registers_json/FSMC_BWTR.json) |
| `FSMC_ECCR2` | `0xA000` | 1586/1741 RM0090 Rev 22 ECC result registers 2/3 (FSMC_ECCR2) | [FSMC_ECCR2.json](../registers_json/FSMC_ECCR2.json) |
| `FSMC_ECCR3` | `0x0094` | Flexible Static Memory Controller (FSMC) FSMC_ECCR3 Register | [FSMC_ECCR3.json](../registers_json/FSMC_ECCR3.json) |
| `FSMC_PATT2` | `0x006C` | Flexible Static Memory Controller (FSMC) FSMC_PATT2 Register | [FSMC_PATT2.json](../registers_json/FSMC_PATT2.json) |
| `FSMC_PATT3` | `0x008C` | Flexible Static Memory Controller (FSMC) FSMC_PATT3 Register | [FSMC_PATT3.json](../registers_json/FSMC_PATT3.json) |
| `FSMC_PATT4` | `0x00AC` | Flexible Static Memory Controller (FSMC) FSMC_PATT4 Register | [FSMC_PATT4.json](../registers_json/FSMC_PATT4.json) |
| `FSMC_PCR2` | `0x0060` | Flexible Static Memory Controller (FSMC) FSMC_PCR2 Register | [FSMC_PCR2.json](../registers_json/FSMC_PCR2.json) |
| `FSMC_PCR3` | `0x0080` | Flexible Static Memory Controller (FSMC) FSMC_PCR3 Register | [FSMC_PCR3.json](../registers_json/FSMC_PCR3.json) |
| `FSMC_PCR4` | `0x00A0` | Flexible Static Memory Controller (FSMC) FSMC_PCR4 Register | [FSMC_PCR4.json](../registers_json/FSMC_PCR4.json) |
| `FSMC_PIO4` | `0xA000` | I/O space timing register 4 (FSMC_PIO4) | [FSMC_PIO4.json](../registers_json/FSMC_PIO4.json) |
| `FSMC_PMEM` | `0x0068` | Flexible Static Memory Controller (FSMC) FSMC_PMEM Register | [FSMC_PMEM.json](../registers_json/FSMC_PMEM.json) |
| `FSMC_SR2` | `0x0064` | Flexible Static Memory Controller (FSMC) FSMC_SR2 Register | [FSMC_SR2.json](../registers_json/FSMC_SR2.json) |
| `FSMC_SR3` | `0x0084` | Flexible Static Memory Controller (FSMC) FSMC_SR3 Register | [FSMC_SR3.json](../registers_json/FSMC_SR3.json) |
| `FSMC_SR4` | `0x00A4` | Flexible Static Memory Controller (FSMC) FSMC_SR4 Register | [FSMC_SR4.json](../registers_json/FSMC_SR4.json) |