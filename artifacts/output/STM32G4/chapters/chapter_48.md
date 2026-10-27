# Chapter 48: Device electronic signature

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32G4 Reference Manual RM0440 - Chapter 48: Device electronic signature.
* **Document Source**: RM0440 Reference Manual
* **PDF Reference Location**: Pages 2121 - 2123
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0440 Ingestion)
```text
RM0440 Rev 9 2121/2140
RM0440 Device electronic signature
2123
48 Device electronic signature
The device electronic signature is stored in the System memory area of the Flash memory
module, and can be read using the debug interface or by the CPU. It contains factory-
programmed identification and calibration data that allow the user firmware or other external
devices to automatically match to the characteristics of the STM32G4 series microcontroller.
48.1 Unique device ID register (96 bits)
The unique device identifier is ideally suited:
• for use as serial numbers (for example USB string serial numbers or other end
applications)
• for use as part of the security keys in order to increase the security of code in Flash
memory while using and combining this unique ID with software cryptographic
primitives and protocols before programming the internal Flash memory
• to activate secure boot processes, etc.
The 96-bit unique device identifier provides a reference number which is unique for any
device and in any context. These bits cannot be altered by the user.
Base address: 0x1FFF 7590
Address offset: 0x00
Read only = 0xXXXX XXXX where X is factory-programmed
Address offset: 0x04
Read only = 0xXXXX XXXX where X is factory-programmed
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
UID[31:16]
r r r rr rrrrrrrrrrr
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
UID[15:0]
r r r rr rrrrrrrrrrr
Bits 31:0 UID[31:0]: X and Y coordinates on the wafer
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
UID[63:48]
r r r rr rrrrrrrrrrr
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
UID[47:32]
r r r rr rrrrrrrrrrr
Bits 31:8 UID[63:40]: LOT_NUM[23:0]
Lot number (ASCII encoded)

Device electronic signature RM0440
2122/2140 RM0440 Rev 9
Address offset: 0x08
Read only = 0xXXXX XXXX where X is factory-programmed
48.2 Flash size data register
Base address: 0x1FFF 75E0
Address offset: 0x00
Read only = 0xXXXX where X is factory-programmed
48.3 Package data register
Base address: 0x1FFF 7500
Address offset: 0x00
Read only = 0xXXXX where X is factory-programmed
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
This bitfield indicates the size of the device Flash memory expressed in Kbytes.
As an example, 0x040 corresponds to 64 Kbytes.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. PKG[4:0]
rrrrr
Bits 15:5 Reserved, must be kept at reset value

RM0440 Rev 9 2123/2140
RM0440 Device electronic signature
2123
Bits 4:0 PKG[4:0]: Package type
00000: LQFP64
00001: WLCSP64
00010: LQFP100 (all devices) and LQFP80 (for category 2 devices)
00101: WLCSP81 and LQFP80 (for category 3 devices)
00111: LQFP128 / UFBGA121
01000: UFQFPN32
01001: LQFP32
01010: UFQFPN48
01011: LQFP48
01100: WLCSP49
01101: UFBGA64
01110: TFBGA100
10001: LQFP80 (for category 4 devices only)
Others: reserved
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* *No dedicated configuration tables referenced in this chapter text.*

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)