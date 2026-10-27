# Independent Watchdog (IWDG)

## 1. Overview & Key Features
The Independent Watchdog (IWDG) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 39](../chapters/chapter_39.md) (Pages 1380 - 1388).

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
* [Figure: Independent Watchdog (IWDG) Architectural Block Diagram](../figures/iwdg_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Independent Watchdog (IWDG) Configuration & Parameter Matrix](../tables/iwdg_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `IWDG` | `0x00` | MS34442V2 IWDG reset LSI VCORE VDD voltage domain Prescaler register IWDG_PR Status register IWDG_SR Reload register IWDG_RLR Key register IWDG_KR 12-bit reload value 12-bit downcounter 8-bit prescaler RM0438 Rev 8 1381/2187 RM0438 Independent watchdog (IWDG) | [IWDG.json](../registers_json/IWDG.json) |
| `IWDG_KR` | `0x00` | IWDG key register (IWDG_KR) | [IWDG_KR.json](../registers_json/IWDG_KR.json) |
| `IWDG_PR` | `0x04` | IWDG prescaler register (IWDG_PR) | [IWDG_PR.json](../registers_json/IWDG_PR.json) |
| `IWDG_RLR` | `0x08` | IWDG reload register (IWDG_RLR) | [IWDG_RLR.json](../registers_json/IWDG_RLR.json) |
| `IWDG_SR` | `0x0C` | IWDG status register (IWDG_SR) | [IWDG_SR.json](../registers_json/IWDG_SR.json) |
| `IWDG_WINR` | `0x10` | Independent Watchdog (IWDG) IWDG_WINR Register | [IWDG_WINR.json](../registers_json/IWDG_WINR.json) |