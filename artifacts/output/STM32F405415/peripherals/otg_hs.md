# USB On-The-Go High-Speed (OTG_HS)

## 1. Overview & Key Features
The USB On-The-Go High-Speed (OTG_HS) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 38](../chapters/chapter_38.md) (Pages 1369 - 1531).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 38](../chapters/chapter_38.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: USB On-The-Go High-Speed (OTG_HS) Architectural Block Diagram](../figures/otg_hs_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: USB On-The-Go High-Speed (OTG_HS) Configuration & Parameter Matrix](../tables/otg_hs_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `OTG_HS_CID` | `0x03C` | OTG_HS core ID register (OTG_HS_CID) | [OTG_HS_CID.json](../registers_json/OTG_HS_CID.json) |
| `OTG_HS_DAI` | `0x818` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_DAI Register | [OTG_HS_DAI.json](../registers_json/OTG_HS_DAI.json) |
| `OTG_HS_DAINT` | `0x818` | 1438/1741 RM0090 Rev 22 OTG_HS device all endpoints interrupt register (OTG_HS_DAINT) | [OTG_HS_DAINT.json](../registers_json/OTG_HS_DAINT.json) |
| `OTG_HS_DAINTMSK` | `0x81C` | OTG_HS all endpoints interrupt mask register (OTG_HS_DAINTMSK) | [OTG_HS_DAINTMSK.json](../registers_json/OTG_HS_DAINTMSK.json) |
| `OTG_HS_DCFG` | `0x800` | Device-mode registers OTG_HS device configuration register (OTG_HS_DCFG) | [OTG_HS_DCFG.json](../registers_json/OTG_HS_DCFG.json) |
| `OTG_HS_DCT` | `0x804` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_DCT Register | [OTG_HS_DCT.json](../registers_json/OTG_HS_DCT.json) |
| `OTG_HS_DCTL` | `0x804` | OTG_HS device control register (OTG_HS_DCTL) | [OTG_HS_DCTL.json](../registers_json/OTG_HS_DCTL.json) |
| `OTG_HS_DEA` | `0x83C` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_DEA Register | [OTG_HS_DEA.json](../registers_json/OTG_HS_DEA.json) |
| `OTG_HS_DEACHINT` | `0x0838` | OTG_HS device each endpoint interrupt register (OTG_HS_DEACHINT) | [OTG_HS_DEACHINT.json](../registers_json/OTG_HS_DEACHINT.json) |
| `OTG_HS_DEACHINTMSK` | `0x083C` | OTG_HS device each endpoint interrupt register mask (OTG_HS_DEACHINTMSK) | [OTG_HS_DEACHINTMSK.json](../registers_json/OTG_HS_DEACHINTMSK.json) |
| `OTG_HS_DIE` | `0x97C` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_DIE Register | [OTG_HS_DIE.json](../registers_json/OTG_HS_DIE.json) |
| `OTG_HS_DIEPEACHMSK1` | `0x844` | OTG_HS device each in endpoint-1 interrupt register (OTG_HS_DIEPEACHMSK1) | [OTG_HS_DIEPEACHMSK1.json](../registers_json/OTG_HS_DIEPEACHMSK1.json) |
| `OTG_HS_DIEPEMPMSK` | `0x834` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_DIEPEMPMSK Register | [OTG_HS_DIEPEMPMSK.json](../registers_json/OTG_HS_DIEPEMPMSK.json) |
| `OTG_HS_DIEPINTX` | `0x00` | This register works with each of the Device IN endpoint interrupt (OTG_HS_DIEPINTX) | [OTG_HS_DIEPINTX.json](../registers_json/OTG_HS_DIEPINTX.json) |
| `OTG_HS_DIEPMSK` | `0x810` | 1436/1741 RM0090 Rev 22 OTG_HS device IN endpoint common interrupt mask register (OTG_HS_DIEPMSK) | [OTG_HS_DIEPMSK.json](../registers_json/OTG_HS_DIEPMSK.json) |
| `OTG_HS_DIEPTSIZ0` | `0x910` | OTG_HS device IN endpoint 0 transfer size register (OTG_HS_DIEPTSIZ0) | [OTG_HS_DIEPTSIZ0.json](../registers_json/OTG_HS_DIEPTSIZ0.json) |
| `OTG_HS_DIEPTSIZX` | `0x00` | OTG_HS device endpoint-x transfer size register (OTG_HS_DIEPTSIZX) | [OTG_HS_DIEPTSIZX.json](../registers_json/OTG_HS_DIEPTSIZX.json) |
| `OTG_HS_DIEPTXFX` | `0x00` | 1418/1741 RM0090 Rev 22 OTG_HS device IN endpoint transmit FIFO size register (OTG_HS_DIEPTXFX) | [OTG_HS_DIEPTXFX.json](../registers_json/OTG_HS_DIEPTXFX.json) |
| `OTG_HS_DO` | `0xB7C` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_DO Register | [OTG_HS_DO.json](../registers_json/OTG_HS_DO.json) |
| `OTG_HS_DOEPCTL0` | `0xB00` | 1448/1741 RM0090 Rev 22 OTG_HS device control OUT endpoint 0 control register (OTG_HS_DOEPCTL0) | [OTG_HS_DOEPCTL0.json](../registers_json/OTG_HS_DOEPCTL0.json) |
| `OTG_HS_DOEPEACHMSK1` | `0x884` | 1444/1741 RM0090 Rev 22 OTG_HS device each OUT endpoint-1 interrupt register (OTG_HS_DOEPEACHMSK1) | [OTG_HS_DOEPEACHMSK1.json](../registers_json/OTG_HS_DOEPEACHMSK1.json) |
| `OTG_HS_DOEPINTX` | `0x00` | This register works with each of the Device OUT endpoint interrupt (OTG_HS_DOEPINTX) | [OTG_HS_DOEPINTX.json](../registers_json/OTG_HS_DOEPINTX.json) |
| `OTG_HS_DOEPMSK` | `0x814` | OTG_HS device OUT endpoint common interrupt mask register (OTG_HS_DOEPMSK) | [OTG_HS_DOEPMSK.json](../registers_json/OTG_HS_DOEPMSK.json) |
| `OTG_HS_DOEPSIZ0` | `0xB10` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_DOEPSIZ0 Register | [OTG_HS_DOEPSIZ0.json](../registers_json/OTG_HS_DOEPSIZ0.json) |
| `OTG_HS_DOEPTSIZ0` | `0xB10` | 1456/1741 RM0090 Rev 22 OTG_HS device OUT endpoint 0 transfer size register (OTG_HS_DOEPTSIZ0) | [OTG_HS_DOEPTSIZ0.json](../registers_json/OTG_HS_DOEPTSIZ0.json) |
| `OTG_HS_DOEPTSIZX` | `0x00` | OTG_HS device endpoint-x transfer size register (OTG_HS_DOEPTSIZX) | [OTG_HS_DOEPTSIZX.json](../registers_json/OTG_HS_DOEPTSIZX.json) |
| `OTG_HS_DST` | `0x808` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_DST Register | [OTG_HS_DST.json](../registers_json/OTG_HS_DST.json) |
| `OTG_HS_DSTS` | `0x808` | OTG_HS device status register (OTG_HS_DSTS) | [OTG_HS_DSTS.json](../registers_json/OTG_HS_DSTS.json) |
| `OTG_HS_DTH` | `0x830` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_DTH Register | [OTG_HS_DTH.json](../registers_json/OTG_HS_DTH.json) |
| `OTG_HS_DTHRCTL` | `0x0830` | OTG_HS Device threshold control register (OTG_HS_DTHRCTL) | [OTG_HS_DTHRCTL.json](../registers_json/OTG_HS_DTHRCTL.json) |
| `OTG_HS_DTX` | `0x918` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_DTX Register | [OTG_HS_DTX.json](../registers_json/OTG_HS_DTX.json) |
| `OTG_HS_DVB` | `0x828` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_DVB Register | [OTG_HS_DVB.json](../registers_json/OTG_HS_DVB.json) |
| `OTG_HS_DVBUSDIS` | `0x0828` | OTG_HS device VBUS discharge time register (OTG_HS_DVBUSDIS) | [OTG_HS_DVBUSDIS.json](../registers_json/OTG_HS_DVBUSDIS.json) |
| `OTG_HS_DVBUSPULSE` | `0x082C` | 1440/1741 RM0090 Rev 22 OTG_HS device VBUS pulsing time register (OTG_HS_DVBUSPULSE) | [OTG_HS_DVBUSPULSE.json](../registers_json/OTG_HS_DVBUSPULSE.json) |
| `OTG_HS_GA` | `0x008` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_GA Register | [OTG_HS_GA.json](../registers_json/OTG_HS_GA.json) |
| `OTG_HS_GAHBCFG` | `0x008` | OTG_HS AHB configuration register (OTG_HS_GAHBCFG) | [OTG_HS_GAHBCFG.json](../registers_json/OTG_HS_GAHBCFG.json) |
| `OTG_HS_GC` | `0x038` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_GC Register | [OTG_HS_GC.json](../registers_json/OTG_HS_GC.json) |
| `OTG_HS_GCCFG` | `0x038` | 1416/1741 RM0090 Rev 22 OTG_HS general core configuration register (OTG_HS_GCCFG) | [OTG_HS_GCCFG.json](../registers_json/OTG_HS_GCCFG.json) |
| `OTG_HS_GI2` | `0x030` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_GI2 Register | [OTG_HS_GI2.json](../registers_json/OTG_HS_GI2.json) |
| `OTG_HS_GIN` | `0x014` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_GIN Register | [OTG_HS_GIN.json](../registers_json/OTG_HS_GIN.json) |
| `OTG_HS_GINTMSK` | `0x018` | 1410/1741 RM0090 Rev 22 OTG_HS interrupt mask register (OTG_HS_GINTMSK) | [OTG_HS_GINTMSK.json](../registers_json/OTG_HS_GINTMSK.json) |
| `OTG_HS_GINTSTS` | `0x014` | 1406/1741 RM0090 Rev 22 OTG_HS core interrupt register (OTG_HS_GINTSTS) | [OTG_HS_GINTSTS.json](../registers_json/OTG_HS_GINTSTS.json) |
| `OTG_HS_GN` | `0x028` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_GN Register | [OTG_HS_GN.json](../registers_json/OTG_HS_GN.json) |
| `OTG_HS_GNPTXFSIZ` | `0x028` | OTG_HS nonperiodic transmit FIFO size/Endpoint 0 transmit FIFO size register (OTG_HS_GNPTXFSIZ) | [OTG_HS_GNPTXFSIZ.json](../registers_json/OTG_HS_GNPTXFSIZ.json) |
| `OTG_HS_GNPTXSTS` | `0x02C` | OTG_HS nonperiodic transmit FIFO/queue status register (OTG_HS_GNPTXSTS) | [OTG_HS_GNPTXSTS.json](../registers_json/OTG_HS_GNPTXSTS.json) |
| `OTG_HS_GO` | `0x000` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_GO Register | [OTG_HS_GO.json](../registers_json/OTG_HS_GO.json) |
| `OTG_HS_GOTGCTL` | `0x000` | OTG_HS control and status register (OTG_HS_GOTGCTL) | [OTG_HS_GOTGCTL.json](../registers_json/OTG_HS_GOTGCTL.json) |
| `OTG_HS_GOTGINT` | `0x04` | OTG_HS interrupt register (OTG_HS_GOTGINT) | [OTG_HS_GOTGINT.json](../registers_json/OTG_HS_GOTGINT.json) |
| `OTG_HS_GR` | `0x010` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_GR Register | [OTG_HS_GR.json](../registers_json/OTG_HS_GR.json) |
| `OTG_HS_GRSTCTL` | `0x010` | OTG_HS reset register (OTG_HS_GRSTCTL) | [OTG_HS_GRSTCTL.json](../registers_json/OTG_HS_GRSTCTL.json) |
| `OTG_HS_GRXFSIZ` | `0x024` | OTG_HS Receive FIFO size register (OTG_HS_GRXFSIZ) | [OTG_HS_GRXFSIZ.json](../registers_json/OTG_HS_GRXFSIZ.json) |
| `OTG_HS_GRXSTSP` | `0x00` | OTG_HS Receive status debug read/OTG status read and pop registers (OTG_HS_GRXSTSP) | [OTG_HS_GRXSTSP.json](../registers_json/OTG_HS_GRXSTSP.json) |
| `OTG_HS_GRXSTSR` | `0x01C` | OTG_HS Receive status debug read/OTG status read and pop registers (OTG_HS_GRXSTSR) | [OTG_HS_GRXSTSR.json](../registers_json/OTG_HS_GRXSTSR.json) |
| `OTG_HS_GU` | `0x00C` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_GU Register | [OTG_HS_GU.json](../registers_json/OTG_HS_GU.json) |
| `OTG_HS_GUSBCFG` | `0x00C` | 1400/1741 RM0090 Rev 22 OTG_HS USB configuration register (OTG_HS_GUSBCFG) | [OTG_HS_GUSBCFG.json](../registers_json/OTG_HS_GUSBCFG.json) |
| `OTG_HS_HAI` | `0x414` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_HAI Register | [OTG_HS_HAI.json](../registers_json/OTG_HS_HAI.json) |
| `OTG_HS_HAINT` | `0x414` | 1422/1741 RM0090 Rev 22 OTG_HS Host all channels interrupt register (OTG_HS_HAINT) | [OTG_HS_HAINT.json](../registers_json/OTG_HS_HAINT.json) |
| `OTG_HS_HAINTMSK` | `0x418` | OTG_HS host all channels interrupt mask register (OTG_HS_HAINTMSK) | [OTG_HS_HAINTMSK.json](../registers_json/OTG_HS_HAINTMSK.json) |
| `OTG_HS_HC` | `0x500` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_HC Register | [OTG_HS_HC.json](../registers_json/OTG_HS_HC.json) |
| `OTG_HS_HCCHARX` | `0x00` | OTG_HS host channel-x characteristics register (OTG_HS_HCCHARX) | [OTG_HS_HCCHARX.json](../registers_json/OTG_HS_HCCHARX.json) |
| `OTG_HS_HCDMAX` | `0x00` | OTG_HS_HCDMAx 0x514 OTG_HS host channel-x DMA address register (OTG_HS_HCDMAX) | [OTG_HS_HCDMAX.json](../registers_json/OTG_HS_HCDMAX.json) |
| `OTG_HS_HCF` | `0x400` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_HCF Register | [OTG_HS_HCF.json](../registers_json/OTG_HS_HCF.json) |
| `OTG_HS_HCFG` | `0x400` | OTG_HS host configuration register (OTG_HS_HCFG) | [OTG_HS_HCFG.json](../registers_json/OTG_HS_HCFG.json) |
| `OTG_HS_HCI` | `0x66C` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_HCI Register | [OTG_HS_HCI.json](../registers_json/OTG_HS_HCI.json) |
| `OTG_HS_HCINTMSKX` | `0x00` | OTG_HS host channel-x interrupt mask register (OTG_HS_HCINTMSKX) | [OTG_HS_HCINTMSKX.json](../registers_json/OTG_HS_HCINTMSKX.json) |
| `OTG_HS_HCS` | `0x664` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_HCS Register | [OTG_HS_HCS.json](../registers_json/OTG_HS_HCS.json) |
| `OTG_HS_HCSPLTX` | `0x00` | OTG_HS_HCSPLTx 0x504 OTG_HS host channel-x split control register (OTG_HS_HCSPLTX) | [OTG_HS_HCSPLTX.json](../registers_json/OTG_HS_HCSPLTX.json) |
| `OTG_HS_HCT` | `0x510` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_HCT Register | [OTG_HS_HCT.json](../registers_json/OTG_HS_HCT.json) |
| `OTG_HS_HCTSIZX` | `0x00` | OTG_HS_HCTSIZx 0x510 OTG_HS host channel-x transfer size register (OTG_HS_HCTSIZX) | [OTG_HS_HCTSIZX.json](../registers_json/OTG_HS_HCTSIZX.json) |
| `OTG_HS_HFI` | `0x404` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_HFI Register | [OTG_HS_HFI.json](../registers_json/OTG_HS_HFI.json) |
| `OTG_HS_HFIR` | `0x404` | 1420/1741 RM0090 Rev 22 OTG_HS Host frame interval register (OTG_HS_HFIR) | [OTG_HS_HFIR.json](../registers_json/OTG_HS_HFIR.json) |
| `OTG_HS_HFN` | `0x408` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_HFN Register | [OTG_HS_HFN.json](../registers_json/OTG_HS_HFN.json) |
| `OTG_HS_HFNUM` | `0x408` | OTG_HS host frame number/frame time remaining register (OTG_HS_HFNUM) | [OTG_HS_HFNUM.json](../registers_json/OTG_HS_HFNUM.json) |
| `OTG_HS_HPR` | `0x440` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_HPR Register | [OTG_HS_HPR.json](../registers_json/OTG_HS_HPR.json) |
| `OTG_HS_HPRT` | `0x440` | OTG_HS host port control and status register (OTG_HS_HPRT) | [OTG_HS_HPRT.json](../registers_json/OTG_HS_HPRT.json) |
| `OTG_HS_HPT` | `0x100` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_HPT Register | [OTG_HS_HPT.json](../registers_json/OTG_HS_HPT.json) |
| `OTG_HS_HPTXFSIZ` | `0x100` | OTG_HS Host periodic transmit FIFO size register (OTG_HS_HPTXFSIZ) | [OTG_HS_HPTXFSIZ.json](../registers_json/OTG_HS_HPTXFSIZ.json) |
| `OTG_HS_HPTXSTS` | `0x410` | OTG_HS_Host periodic transmit FIFO/queue status register (OTG_HS_HPTXSTS) | [OTG_HS_HPTXSTS.json](../registers_json/OTG_HS_HPTXSTS.json) |
| `OTG_HS_PC` | `0xE00` | USB On-The-Go High-Speed (OTG_HS) OTG_HS_PC Register | [OTG_HS_PC.json](../registers_json/OTG_HS_PC.json) |
| `OTG_HS_PCGCCTL` | `0xE00` | OTG_HS power and cl ock gating control register (OTG_HS_PCGCCTL) | [OTG_HS_PCGCCTL.json](../registers_json/OTG_HS_PCGCCTL.json) |
| `OTG_HS_TX0FSIZ` | `0x028` | OTG_HS nonperiodic transmit FIFO size/Endpoint 0 transmit FIFO size register (OTG_HS_TX0FSIZ) | [OTG_HS_TX0FSIZ.json](../registers_json/OTG_HS_TX0FSIZ.json) |