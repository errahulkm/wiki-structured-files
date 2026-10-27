# Operational Amplifier (OPAMP)

## 1. Overview & Key Features
The Operational Amplifier (OPAMP) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 25](../chapters/chapter_25.md) (Pages 849 - 861).

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
| `OPAMP1_` | `0x08` | Operational Amplifier (OPAMP) OPAMP1_ Register | [OPAMP1_.json](../registers_json/OPAMP1_.json) |
| `OPAMP1_CSR` | `0x00` | OPAMP1 control/status register (OPAMP1_CSR) | [OPAMP1_CSR.json](../registers_json/OPAMP1_CSR.json) |
| `OPAMP1_LPOTR` | `0x08` | OPAMP1 offset trimming register in low-power mode (OPAMP1_LPOTR) | [OPAMP1_LPOTR.json](../registers_json/OPAMP1_LPOTR.json) |
| `OPAMP1_OTR` | `0x04` | OPAMP1 offset trimming regi ster in normal mode (OPAMP1_OTR) | [OPAMP1_OTR.json](../registers_json/OPAMP1_OTR.json) |
| `OPAMP2_CRS` | `0x10` | OPAMP2 control/status register (OPAMP2_CRS) | [OPAMP2_CRS.json](../registers_json/OPAMP2_CRS.json) |
| `OPAMP2_CSR` | `0x10` | Operational Amplifier (OPAMP) OPAMP2_CSR Register | [OPAMP2_CSR.json](../registers_json/OPAMP2_CSR.json) |
| `OPAMP2_LPO` | `0x18` | Operational Amplifier (OPAMP) OPAMP2_LPO Register | [OPAMP2_LPO.json](../registers_json/OPAMP2_LPO.json) |
| `OPAMP2_LPOTR` | `0x18` | OPAMP2 offset trimming register in low-power mode (OPAMP2_LPOTR) | [OPAMP2_LPOTR.json](../registers_json/OPAMP2_LPOTR.json) |
| `OPAMP2_OTR` | `0x14` | OPAMP2 offset trimming regi ster in normal mode (OPAMP2_OTR) | [OPAMP2_OTR.json](../registers_json/OPAMP2_OTR.json) |