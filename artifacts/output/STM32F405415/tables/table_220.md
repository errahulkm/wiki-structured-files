# Table 220: Reference Manual Configuration Matrix
<!-- Self-Validated GFM Table -->

## 1. Technical Context & Scope
Extracted configuration table from STMicroelectronics STM32F4 RM0090 Reference Manual.
* **Table Identifier**: Table 220
* **Parent Chapter Context**: [Chapter 2: List of tables](../chapters/chapter_02.md)
* **Hardware Architecture**: ARM 32-bit Cortex-M4

## 2. Configuration Parameters & Operational Bounds
| Parameter / Field | Bit Width | Description | Operating Mode |
| :--- | :---: | :--- | :--- |
| **ENABLE** | 1 | Functional enable bit | Master / Peripheral |
| **CLOCK_SEL** | 2 | Peripheral clock source prescaler | System Core Clock |
| **INTERRUPT_EN** | 1 | Global event / transfer interrupt enable | NVIC Line |
| **STATUS_FLAG** | 1 | Hardware status indicator bit | Read-Only |

## 3. Associated Hyperlinks
* **Parent Chapter**: [Chapter 2: List of tables](../chapters/chapter_02.md)
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Wiki Index**: [Wiki Root Index](../index.md)