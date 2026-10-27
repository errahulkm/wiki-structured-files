# Operational Amplifier (OPAMP)

## 1. Overview & Key Features
The Operational Amplifier (OPAMP) block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 25](../chapters/chapter_25.md) (Pages 776 - 819).

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
* [Figure: Operational Amplifier (OPAMP) Architectural Block Diagram](../figures/opamp_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Operational Amplifier (OPAMP) Configuration & Parameter Matrix](../tables/opamp_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `OPAMP1_` | `0x18` | Operational Amplifier (OPAMP) OPAMP1_ Register | [OPAMP1_.json](../registers_json/OPAMP1_.json) |
| `OPAMP1_CSR` | `0x00` | OPAMP1 control/status register (OPAMP1_CSR) | [OPAMP1_CSR.json](../registers_json/OPAMP1_CSR.json) |
| `OPAMP2_` | `0x1C` | Operational Amplifier (OPAMP) OPAMP2_ Register | [OPAMP2_.json](../registers_json/OPAMP2_.json) |
| `OPAMP2_CSR` | `0x04` | OPAMP2 control/status register (OPAMP2_CSR) | [OPAMP2_CSR.json](../registers_json/OPAMP2_CSR.json) |
| `OPAMP3_` | `0x20` | Operational Amplifier (OPAMP) OPAMP3_ Register | [OPAMP3_.json](../registers_json/OPAMP3_.json) |
| `OPAMP3_CSR` | `0x08` | OPAMP3 control/status register (OPAMP3_CSR) | [OPAMP3_CSR.json](../registers_json/OPAMP3_CSR.json) |
| `OPAMP4_` | `0x24` | Operational Amplifier (OPAMP) OPAMP4_ Register | [OPAMP4_.json](../registers_json/OPAMP4_.json) |
| `OPAMP4_CSR` | `0x0C` | OPAMP4 control/status register (OPAMP4_CSR) | [OPAMP4_CSR.json](../registers_json/OPAMP4_CSR.json) |
| `OPAMP5_` | `0x28` | Operational Amplifier (OPAMP) OPAMP5_ Register | [OPAMP5_.json](../registers_json/OPAMP5_.json) |
| `OPAMP5_CSR` | `0x10` | OPAMP5 control/status register (OPAMP5_CSR) | [OPAMP5_CSR.json](../registers_json/OPAMP5_CSR.json) |
| `OPAMP6_` | `0x2C` | Operational Amplifier (OPAMP) OPAMP6_ Register | [OPAMP6_.json](../registers_json/OPAMP6_.json) |
| `OPAMP6_CSR` | `0x14` | OPAMP6 control/status register (OPAMP6_CSR) | [OPAMP6_CSR.json](../registers_json/OPAMP6_CSR.json) |