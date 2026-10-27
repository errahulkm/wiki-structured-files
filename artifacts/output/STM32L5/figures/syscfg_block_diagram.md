# Figure: System Configuration (SYSCFG) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [System Configuration (SYSCFG)](../system/syscfg.md)
* **PDF Document Location**: Page 456 (RM0438 Reference Manual)
* **Category**: SYSTEM

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[System Configuration (SYSCFG) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0438 Block Diagram: System Configuration (SYSCFG)                                |
| [Parent IP: System Configuration (SYSCFG) | Page 456]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [System Configuration (SYSCFG)](../system/syscfg.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)