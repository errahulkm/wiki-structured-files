# Power Control (PWR)

## 1. Overview & Key Features
The Power Control (PWR) block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 5](../chapters/chapter_05.md) (Pages 92 - 117).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SYSTEM
* **Reference Chapter**: [Chapter 5](../chapters/chapter_05.md)
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
| `PWR_BKP0R` | `0x070` | Power Control (PWR) PWR_BKP0R Register | [PWR_BKP0R.json](../registers_json/PWR_BKP0R.json) |
| `PWR_BKP1R` | `0x074` | Power Control (PWR) PWR_BKP1R Register | [PWR_BKP1R.json](../registers_json/PWR_BKP1R.json) |
| `PWR_BKP2R` | `0x078` | Power Control (PWR) PWR_BKP2R Register | [PWR_BKP2R.json](../registers_json/PWR_BKP2R.json) |
| `PWR_BKP3R` | `0x07C` | Power Control (PWR) PWR_BKP3R Register | [PWR_BKP3R.json](../registers_json/PWR_BKP3R.json) |
| `PWR_BKPXR` | `0x00` | PWR backup x re gister (PWR_BKPXR) | [PWR_BKPXR.json](../registers_json/PWR_BKPXR.json) |
| `PWR_CR1` | `0x000` | Power Control (PWR) PWR_CR1 Register | [PWR_CR1.json](../registers_json/PWR_CR1.json) |
| `PWR_CR2` | `0x004` | PWR control re gister 1 (PWR_CR2) | [PWR_CR2.json](../registers_json/PWR_CR2.json) |
| `PWR_CR3` | `0x008` | PWR control re gister 3 (PWR_CR3) | [PWR_CR3.json](../registers_json/PWR_CR3.json) |
| `PWR_CR4` | `0x00C` | PWR control re gister 4 (PWR_CR4) | [PWR_CR4.json](../registers_json/PWR_CR4.json) |
| `PWR_PDCRA` | `0x024` | PWR Port A pull-down c ontrol register (PWR_PDCRA) | [PWR_PDCRA.json](../registers_json/PWR_PDCRA.json) |
| `PWR_PDCRB` | `0x02C` | PWR Port B pull-down control register (PWR_PDCRB) | [PWR_PDCRB.json](../registers_json/PWR_PDCRB.json) |
| `PWR_PDCRC` | `0x034` | PWR Port C pull-down control register (PWR_PDCRC) | [PWR_PDCRC.json](../registers_json/PWR_PDCRC.json) |
| `PWR_PDCRD` | `0x03C` | PWR Port D pull-down control register (PWR_PDCRD) | [PWR_PDCRD.json](../registers_json/PWR_PDCRD.json) |
| `PWR_PDCRF` | `0x04C` | PWR Port F pull-down control register (PWR_PDCRF) | [PWR_PDCRF.json](../registers_json/PWR_PDCRF.json) |
| `PWR_PUCRA` | `0x020` | PWR Port A pull-up cont rol register (PWR_PUCRA) | [PWR_PUCRA.json](../registers_json/PWR_PUCRA.json) |
| `PWR_PUCRB` | `0x028` | PWR Port B pull-up c ontrol register (PWR_PUCRB) | [PWR_PUCRB.json](../registers_json/PWR_PUCRB.json) |
| `PWR_PUCRC` | `0x030` | PWR Port C pull-up c ontrol register (PWR_PUCRC) | [PWR_PUCRC.json](../registers_json/PWR_PUCRC.json) |
| `PWR_PUCRD` | `0x038` | PWR Port D pull-up c ontrol register (PWR_PUCRD) | [PWR_PUCRD.json](../registers_json/PWR_PUCRD.json) |
| `PWR_PUCRF` | `0x048` | PWR Port F pull-up c ontrol register (PWR_PUCRF) | [PWR_PUCRF.json](../registers_json/PWR_PUCRF.json) |
| `PWR_SCR` | `0x18` | PWR status clear register (PWR_SCR) | [PWR_SCR.json](../registers_json/PWR_SCR.json) |
| `PWR_SR1` | `0x010` | PWR status register 1 (PWR_SR1) | [PWR_SR1.json](../registers_json/PWR_SR1.json) |
| `PWR_SR2` | `0x014` | PWR status register 2 (PWR_SR2) | [PWR_SR2.json](../registers_json/PWR_SR2.json) |