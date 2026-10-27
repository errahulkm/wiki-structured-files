# General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs)

## 1. Overview & Key Features
The General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 8](../chapters/chapter_08.md) (Pages 178 - 195).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 8](../chapters/chapter_08.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) Architectural Block Diagram](../figures/gpio_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) Configuration & Parameter Matrix](../tables/gpio_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `GPIOX_AFRH` | `0x24` | GPIO alternate functi on high register (GPIOX_AFRH) | [GPIOX_AFRH.json](../registers_json/GPIOX_AFRH.json) |
| `GPIOX_AFRL` | `0x20` | GPIO alternate function low register (GPIOX_AFRL) | [GPIOX_AFRL.json](../registers_json/GPIOX_AFRL.json) |
| `GPIOX_BRR` | `0x28` | GPIO port bit r eset register (GPIOX_BRR) | [GPIOX_BRR.json](../registers_json/GPIOX_BRR.json) |
| `GPIOX_BSRR` | `0x18` | GPIO port bit set/re set register (GPIOX_BSRR) | [GPIOX_BSRR.json](../registers_json/GPIOX_BSRR.json) |
| `GPIOX_IDR` | `0x10` | GPIO port input data register (GPIOX_IDR) | [GPIOX_IDR.json](../registers_json/GPIOX_IDR.json) |
| `GPIOX_LCKR` | `0x1C` | GPIO port c onfiguration lock register (GPIOX_LCKR) | [GPIOX_LCKR.json](../registers_json/GPIOX_LCKR.json) |
| `GPIOX_MODER` | `0x00` | GPIO port mode register (GPIOX_MODER) | [GPIOX_MODER.json](../registers_json/GPIOX_MODER.json) |
| `GPIOX_ODR` | `0x14` | GPIO port output da ta register (GPIOX_ODR) | [GPIOX_ODR.json](../registers_json/GPIOX_ODR.json) |
| `GPIOX_OSPEEDR` | `0x08` | GPIO port output sp eed register (GPIOX_OSPEEDR) | [GPIOX_OSPEEDR.json](../registers_json/GPIOX_OSPEEDR.json) |
| `GPIOX_OSPEEDRANDGPIOX_PUPDR` | `0x00` | Introduction Each general-purpose I/O port has four 32-bit configuration registers (GPIOX_OSPEEDRANDGPIOX_PUPDR) | [GPIOX_OSPEEDRANDGPIOX_PUPDR.json](../registers_json/GPIOX_OSPEEDRANDGPIOX_PUPDR.json) |
| `GPIOX_OTYPER` | `0x04` | GPIO port output ty pe register (GPIOX_OTYPER) | [GPIOX_OTYPER.json](../registers_json/GPIOX_OTYPER.json) |
| `GPIOX_PUPDR` | `0x0C` | GPIO port pull-up/pull -down register (GPIOX_PUPDR) | [GPIOX_PUPDR.json](../registers_json/GPIOX_PUPDR.json) |