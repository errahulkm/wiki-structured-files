# Chapter 42: Tamper and backup registers (TAMP)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 42: Tamper and backup registers (TAMP).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 1447 - 1482
* **Taxonomy Section**: SYSTEM
* **Parent IP Module**: [Backup Registers (BKP)](../system/bkp.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 1447/2187
RM0438 Tamper and backup registers (TAMP)
1482
42 Tamper and backup registers (TAMP)
42.1 Introduction
32 32-bit backup registers are retained in all low-power modes and also in VBAT mode. They
can be used to store sensitive data as their content is protected by an tamper detection
circuit. 8 tamper pins and 5 internal tampers are available for anti-tamper detection. The
external tamper pins can be configured for edge detection, or level detection with or without
filtering, or active tamper which increases the security level by auto checking that the
tamper pins are not externally opened or shorted.
42.2 TAMP main features
• 32 backup registers:
– the backup registers (TAMP_BKPxR) are implemented in the RTC domain that
remains powered-on by VBAT when the VDD power is switched off.
• 8 external tamper detection events.
– Each external event can be config ured to be active or passive.
– External passive tampers with config urable filter and internal pull-up.
• 5 internal tamper events.
• Any tamper detection can generate a RTC timestamp event.
• Any tamper detection can erase the backup registers, SRAM2, ICACHE, PKA SRAM
and cryptographic peripherals.
• TrustZone support:
– Tamper secure or non-secure configuration.
– Backup registers configuration in 3 configurable-size areas:
1 read/write secure area.
1 write secure/read non-secure area.
1 read/write non-secure area.
• Monotonic counter.

Tamper and backup registers (TAMP) RM0438
1448/2187 RM0438 Rev 8
42.3 TAMP functional description
42.3.1 TAMP block diagram
[Figure 399](../figures/figure_399.md). TAMP block diagram
1. The number of external and internal tampers depends on products.
MSv43848V4
Internal
tamper
detection
TAMP_IN1
tamp_itamp1 ITAMP1F
tamp_pclk clock domain
Registers interfacetamp_pclk
IRQ interface
...
tamp_itampy
Monotonic
counter
overflow
ITAMP1
...
ITAMPy(1)
ITAMP8
ITAMPyF
...
ITAMP8F
TAMP1F
Tamper detection
EDGE detection
(passive mode)
LEVEL detection
(passive mode)
COMPARATOR
(active mode)
TAMP_OUT1
TAMP_OUT2
TAMP_OUTx(1)
... tampoutsel1 TAMP2F
Tamper detection
EDGE detection
(passive mode)
LEVEL detection
(passive mode)
COMPARATOR
(active mode)
TAMP_OUT1
TAMP_OUT2
TAMP_OUTx(1)
... tampoutsel2
... TAMPxF
Tamper detection
EDGE detection
(passive mode)
LEVEL detection
(passive mode)
COMPARATOR
(active mode)
TAMP_OUT1
TAMP_OUT2
TAMP_OUTx(1)
... tampoutselx
...
TAMP_OUT1
TAMP_IN2
TAMP_OUT2
TAMP_INx
TAMP_OUTx
...
PRNG
TAMP_IN1
TAMP_IN2
TAMP_INx
TAMP1F
TAMPxF
...ITAMP1F
ITAMPyF
Backup registers Monotonic counter
tamp_it
tamp_erase
tamp_ker_ck
overflow
tamp_ker_ck clock domain
tamp_trg1
tamp_trg2
...
...TAMP1F when TAMP1NOER=0
TAMPxF when TAMPxNOER=0
...ITAMP1F when ITAMP1NOER=0
ITAMPyF when ITAMPyNOER=0
tamp_evt
BKERASE
tamp_tzen

RM0438 Rev 8 1449/2187
RM0438 Tamper and backup registers (TAMP)
1482
42.3.2 TAMP pins a nd internal signals
The TAMP kernel clock is usually the LSE at 32.768 kHz although it is possible to select
other clock sources in the RCC (refer to RCC for more details). Some detections modes are
not available in some low-power modes or VBAT when the selected clock is not LSE (refer to
Section 42.4: TAMP low-power modes for more details.
[Table 318](../tables/table_318.md). TAMP input/output pins
Pin name Signal type Description
TAMP_INx (x = pin index) Input Tamper input pin
TAMP_OUTx (x = pin index) Output Tamper output pin
[Table 319](../tables/table_319.md). TAMP internal input/output signals
Internal signal name Si gnal type Description
tamp_ker_ck Input TAMP kernel clock, connected to rtc_ker_ck
and also named RTCCLK in this document
tamp_pclk Input TAMP APB clock, connected to rtc_pclk
tamp_itamp[y]
(y = signal index) Inputs Internal tamper event sources
tamp_tzen Input TAMP TrustZone enabled
tamp_evt Output
Tamper event detection (internal or external)
The tamp_evt is used to generate a RTC
timestamp event
tamp_erase Output
Device secrets erase request following either
tamper event detection (internal or external) or
the software erase request done by writing
BKERASE to 1
tamp_it Output TAMP interrupt (refer to Section 42.5: TAMP
interrupts for details)
tamp_trg[x]
(x = signal index) Output Tamper detection trigger
[Table 320](../tables/table_320.md). TAMP interconnection
Signal name Source/Destination
tamp_tzen From FLASH option bytes: TZEN
tamp_evt rtc_tamp_evt used to generate a timestamp event
tamp_erase
The tamp_erase signal is used to erase the device secrets listed
hereafter: backup registers, SRAM2, ICACHE, PKA SRAM and
cryptographic peripherals
tamp_itamp1 V DD upper voltage threshold monitoring
tamp_itamp2 Temperature monitoring
tamp_itamp3 LSE monitoring

Tamper and backup registers (TAMP) RM0438
1450/2187 RM0438 Rev 8
The TZEN option bit is used to activate TrustZone in the device.
TZEN = 1: TrustZone activated.
TZEN = 0: TrustZone disabled.
When TrustZone is disabled, the APB access to the TAMP registers are non-secure.
42.3.3 TAMP register  write protection
After system reset, the TAMP registers (including backup registers) are protected against
parasitic write access by the DBP bit in the power control peripheral (refer to the PWR
power control section). DBP bit must be set in order to enable TAMP registers write access.
42.3.4 TAMP secure protection modes
By default after a backup domain power-on reset, all TAMP registers can be read or written
in both secure and non-secure modes, except for the TAMP secure mode control register
(TAMP_SMCR) which can be written in secure mode only when TZEN = 1. The TAMP
protection configuration is not affected by a system reset.
When the TAMPDPROT bit is cleared in the TAMP_SMCR register:
• Writing the TAMP registers is possible only in secure mode, except for the backup
registers which have their own protection setting.
• Reading TAMP_SMCR, TAMP_PRIVCR and TAMP_MISR is always possible in secure
and non-secure modes. All the other TAMP registers can be read only in secure mode,
except for the backup registers which have their own protection setting.
The backup registers protection is configured thanks to BKPRWDPROT[7:0] and
BKPWDPROT[7:0] (refer to [Figure 400](../figures/figure_400.md) below):
[Figure 400](../figures/figure_400.md). Backup registers secure protections
1. l= last backup register index
tamp_itamp5 RTC calendar overflow (rtc_calovf)
tamp_itamp8(1) Monotonic counter overflow
1. This signal is generated in the TAMP peripheral.
[Table 320](../tables/table_320.md). TAMP interconnection (continued)
Signal name Source/Destination
MSv43845V1
Read non-secure
Write non-secure
Read non-secure
Write secure
Read secure
Write secure
TAMP_BKPI(1)R
TAMP_BKPtR (t = BKPWDPROT)
TAMP_BKPzR (z = BKPWDPROT-1)
TAMP_BKPyR (y = BKPRWDPROT)
TAMP_BKPxR (x = BKPRWDPROT-1)
TAMP_BKP0R
Protection Zone 3
Protection Zone 2
Protection Zone 1

RM0438 Rev 8 1451/2187
RM0438 Tamper and backup registers (TAMP)
1482
In case TZEN =1, the bits BKPWPRIV and BKPRWPRIV in the TAMP_PRIVCR can be
written only in secure mode.
A non-secure access to a secure-protected register is denied:
• There is no bus error generated.
• A notification is generated through a flag/interrupt in GTZC_TZIC status register 2
(GTZC_TZIC_SR2).
• When write protected, the bits are not written.
• When read protected they are read as 0.
As soon as at least one function is configured to be secured, the TAMP reset and clock
control is also secured in the RCC.
42.3.5 TAMP privilege protection modes
By default after a backup domain power-on reset, all TAMP registers can be read or written
in both privileged and non-privileged modes, except for the TAMP privilege mode control
register (TAMP_PRIVCR) which can be written in privilege mode only. The TAMP protection
configuration is not affected by a system reset.
When the TAMPPRIV bit is set in the TAMP_PRIVCR register:
• Writing the TAMP registers is possible only in privilege mode, except for the backup
registers which have their own protection setting.
• Reading TAMP_SMCR, TAMP_PRIVCR is always possible in privilege and non-
privilege modes. All the other TAMP registers can be read only in privileged mode,
except for the backup registers which have their own protection setting.
The backup registers protection is configured thanks to BKPRWDPROT[7:0] and
BKPRWPRIV for the protection zone 1, and thanks to BKPRWDPROT[7:0],
BKPWDPROT[7:0] and BKPWPRIV for the protection zone 2 (refer to [Figure 400](../figures/figure_400.md)). In case
TZEN = 0, BKPRWDPROT[7:0] and BKPWDPROT[7:0] in TAMP_SMCR register can be
read and written with non-secure access.
A non-privileged access to a privileged-protected register is denied:
• There is no bus error generated.
• When write protected, the bits are not written.
• When read protected they are read as 0.
42.3.6 Tamper detection
The tamper detection can be configured for the following purposes:
• erase the backup registers and the SRAMs listed in [Table 320](../tables/table_320.md): TAMP interconnection
(default configuration)
• generate an interrupt, capable to wake up from Stop and Standby mode
• generate a hardware trigger for the low-power timers
TAMP backup registers
The backup registers (TAMP_BKPxR) are not reset by system reset or when the device
wakes up from Standby mode.

Tamper and backup registers (TAMP) RM0438
1452/2187 RM0438 Rev 8
The backup registers are reset when a tamper detection event occurs except if the
TAMPxNOER bit is set, or if the TAMPxMSK is set in the TAMP_CR2 register, or if the
ITAMPxNOER bit is set in the TAMP_CR3 register.
The backup registers and the device secrets erased by tamp_erase signal (refer to
[Table 320](../tables/table_320.md): TAMP interconnection) can be reset by software by setting the BKERASE bit in
the TAMP_CR2 register.
Note: The backup registers are also erased when the readout protection of the flash is changed
from level 1 to level 0.
Tamper detection initialization
Each input can be enabled by setting the corresponding TAMPxE bits to 1 in the TAMP_CR
register.
Each TAMP_INx tamper detection input is associated with a flag TAMPxF in the TAMP_SR
register.
When TAMPxMSK is cleared:
The TAMPxF flag is asserted after the tamper event on the pin, with the latency provided
below:
• 3 ck_apre cycles when TAMPFLT differs from 0x0 (level detection with filtering)
• 3 ck_apre cycles when TAMPTS = 1 (timestamp on tamper event)
• No latency when TAMPFLT = 0x0 (edge detection) and TAMPTS = 0
A new tamper occurring on the same pin during this period and as long as TAMPxF is set
cannot be detected.
When TAMPxMSK is set:
A new tamper occurring on the same pin cannot be detected during the latency described
above and 2.5 ck_rtc additional cycles.
By setting the TAMPxIE bit in the TAMP_IER register, an interrupt is generated when a
tamper detection event occurs (when TAMPxF is set). Setting TAMPxIE is not allowed when
the corresponding TAMPxMSK is set.
Trigger output generation on tamper event
The tamper event detection can be used as trigger input by the low-power timers.
When TAMPxMSK bit in cleared in TAMP_CR register, the TAMPxF flag must be cleared by
software in order to allow a new tamper detection on the same pin.
When TAMPxMSK bit is set, the TAMPxF flag is masked, and kept cleared in TAMP_SR
register. This configuration allows the low-power timers in Stop mode to be trigged
automatically, without requiring the system wake-up to perform the TAMPxF clearing. In this
case, the backup registers are not cleared.
This feature is available only when the tamper is configured in the Level detection with
filtering on tamper inputs (passive mode) mode.
Timestamp on tamper event
With TAMPTS set to 1 in the RTC_CR, any tamper event causes a timestamp to occur. In
this case, either the TSF bit or the TSOVF bit is set in RTC_SR, in the same manner as if a

RM0438 Rev 8 1453/2187
RM0438 Tamper and backup registers (TAMP)
1482
normal timestamp event occurs. The affected tamper flag register TAMPxF is set in the
TAMP_SR at the same time that TSF or TSOVF is set in the RTC_SR.
Edge detection on tamper inputs (passive mode)
If the TAMPFLT bits are 00, the TAMP_INx pins generate tamper detection events when
either a rising edge/high level or a falling edge/low level is observed depending on the
corresponding TAMPxTRG bit. The internal pull-up resistors on the TAMP_INx inputs are
deactivated when edge detection is selected.
Caution: When using the edge detection, it is recommended to check by software the tamper pin
level just after enabling the tamper detection (by reading the GPIO registers), and before
writing sensitive values in the backup registers, to ensure that an active edge did not occur
before enabling the tamper event detection.
When TAMPFLT = 00 and TAMPxTRG = 0 (rising edge detection), a tamper event may be
detected by hardware if the tamper input is already at high level before enabling the tamper
detection.
After a tamper event has been detected and cleared, the TAMP_INx should be disabled and
then re-enabled (TAMPxE set to 1) before re-programming the backup registers
(TAMP_BKPxR). This prevents the application from writing to the backup registers while the
TAMP_INx input value still indicates a tamper detection. This is equivalent to a level
detection on the TAMP_INx input.
Note: Tamper detection is still active when V DD power is switched off. To avoid unwanted resetting
of the backup registers, the pin to which the TAMPx is mapped should be externally tied to
the correct level.
Level detection with filtering on tamper inputs (passive mode)
Level detection with filtering is performed by setting TAMPFLT to a non-zero value. A tamper
detection event is generated when either 2, 4, or 8 (depending on TAMPFLT) consecutive
samples are observed at the level designated by the TAMPxTRG bits.
The TAMP_INx inputs are precharged through the I/O internal pull-up resistance before its
state is sampled, unless disabled by setting TAMPPUDIS to 1. The duration of the
precharge is determined by the TAMPPRCH bits, allowing for larger capacitances on the
TAMP_INx inputs.
The trade-off between tamper detection latency and power consumption through the pull-up
can be optimized by using TAMPFREQ to determine the frequency of the sampling for level
detection.
Note: Refer to the microcontroller datasheet fo r the electrical characteristics of the pull-up
resistors.
Active tamper detection
When the TAMPxAM bit is set in the TAMP_ATCR, the tamper events are configured in
active mode, which is based on a comparison between a TAMP_OUTy pin and a TAMP_INx
pin. By default (ATOSHARE = 0) the comparison is made between TAMP_INx and
TAMP_OUTx (y = x). When ATOSHARE bit is set, the same output can be used for several
tamper inputs. Refer to ATOSHARE and ATOSEL bits descriptions in the TAMP_ATCR
register.
Every two CK_ATPER cycles (CK_ATPER = 2ATPER x CK_ATPRE = 2ATPER x 2ATCKSEL
RTCCLK), TAMP_OUTy output pin provides a value provided by a pseudo random number

Tamper and backup registers (TAMP) RM0438
1454/2187 RM0438 Rev 8
generator (PRNG). After outputting this value, the TAMP_OUTy pin outputs its opposite
value one CK_ATPER cycle after.
PRNG is consumed by the selected tamper outputs at a different frequency depending on
the number of selected tamper outputs. The number of selected outputs depends on
TAMPxAM, TAMPxE, ATOSEL and ATOSHARE.
• When only 1 output is selected: PRNG is consumed every 16 CK_ATPER periods.
• When 2 outputs are selected: PRNG is consumed every 8 CK_ATPER periods.
• When 3 or 4 outputs are selected: PRNG is consumed every 4 CK_ATPER periods.
• When 5 or more outputs are selected: PRNG is consumed every 2 CK_ATPER periods
The PRNG needs minimum 9 CK_ATPRE cycles to output a new value. Consequently the
minimum ATPER values for correct functionality are provided in the table below:
The TAMP_INx pin is externally connected to TAMP_OUTy pin. The comparison is made
between TAMP_OUTy output value and TAMP_INx received value, taking into account
feedback delay. In case a comparison mismatch occurs, the TAMPxF bit is set in the
TAMP_SR register.
As an example, TAMP_OUT1 can be used for comparison with TAMP_IN1 and TAMP_IN2
by configuring and enabling both TAMP1 and TAMP2 in active mode, with ATOSHARE = 1,
ATOSEL1 = 00 and ATOSEL2 = 00.
The active tamper can be combined with input filtering when FLTEN = 1. In this case, the
tamper is detected only when 2 comparisons are false, in 4 consecutive comparison
samples.
The pseudo-random generator must be initialized with a seed. This is done by writing
consecutively four 32-bit random values in the TAMP_ATSEEDR register. Programming the
seed automatically sends it to the PRNG. As long as the new seed is transferred and
elaborated by the PRNG, the SEEDF bit is set in the TAMP_ATOR and it is not allowed to
switch off the TAMP APB clock. The duration of the elaboration is up to 184 APB clock
cycles after the forth seed is written. Consequently, after writing a new seed, the user must
wait until SEEDF is cleared before entering low-power modes.
The active tamper outputs are activated only after the first seed is written and the
elaboration is completed. Then new seeds can be written and elaborated during active
tamper activity.
Active tamper initialization
Here is the software procedure to initialize the active tampers after system reset:
[Table 321](../tables/table_321.md). Minimum ATPER value
Number of selected outputs Minimum ATPER
10
21
3 or 4 2
5 or more 3

RM0438 Rev 8 1455/2187
RM0438 Tamper and backup registers (TAMP)
1482
Read INITS in TAMP_ATOR register.
• If INITS = 0x0 (initialization was not done):
a) Write TAMP_ATCR to configure Active ta mper clock, filter and output sharing if
any, and active mode.
b) Write TAMP_CR1 to enable tampers (all the needed tampers must be enabled in
the same write access).
c) Write SEED by writing f our times in the TAMP_ATSEEDR.
d) Wait until SEEDF = 0 in RTC_ATOR. Ba ckup registers are then protected by
active tamper.
• If INITS = 0x1 (initialization already done):
No initialization. To increase randomness a new SEED should be provided regularly.
When a new SEED is provided, wait until SEEDF = 0 before entering a low-power
mode which switches off the RTC APB clock.
• In case the tampers are disabled by software, and re-enabled afterwards, the SEED
must be written after enabling tampers:
a) Write TAMP_CR1 to enable tampers (all the needed tampers must be enabled in
the same write access).
b) Write SEED by writing f our times in the TAMP_ATSEEDR.
c) Wait until SEEDF = 0 in RTC_ATOR. Ba ckup registers are then protected by
active tamper.
42.4 TAMP low-power modes
[Table 322](../tables/table_322.md). Effect of low-power modes on TAMP
Mode Description
Sleep No effect.
TAMP interrupts cause the device to exit the Sleep mode.
Stop
No effect on all features, except for level detection with filtering and active tamper modes which
remain active only when the clock source is LSE or LSI.
Tamper events cause the device to exit the Stop mode.
Standby
No effect on all features, except for level detection with filtering and active tamper modes which
remain active only when the clock source is LSE or LSI.Tamper events cause the device to exit the
Standby mode.
Shutdown
No effect on all features, except for level detection with filtering and active tamper modes which
remain active only when the clock source is LSE. Tamper events cause the device to exit the
Shutdown mode.
[Table 323](../tables/table_323.md). TAMP pins functionality over modes
Pin name Functional in all low-power modes Functional in V BAT mode
TAMP_IN[8:1] Yes only TAMP_IN1,2,3
TAMP_OUT[8:1] Yes only TAMP_OUT2

Tamper and backup registers (TAMP) RM0438
1456/2187 RM0438 Rev 8
42.5 TAMP interrupts
The interrupt channel is set in the interrupt status register or in the secure interrupt status
register depending on its secure mode (TAMPDPROT) configuration. The interrupt output or
the secure interrupt output is also activated.
42.6 TAMP registers
Refer to Section 1.2 on page 77 of the reference manual for a list of abbreviations used in
register descriptions. The peripheral registers can be accessed by words (32-bit).
42.6.1 TAMP control register 1 (TAMP_CR1)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
[Table 324](../tables/table_324.md). Non-secure interrupt requests
Interrupt
acronym
Interrupt
event
Event
flag(1)
Enable
control bit(2)
Interrupt
clear
method
Exit from
Sleep
mode
Exit from
Stop and
Standby
modes
Exit from
Shutdown
mode
TAMP
Tamper x(3) TAMPxF TAMPxIE and
TAMPDPROT=1
Write 1 in
CTAMPxF Yes Yes (4) Yes(5)
Internal
tamper y(3) ITAMPyF TAMPyIE and
TAMPDPROT=1
Write 1 in
CITAMPxF Yes Yes (4) Yes(5)
1. The event flags are in the TAMP_SR register.
2. The interrupt masked flags (resulting from event flags AND enable control bits) are in the TAMP_MISR register.
3. The number of tampers and internal tampers events depend on products.
4. In case of level detection with filtering passive tamper m ode, or in case of active tamper mode, wakeup from Stop and
Standby modes is possible only when the TAMP clock source is LSE or LSI.
5. In case of level detection with filtering passive tamper m ode, or in case of active tamper mode, wakeup from Shutdown
modes is possible only when the TAMP clock source is LSE.
[Table 325](../tables/table_325.md). Secure interrupt requests
Interrupt
acronym
Interrupt
event
Event
flag(1)
Enable
control bit(2)
Interrupt
clear
method
Exit from
Sleep
mode
Exit from
Stop and
Standby
modes
Exit from
Shutdow
n mode
TAMP_S
Tamper x(3) TAMPxF TAMPxIE and
TAMPDPROT=0
Write 1 in
CTAMPxF Yes Yes (4) Yes(5)
Internal
tamper y(3) ITAMPyF TAMPyIE and
TAMPDPROT=0
Write 1 in
CITAMPxF Yes Yes (4) Yes(5)
1. The event flags are in the TAMP_SR register.
2. The interrupt masked flags (resulting from event flags AND enable control bits) are in the TAMP_SMISR register.
3. The number of tampers and internal tampers events depend on products.
4. In case of level detection with filtering passive tamper m ode, or in case of active tamper mode, wakeup from Stop and
Standby modes is possible only when the TAMP clock source is LSE or LSI.
5. In case of level detection with filtering passive tamper m ode, or in case of active tamper mode, wakeup from Shutdown
modes is possible only when the TAMP clock source is LSE.

RM0438 Rev 8 1457/2187
RM0438 Tamper and backup registers (TAMP)
1482
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x00
Backup domain reset value: 0xFFFF 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. ITAMP8
E Res. Res. ITAMP5
E Res. ITAMP3
E
ITAMP2
E
ITAMP1
E
rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. TAMP8
E
TAMP7
E
TAMP6
E
TAMP5
E
TAMP4
E
TAMP3
E
TAMP2
E
TAMP1
E
rw rw rw rw rw rw rw rw
Bits 31:24 Reserved, must be kept at reset value.
Bit 23 ITAMP8E: Internal tamper 8 enable
0: Internal tamper 8 disabled.
1: Internal tamper 8 enabled.
Bit 22 Reserved, must be  kept at reset value.
Bit 21 Reserved, must be  kept at reset value.
Bit 20 ITAMP5E: Internal tamper 5 enable
0: Internal tamper 5 disabled.
1: Internal tamper 5 enabled.
Bit 19 Reserved, must be  kept at reset value.
Bit 18 ITAMP3E: Internal tamper 3 enable
0: Internal tamper 3 disabled.
1: Internal tamper 3 enabled.
Bit 17 ITAMP2E: Internal tamper 2 enable
0: Internal tamper 2 disabled.
1: Internal tamper 2 enabled.
Bit 16 ITAMP1E: Internal tamper 1 enable
0: Internal tamper 1 disabled.
1: Internal tamper 1 enabled.
Bits 15:8 Reserved, must be kept at reset value.
Bit 7 TAMP8E: Tamper detection on TAMP_IN8 enable(1)
0: Tamper detection on TAMP_IN8 is disabled.
1: Tamper detection on TAMP_IN8 is enabled.
Bit 6 TAMP7E: Tamper detection on TAMP_IN7 enable(1)
0: Tamper detection on TAMP_IN7 is disabled.
1: Tamper detection on TAMP_IN7 is enabled.

Tamper and backup registers (TAMP) RM0438
1458/2187 RM0438 Rev 8
42.6.2 TAMP control register 2 (TAMP_CR2)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x04
Backup domain reset value: 0x0000 0000
System reset: not affected
Bit 5 TAMP6E: Tamper detection on TAMP_IN6 enable(1)
0: Tamper detection on TAMP_IN6 is disabled.
1: Tamper detection on TAMP_IN6 is enabled.
Bit 4 TAMP5E: Tamper detection on TAMP_IN5 enable(1)
0: Tamper detection on TAMP_IN5 is disabled.
1: Tamper detection on TAMP_IN5 is enabled.
Bit 3 TAMP4E: Tamper detection on TAMP_IN4 enable(1)
0: Tamper detection on TAMP_IN4 is disabled.
1: Tamper detection on TAMP_IN4 is enabled.
Bit 2 TAMP3E: Tamper detection on TAMP_IN3 enable(1)
0: Tamper detection on TAMP_IN3 is disabled.
1: Tamper detection on TAMP_IN3 is enabled.
Bit 1 TAMP2E: Tamper detection on TAMP_IN2 enable(1)
0: Tamper detection on TAMP_IN2 is disabled.
1: Tamper detection on TAMP_IN2 is enabled.
Bit 0 TAMP1E: Tamper detection on TAMP_IN1 enable(1)
0: Tamper detection on TAMP_IN1 is disabled.
1: Tamper detection on TAMP_IN1 is enabled.
1. Tamper detection mode (selected with TAMP_FLTCR, TA MP_ATCR1, TAMP_ATCR2 registers and TAMPxTRG bits in
TAMP_CR2), must be configured before enabling the tamper detection.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
TAMP8
TRG
TAMP7
TRG
TAMP6
TRG
TAMP5
TRG
TAMP4
TRG
TAMP3
TRG
TAMP2
TRG
TAMP1
TRG
BK
ERASE Res. Res. Res. Res. TAMP3
MSK
TAMP2
MSK
TAMP1
MSK
rw rw rw rw rw rw rw rw w rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. TAMP8
NOER
TAMP7
NOER
TAMP6
NOER
TAMP5
NOER
TAMP4
NOER
TAMP3
NOER
TAMP2
NOER
TAMP1
NOER
rw rw rw rw rw rw rw rw

RM0438 Rev 8 1459/2187
RM0438 Tamper and backup registers (TAMP)
1482
Bit 31 TAMP8TRG: Active level for tamper 8 input (active mode disabled)
0:If TAMPFLT ≠ 00 Tamper 8 input staying low triggers a tamper detection event.
If TAMPFLT = 00 Tamper 8 input rising edge and high level triggers a tamper detection
event.
1:If TAMPFLT ≠ 00 Tamper 8 input staying high triggers a tamper detection event.
If TAMPFLT = 00 Tamper 8 input falling edge and low level triggers a tamper detection
event.
Bit 30 TAMP7TRG: Active level for tamper 7 input (active mode disabled)
0:If TAMPFLT ≠ 00 Tamper 7 input staying low triggers a tamper detection event.
If TAMPFLT = 00 Tamper 7 input rising edge and high level triggers a tamper detection
event.
1:If TAMPFLT ≠ 00 Tamper 7 input staying high triggers a tamper detection event.
If TAMPFLT = 00 Tamper 7 input falling edge and low level triggers a tamper detection
event.
Bit 29 TAMP6TRG: Active level for tamper 6 input (active mode disabled)
0:If TAMPFLT ≠ 00 Tamper 6 input staying low triggers a tamper detection event.
If TAMPFLT = 00 Tamper 6 input rising edge and high level triggers a tamper detection
event.
1:If TAMPFLT ≠ 00 Tamper 6 input staying high triggers a tamper detection event.
If TAMPFLT = 00 Tamper 6 input falling edge and low level triggers a tamper detection
event.
Bit 28 TAMP5TRG: Active level for tamper 5 input (active mode disabled)
0:If TAMPFLT ≠ 00 Tamper 5 input staying low triggers a tamper detection event.
If TAMPFLT = 00 Tamper 5 input rising edge and high level triggers a tamper detection
event.
1:If TAMPFLT ≠ 00 Tamper 5 input staying high triggers a tamper detection event.
If TAMPFLT = 00 Tamper 5 input falling edge and low level triggers a tamper detection
event.
Bit 27 TAMP4TRG: Active level for tamper 4 input (active mode disabled)
0:If TAMPFLT ≠ 00 Tamper 4 input staying low triggers a tamper detection event.
If TAMPFLT = 00 Tamper 4 input rising edge and high level triggers a tamper detection
event.
1:If TAMPFLT ≠ 00 Tamper 4 input staying high triggers a tamper detection event.
If TAMPFLT = 00 Tamper 4 input falling edge and low level triggers a tamper detection
event.
Bit 26 TAMP3TRG: Active level for tamper 3 input
0:If TAMPFLT ≠ 00 Tamper 3 input staying low triggers a tamper detection event.
If TAMPFLT = 00 Tamper 3 input rising edge and high level triggers a tamper detection
event.
1:If TAMPFLT ≠ 00 Tamper 3 input staying high triggers a tamper detection event.
If TAMPFLT = 00 Tamper 3 input falling edge and low level triggers a tamper detection
event.
Bit 25 TAMP2TRG: Active level for tamper 2 input
0:If TAMPFLT ≠ 00 Tamper 2 input staying low triggers a tamper detection event.
If TAMPFLT = 00 Tamper 2 input rising edge and high level triggers a tamper detection
event.
1:If TAMPFLT ≠ 00 Tamper 2 input staying high triggers a tamper detection event.
If TAMPFLT = 00 Tamper 2 input falling edge and low level triggers a tamper detection
event.

Tamper and backup registers (TAMP) RM0438
1460/2187 RM0438 Rev 8
Bit 24 TAMP1TRG: Active level for tamper 1 input
0:If TAMPFLT ≠ 00 Tamper 1 input staying low triggers a tamper detection event.
If TAMPFLT = 00 Tamper 1 input rising edge and high level triggers a tamper detection
event.
1:If TAMPFLT ≠ 00 Tamper 1 input staying high triggers a tamper detection event.
If TAMPFLT = 00 Tamper 1 input falling edge and low level triggers a tamper detection
event.
Bit 23 BKERASE: Backup registers(1) erase
Writing ‘1’ to this bit reset the backup registers(1). Writing 0 has no effect. This bit is always
read as 0.
Bits 22:19 Reserved, must be kept at reset value.
Bit 18 TAMP3MSK: Tamper 3 mask
0: Tamper 3 event generates a trigger event and TAMP3F must be cleared by software to
allow next tamper event detection.
1: Tamper 3 event generates a trigger event. TAMP3F is masked and internally cleared by
hardware. The backup registers(1) are not erased.
The tamper 3 interrupt must not be enabled when TAMP3MSK is set.
Bit 17 TAMP2MSK: Tamper 2 mask
0: Tamper 2 event generates a trigger event and TAMP2F must be cleared by software to
allow next tamper event detection.
1: Tamper 2 event generates a trigger event. TAMP2F is masked and internally cleared by
hardware. The backup registers(1) are not erased.
The tamper 2 interrupt must not be enabled when TAMP2MSK is set.
Bit 16 TAMP1MSK: Tamper 1 mask
0: Tamper 1 event generates a trigger event and TAMP1F must be cleared by software to
allow next tamper event detection.
1: Tamper 1 event generates a trigger event. TAMP1F is masked and internally cleared by
hardware. The backup registers(1) are not erased.
The tamper 1 interrupt must not be enabled when TAMP1MSK is set.
Bits 15:8 Reserved, must be kept at reset value.
Bit 7 TAMP8NOER: Tamper 8 no erase
0: Tamper 8 event erases the backup registers.
1: Tamper 8 event does not erase the backup registers(1).
Bit 6 TAMP7NOER: Tamper 7 no erase
0: Tamper 7 event erases the backup registers.
1: Tamper 7 event does not erase the backup registers(1).
Bit 5 TAMP6NOER: Tamper 6 no erase
0: Tamper 6 event erases the backup registers.
1: Tamper 6 event does not erase the backup registers(1).
Bit 4 TAMP5NOER: Tamper 5 no erase
0: Tamper 5 event erases the backup registers.
1: Tamper 5 event does not erase the backup registers(1).
Bit 3 TAMP4NOER: Tamper 4 no erase
0: Tamper 4 event erases the backup registers.
1: Tamper 4 event does not erase the backup registers(1).

RM0438 Rev 8 1461/2187
RM0438 Tamper and backup registers (TAMP)
1482
42.6.3 TAMP control register 3 (TAMP_CR3)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x08
Backup domain reset value: 0x0000 0000
System reset: not affected
Bit 2 TAMP3NOER: Tamper 3 no erase
0: Tamper 3 event erases the backup registers.
1: Tamper 3 event does not erase the backup registers(1).
Bit 1 TAMP2NOER: Tamper 2 no erase
0: Tamper 2 event erases the backup registers.
1: Tamper 2 event does not erase the backup registers(1).
Bit 0 TAMP1NOER: Tamper 1 no erase
0: Tamper 1 event erases the backup registers.
1: Tamper 1 event does not erase the backup registers(1).
1. The device secrets erased by  tamp_erase signal (refer to [Table 320](../tables/table_320.md): TAMP interconnection).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. ITAMP8
NOER Res. Res. ITAMP5
NOER Res. ITAMP3
NOER
ITAMP2
NOER
ITAMP1
NOER
rw rw rw rw rw
Bits 31:8 Reserved, must be kept at reset value.
Bit 7 ITAMP8NOER: Internal Tamper 8 no erase
0: Internal Tamper 8 event erases the backup registers.
1: Internal Tamper 8 event does not erase the backup registers(1).
Bit 6 Reserved, must be kept at reset value.
Bit 5 Reserved, must be kept at reset value.
Bit 4 ITAMP5NOER: Internal Tamper 5 no erase
0: Internal Tamper 5 event erases the backup registers.
1: Internal Tamper 5 event does not erase the backup registers(1).
Bit 3 Reserved, must be kept at reset value.

Tamper and backup registers (TAMP) RM0438
1462/2187 RM0438 Rev 8
42.6.4 TAMP filter contro l register (TAMP_FLTCR)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x0C
Backup domain reset value: 0x0000 0000
System reset: not affected
Bit 2 ITAMP3NOER: Internal Tamper 3 no erase
0: Internal Tamper 3 event erases the backup registers.
1: Internal Tamper 3 event does not erase the backup registers(1).
Bit 1 ITAMP2NOER: Internal Tamper 2 no erase
0: Internal Tamper 2 event erases the backup registers.
1: Internal Tamper 2 event does not erase the backup registers(1).
Bit 0 ITAMP1NOER: Internal Tamper 1 no erase
0: Internal Tamper 1 event erases the backup registers.
1: Internal Tamper 1 event does not erase the backup registers(1).
1. and the device secrets erased by tamp_erase signal (refer to [Table 320](../tables/table_320.md): TAMP interconnection).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. TAMP
PUDIS
TAMPPRCH
[1:0]
TAMPFLT
[1:0]
TAMPFREQ
[2:0]
rw rw rw rw rw rw rw rw
Bits 31:8 Reserved, must be kept at reset value.
Bit 7 TAMPPUDIS: TAMP_INx pull-up disable
This bit determines if each of the TAMPx pins are precharged before each sample.
0: Precharge TAMP_INx pins before sampling (enable internal pull-up)
1: Disable precharge of TAMP_INx pins.

RM0438 Rev 8 1463/2187
RM0438 Tamper and backup registers (TAMP)
1482
Note: This register concerns only the tamper inputs in passive mode.
42.6.5 TAMP active tamper cont rol register 1 (TAMP_ATCR1)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x10
Backup domain reset value: 0x0007 0000
System reset: not affected
Bits 6:5 TAMPPRCH[1:0]: TAMP_INx precharge duration
These bit determines the duration of time during which the pull-up/is activated before each
sample. TAMPPRCH is valid for each of the TAMP_INx inputs.
0x0: 1 RTCCLK cycle
0x1: 2 RTCCLK cycles
0x2: 4 RTCCLK cycles
0x3: 8 RTCCLK cycles
Bits 4:3 TAMPFLT[1:0]: TAMP_INx filter count
These bits determines the number of consecutive samples at the specified level
(TAMP*TRG) needed to activate a tamper event. TAMPFLT is valid for each of the
TAMP_INx inputs.
0x0: Tamper event is activated on edge of TAMP_INx input transitions to the active level (no
internal pull-up on TAMP_INx input).
0x1: Tamper event is activated after 2 consecutive samples at the active level.
0x2: Tamper event is activated after 4 consecutive samples at the active level.
0x3: Tamper event is activated after 8 consecutive samples at the active level.
Bits 2:0 TAMPFREQ[2:0]: Tamper sampling frequency
Determines the frequency at which each of the TAMP_INx inputs are sampled.
0x0: RTCCLK / 32768 (1 Hz when RTCCLK = 32768 Hz)
0x1: RTCCLK / 16384 (2 Hz when RTCCLK = 32768 Hz)
0x2: RTCCLK / 8192 (4 Hz when RTCCLK = 32768 Hz)
0x3: RTCCLK / 4096 (8 Hz when RTCCLK = 32768 Hz)
0x4: RTCCLK / 2048 (16 Hz when RTCCLK = 32768 Hz)
0x5: RTCCLK / 1024 (32 Hz when RTCCLK = 32768 Hz)
0x6: RTCCLK / 512 (64 Hz when RTCCLK = 32768 Hz)
0x7: RTCCLK / 256 (128 Hz when RTCCLK = 32768 Hz)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
FLTEN ATO
SHARE Res. Res. Res. ATPER[2:0] Res. Res. Res. Res. Res. ATCKSEL[2:0]
rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ATOSEL4[1:0] ATOSEL3[1:0] ATOSEL2[1:0] ATOSEL1[1:0] TAMP8
AM
TAMP7
AM
TAMP6
AM
TAMP5
AM
TAMP4
AM
TAMP3
AM
TAMP2
AM
TAMP1
AM
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

Tamper and backup registers (TAMP) RM0438
1464/2187 RM0438 Rev 8
Bit 31 FLTEN: Active tamper filter enable
0: Active tamper filtering disable
1: Active tamper filtering enable: a tamper event is detected when 2 comparison mismatches
occur out of 4 consecutive samples.
Bit 30 ATOSHARE: Active tamper output sharing
0: Each active tamper input TAMP_INi is compared with its dedicated output TAMP_OUTi
1: Each active tamper input TAMP_INi is compared with TAMPOUTSELx as defined below,
with TAMPOUTSELx defined by ATOSELx bits.
TAMP_IN1 is compared with TAMPOUTSEL1
TAMP_IN2 is compared with TAMPOUTSEL2
TAMP_IN3 is compared with TAMPOUTSEL3
TAMP_IN4 is compared with TAMPOUTSEL4
TAMP_IN5 is compared with TAMPOUTSEL5
TAMP_IN6 is compared with TAMPOUTSEL6
TAMP_IN7 is compared with TAMPOUTSEL7
TAMP_IN8 is compared with TAMPOUTSEL8
Bits 29:27 Reserved, must be kept at reset value.
Bits 26:24 ATPER[2:0]: Active tamper output change period
The tamper output is changed every CK_ATPER = (2ATPER x CK_ATPRE) cycles. Refer to
[Table 321](../tables/table_321.md): Minimum ATPER value.
Bits 23:19 Reserved, must be kept at reset value.
Bits 18:16 ATCKSEL[2:0]: Active tamper RTC asynchronous prescaler clock selection
These bits selects the RTC asynchronous prescaler stage output.The selected clock is
CK_ATPRE.
fCK_ATPRE = fRTCCLK / 2ATCKSEL when (PREDIV_A+1) = 128.
000: RTCCLK is selected
001: RTCCLK/2 is selected when (PREDIV_A+1) = 128 (actually selects 1st flip flop output)
010: RTCCLK/4 is selected when (PREDIV_A+1) = 128 (actually selects 2nd flip flop output)
...
111: RTCCLK/128 is selected when (PREDIV_A+1) = 128 (actually selects 7th flip flop
output)
Note: These bits can be written only when all active tampers are disabled. The write
protection remains for up to 1.5 ck_atpre cycles after all the active tampers are
disable.
Bits 15:14 ATOSEL4[1:0]: Active tamper shared output 4 selection
00: TAMPOUTSEL4 = TAMP_OUT1
01: TAMPOUTSEL4 = TAMP_OUT2
10: TAMPOUTSEL4 = TAMP_OUT3
11: TAMPOUTSEL4 = TAMP_OUT4
The selected output must be available in the package pinout.
Bits 13:12 ATOSEL3[1:0]: Active tamper shared output 3 selection
00: TAMPOUTSEL3 = TAMP_OUT1
01: TAMPOUTSEL3 = TAMP_OUT2
10: TAMPOUTSEL3 = TAMP_OUT3
11: TAMPOUTSEL3 = TAMP_OUT4
The selected output must be available in the package pinout

RM0438 Rev 8 1465/2187
RM0438 Tamper and backup registers (TAMP)
1482
Note: Changing the active tampers configuration in this register is not allowed when a TAMPxAM
bit is set, unless the corresponding TAMPxE bits are all cleared in the TAMP_CR1 register.
All tampers configured in active mode must be enabled at the same time (by setting all
related TAMPxE in the same TAMP_CR1 write).
All tampers configured in active mode must be disabled at the same time (by clearing all
related TAMPxE in the same TAMP_CR1 write).
A minimum duration of 1 CK_ATPRE period must be waited for after disabling the active
tampers and before re-enabling them.
Bits 11:10 ATOSEL2[1:0]: Active tamper shared output 2 selection
00: TAMPOUTSEL2 = TAMP_OUT1
01: TAMPOUTSEL2 = TAMP_OUT2
10: TAMPOUTSEL2 = TAMP_OUT3
11: TAMPOUTSEL2 = TAMP_OUT4
The selected output must be available in the package pinout
Bits 9:8 ATOSEL1[1:0]: Active tamper shared output 1 selection
00: TAMPOUTSEL1 = TAMP_OUT1
01: TAMPOUTSEL1 = TAMP_OUT2
10: TAMPOUTSEL1 = TAMP_OUT3
11: TAMPOUTSEL1 = TAMP_OUT4
The selected output must be available in the package pinout
Bit 7 TAMP8AM: Tamper 8 active mode
0: Tamper 8 detection mode is passive.
1: Tamper 8 detection mode is active.
Bit 6 TAMP7AM: Tamper 7 active mode
0: Tamper 7 detection mode is passive.
1: Tamper 7 detection mode is active.
Bit 5 TAMP6AM: Tamper 6 active mode
0: Tamper 6 detection mode is passive.
1: Tamper 6 detection mode is active.
Bit 4 TAMP5AM: Tamper 5 active mode
0: Tamper 5 detection mode is passive.
1: Tamper 5 detection mode is active.
Bit 3 TAMP4AM: Tamper 4 active mode
0: Tamper 4 detection mode is passive.
1: Tamper 4 detection mode is active.
Bit 2 TAMP3AM: Tamper 3 active mode
0: Tamper 3 detection mode is passive.
1: Tamper 3 detection mode is active.
Bit 1 TAMP2AM: Tamper 2 active mode
0: Tamper 2 detection mode is passive.
1: Tamper 2 detection mode is active.
Bit 0 TAMP1AM: Tamper 1 active mode
0: Tamper 1 detection mode is passive.
1: Tamper 1 detection mode is active.

Tamper and backup registers (TAMP) RM0438
1466/2187 RM0438 Rev 8
42.6.6 TAMP active tamper seed  register (TAMP_ATSEEDR)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x14
Backup domain reset value: 0x0000 0000
System reset: not affected
42.6.7 TAMP active tamper out put register (TAMP_ATOR)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x18
Backup domain reset value: 0x0000 0000
System reset: not affected, except for SEEDF which is reset to 0.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
SEED[31:16]
wwwwwwwwwwwwwwww
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
SEED[15:0]
wwwwwwwwwwwwwwww
Bits 31:0 SEED[31:0]: Pseudo-random generator seed value
This register must be written four times with 32-bit values to provide the 128-bit seed to the
PRNG. Writing to this register automatically sends the seed value to the PRNG.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
INITS SEEDF Res. Res. Res. Res. Res. Res. PRNG[7:0]
rr rrrrrrrr

RM0438 Rev 8 1467/2187
RM0438 Tamper and backup registers (TAMP)
1482
42.6.8 TAMP active tamper cont rol register 2 (TAMP_ATCR2)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x1C
Backup domain reset value: 0x0000 0000
System reset: not affected
Bits 31:16 Reserved, must be kept at reset value.
Bit 15 INITS: Active tamper initialization status
This flag is set by hardware when the PRNG has absorbed the first 128-bit seed, meaning
that the enabled active tampers are functional. This flag is cleared when the active tampers
are disabled.
Bit 14 SEEDF: Seed running flag
This flag is set by hardware when a new seed is written in the TAMP_ATSEEDR. It is cleared
by hardware when the PRNG has absorbed this new seed, and by system reset. The TAMP
APB clock must not be switched off as long as SEEDF is set.
Bits 13:8 Reserved, must be kept at reset value.
Bits 7:0 PRNG[7:0]: Pseudo-random generator value
This field provides the values of the PRNG output. Because of potential inconsistencies due
to synchronization delays, PRNG must be read at least twice. The read value is correct if it is
equal to previous read value.
This field can only be read when the APB is in secure mode.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ATOSEL8[2:0] ATOSEL7[2:0] ATOSEL6[2:0] ATOSEL5[2:0] ATOSEL4[2:0]
ATO
SEL3
[2]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ATOSEL3[1:0] ATOSEL2[2:0] ATOSEL1[2:0] Res. Res. Res. Res. Res. Res. Res. Res.
rw rw rw rw rw rw rw rw

Tamper and backup registers (TAMP) RM0438
1468/2187 RM0438 Rev 8
Bits 31:29 ATOSEL8[2:0]: Active tamper shared output 8 selection
000: TAMPOUTSEL8 = TAMP_OUT1
001: TAMPOUTSEL8 = TAMP_OUT2
010: TAMPOUTSEL8 = TAMP_OUT3
011: TAMPOUTSEL8 = TAMP_OUT4
100: TAMPOUTSEL8 = TAMP_OUT5
101: TAMPOUTSEL8 = TAMP_OUT6
110: TAMPOUTSEL8 = TAMP_OUT7
111: TAMPOUTSEL8 = TAMP_OUT8
The selected output must be available in the package pinout.
Bits 28:26 ATOSEL7[2:0]: Active tamper shared output 7 selection
000: TAMPOUTSEL7 = TAMP_OUT1
001: TAMPOUTSEL7 = TAMP_OUT2
010: TAMPOUTSEL7 = TAMP_OUT3
011: TAMPOUTSEL7 = TAMP_OUT4
100: TAMPOUTSEL7 = TAMP_OUT5
101: TAMPOUTSEL7 = TAMP_OUT6
110: TAMPOUTSEL7 = TAMP_OUT7
111: TAMPOUTSEL7 = TAMP_OUT8
The selected output must be available in the package pinout.
Bits 25:23 ATOSEL6[2:0]: Active tamper shared output 6 selection
000: TAMPOUTSEL6 = TAMP_OUT1
001: TAMPOUTSEL6 = TAMP_OUT2
010: TAMPOUTSEL6 = TAMP_OUT3
011: TAMPOUTSEL6 = TAMP_OUT4
100: TAMPOUTSEL6 = TAMP_OUT5
101: TAMPOUTSEL6 = TAMP_OUT6
110: TAMPOUTSEL6 = TAMP_OUT7
111: TAMPOUTSEL6 = TAMP_OUT8
The selected output must be available in the package pinout.
Bits 22:20 ATOSEL5[2:0]: Active tamper shared output 5 selection
000: TAMPOUTSEL5 = TAMP_OUT1
001: TAMPOUTSEL5 = TAMP_OUT2
010: TAMPOUTSEL5 = TAMP_OUT3
011: TAMPOUTSEL5 = TAMP_OUT4
100: TAMPOUTSEL5 = TAMP_OUT5
101: TAMPOUTSEL5 = TAMP_OUT6
110: TAMPOUTSEL5 = TAMP_OUT7
111: TAMPOUTSEL5 = TAMP_OUT8
The selected output must be available in the package pinout.

RM0438 Rev 8 1469/2187
RM0438 Tamper and backup registers (TAMP)
1482
Bits 19:17 ATOSEL4[2:0]: Active tamper shared output 4 selection
000: TAMPOUTSEL4 = TAMP_OUT1
001: TAMPOUTSEL4 = TAMP_OUT2
010: TAMPOUTSEL4 = TAMP_OUT3
011: TAMPOUTSEL4 = TAMP_OUT4
100: TAMPOUTSEL4 = TAMP_OUT5
101: TAMPOUTSEL4 = TAMP_OUT6
110: TAMPOUTSEL4 = TAMP_OUT7
111: TAMPOUTSEL4 = TAMP_OUT8
The selected output must be available in the package pinout.
Bits 18:17 are the mirror of ATOSEL2[1:0] in the TAMP_ATCR1, and so can also be read or
written through TAMP_ATCR1.
Bits 16:14 ATOSEL3[2:0]: Active tamper shared output 3 selection
000: TAMPOUTSEL3 = TAMP_OUT1
001: TAMPOUTSEL3 = TAMP_OUT2
010: TAMPOUTSEL3 = TAMP_OUT3
011: TAMPOUTSEL3 = TAMP_OUT4
100: TAMPOUTSEL3 = TAMP_OUT5
101: TAMPOUTSEL3 = TAMP_OUT6
110: TAMPOUTSEL3 = TAMP_OUT7
111: TAMPOUTSEL3 = TAMP_OUT8
The selected output must be available in the package pinout.
Bits 15:14 are the mirror of ATOSEL3[1:0] in the TAMP_ATCR1, and so can also be read or
written through TAMP_ATCR1.
Bits 13:11 ATOSEL2[2:0]: Active tamper shared output 2 selection
000: TAMPOUTSEL2 = TAMP_OUT1
001: TAMPOUTSEL2 = TAMP_OUT2
010: TAMPOUTSEL2 = TAMP_OUT3
011: TAMPOUTSEL2 = TAMP_OUT4
100: TAMPOUTSEL2 = TAMP_OUT5
101: TAMPOUTSEL2 = TAMP_OUT6
110: TAMPOUTSEL2 = TAMP_OUT7
111: TAMPOUTSEL2 = TAMP_OUT8
The selected output must be available in the package pinout.
Bits 12:11 are the mirror of ATOSEL2[1:0] in the TAMP_ATCR1, and so can also be read or
written through TAMP_ATCR1.
Bits 10:8 ATOSEL1[2:0]: Active tamper shared output 1 selection
000: TAMPOUTSEL1 = TAMP_OUT1
001: TAMPOUTSEL1 = TAMP_OUT2
010: TAMPOUTSEL1 = TAMP_OUT3
011: TAMPOUTSEL1 = TAMP_OUT4
100: TAMPOUTSEL1 = TAMP_OUT5
101: TAMPOUTSEL1 = TAMP_OUT6
110: TAMPOUTSEL1 = TAMP_OUT7
111: TAMPOUTSEL1 = TAMP_OUT8
The selected output must be available in the package pinout.
Bits 9:8 are the mirror of ATOSEL1[1:0] in the TAMP_ATCR1, and so can also be read or
written through TAMP_ATCR1.
Bits 7:0 Reserved, must be kept at reset value.

Tamper and backup registers (TAMP) RM0438
1470/2187 RM0438 Rev 8
Note: Changing the active tampers configuration in this register is not allowed when a TAMPxAM
bit is set, unless the corresponding TAMPxE bits are all cleared in the TAMP_CR1 register.
All tampers configured in active mode must be enabled at the same time (by setting all
related TAMPxE in the same TAMP_CR1 write).
All tampers configured in active mode must be disabled at the same time (by clearing all
related TAMPxE in the same TAMP_CR1 write).
A minimum duration of 1 CK_ATPRE period must be waited for after disabling the active
tampers and before re-enabling them.
42.6.9 TAMP secure mode  register (TAMP_SMCR)
If TZEN = 1, this register can be written only when the APB access is secure. If TZEN=0,
BKPRWDPROT[7:0] and BKPWDPROT[7:0] can be written with non-secure APB access,
and TAMPDPROT cannot be written.
This register can be globally write-protected, or each bit of this register can be individually
write-protected against non-privileged access depending on the TAMP_PRIVCR
configuration (refer to Section 42.3.5: TAMP privilege protection modes).
Address offset: 0x20
Backup domain reset value: 0x8000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
TAMP
DPROT Res. Res. Res. Res. Res. Res. Res. BKPWDPROT[7:0]
rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. BKPRWDPROT[7:0]
rw rw rw rw rw rw rw rw

RM0438 Rev 8 1471/2187
RM0438 Tamper and backup registers (TAMP)
1482
42.6.10 TAMP privilege mode c ontrol register (TAMP_PRIVCR)
This register can be written only when the APB access is privileged.
When TZEN = 1, this register can be write-protected, or each bit of this register can be
individually write-protected against non-secure access depending on the TAMP_SMCR
configuration (refer to Section 42.3.4: TAMP secure protection modes).
Address offset: 0x24
Backup domain reset value: 0x0000 0000
System reset: not affected
Bit 31 TAMPDPROT: Tamper protection (excluding backup registers)
0: Tamper configuration and interrupt can be written only when the APB access is secure.
1: Tamper configuration and interrupt can be written when the APB access is secure or non-
secure.
Note: Refer to Section 42.3.4: TAMP secure protection modes for details on the read
protection.
Bits 30:24 Reserved, must be kept at reset value.
Bits 23:16 BKPWDPROT[7:0]: Backup registers write protection offset
If TZEN=1: backup registers from TAMP_BKPyR (y = BKPRWDPROT, from 0 to 128) to
TAMP_BKPzR (z = BKPWDPROT-1, from 0 to 128, BKPWDPROT ≥
BKPRWDPROT) can be written only when the APB is in secure mode. They can
be read in secure or non-secure mode. This zone is the protection zone 2.
If TZEN=0: the protection zone 2 can be read and written with non-secure access.
Backup registers from TAMP_BKPtR (t = BKPWDPROT, from 0 to 127) can be read or
written when the APB is in secure or in non-secure mode. This zone is the protection zone 3.
If BKPWDPROT = 0 or if BKPWDPROT ≤ BKPRWDPROT: none of the backup registers
have a secure write access. In these configurations the behavior is equivalent to
BKPWDPROT = BKPRWDPROT.
If BKPWPRIV is set, BKPRWDPROT[7:0] and BKPWDPROT[7:0] can be written only in
privileged mode.
Bits 15:8 Reserved, must be kept at reset value.
Bits 7:0 BKPRWDPROT[7:0]: Backup registers read/write protection offset
If TZEN=1: backup registers from TAMP_BKP0R to TAMP_BKPxR (x = BKPRWDPROT-1,
from 0 to 128) can be read and written only when the APB is in secure mode.
This is the protection zone 1.
If TZEN=0: the protection zone 1 can be read and written with non-secure access.
If BKPRWDPROT = 0 none of the backup registers have a secure read/write access.
If BKPRWPRIV is set, BKPRWDPROT[7:0] can be written only in privileged mode.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
TAMP
PRIV
BKP
WPRIV
BKPR
WPRIV Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res.
rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.

Tamper and backup registers (TAMP) RM0438
1472/2187 RM0438 Rev 8
42.6.11 TAMP interrupt enable register (TAMP_IER)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x2C
Backup domain reset value: 0x0000 0000
System reset: not affected
Bit 31 TAMPPRIV: Tamper privilege protection (excluding backup registers)
0: Tamper configuration and interrupt can be written when the APB is in privileged or non-
privileged mode.
1: Tamper configuration and interrupt can be written only when the APB is in privileged
mode.
Note: Refer to Section 42.3.5: TAMP privilege protection modes for details on the read
protection.
Bit 30 BKPWPRIV: Backup registers zone 2 privilege protection
0: Backup registers zone 2 can be written when the APB is in privileged or non-privileged
mode.
1: Backup registers zone 2 can be written only when the APB is in privileged mode.
Bit 29 BKPRWPRIV: Backup registers zone 1 privilege protection
0: Backup registers zone 1 can be read and written when the APB is in privileged or non-
privileged mode.
1: Backup registers zone 1 can be read and written only when the APB is in privileged mode.
Bits 28:0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. ITAMP8
IE Res. Res. ITAMP5
IE Res. ITAMP3
IE
ITAMP2
IE
ITAMP1
IE
rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. TAMP
8IE
TAMP
7IE
TAMP
6IE
TAMP
5IE
TAMP
4IE
TAMP
3IE
TAMP
2IE
TAMP
1IE
rw rw rw rw rw rw rw rw
Bits 31:24 Reserved, must be kept at reset value.
Bit 23 ITAMP8IE: Internal tamper 8 interrupt enable
0: Internal tamper 8 interrupt disabled.
1: Internal tamper 8 interrupt enabled.
Bit 22 Reserved, must be  kept at reset value.
Bit 21 Reserved, must be  kept at reset value.
Bit 20 ITAMP5IE: Internal tamper 5 interrupt enable
0: Internal tamper 5 interrupt disabled.
1: Internal tamper 5 interrupt enabled.
Bit 19 Reserved, must be  kept at reset value.

RM0438 Rev 8 1473/2187
RM0438 Tamper and backup registers (TAMP)
1482
42.6.12 TAMP status register (TAMP_SR)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
Bit 18 ITAMP3IE: Internal tamper 3 interrupt enable
0: Internal tamper 3 interrupt disabled.
1: Internal tamper 3 interrupt enabled.
Bit 17 ITAMP2IE: Internal tamper 2 interrupt enable
0: Internal tamper 2 interrupt disabled.
1: Internal tamper 2 interrupt enabled.
Bit 16 ITAMP1IE: Internal tamper 1 interrupt enable
0: Internal tamper 1 interrupt disabled.
1: Internal tamper 1 interrupt enabled
Bits 15:8 Reserved, must be kept at reset value.
Bit 7 TAMP8IE: Tamper 8 interrupt enable
0: Tamper 8 interrupt disabled.
1: Tamper 8 interrupt enabled.
Bit 6 TAMP7IE: Tamper 7interrupt enable
0: Tamper 7 interrupt disabled.
1: Tamper 7interrupt enabled.
Bit 5 TAMP6IE: Tamper 6 interrupt enable
0: Tamper 6 interrupt disabled.
1: Tamper 6 interrupt enabled.
Bit 4 TAMP5IE: Tamper 5 interrupt enable
0: Tamper 5 interrupt disabled.
1: Tamper 5 interrupt enabled.
Bit 3 TAMP4IE: Tamper 4 interrupt enable
0: Tamper 4 interrupt disabled.
1: Tamper 4 interrupt enabled.
Bit 2 TAMP3IE: Tamper 3 interrupt enable
0: Tamper 3 interrupt disabled.
1: Tamper 3 interrupt enabled..
Bit 1 TAMP2IE: Tamper 2 interrupt enable
0: Tamper 2 interrupt disabled.
1: Tamper 2 interrupt enabled.
Bit 0 TAMP1IE: Tamper 1 interrupt enable
0: Tamper 1 interrupt disabled.
1: Tamper 1 interrupt enabled.

Tamper and backup registers (TAMP) RM0438
1474/2187 RM0438 Rev 8
TAMP privilege protection modes.
Address offset: 0x30
Backup domain reset value: 0x0000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. ITAMP8
F Res. Res. ITAMP5
F Res. ITAMP3
F
ITAMP2
F
ITAMP1
F
rr r r r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. TAMP
8F
TAMP
7F
TAMP
6F
TAMP
5F
TAMP
4F
TAMP
3F
TAMP
2F
TAMP
1F
rrrrrr rr
Bits 31:24 Reserved, must be kept at reset value.
Bit 23 ITAMP8F: Internal tamper 8 flag
This flag is set by hardware when a tamper detection event is detected on the internal
tamper 8.
Bit 22 Reserved, must be  kept at reset value.
Bit 21 Reserved, must be  kept at reset value.
Bit 20 ITAMP5F: Internal tamper 5 flag
This flag is set by hardware when a tamper detection event is detected on the internal
tamper 5.
Bit 19 Reserved, must be  kept at reset value.
Bit 18 ITAMP3F: Internal tamper 3 flag
This flag is set by hardware when a tamper detection event is detected on the internal
tamper 3.
Bit 17 ITAMP2F: Internal tamper 2 flag
This flag is set by hardware when a tamper detection event is detected on the internal
tamper 2.
Bit 16 ITAMP1F: Internal tamper 1 flag
This flag is set by hardware when a tamper detection event is detected on the internal
tamper 1.
Bits 15:8 Reserved, must be kept at reset value.
Bit 7 TAMP8F: TAMP8 detection flag
This flag is set by hardware when a tamper detection event is detected on the TAMP8 input
Bit 6 TAMP7F: TAMP7 detection flag
This flag is set by hardware when a tamper detection event is detected on the TAMP7 input.
Bit 5 TAMP6F: TAMP6 detection flag
This flag is set by hardware when a tamper detection event is detected on the TAMP6 input.
Bit 4 TAMP5F: TAMP5 detection flag
This flag is set by hardware when a tamper detection event is detected on the TAMP5 input.
Bit 3 TAMP4F: TAMP4 detection flag
This flag is set by hardware when a tamper detection event is detected on the TAMP4 input.

RM0438 Rev 8 1475/2187
RM0438 Tamper and backup registers (TAMP)
1482
42.6.13 TAMP non-secure masked inte rrupt status register (TAMP_MISR)
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x34
Backup domain reset value: 0x0000 0000
System reset: not affected
Bit 2 TAMP3F: TAMP3 detection flag
This flag is set by hardware when a tamper detection event is detected on the TAMP3 input.
Bit 1 TAMP2F: TAMP2 detection flag
This flag is set by hardware when a tamper detection event is detected on the TAMP2 input.
Bit 0 TAMP1F: TAMP1 detection flag
This flag is set by hardware when a tamper detection event is detected on the TAMP1 input.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. ITAMP8
MF Res. Res. ITAMP5
MF Res. ITAMP3
MF
ITAMP2
MF
ITAMP1
MF
rr r r r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. TAMP
8MF
TAMP
7MF
TAMP
6MF
TAMP
5MF
TAMP
4MF
TAMP
3MF
TAMP
2MF
TAMP
1MF
rrrrrr rr
Bits 31:24 Reserved, must be kept at reset value.
Bit 23 ITAMP8MF: Internal tamper 8 non-secure interrupt masked flag
This flag is set by hardware when the internal tamper 8 non-secure interrupt is raised.
Bit 22 Reserved, must be  kept at reset value.
Bit 21 Reserved, must be  kept at reset value.
Bit 20 ITAMP5MF: Internal tamper 5 non-secure interrupt masked flag
This flag is set by hardware when the internal tamper 5 non-secure interrupt is raised.
Bit 19 Reserved, must be  kept at reset value.
Bit 18 ITAMP3MF: Internal tamper 3 non-secure interrupt masked flag
This flag is set by hardware when the internal tamper 3 non-secure interrupt is raised.
Bit 17 ITAMP2MF: Internal tamper 2 non-secure interrupt masked flag
This flag is set by hardware when the internal tamper 2 non-secure interrupt is raised.
Bit 16 ITAMP1MF:Internal tamper 1 non-secure interrupt masked flag
This flag is set by hardware when the internal tamper 1 non-secure interrupt is raised.
Bits 15:8 Reserved, must be kept at reset value.
Bit 7 TAMP8MF: TAMP8 non-secure interrupt masked flag
This flag is set by hardware when the tamper 8 non-secure interrupt is raised.
Bit 6 TAMP7MF: TAMP7 non-secure interrupt masked flag
This flag is set by hardware when the tamper 7 non-secure interrupt is raised.

Tamper and backup registers (TAMP) RM0438
1476/2187 RM0438 Rev 8
42.6.14 TAMP secure masked interr upt status register (TAMP_SMISR)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x38
Backup domain reset value: 0x0000 0000
System reset: not affected
Bit 5 TAMP6MF: TAMP6 non-secure interrupt masked flag
This flag is set by hardware when the tamper 6 non-secure interrupt is raised.
Bit 4 TAMP5MF: TAMP5 non-secure interrupt masked flag
This flag is set by hardware when the tamper 5 non-secure interrupt is raised.
Bit 3 TAMP4MF: TAMP4 non-secure interrupt masked flag
This flag is set by hardware when the tamper 4 non-secure interrupt is raised.
Bit 2 TAMP3MF: TAMP3 non-secure interrupt masked flag
This flag is set by hardware when the tamper 3 non-secure interrupt is raised.
Bit 1 TAMP2MF: TAMP2 non-secure interrupt masked flag
This flag is set by hardware when the tamper 2 non-secure interrupt is raised.
Bit 0 TAMP1MF: TAMP1 non-secure interrupt masked flag
This flag is set by hardware when the tamper 1 non-secure interrupt is raised.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. ITAMP8
MF Res. Res. ITAMP5
MF Res. ITAMP3
MF
ITAMP2
MF
ITAMP1
MF
rr r r r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. TAMP
8MF
TAMP
7MF
TAMP
6MF
TAMP
5MF
TAMP
4MF
TAMP
3MF
TAMP
2MF
TAMP
1MF
rrrrrr rr
Bits 31:24 Reserved, must be kept at reset value.
Bit 23 ITAMP8MF: Internal tamper 8 secure interrupt masked flag
This flag is set by hardware when the internal tamper 8 secure interrupt is raised.
Bit 22 Reserved, must be  kept at reset value.
Bit 21 Reserved, must be  kept at reset value.
Bit 20 ITAMP5MF: Internal tamper 5 secure interrupt masked flag
This flag is set by hardware when the internal tamper 5 secure interrupt is raised.
Bit 19 Reserved, must be  kept at reset value.
Bit 18 ITAMP3MF: Internal tamper 3 secure interrupt masked flag
This flag is set by hardware when the internal tamper 3 secure interrupt is raised.

RM0438 Rev 8 1477/2187
RM0438 Tamper and backup registers (TAMP)
1482
42.6.15 TAMP status cl ear register (TAMP_SCR)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x3C
System reset value: 0x0000 0000
Bit 17 ITAMP2MF: Internal tamper 2 secure interrupt masked flag
This flag is set by hardware when the internal tamper 2 secure interrupt is raised.
Bit 16 ITAMP1MF: Internal tamper 1 secure interrupt masked flag
This flag is set by hardware when the internal tamper 1 secure interrupt is raised.
Bits 15:8 Reserved, must be kept at reset value.
Bit 7 TAMP8MF: TAMP8 secure interrupt masked flag
This flag is set by hardware when the tamper 8 secure interrupt is raised.
Bit 6 TAMP7MF: TAMP7 secure interrupt masked flag
This flag is set by hardware when the tamper 7 secure interrupt is raised.
Bit 5 TAMP6MF: TAMP6 secure interrupt masked flag
This flag is set by hardware when the tamper 6 secure interrupt is raised.
Bit 4 TAMP5MF: TAMP5 secure interrupt masked flag
This flag is set by hardware when the tamper 5 secure interrupt is raised.
Bit 3 TAMP4MF: TAMP4 secure interrupt masked flag
This flag is set by hardware when the tamper 4 secure interrupt is raised.
Bit 2 TAMP3MF: TAMP3 secure interrupt masked flag
This flag is set by hardware when the tamper 3 secure interrupt is raised.
Bit 1 TAMP2MF: TAMP2 secure interrupt masked flag
This flag is set by hardware when the tamper 2 secure interrupt is raised.
Bit 0 TAMP1MF: TAMP1 secure interrupt masked flag
This flag is set by hardware when the tamper 1 secure interrupt is raised.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res.
C
ITAMP
8F
Res. Res.
C
ITAMP
5F
Res.
C
ITAMP
3F
C
ITAMP
2F
C
ITAMP
1F
w w www
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. CTAMP
8F
CTAMP
7F
CTAMP
6F
CTAMP
5F
CTAMP
4F
CTAMP
3F
CTAMP
2F
CTAMP
1F
wwwwwwww

Tamper and backup registers (TAMP) RM0438
1478/2187 RM0438 Rev 8
Bits 31:24 Reserved, must be kept at reset value.
Bit 23 CITAMP8F: Clear ITAMP8 detection flag
Writing 1 in this bit clears the ITAMP8F bit in the TAMP_SR register.
Bit 22 Reserved, must be  kept at reset value.
Bit 21 Reserved, must be  kept at reset value.
Bit 20 CITAMP5F: Clear ITAMP5 detection flag
Writing 1 in this bit clears the ITAMP5F bit in the TAMP_SR register.
Bit 19 Reserved, must be  kept at reset value.
Bit 18 CITAMP3F: Clear ITAMP3 detection flag
Writing 1 in this bit clears the ITAMP3F bit in the TAMP_SR register.
Bit 17 CITAMP2F: Clear ITAMP2 detection flag
Writing 1 in this bit clears the ITAMP2F bit in the TAMP_SR register.
Bit 16 CITAMP1F: Clear ITAMP1 detection flag
Writing 1 in this bit clears the ITAMP1F bit in the TAMP_SR register.
Bits 15:8 Reserved, must be kept at reset value.
Bit 7 CTAMP8F: Clear TAMP8 detection flag
Writing 1 in this bit clears the TAMP8F bit in the TAMP_SR register.
Bit 6 CTAMP7F: Clear TAMP7 detection flag
Writing 1 in this bit clears the TAMP7F bit in the TAMP_SR register.
Bit 5 CTAMP6F: Clear TAMP6 detection flag
Writing 1 in this bit clears the TAMP6F bit in the TAMP_SR register.
Bit 4 CTAMP5F: Clear TAMP5 detection flag
Writing 1 in this bit clears the TAMP5F bit in the TAMP_SR register.
Bit 3 CTAMP4F: Clear TAMP4 detection flag
Writing 1 in this bit clears the TAMP4F bit in the TAMP_SR register.
Bit 2 CTAMP3F: Clear TAMP3 detection flag
Writing 1 in this bit clears the TAMP3F bit in the TAMP_SR register.
Bit 1 CTAMP2F: Clear TAMP2 detection flag
Writing 1 in this bit clears the TAMP2F bit in the TAMP_SR register.
Bit 0 CTAMP1F: Clear TAMP1 detection flag
Writing 1 in this bit clears the TAMP1F bit in the TAMP_SR register.

RM0438 Rev 8 1479/2187
RM0438 Tamper and backup registers (TAMP)
1482
42.6.16 TAMP monotonic counter  register (TAMP_COUNTR)
Address offset: 0x040
Backup domain reset value: 0x0000 0000
System reset: not affected
42.6.17 TAMP configuration register (TAMP_CFGR)
Address offset: 0x50
Backup domain reset value: 0x0000 0000
System reset: not affected
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
COUNT[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
COUNT[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 COUNT[31:0]:
This register is read-only only and is incremented by one when a write access is done to this
register. This register cannot roll-over and is frozen when reaching the maximum value.
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. WUTM
ONEN
VMON
EN
TMON
EN Res.
rw rw rw

Tamper and backup registers (TAMP) RM0438
1480/2187 RM0438 Rev 8
42.6.18 TAMP backup x register (TAMP_BKPxR)
This register can be protected against non-secure access. Refer to Section 42.3.4: TAMP
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 42.3.5:
TAMP privilege protection modes.
Address offset: 0x100 + 0x04 * x, (x = 0 to 31)
Backup domain reset value: 0x0000 0000
System reset: not affected
Bits 31:4 Reserved, must be kept at reset value.
Bit 3 WUTMONEN: voltage and temperature monitor periodic enable by RTC wakeup timer
0: RTC wakeup timer not used to enable voltage and temperature monitors
1: RTC wakeup timer used to enable voltage and temperature monitors
Bit 2 VMONEN: voltage monitor enable
0: voltage monitor disable
1: voltage monitor enable
Bit 1 TMONEN: temperature monitor enable
0: temperature monitor disable
1: temperature monitor enable
Bit 0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
BKP[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
BKP[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw w rw rw
Bits 31:0 BKP[31:0]:
The application can write or read data to and from these registers.
They are powered-on by VBAT when VDD is switched off, so that they are not reset by System
reset, and their contents remain valid when the device operates in low-power mode.
In the default configuration this register is reset on a tamper detection event. It is forced to
reset value as long as there is at least one internal or external tamper flag being set. This
register is also reset when the readout protection (RDP) is disabled.

RM0438 Rev 8 1481/2187
RM0438 Tamper and backup registers (TAMP)
1482
42.6.19 TAMP register map
[Table 326](../tables/table_326.md). TAMP register map and reset values
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
0x00 TAMP_CR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ITAMP8E
Res.
Res.
ITAMP5E
Res.
ITAMP3E
ITAMP2E
ITAMP1E
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TAMP8E
TAMP7E
TAMP6E
TAMP5E
TAMP4E
TAMP3E
TAMP2E
TAMP1E
R e s e t  v a l u e 1 1 111 00000000
0x04 TAMP_CR2
TAMP8TRG
TAMP7TRG
TAMP6TRG
TAMP5TRG
TAMP4TRG
TAMP3TRG
TAMP2TRG
TAMP1TRG
BKERASE
Res.
Res.
Res.
Res.
TAMP3MSK
TAMP2MSK
TAMP1MSK
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TAMP8NOER
TAMP7NOER
TAMP6NOER
TAMP5NOER
TAMP4NOER
TAMP3NOER
TAMP2NOER
TAMP1NOER
R e s e t  v a l u e 000000000 000 00000000
0x08 TAMP_CR3
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ITAMP8NOER
Res.
Res.
ITAMP5NOER
Res.
ITAMP3NOER
ITAMP2NOER
ITAMP1NOER
Reset value 0 0 000
0x0C TAMP_FLTCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TAMPPUDIS
.TAMPPRCH[1:0]
.TAMPFLT[1:0]
TAMPFREQ[2:0]
Reset value 00000000
0x10 TAMP_ATCR1
FLTEN
ATOSHARE
Res.
Res.
Res.
AT-
PER[2:0]
Res.
Res.
Res.
Res.
Res.
ATCK-
SEL[2:0]
ATO
SEL4
[1:0]
ATO
SEL3
[1:0]
ATO
SEL2
[1:0]
ATO
SEL1
[1:0]
TAMP8AM
TAMP7AM
TAMP6AM
TAMP5AM
TAMP4AM
TAMP3AM
TAMP2AM
TAMP1AM
R e s e t  v a l u e 00 000 1110000000000000000
0x14
TAMP_
ATSEEDR SEED[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x18 TAMP_ATOR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
INITS
SEEDF
Res.
Res.
Res.
Res.
Res.
Res. PRNG[7:0]
R e s e t  v a l u e 00 00000000
0x1C TAMP_ATCR2
ATO
SEL8
[2:0]
ATO
SEL7
[2:0]
ATO
SEL6
[2:0]
ATO
SEL5
[2:0]
ATO
SEL4
[2:0]
ATO
SEL3
[2:0]
ATO
SEL2
[2:0]
ATO
SEL1
[2:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
R e s e t  v a l u e 000000000000000000000000
0x20 TAMP_SMCR
TAMPDPROT
Res.
Res.
Res.
Res.
Res.
Res.
Res. BKPWDPROT[7:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. BKPRWDPROT[7:0]
R e s e t  v a l u e 1 00000000 00000000
0x240
TAMP_
PRIVCR
TAMPPRIV
BKPWPRIV
BKPRWPRIV
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Reset value 0 0 0

Tamper and backup registers (TAMP) RM0438
1482/2187 RM0438 Rev 8
Refer to Section 2.3 for the register boundary addresses.
0x2C TAMP_IER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ITAMP8IE
Res.
Res.
ITAMP5IE
Res.
ITAMP3IE
ITAMP2IE
.ITAMP1IE
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TAMP8IE
TAMP7IE
TAMP6IE
TAMP5IE
TAMP4IE
TAMP3IE
TAMP2IE
TAMP1IE
R e s e t  v a l u e 0 0 000 00000000
0x30 TAMP_SR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ITAMP8F
Res.
Res.
ITAMP5F
Res.
ITAMP3F
ITAMP2F
.ITAMP1F
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TAMP8F
TAMP7F
TAMP6F
TAMP5F
TAMP4F
TAMP3F
TAMP2F
TAMP1F
R e s e t  v a l u e 0 0 000 00000000
0x34 TAMP_MISR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ITAMP8MF
Res.
Res.
ITAMP5MF
Res.
ITAMP3MF
ITAMP2MF
ITAMP1MF
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TAMP8MF
TAMP7MF
TAMP6MF
TAMP5MF
TAMP4MF
TAMP3MF
TAMP2MF
TAMP1MF
R e s e t  v a l u e 0 0 000 00000000
0x38 TAMP_SMISR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ITAMP8MF
Res.
Res.
ITAMP5MF
Res.
ITAMP3MF
ITAMP2MF
ITAMP1MF
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TAMP8MF
TAMP7MF
TAMP6MF
TAMP5MF
TAMP4MF
TAMP3MF
TAMP2MF
TAMP1MF
R e s e t  v a l u e 0 0 000 00000000
0x3C TAMP_SCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CITAMP8F
Res.
Res.
CITAMP5F
Res.
CITAMP3F
CITAMP2F
CITAMP1F
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CTAMP8F
CTAMP7F
CTAMP6F
CTAMP5F
CTAMP4F
CTAMP3F
CTAMP2F
CTAMP1F
R e s e t  v a l u e 0 0 000 00000000
0x40
TAMP_
COUNTR COUNT[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x50 TAMP_CFGR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
WUTMONEN
VMONEN
TMONEN
Res.
Reset value 000
0x100 +
0x04*x,
(x=
0 to.31)
TAMP_BKPxR BKP[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
[Table 326](../tables/table_326.md). TAMP register map and reset values (continued)
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
* [Figure 399: Architectural Diagram](../figures/figure_399.md)
* [Figure 400: Architectural Diagram](../figures/figure_400.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 318: Configuration Matrix](../tables/table_318.md)
* [Table 319: Configuration Matrix](../tables/table_319.md)
* [Table 320: Configuration Matrix](../tables/table_320.md)
* [Table 321: Configuration Matrix](../tables/table_321.md)
* [Table 322: Configuration Matrix](../tables/table_322.md)
* [Table 323: Configuration Matrix](../tables/table_323.md)
* [Table 324: Configuration Matrix](../tables/table_324.md)
* [Table 325: Configuration Matrix](../tables/table_325.md)
* [Table 326: Configuration Matrix](../tables/table_326.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)