# Chapter 9: System configuration controller (SYSCFG)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32C0 Reference Manual RM0490 - Chapter 9: System configuration controller (SYSCFG).
* **Document Source**: RM0490 Reference Manual
* **PDF Reference Location**: Pages 196 - 217
* **Taxonomy Section**: SYSTEM
* **Parent IP Module**: [System Configuration (SYSCFG)](../system/syscfg.md)

## 2. Official Reference Manual Text Content (RM0490 Ingestion)
```text
System configuration controller (SYSCFG) RM0490
196/1023 RM0490 Rev 6
9 System configuration controller (SYSCFG)
The devices feature a set of configuration registers. The main purposes of the system
configuration controller are the following:
• Enabling/disabling I2C-bus Fast-mode Plus mode on some I/O ports
• Configuring the IR modulation signal and its output polarity
• Remapping of some I/O ports
• Remapping the memory located at the beginning of the code area
• Flag pending interrupts from each interrupt line
• Managing robustness feature
9.1 SYSCFG registers
9.1.1 SYSCFG configuration register 1 (SYSCFG_CFGR1)
This register is used for specific configurations of memory remap and to control special I/O
features.
Two bits are used to configure the type of memory accessible at address 0x0000 0000.
These bits are used to select the physical remap by software and so, bypass the hardware
BOOT selection. After reset these bits take the value selected by the actual boot mode
configuration.
If the Fm+ mode is desired on the I2C pins, first assign GPIOs to I2Cx through the
GPIOx_AFRH or GPIOx_AFRL alternate function registers and then only activate the Fm+
mode.
The Fm+ mode on a GPIO y used as I2Cx can individually be activated by setting its
corresponding I2C_y_FMP bit. It can also collectively be activated for GPIOs used as I2Cx,
by setting the I2Cx_FMP bit. If the Fm+ mode is not desired on a GPIO y used as I2Cx, both
I2C_y_FMP and I2Cx_FMP bits must be cleared.
When the Fm+ mode is activated, the speed configuration of the I/O (GPIOx OSPEEDR) is
ignored.
Address offset: 0x00
Reset value: 0x0000 000X (X is the memory mode selected by the actual boot mode
configuration)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res.
I2C_
PC14_
FMP
I2C_
PA10_
FMP
I2C_
PA9_
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
rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. IR_MOD[1:0] IR_POL PA12_RMP PA11_RMP Res. MEM_MODE[1:0]
rw rw rw rw rw rw rw

RM0490 Rev 6 197/1023
RM0490 System configurat ion controller (SYSCFG)
217
Bits 31:25 Reserved, must  be kept at reset value.
Bit 24 I2C_PC14_FMP: Fast-mode Plus (Fm+) enable for PC14
This bit is set and cleared by software. It enables I2C Fm+ driving capability on PC14 I/O
port.
0: Disable if not enabled through I2Cx_FMP
1: Enable
Note: Not available on STM32C011xx.
Bit 23 I2C_PA10_FMP: Fast-mode Plus (Fm+) enable for PA10
This bit is set and cleared by software. It enables I2C Fm+ driving capability on PA10 I/O
port.
0: Disable disabled if not enabled through I2Cx_FMP
1: Enable
Bit 22 I2C_PA9_FMP: Fast-mode Plus (Fm+) enable for PA9
This bit is set and cleared by software. It enables I2C Fm+ driving capability on PA9 I/O port.
0: Disable disabled if not enabled through I2Cx_FMP
1: Enable
Bit 21 I2C2_FMP: Fast-mode Plus (Fm+) enable for I2C2
This bit is set and cleared by software. It enables I2C Fm+ driving capability on I/O ports
configured as I2C2 through GPIOx_AFR registers.
0: Disable disabled if not enabled through I2C_y_FMP
1: Enable
Note: Only applicable to STM32C051xx, STM32C071xx, and STM32C091xx/92xx. Reserved
on the other products.
Bit 20 I2C1_FMP: Fast-mode Plus (Fm+) enable for I2C1
This bit is set and cleared by software. It enables I2C Fm+ driving capability on I/O ports
configured as I2C1 through GPIOx_AFR registers.
0: Disable disabled if not enabled through I2C_y_FMP
1: Enable
Bit 19 I2C_PB9_FMP: Fast-mode Plus (Fm+) enable for PB9
This bit is set and cleared by software. It enables I2C Fm+ driving capability on PB9 I/O port.
0: Disable disabled if not enabled through I2Cx_FMP
1: Enable
Note: Not available on STM32C011xx.
Bit 18 I2C_PB8_FMP: Fast-mode Plus (Fm+) enable for PB8
This bit is set and cleared by software. It enables I2C Fm+ driving capability on PB8 I/O port.
0: Disable disabled if not enabled through I2Cx_FMP
1: Enable
Note: Not available on STM32C011xx.
Bit 17 I2C_PB7_FMP: Fast-mode Plus (Fm+) enable for PB7
This bit is set and cleared by software. It enables I2C Fm+ driving capability on PB7 I/O port.
0: Disable disabled if not enabled through I2Cx_FMP
1: Enable
Bit 16 I2C_PB6_FMP: Fast-mode Plus (Fm+) enable for PB6
This bit is set and cleared by software. It enables I2C Fm+ driving capability on PB6 I/O port.
0: Disable disabled if not enabled through I2Cx_FMP
1: Enable
Bits 15:8 Reserved, must be kept at reset value.

System configuration controller (SYSCFG) RM0490
198/1023 RM0490 Rev 6
9.1.2 SYSCFG configuration register 2 (SYSCFG_CFGR2)
Address offset: 0x18
Reset value: 0x0000 0000
Bits 7:6 IR_MOD[1:0]: IR Modulation Envelope signal selection
This bitfield selects the signal for IR modulation envelope:
00: TIM16
01: USART1
10: USART2
11: Reserved
Bit 5 IR_POL: IR output polarity selection
0: Output of IRTIM (IR_OUT) is not inverted
1: Output of IRTIM (IR_OUT) is inverted
Bit 4 PA12_RMP: PA12 pin remapping
This bit is set and cleared by software. When set, it remaps the PA12 pin to operate as PA10
GPIO port, instead as PA12 GPIO port. In this case, the original PA10 pin (if available) is
forced to analog mode.
0: No remap (PA12)
1: Remap (PA10)
Note: If the PINMUX4[1:0] bitfie ld of the SYSCFG_CFGR3 register is at 00, PA12_RMP must
be kept at 0 to prevent conflict due to two GPIO outputs with different output levels
connected to the same pin.
Bit 3 PA11_RMP: PA11 pin remapping
This bit is set and cleared by software. When set, it remaps the PA11 pin to operate as PA9
GPIO port, instead as PA11 GPIO port. In this case, the original PA9 pin (if available) is
forced to analog mode.
0: No remap (PA11)
1: Remap (PA9)
Note: If the PINMUX2[1:0]  bitfield of the SYSCFG_CFGR3 register is at 00, PA11_RMP must
be kept at 0 to prevent conflict due to two GPIO outputs with different output levels
connected to the same pin.
Bit 2 Reserved, must be kept at reset value.
Bits 1:0 MEM_MODE[1:0]: Memory mapping selection bits
This bitfield controlled by software selects the memory internally mapped at the address
0x0000 0000. Its reset value is determined by the boot mode configuration. Refer to
Section 3: Boot modes for more details.
x0: Main flash memory
01: System flash memory
11: Embedded SRAM
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res.
LOCKU
P_LOC
K
rw

RM0490 Rev 6 199/1023
RM0490 System configurat ion controller (SYSCFG)
217
9.1.3 SYSCFG configuration register 3 (SYSCFG_CFGR3)
In some products/packages with low pin count, several GPIOs may be internally connected
to the same pin. This register allows selecting the active GPIO that keeps the setting
specified by its corresponding GPIOx_MODER register. For STM32C011xx, STM32C031xx,
and STM32C071xx, the other GPIOs connected to the same pin are forced into digital input
(passive) mode regardless of their corresponding GPIOx_MODER register settings. For
STM32C051xx and STM32C091xx/92xx, the output buffer of the other GPIOs connected to
the same pin are disabled regardless of their corresponding GPIOx_MODER register
settings.
This is only effective when the SECURE_MUXING_EN bit of the FLASH option register
(FLASH_OPTR) is set (default).
When SECURE_MUXING_EN is cleared, SYSCFG_CFGR3 has no effect. All GPIOs
connected to the same pin keep the configuration set in their corresponding
GPIOx_MODER register. The user software must then ensure that there is no conflict
between the GPIOs.
In the following bitfield descriptions, for products/packages not listed in the “condition”
preceding the bitfield values, consider the bitfield as reserved and keep it at its reset value.
Address offset: 0x3C
Reset value: 0x0000 0000
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 LOCKUP_LOCK: Cortex®-M0+ LOCKUP enable
This bit is set by software and cleared by system reset. When set, it enables the connection
of Cortex®-M0+ LOCKUP (HardFault) output to the TIM1/16/17 Break input.
0: Disable
1: Enable
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PINMUX7[1:0] PINMUX6[1:0] PINMUX5[1:0] PINMUX4[1:0] PINMUX3[1:0] PINMUX2[1:0] PINMUX1[1:0] PINMUX0[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:14 PINMUX7[1:0]: Pin GPIO multiplexer 7
This bitfield is set and cleared by software. It selects an active GPIO on a pin.
Condition: STM32C051x - GPIO assigned to WLCSP15 ball A2 or TSSOP20 pin 1
00: PB7
01: PB8
Other: Reserved

System configuration controller (SYSCFG) RM0490
200/1023 RM0490 Rev 6
Bits 13:12 PINMUX6[1:0]: Pin GPIO multiplexer 6
This bitfield is set and cleared by software. It selects an active GPIO on a pin.
Condition: STM32C051x - GPIO assigned to WLCSP15 ball B1 or TSSOP20 pin 20
00: PB6
01: PB3
10: PB4
11: PB5
Bits 11:10 PINMUX5[1:0]: Pin GPIO multiplexer 5
This bitfield is set and cleared by software. It selects an active GPIO on a pin.
Condition: STM32C011x - GPIO assigned to WLCSP12 ball F1
00: PA3
01: PA4
10: PA5
11: PA6
Condition: STM32C051xx - GPIO assigned to WLCSP15 ball E2 or TSSOP20 pin 19
00: PA14-BOOT0
01: PA15
Other: Reserved
Bits 9:8 PINMUX4[1:0]: Pin GPIO multiplexer 4
This bitfield is set and cleared by software. It selects an active GPIO on a pin.
Condition: STM32C011x - GPIO assigned to WLCSP12 ball E2
00: PA7
01: PA12
Other: Reserved
Condition: STM32C051xx - GPIO assigned to WLCSP15 ball H1
00: PA7
01: PA12 [PA10]
Other: Reserved
Condition: STM32C091/92xx - GPIO assigned to TSSOP20 pin 1 or WLCSP24 ball B4
00: PB7
01: PB8
Other: Reserved
Note: The PA12_RMP bit of th e SYSCFG_CFGR1 takes priority over the selection through
this bitfield. Refer to the description of the SYSCFG_CFGR1 register for more details.

RM0490 Rev 6 201/1023
RM0490 System configurat ion controller (SYSCFG)
217
Bits 7:6 PINMUX3[1:0]: Pin GPIO multiplexer 3
This bitfield is set and cleared by software. It selects an active GPIO on a pin.
Condition: STM32C011x - GPIO assigned to SO8 pin 8
00: PA14
01: PB6
10: PC15
11: Reserved
Condition: STM32C051xx - GPIO assigned to WLCSP15 ball J2
00: PA5
01: PA6
Other: Reserved
Condition: STM32C071xx - GPIO assigned to WLCSP19 ball D3 or TSSOP20 pin 1
00: PB7
01: PB8
Other: Reserved
Condition: STM32C091/92xx - GPIO assigned WLCSP24 ball A3
00: PB5
01: PB3
Other: Reserved
Bits 5:4 PINMUX2[1:0]: Pin GPIO multiplexer 2
This bitfield is set and cleared by software. It selects an active GPIO on a pin.
Condition: STM32C011x - GPIO assigned to SO8 pin 5
00: PA8
01: PA11
Other: Reserved
Condition: STM32C051xx - GPIO assigned to WLCSP15 ball K3
00: PA3
01: PA4
Other: Reserved
Condition: STM32C071xx - GPIO assigned to TSSOP20 pin 20 or WLCSP19 pin B3
00: PB6
01: PB3
10: PB4
11: PB5
Condition: STM32C091/92xx - GPIO assigned to TSSOP20 pin 20
00: PB6
01: PB3
10: PB4
11: PB5
Condition: STM32C091/92xx - GPIO assigned to  WLCSP24 ball A5
00: PB6
01: PB4
Other: Reserved
Note: The PA11_RMP bit of the SYSCFG_CFGR1 takes priority over the selection through
this bitfield. Refer to the description of the SYSCFG_CFGR1 register for more details.

System configuration controller (SYSCFG) RM0490
202/1023 RM0490 Rev 6
9.1.4 SYSCFG interrupt line 0 st atus register (SYSCFG_ITLINE0)
A dedicated set of registers is implemented on the device to collect all pending interrupt
sources associated with each interrupt line into a single register. This allows users to check
by single read which peripheral requires service in case more than one source is associated
to the interrupt line.
All bits in those registers are read only, set by hardware when there is corresponding
Bits 3:2 PINMUX1[1:0]: Pin GPIO multiplexer 1
This bitfield is set and cleared by software. It selects an active GPIO on a pin.
Condition: STM32C011x - GPIO assigned to SO8 pin 4 or WLCSP12 ball F3
00: PF2-NRST
01: PA0
10: PA1
11: PA2
Condition: STM32C051xx - GPIO assigned to  WLCSP15 ball G2
00: PA1
01: PA2
Other: Reserved
Condition: STM32C071xx - GPIO assigned to WLCSP19 ball B1 or TSSOP20 pin 19
00: PA14
01: PA15
Other: Reserved
Condition: STM32C091/92xx - GPIO assigned to TSSOP20 pin 15
00: PA8
01: PB0
10: PB1
11: PB2
Condition: STM32C091/92xx - GPIO assigned to  WLCSP24 pin G1
00: PA8
01: PB2
Other: Reserved
Bits 1:0 PINMUX0[1:0]: Pin GPIO multiplexer 0
This bitfield is set and cleared by software. It selects an active GPIO on a pin.
Condition: STM32C011x - GPIO assigned to SO8 pin 1
00: PB7
01: PC14
Other: Reserved
Condition: STM32C051xx - GPIO assigned to WLCSP15 ball H3
00: PF2-NRST
01: PA0
Other: Reserved
Condition: STM32C071xx - GPIO assigned to WLCSP19 ball H3
00: PF2-NRST
01: PA0
Other: Reserved
Condition: STM32C091/92xx - GPIO assigned to TSSOP20 pin 19
00: PA14
01: PA15
Other: Reserved

RM0490 Rev 6 203/1023
RM0490 System configurat ion controller (SYSCFG)
217
interrupt request pending and cleared by resetting the interrupt source flags in the
peripheral registers.
Address offset: 0x80
Reset value: 0x0000 0000
9.1.5 SYSCFG interrupt line 1 st atus register (SYSCFG_ITLINE1)
This register is only available on STM32C071xx. On the other devices, it is reserved.
Address offset: 0x84
Reset value: 0x0000 0000
9.1.6 SYSCFG interrupt line 2 st atus register (SYSCFG_ITLINE2)
Address offset: 0x88
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. WWDG
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 WWDG: Window watchdog interrupt pending flag
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 98765432 1 0
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
PVM_
VDDIO2
_OUT
Res.
r
Bits 31:2 Reserved, must be kept at reset value.
Bit 1 PVM_VDDIO2_OUT: VDDIO2 supply monitoring interrupt request pending (EXTI line 34)
Bit 0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. RTC Res.
r

System configuration controller (SYSCFG) RM0490
204/1023 RM0490 Rev 6
9.1.7 SYSCFG interrupt line 3 st atus register (SYSCFG_ITLINE3)
Address offset: 0x8C
Reset value: 0x0000 0000
9.1.8 SYSCFG interrupt line 4 st atus register (SYSCFG_ITLINE4)
Address offset: 0x90
Reset value: 0x0000 0000
Bits 31:2 Reserved, must be kept at reset value.
Bit 1 RTC: RTC interrupt request pending (EXTI line 19)
Bit 0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
FLASH
_
ITF
Res.
r
Bits 31:2 Reserved, must be kept at reset value.
Bit 1 FLASH_ITF: Flash interface interrupt request pending
Bit 0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CRS RCC
rr
Bits 31:2 Reserved, must be kept at reset value.
Bit 1 CRS: CRS interrupt request pending
Note: Only applicable on STM32C071xx, reserved on other products.
Bit 0 RCC: Reset and clock control interrupt request pending

RM0490 Rev 6 205/1023
RM0490 System configurat ion controller (SYSCFG)
217
9.1.9 SYSCFG interrupt line 5 st atus register (SYSCFG_ITLINE5)
Address offset: 0x94
Reset value: 0x0000 0000
9.1.10 SYSCFG interrupt line 6 st atus register (SYSCFG_ITLINE6)
Address offset: 0x98
Reset value: 0x0000 0000
9.1.11 SYSCFG interrupt line 7 st atus register (SYSCFG_ITLINE7)
Address offset: 0x9C
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. EXTI1 EXTI0
rr
Bits 31:2 Reserved, must be kept at reset value.
Bit 1 EXTI1: EXTI line 1 interrupt request pending
Bit 0 EXTI0: EXTI line 0 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. EXTI3 EXTI2
rr
Bits 31:2 Reserved, must be kept at reset value.
Bit 1 EXTI3: EXTI line 3 interrupt request pending
Bit 0 EXTI2: EXTI line 2 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. EXTI15 EXTI14 EXTI13 EXTI12 EXTI11 EXTI10 EXTI9 EXTI8 EXTI7 EXTI6 EXTI5 EXTI4
rrrrrrrrrrrr

System configuration controller (SYSCFG) RM0490
206/1023 RM0490 Rev 6
9.1.12 SYSCFG interrupt line 8 st atus register (SYSCFG_ITLINE8)
This register is only available on STM32C071xx. On the other devices, it is reserved.
Address offset: 0xA0
Reset value: 0x0000 0000
9.1.13 SYSCFG interrupt line 9 st atus register (SYSCFG_ITLINE9)
Address offset: 0xA4
Reset value: 0x0000 0000
Bits 31:12 Reserved, must be kept at reset value.
Bit 11 EXTI15: EXTI line 15 interrupt request pending
Bit 10 EXTI14: EXTI line 14 interrupt request pending
Bit 9 EXTI13: EXTI line 13 interrupt request pending
Bit 8 EXTI12: EXTI line 12 interrupt request pending
Bit 7 EXTI11: EXTI line 11 interrupt request pending
Bit 6 EXTI10: EXTI line 10 interrupt request pending
Bit 5 EXTI9: EXTI line 9 interrupt request pending
Bit 4 EXTI8: EXTI line 8 interrupt request pending
Bit 3 EXTI7: EXTI line 7 interrupt request pending
Bit 2 EXTI6: EXTI line 6 interrupt request pending
Bit 1 EXTI5: EXTI line 5 interrupt request pending
Bit 0 EXTI4: EXTI line 4 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. USB
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 USB: USB interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. DMA1_CH1
r

RM0490 Rev 6 207/1023
RM0490 System configurat ion controller (SYSCFG)
217
9.1.14 SYSCFG interrupt line 10 st atus register (SYSCFG_ITLINE10)
Address offset: 0xA8
Reset value: 0x0000 0000
9.1.15 SYSCFG interrupt line 11 st atus register (SYSCFG_ITLINE11)
Address offset: 0xAC
Reset value: 0x0000 0000
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 DMA1_CH1: DMA1 channel 1interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. DMA1_CH3 DMA1_CH2
rr
Bits 31:2 Reserved, must be kept at reset value.
Bit 1 DMA1_CH3: DMA1 channel 3 interrupt request pending
Bit 0 DMA1_CH2: DMA1 channel 2 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. DMA_CH7 DMA_CH6 DMA_CH5 DMA_CH4 DMAMUX
rrrrr
Bits 31:5 Reserved, must be kept at reset value.
Bit 4 DMA_CH7: DMA channel 7 interrupt request pending
Note: Only applicable to STM32C091xx/92xx, reserved on the other products.
Bit 3 DMA_CH6: DMA channel 6 interrupt request pending
Note: Only applicable to STM32C091xx/92xx, reserved on the other products.
Bit 2 DMA_CH5: DMA channel 5 interrupt request pending
Note: Only applicable to STM32C051xx, STM32C071xx, and STM32C091xx/92xx, reserved
on the other products.
Bit 1 DMA_CH4: DMA channel 4 interrupt request pending
Note: Only applicable to STM32C051xx, STM32C071xx, and STM32C091xx/92xx, reserved
on the other products.
Bit 0 DMAMUX: DMAMUX interrupt request pending

System configuration controller (SYSCFG) RM0490
208/1023 RM0490 Rev 6
9.1.16 SYSCFG interrupt line 12 st atus register (SYSCFG_ITLINE12)
Address offset: 0xB0
Reset value: 0x0000 0000
9.1.17 SYSCFG interrupt line 13 st atus register (SYSCFG_ITLINE13)
Address offset: 0xB4
Reset value: 0x0000 0000
9.1.18 SYSCFG interrupt line 14 st atus register (SYSCFG_ITLINE14)
Address offset: 0xB8
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. ADC
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 ADC: ADC interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. TIM1_BRK TIM1_UPD TIM1_TRG TIM1_CCU
rrrr
Bits 31:4 Reserved, must be kept at reset value.
Bit 3 TIM1_BRK: Timer 1 break interrupt request pending
Bit 2 TIM1_UPD: Timer 1 update interrupt request pending
Bit 1 TIM1_TRG: Timer 1 trigger interrupt request pending
Bit 0 TIM1_CCU: Timer 1 commutation interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. TIM1_CC
r

RM0490 Rev 6 209/1023
RM0490 System configurat ion controller (SYSCFG)
217
9.1.19 SYSCFG interrupt line 15 st atus register (SYSCFG_ITLINE15)
This register is only available on STM32C051xx, STM32C071xx, and STM32C091xx/92xx.
On the other devices, it is reserved.
Address offset: 0xBC
Reset value: 0x0000 0000
9.1.20 SYSCFG interrupt line 16 st atus register (SYSCFG_ITLINE16)
Address offset: 0xC0
Reset value: 0x0000 0000
9.1.21 SYSCFG interrupt line 19 st atus register (SYSCFG_ITLINE19)
Address offset: 0xCC
Reset value: 0x0000 0000
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 TIM1_CC: Timer 1 capture compare interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. TIM2
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 TIM2: TIM2 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. TIM3
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 TIM3: Timer 3 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. TIM14
r

System configuration controller (SYSCFG) RM0490
210/1023 RM0490 Rev 6
9.1.22 SYSCFG interrupt line 20 st atus register (SYSCFG_ITLINE20)
This register is only available on STM32C091xx/92xx. On the other devices, it is reserved.
Address offset: 0xD0
Reset value: 0x0000 0000
9.1.23 SYSCFG interrupt line 21 st atus register (SYSCFG_ITLINE21)
Address offset: 0xD4
Reset value: 0x0000 0000
9.1.24 SYSCFG interrupt line 22 st atus register (SYSCFG_ITLINE22)
Address offset: 0xD8
Reset value: 0x0000 0000
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 TIM14: Timer 14 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. TIM15
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 TIM15: Timer 15 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. TIM16
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 TIM16: Timer 16 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. TIM17
r

RM0490 Rev 6 211/1023
RM0490 System configurat ion controller (SYSCFG)
217
9.1.25 SYSCFG interrupt line 23 st atus register (SYSCFG_ITLINE23)
Address offset: 0xDC
Reset value: 0x0000 0000
9.1.26 SYSCFG interrupt line 24 st atus register (SYSCFG_ITLINE24)
This register is only available on STM32C051xx, STM32C071xx, and STM32C091xx/92xx.
On the other devices, it is reserved.
Address offset: 0xE0
Reset value: 0x0000 0000
9.1.27 SYSCFG interrupt line 25 st atus register (SYSCFG_ITLINE25)
Address offset: 0xE4
Reset value: 0x0000 0000
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 TIM17: Timer 17 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. I2C1
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 I2C1: I2C1 interrupt request pending, combined with EXTI line 23
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. I2C2
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 I2C2: I2C2 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. SPI1
r

System configuration controller (SYSCFG) RM0490
212/1023 RM0490 Rev 6
9.1.28 SYSCFG interrupt line 26 st atus register (SYSCFG_ITLINE26)
This register is only available on STM32C051xx, STM32C071xx, and STM32C091xx/92xx.
On the other devices, it is reserved.
Address offset: 0xE8
Reset value: 0x0000 0000
9.1.29 SYSCFG interrupt line 27 st atus register (SYSCFG_ITLINE27)
Address offset: 0xEC
Reset value: 0x0000 0000
9.1.30 SYSCFG interrupt line 28 st atus register (SYSCFG_ITLINE28)
Address offset: 0xF0
Reset value: 0x0000 0000
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 SPI1: SPI1 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. SPI2
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 SPI2: SPI2 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. USART1
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 USART1: USART1 interrupt request pending, combined with EXTI line 25

RM0490 Rev 6 213/1023
RM0490 System configurat ion controller (SYSCFG)
217
9.1.31 SYSCFG interrupt line 29 st atus register (SYSCFG_ITLINE29)
This register is only available on STM32C091xx/92xx. On the other devices, it is reserved.
Address offset: 0xF4
Reset value: 0x0000 0000
9.1.32 SYSCFG interrupt line 30 st atus register (SYSCFG_ITLINE30)
This register is only available on STM32C092xx. On the other devices, it is reserved.
Address offset: 0xF8
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. USART2
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 USART2: USART2 interrupt request pending (EXTI line 26)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 98765432 1 0
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. USART4 USART3
rr
Bits 31:2 Reserved, must be kept at reset value.
Bit 1 USART4: USART4 interrupt request pending
Bit 0 USART3: USART3 interrupt request pending
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 987654321 0
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. FDCAN_IT0
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 FDCAN_IT0: FDCAN interrupt request 0 pending

System configuration controller (SYSCFG) RM0490
214/1023 RM0490 Rev 6
9.1.33 SYSCFG interrupt line 31 st atus register (SYSCFG_ITLINE31)
This register is only available on STM32C092xx. On the other devices, it is reserved.
Address offset: 0xFC
Reset value: 0x0000 0000
9.1.34 SYSCFG register map
The following table gives the SYSCFG register map and the reset values.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 987654321 0
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. FDCAN_IT1
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 FDCAN_IT1: FDCAN interrupt request 1 pending
[Table 41](../tables/table_41.md). SYSCFG register map and reset values
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
SYSCFG_CFGR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
I2C_PC14_FMP
I2C_PA10_FMP
I2C_PA9_FMP
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
Res.
Res.
IR_MOD
IR_POL
PA12_RMP
PA11_RMP
Res.
MEM_MODE[1:0]
R e s e t  v a l u e 000000000 00000 XX
0x04 to
0x17 Reserved Reserved
0x18
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
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
LOCUP_LOCK
Reset value 0
0x1C to
0x3B Reserved Reserved
0x3C
SYSCFG_CFGR3
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
PINMUX7
PINMUX6
PINMUX5
PINMUX4
PINMUX3
PINMUX2
PINMUX1
PINMUX0
R e s e t  v a l u e 0000000000000000
0x40 to
0x7F Reserved Reserved
0x80
SYSCFG_ITLINE0
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
Res.
WWDG
Reset value

RM0490 Rev 6 215/1023
RM0490 System configurat ion controller (SYSCFG)
217
0x84
SYSCFG_ITLINE1
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
PVM_VDDIO2_OUT
Res.
Reset value 0
0x88
SYSCFG_ITLINE2
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
RTC
Res.
Reset value 0
0x8C
SYSCFG_ITLINE3
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
FLASH_ITF
Res.
Reset value 0
0x90
SYSCFG_ITLINE4
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
CRS
RCC
Reset value 00
0x94
SYSCFG_ITLINE5
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
EXTI1
EXTI0
Reset value 00
0x98
SYSCFG_ITLINE6
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
EXTI3
EXTI2
Reset value 00
0x9C
SYSCFG_ITLINE7
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
EXTI15
EXTI14
EXTI13
EXTI12
EXTI11
EXTI10
EXTI9
EXTI8
EXTI7
EXTI6
EXTI5
EXTI4
Reset value 000000000000
0xA0
SYSCFG_ITLINE8
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
Res.
USB
Reset value 0
0xA4
SYSCFG_ITLINE9
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
Res.
DMA1_CH1
Reset value 0
0xA8
SYSCFG_ITLINE10
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
DMA1_CH3
DMA1_CH2
Reset value 00
0xAC
SYSCFG_ITLINE11
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
DMA1_CH7
DMA1_CH6
DMA1_CH5
DMA1_CH4
DMAMUX
Reset value 00000
0xB0
SYSCFG_ITLINE12
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
Res.
ADC
Reset value 0
0xB4
SYSCFG_ITLINE13
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
TIM1_BRK
TIM1_UPD
TIM1_TRG
TIM1_CCU
Reset value 0000
[Table 41](../tables/table_41.md). SYSCFG register map and reset values (continued)
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

System configuration controller (SYSCFG) RM0490
216/1023 RM0490 Rev 6
0xB8
SYSCFG_ITLINE14
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
Res.
TIM1_CC
Reset value 0
0xBC
SYSCFG_ITLINE15
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
Res.
TIM2
Reset value 0
0xC0
SYSCFG_ITLINE16
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
Res.
TIM3
Reset value 0
0xC4-
0xC8 Reserved Reserved
0xCC
SYSCFG_ITLINE19
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
Res.
TIM14
Reset value 0
0xD0
SYSCFG_ITLINE20
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
Res.
TIM15
Reset value 0
0xD4
SYSCFG_ITLINE21
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
Res.
TIM16
Reset value 0
0xD8
SYSCFG_ITLINE22
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
Res.
TIM17
Reset value 0
0xDC
SYSCFG_ITLINE23
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
Res.
I2C1
Reset value 0
0xE0
SYSCFG_ITLINE24
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
Res.
I2C2
Reset value 0
0xE4
SYSCFG_ITLINE25
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
Res.
SPI1
Reset value 0
0xE8
SYSCFG_ITLINE26
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
Res.
SPI2
Reset value 0
0xEC
SYSCFG_ITLINE27
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
Res.
USART1
Reset value 0
0xF0
SYSCFG_ITLINE28
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
Res.
USART2
Reset value 0
0xF4
SYSCFG_ITLINE29
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
USART4
USART3
Reset value 00
0xF8
SYSCFG_ITLINE30
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
Res.
FDCAN_IT0
Reset value 0
[Table 41](../tables/table_41.md). SYSCFG register map and reset values (continued)
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

RM0490 Rev 6 217/1023
RM0490 System configurat ion controller (SYSCFG)
217
Refer to Section 2.2 on page 45 for the register boundary addresses.
0xFC
SYSCFG_ITLINE31
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
Res.
FDCAN_IT1
Reset value 0
[Table 41](../tables/table_41.md). SYSCFG register map and reset values (continued)
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
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* [Table 41: Configuration Matrix](../tables/table_41.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)