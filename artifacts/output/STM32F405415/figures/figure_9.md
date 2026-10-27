# Figure: Interrupts and Events (NVIC/EXTI) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Interrupts and Events (NVIC/EXTI)](../core/interrupts.md)
* **PDF Document Location**: Page 373 (RM0090 Reference Manual)
* **Category**: CORE

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Interrupts and Events (NVIC/EXTI) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0090 Block Diagram: Interrupts and Events (NVIC/EXTI)                                |
| [Parent IP: Interrupts and Events (NVIC/EXTI) | Page 373]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Interrupts and Events (NVIC/EXTI)](../core/interrupts.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)