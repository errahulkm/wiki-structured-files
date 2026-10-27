# Chapter 10: System configuration controller (SYSCFG)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32G4 Reference Manual RM0440 - Chapter 10: System configuration controller (SYSCFG).
* **Document Source**: RM0440 Reference Manual
* **PDF Reference Location**: Pages 364 - 375
* **Taxonomy Section**: SYSTEM
* **Parent IP Module**: [System Configuration (SYSCFG)](../system/syscfg.md)

## 2. Official Reference Manual Text Content (RM0440 Ingestion)
```text
System configuration controller (SYSCFG) RM0440
364/2140 RM0440 Rev 9
10 System configuration controller (SYSCFG)
10.1 SYSCFG main features
The STM32G4 series devices feature a set of configuration registers. The main purposes of
the system configuration controller are the following:
• Remapping memory areas
• Managing the external interrupt line connection to the GPIOs
• Managing robustness feature
• Setting CCM RAM write protection and software erase
• Configuring FPU interrupts
• Enabling /disabling I2C Fast-mode Plus driving capability on some I/Os and voltage
booster for I/Os analog switches.
10.2 SYSCFG registers
10.2.1 SYSCFG memory remap register (SYSCFG_MEMRMP)
This register is used for specific configurations on memory remap.
Address offset: 0x00
Reset value: 0x0000 000X (X is the memory mode selected by the BOOT0 pin and BOOT1
option bit)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res Res Res Res Res Res Res FB_
MODE Res Res Res Res Res MEM_MODE
rw rw rw rw
Bits 31:9 Reserved, must be kept at reset value.
Bit 8 FB_MODE: Flash Bank mode selection
0: Flash Bank 1 mapped at 0x0800 0000 (and aliased @0x0000 0000(1)) and Flash Bank 2
mapped at 0x0804 0000 (and aliased at 0x0008 0000)
1: Flash Bank2 mapped at 0x0800 0000 (and aliased @0x0000 0000(1)) and Flash Bank 1
mapped at 0x0804 0000 (and aliased at 0x0008 0000)
Bits 7:3 Reserved, must be kept at reset value.

RM0440 Rev 9 365/2140
RM0440 System configurat ion controller (SYSCFG)
375
Note: When the FSMC is remapped at address 0x00 00 0000, only the first two regions of Bank 1
memory controller (Bank1 NOR/PSRAM 1 and NOR/PSRAM 2) can be remapped. In remap
mode, the CPU can access the external memory via ICode bus instead of System bus
which boosts up the performance.
10.2.2 SYSCFG configuration register 1 (SYSCFG_CFGR1)
Address offset: 0x04
Reset value: 0x7C00 0000
Bits 2:0 MEM_MODE: Memory mapping selection
These bits control the memory internal mapping at address 0x0000 0000. These bits are
used to select the physical remap by software and so, bypass the BOOT pin and the option
bit setting. After reset these bits take the value selected by BOOT0 pin (or option bit
nBOOT0) and BOOT1 option bit.
000: Main Flash memory mapped at 0x00000000(1).
001: System Flash memory mapped at 0x00000000.
010: FSMC memory.
011: SRAM1 mapped at 0x00000000.
100: QUADSPI memory mapped at 0x0000 0000
101: Reserved
111: Reserved
1. When BFB2 bit is set, the system memory remains aliased at @0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
FPU_IE[5..0] Res Res I2C4_
FMP
I2C3_
FMP
I2C2_
FMP
I2C1_
FMP
I2C_
PB9_
FMP
I2C_
PB8_
FMP
I2C_
PB7_
FMP
I2C_
PB6_
FMP
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res Res Res Res Res Res ANAS
WVDD
BOOST
EN Res Res Res Res Res Res Res Res
rw rw
Bits 31:26 FPU_IE[5..0]: Floating Point Unit interrupts enable bits
FPU_IE[5]: Inexact interrupt enable
FPU_IE[4]: Input denormal interrupt enable
FPU_IE[3]: Overflow interrupt enable
FPU_IE[2]: underflow interrupt enable
FPU_IE[1]: Divide-by-zero interrupt enable
FPU_IE[0]: Invalid operation interrupt enable
Bits 25:24 Reserved, must  be kept at reset value.
Bit 23 I2C4_FMP: Fast-mode Plus driving capability activation
This bit enables the Fm+ driving mode on I2C4 pins selected through AF selection bits.
0: Fm+ mode is not enabled on I2C4 pins selected through AF selection bits
1: Fm+ mode is enabled on I2C4 pins selected through AF selection bits.

System configuration controller (SYSCFG) RM0440
366/2140 RM0440 Rev 9
[Table 60](../tables/table_60.md) describes when the bit 9 (ANASWVDD) and the bit 8 (BOOSTEN) should be set or
reset depending on the voltage settings.
Note: When FM+ mode is activate d on GPIO pin, the speed configuration of the GPIO (in
GPIOx_OSPEEDR register) is ignored. Program this register only after the AF selection
through the GPIOx_AFRH or GPIOx_AFRL register.
Bit 22 I2C3_FMP: I2C3 Fast-mode Plus driving capability activation
This bit enables the Fm+ driving mode on I2C3 pins selected through AF selection bits.
0: Fm+ mode is not enabled on I2C3 pins selected through AF selection bits
1: Fm+ mode is enabled on I2C3 pins selected through AF selection bits.
Bit 21 I2C2_FMP: I2C2 Fast-mode Plus driving capability activation
This bit enables the Fm+ driving mode on I2C2 pins selected through AF selection bits.
0: Fm+ mode is not enabled on I2C2 pins selected through AF selection bits
1: Fm+ mode is enabled on I2C2 pins selected through AF selection bits.
Bit 20 I2C1_FMP: I2C1 Fast-mode Plus driving capability activation
This bit enables the Fm+ driving mode on I2C1 pins selected through AF selection bits.
0: Fm+ mode is not enabled on I2C1 pins selected through AF selection bits
1: Fm+ mode is enabled on I2C1 pins selected through AF selection bits.
Bit 19 I2C_PB9_FMP: Fast-mode Plus (Fm+) driving capability activation on PB9
This bit enables the Fm+ driving mode for PB9.
0: PB9 pin operates in standard mode.
1: Fm+ mode enabled on PB9 pin, and the Speed control is bypassed.
Bit 18 I2C_PB8_FMP: Fast-mode Plus (Fm+) driving capability activation on PB8
This bit enables the Fm+ driving mode for PB8.
0: PB8 pin operates in standard mode.
1: Fm+ mode enabled on PB8 pin, and the Speed control is bypassed.
Bit 17 I2C_PB7_FMP: Fast-mode Plus (Fm+) driving capability activation on PB7
This bit enables the Fm+ driving mode for PB7.
0: PB7 pin operates in standard mode.
1: Fm+ mode enabled on PB7 pin, and the Speed control is bypassed.
Bit 16 I2C_PB6_FMP: Fast-mode Plus (Fm+) driving capability activation on PB6
This bit enables the Fm+ driving mode for PB6.
0: PB6 pin operates in standard mode.
1: Fm+ mode enabled on PB6 pin, and the Speed control is bypassed.
Bits 15:10 Reserved, must  be kept at reset value.
Bit 9 ANASWVDD: GPIO analog switch control voltage selection
0: I/O analog switches supplied by VDDA or booster when booster is ON
1: I/O analog switches supplied by VDD.
Refer to [Table 60](../tables/table_60.md) for bit 9 setting.
Bit 8 BOOSTEN: I/O analog switch voltage booster enable
0: I/O analog switches are supplied by VDDA voltage. This is the recommended configuration
when using the ADC in high VDDA voltage operation.
1: I/O analog switches are supplied by a dedicated voltage booster (supplied by VDD). This is
the recommended configuration when using the ADC in low VDDA voltage operation.
Bits 7:0 Reserved, must be kept at reset value.

RM0440 Rev 9 367/2140
RM0440 System configurat ion controller (SYSCFG)
375
10.2.3 SYSCFG external interrup t configuration register 1
(SYSCFG_EXTICR1)
Address offset: 0x08
Reset value: 0x0000 0000
[Table 60](../tables/table_60.md). BOOSTEN and ANASWVDD set/reset
VDD VDDA BOOSTEN ANASWVDD
->  2 . 4 V0 0
> 2.4 V < 2.4 V 0 1
< 2.4 V < 2.4 V 1 0
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
EXTI3[3:0] EXTI2[3:0] EXTI1[3:0] EXTI0[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:12  EXTI3[3:0]: EXTI 3 configuration bits
These bits are written by software to select the source input for the EXTI3
external interrupt.
0000: PA[3] pin
0001: PB[3] pin
0010: PC[3] pin
0011: PD[3] pin
0100: PE[3] pin
0101: PF[3] pin
0110: PG[3] pin
Bits 11:8  EXTI2[3:0]: EXTI 2 configuration bits
These bits are written by software to select the source input for the EXTI2
external interrupt.
0000: PA[2] pin
0001: PB[2] pin
0010: PC[2] pin
0011: PD[2] pin
0100: PE[2] pin
0101: PF[2] pin
0110: PG[2] pin

System configuration controller (SYSCFG) RM0440
368/2140 RM0440 Rev 9
10.2.4 SYSCFG external interrup t configuration register 2
(SYSCFG_EXTICR2)
Address offset: 0x0C
Reset value: 0x0000 0000
Bits 7:4  EXTI1[3:0]: EXTI 1 configuration bits
These bits are written by software to select the source input for the EXTI1
external interrupt.
0000: PA[1] pin
0001: PB[1] pin
0010: PC[1] pin
0011: PD[1] pin
0100: PE[1] pin
0101: PF[1] pin
0110: PG[1] pin
Bits 3:0  EXTI0[3:0]: EXTI 0 configuration bits
These bits are written by software to select the source input for the EXTI0
external interrupt.
0000: PA[0] pin
0001: PB[0] pin
0010: PC[0] pin
0011: PD[0] pin
0100: PE[0] pin
0101: PF[0] pin
0110: PG[0] pin
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
EXTI7[3:0] EXTI6[3:0] EXTI5[3:0] EXTI4[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:12  EXTI7[3:0]: EXTI 7 configuration bits
These bits are written by software to select the source input for the EXTI7
external interrupt.
0000: PA[7] pin
0001: PB[7] pin
0010: PC[7] pin
0011: PD[7] pin
0100: PE[7] pin
0101: PF[7] pin
0110: PG[7] pin

RM0440 Rev 9 369/2140
RM0440 System configurat ion controller (SYSCFG)
375
Note: Some of the I/O pins mentioned in the above register may not be available on small
packages.
10.2.5 SYSCFG external interrup t configuration register 3
(SYSCFG_EXTICR3)
Address offset: 0x10
Reset value: 0x0000 0000
Bits 11:8  EXTI6[3:0]: EXTI 6 configuration bits
These bits are written by software to select the source input for the EXTI6
external interrupt.
0000: PA[6] pin
0001: PB[6] pin
0010: PC[6] pin
0011: PD[6] pin
0100: PE[6] pin
0101: PF[6] pin
0110: PG[6] pin
Bits 7:4  EXTI5[3:0]: EXTI 5 configuration bits
These bits are written by software to select the source input for the EXTI5
external interrupt.
0000: PA[5] pin
0001: PB[5] pin
0010: PC[5] pin
0011: PD[5] pin
0100: PE[5] pin
0101: PF[5] pin
0110: PG[5] pin
Bits 3:0  EXTI4[3:0]: EXTI 4 configuration bits
These bits are written by software to select the source input for the EXTI4
external interrupt.
0000: PA[4] pin
0001: PB[4] pin
0010: PC[4] pin
0011: PD[4] pin
0100: PE[4] pin
0101: PF[4] pin
0110: PG[4] pin
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
EXTI11[3:0] EXTI10[3:0] EXTI9[3:0] EXTI8[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must be kept at reset value.

System configuration controller (SYSCFG) RM0440
370/2140 RM0440 Rev 9
Note: Some of the I/O pins mentioned in the above register may not be available on small
packages.
Bits 15:12  EXTI11[3:0]: EXTI 11 configuration bits
These bits are written by software to select the source input for the EXTI11
external interrupt.
0000: PA[11] pin
0001: PB[11] pin
0010: PC[11] pin
0011: PD[11] pin
0100: PE[11] pin
0101: PF[11] pin
Bits 11:8  EXTI10[3:0]: EXTI 10 configuration bits
These bits are written by software to select the source input for the EXTI10
external interrupt.
0000: PA[10] pin
0001: PB[10] pin
0010: PC[10] pin
0011: PD[10] pin
0100: PE[10] pin
0101: PF[10] pin
0110: PG[10] pin
Bits 7:4  EXTI9[3:0]: EXTI 9 configuration bits
These bits are written by software to select the source input for the EXTI9
external interrupt.
0000: PA[9] pin
0001: PB[9] pin
0010: PC[9] pin
0011: PD[9] pin
0100: PE[9] pin
0101: PF[9] pin
0110: PG[9] pin
Bits 3:0  EXTI8[3:0]: EXTI 8 configuration bits
These bits are written by software to select the source input for the EXTI8
external interrupt.
0000: PA[8] pin
0001: PB[8] pin
0010: PC[8] pin
0011: PD[8] pin
0100: PE[8] pin
0101: PF[8] pin
0110: PG[8] pin

RM0440 Rev 9 371/2140
RM0440 System configurat ion controller (SYSCFG)
375
10.2.6 SYSCFG external interrup t configuration register 4
(SYSCFG_EXTICR4)
Address offset: 0x14
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
EXTI15[3:0] EXTI14[3:0] EXTI13[3:0] EXTI12[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:12  EXTI15[3:0]: EXTI 15 configuration bits
These bits are written by software to select the source input for the EXTI15 external
interrupt.
0000: PA[15] pin
0001: PB[15] pin
0010: PC[15] pin
0011: PD[15] pin
0100: PE[15] pin
0101: PF[15] pin
Bits 11:8  EXTI14[3:0]: EXTI 14 configuration bits
These bits are written by software to select the source input for the EXTI14 external
interrupt.
0000: PA[14] pin
0001: PB[14] pin
0010: PC[14] pin
0011: PD[14] pin
0100: PE[14] pin
0101: PF[14] pin
Bits 7:4  EXTI13[3:0]: EXTI 13 configuration bits
These bits are written by software to select the source input for the EXTI13 external
interrupt.
0000: PA[13] pin
0001: PB[13] pin
0010: PC[13] pin
0011: PD[13] pin
0100: PE[13] pin
0101: PF[13] pin
Bits 3:0  EXTI12[3:0]: EXTI 12 configuration bits
These bits are written by software to select the source input for the EXTI12 external
interrupt.
0000: PA[12] pin
0001: PB[12] pin
0010: PC[12] pin
0011: PD[12] pin
0100: PE[12] pin
0101: PF[12] pin

System configuration controller (SYSCFG) RM0440
372/2140 RM0440 Rev 9
Note: Some of the I/O pins mentioned in the above register may not be available on small
packages.
10.2.7 SYSCFG CCM SRAM control and status register (SYSCFG_SCSR)
Address offset: 0x18
System reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res Res Res Res Res Res Res Res Res Res Res Res Res Res CCM
BSY
CCM
ER
rr w
Bits 31:2 Reserved, must be kept at reset value
Bit 1 CCMBSY: CCM SRAM busy by erase operation
0: No CCM SRAM erase operation is on going.
1: CCM SRAM erase operation is on going.
Bit 0 CCMER: CCM SRAM Erase
Setting this bit starts a hardware CCM SRAM erase operation. This bit is
automatically cleared at the end of the CCM SRAM erase operation.
Note: This bit is write-protected: setting this bit is possible only after the correct
key sequence is written in the SYSCFG_SKR register.

RM0440 Rev 9 373/2140
RM0440 System configurat ion controller (SYSCFG)
375
10.2.8 SYSCFG configuration register 2 (SYSCFG_CFGR2)
Address offset: 0x1C
System reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res Res Res Res Res Res Res SPF Res Res Res Res ECCL PVDL SPL CLL
r c _ w 1 r sr sr sr s
Bits 31:9 Reserved, must be kept at reset value
Bit 8 SPF: SRAM1 and CCM SRAM parity error flag
This bit is set by hardware when an SRAM1 or CCM SRAM parity error is
detected. It is cleared by software by writing ‘1’.
0: No parity error detected
1: Parity error detected
Bits 7:4 Reserved, must be kept at reset value
Bit 3 ECCL: ECC Lock
This bit is set by software and cleared only by a system reset. It can be used to
enable and lock the Flash ECC error connection to TIM1/8/15/16/17/20 break
input and hrtim_sys_flt input of HRTIM1.
0: ECC error disconnected from TIM1/8/15/16/17/20 break input and
hrtim_sys_flt input of HRTIM1.
1: ECC error connected to TIM1/8/15/16/17/20 break input and hrtim_sys_flt
input of HRTIM1.
Bit 2 PVDL: PVD lock enable bit
This bit is set by software and cleared only by a system reset. It can be used to
enable and lock the PVD connection to TIM1/8/15/16/17/20 break input and
hrtim_sys_flt input of HRTIM1., as well as the PVDE and PLS[2:0] in the
PWR_CR2 register.
0: PVD interrupt disconnected from TIM1/8/15/16/17/20 break input and
hrtim_sys_flt input of HRTIM1. PVDE and PLS[2:0] bits can be programmed by
the application.
1: PVD interrupt connected to TIM1/8/15/16/17/20 break input and hrtim_sys_flt
input of HRTIM1, PVDE and PLS[2:0] bits are read only.
Bit 1 SPL: SRAM1 and CCM SRAM parity lock bit
This bit is set by software and cleared only by a system reset. It can be used to
enable and lock the SRAM1 or CCM SRAM parity error signal connection to
TIM1/8/15/16/17/20 break input and hrtim_sys_flt input of HRTIM1.
0: CCM SRAM parity error signal disconnected from TIM1/8/15/16/17/20 break
input and hrtim_sys_flt input of HRTIM1.
1: CCM SRAM parity error signal connected to TIM1/8/15/16/17/20 break input
and hrtim_sys_flt input of HRTIM1.

System configuration controller (SYSCFG) RM0440
374/2140 RM0440 Rev 9
10.2.9 SYSCFG CCM SRAM write pr otection register (SYSCFG_SWPR)
Address offset: 0x20
System reset value: 0x0000 0000
10.2.10 SYSCFG CCM SRAM key  register (SYSCFG_SKR)
Address offset: 0x24
System reset value: 0x0000 0000
Bit 0 CLL: Cortex®-M4 LOCKUP (Hardfault) output enable bit
This bit is set by software and cleared only by a system reset. It can be used to
enable and lock the connection of Cortex®-M4 with FPU LOCKUP (Hardfault)
output to TIM1/8/15/16/17/20 break input and hrtim_sys_flt input of HRTIM1.
0: Cortex®-M4 LOCKUP output disconnected from TIM1/8/15/16/17/20 break
input and hrtim_sys_flt input of HRTIM1.
1: Cortex®-M4 LOCKUP output connected to TIM1/8/15/16/17/20 break input
and hrtim_sys_flt input of HRTIM1.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
P31WP P30WP P29WP P28WP P27WP P26WP P25WP P24WP P23WP P22WP P21WP P20WP P19WP P18WP P17WP P16WP
rs rs rs rs rs rs rs rs rs rs rs rs rs rs rs rs
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
P15WP P14WP P13WP P12WP P11WP P10WP P9WP P8WP P7WP P6WP P5WP P4WP P3WP P2WP P1WP P0WP
rs rs rs rs rs rs rs rs rs rs rs rs rs rs rs rs
Bits 31:0 PxWP (x = 0 to 31): CCM SRAM page x write protection
These bits are set by software and cleared only by a system reset.
0: Write protection of CCM SRAM page x is disabled.
1: Write protection of CCM SRAM page x is enabled.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res Res
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res Res Res Res Res Res Res Res KEY[7:0]
wwwwwwww
Bits 31:8 Reserved, must be kept at reset value
Bits 7:0 KEY[7:0]: CCM SRAM write protection key for software erase
The following steps are required to unlock the write protection of the CCMER bit
in the SYSCFG_SCSR register.
1. Write "0xCA” into Key[7:0]
2. Write "0x53” into Key[7:0]
Writing a wrong key reactivates the write protection.

RM0440 Rev 9 375/2140
RM0440 System configurat ion controller (SYSCFG)
375
10.2.11 SYSCFG register map
The following table gives the SYSCFG register map and the reset values.
Refer to Section 2.2 on page 82 for the register boundary addresses.
[Table 61](../tables/table_61.md). SYSCFG register map and reset values
Offset Register
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
0x00
SYSCFG_
MEMRMP
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
FB_MODE
Res.
Res.
Res.
Res.
Res.
MEM_
MODE
Reset value 0x x x
0x04
SYSCFG_CFGR1 FPU_IE[5..0]
Res.
Res.
I2C4_FMP
I2C3_FMP
I2C2_FMP
I2C1_FMP
I2C_PB9_FMP
I2C_PB8_FMP
I2C_PB7_FMP
I2C_PB6_FMP
Res.
Res.
Res.
Res.
Res.
Res.
ANASWVDD
BOOSTEN
Res.
Res.
Res.
Res.
Res.
Res.
Res.
FWDIS
R e s e t  v a l u e 011111 00000000 00 0001
0x08
SYSCFG_EXTICR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
EXTI3
[3:0]
EXTI2
[3:0]
EXTI1
[3:0]
EXTI0
[3:0]
R e s e t  v a l u e 0000000000000000
0x0C
SYSCFG_EXTICR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
EXTI7
[3:0]
EXTI6
[3:0]
EXTI5
[3:0]
EXTI4
[3:0]
R e s e t  v a l u e 0000000000000000
0x10
SYSCFG_EXTICR3
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
EXTI11
[3:0]
EXTI10
[3:0]
EXTI9
[3:0]
EXTI8
[3:0]
R e s e t  v a l u e 0000000000000000
0x14
SYSCFG_EXTICR4
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
EXTI15
[3:0]
EXTI14
[3:0]
EXTI13
[3:0]
EXTI12
[3:0]
R e s e t  v a l u e 0000000000000000
0x18
SYSCFG_SCSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCMBSY
CCMER
Reset value 00
0x1C
SYSCFG_CFGR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SPF
Res.
Res.
Res.
Res.
ECCL
PVDL
SPL
CLL
Reset value 00 0 0 0
0x20
SYSCFG_SWPR
P31WP
P30WP
P29WP
P28WP
P27WP
P26WP
P25WP
P24WP
P23WP
P22WP
P21WP
P20WP
P19WP
P18WP
P17WP
P16WP
P15WP
P14WP
P13WP
P12WP
P11WP
P10WP
P9WP
P8WP
P7WP
P6WP
P5WP
P4WP
P3WP
P2WP
P1WP
P0WP
R e s e t  v a l u e 00000000000000000000000000000000
0x24
SYSCFG_SKR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. KEY
Reset value 00000000
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* [Table 60: Configuration Matrix](../tables/table_60.md)
* [Table 61: Configuration Matrix](../tables/table_61.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)