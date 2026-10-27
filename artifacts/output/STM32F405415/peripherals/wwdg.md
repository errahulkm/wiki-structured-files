# Window Watchdog (WWDG)

## 1. Overview & Key Features
The Window Watchdog (WWDG) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 25](../chapters/chapter_25.md) (Pages 709 - 715).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 25](../chapters/chapter_25.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Window Watchdog (WWDG) Architectural Block Diagram](../figures/wwdg_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Window Watchdog (WWDG) Configuration & Parameter Matrix](../tables/wwdg_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `WWDG_CFR` | `0x04` | Configuration register (WWDG_CFR) | [WWDG_CFR.json](../registers_json/WWDG_CFR.json) |
| `WWDG_CR` | `0x00` | Control register (WWDG_CR) | [WWDG_CR.json](../registers_json/WWDG_CR.json) |
| `WWDG_SR` | `0x08` | Status register (WWDG_SR) | [WWDG_SR.json](../registers_json/WWDG_SR.json) |