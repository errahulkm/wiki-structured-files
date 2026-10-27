# Serial Peripheral Interface (SPI)

## 1. Overview & Key Features
The Serial Peripheral Interface (SPI) block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 20](../chapters/chapter_20.md), [Chapter 42](../chapters/chapter_42.md) (Pages 563 - 590).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 20](../chapters/chapter_20.md), [Chapter 42](../chapters/chapter_42.md)
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
| `I2S` | `0x00` | 0x76A3 Only one access to the SPIx-DR register MS19598V1 MS30106V1 CK WS short frame SD WS long frame 13-bits MSB LSB MSB RM0440 Rev 9 1863/2140 RM0440 Serial peripheral interface / integrated interchip sound (I2S) | [I2S.json](../registers_json/I2S.json) |
| `SPI` | `0x20` | 0x76A3 Only one access to the SPIx-DR register MS19598V1 MS30106V1 CK WS short frame SD WS long frame 13-bits MSB LSB MSB RM0440 Rev 9 1863/2140 RM0440 Serial peripheral interface / integrated interchip sound (SPI) | [SPI.json](../registers_json/SPI.json) |
| `SPIX_CRCPR` | `0x10` | SPI CRC polynomial register (SPIX_CRCPR) | [SPIX_CRCPR.json](../registers_json/SPIX_CRCPR.json) |
| `SPIX_DR` | `0x0C` | SPI data register (SPIX_DR) | [SPIX_DR.json](../registers_json/SPIX_DR.json) |
| `SPIX_I2SCFGR` | `0x1C` | SPIx_I2S configurati on register (SPIX_I2SCFGR) | [SPIX_I2SCFGR.json](../registers_json/SPIX_I2SCFGR.json) |
| `SPIX_I2SPR` | `0x20` | SPIx_I2S prescaler register (SPIX_I2SPR) | [SPIX_I2SPR.json](../registers_json/SPIX_I2SPR.json) |
| `SPIX_RXCRCR` | `0x14` | SPI Rx CRC regi ster (SPIX_RXCRCR) | [SPIX_RXCRCR.json](../registers_json/SPIX_RXCRCR.json) |
| `SPIX_SR` | `0x08` | SPI status register (SPIX_SR) | [SPIX_SR.json](../registers_json/SPIX_SR.json) |