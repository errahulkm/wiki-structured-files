# Figure: Serial Peripheral Interface (SPI) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Serial Peripheral Interface (SPI)](../peripherals/spi.md)
* **PDF Document Location**: Page 830 (RM0490 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Serial Peripheral Interface (SPI) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0490 Block Diagram: Serial Peripheral Interface (SPI)                                |
| [Parent IP: Serial Peripheral Interface (SPI) | Page 830]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Serial Peripheral Interface (SPI)](../peripherals/spi.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)