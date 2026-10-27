# Figure: Hash Processor (HASH) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Hash Processor (HASH)](../security/hash.md)
* **PDF Document Location**: Page 1001 (RM0438 Reference Manual)
* **Category**: SECURITY

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Hash Processor (HASH) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0438 Block Diagram: Hash Processor (HASH)                                |
| [Parent IP: Hash Processor (HASH) | Page 1001]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Hash Processor (HASH)](../security/hash.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)