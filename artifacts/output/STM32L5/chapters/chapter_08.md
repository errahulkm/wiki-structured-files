# Chapter 8: Power control (PWR)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 8: Power control (PWR).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 259 - 322
* **Taxonomy Section**: SYSTEM
* **Parent IP Module**: [Power Control (PWR)](../system/pwr.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 259/2187
RM0438 Power control (PWR)
322
8 Power control (PWR)
The power controller (PWR) main features are:
• Power supplies and supply domains
– Core domains (VCORE)
– VDD domain
– Backup domain (VBAT)
– Analog domain (VDDA)
– Supply for the SMPS power stage (available on SMPS packages)
– VDDIO2 domain on Port G
– VDDUSB for USB transceiver
• System supply voltage regulation
– SMPS step down converter
– Voltage regulator (LDO)
– External SMPS mode
• Power supply supervision
– POR/PDR monitor
– BOR monitor
–P V D  m o n i t o r
– PVM monitor (VDDA, VDDUSB, VDDIO2)
– Temperature threshold monitor
– Upper VDD voltage threshold monitor
• Power management
– Operating modes
– Voltage scaling control
– Low-power modes
• VBAT battery charging
• TrustZone security
8.1 Power supplies and supply domains
The STM32L552xx and STM32L562xx devices require a 1.71 V to 3.6 V operating supply
voltage (VDD). Several peripherals are supplied through independent power domains: VDDA,
VDDIO2, VDDUSB. Those supplies must not be provided without a valid operating supply on
the VDD pin.
• VDD = 1.71 V to 3.6 V
VDD is the external power supply for the I/Os, the internal regulator (or the SMPS step
down converter depending on the device) and the system analog such as reset, power
management and internal clocks. It is provided externally through VDD pins.
• VDDA = 1.62 V (ADCs/COMPs) / 1.8 V (DACs/OPAMPs) / 2.4 V (VREFBUF) to 3.6 V
VDDA is the external analog power supply for A/D converters, D/A converters, voltage
reference buffer, operational amplifiers and comparators. The VDDA voltage level is
independent from the VDD voltage. VDDA should be preferably connected to VDD when

Power control (PWR) RM0438
260/2187 RM0438 Rev 8
these peripherals are not used.
• VDDSMPS = 2 V to 3.6 V
VDDSMPS is the external power supply for the SMPS step down converter. It is
provided externally through VDDSMPS supply pin, and shall be connected to the same
supply as VDD.
• VLXSMPS is the switched SMPS step down converter output.
• V15SMPS are the power supply for the system regulator. It is provided externally through
the SMPS step down converter VLXSMPS output.
Note: The SMPS power supply pins are availabl e only on a specific package with SMPS step
down converter option.
• VDD12 = 1.05 to 1.32 V
VDD12 is the external power supply bypassing the internal regulator when connected
to an external SMPS. It is provided externally through VDD12 pins and only available
on packages with the external SMPS supply option. VDD12 does not require any
external decoupling capacitance and cannot support any external load.
Note: The VDD12 power supply pins are available onl y on a specific package with external SMPS
option.
• VDDUSB = 3.0 V to 3.6 V
VDDUSB is the external independent power supply for USB transceivers. The VDDUSB
voltage level is independent from the VDD voltage. VDDUSB should be preferably
connected to VDD when the USB is not used.
The VDDUSB power supply may not be present as a dedicated pin, but to be internally
bonded to VDD. For such devices, VDD has to respect the VDDUSB supply range when
the USB is used.
• VDDIO2 = 1.08 V to 3.6 V
VDDIO2 is the external power supply for 14 I/Os (Port G[15:2]). The VDDIO2 voltage level
is independent from the VDD voltage and should preferably be connected to VDD when
PG[15:2] are not used.
• VBAT = 1.55 V to 3.6 V
VBAT is the power supply for RTC, external clock 32 kHz oscillator and backup registers
(through power switch) when VDD is not present. VBAT is internally bonded to VDD for
small packages without dedicated pin.
• VREF-, VREF+
VREF+ is the input reference voltage for ADCs and DACs. It is also the output of the
internal voltage reference buffer when enabled.
When VDDA < 2 V, VREF+ must be equal to VDDA.
When VDDA > 2 V, VREF+ must be between 2 V and VDDA.
VREF+ can be grounded when ADC and DAC are not active.
The internal voltage reference buffer supports two output voltages, which are
configured with VRS bit in the VREFBUF_CSR register:
–V REF+ around 2.048 V. This requires VDDA equal to or higher than 2.4 V.
–V REF+ around 2.5 V. This requires VDDA equal to or higher than 2.8 V.
On some packages, VREF- and VREF+ pins are not available. When not available on
the package, they are internally bonded to respectively VSSA and VDDA.

RM0438 Rev 8 261/2187
RM0438 Power control (PWR)
322
When the VREF+ is double-bonded with VDDA in a package, the internal voltage
reference buffer is not available and must be kept disable (refer to related device
datasheet for packages pinout description).
VREF- must always be equal to VSSA.
In the STM32L552xx and STM32L562xx devices, the I/Os, the embedded LDO regulator
and the system analog peripherals (such as PLLs and reset block) are fed by VDD supply
source. The embedded linear voltage regulator is used to supply the internal digital power
VCORE. VCORE is the power supply for digital peripherals and memories.
[Figure 21](../figures/figure_21.md). STM32L552xx and STM32L562xx power supply overview
1. V CORE is provided by either MR or LPR, depending on the operating power mode.
MSv49301V2
VDDA domain
Backup domain
2 x D/A converters
2 x A/D converters
Standby circuitry
(Wakeup logic,
IWDG)
Low voltage detector
LSE crystal 32 K osc
BKP registers
RCC BDCR register
RTC
2 x comparators
2 x operational amplifiers
Voltage reference buffer
I/O ring
Temp. sensor
Reset block
3 x PLL, HSI, MSI
USB transceivers
VDDUSB
VDDIO2
VDDIO1
I/O ring
VDDIO2
VDDA
VSSA
VSS
VSS
VDDIO2 domain
VDD domain
VCORE
(1)
VSS
VDD
VBAT
SPMS LPR
MR
unused block
VCORE domain
VCORE domain
Core
SRAM1
SRAM2
Digital
peripherals
Flash memory

Power control (PWR) RM0438
262/2187 RM0438 Rev 8
In the STM32L552xxxP and STM32L562xxxP devices, the I/Os and system analog
peripherals (such as PLLs, and reset block) are fed by VDD supply source. The VCORE,
power supply for digital peripherals and memories is generated from external SMPS.
[Figure 22](../figures/figure_22.md). STM32L552xxxP and STM32L562xxxP power supply overview
1. If the selected package has the external SMPS option but  no external SMPS is used by the application (the
embedded LDO is used instead), the VDD12 pins are kept unconnected.
2. VDD12 is intended to be connected with external SMPS (switched-mode power supply) to generate the
VCORE logic supply in Run, Sleep and Stop 0 modes only.
MSv49336V2
VDDA domain
Backup domain
2 x D/A converters
2 x A/D converters
Standby circuitry
(Wakeup logic,
IWDG)
Low voltage detector
LSE crystal 32 K osc
BKP registers
RCC BDCR register
RTC
2 x comparators
2 x operational amplifiers
Voltage reference buffer
I/O ring
Temp. sensor
Reset block
3 x PLL, HSI, MSI
USB transceivers
VDDUSB
VDDIO2
VDDIO1
I/O ring
VDDIO2
VDDA
VSSA
VSS
VSS
VDDIO2 domain
VDD domain
VCORE
VSS
VDD
VBAT
SMPS LPR
MR
2x VDD12(1)(2)
VCORE domain
Core
SRAM1
SRAM2
Digital
peripherals
Flash memory
unused blocks

RM0438 Rev 8 263/2187
RM0438 Power control (PWR)
322
In the STM32L552xxxQ and STM32L562xxxQ devices, the I/Os, the embedded SMPS step
down converter and the system analog peripherals (such as PLLs and reset block) are fed
by VDD supply source. The embedded linear main voltage regulator that provides the VCORE
supply for digital peripherals and memories is fed by the SMSP step down converter output.
[Figure 23](../figures/figure_23.md). STM32L552xxxQ and STM32L562xxxQ power supply overview
1. Refer to [Figure 24](../figures/figure_24.md) for SMPS step down converter power supply scheme.
2. During Low-power sleep, Low-power run, Stop 1, Stop 2, Standby and Shutdown modes, the SMPS step
down converter is switched to Open mode. In Low-power sleep, Low-power run, Stop 1, Stop 2 and
Standby with SRAM2 retention modes, the low-power regulator is used to provide the VCORE.
The SMPS is used in Run, Sleep and Stop 0 modes. It supplies the main regulator which provides the
VCORE.
Note: If the selected package has the SMPS step down converter option but the SMPS is not used
by the application (and the embedded LDO is used instead), it is recommended to set the
SMPS power supply pins as follows:
- VDDSMPS and VLXSMPS connected to VSS
- V15SMPSconnected to VDD.
MSv49332V2
VDDA domain
Backup domain
2 x D/A converters
2 x A/D converters
Standby circuitry
(Wakeup logic,
IWDG)
Low voltage detector
LSE crystal 32 K osc
BKP registers
RCC BDCR register
RTC
2 x comparators
2 x operational amplifiers
Voltage reference buffer
I/O ring
VCORE domain
Temp. sensor
Reset block
3 x PLL, HSI, MSI
USB transceivers
VDDUSB
VDDIO2
VDDIO1
I/O ring
VDDIO2
VDDA
VSSA
VSS
VSS
VDDIO2 domain
VDD domain
VCORE
VSS
VDD
VBAT
SMPS
(1)(2) LPR
VLXSMPS
MR
VSSSMPS
2 x V15SMPS
VDDSMPS
VCORE domain
Core
SRAM1
SRAM2
Digital
peripherals
Flash memory

Power control (PWR) RM0438
264/2187 RM0438 Rev 8
8.1.1 Independent analog peripherals supply
To improve ADC and DAC conversion accuracy and to extend the supply flexibility, the
analog peripherals have an independent power supply which can be separately filtered and
shielded from noise on the PCB.
• The analog peripherals voltage supply input is available on a separate VDDA pin.
• An isolated supply ground connection is provided on VSSA pin.
The VDDA supply voltage can be different from VDD. The presence of VDDA must be checked
before enabling any of the analog peripherals supplied by VDDA (A/D converter, D/A
converter, comparators, operational amplifiers, voltage reference buffer).
The VDDA supply can be monitored by the peripheral voltage monitoring (PVM), and
compared with two thresholds (1.65 V for PVM3 or 1.8 V for PVM4), refer to Section 8.3.3:
Peripheral voltage monitoring (PVM) for more details.
When a single supply is used, VDDA can be externally connected to VDD through the
external filtering circuit in order to ensure a noise-free VDDA reference voltage.
ADC and DAC reference voltage
To ensure a better accuracy on low-voltage inputs and outputs, the user can connect to
VREF+ a separate reference voltage lower than VDDA. VREF+ is the highest voltage,
represented by the full scale value, for an analog input (ADC) or output (DAC) signal.
VREF+ can be provided either by an external reference of by an internal buffered voltage
reference (VREFBUF).
The internal voltage reference is enabled by setting the ENVR bit in the Section 23.4.1:
VREFBUF control and status register (VREFBUF_CSR). The voltage reference is set to
2.5 V when the VRS bit is set and to 2.048 V when the VRS bit is cleared. The internal
voltage reference can also provide the voltage to external components through VREF+ pin.
Refer to the device datasheet and to Section 23: Voltage reference buffer (VREFBUF) for
further information.
8.1.2 Independent I/O supply rail
Some I/Os from port G (PG[15:2]) are supplied from a separate supply rail. The power
supply for this rail can range from 1.08 V to 3.6 V and is provided externally through the
VDDIO2 pin. The VDDIO2 voltage level is completely independent from VDD or VDDA. The
VDDIO2 pin is available only for some packages. Refer to the pinout diagrams or tables in the
related device datasheet(s) for I/O list(s).
After reset, the I/Os supplied by VDDIO2 are logically and electrically isolated and therefore
are not available. The isolation must be removed before using any I/O from PG[15:2], by
setting the IOSV bit in the PWR_CR2 register, once the VDDIO2 supply is present.
The VDDIO2 supply is monitored by the peripheral voltage monitoring (PVM2) and compared
with the internal reference voltage (3/4 VREFINT, around 0.9V), refer to Section 8.3.3:
Peripheral voltage monitoring (PVM) for more details.
8.1.3 Independent USB transceivers supply
The USB transceivers are supplied from a separate VDDUSB power supply pin. VDDUSB
range is from 3.0 V to 3.6 V and is completely independent from VDD or VDDA.

RM0438 Rev 8 265/2187
RM0438 Power control (PWR)
322
After reset, the USB features supplied by VDDUSB are logically and electrically isolated and
therefore are not available. The isolation must be removed before using the USB peripheral,
by setting the USV bit in the PWR_CR2 register, once the VDDUSB supply is present.
The VDDUSB supply is monitored by the peripheral voltage monitoring (PVM1) and
compared with the internal reference voltage (VREFINT, around 1.2 V), refer to Section 8.3.3:
Peripheral voltage monitoring (PVM) for more details.
8.1.4 Battery backup domain
To retain the content of the backup registers and supply the RTC function when VDD is
turned off, the VBAT pin can be connected to an optional backup voltage supplied by a
battery or by another source.
The VBAT pin powers the RTC unit, the LSE oscillator and the PC13 to PC15 I/Os, allowing
the RTC to operate even when the main power supply is turned off. The switch to the VBAT
supply is controlled by the power-down reset embedded in the Reset block.
Warning: During tRSTTEMPO (temporization at VDD startup) or after a PDR
has been detected, the power switch between VBAT and VDD
remains connected to VBAT.
During the startup phase, if VDD is established in less than
tRSTTEMPO (refer to the datasheet for the value of tRSTTEMPO)
and VDD > VBAT + 0.6 V, a current may be injected into VBAT
through an internal diode connected between VDD and the
power switch (VBAT).
If the power supply/battery connected to the VBAT pin cannot
support this current injection, it is strongly recommended to
connect an external low-drop diode between this power
supply and the VBAT pin.
If no external battery is used in the application, it is recommended to connect VBAT to VDD
supply and add a 100 nF ceramic decoupling capacitor on VBAT pin.
When the backup domain is supplied by VDD (analog switch connected to VDD), the
following pins are available:
• PC13, PC14 and PC15, which can be used as GPIO pins
• PC13, PC14 and PC15, which can be configured by RTC or LSE (refer to Section 41.3:
RTC functional description on page 1396)
• PA0/TAMP_IN2/TAMP_OUT1 and PE6/TAMP_IN3/TAMP_OUT6 when they are
configured by the tamper as tamper pins
Note: Due to the fact that the analog switch can transfer only a limited amount of current (3  mA),
the use of GPIO PC13 to PC15 in Output mode is restricted: the speed has to be limited to
2 MHz with a maximum load of 30 pF and these I/Os must not be used as a current source
(for example to drive a LED).
When the backup domain is supplied by VBAT (analog switch connected to VBAT because
VDD is not present), the following functions are available:
• PC13, PC14 and PC15 can be controlled only by RTC or LSE (refer to Section 41.3:

Power control (PWR) RM0438
266/2187 RM0438 Rev 8
RTC functional description)
• PA0/TAMP_IN2 and PE6/TAMP_IN3 when they are configured by the tamper as
tamper pins
Backup domain access
After a system reset, the backup domain (RTC registers and backup registers) is protected
against possible unwanted write accesses. To enable access to the backup domain,
proceed as follows:
1. Enable the power interface clock by setting the PWREN bits in the Section 9.8.13: RCC
APB1 peripheral reset register 1 (RCC_APB1RSTR1)
2. Set the DBP bit in the Power control register 1 (PWR_CR1) to enable access to the
backup domain
3. Select the RTC clock source in the RCC Backup domain control register (RCC_BDCR).
4. Enable the RTC clock by setting the RTCEN [15] bit in the RCC Backup domain control
register (RCC_BDCR).
VBAT battery charging
When VDD is present, It is possible to charge the external battery on VBAT through an
internal resistance.
The VBAT charging is done either through a 5 kOhm resistor or through a 1.5 kOhm resistor
depending on the VBRS bit value in the PWR_CR4 register.
The battery charging is enabled by setting VBE bit in the PWR_CR4 register. It is
automatically disabled in VBAT mode.
8.2 System supply voltage regulation
8.2.1 Voltage regulator
Two embedded linear voltage regulators supply all the digital circuitries, except for the
Standby circuitry and the backup domain. The main regulator output voltage (VCORE) can be
programmed by software to three different power ranges (Range 0, Range 1 and Range 2)
in order to optimize the consumption depending on the system’s maximum operating
frequency (refer to Section 9.3.10: Clock source frequency versus voltage scaling and to
Section 6.3.3: Read access latency).
At power-on reset or a system reset, the main regulator voltage Range 2 is selected by
default.
The voltage regulators are always enabled after a reset. Depending on the application
modes, the VCORE supply is provided either by the main regulator (MR) or by the low-power
regulator (LPR).
• In Run, Sleep and Stop 0 modes, both regulators are enabled and the main regulator
(MR) supplies full power to the VCORE domain (core, memories and digital peripherals).
• In Low-power run and Low-power sleep modes, the main regulator is off and the low-
power regulator (LPR) supplies low power to the VCORE domain, preserving the
contents of the registers, SRAM1 and SRAM2.
• In Stop 1 and Stop 2 modes, the main regulator is off and the low-power regulator
(LPR) supplies low-power to the VCORE domain, preserving the contents of the

RM0438 Rev 8 267/2187
RM0438 Power control (PWR)
322
registers, SRAM1and SRAM2.
• In Standby mode, the SRAM2 content can be fully or partially (only 4 Kbytes) preserved
(depending on RRS[1:0] bits in the PWR_CR3 register), the main regulator (MR) is off
and the low-power regulator (LPR) provides the supply to SRAM2 only. The core,
digital peripherals (except Standby circuitry and backup domain) and SRAM1 are
powered off.
• In Standby mode, both regulators are powered off. The contents of the registers,
SRAM1 and SRAM2 is lost except for the Standby circuitry and the backup domain.
• In Shutdown mode, both regulators are powered off. When exiting from Shutdown
mode, a power-on reset is generated. Consequently, the contents of the registers, all
SRAMs is lost, except for the backup domain.
8.2.2 Embedded SMPS step down converter
The built-in SMPS step down converter is a power-efficient DC/DC non-linear switching
regulator that improves low-power performance when the VDD voltage is high enough. The
SMPS step down converter automatically enters in Bypass mode when the VDD voltage falls
below a VDD minimum value following the selected voltage range and switched back to the
selected operating mode when VDD rises above the minimum value.
When the SMPS step down converter is enabled, it can be configured in:
• High-power mode (HPM): achieving a high efficiency at high current load.
SMPS high-power mode is used in all ranges (0, 1 and 2).
It is the default selected mode after POR reset.
• Low-power mode (LPM): achieving a high efficiency at low current load.
When enabled, the voltage scaling must not be modified. This mode shall be only
selected in Range 2 and when power consumption does not exceed 30 mA.
• Bypass mode:
When the Bypass mode is enabled, the SMPS step down converter is switched OFF
and it is possible to change the voltage scaling. This mode can be forced by software
by setting the SMPSBYP bit in PWR_CR4 register. The Bypass mode can be enabled
or disabled on the fly at any time by the application software whatever the selected
operation mode.
In Range 0 and Range 1, the SMPS Bypass mode is selected automatically when VDD
drops below 2.05 V.
In Range 2, if VDD is less than 2.05 V, the SMPS Bypass mode must be forced by
software. For this purpose, the PVD0 should monitor the VDD power supply and the
software must force bypass mode by setting the SMPSBYP bit in PWR_CR4 register.
The following table summarizes the SMPS behavior depending on the main regulator
range, VDD and consumption.

Power control (PWR) RM0438
268/2187 RM0438 Rev 8
Refer to [Table 63](../tables/table_63.md) for SMPS step down converter operating mode.
The sequence to go from Low-power to High-power mode is:
1. Clearing the SMPSLPEN bit in the PWR_CR4 register
2. Check that the SMPSHPRDY flag is set in PWR_SR1 register
The sequence to go from High-power to Low-power mode is:
1. Configure the system frequency and voltage scaling
2. Set the SMPSLPEN bit in the PWR_CR4 register
Note: If the Bypass mode is active and the SMPSL PEN bit is set, the switch to SMPS Low-power
mode is delayed until the SMPS step down converter exits the Bypass mode.
Note: The SMPS step down converter operating mode and Voltage scaling range selection shall
be changed only in RUN mode.
8.2.3 SMPS step down converter power supply scheme
The SMPS step down converter requires an external coil with typical value of 4.7 µH to be
connected between the dedicated VLXSMPS pin to VSSSMPS via a capacitor of 4.7µF. It is
switched OFF when:
• LPREG is used
or
• SMPS is configured in Bypass mode by software in RUN/SLEEP modes (SMPSBYP bit
set in PWR_CR4).
[Table 62](../tables/table_62.md). SMPS modes summary
Ranges Max AHB clock V CORE
SMPS mode
VDD ≤ 2.05 V V DD > 2.05 V
Range 0 110 MHz 1.28 V Automatic Bypass mode
V15SMPS = VDD
HP mode
Max current consumption = 120 mA
V15SMPS = 1.6 V
Range 1 80 MHz 1.2 V Automatic Bypass mode
V15SMPS = VDD
HP mode
Max current consumption = 80 mA
V15SMPS = 1.5 V
Range 2 26 MHz 1.0 V Software Bypass mode(1)
V15SMPS = VDD
LP mode or HP mode
Max current consumption = 30 mA
V15SMPS = 1.3 V
1. There is no automatic SMPS bypass in Range 2. T he user application should use PVD0 to monitor VDD supply and request
the SMPS Bypass mode.
[Table 63](../tables/table_63.md). SMPS step down converter operating mode
SMPSBYP bit SMPSLPEN bit SM PSHPRDY flag Description
0 0 1 High-power mode
0 1 0 Low-power mode
1 x x Bypass mode

RM0438 Rev 8 269/2187
RM0438 Power control (PWR)
322
Thus, only main regulator is used by the application.
Refer to [Figure 24](../figures/figure_24.md) below.
[Figure 24](../figures/figure_24.md). SMPS step down converter power supply scheme
If the selected package is with the SMPS step down converter option but it is never used by
the application, it is mandatory to set the SMPS power supply pins as follows:
• VDDSMPS and VLXSMPS connected to VSS
• V15SMPSconnected to VDD
8.2.4 SMPS step down conver ter versus low-power mode
The SMPS step down converter operating mode depends on the selected operating and
upon the system operating modes (LP)Run, (LP)Sleep, Stop 0, Stop 1, Stop 2, Standby, and
Shutdown.
During Stop 1, Stop 2, Standby and Shutdown modes the SMPS step down converter is
switched to Open mode (see [Table 64](../tables/table_64.md)). When exiting from low-power modes (except
Shutdown) the SMPS step down converter is set by hardware to the mode selected prior to
the low-power mode selection. The SMPS step down converter mode configuration bits in
PWR_CR4 (SMPSLEN or SMPSBYP) are retained in Standby mode.
After POR reset, the SMPS step down converter is in High-power mode.
Note: It is recommended to enable the SMPS bypass mode prior entering Stop modes in order to
reduce the wake up time.
MSv49346V2
Main
regulator
VDDSMPS
VLXSMPS
VDD SMPS
Step Down
Converter
VSSSMPS
V15SMPS
VCORE
V15SMPS
VDD
VSS
[Table 64](../tables/table_64.md). SMPS step down converter versus low-power modes
System operating mode SMPS step down
converter state Description
Run, Sleep ON
SMPS in HPM or LPM mode and, in ranges
0/1 it switches to Bypass mode following
VDD minimum value versus the selected
voltage range
Stop 0 ON SMPS in HPM or LPM mode
Stop 1, Stop 2, Low power run,
Low power sleep,
Standby with SRAM2 retention
Open SMPS is bypassed, LPR regulator is used
Standby and Shutdown Open SMPS is bypassed

Power control (PWR) RM0438
270/2187 RM0438 Rev 8
Note: If the Bypass mode is requested, entering St op 1 or Stop 2 or Low-power run or Low-power
sleep modes shall be delayed until the SMPS BYPASS ready flag SMPSBYPRDY is set.
Note: In Low-power run mode, the following bits  shall not be modified (PWR_CR4: SMPSLPEN,
SMPSFSTEN, SMPSBYP).
SMPS step down converter fast startup
After POR reset, the SMPS step down converter starts in High-power mode and in Slow-
startup mode. The low-startup feature is selected to limit the inrush current after power-on
reset.
However, it is possible to configure a faster startup on the fly and it is applied for next SMPS
startup (after a wakeup from low-power mode - except Shutdown and VBAT modes) or for
next SMPS output voltage change (Bypass or VOS change). The fast startup is selected by
setting the SMPSFSTEN bit in the PWR_CR4 register.
Note: Setting the SMPSFSTEN bit in the PWR_CR4 re gister allows also a faster switch to Bypass
mode (i.e. V15SMPS reaching VDD).
Note: The timing needed for Bypass mode to be  effective (i.e. SMPSBYPRDY flag is set) is
counted starting from V15 already at target value (1.3V (Range 2); 1.5V (Range 1); 1.6V
(Range 0)). This timing is determined by the parameter V15 slew rate, depending itself on
the fact that fast startup is enabled or disabled. Refer to the device datasheet.
8.2.5 Dynamic voltag e scaling management
The dynamic voltage scaling is a power management technique which consists in
increasing or decreasing the voltage used for the digital peripherals (VCORE), according to
the application performance and power consumption needs.
Dynamic voltage scaling to increase VCORE is known as overvolting. It allows the device to
improve its performance.
Dynamic voltage scaling to decrease VCORE is known as undervolting. It is performed to
save power, particularly in laptop and other mobile devices where the energy comes from a
battery and is thus limited.
The main regulator operates in the following ranges:
• Main regulator Range 0: high performance;
It provides a typical output voltage at 1.28 V. It is used when the system clock
frequency is up to 110 MHz. The flash access time for read access is minimum, write
and erase operations are possible.
• Main regulator Range 1: medium performance;
It provides a typical output voltage at 1.2 V. It is used when the system clock frequency
is up to 80 MHz. The flash access time for read access is minimum, write and erase
operations are possible.
• Main regulator Range 2: low-power range.
It provides a typical output voltage at 1.0 V. The system clock frequency can be up to
26 MHz.The flash access time for a read access is increased as compared to Range 1;
write and erase operations are not possible.
Voltage scaling is selected through the VOS[1:0] bits in the PWR_CR1 register. The main
regulator voltage Range 2 is selected by default.
Note: In Low-power run mode, the VOS[1:0] must not be modified.

RM0438 Rev 8 271/2187
RM0438 Power control (PWR)
322
Voltage scaling and SMPS step down converter
When the SMPS step down converter is selected, the VOS[1:0] bits must not be modified
when the SMPS is in a low-power mode.
When the voltage scaling is updated, the SMPS step down converter output voltage is
scaled automatically following the selected voltage range.
The sequence to go from Range 0 /Range 1 to Range 2 is:
1. In case of switching from Range 0 to Range 2, the system clock must be divided
by 2 using the AHB prescaler before switching to a lower system frequency for at
least 1 us and then reconfigure the AHB prescaler.
2. Reduce the system frequency to a value lower than 26 MHz.
3. Adjust number of wait states according new frequency target in Range 2
(LATENCY bits in the FLASH_ACR).
4. Program the VOS[1:0] bits to “10” in the PWR_CR1 register.
The sequence to go from Range 2 to Range 1/Range 0 is:
1. Program the VOS[1:0] bits to “01” in the PWR_CR1 register.
2. Wait until the VOSF flag is cleared in the PWR_SR2 register.
3. Adjust number of wait states according new frequency target in Range 0 or
Range 1 (LATENCY bits in the FLASH_ACR).
4. Increase the system frequency by following below procedure:
– If the system frequency is 26 MHz < SYSCLK <= 80 MHz:
- Configure and switch to PLL for a new system frequency.
– If the system frequency is SYSCLK > 80 MHz:
- The system clock must be divided by 2 using the AHB prescaler before switching
to a higher system frequency.
- Configure and switch to PLL for a new system frequency.
- Wait for at least 1us and then reconfigure the AHB prescaler to get the needed
HCLK clock frequency.
The sequence to switch from Range 1 to Range 0 is:
1. The system clock must be divided by 2 using the AHB prescaler before switching
to a higher system frequency.
2. Adjust the number of wait states according to the new frequency target in range1
3. Configure and switch to new system frequency.
4. Wait for at least 1us and then reconfigure the AHB prescaler to get the needed
HCLK clock frequency.
The sequence to switch from Range 0 boost mode to Range 1 mode is:
1. Adjust the number of wait states according to the new frequency target in Range 0
default mode
2. Configure and switch to new system frequency.
8.2.6 VDD12 domain and external SMPS
VDD12 is intended to be connected with external SMPS (switched-mode power supply) to
generate the VCORE logic supply in Run, Sleep and Stop 0 modes only.

Power control (PWR) RM0438
272/2187 RM0438 Rev 8
VDD12 pins correspond to the internal VCORE powering the digital part of Core, RAMs,
FLASH and peripherals. This significantly improves the power consumption with a gain from
50% or more depending of the external SMPS performances.
The main benefit occurs in Run and Sleep modes whereas in Stop 0 mode, the gain is less
significant.
The figure below shows a schematic to understand how the internal regulator stops
supplying VCORE when an external voltage VDD12 is provided.
As VDD12 shares the same pin as output of the internal regulator, applying a slightly higher
voltage (typically +50 mV) on the VDD12 blocks, the PMOS and the regulator consumption
is negligible.
[Figure 25](../figures/figure_25.md). Internal main regulator overview
A switch, controlled by the chosen GPIO, is inserted between the external SMPS output and
VDD12.
There are two possible states:
• Connected: Switch is closed so external SMPS powers VDD12
• Disconnected: Switch is open and VDD12 is disconnected from external SMPS output
Proper software management through GPIOs to enable/disable external SMPS and to
connect/disconnect external SMPS through the switch, is required to conform with the rules
described below. See also Section 8.2.5: Dynamic voltage scaling management.
MSv44809V1
Ref
Vsmps
Switch PMOS
Voltage regulator
VDD
VDD12
VCORE

RM0438 Rev 8 273/2187
RM0438 Power control (PWR)
322
It is mandatory to respect the following rules to avoid any damage or instability on either
digital parts or internal regulators:
• In Run, Sleep and Stop 0 modes, VDD12 can be connected and should respect
– VDD12 < 1.32 V
– VDD12 ≥ VCORE + 50 mV giving for main regulator
Range 0, VCORE =1.28 V so VDD12 should be greater than 1.33 V, but this cannot
match previous rule VDD12 < 1.32 V, so it is not a functional use case with an
external SMPS.
Range 1, VCORE = 1.2 V so VDD12 should be greater than 1.25 V.
Range 2, VCORE = 1.0 V so VDD12 should be greater than 1.05 V
– VDD12 ≥ 1.08 V in Range 1 when 80 MHz ≥ SYSCLK frequency ≥ 26 MHz
– VDD12 ≥ 1.14 V in Range 0 when SYSCLK frequency > 80 MHz
• In all other modes, such as LPRun, LPSleep, Stop 1, Stop 2, Standby and Shutdown
modes, VDD12 must be disconnected from external SMPS output. This means that the
pin must be connected to a high impedance output:
– VDD12 connected to HiZ (voltage is provided by internal regulators)
• Transitions of VDD12 from connected to disconnected is only allowed when SYSCLK
frequency ≤ 26 MHz to avoid to big voltage drop on main regulator side.
Note: In case of asynchronous reset while having the V DD12 ≤ 1.25 V, VDD12 should switch to HiZ
in less than regulator switching time from Range 2 to Range 1 (~1 us).
Note: V DD12 Range 2 is extended down to 1.00 V for better efficiency, thus following formula
applies when bit EXTSMPSEN in the Power control register 4 (PWR_CR4) is set:
Range 2, VCORE = 0.95 V so VDD12 should be greater than 1.00 V
Note: For more details on V DD12 management, refer to AN4978 “Design recommendations for
STM32L4xxxx with external SMPS, for ultra-low-power applications with high performance”.
8.3 Power supply supervision
8.3.1 Power-on reset (POR) / power-down reset (PDR) /
brown-out reset (BOR)
The device has an integrated power-on reset (POR) / power-down reset (PDR), coupled
with a brown-out reset (BOR) circuitry. The BOR is active in all power modes except
Shutdown mode, and cannot be disabled.
Five BOR thresholds can be selected through option bytes.
During power-on, the BOR keeps the device under reset until the supply voltage VDD
reaches the specified VBORx threshold. When VDD drops below the selected threshold, a
device reset is generated. When VDD is above the VBORx upper limit, the device reset is
released and the system can start.
For more details on the brown-out reset thresholds, refer to the electrical characteristics
section in the datasheet.
During Stop 2 and Standby modes, it is possible to set the BOR in Ultra-low-power mode to
further reduce the current consumption by setting the ULPMEN bit in PWR_CR3 register.

Power control (PWR) RM0438
274/2187 RM0438 Rev 8
For Stop 2 mode, the BOR Ultra-low-power mode can be set if the BORH is set, otherwise
there is no power consumption optimization.
[Figure 26](../figures/figure_26.md). Brown-out reset waveform
1. The reset temporization t RSTTEMPO is present only for the BOR lowest threshold (VBOR0).
8.3.2 Programmable voltage detector (PVD)
The user can use the PVD to monitor the VDD power supply by comparing it to a threshold
selected by the PLS[2:0] bits in the Power control register 2 (PWR_CR2).
The PVD is enabled by setting the PVDE bit.
A PVDO flag is available, in the Power status register 2 (PWR_SR2), to indicate if VDD is
higher or lower than the PVD threshold. This event is internally connected to the EXTI line16
and can generate an interrupt if enabled through the EXTI registers. The rising/falling edge
sensitivity of the EXTI line16 is configured to rising edge sensitivity, the interrupt is
generated when VDD drops below the PVD threshold. As an example, the service routine
can perform emergency shutdown tasks.
[Figure 27](../figures/figure_27.md). PVD thresholds
MS31444V5
VBOR0 (rising edge)
hysteresis
Temporization
tRSTTEMPO
Reset
VDD
VBOR0 (falling edge)
MS31445V2
PVD output
V        thresholdPVD
V              DD
100 mV
hysteresis

RM0438 Rev 8 275/2187
RM0438 Power control (PWR)
322
8.3.3 Peripheral volt age monitoring (PVM)
Only VDD is monitored by default, as it is the only supply required for all system-related
functions. The other supplies (VDDA, VDDIO2 and VDDUSB) can be independent from VDD
and can be monitored with four peripheral voltage monitoring (PVM).
Each of the four PVMx (x=1, 2, 3, 4) is a comparator between a fixed threshold VPVMx and
the selected power supply. PVMOx flags indicate if the independent power supply is higher
or lower than the PVMx threshold: PVMOx flag is cleared when the supply voltage is above
the PVMx threshold, and is set when the supply voltage is below the PVMx threshold.
Each PVM output is connected to an EXTI line and can generate an interrupt if enabled
through the EXTI registers. The PVMx output interrupt is generated when the independent
power supply drops below the PVMx threshold and/or when it rises above the PVMx
threshold, depending on EXTI line rising/falling edge configuration.
Each PVM can remain active in Stop 0, Stop 1 and Stop 2 modes, and the PVM interrupt
can wake up from the Stop mode.
The independent supplies (VDDA, VDDIO2 and VDDUSB) are not considered as present by
default, and a logical and electrical isolation is applied to ignore any information coming
from the peripherals supplied by these dedicated supplies.
• If these supplies are shorted externally to VDD, the application should assume they are
available without enabling any peripheral voltage monitoring.
• If these supplies are independent from VDD, the peripheral voltage monitoring (PVM)
can be enabled to confirm whether the supply is present or not.
The following sequence must be done before using the USB peripheral:
1. If V DDUSB is independent from VDD:
a) Enable the PVM1 by setting PVME1 bit in the Power control register 2
(PWR_CR2).
b) Wait for the PVM1 wakeup time.
c) Wait until PVMO1 bit is cleared in the Power status register 2 (PWR_SR2).
d) Optional: Disable the PVM1 for consumption saving.
2. Set the USV bit in the Power control register 2 (PWR_CR2) to remove the VDDUSB
power isolation.
The following sequence must be done before using any I/O from PG[15:2]:
[Table 65](../tables/table_65.md). PVM features
PVM Power supply PVM threshold EXTI line
PVM1 V DDUSB VPVM1 (around 1.2 V) 35
PVM2 V DDIO2 VPVM2 (around 0.9 V) 36
PVM3 V DDA VPVM3 (around 1.65 V) 37
PVM4 V DDA VPVM4 (around 1.8 V) 38

Power control (PWR) RM0438
276/2187 RM0438 Rev 8
1. If V DDIO2 is independent from VDD:
a) Enable the PVM2 by setting PVME2 bit in the Power control register 2
(PWR_CR2).
b) Wait for the PVM2 wakeup time.
c) Wait until PVMO2 bit is cleared in the Power control register 2 (PWR_CR2).
d) Optional: Disable the PVM2 for consumption saving.
2. Set the IOSV bit in the Power control register 2 (PWR_CR2) to remove the VDDIO2
power isolation.
The following sequence must be done before using any of these analog peripherals: analog
to digital converters, digital to analog converters, comparators, operational amplifiers,
voltage reference buffer:
1. If V DDA is independent from VDD:
a) Enable the PVM3 (or PVM4) by setting PVME3 (or PVME4) bit in the Power
control register 2 (PWR_CR2).
b) Wait for the PVM3 (or PVM4) wakeup time.
c) Wait until PVMO3 (or PVM O4) bit is cleared in the Power status register 2
(PWR_SR2).
d) Optional: Disable the PVM3 (or PVM4) for consumption saving.
Enable the analog peripheral, which automatically removes the VDDA isolation.
8.3.4 Upper voltage threshold monitoring
The upper VDD voltage monitoring is enabled by setting the bit VMONEN in the
TAMP_CFGR register.
If the upper VDD voltage monitoring internal tamper is enabled in the TAMP peripheral
(ITAMP1E=1 in the TAMP_CR1 register), a tamper event is generated when the VDD
domain voltage is above the specified threshold.
The upper VDD monitoring can be periodical. This feature is enabled by setting the bit
WUTMONEN in the TAMP configuration register TAMP_CFGR.
In this case, the monitoring is controlled by the RTC wakeup timer PWM resulting from the
WUTF flag automatic clear and depending on the bitsfield WUTOCLR in the RTC_WUTR
register. For more details, refer to the RTC section.
The monitoring is enabled during the PWM high level and disabled during the PWM low
level.
Note: For threshold value, refer to the product datasheet.
Note: In case the VDD is below the function al range, a Brown-out reset is generated.
8.3.5 Temperature threshold monitoring
The temperature monitoring is enabled by setting the bit TMONEN in the TAMP_CFGR
register.
If the temperature monitoring internal tamper is enabled in the TAMP peripheral
(ITAMP2E=1 in the TAMP_CR1 register), a tamper event is generated when the
temperature is above or below the specified thresholds.

RM0438 Rev 8 277/2187
RM0438 Power control (PWR)
322
The temperature monitoring can be periodical. This feature is enabled by setting the bit
WUTMONEN in the TAMP configuration register TAMP_CFGR.
In this case, the monitoring is controlled by the RTC wakeup timer PWM resulting from the
WUTF flag automatic clear and depending on the bitfield WUTOCLR in the RTC_WUTR
register. For more details, refer to the RTC section.
The monitoring is enabled during the PWM high level and disabled during the PWM low
level.
Note: For thresholds values, refer to the product datasheet.
8.4 Power management
8.4.1 Power modes
By default, the microcontroller is in Run mode after a system or a power reset. Several low-
power modes are available to save power when the CPU does not need to be kept running,
for example when waiting for an external event. It is up to the user to select the mode that
gives the best compromise between low-power consumption, short startup time and
available wakeup sources.
The device features eight low-power modes:
• Sleep mode: CPU clock off, all peripherals including Cortex®-M33 core such as NVIC
and SysTick can run and wake up the CPU when an interrupt or an event occurs. Refer
to Section 8.4.5: Sleep mode.
• Low-power run mode: This mode is achieved when the system clock frequency is
reduced below 2 MHz. The code is executed from the SRAM or the flash memory. The
regulator is in Low-power mode to minimize the regulator's operating current. Refer to
Section 8.4.3: Low-power run mode (LP run).
• Low-power sleep mode: This mode is entered from the Low-power run mode: Cortex®-
M33 is off. Refer to Section 8.4.6: Low-power sleep mode (LP sleep).
• Stop 0, Stop 1 and Stop 2 modes: SRAM1, SRAM2 and all registers content are
retained. All clocks in the VCORE domain are stopped, the PLL, the MSI, the HSI16 and
the HSE are disabled. The LSI and the LSE can be kept running.
The RTC can remain active (Stop mode with RTC, Stop mode without RTC).
Some peripherals with the wakeup capability can enable the HSI16 RC during the Stop
mode to detect their wakeup condition.
In Stop 2 mode, most of the VCORE domain is put in a lower leakage mode.
Stop 1 offers the largest number of active peripherals and wakeup sources, a smaller
wakeup time but a higher consumption than Stop 2. In Stop 0 mode, the main regulator
remains ON, which allows the fastest wakeup time but with much higher consumption.
The active peripherals and wakeup sources are the same as in Stop 1 mode.
The system clock, when exiting from Stop 0, Stop 1 or Stop 2 mode, can be either MSI
up to 48 MHz or HSI16, depending on the software configuration.
Refer to Section 8.4.7: Stop 0 mode and Section 8.4.9: Stop 2 mode.
• Standby mode: VCORE domain is powered off. However, it is possible to preserve the
full SRAM2 content or only 4 Kbytes:
– Standby mode with full or only the upper 4 Kbytes of SRAM2 retention when the
RRS[1:0] bits are set to ‘01’ or ‘10’ respectively in the PWR_CR3 register. In this

Power control (PWR) RM0438
278/2187 RM0438 Rev 8
case, the SRAM2 is supplied by the low-power regulator.
– Standby mode when the RRS[1:0] bits are cleared in PWR_CR3 register. In this
case the main regulator and the low-power regulator are powered off.
All clocks in the VCORE domain are stopped, the PLL, the MSI, the HSI16 and the HSE
are disabled. The LSI and the LSE can be kept running.
The RTC can remain active (Standby mode with RTC, Standby mode without RTC).
The system clock, when exiting Standby modes, is MSI from 1 MHz up to 8 MHz.
Refer to Section 8.4.10: Standby mode.
• Shutdown mode: VCORE domain is powered off. All clocks in the VCORE domain are
stopped, the PLL, the MSI, the HSI16, the LSI and the HSE are disabled. The LSE can
be kept running. The system clock, when exiting the Shutdown mode, is MSI at 4 MHz.
In this mode, the supply voltage monitoring is disabled and the product behavior is not
guaranteed in case of a power voltage drop. Refer to Section 8.4.11: Shutdown mode.
In addition, the power consumption in Run mode can be reduced by one of the following
means:
• Slowing down the system clocks
• Gating the clocks to the APB and AHB peripherals when they are unused.
[Figure 28](../figures/figure_28.md). Low-power modes possible transitions
MS33361V2
Run mode
Low power run mode
Low power sleep mode
Stop 1 mode
Stop 2 mode
Shutdown mode
Standby mode
Sleep mode
Stop 0 mode

RM0438 Rev 8 279/2187
RM0438 Power control (PWR)
322
[Table 66](../tables/table_66.md). Low-power mode summary
Mode name Entry Wakeup
source(1)
Wakeup
system clock Effect on clocks
Voltage
regulators
MR LPR
Sleep
(Sleep-now or
Sleep-on-exit)
WFI or Return
from ISR Any interrupt Same as before
entering Sleep mode
CPU clock OFF
no effect on other
clocks or analog clock
sources
ON ON
WFE Wakeup event
Low-power
run Set LPR bit Clear LPR bit Same as low-power
run clock None OFF ON
Low-power
sleep
Set LPR bit + WFI
or Return
from ISR
Any interrupt Same as before
entering Low-power
sleep mode
CPU clock OFF
no effect on other
clocks or analog clock
sources
OFF ON
Set LPR bit + WFE Wakeup event OFF ON
Stop 0
LPMS=”000” +
SLEEPDEEP bit +
WFI or Return
from ISR or WFE
Any EXTI line
(configured in the
EXTI registers)
Specific peripher-
als events
HSI16 when STOP-
WUCK=1 in
RCC_CFGR
MSI with the fre-
quency before enter-
ing the Stop mode
when STOP-
WUCK=0.
All clocks OFF except
LSI and LSE
ON
ON
Stop 1
LPMS=”001” +
SLEEPDEEP bit +
WFI or Return
from ISR or WFE
OFF
Stop 2
LPMS=”010” +
SLEEPDEEP bit +
WFI or Return
from ISR or WFE
Standby with
SRAM2_4KB
LPMS=”011”+ Set
RRS[1:0] bits to
“10”+ SLEEPDEEP
bit + WFI or Return
from ISR or WFE
WKUP pin edge,
RTC event,
external reset in
NRST pin,
IWDG reset
MSI from 1 MHz up
to 8 MHz
Standby with
SRAM2_Full
LPMS=”011”+ Set
RRS bits to “01”+
SLEEPDEEP bit +
WFI or Return
from ISR or WFE
Standby
LPMS=”011” +
Clear RRS bits +
SLEEPDEEP bit +
WFI or Return
from ISR or WFE
OFF OFF
Shutdown
LPMS=”1--” +
SLEEPDEEP bit +
WFI or Return
from ISR or WFE
WKUP pin edge,
RTC event,
external reset in
NRST pin
MSI 4 MHz All clocks OFF except
LSE OFF OFF
1. Refer to [Table 67](../tables/table_67.md): Functionalities depending on the working mode.

Power control (PWR) RM0438
280/2187 RM0438 Rev 8
[Table 67](../tables/table_67.md). Functionalities depending on the working mode(1)
Peripheral Run Sleep
Low-
power
run
Low-
power
sleep
Stop 0/1 Stop 2 Standby Shutdown
VBAT
-
Wakeup capability
-
Wakeup capability
-
Wakeup capability
-
Wakeup capability
CPU Y - Y - - -- -- -- --
Flash memory
(2 Mbytes) O(2) O(2) O(2) O(2) - -- -- -- --
SRAM1
(192 Kbytes) YY (3) YY (3) Y -Y -- -- --
SRAM2 (64 Kbytes) Y Y (3) YY (3) Y -Y -O (4) -- --
F S M C OOOO - -- -- -- --
OctoSPI O O O O - -- -- -- --
O T F D E C OOOO - -- -- -- --
Backup registers Y Y Y Y Y -Y -Y -Y -Y
Brownout reset
(BOR) YYYY Y YY YY Y- --
Programmable
voltage detector
(PVD)
OOOO O OO O- -- --
Peripheral voltage
monitor (PVMx;
x=1,2,3,4)
OOOO O OO O- -- --
D M A OOOO - -- -- -- --
High speed internal
(HSI16) OOOO (5) - (5) -- -- --
Oscillator HSI48 O O - - - - - -- -- --
High speed external
(HSE) OOOO - -- -- -- --
Low speed internal
(LSI) OOOO O -O -O -- --
Low speed external
(LSE) OOOO O -O -O -O -O
Multi speed internal
(MSI) OOOO - -- -- -- --
Clock security
system (CSS) OOOO - -- -- -- --
Clock security
system on LSE OOOO O OO OO O- --

RM0438 Rev 8 281/2187
RM0438 Power control (PWR)
322
VDD voltage
monitoring,
temperature
monitoring
OOOO O OO OO O- --
R T C  /  T A M P OOOO O OO OO OO OO
Number of RTC
Tamper pins 8888 8 O8 O8 O8 O3
USB, UCPD O (8) O(8) -- - O- -- -- --
USARTx
(x=1,2,3,4,5) OOOO O (6) O(6) - -- -- --
Low-power UART
(LPUART) OOOO O (6) O(6) O(6) O(6) - -- --
I2Cx (x=1,2,4) O O O O O (7) O(7) - -- -- --
I 2 C 3 OOOO O (7) O(7) O(7) O(7) - -- --
SPIx (x=1,2,3) O O O O - -- -- -- --
FDCAN1 O O O O - -- -- -- --
S D M M C 1 OOOO - -- -- -- --
SAIx (x=1,2) O O O O - -- -- -- --
D F S D M 1 OOOO - -- -- -- --
ADCx (x=1,2) O O O O - -- -- -- --
DACx (x=1,2) O O O O O -- -- -- --
VREFBUF O O O O O -- -- -- --
OPAMPx (x=1,2) O O O O O -- -- -- --
C O M P x  ( x = 1 , 2 ) OOOO O OO O- -- --
Temperature sensor O O O O - -- -- -- --
Timers (TIMx) O O O O - -- -- -- --
Low-power timer 1,
3 (LPTIM1 and
LPTIM3)
OOOO O OO O- -- --
Low-power timer 2
(LPTIM2) OOOO O O- -- -- --
Independent
watchdog (IWDG) OOOO O OO OO O- --
[Table 67](../tables/table_67.md). Functionalities depending on the working mode(1) (continued)
Peripheral Run Sleep
Low-
power
run
Low-
power
sleep
Stop 0/1 Stop 2 Standby Shutdown
VBAT
-
Wakeup capability
-
Wakeup capability
-
Wakeup capability
-
Wakeup capability

Power control (PWR) RM0438
282/2187 RM0438 Rev 8
Debug mode
By default, the debug connection is lost if the application puts the MCU in Stop 0, Stop 1,
Stop 2, Standby or Shutdown mode while the debug features are used. This is due to the
fact that the Cortex®-M33 core is no longer clocked.
Window watchdog
(WWDG) OOOO - -- -- -- --
SysTick timer O O O O - -- -- -- --
Touch sensing
controller (TSC) OOOO - -- -- -- --
Random number
generator (RNG) O(8) O(8) -- - -- -- -- --
AES hardware
accelerator OOOO - -- -- -- --
HASH hardware
accelerator OOOO - -- -- -- --
PKA O O O O - -- -- -- --
CRC calculation
unit OOOO - -- -- -- --
G P I O s OOOO O OO O (9)
5
pins
(10)
(11)
5
pins
(10)
-
1. Legend: Y = yes (enable). O = optional (disable by default, can be enabled by software). - = not available.
Gray cells highlight the wakeup capability in each mode.
2. The flash can be configured in Power-down m ode. By default, it is not in Power-down mode.
3. The SRAM clock can be gated on or off.
4. 4 Kbytes or full SRAM2 content is preserved depending on RRS[1:0] bits configuration in PWR_CR3 register.
5. Some peripherals with wakeup from Stop capability can reque st HSI16 to be enabled. In this case, HSI16 is woken up by
the peripheral, and only feeds the peripheral which requested it. HSI16 is automatically put off when the peripheral does not
need it anymore.
6. UART and LPUART reception is functional in Stop mode,  and generates a wakeup interrupt on Start, address match or
received frame event.
7. I2C address detection is functional in Stop mode, and generates a wakeup interrupt in case of address match.
8. Voltage scaling range 1 only.
9. I/Os can be configured with internal pul l-up, pull-down or floating in Standby mode.
10. The I/Os with wakeup from standby/shutdown capability are: PA0, PC13, PE6, PA2, PC5.
11. I/Os can be configured with internal pul l-up, pull-down or floating in Shutdown mode but the configuration is lost when
exiting the Shutdown mode.
[Table 67](../tables/table_67.md). Functionalities depending on the working mode(1) (continued)
Peripheral Run Sleep
Low-
power
run
Low-
power
sleep
Stop 0/1 Stop 2 Standby Shutdown
VBAT
-
Wakeup capability
-
Wakeup capability
-
Wakeup capability
-
Wakeup capability

RM0438 Rev 8 283/2187
RM0438 Power control (PWR)
322
However, by setting some configuration bits in the DBGMCU_CR register, the software can
be debugged even when using the low-power modes extensively. For more details, refer to
Section 52.2.5: Debug and low-power modes.
8.4.2 Run mode
Slowing down system clocks
In Run mode, the speed of the system clocks (SYSCLK, HCLK, PCLK) can be reduced by
programming the prescaler registers. These prescalers can also be used to slow down the
peripherals before entering the Sleep mode.
For more details, refer to Section 9.8.3: RCC clock configuration register (RCC_CFGR).
Peripheral clock gating
In Run mode, the HCLK and PCLK for individual peripherals and memories can be stopped
at any time to reduce the power consumption.
To further reduce the power consumption in Sleep mode, the peripheral clocks can be
disabled prior to executing the WFI or WFE instructions.
The peripheral clock gating is controlled by the RCC_AHBxENR and RCC_APBxENR
registers.
Disabling the peripherals clocks in Sleep mode can be performed automatically by resetting
the corresponding bit in the RCC_AHBxSMENR and RCC_APBxSMENR registers.
8.4.3 Low-power r un mode (LP run)
To further reduce the consumption when the system is in Run mode, the regulator can be
configured in low-power mode. In this mode, the system frequency should not exceed
2 MHz.
Refer to the product datasheet for more details on voltage regulator and peripherals
operating conditions.
I/O states in Low-power run mode
In Low-power run mode, all I/O pins keep the same state as in Run mode.
Entering the Low-power run mode
To enter the Low-power run mode, proceed as follows:
1. Optional: Jump into the SRAM and power-down the flash by setting the RUN_PD bit in
the Flash access control register (FLASH_ACR).
2. Decrease the system clock frequency below 2 MHz.
3. Force the regulator in Low-power mode by setting the LPR bit in the PWR_CR1
register.
Refer to [Table 68](../tables/table_68.md): Low-power run on how to enter the Low-power run mode.
Exiting the Low-power run mode
To exit the Low-power run mode, proceed as follows:

Power control (PWR) RM0438
284/2187 RM0438 Rev 8
1. Force the regulator in Main mode by clearing the LPR bit in the PWR_CR1 register.
2. Wait until REGLPF bit is cleared in the PWR_SR2 register.
3. Increase the syst em clock frequency.
Refer to [Table 68](../tables/table_68.md): Low-power run on how to exit the Low-power run mode.
8.4.4 Low-power modes
Entering into a low-power mode
Low-power modes are entered by the MCU by executing the WFI (wait for interrupt), or
WFE (wait for event) instructions, or when the SLEEPONEXIT bit in the Cortex®-M33
system control register is set on Return from ISR.
Entering into a low-power mode through WFI or WFE is executed only if no interrupt is
pending or no event is pending.
Exiting from a low-power mode
From Sleep mode and Stop mode the MCU exits the low-power mode depending on the
way the low-power mode was entered:
• If the WFI instruction or return from ISR was used to enter the low-power mode, any
peripheral interrupt acknowledged by the NVIC can wake up the device.
• If the WFE instruction is used to enter the low-power mode, the MCU exits the low-
power mode as soon as an event occurs. The wakeup event can be generated either
by:
– NVIC IRQ interrupt.
- When SEVONPEND = 0 in the Cortex®-M33 system control register. By enabling
an interrupt in the peripheral control register and in the NVIC. When the MCU
resumes from WFE, the peripheral interrupt pending bit and the NVIC peripheral
IRQ channel pending bit (in the NVIC interrupt clear pending register) have to be
cleared.
Only NVIC interrupts with sufficient priority wakeup and interrupt the MCU.
- When SEVONPEND = 1 in the Cortex®-M33 System Control register.
By enabling an interrupt in the peripheral control register and optionally in the
NVIC. When the MCU resumes from WFE, the peripheral interrupt pending bit and
[Table 68](../tables/table_68.md). Low-power run
Low-power run mode Description
Mode entry Decrease the system clock frequency below 2 MHz
LPR = 1
Mode exit
LPR = 0
Wait until REGLPF = 0
Increase the system clock frequency
Wakeup latency Regulator wakeup time from low-power mode

RM0438 Rev 8 285/2187
RM0438 Power control (PWR)
322
when enabled the NVIC peripheral IRQ channel pending bit (in the NVIC interrupt
clear pending register) have to be cleared.
All NVIC interrupts wakes up the MCU, even the disabled ones. Only enabled
NVIC interrupts with sufficient priority wake up and interrupt the MCU.
–E v e n t
Configuring a EXTI line in Event mode. When the CPU resumes from WFE, it is
not necessary to clear the EXTI peripheral interrupt pending bit or the NVIC IRQ
channel pending bit as the pending bits corresponding to the event line is not set.
It may be necessary to clear the interrupt flag in the peripheral.
From Standby modes, and Shutdown modes the MCU exits the low-power mode through an
external reset (NRST pin), an IWDG reset, a rising edge on one of the enabled WKUPx pins
or a RTC event occurs (see [Figure 398](../figures/figure_398.md): RTC block diagram).
After waking up from Standby or Shutdown mode, program execution restarts in the same
way as after a Reset (boot pin sampling, option bytes loading, reset vector is fetched, etc.).
8.4.5 Sleep mode
I/O states in Sleep mode
In Sleep mode, all I/O pins keep the same state as in Run mode.
Entering the Sleep mode
The Sleep mode is entered according Section : Entering into a low-power mode, when the
SLEEPDEEP bit in the Cortex®-M33 System Control register is clear.
Refer to [Table 69](../tables/table_69.md): Sleep mode for details on how to enter the Sleep mode.
Exiting the Sleep mode
The Sleep mode is exit according Section : Exiting from a low-power mode.
Refer to [Table 69](../tables/table_69.md): Sleep mode for more details on how to exit the Sleep mode.
[Table 69](../tables/table_69.md). Sleep mode
Sleep-now mode Description
Mode entry
WFI (Wait for Interrupt) or WFE (Wait for Event) while:
– SLEEPDEEP = 0
– No interrupt (for WFI) or event (for WFE) is pending
Refer to the Cortex®-M33 system control register.
On return from ISR while:
– SLEEPDEEP = 0 and
– SLEEPONEXIT = 1
– No interrupt is pending
Refer to the Cortex®-M33 System Control register.

Power control (PWR) RM0438
286/2187 RM0438 Rev 8
8.4.6 Low-power sleep mode (LP sleep)
Refer to the product datasheet for more details on voltage regulator and peripherals
operating conditions.
I/O states in Low-power sleep mode
In Low-power sleep mode, all I/O pins keep the same state as in Run mode.
Entering the Low-power sleep mode
The Low-power sleep mode is entered from Low-power run mode according to Section :
Entering into a low-power mode, when the SLEEPDEEP bit in the Cortex®-M33 system
control register is clear.
Refer to [Table 70](../tables/table_70.md): Low-power sleep for details on how to enter the Low-power sleep mode.
Exiting the Low-power sleep mode
The Low-power sleep mode is exit according to Section : Exiting from a low-power mode.
When exiting the Low-power sleep mode by issuing an interrupt or an event, the MCU is in
Low-power run mode.
Refer to [Table 70](../tables/table_70.md): Low-power sleep for details on how to exit the Low-power sleep mode.
Mode exit
If WFI or return from ISR was used for entry
Interrupt: refer to [Table 109](../tables/table_109.md): STM32L552xx and STM32L562xx vector
table
If WFE was used for entry and SEVONPEND = 0:
Wakeup event: refer to Section 17.3: EXTI functional description
If WFE was used for entry and SEVONPEND = 1:
Interrupt even when disabled in NVIC: refer to [Table 109](../tables/table_109.md): STM32L552xx
and STM32L562xx vector table or Wakeup event: refer to Section 17.3:
EXTI functional description
Wakeup latency None
[Table 69](../tables/table_69.md). Sleep mode (continued)
Sleep-now mode Description

RM0438 Rev 8 287/2187
RM0438 Power control (PWR)
322
8.4.7 Stop 0 mode
The Stop 0 mode is based on the Cortex®-M33 Deepsleep mode combined with the
peripheral clock gating. The voltage regulator is configured in Main regulator mode. In Stop
0 mode, all clocks in the VCORE domain are stopped; the PLL, the MSI, the HSI16 and the
HSE oscillators are disabled. Some peripherals with the wakeup capability (I2Cx (x=1,2,3),
U(S)ARTx(x=1,2...5) and LPUART) can switch on the HSI16 to receive a frame, and switch
off the HSI16 after receiving the frame if it is not a wakeup frame. In this case, the HSI16
clock is propagated only to the peripheral requesting it.
SRAM1, SRAM2 and register contents are preserved.
The BOR is always available in Stop 0 mode. The consumption is increased when
thresholds higher than VBOR0 are used.
I/O states in Stop 0 mode
In the Stop 0 mode, all I/O pins keep the same state as in the Run mode.
Entering the Stop 0 mode
The Stop 0 mode is entered according Section : Entering into a low-power mode, when the
SLEEPDEEP bit in the Cortex®-M33 System Control register is set.
[Table 70](../tables/table_70.md). Low-power sleep
Low-power sleep-now
mode Description
Mode entry
Low-power sleep mode is entered from the Low-power run mode.
WFI (Wait for Interrupt) or WFE (Wait for Event) while:
– SLEEPDEEP = 0
– No interrupt (for WFI) or event (for WFE) is pending
Refer to the Cortex®-M33 System Control register.
Low-power sleep mode is entered from the Low-power run mode.
On return from ISR while:
– SLEEPDEEP = 0 and
– SLEEPONEXIT = 1
– No interrupt is pending
Refer to the Cortex®-M33 System Control register.
Mode exit
If WFI or Return from ISR was used for entry
Interrupt: refer to [Table 109](../tables/table_109.md): STM32L552xx and STM32L562xx vector
table
If WFE was used for entry and SEVONPEND = 0:
Wakeup event: refer to Section 17.3: EXTI functional description
If WFE was used for entry and SEVONPEND = 1:
Interrupt even when disabled in NVIC: refer to [Table 109](../tables/table_109.md): STM32L552xx
and STM32L562xx vector table
Wakeup event: refer to Section 17.3: EXTI functional description
After exiting the Low-power sleep mode, the MCU is in Low-power run
mode.
Wakeup latency None

Power control (PWR) RM0438
288/2187 RM0438 Rev 8
Refer to [Table 71](../tables/table_71.md): Stop 0 mode for details on how to enter the Stop 0 mode.
If flash memory programming is ongoing, the Stop 0 mode entry is delayed until the memory
access is finished.
If an access to the APB domain is ongoing, The Stop 0 mode entry is delayed until the APB
access is finished.
In Stop 0 mode, the following features can be selected by programming individual control
bits:
• Independent watchdog (IWDG): the IWDG is started by writing to its key register or by
hardware option. Once started, it cannot be stopped except by a reset. See
Section 39.3: IWDG functional description.
• Real-time clock (RTC): this is configured by the RTCEN bit in the RCC Backup domain
control register (RCC_BDCR).
• Internal RC oscillator (LSI): LSI clock or LSI clock divided by 128, this is configured by
the LSION and LSIPRE bits in the RCC control/status register (RCC_CSR).
• External 32.768 kHz oscillator (LSE): this is configured by the LSEON bit in the RCC
Backup domain control register (RCC_BDCR).
Several peripherals can be used in Stop 0 mode and can add consumption if they are
enabled and clocked by LSI or LSE, or when they request the HSI16 clock: LPTIM1,
LPTIM2, I2Cx (x=1,2,3,4) U(S)ARTx(x=1,2...5), LPUART.
The DACx (x=1,2), the OPAMPs and the comparators can be used in Stop 0 mode, the
PVMx (x=1,2,3,4) and the PVD as well. If they are not needed, they must be disabled by
software to save their power consumptions.
The ADCx (x=1,2,3), temperature sensor and VREFBUF buffer can consume power during
the Stop 0 mode, unless they are disabled before entering this mode.
Exiting the Stop 0 mode
The Stop 0 mode is exit according Section : Entering into a low-power mode.
Refer to [Table 71](../tables/table_71.md): Stop 0 mode for details on how to exit Stop 0 mode.
When exiting Stop 0 mode by issuing an interrupt or a wakeup event, the HSI16 oscillator is
selected as system clock if the bit STOPWUCK is set in RCC clock configuration register
(RCC_CFGR). The MSI oscillator is selected as system clock if the bit STOPWUCK is
cleared. The wakeup time is shorter when HSI16 is selected as wakeup system clock. The
MSI selection allows wakeup at higher frequency, up to 48 MHz.
When exiting the Stop 0 mode, the MCU is either in Run mode (Range 0, Range 1 or Range
2) or in Low-power run mode if the bit LPR is set in the PWR_CR1 register.

RM0438 Rev 8 289/2187
RM0438 Power control (PWR)
322
8.4.8 Stop 1 mode
The Stop 1 mode is the same as Stop 0 mode except that the main regulator is OFF, and
only the low-power regulator is ON. Stop 1 mode can be entered from Run mode and from
Low-power run mode.
Refer to [Table 72](../tables/table_72.md): Stop 1 mode for details on how to enter and exit Stop 1 mode.
[Table 71](../tables/table_71.md). Stop 0 mode
Stop 0 mode Description
Mode entry
WFI (Wait for Interrupt) or WFE (Wait for Event) while:
– SLEEPDEEP bit is set in Cortex®-M33 System Control register
– No interrupt (for WFI) or event (for WFE) is pending
– LPMS = “000” in PWR_CR1
On Return from ISR while:
– SLEEPDEEP bit is set in Cortex®-M33 System Control register
– SLEEPONEXIT = 1
– No interrupt is pending
– LPMS = “000” in PWR_CR1
Note: To enter Stop 0 mode, all EXTI Line pending bits (in EXTI rising
edge pending register (EXTI_RPR2)), and the peripheral flags
generating wakeup interrupts must be cleared. Otherwise, the Stop
0 mode entry procedure is ignored and program execution
continues.
Mode exit
If WFI or Return from ISR was used for entry
Any EXTI Line configured in Interrupt mode (the corresponding EXTI
Interrupt vector must be enabled in the NVIC). The interrupt source can
be external interrupts or peripherals with wakeup capability. Refer to
[Table 109](../tables/table_109.md): STM32L552xx and STM32L562xx vector table.
If WFE was used for entry and SEVONPEND = 0:
Any EXTI Line configured in Event mode. Refer to Section 17.3: EXTI
functional description.
If WFE was used for entry and SEVONPEND = 1:
Any EXTI Line configured in Interrupt mode (even if the corresponding
EXTI Interrupt vector is disabled in the NVIC). The interrupt source can
be external interrupts or peripherals with wakeup capability. Refer
toTable 109: STM32L552xx and STM32L562xx vector table.
Wakeup event: refer to Section 17.3: EXTI functional description
Wakeup latency Longest wakeup time between: MSI or HSI16 wakeup time and flash
wakeup time from Stop 0 mode.

Power control (PWR) RM0438
290/2187 RM0438 Rev 8
8.4.9 Stop 2 mode
The Stop 2 mode is based on the Cortex®-M33 Deepsleep mode combined with peripheral
clock gating. In Stop 2 mode, all clocks in the VCORE domain are stopped, the PLL, the MSI,
the HSI16 and the HSE oscillators are disabled. Some peripherals with wakeup capability
(I2C3 and LPUART) can switch on the HSI16 to receive a frame, and switch off the HSI16
after receiving the frame if it is not a wakeup frame. In this case the HSI16 clock is
propagated only to the peripheral requesting it.
SRAM1, SRAM2 and register contents are preserved.
The BOR is always available in Stop 2 mode. The consumption is increased when
thresholds higher than VBOR0 are used.
Note: The comparators outputs, the LPUART outpu ts and the LPTIM1 outputs are forced to low
speed (OSPEEDy=00) during the Stop 2 mode.
[Table 72](../tables/table_72.md). Stop 1 mode
Stop 1 mode Description
Mode entry
WFI (wait for interrupt) or WFE (wait for event) while:
– SLEEPDEEP bit is set in Cortex®-M33 System Control register
– No interrupt (for WFI) or event (for WFE) is pending
– LPMS = “001” in PWR_CR1
On Return from ISR while:
– SLEEPDEEP bit is set in Cortex®-M33 System Control register
– SLEEPONEXIT = 1
– No interrupt is pending
– LPMS = “001” in PWR_CR1
Note: To enter Stop 1 mode, all EXTI Line pending bits (in EXTI rising
edge pending register (EXTI_RPR1)), and the peripheral flags
generating wakeup interrupts must be cleared. Otherwise, the Stop
1 mode entry procedure is ignored and program execution
continues.
Mode exit
If WFI or Return from ISR was used for entry
Any EXTI Line configured in Interrupt mode (the corresponding EXTI
Interrupt vector must be enabled in the NVIC). The interrupt source can
be external interrupts or peripherals with wakeup capability. Refer to
[Table 109](../tables/table_109.md): STM32L552xx and STM32L562xx vector table.
If WFE was used for entry and SEVONPEND = 0:
Any EXTI Line configured in Event mode. Refer to Section 17.3: EXTI
functional description.
If WFE was used for entry and SEVONPEND = 1:
Any EXTI Line configured in Interrupt mode (even if the corresponding
EXTI Interrupt vector is disabled in the NVIC). The interrupt source can
be external interrupts or peripherals with wakeup capability. Refer
toTable 109: STM32L552xx and STM32L562xx vector table.
Wakeup event: refer to Section 17.3: EXTI functional description
Wakeup latency Longest wakeup time between: MSI or HSI16 wakeup time and regulator
wakeup time from low-power mode + flash wakeup time from Stop 1 mode.

RM0438 Rev 8 291/2187
RM0438 Power control (PWR)
322
I/O states in Stop 2 mode
In the Stop 2 mode, all I/O pins keep the same state as in the Run mode.
Entering Stop 2 mode
The Stop 2 mode is entered according Section : Entering into a low-power mode, when the
SLEEPDEEP bit in the Cortex®-M33 System Control register is set.
Refer to [Table 73](../tables/table_73.md): Stop 2 mode for details on how to enter the Stop 2 mode.
Stop 2 mode can only be entered from Run mode. It is not possible to enter Stop 2 mode
from the Low-power run mode.
If flash memory programming is ongoing, the Stop 2 mode entry is delayed until the memory
access is finished.
If an access to the APB domain is ongoing, The Stop 2 mode entry is delayed until the APB
access is finished.
In Stop 2 mode, the following features can be selected by programming individual control
bits:
• Independent watchdog (IWDG): the IWDG is started by writing to its key register or by
hardware option. Once started it cannot be stopped except by a Reset. See
Section 39.3: IWDG functional description in Section 39: Independent watchdog
(IWDG).
• Real-time clock (RTC): this is configured by the RTCEN bit in the RCC Backup domain
control register (RCC_BDCR).
• Internal RC oscillator (LSI): LSI clock or LSI clock divided by 128, this is configured by
the LSION and LSIPRE bits in the RCC control/status register (RCC_CSR).
• External 32.768 kHz oscillator (LSE): this is configured by the LSEON bit in the RCC
Backup domain control register (RCC_BDCR).
Several peripherals can be used in Stop 2 mode and can add consumption if they are
enabled and clocked by LSI or LSE, or when they request the HSI16 clock: LPTIM1, I2C3,
LPUART.
The comparators can be used in Stop 2 mode, the PVMx (x=1,2,3,4) and the PVD as well. If
they are not needed, they must be disabled by software to save their power consumptions.
The ADCx, OPAMPx, DACx, temperature sensor and VREFBUF buffer can consume power
during Stop 2 mode, unless they are disabled before entering this mode.
All the peripherals which cannot be enabled in Stop 2 mode must be either disabled by
clearing the enable bit in the peripheral itself, or put under reset state by setting the
corresponding bit in the RCC AHB1 peripheral reset register (RCC_AHB1RSTR), RCC
AHB2 peripheral reset register (RCC_AHB2RSTR), RCC AHB3 peripheral reset register
(RCC_AHB3RSTR), RCC APB1 peripheral reset register 1 (RCC_APB1RSTR1), RCC
APB1 peripheral reset register 2 (RCC_APB1RSTR2), RCC APB2 peripheral reset register
(RCC_APB2RSTR).
Exiting Stop 2 mode
The Stop 2 mode is exit according to Section : Exiting from a low-power mode.
Refer to [Table 73](../tables/table_73.md): Stop 2 mode for details on how to exit Stop 2 mode.

Power control (PWR) RM0438
292/2187 RM0438 Rev 8
When exiting Stop 2 mode by issuing an interrupt or a wakeup event, the HSI16 oscillator is
selected as system clock if the bit STOPWUCK is set in RCC clock configuration register
(RCC_CFGR). The MSI oscillator is selected as system clock if the bit STOPWUCK is
cleared. The wakeup time is shorter when HSI16 is selected as wakeup system clock. The
MSI selection allows wakeup at higher frequency, up to 48 MHz.
When exiting the Stop 2 mode, the MCU is in Run mode (Range 0, Range 1 or Range 2
depending on VOS bit in PWR_CR1).
8.4.10 Standby mode
The Standby mode permits the achievement of the lowest power consumption with BOR. It
is based on the Cortex®-M33 Deepsleep mode, with the voltage regulators disabled (except
when SRAM2 content is preserved). The PLL, the HSI16, the MSI and the HSE oscillators
are also switched off.
[Table 73](../tables/table_73.md). Stop 2 mode
Stop 2 mode Description
Mode entry
WFI (wait for interrupt) or WFE (wait for event) while:
– SLEEPDEEP bit is set in Cortex®-M33 system control register
– No interrupt (for WFI) or event (for WFE) is pending
– LPMS = “010” in PWR_CR1
On return from ISR while:
– SLEEPDEEP bit is set in Cortex®-M33 System Control register
– SLEEPONEXIT = 1
– No interrupt is pending
– LPMS = “010” in PWR_CR1
Note: To enter Stop 2 mode, all EXTI Line pending bits (in EXTI rising
edge pending register (EXTI_RPR2)), and the peripheral flags gen-
erating wakeup interrupts must be cleared. Otherwise, the Stop
mode entry procedure is ignored and program execution continues.
Mode exit
If WFI or Return from ISR was used for entry:
Any EXTI Line configured in Interrupt mode (the corresponding EXTI
Interrupt vector must be enabled in the NVIC). The interrupt source can
be external interrupts or peripherals with wakeup capability. Refer to
[Table 109](../tables/table_109.md): STM32L552xx and STM32L562xx vector table.
If WFE was used for entry and SEVONPEND = 0:
Any EXTI Line configured in Event mode. Refer to Section 17.3: EXTI
functional description.
If WFE was used for entry and SEVONPEND = 1:
Any EXTI Line configured in Interrupt mode (even if the corresponding
EXTI Interrupt vector is disabled in the NVIC). The interrupt source can
be external interrupts or peripherals with wakeup capability. Refer to
[Table 109](../tables/table_109.md): STM32L552xx and STM32L562xx vector table.
Any EXTI Line configured in Event mode. Refer to Section 17.3: EXTI
functional description.
Wakeup latency Longest wakeup time between: MSI or HSI16 wakeup time and regulator
wakeup time from low-power mode + flash wakeup time from Stop 2 mode.

RM0438 Rev 8 293/2187
RM0438 Power control (PWR)
322
SRAM1 and register contents are lost except for registers in the Backup domain and
Standby circuitry (see [Figure 21](../figures/figure_21.md)). SRAM2 content can be can be partially or fully preserved
depending on RRS[1:0] bits configuration in PWR_CR3. In this case the Low-power
regulator is ON and provides the supply to SRAM2 only.
The BOR is always available in Standby mode. The consumption is increased when
thresholds higher than VBOR0 are used.
I/O states in Standby mode
In the Standby mode, the IO’s are by default in floating state. If the APC bit of PWR_CR3
register has been set, the I/Os can be configured either with a pull-up (refer to
PWR_PUCRx registers (x=A,B,C,D,E,F,G,H)), or with a pull-down (refer to PWR_PDCRx
registers (x=A,B,C,D,E,F,G,H)), or can be kept in analog state if none of the PWR_PUCRx
or PWR_PDCRx register has been set. The pull-down configuration has highest priority over
pull-up configuration in case both PWR_PUCRx and PWR_PDCRx are set for the same IO.
Some I/Os (listed in Section 11.3.1: General-purpose I/O (GPIO)) are used for JTAG/SW
debug and can only be configured to their respective reset pull-up or pull-down state during
Standby mode setting their respective bit in the PWR_PUCRx or PWR_PDCRx registers to
‘1’, or to be configured to floating state if the bit is kept at ‘0’.
The RTC outputs on PC13 are functional in Standby mode. PC14 and PC15 used for LSE
are also functional. 5 wakeup pins (WKUPx, x=1,2...5) and tamper inputs are available.
Entering Standby mode
The Standby mode is entered according Section : Entering into a low-power mode, when
the SLEEPDEEP bit in the Cortex®-M33 System Control register is set.
Refer to [Table 74](../tables/table_74.md): Standby mode for details on how to enter Standby mode.
In Standby mode, the following features can be selected by programming individual control
bits:
• Independent watchdog (IWDG): the IWDG is started by writing to its Key register or by
hardware option. Once started it cannot be stopped except by a reset. See
Section 39.3: IWDG functional description in Section 39: Independent watchdog
(IWDG).
• Real-time clock (RTC): this is configured by the RTCEN bit in the Backup domain
control register (RCC_BDCR).
• Internal RC oscillator (LSI): LSI clock or LSI clock divided by 128, this is configured by
the LSION and LSIPRE bits in the Control/status register (RCC_CSR).
• External 32.768 kHz oscillator (LSE): this is configured by the LSEON bit in the Backup
domain control register (RCC_BDCR).
Exiting Standby mode
The Standby mode is exited according Section : Entering into a low-power mode. The SBF
status flag in the Power control register 3 (PWR_CR3) indicates that the MCU was in
Standby mode. All registers are reset after wakeup from Standby except for Power control
register 3 (PWR_CR3).
Refer to [Table 74](../tables/table_74.md): Standby mode for more details on how to exit Standby mode.

Power control (PWR) RM0438
294/2187 RM0438 Rev 8
When exiting Standby mode, I/O’s that were configured with pull-up or pull-down during
Standby through registers PWR_PUCRx or PWR_PDCRx keep this configuration upon
exiting Standby mode until the bit APC of PWR_CR3 register has been cleared. Once the bit
APC is cleared, they are either configured to their reset values or to the pull-up/pull-down
state according the GPIOx_PUPDR registers. The content of the PWR_PUCRx or
PWR_PDCRx registers however is not lost and can be re-used for a sub-sequent entering
into Standby mode.
Some I/Os (listed in Section 11.3.1: General-purpose I/O (GPIO)) are used for JTAG/SW
debug and have internal pull-up or pull-down activated after reset so is configured at this
reset value as well when exiting Standby mode.
For IO’s, with a pull-up or pull-down pre-defined after reset (some JTAG/SW IO’s) or with
GPIOx_PUPDR programming done after exiting from Standby, in case those programming
is different from the PWR_PUCRx or PWR_PDCRx programmed value during Standby, both
a pull-down and pull-up are applied until the bit APC is cleared, releasing the PWR_PUCRx
or PWR_PDCRx programmed value.
[Table 74](../tables/table_74.md). Standby mode
Standby mode Description
Mode entry
WFI (Wait for Interrupt) or WFE (Wait for Event) while:
– SLEEPDEEP bit is set in Cortex®-M33 System Control register
– No interrupt (for WFI) or event (for WFE) is pending
– LPMS = “011” in PWR_CR1
– WUFx bits are cleared in power status register 1 (PWR_SR1)
On return from ISR while:
– SLEEPDEEP bit is set in Cortex®-M33 System Control register
– SLEEPONEXIT = 1
– No interrupt is pending
– LPMS = “011” in PWR_CR1 and
– WUFx bits are cleared in power status register 1 (PWR_SR1)
– The RTC flag corresponding to the chosen wakeup source (RTC Alarm
A, RTC Alarm B, RTC wakeup, tamper or timestamp flags) is cleared
Mode exit WKUPx pin edge, RTC event, external Reset in NRST pin, IWDG Reset,
BOR reset
Wakeup latency Reset phase

RM0438 Rev 8 295/2187
RM0438 Power control (PWR)
322
8.4.11 Shutdown mode
The Shutdown mode allows to achieve the lowest power consumption. It is based on the
Deepsleep mode, with the voltage regulator disabled. The VCORE domain is consequently
powered off. The PLL, the HSI16, the MSI, the LSI and the HSE oscillators are also
switched off.
SRAM1, SRAM2 and register contents are lost except for registers in the Backup domain.
The BOR is not available in Shutdown mode. No power voltage monitoring is possible in this
mode, therefore the switch to Backup domain is not supported.
I/O states in Shutdown mode
In the Shutdown mode, are by default in floating state. If the APC bit of PWR_CR3 register
has been set, the I/Os can be configured either with a pull-up (refer to PWR_PUCRx
registers (x=A,B,C,D,E,F,G,H), or with a pull-down (refer to PWR_PDCRx registers
(x=A,B,C,D,E,F,G,H)), or can be kept in analog state if none of the PWR_PUCRx or
PWR_PDCRx register has been set. The pull-down configuration has highest priority over
pull-up configuration in case both PWR_PUCRx and PWR_PDCRx are set for the same IO.
However this configuration is lost when exiting the Shutdown mode due to the power-on
reset.
Some I/Os (listed in Section 11.3.1: General-purpose I/O (GPIO)) are used for JTAG/SW
debug and can only be configured to their respective reset pull-up or pull-down state during
Standby mode setting their respective bit in the PWR_PUCRx or PWR_PDCRx registers to
‘1’, or to be configured to floating state if the bit is kept at ‘0’.
The RTC outputs on PC13 are functional in Shutdown mode. PC14 and PC15 used for LSE
are also functional. Five wakeup pins (WKUPx, x=1,2...5) and the three RTC tampers are
available.
Entering Shutdown mode
The Shutdown mode is entered according Entering into a low-power mode, when the
SLEEPDEEP bit in the Cortex®-M33 System Control register is set.
Refer to [Table 75](../tables/table_75.md): Shutdown mode for details on how to enter Shutdown mode.
In Shutdown mode, the following features can be selected by programming individual
control bits:
• Real-time clock (RTC): this is configured by the RTCEN bit in the Backup domain
control register (RCC_BDCR). Caution: in case of VDD power-down the RTC content is
lost.
• External 32.768 kHz oscillator (LSE): this is configured by the LSEON bit in the Backup
domain control register (RCC_BDCR).
Exiting Shutdown mode
The Shutdown mode is exit according Section : Exiting from a low-power mode. A power-on
reset occurs when exiting from Shutdown mode. All registers (except for the ones in the
Backup domain) are reset after wakeup from Shutdown.
Refer to [Table 75](../tables/table_75.md): Shutdown mode for more details on how to exit Shutdown mode.
When exiting Shutdown mode, I/Os that were configured with pull-up or pull-down during
Shutdown through registers PWR_PUCRx or PWR_PDCRx lose their configuration and are

Power control (PWR) RM0438
296/2187 RM0438 Rev 8
configured in floating state or to their pull-up pull-down reset value (for some I/Os listed in
Section 11.3.1: General-purpose I/O (GPIO)).
8.4.12 Auto-wakeup from a low-power mode
The RTC can be used to wakeup the MCU from a low-power mode without depending on an
external interrupt (Auto-wakeup mode). The RTC provides a programmable time base for
waking up from Stop (0, 1 or 2) or Standby mode at regular intervals. For this purpose, two
of the three alternative RTC clock sources can be selected by programming the
RTCSEL[1:0] bits in the RCC Backup domain control register (RCC_BDCR):
• Low-power 32.768 kHz external crystal oscillator (LSE OSC)
This clock source provides a precise time base with very low-power consumption.
• Low-power internal RC Oscillator (LSI)
This clock source has the advantage of saving the cost of the 32.768 kHz crystal. This
internal RC Oscillator is designed to add minimum power consumption.
To wakeup from Stop mode with an RTC event (alarm, wake-up timer, timestamp), it is
necessary to:
• Configure the EXTI Line 17 for non-secure interrupt and EXTI Line 18 for secure
interrupts to be sensitive to rising edge
• Configure the RTC to generate the RTC event (alarm, wake-up timer, timestamp)
To wakeup from Standby mode, there is no need to configure the EXTI Line 17 or
EXTI Line 18.
8.5 PWR TrustZone security
When the TrustZone security is activated by the TZEN option bit in the FLASH_OPTR
register, some PWR register fields can be secured against non-secure access.
[Table 75](../tables/table_75.md). Shutdown mode
Shutdown mode Description
Mode entry
WFI (Wait for Interrupt) or WFE (Wait for Event) while:
– SLEEPDEEP bit is set in Cortex®-M33 System Control register
– No interrupt (for WFI) or event (for WFE) is pending
– LPMS = “1XX” in PWR_CR1
– WUFx bits are cleared in power status register 1 (PWR_SR1)
On return from ISR while:
– SLEEPDEEP bit is set in Cortex®-M33 System Control register
– SLEEPONEXT = 1
– No interrupt is pending
– LPMS = “1XX” in PWR_CR1 and
– WUFx bits are cleared in power status register 1 (PWR_SR1)
– The RTC flag corresponding to the chosen wakeup source (RTC
Alarm A, RTC Alarm B, RTC wakeup, tamper or timestamp flags) is
cleared
Mode exit WKUPx pin edge, RTC event, external Reset in NRST pin
Wakeup latency Reset phase

RM0438 Rev 8 297/2187
RM0438 Power control (PWR)
322
The PWR TrustZone security allows to secure the following features through the security
configuration register PWR_SECCFGR:
• Low-power mode
• Wake-up (WKUP) pins
• Voltage detection and monitoring
• VBAT mode
Other PWR configuration bits are secure when:
• The system clock selection is secure in RCC, the voltage scaling (VOS) configuration is
secure
• A GPIO is configured as secure, its corresponding bit for Pull-up/Pull-down
configuration in Standby mode is secure
• The RTC is secure, the backup domain write protection DBP bit in PWR_CR1 register
is secure.
• The UCPD is secure, the UCPD_DBDIS and UCPD_STDBY bits are secure in the
PWR_CR3 register.
[Table 76](../tables/table_76.md) gives a summary of the PWR secured bits following the security configuration bit in
the PWR_SECCFGR register. When one security configuration bit is set, some
configuration bits are secured. The PWR registers may contain secure and non-secure bits:
• Secured bits: read and write operations are only allowed by a secure access. Non-
secure read or write accesses are RAZ/WI. There is no illegal access event generated.
• Non-secure bits: no restriction. Read and write operations are allowed by both secure
and non-secure accesses.
A non-secure write access to PWR_SECCFGR register is WI and generates an illegal
access event. An illegal access interrupt is generated if the PWR illegal access interrupt is
enabled in the TZIC_IER2 register. There is no restriction for non-secure read access.
When the TrustZone security is disabled (TZEN = 0 in FLASH_OPTR register), all registers
are non-secure. The PWR_SECCFGR secure register and security status registers are
RAZ/WI.
.
[Table 76](../tables/table_76.md). PWR Security configuration summary
Secure configura-
tion register
Security configura-
tion bit Secured bits Register name
Non-secure
access on secure
bits
PWR_SECCFGR NA (1) - PWR_SECCFGR
Read is OK.
WI and illegal
access event
PWR_SECCFGR At least one bit is set PRIV PWR_PRIVCFGR
Read is OK.
WI and illegal
access event(2)

Power control (PWR) RM0438
298/2187 RM0438 Rev 8
8.5.1 PWR Privileged a nd Unprivileged modes
The PWR registers can be can be read and written by privileged and unprivileged accesses
depending on PRIV bit in PWR_PRIVCFGR register.
• When the PRIV bit is reset, all PWR registers could be read and written by both
privileged or unprivileged access.
• When the PRIV bit is set, all PWR registers could be read and written by privileged
access only (except PWR_SR1, PWR_SR2 and PWR_SECFGR registers).
Unprivileged access to a privileged registers is RAZ/WI.
8.6 PWR registers
The peripheral registers can be accessed by half-words (16-bit) or words (32-bit).
PWR_SECCFGR
LPMSEC
LPMS[1:0],
LPR PWR_CR1
RAZ/WI
RRS[1:0] PWR_CR3
CSBF,
CWUFx PWR_SCR WI
WUPxSEC or LPM-
SEC(1)
WUPx PWR_CR3
RAZ/WI
WUPPx PWR_CR4
VDMSEC
All bits in PWR_CR2 PWR_CR2
ULPMEN PWR_CR3
SMPSBYP ,
EXTSMPSEN,
SMPSFSTEN,
SMPSLPEN
PWR_CR4
RAZ/WI
VBSEC
DBP PWR_CR1
VBRS, VBE PWR_CR4
APCSEC APC PWR_CR3
TZSC_SECFGR UCPD1SEC UCPD_DBDIS and
UCPD_STDBY PWR_CR3
RAZ/WI
RCC_SECCFGR CKSYSSEC VOS[1:0] PWR_CR1
GPIOx_SECCFGR
(x=A,B..H) SECy (y=0..15)
PUy (y=0..15) PWR_PUCRx (x = A,
B..H)
PDy (y=0..15) PWR_PDCRx (x = A,
B..H)
1. PWR_SECCFGR register is always secure.
2. Illegal access event is generated only when the PWR_PRIVCFGR is secure.
[Table 76](../tables/table_76.md). PWR Security configuration summary
Secure configura-
tion register
Security configura-
tion bit Secured bits Register name
Non-secure
access on secure
bits

RM0438 Rev 8 299/2187
RM0438 Power control (PWR)
322
8.6.1 Power control re gister 1 (PWR_CR1)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on PWR_SECCFGR and RCC_SECCFGR configuration regis-
ters. A non-secure read/write access on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
This register is reset after wakeup from Standby mode.
Address offset: 0x00
Reset value: 0x0000 0400
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. LPR Res. Res. Res. VOS[1:0] DBP Res. Res. Res. Res. Res. LPMS[2:0]
rw rw rw rw rw rw rw
Bits 31:15 Reserved, must  be kept at reset value.
Bit 14 LPR: Low-power run
When this bit is set, the regulator is switched from Main mode (MR) to Low-power run mode
(LPR).
Note: Stop 2 mode cannot be entered when LPR bit is set. Stop 1 is entered instead.
Bits 13:11 Reserved, must be kept at reset value.
Bits 10:9 VOS[1:0]: Voltage scaling range selection
00: Range 0
01: Range 1
10: Range 2
11: Cannot be written (forbidden by hardware).
Bit 8 DBP: Disable backup domain write protection.
In reset state, the RTC and backup registers are protected against parasitic write access.
This bit must be set to enable write access to these registers.
0: Access to RTC and Backup registers disabled
1: Access to RTC and Backup registers enabled.
Bits 7:3 Reserved, must be kept at reset value.
Bits 2:0 LPMS[2:0]: Low-power mode selection
These bits select the low-power mode entered when CPU enters the Deepsleep mode.
000: Stop 0 mode
001: Stop 1 mode
010: Stop 2 mode
011: Standby mode
1xx: Shutdown mode
Note: If LPR bit is set, Stop 2 mode cannot be selected and Stop 1 mode shall be entered
instead of Stop 2.
Note: In Standby mode, SRAM2 can be preserv ed or not, depending on RRS bit configuration
in PWR_CR3.

Power control (PWR) RM0438
300/2187 RM0438 Rev 8
8.6.2 Power control re gister 2 (PWR_CR2)
When the system is secure (TZEN =1), this register is protected against non-secure access
when VDMSEC=1 in the PWR_SECCFGR register. A non-secure read/write access is
RAZ/WI and generates and illegal access event.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Address offset: 0x04
Reset value: 0x0000 0000
This register is reset when exiting the Standby mode.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. USV IOSV Res. PVME4 PVME3 PVME2 PVME1 PLS[2:0] PVDE
rw rw rw rw rw rw rw rw rw rw
Bits 31:11 Reserved, must be kept at reset value.
Bit 10 USV: VDDUSB USB supply valid
This bit is used to validate the VDDUSB supply for electrical and logical isolation purpose.
Setting this bit is mandatory to use the USB peripheral. If VDDUSB is not always
present in the application, the PVM can be used to determine whether this supply is ready or
not.
0: VDDUSB is not present. Logical and electrical isolation is applied to ignore this supply.
1: VDDUSB is valid.
Bit 9 IOSV: VDDIO2 Independent I/Os supply valid
This bit is used to validate the VDDIO2 supply for electrical and logical isolation purpose.
Setting this bit is mandatory to use PG[15:2]. If VDDIO2 is not always present in the
application, the PVM can be used to determine whether this supply is ready or not.
0: VDDIO2 is not present. Logical and electrical isolation is applied to ignore this supply.
1: VDDIO2 is valid.
Bit 8 Reserved, must be kept at reset value.
Bit 7 PVME4: Peripheral voltage monitoring 4 enable: VDDA vs. 1.8 V
0: PVM4 (VDDA monitoring vs. 1.8 V threshold) disable.
1: PVM4 (VDDA monitoring vs. 1.8 .V threshold) enable.
Bit 6 PVME3: Peripheral voltage monitoring 3 enable: VDDA vs. 1.62V
0: PVM3 (VDDA monitoring vs. 1.62V threshold) disable.
1: PVM3 (VDDA monitoring vs. 1.62V threshold) enable.
Bit 5 PVME2: Peripheral voltage monitoring 2 enable: VDDIO2 vs. 0.9V
0: PVM2 (VDDIO2 monitoring vs. 0.9V threshold) disable.
1: PVM2 (VDDIO2 monitoring vs. 0.9V threshold) enable.

RM0438 Rev 8 301/2187
RM0438 Power control (PWR)
322
8.6.3 Power control re gister 3 (PWR_CR3)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on PWR_SECCFGR and TZSC_SECCFGR configuration. A non-
secure read/write access on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: Additional APB cycles are needed to access this register versus a standard APB
access (3 for a write and 2 for a read).
This register is not reset when exiting Standby modes and with the PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x08
Reset value: 0x0000 0000
Bit 4 PVME1: Peripheral voltage monitoring 1 enable: VDDUSB vs. 1.2V
0: PVM1 (VDDUSB monitoring vs. 1.2V threshold) disable.
1: PVM1 (VDDUSB monitoring vs. 1.2V threshold) enable.
Bits 3:1 PLS[2:0]: Programmable voltage detector level selection.
These bits select the voltage threshold detected by the programmable voltage detector:
000: VPVD0 around 2.0 V
001: VPVD1 around 2.2 V
010: VPVD2 around 2.4 V
011: VPVD3 around 2.5 V
100: VPVD4 around 2.6 V
101: VPVD5 around 2.8 V
110: VPVD6 around 2.9 V
111: External input analog voltage PVD_IN (compared internally to VREFINT)
Note: These bits are write-protected when  the bit PVDL (PVD Lock) is set in the
SYSCFG_CBR register.
These bits are reset only by a system reset.
Bit 0 PVDE: Programmable voltage detector enable
0: Programmable voltage detector disable.
1: Programmable voltage detector enable.
Note: This bit is write-protected when the bit PVDL (PVD Lock) is set in the SYSCFG_CBR
register.
This bit is reset only by a system reset.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. UCPD_
DBDIS
UCPD_
STDBY Res. ULPM
EN APC RRS[1:0] Res. Res. Res. EWUP5 EWUP4 EWUP3 EWUP2 EWUP1
rw rw rw rw rw rw rw rw rw rw rw

Power control (PWR) RM0438
302/2187 RM0438 Rev 8
Bits 31:15 Reserved, must  be kept at reset value.
Bit 14 UCPD_DBDIS: USB Type-C and power delivery dead dattery disable
After exiting reset, the USB Type-C “dead battery” behavior is enabled, which may have a
pulldown effect on CC1 and CC2 pins. It is recommended to disable it in all cases, either to
stop this pull-down or to hand over control to the UCPD (which should therefore be initialized
before doing the disable).
0: enable USB Type-C dead battery pull-down behavior on UCPDx_CC1 and UCPDx_CC2
pins
1: disable USB Type-C dead battery pull-down behavior on UCPDx_CC1 and UCPDx_CC2
pins
Bit 13 UCPD_STDBY: USB Type-C and power delivery Standby mode
When set, this bit allows to memorize the UCPD configuration in Standby mode.
This bit must be written to ‘1’ just before entering Standby mode when using UCPD, and it
must be written to 0 after exiting the Standby mode and before writing any UCPD registers.
Bit 12 Reserved, must be kept at reset value.
Bit 11 ULPMEN: Ultra-low-power mode enable
When this bit is set, the BOR and PVD are in Ultra-low-power mode during Stop 2 and
Standby mode in order to further reduce the current consumption.
0: BORL, BORH and PVD operating in Default mode.
1: Enable Ultra-low-power mode for BORL, BORH and PVD during Stop 2 and Standby
mode.
In Stop 2 mode, ULPMEN can be set if BORH and PVD are enabled, otherwise there is no
power consumption optimization.
Bit 10 APC: Apply pull-up and pull-down configuration
When this bit is set, the I/O pull-up and pull-down configurations defined in the PWR_PUCRx
and PWR_PDCRx registers are applied. When this bit is cleared, the PWR_PUCRx and
PWR_PDCRx registers are not applied to the I/Os, instead the I/Os are in Floating mode
during Standby or configured according GPIO controller GPIOx_PUPDR register during Run
mode.
Bits 9:8 RRS[1:0]: SRAM2 retention in Standby mode
00: SRAM2 is powered off in Standby mode (SRAM2 content is lost).
01: Full SRAM2 is powered by the low-power regulator in Standby mode (Full SRAM2
content is kept).
10: Only the upper 4 Kbytes of SRAM2 are powered by the low-power regulator in Standby
mode (upper 4 Kbytes of SRAM2 content 0x2003 F000 - 0x2003 FFFF is kept).
11: Reserved
Bits 7:5 Reserved, must be kept at reset value.
Bit 4 EWUP5: Enable wakeup pin WKUP5
When this bit is set, the external wakeup pin WKUP5 is enabled and triggers a wakeup from
Standby or Shutdown event when a rising or a falling edge occurs.The active edge is
configured via the WUPP5 bit in the PWR_CR4 register.
Bit 3 EWUP4: Enable wakeup pin WKUP4
When this bit is set, the external wakeup pin WKUP4 is enabled and triggers a wakeup from
Standby or Shutdown event when a rising or a falling edge occurs. The active edge is
configured via the WUPP4 bit in the PWR_CR4 register.

RM0438 Rev 8 303/2187
RM0438 Power control (PWR)
322
8.6.4 Power control re gister 4 (PWR_CR4)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on PWR_SECCFGR configuration. A non-secure read/write
access on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
This register is not reset when exiting Standby modes and with the PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x0C
Reset value: 0x0000 0000
Bit 2 EWUP3: Enable wakeup pin WKUP3
When this bit is set, the external wakeup pin WKUP3 is enabled and triggers a wakeup from
Standby or Shutdown event when a rising or a falling edge occurs. The active edge is
configured via the WUPP3 bit in the PWR_CR4 register.
Bit 1 EWUP2: Enable wakeup pin WKUP2
When this bit is set, the external wakeup pin WKUP2 is enabled and triggers a wakeup from
Standby or Shutdown event when a rising or a falling edge occurs. The active edge is
configured via the WUPP2 bit in the PWR_CR4 register.
Bit 0 EWUP1: Enable wakeup pin WKUP1
When this bit is set, the external wakeup pin WKUP1 is enabled and triggers a wakeup from
Standby or Shutdown event when a rising or a falling edge occurs. The active edge is
configured via the WUPP1 bit in the PWR_CR4 register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
SMPSL
PEN
SMPS
FSTEN
EXTS
MPSE
N
SMPS
BYP Res. Res. VBRS VBE Res. Res. Res. WUPP5 WUPP4 WUPP3 WUPP2 WUPP1
rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bit 15 SMPSLPEN: Enable SMPS low-power mode
When this enable the SMPS low-power mode. When set, it is forbidden to modify the voltage
scaling configuration.
0: SMPS low-power mode disable
1: SMPS low-power mod enable
Bit 14 SMPSFSTEN: Enable SMPS fast soft start
0: SMPS fast soft start disable
1: SMPS fast soft start enable.

Power control (PWR) RM0438
304/2187 RM0438 Rev 8
8.6.5 Power status register 1 ( PWR_SR1)
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
This register is not reset when exiting Standby modes and with the PWRRST bit in the
RCC_APB1RSTR1 register.
Access: 2 additional APB cycles are needed to read this register vs. a standard APB read.
Address offset: 0x10
Bit 13 EXTSMPSEN: Enable external SMPS mode
This bit is used for external SMPS mode, it must be set when the external SMPS switch is
closed.
0: Disable the external SMPS mode
1: Enable external SMPS mode
Bit 12 SMPSBYP: SMPS Bypass mode
This bit is used to force the SMPS step down converter in Bypass mode.
0: SMPS Bypass mode disable
1: SMPS Bypass mode enable
Bits 11:10 Reserved, must be kept at reset value.
Bit 9 VBRS: VBAT battery charging resistor selection
0: Charge VBAT through a 5 kOhms resistor
1: Charge VBAT through a 1.5 kOhms resistor
Bit 8 VBE: VBAT battery charging enable
0: VBAT battery charging disable
1: VBAT battery charging enable
Bits 7:5 Reserved, must be kept at reset value.
Bit 4 WUPP5: Wakeup pin WKUP5 polarity
This bit defines the polarity used for an event detection on external wake-up pin, WKUP5
0: Detection on high level (rising edge)
1: Detection on low level (falling edge)
Bit 3 WUPP4: Wakeup pin WKUP4 polarity
This bit defines the polarity used for an event detection on external wake-up pin, WKUP4
0: Detection on high level (rising edge)
1: Detection on low level (falling edge)
Bit 2 WUPP3: Wakeup pin WKUP3 polarity
This bit defines the polarity used for an event detection on external wake-up pin, WKUP3
0: Detection on high level (rising edge)
1: Detection on low level (falling edge)
Bit 1 WUPP2: Wakeup pin WKUP2 polarity
This bit defines the polarity used for an event detection on external wake-up pin, WKUP2
0: Detection on high level (rising edge)
1: Detection on low level (falling edge)
Bit 0 WUPP1: Wakeup pin WKUP1 polarity
This bit defines the polarity used for an event detection on external wake-up pin, WKUP1
0: Detection on high level (rising edge)
1: Detection on low level (falling edge)

RM0438 Rev 8 305/2187
RM0438 Power control (PWR)
322
Reset value: 0x00A0 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
SMPS
HPRD
Y
Res.
EXTS
MPSR
DY
SMPS
BYPR
DY
Res. Res. Res. SBF Res. Res. Res. WUF5 WUF4 WUF3 WUF2 WUF1
r r r r rrrrr
Bits 31:16 Reserved, must  be kept at reset value.
Bit 15 SMPSHPRDY: SMPS High-power mode ready
This bit is set when the SMPS step down converter is in High-power mode.
Bit 14 Reserved, must be kept at reset value.
Bit 13 EXTSMPSRDY: External SMPS mode ready
This bit is set when the main regulator is ready and can be switched in external SMPS mode.
When set, the external SMPS switch can be closed.
Bit 12 SMPSBYPRDY: SMPS BYPASS ready
This bit is set when the SMPS step down converter is in Bypass mode. It is cleared when the
SMPS exits the Bypass mode when it is switched to High-power or Low-power mode.
Bits 11:9 Reserved, must be kept at reset value.
Bit 8 SBF: Standby flag
This bit is set by hardware when the device enters the Standby mode and is cleared by
setting the CSBF bit in the PWR_SCR register, or by a power-on reset. It is not cleared by the
system reset.
0: The device did not enter the Standby mode
1: The device entered the Standby mode.
Bits 7:5 Reserved, must be kept at reset value.
Bit 4 WUF5: Wakeup flag 5
This bit is set when a wakeup event is detected on wakeup pin, WKUP5. It is cleared by
writing ‘1’ in the CWUF5 bit of the PWR_SCR register.
Bit 3 WUF4: Wakeup flag 4
This bit is set when a wakeup event is detected on wakeup pin,WKUP4. It is cleared by
writing ‘1’ in the CWUF4 bit of the PWR_SCR register.
Bit 2 WUF3: Wakeup flag 3
This bit is set when a wakeup event is detected on wakeup pin, WKUP3. It is cleared by
writing ‘1’ in the CWUF3 bit of the PWR_SCR register.
Bit 1 WUF2: Wakeup flag 2
This bit is set when a wakeup event is detected on wakeup pin, WKUP2. It is cleared by
writing ‘1’ in the CWUF2 bit of the PWR_SCR register.
Bit 0 WUF1: Wakeup flag 1
This bit is set when a wakeup event is detected on wakeup pin, WKUP1. It is cleared by
writing ‘1’ in the CWUF1 bit of the PWR_SCR register.

Power control (PWR) RM0438
306/2187 RM0438 Rev 8
8.6.6 Power status register 2 (PWR_SR2)
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
This register is partially reset when exiting Standby/Shutdown modes.
Address offset: 0x14
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PVMO
4
PVMO
3
PVMO
2
PVMO
1 PVDO VOSF REGLP
F
REGLP
S Res. Res. Res. Res. Res. Res. Res. Res.
rrrrrrr r
Bits 31:16 Reserved, must  be kept at reset value.
Bit 15 PVMO4: Peripheral voltage monitoring output: VDDA vs. 1.8 V
0: VDDA voltage is above PVM4 threshold (around 1.8 V).
1: VDDA voltage is below PVM4 threshold (around 1.8 V).
Note: PVMO4 is cleared when PVM4 is disabled (PVME4 = 0). After enabling PVM4, the
PVM4 output is valid after the PVM4 wakeup time.
Bit 14 PVMO3: Peripheral voltage monitoring output: VDDA vs. 1.62 V
0: VDDA voltage is above PVM3 threshold (around 1.62 V).
1: VDDA voltage is below PVM3 threshold (around 1.62 V).
Note: PVMO3 is cleared when PVM3 is disabled (PVME3 = 0). After enabling PVM3, the
PVM3 output is valid after the PVM3 wakeup time.
Bit 13 PVMO2: Peripheral voltage monitoring output: VDDIO2 vs. 0.9 V
0: VDDIO2 voltage is above PVM2 threshold (around 0.9 V).
1: VDDIO2 voltage is below PVM2 threshold (around 0.9 V).
Note: PVMO2 is cleared when PVM2 is disabled (PVME2 = 0). After enabling PVM2, the
PVM2 output is valid after the PVM2 wakeup time.
Bit 12 PVMO1: Peripheral voltage monitoring output: VDDUSB vs. 1.2 V
0: VDDUSB voltage is above PVM1 threshold (around 1.2 V).
1: VDDUSB voltage is below PVM1 threshold (around 1.2 V).
Note: PVMO1 is cleared when PVM1 is disabled (PVME1 = 0). After enabling PVM1, the
PVM1 output is valid after the PVM1 wakeup time.
Bit 11 PVDO: Programmable voltage detector output
0: VDD is above the selected PVD threshold
1: VDD is below the selected PVD threshold
Bit 10 VOSF: Voltage scaling flag
A delay is required for the internal regulator to be ready after the voltage scaling has been
changed. VOSF indicates that the regulator reached the voltage level defined with VOS bits
of the PWR_CR1 register.
0: The regulator is ready in the selected voltage range
1: The regulator output voltage is changing to the required voltage level

RM0438 Rev 8 307/2187
RM0438 Power control (PWR)
322
8.6.7 Power status clea r register (PWR_SCR)
When the system is secure (TZEN =1), this register is protected against non-secure access
when LPMSEC=1 in the PWR_SECCFGR register. A non-secure read/write access is
RAZ/WI and generates and illegal access event.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: 3 additional APB cycles are needed to write this register vs. a standard APB write.
Address offset: 0x18
Reset value: 0x0000 0000
Bit 9 REGLPF: Low-power regulator flag
This bit is set by hardware when the MCU is in Low-power run mode. When the MCU exits
from the Low-power run mode, this bit remains at 1 until the regulator is ready in Main mode.
A polling on this bit must be done before increasing the product frequency.
This bit is cleared by hardware when the regulator is ready.
0: The regulator is ready in Main mode (MR)
1: The regulator is in Low-power mode (LPR)
Bit 8 REGLPS: Low-power regulator started
This bit provides the information whether the low-power regulator is ready after a power-on
reset or a Standby/Shutdown. If the Standby mode is entered while REGLPS bit is still
cleared, the wakeup from Standby mode time may be increased.
0: The low-power regulator is not ready
1: The low-power regulator is ready
Bits 7:0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. CSBF Res. Res. Res. CWUF5 CWUF4 CWUF3 CWUF2 CWUF1
ww w w w w
Bits 31:9 Reserved, must be kept at reset value.
Bit 8 CSBF: Clear standby flag
Setting this bit clears the SBF flag in the PWR_SR1 register.
Bits 7:5 Reserved, must be kept at reset value.
Bit 4 CWUF5: Clear wakeup flag 5
Setting this bit clears the WUF5 flag in the PWR_SR1 register.
Bit 3 CWUF4: Clear wakeup flag 4
Setting this bit clears the WUF4 flag in the PWR_SR1 register.

Power control (PWR) RM0438
308/2187 RM0438 Rev 8
8.6.8 Power Port A pull-up c ontrol register (PWR_PUCRA)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x20.
Reset value: 0x0000 0000
8.6.9 Power Port A pull-down co ntrol register (PWR_PDCRA)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
Bit 2 CWUF3: Clear wakeup flag 3
Setting this bit clears the WUF3 flag in the PWR_SR1 register.
Bit 1 CWUF2: Clear wakeup flag 2
Setting this bit clears the WUF2 flag in the PWR_SR1 register.
Bit 0 CWUF1: Clear wakeup flag 1
Setting this bit clears the WUF1 flag in the PWR_SR1 register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PU15 PU14 PU13 PU12 PU11 PU10 PU9 PU8 PU7 PU6 PU5 PU4 PU3 PU2 PU1 PU0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PU[15:0]: Port A pull-up bit y (y=0..15)
When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register.
If the corresponding PDy bit is also set, the pull-up is not activated and the pull-down is
activated instead with highest priority.

RM0438 Rev 8 309/2187
RM0438 Power control (PWR)
322
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x24.
Reset value: 0x0000 0000
8.6.10 Power Port B pull-up control register (PWR_PUCRB)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
Address offset: 0x28.
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PD15 PD14 PD13 PD12 PD11 PD10 PD9 PD8 PD7 PD6 PD5 PD4 PD3 PD2 PD1 PD0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PD[15:0]: Port A pull-down bit y (y=0..15)
When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PU15 PU14 PU13 PU12 PU11 PU10 PU9 PU8 PU7 PU6 PU5 PU4 PU3 PU2 PU1 PU0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PU[15:0]: Port B pull-up bit y (y=0..15)
When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register.
The pull-up is not activated if the corresponding PDy bit is also set.

Power control (PWR) RM0438
310/2187 RM0438 Rev 8
8.6.11 Power Port B pull-down control register (PWR_PDCRB)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
Address offset: 0x2C.
Reset value: 0x0000 0000
8.6.12 Power Port C pull-up control register (PWR_PUCRC)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
Address offset: 0x30.
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PD15 PD14 PD13 PD12 PD11 PD10 PD9 PD8 PD7 PD6 PD5 PD4 PD3 PD2 PD1 PD0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PD[15:0]: Port B pull-down bit y (y=0..15)
When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.

RM0438 Rev 8 311/2187
RM0438 Power control (PWR)
322
8.6.13 Power Port C pull-down control register (PWR_PDCRC)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
Address offset: 0x34.
Reset value: 0x0000 0000
8.6.14 Power Port D pull-up control register (PWR_PUCRD)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PU15 PU14 PU13 PU12 PU11 PU10 PU9 PU8 PU7 PU6 PU5 PU4 PU3 PU2 PU1 PU0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PU[15:0]: Port C pull-up bit y (y=0..15)
When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register.
The pull-up is not activated if the corresponding PDy bit is also set.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PD15 PD14 PD13 PD12 PD11 PD10 PD9 PD8 PD7 PD6 PD5 PD4 PD3 PD2 PD1 PD0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PD[15:0]: Port C pull-down bit y (y=0..15)
When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.

Power control (PWR) RM0438
312/2187 RM0438 Rev 8
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x38.
Reset value: 0x0000 0000
8.6.15 Power Port D pull-down control register (PWR_PDCRD)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
Address offset: 0x3C.
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PU15 PU14 PU13 PU12 PU11 PU10 PU9 PU8 PU7 PU6 PU5 PU4 PU3 PU2 PU1 PU0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PU[15:0]: Port D pull-up bit y (y=0..15)
When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register.
The pull-up is not activated if the corresponding PDy bit is also set.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PD15 PD14 PD13 PD12 PD11 PD10 PD9 PD8 PD7 PD6 PD5 PD4 PD3 PD2 PD1 PD0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PD[15:0]: Port D pull-down bit y (y=0..15)
When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.

RM0438 Rev 8 313/2187
RM0438 Power control (PWR)
322
8.6.16 Power Port E pull-up control register (PWR_PUCRE)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x20.
Reset value: 0x0000 0000
8.6.17 Power Port E pull-down control register (PWR_PDCRE)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x44.
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PU15 PU14 PU13 PU12 PU11 PU10 PU9 PU8 PU7 PU6 PU5 PU4 PU3 PU2 PU1 PU0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PU[15:0]: Port E pull-up bit y (y=0..15)
When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register.
The pull-up is not activated if the corresponding PDy bit is also set.

Power control (PWR) RM0438
314/2187 RM0438 Rev 8
8.6.18 Power Port F pull-up control register (PWR_PUCRF)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x48.
Reset value: 0x0000 0000
8.6.19 Power Port F pull-down control register (PWR_PDCRF)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PD15 PD14 PD13 PD12 PD11 PD10 PD9 PD8 PD7 PD6 PD5 PD4 PD3 PD2 PD1 PD0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PD[15:0]: Port E pull-down bit y (y=0..15)
When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PU15 PU14 PU13 PU12 PU11 PU10 PU9 PU8 PU7 PU6 PU5 PU4 PU3 PU2 PU1 PU0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PU[15:0]: Port F pull-up bit y (y=0..15)
When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register.
The pull-up is not activated if the corresponding PFy bit is also set.

RM0438 Rev 8 315/2187
RM0438 Power control (PWR)
322
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x4C.
Reset value: 0x0000 0000
8.6.20 Power Port G pull-up control register (PWR_PUCRG)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x50.
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PD15 PD14 PD13 PD12 PD11 PD10 PD9 PD8 PD7 PD6 PD5 PD4 PD3 PD2 PD1 PD0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PD[15:0]: Port F pull-down bit y (y=0..15)
When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PU15 PU14 PU13 PU12 PU11 PU10 PU9 PU8 PU7 PU6 PU5 PU4 PU3 PU2 PU1 PU0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PU[15:0]: Port G pull-up bit y (y=0..15)
When set, this bit activates the pull-up on PG[y] when APC bit is set in PWR_CR3 register.
The pull-up is not activated if the corresponding PGy bit is also set.

Power control (PWR) RM0438
316/2187 RM0438 Rev 8
8.6.21 Power Port G pull-down control register (PWR_PDCRG)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x54.
Reset value: 0x0000 0000
8.6.22 Power Port H pull-up control register (PWR_PUCRH)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x58.
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PD15 PD14 PD13 PD12 PD11 PD10 PD9 PD8 PD7 PD6 PD5 PD4 PD3 PD2 PD1 PD0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PD[15:0]: Port G pull-down bit y (y=0..15)
When set, this bit activates the pull-down on PG[y] when APC bit is set in PWR_CR3 register.

RM0438 Rev 8 317/2187
RM0438 Power control (PWR)
322
8.6.23 Power Port H pull-down control register (PWR_PDCRH)
When the system is secure (TZEN =1), some register fields are protected against non-
secure access depending on GPIO secure bit configuration. A non-secure read/write access
on secured bits is RAZ/WI.
When the system is not secure (TZEN=0), there is no access restriction.
This register is protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
Access: Additional APB cycles are needed to access this register vs. a standard APB
access (3 for a write and 2 for a read).
This register is not reset when exiting Standby modes and with PWRRST bit in the
RCC_APB1RSTR1 register.
Address offset: 0x5C.
Reset value: 0x0000 0000
8.6.24 Power secure configur ation register (PWR_SECCFGR)
When the system is secure (TZEN =1), this register provides write access security and can
be written only when the access is secure. A non-secure write access is WI and generates
an illegal access event. There are no read restrictions
When the system is not secure (TZEN=0), this register is RAZ/WI.
This register can be protected against non-privileged access when PRIV=1 in the
PWR_PRIVCFGR register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PU15 PU14 PU13 PU12 PU11 PU10 PU9 PU8 PU7 PU6 PU5 PU4 PU3 PU2 PU1 PU0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PU[15:0]: Port H pull-up bit y (y=0..15)
When set, this bit activates the pull-up on PH[y] when APC bit is set in PWR_CR3 register.
The pull-up is not activated if the corresponding PHy bit is also set.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PD15 PD14 PD13 PD12 PD11 PD10 PD9 PD8 PD7 PD6 PD5 PD4 PD3 PD2 PD1 PD0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 PD[15:0]: Port H pull-down bit y (y=0..15)
When set, this bit activates the pull-down on PH[y] when APC bit is set in PWR_CR3 register.

Power control (PWR) RM0438
318/2187 RM0438 Rev 8
Address offset: 0x78.
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. APCSE
C VBSEC VDMSE
C
LPMSE
C Res. Res. Res. WUP5S
EC
WUP4S
EC
WUP3S
EC
WUP2S
EC
WUP1S
EC
rw rw rw rw rw rw rw rw rw
Bits 31:12 Reserved, must  be kept at reset value.
Bit 11 APCSEC: APC security
0: APC bit in PWR_CR3 can be read and written by secure or non-secure access.
1: APC bit in PWR_CR3 can be read and written by secure access only
Bit 10 VBSEC: Voltage battery security
0: VBRS and VBE bits in PWR_CR4 and DPB bit in PWR_CR1 can be read and written by
secure or non-secure access.
1: VBRS and VBE bits in PWR_CR4 and DPB bit in PWR_CR1 can be read and written by
secure access only.
Refer to [Table 76](../tables/table_76.md) for full list of secured bits.
Bit 9 VDMSEC: Voltage detection and monitoring security
0: PWR_CR2 and some bit fields in PWR_CR3 and PWR_CR4 registers can be read and
written by secure or non-secure access.
1: PWR_CR2 and some bit fields in PWR_CR3 and PWR_CR4 registers can be read and
written by secure access only.
Refer to [Table 76](../tables/table_76.md) for full list of secured bits.
Bit 8 LPMSEC: Low-power mode security
0: Low-power mode and WKUPx related bit field in PWR_CR1, PWR_CR3, PWR_CR4 and
PWR_SCR can be read and written by secure or non-secure access.
1: Low-power mode and WKUPx related bit field in PWR_CR1, PWR_CR3, PWR_CR4 and
PWR_SCR can be read and written by secure access only
Note: This bit has a priority over WKUPxSEC bit.
Bits 7:5 Reserved, must be kept at reset value.
Bit 4 WUP5SEC: WKUP5 pin security
0: The bits related to the WKUP5 wakeup pin in PWR_CR3 and PWR_CR4 can be read and
written by secure or non-secure access.
1: The bits related to the WKUP5 wakeup pin in PWR_CR3 and PWR_CR4 can be read and
written by secure access only
Bit 3 WUP4SEC: WKUP4 pin security
0: The bits related to the WKUP4 wakeup pin in PWR_CR3 and PWR_CR4 can be read and
written by secure or non-secure access.
1: The bits related to the WKUP4 wakeup pin in PWR_CR3 and PWR_CR4 can be read and
written by secure access only

RM0438 Rev 8 319/2187
RM0438 Power control (PWR)
322
8.6.25 Power privilege configur ation register (PWR_PRIVCFGR)
This register can be read by both privileged and unprivileged access.
When the system is secure (TZEN =1),this register can be read by secure and non-secure
access. It is write-protected against non-secure write access when at least one bit is set in
the PWR_SECCFGR register
Address offset: 0x80.
Reset value: 0x0000 0000
Bit 2 WUP3SEC: WKUP3 pin security
0: The bits related to the WKUP3 wakeup pin in PWR_CR3 and PWR_CR4 can be read and
written by secure or non-secure access.
1: The bits related to the WKUP3 wakeup pin in PWR_CR3 and PWR_CR4 can be read and
written by secure access only
Bit 1 WUP2SEC: WKUP2 pin security
0: The bits related to the WKUP2 wakeup pin in PWR_CR3 and PWR_CR4 can be read and
written by secure or non-secure access.
1: The bits related to the WKUP2 wakeup pin in PWR_CR3 and PWR_CR4 can be read and
written by secure access only
Bit 0 WUP1SEC: WKUP1 pin security
0: The bits related to the WKUP1 wakeup pin in PWR_CR3 and PWR_CR4 can be read and
written by secure or non-secure access.
1: The bits related to the WKUP1 wakeup pin in PWR_CR3 and PWR_CR4 can be read and
written by secure access only
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. PRIV
rw
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 PRIV: Privilege protection
Set and reset by software.
This bit can be read by both privileged or unprivileged access. when set, it can only be
cleared by a privileged access.
0: All PWR registers can be read and written with privileged or non-privileged access.
1: All PWR registers (except PWR_SR1, PWR_SR2 and PWR_SECFGR registers) can be
read and written only with privileged access. An unprivileged access to PWR registers is
RAZ/WI.
If the PWR is not secure, the PRIV bit can be written by a secure or non-secure privileged
access.
If TrustZone security is enabled (TZEN = 1), if the PWR is secure, the PRIV bit can be written
only by a secure privileged access:
– A non-secure write access generates an illegal access event and write is ignored.
– A secure unprivileged write access on PRIV bit is ignored.

Power control (PWR) RM0438
320/2187 RM0438 Rev 8
8.6.26 PWR register map and reset values
[Table 77](../tables/table_77.md). PWR register map and reset values
Offset Register name
reset value
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
0x00 PWR_CR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
LPR
Res.
Res.
Res.
VOS [1:0]
DBP
Res.
Res.
Res.
Res.
Res.
LPMS [2:0]
Reset value 0 0 1 0 0 0 0
0x04 PWR_CR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
USV
IOSV
Res.
PVME4
PVME3
PVME2
PVME1
PLS [2:0]
PVDE
R e s e t  v a l u e 00 00000000
0x08 PWR_CR3
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
UCPD_DBDIS
UCPD_STDBY
Res
ULPMEN
APC
RRS[1:0]
Res.
Res.
Res.
EWUP5
EWUP4
EWUP3
EWUP2
EWUP1
R e s e t  v a l u e 00 0000 00000
0x0C PWR_CR4
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SMPSLPEN
SMPSFSTEN
EXTSMPSEN
SMPSBYP
Res.
Res.
VBRS
VBE
Res.
Res.
Res.
WUPP5
WUPP4
WUPP3
WUPP2
WUPP1
R e s e t  v a l u e 0000 00 00000
0x10 PWR_SR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SMPSHPRDY
Res.
EXTSMPSRDY
SMPSBYPRDY
Res.
Res.
Res.
SBF
Res.
Res.
Res.
WUF5
WUF4
WUF3
WUF2
WUF1
Reset value 0 0 0 0 0 0 0 0 0
0x14 PWR_SR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PVMO4
PVMO3
PVMO2
PVMO1
PVDO
VOSF
REGLPF
REGLPS
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
R e s e t  v a l u e 00000000
0x18 PWR_SCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CSBF
Res.
Res.
Res.
CWUF5
CWUF4
CWUF3
CWUF2
CWUF1
Reset value 0 0 0 0 0 0
0x20 PWR_PUCRA
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PU15
PU14
PU13
PU12
PU11
PU10
PU9
PU8
PU7
PU6
PU5
PU4
PU3
PU2
PU1
PU0
R e s e t  v a l u e 0000000000000000
0x24 PWR_PDCRA
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PD15
PD14
PD13
PD12
PD11
PD10
PD9
PD8
PD7
PD6
PD5
PD4
PD3
PD2
PD1
PD0
R e s e t  v a l u e 0000000000000000
0x28 PWR_PUCRB
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PU15
PU14
PU13
PU12
PU11
PU10
PU9
PU8
PU7
PU6
PU5
PU4
PU3
PU2
PU1
PU0
R e s e t  v a l u e 0000000000000000

RM0438 Rev 8 321/2187
RM0438 Power control (PWR)
322
0x2C PWR_PDCRB
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PD15
PD14
PD13
PD12
PD11
PD10
PD9
PD8
PD7
PD6
PD5
PD4
PD3
PD2
PD1
PD0
R e s e t  v a l u e 0000000000000000
0x30 PWR_PUCRC
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PU15
PU14
PU13
PU12
PU11
PU10
PU9
PU8
PU7
PU6
PU5
PU4
PU3
PU2
PU1
PU0
R e s e t  v a l u e 0000000000000000
0x34 PWR_PDCRC
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PD15
PD14
PD13
PD12
PD11
PD10
PD9
PD8
PD7
PD6
PD5
PD4
PD3
PD2
PD1
PD0
R e s e t  v a l u e 0000000000000000
0x38 PWR_PUCRD
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PU15
PU14
PU13
PU12
PU11
PU10
PU9
PU8
PU7
PU6
PU5
PU4
PU3
PU2
PU1
PU0
R e s e t  v a l u e 0000000000000000
0x3C PWR_PDCRD
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PD15
PD14
PD13
PD12
PD11
PD10
PD9
PD8
PD7
PD6
PD5
PD4
PD3
PD2
PD1
PD0
R e s e t  v a l u e 0000000000000000
0x20 PWR_PUCRE
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PU15
PU14
PU13
PU12
PU11
PU10
PU9
PU8
PU7
PU6
PU5
PU4
PU3
PU2
PU1
PU0
R e s e t  v a l u e 0000000000000000
0x44 PWR_PDCRE
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PD15
PD14
PD13
PD12
PD11
PD10
PD9
PD8
PD7
PD6
PD5
PD4
PD3
PD2
PD1
PD0
R e s e t  v a l u e 0000000000000000
0x48 PWR_PUCRF
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PU15
PU14
PU13
PU12
PU11
PU10
PU9
PU8
PU7
PU6
PU5
PU4
PU3
PU2
PU1
PU0
R e s e t  v a l u e 0000000000000000
0x4C PWR_PDCRF
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PD15
PD14
PD13
PD12
PD11
PD10
PD9
PD8
PD7
PD6
PD5
PD4
PD3
PD2
PD1
PD0
R e s e t  v a l u e 0000000000000000
0x50 PWR_PUCRG
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PU15
PU14
PU13
PU12
PU11
PU10
PU9
PU8
PU7
PU6
PU5
PU4
PU3
PU2
PU1
PU0
R e s e t  v a l u e 0000000000000000
0x54 PWR_PDCRG
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PD15
PD14
PD13
PD12
PD11
PD10
PD9
PD8
PD7
PD6
PD5
PD4
PD3
PD2
PD1
PD0
R e s e t  v a l u e 0000000000000000
0x58 PWR_PUCRH
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PU15
PU14
PU13
PU12
PU11
PU10
PU9
PU8
PU7
PU6
PU5
PU4
PU3
PU2
PU1
PU0
R e s e t  v a l u e 0000000000000000
0x5C PWR_PDCRH
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PD15
PD14
PD13
PD12
PD11
PD10
PD9
PD8
PD7
PD6
PD5
PD4
PD3
PD2
PD1
PD0
R e s e t  v a l u e 0000000000000000
0x78
PWR_SECCF
GR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
APCSEC
VBSEC
VDMSEC
LPMSEC
Res.
Res.
Res.
WUP5SEC
WUP4SEC
WUP3SEC
WUP2SEC
WUP1SEC
R e s e t  v a l u e 0000 00000
0x80
PWR_PRIVCF
GR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PRIV
Reset value 0
[Table 77](../tables/table_77.md). PWR register map and reset values (continued)
Offset Register name
reset value
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

Power control (PWR) RM0438
322/2187 RM0438 Rev 8
Refer to Section 2.3 on page 86 for the register boundary addresses.
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 21: Architectural Diagram](../figures/figure_21.md)
* [Figure 22: Architectural Diagram](../figures/figure_22.md)
* [Figure 23: Architectural Diagram](../figures/figure_23.md)
* [Figure 24: Architectural Diagram](../figures/figure_24.md)
* [Figure 25: Architectural Diagram](../figures/figure_25.md)
* [Figure 26: Architectural Diagram](../figures/figure_26.md)
* [Figure 27: Architectural Diagram](../figures/figure_27.md)
* [Figure 28: Architectural Diagram](../figures/figure_28.md)
* [Figure 398: Architectural Diagram](../figures/figure_398.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 62: Configuration Matrix](../tables/table_62.md)
* [Table 63: Configuration Matrix](../tables/table_63.md)
* [Table 64: Configuration Matrix](../tables/table_64.md)
* [Table 65: Configuration Matrix](../tables/table_65.md)
* [Table 66: Configuration Matrix](../tables/table_66.md)
* [Table 67: Configuration Matrix](../tables/table_67.md)
* [Table 68: Configuration Matrix](../tables/table_68.md)
* [Table 69: Configuration Matrix](../tables/table_69.md)
* [Table 70: Configuration Matrix](../tables/table_70.md)
* [Table 71: Configuration Matrix](../tables/table_71.md)
* [Table 72: Configuration Matrix](../tables/table_72.md)
* [Table 73: Configuration Matrix](../tables/table_73.md)
* [Table 74: Configuration Matrix](../tables/table_74.md)
* [Table 75: Configuration Matrix](../tables/table_75.md)
* [Table 76: Configuration Matrix](../tables/table_76.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)