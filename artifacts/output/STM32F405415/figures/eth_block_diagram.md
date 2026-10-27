# Figure: Ethernet MAC (ETH) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Ethernet MAC (ETH)](../peripherals/eth.md)
* **PDF Document Location**: Page 1113 (RM0090 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Ethernet MAC (ETH) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0090 Block Diagram: Ethernet MAC (ETH)                                |
| [Parent IP: Ethernet MAC (ETH) | Page 1113]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Ethernet MAC (ETH)](../peripherals/eth.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)