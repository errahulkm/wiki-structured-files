# Serial Peripheral Interface (SPI)

## 1. Overview & Key Features
The Serial Peripheral Interface (SPI) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 20](../chapters/chapter_20.md), [Chapter 46](../chapters/chapter_46.md) (Pages 626 - 682).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 20](../chapters/chapter_20.md), [Chapter 46](../chapters/chapter_46.md)
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
| `SPI` | `0x18` | Serial Peripheral Interface (SPI) SPI Register | [SPI.json](../registers_json/SPI.json) |
| `SPIX_CRCPR` | `0x10` | SPI CRC polynomial register (SPIX_CRCPR) | [SPIX_CRCPR.json](../registers_json/SPIX_CRCPR.json) |
| `SPIX_DR` | `0x0C` | SPI data register (SPIX_DR) | [SPIX_DR.json](../registers_json/SPIX_DR.json) |
| `SPIX_RXCRCR` | `0x14` | SPI Rx CRC regi ster (SPIX_RXCRCR) | [SPIX_RXCRCR.json](../registers_json/SPIX_RXCRCR.json) |
| `SPIX_SR` | `0x08` | SPI status register (SPIX_SR) | [SPIX_SR.json](../registers_json/SPIX_SR.json) |