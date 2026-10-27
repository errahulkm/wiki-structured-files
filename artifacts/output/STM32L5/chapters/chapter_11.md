# Chapter 11: General-purpose I/Os (GPIO)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 11: General-purpose I/Os (GPIO).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 435 - 455
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs)](../peripherals/gpio.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 435/2187
RM0438 General-purpose I/Os (GPIO)
455
11 General-purpose I/Os (GPIO)
11.1 Introduction
Each general-purpose I/O port has four 32-bit configuration registers (GPIOx_MODER,
GPIOx_OTYPER, GPIOx_OSPEEDR and GPIOx_PUPDR), two 32-bit data registers
(GPIOx_IDR and GPIOx_ODR) and a 32-bit set/reset register (GPIOx_BSRR). In addition
all GPIOs have a 32-bit locking register (GPIOx_LCKR) and two 32-bit alternate function
selection registers (GPIOx_AFRH and GPIOx_AFRL) and a secure configuration register
(GPIOx_SECCFGR).
11.2 GPIO main features
• Output states: push-pull or open drain + pull-up/down
• Output data from output data register (GPIOx_ODR) or peripheral (alternate function
output)
• Speed selection for each I/O
• Input states: floating, pull-up/down, analog
• Input data to input data register (GPIOx_IDR) or peripheral (alternate function input)
• Bit set and reset register (GPIOx_ BSRR) for bitwise write access to GPIOx_ODR
• Locking mechanism (GPIOx_LCKR) provided to freeze the I/O port configurations
• Analog function
• Alternate function selection registers
• Fast toggle capable of changing every two clock cycles
• Highly flexible pin multiplexing allows the use of I/O pins as GPIOs or as one of several
peripheral functions
• TrustZone security support
11.3 GPIO functional description
Subject to the specific hardware characteristics of each I/O port listed in the datasheet, each
port bit of the general-purpose I/O (GPIO) ports can be individually configured by software in
several modes:
• Input floating
• Input pull-up
• Input-pull-down
• Analog
• Output open-drain with pull-up or pull-down capability
• Output push-pull with pull-up or pull-down capability
• Alternate function push-pull with pull-up or pull-down capability
• Alternate function open-drain with pull-up or pull-down capability
Each I/O port bit is freely programmable, however the I/O port registers have to be
accessed as 32-bit words, half-words or bytes. The purpose of the GPIOx_BSRR register is

General-purpose I/Os (GPIO) RM0438
436/2187 RM0438 Rev 8
to allow atomic read/modify accesses to any of the GPIOx_ODR registers. In this way, there
is no risk of an IRQ occurring between the read and the modify access.
[Figure 37](../figures/figure_37.md) and [Figure 38](../figures/figure_38.md) show the basic structures of a standard and a 5-Volt tolerant I/O
port bit, respectively. [Table 89](../tables/table_89.md) gives the possible port bit configurations.
[Figure 37](../figures/figure_37.md). Basic structure of an I/O port bit
[Figure 38](../figures/figure_38.md). Basic structure of a 5-Volt tolerant I/O port bit
1. V DD_FT is a potential specific to five-volt tolerant I/Os and different from VDD.
Alternate function output
Alternate function input
Push-pull,
open-drain or
disabled
Input data register
Output data register
Read/write
From on-chip
peripheral
To on-chip
peripheral
Output
control
Analog
on/off Pull
Pull
down
on/off
I/O pin
VDDIOx
VDDIOx
VSS
VSS
trigger
VSS
VDDIOx
Protection
diode
Protection
diode
on/off
Input driver
Output driver
up
P-MOS
N-MOS
Read
Bit set/reset registers
Write
Analog
MS31476V1
Alternate function output
Alternate function input
Push-pull,
open-drain or
disabled
Output data registerRead/write
From on-chip
peripheral
To on-chip
peripheral
Output
control
on/off
Pull
Pullon/off
I/O pin
VDDIOx
VDDIOx
VSS
VSS
TTL Schmitt
trigger
VSS
VDD_FT
(1)
Protection
diode
Protection
diode
on/off
Input driver
Output driver
down
up
P-MOS
N-MOS
Read
Bit set/reset registers
Write
Input data register
ai15939d

RM0438 Rev 8 437/2187
RM0438 General-purpose I/Os (GPIO)
455
[Table 89](../tables/table_89.md). Port bit configuration table(1)
1. GP = general-purpose, PP = push- pull, PU = pull-up, PD = pull-down, OD = open-drain, AF = alternate
function.
MODE(i)
[1:0] OTYPER(i) OSPEED(i)
[1:0]
PUPD(i)
[1:0] I/O configuration
01
0
SPEED
[1:0]
0 0 GP output PP
0 0 1 GP output PP + PU
0 1 0 GP output PP + PD
0 1 1 Reserved
1 0 0 GP output OD
1 0 1 GP output OD + PU
1 1 0 GP output OD + PD
1 1 1 Reserved (GP output OD)
10
0
SPEED
[1:0]
0 0 AF PP
00 1 A F P P  +  P U
01 0 A F P P  +  P D
0 1 1 Reserved
10 0 A F O D
10 1 A F O D  +  P U
11 0 A F O D  +  P D
1 1 1 Reserved
00
x x x 0 0 Input Floating
x x x 0 1 Input PU
x x x 1 0 Input PD
x x x 1 1 Reserved (input floating)
11
x x x 0 0 Input/output Analog
xx x 0 1
Reservedxx x 1 0
xx x 1 1

General-purpose I/Os (GPIO) RM0438
438/2187 RM0438 Rev 8
11.3.1 General-purpose I/O (GPIO)
During and just after reset, the alternate functions are not active and most of the I/O ports
are configured in analog mode.
The debug pins are in AF pull-up/pull-down after reset:
• PA15: JTDI in pull-up
• PA14: JTCK/SWCLK in  pull-down
• PA13: JTMS/SWDAT in pull-up
• PB4: NJTRST in pull-up
• PB3: JTDO in floating state no pull-up/pull-down
PH3/BOOT0 is in input mode during the reset until at least the end of the option byte loading
phase. See Section 11.3.15: Using PH3 as GPIO.
When the pin is configured as output, the value written to the output data register
(GPIOx_ODR) is output on the I/O pin. It is possible to use the output driver in push-pull
mode or open-drain mode (only the low level is driven, high level is HI-Z).
The input data register (GPIOx_IDR) captures the data present on the I/O pin at every AHB
clock cycle.
All GPIO pins have weak internal pull-up and pull-down resistors, which can be activated or
not depending on the value in the GPIOx_PUPDR register.
11.3.2 I/O pin alternate func tion multiplexer and mapping
The device I/O pins are connected to on-board peripherals/modules through a multiplexer
that allows only one peripheral alternate function (AF) connected to an I/O pin at a time. In
this way, there can be no conflict between peripherals available on the same I/O pin.
Each I/O pin has a multiplexer with up to sixteen alternate function inputs (AF0 to AF15) that
can be configured through the GPIOx_AFRL (for pin 0 to 7) and GPIOx_AFRH (for pin 8 to
15) registers:
• After reset the multiplexer selection is alternate function 0 (AF0). The I/Os are
configured in alternate function mode through GPIOx_MODER register.
• The specific alternate function assignments for each pin are detailed in the device
datasheet.
In addition to this flexible I/O multiplexing architecture, each peripheral has alternate
functions mapped onto different I/O pins to optimize the number of peripherals available in
smaller packages.
To use an I/O in a given configuration, the user has to proceed as follows:
• Debug function: after each device reset these pins are assigned as alternate function
pins immediately usable by the debugger host
• GPIO: configure the desired I/O as output, input or analog in the GPIOx_MODER
register.
• Alternate function:
– Connect the I/O to the desired AFx in  one of the GPIOx_AFRL or GPIOx_AFRH
register.
– Select the type, pull-up/pull-down and  output speed via the GPIOx_OTYPER,
GPIOx_PUPDR and GPIOx_OSPEEDER registers, respectively.

RM0438 Rev 8 439/2187
RM0438 General-purpose I/Os (GPIO)
455
– Configure the desired I/O as an alternat e function in the GPIOx_MODER register.
– The Cortex ®-M33 output EVENTOUT signal can be output as alternate function
on several I/Os. An event can be signaled through the configured pin after
executing SEV instruction.
• Additional functions:
– For the ADC, DAC and COMP, configure the desired I/O in analog mode in the
GPIOx_MODER register and configure the required function in the ADC, DAC,
OPAMP and COMP registers.
As indicated above, for the additional functions (such as DAC or OPAMP), the
output is controlled by the corresponding peripheral. Care must be taken to select
the I/O port analog function before enabling the additional function output in the
peripheral control register.
– For the additional functions like RTC,  WKUPx and oscillators, configure the
required function in the related RTC, PWR and RCC registers. These functions
have priority over the configuration in the standard GPIO registers.
Refer to the “Alternate function mapping” table in the device datasheet for the detailed
mapping of the alternate function I/O pins.
11.3.3 I/O port control registers
Each of the GPIO ports has four 32-bit memory-mapped control registers (GPIOx_MODER,
GPIOx_OTYPER, GPIOx_OSPEEDR, GPIOx_PUPDR) to configure up to 16 I/Os. The
GPIOx_MODER register is used to select the I/O mode (input, output, AF, analog). The
GPIOx_OTYPER and GPIOx_OSPEEDR registers are used to select the output type (push-
pull or open-drain) and speed. The GPIOx_PUPDR register is used to select the pull-
up/pull-down whatever the I/O direction.
11.3.4 I/O port data registers
Each GPIO has two 16-bit memory-mapped data registers: input and output data registers
(GPIOx_IDR and GPIOx_ODR). GPIOx_ODR stores the data to be output, it is read/write
accessible. The data input through the I/O are stored into the input data register
(GPIOx_IDR), a read-only register.
See Section 11.6.5: GPIO port input data register (GPIOx_IDR) (x = A to H) and
Section 11.6.6: GPIO port output data register (GPIOx_ODR) (x = A to H) for the register
descriptions.
11.3.5 I/O data bitwise handling
The bit set reset register (GPIOx_BSRR) is a 32-bit register which allows the application to
set and reset each individual bit in the output data register (GPIOx_ODR). The bit set reset
register has twice the size of GPIOx_ODR.
To each bit in GPIOx_ODR, correspond two control bits in GPIOx_BSRR: BS(i) and BR(i).
When written to 1, bit BS(i) sets the corresponding ODR(i) bit. When written to 1, bit BR(i)
resets the ODR(i) corresponding bit.
Writing any bit to 0 in GPIOx_BSRR does not have any effect on the corresponding bit in
GPIOx_ODR. If there is an attempt to both set and reset a bit in GPIOx_BSRR, the set
action takes priority.

General-purpose I/Os (GPIO) RM0438
440/2187 RM0438 Rev 8
Using the GPIOx_BSRR register to change the values of individual bits in GPIOx_ODR is a
“one-shot” effect that does not lock the GPIOx_ODR bits. The GPIOx_ODR bits can always
be accessed directly. The GPIOx_BSRR register provides a way of performing atomic
bitwise handling.
There is no need for the software to disable interrupts when programming the GPIOx_ODR
at bit level: it is possible to modify one or more bits in a single atomic AHB write access.
11.3.6 GPIO locking mechanism
It is possible to freeze the GPIO control registers by applying a specific write sequence to
the GPIOx_LCKR register. The frozen registers are GPIOx_MODER, GPIOx_OTYPER,
GPIOx_OSPEEDR, GPIOx_PUPDR, GPIOx_AFRL and GPIOx_AFRH.
To write the GPIOx_LCKR register, a specific write / read sequence has to be applied. When
the right LOCK sequence is applied to bit 16 in this register, the value of LCKR[15:0] is used
to lock the configuration of the I/Os (during the write sequence the LCKR[15:0] value must
be the same). When the LOCK sequence has been applied to a port bit, the value of the port
bit can no longer be modified until the next MCU reset or peripheral reset. Each
GPIOx_LCKR bit freezes the corresponding bit in the control registers (GPIOx_MODER,
GPIOx_OTYPER, GPIOx_OSPEEDR, GPIOx_PUPDR, GPIOx_AFRL and GPIOx_AFRH.
The LOCK sequence (refer to Section 11.6.8: GPIO port configuration lock register
(GPIOx_LCKR) (x = A to H)) can only be performed using a word (32-bit long) access to the
GPIOx_LCKR register due to the fact that GPIOx_LCKR bit 16 has to be set at the same
time as the [15:0] bits.
For more details refer to LCKR register description in Section 11.6.8: GPIO port
configuration lock register (GPIOx_LCKR) (x = A to H).
11.3.7 I/O alternate function input/output
Two registers are provided to select one of the alternate function inputs/outputs available for
each I/O. With these registers, the user can connect an alternate function to some other pin
as required by the application.
This means that a number of possible peripheral functions are multiplexed on each GPIO
using the GPIOx_AFRL and GPIOx_AFRH alternate function registers. The application can
thus select any one of the possible functions for each I/O. The AF selection signal being
common to the alternate function input and alternate function output, a single channel is
selected for the alternate function input/output of a given I/O.
To know which functions are multiplexed on each GPIO pin, refer to the device datasheet.
11.3.8 External interrupt/wakeup lines
All ports have external interrupt capability. To use external interrupt lines, the port can be
configured in input, output or alternate function mode (the port must not be configured in
analog mode).
Refer to Section 17: Extended interrupts and event controller (EXTI).

RM0438 Rev 8 441/2187
RM0438 General-purpose I/Os (GPIO)
455
11.3.9 Input configuration
When the I/O port is programmed as input:
• The output buffer is disabled
• The Schmitt trigger input is activated
• The pull-up and pull-down resistors are activated depending on the value in the
GPIOx_PUPDR register
• The data present on the I/O pin are sampled into the input data register every AHB
clock cycle
• A read access to the input data register provides the I/O state
[Figure 39](../figures/figure_39.md) shows the input configuration of the I/O port bit.
[Figure 39](../figures/figure_39.md). Input floating/pull up/pull down configurations
11.3.10 Output configuration
When the I/O port is programmed as output:
• The output buffer is enabled:
– Open drain mode: A “0” in the Output register activates the N-MOS whereas a “1”
in the Output register leaves the port in Hi-Z (the P-MOS is never activated)
– Push-pull mode: A “0” in the Output register activates the N-MOS whereas a “1” in
the Output register activates the P-MOS
• The Schmitt trigger input is activated
• The pull-up and pull-down resistors are activated depending on the value in the
GPIOx_PUPDR register
• The data present on the I/O pin are sampled into the input data register every AHB
clock cycle
• A read access to the input data register gets the I/O state
• A read access to the output data register gets the last written value
[Figure 40](../figures/figure_40.md) shows the output configuration of the I/O port bit.
on/off
pull
pull
on/off
I/O pin
VDDIOx
VSS
TTL Schmitt
trigger
VSS
VDDIOx
protection
diode
protection
diode
on
input driver
output driver
down
up
Input data register
Output data registerRead/write
Read
Bit set/reset registers
Write
MS31477V1

General-purpose I/Os (GPIO) RM0438
442/2187 RM0438 Rev 8
[Figure 40](../figures/figure_40.md). Output configuration
11.3.11 Alternate function configuration
When the I/O port is programmed as alternate function:
• The output buffer can be configured in open-drain or push-pull mode
• The output buffer is driven by the signals coming from the peripheral (transmitter
enable and data)
• The Schmitt trigger input is activated
• The weak pull-up and pull-down resistors are activated or not depending on the value
in the GPIOx_PUPDR register
• The data present on the I/O pin are sampled into the input data register every AHB
clock cycle
• A read access to the input data register gets the I/O state
[Figure 41](../figures/figure_41.md) shows the Alternate function configuration of the I/O port bit.
[Figure 41](../figures/figure_41.md). Alternate function configuration
Push-pull or
Open-drain
Output
control
VDDIOx
VSS
TTL Schmitt
trigger
on
Input driver
Output driver
P-MOS
N-MOS
Input data register
Output data registerRead/write
Read
Bit set/reset registers
Write
on/off
pull
pull
on/off
VDDIOx
VSS VSS
VDDIOx
protection
diode
protection
diodedown
up
I/O pin
MS31478V1
MSv34756V1
Alternate function output
Alternate function input
push-pull or
open-drainFrom on-chip
peripheral
To on-chip
peripheral
Output
control
VDD
VSS
TTL Schmitt
trigger
on
Input driver
Output driver
P-MOS
N-MOS
Input data register
Output data registerRead/write
Read
Bit set/reset registers
Write
on/off
on/off
VDDIOx
VSS VSS
protection
diode
protection
diode
Pull
Pull
I/O pin
down
up
VDDIOx

RM0438 Rev 8 443/2187
RM0438 General-purpose I/Os (GPIO)
455
11.3.12 Analog configuration
When the I/O port is programmed as analog configuration:
• The output buffer is disabled
• The Schmitt trigger input is deactivated, providing zero consumption for every analog
value of the I/O pin. The output of the Schmitt trigger is forced to a constant value (0).
• The weak pull-up and pull-down resistors are disabled by hardware
• Read access to the input data register gets the value “0”
[Figure 42](../figures/figure_42.md) shows the high-impedance, analog-input configuration of the I/O port bits.
[Figure 42](../figures/figure_42.md). High impedance-analog configuration
11.3.13 Using the HSE or LS E oscillator pins as GPIOs
When the HSE or LSE oscillator is switched OFF (default state after reset), the related
oscillator pins can be used as normal GPIOs.
When the HSE or LSE oscillator is switched ON (by setting the HSEON or LSEON bit in the
RCC_CSR register) the oscillator takes control of its associated pins and the GPIO
configuration of these pins has no effect.
When the oscillator is configured in a user external clock mode, only the  pin is reserved for
clock input and the OSC_OUT or OSC32_OUT pin can still be used as normal GPIO.
11.3.14 Using the GPIO pins  in the RTC supply domain
The PC13/PC14/PC15 GPIO functionality is lost when the core supply domain is powered
off (when the device enters Standby mode). In this case, if their GPIO configuration is not
bypassed by the RTC configuration, these pins are set in an analog input mode.
For details about I/O control by the RTC, refer to Section 41.3: RTC functional description.
From on-chip
peripheral
To on-chip
peripheral
Analog
trigger
off
Input driver
0
Input data register
Output data registerRead/write
Read
Bit set/reset registers
Write
Analog
VSS
VDDIOx
protection
diode
protection
diode
I/O pin
MS31480V1
TTL Schmitt

General-purpose I/Os (GPIO) RM0438
444/2187 RM0438 Rev 8
11.3.15 Using PH3 as GPIO
PH3 may be used as boot pin (BOOT0) or as a GPIO. Depending on the nSWBOOT0 bit in
the user option byte, it switches from the input mode to the analog input mode:
• After the option byte loading phase if nSWBOOT0 = 1.
• After reset if nSWBOOT0 = 0.
11.4 TrustZone security
The TrustZone security is activated by the TZEN option bit in the FLASH_OPTR. When the
TrustZone is active (TZEN=1), each I/O pin of GPIO port can be individually configured as
secure through the GPIOx_SECCFGR register.
When the selected I/O pin is configured as secure, its corresponding configuration bits for
alternate function, mode selection, I/O data are secure against a non-secure access. In
case of non-secure access, these bits are RAZ/WI.
The I/Os with peripherals functions are also conditioned by the peripheral security
configuration:
• For peripherals for which the I/O pin selection is done through alternate functions
registers: if the peripheral is configured as secure, it cannot be connected to a non-
secure I/O pin. If this is not respected, the input data to the secure peripheral is forced
to '0' (I/O input pin value is ignored) and the output pin value is forced to '0', thus
avoiding any secure information leak through non-secure I/Os.
• For I/Os with analog switches, directly controlled by peripherals (such as ADC for
instance): If the I/O is secure, the I/O analog switch cannot be controlled by a non-
secure peripheral. If this is not respected, the switch would remain open. This prevent
the redirection of secure data to a non-secure peripheral or I/O through analog path.
• Some of the paths between I/Os additional functions mainly and peripherals are not
blocked if the I/O is secure and the peripheral is non-secure. Therefore it is
recommended to configure those peripherals as secure even when not used by the
application. When the path has a security control, it follows the same rule as I/O
selection through alternate functions.
• Refer to the device pins definition table in datasheet for more information about
peripherals alternate functions and additional functions mapping.
After reset, all GPIO ports are secure.
[Table 90](../tables/table_90.md) gives a summary of the I/O port secured bits following the security configuration bit
in the GPIO_SECCFGR register. When the I/O bit port is configured as secure:
• Secured bits: read and write operations are only allowed by a secure access. Non-
secure read or write accesses on secured bits are RAZ/WI. There is no illegal access
event generated.
• Non-secure bits: no restriction. Read and write operations are allowed by both secure
and non-secure accesses.
When the TrustZone security is disabled (TZEN = 0 in FLASH_OPTR register), all registers
bits are non-secure. The GPIOx_SECCFGR register is RAZ/WI.

RM0438 Rev 8 445/2187
RM0438 General-purpose I/Os (GPIO)
455
Note: GPIOx, x= A..H , and y=0..15
11.5 Privileged and Unprivileged modes
All GPIO registers can be read and written by privileged and unprivileged accesses,
whatever the security state (secure or non-secure).
[Table 90](../tables/table_90.md). GPIO secured bits
Secure configuration bit Secured bit Register name
Non-secure
access on secure
bits
SECy = 1 in GPIOx_SECCFGR
MODEy[1:0] GPIOx_MODER
RAZ/WI
OTy GPIOx_OTYPER
OSPEEDy[1:0] GPIOx_OSPEEDR
PUPDy[1:0] GPIOx_PUPDR
IDy GPIOx_IDR
ODy GPIOx_ODR
BSy GPIOx_BSRR
LCKy GPIOx_LCKR
AFSELy[3:0] GPIOx_AFRL
BRy
GPIOx_AFRH
GPIOx_BRR

General-purpose I/Os (GPIO) RM0438
446/2187 RM0438 Rev 8
11.6 GPIO registers
This section gives a detailed description of the GPIO registers.
For a summary of register bits, register address offsets and reset values, refer to [Table 91](../tables/table_91.md).
The peripheral registers can be written in word, half word or byte mode.
11.6.1 GPIO port mode register (GPIOx_MODER)
(x =A to H)
Address offset:0x00
Reset value: 0xABFF FFFF (for port A)
Reset value: 0xFFFF FEBF (for port B)
Reset value: 0xFFFF FFFF (for ports C..G)
Reset value: 0x0000 000F (for port H)
11.6.2 GPIO port output ty pe register (GPIOx_OTYPER)
(x = A to H)
Address offset: 0x04
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
MODE15[1:0] MODE14[1:0] MODE13[1:0] MODE12[1:0] MODE11[1:0] MODE10[1:0] MODE9[1:0] MODE8[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
MODE7[1:0] MODE6[1:0] MODE5[1:0] MODE4[1:0] MODE3[1:0] MODE2[1:0] MODE1[1:0] MODE0[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 MODE[15:0][1:0]: Port x configuration I/O pin y (y = 15 to 0)
These bits are written by software to configure the I/O mode.
00: Input mode
01: General purpose output mode
10: Alternate function mode
11: Analog mode (reset state)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
OT15 OT14 OT13 OT12 OT11 OT10 OT9 OT8 OT7 OT6 OT5 OT4 OT3 OT2 OT1 OT0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 447/2187
RM0438 General-purpose I/Os (GPIO)
455
11.6.3 GPIO port output sp eed register (GPIOx_OSPEEDR)
(x = A to H)
Address offset: 0x08
Reset value: 0x0C00 0000 (for port A)
Reset value: 0x0000 0000 (for the other ports)
11.6.4 GPIO port pull-up/pull -down register (GPIOx_PUPDR)
(x = A to H)
Address offset: 0x0C
Reset value: 0x6400 0000 (for port A)
Reset value: 0x0000 0100 (for port B)
Reset value: 0x0000 0000 (for other ports)
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 OT[15:0]: Port x configuration I/O pin y (y = 15 to 0)
These bits are written by software to configure the I/O output type.
0: Output push-pull (reset state)
1: Output open-drain
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
OSPEED15
[1:0]
OSPEED14
[1:0]
OSPEED13
[1:0]
OSPEED12
[1:0]
OSPEED11
[1:0]
OSPEED10
[1:0]
OSPEED9
[1:0]
OSPEED8
[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
OSPEED7
[1:0]
OSPEED6
[1:0]
OSPEED5
[1:0]
OSPEED4
[1:0]
OSPEED3
[1:0]
OSPEED2
[1:0]
OSPEED1
[1:0]
OSPEED0
[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 OSPEED[15:0][1:0]: Port x configuration I/O pin y (y = 15 to 0)
These bits are written by software to configure the I/O output speed.
00: Low speed
01: Medium speed
10: High speed(1)
11: Very high speed(1)
Note: Refer to the device datasheet for the frequency specifications and the power supply
and load conditions for each speed..
1. Not available for FT_c IOs.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
PUPD15[1:0] PUPD14[1:0] PUPD13[1:0] PUPD12[1:0 ] PUPD11[1:0] PUPD10[1:0] PUPD9[1:0] PUPD8[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PUPD7[1:0] PUPD6[1:0] PUPD5[1:0] PUPD4[1:0] PUPD3[1:0] PUPD2[1:0] PUPD1[1:0] PUPD0[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

General-purpose I/Os (GPIO) RM0438
448/2187 RM0438 Rev 8
11.6.5 GPIO port  input data register (GPIOx_IDR)
(x = A to H)
Address offset: 0x10
Reset value: 0x0000 XXXX
11.6.6 GPIO port output data register (GPIOx_ODR)
(x = A to H)
Address offset: 0x14
Reset value: 0x0000 0000
11.6.7 GPIO port bit set/ reset register (GPIOx_BSRR)
(x = A to H)
Address offset: 0x18
Bits 31:0 PUPD[15:0][1:0]: Port x configuration I/O pin y (y = 15 to 0)
These bits are written by software to configure the I/O pull-up or pull-down
00: No pull-up, pull-down
01: Pull-up
10: Pull-down
11: Reserved
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ID15 ID14 ID13 ID12 ID11 ID10 ID9 ID8 ID7 ID6 ID5 ID4 ID3 ID2 ID1 ID0
rrrrrrr r r r rrrrrr
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 ID[15:0]: Port x input data I/O pin y (y = 15 to 0)
These bits are read-only. They contain the input value of the corresponding I/O port.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
OD15 OD14 OD13 OD12 OD11 OD10 OD9 OD8 OD7 OD6 OD5 OD4 OD3 OD2 OD1 OD0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 OD[15:0]: Port output data I/O pin y (y = 15 to 0)
These bits can be read and written by software.
Note: For atomic bit set/reset, the OD bits can be  individually set and/or reset by writing to the
GPIOx_BSRR register (x = A to H).

RM0438 Rev 8 449/2187
RM0438 General-purpose I/Os (GPIO)
455
Reset value: 0x0000 0000
11.6.8 GPIO port configurat ion lock register (GPIOx_LCKR)
(x = A to H)
This register is used to lock the configuration of the port bits when a correct write sequence
is applied to bit 16 (LCKK). The value of bits [15:0] is used to lock the configuration of the
GPIO. During the write sequence, the value of LCKR[15:0] must not change. When the
LOCK sequence has been applied on a port bit, the value of this port bit can no longer be
modified until the next MCU reset or peripheral reset.
Note: A specific write se quence is used to write to the GPIOx_LCKR register. Only word access
(32-bit long) is allowed during this locking sequence.
Each lock bit freezes a specific configuration register (control and alternate function
registers).
Address offset: 0x1C
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
BR15 BR14 BR13 BR12 BR11 BR10 BR9 BR8 BR7 BR6 BR5 BR4 BR3 BR2 BR1 BR0
wwwwwwwww w w w w www
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
BS15 BS14 BS13 BS12 BS11 BS10 BS9 BS8 BS7 BS6 BS5 BS4 BS3 BS2 BS1 BS0
wwwwwwwww w w w w www
Bits 31:16 BR[15:0]: Port x reset I/O pin y (y = 15 to 0)
These bits are write-only. A read to these bits returns the value 0x0000.
0: No action on the corresponding ODx bit
1: Resets the corresponding ODx bit
Note: If both BSx and BRx are set, BSx has priority.
Bits 15:0 BS[15:0]: Port x set I/O pin y (y = 15 to 0)
These bits are write-only. A read to these bits returns the value 0x0000.
0: No action on the corresponding ODx bit
1: Sets the corresponding ODx bit
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. LCKK
rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
LCK15 LCK14 LCK13 LCK12 LCK11 LCK10 LCK9 LC K8 LCK7 LCK6 LCK5 LCK4 LCK3 LCK2 LCK1 LCK0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

General-purpose I/Os (GPIO) RM0438
450/2187 RM0438 Rev 8
11.6.9 GPIO alternate functi on low register (GPIOx_AFRL)
(x = A to H)
Address offset: 0x20
Reset value: 0x0000 0000
Bits 31:17 Reserved, must be kept at reset value.
Bit 16 LCKK: Lock key
This bit can be read any time. It can only be modified using the lock key write sequence.
0: Port configuration lock key not active
1: Port configuration lock key active. The GPIOx_LCKR register is locked until the next MCU
reset or peripheral reset.
LOCK key write sequence:
WR LCKR[16] = ‘1’ + LCKR[15:0]
WR LCKR[16] = ‘0’ + LCKR[15:0]
WR LCKR[16] = ‘1’ + LCKR[15:0]
RD LCKR
RD LCKR[16] = ‘1’ (this read operation is optional but it confirms that the lock is active)
Note: During the LOCK key write sequence, the value of LCK[15:0] must not change.
Any error in the lock sequence aborts the lock.
After the first lock sequence on any bit of the port, any read access on the LCKK bit
returns ‘1’ until the next MCU reset or peripheral reset.
Bits 15:0 LCK[15:0]: Port x lock I/O pin y (y = 15 to 0)
These bits are read/write but can only be written when the LCKK bit is ‘0.
0: Port configuration not locked
1: Port configuration locked
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
AFSEL7[3:0] AFSEL6[3:0] AFSEL5[3:0] AFSEL4[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
AFSEL3[3:0] AFSEL2[3:0] AFSEL1[3:0] AFSEL0[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 451/2187
RM0438 General-purpose I/Os (GPIO)
455
11.6.10 GPIO alternate functi on high register (GPIOx_AFRH)
(x = A to H)
Address offset: 0x24
Reset value: 0x0000 0000
Bits 31:0 AFSEL[7:0][3:0]: Alternate function selection for port x I/O pin y (y = 7 to 0)
These bits are written by software to configure alternate function I/Os.
0000: AF0
0001: AF1
0010: AF2
0011: AF3
0100: AF4
0101: AF5
0110: AF6
0111: AF7
1000: AF8
1001: AF9
1010: AF10
1011: AF11
1100: AF12
1101: AF13
1110: AF14
1111: AF15
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
AFSEL15[3:0] AFSEL14[3:0] AFSEL13[3:0] AFSEL12[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
AFSEL11[3:0] AFSEL10[3:0] AFSEL9[3:0] AFSEL8[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

General-purpose I/Os (GPIO) RM0438
452/2187 RM0438 Rev 8
11.6.11 GPIO port bi t reset register (GPIOx_BRR) (x = A to H)
Address offset: 0x28
Reset value: 0x0000 0000
11.6.12 GPIO secure conf iguration register (GPIOx_SECCFGR) (x = A to H)
When the system is secure (TZEN = 1), this register provides write access security and can
be written only by a secure access. It is used to configure a selected I/O as secure. A non-
secure write access to this register is discarded. A non-secure read is possible, and thus
provides visibility on secured I/O pins on the GPIO port.
When the system is not secure (TZEN = 0), this register is WI and its content has no effect.
Address offset: 0x30
Reset value: 0x0000 FFFF (A to G) and 0x0000 000B (H)
Bits 31:0 AFSEL[15:8][3:0]: Alternate function selection for port x I/O pin y (y = 15 to 8)
These bits are written by software to configure alternate function I/Os.
0000: AF0
0001: AF1
0010: AF2
0011: AF3
0100: AF4
0101: AF5
0110: AF6
0111: AF7
1000: AF8
1001: AF9
1010: AF10
1011: AF11
1100: AF12
1101: AF13
1110: AF14
1111: AF15
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
BR15 BR14 BR13 BR12 BR11 BR10 BR9 BR8 BR7 BR6 BR5 BR4 BR3 BR2 BR1 BR0
wwwwwwwww w w w w www
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 BR[15:0]: Port x reset IO pin y (y = 15 to 0)
These bits are write-only. A read to these bits returns the value 0x0000.
0: No action on the corresponding ODx bit
1: Reset the corresponding ODx bit

RM0438 Rev 8 453/2187
RM0438 General-purpose I/Os (GPIO)
455
Note: Bits are “rw” when TZEN = 1.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
SEC15 SEC14 SEC13 SEC12 SEC11 SEC10 SEC9 SEC8 SEC7 SEC6 SEC5 SEC4 SEC3 SEC2 SEC1 SEC0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved
Bits 15:0 SEC[15:0]: I/O pin of Port x secure bit enable y (y= 0..15)
These bits are written by software to enable the security I/O port pin.
0: The I/O pin is non-secure
1: The I/O pin is secure. Refer to [Table 90](../tables/table_90.md) for all corresponding secured bits.

General-purpose I/Os (GPIO) RM0438
454/2187 RM0438 Rev 8
11.6.13 GPIO register map
The following table gives the GPIO register map and reset values.
[Table 91](../tables/table_91.md). GPIO register map and reset values
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
0x00
GPIOx_MODER
(where x = A to H)
MODE15[1:0]
MODE14[1:0]
MODE13[1:0]
MODE12[1:0]
MODE11[1:0]
MODE10[1:0]
MODE9[1:0]
MODE8[1:0]
MODE7[1:0]
MODE6[1:0]
MODE5[1:0]
MODE4[1:0]
MODE3[1:0]
MODE2[1:0]
MODE1[1:0]
MODE0[1:0]
R e s e t  v a l u e  x  =  A 10101011111111111111111111111111
R e s e t  v a l u e  x  =  B 11111111111111111111111010111111
R e s e t  v a l u e  x  =  C  t o  G 11111111111111111111111111111111
R e s e t  v a l u e  x  =  H 00000000000000000000000000001111
0x04
GPIOx_OTYPER
(where x = A..H)
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OT15
OT14
OT13
OT12
OT11
OT10
OT9
OT8
OT7
OT6
OT5
OT4
OT3
OT2
OT1
OT0
R e s e t  v a l u e 0000000000000000
0x08
GPIOx_OSPEEDR
(where x = A to H)
OSPEED15[1:0]
OSPEED14[1:0]
OSPEED13[1:0]
OSPEED12[1:0]
OSPEED11[1:0]
OSPEED10[1:0]
OSPEED9[1:0]
OSPEED8[1:0]
OSPEED7[1:0]
OSPEED6[1:0]
OSPEED5[1:0]
OSPEED4[1:0]
OSPEED3[1:0]
OSPEED2[1:0]
OSPEED1[1:0]
OSPEED0[1:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x0C
GPIOA_PUPDR
(where x = A to H)
PUPDR15[1:0]
PUPDR14[1:0]
PUPDR13[1:0]
PUPDR12[1:0]
PUPDR11[1:0]
PUPDR10[1:0]
PUPDR9[1:0]
PUPDR8[1:0]
PUPDR7[1:0]
PUPDR6[1:0]
PUPDR5[1:0]
PUPDR4[1:0]
PUPDR3[1:0]
PUPDR2[1:0]
PUPDR1[1:0]
PUPDR0[1:0]
R e s e t  v a l u e  x  =  A 01100100000000000000000000000000
R e s e t  v a l u e  x  =  B 00000000000000000000000100000000
R e s e t  v a l u e  x  =  C  t o  H 00000000000000000000000000000000
0x10
GPIOx_IDR
(where x = A to H)
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ID15
ID14
ID13
ID12
ID11
ID10
ID9
ID8
ID7
ID6
ID5
ID4
ID3
ID2
ID1
ID0
R e s e t  v a l u e xxxxxxxxxxxxxxxx
0x14
GPIOx_ODR
(where x = A to H)
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OD15
OD14
OD13
OD12
OD11
OD10
OD9
OD8
OD7
OD6
OD5
OD4
OD3
OD2
OD1
OD0
R e s e t  v a l u e 0000000000000000
0x18
GPIOx_BSRR
(where x = A to H)
BR15
BR14
BR13
BR12
BR11
BR10
BR9
BR8
BR7
BR6
BR5
BR4
BR3
BR2
BR1
BR0
BS15
BS14
BS13
BS12
BS11
BS10
BS9
BS8
BS7
BS6
BS5
BS4
BS3
BS2
BS1
BS0
R e s e t  v a l u e 00000000000000000000000000000000
0x1C
GPIOx_LCKR
(where x = A to H)
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
LCKK
LCK15
LCK14
LCK13
LCK12
LCK11
LCK10
LCK9
LCK8
LCK7
LCK6
LCK5
LCK4
LCK3
LCK2
LCK1
LCK0
R e s e t  v a l u e 00000000000000000
0x20
GPIOx_AFRL
(where x = A to H) 7[3:0] 6[3:0] 5[3:0] 4[3:0] 3[3:0] 2[3:0] 1[3:0] 0[3:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x24
GPIOx_AFRH
(where x = A to H) 15[3:0] 14[3:0] 13[3:0] 12[3:0] 11[3:0] 10[3:0] 9[3:0] 8[3:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x28
GPIOx_BRR
(where x = A to H))
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
BR15
BR14
BR13
BR12
BR11
BR10
BR9
BR8
BR7
BR6
BR5
BR4
BR3
BR2
BR1
BR0
R e s e t  v a l u e 0000000000000000

RM0438 Rev 8 455/2187
RM0438 General-purpose I/Os (GPIO)
455
Refer to Section 2.3 on page 86 for the register boundary addresses.
0x30
GPIOx_SECCFGR
(where x = A to H)
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SEC15
SEC14
SEC13
SEC12
SEC11
SEC10
SEC9
SEC8
SEC7
SEC6
SEC5
SEC4
SEC3
SEC2
SEC1
SEC0
Reset value
(where x = A to G) 1111111111111111
Reset value
(where x = H) 0000000000001011
[Table 91](../tables/table_91.md). GPIO register map and reset values (continued)
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
* [Figure 37: Architectural Diagram](../figures/figure_37.md)
* [Figure 38: Architectural Diagram](../figures/figure_38.md)
* [Figure 39: Architectural Diagram](../figures/figure_39.md)
* [Figure 40: Architectural Diagram](../figures/figure_40.md)
* [Figure 41: Architectural Diagram](../figures/figure_41.md)
* [Figure 42: Architectural Diagram](../figures/figure_42.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 89: Configuration Matrix](../tables/table_89.md)
* [Table 90: Configuration Matrix](../tables/table_90.md)
* [Table 91: Configuration Matrix](../tables/table_91.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)