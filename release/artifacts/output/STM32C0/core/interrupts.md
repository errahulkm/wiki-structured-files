# Interrupts and Events (NVIC/EXTI)

## 1. Overview & Key Features
The Interrupts and Events (NVIC/EXTI) block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 13](../chapters/chapter_13.md), [Chapter 14](../chapters/chapter_14.md) (Pages 259 - 261).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: CORE
* **Reference Chapter**: [Chapter 13](../chapters/chapter_13.md), [Chapter 14](../chapters/chapter_14.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Interrupts and Events (NVIC/EXTI) Architectural Block Diagram](../figures/interrupts_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Interrupts and Events (NVIC/EXTI) Configuration & Parameter Matrix](../tables/interrupts_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `INTERRUPTS_CR` | `0x00` | Interrupts and Events (NVIC/EXTI) Control Register | [INTERRUPTS_CR.json](../registers_json/INTERRUPTS_CR.json) |
| `INTERRUPTS_SR` | `0x04` | Interrupts and Events (NVIC/EXTI) Status Register | [INTERRUPTS_SR.json](../registers_json/INTERRUPTS_SR.json) |
| `INTERRUPTS_DR` | `0x08` | Interrupts and Events (NVIC/EXTI) Data Register | [INTERRUPTS_DR.json](../registers_json/INTERRUPTS_DR.json) |