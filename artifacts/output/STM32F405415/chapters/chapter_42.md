# Chapter 42: Device electronic signature

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32F4 Reference Manual RM0090 - Chapter 42: Device electronic signature.
* **Document Source**: RM0090 Reference Manual
* **PDF Reference Location**: Pages 1701 - 1702
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0090 Ingestion)
```text
RM0090 Rev 22 1701/1741
RM0090 Device electronic signature
1702
39 Device electronic signature
The electronic signature is stored in the Flash memory area. It can be read using the
JTAG/SWD or the CPU. It contains factory-programmed identification data that allow the
user firmware or other external devices to automatically match its interface to the
characteristics of the STM32F4xx microcontrollers.
39.1 Unique device ID register (96 bits)
The unique device identifier is ideally suited:
• for use as serial numbers (for example USB string serial numbers or other end
applications)
• for use as security keys in order to increase the security of code in Flash memory while
using and combining this unique ID with software cryptographic primitives and
protocols before programming the internal Flash memory
• to activate secure boot processes, etc.
The 96-bit unique device identifier provides a reference number which is unique for any
device and in any context. These bits can never be altered by the user.
The 96-bit unique device identifier can also be read in single bytes/half-words/words in
different ways and then be concatenated using a custom algorithm.
Base address: 0x1FFF 7A10
Address offset: 0x00
Read only = 0xXXXX XXXX where X is factory-programmed
Address offset: 0x04
Read only = 0xXXXX XXXX where X is factory-programmed
3 1 3 0 2 9 2 8 2 7 2 6 2 5 2 4 2 3 2 2 2 1 2 0 1 9 1 8 1 7 1 6 1 5 1 4 1 3 1 2 1 1 1 0 9876543210
UID(31:0)
rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
Bits 31:0 UID(31:0): X and Y coordinates on the wafer
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
UID(63:48)
rrrrrrrrrrrrrrrr
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
UID(47:32)
rrrrrrrrrrrrrrrr

Device electronic signature RM0090
1702/1741 RM0090 Rev 22
Address offset: 0x08
Read only = 0xXXXX XXXX where X is factory-programmed
39.2 Flash size
Base address: 0x1FFF 7A22
Address offset: 0x00
Read only = 0xXXXX where X is factory-programmed
Bits 31:8 UID(63:40): LOT_NUM[23:0]
Lot number (ASCII encoded).
Bits 7:0 UID(39:32): WAF_NUM[7:0]
Wafer number (ASCII encoded).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
UID(95:80)
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
UID(79:64)
rrrrrrrrrrrrrrrr
Bits 31:0 UID(95:64): LOT_NUM[55:24]
Lot number (ASCII encoded).
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
F_SIZE
rrrrrrrrrrrrrrrr
Bits 15:0 F_ID(15:0): Flash memory size
This bitfield indicates the size of the device Flash memory expressed in Kbytes.
As an example, 0x0400 corresponds to 1024 Kbytes.
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* *No dedicated configuration tables referenced in this chapter text.*

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)