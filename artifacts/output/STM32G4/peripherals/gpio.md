# General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs)

## 1. Overview & Key Features
The General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 9](../chapters/chapter_09.md) (Pages 345 - 363).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 9](../chapters/chapter_09.md)
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
| `GPIO` | `0x28` | Push-pull or Open-drain Output control VDDIOx VSS TTL Schmitt trigger on Input driver Output driver P-MOS N-MOS Input data register Output data registerRead/write Read Bit set/reset registers Write on/off pull pull on/off VDDIOx VSS VSS VDDIOx protection diode protection diodedown up I/O pin MS31478V1 MSv34756V1 Alternate function output Alternate function input push-pull or open-drainFrom on-chip peripheral To on-chip peripheral Output control VDD VSS TTL Schmitt trigger on Input driver Output driver P-MOS N-MOS Input data register Output data registerRead/write Read Bit set/reset registers Write on/off on/off VDDIOx VSS VSS protection diode protection diode Pull Pull I/O pin down up VDDIOx RM0440 Rev 9 353/2140 RM0440 General-purpose I/Os (GPIO) | [GPIO.json](../registers_json/GPIO.json) |
| `GPIOA_MODER` | `0x00` | General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) GPIOA_MODER Register | [GPIOA_MODER.json](../registers_json/GPIOA_MODER.json) |
| `GPIOA_OSPEEDR` | `0x08` | General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) GPIOA_OSPEEDR Register | [GPIOA_OSPEEDR.json](../registers_json/GPIOA_OSPEEDR.json) |
| `GPIOA_PUPDR` | `0x0C` | General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) GPIOA_PUPDR Register | [GPIOA_PUPDR.json](../registers_json/GPIOA_PUPDR.json) |
| `GPIOB_MODER` | `0x00` | General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) GPIOB_MODER Register | [GPIOB_MODER.json](../registers_json/GPIOB_MODER.json) |
| `GPIOB_PUPDR` | `0x0C` | General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) GPIOB_PUPDR Register | [GPIOB_PUPDR.json](../registers_json/GPIOB_PUPDR.json) |
| `GPIOX_AFRH` | `0x00` | GPIO alternate functi on high register (GPIOX_AFRH) | [GPIOX_AFRH.json](../registers_json/GPIOX_AFRH.json) |
| `GPIOX_AFRL` | `0x00` | GPIO alternate function low register (GPIOX_AFRL) | [GPIOX_AFRL.json](../registers_json/GPIOX_AFRL.json) |
| `GPIOX_BSRR` | `0x00` | GPIO port bit set/re set register (GPIOX_BSRR) | [GPIOX_BSRR.json](../registers_json/GPIOX_BSRR.json) |
| `GPIOX_IDR` | `0x00` | GPIO port input data register (GPIOX_IDR) | [GPIOX_IDR.json](../registers_json/GPIOX_IDR.json) |
| `GPIOX_LCKR` | `0x00` | GPIO port c onfiguration lock register (GPIOX_LCKR) | [GPIOX_LCKR.json](../registers_json/GPIOX_LCKR.json) |
| `GPIOX_MODER` | `0x00` | GPIO port mode register (GPIOX_MODER) | [GPIOX_MODER.json](../registers_json/GPIOX_MODER.json) |
| `GPIOX_ODR` | `0x00` | GPIO port output da ta register (GPIOX_ODR) | [GPIOX_ODR.json](../registers_json/GPIOX_ODR.json) |
| `GPIOX_OSPEEDR` | `0x00` | GPIO port output sp eed register (GPIOX_OSPEEDR) | [GPIOX_OSPEEDR.json](../registers_json/GPIOX_OSPEEDR.json) |
| `GPIOX_OTYPER` | `0x00` | GPIO port output ty pe register (GPIOX_OTYPER) | [GPIOX_OTYPER.json](../registers_json/GPIOX_OTYPER.json) |
| `GPIOX_PUPDR` | `0x00` | GPIO port pull-up/pull -down register (GPIOX_PUPDR) | [GPIOX_PUPDR.json](../registers_json/GPIOX_PUPDR.json) |