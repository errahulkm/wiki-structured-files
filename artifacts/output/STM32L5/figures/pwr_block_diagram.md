# Figure: Power Control (PWR) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Power Control (PWR)](../system/pwr.md)
* **PDF Document Location**: Page 259 (RM0438 Reference Manual)
* **Category**: SYSTEM

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Power Control (PWR) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0438 Block Diagram: Power Control (PWR)                                |
| [Parent IP: Power Control (PWR) | Page 259]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Power Control (PWR)](../system/pwr.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)