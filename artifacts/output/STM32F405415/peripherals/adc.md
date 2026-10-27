# Analog-to-Digital Converter (ADC)

## 1. Overview & Key Features
The Analog-to-Digital Converter (ADC) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 16](../chapters/chapter_16.md) (Pages 390 - 434).

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
| `ADC_CCR` | `0x04` | ADC common contro l register (ADC_CCR) | [ADC_CCR.json](../registers_json/ADC_CCR.json) |
| `ADC_CDR` | `0x08` | ADC common regular data register for dual and triple modes (ADC_CDR) | [ADC_CDR.json](../registers_json/ADC_CDR.json) |
| `ADC_CR1` | `0x04` | Analog-to-Digital Converter (ADC) ADC_CR1 Register | [ADC_CR1.json](../registers_json/ADC_CR1.json) |
| `ADC_CR2` | `0x08` | Analog-to-Digital Converter (ADC) ADC_CR2 Register | [ADC_CR2.json](../registers_json/ADC_CR2.json) |
| `ADC_CSR` | `0x00` | ADC Common status register (ADC_CSR) | [ADC_CSR.json](../registers_json/ADC_CSR.json) |
| `ADC_DR` | `0x4C` | ADC regular da ta register (ADC_DR) | [ADC_DR.json](../registers_json/ADC_DR.json) |
| `ADC_HTR` | `0x24` | ADC watchdog higher thr eshold register (ADC_HTR) | [ADC_HTR.json](../registers_json/ADC_HTR.json) |
| `ADC_JDR1` | `0x3C` | Analog-to-Digital Converter (ADC) ADC_JDR1 Register | [ADC_JDR1.json](../registers_json/ADC_JDR1.json) |
| `ADC_JDR2` | `0x40` | Analog-to-Digital Converter (ADC) ADC_JDR2 Register | [ADC_JDR2.json](../registers_json/ADC_JDR2.json) |
| `ADC_JDR3` | `0x44` | Analog-to-Digital Converter (ADC) ADC_JDR3 Register | [ADC_JDR3.json](../registers_json/ADC_JDR3.json) |
| `ADC_JDR4` | `0x48` | Analog-to-Digital Converter (ADC) ADC_JDR4 Register | [ADC_JDR4.json](../registers_json/ADC_JDR4.json) |
| `ADC_JOFR1` | `0x14` | Analog-to-Digital Converter (ADC) ADC_JOFR1 Register | [ADC_JOFR1.json](../registers_json/ADC_JOFR1.json) |
| `ADC_JOFR2` | `0x18` | Analog-to-Digital Converter (ADC) ADC_JOFR2 Register | [ADC_JOFR2.json](../registers_json/ADC_JOFR2.json) |
| `ADC_JOFR3` | `0x1C` | Analog-to-Digital Converter (ADC) ADC_JOFR3 Register | [ADC_JOFR3.json](../registers_json/ADC_JOFR3.json) |
| `ADC_JOFR4` | `0x20` | Analog-to-Digital Converter (ADC) ADC_JOFR4 Register | [ADC_JOFR4.json](../registers_json/ADC_JOFR4.json) |
| `ADC_JSQR` | `0x38` | ADC injected seque nce register (ADC_JSQR) | [ADC_JSQR.json](../registers_json/ADC_JSQR.json) |
| `ADC_LTR` | `0x28` | ADC watchdog lower thr eshold register (ADC_LTR) | [ADC_LTR.json](../registers_json/ADC_LTR.json) |
| `ADC_SMPR1` | `0x0C` | ADC sample time register 1 (ADC_SMPR1) | [ADC_SMPR1.json](../registers_json/ADC_SMPR1.json) |
| `ADC_SMPR2` | `0x10` | ADC sample time register 2 (ADC_SMPR2) | [ADC_SMPR2.json](../registers_json/ADC_SMPR2.json) |
| `ADC_SQR1` | `0x2C` | ADC regular sequenc e register 1 (ADC_SQR1) | [ADC_SQR1.json](../registers_json/ADC_SQR1.json) |
| `ADC_SQR2` | `0x30` | ADC regular sequenc e register 2 (ADC_SQR2) | [ADC_SQR2.json](../registers_json/ADC_SQR2.json) |
| `ADC_SQR3` | `0x34` | ADC regular sequenc e register 3 (ADC_SQR3) | [ADC_SQR3.json](../registers_json/ADC_SQR3.json) |
| `ADC_SR` | `0x00` | ADC status register (ADC_SR) | [ADC_SR.json](../registers_json/ADC_SR.json) |