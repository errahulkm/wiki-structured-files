# Inter-Integrated Circuit (I2C)

## 1. Overview & Key Features
The Inter-Integrated Circuit (I2C) block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 39](../chapters/chapter_39.md) (Pages 1625 - 1688).

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
* [Figure: Inter-Integrated Circuit (I2C) Architectural Block Diagram](../figures/i2c_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Inter-Integrated Circuit (I2C) Configuration & Parameter Matrix](../tables/i2c_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `I2C_` | `0x10` | Inter-Integrated Circuit (I2C) I2C_ Register | [I2C_.json](../registers_json/I2C_.json) |
| `I2C_CR1` | `0x00` | I2C control register 1 (I2C_CR1) | [I2C_CR1.json](../registers_json/I2C_CR1.json) |
| `I2C_CR2` | `0x04` | I2C control register 2 (I2C_CR2) | [I2C_CR2.json](../registers_json/I2C_CR2.json) |
| `I2C_ICR` | `0x1C` | I2C interrupt clea r register (I2C_ICR) | [I2C_ICR.json](../registers_json/I2C_ICR.json) |
| `I2C_ISR` | `0x18` | I2C interrupt and st atus register (I2C_ISR) | [I2C_ISR.json](../registers_json/I2C_ISR.json) |
| `I2C_OAR1` | `0x08` | I2C own address 1 register (I2C_OAR1) | [I2C_OAR1.json](../registers_json/I2C_OAR1.json) |
| `I2C_OAR2` | `0x0C` | I2C own address 2 register (I2C_OAR2) | [I2C_OAR2.json](../registers_json/I2C_OAR2.json) |
| `I2C_PECR` | `0x20` | I2C PEC register (I2C_PECR) | [I2C_PECR.json](../registers_json/I2C_PECR.json) |
| `I2C_RXDR` | `0x24` | I2C receive data register (I2C_RXDR) | [I2C_RXDR.json](../registers_json/I2C_RXDR.json) |
| `I2C_TIMEOUTR` | `0x14` | I2C timeout regi ster (I2C_TIMEOUTR) | [I2C_TIMEOUTR.json](../registers_json/I2C_TIMEOUTR.json) |
| `I2C_TIMINGR` | `0x10` | I2C timing register (I2C_TIMINGR) | [I2C_TIMINGR.json](../registers_json/I2C_TIMINGR.json) |
| `I2C_TXDR` | `0x28` | I2C transmit da ta register (I2C_TXDR) | [I2C_TXDR.json](../registers_json/I2C_TXDR.json) |