# Figure: Window Watchdog (WWDG) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Window Watchdog (WWDG)](../peripherals/wwdg.md)
* **PDF Document Location**: Page 641 (RM0490 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Window Watchdog (WWDG) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0490 Block Diagram: Window Watchdog (WWDG)                                |
| [Parent IP: Window Watchdog (WWDG) | Page 641]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Window Watchdog (WWDG)](../peripherals/wwdg.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)