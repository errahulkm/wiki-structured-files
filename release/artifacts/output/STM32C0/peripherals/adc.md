# Analog-to-Digital Converter (ADC)

## 1. Overview & Key Features
The Analog-to-Digital Converter (ADC) block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 16](../chapters/chapter_16.md) (Pages 287 - 345).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 16](../chapters/chapter_16.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Analog-to-Digital Converter (ADC) Architectural Block Diagram](../figures/adc_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Analog-to-Digital Converter (ADC) Configuration & Parameter Matrix](../tables/adc_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `ADC_AWD1TR` | `0x20` | ADC watchdog threshol d register (ADC_AWD1TR) | [ADC_AWD1TR.json](../registers_json/ADC_AWD1TR.json) |
| `ADC_AWD2CR` | `0xA0` | ADC analog watc hdog 2 configuration register (ADC_AWD2CR) | [ADC_AWD2CR.json](../registers_json/ADC_AWD2CR.json) |
| `ADC_AWD2TR` | `0x24` | ADC watchdog threshol d register (ADC_AWD2TR) | [ADC_AWD2TR.json](../registers_json/ADC_AWD2TR.json) |
| `ADC_AWD3CR` | `0xA4` | ADC Analog Watchdog 3 Conf iguration register (ADC_AWD3CR) | [ADC_AWD3CR.json](../registers_json/ADC_AWD3CR.json) |
| `ADC_AWD3TR` | `0x2C` | ADC watchdog threshol d register (ADC_AWD3TR) | [ADC_AWD3TR.json](../registers_json/ADC_AWD3TR.json) |
| `ADC_CALFACT` | `0xB4` | Analog-to-Digital Converter (ADC) ADC_CALFACT Register | [ADC_CALFACT.json](../registers_json/ADC_CALFACT.json) |
| `ADC_CCR` | `0x308` | ADC common configurat ion register (ADC_CCR) | [ADC_CCR.json](../registers_json/ADC_CCR.json) |
| `ADC_CFGR1` | `0x0C` | ADC configuration register 1 (ADC_CFGR1) | [ADC_CFGR1.json](../registers_json/ADC_CFGR1.json) |
| `ADC_CFGR2` | `0x10` | ADC configuration register 2 (ADC_CFGR2) | [ADC_CFGR2.json](../registers_json/ADC_CFGR2.json) |
| `ADC_CHSELR` | `0x28` | ADC channel selecti on register (ADC_CHSELR) | [ADC_CHSELR.json](../registers_json/ADC_CHSELR.json) |
| `ADC_CR` | `0x08` | ADC control register (ADC_CR) | [ADC_CR.json](../registers_json/ADC_CR.json) |
| `ADC_DR` | `0x40` | ADC data register (ADC_DR) | [ADC_DR.json](../registers_json/ADC_DR.json) |
| `ADC_IER` | `0x04` | ADC interrupt enab le register (ADC_IER) | [ADC_IER.json](../registers_json/ADC_IER.json) |
| `ADC_ISR` | `0x00` | ADC interrupt and st atus register (ADC_ISR) | [ADC_ISR.json](../registers_json/ADC_ISR.json) |
| `ADC_SMPR` | `0x14` | ADC sampling time register (ADC_SMPR) | [ADC_SMPR.json](../registers_json/ADC_SMPR.json) |