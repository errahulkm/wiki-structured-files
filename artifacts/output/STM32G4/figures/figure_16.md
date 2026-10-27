# Figure: Random Number Generator (RNG) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Random Number Generator (RNG)](../security/rng.md)
* **PDF Document Location**: Page 820 (RM0440 Reference Manual)
* **Category**: SECURITY

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Random Number Generator (RNG) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0440 Block Diagram: Random Number Generator (RNG)                                |
| [Parent IP: Random Number Generator (RNG) | Page 820]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Random Number Generator (RNG)](../security/rng.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)