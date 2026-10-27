# Controller Area Network (bxCAN)

## 1. Overview & Key Features
The Controller Area Network (bxCAN) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 35](../chapters/chapter_35.md) (Pages 1069 - 1112).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 35](../chapters/chapter_35.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Controller Area Network (bxCAN) Architectural Block Diagram](../figures/can_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Controller Area Network (bxCAN) Configuration & Parameter Matrix](../tables/can_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `CAN_BTR` | `0x1C` | CAN bit timing register (CAN_BTR) | [CAN_BTR.json](../registers_json/CAN_BTR.json) |
| `CAN_ESR` | `0x18` | 1098/1741 RM0090 Rev 22 CAN error status register (CAN_ESR) | [CAN_ESR.json](../registers_json/CAN_ESR.json) |
| `CAN_F0R1` | `0x240` | Controller Area Network (bxCAN) CAN_F0R1 Register | [CAN_F0R1.json](../registers_json/CAN_F0R1.json) |
| `CAN_F0R2` | `0x244` | Controller Area Network (bxCAN) CAN_F0R2 Register | [CAN_F0R2.json](../registers_json/CAN_F0R2.json) |
| `CAN_F1R1` | `0x248` | Controller Area Network (bxCAN) CAN_F1R1 Register | [CAN_F1R1.json](../registers_json/CAN_F1R1.json) |
| `CAN_F1R2` | `0x24C` | Controller Area Network (bxCAN) CAN_F1R2 Register | [CAN_F1R2.json](../registers_json/CAN_F1R2.json) |
| `CAN_F27R1` | `0x318` | Controller Area Network (bxCAN) CAN_F27R1 Register | [CAN_F27R1.json](../registers_json/CAN_F27R1.json) |
| `CAN_F27R2` | `0x31C` | Controller Area Network (bxCAN) CAN_F27R2 Register | [CAN_F27R2.json](../registers_json/CAN_F27R2.json) |
| `CAN_FA1R` | `0x21C` | CAN filter activation register (CAN_FA1R) | [CAN_FA1R.json](../registers_json/CAN_FA1R.json) |
| `CAN_FFA1R` | `0x214` | CAN filter FIFO assignment register (CAN_FFA1R) | [CAN_FFA1R.json](../registers_json/CAN_FFA1R.json) |
| `CAN_FM1R` | `0x204` | CAN filter mode register (CAN_FM1R) | [CAN_FM1R.json](../registers_json/CAN_FM1R.json) |
| `CAN_FMR` | `0x200` | CAN filter registers CAN filter master register (CAN_FMR) | [CAN_FMR.json](../registers_json/CAN_FMR.json) |
| `CAN_FS1R` | `0x20C` | CAN filter scale register (CAN_FS1R) | [CAN_FS1R.json](../registers_json/CAN_FS1R.json) |
| `CAN_IER` | `0x14` | CAN interrupt enable register (CAN_IER) | [CAN_IER.json](../registers_json/CAN_IER.json) |
| `CAN_MCR` | `0x000` | CAN master control register (CAN_MCR) | [CAN_MCR.json](../registers_json/CAN_MCR.json) |
| `CAN_MSR` | `0x04` | 1092/1741 RM0090 Rev 22 CAN master status register (CAN_MSR) | [CAN_MSR.json](../registers_json/CAN_MSR.json) |
| `CAN_RDH0R` | `0x1BC` | Controller Area Network (bxCAN) CAN_RDH0R Register | [CAN_RDH0R.json](../registers_json/CAN_RDH0R.json) |
| `CAN_RDH1R` | `0x1CC` | Controller Area Network (bxCAN) CAN_RDH1R Register | [CAN_RDH1R.json](../registers_json/CAN_RDH1R.json) |
| `CAN_RDL0R` | `0x1B8` | Controller Area Network (bxCAN) CAN_RDL0R Register | [CAN_RDL0R.json](../registers_json/CAN_RDL0R.json) |
| `CAN_RDL1R` | `0x1C8` | Controller Area Network (bxCAN) CAN_RDL1R Register | [CAN_RDL1R.json](../registers_json/CAN_RDL1R.json) |
| `CAN_RDT0R` | `0x1B4` | Controller Area Network (bxCAN) CAN_RDT0R Register | [CAN_RDT0R.json](../registers_json/CAN_RDT0R.json) |
| `CAN_RDT1R` | `0x1C4` | Controller Area Network (bxCAN) CAN_RDT1R Register | [CAN_RDT1R.json](../registers_json/CAN_RDT1R.json) |
| `CAN_RF0R` | `0x0C` | CAN receive FIFO 0 register (CAN_RF0R) | [CAN_RF0R.json](../registers_json/CAN_RF0R.json) |
| `CAN_RF1R` | `0x10` | 1096/1741 RM0090 Rev 22 CAN receive FIFO 1 register (CAN_RF1R) | [CAN_RF1R.json](../registers_json/CAN_RF1R.json) |
| `CAN_RI0R` | `0x1B0` | Controller Area Network (bxCAN) CAN_RI0R Register | [CAN_RI0R.json](../registers_json/CAN_RI0R.json) |
| `CAN_RI1R` | `0x1C0` | Controller Area Network (bxCAN) CAN_RI1R Register | [CAN_RI1R.json](../registers_json/CAN_RI1R.json) |
| `CAN_TDH0R` | `0x18C` | Controller Area Network (bxCAN) CAN_TDH0R Register | [CAN_TDH0R.json](../registers_json/CAN_TDH0R.json) |
| `CAN_TDH1R` | `0x19C` | Controller Area Network (bxCAN) CAN_TDH1R Register | [CAN_TDH1R.json](../registers_json/CAN_TDH1R.json) |
| `CAN_TDH2R` | `0x1AC` | Controller Area Network (bxCAN) CAN_TDH2R Register | [CAN_TDH2R.json](../registers_json/CAN_TDH2R.json) |
| `CAN_TDL0R` | `0x188` | Controller Area Network (bxCAN) CAN_TDL0R Register | [CAN_TDL0R.json](../registers_json/CAN_TDL0R.json) |
| `CAN_TDL1R` | `0x198` | Controller Area Network (bxCAN) CAN_TDL1R Register | [CAN_TDL1R.json](../registers_json/CAN_TDL1R.json) |
| `CAN_TDL2R` | `0x1A8` | Controller Area Network (bxCAN) CAN_TDL2R Register | [CAN_TDL2R.json](../registers_json/CAN_TDL2R.json) |
| `CAN_TDT0R` | `0x184` | Controller Area Network (bxCAN) CAN_TDT0R Register | [CAN_TDT0R.json](../registers_json/CAN_TDT0R.json) |
| `CAN_TDT1R` | `0x194` | Controller Area Network (bxCAN) CAN_TDT1R Register | [CAN_TDT1R.json](../registers_json/CAN_TDT1R.json) |
| `CAN_TDT2R` | `0x1A4` | Controller Area Network (bxCAN) CAN_TDT2R Register | [CAN_TDT2R.json](../registers_json/CAN_TDT2R.json) |
| `CAN_TDTXR` | `0x00` | CAN mailbox data length control and time stamp register (CAN_TDTXR) | [CAN_TDTXR.json](../registers_json/CAN_TDTXR.json) |
| `CAN_TI0R` | `0x180` | Controller Area Network (bxCAN) CAN_TI0R Register | [CAN_TI0R.json](../registers_json/CAN_TI0R.json) |
| `CAN_TI1R` | `0x190` | Controller Area Network (bxCAN) CAN_TI1R Register | [CAN_TI1R.json](../registers_json/CAN_TI1R.json) |
| `CAN_TI2R` | `0x1A0` | Controller Area Network (bxCAN) CAN_TI2R Register | [CAN_TI2R.json](../registers_json/CAN_TI2R.json) |
| `CAN_TSR` | `0x08` | CAN transmit status register (CAN_TSR) | [CAN_TSR.json](../registers_json/CAN_TSR.json) |