# Figure: Inter-Integrated Circuit (I2C) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Inter-Integrated Circuit (I2C)](../peripherals/i2c.md)
* **PDF Document Location**: Page 1483 (RM0438 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Inter-Integrated Circuit (I2C) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0438 Block Diagram: Inter-Integrated Circuit (I2C)                                |
| [Parent IP: Inter-Integrated Circuit (I2C) | Page 1483]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Inter-Integrated Circuit (I2C)](../peripherals/i2c.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)