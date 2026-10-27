# Universal Synchronous Asynchronous Receiver Transmitter (USART)

## 1. Overview & Key Features
The Universal Synchronous Asynchronous Receiver Transmitter (USART) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 33](../chapters/chapter_33.md) (Pages 960 - 1013).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 33](../chapters/chapter_33.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Universal Synchronous Asynchronous Receiver Transmitter (USART) Architectural Block Diagram](../figures/usart_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Universal Synchronous Asynchronous Receiver Transmitter (USART) Configuration & Parameter Matrix](../tables/usart_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `USART_BRR` | `0x08` | Baud rate register (USART_BRR) | [USART_BRR.json](../registers_json/USART_BRR.json) |
| `USART_CR1` | `0x0C` | Control register 1 (USART_CR1) | [USART_CR1.json](../registers_json/USART_CR1.json) |
| `USART_CR2` | `0x10` | Control register 2 (USART_CR2) | [USART_CR2.json](../registers_json/USART_CR2.json) |
| `USART_CR3` | `0x14` | Control register 3 (USART_CR3) | [USART_CR3.json](../registers_json/USART_CR3.json) |
| `USART_DR` | `0x04` | Data register (USART_DR) | [USART_DR.json](../registers_json/USART_DR.json) |
| `USART_GTPR` | `0x18` | Guard time and prescal er register (USART_GTPR) | [USART_GTPR.json](../registers_json/USART_GTPR.json) |
| `USART_SR` | `0x00` | Status register (USART_SR) | [USART_SR.json](../registers_json/USART_SR.json) |