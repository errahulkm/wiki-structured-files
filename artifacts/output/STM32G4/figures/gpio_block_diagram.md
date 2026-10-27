# Figure: General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) Architectural Block Diagram

## 1. Parent Module & Reference Context
* **Parent IP Module**: [General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs)](../peripherals/gpio.md)
* **PDF Document Location**: Page 345 (RM0440 Reference Manual)
* **Category**: PERIPHERALS

## 2. Text / Pen-Sketch / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) Control Logic]
    IP_CTRL --> STATE[Operational State Machine]
    STATE --> DATA_REG[Data & Configuration Registers]
    DATA_REG --> PINS[Peripheral Interconnect & Signals]
```

```
+-------------------------------------------------------------------+
| RM0440 Block Diagram: General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs)                                |
| [Parent IP: General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs) | Page 345]                              |
+------------------------+------------------------------------------+
| Control & Status Logic | Hardware Register Interface (AHB/APB)    |
+------------------------+------------------------------------------+
| Operating State Machine| Internal FIFOs & Signal Routing          |
+------------------------+------------------------------------------+
```

## 3. Associated IP Module & Memory Links
* **Parent Peripheral IP**: [General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs)](../peripherals/gpio.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)