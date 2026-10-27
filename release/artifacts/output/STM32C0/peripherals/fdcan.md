# FDCAN Interface

## 1. Overview & Key Features
The FDCAN Interface block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 28](../chapters/chapter_28.md) (Pages 888 - 953).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 28](../chapters/chapter_28.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: FDCAN Interface Architectural Block Diagram](../figures/fdcan_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: FDCAN Interface Configuration & Parameter Matrix](../tables/fdcan_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `FDCAN_CCCR` | `0x0018` | FDCAN CC control register (FDCAN_CCCR) | [FDCAN_CCCR.json](../registers_json/FDCAN_CCCR.json) |
| `FDCAN_CKDIV` | `0x0100` | FDCAN CFG clock divi der register (FDCAN_CKDIV) | [FDCAN_CKDIV.json](../registers_json/FDCAN_CKDIV.json) |
| `FDCAN_CREL` | `0x0000` | FDCAN core release register (FDCAN_CREL) | [FDCAN_CREL.json](../registers_json/FDCAN_CREL.json) |
| `FDCAN_DBTP` | `0x000C` | FDCAN data bit timing and prescaler register (FDCAN_DBTP) | [FDCAN_DBTP.json](../registers_json/FDCAN_DBTP.json) |
| `FDCAN_ECR` | `0x0040` | FDCAN error count er register (FDCAN_ECR) | [FDCAN_ECR.json](../registers_json/FDCAN_ECR.json) |
| `FDCAN_ENDN` | `0x0004` | FDCAN endian re gister (FDCAN_ENDN) | [FDCAN_ENDN.json](../registers_json/FDCAN_ENDN.json) |
| `FDCAN_HPMS` | `0x0088` | FDCAN high-priority messag e status register (FDCAN_HPMS) | [FDCAN_HPMS.json](../registers_json/FDCAN_HPMS.json) |
| `FDCAN_IE` | `0x0054` | FDCAN interrupt en able register (FDCAN_IE) | [FDCAN_IE.json](../registers_json/FDCAN_IE.json) |
| `FDCAN_ILE` | `0x005C` | FDCAN interrupt line enable register (FDCAN_ILE) | [FDCAN_ILE.json](../registers_json/FDCAN_ILE.json) |
| `FDCAN_ILS` | `0x0058` | FDCAN interrupt line select register (FDCAN_ILS) | [FDCAN_ILS.json](../registers_json/FDCAN_ILS.json) |
| `FDCAN_IR` | `0x0050` | FDCAN interrupt register (FDCAN_IR) | [FDCAN_IR.json](../registers_json/FDCAN_IR.json) |
| `FDCAN_NBTP` | `0x001C` | FDCAN nominal bit timing a nd prescaler register (FDCAN_NBTP) | [FDCAN_NBTP.json](../registers_json/FDCAN_NBTP.json) |
| `FDCAN_PSR` | `0x0044` | FDCAN protocol st atus register (FDCAN_PSR) | [FDCAN_PSR.json](../registers_json/FDCAN_PSR.json) |
| `FDCAN_RWD` | `0x0014` | FDCAN RAM watchdog register (FDCAN_RWD) | [FDCAN_RWD.json](../registers_json/FDCAN_RWD.json) |
| `FDCAN_RXF0A` | `0x0094` | CAN Rx FIFO 0 acknowle dge register (FDCAN_RXF0A) | [FDCAN_RXF0A.json](../registers_json/FDCAN_RXF0A.json) |
| `FDCAN_RXF0S` | `0x0090` | FDCAN Rx FIFO 0 stat us register (FDCAN_RXF0S) | [FDCAN_RXF0S.json](../registers_json/FDCAN_RXF0S.json) |
| `FDCAN_RXF1A` | `0x009C` | FDCAN Rx FIFO 1 ack nowledge register (FDCAN_RXF1A) | [FDCAN_RXF1A.json](../registers_json/FDCAN_RXF1A.json) |
| `FDCAN_RXF1S` | `0x0098` | FDCAN Rx FIFO 1 stat us register (FDCAN_RXF1S) | [FDCAN_RXF1S.json](../registers_json/FDCAN_RXF1S.json) |
| `FDCAN_RXGFC` | `0x00` | FDCAN global filter conf iguration register (FDCAN_RXGFC) | [FDCAN_RXGFC.json](../registers_json/FDCAN_RXGFC.json) |
| `FDCAN_TDCR` | `0x0048` | FDCAN transmitter delay co mpensation register (FDCAN_TDCR) | [FDCAN_TDCR.json](../registers_json/FDCAN_TDCR.json) |
| `FDCAN_TEST` | `0x0010` | FDCAN test register (FDCAN_TEST) | [FDCAN_TEST.json](../registers_json/FDCAN_TEST.json) |
| `FDCAN_TOCC` | `0x0028` | FDCAN timeout counter c onfiguration register (FDCAN_TOCC) | [FDCAN_TOCC.json](../registers_json/FDCAN_TOCC.json) |
| `FDCAN_TOCV` | `0x002C` | FDCAN timeout counter value register (FDCAN_TOCV) | [FDCAN_TOCV.json](../registers_json/FDCAN_TOCV.json) |
| `FDCAN_TSCC` | `0x0020` | FDCAN timestamp counter c onfiguration register (FDCAN_TSCC) | [FDCAN_TSCC.json](../registers_json/FDCAN_TSCC.json) |
| `FDCAN_TSCV` | `0x0024` | FDCAN timestamp counter value register (FDCAN_TSCV) | [FDCAN_TSCV.json](../registers_json/FDCAN_TSCV.json) |
| `FDCAN_TXBAR` | `0x00CC` | FDCAN Tx buffer add re quest register (FDCAN_TXBAR) | [FDCAN_TXBAR.json](../registers_json/FDCAN_TXBAR.json) |
| `FDCAN_TXBC` | `0x00C0` | FDCAN Tx buffer confi guration register (FDCAN_TXBC) | [FDCAN_TXBC.json](../registers_json/FDCAN_TXBC.json) |
| `FDCAN_TXBCF` | `0x00D8` | FDCAN Tx buffer cancellation finished register (FDCAN_TXBCF) | [FDCAN_TXBCF.json](../registers_json/FDCAN_TXBCF.json) |
| `FDCAN_TXBCIE` | `0x00E0` | FDCAN Tx buffer cancellation fi nished interrupt enable register (FDCAN_TXBCIE) | [FDCAN_TXBCIE.json](../registers_json/FDCAN_TXBCIE.json) |
| `FDCAN_TXBCR` | `0x00D0` | FDCAN Tx buffer cancellati on request register (FDCAN_TXBCR) | [FDCAN_TXBCR.json](../registers_json/FDCAN_TXBCR.json) |
| `FDCAN_TXBRP` | `0x00C8` | FDCAN Tx buffer request pending register (FDCAN_TXBRP) | [FDCAN_TXBRP.json](../registers_json/FDCAN_TXBRP.json) |
| `FDCAN_TXBTIE` | `0x00DC` | FDCAN Tx buffer transmi ssion interrupt enable register (FDCAN_TXBTIE) | [FDCAN_TXBTIE.json](../registers_json/FDCAN_TXBTIE.json) |
| `FDCAN_TXBTO` | `0x00D4` | FDCAN Tx buffer transmission occurred register (FDCAN_TXBTO) | [FDCAN_TXBTO.json](../registers_json/FDCAN_TXBTO.json) |
| `FDCAN_TXEFA` | `0x00E8` | FDCAN Tx event FIFO ack nowledge register (FDCAN_TXEFA) | [FDCAN_TXEFA.json](../registers_json/FDCAN_TXEFA.json) |
| `FDCAN_TXEFS` | `0x00E4` | FDCAN Tx event FIFO st atus register (FDCAN_TXEFS) | [FDCAN_TXEFS.json](../registers_json/FDCAN_TXEFS.json) |
| `FDCAN_TXFQS` | `0x00` | FDCAN Tx FIFO/queue status register (FDCAN_TXFQS) | [FDCAN_TXFQS.json](../registers_json/FDCAN_TXFQS.json) |
| `FDCAN_XIDAM` | `0x0084` | FDCAN extended ID and mask register (FDCAN_XIDAM) | [FDCAN_XIDAM.json](../registers_json/FDCAN_XIDAM.json) |