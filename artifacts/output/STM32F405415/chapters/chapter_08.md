# Chapter 8: Power controller (PWR)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32F4 Reference Manual RM0090 - Chapter 8: Power controller (PWR).
* **Document Source**: RM0090 Reference Manual
* **PDF Reference Location**: Pages 116 - 150
* **Taxonomy Section**: SYSTEM
* **Parent IP Module**: [Power Control (PWR)](../system/pwr.md)

## 2. Official Reference Manual Text Content (RM0090 Ingestion)
```text
Power controller (PWR) RM0090
116/1741 RM0090 Rev 22
5 Power controller (PWR)
This section applies to the whole STM32F4xx family, unless otherwise specified.
5.1 Power supplies
The device requires a 1.8 to 3.6 V operating voltage supply (VDD). An embedded linear
voltage regulator is used to supply the internal 1.2 V digital power.
The real-time clock (RTC), the RTC backup registers, and the backup SRAM (BKP SRAM)
can be powered from the VBAT voltage when the main VDD supply is powered off.
Note: Depending on the operating power supply range, some peripheral may be used with limited
functionality and performance. For more details refer to section “General operating
conditions” in STM32F4xx datasheets.
[Figure 9](../figures/figure_9.md). Power supply overview for STM32F405xx/07xx and STM32F415xx/17xx
1. V DDA and VSSA must be connected to VDD and VSS, respectively.
MS19911V2
Backup circuitry
(OSC32K,RTC,
Wakeup logic
Backup registers,
backup RAM)
Kernel logic
(CPU, digital
& RAM)
Analog:
RCs,
PLL,..
Power
switch
VBAT
GPIOs
OUT
IN
15 × 100 nF
+ 1 × 4.7 μF
VBAT =
1.65 to 3.6V
Voltage
regulator
VDDA
ADC
Level shifter
IO
Logic
VDD
100 nF
+ 1 μF
Flash memory
VCAP_1
VCAP_22 × 2.2 μF
BYPASS_REG
PDR_ON
Reset
controller
VDD
1/2/...14/15
VSS
1/2/...14/15
VDD
VREF+
VREF-
VSSA
VREF
100 nF
+ 1 μF

RM0090 Rev 22 117/1741
RM0090 Power controller (PWR)
150
[Figure 10](../figures/figure_10.md). Power supply overview for STM32F42xxx and STM32F43xxx
1. V DDA and VSSA must be connected to VDD and VSS, respectively.
5.1.1 Independent A/D converte r supply and reference voltage
To improve conversion accuracy, the ADC has an independent power supply which can be
separately filtered and shielded from noise on the PCB.
• The ADC voltage supply input is available on a separate VDDA pin.
• An isolated supply ground connection is provided on VSSA pin.
To ensure a better accuracy of low voltage inputs, the user can connect a separate external
reference voltage ADC input on VREF. The voltage on VREF ranges from 1.8 V to VDDA.
MS30482V2
VDD
1/2/...14/20
Analog:
RCs, PLL,
...
Power switch
VBAT
GP I/Os
OUT
IN Kernel logic
(CPU,
digital
& RAM)
Backup circuitry
(OSC32K,RTC,
Backup registers,
backup RAM)
Wakeup logic
19 × 100 nF
+ 1 × 4.7 μF
VBAT =
1.65 to 3.6V
Voltage
regulator
VSS
1/2/...14/20
VDDA
VREF+
VREF-
VSSA
ADC
Level shifter
IO
Logic
VDD
+ 1 μF
VREF
100 nF
+ 1 μF
VDD
Flash memory
VCAP_1VCAP_22 × 2.2 μF
BYPASS_REG
PDR_ON
Reset
controller
100 nF

Power controller (PWR) RM0090
118/1741 RM0090 Rev 22
5.1.2 Battery backup domain
Backup domain description
To retain the content of the RTC backup registers, backup SRAM, and supply the RTC when
VDD is turned off, VBAT pin can be connected to an optional standby voltage supplied by a
battery or by another source.
To allow the RTC to operate even when the main digital supply (VDD) is turned off, the VBAT
pin powers the following blocks:
• The RTC
• The LSE oscillator
• The backup SRAM when the low-power backup regulator is enabled
• PC13 to PC15 I/Os, plus PI8 I/O (when available)
The switch to the VBAT supply is controlled by the power-down reset embedded in the Reset
block.
Warning: During tRSTTEMPO (temporization at VDD startup) or after a PDR
is detected, the power switch between VBAT and VDD remains
connected to VBAT.
During the startup phase, if VDD is established in less than
tRSTTEMPO (Refer to the datasheet for the value of tRSTTEMPO)
and VDD > VBAT + 0.6 V, a current may be injected into VBAT
through an internal diode connected between VDD and the
power switch (VBAT).
If the power supply/battery connected to the VBAT pin cannot
support this current injection, it is strongly recommended to
connect an external low-drop diode between this power
supply and the VBAT pin.
If no external battery is used in the application, it is recommended to connect VBAT pin to
VDD supply, and add a 100 nF ceramic decoupling capacitor on VBAT pin.
When the backup domain is supplied by VDD (analog switch connected to VDD), the
following functions are available:
• PC14 and PC15 can be used as either GPIO or LSE pins
• PC13 can be used as a GPIOas the RTC_AF1 pin (refer to [Table 38](../tables/table_38.md): RTC_AF1 pin for
more details about this pin configuration)
Note: Due to the fact that the switch only sinks a limited amount of current (3 mA), the use of PI8
and PC13 to PC15 GPIOs in output mode is restricted: the speed has to be limited to 2 MHz
with a maximum load of 30 pF and these I/Os must not be used as a current source (e.g. to
drive an LED).

RM0090 Rev 22 119/1741
RM0090 Power controller (PWR)
150
When the backup domain is supplied by VBAT (analog switch connected to VBAT because
VDD is not present), the following functions are available:
• PC14 and PC15 can be used as LSE pins only
• PC13 can be used as the RTC_AF1 pin (refer to [Table 38](../tables/table_38.md): RTC_AF1 pin for more
details about this pin configuration)
• PI8 can be used as RTC_AF2
Backup domain access
After reset, the backup domain (RTC registers, RTC backup register and backup SRAM) is
protected against possible unwanted write accesses. To enable access to the backup
domain, proceed as follows:
• Access to the RTC and RTC backup registers
1. Enable the power interfac e clock by setting the PWREN bits in the RCC_APB1ENR
register (see Section 7.3.13 and Section 6.3.13)
2. Set the DBP bit in the Section 5.4.1 and PWR power control register (PWR_CR) for
STM32F42xxx and STM32F43xxx to enable access to the backup domain
3. Select the RTC clock source: see Section 7.2.8: RTC/AWU clock
4. Enable the RTC clock by programming the RTCEN [15] bit in the Section 7.3.20: RCC
Backup domain control register (RCC_BDCR)
• Access to the backup SRAM
1. Enable the power interfac e clock by setting the PWREN bits in the RCC_APB1ENR
register (see Section 7.3.13 and Section 6.3.13 for STM32F405xx/07xx and
STM32F415xx/17xx and STM32F42xxx and STM32F43xxx, respectively)
2. Set the DBP bit in the PWR power control register (PWR_CR) for STM32F405xx/07xx
and STM32F415xx/17xx and PWR power control register (PWR_CR) for
STM32F42xxx and STM32F43xxx to enable access to the backup domain
3. Enable the backup  SRAM clock by setting BKPSRAMEN bit in the RCC AHB1
peripheral clock enable register (RCC_AHB1ENR).
RTC and RTC backup registers
The real-time clock (RTC) is an independent BCD timer/counter. The RTC provides a time-
of-day clock/calendar, two programmable alarm interrupts, and a periodic programmable
wake-up flag with interrupt capability. The RTC contains 20 backup data registers (80 bytes)
which are reset when a tamper detection event occurs. For more details refer to Section 26:
Real-time clock (RTC).
Backup SRAM
The backup domain includes 4 Kbytes of backup SRAM addressed in 32-bit, 16-bit or 8-bit
mode. Its content is retained even in Standby or VBAT mode when the low-power backup
regulator is enabled. It can be considered as an internal EEPROM when VBAT is always
present.
When the backup domain is supplied by VDD (analog switch connected to VDD), the backup
SRAM is powered from VDD which replaces the VBAT power supply to save battery life.
When the backup domain is supplied by VBAT (analog switch connected to VBAT because
VDD is not present), the backup SRAM is powered by a dedicated low-power regulator. This
regulator can be ON or OFF depending whether the application needs the backup SRAM
function in Standby and VBAT modes or not. The power-down of this regulator is controlled

Power controller (PWR) RM0090
120/1741 RM0090 Rev 22
by a dedicated bit, the BRE control bit of the PWR_CSR register (see Section 5.4.2: PWR
power control/status register (PWR_CSR)  for STM32F405xx/07xx and
STM32F415xx/17xx).
The backup SRAM is not mass erased by an tamper event. When the Flash memory is read
protected, the backup SRAM is also read protected to prevent confidential data, such as
cryptographic private key, from being accessed. When the protection level change from
level 1 to level 0 is requested, the backup SRAM content is erased.
[Figure 11](../figures/figure_11.md). Backup domain
5.1.3 Voltage regulator for ST M32F405xx/07xx and STM32F415xx/17xx
An embedded linear voltage regulator supplies all the digital circuitries except for the backup
domain and the Standby circuitry. The regulator output voltage is around 1.2 V.
This voltage regulator requires one or two external capacitors to be connected to one or two
dedicated pins, VCAP_1 and  VCAP_2 available in all packages. Specific pins must be
connected either to VSS or VDD to activate or deactivate the voltage regulator. These pins
depend on the package.
When activated by software, the voltage regulator is always enabled after Reset. It works in
three different modes depending on the application modes.
• In Run mode, the regulator supplies full power to the 1.2 V domain (core, memories
and digital peripherals). In this mode, the regulator output voltage (around 1.2 V) can
be scaled by software to different voltage values:
Scale 1 or scale 2 can be configured on the fly through VOS[1:0] bits of the
PWR_CR register.
The voltage scaling allows optimizing the power consumption when the device is
clocked below the maximum system frequency.
• In Stop mode, the main regulator or the low-power regulator supplies to the 1.2 V
domain, thus preserving the content of registers and internal SRAM. The voltage
MS30430V1
Voltage regulator
3.3 -> 1.2 V
1.2 V domain
Backup SRAM
interface
Power switch LP  voltage regulator
3.3 -> 1.2 V
Backup SRAM
1.2 V
RTC LSE 32.768 Hz
Backup domain

RM0090 Rev 22 121/1741
RM0090 Power controller (PWR)
150
regulator can be put either in main regulator mode (MR) or in low-power mode (LPR).
The programmed voltage scale remains the same during Stop mode:
The programmed voltage scale remains the same during Stop mode (see
Section 5.4.1: PWR power control register (PWR_CR) for STM32F405xx/07xx
and STM32F415xx/17xx).
• In Standby mode, the regulator is powered down. The content of the registers and
SRAM are lost except for the Standby circuitry and the backup domain.
Note: For more details, refer to the voltage regulator section in the STM32F405xx/07xx and
STM32F415xx/17xx datasheets.
5.1.4 Voltage regulator for STM32F42xxx and STM32F43xxx
An embedded linear voltage regulator supplies all the digital circuitries except for the backup
domain and the Standby circuitry. The regulator output voltage is around 1.2 V.
This voltage regulator requires two external capacitors to be connected to two dedicated
pins, VCAP_1 and VCAP_2 available in all packages. Specific pins must be connected
either to VSS or VDD to activate or deactivate the voltage regulator. These pins depend on
the package.
When activated by software, the voltage regulator is always enabled after Reset. It works in
three different modes depending on the application modes (Run, Stop, or Standby mode).
• In Run mode, the main regulator supplies full power to the 1.2 V domain (core,
memories and digital peripherals). In this mode, the regulator output voltage (around
1.2 V) can be scaled by software to different voltage values (scale 1, scale 2, and scale
3 can be configured through VOS[1:0] bits of the PWR_CR register). The scale can be
modified only when the PLL is OFF and the HSI or HSE clock source is selected as
system clock source. The new value programmed is active only when the PLL is ON.
When the PLL is OFF, the voltage scale 3 is automatically selected.
The voltage scaling allows optimizing the power consumption when the device is
clocked below the maximum system frequency. After exit from Stop mode, the voltage

Power controller (PWR) RM0090
122/1741 RM0090 Rev 22
scale 3 is automatically selected.(see Section 5.4.1: PWR power control register
(PWR_CR) for STM32F405xx/07xx and STM32F415xx/17xx.
2 operating modes are available:
– Normal mode: The CPU and core logic operate at maximum frequency at a given
voltage scaling (scale 1, scale 2 or scale 3)
– Over-drive mode: This mode allows the CPU and the core logic to operate at a
higher frequency than the normal mode for the voltage scaling scale 1 and scale
2.
• In Stop mode: the main regulator or low-power regulator supplies a low-power voltage
to the 1.2V domain, thus preserving the content of registers and internal SRAM.
The voltage regulator can be put either in main regulator mode (MR) or in low-power
mode (LPR). Both modes can be configured by software as follows:
– Normal mode: the 1.2 V domain is preserved in nominal leakage mode. It is the
default mode when the main regulator (MR) or the low-power regulator (LPR) is
enabled.
– Under-drive mode: the 1.2 V domain is preserved in reduced leakage mode. This
mode is only available with the main regulator or in low-power regulator mode
(see [Table 23](../tables/table_23.md)).
• In Standby mode: the regulator is powered down. The content of the registers and
SRAM are lost except for the Standby circuitry and the backup domain.
Note: Over-drive and under-drive mode are not available when the regulator is bypassed.
For more details, refer to the voltage regulator section in the STM32F42xxx and
STM32F43xxx datasheets.
[Table 23](../tables/table_23.md). Voltage regulator configuration mode versus device operating mode(1)
1. ‘-’ means that the corresponding configuration is not available.
Voltage regulator
configuration Run mode Sleep mode Stop mode Standby mode
Normal mode MR MR MR or LPR -
Over-drive
mode(2)
2. The over-drive mode is not available when V DD = 1.8 to 2.1 V.
MR MR - -
Under-drive mode - - MR or LPR -
Power-down
mode --- Y e s

RM0090 Rev 22 123/1741
RM0090 Power controller (PWR)
150
Entering Over-drive mode
It is recommended to enter Over-drive mode when the application is not running critical
tasks and when the system clock source is either HSI or HSE. To optimize the configuration
time, enable the Over-drive mode during the PLL lock phase.
To enter Over-drive mode, follow the sequence below:
1. Select HSI or HSE as system clock.
2. Configure RCC_PL LCFGR register and set PLLON bit of RCC_CR register.
3. Set ODEN bit of PWR_CR register to enab le the Over-drive mode and wait for the
ODRDY flag to be set in the PWR_CSR register.
4. Set the ODSW bit in the PWR_CR register to  switch the voltage regulator from Normal
mode to Over-drive mode. The System is stalled during the switch but the PLL clock
system is still running during locking phase.
5. Wait for the ODSWRDY flag in the PWR_CSR to be set.
6. Select the required Flash latency as well as AHB and APB prescalers.
7. Wait for PLL lock.
8. Switch the system clock to the PLL.
9. Enable the peripherals that are not genera ted by the System PLL (I2S clock, LCD-TFT
clock, SAI1 clock, USB_48MHz clock....).
Note: The PLLI2S and PLLSAI can be configured at the same time as the system PLL.
During the Over-drive switch activation, no peripheral clocks should be enabled. The
peripheral clocks must be enabled once the Over-drive mode is activated.
Entering Stop mode disables the Over-drive mode, as well as the PLL. The application
software has to configure again the Over-drive mode and the PLL after exiting from Stop
mode.
Exiting from Over-drive mode
It is recommended to exit from Over-drive mode when the application is not running critical
tasks and when the system clock source is either HSI or HSE.There are two sequences that
allow exiting from over-drive mode:
• By resetting simultaneously the ODEN and ODSW bits bit in the PWR_CR register
(sequence 1)
• By resetting first the ODSW bit to switch the voltage regulator to Normal mode and then
resetting the ODEN bit to disable the Over-drive mode (sequence 2).
Example of sequence 1:
1. Select HSI or HSE as system clock source.
2. Disable the peripheral clocks that are not generated by the System PLL (I2S clock,
LCD-TFT clock, SAI1 clock, USB_48MHz clock,....)
3. Reset simultaneously the ODEN and the ODSW  bits in the PWR_CR register to switch
back the voltage regulator to Normal mode and disable the Over-drive mode.
4. Wait for the ODWRDY flag of PWR_CSR to be reset.

Power controller (PWR) RM0090
124/1741 RM0090 Rev 22
Example of sequence 2:
1. Select HSI or HSE as system clock source.
2. Disable the peripheral clocks that are not generated by the System PLL (I2S clock,
LCD-TFT clock, SAI1 clock, USB_48MHz clock,....).
3. Reset the ODSW bit in the PWR_CR register  to switch back the voltage regulator to
Normal mode. The system clock is stalled during voltage switching.
4. Wait for the ODWRDY flag of PWR_CSR to be reset.
5. Reset the ODEN bit in the PWR_CR register to disable the Over-drive mode.
Note: During step 3, the ODEN bit remains set and the Over-drive mode is still enabled but not
active (ODSW bit is reset). If the ODEN bit is reset instead, the Over-drive mode is disabled
and the voltage regulator is switched back to the initial voltage.
5.2 Power supply supervisor
5.2.1 Power-on reset (POR )/power-down reset (PDR)
The device has an integrated POR/PDR circuitry that allows proper operation starting
from 1.8 V.
The device remains in Reset mode when VDD/VDDA is below a specified threshold,
VPOR/PDR, without the need for an external reset circuit. For more details concerning the
power on/power-down reset threshold, refer to the electrical characteristics of the
datasheet.
[Figure 12](../figures/figure_12.md). Power-on reset/power-down reset waveform
MSv30431V2
VDD/VDDA
40 mV
hysteresis
POR
POR
Reset
Temporization
tRSTTEMPO

RM0090 Rev 22 125/1741
RM0090 Power controller (PWR)
150
5.2.2 Brownout reset (BOR)
During power on, the Brownout reset (BOR) keeps the device under reset until the supply
voltage reaches the specified VBOR threshold.
VBOR is configured through device option bytes. By default, BOR is off. 3 programmable
VBOR threshold levels can be selected:
• BOR Level 3 (VBOR3). Brownout threshold level 3.
• BOR Level 2 (VBOR2). Brownout threshold level 2.
• BOR Level 1 (VBOR1). Brownout threshold level 1.
Note: For full details about BOR char acteristics, refer to the "Electrical characteristics" section in
the device datasheet.
When the supply voltage (VDD) drops below the selected VBOR threshold, a device reset is
generated.
The BOR can be disabled by programming the device option bytes. In this case, the
power-on and power-down is then monitored by the POR/ PDR (see Section 5.2.1: Power-
on reset (POR)/power-down reset (PDR)).
The BOR threshold hysteresis is ~100 mV (between the rising and the falling edge of the
supply voltage).
[Figure 13](../figures/figure_13.md). BOR thresholds
5.2.3 Programmable voltage detector (PVD)
You can use the PVD to monitor the VDD power supply by comparing it to a threshold
selected by the PLS[2:0] bits in the PWR power control register (PWR_CR) for
MS30433V1
VDD/VDDA
100 mV
hysteresis
BOR threshold
Reset

Power controller (PWR) RM0090
126/1741 RM0090 Rev 22
STM32F405xx/07xx and STM32F415xx/17xx and PWR power control register (PWR_CR)
for STM32F42xxx and STM32F43xxx.
The PVD is enabled by setting the PVDE bit.
A PVDO flag is available, in the PWR power control/status register (PWR_CSR)  for
STM32F405xx/07xx and STM32F415xx/17xx, to indicate if VDD is higher or lower than the
PVD threshold. This event is internally connected to the EXTI line 16 and can generate an
interrupt if enabled through the EXTI registers. The PVD output interrupt can be generated
when VDD drops below the PVD threshold and/or when VDD rises above the PVD threshold
depending on EXTI line16 rising/falling edge configuration. As an example the service
routine could perform emergency shutdown tasks.
[Figure 14](../figures/figure_14.md). PVD thresholds
5.3 Low-power modes
By default, the microcontroller is in Run mode after a system or a power-on reset. In Run
mode the CPU is clocked by HCLK and the program code is executed. Several low-power
modes are available to save power when the CPU does not need to be kept running, for
example when waiting for an external event. It is up to the user to select the mode that gives
the best compromise between low-power consumption, short startup time and available
wake-up sources.
The devices feature three low-power modes:
• Sleep mode (Cortex®-M4 with FPU core stopped, peripherals kept running)
• Stop mode (all clocks are stopped)
• Standby mode (1.2 V domain powered off)
MS30432V2
VDD
100 mV
hysteresis
PVD threshold
PVD output

RM0090 Rev 22 127/1741
RM0090 Power controller (PWR)
150
In addition, the power consumption in Run mode can be reduce by one of the following
means:
• Slowing down the system clocks
• Gating the clocks to the APBx and AHBx peripherals when they are unused.
Entering low-power mode
Low-power modes are entered by the MCU by executing the WFI (Wait For Interrupt), or
WFE (Wait for Event) instructions, or when the SLEEPONEXIT bit in the Cortex®-M4 with
FPU System Control register is set on Return from ISR.
Entering Low-power mode through WFI or WFE is executed only if no interrupt is pending or
no event is pending.
Exiting low-power mode
The MCU exits from Sleep and Stop modes low-power mode depending on the way the low-
power mode was entered:
• If the WFI instruction or Return from ISR was used to enter the low-power mode, any
peripheral interrupt acknowledged by the NVIC can wake up the device.
• If the WFE instruction is used to enter the low-power mode, the MCU exits the low-
power mode as soon as an event occurs. The wake-up event can be generated either
by:
– NVIC IRQ interrupt:
When SEVONPEND = 0 in the Cortex®-M4 with FPU System Control register: by
enabling an interrupt in the peripheral control register and in the NVIC. When the
MCU resumes from WFE, the peripheral interrupt pending bit and the NVIC
peripheral IRQ channel pending bit (in the NVIC interrupt clear pending register)
have to be cleared. Only NVIC interrupts with sufficient priority wakes up and
interrupts the MCU.
When SEVONPEND = 1 in the Cortex®-M4 with FPU System Control register: by
enabling an interrupt in the peripheral control register and optionally in the NVIC.
When the MCU resumes from WFE, the peripheral interrupt pending bit and when
enabled the NVIC peripheral IRQ channel pending bit (in the NVIC interrupt clear
pending register) have to be cleared. All NVIC interrupts wakes up the MCU, even
the disabled ones. Only enabled NVIC interrupts with sufficient priority wakes up
and interrupts the MCU.
–E v e n t
This is done by configuring a EXTI line in event mode. When the CPU resumes
from WFE, it is not necessary to clear the EXTI peripheral interrupt pending bit or
the NVIC IRQ channel pending bit as the pending bits corresponding to the event
line is not set. It may be necessary to clear the interrupt flag in the peripheral.
The MCU exits from Standby low-power mode through an external reset (NRST pin), an
IWDG reset, a rising edge on one of the enabled WKUPx pins or a RTC event occurs (see
[Figure 237](../figures/figure_237.md): RTC block diagram).
After waking up from Standby mode, program execution restarts in the same way as after a
Reset (boot pin sampling, option bytes loading, reset vector is fetched, etc.).

Power controller (PWR) RM0090
128/1741 RM0090 Rev 22
Only enabled NVIC interrupts with sufficient priority wakes up and interrupts the MCU.
5.3.1 Slowing dow n system clocks
In Run mode the speed of the system clocks (SYSCLK, HCLK, PCLK1, PCLK2) can be
reduced by programming the prescaler registers. These prescalers can also be used to slow
down peripherals before entering Sleep mode.
For more details refer to Section 7.3.3: RCC clock configuration register (RCC_CFGR).
5.3.2 Peripheral clock gating
In Run mode, the HCLKx and PCLKx for individual peripherals and memories can be
stopped at any time to reduce power consumption.
To further reduce power consumption in Sleep mode the peripheral clocks can be disabled
prior to executing the WFI or WFE instructions.
[Table 24](../tables/table_24.md). Low-power mode summary
Mode name Entry Wake-up Effect on 1.2 V
domain clocks
Effect on
VDD
domain
clocks
Voltage regulator
Sleep
(Sleep now or
Sleep-on-
exit)
WFI or Return
from ISR Any interrupt CPU CLK OFF
no effect on other
clocks or analog
clock sources
None ON
WFE Wake-up event
Stop
PDDS and LPDS
bits +
SLEEPDEEP bit
+ WFI, Return
from ISR or WFE
Any EXTI line (configured
in the EXTI registers,
internal and external lines)
All 1.2 V domain
clocks OFF
HSI and
HSE
oscillator
s OFF
ON or in low- power
mode (depends on
PWR power control
register (PWR_CR)
for
STM32F405xx/07x
x and
STM32F415xx/17x
x and PWR power
control register
(PWR_CR) for
STM32F405xx/07x
x and
STM32F415xx/17x
xPWR power
control register
(PWR_CR) for
STM32F42xxx and
STM32F43xxx
Standby
PDDS bit +
SLEEPDEEP bit
+ WFI, Return
from ISR or WFE
WKUP pin rising edge,
RTC alarm (Alarm A or
Alarm B), RTC Wake-up
event, RTC tamper
events, RTC time stamp
event, external reset in
NRST pin, IWDG reset
OFF

RM0090 Rev 22 129/1741
RM0090 Power controller (PWR)
150
Peripheral clock gating is controlled by the AHB1 peripheral clock enable register
(RCC_AHB1ENR), AHB2 peripheral clock enable register (RCC_AHB2ENR), AHB3
peripheral clock enable register (RCC_AHB3ENR) (see Section 7.3.10: RCC AHB1
peripheral clock enable register (RCC_AHB1ENR), Section 7.3.11: RCC AHB2 peripheral
clock enable register (RCC_AHB2ENR), Section 7.3.12: RCC AHB3 peripheral clock
enable register (RCC_AHB3ENR) for STM32F405xx/07xx and STM32F415xx/17xx, and
Section 6.3.10: RCC AHB1 peripheral clock register (RCC_AHB1ENR), Section 6.3.11:
RCC AHB2 peripheral clock enable register (RCC_AHB2ENR), and Section 6.3.12: RCC
AHB3 peripheral clock enable register (RCC_AHB3ENR) for STM32F42xxx and
STM32F43xxx).
Disabling the peripherals clocks in Sleep mode can be performed automatically by resetting
the corresponding bit in RCC_AHBxLPENR and RCC_APBxLPENR registers.
5.3.3 Sleep mode
Entering Sleep mode
The Sleep mode is entered according to Section : Entering low-power mode, when the
SLEEPDEEP bit in the Cortex®-M4 with FPU System Control register is cleared.
Refer to [Table 25](../tables/table_25.md) and [Table 26](../tables/table_26.md) for details on how to enter Sleep mode.
Note: All interrupt pending bits must be cleared before the sleep mode entry.
Exiting Sleep mode
The Sleep mode is exited according to Section : Exiting low-power mode.
Refer to [Table 25](../tables/table_25.md) and [Table 26](../tables/table_26.md) for more details on how to exit Sleep mode.
[Table 25](../tables/table_25.md). Sleep-now entry and exit
Sleep-now mode Description
Mode entry
WFI (Wait for Interrupt) or WFE (Wait for Event) while:
– SLEEPDEEP = 0, and
– No interrupt (for WFI) or event (for WFE) is pending.
Refer to the Cortex®-M4 with FPU System Control register.
On Return from ISR while:
– SLEEPDEEP = 0 and
– SLEEPONEXIT = 1,
– No interrupt is pending.
Refer to the Cortex®-M4 with FPU System Control register.

Power controller (PWR) RM0090
130/1741 RM0090 Rev 22
5.3.4 Stop mode (STM32F405xx/ 07xx and STM32F415xx/17xx)
The Stop mode is based on the Cortex®-M4 with FPU deepsleep mode combined with
peripheral clock gating. The voltage regulator can be configured either in normal or low-
power mode. In Stop mode, all clocks in the 1.2 V domain are stopped, the PLLs, the HSI
and the HSE RC oscillators are disabled. Internal SRAM and register contents are
preserved.
By setting the FPDS bit in the PWR_CR register, the Flash memory also enters power-down
mode when the device enters Stop mode. When the Flash memory is in power-down mode,
an additional startup delay is incurred when waking up from Stop mode (see [Table 27](../tables/table_27.md): Stop
operating modes  (STM32F405xx/07xx and STM32F415xx/17xx) and Section 5.4.1: PWR
power control register (PWR_CR) for STM32F405xx/07xx and STM32F415xx/17xx).
Mode exit
If WFI or Return from ISR was used for entry:
Interrupt: Refer to [Table 62](../tables/table_62.md): Vector table for STM32F405xx/07xx and
STM32F415xx/17xx and [Table 63](../tables/table_63.md): Vector table for STM32F42xxx and
STM32F43xxx
If WFE was used for entry and SEVONPEND = 0
Wake-up event: Refer to Section 12.2.3: Wake-up event management
f WFE was used for entry and SEVONPEND = 1
Interrupt even when disabled in NVIC: refer to [Table 62](../tables/table_62.md): Vector table for
STM32F405xx/07xx and STM32F415xx/17xx and [Table 63](../tables/table_63.md): Vector table
for STM32F42xxx and STM32F43xxx or Wake-up event (see
Section 12.2.3: Wake-up event management).
Wake-up latency None
[Table 26](../tables/table_26.md). Sleep-on-exit entry and exit
Sleep-on-exit Description
Mode entry
WFI (Wait for Interrupt) or WFE (Wait for Event) while:
– SLEEPDEEP = 0, and
– No interrupt (for WFI) or event (for WFE) is pending.
Refer to the Cortex®-M4 with FPU System Control register.
On Return from ISR while:
– SLEEPDEEP = 0, and
– SLEEPONEXIT = 1, and
– No interrupt is pending.
Refer to the Cortex®-M4 with FPU System Control register.
Mode exit
Interrupt: refer to [Table 62](../tables/table_62.md): Vector table for STM32F405xx/07xx and
STM32F415xx/17xx and [Table 63](../tables/table_63.md): Vector table for STM32F42xxx and
STM32F43xxx
Wake-up latency None
[Table 25](../tables/table_25.md). Sleep-now entry and exit (continued)
Sleep-now mode Description

RM0090 Rev 22 131/1741
RM0090 Power controller (PWR)
150
Entering Stop mode (for STM32F405xx/07xx and STM32F415xx/17xx)
The Stop mode is entered according to Section : Entering low-power mode, when the
SLEEPDEEP bit in the Cortex®-M4 with FPU System Control register is set.
Refer to [Table 28](../tables/table_28.md) for details on how to enter the Stop mode.
To further reduce power consumption in Stop mode, the internal voltage regulator can be put
in low-power mode. This is configured by the LPDS bit of the PWR power control register
(PWR_CR) for STM32F405xx/07xx and STM32F415xx/17xx and PWR power control
register (PWR_CR) for STM32F42xxx and STM32F43xxx.
If Flash memory programming is ongoing, the Stop mode entry is delayed until the memory
access is finished.
If an access to the APB domain is ongoing, The Stop mode entry is delayed until the APB
access is finished.
In Stop mode, the following features can be selected by programming individual control bits:
• Independent watchdog (IWDG): the IWDG is started by writing to its Key register or by
hardware option. Once started it cannot be stopped except by a Reset. See
Section 21.3 in Section 21: Independent watchdog (IWDG).
• Real-time clock (RTC): this is configured by the RTCEN bit in the Section 7.3.20: RCC
Backup domain control register (RCC_BDCR)
• Internal RC oscillator (LSI RC): this is configured by the LSION bit in the
Section 7.3.21: RCC clock control & status register (RCC_CSR).
• External 32.768 kHz oscillator (LSE OSC): this is configured by the LSEON bit in the
Section 7.3.20: RCC Backup domain control register (RCC_BDCR).
The ADC or DAC can also consume power during the Stop mode, unless they are disabled
before entering it. To disable them, the ADON bit in the ADC_CR2 register and the ENx bit
in the DAC_CR register must both be written to 0.
[Table 27](../tables/table_27.md). Stop operating modes
(STM32F405xx/07xx and STM32F415xx/17xx)
Stop mode LPDS bit FPDS bit Wake-up latency
STOP MR
(Main regulator) 0 0 HSI RC startup time
STOP MR-FPD 0 1
HSI RC startup time +
Flash wake-up time from Power
Down mode
STOP LP 1 0
HSI RC startup time +
regulator wake-up time from LP
mode
STOP LP-FPD 1 1
HSI RC startup time +
Flash wake-up time from Power
Down mode +
regulator wake-up time from LP
mode

Power controller (PWR) RM0090
132/1741 RM0090 Rev 22
Note: If the application needs to disable the exte rnal clock before entering Stop mode, the HSEON
bit must first be disabled and the system clock switched to HSI.
Otherwise, if the HSEON bit is kept enabled while the external clock (external oscillator) can
be removed before entering stop mode, the clock security system (CSS) feature must be
enabled to detect any external oscillator failure and avoid a malfunction behavior when
entering stop mode.
Exiting Stop mode (for STM32F405xx/07xx and STM32F415xx/17xx)
The Stop mode is exited according to Section : Exiting low-power mode.
Refer to [Table 28](../tables/table_28.md) for more details on how to exit Stop mode.
When exiting Stop mode by issuing an interrupt or a wake-up event, the HSI RC oscillator is
selected as system clock.
When the voltage regulator operates in low-power mode, an additional startup delay is
incurred when waking up from Stop mode. By keeping the internal regulator ON during Stop
mode, the consumption is higher although the startup time is reduced.
[Table 28](../tables/table_28.md). Stop mode entry and exit (for STM32F405xx/07xx and STM32F415xx/17xx)
Stop mode Description
Mode entry
WFI (Wait for Interrupt) or WFE (Wait for Event) while:
– No interrupt (for WFI) or event (for WFE) is pending,
– SLEEPDEEP bit is set in Cortex®-M4 with FPU System Control register,
– PDDS bit is cleared in Power Control register (PWR_CR),
– Select the voltage regulator mode by configuring LPDS bit in PWR_CR.
On Return from ISR:
– No interrupt is pending,
– SLEEPDEEP bit is set in Cortex®-M4 with FPU System Control register,
– SLEEPONEXIT = 1,
– PDDS bit is cleared in Power Control register (PWR_CR).
Note: To enter Stop mode, all EXTI Line pending bits (in Pending register
(EXTI_PR)), all peripheral interrupts pending bits, the RTC Alarm
(Alarm A and Alarm B), RTC wake-up, RTC tamper, and RTC time
stamp flags, must be reset. Otherwise, the Stop mode entry
procedure is ignored and program execution continues.

RM0090 Rev 22 133/1741
RM0090 Power controller (PWR)
150
5.3.5 Stop mode (STM 32F42xxx and STM32F43xxx)
The Stop mode is based on the Cortex®-M4 with FPU deepsleep mode combined with
peripheral clock gating. The voltage regulator can be configured either in normal or low-
power mode. In Stop mode, all clocks in the 1.2 V domain are stopped, the PLLs, the HSI
and the HSE RC oscillators are disabled. Internal SRAM and register contents are
preserved.
In Stop mode, the power consumption can be further reduced by using additional settings in
the PWR_CR register. However this induces an additional startup delay when waking up
from Stop mode (see [Table 29](../tables/table_29.md)).
Mode exit
If WFI or Return from ISR was used for entry:
Any EXTI lines configured in Interrupt mode (the corresponding EXTI
Interrupt vector must be enabled in the NVIC). The interrupt source can
be external interrupts or peripherals with wake-up capability. Refer to
[Table 62](../tables/table_62.md): Vector table for STM32F405xx/07xx and STM32F415xx/17xx
on page 374 and [Table 63](../tables/table_63.md): Vector table for STM32F42xxx and
STM32F43xxx.
If WFE was used for entry and SEVONPEND = 0
Any EXTI lines configured in event mode. Refer to Section 12.2.3: Wake-
up event management on page 382.
If WFE was used for entry and SEVONPEND = 1:
– Any EXTI lines configured in Interrupt mode (even if the corresponding
EXTI Interrupt vector is disabled in the NVIC). The interrupt source can
be an external interrupt or a peripheral with wake-up capability. Refer to
[Table 62](../tables/table_62.md): Vector table for STM32F405xx/07xx and STM32F415xx/17xx
on page 374 and [Table 63](../tables/table_63.md): Vector table for STM32F42xxx and
STM32F43xxx.
– Wake-up event: refer to Section 12.2.3: Wake-up event management on
page 382.
Wake-up latency [Table 27](../tables/table_27.md): Stop operating modes  (STM32F405xx/07xx and
STM32F415xx/17xx)
[Table 28](../tables/table_28.md). Stop mode entry and exit (for STM32F405xx/07xx and STM32F415xx/17xx)
Stop mode Description

Power controller (PWR) RM0090
134/1741 RM0090 Rev 22
Entering Stop mode (STM32F42xxx and STM32F43xxx)
The Stop mode is entered according to Section : Entering low-power mode, when the
SLEEPDEEP bit in the Cortex®-M4 with FPU System Control register is set.
Refer to [Table 30](../tables/table_30.md) for details on how to enter the Stop mode.
When the microcontroller enters in Stop mode, the voltage scale 3 is automatically selected.
To further reduce power consumption in Stop mode, the internal voltage regulator can be put
in low voltage mode. This is configured by the LPDS, MRUDS, LPUDS and UDEN bits of
the PWR power control register (PWR_CR) for STM32F405xx/07xx and
STM32F415xx/17xx.
If Flash memory programming is ongoing, the Stop mode entry is delayed until the memory
access is finished.
If an access to the APB domain is ongoing, The Stop mode entry is delayed until the APB
access is finished.
If the Over-drive mode was enabled before entering Stop mode, it is automatically disabled
during when the Stop mode is activated.
[Table 29](../tables/table_29.md). Stop operating modes (STM32F42xxx and STM32F43xxx)
Voltage Regulator Mode UDEN[1:0]
bits
MRUDS
bit
LPUDS
bit
LPDS
bit
FPDS
bit Wake-up latency
Normal
mode
STOP MR
(Main Regulator)  - 0  - 0 0 HSI RC startup time
STOP MR- FPD  - 0  - 0 1
HSI RC startup time +
Flash wake-up time from power-
down mode
STOP LP  - 0 0 1 0
HSI RC startup time +
regulator wake-up time from LP
mode
STOP LP-FPD  -  - 0 1 1
HSI RC startup time +
Flash wake-up time from power-
down mode +
regulator wake-up time from LP
mode
Under-
drive
Mode
STOP UMR-
FPD 3 1  - 0  -
HSI RC startup time +
Flash wake-up time from power-
down mode +
Main regulator wake-up time from
under-drive mode + Core logic to
nominal mode
STOP ULP-FPD 3  - 1 1  -
HSI RC startup time +
Flash wake-up time from power-
down mode +
regulator wake-up time from LP
under-drive mode + Core logic to
nominal mode

RM0090 Rev 22 135/1741
RM0090 Power controller (PWR)
150
In Stop mode, the following features can be selected by programming individual control bits:
• Independent watchdog (IWDG): the IWDG is started by writing to its Key register or by
hardware option. Once started it cannot be stopped except by a Reset. See
Section 21.3 in Section 21: Independent watchdog (IWDG).
• Real-time clock (RTC): this is configured by the RTCEN bit in the Section 7.3.20: RCC
Backup domain control register (RCC_BDCR)
• Internal RC oscillator (LSI RC): this is configured by the LSION bit in the
Section 7.3.21: RCC clock control & status register (RCC_CSR).
• External 32.768 kHz oscillator (LSE OSC): this is configured by the LSEON bit in the
RCC Backup domain control register (RCC_BDCR).
The ADC or DAC can also consume power during the Stop mode, unless they are disabled
before entering it. To disable them, the ADON bit in the ADC_CR2 register and the ENx bit
in the DAC_CR register must both be written to 0.
Note: Before entering Stop mode, it is recommended to enable the clock security system (CSS)
feature to prevent external oscillator (HSE) failure from impacting the internal MCU
behavior.
Exiting Stop mode (STM32F42xxx and STM32F43xxx)
The Stop mode is exited according to Section : Exiting low-power mode.
Refer to [Table 30](../tables/table_30.md) for more details on how to exit Stop mode.
When exiting Stop mode by issuing an interrupt or a wake-up event, the HSI RC oscillator is
selected as system clock.
If the Under-drive mode was enabled, it is automatically disabled after exiting Stop mode.
When the voltage regulator operates in low voltage mode, an additional startup delay is
incurred when waking up from Stop mode. By keeping the internal regulator ON during Stop
mode, the consumption is higher although the startup time is reduced.
When the voltage regulator operates in Under-drive mode, an additional startup delay is
induced when waking up from Stop mode.

Power controller (PWR) RM0090
136/1741 RM0090 Rev 22
5.3.6 Standby mode
The Standby mode allows to achieve the lowest power consumption. It is based on the
Cortex®-M4 with FPU deepsleep mode, with the voltage regulator disabled. The 1.2 V
domain is consequently powered off. The PLLs, the HSI oscillator and the HSE oscillator are
also switched off. SRAM and register contents are lost except for registers in the backup
domain (RTC registers, RTC backup register and backup SRAM), and Standby circuitry (see
[Figure 9](../figures/figure_9.md)).
[Table 30](../tables/table_30.md). Stop mode entry and exit (STM32F42xxx and STM32F43xxx)
Stop mode Description
Mode entry
WFI (Wait for Interrupt) or WFE (Wait for Event) while:
– No interrupt or event is pending,
– SLEEPDEEP bit is set in Cortex®-M4 with FPU System Control register,
– PDDS bit is cleared in Power Control register (PWR_CR),
– Select the voltage regulator mode by configuring LPDS, MRUDS, LPUDS
and UDEN bits in PWR_CR (see [Table 29](../tables/table_29.md): Stop operating modes
(STM32F42xxx and STM32F43xxx)).
On Return from ISR while:
– No interrupt is pending,
– SLEEPDEEP bit is set in Cortex®-M4 with FPU System Control register,
and
– SLEEPONEXIT = 1, and
– PDDS is cleared in PWR_CR1.
Note: To enter Stop mode, all EXTI Line pending bits (in Pending register
(EXTI_PR)), all peripheral interrupts pending bits, the RTC Alarm
(Alarm A and Alarm B), RTC wake-up, RTC tamper, and RTC time
stamp flags, must be reset. Otherwise, the Stop mode entry
procedure is ignored and program execution continues.
Mode exit
If WFI or Return from ISR was used for entry:
All EXTI lines configured in Interrupt mode (the corresponding EXTI
Interrupt vector must be enabled in the NVIC). The interrupt source can
be external interrupts or peripherals with wake-up capability. Refer to
[Table 62](../tables/table_62.md): Vector table for STM32F405xx/07xx and STM32F415xx/17xx
on page 374.
If WFE was used for entry and SEVONPEND = 0:
All EXTI Lines configured in event mode. Refer to Section 12.2.3: Wake-
up event management on page 382
If WFE was used for entry and SEVONPEND = 1:
– Any EXTI lines configured in Interrupt mode (even if the corresponding
EXTI Interrupt vector is disabled in the NVIC). The interrupt source can
be external interrupts or peripherals with wake-up capability. Refer to
[Table 62](../tables/table_62.md): Vector table for STM32F405xx/07xx and STM32F415xx/17xx
on page 374 and [Table 63](../tables/table_63.md): Vector table for STM32F42xxx and
STM32F43xxx.
– Wake-up event: refer to Section 12.2.3: Wake-up event management on
page 382.
Wake-up latency Refer to [Table 29](../tables/table_29.md): Stop operating modes (STM32F42xxx and
STM32F43xxx)

RM0090 Rev 22 137/1741
RM0090 Power controller (PWR)
150
Entering Standby mode
The Standby mode is entered according to Section : Entering low-power mode, when the
SLEEPDEEP bit in the Cortex®-M4 with FPU System Control register is set.
Refer to [Table 31](../tables/table_31.md) for more details on how to enter Standby mode.
In Standby mode, the following features can be selected by programming individual control
bits:
• Independent watchdog (IWDG): the IWDG is started by writing to its Key register or by
hardware option. Once started it cannot be stopped except by a reset. See
Section 21.3 in Section 21: Independent watchdog (IWDG).
• Real-time clock (RTC): this is configured by the RTCEN bit in the backup domain
control register (RCC_BDCR)
• Internal RC oscillator (LSI RC): this is configured by the LSION bit in the Control/status
register (RCC_CSR).
• External 32.768 kHz oscillator (LSE OSC): this is configured by the LSEON bit in the
backup domain control register (RCC_BDCR)
Exiting Standby mode
The Standby mode is exited according to Section : Exiting low-power mode. The SBF status
flag in PWR_CR (see Section 5.4.2: PWR power control/status register (PWR_CSR)  for
STM32F405xx/07xx and STM32F415xx/17xx) indicates that the MCU was in Standby
mode. All registers are reset after wake-up from Standby except for PWR_CR.
Refer to [Table 31](../tables/table_31.md) for more details on how to exit Standby mode.
[Table 31](../tables/table_31.md). Standby mode entry and exit
Standby mode Description
Mode entry
WFI (Wait for Interrupt) or WFE (Wait for Event) while:
– SLEEPDEEP is set in Cortex®-M4 with FPU System Control register,
– PDDS bit is set in Power Control register (PWR_CR),
– No interrupt (for WFI) or event (for WFE) is pending,
– WUF bit is cleared in Power Control register (PWR_CR),
– the RTC flag corresponding to the chosen wake-up source (RTC Alarm
A, RTC Alarm B, RTC wake-up, Tamper or Timestamp flags) is cleared
On return from ISR while:
– SLEEPDEEP bit is set in Cortex®-M4 with FPU System Control register,
and
– SLEEPONEXIT = 1, and
– PDDS bit is set in Power Control register (PWR_CR), and
– No interrupt is pending,
– WUF bit is cleared in Power Control/Status register (PWR_SR),
– The RTC flag corresponding to the chosen wake-up source (RTC Alarm
A, RTC Alarm B, RTC wake-up, Tamper or Timestamp flags) is cleared.
Mode exit WKUP pin rising edge, RTC alarm (Alarm A and Alarm B), RTC wake-up,
tamper event, time stamp event, external reset in NRST pin, IWDG reset.
Wake-up latency Reset phase.

Power controller (PWR) RM0090
138/1741 RM0090 Rev 22
I/O states in Standby mode
In Standby mode, all I/O pins are high impedance except for:
• Reset pad (still available)
• RTC_AF1 pin (PC13) if configured for tamper, time stamp, RTC Alarm out, or RTC
clock calibration out
• WKUP pin (PA0), if enabled
Debug mode
By default, the debug connection is lost if the application puts the MCU in Stop or Standby
mode while the debug features are used. This is due to the fact that the Cortex®-M4 with
FPU core is no longer clocked.
However, by setting some configuration bits in the DBGMCU_CR register, the software can
be debugged even when using the low-power modes extensively. For more details, refer to
Section 38.16.1: Debug support for low-power modes.
5.3.7 Programming the RTC alternate f unctions to wake up the device from
the Stop and Standby modes
The MCU can be woken up from a low-power mode by an RTC alternate function.
The RTC alternate functions are the RTC alarms (Alarm A and Alarm B), RTC wake-up,
RTC tamper event detection and RTC time stamp event detection.
These RTC alternate functions can wake up the system from the Stop and Standby low-
power modes.
The system can also wake up from low-power modes without depending on an external
interrupt (Auto-wake-up mode), by using the RTC alarm or the RTC wake-up events.
The RTC provides a programmable time base for waking up from the Stop or Standby mode
at regular intervals.
For this purpose, two of the three alternate RTC clock sources can be selected by
programming the RTCSEL[1:0] bits in the Section 7.3.20: RCC Backup domain control
register (RCC_BDCR):
• Low-power 32.768 kHz external crystal oscillator (LSE OSC)
This clock source provides a precise time base with a very low-power consumption
(additional consumption of less than 1 µA under typical conditions)
• Low-power internal RC oscillator (LSI RC)
This clock source has the advantage of saving the cost of the 32.768 kHz crystal. This
internal RC oscillator is designed to use minimum power.

RM0090 Rev 22 139/1741
RM0090 Power controller (PWR)
150
RTC alternate functions to wake up the device from the Stop mode
• To wake up the device from the Stop mode with an RTC alarm event, it is necessary to:
a) Configure the EXTI Line 17 to be sensitive to rising edges (Interrupt or Event
modes)
b) Enable the RTC Alarm Interrupt in the RTC_CR register
c) Configure the RTC to generate the RTC alarm
• To wake up the device from the Stop mode with an RTC tamper or time stamp event, it
is necessary to:
a) Configure the EXTI Line 21 to be sensitive to rising edges (Interrupt or Event
modes)
b) Enable the RTC time stamp Interrupt in the RTC_CR register or the RTC tamper
interrupt in the RTC_TAFCR register
c) Configure the RTC to detect the tamper or time stamp event
• To wake up the device from the Stop mode with an RTC wake-up event, it is necessary
to:
a) Configure the EXTI Line 22 to be sensitive to rising edges (Interrupt or Event
modes)
b) Enable the RTC wake-up in terrupt in the RTC_CR register
c) Configure the RTC to generate the RTC Wake-up event
RTC alternate functions to wake up the device from the Standby mode
• To wake up the device from the Standby mode with an RTC alarm event, it is necessary
to:
a) Enable the RTC alarm inte rrupt in the RTC_CR register
b) Configure the RTC to generate the RTC alarm
• To wake up the device from the Standby mode with an RTC tamper or time stamp
event, it is necessary to:
a) Enable the RTC time stamp interrupt in the RTC_CR register or the RTC tamper
interrupt in the RTC_TAFCR register
b) Configure the RTC to detect the tamper or time stamp event
• To wake up the device from the Standby mode with an RTC wake-up event, it is
necessary to:
a) Enable the RTC wake-up in terrupt in the RTC_CR register
b) Configure the RTC to generate the RTC wake-up event
Safe RTC alternate function wake-up flag clearing sequence
If the selected RTC alternate function is set before the PWR wake-up flag (WUTF) is
cleared, it is not detected on the next event as detection is made once on the rising edge.
To avoid bouncing on the pins onto which the RTC alternate functions are mapped, and exit
correctly from the Stop and Standby modes, it is recommended to follow the sequence
below before entering the Standby mode:
• When using RTC alarm to wake up the device from the low-power modes:
a) Disable the RTC alarm interrupt (ALRAIE or ALRBIE bits in the RTC_CR register)
b) Clear the RTC alarm (ALRAF/ALRBF) flag

Power controller (PWR) RM0090
140/1741 RM0090 Rev 22
c) Clear the PWR Wake-up (WUF) flag
d) Enable the RTC alarm interrupt
e) Re-enter the low-power mode
• When using RTC wake-up to wake up the device from the low-power modes:
a) Disable the RTC Wake-up interrupt (WUTIE bit in the RTC_CR register)
b) Clear the RTC Wake-up (WUTF) flag
c) Clear the PWR Wake-up (WUF) flag
d) Enable the RTC Wake-up interrupt
e) Re-enter the low-power mode
• When using RTC tamper to wake up the device from the low-power modes:
a) Disable the RTC tamper interrupt (TAMPIE bit in the RTC_TAFCR register)
b) Clear the Tamper (TAMP1F/TSF) flag
c) Clear the PWR Wake-up (WUF) flag
d) Enable the RTC tamper interrupt
e) Re-enter the low-power mode
• When using RTC time stamp to wake up the device from the low-power modes:
a) Disable the RTC time stamp interrupt (TSIE bit in RTC_CR)
b) Clear the RTC time stamp (TSF) flag
c) Clear the PWR Wake-up (WUF) flag
d) Enable the RTC TimeStamp interrupt
e) Re-enter the low-power mode

RM0090 Rev 22 141/1741
RM0090 Power controller (PWR)
150
5.4 Power control registers  (STM32F405xx/07xx and
STM32F415xx/17xx)
5.4.1 PWR power control register (PWR_CR)
for STM32F405xx/07xx and STM32F415xx/17xx
Address offset: 0x00
Reset value: 0x0000 4000 (reset by wake-up from Standby mode)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Reserved
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res.
VOS
Reserved
FPDS DBP PLS[2:0] PVDE CSBF CWUF PDDS LPDS
rw rw rw rw rw rw rw w w rw rw
Bits 31:15 Reserved, must be kept at reset value.
Bit 14 VOS: Regulator voltage scaling output selection
This bit controls the main internal voltage regulator output voltage to achieve a trade-off
between performance and power consumption when the device does not operate at the
maximum frequency.
0: Scale 2 mode
1: Scale 1 mode (default value at reset)
Bits 13:10 Reserved, must be kept at reset value.
Bit 9 FPDS: Flash power-down in Stop mode
When set, the Flash memory enters power-down mode when the device enters Stop mode.
This allows to achieve a lower consumption in stop mode but a longer restart time.
0: Flash memory not in power-down when the device is in Stop mode
1: Flash memory in power-down when the device is in Stop mode
Bit 8 DBP: Disable backup domain write protection
In reset state, the RCC_BDCR register, the RTC registers (including the backup registers),
and the BRE bit of the PWR_CSR register, are protected against parasitic write access. This
bit must be set to enable write access to these registers.
0: Access to RTC and RTC Backup registers and backup SRAM disabled
1: Access to RTC and RTC Backup registers and backup SRAM enabled
Note: Depending on the APB1 prescaler, there is a delay between writing to DBP and the
effective disabling/enabling of the backup domain protection. Therefore, a dummy read
operation to the PWR_CR register is required just after writing to the DBP bit.

Power controller (PWR) RM0090
142/1741 RM0090 Rev 22
5.4.2 PWR power control/st atus register (PWR_CSR)
for STM32F405xx/07xx and STM32F415xx/17xx
Address offset: 0x04
Reset value: 0x0000 0000 (not reset by wake-up from Standby mode)
Additional APB cycles are needed to read this register versus a standard APB read.
Bits 7:5 PLS[2:0]: PVD level selection
These bits are written by software to select the voltage threshold detected by the
programmable voltage detector
000: 2.0 V
001: 2.1 V
010: 2.3 V
011: 2.5 V
100: 2.6 V
101: 2.7 V
110: 2.8 V
111: 2.9 V
Note: Refer to the electrical characteristics of the datasheet for more details.
Bit 4 PVDE: Programmable voltage detector enable
This bit is set and cleared by software.
0: PVD disabled
1: PVD enabled
Bit 3 CSBF: Clear standby flag
This bit is always read as 0.
0: No effect
1: Clear the SBF Standby Flag (write).
Bit 2 CWUF: Clear wake-up flag
This bit is always read as 0.
0: No effect
1: Clear the WUF Wake-up Flag after 2 System clock cycles
Bit 1 PDDS: Power-down deepsleep
This bit is set and cleared by software. It works together with the LPDS bit.
0: Enter Stop mode when the CPU enters deepsleep. The regulator status depends on the
LPDS bit.
1: Enter Standby mode when the CPU enters deepsleep.
Bit 0 LPDS: Low-power deepsleep
This bit is set and cleared by software. It works together with the PDDS bit.
0: Voltage regulator on during Stop mode
1: Voltage regulator in low-power mode during Stop mode
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Reserved
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res
VOS
RDY Reserved
BRE EWUP
Reserved
BRR PVDO SBF WUF
r r w r w rrrr

RM0090 Rev 22 143/1741
RM0090 Power controller (PWR)
150
Bits 31:15 Reserved, must be kept at reset value.
Bit 14 VOSRDY: Regulator voltage scaling output selection ready bit
0: Not ready
1: Ready
Bits 13:10 Reserved, must be kept at reset value.
Bit 9 BRE: Backup regulator enable
When set, the Backup regulator (used to maintain backup SRAM content in Standby and
VBAT modes) is enabled. If BRE is reset, the backup regulator is switched off. The backup
SRAM can still be used but its content is lost in the Standby and VBAT modes. Once set, the
application must wait that the Backup Regulator Ready flag (BRR) is set to indicate that the
data written into the RAM is maintained in the Standby and VBAT modes.
0: Backup regulator disabled
1: Backup regulator enabled
Note: This bit is not reset when  the device wakes up from Standby mode, by a system reset,
or by a power reset. This bit is reset by a backup domain reset.
The DBP bit of the PWR_CR register must be set before BRE can be written.
Bit 8 EWUP: Enable WKUP pin
This bit is set and cleared by software.
0: WKUP pin is used for general purpose I/O. An event on the WKUP pin does not wake up
the device from Standby mode.
1: WKUP pin is used for wake-up from Standby mode and forced in input pull down
configuration (rising edge on WKUP pin wakes-up the system from Standby mode).
Note: This bit is reset by a system reset.
Bits 7:4 Reserved, must be kept at reset value.
Bit 3 BRR: Backup regulator ready
Set by hardware to indicate that the Backup Regulator is ready.
0: Backup Regulator not ready
1: Backup Regulator ready
Note: This bit is not reset when the device wake s up from Standby mode or by a system reset
or power reset. This bit is reset by a backup domain reset.
Bit 2 PVDO: PVD output
This bit is set and cleared by hardware. It is valid only if PVD is enabled by the PVDE bit.
0: VDD is higher than the PVD threshold selected with the PLS[2:0] bits.
1: VDD is lower than the PVD threshold selected with the PLS[2:0] bits.
Note: The PVD is stopped by Standby mode. For this reason, this bit is equal to 0 after
Standby or reset until the PVDE bit is set.
Bit 1 SBF: Standby flag
This bit is set by hardware and cleared only by a POR/PDR (power-on reset/power-down
reset) or by setting the CSBF bit in the PWR_CR register.
0: Device has not been in Standby mode
1: Device has been in Standby mode

Power controller (PWR) RM0090
144/1741 RM0090 Rev 22
Bit 0 WUF: Wake-up flag
This bit is set by hardware and cleared either by a system reset or by setting the CWUF bit in
the PWR_CR register.
0: No wake-up event occurred
1: A wake-up event was received from the WKUP pin or from the RTC alarm (Alarm A or
Alarm B), RTC Tamper event, RTC TimeStamp event or RTC Wake-up).
Note: An additional wake-up event is detected if the WKUP pin is enabled (by setting the
EWUP bit) when the WKUP pin level is already high.

RM0090 Rev 22 145/1741
RM0090 Power controller (PWR)
150
5.5 Power control registers (STM32F42xxx and STM32F43xxx)
5.5.1 PWR power control register (PWR_CR)
for STM32F42xxx and STM32F43xxx
Address offset: 0x00
Reset value: 0x0000 C000 (reset by wake-up from Standby mode)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Reserved
UDEN[1:0] ODSWE
N ODEN
rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
VOS[1:0] ADCDC1
Res.
MRUDS LPUDS FPDS DBP PLS[2:0] PVDE CSBF CWUF PDDS LPDS
rw rw rw rw rw rw rw rw rw rw rw rc_w1 rc_w1 rw rw
Bits 31:20 Reserved, must be kept at reset value.
Bits 19:18 UDEN[1:0]: Under-drive enable in stop mode
These bits are set by software. They allow to achieve a lower power consumption in Stop
mode but with a longer wake-up time.
When set, the digital area has less leakage consumption when the device enters Stop mode.
00: Under-drive disable
01: Reserved
10: Reserved
11:Under-drive enable
Bit 17 ODSWEN: Over-drive switching enabled.
This bit is set by software. It is cleared automatically by hardware after exiting from Stop
mode or when the ODEN bit is reset. When set, It is used to switch to Over-drive mode.
To set or reset the ODSWEN bit, the HSI or HSE must be selected as system clock.
The ODSWEN bit must only be set when the ODRDY flag is set to switch to Over-drive
mode.
0: Over-drive switching disabled
1: Over-drive switching enabled
Note: On any over-drive switch (enabled or disabled), the system clock is stalled during the
internal voltage set up.
Bit 16 ODEN: Over-drive enable
This bit is set by software. It is cleared automatically by hardware after exiting from Stop
mode. It is used to enabled the Over-drive mode in order to reach a higher frequency.
To set or reset the ODEN bit, the HSI or HSE must be selected as system clock. When the
ODEN bit is set, the application must first wait for the Over-drive ready flag (ODRDY) to be
set before setting the ODSWEN bit.
0: Over-drive disabled
1: Over-drive enabled

Power controller (PWR) RM0090
146/1741 RM0090 Rev 22
Bits 15:14 VOS[1:0]: Regulator voltage scaling output selection
These bits control the main internal voltage regulator output voltage to achieve a trade-off
between performance and power consumption when the device does not operate at the
maximum frequency (refer to the STM32F42xx and STM32F43xx datasheets for more
details).
These bits can be modified only when the PLL is OFF. The new value programmed is active
only when the PLL is ON. When the PLL is OFF, the voltage scale 3 is automatically
selected.
00: Reserved (Scale 3 mode selected)
01: Scale 3 mode
10: Scale 2 mode
11: Scale 1 mode (reset value)
Bit 13 ADCDC1:
0: No effect.
1: Refer to AN4073 for details on how to use this bit.
Note: This bit can only be set when operating at supply voltage range 2.7 to 3.6V and when
the Prefetch is OFF.
Bit 12 Reserved, must be kept at reset value.
Bit 11 MRUDS: Main regulator in deepsleep under-drive mode
This bit is set and cleared by software.
0: Main regulator ON when the device is in Stop mode
1: Main Regulator in under-drive mode and Flash memory in power-down when the device is
in Stop under-drive mode.
Bit 10 LPUDS: Low-power regulator in deepsleep under-drive mode
This bit is set and cleared by software.
0: Low-power regulator ON if LPDS bit is set when the device is in Stop mode
1: Low-power regulator in under-drive mode if LPDS bit is set and Flash memory in power-
down when the device is in Stop under-drive mode.
Bit 9 FPDS: Flash power-down in Stop mode
When set, the Flash memory enters power-down mode when the device enters Stop mode.
This allows to achieve a lower consumption in stop mode but a longer restart time.
0: Flash memory not in power-down when the device is in Stop mode
1: Flash memory in power-down when the device is in Stop mode
Bit 8 DBP: Disable backup domain write protection
In reset state, the RCC_BDCR register, the RTC registers (including the backup registers),
and the BRE bit of the PWR_CSR register, are protected against parasitic write access. This
bit must be set to enable write access to these registers.
0: Access to RTC and RTC Backup registers and backup SRAM disabled
1: Access to RTC and RTC Backup registers and backup SRAM enabled

RM0090 Rev 22 147/1741
RM0090 Power controller (PWR)
150
Bits 7:5 PLS[2:0]: PVD level selection
These bits are written by software to select the voltage threshold detected by the
programmable voltage detector
000: 2.0 V
001: 2.1 V
010: 2.3 V
011: 2.5 V
100: 2.6 V
101: 2.7 V
110: 2.8 V
111: 2.9 V
Note: Refer to the electrical characteristics of the datasheet for more details.
Bit 4 PVDE: Programmable voltage detector enable
This bit is set and cleared by software.
0: PVD disabled
1: PVD enabled
Bit 3 CSBF: Clear standby flag
This bit is always read as 0.
0: No effect
1: Clear the SBF Standby Flag (write).
Bit 2 CWUF: Clear wake-up flag
This bit is always read as 0.
0: No effect
1: Clear the WUF Wake-up Flag after 2 System clock cycles
Bit 1 PDDS: Power-down deepsleep
This bit is set and cleared by software. It works together with the LPDS bit.
0: Enter Stop mode when the CPU enters deepsleep. The regulator status depends on the
LPDS bit.
1: Enter Standby mode when the CPU enters deepsleep.
Bit 0 LPDS: Low-power deepsleep
This bit is set and cleared by software. It works together with the PDDS bit.
0:Main voltage regulator ON during Stop mode
1: Low-power voltage regulator ON during Stop mode

Power controller (PWR) RM0090
148/1741 RM0090 Rev 22
5.5.2 PWR power control/st atus register (PWR_CSR)
for STM32F42xxx and STM32F43xxx
Address offset: 0x04
Reset value: 0x0000 0000 (not reset by wake-up from Standby mode)
Additional APB cycles are needed to read this register versus a standard APB read.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Reserved
UDRDY[1:0] ODSWRDY ODRDY
rc_w1 rc_w1 r r
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res
VOS
RDY Reserved
BRE EWUP
Reserved.
BRR PVDO SBF WUF
rr w r wr r r r
Bits 31:20 Reserved, must be kept at reset value.
Bits 19:18 UDRDY[1:0]: Under-drive ready flag
These bits are set by hardware when MCU entered stop Under-drive mode and exited.
When the under-drive mode is enabled, these bits are not set as long as the MCU has not
entered stop mode yet. They are cleared by programming them to 1.
00: Under-drive is disabled
01: Reserved
10: Reserved
11:Under-drive mode is activated in Stop mode.
Bit 17 ODSWRDY: Over-drive mode switching ready
0: Over-drive mode is not active.
1: Over-drive mode is active on digital area on 1.2 V domain
Bit 16 ODRDY: Over-drive mode ready
0: Over-drive mode not ready.
1: Over-drive mode ready
Bit 14 VOSRDY: Regulator voltage scaling output selection ready bit
0: Not ready
1: Ready
Bits 13:10 Reserved, must be kept at reset value.
Bit 9 BRE: Backup regulator enable
When set, the Backup regulator (used to maintain backup SRAM content in Standby and
VBAT modes) is enabled. If BRE is reset, the backup regulator is switched off. The backup
SRAM can still be used but its content is lost in the Standby and VBAT modes. Once set, the
application must wait that the Backup Regulator Ready flag (BRR) is set to indicate that the
data written into the RAM is maintained in the Standby and VBAT modes.
0: Backup regulator disabled
1: Backup regulator enabled
Note: This bit is not reset when  the device wakes up from Standby mode, by a system reset,
or by a power reset. This bit is reset by a backup domain reset.
The DBP bit of the PWR_CR register must be set before BRE can be written.

RM0090 Rev 22 149/1741
RM0090 Power controller (PWR)
150
Bit 8 EWUP: Enable WKUP pin
This bit is set and cleared by software.
0: WKUP pin is used for general purpose I/O. An event on the WKUP pin does not wake up
the device from Standby mode.
1: WKUP pin is used for wake-up from Standby mode and forced in input pull down
configuration (rising edge on WKUP pin wakes-up the system from Standby mode).
Note: This bit is reset by a system reset.
Bits 7:4 Reserved, must be kept at reset value.
Bit 3 BRR: Backup regulator ready
Set by hardware to indicate that the Backup Regulator is ready.
0: Backup Regulator not ready
1: Backup Regulator ready
Note: This bit is not reset when the device wake s up from Standby mode or by a system reset
or power reset. This bit is reset by a backup domain reset.
Bit 2 PVDO: PVD output
This bit is set and cleared by hardware. It is valid only if PVD is enabled by the PVDE bit.
0: VDD is higher than the PVD threshold selected with the PLS[2:0] bits.
1: VDD is lower than the PVD threshold selected with the PLS[2:0] bits.
Note: The PVD is stopped by Standby mode. For this reason, this bit is equal to 0 after
Standby or reset until the PVDE bit is set.
Bit 1 SBF: Standby flag
This bit is set by hardware and cleared only by a POR/PDR (power-on reset/power-down
reset) or by setting the CSBF bit in the PWR power control register (PWR_CR) for
STM32F405xx/07xx and STM32F415xx/17xx
0: Device has not been in Standby mode
1: Device has been in Standby mode
Bit 0 WUF: Wake-up flag
This bit is set by hardware and cleared either by a system reset or by setting the CWUF bit in
the PWR_CR register.
0: No wake-up event occurred
1: A wake-up event was received from the WKUP pin or from the RTC alarm (Alarm A or
Alarm B), RTC Tamper event, RTC TimeStamp event or RTC Wake-up).
Note: An additional wake-up event is detected if the WKUP pin is enabled (by setting the
EWUP bit) when the WKUP pin level is already high.

Power controller (PWR) RM0090
150/1741 RM0090 Rev 22
5.6 PWR register map
The following table summarizes the PWR registers.
Refer to Section 2.3: Memory map for the register boundary addresses.
[Table 32](../tables/table_32.md). PWR - register map and reset values for
STM32F405xx/07xx and STM32F415xx/17xx
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
0x000 PWR_CR Reserved
VOSReserved
FPDS
DBP
PLS[2:0]
PVDE
CSBF
CWUF
PDDS
LPDS
R e s e t  v a l u e 1 0000000000
0x004 PWR_CSR Reserved
VOSRDY
Reserved
BRE
EWUPReserved
BRR
PVDO
SBF
WUF
R e s e t  v a l u e 0 00 0000
[Table 33](../tables/table_33.md). PWR - register map and reset values for STM32F42xxx and STM32F43xxx
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
0x000 PWR_CR Reserved
UDEN[1:0]
ODSWEN
ODEN
VOS[1:0]
ADCDC1
Reserved
MRUDS
LPUDS
FPDS
DBP
PLS[2:0]
PVDE
CSBF
CWUF
PDDS
LPDS
R e s e t  v a l u e 0000110 000000000000
0x004 PWR_CSR Reserved
UDRDY[1:0]
ODSWRDY
ODRDY
Reserved
VOSRDY
Reserved
BRE
EWUPReserved
BRR
PVDO
SBF
WUF
R e s e t  v a l u e 0000 0 00 0000
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 9: Architectural Diagram](../figures/figure_9.md)
* [Figure 10: Architectural Diagram](../figures/figure_10.md)
* [Figure 11: Architectural Diagram](../figures/figure_11.md)
* [Figure 12: Architectural Diagram](../figures/figure_12.md)
* [Figure 13: Architectural Diagram](../figures/figure_13.md)
* [Figure 14: Architectural Diagram](../figures/figure_14.md)
* [Figure 237: Architectural Diagram](../figures/figure_237.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 23: Configuration Matrix](../tables/table_23.md)
* [Table 24: Configuration Matrix](../tables/table_24.md)
* [Table 25: Configuration Matrix](../tables/table_25.md)
* [Table 26: Configuration Matrix](../tables/table_26.md)
* [Table 27: Configuration Matrix](../tables/table_27.md)
* [Table 28: Configuration Matrix](../tables/table_28.md)
* [Table 29: Configuration Matrix](../tables/table_29.md)
* [Table 30: Configuration Matrix](../tables/table_30.md)
* [Table 31: Configuration Matrix](../tables/table_31.md)
* [Table 32: Configuration Matrix](../tables/table_32.md)
* [Table 33: Configuration Matrix](../tables/table_33.md)
* [Table 38: Configuration Matrix](../tables/table_38.md)
* [Table 62: Configuration Matrix](../tables/table_62.md)
* [Table 63: Configuration Matrix](../tables/table_63.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)