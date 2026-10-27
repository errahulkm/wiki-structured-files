# Direct Memory Access Controller (DMA)

## 1. Overview & Key Features
The Direct Memory Access Controller (DMA) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 13](../chapters/chapter_13.md), [Chapter 14](../chapters/chapter_14.md) (Pages 304 - 340).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 13](../chapters/chapter_13.md), [Chapter 14](../chapters/chapter_14.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Direct Memory Access Controller (DMA) Architectural Block Diagram](../figures/dma_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Direct Memory Access Controller (DMA) Configuration & Parameter Matrix](../tables/dma_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `DMA2D_AMTCR` | `0x004C` | DMA2D AHB master timer conf iguration register (DMA2D_AMTCR) | [DMA2D_AMTCR.json](../registers_json/DMA2D_AMTCR.json) |
| `DMA2D_BGCLUT` | `0x0BFF` | Direct Memory Access Controller (DMA) DMA2D_BGCLUT Register | [DMA2D_BGCLUT.json](../registers_json/DMA2D_BGCLUT.json) |
| `DMA2D_BGCMAR` | `0x0030` | DMA2D background CLUT memory address register (DMA2D_BGCMAR) | [DMA2D_BGCMAR.json](../registers_json/DMA2D_BGCMAR.json) |
| `DMA2D_BGCOLR` | `0x0028` | DMA2D background colo r register (DMA2D_BGCOLR) | [DMA2D_BGCOLR.json](../registers_json/DMA2D_BGCOLR.json) |
| `DMA2D_BGMAR` | `0x0014` | DMA2D background memory address register (DMA2D_BGMAR) | [DMA2D_BGMAR.json](../registers_json/DMA2D_BGMAR.json) |
| `DMA2D_BGOR` | `0x0018` | DMA2D background off set register (DMA2D_BGOR) | [DMA2D_BGOR.json](../registers_json/DMA2D_BGOR.json) |
| `DMA2D_BGPFCCR` | `0x0024` | DMA2D background PFC c ontrol register (DMA2D_BGPFCCR) | [DMA2D_BGPFCCR.json](../registers_json/DMA2D_BGPFCCR.json) |
| `DMA2D_CR` | `0x0000` | DMA2D control register (DMA2D_CR) | [DMA2D_CR.json](../registers_json/DMA2D_CR.json) |
| `DMA2D_FGCLUT` | `0x07FF` | Direct Memory Access Controller (DMA) DMA2D_FGCLUT Register | [DMA2D_FGCLUT.json](../registers_json/DMA2D_FGCLUT.json) |
| `DMA2D_FGCMAR` | `0x002C` | DMA2D foreground CLUT memory address register (DMA2D_FGCMAR) | [DMA2D_FGCMAR.json](../registers_json/DMA2D_FGCMAR.json) |
| `DMA2D_FGCOLR` | `0x0020` | DMA2D foreground colo r register (DMA2D_FGCOLR) | [DMA2D_FGCOLR.json](../registers_json/DMA2D_FGCOLR.json) |
| `DMA2D_FGMAR` | `0x000C` | DMA2D foreground memory address register (DMA2D_FGMAR) | [DMA2D_FGMAR.json](../registers_json/DMA2D_FGMAR.json) |
| `DMA2D_FGOR` | `0x0010` | DMA2D foreground off set register (DMA2D_FGOR) | [DMA2D_FGOR.json](../registers_json/DMA2D_FGOR.json) |
| `DMA2D_FGPFCCR` | `0x001C` | DMA2D foreground PFC c ontrol register (DMA2D_FGPFCCR) | [DMA2D_FGPFCCR.json](../registers_json/DMA2D_FGPFCCR.json) |
| `DMA2D_IFCR` | `0x0008` | DMA2D interrupt flag clear register (DMA2D_IFCR) | [DMA2D_IFCR.json](../registers_json/DMA2D_IFCR.json) |
| `DMA2D_ISR` | `0x0004` | DMA2D Interrupt Stat us Register (DMA2D_ISR) | [DMA2D_ISR.json](../registers_json/DMA2D_ISR.json) |
| `DMA2D_LWR` | `0x0048` | DMA2D line waterma rk register (DMA2D_LWR) | [DMA2D_LWR.json](../registers_json/DMA2D_LWR.json) |
| `DMA2D_NLR` | `0x0044` | DMA2D number of line register (DMA2D_NLR) | [DMA2D_NLR.json](../registers_json/DMA2D_NLR.json) |
| `DMA2D_OCOLR` | `0x0038` | DMA2D output color register (DMA2D_OCOLR) | [DMA2D_OCOLR.json](../registers_json/DMA2D_OCOLR.json) |
| `DMA2D_OMAR` | `0x003C` | DMA2D output memory address register (DMA2D_OMAR) | [DMA2D_OMAR.json](../registers_json/DMA2D_OMAR.json) |
| `DMA2D_OOR` | `0x0040` | DMA2D output offset register (DMA2D_OOR) | [DMA2D_OOR.json](../registers_json/DMA2D_OOR.json) |
| `DMA2D_OPFCCR` | `0x0034` | DMA2D output PFC cont rol register (DMA2D_OPFCCR) | [DMA2D_OPFCCR.json](../registers_json/DMA2D_OPFCCR.json) |
| `DMA_HIFCR` | `0x0C` | DMA high interrupt flag clear register (DMA_HIFCR) | [DMA_HIFCR.json](../registers_json/DMA_HIFCR.json) |
| `DMA_HISR` | `0x04` | DMA high interrupt st atus register (DMA_HISR) | [DMA_HISR.json](../registers_json/DMA_HISR.json) |
| `DMA_LIFCR` | `0x08` | DMA low interrupt flag clear register (DMA_LIFCR) | [DMA_LIFCR.json](../registers_json/DMA_LIFCR.json) |
| `DMA_LISR` | `0x0000` | DMA low interrupt st atus register (DMA_LISR) | [DMA_LISR.json](../registers_json/DMA_LISR.json) |
| `DMA_S0CR` | `0x0010` | Direct Memory Access Controller (DMA) DMA_S0CR Register | [DMA_S0CR.json](../registers_json/DMA_S0CR.json) |
| `DMA_S0FCR` | `0x0024` | Direct Memory Access Controller (DMA) DMA_S0FCR Register | [DMA_S0FCR.json](../registers_json/DMA_S0FCR.json) |
| `DMA_S0M0AR` | `0x001C` | Direct Memory Access Controller (DMA) DMA_S0M0AR Register | [DMA_S0M0AR.json](../registers_json/DMA_S0M0AR.json) |
| `DMA_S0M1AR` | `0x0020` | Direct Memory Access Controller (DMA) DMA_S0M1AR Register | [DMA_S0M1AR.json](../registers_json/DMA_S0M1AR.json) |
| `DMA_S0NDTR` | `0x0014` | Direct Memory Access Controller (DMA) DMA_S0NDTR Register | [DMA_S0NDTR.json](../registers_json/DMA_S0NDTR.json) |
| `DMA_S0PAR` | `0x0018` | Direct Memory Access Controller (DMA) DMA_S0PAR Register | [DMA_S0PAR.json](../registers_json/DMA_S0PAR.json) |
| `DMA_S1CR` | `0x0028` | Direct Memory Access Controller (DMA) DMA_S1CR Register | [DMA_S1CR.json](../registers_json/DMA_S1CR.json) |
| `DMA_S1FCR` | `0x003C` | Direct Memory Access Controller (DMA) DMA_S1FCR Register | [DMA_S1FCR.json](../registers_json/DMA_S1FCR.json) |
| `DMA_S1M0AR` | `0x0034` | Direct Memory Access Controller (DMA) DMA_S1M0AR Register | [DMA_S1M0AR.json](../registers_json/DMA_S1M0AR.json) |
| `DMA_S1M1AR` | `0x0038` | Direct Memory Access Controller (DMA) DMA_S1M1AR Register | [DMA_S1M1AR.json](../registers_json/DMA_S1M1AR.json) |
| `DMA_S1NDTR` | `0x002C` | Direct Memory Access Controller (DMA) DMA_S1NDTR Register | [DMA_S1NDTR.json](../registers_json/DMA_S1NDTR.json) |
| `DMA_S1PAR` | `0x0030` | Direct Memory Access Controller (DMA) DMA_S1PAR Register | [DMA_S1PAR.json](../registers_json/DMA_S1PAR.json) |
| `DMA_S2CR` | `0x0040` | Direct Memory Access Controller (DMA) DMA_S2CR Register | [DMA_S2CR.json](../registers_json/DMA_S2CR.json) |
| `DMA_S2FCR` | `0x0054` | Direct Memory Access Controller (DMA) DMA_S2FCR Register | [DMA_S2FCR.json](../registers_json/DMA_S2FCR.json) |
| `DMA_S2M0AR` | `0x004C` | Direct Memory Access Controller (DMA) DMA_S2M0AR Register | [DMA_S2M0AR.json](../registers_json/DMA_S2M0AR.json) |
| `DMA_S2M1AR` | `0x0050` | Direct Memory Access Controller (DMA) DMA_S2M1AR Register | [DMA_S2M1AR.json](../registers_json/DMA_S2M1AR.json) |
| `DMA_S2NDTR` | `0x0044` | Direct Memory Access Controller (DMA) DMA_S2NDTR Register | [DMA_S2NDTR.json](../registers_json/DMA_S2NDTR.json) |
| `DMA_S2PAR` | `0x0048` | Direct Memory Access Controller (DMA) DMA_S2PAR Register | [DMA_S2PAR.json](../registers_json/DMA_S2PAR.json) |
| `DMA_S3CR` | `0x0058` | Direct Memory Access Controller (DMA) DMA_S3CR Register | [DMA_S3CR.json](../registers_json/DMA_S3CR.json) |
| `DMA_S3FCR` | `0x006C` | Direct Memory Access Controller (DMA) DMA_S3FCR Register | [DMA_S3FCR.json](../registers_json/DMA_S3FCR.json) |
| `DMA_S3M0AR` | `0x0064` | Direct Memory Access Controller (DMA) DMA_S3M0AR Register | [DMA_S3M0AR.json](../registers_json/DMA_S3M0AR.json) |
| `DMA_S3M1AR` | `0x0068` | Direct Memory Access Controller (DMA) DMA_S3M1AR Register | [DMA_S3M1AR.json](../registers_json/DMA_S3M1AR.json) |
| `DMA_S3NDTR` | `0x005C` | Direct Memory Access Controller (DMA) DMA_S3NDTR Register | [DMA_S3NDTR.json](../registers_json/DMA_S3NDTR.json) |
| `DMA_S3PAR` | `0x0060` | Direct Memory Access Controller (DMA) DMA_S3PAR Register | [DMA_S3PAR.json](../registers_json/DMA_S3PAR.json) |
| `DMA_S4CR` | `0x0070` | Direct Memory Access Controller (DMA) DMA_S4CR Register | [DMA_S4CR.json](../registers_json/DMA_S4CR.json) |
| `DMA_S4FCR` | `0x0084` | Direct Memory Access Controller (DMA) DMA_S4FCR Register | [DMA_S4FCR.json](../registers_json/DMA_S4FCR.json) |
| `DMA_S4M0AR` | `0x007C` | Direct Memory Access Controller (DMA) DMA_S4M0AR Register | [DMA_S4M0AR.json](../registers_json/DMA_S4M0AR.json) |
| `DMA_S4M1AR` | `0x0080` | Direct Memory Access Controller (DMA) DMA_S4M1AR Register | [DMA_S4M1AR.json](../registers_json/DMA_S4M1AR.json) |
| `DMA_S4NDTR` | `0x0074` | Direct Memory Access Controller (DMA) DMA_S4NDTR Register | [DMA_S4NDTR.json](../registers_json/DMA_S4NDTR.json) |
| `DMA_S4PAR` | `0x0078` | Direct Memory Access Controller (DMA) DMA_S4PAR Register | [DMA_S4PAR.json](../registers_json/DMA_S4PAR.json) |
| `DMA_S5CR` | `0x0088` | Direct Memory Access Controller (DMA) DMA_S5CR Register | [DMA_S5CR.json](../registers_json/DMA_S5CR.json) |
| `DMA_S5FCR` | `0x009C` | Direct Memory Access Controller (DMA) DMA_S5FCR Register | [DMA_S5FCR.json](../registers_json/DMA_S5FCR.json) |
| `DMA_S5M0AR` | `0x0094` | Direct Memory Access Controller (DMA) DMA_S5M0AR Register | [DMA_S5M0AR.json](../registers_json/DMA_S5M0AR.json) |
| `DMA_S5M1AR` | `0x0098` | Direct Memory Access Controller (DMA) DMA_S5M1AR Register | [DMA_S5M1AR.json](../registers_json/DMA_S5M1AR.json) |
| `DMA_S5NDTR` | `0x008C` | Direct Memory Access Controller (DMA) DMA_S5NDTR Register | [DMA_S5NDTR.json](../registers_json/DMA_S5NDTR.json) |
| `DMA_S5PAR` | `0x0090` | Direct Memory Access Controller (DMA) DMA_S5PAR Register | [DMA_S5PAR.json](../registers_json/DMA_S5PAR.json) |
| `DMA_S6CR` | `0x00A0` | Direct Memory Access Controller (DMA) DMA_S6CR Register | [DMA_S6CR.json](../registers_json/DMA_S6CR.json) |
| `DMA_S6FCR` | `0x00B4` | Direct Memory Access Controller (DMA) DMA_S6FCR Register | [DMA_S6FCR.json](../registers_json/DMA_S6FCR.json) |
| `DMA_S6M0AR` | `0x00AC` | Direct Memory Access Controller (DMA) DMA_S6M0AR Register | [DMA_S6M0AR.json](../registers_json/DMA_S6M0AR.json) |
| `DMA_S6M1AR` | `0x00B0` | Direct Memory Access Controller (DMA) DMA_S6M1AR Register | [DMA_S6M1AR.json](../registers_json/DMA_S6M1AR.json) |
| `DMA_S6NDTR` | `0x00A4` | Direct Memory Access Controller (DMA) DMA_S6NDTR Register | [DMA_S6NDTR.json](../registers_json/DMA_S6NDTR.json) |
| `DMA_S6PAR` | `0x00A8` | Direct Memory Access Controller (DMA) DMA_S6PAR Register | [DMA_S6PAR.json](../registers_json/DMA_S6PAR.json) |
| `DMA_S7CR` | `0x00B8` | Direct Memory Access Controller (DMA) DMA_S7CR Register | [DMA_S7CR.json](../registers_json/DMA_S7CR.json) |
| `DMA_S7FCR` | `0x00CC` | Direct Memory Access Controller (DMA) DMA_S7FCR Register | [DMA_S7FCR.json](../registers_json/DMA_S7FCR.json) |
| `DMA_S7M0AR` | `0x00C4` | Direct Memory Access Controller (DMA) DMA_S7M0AR Register | [DMA_S7M0AR.json](../registers_json/DMA_S7M0AR.json) |
| `DMA_S7M1AR` | `0x00C8` | Direct Memory Access Controller (DMA) DMA_S7M1AR Register | [DMA_S7M1AR.json](../registers_json/DMA_S7M1AR.json) |
| `DMA_S7NDTR` | `0x00BC` | Direct Memory Access Controller (DMA) DMA_S7NDTR Register | [DMA_S7NDTR.json](../registers_json/DMA_S7NDTR.json) |
| `DMA_S7PAR` | `0x00C0` | Direct Memory Access Controller (DMA) DMA_S7PAR Register | [DMA_S7PAR.json](../registers_json/DMA_S7PAR.json) |