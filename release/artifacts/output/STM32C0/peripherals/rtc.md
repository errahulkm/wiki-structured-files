# Real-Time Clock (RTC)

## 1. Overview & Key Features
The Real-Time Clock (RTC) block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 24](../chapters/chapter_24.md) (Pages 647 - 677).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 24](../chapters/chapter_24.md)
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
| `RTC_ALRMAR` | `0x40` | RTC alarm A re gister (RTC_ALRMAR) | [RTC_ALRMAR.json](../registers_json/RTC_ALRMAR.json) |
| `RTC_ALRMASSR` | `0x00` | RTC alarm A sub sec ond register (RTC_ALRMASSR) | [RTC_ALRMASSR.json](../registers_json/RTC_ALRMASSR.json) |
| `RTC_CALR` | `0x00` | RTC calibration register (RTC_CALR) | [RTC_CALR.json](../registers_json/RTC_CALR.json) |
| `RTC_CR` | `0x18` | RTC control register (RTC_CR) | [RTC_CR.json](../registers_json/RTC_CR.json) |
| `RTC_DR` | `0x04` | RTC date register (RTC_DR) | [RTC_DR.json](../registers_json/RTC_DR.json) |
| `RTC_ICSR` | `0x0C` | RTC initialization control and status register (RTC_ICSR) | [RTC_ICSR.json](../registers_json/RTC_ICSR.json) |
| `RTC_MISR` | `0x54` | RTC masked interrupt status register (RTC_MISR) | [RTC_MISR.json](../registers_json/RTC_MISR.json) |
| `RTC_PRER` | `0x10` | RTC prescaler re gister (RTC_PRER) | [RTC_PRER.json](../registers_json/RTC_PRER.json) |
| `RTC_SCR` | `0x5C` | RTC status clear register (RTC_SCR) | [RTC_SCR.json](../registers_json/RTC_SCR.json) |
| `RTC_SHIFTR` | `0x2C` | RTC shift control register (RTC_SHIFTR) | [RTC_SHIFTR.json](../registers_json/RTC_SHIFTR.json) |
| `RTC_SR` | `0x50` | RTC status register (RTC_SR) | [RTC_SR.json](../registers_json/RTC_SR.json) |
| `RTC_SSR` | `0x08` | This bit is set by hardware each time the calendar registers are copied into the shadow registers (RTC_SSR) | [RTC_SSR.json](../registers_json/RTC_SSR.json) |
| `RTC_TR` | `0x00` | Real-Time Clock (RTC) RTC_TR Register | [RTC_TR.json](../registers_json/RTC_TR.json) |
| `RTC_TRANDRTC_DR` | `0x00` | This flag is set by hardware when the time/date registers (RTC_TRANDRTC_DR) | [RTC_TRANDRTC_DR.json](../registers_json/RTC_TRANDRTC_DR.json) |
| `RTC_TSDR` | `0x34` | RTC timestamp da te register (RTC_TSDR) | [RTC_TSDR.json](../registers_json/RTC_TSDR.json) |
| `RTC_TSSSR` | `0x38` | RTC timestamp sub s econd register (RTC_TSSSR) | [RTC_TSSSR.json](../registers_json/RTC_TSSSR.json) |
| `RTC_TSTR` | `0x30` | RTC timestamp ti me register (RTC_TSTR) | [RTC_TSTR.json](../registers_json/RTC_TSTR.json) |
| `RTC_WPR` | `0x24` | RTC write protectio n register (RTC_WPR) | [RTC_WPR.json](../registers_json/RTC_WPR.json) |