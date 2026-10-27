# Figure: Secure Digital Input/Output (SDIO) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Secure Digital Input/Output (SDIO)](../peripherals/sdio.md)
* **PDF Document Location**: Page 1014 (RM0090 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Secure Digital Input/Output (SDIO) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0090 Block Diagram: Secure Digital Input/Output (SDIO)                                |
| [Parent IP: Secure Digital Input/Output (SDIO) | Page 1014]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Secure Digital Input/Output (SDIO)](../peripherals/sdio.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)