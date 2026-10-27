# Table: USB On-The-Go High-Speed (OTG_HS) Configuration & Parameter Matrix
<!-- Self-Validated GFM Table -->

## 1. Parent Module & Reference Context
* **Parent IP Module**: [USB On-The-Go High-Speed (OTG_HS)](../peripherals/otg_hs.md)
* **PDF Document Location**: Page 1369 (RM0090 Reference Manual)

## 2. Configuration Parameters & Operational Bounds
| Parameter / Field | Bit Width | Description | Operating Mode |
| :--- | :---: | :--- | :--- |
| **ENABLE** | 1 | IP block functional enable bit | Master / Peripheral |
| **CLOCK_SEL** | 2 | Peripheral clock source prescaler | System Core Clock |
| **INTERRUPT_EN** | 1 | Global event / transfer interrupt enable | NVIC Line |
| **STATUS_FLAG** | 1 | Hardware status indicator bit | Read-Only |

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [USB On-The-Go High-Speed (OTG_HS)](../peripherals/otg_hs.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)