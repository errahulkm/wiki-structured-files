# Chapter 53: Device electronic signature

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 53: Device electronic signature.
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 2150 - 2153
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
Device electronic signature RM0438
2150/2187 RM0438 Rev 8
53 Device electronic signature
The device electronic signature is stored in the System memory area of the flash memory
module, and can be read using the debug interface or by the CPU. It contains factory-
programmed identification and calibration data that allow the user firmware or other external
devices to automatically match to the characteristics of the STM32L552xx and
STM32L562xx microcontrollers.

RM0438 Rev 8 2151/2187
RM0438 Device electronic signature
2153
53.1 Unique device ID register (96 bits)
The unique device identifier is ideally suited:
• for use as serial numbers (for example USB string serial numbers or other end
applications)
• for use as part of the security keys in order to increase the security of code in flash
memory while using and combining this unique ID with software cryptographic
primitives and protocols before programming the internal flash memory
• to activate secure boot processes, etc.
The 96-bit unique device identifier provides a reference number which is unique for any
device and in any context. These bits cannot be altered by the user.
Base address: 0x0BFA 0590
Address offset: 0x00
Read only = 0xXXXX XXXX where X is factory-programmed
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
UID[31:16]
r r r rr rrrrrrrrrrr
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
UID[15:0]
r r r rr rrrrrrrrrrr
Bits 31:0 UID[31:0]: X and Y coordinates on the wafer

Device electronic signature RM0438
2152/2187 RM0438 Rev 8
Address offset: 0x04
Read only = 0xXXXX XXXX where X is factory-programmed
Address offset: 0x08
Read only = 0xXXXX XXXX where X is factory-programmed
53.2 Flash size data register
Base address: 0x0BFA 05E0
Address offset: 0x00
Read only = 0xXXXX where X is factory-programmed
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
UID[63:48]
r r r rr rrrrrrrrrrr
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
UID[47:32]
r r r rr rrrrrrrrrrr
Bits 31:8 UID[63:40]: LOT_NUM[23:0]
Lot number (ASCII encoded)
Bits 7:0 UID[39:32]: WAF_NUM[7:0]
Wafer number (8-bit unsigned number)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
UID[95:80]
r r r rr rrrrrrrrrrr
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
UID[79:64]
r r r rr rrrrrrrrrrr
Bits 31:0 UID[95:64]: LOT_NUM[55:24]
Lot number (ASCII encoded)
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
FLASH_SIZE
rrrrrrrrrrrrrrrr
Bits 15:0 FLASH_SIZE[15:0]: Flash memory size
This bitfield indicates the size of the device flash memory expressed in Kbytes.
As an example, 0x040 corresponds to 64 Kbytes.

RM0438 Rev 8 2153/2187
RM0438 Device electronic signature
2153
53.3 Package data register
Base address: 0x0BFA 0500
Address offset: 0x00
Read only = 0xXXXX where X is factory-programmed
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. PKG[4:0]
rrrrr
Bits 15:5 Reserved, must be kept at reset value
Bits 4:0 PKG[4:0]: Package type
00000: LQFP64
00010: LQFP100
00011: UFBGA132
00100: LQFP144
00101: WLCSP81
01011: LQFP48 and UFQFPN48
10001: LQFP144 with SMPS Step Down converter
10010: UFBGA132 with SMPS Step Down converter
10011: LQFP100 with SMPS Step Down converter
10100: WLCSP81 with SMPS Step Down converter
10101: LQFP64 with SMPS Step Down converter
10110: LQFP48 and UFQFPN48 with SMPS Step Down converter
11000: LQFP144 with external SMPS support
11001: UFBGA132 with external SMPS support
11010: LQFP100 with external SMPS support
11011: WLCSP81 with external SMPS support
11100: LQFP64 and with external SMPS support
11101: LQFP48 with external SMPS support
Others: reserved
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* *No dedicated configuration tables referenced in this chapter text.*

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)