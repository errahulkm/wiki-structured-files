# Figure: Flexible Memory Controller (FMC) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Flexible Memory Controller (FMC)](../peripherals/fmc.md)
* **PDF Document Location**: Page 1590 (RM0090 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Flexible Memory Controller (FMC) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0090 Block Diagram: Flexible Memory Controller (FMC)                                |
| [Parent IP: Flexible Memory Controller (FMC) | Page 1590]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Flexible Memory Controller (FMC)](../peripherals/fmc.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)