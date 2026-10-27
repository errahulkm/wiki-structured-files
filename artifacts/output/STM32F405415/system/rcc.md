# Reset and Clock Control (RCC)

## 1. Overview & Key Features
The Reset and Clock Control (RCC) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 9](../chapters/chapter_09.md), [Chapter 10](../chapters/chapter_10.md) (Pages 151 - 213).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: SYSTEM
* **Reference Chapter**: [Chapter 9](../chapters/chapter_09.md), [Chapter 10](../chapters/chapter_10.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Reset and Clock Control (RCC) Architectural Block Diagram](../figures/rcc_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Reset and Clock Control (RCC) Configuration & Parameter Matrix](../tables/rcc_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `RCC_AHB1ENR` | `0x30` | RCC AHB1 peripheral clo ck enable register (RCC_AHB1ENR) | [RCC_AHB1ENR.json](../registers_json/RCC_AHB1ENR.json) |
| `RCC_AHB1LPENR` | `0x50` | RCC AHB1 peripheral clock enable in low power mode register (RCC_AHB1LPENR) | [RCC_AHB1LPENR.json](../registers_json/RCC_AHB1LPENR.json) |
| `RCC_AHB1RSTR` | `0x10` | RCC AHB1 peripheral reset register (RCC_AHB1RSTR) | [RCC_AHB1RSTR.json](../registers_json/RCC_AHB1RSTR.json) |
| `RCC_AHB2ENR` | `0x34` | RCC AHB2 peripheral clo ck enable register (RCC_AHB2ENR) | [RCC_AHB2ENR.json](../registers_json/RCC_AHB2ENR.json) |
| `RCC_AHB2LPENR` | `0x54` | RCC AHB2 peripheral clock enable in low power mode register (RCC_AHB2LPENR) | [RCC_AHB2LPENR.json](../registers_json/RCC_AHB2LPENR.json) |
| `RCC_AHB2RSTR` | `0x14` | RCC AHB2 peripheral reset register (RCC_AHB2RSTR) | [RCC_AHB2RSTR.json](../registers_json/RCC_AHB2RSTR.json) |
| `RCC_AHB3ENR` | `0x38` | RCC AHB3 peripheral clo ck enable register (RCC_AHB3ENR) | [RCC_AHB3ENR.json](../registers_json/RCC_AHB3ENR.json) |
| `RCC_AHB3LPENR` | `0x58` | RCC AHB3 peripheral clock enable in low power mode register (RCC_AHB3LPENR) | [RCC_AHB3LPENR.json](../registers_json/RCC_AHB3LPENR.json) |
| `RCC_AHB3RSTR` | `0x18` | RCC AHB3 peripheral reset register (RCC_AHB3RSTR) | [RCC_AHB3RSTR.json](../registers_json/RCC_AHB3RSTR.json) |
| `RCC_APB1ENR` | `0x40` | RCC APB1 peripher al clock enable register (RCC_APB1ENR) | [RCC_APB1ENR.json](../registers_json/RCC_APB1ENR.json) |
| `RCC_APB1LPENR` | `0x60` | RCC APB1 peripheral clock enable in low power mode register (RCC_APB1LPENR) | [RCC_APB1LPENR.json](../registers_json/RCC_APB1LPENR.json) |
| `RCC_APB1RSTR` | `0x20` | RCC APB1 peripheral reset register (RCC_APB1RSTR) | [RCC_APB1RSTR.json](../registers_json/RCC_APB1RSTR.json) |
| `RCC_APB2ENR` | `0x44` | RCC APB2 peripheral clo ck enable register (RCC_APB2ENR) | [RCC_APB2ENR.json](../registers_json/RCC_APB2ENR.json) |
| `RCC_APB2LPENR` | `0x64` | RCC APB2 peripheral cl ock enabled in low power mode register (RCC_APB2LPENR) | [RCC_APB2LPENR.json](../registers_json/RCC_APB2LPENR.json) |
| `RCC_APB2RSTR` | `0x24` | RCC APB2 peripheral reset register (RCC_APB2RSTR) | [RCC_APB2RSTR.json](../registers_json/RCC_APB2RSTR.json) |
| `RCC_BDCR` | `0x70` | RCC Backup domain control register (RCC_BDCR) | [RCC_BDCR.json](../registers_json/RCC_BDCR.json) |
| `RCC_CFGR` | `0x08` | RCC clock configurat ion register (RCC_CFGR) | [RCC_CFGR.json](../registers_json/RCC_CFGR.json) |
| `RCC_CIR` | `0x0C` | RCC clock interrupt register (RCC_CIR) | [RCC_CIR.json](../registers_json/RCC_CIR.json) |
| `RCC_CR` | `0x00` | RCC clock cont rol register (RCC_CR) | [RCC_CR.json](../registers_json/RCC_CR.json) |
| `RCC_CSR` | `0x74` | Reset and Clock Control (RCC) RCC_CSR Register | [RCC_CSR.json](../registers_json/RCC_CSR.json) |
| `RCC_DCKCFGR` | `0x8C` | RCC Dedicated Clock Confi guration Register (RCC_DCKCFGR) | [RCC_DCKCFGR.json](../registers_json/RCC_DCKCFGR.json) |
| `RCC_PLLCFGR` | `0x04` | RCC PLL configurati on register (RCC_PLLCFGR) | [RCC_PLLCFGR.json](../registers_json/RCC_PLLCFGR.json) |
| `RCC_PLLI2SCFGR` | `0x84` | RCC PLLI2S configurat ion register (RCC_PLLI2SCFGR) | [RCC_PLLI2SCFGR.json](../registers_json/RCC_PLLI2SCFGR.json) |
| `RCC_PLLSAICFGR` | `0x88` | RCC PLL configurati on register (RCC_PLLSAICFGR) | [RCC_PLLSAICFGR.json](../registers_json/RCC_PLLSAICFGR.json) |
| `RCC_SSCGR` | `0x80` | RCC spread spectrum clo ck generation register (RCC_SSCGR) | [RCC_SSCGR.json](../registers_json/RCC_SSCGR.json) |