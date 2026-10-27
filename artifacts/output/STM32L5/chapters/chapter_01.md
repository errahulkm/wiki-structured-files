# Chapter 1: Documentation conventions

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 1: Documentation conventions.
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 77 - 78
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 77/2187
RM0438 Documentation conventions
78
1 Documentation conventions
1.1 General information
The STM32L552xx and STM32L562xx devices have an Arm®(a) Cortex®-M33 core with
Arm®(a) TrustZone®.
1.2 List of abbrevia tions for registers
The following abbreviations(b) are used in register descriptions:
a. Arm and TrustZone are registered trademarks of Arm Limited (or its subsidiaries) in the US and/or
elsewhere.
b. This is an exhaustive list of all abbreviations applicab le to STMicroelectronics microcontrollers, some of
them may not be used in the current document.
read/write (rw) Software can read and write to this bit.
read-only (r) Software can only read this bit.
write-only (w) Software can only write to this bit. Reading this bit returns the reset value.
read/clear write0 (rc_w0) Software can read as well as clear this bit by writing 0. Writing 1 has no
effect on the bit value.
read/clear write1 (rc_w1) Software can read as well as clear this bit by writing 1. Writing 0 has no
effect on the bit value.
read/clear write (rc_w) Software ca n read as well as clear this bit by writing to the register. The
value written to this bit is not important.
read/clear by read (rc_r) Software can read this bit. Reading this bit automatically clears it to 0.
Writing this bit has no effect on the bit value.
read/set by read (rs_r) Software can read this bi t. Reading this bit automatically sets it to 1.
Writing this bit has no effect on the bit value.
read/set (rs) Software can read as well as set this bit. Writing 0 has no effect on the bit
value.
read/write once (rwo) Software can only write once to this bit and can also read it at any time.
Only a reset can return the bit to its reset value.
toggle (t) The software can to ggle this bit by writing 1. Writing 0 has no effect.
read-only write trigger (rt_w1) Software can read this bit. Writing 1 triggers an event but has no effect on
the bit value.
Reserved (Res.) Reserved bit, must be kept at reset value.

Documentation conventions RM0438
78/2187 RM0438 Rev 8
1.3 Register reset value
Bits (binary notation) or bits nibbles (hexadecimal notation) of which the reset value is
undefined are marked as X.
Bits (binary notation) or bits nibbles (hexadecimal notation) of which the reset value is
unmodified are marked as U.
1.4 Glossary
This section gives a brief definition of acronyms and abbreviations used in this document:
• Word: data of 32-bit length.
• Half-word: data of 16-bit length.
• Byte: data of 8-bit length.
• IAP (in-application programming): IAP is the ability to re-program the flash memory
of a microcontroller while the user program is running.
• ICP (in-circuit programming): ICP is the ability to program the flash memory of a
microcontroller using the JTAG protocol, the SWD protocol or the bootloader while the
device is mounted on the user application board.
• Option bytes: device configuration bits stored in the flash memory.
• OBL: option byte loader.
• AHB: advanced high-performance bus.
• APB: advanced peripheral bus.
• RAZ: read-as-zero.
• WI: writes ignored.
• RAZ/WI: read-as-zero, writes ignored.
1.5 Availability of peripherals
For availability of peripherals and their number across all devices, refer to the particular
device datasheet.
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* *No dedicated configuration tables referenced in this chapter text.*

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)