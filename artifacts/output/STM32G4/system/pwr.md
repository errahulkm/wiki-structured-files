# Power Control (PWR)

## 1. Overview & Key Features
The Power Control (PWR) block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 6](../chapters/chapter_06.md) (Pages 228 - 269).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SYSTEM
* **Reference Chapter**: [Chapter 6](../chapters/chapter_06.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Power Control (PWR) Architectural Block Diagram](../figures/pwr_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Power Control (PWR) Configuration & Parameter Matrix](../tables/pwr_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `PWR_CR1` | `0x00` | Power Control (PWR) PWR_CR1 Register | [PWR_CR1.json](../registers_json/PWR_CR1.json) |
| `PWR_CR2` | `0x04` | Power Control (PWR) PWR_CR2 Register | [PWR_CR2.json](../registers_json/PWR_CR2.json) |
| `PWR_CR3` | `0x08` | Power Control (PWR) PWR_CR3 Register | [PWR_CR3.json](../registers_json/PWR_CR3.json) |
| `PWR_CR4` | `0x0C` | Power Control (PWR) PWR_CR4 Register | [PWR_CR4.json](../registers_json/PWR_CR4.json) |
| `PWR_CR5` | `0x80` | Power control register (PWR_CR5) | [PWR_CR5.json](../registers_json/PWR_CR5.json) |
| `PWR_PDCRA` | `0x24` | Power Port A pull-down co ntrol register (PWR_PDCRA) | [PWR_PDCRA.json](../registers_json/PWR_PDCRA.json) |
| `PWR_PDCRB` | `0x2C` | Power Port B pull-down control register (PWR_PDCRB) | [PWR_PDCRB.json](../registers_json/PWR_PDCRB.json) |
| `PWR_PDCRC` | `0x34` | Power Port C pull-down control register (PWR_PDCRC) | [PWR_PDCRC.json](../registers_json/PWR_PDCRC.json) |
| `PWR_PDCRD` | `0x3C` | Power Port D pull-down control register (PWR_PDCRD) | [PWR_PDCRD.json](../registers_json/PWR_PDCRD.json) |
| `PWR_PDCRE` | `0x44` | Power Port E pull-down control register (PWR_PDCRE) | [PWR_PDCRE.json](../registers_json/PWR_PDCRE.json) |
| `PWR_PDCRF` | `0x4C` | Power Port F pull-down control register (PWR_PDCRF) | [PWR_PDCRF.json](../registers_json/PWR_PDCRF.json) |
| `PWR_PDCRG` | `0x54` | Power Port G pull-down control register (PWR_PDCRG) | [PWR_PDCRG.json](../registers_json/PWR_PDCRG.json) |
| `PWR_PUCRA` | `0x20` | Power Port A pull-up c ontrol register (PWR_PUCRA) | [PWR_PUCRA.json](../registers_json/PWR_PUCRA.json) |
| `PWR_PUCRB` | `0x28` | Power Port B pull-up control register (PWR_PUCRB) | [PWR_PUCRB.json](../registers_json/PWR_PUCRB.json) |
| `PWR_PUCRC` | `0x30` | Power Port C pull-up control register (PWR_PUCRC) | [PWR_PUCRC.json](../registers_json/PWR_PUCRC.json) |
| `PWR_PUCRD` | `0x38` | Power Port D pull-up control register (PWR_PUCRD) | [PWR_PUCRD.json](../registers_json/PWR_PUCRD.json) |
| `PWR_PUCRE` | `0x40` | Power Port E pull-up control register (PWR_PUCRE) | [PWR_PUCRE.json](../registers_json/PWR_PUCRE.json) |
| `PWR_PUCRF` | `0x48` | Power Port F pull-up control register (PWR_PUCRF) | [PWR_PUCRF.json](../registers_json/PWR_PUCRF.json) |
| `PWR_PUCRG` | `0x50` | Power Port G pull-up control register (PWR_PUCRG) | [PWR_PUCRG.json](../registers_json/PWR_PUCRG.json) |
| `PWR_SCR` | `0x18` | Power status clea r register (PWR_SCR) | [PWR_SCR.json](../registers_json/PWR_SCR.json) |
| `PWR_SR1` | `0x10` | Power status register 1 (PWR_SR1) | [PWR_SR1.json](../registers_json/PWR_SR1.json) |
| `PWR_SR2` | `0x14` | Power status register 2 (PWR_SR2) | [PWR_SR2.json](../registers_json/PWR_SR2.json) |