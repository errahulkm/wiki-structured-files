# Hash Processor (HASH)

## 1. Overview & Key Features
The Hash Processor (HASH) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 28](../chapters/chapter_28.md) (Pages 768 - 793).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SECURITY
* **Reference Chapter**: [Chapter 28](../chapters/chapter_28.md)
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
| `HASH_CR` | `0x00` | Hash Processor (HASH) HASH_CR Register | [HASH_CR.json](../registers_json/HASH_CR.json) |
| `HASH_CSR0` | `0xF8` | Hash Processor (HASH) HASH_CSR0 Register | [HASH_CSR0.json](../registers_json/HASH_CSR0.json) |
| `HASH_CSR50` | `0x1C0` | Hash Processor (HASH) HASH_CSR50 Register | [HASH_CSR50.json](../registers_json/HASH_CSR50.json) |
| `HASH_CSR53` | `0x1CC` | Hash Processor (HASH) HASH_CSR53 Register | [HASH_CSR53.json](../registers_json/HASH_CSR53.json) |
| `HASH_CSRX` | `0x0F8` | HASH context swap registers (HASH_CSRX) | [HASH_CSRX.json](../registers_json/HASH_CSRX.json) |
| `HASH_DIN` | `0x04` | HASH data input register (HASH_DIN) | [HASH_DIN.json](../registers_json/HASH_DIN.json) |
| `HASH_HR0` | `0x310` | Hash Processor (HASH) HASH_HR0 Register | [HASH_HR0.json](../registers_json/HASH_HR0.json) |
| `HASH_HR1` | `0x314` | Hash Processor (HASH) HASH_HR1 Register | [HASH_HR1.json](../registers_json/HASH_HR1.json) |
| `HASH_HR2` | `0x318` | Hash Processor (HASH) HASH_HR2 Register | [HASH_HR2.json](../registers_json/HASH_HR2.json) |
| `HASH_HR3` | `0x31C` | Hash Processor (HASH) HASH_HR3 Register | [HASH_HR3.json](../registers_json/HASH_HR3.json) |
| `HASH_HR4` | `0x320` | Hash Processor (HASH) HASH_HR4 Register | [HASH_HR4.json](../registers_json/HASH_HR4.json) |
| `HASH_HR5` | `0x324` | Hash Processor (HASH) HASH_HR5 Register | [HASH_HR5.json](../registers_json/HASH_HR5.json) |
| `HASH_HR6` | `0x328` | Hash Processor (HASH) HASH_HR6 Register | [HASH_HR6.json](../registers_json/HASH_HR6.json) |
| `HASH_HR7` | `0x32C` | Hash Processor (HASH) HASH_HR7 Register | [HASH_HR7.json](../registers_json/HASH_HR7.json) |
| `HASH_IMR` | `0x20` | HASH interrupt enable register (HASH_IMR) | [HASH_IMR.json](../registers_json/HASH_IMR.json) |
| `HASH_SR` | `0x24` | HASH status register (HASH_SR) | [HASH_SR.json](../registers_json/HASH_SR.json) |
| `HASH_STR` | `0x08` | Hash Processor (HASH) HASH_STR Register | [HASH_STR.json](../registers_json/HASH_STR.json) |