# Analog-to-Digital Converter (ADC)

## 1. Overview & Key Features
The Analog-to-Digital Converter (ADC) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 21](../chapters/chapter_21.md) (Pages 683 - 795).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 21](../chapters/chapter_21.md)
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
| `ADC` | `0x000` | Offset Register name reset value 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0438 Rev 8 795/2187 RM0438 Analog-to-digital converters (ADC) | [ADC.json](../registers_json/ADC.json) |
| `ADC1` | `0x0B8` | Analog-to-Digital Converter (ADC) ADC1 Register | [ADC1.json](../registers_json/ADC1.json) |
| `ADC2` | `0x1B8` | Analog-to-Digital Converter (ADC) ADC2 Register | [ADC2.json](../registers_json/ADC2.json) |
| `ADCX_CDR` | `0x00` | ADC channel to read the common ADC register (ADCX_CDR) | [ADCX_CDR.json](../registers_json/ADCX_CDR.json) |
| `ADC_AWD2CR` | `0xA0` | ADC analog wa tchdog 2 configuration register (ADC_AWD2CR) | [ADC_AWD2CR.json](../registers_json/ADC_AWD2CR.json) |
| `ADC_AWD3CR` | `0xA4` | ADC analog wa tchdog 3 configuration register (ADC_AWD3CR) | [ADC_AWD3CR.json](../registers_json/ADC_AWD3CR.json) |
| `ADC_CALFACT` | `0xB4` | Analog-to-Digital Converter (ADC) ADC_CALFACT Register | [ADC_CALFACT.json](../registers_json/ADC_CALFACT.json) |
| `ADC_CCR` | `0x308` | ADC common contro l register (ADC_CCR) | [ADC_CCR.json](../registers_json/ADC_CCR.json) |
| `ADC_CDR` | `0x0C` | Analog-to-Digital Converter (ADC) ADC_CDR Register | [ADC_CDR.json](../registers_json/ADC_CDR.json) |
| `ADC_CFGR` | `0x0C` | ADC configurati on register (ADC_CFGR) | [ADC_CFGR.json](../registers_json/ADC_CFGR.json) |
| `ADC_CFGR2` | `0x10` | ADC configuration register 2 (ADC_CFGR2) | [ADC_CFGR2.json](../registers_json/ADC_CFGR2.json) |
| `ADC_CR` | `0x08` | ADC control register (ADC_CR) | [ADC_CR.json](../registers_json/ADC_CR.json) |
| `ADC_CSR` | `0x300` | ADC common status register (ADC_CSR) | [ADC_CSR.json](../registers_json/ADC_CSR.json) |
| `ADC_DIFSEL` | `0xB0` | ADC differential mode se lection register (ADC_DIFSEL) | [ADC_DIFSEL.json](../registers_json/ADC_DIFSEL.json) |
| `ADC_DR` | `0x40` | ADC regular da ta register (ADC_DR) | [ADC_DR.json](../registers_json/ADC_DR.json) |
| `ADC_IER` | `0x04` | ADC interrupt enable register (ADC_IER) | [ADC_IER.json](../registers_json/ADC_IER.json) |
| `ADC_ISR` | `0x00` | ADC interrupt and st atus register (ADC_ISR) | [ADC_ISR.json](../registers_json/ADC_ISR.json) |
| `ADC_JDR1` | `0x80` | Analog-to-Digital Converter (ADC) ADC_JDR1 Register | [ADC_JDR1.json](../registers_json/ADC_JDR1.json) |
| `ADC_JDR2` | `0x84` | Analog-to-Digital Converter (ADC) ADC_JDR2 Register | [ADC_JDR2.json](../registers_json/ADC_JDR2.json) |
| `ADC_JDR3` | `0x88` | Analog-to-Digital Converter (ADC) ADC_JDR3 Register | [ADC_JDR3.json](../registers_json/ADC_JDR3.json) |
| `ADC_JDR4` | `0x8C` | Analog-to-Digital Converter (ADC) ADC_JDR4 Register | [ADC_JDR4.json](../registers_json/ADC_JDR4.json) |
| `ADC_JDRY` | `0x80` | ADC injected channel y data register (ADC_JDRY) | [ADC_JDRY.json](../registers_json/ADC_JDRY.json) |
| `ADC_JSQR` | `0x4C` | ADC injected seque nce register (ADC_JSQR) | [ADC_JSQR.json](../registers_json/ADC_JSQR.json) |
| `ADC_OFR1` | `0x60` | Analog-to-Digital Converter (ADC) ADC_OFR1 Register | [ADC_OFR1.json](../registers_json/ADC_OFR1.json) |
| `ADC_OFR2` | `0x64` | Analog-to-Digital Converter (ADC) ADC_OFR2 Register | [ADC_OFR2.json](../registers_json/ADC_OFR2.json) |
| `ADC_OFR3` | `0x68` | Analog-to-Digital Converter (ADC) ADC_OFR3 Register | [ADC_OFR3.json](../registers_json/ADC_OFR3.json) |
| `ADC_OFR4` | `0x6C` | Analog-to-Digital Converter (ADC) ADC_OFR4 Register | [ADC_OFR4.json](../registers_json/ADC_OFR4.json) |
| `ADC_OFRY` | `0x60` | ADC offset y register (ADC_OFRY) | [ADC_OFRY.json](../registers_json/ADC_OFRY.json) |
| `ADC_SMPR1` | `0x14` | ADC sample time register 1 (ADC_SMPR1) | [ADC_SMPR1.json](../registers_json/ADC_SMPR1.json) |
| `ADC_SMPR2` | `0x18` | ADC sample time register 2 (ADC_SMPR2) | [ADC_SMPR2.json](../registers_json/ADC_SMPR2.json) |
| `ADC_SQR1` | `0x30` | ADC regular sequenc e register 1 (ADC_SQR1) | [ADC_SQR1.json](../registers_json/ADC_SQR1.json) |
| `ADC_SQR2` | `0x34` | ADC regular sequenc e register 2 (ADC_SQR2) | [ADC_SQR2.json](../registers_json/ADC_SQR2.json) |
| `ADC_SQR3` | `0x38` | ADC regular sequenc e register 3 (ADC_SQR3) | [ADC_SQR3.json](../registers_json/ADC_SQR3.json) |
| `ADC_SQR4` | `0x3C` | ADC regular sequenc e register 4 (ADC_SQR4) | [ADC_SQR4.json](../registers_json/ADC_SQR4.json) |
| `ADC_TR1` | `0x20` | ADC watchdog threshol d register 1 (ADC_TR1) | [ADC_TR1.json](../registers_json/ADC_TR1.json) |
| `ADC_TR2` | `0x24` | ADC watchdog threshol d register 2 (ADC_TR2) | [ADC_TR2.json](../registers_json/ADC_TR2.json) |
| `ADC_TR3` | `0x28` | ADC watchdog threshol d register 3 (ADC_TR3) | [ADC_TR3.json](../registers_json/ADC_TR3.json) |