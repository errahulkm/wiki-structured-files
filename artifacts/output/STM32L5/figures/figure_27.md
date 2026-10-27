# Figure: Serial Audio Interface (SAI) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Serial Audio Interface (SAI)](../peripherals/sai.md)
* **PDF Document Location**: Page 1723 (RM0438 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Serial Audio Interface (SAI) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0438 Block Diagram: Serial Audio Interface (SAI)                                |
| [Parent IP: Serial Audio Interface (SAI) | Page 1723]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Serial Audio Interface (SAI)](../peripherals/sai.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)