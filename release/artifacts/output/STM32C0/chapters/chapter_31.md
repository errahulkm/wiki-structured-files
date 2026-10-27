# Chapter 31: Device electronic signature

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32C0 Reference Manual RM0490 - Chapter 31: Device electronic signature.
* **Document Source**: RM0490 Reference Manual
* **PDF Reference Location**: Pages 1015 - 1017
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0490 Ingestion)
```text
RM0490 Rev 6 1015/1023
RM0490 Device electronic signature
1017
31 Device electronic signature
The device electronic signature is stored in the system memory area of the flash memory
module, and can be read using the debug inter face or by the CPU. It contains factory-
programmed identification and calibration data that allow the user firmware or other external
devices to automatically match to the characteristics of the STM32C0 series microcontroller.
31.1 Unique device ID register (96 bits) (UID)
Base address: 0x1FFF 7550
Address offset: 0x00
Reset value: 0xXXXX XXXX (where X is factory-programmed)
The unique device identifier is ideally suited:
• for use as serial numbers (for example USB string serial numbers or other end
applications)
• for use as part of the security keys in order to increase the security of code in flash
memory while using and combining this unique ID with software cryptographic
primitives and protocols before programming the internal flash memory
• to activate secure boot processes, and so on.
The 96-bit unique device identifier provides a reference number which is unique for any
device and in any context. These bits cannot be altered by the user.
Address offset: 0x04
Reset value: 0xXXXX XXXX where X is factory-programmed
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

Device electronic signature RM0490
1016/1023 RM0490 Rev 6
Address offset: 0x08
Reset value: 0xXXXX XXXX where X is factory-programmed
31.2 Flash memory size data register (FSIZER)
Base address: 0x1FFF 75A0
Address offset: 0x00
Reset value: 0xXXXX where X is factory-programmed
31.3 Package data register (PCKR)
Base address: 0x1FFF 7500
Address offset: 0x00
Reset value: 0xXXXX where X is factory-programmed
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
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. PKG[3:0]
rrrr

RM0490 Rev 6 1017/1023
RM0490 Device electronic signature
1017
Bits 15:4 Reserved
Bits 3:0 PKG[3:0]: Package type
Condition: STM32C011xx
0001: SO8
0010: WLCSP12
0011: UFQFPN20
0100: TSSOP20
Other: Reserved
Condition: STM32C031xx
0010: TSSOP20
0011: UFQFPN28
0100: UFQFPN32 / LQFP32
0101: UFQFPN48 / LQFP48
Other: Reserved
Condition: STM32C051xx
0001: WLCSP15
0010: TSSOP20
0011: UFQFPN28
0100: UFQFPN32 / LQFP32
0101: UFQFPN48 / LQFP48
Other: Reserved
Condition: STM32C071xx
0001: WLCSP19_GP
0010: WLCSP19_N
0011: TSSOP20_GP
0100: TSSOP20_N
0101: UFQFPN28_GP
0110: UFQFPN28_N
0111: UFQFPN32_GP / LQFP32_GP
1000: UFQFPN32_N / LQFP32_N
1001: UFQFPN48_GP / LQFP48_GP
1010: UFQFPN48_N / LQFP48_N
1011: LQFP64_GP
1100: LQFP64_N
1101: UFBGA64_GP
1110: UFBGA64_N
Other: Reserved
Condition: STM32C091xx/92xx
0001: TSSOP20
0010: WLCSP24
0011: UFQFPN28
0100: UFQFPN32 / LQFP32
0101: UFQFPN48 / LQFP48
0110: UFBGA64 / LQFP64
Other: Reserved
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* *No dedicated configuration tables referenced in this chapter text.*

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)