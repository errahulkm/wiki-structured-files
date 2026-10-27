# Ethernet MAC (ETH)

## 1. Overview & Key Features
The Ethernet MAC (ETH) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 36](../chapters/chapter_36.md) (Pages 1113 - 1227).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 36](../chapters/chapter_36.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Ethernet MAC (ETH) Architectural Block Diagram](../figures/eth_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Ethernet MAC (ETH) Configuration & Parameter Matrix](../tables/eth_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `ETH_DMABMR` | `0x1000` | Ethernet DMA bus mode register (ETH_DMABMR) | [ETH_DMABMR.json](../registers_json/ETH_DMABMR.json) |
| `ETH_DMACHRBAR` | `0x1054` | Ethernet DMA current host receive buffer address register (ETH_DMACHRBAR) | [ETH_DMACHRBAR.json](../registers_json/ETH_DMACHRBAR.json) |
| `ETH_DMACHRDR` | `0x104C` | Ethernet DMA current host receive descriptor register (ETH_DMACHRDR) | [ETH_DMACHRDR.json](../registers_json/ETH_DMACHRDR.json) |
| `ETH_DMACHTBAR` | `0x1050` | Ethernet DMA current host transmit buffer address register (ETH_DMACHTBAR) | [ETH_DMACHTBAR.json](../registers_json/ETH_DMACHTBAR.json) |
| `ETH_DMACHTDR` | `0x1048` | Ethernet DMA current host transmit descriptor register (ETH_DMACHTDR) | [ETH_DMACHTDR.json](../registers_json/ETH_DMACHTDR.json) |
| `ETH_DMAIER` | `0x101C` | Ethernet DMA interrupt enable register (ETH_DMAIER) | [ETH_DMAIER.json](../registers_json/ETH_DMAIER.json) |
| `ETH_DMAMFB` | `0x1020` | Ethernet MAC (ETH) ETH_DMAMFB Register | [ETH_DMAMFB.json](../registers_json/ETH_DMAMFB.json) |
| `ETH_DMAMFBOCR` | `0x1020` | Ethernet DMA missed frame and buffer overflow counter register (ETH_DMAMFBOCR) | [ETH_DMAMFBOCR.json](../registers_json/ETH_DMAMFBOCR.json) |
| `ETH_DMAOMR` | `0x1018` | 1216/1741 RM0090 Rev 22 Ethernet DMA operation mode register (ETH_DMAOMR) | [ETH_DMAOMR.json](../registers_json/ETH_DMAOMR.json) |
| `ETH_DMARDLA` | `0x100C` | Ethernet MAC (ETH) ETH_DMARDLA Register | [ETH_DMARDLA.json](../registers_json/ETH_DMARDLA.json) |
| `ETH_DMARDLAR` | `0x100C` | Ethernet DMA receive descriptor list address register (ETH_DMARDLAR) | [ETH_DMARDLAR.json](../registers_json/ETH_DMARDLAR.json) |
| `ETH_DMARPDR` | `0x1008` | EHERNET DMA receive poll demand register (ETH_DMARPDR) | [ETH_DMARPDR.json](../registers_json/ETH_DMARPDR.json) |
| `ETH_DMARSWTR` | `0x1024` | 1222/1741 RM0090 Rev 22 Ethernet DMA receive status watchdog timer register (ETH_DMARSWTR) | [ETH_DMARSWTR.json](../registers_json/ETH_DMARSWTR.json) |
| `ETH_DMASR` | `0x1014` | 1214/1741 RM0090 Rev 22 Ethernet DMA status register (ETH_DMASR) | [ETH_DMASR.json](../registers_json/ETH_DMASR.json) |
| `ETH_DMATDLA` | `0x1010` | Ethernet MAC (ETH) ETH_DMATDLA Register | [ETH_DMATDLA.json](../registers_json/ETH_DMATDLA.json) |
| `ETH_DMATDLAR` | `0x1010` | Ethernet DMA transmit descriptor list address register (ETH_DMATDLAR) | [ETH_DMATDLAR.json](../registers_json/ETH_DMATDLAR.json) |
| `ETH_DMATPDR` | `0x1004` | 1212/1741 RM0090 Rev 22 Ethernet DMA transmit poll demand register (ETH_DMATPDR) | [ETH_DMATPDR.json](../registers_json/ETH_DMATPDR.json) |
| `ETH_MACA0HR` | `0x0040` | Ethernet MAC address 0 high register (ETH_MACA0HR) | [ETH_MACA0HR.json](../registers_json/ETH_MACA0HR.json) |
| `ETH_MACA0LR` | `0x0044` | Ethernet MAC address 0 low register (ETH_MACA0LR) | [ETH_MACA0LR.json](../registers_json/ETH_MACA0LR.json) |
| `ETH_MACA1HR` | `0x0048` | Ethernet MAC address 1 high register (ETH_MACA1HR) | [ETH_MACA1HR.json](../registers_json/ETH_MACA1HR.json) |
| `ETH_MACA1LR` | `0x004C` | 1196/1741 RM0090 Rev 22 Ethernet MAC address1 low register (ETH_MACA1LR) | [ETH_MACA1LR.json](../registers_json/ETH_MACA1LR.json) |
| `ETH_MACA2HR` | `0x0050` | Ethernet MAC address 2 high register (ETH_MACA2HR) | [ETH_MACA2HR.json](../registers_json/ETH_MACA2HR.json) |
| `ETH_MACA2LR` | `0x0054` | Ethernet MAC address 2 low register (ETH_MACA2LR) | [ETH_MACA2LR.json](../registers_json/ETH_MACA2LR.json) |
| `ETH_MACA3HR` | `0x0058` | Ethernet MAC address 3 high register (ETH_MACA3HR) | [ETH_MACA3HR.json](../registers_json/ETH_MACA3HR.json) |
| `ETH_MACA3LR` | `0x005C` | 1198/1741 RM0090 Rev 22 Ethernet MAC address 3 low register (ETH_MACA3LR) | [ETH_MACA3LR.json](../registers_json/ETH_MACA3LR.json) |
| `ETH_MACCR` | `0x0000` | MAC register description Ethernet MAC configuration register (ETH_MACCR) | [ETH_MACCR.json](../registers_json/ETH_MACCR.json) |
| `ETH_MACDBGR` | `0x0034` | 1192/1741 RM0090 Rev 22 Ethernet MAC debug register (ETH_MACDBGR) | [ETH_MACDBGR.json](../registers_json/ETH_MACDBGR.json) |
| `ETH_MACFCR` | `0x0018` | Ethernet MAC flow control register (ETH_MACFCR) | [ETH_MACFCR.json](../registers_json/ETH_MACFCR.json) |
| `ETH_MACFFR` | `0x0004` | Ethernet MAC frame filter register (ETH_MACFFR) | [ETH_MACFFR.json](../registers_json/ETH_MACFFR.json) |
| `ETH_MACHTHR` | `0x0008` | Ethernet MAC hash table high register (ETH_MACHTHR) | [ETH_MACHTHR.json](../registers_json/ETH_MACHTHR.json) |
| `ETH_MACHTLR` | `0x000C` | 1186/1741 RM0090 Rev 22 Ethernet MAC hash table low register (ETH_MACHTLR) | [ETH_MACHTLR.json](../registers_json/ETH_MACHTLR.json) |
| `ETH_MACIMR` | `0x003C` | 1194/1741 RM0090 Rev 22 Ethernet MAC interrupt mask register (ETH_MACIMR) | [ETH_MACIMR.json](../registers_json/ETH_MACIMR.json) |
| `ETH_MACMIIAR` | `0x0010` | Ethernet MAC MII address register (ETH_MACMIIAR) | [ETH_MACMIIAR.json](../registers_json/ETH_MACMIIAR.json) |
| `ETH_MACMIIDR` | `0x0014` | Ethernet MAC MII data register (ETH_MACMIIDR) | [ETH_MACMIIDR.json](../registers_json/ETH_MACMIIDR.json) |
| `ETH_MACPMTCSR` | `0x002C` | Ethernet MAC PMT control and status register (ETH_MACPMTCSR) | [ETH_MACPMTCSR.json](../registers_json/ETH_MACPMTCSR.json) |
| `ETH_MACRWUFFR` | `0x0028` | 1190/1741 RM0090 Rev 22 Ethernet MAC remote wake-up frame filter register (ETH_MACRWUFFR) | [ETH_MACRWUFFR.json](../registers_json/ETH_MACRWUFFR.json) |
| `ETH_MACSR` | `0x0038` | Ethernet MAC interrupt status register (ETH_MACSR) | [ETH_MACSR.json](../registers_json/ETH_MACSR.json) |
| `ETH_MACVLANTR` | `0x001C` | Ethernet MAC VLAN tag register (ETH_MACVLANTR) | [ETH_MACVLANTR.json](../registers_json/ETH_MACVLANTR.json) |
| `ETH_MMCCR` | `0x0100` | MMC register description Ethernet MMC control register (ETH_MMCCR) | [ETH_MMCCR.json](../registers_json/ETH_MMCCR.json) |
| `ETH_MMCRFAE` | `0x198` | Ethernet MAC (ETH) ETH_MMCRFAE Register | [ETH_MMCRFAE.json](../registers_json/ETH_MMCRFAE.json) |
| `ETH_MMCRFAECR` | `0x0198` | Ethernet MMC received frames with alignment error counter register (ETH_MMCRFAECR) | [ETH_MMCRFAECR.json](../registers_json/ETH_MMCRFAECR.json) |
| `ETH_MMCRFC` | `0x194` | Ethernet MAC (ETH) ETH_MMCRFC Register | [ETH_MMCRFC.json](../registers_json/ETH_MMCRFC.json) |
| `ETH_MMCRFCECR` | `0x0194` | Ethernet MMC received frames with CRC error counter register (ETH_MMCRFCECR) | [ETH_MMCRFCECR.json](../registers_json/ETH_MMCRFCECR.json) |
| `ETH_MMCRGU` | `0x1C4` | Ethernet MAC (ETH) ETH_MMCRGU Register | [ETH_MMCRGU.json](../registers_json/ETH_MMCRGU.json) |
| `ETH_MMCRGUFCR` | `0x01C4` | MMC received good unicast frames counter register (ETH_MMCRGUFCR) | [ETH_MMCRGUFCR.json](../registers_json/ETH_MMCRGUFCR.json) |
| `ETH_MMCRIMR` | `0x010C` | Ethernet MMC receive interrupt mask register (ETH_MMCRIMR) | [ETH_MMCRIMR.json](../registers_json/ETH_MMCRIMR.json) |
| `ETH_MMCRIR` | `0x0104` | Ethernet MMC receive interrupt register (ETH_MMCRIR) | [ETH_MMCRIR.json](../registers_json/ETH_MMCRIR.json) |
| `ETH_MMCTGF` | `0x150` | Ethernet MAC (ETH) ETH_MMCTGF Register | [ETH_MMCTGF.json](../registers_json/ETH_MMCTGF.json) |
| `ETH_MMCTGFCR` | `0x0168` | Ethernet MMC transmitted good frames counter register (ETH_MMCTGFCR) | [ETH_MMCTGFCR.json](../registers_json/ETH_MMCTGFCR.json) |
| `ETH_MMCTGFMSCCR` | `0x0150` | Ethernet MMC transmitted good frames after more than a single collision counter register (ETH_MMCTGFMSCCR) | [ETH_MMCTGFMSCCR.json](../registers_json/ETH_MMCTGFMSCCR.json) |
| `ETH_MMCTGFS` | `0x14C` | Ethernet MAC (ETH) ETH_MMCTGFS Register | [ETH_MMCTGFS.json](../registers_json/ETH_MMCTGFS.json) |
| `ETH_MMCTGFSCCR` | `0x014C` | 1202/1741 RM0090 Rev 22 Ethernet MMC transmitted good frames after a single collision counter register (ETH_MMCTGFSCCR) | [ETH_MMCTGFSCCR.json](../registers_json/ETH_MMCTGFSCCR.json) |
| `ETH_MMCTIMR` | `0x0110` | Ethernet MMC transmit interrupt mask register (ETH_MMCTIMR) | [ETH_MMCTIMR.json](../registers_json/ETH_MMCTIMR.json) |
| `ETH_MMCTIR` | `0x0108` | 1200/1741 RM0090 Rev 22 Ethernet MMC transmit interrupt register (ETH_MMCTIR) | [ETH_MMCTIR.json](../registers_json/ETH_MMCTIR.json) |
| `ETH_PTPPPSC` | `0x72C` | Ethernet MAC (ETH) ETH_PTPPPSC Register | [ETH_PTPPPSC.json](../registers_json/ETH_PTPPPSC.json) |
| `ETH_PTPPPSCR` | `0x072C` | 1210/1741 RM0090 Rev 22 Ethernet PTP PPS control register (ETH_PTPPPSCR) | [ETH_PTPPPSCR.json](../registers_json/ETH_PTPPPSCR.json) |
| `ETH_PTPSSIR` | `0x0704` | 1206/1741 RM0090 Rev 22 Ethernet PTP subsecond increment register (ETH_PTPSSIR) | [ETH_PTPSSIR.json](../registers_json/ETH_PTPSSIR.json) |
| `ETH_PTPTSAR` | `0x0718` | Ethernet PTP time stamp addend register (ETH_PTPTSAR) | [ETH_PTPTSAR.json](../registers_json/ETH_PTPTSAR.json) |
| `ETH_PTPTSCR` | `0x0700` | Ethernet PTP time stamp control register (ETH_PTPTSCR) | [ETH_PTPTSCR.json](../registers_json/ETH_PTPTSCR.json) |
| `ETH_PTPTSHR` | `0x0708` | Ethernet PTP time stamp high register (ETH_PTPTSHR) | [ETH_PTPTSHR.json](../registers_json/ETH_PTPTSHR.json) |
| `ETH_PTPTSHU` | `0x710` | Ethernet MAC (ETH) ETH_PTPTSHU Register | [ETH_PTPTSHU.json](../registers_json/ETH_PTPTSHU.json) |
| `ETH_PTPTSHUR` | `0x0710` | Ethernet PTP time stamp high update register (ETH_PTPTSHUR) | [ETH_PTPTSHUR.json](../registers_json/ETH_PTPTSHUR.json) |
| `ETH_PTPTSLR` | `0x070C` | Ethernet PTP time stamp low register (ETH_PTPTSLR) | [ETH_PTPTSLR.json](../registers_json/ETH_PTPTSLR.json) |
| `ETH_PTPTSLU` | `0x714` | Ethernet MAC (ETH) ETH_PTPTSLU Register | [ETH_PTPTSLU.json](../registers_json/ETH_PTPTSLU.json) |
| `ETH_PTPTSLUR` | `0x0714` | 1208/1741 RM0090 Rev 22 Ethernet PTP time stamp low update register (ETH_PTPTSLUR) | [ETH_PTPTSLUR.json](../registers_json/ETH_PTPTSLUR.json) |
| `ETH_PTPTSSR` | `0x0728` | Ethernet PTP time stamp status register (ETH_PTPTSSR) | [ETH_PTPTSSR.json](../registers_json/ETH_PTPTSSR.json) |
| `ETH_PTPTTHR` | `0x071C` | Ethernet PTP target time high register (ETH_PTPTTHR) | [ETH_PTPTTHR.json](../registers_json/ETH_PTPTTHR.json) |
| `ETH_PTPTTLR` | `0x0720` | Ethernet PTP target time low register (ETH_PTPTTLR) | [ETH_PTPTTLR.json](../registers_json/ETH_PTPTTLR.json) |