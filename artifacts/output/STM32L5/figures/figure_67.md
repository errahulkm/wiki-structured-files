# Figure 67: Reference Manual Diagram
<!-- Self-Validated Visual Figure -->

## 1. Technical Context & Scope
Extracted diagram reference from STMicroelectronics STM32L5 RM0438 Reference Manual.
* **Figure Identifier**: Figure 67
* **Parent Chapter Context**: [Chapter 19: Flexible static memory controller (FSMC)](../chapters/chapter_19.md)
* **Hardware Architecture**: ARM 32-bit Cortex-M33

## 2. Text / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Peripheral Control Logic]
    IP_CTRL --> DATA_REG[Registers & FIFOs]
    DATA_REG --> PINS[Signal Interface]
```

## 3. Associated Hyperlinks
* **Parent Chapter**: [Chapter 19: Flexible static memory controller (FSMC)](../chapters/chapter_19.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)