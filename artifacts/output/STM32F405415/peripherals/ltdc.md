# LCD-TFT Display Controller (LTDC)

## 1. Overview & Key Features
The LCD-TFT Display Controller (LTDC) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 19](../chapters/chapter_19.md) (Pages 480 - 514).

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
* [Figure: LCD-TFT Display Controller (LTDC) Architectural Block Diagram](../figures/ltdc_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: LCD-TFT Display Controller (LTDC) Configuration & Parameter Matrix](../tables/ltdc_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `LTDC_AWCR` | `0x0010` | LTDC Active Width Confi guration Register (LTDC_AWCR) | [LTDC_AWCR.json](../registers_json/LTDC_AWCR.json) |
| `LTDC_BCCR` | `0x002C` | LTDC Background Color Conf iguration Register (LTDC_BCCR) | [LTDC_BCCR.json](../registers_json/LTDC_BCCR.json) |
| `LTDC_BPCR` | `0x000C` | LTDC Back Porch Confi guration Register (LTDC_BPCR) | [LTDC_BPCR.json](../registers_json/LTDC_BPCR.json) |
| `LTDC_CDSR` | `0x0048` | LTDC Current Display Status Register (LTDC_CDSR) | [LTDC_CDSR.json](../registers_json/LTDC_CDSR.json) |
| `LTDC_CPSR` | `0x44` | LTDC Current Position Status Register (LTDC_CPSR) | [LTDC_CPSR.json](../registers_json/LTDC_CPSR.json) |
| `LTDC_GCR` | `0x0018` | LTDC Global Contro l Register (LTDC_GCR) | [LTDC_GCR.json](../registers_json/LTDC_GCR.json) |
| `LTDC_ICR` | `0x3C` | LTDC Interrupt Clear Register (LTDC_ICR) | [LTDC_ICR.json](../registers_json/LTDC_ICR.json) |
| `LTDC_IER` | `0x0034` | LTDC Interrupt Enable Register (LTDC_IER) | [LTDC_IER.json](../registers_json/LTDC_IER.json) |
| `LTDC_ISR` | `0x0038` | LTDC Interrupt Stat us Register (LTDC_ISR) | [LTDC_ISR.json](../registers_json/LTDC_ISR.json) |
| `LTDC_L1BFCR` | `0x00A0` | LCD-TFT Display Controller (LTDC) LTDC_L1BFCR Register | [LTDC_L1BFCR.json](../registers_json/LTDC_L1BFCR.json) |
| `LTDC_L1CACR` | `0x0098` | LCD-TFT Display Controller (LTDC) LTDC_L1CACR Register | [LTDC_L1CACR.json](../registers_json/LTDC_L1CACR.json) |
| `LTDC_L1CFBAR` | `0x00AC` | LCD-TFT Display Controller (LTDC) LTDC_L1CFBAR Register | [LTDC_L1CFBAR.json](../registers_json/LTDC_L1CFBAR.json) |
| `LTDC_L1CFBLNR` | `0x00B4` | LCD-TFT Display Controller (LTDC) LTDC_L1CFBLNR Register | [LTDC_L1CFBLNR.json](../registers_json/LTDC_L1CFBLNR.json) |
| `LTDC_L1CFBLR` | `0x00B0` | LCD-TFT Display Controller (LTDC) LTDC_L1CFBLR Register | [LTDC_L1CFBLR.json](../registers_json/LTDC_L1CFBLR.json) |
| `LTDC_L1CKCR` | `0x0090` | LCD-TFT Display Controller (LTDC) LTDC_L1CKCR Register | [LTDC_L1CKCR.json](../registers_json/LTDC_L1CKCR.json) |
| `LTDC_L1CLUTWR` | `0x00C4` | LCD-TFT Display Controller (LTDC) LTDC_L1CLUTWR Register | [LTDC_L1CLUTWR.json](../registers_json/LTDC_L1CLUTWR.json) |
| `LTDC_L1CR` | `0x0084` | LCD-TFT Display Controller (LTDC) LTDC_L1CR Register | [LTDC_L1CR.json](../registers_json/LTDC_L1CR.json) |
| `LTDC_L1DCCR` | `0x009C` | LCD-TFT Display Controller (LTDC) LTDC_L1DCCR Register | [LTDC_L1DCCR.json](../registers_json/LTDC_L1DCCR.json) |
| `LTDC_L1PFCR` | `0x0094` | LCD-TFT Display Controller (LTDC) LTDC_L1PFCR Register | [LTDC_L1PFCR.json](../registers_json/LTDC_L1PFCR.json) |
| `LTDC_L1WHPCR` | `0x0088` | LCD-TFT Display Controller (LTDC) LTDC_L1WHPCR Register | [LTDC_L1WHPCR.json](../registers_json/LTDC_L1WHPCR.json) |
| `LTDC_L1WVPCR` | `0x008C` | LCD-TFT Display Controller (LTDC) LTDC_L1WVPCR Register | [LTDC_L1WVPCR.json](../registers_json/LTDC_L1WVPCR.json) |
| `LTDC_L2BFCR` | `0x0120` | LCD-TFT Display Controller (LTDC) LTDC_L2BFCR Register | [LTDC_L2BFCR.json](../registers_json/LTDC_L2BFCR.json) |
| `LTDC_L2CACR` | `0x0118` | LCD-TFT Display Controller (LTDC) LTDC_L2CACR Register | [LTDC_L2CACR.json](../registers_json/LTDC_L2CACR.json) |
| `LTDC_L2CFBAR` | `0x012C` | LCD-TFT Display Controller (LTDC) LTDC_L2CFBAR Register | [LTDC_L2CFBAR.json](../registers_json/LTDC_L2CFBAR.json) |
| `LTDC_L2CFBLNR` | `0x0134` | LCD-TFT Display Controller (LTDC) LTDC_L2CFBLNR Register | [LTDC_L2CFBLNR.json](../registers_json/LTDC_L2CFBLNR.json) |
| `LTDC_L2CFBLR` | `0x0130` | LCD-TFT Display Controller (LTDC) LTDC_L2CFBLR Register | [LTDC_L2CFBLR.json](../registers_json/LTDC_L2CFBLR.json) |
| `LTDC_L2CKCR` | `0x0110` | LCD-TFT Display Controller (LTDC) LTDC_L2CKCR Register | [LTDC_L2CKCR.json](../registers_json/LTDC_L2CKCR.json) |
| `LTDC_L2CLUTWR` | `0x0144` | LCD-TFT Display Controller (LTDC) LTDC_L2CLUTWR Register | [LTDC_L2CLUTWR.json](../registers_json/LTDC_L2CLUTWR.json) |
| `LTDC_L2CR` | `0x0104` | LCD-TFT Display Controller (LTDC) LTDC_L2CR Register | [LTDC_L2CR.json](../registers_json/LTDC_L2CR.json) |
| `LTDC_L2DCCR` | `0x011C` | LCD-TFT Display Controller (LTDC) LTDC_L2DCCR Register | [LTDC_L2DCCR.json](../registers_json/LTDC_L2DCCR.json) |
| `LTDC_L2PFCR` | `0x0114` | LCD-TFT Display Controller (LTDC) LTDC_L2PFCR Register | [LTDC_L2PFCR.json](../registers_json/LTDC_L2PFCR.json) |
| `LTDC_L2WHPCR` | `0x0108` | LCD-TFT Display Controller (LTDC) LTDC_L2WHPCR Register | [LTDC_L2WHPCR.json](../registers_json/LTDC_L2WHPCR.json) |
| `LTDC_L2WVPCR` | `0x010C` | LCD-TFT Display Controller (LTDC) LTDC_L2WVPCR Register | [LTDC_L2WVPCR.json](../registers_json/LTDC_L2WVPCR.json) |
| `LTDC_LIPCR` | `0x0040` | LTDC Line Interrupt Position Configuration Register (LTDC_LIPCR) | [LTDC_LIPCR.json](../registers_json/LTDC_LIPCR.json) |
| `LTDC_LXBFCR` | `0x00` | LTDC Layerx Blending Factors Configuration Register (LTDC_LXBFCR) | [LTDC_LXBFCR.json](../registers_json/LTDC_LXBFCR.json) |
| `LTDC_LXCACR` | `0x00` | LTDC Layerx Constant Alpha Configuration Register (LTDC_LXCACR) | [LTDC_LXCACR.json](../registers_json/LTDC_LXCACR.json) |
| `LTDC_LXCFBAR` | `0x00` | LTDC Layerx Color Frame Buff er Address Register (LTDC_LXCFBAR) | [LTDC_LXCFBAR.json](../registers_json/LTDC_LXCFBAR.json) |
| `LTDC_LXCFBLR` | `0x00` | LTDC Layerx Color Frame Buff er Length Register (LTDC_LXCFBLR) | [LTDC_LXCFBLR.json](../registers_json/LTDC_LXCFBLR.json) |
| `LTDC_LXCKCR` | `0x00` | LTDC Layerx Color Keying Conf iguration Register (LTDC_LXCKCR) | [LTDC_LXCKCR.json](../registers_json/LTDC_LXCKCR.json) |
| `LTDC_LXCLUTWR` | `0x00` | LTDC Layerx CLUT Write Register (LTDC_LXCLUTWR) | [LTDC_LXCLUTWR.json](../registers_json/LTDC_LXCLUTWR.json) |
| `LTDC_LXDCCR` | `0x00` | LTDC Layerx Default Color Co nfiguration Register (LTDC_LXDCCR) | [LTDC_LXDCCR.json](../registers_json/LTDC_LXDCCR.json) |
| `LTDC_LXPFCR` | `0x00` | LTDC Layerx Pixel Format C onfiguration Register (LTDC_LXPFCR) | [LTDC_LXPFCR.json](../registers_json/LTDC_LXPFCR.json) |
| `LTDC_SRCR` | `0x0024` | LTDC Shadow Reload Conf iguration Register (LTDC_SRCR) | [LTDC_SRCR.json](../registers_json/LTDC_SRCR.json) |
| `LTDC_SSCR` | `0x0008` | LTDC Synchronization Size C onfiguration Register (LTDC_SSCR) | [LTDC_SSCR.json](../registers_json/LTDC_SSCR.json) |
| `LTDC_TWCR` | `0x0014` | LTDC Total Width Config uration Register (LTDC_TWCR) | [LTDC_TWCR.json](../registers_json/LTDC_TWCR.json) |