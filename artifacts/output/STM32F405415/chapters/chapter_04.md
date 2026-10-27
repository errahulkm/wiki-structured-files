# Chapter 4: Documentation conventions

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32F4 Reference Manual RM0090 - Chapter 4: Documentation conventions.
* **Document Source**: RM0090 Reference Manual
* **PDF Reference Location**: Pages 57 - 58
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0090 Ingestion)
```text
RM0090 Rev 22 57/1741
RM0090 Documentation conventions
112
1 Documentation conventions
The STM32F405xx/07xx, STM32F415xx/17xx, STM32F42xxx and STM32F43xxx devices
have an Arm®(a)(b) Cortex®(c) -M4 with FPU core.
1.1 List of abbrevia tions for registers
The following abbreviations are used in register descriptions:
a. Arm is a registered trademark of Arm Limited (o r its subsidiaries) in the US and/or elsewhere.
b. The Arm word and logo are trademarks of Arm Limited (o r its subsidiaries) in the US and/or elsewhere. All
rights reserved.
c. Arm and Cortex are registered trademarks of Arm Limited (or its subsidiaries or affiliates) in the US and/or
elsewhere.
read/write (rw) Softwa re can read and write to these bits.
read-only (r) Software can only read these bits.
write-only (w) Software can only write to this bit. Reading the bit returns the reset
value.
read/clear (rc_w1) Software can read as well as clear this bit by writing 1. Writing ‘0’ has
no effect on the bit value.
read/clear (rc_w0) Software can read as well as clear this bit by writing 0. Writing ‘1’ has
no effect on the bit value.
read/clear by read
(rc_r)
Software can read this bit. Reading this bit automatically clears it to ‘0’.
Writing ‘0’ has no effect on the bit value.
read/set (rs) Software can read as well as se t this bit. Writing ‘0’ has no effect on the
bit value.
read-only write
trigger (rt_w)
Software can read this bit. Writing ‘0’ or ‘1’ triggers an event but has no
effect on the bit value.
toggle (t) Software can only toggle this bit by writing ‘1’. Writing ‘0’ has no effect.
Reserved (Res.) Reserved bit, mu st be kept at reset value.

Documentation conventions RM0090
58/1741 RM0090 Rev 22
1.2 Glossary
This section gives a brief definition of acronyms and abbreviations used in this document:
• The CPU core integrates two debug ports:
– JTAG debug port (JTAG-DP) provides a 5-pin standard interface based on the
Joint Test Action Group (JTAG) protocol.
– SWD debug port (SWD-DP) provides a 2-pin (clock and data) interface based on
the Serial Wire Debug (SWD) protocol.
For both the JTAG and SWD protocols, please refer to the Cortex®-M4 with FPU
Technical Reference Manual
• Word: data/instruction of 32-bit length.
• Half word: data/instruction of 16-bit length.
• Byte: data of 8-bit length.
• Double word: data of 64-bit length.
• IAP (in-application programming): IAP is the ability to reprogram the flash memory of a
microcontroller while the user program is running.
• ICP (in-circuit programming): ICP is the ability to program the flash memory of a
microcontroller using the JTAG protocol, the SWD protocol or the bootloader while the
device is mounted on the user application board.
• I-Code: this bus connects the Instruction bus of the CPU core to the Flash instruction
interface. Prefetch is performed on this bus.
• D-Code: this bus connects the D-Code bus (literal load and debug access) of the CPU
to the Flash data interface.
• Option bytes: product configuration bits stored in the flash memory.
• OBL: option byte loader.
• AHB: advanced high-performance bus.
• CPU: refers to the Cortex®-M4 with FPU core.
1.3 Peripheral availability
For peripheral availability and number across all STM32F405xx/07xx and
STM32F415xx/17xx sales types, please refer to the STM32F405xx/07xx and
STM32F415xx/17xx datasheets.
For peripheral availability and number across all STM32F42xxx and STM32F43xxx sales
types, please refer to the STM32F42xxx and STM32F43xxx datasheets.
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* *No dedicated configuration tables referenced in this chapter text.*

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)