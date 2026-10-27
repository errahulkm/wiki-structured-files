# Figure: LCD-TFT Display Controller (LTDC) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [LCD-TFT Display Controller (LTDC)](../peripherals/ltdc.md)
* **PDF Document Location**: Page 480 (RM0090 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[LCD-TFT Display Controller (LTDC) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0090 Block Diagram: LCD-TFT Display Controller (LTDC)                                |
| [Parent IP: LCD-TFT Display Controller (LTDC) | Page 480]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [LCD-TFT Display Controller (LTDC)](../peripherals/ltdc.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)