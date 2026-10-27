# Secure Digital Input/Output (SDIO)

## 1. Overview & Key Features
The Secure Digital Input/Output (SDIO) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 34](../chapters/chapter_34.md) (Pages 1014 - 1068).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 34](../chapters/chapter_34.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Secure Digital Input/Output (SDIO) Architectural Block Diagram](../figures/sdio_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Secure Digital Input/Output (SDIO) Configuration & Parameter Matrix](../tables/sdio_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `SDIO_ARG` | `0x08` | SDIO argument register (SDIO_ARG) | [SDIO_ARG.json](../registers_json/SDIO_ARG.json) |
| `SDIO_CLKCR` | `0x04` | SDI clock control register (SDIO_CLKCR) | [SDIO_CLKCR.json](../registers_json/SDIO_CLKCR.json) |
| `SDIO_CMD` | `0x0C` | Secure Digital Input/Output (SDIO) SDIO_CMD Register | [SDIO_CMD.json](../registers_json/SDIO_CMD.json) |
| `SDIO_DCOUNT` | `0x30` | SDIO data counter register (SDIO_DCOUNT) | [SDIO_DCOUNT.json](../registers_json/SDIO_DCOUNT.json) |
| `SDIO_DCTRL` | `0x2C` | SDIO data control register (SDIO_DCTRL) | [SDIO_DCTRL.json](../registers_json/SDIO_DCTRL.json) |
| `SDIO_DLEN` | `0x28` | SDIO data length register (SDIO_DLEN) | [SDIO_DLEN.json](../registers_json/SDIO_DLEN.json) |
| `SDIO_DTIMER` | `0x24` | Secure Digital Input/Output (SDIO) SDIO_DTIMER Register | [SDIO_DTIMER.json](../registers_json/SDIO_DTIMER.json) |
| `SDIO_FIFO` | `0x80` | SDIO data FIFO register (SDIO_FIFO) | [SDIO_FIFO.json](../registers_json/SDIO_FIFO.json) |
| `SDIO_FIFOCNT` | `0x48` | SDIO FIFO counter register (SDIO_FIFOCNT) | [SDIO_FIFOCNT.json](../registers_json/SDIO_FIFOCNT.json) |
| `SDIO_ICR` | `0x38` | SDIO interrupt cl ear register (SDIO_ICR) | [SDIO_ICR.json](../registers_json/SDIO_ICR.json) |
| `SDIO_MASK` | `0x3C` | SDIO mask regi ster (SDIO_MASK) | [SDIO_MASK.json](../registers_json/SDIO_MASK.json) |
| `SDIO_POWER` | `0x00` | SDIO power control register (SDIO_POWER) | [SDIO_POWER.json](../registers_json/SDIO_POWER.json) |
| `SDIO_RESP1` | `0x14` | Secure Digital Input/Output (SDIO) SDIO_RESP1 Register | [SDIO_RESP1.json](../registers_json/SDIO_RESP1.json) |
| `SDIO_RESP2` | `0x18` | Secure Digital Input/Output (SDIO) SDIO_RESP2 Register | [SDIO_RESP2.json](../registers_json/SDIO_RESP2.json) |
| `SDIO_RESP3` | `0x1C` | Secure Digital Input/Output (SDIO) SDIO_RESP3 Register | [SDIO_RESP3.json](../registers_json/SDIO_RESP3.json) |
| `SDIO_RESP4` | `0x20` | Secure Digital Input/Output (SDIO) SDIO_RESP4 Register | [SDIO_RESP4.json](../registers_json/SDIO_RESP4.json) |
| `SDIO_RESPCMD` | `0x10` | SDIO command response register (SDIO_RESPCMD) | [SDIO_RESPCMD.json](../registers_json/SDIO_RESPCMD.json) |
| `SDIO_STA` | `0x34` | SDIO status register (SDIO_STA) | [SDIO_STA.json](../registers_json/SDIO_STA.json) |