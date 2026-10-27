# Figure: Digital-to-Analog Converter (DAC) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Digital-to-Analog Converter (DAC)](../peripherals/dac.md)
* **PDF Document Location**: Page 714 (RM0440 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Digital-to-Analog Converter (DAC) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0440 Block Diagram: Digital-to-Analog Converter (DAC)                                |
| [Parent IP: Digital-to-Analog Converter (DAC) | Page 714]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Digital-to-Analog Converter (DAC)](../peripherals/dac.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)