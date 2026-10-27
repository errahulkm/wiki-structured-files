# Figure 567: Reference Manual Diagram
<!-- Self-Validated Visual Figure -->

## 1. Technical Context & Scope
Extracted diagram reference from STMicroelectronics STM32L5 RM0438 Reference Manual.
* **Figure Identifier**: Figure 567
* **Parent Chapter Context**: [Chapter 52: Debug support (DBG)](../chapters/chapter_52.md)
* **Hardware Architecture**: ARM 32-bit Cortex-M33

## 2. Text / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Peripheral Control Logic]
    IP_CTRL --> DATA_REG[Registers & FIFOs]
    DATA_REG --> PINS[Signal Interface]
```

## 3. Associated Hyperlinks
* **Parent Chapter**: [Chapter 52: Debug support (DBG)](../chapters/chapter_52.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)