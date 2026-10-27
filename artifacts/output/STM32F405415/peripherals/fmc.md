# Flexible Memory Controller (FMC)

## 1. Overview & Key Features
The Flexible Memory Controller (FMC) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 40](../chapters/chapter_40.md) (Pages 1590 - 1670).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 40](../chapters/chapter_40.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Flexible Memory Controller (FMC) Architectural Block Diagram](../figures/fmc_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Flexible Memory Controller (FMC) Configuration & Parameter Matrix](../tables/fmc_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `FMC_BCR1` | `0x00` | Flexible Memory Controller (FMC) FMC_BCR1 Register | [FMC_BCR1.json](../registers_json/FMC_BCR1.json) |
| `FMC_BCR2` | `0x08` | Flexible Memory Controller (FMC) FMC_BCR2 Register | [FMC_BCR2.json](../registers_json/FMC_BCR2.json) |
| `FMC_BCR3` | `0x10` | Flexible Memory Controller (FMC) FMC_BCR3 Register | [FMC_BCR3.json](../registers_json/FMC_BCR3.json) |
| `FMC_BCR4` | `0x18` | Flexible Memory Controller (FMC) FMC_BCR4 Register | [FMC_BCR4.json](../registers_json/FMC_BCR4.json) |
| `FMC_BTR1` | `0x04` | Flexible Memory Controller (FMC) FMC_BTR1 Register | [FMC_BTR1.json](../registers_json/FMC_BTR1.json) |
| `FMC_BTR2` | `0x0C` | Flexible Memory Controller (FMC) FMC_BTR2 Register | [FMC_BTR2.json](../registers_json/FMC_BTR2.json) |
| `FMC_BTR3` | `0x14` | Flexible Memory Controller (FMC) FMC_BTR3 Register | [FMC_BTR3.json](../registers_json/FMC_BTR3.json) |
| `FMC_BTR4` | `0x1C` | Flexible Memory Controller (FMC) FMC_BTR4 Register | [FMC_BTR4.json](../registers_json/FMC_BTR4.json) |
| `FMC_BWTR1` | `0x104` | Flexible Memory Controller (FMC) FMC_BWTR1 Register | [FMC_BWTR1.json](../registers_json/FMC_BWTR1.json) |
| `FMC_BWTR2` | `0x10C` | Flexible Memory Controller (FMC) FMC_BWTR2 Register | [FMC_BWTR2.json](../registers_json/FMC_BWTR2.json) |
| `FMC_BWTR3` | `0x104` | Flexible Memory Controller (FMC) FMC_BWTR3 Register | [FMC_BWTR3.json](../registers_json/FMC_BWTR3.json) |
| `FMC_BWTR4` | `0x10C` | Flexible Memory Controller (FMC) FMC_BWTR4 Register | [FMC_BWTR4.json](../registers_json/FMC_BWTR4.json) |
| `FMC_ECCR2` | `0x54` | 1650/1741 RM0090 Rev 22 ECC result registers 2/3 (FMC_ECCR2) | [FMC_ECCR2.json](../registers_json/FMC_ECCR2.json) |
| `FMC_ECCR3` | `0x94` | Flexible Memory Controller (FMC) FMC_ECCR3 Register | [FMC_ECCR3.json](../registers_json/FMC_ECCR3.json) |
| `FMC_PATT2` | `0x6C` | Flexible Memory Controller (FMC) FMC_PATT2 Register | [FMC_PATT2.json](../registers_json/FMC_PATT2.json) |
| `FMC_PATT3` | `0x8C` | Flexible Memory Controller (FMC) FMC_PATT3 Register | [FMC_PATT3.json](../registers_json/FMC_PATT3.json) |
| `FMC_PATT4` | `0xAC` | Flexible Memory Controller (FMC) FMC_PATT4 Register | [FMC_PATT4.json](../registers_json/FMC_PATT4.json) |
| `FMC_PCR2` | `0x60` | Flexible Memory Controller (FMC) FMC_PCR2 Register | [FMC_PCR2.json](../registers_json/FMC_PCR2.json) |
| `FMC_PCR3` | `0x80` | Flexible Memory Controller (FMC) FMC_PCR3 Register | [FMC_PCR3.json](../registers_json/FMC_PCR3.json) |
| `FMC_PCR4` | `0xA0` | Flexible Memory Controller (FMC) FMC_PCR4 Register | [FMC_PCR4.json](../registers_json/FMC_PCR4.json) |
| `FMC_PIO4` | `0xB0` | 1648/1741 RM0090 Rev 22 I/O space timing register 4 (FMC_PIO4) | [FMC_PIO4.json](../registers_json/FMC_PIO4.json) |
| `FMC_PMEM2` | `0x68` | Flexible Memory Controller (FMC) FMC_PMEM2 Register | [FMC_PMEM2.json](../registers_json/FMC_PMEM2.json) |
| `FMC_PMEM3` | `0x88` | Flexible Memory Controller (FMC) FMC_PMEM3 Register | [FMC_PMEM3.json](../registers_json/FMC_PMEM3.json) |
| `FMC_PMEM4` | `0xA8` | Flexible Memory Controller (FMC) FMC_PMEM4 Register | [FMC_PMEM4.json](../registers_json/FMC_PMEM4.json) |
| `FMC_SDCMR` | `0x150` | SDRAM Command Mode register (FMC_SDCMR) | [FMC_SDCMR.json](../registers_json/FMC_SDCMR.json) |
| `FMC_SDCR_1` | `0x140` | Flexible Memory Controller (FMC) FMC_SDCR_1 Register | [FMC_SDCR_1.json](../registers_json/FMC_SDCR_1.json) |
| `FMC_SDCR_2` | `0x144` | Flexible Memory Controller (FMC) FMC_SDCR_2 Register | [FMC_SDCR_2.json](../registers_json/FMC_SDCR_2.json) |
| `FMC_SDRTR` | `0x154` | 1666/1741 RM0090 Rev 22 SDRAM Refresh Timer register (FMC_SDRTR) | [FMC_SDRTR.json](../registers_json/FMC_SDRTR.json) |
| `FMC_SDSR` | `0x158` | SDRAM Status register (FMC_SDSR) | [FMC_SDSR.json](../registers_json/FMC_SDSR.json) |
| `FMC_SDTR1` | `0x148` | Flexible Memory Controller (FMC) FMC_SDTR1 Register | [FMC_SDTR1.json](../registers_json/FMC_SDTR1.json) |
| `FMC_SDTR2` | `0x14C` | Flexible Memory Controller (FMC) FMC_SDTR2 Register | [FMC_SDTR2.json](../registers_json/FMC_SDTR2.json) |
| `FMC_SR2` | `0x64` | Flexible Memory Controller (FMC) FMC_SR2 Register | [FMC_SR2.json](../registers_json/FMC_SR2.json) |
| `FMC_SR3` | `0x84` | Flexible Memory Controller (FMC) FMC_SR3 Register | [FMC_SR3.json](../registers_json/FMC_SR3.json) |
| `FMC_SR4` | `0xA4` | Flexible Memory Controller (FMC) FMC_SR4 Register | [FMC_SR4.json](../registers_json/FMC_SR4.json) |