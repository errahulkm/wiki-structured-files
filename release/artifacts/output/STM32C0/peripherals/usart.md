# Universal Synchronous Asynchronous Receiver Transmitter (USART)

## 1. Overview & Key Features
The Universal Synchronous Asynchronous Receiver Transmitter (USART) block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 26](../chapters/chapter_26.md) (Pages 743 - 829).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 26](../chapters/chapter_26.md)
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
| `USART_BRR` | `0x0C` | USART baud rate register (USART_BRR) | [USART_BRR.json](../registers_json/USART_BRR.json) |
| `USART_CR1` | `0x00` | Universal Synchronous Asynchronous Receiver Transmitter (USART) USART_CR1 Register | [USART_CR1.json](../registers_json/USART_CR1.json) |
| `USART_CR2` | `0x04` | USART control register 2 (USART_CR2) | [USART_CR2.json](../registers_json/USART_CR2.json) |
| `USART_CR3` | `0x08` | USART control register 3 (USART_CR3) | [USART_CR3.json](../registers_json/USART_CR3.json) |
| `USART_GTPR` | `0x10` | USART guard time and pr escaler register (USART_GTPR) | [USART_GTPR.json](../registers_json/USART_GTPR.json) |
| `USART_ICR` | `0x20` | USART interrupt flag clear register (USART_ICR) | [USART_ICR.json](../registers_json/USART_ICR.json) |
| `USART_ISR` | `0x1C` | USART interrupt and st atus register (USART_ISR) | [USART_ISR.json](../registers_json/USART_ISR.json) |
| `USART_PRESC` | `0x00` | USART prescaler re gister (USART_PRESC) | [USART_PRESC.json](../registers_json/USART_PRESC.json) |
| `USART_RDR` | `0x24` | USART receive data register (USART_RDR) | [USART_RDR.json](../registers_json/USART_RDR.json) |
| `USART_RQR` | `0x18` | USART request re gister (USART_RQR) | [USART_RQR.json](../registers_json/USART_RQR.json) |
| `USART_RTOR` | `0x14` | USART receiver timeout register (USART_RTOR) | [USART_RTOR.json](../registers_json/USART_RTOR.json) |
| `USART_TDR` | `0x28` | USART transmit data register (USART_TDR) | [USART_TDR.json](../registers_json/USART_TDR.json) |