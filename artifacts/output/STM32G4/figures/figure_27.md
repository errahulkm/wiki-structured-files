# Figure: Debug Support (DBG) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Debug Support (DBG)](../core/debug.md)
* **PDF Document Location**: Page 2088 (RM0440 Reference Manual)
* **Category**: CORE

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Debug Support (DBG) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0440 Block Diagram: Debug Support (DBG)                                |
| [Parent IP: Debug Support (DBG) | Page 2088]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Debug Support (DBG)](../core/debug.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)