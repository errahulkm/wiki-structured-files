# Figure: Analog-to-Digital Converter (ADC) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Analog-to-Digital Converter (ADC)](../peripherals/adc.md)
* **PDF Document Location**: Page 591 (RM0440 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Analog-to-Digital Converter (ADC) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0440 Block Diagram: Analog-to-Digital Converter (ADC)                                |
| [Parent IP: Analog-to-Digital Converter (ADC) | Page 591]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Analog-to-Digital Converter (ADC)](../peripherals/adc.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)