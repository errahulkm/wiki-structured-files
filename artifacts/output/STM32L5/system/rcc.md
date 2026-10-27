# Reset and Clock Control (RCC)

## 1. Overview & Key Features
The Reset and Clock Control (RCC) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 9](../chapters/chapter_09.md) (Pages 323 - 423).

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
* [Figure: Reset and Clock Control (RCC) Architectural Block Diagram](../figures/rcc_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Reset and Clock Control (RCC) Configuration & Parameter Matrix](../tables/rcc_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `RCC` | `0x00` | Offset Register Name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0438 Rev 8 423/2187 RM0438 Reset and clock control (RCC) | [RCC.json](../registers_json/RCC.json) |
| `RCC_` | `0x100` | Reset and Clock Control (RCC) RCC_ Register | [RCC_.json](../registers_json/RCC_.json) |
| `RCC_AHB1` | `0x068` | Reset and Clock Control (RCC) RCC_AHB1 Register | [RCC_AHB1.json](../registers_json/RCC_AHB1.json) |
| `RCC_AHB1ENR` | `0x048` | RCC AHB1 peripheral clo ck enable register (RCC_AHB1ENR) | [RCC_AHB1ENR.json](../registers_json/RCC_AHB1ENR.json) |
| `RCC_AHB1RSTR` | `0x028` | RCC AHB1 peripheral reset register (RCC_AHB1RSTR) | [RCC_AHB1RSTR.json](../registers_json/RCC_AHB1RSTR.json) |
| `RCC_AHB1SECSR` | `0x00` | RCC AHB1 security stat us register (RCC_AHB1SECSR) | [RCC_AHB1SECSR.json](../registers_json/RCC_AHB1SECSR.json) |
| `RCC_AHB1SMENR` | `0x068` | RCC AHB1 peripheral clocks enab le in Sleep and Stop modes register (RCC_AHB1SMENR) | [RCC_AHB1SMENR.json](../registers_json/RCC_AHB1SMENR.json) |
| `RCC_AHB2` | `0x06C` | Reset and Clock Control (RCC) RCC_AHB2 Register | [RCC_AHB2.json](../registers_json/RCC_AHB2.json) |
| `RCC_AHB2ENR` | `0x04C` | RCC AHB2 peripheral clo ck enable register (RCC_AHB2ENR) | [RCC_AHB2ENR.json](../registers_json/RCC_AHB2ENR.json) |
| `RCC_AHB2RSTR` | `0x02C` | RCC AHB2 peripheral reset register (RCC_AHB2RSTR) | [RCC_AHB2RSTR.json](../registers_json/RCC_AHB2RSTR.json) |
| `RCC_AHB2SECSR` | `0x00` | RCC AHB2 security stat us register (RCC_AHB2SECSR) | [RCC_AHB2SECSR.json](../registers_json/RCC_AHB2SECSR.json) |
| `RCC_AHB2SMENR` | `0x06C` | RCC AHB2 peripheral clocks enab le in Sleep and Stop modes register (RCC_AHB2SMENR) | [RCC_AHB2SMENR.json](../registers_json/RCC_AHB2SMENR.json) |
| `RCC_AHB3` | `0x070` | Reset and Clock Control (RCC) RCC_AHB3 Register | [RCC_AHB3.json](../registers_json/RCC_AHB3.json) |
| `RCC_AHB3ENR` | `0x050` | RCC AHB3 peripheral cl ock enable register (RCC_AHB3ENR) | [RCC_AHB3ENR.json](../registers_json/RCC_AHB3ENR.json) |
| `RCC_AHB3RSTR` | `0x030` | RCC AHB3 peripheral reset register (RCC_AHB3RSTR) | [RCC_AHB3RSTR.json](../registers_json/RCC_AHB3RSTR.json) |
| `RCC_AHB3SECSR` | `0x00` | RCC AHB3 security stat us register (RCC_AHB3SECSR) | [RCC_AHB3SECSR.json](../registers_json/RCC_AHB3SECSR.json) |
| `RCC_AHB3SMENR` | `0x070` | RCC AHB3 peripheral clocks enab le in Sleep and Stop modes register (RCC_AHB3SMENR) | [RCC_AHB3SMENR.json](../registers_json/RCC_AHB3SMENR.json) |
| `RCC_AHBXENR` | `0x00` | Peripheral clo ck enable registers (RCC_AHBXENR) | [RCC_AHBXENR.json](../registers_json/RCC_AHBXENR.json) |
| `RCC_APB1` | `0x0FC` | Reset and Clock Control (RCC) RCC_APB1 Register | [RCC_APB1.json](../registers_json/RCC_APB1.json) |
| `RCC_APB1ENR1` | `0x00` | RCC APB1 peripheral clock enable register 1 (RCC_APB1ENR1) | [RCC_APB1ENR1.json](../registers_json/RCC_APB1ENR1.json) |
| `RCC_APB1ENR2` | `0x05C` | RCC APB1 peripheral clock enable register 2 (RCC_APB1ENR2) | [RCC_APB1ENR2.json](../registers_json/RCC_APB1ENR2.json) |
| `RCC_APB1RSTR1` | `0x038` | RCC APB1 peripheral re set register 1 (RCC_APB1RSTR1) | [RCC_APB1RSTR1.json](../registers_json/RCC_APB1RSTR1.json) |
| `RCC_APB1RSTR2` | `0x03C` | RCC APB1 peripheral re set register 2 (RCC_APB1RSTR2) | [RCC_APB1RSTR2.json](../registers_json/RCC_APB1RSTR2.json) |
| `RCC_APB1SECSR1` | `0x00` | RCC APB1 security status register 1 (RCC_APB1SECSR1) | [RCC_APB1SECSR1.json](../registers_json/RCC_APB1SECSR1.json) |
| `RCC_APB1SECSR2` | `0x00` | RCC APB1 security status register 2 (RCC_APB1SECSR2) | [RCC_APB1SECSR2.json](../registers_json/RCC_APB1SECSR2.json) |
| `RCC_APB1SMENR1` | `0x00` | RCC APB1 peripheral clocks enable in Sleep and Stop modes register 1 (RCC_APB1SMENR1) | [RCC_APB1SMENR1.json](../registers_json/RCC_APB1SMENR1.json) |
| `RCC_APB1SMENR2` | `0x07C` | RCC APB1 peripheral clocks enable in Sleep and Stop modes register 2 (RCC_APB1SMENR2) | [RCC_APB1SMENR2.json](../registers_json/RCC_APB1SMENR2.json) |
| `RCC_APB2` | `0x080` | Reset and Clock Control (RCC) RCC_APB2 Register | [RCC_APB2.json](../registers_json/RCC_APB2.json) |
| `RCC_APB2ENR` | `0x00` | RCC APB2 peripheral clo ck enable register (RCC_APB2ENR) | [RCC_APB2ENR.json](../registers_json/RCC_APB2ENR.json) |
| `RCC_APB2RSTR` | `0x040` | RCC APB2 peripheral reset register (RCC_APB2RSTR) | [RCC_APB2RSTR.json](../registers_json/RCC_APB2RSTR.json) |
| `RCC_APB2SECSR` | `0x00` | RCC APB2 security stat us register (RCC_APB2SECSR) | [RCC_APB2SECSR.json](../registers_json/RCC_APB2SECSR.json) |
| `RCC_APB2SMENR` | `0x00` | RCC APB2 peripheral clocks enab le in Sleep and Stop modes register (RCC_APB2SMENR) | [RCC_APB2SMENR.json](../registers_json/RCC_APB2SMENR.json) |
| `RCC_APBXENRY` | `0x00` | Peripheral clo ck enable registers (RCC_APBXENRY) | [RCC_APBXENRY.json](../registers_json/RCC_APBXENRY.json) |
| `RCC_BDCR` | `0x0090` | RCC Backup domain control register (RCC_BDCR) | [RCC_BDCR.json](../registers_json/RCC_BDCR.json) |
| `RCC_CCIPR1` | `0x00` | RCC peripherals independent clock configuration register 1 (RCC_CCIPR1) | [RCC_CCIPR1.json](../registers_json/RCC_CCIPR1.json) |
| `RCC_CCIPR2` | `0x00` | RCC peripherals independent clock configuration register 2 (RCC_CCIPR2) | [RCC_CCIPR2.json](../registers_json/RCC_CCIPR2.json) |
| `RCC_CFGR` | `0x008` | RCC clock configurat ion register (RCC_CFGR) | [RCC_CFGR.json](../registers_json/RCC_CFGR.json) |
| `RCC_CICR` | `0x020` | RCC clock interrupt clear register (RCC_CICR) | [RCC_CICR.json](../registers_json/RCC_CICR.json) |
| `RCC_CIER` | `0x018` | RCC clock interrupt en able register (RCC_CIER) | [RCC_CIER.json](../registers_json/RCC_CIER.json) |
| `RCC_CIFR` | `0x01C` | RCC clock interrupt flag register (RCC_CIFR) | [RCC_CIFR.json](../registers_json/RCC_CIFR.json) |
| `RCC_CR` | `0x000` | RCC clock cont rol register (RCC_CR) | [RCC_CR.json](../registers_json/RCC_CR.json) |
| `RCC_CRRCR` | `0x00` | RCC clock recovery RC register (RCC_CRRCR) | [RCC_CRRCR.json](../registers_json/RCC_CRRCR.json) |
| `RCC_CSR` | `0x094` | RCC control/stat us register (RCC_CSR) | [RCC_CSR.json](../registers_json/RCC_CSR.json) |
| `RCC_DLY` | `0xA4` | Reset and Clock Control (RCC) RCC_DLY Register | [RCC_DLY.json](../registers_json/RCC_DLY.json) |
| `RCC_DLYCFGR` | `0x00` | OCTOSPI delay configur ation register (RCC_DLYCFGR) | [RCC_DLYCFGR.json](../registers_json/RCC_DLYCFGR.json) |
| `RCC_ICSCR` | `0x004` | RCC internal clock sources cal ibration register (RCC_ICSCR) | [RCC_ICSCR.json](../registers_json/RCC_ICSCR.json) |
| `RCC_PLLCFGR` | `0x00C` | RCC PLL configurati on register (RCC_PLLCFGR) | [RCC_PLLCFGR.json](../registers_json/RCC_PLLCFGR.json) |
| `RCC_PLLSAI1CFGR` | `0x010` | RCC PLLSAI1 configurati on register (RCC_PLLSAI1CFGR) | [RCC_PLLSAI1CFGR.json](../registers_json/RCC_PLLSAI1CFGR.json) |
| `RCC_PLLSAI2CFGR` | `0x014` | RCC PLLSAI2 configurati on register (RCC_PLLSAI2CFGR) | [RCC_PLLSAI2CFGR.json](../registers_json/RCC_PLLSAI2CFGR.json) |
| `RCC_SECCFGR` | `0x00` | RCC secure configuration register (RCC_SECCFGR) | [RCC_SECCFGR.json](../registers_json/RCC_SECCFGR.json) |
| `RCC_SECSR` | `0x00` | RCC secure status register (RCC_SECSR) | [RCC_SECSR.json](../registers_json/RCC_SECSR.json) |