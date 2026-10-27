# Serial Peripheral Interface (SPI)

## 1. Overview & Key Features
The Serial Peripheral Interface (SPI) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 31](../chapters/chapter_31.md) (Pages 868 - 920).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 31](../chapters/chapter_31.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Serial Peripheral Interface (SPI) Architectural Block Diagram](../figures/spi_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Serial Peripheral Interface (SPI) Configuration & Parameter Matrix](../tables/spi_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `SPI_CR1` | `0x00` | Serial Peripheral Interface (SPI) SPI_CR1 Register | [SPI_CR1.json](../registers_json/SPI_CR1.json) |
| `SPI_CR2` | `0x04` | Serial Peripheral Interface (SPI) SPI_CR2 Register | [SPI_CR2.json](../registers_json/SPI_CR2.json) |
| `SPI_CRCPR` | `0x10` | Serial Peripheral Interface (SPI) SPI_CRCPR Register | [SPI_CRCPR.json](../registers_json/SPI_CRCPR.json) |
| `SPI_DR` | `0x0C` | SPI data register (SPI_DR) | [SPI_DR.json](../registers_json/SPI_DR.json) |
| `SPI_I2SCFGR` | `0x1C` | SPI_I 2S configuration register (SPI_I2SCFGR) | [SPI_I2SCFGR.json](../registers_json/SPI_I2SCFGR.json) |
| `SPI_I2SPR` | `0x20` | SPI_I 2S prescaler register (SPI_I2SPR) | [SPI_I2SPR.json](../registers_json/SPI_I2SPR.json) |
| `SPI_RXCRCR` | `0x14` | Serial Peripheral Interface (SPI) SPI_RXCRCR Register | [SPI_RXCRCR.json](../registers_json/SPI_RXCRCR.json) |
| `SPI_SR` | `0x08` | SPI status register (SPI_SR) | [SPI_SR.json](../registers_json/SPI_SR.json) |
| `SPI_TXCRCR` | `0x18` | Serial Peripheral Interface (SPI) SPI_TXCRCR Register | [SPI_TXCRCR.json](../registers_json/SPI_TXCRCR.json) |