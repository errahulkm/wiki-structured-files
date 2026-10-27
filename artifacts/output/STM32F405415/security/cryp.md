# Cryptographic Processor (CRYP)

## 1. Overview & Key Features
The Cryptographic Processor (CRYP) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 26](../chapters/chapter_26.md) (Pages 716 - 762).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SECURITY
* **Reference Chapter**: [Chapter 26](../chapters/chapter_26.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Cryptographic Processor (CRYP) Architectural Block Diagram](../figures/cryp_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Cryptographic Processor (CRYP) Configuration & Parameter Matrix](../tables/cryp_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `CRYP_CR` | `0x00` | Cryptographic Processor (CRYP) CRYP_CR Register | [CRYP_CR.json](../registers_json/CRYP_CR.json) |
| `CRYP_CSGC` | `0x8C` | Cryptographic Processor (CRYP) CRYP_CSGC Register | [CRYP_CSGC.json](../registers_json/CRYP_CSGC.json) |
| `CRYP_DIN` | `0x08` | CRYP data input register (CRYP_DIN) | [CRYP_DIN.json](../registers_json/CRYP_DIN.json) |
| `CRYP_DMAC` | `0x10` | Cryptographic Processor (CRYP) CRYP_DMAC Register | [CRYP_DMAC.json](../registers_json/CRYP_DMAC.json) |
| `CRYP_DMACR` | `0x10` | CRYP DMA control register (CRYP_DMACR) | [CRYP_DMACR.json](../registers_json/CRYP_DMACR.json) |
| `CRYP_DOUT` | `0x0C` | CRYP data output register (CRYP_DOUT) | [CRYP_DOUT.json](../registers_json/CRYP_DOUT.json) |
| `CRYP_IMSC` | `0x14` | Cryptographic Processor (CRYP) CRYP_IMSC Register | [CRYP_IMSC.json](../registers_json/CRYP_IMSC.json) |
| `CRYP_IMSCR` | `0x14` | CRYP interrupt mask set/c lear register (CRYP_IMSCR) | [CRYP_IMSCR.json](../registers_json/CRYP_IMSCR.json) |
| `CRYP_IV0LR` | `0x40` | Cryptographic Processor (CRYP) CRYP_IV0LR Register | [CRYP_IV0LR.json](../registers_json/CRYP_IV0LR.json) |
| `CRYP_IV0RR` | `0x44` | Cryptographic Processor (CRYP) CRYP_IV0RR Register | [CRYP_IV0RR.json](../registers_json/CRYP_IV0RR.json) |
| `CRYP_IV1LR` | `0x48` | Cryptographic Processor (CRYP) CRYP_IV1LR Register | [CRYP_IV1LR.json](../registers_json/CRYP_IV1LR.json) |
| `CRYP_IV1RR` | `0x4C` | Cryptographic Processor (CRYP) CRYP_IV1RR Register | [CRYP_IV1RR.json](../registers_json/CRYP_IV1RR.json) |
| `CRYP_K0LR` | `0x20` | Cryptographic Processor (CRYP) CRYP_K0LR Register | [CRYP_K0LR.json](../registers_json/CRYP_K0LR.json) |
| `CRYP_K0RR` | `0x24` | Cryptographic Processor (CRYP) CRYP_K0RR Register | [CRYP_K0RR.json](../registers_json/CRYP_K0RR.json) |
| `CRYP_K3LR` | `0x38` | Cryptographic Processor (CRYP) CRYP_K3LR Register | [CRYP_K3LR.json](../registers_json/CRYP_K3LR.json) |
| `CRYP_K3RR` | `0x3C` | Cryptographic Processor (CRYP) CRYP_K3RR Register | [CRYP_K3RR.json](../registers_json/CRYP_K3RR.json) |
| `CRYP_MISR` | `0x1C` | CRYP masked interrupt st atus register (CRYP_MISR) | [CRYP_MISR.json](../registers_json/CRYP_MISR.json) |
| `CRYP_RISR` | `0x18` | CRYP raw interrupt st atus register (CRYP_RISR) | [CRYP_RISR.json](../registers_json/CRYP_RISR.json) |
| `CRYP_SR` | `0x04` | CRYP status register (CRYP_SR) | [CRYP_SR.json](../registers_json/CRYP_SR.json) |