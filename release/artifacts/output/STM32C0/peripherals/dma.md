# Direct Memory Access Controller (DMA)

## 1. Overview & Key Features
The Direct Memory Access Controller (DMA) block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 11](../chapters/chapter_11.md), [Chapter 12](../chapters/chapter_12.md) (Pages 223 - 242).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 11](../chapters/chapter_11.md), [Chapter 12](../chapters/chapter_12.md)
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
| `DMAMUX` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0490 Rev 6 243/1023 RM0490 DMA request multiplexer (DMAMUX) | [DMAMUX.json](../registers_json/DMAMUX.json) |
| `DMAMUX_C0CR` | `0x000` | Direct Memory Access Controller (DMA) DMAMUX_C0CR Register | [DMAMUX_C0CR.json](../registers_json/DMAMUX_C0CR.json) |
| `DMAMUX_C1CR` | `0x004` | Direct Memory Access Controller (DMA) DMAMUX_C1CR Register | [DMAMUX_C1CR.json](../registers_json/DMAMUX_C1CR.json) |
| `DMAMUX_C2CR` | `0x008` | Direct Memory Access Controller (DMA) DMAMUX_C2CR Register | [DMAMUX_C2CR.json](../registers_json/DMAMUX_C2CR.json) |
| `DMAMUX_C3CR` | `0x00C` | Direct Memory Access Controller (DMA) DMAMUX_C3CR Register | [DMAMUX_C3CR.json](../registers_json/DMAMUX_C3CR.json) |
| `DMAMUX_C4CR` | `0x010` | Direct Memory Access Controller (DMA) DMAMUX_C4CR Register | [DMAMUX_C4CR.json](../registers_json/DMAMUX_C4CR.json) |
| `DMAMUX_CFR` | `0x084` | DMAMUX request line multipl exer interrupt clear flag register (DMAMUX_CFR) | [DMAMUX_CFR.json](../registers_json/DMAMUX_CFR.json) |
| `DMAMUX_CSR` | `0x080` | DMAMUX request line multiplexer interrupt channel status register (DMAMUX_CSR) | [DMAMUX_CSR.json](../registers_json/DMAMUX_CSR.json) |
| `DMAMUX_CXCR` | `0x000` | DMAMUX request line multipl exer channel x configuration register (DMAMUX_CXCR) | [DMAMUX_CXCR.json](../registers_json/DMAMUX_CXCR.json) |
| `DMAMUX_RG0CR` | `0x100` | Direct Memory Access Controller (DMA) DMAMUX_RG0CR Register | [DMAMUX_RG0CR.json](../registers_json/DMAMUX_RG0CR.json) |
| `DMAMUX_RG1CR` | `0x104` | Direct Memory Access Controller (DMA) DMAMUX_RG1CR Register | [DMAMUX_RG1CR.json](../registers_json/DMAMUX_RG1CR.json) |
| `DMAMUX_RG2CR` | `0x108` | Direct Memory Access Controller (DMA) DMAMUX_RG2CR Register | [DMAMUX_RG2CR.json](../registers_json/DMAMUX_RG2CR.json) |
| `DMAMUX_RG3CR` | `0x10C` | Direct Memory Access Controller (DMA) DMAMUX_RG3CR Register | [DMAMUX_RG3CR.json](../registers_json/DMAMUX_RG3CR.json) |
| `DMAMUX_RGCFR` | `0x144` | DMAMUX request generator interrupt clear flag register (DMAMUX_RGCFR) | [DMAMUX_RGCFR.json](../registers_json/DMAMUX_RGCFR.json) |
| `DMAMUX_RGSR` | `0x140` | DMAMUX request generato r interrupt status register (DMAMUX_RGSR) | [DMAMUX_RGSR.json](../registers_json/DMAMUX_RGSR.json) |
| `DMAMUX_RGXCR` | `0x100` | DMAMUX request generator channel x configuration register (DMAMUX_RGXCR) | [DMAMUX_RGXCR.json](../registers_json/DMAMUX_RGXCR.json) |
| `DMA_CCR1` | `0x008` | Direct Memory Access Controller (DMA) DMA_CCR1 Register | [DMA_CCR1.json](../registers_json/DMA_CCR1.json) |
| `DMA_CCR2` | `0x01C` | Direct Memory Access Controller (DMA) DMA_CCR2 Register | [DMA_CCR2.json](../registers_json/DMA_CCR2.json) |
| `DMA_CCR3` | `0x030` | Direct Memory Access Controller (DMA) DMA_CCR3 Register | [DMA_CCR3.json](../registers_json/DMA_CCR3.json) |
| `DMA_CCR4` | `0x044` | Direct Memory Access Controller (DMA) DMA_CCR4 Register | [DMA_CCR4.json](../registers_json/DMA_CCR4.json) |
| `DMA_CCR5` | `0x058` | Direct Memory Access Controller (DMA) DMA_CCR5 Register | [DMA_CCR5.json](../registers_json/DMA_CCR5.json) |
| `DMA_CCR6` | `0x06C` | Direct Memory Access Controller (DMA) DMA_CCR6 Register | [DMA_CCR6.json](../registers_json/DMA_CCR6.json) |
| `DMA_CCR7` | `0x080` | Direct Memory Access Controller (DMA) DMA_CCR7 Register | [DMA_CCR7.json](../registers_json/DMA_CCR7.json) |
| `DMA_CCRX` | `0x08` | DMA channel x config uration register (DMA_CCRX) | [DMA_CCRX.json](../registers_json/DMA_CCRX.json) |
| `DMA_CMAR1` | `0x014` | Direct Memory Access Controller (DMA) DMA_CMAR1 Register | [DMA_CMAR1.json](../registers_json/DMA_CMAR1.json) |
| `DMA_CMAR2` | `0x028` | Direct Memory Access Controller (DMA) DMA_CMAR2 Register | [DMA_CMAR2.json](../registers_json/DMA_CMAR2.json) |
| `DMA_CMAR3` | `0x03C` | Direct Memory Access Controller (DMA) DMA_CMAR3 Register | [DMA_CMAR3.json](../registers_json/DMA_CMAR3.json) |
| `DMA_CMAR4` | `0x050` | Direct Memory Access Controller (DMA) DMA_CMAR4 Register | [DMA_CMAR4.json](../registers_json/DMA_CMAR4.json) |
| `DMA_CMAR5` | `0x064` | Direct Memory Access Controller (DMA) DMA_CMAR5 Register | [DMA_CMAR5.json](../registers_json/DMA_CMAR5.json) |
| `DMA_CMAR6` | `0x078` | Direct Memory Access Controller (DMA) DMA_CMAR6 Register | [DMA_CMAR6.json](../registers_json/DMA_CMAR6.json) |
| `DMA_CMAR7` | `0x08C` | Direct Memory Access Controller (DMA) DMA_CMAR7 Register | [DMA_CMAR7.json](../registers_json/DMA_CMAR7.json) |
| `DMA_CMARX` | `0x14` | DMA channel x memory address register (DMA_CMARX) | [DMA_CMARX.json](../registers_json/DMA_CMARX.json) |
| `DMA_CNDTR1` | `0x00C` | Direct Memory Access Controller (DMA) DMA_CNDTR1 Register | [DMA_CNDTR1.json](../registers_json/DMA_CNDTR1.json) |
| `DMA_CNDTR2` | `0x020` | Direct Memory Access Controller (DMA) DMA_CNDTR2 Register | [DMA_CNDTR2.json](../registers_json/DMA_CNDTR2.json) |
| `DMA_CNDTR3` | `0x034` | Direct Memory Access Controller (DMA) DMA_CNDTR3 Register | [DMA_CNDTR3.json](../registers_json/DMA_CNDTR3.json) |
| `DMA_CNDTR4` | `0x048` | Direct Memory Access Controller (DMA) DMA_CNDTR4 Register | [DMA_CNDTR4.json](../registers_json/DMA_CNDTR4.json) |
| `DMA_CNDTR5` | `0x05C` | Direct Memory Access Controller (DMA) DMA_CNDTR5 Register | [DMA_CNDTR5.json](../registers_json/DMA_CNDTR5.json) |
| `DMA_CNDTR6` | `0x070` | Direct Memory Access Controller (DMA) DMA_CNDTR6 Register | [DMA_CNDTR6.json](../registers_json/DMA_CNDTR6.json) |
| `DMA_CNDTR7` | `0x084` | Direct Memory Access Controller (DMA) DMA_CNDTR7 Register | [DMA_CNDTR7.json](../registers_json/DMA_CNDTR7.json) |
| `DMA_CNDTRX` | `0x0C` | DMA channel x number of data to transfer register (DMA_CNDTRX) | [DMA_CNDTRX.json](../registers_json/DMA_CNDTRX.json) |
| `DMA_CPAR1` | `0x010` | Direct Memory Access Controller (DMA) DMA_CPAR1 Register | [DMA_CPAR1.json](../registers_json/DMA_CPAR1.json) |
| `DMA_CPAR2` | `0x024` | Direct Memory Access Controller (DMA) DMA_CPAR2 Register | [DMA_CPAR2.json](../registers_json/DMA_CPAR2.json) |
| `DMA_CPAR3` | `0x038` | Direct Memory Access Controller (DMA) DMA_CPAR3 Register | [DMA_CPAR3.json](../registers_json/DMA_CPAR3.json) |
| `DMA_CPAR4` | `0x04C` | Direct Memory Access Controller (DMA) DMA_CPAR4 Register | [DMA_CPAR4.json](../registers_json/DMA_CPAR4.json) |
| `DMA_CPAR5` | `0x060` | Direct Memory Access Controller (DMA) DMA_CPAR5 Register | [DMA_CPAR5.json](../registers_json/DMA_CPAR5.json) |
| `DMA_CPAR6` | `0x074` | Direct Memory Access Controller (DMA) DMA_CPAR6 Register | [DMA_CPAR6.json](../registers_json/DMA_CPAR6.json) |
| `DMA_CPAR7` | `0x088` | Direct Memory Access Controller (DMA) DMA_CPAR7 Register | [DMA_CPAR7.json](../registers_json/DMA_CPAR7.json) |
| `DMA_CPARX` | `0x10` | DMA channel x peripheral address register (DMA_CPARX) | [DMA_CPARX.json](../registers_json/DMA_CPARX.json) |
| `DMA_CPARXANDDMA_CMARX` | `0x00` | reconfiguring the other channel registers (DMA_CPARXANDDMA_CMARX) | [DMA_CPARXANDDMA_CMARX.json](../registers_json/DMA_CPARXANDDMA_CMARX.json) |
| `DMA_IFCR` | `0x04` | DMA interrupt flag clear register (DMA_IFCR) | [DMA_IFCR.json](../registers_json/DMA_IFCR.json) |
| `DMA_ISR` | `0x000` | Direct Memory Access Controller (DMA) DMA_ISR Register | [DMA_ISR.json](../registers_json/DMA_ISR.json) |