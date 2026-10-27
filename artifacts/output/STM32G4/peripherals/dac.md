# Digital-to-Analog Converter (DAC)

## 1. Overview & Key Features
The Digital-to-Analog Converter (DAC) block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 22](../chapters/chapter_22.md) (Pages 714 - 763).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 22](../chapters/chapter_22.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Digital-to-Analog Converter (DAC) Architectural Block Diagram](../figures/dac_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Digital-to-Analog Converter (DAC) Configuration & Parameter Matrix](../tables/dac_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `DAC` | `0x00` | Offset Register name reset value 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0440 Rev 9 763/2140 RM0440 Digital-to-analog converter (DAC) | [DAC.json](../registers_json/DAC.json) |
| `DAC2` | `0xDAC1` | Digital-to-Analog Converter (DAC) DAC2 Register | [DAC2.json](../registers_json/DAC2.json) |
| `DAC4` | `0xDAC3` | Digital-to-Analog Converter (DAC) DAC4 Register | [DAC4.json](../registers_json/DAC4.json) |
| `DAC_` | `0x60` | Digital-to-Analog Converter (DAC) DAC_ Register | [DAC_.json](../registers_json/DAC_.json) |
| `DAC_CCR` | `0x38` | DAC calibration c ontrol register (DAC_CCR) | [DAC_CCR.json](../registers_json/DAC_CCR.json) |
| `DAC_CR` | `0x00` | DAC control register (DAC_CR) | [DAC_CR.json](../registers_json/DAC_CR.json) |
| `DAC_DHR12L1` | `0x0C` | DAC channel1 12-bit left aligned data holding register (DAC_DHR12L1) | [DAC_DHR12L1.json](../registers_json/DAC_DHR12L1.json) |
| `DAC_DHR12L2` | `0x00` | DAC channel2 12-bit left aligned data holding register (DAC_DHR12L2) | [DAC_DHR12L2.json](../registers_json/DAC_DHR12L2.json) |
| `DAC_DHR12LD` | `0x24` | Dual DAC 12-bit left al igned data holding register (DAC_DHR12LD) | [DAC_DHR12LD.json](../registers_json/DAC_DHR12LD.json) |
| `DAC_DHR12R1` | `0x08` | DAC channel1 12-bit righ t-aligned data holding register (DAC_DHR12R1) | [DAC_DHR12R1.json](../registers_json/DAC_DHR12R1.json) |
| `DAC_DHR12R2` | `0x00` | DAC channel2 12-bit righ t aligned data holding register (DAC_DHR12R2) | [DAC_DHR12R2.json](../registers_json/DAC_DHR12R2.json) |
| `DAC_DHR12RD` | `0x20` | Dual DAC 12-bit right-ali gned data holding register (DAC_DHR12RD) | [DAC_DHR12RD.json](../registers_json/DAC_DHR12RD.json) |
| `DAC_DHR8R1` | `0x10` | DAC channel1 8-bit right aligned data holding register (DAC_DHR8R1) | [DAC_DHR8R1.json](../registers_json/DAC_DHR8R1.json) |
| `DAC_DHR8R2` | `0x00` | DAC channel2 8-bit right- aligned data holding register (DAC_DHR8R2) | [DAC_DHR8R2.json](../registers_json/DAC_DHR8R2.json) |
| `DAC_DHR8RD` | `0x28` | Dual DAC 8-bit right al igned data holding register (DAC_DHR8RD) | [DAC_DHR8RD.json](../registers_json/DAC_DHR8RD.json) |
| `DAC_DOR1` | `0x2C` | DAC channel1 data output register (DAC_DOR1) | [DAC_DOR1.json](../registers_json/DAC_DOR1.json) |
| `DAC_DOR2` | `0x00` | DAC channel2 data output register (DAC_DOR2) | [DAC_DOR2.json](../registers_json/DAC_DOR2.json) |
| `DAC_MCR` | `0x3C` | DAC mode cont rol register (DAC_MCR) | [DAC_MCR.json](../registers_json/DAC_MCR.json) |
| `DAC_SHHR` | `0x48` | DAC sample and hold time register (DAC_SHHR) | [DAC_SHHR.json](../registers_json/DAC_SHHR.json) |
| `DAC_SHRR` | `0x4C` | DAC sample and hold refr esh time register (DAC_SHRR) | [DAC_SHRR.json](../registers_json/DAC_SHRR.json) |
| `DAC_SHSR1` | `0x40` | DAC channel1 sample and hold sample time register (DAC_SHSR1) | [DAC_SHSR1.json](../registers_json/DAC_SHSR1.json) |
| `DAC_SHSR2` | `0x00` | DAC channel2 sample a nd hold sample time register (DAC_SHSR2) | [DAC_SHSR2.json](../registers_json/DAC_SHSR2.json) |
| `DAC_SR` | `0x34` | DAC status register (DAC_SR) | [DAC_SR.json](../registers_json/DAC_SR.json) |
| `DAC_STMODR` | `0x60` | DAC sawtooth mode register (DAC_STMODR) | [DAC_STMODR.json](../registers_json/DAC_STMODR.json) |
| `DAC_STR` | `0x5C` | Digital-to-Analog Converter (DAC) DAC_STR Register | [DAC_STR.json](../registers_json/DAC_STR.json) |
| `DAC_STR1` | `0x58` | DAC channel1 sawt ooth register (DAC_STR1) | [DAC_STR1.json](../registers_json/DAC_STR1.json) |
| `DAC_STR2` | `0x00` | DAC channel2 sawt ooth register (DAC_STR2) | [DAC_STR2.json](../registers_json/DAC_STR2.json) |
| `DAC_SWTRGR` | `0x04` | DAC software trigge r register (DAC_SWTRGR) | [DAC_SWTRGR.json](../registers_json/DAC_SWTRGR.json) |