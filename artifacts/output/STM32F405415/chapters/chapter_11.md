# Chapter 11: General-purpose I/Os (GPIO)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32F4 Reference Manual RM0090 - Chapter 11: General-purpose I/Os (GPIO).
* **Document Source**: RM0090 Reference Manual
* **PDF Reference Location**: Pages 269 - 290
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [General-Purpose and Alternate-Function I/Os (GPIOs/AFIOs)](../peripherals/gpio.md)

## 2. Official Reference Manual Text Content (RM0090 Ingestion)
```text
RM0090 Rev 22 269/1741
RM0090 General-purpose I/Os (GPIO)
290
8 General-purpose I/Os (GPIO)
This section applies to the whole STM32F4xx family, unless otherwise specified.
8.1 GPIO introduction
Each general-purpose I/O port has four 32-bit configuration registers (GPIOx_MODER,
GPIOx_OTYPER, GPIOx_OSPEEDR and GPIOx_PUPDR), two 32-bit data registers
(GPIOx_IDR and GPIOx_ODR), a 32-bit set/reset register (GPIOx_BSRR), a 32-bit locking
register (GPIOx_LCKR) and two 32-bit alternate function selection register (GPIOx_AFRH
and GPIOx_AFRL).
8.2 GPIO main features
• Up to 16 I/Os under control
• Output states: push-pull or open drain + pull-up/down
• Output data from output data register (GPIOx_ODR) or peripheral (alternate function
output)
• Speed selection for each I/O
• Input states: floating, pull-up/down, analog
• Input data to input data register (GPIOx_IDR) or peripheral (alternate function input)
• Bit set and reset register (GPIOx_BSRR) for bitwise write access to GPIOx_ODR
• Locking mechanism (GPIOx_LCKR) provided to freeze the I/O configuration
• Analog function
• Alternate function input/output selection registers (at most 16 AFs per I/O)
• Fast toggle capable of changing every two clock cycles
• Highly flexible pin multiplexing allows the use of I/O pins as GPIOs or as one of several
peripheral functions
8.3 GPIO functional description
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

General-purpose I/Os (GPIO) RM0090
270/1741 RM0090 Rev 22
Each I/O port bit is freely programmable, however the I/O port registers have to be
accessed as 32-bit words, half-words or bytes. The purpose of the GPIOx_BSRR register is
to allow atomic read/modify accesses to any of the GPIO registers. In this way, there is no
risk of an IRQ occurring between the read and the modify access.
[Figure 25](../figures/figure_25.md) shows the basic structure of a 5 V-tolerant I/O port bit. [Table 40](../tables/table_40.md) gives the possible
port bit configurations.
[Figure 25](../figures/figure_25.md). Basic structure of a 5 V-tolerant I/O port bit
1. V DD_FT is a potential specific to 5 V-tolerant I/Os and different from VDD.
[Table 36](../tables/table_36.md). Port bit configuration table(1)
MODER(i)
[1:0] OTYPER(i) OSPEEDR(i)
[B:A]
PUPDR(i)
[1:0] I/O configuration
01
0
SPEED
[B:A]
0 0 GP output PP
0 0 1 GP output PP + PU
0 1 0 GP output PP + PD
0 1 1 Reserved
1 0 0 GP output OD
1 0 1 GP output OD + PU
1 1 0 GP output OD + PD
1 1 1 Reserved (GP output OD)
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
Analog
on/off
Pull
Pullon/off
I/O pin
VDD
VDD
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
Analog
Input data register
ai15939b

RM0090 Rev 22 271/1741
RM0090 General-purpose I/Os (GPIO)
290
8.3.1 General-purpose I/O (GPIO)
During and just after reset, the alternate functions are not active and the I/O ports are
configured in input floating mode.
The debug pins are in AF pull-up/pull-down after reset:
• PA15: JTDI in pull-up
• PA14: JTCK/SWCLK in pull-down
• PA13: JTMS/SWDAT in pull-up
• PB4: NJTRST in pull-up
• PB3: JTDO in floating state
When the pin is configured as output, the value written to the output data register
(GPIOx_ODR) is output on the I/O pin. It is possible to use the output driver in push-pull
mode or open-drain mode (only the N-MOS is activated when 0 is output).
The input data register (GPIOx_IDR) captures the data present on the I/O pin at every AHB1
clock cycle.
All GPIO pins have weak internal pull-up and pull-down resistors, which can be activated or
not depending on the value in the GPIOx_PUPDR register.
10
0
SPEED
[B:A]
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
1. GP = general-purpose, PP = push- pull, PU = pull-up, PD = pull-down, OD = open-drain, AF = alternate
function.
[Table 36](../tables/table_36.md). Port bit configuration table(1) (continued)
MODER(i)
[1:0] OTYPER(i) OSPEEDR(i)
[B:A]
PUPDR(i)
[1:0] I/O configuration

General-purpose I/Os (GPIO) RM0090
272/1741 RM0090 Rev 22
8.3.2 I/O pin multip lexer and mapping
The microcontroller I/O pins are connected to onboard peripherals/modules through a
multiplexer that allows only one peripheral’s alternate function (AF) connected to an I/O pin
at a time. In this way, there can be no conflict between peripherals sharing the same I/O pin.
Each I/O pin has a multiplexer with sixteen alternate function inputs (AF0 to AF15) that can
be configured through the GPIOx_AFRL (for pin 0 to 7) and GPIOx_AFRH (for pin 8 to 15)
registers:
• After reset all I/Os are connected to the system’s alternate function 0 (AF0).
• The peripherals’ alternate functions are mapped from AF1 to AF13.
• Cortex®-M4 with FPU output EVENTOUT signal can be used by configuring the I/O pin
to output on AF15.
An event can be signaled through the configured pin after executing SEV assembly
instruction. It can be used as internal trigger for some peripheral or externally on
related GPIO.
This structure is shown in [Figure 26](../figures/figure_26.md).
In addition to this flexible I/O multiplexing architecture, each peripheral has alternate
functions mapped onto different I/O pins to optimize the number of peripherals available in
smaller packages.
To use an I/O in a given configuration, proceed as follows:
• System function
Connect the I/O to AF0 and configure it depending on the function used:
– JTAG/SWD, after each device reset these pins are assigned as dedicated pins
immediately usable by the debugger host (not controlled by the GPIO controller)
– RTC_REFIN: this pin should be configured in Input floating mode
– MCO1 and MCO2:  these pins have to be configured in alternate function mode.
Note: The user can disable some or all of the JT AG/SWD pins and so release the associated pins
for GPIO usage (released pins highlighted in gray in the table).
For more details refer to Section 7.2.10: Clock-out capability and Section 6.2.10: Clock-out
capability.

RM0090 Rev 22 273/1741
RM0090 General-purpose I/Os (GPIO)
290
• GPIO
Configure the desired I/O as output or input in the GPIOx_MODER register.
• Peripheral alternate function
For the ADC and DAC, configure the desired I/O as analog in the GPIOx_MODER
register.
For other peripherals:
– Configure the desired I/O as an altern ate function in the GPIOx_MODER register
– Select the type, pull-up/pull-down and  output speed via the GPIOx_OTYPER,
GPIOx_PUPDR and GPIOx_OSPEEDR registers, respectively
– Connect the I/O to the desired AFx in  the GPIOx_AFRL or GPIOx_AFRH register
• EVENTOUT
Configure the I/O pin used to output the Cortex®-M4 with FPU EVENTOUT signal by
connecting it to AF15
Note: EVENTOUT is not mapped onto the following I/O pins: PC13, PC14, PC15, PH0, PH1 and
PI8.
Refer to the “Alternate function mapping” table in the datasheets for the detailed mapping of
the system and peripherals’ alternate function I/O pins.
[Table 37](../tables/table_37.md). Flexible SWJ-DP pin assignment
Available debug ports
SWJ I/O pin assigned
PA13/
JTMS/
SWDIO
PA14/
JTCK/
SWCLK
PA15/
JTDI
PB3/
JTDO
PB4/
NJTRST
Full SWJ (JTAG-DP + SW-DP) - Reset state X X X X X
Full SWJ (JTAG-DP + SW-DP) but without NJTRST X X X X
JTAG-DP disabled and SW-DP enabled X X
JTAG-DP disabled and SW-DP disabled Released

General-purpose I/Os (GPIO) RM0090
274/1741 RM0090 Rev 22
[Figure 26](../figures/figure_26.md). Selecting an alternate function on  STM32F405xx/07xx and
STM32F415xx/17xx
1. Configured in FS.
ai17538
For pins 0 to 7, the GPIOx_AFRL[31:0] register selects the dedicated alternate function
AF0 (system)
AF1 (TIM1/TIM2)
AF2 (TIM3..5)
AF3 (TIM8..11)
AF4 (I2C1..3)
AF5 (SPI1/SPI2)
AF6 (SPI3)
AF7 (USART1..3)
AF8 (USART4..6)
AF9 (CAN1/CAN2, TIM12..14)
AF10 (OTG_FS, OTG_HS)
AF11 (ETH)
AF12 (FSMC, SDIO, OTG_HS(1))
AF13 (DCMI)
AF14
AF15 (EVENTOUT)
Pin x (x = 0..7)
AFRL[31:0]
For pins 8 to 15, the GPIOx_AFRH[31:0] register selects the dedicated alternate function
AF0 (system)
AF1 (TIM1/TIM2)
AF2 (TIM3..5)
AF3 (TIM8..11)
AF4 (I2C1..3)
AF5 (SPI1/SPI2)
AF6 (SPI3)
AF7 (USART1..3)
AF8 (USART4..6)
AF9 (CAN1/CAN2, TIM12..14)
AF10 (OTG_FS, OTG_HS)
AF11 (ETH)
AF12 (FSMC, SDIO, OTG_HS(1))
AF13 (DCMI)
AF14
AF15 (EVENTOUT)
Pin x (x = 8..15)
AFRH[31:0]
1
1

RM0090 Rev 22 275/1741
RM0090 General-purpose I/Os (GPIO)
290
[Figure 27](../figures/figure_27.md). Selecting an alternate function on STM32F42xxx and STM32F43xxx
1. Configured in FS.
MS60208V1
For pins 0 to 7, the GPIOx_AFRL[31:0] register selects the dedicated alternate function
AF0 (system)
AF1 (TIM1/TIM2)
AF2 (TIM3..5)
AF3 (TIM8..11)
AF4 (I2C1..3)
AF5 (SPI1/2/3/4/5/6)
AF6 (SPI2/3/SAI1)
AF7 (USART1..3)
AF8 (USART4..8)
AF9 (CAN1/CAN2, LTDC, TIM12..14)
AF10 (OTG_FS, OTG_HS)
AF11 (ETH)
AF12 (FMC, SDIO, OTG_HS(1))
AF13 (DCMI)
AF14 (LTDC)
AF15 (EVENTOUT)
Pin x (x = 0..7)
AFRL[31:0]
For pins 8 to 15, the GPIOx_AFRH[31:0] register selects the dedicated alternate function
AF0 (system)
AF1 (TIM1/TIM2)
AF2 (TIM3..5)
AF3 (TIM8..11)
AF4 (I2C1..3)
AF5 (SPI1/2/4/5/6)
AF6 (SPI2/3/SAI1)
AF7 (USART1..3)
AF8 (USART4..8)
AF9 (CAN1/CAN2, TIM12..14)
AF10 (OTG_FS, OTG_HS)
AF11 (ETH)
AF12 (FMC, SDIO, OTG_HS(1))
AF13 (DCMI)
AF14 (LTDC)
AF15 (EVENTOUT)
Pin x (x = 8..15)
AFRH[31:0]
1
1

General-purpose I/Os (GPIO) RM0090
276/1741 RM0090 Rev 22
8.3.3 I/O port control registers
Each of the GPIOs has four 32-bit memory-mapped control registers (GPIOx_MODER,
GPIOx_OTYPER, GPIOx_OSPEEDR, GPIOx_PUPDR) to configure up to 16 I/Os.
The GPIOx_MODER register is used to select the I/O direction (input, output, AF, analog).
The GPIOx_OTYPER and GPIOx_OSPEEDR registers are used to select the output type
(push-pull or open-drain) and speed (the I/O speed pins are directly connected to the
corresponding GPIOx_OSPEEDR register bits whatever the I/O direction). The
GPIOx_PUPDR register is used to select the pull-up/pull-down whatever the I/O direction.
8.3.4 I/O port data registers
Each GPIO has two 16-bit memory-mapped data registers: input and output data registers
(GPIOx_IDR and GPIOx_ODR). GPIOx_ODR stores the data to be output, it is read/write
accessible. The data input through the I/O are stored into the input data register
(GPIOx_IDR), a read-only register.
See Section 8.4.5 and Section 8.4.6 for the register descriptions.
8.3.5 I/O data bitwise handling
The bit set reset register (GPIOx_BSRR) is a 32-bit register which allows the application to
set and reset each individual bit in the output data register (GPIOx_ODR). The bit set reset
register has twice the size of GPIOx_ODR.
To each bit in GPIOx_ODR, correspond two control bits in GPIOx_BSRR: BSRR(i) and
BSRR(i+SIZE). When written to 1, bit BSRR(i) sets the corresponding ODR(i) bit. When
written to 1, bit BSRR(i+SIZE) resets the ODR(i) corresponding bit.
Writing any bit to 0 in GPIOx_BSRR does not have any effect on the corresponding bit in
GPIOx_ODR. If there is an attempt to both set and reset a bit in GPIOx_BSRR, the set
action takes priority.
Using the GPIOx_BSRR register to change the values of individual bits in GPIOx_ODR is a
“one-shot” effect that does not lock the GPIOx_ODR bits. The GPIOx_ODR bits can always
be accessed directly. The GPIOx_BSRR register provides a way of performing atomic
bitwise handling.
There is no need for the software to disable interrupts when programming the GPIOx_ODR
at bit level: it is possible to modify one or more bits in a single atomic AHB1 write access.
8.3.6 GPIO locking mechanism
It is possible to freeze the GPIO control registers by applying a specific write sequence to
the GPIOx_LCKR register. The frozen registers are GPIOx_MODER, GPIOx_OTYPER,
GPIOx_OSPEEDR, GPIOx_PUPDR, GPIOx_AFRL and GPIOx_AFRH.
To write the GPIOx_LCKR register, a specific write / read sequence has to be applied. When
the right LOCK sequence is applied to bit 16 in this register, the value of LCKR[15:0] is used
to lock the configuration of the I/Os (during the write sequence the LCKR[15:0] value must
be the same). When the LOCK sequence has been applied to a port bit, the value of the port
bit can no longer be modified until the next MCU or peripheral reset. Each GPIOx_LCKR bit
freezes the corresponding bit in the control registers (GPIOx_MODER, GPIOx_OTYPER,
GPIOx_OSPEEDR, GPIOx_PUPDR, GPIOx_AFRL and GPIOx_AFRH).

RM0090 Rev 22 277/1741
RM0090 General-purpose I/Os (GPIO)
290
The LOCK sequence (refer to Section 8.4.8: GPIO port configuration lock register
(GPIOx_LCKR) (x = A..I/J/K)) can only be performed using a word (32-bit long) access to
the GPIOx_LCKR register due to the fact that GPIOx_LCKR bit 16 has to be set at the same
time as the [15:0] bits.
For more details refer to LCKR register description in Section 8.4.8.
8.3.7 I/O alternate function input/output
Two registers are provided to select one out of the sixteen alternate function inputs/outputs
available for each I/O. With these registers, you can connect an alternate function to some
other pin as required by your application.
This means that a number of possible peripheral functions are multiplexed on each GPIO
using the GPIOx_AFRL and GPIOx_AFRH alternate function registers. The application can
thus select any one of the possible functions for each I/O. The AF selection signal being
common to the alternate function input and alternate function output, a single channel is
selected for the alternate function input/output of one I/O.
To know which functions are multiplexed on each GPIO pin, refer to the datasheets.
Note: The application is allowed to  select one of the possible peripheral functions for each I/O at a
time.
8.3.8 External in terrupt/wake-up lines
All ports have external interrupt capability. To use external interrupt lines, the port must be
configured in input mode, refer to Section 12.2: External interrupt/event controller (EXTI)
and Section 12.2.3: Wake-up event management.
8.3.9 Input configuration
When the I/O port is programmed as Input:
• the output buffer is disabled
• the Schmitt trigger input is activated
• the pull-up and pull-down resistors are activated depending on the value in the
GPIOx_PUPDR register
• The data present on the I/O pin are sampled into the input data register every AHB1
clock cycle
• A read access to the input data register provides the I/O State
[Figure 28](../figures/figure_28.md) shows the input configuration of the I/O port bit.

General-purpose I/Os (GPIO) RM0090
278/1741 RM0090 Rev 22
[Figure 28](../figures/figure_28.md). Input floating/pull up/pull down configurations
8.3.10 Output configuration
When the I/O port is programmed as output:
• The output buffer is enabled:
– Open drain mode: A “0” in the Output register activates the N-MOS whereas a “1”
in the Output register leaves the port in Hi-Z (the P-MOS is never activated)
– Push-pull mode: A “0” in the Output register activates the N-MOS whereas a “1” in
the Output register activates the P-MOS
• The Schmitt trigger input is activated
• The weak pull-up and pull-down resistors are activated or not depending on the value
in the GPIOx_PUPDR register
• The data present on the I/O pin are sampled into the input data register every AHB1
clock cycle
• A read access to the input data register gets the I/O state
• A read access to the output data register gets the last written value
[Figure 29](../figures/figure_29.md) shows the output configuration of the I/O port bit.
on/off
pull
pull
on/off
I/O pin
VDD
VSS
TTL Schmitt
trigger
VSS
VDD
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
ai15940b

RM0090 Rev 22 279/1741
RM0090 General-purpose I/Os (GPIO)
290
[Figure 29](../figures/figure_29.md). Output configuration
8.3.11 Alternate function configuration
When the I/O port is programmed as alternate function:
• The output buffer can be configured as open-drain or push-pull
• The output buffer is driven by the signal coming from the peripheral (transmitter enable
and data)
• The Schmitt trigger input is activated
• The weak pull-up and pull-down resistors are activated or not depending on the value
in the GPIOx_PUPDR register
• The data present on the I/O pin are sampled into the input data register every AHB1
clock cycle
• A read access to the input data register gets the I/O state
[Figure 30](../figures/figure_30.md) shows the Alternate function configuration of the I/O port bit.
[Figure 30](../figures/figure_30.md). Alternate function configuration
Push-pull or
Open-drain
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
pull
pull
on/off
VDD
VSS VSS
VDD
protection
diode
protection
diodedown
up
I/O pin
ai15941b
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
VDD
VSS VSS
VDD
protection
diode
protection
diode
Pull
Pull
I/O pin
down
up
ai15942b

General-purpose I/Os (GPIO) RM0090
280/1741 RM0090 Rev 22
8.3.12 Analog configuration
When the I/O port is programmed as analog configuration:
• The output buffer is disabled
• The Schmitt trigger input is deactivated, providing zero consumption for every analog
value of the I/O pin. The output of the Schmitt trigger is forced to a constant value (0).
• The weak pull-up and pull-down resistors are disabled
• Read access to the input data register gets the value “0”
Note: In the analog configuration, the I/O pins cannot be 5 Volt tolerant.
[Figure 31](../figures/figure_31.md) shows the high-impedance, analog-input configuration of the I/O port bit.
[Figure 31](../figures/figure_31.md). High impedance-analog configuration
8.3.13 Using the OSC32_IN/OSC 32_OUT pins as GPIO PC14/PC15
port pins
The LSE oscillator pins OSC32_IN and OSC32_OUT can be used as general-purpose
PC14 and PC15 I/Os, respectively, when the LSE oscillator is off. The PC14 and PC15 I/Os
are only configured as LSE oscillator pins OSC32_IN and OSC32_OUT when the LSE
oscillator is ON. This is done by setting the LSEON bit in the RCC_BDCR register. The LSE
has priority over the GPIO function.
Note: The PC14/PC15 GPIO functionality is lost when the 1.2 V domain is powered off (by the
device entering the standby mode) or when the backup domain is supplied by VBAT (VDD no
more supplied). In this case the I/Os are set in analog input mode.
8.3.14 Using the OSC_IN/OSC_OUT pins as GPIO PH0/PH1 port pins
The HSE oscillator pins OSC_IN/OSC_OUT can be used as general-purpose PH0/PH1
I/Os, respectively, when the HSE oscillator is OFF. (after reset, the HSE oscillator is off). The
PH0/PH1 I/Os are only configured as OSC_IN/OSC_OUT HSE oscillator pins when the
HSE oscillator is ON. This is done by setting the HSEON bit in the RCC_CR register. The
HSE has priority over the GPIO function.
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
VDD
protection
diode
protection
diode
I/O pin
ai15943
TTL Schmitt

RM0090 Rev 22 281/1741
RM0090 General-purpose I/Os (GPIO)
290
8.3.15 Selection of RTC_AF1 a nd RTC_AF2 alternate functions
The STM32F4xx feature two GPIO pins RTC_AF1 and RTC_AF2 that can be used for the
detection of a tamper or time stamp event, or RTC_ALARM, or RTC_CALIB RTC outputs.
• The RTC_AF1 (PC13) can be used for the following purposes:
RTC_ALARM output: this output can be RTC Alarm A, RTC Alarm B or RTC Wake-up
depending on the OSEL[1:0] bits in the RTC_CR register
• RTC_CALIB output: this feature is enabled by setting the COE[23] in the RTC_CR
register
• RTC_TAMP1: tamper event detection
• RTC_TS: time stamp event detection
The RTC_AF2 (PI8) can be used for the following purposes:
• RTC_TAMP1: tamper event detection
• RTC_TAMP2: tamper event detection
• RTC_TS: time stamp event detection
The selection of the corresponding pin is performed through the RTC_TAFCR register as
follows:
• TAMP1INSEL is used to select which pin is used as the RTC_TAMP1 tamper input
• TSINSEL is used to select which pin is used as the RTC_TS time stamp input
• ALARMOUTTYPE is used to select whether the RTC_ALARM is output in push-pull or
open-drain mode
The output mechanism follows the priority order listed in [Table 38](../tables/table_38.md) and [Table 39](../tables/table_39.md).
[Table 38](../tables/table_38.md). RTC_AF1 pin(1)
Pin
configuration
and function
RTC_ALARM
enabled
RTC_CALIB
enabled
Tamper
enabled
Time
stamp
enabled
TAMP1INSEL
TAMPER1
pin selection
TSINSEL
TIMESTAMP
pin
selection
ALARMOUTTYPE
RTC_ALARM
configuration
Alarm out
output OD 1D o n ’ t  c a r e Don’t
care
Don’t
care Don’t care Don’t care 0
Alarm out
output PP 1D o n ’ t  c a r e Don’t
care
Don’t
care Don’t care Don’t care 1
Calibration
out output PP 01 Don’t
care
Don’t
care Don’t care Don’t care Don’t care
TAMPER1
input floating 0 0 1 0 0 Don’t care Don’t care
TIMESTAMP
and
TAMPER1
input floating
0 0 1 1 0 0 Don’t care
TIMESTAMP
input floating 0 0 0 1 Don’t care 0 Don’t care
Standard
GPIO 0 0 0 0 Don’t care Don’t care Don’t care
1. OD: open drain; PP: push-pull.

General-purpose I/Os (GPIO) RM0090
282/1741 RM0090 Rev 22
[Table 39](../tables/table_39.md). RTC_AF2 pin
Pin configuration and function Tamper
enabled
Time
stamp
enabled
TAMP1INSEL
TAMPER1
pin selection
TSINSEL
TIMESTAMP
pin
selection
ALARMOUTTYPE
RTC_ALARM
configuration
TAMPER1 input floating 1 0 1 Don’t care Don’t care
TIMESTAMP and TAMPER1 input
floating 11 1 1 D o n ’ t  c a r e
TIMESTAMP input floating 0 1 Don’t care 1 Don’t care
Standard GPIO 0 0 Don’t care Don’t care Don’t care

RM0090 Rev 22 283/1741
RM0090 General-purpose I/Os (GPIO)
290
8.4 GPIO registers
This section gives a detailed description of the GPIO registers.
For a summary of register bits, register address offsets and reset values, refer to [Table 40](../tables/table_40.md).
The GPIO registers can be accessed by byte (8 bits), half-words (16 bits) or words (32 bits).
8.4.1 GPIO port mode register  (GPIOx_MODER) (x = A..I/J/K)
Address offset: 0x00
Reset values:
• 0xA800 0000 for port A
• 0x0000 0280 for port B
• 0x0000 0000 for other ports
8.4.2 GPIO port output type  register (GPIOx_OTYPER)
(x = A..I/J/K)
Address offset: 0x04
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
MODER15[1:0] MODER14[1:0] MODER13[1:0] MODER12[1:0] MODER11[1:0] MODER10[1:0] MODER9[1:0] MODER8[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
MODER7[1:0] MODER6[1:0] MODER5[1:0] MODER4[1:0] MODER3[1:0] MODER2[1:0] MODER1[1:0] MODER0[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 2y:2y+1 MODERy[1:0]: Port x configuration bits (y = 0..15)
These bits are written by software to configure the I/O direction mode.
00: Input (reset state)
01: General purpose output mode
10: Alternate function mode
11: Analog mode
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Reserved
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
OT15 OT14 OT13 OT12 OT11 OT10 OT9 OT8 OT7 OT6 OT5 OT4 OT3 OT2 OT1 OT0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 OTy: Port x configuration bits (y = 0..15)
These bits are written by software to configure the output type of the I/O port.
0: Output push-pull (reset state)
1: Output open-drain

General-purpose I/Os (GPIO) RM0090
284/1741 RM0090 Rev 22
8.4.3 GPIO port output sp eed register (GPIOx_OSPEEDR)
(x = A..I/J/K)
Address offset: 0x08
Reset values:
• 0x0C00 0000 for port A
• 0x0000 00C0 for port B
• 0x0000 0000 for other ports
8.4.4 GPIO port pull-up/pull -down register (GPIOx_PUPDR)
(x = A..I/J/K)
Address offset: 0x0C
Reset values:
• 0x6400 0000 for port A
• 0x0000 0100 for port B
• 0x0000 0000 for other ports
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
OSPEEDR15
[1:0]
OSPEEDR14
[1:0]
OSPEEDR13
[1:0]
OSPEEDR12
[1:0]
OSPEEDR11
[1:0]
OSPEEDR10
[1:0]
OSPEEDR9
[1:0]
OSPEEDR8
[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
OSPEEDR7[1:0] OSPEEDR6[1:0] OSPEEDR5[1:0] OSPEEDR4[1:0] OSPEEDR3[1:0] OSPEEDR2[1:0] OSPEEDR1
[1:0]
OSPEEDR0
1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 2y:2y+1 OSPEEDRy[1:0]: Port x configuration bits (y = 0..15)
These bits are written by software to configure the I/O output speed.
00: Low speed
01: Medium speed
10: High speed
11: Very high speed
Note: Refer to the product datasheets for the values of OSPEEDRy bits versus VDD
range and external load.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
PUPDR15[1:0] PUPDR14[1:0] PUPDR13[1:0] PUPDR12[1:0] PUPDR11[1:0] PUPDR10[1:0] PUPDR9[1:0] PUPDR8[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PUPDR7[1:0] PUPDR6[1:0] PUPDR5[1:0] PUPDR4[1:0 ] PUPDR3[1:0] PUPDR2[1:0] PUPDR1[1:0] PUPDR0[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0090 Rev 22 285/1741
RM0090 General-purpose I/Os (GPIO)
290
8.4.5 GPIO port input  data register (GPIOx_IDR) (x = A..I/J/K)
Address offset: 0x10
Reset value: 0x0000 XXXX (where X means undefined)
8.4.6 GPIO port output data re gister (GPIOx_ODR) (x = A..I/J/K)
Address offset: 0x14
Reset value: 0x0000 0000
Bits 2y:2y+1 PUPDRy[1:0]: Port x configuration bits (y = 0..15)
These bits are written by software to configure the I/O pull-up or pull-down
00: No pull-up, pull-down
01: Pull-up
10: Pull-down
11: Reserved
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Reserved
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
IDR15 IDR14 IDR13 IDR12 IDR11 IDR10 IDR9 IDR8 IDR7 IDR6 IDR5 IDR4 IDR3 IDR2 IDR1 IDR0
rrrrrrr r r r rrrrrr
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 IDRy: Port input data (y = 0..15)
These bits are read-only and can be accessed in word mode only. They contain the input
value of the corresponding I/O port.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Reserved
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ODR15 ODR14 ODR13 ODR12 ODR11 ODR10 ODR9 ODR8 ODR7 ODR6 ODR5 ODR4 ODR3 ODR2 ODR1 ODR0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 ODRy: Port output data (y = 0..15)
These bits can be read and written by software.
Note: For atomic bit set/reset, the ODR bits can be individually set and reset by writing to the
GPIOx_BSRR register (x = A..I/J/K).

General-purpose I/Os (GPIO) RM0090
286/1741 RM0090 Rev 22
8.4.7 GPIO port bit se t/reset register (GPIOx_BSRR) (x = A..I/J/K)
Address offset: 0x18
Reset value: 0x0000 0000
8.4.8 GPIO port c onfiguration lock register (GPIOx_LCKR)
(x = A..I/J/K)
This register is used to lock the configuration of the port bits when a correct write sequence
is applied to bit 16 (LCKK). The value of bits [15:0] is used to lock the configuration of the
GPIO. During the write sequence, the value of LCKR[15:0] must not change. When the
LOCK sequence has been applied on a port bit, the value of this port bit can no longer be
modified until the next MCU or peripheral reset.
Note: A specific write se quence is used to write to the GPIOx_LCKR register. Only word access
(32-bit long) is allowed during this write sequence.
Each lock bit freezes a specific configuration register (control and alternate function
registers).
Address offset: 0x1C
Reset value: 0x0000 0000
Access: 32-bit word only, read/write register
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
BR15 BR14 BR13 BR12 BR11 BR10 BR9 BR8 BR7 BR6 BR5 BR4 BR3 BR2 BR1 BR0
wwwwwwwww w w w w www
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
BS15 BS14 BS13 BS12 BS11 BS10 BS9 BS8 BS7 BS6 BS5 BS4 BS3 BS2 BS1 BS0
wwwwwwwww w w w w www
Bits 31:16 BRy: Port x reset bit y (y = 0..15)
These bits are write-only and can be accessed in word, half-word or byte mode. A read to
these bits returns the value 0x0000.
0: No action on the corresponding ODRx bit
1: Resets the corresponding ODRx bit
Note: If both BSx and BRx are set, BSx has priority.
Bits 15:0 BSy: Port x set bit y (y= 0..15)
These bits are write-only and can be accessed in word, half-word or byte mode. A read to
these bits returns the value 0x0000.
0: No action on the corresponding ODRx bit
1: Sets the corresponding ODRx bit
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Reserved
LCKK
rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
LCK15 LCK14 LCK13 LCK12 LCK11 LCK10 LCK9 LC K8 LCK7 LCK6 LCK5 LCK4 LCK3 LCK2 LCK1 LCK0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0090 Rev 22 287/1741
RM0090 General-purpose I/Os (GPIO)
290
8.4.9 GPIO alternate function low re gister (GPIOx_AFRL) (x = A..I/J/K)
Address offset: 0x20
Reset value: 0x0000 0000
Bits 31:17 Reserved, must be kept at reset value.
Bit 16 LCKK[16]: Lock key
This bit can be read any time. It can only be modified using the lock key write sequence.
0: Port configuration lock key not active
1: Port configuration lock key active. The GPIOx_LCKR register is locked until an MCU reset
or a peripheral reset occurs.
LOCK key write sequence:
WR LCKR[16] = ‘1’ + LCKR[15:0]
WR LCKR[16] = ‘0’ + LCKR[15:0]
WR LCKR[16] = ‘1’ + LCKR[15:0]
RD LCKR
RD LCKR[16] = ‘1’ (this read operation is optional but it confirms that the lock is active)
Note: During the LOCK key write sequence, the value of LCK[15:0] must not change.
Any error in the lock sequence aborts the lock.
After the first lock sequence on any bit of the port, any read access on the LCKK bit
returns ‘1’ until the next CPU reset.
Bits 15:0 LCKy: Port x lock bit y (y= 0..15)
These bits are read/write but can only be written when the LCKK bit is ‘0.
0: Port configuration not locked
1: Port configuration locked
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
AFRL7[3:0] AFRL6[3:0] AFRL5[3:0] AFRL4[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
AFRL3[3:0] AFRL2[3:0] AFRL1[3:0] AFRL0[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 AFRLy: Alternate function selection for port x bit y (y = 0..7)
These bits are written by software to configure alternate function I/Os
AFRLy selection:
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

General-purpose I/Os (GPIO) RM0090
288/1741 RM0090 Rev 22
8.4.10 GPIO alternate functi on high register (GPIOx_AFRH)
(x = A..I/J)
Address offset: 0x24
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
AFRH15[3:0] AFRH14[3:0] AFRH13[3:0] AFRH12[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
AFRH11[3:0] AFRH10[3:0] AFRH9[3:0] AFRH8[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 AFRHy: Alternate function selection for port x bit y (y = 8..15)
These bits are written by software to configure alternate function I/Os
AFRHy selection:
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

RM0090 Rev 22 289/1741
RM0090 General-purpose I/Os (GPIO)
290
8.4.11 GPIO register map
The following table gives the GPIO register map and the reset values.
[Table 40](../tables/table_40.md). GPIO register map and reset values
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
GPIOA_
MODER
MODER15[1:0]
MODER14[1:0]
MODER13[1:0]
MODER12[1:0]
MODER11[1:0]
MODER10[1:0]
MODER9[1:0]
MODER8[1:0]
MODER7[1:0]
MODER6[1:0]
MODER5[1:0]
MODER4[1:0]
MODER3[1:0]
MODER2[1:0]
MODER1[1:0]
MODER0[1:0]
R e s e t  v a l u e 10101000000000000000000000000000
0x00
GPIOB_
MODER
MODER15[1:0]
MODER14[1:0]
MODER13[1:0]
MODER12[1:0]
MODER11[1:0]
MODER10[1:0]
MODER9[1:0]
MODER8[1:0]
MODER7[1:0]
MODER6[1:0]
MODER5[1:0]
MODER4[1:0]
MODER3[1:0]
MODER2[1:0]
MODER1[1:0]
MODER0[1:0]
R e s e t  v a l u e 00000000000000000000001010000000
0x00
GPIOx_MODER
(where x =
C..I/J/K)
MODER15[1:0]
MODER14[1:0]
MODER13[1:0]
MODER12[1:0]
MODER11[1:0]
MODER10[1:0]
MODER9[1:0]
MODER8[1:0]
MODER7[1:0]
MODER6[1:0]
MODER5[1:0]
MODER4[1:0]
MODER3[1:0]
MODER2[1:0]
MODER1[1:0]
MODER0[1:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x04
GPIOx_
OTYPER
(where x =
A..I/J/K)
Reserved
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
GPIOx_
OSPEEDR
(where x =
A..I/J/K except
B)
OSPEEDR15[1:0]
OSPEEDR14[1:0]
OSPEEDR13[1:0]
OSPEEDR12[1:0]
OSPEEDR11[1:0]
OSPEEDR10[1:0]
OSPEEDR9[1:0]
OSPEEDR8[1:0]
OSPEEDR7[1:0]
OSPEEDR6[1:0]
OSPEEDR5[1:0]
OSPEEDR4[1:0]
OSPEEDR3[1:0]
OSPEEDR2[1:0]
OSPEEDR1[1:0]
OSPEEDR0[1:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x08
GPIOB_
OSPEEDR
OSPEEDR15[1:0]
OSPEEDR14[1:0]
OSPEEDR13[1:0]
OSPEEDR12[1:0]
OSPEEDR11[1:0]
OSPEEDR10[1:0]
OSPEEDR9[1:0]
OSPEEDR8[1:0]
OSPEEDR7[1:0]
OSPEEDR6[1:0]
OSPEEDR5[1:0]
OSPEEDR4[1:0]
OSPEEDR3[1:0]
OSPEEDR2[1:0]
OSPEEDR1[1:0]
OSPEEDR0[1:0]
R e s e t  v a l u e 00000000000000000000000011000000
0x0C GPIOA_PUPDR
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
R e s e t  v a l u e 01100100000000000000000000000000
0x0C GPIOB_PUPDR
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
R e s e t  v a l u e 00000000000000000000000100000000

General-purpose I/Os (GPIO) RM0090
290/1741 RM0090 Rev 22
Refer to Section 2.3: Memory map for the register boundary addresses.
0x0C
GPIOx_PUPDR
(where x =
C..I/J/K)
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
R e s e t  v a l u e 00000000000000000000000000000000
0x10
GPIOx_IDR
(where x =
A..I/J/K) Reserved
IDR15
IDR14
IDR13
IDR12
IDR11
IDR10
IDR9
IDR8
IDR7
IDR6
IDR5
IDR4
IDR3
IDR2
IDR1
IDR0
R e s e t  v a l u e xxxxxxxxxxxxxxxx
0x14
GPIOx_ODR
(where x =
A..I/J/K) Reserved
ODR15
ODR14
ODR13
ODR12
ODR11
ODR10
ODR9
ODR8
ODR7
ODR6
ODR5
ODR4
ODR3
ODR2
ODR1
ODR0
R e s e t  v a l u e 0000000000000000
0x18
GPIOx_BSRR
(where x =
A..I/J/K)
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
(where x =
A..I/J/K) Reserved
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
(where x =
A..I/J/K)
AFRL7[3:0] AFRL6[3:0] AFRL5[3:0] AFRL4[3:0] AFRL3[3:0] AFRL2[3:0] AFRL1[3:0] AFRL0[3:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x24
GPIOx_AFRH
(where x =
A..I/J)
AFRH15[3:0] AFRH14[3:0] AFRH13[3:0] AFRH12[3:0] AFRH11[3:0] AFRH10[3:0] AFRH9[3:0] AFRH8[3:0]
R e s e t  v a l u e 00000000000000000000000000000000
[Table 40](../tables/table_40.md). GPIO register map and reset values (continued)
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
* [Figure 25: Architectural Diagram](../figures/figure_25.md)
* [Figure 26: Architectural Diagram](../figures/figure_26.md)
* [Figure 27: Architectural Diagram](../figures/figure_27.md)
* [Figure 28: Architectural Diagram](../figures/figure_28.md)
* [Figure 29: Architectural Diagram](../figures/figure_29.md)
* [Figure 30: Architectural Diagram](../figures/figure_30.md)
* [Figure 31: Architectural Diagram](../figures/figure_31.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 36: Configuration Matrix](../tables/table_36.md)
* [Table 37: Configuration Matrix](../tables/table_37.md)
* [Table 38: Configuration Matrix](../tables/table_38.md)
* [Table 39: Configuration Matrix](../tables/table_39.md)
* [Table 40: Configuration Matrix](../tables/table_40.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)