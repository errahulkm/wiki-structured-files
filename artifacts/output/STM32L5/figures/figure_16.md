# Figure: Operational Amplifier (OPAMP) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Operational Amplifier (OPAMP)](../peripherals/opamp.md)
* **PDF Document Location**: Page 849 (RM0438 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Operational Amplifier (OPAMP) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0438 Block Diagram: Operational Amplifier (OPAMP)                                |
| [Parent IP: Operational Amplifier (OPAMP) | Page 849]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Operational Amplifier (OPAMP)](../peripherals/opamp.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)