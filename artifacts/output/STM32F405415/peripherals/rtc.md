# Real-Time Clock (RTC)

## 1. Overview & Key Features
The Real-Time Clock (RTC) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 29](../chapters/chapter_29.md) (Pages 794 - 834).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 29](../chapters/chapter_29.md)
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
| `RTC_ALRMAR` | `0x1C` | RTC alarm A register (RTC_ALRMAR) | [RTC_ALRMAR.json](../registers_json/RTC_ALRMAR.json) |
| `RTC_ALRMASSR` | `0x44` | RTC alarm A sub sec ond register (RTC_ALRMASSR) | [RTC_ALRMASSR.json](../registers_json/RTC_ALRMASSR.json) |
| `RTC_ALRMBR` | `0x20` | Real-Time Clock (RTC) RTC_ALRMBR Register | [RTC_ALRMBR.json](../registers_json/RTC_ALRMBR.json) |
| `RTC_ALRMBSSR` | `0x48` | RTC alarm B sub second register (RTC_ALRMBSSR) | [RTC_ALRMBSSR.json](../registers_json/RTC_ALRMBSSR.json) |
| `RTC_BKP0R` | `0x9C` | Real-Time Clock (RTC) RTC_BKP0R Register | [RTC_BKP0R.json](../registers_json/RTC_BKP0R.json) |
| `RTC_BKPXR` | `0x50` | RTC backup registers (RTC_BKPXR) | [RTC_BKPXR.json](../registers_json/RTC_BKPXR.json) |
| `RTC_CALIBR` | `0x18` | Real-Time Clock (RTC) RTC_CALIBR Register | [RTC_CALIBR.json](../registers_json/RTC_CALIBR.json) |
| `RTC_CALR` | `0x3C` | RTC calibration register (RTC_CALR) | [RTC_CALR.json](../registers_json/RTC_CALR.json) |
| `RTC_CR` | `0x08` | RTC control register (RTC_CR) | [RTC_CR.json](../registers_json/RTC_CR.json) |
| `RTC_DR` | `0x04` | RTC date register (RTC_DR) | [RTC_DR.json](../registers_json/RTC_DR.json) |
| `RTC_ISR` | `0x0C` | RTC initialization and status register (RTC_ISR) | [RTC_ISR.json](../registers_json/RTC_ISR.json) |
| `RTC_PRER` | `0x10` | Real-Time Clock (RTC) RTC_PRER Register | [RTC_PRER.json](../registers_json/RTC_PRER.json) |
| `RTC_SHIFTR` | `0x2C` | RTC shift contro l register (RTC_SHIFTR) | [RTC_SHIFTR.json](../registers_json/RTC_SHIFTR.json) |
| `RTC_SSR` | `0x28` | RTC sub second register (RTC_SSR) | [RTC_SSR.json](../registers_json/RTC_SSR.json) |
| `RTC_TAFCR` | `0x40` | RTC tamper and alternat e function configuration register (RTC_TAFCR) | [RTC_TAFCR.json](../registers_json/RTC_TAFCR.json) |
| `RTC_TR` | `0x00` | RTC time register (RTC_TR) | [RTC_TR.json](../registers_json/RTC_TR.json) |
| `RTC_TSDR` | `0x34` | RTC time stamp da te register (RTC_TSDR) | [RTC_TSDR.json](../registers_json/RTC_TSDR.json) |
| `RTC_TSSSR` | `0x38` | RTC timestamp sub s econd register (RTC_TSSSR) | [RTC_TSSSR.json](../registers_json/RTC_TSSSR.json) |
| `RTC_TSTR` | `0x30` | RTC time stamp ti me register (RTC_TSTR) | [RTC_TSTR.json](../registers_json/RTC_TSTR.json) |
| `RTC_WPR` | `0x24` | RTC write protect ion register (RTC_WPR) | [RTC_WPR.json](../registers_json/RTC_WPR.json) |
| `RTC_WUTR` | `0x14` | RTC wake-up timer register (RTC_WUTR) | [RTC_WUTR.json](../registers_json/RTC_WUTR.json) |