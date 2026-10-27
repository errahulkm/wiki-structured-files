# Real-Time Clock (RTC)

## 1. Overview & Key Features
The Real-Time Clock (RTC) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 41](../chapters/chapter_41.md) (Pages 1395 - 1446).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 41](../chapters/chapter_41.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Real-Time Clock (RTC) Architectural Block Diagram](../figures/rtc_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Real-Time Clock (RTC) Configuration & Parameter Matrix](../tables/rtc_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `RTC_` | `0x44` | Real-Time Clock (RTC) RTC_ Register | [RTC_.json](../registers_json/RTC_.json) |
| `RTC_ALRMAR` | `0x40` | Real-Time Clock (RTC) RTC_ALRMAR Register | [RTC_ALRMAR.json](../registers_json/RTC_ALRMAR.json) |
| `RTC_ALRMASSR` | `0x00` | RTC alarm A sub sec ond register (RTC_ALRMASSR) | [RTC_ALRMASSR.json](../registers_json/RTC_ALRMASSR.json) |
| `RTC_ALRMBR` | `0x48` | Real-Time Clock (RTC) RTC_ALRMBR Register | [RTC_ALRMBR.json](../registers_json/RTC_ALRMBR.json) |
| `RTC_ALRMBSSR` | `0x00` | RTC alarm B sub second register (RTC_ALRMBSSR) | [RTC_ALRMBSSR.json](../registers_json/RTC_ALRMBSSR.json) |
| `RTC_CALR` | `0x00` | RTC calibration register (RTC_CALR) | [RTC_CALR.json](../registers_json/RTC_CALR.json) |
| `RTC_CR` | `0x18` | RTC control register (RTC_CR) | [RTC_CR.json](../registers_json/RTC_CR.json) |
| `RTC_DR` | `0x04` | RTC date register (RTC_DR) | [RTC_DR.json](../registers_json/RTC_DR.json) |
| `RTC_ICSR` | `0x0C` | RTC initialization control and status register (RTC_ICSR) | [RTC_ICSR.json](../registers_json/RTC_ICSR.json) |
| `RTC_MISR` | `0x54` | RTC non-secure masked interr upt status register (RTC_MISR) | [RTC_MISR.json](../registers_json/RTC_MISR.json) |
| `RTC_PRER` | `0x10` | Real-Time Clock (RTC) RTC_PRER Register | [RTC_PRER.json](../registers_json/RTC_PRER.json) |
| `RTC_PRIVCR` | `0x1C` | RTC privilege mode c ontrol register (RTC_PRIVCR) | [RTC_PRIVCR.json](../registers_json/RTC_PRIVCR.json) |
| `RTC_SCR` | `0x5C` | RTC status clear register (RTC_SCR) | [RTC_SCR.json](../registers_json/RTC_SCR.json) |
| `RTC_SHIFTR` | `0x2C` | RTC shift contro l register (RTC_SHIFTR) | [RTC_SHIFTR.json](../registers_json/RTC_SHIFTR.json) |
| `RTC_SMCR` | `0x20` | RTC secure mode cont rol register (RTC_SMCR) | [RTC_SMCR.json](../registers_json/RTC_SMCR.json) |
| `RTC_SMISR` | `0x58` | RTC secure masked interrupt status register (RTC_SMISR) | [RTC_SMISR.json](../registers_json/RTC_SMISR.json) |
| `RTC_SR` | `0x50` | RTC status register (RTC_SR) | [RTC_SR.json](../registers_json/RTC_SR.json) |
| `RTC_SSR` | `0x08` | RTC sub second register (RTC_SSR) | [RTC_SSR.json](../registers_json/RTC_SSR.json) |
| `RTC_TR` | `0x00` | RTC time register (RTC_TR) | [RTC_TR.json](../registers_json/RTC_TR.json) |
| `RTC_TSDR` | `0x34` | RTC timestamp da te register (RTC_TSDR) | [RTC_TSDR.json](../registers_json/RTC_TSDR.json) |
| `RTC_TSSSR` | `0x38` | RTC timestamp sub s econd register (RTC_TSSSR) | [RTC_TSSSR.json](../registers_json/RTC_TSSSR.json) |
| `RTC_TSTR` | `0x30` | RTC timestamp ti me register (RTC_TSTR) | [RTC_TSTR.json](../registers_json/RTC_TSTR.json) |
| `RTC_WPR` | `0x24` | RTC write protect ion register (RTC_WPR) | [RTC_WPR.json](../registers_json/RTC_WPR.json) |
| `RTC_WUTR` | `0x14` | RTC wake-up timer register (RTC_WUTR) | [RTC_WUTR.json](../registers_json/RTC_WUTR.json) |