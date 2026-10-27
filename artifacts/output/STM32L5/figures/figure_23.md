# Figure: Real-Time Clock (RTC) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Real-Time Clock (RTC)](../peripherals/rtc.md)
* **PDF Document Location**: Page 1395 (RM0438 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Real-Time Clock (RTC) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0438 Block Diagram: Real-Time Clock (RTC)                                |
| [Parent IP: Real-Time Clock (RTC) | Page 1395]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Real-Time Clock (RTC)](../peripherals/rtc.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)