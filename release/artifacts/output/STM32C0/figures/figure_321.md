# Figure 321: Reference Manual Diagram
<!-- Self-Validated Visual Figure -->

## 1. Technical Context & Scope
Extracted diagram reference from STMicroelectronics STM32C0 RM0490 Reference Manual.
* **Figure Identifier**: Figure 321
* **Parent Chapter Context**: [Chapter 28: FD controller area network (FDCAN)](../chapters/chapter_28.md)
* **Hardware Architecture**: ARM 32-bit Cortex-M0/M0+

## 2. Text / ASCII & Mermaid Structural Model
```mermaid
graph TD
    BUS[System Bus Matrix] --> IP_CTRL[Peripheral Control Logic]
    IP_CTRL --> DATA_REG[Registers & FIFOs]
    DATA_REG --> PINS[Signal Interface]
```

## 3. Associated Hyperlinks
* **Parent Chapter**: [Chapter 28: FD controller area network (FDCAN)](../chapters/chapter_28.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)