# System Configuration (SYSCFG)

## 1. Overview & Key Features
The System Configuration (SYSCFG) block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 9](../chapters/chapter_09.md) (Pages 196 - 217).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SYSTEM
* **Reference Chapter**: [Chapter 9](../chapters/chapter_09.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: System Configuration (SYSCFG) Architectural Block Diagram](../figures/syscfg_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: System Configuration (SYSCFG) Configuration & Parameter Matrix](../tables/syscfg_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `SYSCFG_CFGR1` | `0x00` | SYSCFG configuration register 1 (SYSCFG_CFGR1) | [SYSCFG_CFGR1.json](../registers_json/SYSCFG_CFGR1.json) |
| `SYSCFG_CFGR2` | `0x18` | SYSCFG configuration register 2 (SYSCFG_CFGR2) | [SYSCFG_CFGR2.json](../registers_json/SYSCFG_CFGR2.json) |
| `SYSCFG_CFGR3` | `0x3C` | SYSCFG configuration register 3 (SYSCFG_CFGR3) | [SYSCFG_CFGR3.json](../registers_json/SYSCFG_CFGR3.json) |
| `SYSCFG_ITLINE0` | `0x80` | SYSCFG interrupt line 0 st atus register (SYSCFG_ITLINE0) | [SYSCFG_ITLINE0.json](../registers_json/SYSCFG_ITLINE0.json) |
| `SYSCFG_ITLINE1` | `0x84` | SYSCFG interrupt line 1 st atus register (SYSCFG_ITLINE1) | [SYSCFG_ITLINE1.json](../registers_json/SYSCFG_ITLINE1.json) |
| `SYSCFG_ITLINE10` | `0xA8` | SYSCFG interrupt line 10 st atus register (SYSCFG_ITLINE10) | [SYSCFG_ITLINE10.json](../registers_json/SYSCFG_ITLINE10.json) |
| `SYSCFG_ITLINE11` | `0xAC` | SYSCFG interrupt line 11 st atus register (SYSCFG_ITLINE11) | [SYSCFG_ITLINE11.json](../registers_json/SYSCFG_ITLINE11.json) |
| `SYSCFG_ITLINE12` | `0xB0` | SYSCFG interrupt line 12 st atus register (SYSCFG_ITLINE12) | [SYSCFG_ITLINE12.json](../registers_json/SYSCFG_ITLINE12.json) |
| `SYSCFG_ITLINE13` | `0xB4` | SYSCFG interrupt line 13 st atus register (SYSCFG_ITLINE13) | [SYSCFG_ITLINE13.json](../registers_json/SYSCFG_ITLINE13.json) |
| `SYSCFG_ITLINE14` | `0xB8` | SYSCFG interrupt line 14 st atus register (SYSCFG_ITLINE14) | [SYSCFG_ITLINE14.json](../registers_json/SYSCFG_ITLINE14.json) |
| `SYSCFG_ITLINE15` | `0xBC` | SYSCFG interrupt line 15 st atus register (SYSCFG_ITLINE15) | [SYSCFG_ITLINE15.json](../registers_json/SYSCFG_ITLINE15.json) |
| `SYSCFG_ITLINE16` | `0xC0` | SYSCFG interrupt line 16 st atus register (SYSCFG_ITLINE16) | [SYSCFG_ITLINE16.json](../registers_json/SYSCFG_ITLINE16.json) |
| `SYSCFG_ITLINE19` | `0xCC` | SYSCFG interrupt line 19 st atus register (SYSCFG_ITLINE19) | [SYSCFG_ITLINE19.json](../registers_json/SYSCFG_ITLINE19.json) |
| `SYSCFG_ITLINE2` | `0x88` | SYSCFG interrupt line 2 st atus register (SYSCFG_ITLINE2) | [SYSCFG_ITLINE2.json](../registers_json/SYSCFG_ITLINE2.json) |
| `SYSCFG_ITLINE20` | `0xD0` | SYSCFG interrupt line 20 st atus register (SYSCFG_ITLINE20) | [SYSCFG_ITLINE20.json](../registers_json/SYSCFG_ITLINE20.json) |
| `SYSCFG_ITLINE21` | `0xD4` | SYSCFG interrupt line 21 st atus register (SYSCFG_ITLINE21) | [SYSCFG_ITLINE21.json](../registers_json/SYSCFG_ITLINE21.json) |
| `SYSCFG_ITLINE22` | `0xD8` | SYSCFG interrupt line 22 st atus register (SYSCFG_ITLINE22) | [SYSCFG_ITLINE22.json](../registers_json/SYSCFG_ITLINE22.json) |
| `SYSCFG_ITLINE23` | `0xDC` | SYSCFG interrupt line 23 st atus register (SYSCFG_ITLINE23) | [SYSCFG_ITLINE23.json](../registers_json/SYSCFG_ITLINE23.json) |
| `SYSCFG_ITLINE24` | `0xE0` | SYSCFG interrupt line 24 st atus register (SYSCFG_ITLINE24) | [SYSCFG_ITLINE24.json](../registers_json/SYSCFG_ITLINE24.json) |
| `SYSCFG_ITLINE25` | `0xE4` | SYSCFG interrupt line 25 st atus register (SYSCFG_ITLINE25) | [SYSCFG_ITLINE25.json](../registers_json/SYSCFG_ITLINE25.json) |
| `SYSCFG_ITLINE26` | `0xE8` | SYSCFG interrupt line 26 st atus register (SYSCFG_ITLINE26) | [SYSCFG_ITLINE26.json](../registers_json/SYSCFG_ITLINE26.json) |
| `SYSCFG_ITLINE27` | `0xEC` | SYSCFG interrupt line 27 st atus register (SYSCFG_ITLINE27) | [SYSCFG_ITLINE27.json](../registers_json/SYSCFG_ITLINE27.json) |
| `SYSCFG_ITLINE28` | `0xF0` | SYSCFG interrupt line 28 st atus register (SYSCFG_ITLINE28) | [SYSCFG_ITLINE28.json](../registers_json/SYSCFG_ITLINE28.json) |
| `SYSCFG_ITLINE29` | `0xF4` | SYSCFG interrupt line 29 st atus register (SYSCFG_ITLINE29) | [SYSCFG_ITLINE29.json](../registers_json/SYSCFG_ITLINE29.json) |
| `SYSCFG_ITLINE3` | `0x8C` | SYSCFG interrupt line 3 st atus register (SYSCFG_ITLINE3) | [SYSCFG_ITLINE3.json](../registers_json/SYSCFG_ITLINE3.json) |
| `SYSCFG_ITLINE30` | `0xF8` | SYSCFG interrupt line 30 st atus register (SYSCFG_ITLINE30) | [SYSCFG_ITLINE30.json](../registers_json/SYSCFG_ITLINE30.json) |
| `SYSCFG_ITLINE31` | `0xFC` | SYSCFG interrupt line 31 st atus register (SYSCFG_ITLINE31) | [SYSCFG_ITLINE31.json](../registers_json/SYSCFG_ITLINE31.json) |
| `SYSCFG_ITLINE4` | `0x90` | SYSCFG interrupt line 4 st atus register (SYSCFG_ITLINE4) | [SYSCFG_ITLINE4.json](../registers_json/SYSCFG_ITLINE4.json) |
| `SYSCFG_ITLINE5` | `0x94` | SYSCFG interrupt line 5 st atus register (SYSCFG_ITLINE5) | [SYSCFG_ITLINE5.json](../registers_json/SYSCFG_ITLINE5.json) |
| `SYSCFG_ITLINE6` | `0x98` | SYSCFG interrupt line 6 st atus register (SYSCFG_ITLINE6) | [SYSCFG_ITLINE6.json](../registers_json/SYSCFG_ITLINE6.json) |
| `SYSCFG_ITLINE7` | `0x9C` | SYSCFG interrupt line 7 st atus register (SYSCFG_ITLINE7) | [SYSCFG_ITLINE7.json](../registers_json/SYSCFG_ITLINE7.json) |
| `SYSCFG_ITLINE8` | `0xA0` | SYSCFG interrupt line 8 st atus register (SYSCFG_ITLINE8) | [SYSCFG_ITLINE8.json](../registers_json/SYSCFG_ITLINE8.json) |
| `SYSCFG_ITLINE9` | `0xA4` | SYSCFG interrupt line 9 st atus register (SYSCFG_ITLINE9) | [SYSCFG_ITLINE9.json](../registers_json/SYSCFG_ITLINE9.json) |