# Hash Processor (HASH)

## 1. Overview & Key Features
The Hash Processor (HASH) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 30](../chapters/chapter_30.md) (Pages 1001 - 1022).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SECURITY
* **Reference Chapter**: [Chapter 30](../chapters/chapter_30.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Hash Processor (HASH) Architectural Block Diagram](../figures/hash_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Hash Processor (HASH) Configuration & Parameter Matrix](../tables/hash_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `HASH` | `0x1022` | Hash Processor (HASH) HASH Register | [HASH.json](../registers_json/HASH.json) |
| `HASH_CR` | `0x00` | Hash Processor (HASH) HASH_CR Register | [HASH_CR.json](../registers_json/HASH_CR.json) |
| `HASH_CSR` | `0x1CC` | Hash Processor (HASH) HASH_CSR Register | [HASH_CSR.json](../registers_json/HASH_CSR.json) |
| `HASH_CSR0` | `0x0F8` | Hash Processor (HASH) HASH_CSR0 Register | [HASH_CSR0.json](../registers_json/HASH_CSR0.json) |
| `HASH_CSRX` | `0x0F8` | HASH context swap register x (HASH_CSRX) | [HASH_CSRX.json](../registers_json/HASH_CSRX.json) |
| `HASH_DIN` | `0x04` | HASH data input register (HASH_DIN) | [HASH_DIN.json](../registers_json/HASH_DIN.json) |
| `HASH_HR0` | `0x310` | Hash Processor (HASH) HASH_HR0 Register | [HASH_HR0.json](../registers_json/HASH_HR0.json) |
| `HASH_HR1` | `0x314` | Hash Processor (HASH) HASH_HR1 Register | [HASH_HR1.json](../registers_json/HASH_HR1.json) |
| `HASH_HR2` | `0x318` | Hash Processor (HASH) HASH_HR2 Register | [HASH_HR2.json](../registers_json/HASH_HR2.json) |
| `HASH_HR3` | `0x31C` | Hash Processor (HASH) HASH_HR3 Register | [HASH_HR3.json](../registers_json/HASH_HR3.json) |
| `HASH_HR4` | `0x320` | Hash Processor (HASH) HASH_HR4 Register | [HASH_HR4.json](../registers_json/HASH_HR4.json) |
| `HASH_HR5` | `0x324` | Hash Processor (HASH) HASH_HR5 Register | [HASH_HR5.json](../registers_json/HASH_HR5.json) |
| `HASH_HR6` | `0x328` | Hash Processor (HASH) HASH_HR6 Register | [HASH_HR6.json](../registers_json/HASH_HR6.json) |
| `HASH_HR7` | `0x32C` | Hash Processor (HASH) HASH_HR7 Register | [HASH_HR7.json](../registers_json/HASH_HR7.json) |
| `HASH_HRA0` | `0x0C` | Hash Processor (HASH) HASH_HRA0 Register | [HASH_HRA0.json](../registers_json/HASH_HRA0.json) |
| `HASH_HRA1` | `0x10` | Hash Processor (HASH) HASH_HRA1 Register | [HASH_HRA1.json](../registers_json/HASH_HRA1.json) |
| `HASH_HRA2` | `0x14` | Hash Processor (HASH) HASH_HRA2 Register | [HASH_HRA2.json](../registers_json/HASH_HRA2.json) |
| `HASH_HRA3` | `0x18` | Hash Processor (HASH) HASH_HRA3 Register | [HASH_HRA3.json](../registers_json/HASH_HRA3.json) |
| `HASH_HRA4` | `0x1C` | Hash Processor (HASH) HASH_HRA4 Register | [HASH_HRA4.json](../registers_json/HASH_HRA4.json) |
| `HASH_HRAX` | `0x0C` | HASH aliased digest register x (HASH_HRAX) | [HASH_HRAX.json](../registers_json/HASH_HRAX.json) |
| `HASH_HRX` | `0x310` | HASH supplementary digest register x (HASH_HRX) | [HASH_HRX.json](../registers_json/HASH_HRX.json) |
| `HASH_IMR` | `0x20` | HASH interrupt enable register (HASH_IMR) | [HASH_IMR.json](../registers_json/HASH_IMR.json) |
| `HASH_SR` | `0x24` | HASH status register (HASH_SR) | [HASH_SR.json](../registers_json/HASH_SR.json) |
| `HASH_STR` | `0x08` | Hash Processor (HASH) HASH_STR Register | [HASH_STR.json](../registers_json/HASH_STR.json) |