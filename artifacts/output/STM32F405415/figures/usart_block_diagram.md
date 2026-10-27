# Figure: Universal Synchronous Asynchronous Receiver Transmitter (USART) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [Universal Synchronous Asynchronous Receiver Transmitter (USART)](../peripherals/usart.md)
* **PDF Document Location**: Page 960 (RM0090 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Universal Synchronous Asynchronous Receiver Transmitter (USART) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0090 Block Diagram: Universal Synchronous Asynchronous Receiver Transmitter (USART)                                |
| [Parent IP: Universal Synchronous Asynchronous Receiver Transmitter (USART) | Page 960]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [Universal Synchronous Asynchronous Receiver Transmitter (USART)](../peripherals/usart.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)