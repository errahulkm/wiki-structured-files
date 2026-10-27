# General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs)

## 1. Overview & Key Features
The General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 11](../chapters/chapter_11.md) (Pages 269 - 290).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 11](../chapters/chapter_11.md)
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
| `GPIOA_PUPDR` | `0x0C` | General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) GPIOA_PUPDR Register | [GPIOA_PUPDR.json](../registers_json/GPIOA_PUPDR.json) |
| `GPIOB_PUPDR` | `0x0C` | General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) GPIOB_PUPDR Register | [GPIOB_PUPDR.json](../registers_json/GPIOB_PUPDR.json) |
| `GPIOX_AFRH` | `0x00` | GPIO alternate functi on high register (GPIOX_AFRH) | [GPIOX_AFRH.json](../registers_json/GPIOX_AFRH.json) |
| `GPIOX_LCKR` | `0x00` | GPIO port c onfiguration lock register (GPIOX_LCKR) | [GPIOX_LCKR.json](../registers_json/GPIOX_LCKR.json) |
| `GPIOX_OSPEEDR` | `0x00` | GPIO port output sp eed register (GPIOX_OSPEEDR) | [GPIOX_OSPEEDR.json](../registers_json/GPIOX_OSPEEDR.json) |
| `GPIOX_OTYPER` | `0x00` | GPIO port output type register (GPIOX_OTYPER) | [GPIOX_OTYPER.json](../registers_json/GPIOX_OTYPER.json) |
| `GPIOX_PUPDR` | `0x00` | GPIO port pull-up/pull -down register (GPIOX_PUPDR) | [GPIOX_PUPDR.json](../registers_json/GPIOX_PUPDR.json) |