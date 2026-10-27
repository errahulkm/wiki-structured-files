# Figure: Independent Watchdog (IWDG) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Independent Watchdog (IWDG)](../peripherals/iwdg.md)
* **PDF Document Location**: Page 1380 (RM0438 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Independent Watchdog (IWDG) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0438 Block Diagram: Independent Watchdog (IWDG)                                |
| [Parent IP: Independent Watchdog (IWDG) | Page 1380]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Independent Watchdog (IWDG)](../peripherals/iwdg.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)