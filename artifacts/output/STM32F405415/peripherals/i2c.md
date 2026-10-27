# Inter-Integrated Circuit (I2C)

## 1. Overview & Key Features
The Inter-Integrated Circuit (I2C) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 30](../chapters/chapter_30.md) (Pages 835 - 867).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 30](../chapters/chapter_30.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Inter-Integrated Circuit (I2C) Architectural Block Diagram](../figures/i2c_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Inter-Integrated Circuit (I2C) Configuration & Parameter Matrix](../tables/i2c_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `I2C_CCR` | `0x1C` | I 2C Clock control register (I2C_CCR) | [I2C_CCR.json](../registers_json/I2C_CCR.json) |
| `I2C_CR1` | `0x00` | I 2C Control register 1 (I2C_CR1) | [I2C_CR1.json](../registers_json/I2C_CR1.json) |
| `I2C_CR2` | `0x04` | I 2C Control register 2 (I2C_CR2) | [I2C_CR2.json](../registers_json/I2C_CR2.json) |
| `I2C_DR` | `0x10` | I 2C Data register (I2C_DR) | [I2C_DR.json](../registers_json/I2C_DR.json) |
| `I2C_FLTR` | `0x24` | I 2C FLTR register (I2C_FLTR) | [I2C_FLTR.json](../registers_json/I2C_FLTR.json) |
| `I2C_OAR1` | `0x08` | I 2C Own address register 1 (I2C_OAR1) | [I2C_OAR1.json](../registers_json/I2C_OAR1.json) |
| `I2C_OAR2` | `0x0C` | I 2C Own address register 2 (I2C_OAR2) | [I2C_OAR2.json](../registers_json/I2C_OAR2.json) |
| `I2C_SR1` | `0x14` | I 2C Status register 1 (I2C_SR1) | [I2C_SR1.json](../registers_json/I2C_SR1.json) |
| `I2C_SR2` | `0x18` | I 2C Status register 2 (I2C_SR2) | [I2C_SR2.json](../registers_json/I2C_SR2.json) |
| `I2C_TRISE` | `0x20` | I 2C TRISE register (I2C_TRISE) | [I2C_TRISE.json](../registers_json/I2C_TRISE.json) |