# Figure: Cryptographic Processor (CRYP) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Cryptographic Processor (CRYP)](../security/cryp.md)
* **PDF Document Location**: Page 716 (RM0090 Reference Manual)
* **Category**: SECURITY

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Cryptographic Processor (CRYP) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0090 Block Diagram: Cryptographic Processor (CRYP)                                |
| [Parent IP: Cryptographic Processor (CRYP) | Page 716]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Cryptographic Processor (CRYP)](../security/cryp.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)