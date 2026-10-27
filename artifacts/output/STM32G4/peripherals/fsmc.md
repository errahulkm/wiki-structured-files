# Flexible Static Memory Controller (FSMC)

## 1. Overview & Key Features
The Flexible Static Memory Controller (FSMC) block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 19](../chapters/chapter_19.md) (Pages 507 - 562).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 19](../chapters/chapter_19.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Flexible Static Memory Controller (FSMC) Architectural Block Diagram](../figures/fsmc_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Flexible Static Memory Controller (FSMC) Configuration & Parameter Matrix](../tables/fsmc_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `FSMC` | `0x00` | FMC interrupts to NVIC From clock controller NOR/PSRAM memory controller Configuration registers NAND memory controller HCLK FMC_NWAIT NAND signals NOR / PSRAM / SRAM shared signals Shared signals NOR / PSRAM / SRAM shared signals RM0440 Rev 9 509/2140 RM0440 Flexible static me mory controller (FSMC) | [FSMC.json](../registers_json/FSMC.json) |