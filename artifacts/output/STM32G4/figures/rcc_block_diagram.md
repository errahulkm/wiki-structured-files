# Figure: Reset and Clock Control (RCC) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Reset and Clock Control (RCC)](../system/rcc.md)
* **PDF Document Location**: Page 270 (RM0440 Reference Manual)
* **Category**: SYSTEM

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Reset and Clock Control (RCC) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0440 Block Diagram: Reset and Clock Control (RCC)                                |
| [Parent IP: Reset and Clock Control (RCC) | Page 270]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Reset and Clock Control (RCC)](../system/rcc.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)