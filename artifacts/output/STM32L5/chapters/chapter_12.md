# Chapter 12: System configuration controller (SYSCFG)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 12: System configuration controller (SYSCFG).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 456 - 468
* **Taxonomy Section**: SYSTEM
* **Parent IP Module**: [System Configuration (SYSCFG)](../system/syscfg.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
System configuration controller (SYSCFG) RM0438
456/2187 RM0438 Rev 8
12 System configuration controller (SYSCFG)
12.1 SYSCFG main features
The STM32L552xx and STM32L552xx devices feature a set of configuration registers.
The main purposes of the system configuration controller are the following:
• Managing robustness feature
• Setting SRAM2 write protection and software erase
• Configuring FPU interrupts
• Enabling/disabling the I2C fast-mode plus driving capability on some I/Os and voltage
booster for I/Os analog switches
• Configuring TrustZone security register access
12.2 SYSCFG TrustZone security and privilege
SYSCFG TrustZone security
When the TrustZone security is activated, the SYSCFG is able to secure registers from
being modified by non-secure accesses.
The TrustZone security is activated by the TZEN option bit in the FLASH_OPTR register.
A non-secure read/write access to a secured register is RAZ/WI and generates an illegal
access event. An illegal access interrupt is generated if the SYSCFG illegal access event is
enabled in the GTZC_TZIC_IER register.
Privileged/unprivileged mode
The SYSCFG registers can be read and written by privileged and unprivileged accesses
except the SYSCFG registers for CPU configuration: SYSCFG_CSLCKR,
SYSCFG_FPUIMR and SYSCFG_CNSLCKR registers.
An unprivileged access to a privileged register is RAZ/WI.
The table below shows the register security overview.
[Table 92](../tables/table_92.md). TrustZone security and privilege register accesses
SYSCFG register
name
Read/write access with TrustZone configuration(1) Privileged
/unprivileged access
TZEN = 1 TZEN = 0 NA
SYSCFG_
SECCFGR
Read: no restriction
Write: secure access only
Write non-secure: is WI and generates an illegal access
event
RAZ/WI No restriction
SYSCFG_CSLCKR
Read/Write: secure access only
Read/Write non-secure: is RAZ/WI and generates and
an illegal access event
RAZ/WI Privileged only
Unprivileged: RAZ/WI

RM0438 Rev 8 457/2187
RM0438 System configurat ion controller (SYSCFG)
468
SYSCFG_FPUIMR
Read/Write secure access only if FPUSEC bit is set
Read/Write non-secure: is RAZ/WI and generates an
illegal access event
No
restriction
Privileged only
Unprivileged: RAZ/WI
SYSCFG_CNSLCKR Read/wri te: no restriction No
restriction
Privileged only
Unprivileged: RAZ/WI
SYSCFG_CFGR1
Read/Write: secure access only for secure bits
depending on peripheral security bits in
GTZSC_SECFGR register
Read/Write non-secure: only for non-secure bits,
otherwise is RAZ/WI
No
restriction No restriction
SYSCFG_SWPR,
SYSCFG_SWPR2,
SYSCFG_SKR,
SYSCFG_SCSR
– If SRAM2SEC bit is set:
Read/Write: secure access only
Read/Write Non-secure: is RAZ/WI and generates an
illegal access event
– If SRAM2SEC bit is reset:
Read/Write: no restriction
No
restriction No restriction
SYSCFG_CFGR2
– If CLASSBSEC bit is set:
Read/Write: secure access only
Read/Write Non-secure: is RAZ/WI and generates an
illegal access event
– If CLASSBSEC bit is reset:
Read/Write: no restriction
No
restriction No restriction
SYSCFG_
RSSCMDR RAZ/WI if register access is not allowed(2) RAZ/WI No restriction
1. TrustZone security is activated by the TZEN option bit in the FLASH_OPTR register.
2. Refer to register description for register access.
[Table 92](../tables/table_92.md). TrustZone security and privilege register accesses (continued)
SYSCFG register
name
Read/write access with TrustZone configuration(1) Privileged
/unprivileged access
TZEN = 1 TZEN = 0 NA

System configuration controller (SYSCFG) RM0438
458/2187 RM0438 Rev 8
12.3 SYSCFG registers
12.3.1 SYSCFG secure configurat ion register (SYSCFG_SECCFGR)
Address offset: 0x00
Reset value: 0x0000 0000
When the system is secure (TZEN = 1), this register provides write access security and can
be written only when the access is secure. It can be globally write-protected, or each bit of
this register can be individually write-protected.A non-secure write access is WI and
generates an illegal access event. There are no read restrictions.
When the system is not secure (TZEN = 0), this register is RAZ/WI.
This register can be read and written by privileged and unprivileged access.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. FPUSE
C
SRAM2
SEC
CLASS
BSEC
SYSCF
GSEC
rw rw rw rw
Bits 31:4 Reserved, must be kept at reset value.
Bit 3 FPUSEC: FPU security
0: SYSCFG_FPUIMR register can be written by secure and non-secure access.
1: SYSCFG_FPUIMR register can be written by secure access only.
Bit 2 SRAM2SEC: SRAM2 security
0: SYSCFG_SKR, SYSCFG_SCR, and SYSCFG_SWPRx registers can be written by secure
and non-secure access.
1: SYSCFG_SKR, SYSCFG_SCR, and SYSCFG_SWPRx register can be written by secure
access only.
Bit 1 CLASSBSEC: ClassB security
0: SYSCFG_CFGR2 register can be written by secure and non-secure access.
1: SYSCFG_CFGR2 register can be written by secure access only.
Bit 0 SYSCFGSEC: SYSCFG clock control security
0: SYSCFG configuration clock in RCC registers can be written by secure and non-secure
access.
1: SYSCFG configuration clock in RCC registers can be written by secure access only.

RM0438 Rev 8 459/2187
RM0438 System configurat ion controller (SYSCFG)
468
12.3.2 SYSCFG configuration register 1 (SYSCFG_CFGR1)
Address offset: 0x04
Reset value: 0x0000 0000
When the system is secure (TZEN = 1), this register can be a mix of secure and non-secure
bits depending on I2Cx, ADC security configuration bit in TZSC_SECCFGR register and
GPIO security bits. A non-secure read/write access on secured bits is RAZ/WI.
When the system is not secure (TZEN = 0), there is no access restriction.
This register can be read and written by privileged and unprivileged access.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. I2C4_
FMP
I2C3_
FMP
I2C2
_FMP
I2C1
_FMP
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
rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. ANAS
WVDD
BOOST
EN Res. Res. Res. Res. Res. Res. Res. Res.
rw rw
Bits 31:24 Reserved, must  be kept at reset value.
Bit 23 I2C4_FMP: I2C4 fast-mode plus (Fm+) driving capability activation.
This bit enables the Fm+ driving mode on I2C4 pins selected through AF selection bits.
0: Fm+ mode is not enabled on I2C4 pins selected through AF selection bits.
1: Fm+ mode is enabled on I2C4 pins selected through AF selection bits.
Bit 22 I2C3_FMP: 12C3 fast-mode plus driving capability activation
This bit enables the Fm+ driving mode on I2C3 pins selected through AF selection bits.
0: Fm+ mode is not enabled on I2C3 pins selected through AF selection bits.
1: Fm+ mode is enabled on I2C3 pins selected through AF selection bits.
Bit 21 I2C2_FMP: 12C2 fast-mode plus driving capability activation
This bit enables the Fm+ driving mode on I2C3 pins selected through AF selection bits.
0: Fm+ mode is not enabled on I2C2 pins selected through AF selection bits.
1: Fm+ mode is enabled on I2C2 pins selected through AF selection bits.
Bit 20 I2C1_FMP: 12C1 fast-mode plus driving capability activation
This bit enables the Fm+ driving mode on I2C3 pins selected through AF selection bits.
0: Fm+ mode is not enabled on I2C1 pins selected through AF selection bits.
1: Fm+ mode is enabled on I2C1 pins selected through AF selection bits.
Bit 19 I2C_PB9_FMP: 12C1 fast-mode plus driving capability activation on PB9
This bit enables the Fm+ driving mode for PB9.
0: PB9 pin operates in standard mode.
1: Fm+ mode is enabled on PB9 pin, and the speed control is bypassed.
Bit 18 I2C_PB8_FMP: 12C1 fast-mode plus driving capability activation on PB8
This bit enables the Fm+ driving mode for PB8.
0: PB8 pin operates in standard mode.
1: Fm+ mode is enabled on PB8 pin, and the speed control is bypassed.

System configuration controller (SYSCFG) RM0438
460/2187 RM0438 Rev 8
The table below describes when the bit 8 (BOOSTEN) and the bit 9 (ANASWVDD) must be
set or reset depending on the voltage settings.
Bit 17 I2C_PB7_FMP: 12C1 fast-mode plus driving capability activation on PB7
This bit enables the Fm+ driving mode for PB7.
0: PB7 pin operates in standard mode.
1: Fm+ mode is enabled on PB7 pin, and the speed control is bypassed.
Bit 16 I2C_PB6_FMP: 12C1 fast-mode plus driving capability activation on PB6
This bit enables the Fm+ driving mode for PB6.
0: PB6 pin operates in standard mode.
1: Fm+ mode is enabled on PB6 pin, and the speed control is bypassed.
Bits 15:10 Reserved, must  be kept at reset value.
Bit 9 ANASWVDD: GPIO analog switch control voltage selection
0: I/O analog switches supplied by VDDA or booster when booster is on
1: I/O analog switches supplied by VDD.
Note: Refer to [Table 93](../tables/table_93.md): BOOSTEN and ANASWVDD set/reset for bit 9 setting.
Bit 8 BOOSTEN: I/O analog switch voltage booster enable.
0: I/O analog switches are supplied by VDDA voltage. This is the recommended configuration
when using the ADC in high VDDA voltage operation.
1: I/O analog switches are supplied by a dedicated voltage booster (supplied by VDD). This is
the recommended configuration when using the ADC in low VDDA voltage operation.
Note: Refer to [Table 93](../tables/table_93.md): BOOSTEN and ANASWVDD set/reset for bit 8 setting.
Bits 7:0 Reserved, must be kept at reset value.
[Table 93](../tables/table_93.md). BOOSTEN and ANASWVDD set/reset
VDD VDDA BOOSTEN ANASWVDD
- > 2.4 V
0
0
> 2.4 V
< 2.4 V
1
< 2.4 V 1 0

RM0438 Rev 8 461/2187
RM0438 System configurat ion controller (SYSCFG)
468
12.3.3 FPU interrupt mask register (SYSCFG_FPUIMR)
Address offset: 0x08
Reset value: 0x0000 001F
When the system is secure (TZEN =1), this register can be protected against non-secure
access by setting the FPUSEC bit in the SYSCFG_SECCFGR register. A non-secure
read/write access is RAZ/WI and generates an illegal access event.
When the system is not secure (TZEN=0), there is no access restriction.
This register can be read and written by privileged access only. Unprivileged access is
RAZ/WI.
12.3.4 SYSCFG CPU non-secure lock register (SYSCFG_CNSLCKR)
Address offset: 0x0C
Reset value: 0x0000 0000
This register is used to lock the configuration of non-secure MPU and VTOR_NS registers.
This register can be read and written by privileged access only. Unprivileged access is
RAZ/WI.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. FPU_IE[5:0]
rw rw rw rw rw rw
Bits 31:6 Reserved, must be kept at reset value.
Bits 5:0 FPU_IE[5:0]: Floating point unit interrupts enable bits
FPU_IE[5]: Inexact interrupt enable (interrupt disable at reset)
FPU_IE[4]: Input abnormal interrupt enable
FPU_IE[3]: Overflow interrupt enable
FPU_IE[2]: Underflow interrupt enable
FPU_IE[1]: Divide-by-zero interrupt enable
FPU_IE[0]: Invalid operation Interrupt enable
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. LOCKN
SMPU
LOCKN
SVTOR
rs rs
Bits 31:2 Reserved, must be kept at reset value.

System configuration controller (SYSCFG) RM0438
462/2187 RM0438 Rev 8
12.3.5 SYSCFG CPU secure lock register (SYSCFG_CSLOCKR)
Address offset: 0x10
Reset value: 0x0000 0000
This register is used to lock the configuration of PRIS and BFHFNMINS bits in the AIRCR
register, SAU, secure MPU and VTOR_S registers.
When the system is secure (TZEN = 1), this register can be written only when the access is
secure. A non-secure read/write access is RAZ/WI and generates an illegal access event.
When the system is not secure (TZEN = 0), this register is RAZ/WI
This register can be read and written by privileged access only. Unprivileged access is
RAZ/WI.
Bit 1 LOCKNSMPU: Non-secure MPU registers lock
This bit is set by software and cleared only by a system reset. When is set, it disables write
access to non-secure MPU_CTRL_NS, MPU_RNR_NS and MPU_RBAR_NS registers.
0: Non-secure MPU registers write is enabled.
1: Non-secure MPU registers write is disabled.
Bit 0 LOCKNSVTOR: VTOR_NS register lock
This bit is set by software and cleared only by a system reset.
0: VTOR_NS register write is enabled.
1: VTOR_NS register write is disabled.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. LOCKS
AU
LOCKS
MPU
LOCKS
VTAIR
CR
rs rs rs
Bits 31:3 Reserved, must be kept at reset value.
Bit 2 LOCKSAU: SAU registers lock
This bit is set by software and cleared only by a system reset. When is set, it disables write
access to SAU_CTRL, SAU_RNR, SAU_RBAR and SAU_RLAR registers.
0: SAU registers write is enabled.
1: SAU registers write is disabled.
Bit 1 LOCKSMPU: Secure MPU registers lock
This bit is set by software and cleared only by a system reset. When is set, it disables write
access to secure MPU_CTRL, MPU_RNR and MPU_RBAR registers.
0: Secure MPU registers writes is enabled.
1: Secure MPU registers writes is disabled.
Bit 0 LOCKSVTAIRCR: VTOR_S register and AIRCR register bits lock
This bit is set by software and cleared only by a system reset. When is set, it disables write
access to VTOR_S register, PRIS and BFHFNMINS bits in the AIRCR register.
0: VTOR_S register PRIS and BFHFNMINS bits in the AIRCR register write is enabled.
1: VTOR_S register PRIS and BFHFNMINS bits in the AIRCR register write is disabled.

RM0438 Rev 8 463/2187
RM0438 System configurat ion controller (SYSCFG)
468
12.3.6 SYSCFG configuration register 2 (SYSCFG_CFGR2)
Address offset: 0x14
Reset value: 0x0000 0000
When the system is secure (TZEN = 1), this register can be protected against non-secure
access by setting the CLASSBSEC bit in the SYSCFG_SECCFGR register. When
CLASSBSEC bit is set, only secure access is allowed. A non-secure read/write access is
RAZ/WI and generates an illegal access event.
When the system is not secure (TZEN = 0), there is no access restriction.
This register can be read and written by privileged and unprivileged access.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. SPF Res. Res. Res. Res. ECCL PVDL SPL CLL
r c _ w 1 r sr sr sr s
Bits 31:9 Reserved, must be kept at reset value.
Bit 8 SPF: SRAM2 parity error flag
This bit is set by hardware when an SRAM2 parity error is detected. It is cleared by software
by writing 1.
0: No SRAM2 parity error detected
1: SRAM2 parity error detected
Bits 7:4 Reserved, must be kept at reset value.
Bit 3 ECCL: ECC lock
This bit is set by software and cleared only by a system reset. It can be used to enable and
lock the flash ECC error connection to TIM1/8/15/16/17 Break input.
0: ECC error disconnected from TIM1/8/15/16/17 break input
1: ECC error connected to TIM1/8/15/16/17 break input.
Bit 2 PVDL: PVD lock enable bit
This bit is set by software and cleared only by a system reset. It can be used to enable and
lock the PVD connection to TIM1/8/15/16/17 break input, as well as the PVDE and PLS[2:0]
in the PWR_CR2 register.
0: PVD interrupt disconnected from TIM1/8/15/16/17 break input. PVDE and PLS[2:0] bits
can be programmed by the application.
1: PVD interrupt connected to TIM1/8/15/16/17 break input, PVDE and PLS[2:0] bits are read
only.
Bit 1 SPL: SRAM2 parity lock bit
This bit is set by software and cleared only by a system reset. It can be used to enable and
lock the SRAM2 parity error signal connection to TIM1/8/15/16/17 break inputs.
0: SRAM2 parity error signal disconnected from TIM1/8/15/16/17 break inputs
1: SRAM2 parity error signal connected to TIM1/8/15/16/17 break inputs

System configuration controller (SYSCFG) RM0438
464/2187 RM0438 Rev 8
12.3.7 SYSCFG SRAM2 control and status register (SYSCFG_SCSR)
Address offset: 0x18
Reset value: 0x0000 0000
When the system is secure (TZEN =1), this register can be protected against non-secure
access by setting the SRAM2SEC bit in the SYSCFG_SECCFGR register. When
SRAM2SEC bit is set, only secure access is allowed. A non-secure read/write access is
RAZ/WI and generates an illegal access event.
When the system is not secure (TZEN=0), here is no access restriction.
This register can be read and written by privileged and unprivileged access.
Bit 0 CLL: Cortex-M33 LOCKUP (HardFault) output enable bit
This bit is set by software and cleared only by a system reset. It can be used to enable and
lock the connection of Cortex-M33 LOCKUP (hardfault) output to TIM1/8/15/16/17 break
input.
0: Cortex-M33 LOCKUP output disconnected from TIM1/8/15/16/17 break inputs
1: Cortex-M33 LOCKUP output connected to TIM1/8/15/16/17 break inputs
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. SRAM2
BSY
SRAM2
ER
rr w
Bits 31:2 Reserved, must be kept at reset value.
Bit 1 SRAM2BSY: SRAM2 busy by erase operation
0: No SRAM2 erase operation ongoing
1: SRAM2 erase operation ongoing
Bit 0 SRAM2ER: SRAM2 erase
Setting this bit starts a hardware SRAM2 erase operation. This bit is automatically cleared at
the end of the SRAM2 erase operation
Note: This bit is write-protected:  setting this bit is possible only after the correct key sequence
is written in the SYSCFG_SKR register.

RM0438 Rev 8 465/2187
RM0438 System configurat ion controller (SYSCFG)
468
12.3.8 SYSCFG SRAM2 key re gister (SYSCFG_SKR)
Address offset: 0x1C
Reset value: 0x0000 0000
When the system is secure (TZEN = 1), this register can be protected against non-secure
access by setting the SRAM2SEC bit in the SYSCFG_SECCFGR register. When
SRAM2SEC bit is set, only secure access is allowed. A non-secure read/write access is
RAZ/WI and generates an illegal access event.
When the system is not secure (TZEN = 0), there is no access restriction.
This register can be read and written by privileged and unprivileged access.
w
12.3.9 SYSCFG SRAM2 write protec tion register (SYSCFG_SWPR)
Address offset: 0x20
Reset value: 0x0000 0000
When the system is secure (TZEN =1), this register can be protected against non-secure
access by setting the SRAM2SEC bit in the SYSCFG_SECCFGR register. When
SRAM2SEC bit is set, only secure access is allowed. A non-secure read/write access is
RAZ/WI and generates an illegal access event.
When the system is not secure (TZEN=0), there is no access restriction.
This register can be read and written by privileged and unprivileged access.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. KEY[7:0]
wwwwwwww
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 KEY[7:0]: SRAM2 write protection key for software erase
The following steps are required to unlock the write protection of SRAM2ER
in SYSCFG_CFGR2.
0: Write 0xCA into Key[7:0].
1: Write 0x53 into Key[7:0].
Writing a wrong key reactivates the write protection.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
P31WP P30WP P29WP P28WP P27WP P26WP P25WP P24WP P23WP P22WP P21WP P20WP P19WP P18WP P17WP P16WP
rs rs rs rs rs rs rs rs rs rs rs rs rs rs rs rs
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
P15WP P14WP P13WP P12WP P11WP P10WP P9WP P8WP P7WP P6WP P5WP P4WP P3WP P2WP P1WP P0WP
rs rs rs rs rs rs rs rs rs rs rs rs rs rs rs rs

System configuration controller (SYSCFG) RM0438
466/2187 RM0438 Rev 8
12.3.10 SYSCFG SRAM2 wr ite protection register 2 (SYSCFG_SWPR2)
Address offset: 0x24
Reset value: 0x0000 0000
When the system is secure (TZEN = 1), this register can be protected against non-secure
access by setting the SRAM2SEC bit in the SYSCFG_SECCFGR register. When
SRAM2SEC bit is set, only secure access is allowed. A non-secure read/write access is
RAZ/WI and generates an illegal access event.
When the system is not secure (TZEN = 0), there is no access restriction.
This register can be read and written by privileged and unprivileged access.
12.3.11 SYSCFG RSS command re gister (SYSCFG_RSSCMDR)
Address offset: 0x2C
Power-on reset value: 0x0000 0000
System reset: not affected
When the system is secure (TZEN = 1), this register can be read and written only when the
APB access is secure. Otherwise it is RAZ/WI.
When the system is not secure (TZEN = 0), this register is RAZ/WI.
This register can be read and written by privileged and unprivileged access.
Bits 31:0 PxWP: SRAM2 1 Kbyte page x write protection (x = 31 to 0)
These bits are set by software and cleared only by a system reset.
0: Write protection of SRAM2 1-Kbyte page x is disabled.
1: Write protection of SRAM2 1-Kbyte page x is enabled.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
P63WP P62WP P61WP P60WP P59WP P58WP P57WP P56WP P55WP P54WP P53WP P52WP P51WP P50WP P49WP P48WP
rs rs rs rs rs rs rs rs rs rs rs rs rs rs rs rs
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
P47WP P46WP P45WP P44WP P43WP P42WP P41WP P40WP P39WP P38WP P37WP P36WP P35WP P34WP P33WP P32WP
rs rs rs rs rs rs rs rs rs rs rs rs rs rs rs rs
Bits 31:0 PxWP: SRAM2 1 Kbyte page x write protection (x = 63 to 32)
These bits are set by software and cleared only by a system reset.
0: Write protection of SRAM2 1-Kbyte page x is disabled.
1: Write protection of SRAM2 1-Kbyte page x is enabled.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
RSSCMD[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 467/2187
RM0438 System configurat ion controller (SYSCFG)
468
ì
12.3.12 SYSCFG register map
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 RSSCMD[15:0]: RSS commands
Defines a command to be executed by the RSS.
0x01C0: request boot from RSS with jump to bootloader when BOOT_LOCK bitfield from
FLASH_SECBOOTADD0R option byte register and FLASH_OPTR_nBOOT0
bitfield from FLASH_OPTR option byte register are cleared.
[Table 94](../tables/table_94.md). SYSCFG register map and reset values
Offset Register name
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
0x00 SYSCFG_SECCFGR
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
FPUSECC
SRAM2SEC
CLASSBSEC
SYSCFGSEC
Reset value 0000
0x04 SYSCFG_CFGR1
Res.
Res.
Res.
Res.
Res.
Res.
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
Res.
R e s e t  v a l u e 00000000 00
0x08 SYSCFG_FPUIMR
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
Res. FPU_IE[5:0]
Reset value 111111
0x0C SYSCFG_ CNSLCKR
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
LOCKNSMPU
LOCKNSVTOR
Reset value 00
0x10 SYSCFG _CSLOCKR
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
LOCKSAU
LOCKSMPU
LOCKSVTAIRCR
Reset value 000
0x14 SYSCFG_CFGR2
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
SSPF
Res.
Res.
Res.
Res.
ECCL
PVDL
SPL
CLL.
Reset value 00 0 0 0
0x18 SYSCFG_SCSR
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
SRAM2BS
SRAM2ER
Reset value 00
0x1C SYSCFG_SKR
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
Res. KEY [7:0]
Reset value 00000000
0x20 SYSCFG_SWPR
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
0x24 SYSCFG_SWPR2
P63WP
P62WP
P61WP
P60WP
P59WP
P58WP
P57WP
P56WP
P55WP
P54WP
P53WP
P52WP
P51WP
P50WP
P49WP
P48WP
P47WP
P46WP
P45WP
P44WP
P43WP
P42WP
P41WP
P40WP
P39WP
P38WP
P37WP
P36WP
P35WP
P34WP
P33WP
P32WP
R e s e t  v a l u e 00000000000000000000000000000000

System configuration controller (SYSCFG) RM0438
468/2187 RM0438 Rev 8
Refer to Section 2.3 for the register boundary addresses.
0x2C
SYSCFG_RSSCMDR
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
Res. RSSCMD[15:0]
P o w e r - o n  r e s e t  v a l u e 0000000000000000
S y s t e m  r e s e t  v a l u e 0000000000000000
[Table 94](../tables/table_94.md). SYSCFG register map and reset values (continued)
Offset Register name
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
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* [Table 92: Configuration Matrix](../tables/table_92.md)
* [Table 93: Configuration Matrix](../tables/table_93.md)
* [Table 94: Configuration Matrix](../tables/table_94.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)