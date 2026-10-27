# Figure: Flexible Static Memory Controller (FSMC) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Flexible Static Memory Controller (FSMC)](../peripherals/fsmc.md)
* **PDF Document Location**: Page 570 (RM0438 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Flexible Static Memory Controller (FSMC) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0438 Block Diagram: Flexible Static Memory Controller (FSMC)                                |
| [Parent IP: Flexible Static Memory Controller (FSMC) | Page 570]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Flexible Static Memory Controller (FSMC)](../peripherals/fsmc.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)