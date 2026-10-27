# SDMMC Interface

## 1. Overview & Key Features
The SDMMC Interface block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 48](../chapters/chapter_48.md) (Pages 1791 - 1868).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 48](../chapters/chapter_48.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: SDMMC Interface Architectural Block Diagram](../figures/sdmmc_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: SDMMC Interface Configuration & Parameter Matrix](../tables/sdmmc_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `SDMMC` | `0x00` | To control unit Odd receive shift register Even CRCEven receive shift register Odd transmit shift register Even transmit shift register Odd CRC Even CRC Mux in RM0438 Rev 8 1807/2187 RM0438 Secure digital input/output MultiMediaCard interface (SDMMC) | [SDMMC.json](../registers_json/SDMMC.json) |
| `SDMMC_` | `0x05C` | SDMMC Interface SDMMC_ Register | [SDMMC_.json](../registers_json/SDMMC_.json) |
| `SDMMC_ACKTIMER` | `0x040` | SDMMC acknowledgment ti mer register (SDMMC_ACKTIMER) | [SDMMC_ACKTIMER.json](../registers_json/SDMMC_ACKTIMER.json) |
| `SDMMC_ARGR` | `0x008` | SDMMC argument register (SDMMC_ARGR) | [SDMMC_ARGR.json](../registers_json/SDMMC_ARGR.json) |
| `SDMMC_CLKCR` | `0x004` | SDMMC clock control register (SDMMC_CLKCR) | [SDMMC_CLKCR.json](../registers_json/SDMMC_CLKCR.json) |
| `SDMMC_DCNTR` | `0x030` | SDMMC data counter register (SDMMC_DCNTR) | [SDMMC_DCNTR.json](../registers_json/SDMMC_DCNTR.json) |
| `SDMMC_DCTRL` | `0x02C` | SDMMC data control register (SDMMC_DCTRL) | [SDMMC_DCTRL.json](../registers_json/SDMMC_DCTRL.json) |
| `SDMMC_DLENR` | `0x028` | SDMMC data length register (SDMMC_DLENR) | [SDMMC_DLENR.json](../registers_json/SDMMC_DLENR.json) |
| `SDMMC_DTIMER` | `0x024` | SDMMC data timer register (SDMMC_DTIMER) | [SDMMC_DTIMER.json](../registers_json/SDMMC_DTIMER.json) |
| `SDMMC_FIFORX` | `0x080` | SDMMC data FIFO registers x (SDMMC_FIFORX) | [SDMMC_FIFORX.json](../registers_json/SDMMC_FIFORX.json) |
| `SDMMC_ICR` | `0x038` | SDMMC interrupt cl ear register (SDMMC_ICR) | [SDMMC_ICR.json](../registers_json/SDMMC_ICR.json) |
| `SDMMC_IDMABASE0R` | `0x058` | SDMMC IDMA buffer 0 base address register (SDMMC_IDMABASE0R) | [SDMMC_IDMABASE0R.json](../registers_json/SDMMC_IDMABASE0R.json) |
| `SDMMC_IDMABASE1R` | `0x05C` | SDMMC IDMA buffer 1 base address register (SDMMC_IDMABASE1R) | [SDMMC_IDMABASE1R.json](../registers_json/SDMMC_IDMABASE1R.json) |
| `SDMMC_IDMABSIZER` | `0x054` | SDMMC IDMA buffer size register (SDMMC_IDMABSIZER) | [SDMMC_IDMABSIZER.json](../registers_json/SDMMC_IDMABSIZER.json) |
| `SDMMC_IDMACTRLR` | `0x050` | SDMMC DMA control register (SDMMC_IDMACTRLR) | [SDMMC_IDMACTRLR.json](../registers_json/SDMMC_IDMACTRLR.json) |
| `SDMMC_POWER` | `0x000` | SDMMC power control register (SDMMC_POWER) | [SDMMC_POWER.json](../registers_json/SDMMC_POWER.json) |
| `SDMMC_RESPCMDR` | `0x010` | SDMMC command response register (SDMMC_RESPCMDR) | [SDMMC_RESPCMDR.json](../registers_json/SDMMC_RESPCMDR.json) |
| `SDMMC_STAR` | `0x034` | SDMMC status register (SDMMC_STAR) | [SDMMC_STAR.json](../registers_json/SDMMC_STAR.json) |