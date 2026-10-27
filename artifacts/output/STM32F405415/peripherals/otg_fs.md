# USB On-The-Go Full-Speed (OTG_FS)

## 1. Overview & Key Features
The USB On-The-Go Full-Speed (OTG_FS) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 37](../chapters/chapter_37.md) (Pages 1228 - 1368).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 37](../chapters/chapter_37.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: USB On-The-Go Full-Speed (OTG_FS) Architectural Block Diagram](../figures/otg_fs_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: USB On-The-Go Full-Speed (OTG_FS) Configuration & Parameter Matrix](../tables/otg_fs_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `OTG_FS_CID` | `0x03C` | 1278/1741 RM0090 Rev 22 OTG_FS core ID register (OTG_FS_CID) | [OTG_FS_CID.json](../registers_json/OTG_FS_CID.json) |
| `OTG_FS_DAINT` | `0x818` | OTG_FS device all endpoints interrupt register (OTG_FS_DAINT) | [OTG_FS_DAINT.json](../registers_json/OTG_FS_DAINT.json) |
| `OTG_FS_DAINTMSK` | `0x81C` | 1296/1741 RM0090 Rev 22 OTG_FS all endpoints interrupt mask register (OTG_FS_DAINTMSK) | [OTG_FS_DAINTMSK.json](../registers_json/OTG_FS_DAINTMSK.json) |
| `OTG_FS_DCFG` | `0x800` | Device-mode registers OTG_FS device configuration register (OTG_FS_DCFG) | [OTG_FS_DCFG.json](../registers_json/OTG_FS_DCFG.json) |
| `OTG_FS_DCTL` | `0x804` | OTG_FS device control register (OTG_FS_DCTL) | [OTG_FS_DCTL.json](../registers_json/OTG_FS_DCTL.json) |
| `OTG_FS_DIEPC` | `0x900` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_DIEPC Register | [OTG_FS_DIEPC.json](../registers_json/OTG_FS_DIEPC.json) |
| `OTG_FS_DIEPCTL0` | `0x900` | OTG_FS device control IN endpoint 0 control register (OTG_FS_DIEPCTL0) | [OTG_FS_DIEPCTL0.json](../registers_json/OTG_FS_DIEPCTL0.json) |
| `OTG_FS_DIEPE` | `0x834` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_DIEPE Register | [OTG_FS_DIEPE.json](../registers_json/OTG_FS_DIEPE.json) |
| `OTG_FS_DIEPEMPMSK` | `0x834` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_DIEPEMPMSK Register | [OTG_FS_DIEPEMPMSK.json](../registers_json/OTG_FS_DIEPEMPMSK.json) |
| `OTG_FS_DIEPI` | `0x968` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_DIEPI Register | [OTG_FS_DIEPI.json](../registers_json/OTG_FS_DIEPI.json) |
| `OTG_FS_DIEPINTX` | `0x00` | OTG_FS_DIEPINTx 0x908 OTG_FS device endpoint-x interrupt register (OTG_FS_DIEPINTX) | [OTG_FS_DIEPINTX.json](../registers_json/OTG_FS_DIEPINTX.json) |
| `OTG_FS_DIEPM` | `0x810` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_DIEPM Register | [OTG_FS_DIEPM.json](../registers_json/OTG_FS_DIEPM.json) |
| `OTG_FS_DIEPMSK` | `0x810` | OTG_FS device IN endpoint common interrupt mask register (OTG_FS_DIEPMSK) | [OTG_FS_DIEPMSK.json](../registers_json/OTG_FS_DIEPMSK.json) |
| `OTG_FS_DIEPT` | `0x970` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_DIEPT Register | [OTG_FS_DIEPT.json](../registers_json/OTG_FS_DIEPT.json) |
| `OTG_FS_DIEPTSIZ0` | `0x910` | 1308/1741 RM0090 Rev 22 OTG_FS device IN endpoint 0 transfer size register (OTG_FS_DIEPTSIZ0) | [OTG_FS_DIEPTSIZ0.json](../registers_json/OTG_FS_DIEPTSIZ0.json) |
| `OTG_FS_DIEPTSIZX` | `0x00` | OTG_FS device endpoint-x transfer size register (OTG_FS_DIEPTSIZX) | [OTG_FS_DIEPTSIZX.json](../registers_json/OTG_FS_DIEPTSIZX.json) |
| `OTG_FS_DIEPTXFX` | `0x00` | OTG_FS device IN endpoint transmit FIFO size register (OTG_FS_DIEPTXFX) | [OTG_FS_DIEPTXFX.json](../registers_json/OTG_FS_DIEPTXFX.json) |
| `OTG_FS_DOEP` | `0xB70` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_DOEP Register | [OTG_FS_DOEP.json](../registers_json/OTG_FS_DOEP.json) |
| `OTG_FS_DOEPCTL0` | `0xB00` | 1302/1741 RM0090 Rev 22 OTG_FS device control OUT endpoint 0 control register (OTG_FS_DOEPCTL0) | [OTG_FS_DOEPCTL0.json](../registers_json/OTG_FS_DOEPCTL0.json) |
| `OTG_FS_DOEPI` | `0xB68` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_DOEPI Register | [OTG_FS_DOEPI.json](../registers_json/OTG_FS_DOEPI.json) |
| `OTG_FS_DOEPINTX` | `0x00` | OTG_FS_DOEPINTx 0xB08 OTG_FS device endpoint-x interrupt register (OTG_FS_DOEPINTX) | [OTG_FS_DOEPINTX.json](../registers_json/OTG_FS_DOEPINTX.json) |
| `OTG_FS_DOEPMSK` | `0x814` | 1294/1741 RM0090 Rev 22 OTG_FS device OUT endpoint common interrupt mask register (OTG_FS_DOEPMSK) | [OTG_FS_DOEPMSK.json](../registers_json/OTG_FS_DOEPMSK.json) |
| `OTG_FS_DOEPTSIZ0` | `0xB10` | 1310/1741 RM0090 Rev 22 OTG_FS device OUT endpoint 0 transfer size register (OTG_FS_DOEPTSIZ0) | [OTG_FS_DOEPTSIZ0.json](../registers_json/OTG_FS_DOEPTSIZ0.json) |
| `OTG_FS_DOEPTSIZX` | `0x00` | OTG_FS device OUT endpoint-x transfer size register (OTG_FS_DOEPTSIZX) | [OTG_FS_DOEPTSIZX.json](../registers_json/OTG_FS_DOEPTSIZX.json) |
| `OTG_FS_DSTS` | `0x808` | OTG_FS device status register (OTG_FS_DSTS) | [OTG_FS_DSTS.json](../registers_json/OTG_FS_DSTS.json) |
| `OTG_FS_DVBU` | `0x828` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_DVBU Register | [OTG_FS_DVBU.json](../registers_json/OTG_FS_DVBU.json) |
| `OTG_FS_DVBUSDIS` | `0x0828` | OTG_FS device VBUS discharge time register (OTG_FS_DVBUSDIS) | [OTG_FS_DVBUSDIS.json](../registers_json/OTG_FS_DVBUSDIS.json) |
| `OTG_FS_DVBUSPULSE` | `0x082C` | OTG_FS device VBUS pulsing time register (OTG_FS_DVBUSPULSE) | [OTG_FS_DVBUSPULSE.json](../registers_json/OTG_FS_DVBUSPULSE.json) |
| `OTG_FS_GAHB` | `0x008` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_GAHB Register | [OTG_FS_GAHB.json](../registers_json/OTG_FS_GAHB.json) |
| `OTG_FS_GAHBCFG` | `0x008` | 1262/1741 RM0090 Rev 22 OTG_FS AHB configuration register (OTG_FS_GAHBCFG) | [OTG_FS_GAHBCFG.json](../registers_json/OTG_FS_GAHBCFG.json) |
| `OTG_FS_GCCFG` | `0x038` | OTG_FS general core configuration register (OTG_FS_GCCFG) | [OTG_FS_GCCFG.json](../registers_json/OTG_FS_GCCFG.json) |
| `OTG_FS_GINT` | `0x018` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_GINT Register | [OTG_FS_GINT.json](../registers_json/OTG_FS_GINT.json) |
| `OTG_FS_GINTMSK` | `0x018` | OTG_FS interrupt mask register (OTG_FS_GINTMSK) | [OTG_FS_GINTMSK.json](../registers_json/OTG_FS_GINTMSK.json) |
| `OTG_FS_GINTS` | `0x014` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_GINTS Register | [OTG_FS_GINTS.json](../registers_json/OTG_FS_GINTS.json) |
| `OTG_FS_GINTSTS` | `0x014` | OTG_FS core interrupt register (OTG_FS_GINTSTS) | [OTG_FS_GINTSTS.json](../registers_json/OTG_FS_GINTSTS.json) |
| `OTG_FS_GOTG` | `0x000` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_GOTG Register | [OTG_FS_GOTG.json](../registers_json/OTG_FS_GOTG.json) |
| `OTG_FS_GOTGCTL` | `0x000` | OTG_FS control and status register (OTG_FS_GOTGCTL) | [OTG_FS_GOTGCTL.json](../registers_json/OTG_FS_GOTGCTL.json) |
| `OTG_FS_GOTGINT` | `0x04` | 1260/1741 RM0090 Rev 22 OTG_FS interrupt register (OTG_FS_GOTGINT) | [OTG_FS_GOTGINT.json](../registers_json/OTG_FS_GOTGINT.json) |
| `OTG_FS_GRST` | `0x010` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_GRST Register | [OTG_FS_GRST.json](../registers_json/OTG_FS_GRST.json) |
| `OTG_FS_GRSTCTL` | `0x010` | OTG_FS reset register (OTG_FS_GRSTCTL) | [OTG_FS_GRSTCTL.json](../registers_json/OTG_FS_GRSTCTL.json) |
| `OTG_FS_GRXF` | `0x024` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_GRXF Register | [OTG_FS_GRXF.json](../registers_json/OTG_FS_GRXF.json) |
| `OTG_FS_GRXFSIZ` | `0x024` | Device mode OTG_FS Receive FIFO size register (OTG_FS_GRXFSIZ) | [OTG_FS_GRXFSIZ.json](../registers_json/OTG_FS_GRXFSIZ.json) |
| `OTG_FS_GRXS` | `0x01C` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_GRXS Register | [OTG_FS_GRXS.json](../registers_json/OTG_FS_GRXS.json) |
| `OTG_FS_GRXSTSP` | `0x00` | 1274/1741 RM0090 Rev 22 OTG_FS Receive status debug read/OTG status read and pop registers (OTG_FS_GRXSTSP) | [OTG_FS_GRXSTSP.json](../registers_json/OTG_FS_GRXSTSP.json) |
| `OTG_FS_GRXSTSR` | `0x01C` | 1274/1741 RM0090 Rev 22 OTG_FS Receive status debug read/OTG status read and pop registers (OTG_FS_GRXSTSR) | [OTG_FS_GRXSTSR.json](../registers_json/OTG_FS_GRXSTSR.json) |
| `OTG_FS_GUSB` | `0x00C` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_GUSB Register | [OTG_FS_GUSB.json](../registers_json/OTG_FS_GUSB.json) |
| `OTG_FS_GUSBCFG` | `0x00C` | OTG_FS USB configuration register (OTG_FS_GUSBCFG) | [OTG_FS_GUSBCFG.json](../registers_json/OTG_FS_GUSBCFG.json) |
| `OTG_FS_HAINT` | `0x414` | 1282/1741 RM0090 Rev 22 OTG_FS Host all channels interrupt register (OTG_FS_HAINT) | [OTG_FS_HAINT.json](../registers_json/OTG_FS_HAINT.json) |
| `OTG_FS_HAINTMSK` | `0x418` | OTG_FS Host all channels interrupt mask register (OTG_FS_HAINTMSK) | [OTG_FS_HAINTMSK.json](../registers_json/OTG_FS_HAINTMSK.json) |
| `OTG_FS_HCCH` | `0x500` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_HCCH Register | [OTG_FS_HCCH.json](../registers_json/OTG_FS_HCCH.json) |
| `OTG_FS_HCCHARX` | `0x00` | 1286/1741 RM0090 Rev 22 OTG_FS Host channel-x characteristics register (OTG_FS_HCCHARX) | [OTG_FS_HCCHARX.json](../registers_json/OTG_FS_HCCHARX.json) |
| `OTG_FS_HCFG` | `0x400` | OTG_FS Host configuration register (OTG_FS_HCFG) | [OTG_FS_HCFG.json](../registers_json/OTG_FS_HCFG.json) |
| `OTG_FS_HCINT` | `0x5EC` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_HCINT Register | [OTG_FS_HCINT.json](../registers_json/OTG_FS_HCINT.json) |
| `OTG_FS_HCINTMSKX` | `0x00` | 1288/1741 RM0090 Rev 22 OTG_FS Host channel-x interrupt mask register (OTG_FS_HCINTMSKX) | [OTG_FS_HCINTMSKX.json](../registers_json/OTG_FS_HCINTMSKX.json) |
| `OTG_FS_HCTSI` | `0x510` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_HCTSI Register | [OTG_FS_HCTSI.json](../registers_json/OTG_FS_HCTSI.json) |
| `OTG_FS_HCTSIZ2` | `0x1368` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_HCTSIZ2 Register | [OTG_FS_HCTSIZ2.json](../registers_json/OTG_FS_HCTSIZ2.json) |
| `OTG_FS_HCTSIZX` | `0x00` | OTG_FS_HCTSIZx 0x510 OTG_FS Host channel-x transfer size register (OTG_FS_HCTSIZX) | [OTG_FS_HCTSIZX.json](../registers_json/OTG_FS_HCTSIZX.json) |
| `OTG_FS_HFIR` | `0x404` | OTG_FS Host frame interval register (OTG_FS_HFIR) | [OTG_FS_HFIR.json](../registers_json/OTG_FS_HFIR.json) |
| `OTG_FS_HFNU` | `0x408` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_HFNU Register | [OTG_FS_HFNU.json](../registers_json/OTG_FS_HFNU.json) |
| `OTG_FS_HFNUM` | `0x408` | OTG_FS Host frame number/frame time remaining register (OTG_FS_HFNUM) | [OTG_FS_HFNUM.json](../registers_json/OTG_FS_HFNUM.json) |
| `OTG_FS_HNPT` | `0x028` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_HNPT Register | [OTG_FS_HNPT.json](../registers_json/OTG_FS_HNPT.json) |
| `OTG_FS_HNPTXFSIZ` | `0x1275` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_HNPTXFSIZ Register | [OTG_FS_HNPTXFSIZ.json](../registers_json/OTG_FS_HNPTXFSIZ.json) |
| `OTG_FS_HNPTXSTS` | `0x02C` | Host mode Device mode OTG_FS non-periodic transmit FIFO/queue status register (OTG_FS_HNPTXSTS) | [OTG_FS_HNPTXSTS.json](../registers_json/OTG_FS_HNPTXSTS.json) |
| `OTG_FS_HPRT` | `0x440` | OTG_FS Host port control and status register (OTG_FS_HPRT) | [OTG_FS_HPRT.json](../registers_json/OTG_FS_HPRT.json) |
| `OTG_FS_HPTX` | `0x100` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_HPTX Register | [OTG_FS_HPTX.json](../registers_json/OTG_FS_HPTX.json) |
| `OTG_FS_HPTXFSIZ` | `0x100` | OTG_FS Host periodic transmit FIFO size register (OTG_FS_HPTXFSIZ) | [OTG_FS_HPTXFSIZ.json](../registers_json/OTG_FS_HPTXFSIZ.json) |
| `OTG_FS_HPTXSTS` | `0x410` | OTG_FS_Host periodic transmit FIFO/queue status register (OTG_FS_HPTXSTS) | [OTG_FS_HPTXSTS.json](../registers_json/OTG_FS_HPTXSTS.json) |
| `OTG_FS_PCGC` | `0xE00` | USB On-The-Go Full-Speed (OTG_FS) OTG_FS_PCGC Register | [OTG_FS_PCGC.json](../registers_json/OTG_FS_PCGC.json) |
| `OTG_FS_PCGCCTL` | `0xE00` | OTG_FS power and cl ock gating control register (OTG_FS_PCGCCTL) | [OTG_FS_PCGCCTL.json](../registers_json/OTG_FS_PCGCCTL.json) |