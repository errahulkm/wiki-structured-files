# Figure: USB On-The-Go Full-Speed (OTG_FS) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [USB On-The-Go Full-Speed (OTG_FS)](../peripherals/otg_fs.md)
* **PDF Document Location**: Page 1228 (RM0090 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[USB On-The-Go Full-Speed (OTG_FS) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0090 Block Diagram: USB On-The-Go Full-Speed (OTG_FS)                                |
| [Parent IP: USB On-The-Go Full-Speed (OTG_FS) | Page 1228]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [USB On-The-Go Full-Speed (OTG_FS)](../peripherals/otg_fs.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)