# Figure: Global TrustZone Security Controller Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Global TrustZone Security Controller](../security/trustzone.md)
* **PDF Document Location**: Page 130 (RM0438 Reference Manual)
* **Category**: SECURITY

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Global TrustZone Security Controller Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0438 Block Diagram: Global TrustZone Security Controller                                |
| [Parent IP: Global TrustZone Security Controller | Page 130]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Global TrustZone Security Controller](../security/trustzone.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)