# Chapter 41: Real-time clock (RTC)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 41: Real-time clock (RTC).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 1395 - 1446
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Real-Time Clock (RTC)](../peripherals/rtc.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 1395/2187
RM0438 Real-time clock (RTC)
1482
41 Real-time clock (RTC)
41.1 Introduction
The RTC provides an automatic wake-up to manage all low-power modes.
The real-time clock (RTC) is an independent BCD timer/counter. The RTC provides a time-
of-day clock/calendar with programmable alarm interrupts.
As long as the supply voltage remains in the operating range, the RTC never stops,
regardless of the device status (Run mode, low-power mode or under reset).
The RTC is functional in VBAT mode.
41.2 RTC main features
The RTC supports the following features (see [Figure 398](../figures/figure_398.md): RTC block diagram):
• Calendar with subsecond, seconds, minutes, hours (12 or 24 format), week day, date,
month, year, in BCD (binary-coded decimal) format.
• Automatic correction for 28, 29 (leap year), 30, and 31 days of the month.
• Two programmable alarms.
• On-the-fly correction from 1 to 32767 RTC clock pulses. This can be used to
synchronize it with a master clock.
• Reference clock detection: a more precise second source clock (50 or 60 Hz) can be
used to enhance the calendar precision.
• Digital calibration circuit with 0.95 ppm resolution, to compensate for quartz crystal
inaccuracy.
• Timestamp feature which can be used to save the calendar content. This function can
be triggered by an event on the timestamp pin, or by a tamper event, or by a switch to
VBAT mode.
• 17-bit auto-reload wake-up timer (WUT) for periodic events with programmable
resolution and period.
• TrustZone support:
– RTC fully securable
– Alarm A, alarm B, wakeup Timer and time stamp individual secure or non-secure
configuration
The RTC is supplied through a switch that takes power either from the VDD supply when
present or from the VBAT pin.
The RTC clock sources can be:
• A 32.768 kHz external crystal (LSE)
• An external resonator or oscillator (LSE)
• The internal low power RC oscillator (LSI, with typical frequency of 32 kHz)
• The high-speed external clock (HSE), divided by a prescaler in the RCC.
The RTC is functional in VBAT mode and in all low-power modes when it is clocked by the
LSE. When clocked by the LSI, the RTC is not functional in VBAT mode, but is functional in
all low-power modes except Shutdown mode.

Real-time clock (RTC) RM0438
1396/2187 RM0438 Rev 8
All RTC events (Alarm, wake-up Timer, Timestamp) can generate an interrupt and wake-up
the device from the low-power modes.
41.3 RTC functional description
41.3.1 RTC block diagram

RM0438 Rev 8 1397/2187
RM0438 Real-time clock (RTC)
1482
[Figure 398](../figures/figure_398.md). RTC block diagram
MSv47492V1
rtc_alrb_trg
Alarm A
RTC_ALRMAR
RTC_ALRMASSR
Alarm B
RTC_ALRMBR
RTC_ALRMBSSR
=
=
rtc_wut_trg
rtc_alra_trg
16-bit wakeup
auto reload timer
RTC_WUTR
Shadow
registers
RTC_TR,
RTC_DR
Output
control
RTC_OUT1
RTC_OUT2
TAMP
TAMPOE
Shadow register
RTC_SSR
Calendar
Synchronous
prescaler
(default = 256)
RTC_PRER
CALIB
OSEL[1:0]
ck_apre
(default 256 Hz)
TAMPALARM
ALARM
rtc_tamp_evt
RTC_REFIN
RTC_TS
Time stamp registers
RTC_TSTR
RTC_TSDR
RTC_TSSR
Time stamp detectionrtc_its
rtc_ker_ck
ck_spre
(default 1 Hz)
Prescaler
2, 4, 8, 16
WUCKSEL[1:0]
TSF
rtc_calovf
ck_apre clock domain
ck_wut clock domain
=0
WUTF
ALRAF
ALRBF
rtc_pclk clock domain
Registers interface
rtc_pclk IRQ interface
rtc_it
ck_wut
rtc_ker_ck clock domain
Smooth
calibration
RTC_CALR
Asynchronous
prescaler
(default = 128)
RTC_PRER
rtc_tzen

Real-time clock (RTC) RM0438
1398/2187 RM0438 Rev 8
41.3.2 RTC pins and internal signals
RTC_OUT1 and RTC_OUT2 select one of the following two outputs:
– CALIB: 512 Hz or 1 Hz clock output (with an LSE frequency of 32.768 kHz). This
output is enabled by setting the COE bit in the RTC_CR register.
– TAMPALRM: This output is the OR between TAMP and ALARM outputs.
ALARM is enabled by configuring the OSEL[1:0] bits in the RTC_CR register which select
the alarm A, alarm B or wake-up outputs. TAMP is enabled by setting the TAMPOE bit in the
RTC_CR register which selects the tamper event outputs.
The RTC kernel clock is usually the LSE at 32.768 kHz although it is possible to select other
clock sources in the RCC (refer to RCC for more details). Some functions are not available
in some low-power modes or VBAT when the selected clock is not LSE. Refer to
Section 41.4: RTC low-power modes for more details.
[Table 308](../tables/table_308.md). RTC input/output pins
Pin name Signal type Description
RTC_TS Input RTC timestamp input
RTC_REFIN Input RTC 50 or 60 Hz reference clock input
RTC_OUT1 Output RTC output 1
RTC_OUT2 Output RTC output 2
[Table 309](../tables/table_309.md). RTC internal input/output signals
Internal signal name Signal type Description
rtc_ker_ck Input RTC kernel clock, al so named RTCCLK in this document
rtc_pclk Input RTC APB clock
rtc_its Input RTC internal timestamp event
rtc_tamp_evt Input Tamper event (internal or external) detected in TAMP
peripheral
rtc_tzen Input RTC TrustZone enabled
rtc_it Output RTC interrupts (refer to Section 41.5: RTC interrupts for
details)
rtc_alra_trg Output RTC alarm A event detection trigger
rtc_alrb_trg Output RTC alarm B event detection trigger
rtc_wut_trg Output RTC wake-up timer event detection trigger
rtc_calovf Output
RTC calendar overflow: this signal is generated when the
RTC calendar reaches its maximum value, on the 31st of
December 99, at 23:59:59. The calendar is then frozen and
cannot overflow.

RM0438 Rev 8 1399/2187
RM0438 Real-time clock (RTC)
1482
The TZEN option bit is used to activate TrustZone in the device.
TZEN = 1: TrustZone activated.
TZEN = 0: TrustZone disabled.
When TrustZone is disabled, the APB access to the RTC registers are non-secure.
The triggers outputs can be used as triggers for other peripherals.
41.3.3 GPIOs controlled  by the RTC and TAMP
The GPIOs included in the battery backup domain (VBAT) are directly controlled by the
peripherals providing functions on these I/Os, whatever the GPIO configuration.
Both RTC and TAMP peripherals provide functions on these I/Os (refer to Section 42:
Tamper and backup registers (TAMP)).
RTC_OUT1, RTC_TS, TAMP_IN1 and TAMP_OUT2 are mapped on the same pin (PC13).
The RTC and TAMP functions mapped on PC13 are available in all low-power modes and in
VBAT mode.
The output mechanism follows the priority order shown in [Table 311](../tables/table_311.md).
[Table 310](../tables/table_310.md). RTC interconnection
Signal name Source/destination
rtc_its From power controller (PWR):  main power loss/switch to VBAT detection output
rtc_tamp_evt From TAMP peripheral: tamp_evt
rtc_tzen From FLASH option bytes: TZEN
rtc_wut_trg To temperature sensor power-on (when cleared) and down (when set)
rtc_calovf To TAMP peripheral: tamp_itamp5
[Table 311](../tables/table_311.md). RTC pin PC13 configuration(1)
PC13 Pin function
OSEL[1:0]
(ALARM output enable)
TAMPOE
(TAMPER output enable)
COE
(CALIB output enable)
OUT2EN
TAMPALRM_TYPE
TAMPALRM_PU
TAMP2E & TAMP2AM
TAMP1E
(TAMP_IN1 input enable)
TSE
(RTC_TS input enable)
TAMPALRM output
Push-Pull
01 or
10 or
11
0
Don’t
care
Don’t
care 00 Don’t
care
Don’t
care
Don’t
care00 1
01 or
10 or
11
1

Real-time clock (RTC) RM0438
1400/2187 RM0438 Rev 8
TAMPALRM
output
Open-Drain(2)
No pull
01 or
10 or
11
0
Don’t
care
Don’t
care 10 Don’t
care
Don’t
care
Don’t
care00 1
01 or
10 or
11
1
Internal
pull-up
01 or
10 or
11
0
Don’t
care
Don’t
care 11 Don’t
care
Don’t
care
Don’t
care00 1
01 or
10 or
11
1
CALIB output PP 00 0 1 0 Don’t
care
Don’t
care
Don’t
care
Don’t
care
Don’t
care
TAMP_OUT2 output PP 00 0 0 0 Don’t
care
Don’t
care 1 Don’t
care
Don’t
care
TAMP_IN1 input floating
00 0 0 Don’t
care
Don’t
care
Don’t
care 01000 0 1
1Don’t
care
Don’t
care 0
RTC_TS and TAMP_IN1
input floating
00 0 0 Don’t
care
Don’t
care
Don’t
care
0
1100 0 1
1
0
Don’t
care
Don’t
care 00
RTC_TS input floating
00 0 0 Don’t
care
Don’t
care
Don’t
care
0
0100 0 1
1
0
Don’t
care
Don’t
care 00
[Table 311](../tables/table_311.md). RTC pin PC13 configuration(1) (continued)
PC13 Pin function
OSEL[1:0]
(ALARM output enable)
TAMPOE
(TAMPER output enable)
COE
(CALIB output enable)
OUT2EN
TAMPALRM_TYPE
TAMPALRM_PU
TAMP2E & TAMP2AM
TAMP1E
(TAMP_IN1 input enable)
TSE
(RTC_TS input enable)

RM0438 Rev 8 1401/2187
RM0438 Real-time clock (RTC)
1482
In addition, it is possible to output RTC_OUT2 on PB2 pin thanks to OUT2EN bit. This
output is not available in VBAT mode. The different functions are mapped on RTC_OUT1 or
on RTC_OUT2 depending on OSEL, COE and OUT2EN configuration, as shown in table
[Table 312](../tables/table_312.md).
41.3.4 RTC secure protection modes
By default after a backup domain power-on reset, all RTC registers can be read or written in
both secure and non-secure modes, except for the RTC secure mode control register
(RTC_SMCR) which can be written in secure mode only. The RTC protection configuration
is not affected by a system reset.
Wakeup pin or Standard
GPIO
00 0 0 Don’t
care
Don’t
care
Don’t
care
0
0000 0 1
1
0
Don’t
care
Don’t
care 00
1. OD: open drain; PP: push-pull.
2. In this configuration the GPIO must be configured in input.
[Table 311](../tables/table_311.md). RTC pin PC13 configuration(1) (continued)
PC13 Pin function
OSEL[1:0]
(ALARM output enable)
TAMPOE
(TAMPER output enable)
COE
(CALIB output enable)
OUT2EN
TAMPALRM_TYPE
TAMPALRM_PU
TAMP2E & TAMP2AM
TAMP1E
(TAMP_IN1 input enable)
TSE
(RTC_TS input enable)
[Table 312](../tables/table_312.md). RTC_OUT mapping
OSEL[1:0] bits
ALARM
output enable)
COE bit (CALIB
output enable)
OUT2EN
bit
RTC_OUT1 on
PC13
RTC_OUT2 on
PB2
00 0
0
--
00 1 CALIB -
01 or 10 or 11 Don’t care TAMPALRM -
00 0
1
--
00 1 - CALIB
01 or 10 or 11 0 - TAMPALRM
01 or 10 or 11 1 TAMPALRM CALIB

Real-time clock (RTC) RM0438
1402/2187 RM0438 Rev 8
When the DECPROT bit is cleared in the RTC_SMCR register:
• Writing the RTC registers is possible only in secure mode.
• Reading RTC_SMCR, RTC_PRIVCR, RTC_MISR, RTC_TR, RTC_DR, RTC_SSR,
RTC_PRER and RTC_CALR is always possible in secure and non-secure modes. All
the other RTC registers can be read only in secure mode.
When the DECPROT bit is set, it is still possible to protect some of the registers by clearing
dedicated INITDPROT, CALDPROT, TSDPROT, WUTDPROT, ALRADPROT or
ALRBDPROT control bits. If all these bits are also set, all the RTC registers can be read and
written in secure and non-secure mode.
• When INITDPROT is cleared:
– RTC_TR, RTC_DR, RTC_PRER registers, plus INIT in RTC_ICSR, FMT control
bits in RTC_CR and INITPRIV in the RTC_PRIVCR can be written only in secure
mode.
– These registers and control bits can be read in secure and non-secure mode.
• When CALDPROT is cleared:
– RTC_SHIFTR and RTC_CALR registers,  plus ADD1H, SUB1H and REFCKON
control bits in the RTC_CR and CALPRIV in the RTC_PRIVCR can be written only
in secure mode.
– These registers and control bits can be read in secure and non-secure mode.
• When ALRADPROT is cleared:
– RTC_ALRMAR, RTC_ALRMASSR register s, plus ALRAE, ALRAIE in the
RTC_CR, CALRAF in the RTC_SCR, ALRAF in RTC_SR, and ALRAMF in
RTC_SMISR can be read and written only in secure mode.
– ALRAPRIV in the RTC_PRIVCR can be written only in secure mode
• When ALRBDPROT is cleared:
– RTC_ALRMBR, RTC_ALRMBSSR registers,  plus ALRBE and ALRBIE in the
RTC_CR, CALRBF in the RTC_SCR, ALRBF in RTC_SR, and ALRBMF in
RTC_SMISR can be read and written only in secure mode.
– ALRBPRIV in the RTC_PRIVCR can be written only in secure mode.
• When WUTDPROT is cleared:
– RTC_WUTR register, plus WUTE, WUTI E and WUCKSEL control bits in the
RTC_CR, CWUTF in the RTC_SCR, WUTF in RTC_SR, and WUTMF in
RTC_SMISR can be read and written only in secure mode.
– WUTPRIV in the RTC_PRIVCR can be written only in secure mode
• When TSDPROT is cleared:
– RTC_TSTR, RTC_TSDR and RTC_TSSSR re gisters, plus TAMPTS, ITSE, TSE,
TSIE, TSEDGE control bits in the RTC_CR, CITSF, CTSOVF and CTSF bits in the
RTC_SCR, TSF, TSOVF and ITSF in RTC_SR, and TSMF, TSOVMF and ITSMF
in RTC_SMISR can be read and written only in secure mode.
– TSPRIV in the RTC_PRIVCR can be  written only in secure mode
A non-secure access to a secure-protected register is denied:
• There is no bus error generated.
• In case the register has a global protection: a notification is generated through a
flag/interrupt in GTZC_TZIC status register 2 (GTZC_TZIC_SR2). In case only a few

RM0438 Rev 8 1403/2187
RM0438 Real-time clock (RTC)
1482
bits of the register are protected (for registers with mixed features such as RTC_CR...),
no notification is generated.
• When write protected, the bits are not written.
• When read protected they are read as 0.
As soon as at least one function is configured to be secured, the RTC reset and clock
control is also secured in the RCC.
41.3.5 RTC privilege protection modes
By default after a backup domain power-on reset, all RTC registers can be read or written in
both privileged and non-privileged modes, except for the RTC privilege mode control
register (RTC_PRIVCR) which can be written in privilege mode only. The RTC protection
configuration is not affected by a system reset.
When the PRIV bit is set in the RTC_PRIVCR register:
• Writing the RTC registers is possible only in privileged mode.
• Reading the RTC_SMCR, RTC_PRIVCR, RTC_TR, RTC_DR, RTC_SSR, RTC_PRER
and RTC_CALR is always possible in privilege and non-privilege modes. All the other
RTC registers can be read only in privilege mode.
When the PRIV bit is cleared, it is still possible to protect some of the registers by setting
dedicated INITPRIV, CALPRIV, TSPRIV, WUTPRIV, ALRAPRV or ALRBPRIV control bits. If
all these bits are also cleared, all the RTC registers can be read or written in privilege and
non-privilege modes.
• When INITPRIV is set:
– RTC_TR, RTC_DR, RTC_PRER registers, plus INIT in RTC_ICSR and FMT
control bits in RTC_CR, plus INITDPROT in the RTC_SMCR can be written only in
privilege mode.
– These registers and control bits can be read in privilege and non-privilege mode.
• When CALPRIV is set:
– RTC_SHIFTR and RTC_CALR registers,  plus ADD1H, SUB1H and REFCKON
control bits in the RTC_CR, plus CALDPROT in the RTC_SMCR can be written
only in privilege mode.
– These registers and control bits can be read in privilege and non-privilege mode.
• When ALRAPRIV is set:
– RTC_ALRMAR, RTC_ALRMASSR and RTC_ ALRABINR registers, plus ALRAE
and ALRAIE in the RTC_CR, and CALRAF in the RTC_SCR, ALRAF in RTC_SR,
and ALRAMF in RTC_MISR and RTC_SMISR can be read and written only in
privilege mode.
– ALRADPROT in the RTC_SMCR can be  written only in privilege mode.
• When ALRBPRIV is set:
– RTC_ALRMBR, RTC_ALRMBSSR and RTC_ ALRBBINR registers, plus ALRBE
and ALRBIE in the RTC_CR, and CALRBF in the RTC_SCR, ALRBF in RTC_SR,

Real-time clock (RTC) RM0438
1404/2187 RM0438 Rev 8
and ALRBMF in RTC_MISR and RTC_SMISR can be read and written only in
privilege mode.
– ALRBDPROT in the RTC_SMCR can be  written only in privilege mode.
• When WUTPRIV is set:
– RTC_WUTR register, plus WUTE, WUTI E and WUCKSEL control bits in the
RTC_CR, and CWUTF in the RTC_SCR, WUTF in RTC_SR, and WUTMF in
RTC_MISR and RTC_SMISR can be read and written only in privilege mode.
– WUTDPROT in the RTC_SMCR can be written only in privilege mode.
• When TSPRIV is set:
– RTC_TSTR, RTC_TSDR and RTC_TSSSR re gisters, plus TAMPTS, ITSE, TSE,
TSIE, TSEDGE control bits in the RTC_CR, CITSF, CTSOVF and CTSF bits in the
RTC_SCR, TSF, TSOVF and ITSF in RTC_SR, and TSMF, TSOVMF and ITSMF
in RTC_MISR and RTC_SMISR can be read and written only in privilege mode.
– TSDPROT in the RTC_SMCR can be written only in privilege mode.
A non-privileged access to a privileged-protected register is denied:
• There is no bus error generated.
• When write protected, the bits are not written.
• When read protected they are read as 0.
41.3.6 Clock and prescalers
The RTC clocks must respect this ratio: frequency(PCLK) ≥ 2 × frequency(RTCCLK).
The RTC clock source (RTCCLK) is selected through the clock controller among the LSE
clock, the LSI oscillator clock, and the HSE clock. For more information on the RTC clock
source configuration, refer to “Reset and clock control (RCC)”.
A programmable prescaler stage generates a 1 Hz clock which is used to update the
calendar. To minimize power consumption, the prescaler is split into 2 programmable
prescalers (see [Figure 398](../figures/figure_398.md): RTC block diagram):
• A 7-bit asynchronous prescaler configured through the PREDIV_A bits of the
RTC_PRER register.
• A 15-bit synchronous prescaler configured through the PREDIV_S bits of the
RTC_PRER register.
Note: When both prescalers are used, it is recommended to configure the asynchronous prescaler
to a high value to minimize consumption.
The asynchronous prescaler division factor is set to 128, and the synchronous division
factor to 256, to obtain an internal clock frequency of 1 Hz (ck_spre) with an LSE frequency
of 32.768 kHz.
The minimum division factor is 1 and the maximum division factor is 222.
This corresponds to a maximum input frequency of around 4 MHz.
fck_apre is given by the following formula:
fCK_APRE
fRTCCLK
PREDIV_A 1+---------------------------------------=

RM0438 Rev 8 1405/2187
RM0438 Real-time clock (RTC)
1482
The ck_apre clock is used to clock the binary RTC_SSR subseconds downcounter. When it
reaches 0, RTC_SSR is reloaded with the content of PREDIV_S.
fck_spre is given by the following formula:
The ck_spre clock can be used either to update the calendar or as timebase for the 16-bit
wake-up auto-reload timer. To obtain short timeout periods, the 16-bit wake-up auto-reload
timer can also run with the RTCCLK divided by the programmable 4-bit asynchronous
prescaler (see Section 41.3.10: Periodic auto-wake-up for details).
41.3.7 Real-time clock and calendar
The RTC calendar time and date registers are accessed through shadow registers which
are synchronized with PCLK (APB clock). They can also be accessed directly in order to
avoid waiting for the synchronization duration.
• RTC_SSR for the subseconds
• RTC_TR for the time
• RTC_DR for the date
Every RTCCLK periods, the current calendar value is copied into the shadow registers, and
the RSF bit of RTC_ICSR register is set (see Section 41.6.12: RTC shift control register
(RTC_SHIFTR)). The copy is not performed in Stop and Standby mode. When exiting these
modes, the shadow registers are updated after up to 4 RTCCLK periods.
When the application reads the calendar registers, it accesses the content of the shadow
registers. It is possible to make a direct access to the calendar registers by setting the
BYPSHAD control bit in the RTC_CR register. By default, this bit is cleared, and the user
accesses the shadow registers.
When reading the RTC_SSR, RTC_TR or RTC_DR registers in BYPSHAD = 0 mode, the
frequency of the APB clock (fAPB) must be at least 7 times the frequency of the RTC clock
(fRTCCLK).
The shadow registers are reset by system reset.
41.3.8 Calendar ultra-low power mode
It is possible to reduce drastically the RTC power consumption by setting the LPCAL bit in
the RTC_CALR register. In this configuration, the whole RTC is clocked by ck_apre only
instead of both RTCCLK and ck_apre. Consequently, some flags delays are longer, and the
calibration window is longer (refer to Section : Calibration ultra-low-power mode).
The LPCAL bit is ignored (assumed to be 0) when asynchronous prescaler division factor
(PREDIV_A+1) is not a power of 2.
Switching from LPCAL=0 to LPCAL=1 or from LPCAL=1 to LPCAL=0 is not immediate and
requires a few ck_apre periods to complete.
41.3.9 Programmable alarms
The RTC unit provides programmable alarm: alarm A and alarm B. The description below is
given for alarm A, but can be translated in the same way for alarm B.
fCK_SPRE
fRTCCLK
PREDIV_S 1+() PREDIV_A 1+()×-----------------------------------------------------------------------------------------------=

Real-time clock (RTC) RM0438
1406/2187 RM0438 Rev 8
The programmable alarm function is enabled through the ALRAE bit in the RTC_CR
register.
The ALRAF is set to 1 if the calendar subseconds, seconds, minutes, hours, date or day
match the values programmed in the alarm registers RTC_ALRMASSR and
RTC_ALRMAR. Each calendar field can be independently selected through the MSKx bits
of the RTC_ALRMAR register, and through the MASKSSx bits of the RTC_ALRMASSR
register.
The alarm interrupt is enabled through the ALRAIE bit in the RTC_CR register.
Caution: If the seconds field is selected (MSK1 bit reset in RTC_ALRMAR), the synchronous
prescaler division factor set in the RTC_PRER register must be at least 3 to ensure correct
behavior.
Alarm A and alarm B (if enabled by bits OSEL[1:0] in RTC_CR register) can be routed to the
TAMPALRM output. TAMPALRM output polarity can be configured through bit POL the
RTC_CR register.
41.3.10 Periodic auto-wake-up
The periodic wake-up flag is generated by a 16-bit programmable auto-reload down-
counter. The wake-up timer range can be extended to 17 bits.
The wake-up function is enabled through the WUTE bit in the RTC_CR register.
The wake-up timer clock input ck_wut can be:
• RTC clock (RTCCLK) divided by 2, 4, 8, or 16.
When RTCCLK is LSE (32.768 kHz), this allows the wake-up interrupt period to be
configured from 122 µs to 32 s, with a resolution down to 61 µs.
• ck_spre (usually 1 Hz internal clock).
When ck_spre frequency is 1 Hz, this allows a wake-up time to be achieved from 1 s to
around 36 hours with one-second resolution. This large programmable time range is
divided in 2 parts:
– from 1 s to 18 hours when WUCKSEL [2:1] = 10
– and from around 18 h to 36 h when WUCKSEL[2:1] = 11. In this last case 2 16 is
added to the 16-bit counter current value. When the initialization sequence is
complete (see Programming the wake-up timer on page 1409), the timer starts
counting down. When the wake-up function is enabled, the down-counting
remains active in low-power modes. In addition, when it reaches 0, the WUTF flag
is set in the RTC_SR register, and the wake-up counter is automatically reloaded
with its reload value (RTC_WUTR register value).
Depending on WUTOCLR in the RTC_WUTR register, the WUTF flag must either be
cleared by software (WUTOCLR = 0x0000), or the WUTF is automatically cleared by
hardware when the auto-reload down counter reaches WUTOCLR value
(0x0000<WUTOCLR<=WUT).
The wake-up flag is output on an internal signal rtc_wut that can be used by other
peripherals (refer to section Section 41.3.1: RTC block diagram).
When the periodic wake-up interrupt is enabled by setting the WUTIE bit in the RTC_CR
register, it can exit the device from low-power modes.

RM0438 Rev 8 1407/2187
RM0438 Real-time clock (RTC)
1482
The periodic wake-up flag can be routed to the TAMPALRM output provided it has been
enabled through bits OSEL[1:0] of RTC_CR register. TAMPALRM output polarity can be
configured through the POL bit in the RTC_CR register.
System reset, as well as low-power modes (Sleep, Stop and Standby) have no influence on
the wake-up timer.
41.3.11 RTC initialization and configuration
RTC register access
The RTC registers are 32-bit registers. The APB interface introduces two wait states in RTC
register accesses except on read accesses to calendar shadow registers when
BYPSHAD = 0.
RTC register write protection
After system reset, the RTC registers are protected against parasitic write access by the
DBP bit in the power control peripheral (refer to the PWR power control section). DBP bit
must be set in order to enable RTC registers write access.
After Backup domain reset, some of the RTC registers are write-protected: RTC_TR,
RTC_DR, RTC_PRER, RTC_CALR, RTC_SHIFTR, the bit INIT in RTC_ICSR and the bits
FMT, SUB1H, ADD1H, REFCKON in RTC_CR.
The following steps are required to unlock the write protection on the protected RTC
registers.
1. Write 0xCA into the RTC_WPR register.
2. Write 0x53 into the RTC_WPR register.
Writing a wrong key reactivates the write protection.
The protection mechanism is not affected by system reset.
The registers protected by INITPRIV are write-protected by the INIT KEY.
The registers protected by CALDPRIV are write-protected by the CAL KEY.
In case PRIV or INITPRIV is set in the RTC_PRIVCR, and/or DPROT or INITDPROT is
cleared in the RTC_SMCR: the INIT KEY is unlocked and locked only if the write accesses
into the RTC_WPR register are done in the privilege and security mode defined by PRIV,
INITPRIV, DPROT, INITDPROT configuration.
In case PRIV or CALPRIV is set in the RTC_PRIVCR, and/or DPROT or CALDPROT is
cleared in the RTC_SMCR: the CAL KEY is unlocked and locked only if the write accesses
into the RTC_WPR register are done in the privilege and security mode defined by PRIV,
CALPRIV, DPROT, CALDPROT configuration.
Calendar initialization and configuration
To program the initial time and date calendar values, including the time format and the
prescaler configuration, the following sequence is required:
1. Set INIT bit to 1 in the RTC_ ICSR register to enter initialization mode. In this mode, the
calendar counter is stopped and its value can be updated.
2. Poll INITF bit of in the RTC_ICSR regist er. The initialization phase mode is entered
when INITF is set to 1.

Real-time clock (RTC) RM0438
1408/2187 RM0438 Rev 8
If LPCAL=0: INITF is set around 2 RTCCLK cycles after INIT bit is set.
If LPCAL=1: INITF is set up to 2 ck_apre cycle after INIT bit is set.
3. To generate a 1  Hz clock for the calendar counter, program both the prescaler factors
in RTC_PRER register.
4. Load the initial time and date values in the shadow registers (RTC_TR and RTC_DR),
and configure the time format (12 or 24 hours) through the FMT bit in the RTC_CR
register.
5. Exit the initialization mode by clearing the INIT bit. The actual calendar counter value is
then automatically loaded.
If LPCAL=0: the counting restarts after 4 RTCCLK clock cycles.
If LPCAL=1: the counting restarts after up to 2 RTCCLK + 1 ck_apre.
When the initialization sequence is complete, the calendar starts counting.
RTC_SSR contains the value of the synchronous prescaler counter. This allows one to
calculate the exact time being maintained by the RTC down to a resolution of 1 /
(PREDIV_S + 1) seconds. As a consequence, the resolution can be improved by increasing
the synchronous prescaler value (PREDIV_S[14:0]). The maximum resolution allowed
(30.52 μs with a 32768 Hz clock) is obtained with PREDIV_S set to 0x7FFF.
However, increasing PREDIV_S means that PREDIV_A must be decreased in order to
maintain the synchronous prescaler output at 1 Hz. In this way, the frequency of the
asynchronous prescaler output increases, which may increase the RTC dynamic
consumption. The RTC dynamic consumption is optimized for PREDIV_A+1 being a power
of 2.
Note: After a system reset, the application can read the INITS flag in the RTC_ICSR register to
check if the calendar has been initialized or not. If this flag equals 0, the calendar has not
been initialized since the year field is set at its Backup domain reset default value (0x00).
To read the calendar after initialization, the software must first check that the RSF flag is set
in the RTC_ICSR register.
Daylight saving time
The daylight saving time management is performed through bits SUB1H, ADD1H, and BKP
of the RTC_CR register.
Using SUB1H or ADD1H, the software can subtract or add one hour to the calendar in one
single operation without going through the initialization procedure.
In addition, the software can use the BKP bit to memorize this operation.
Programming the alarm
A similar procedure must be followed to program or update the programmable alarms. The
procedure below is given for alarm A but can be translated in the same way for alarm B.
1. Clear ALRAE in RTC_CR to disable alarm A.
2. Program the alarm A regist ers (RTC_ALRMASSR/RTC_ALRMAR).
3. Set ALRAE in the RTC_CR register to enable alarm A again.
Note: Each change of the RTC_CR register is taken into account after around 2 RTCCLK clock
cycles due to clock synchronization.

RM0438 Rev 8 1409/2187
RM0438 Real-time clock (RTC)
1482
Programming the wake-up timer
The following sequence is required to configure or change the wake-up timer auto-reload
value (WUT[15:0] in RTC_WUTR):
1. Clear WUTE in RTC_CR to disable the wake-up timer.
2. Poll WUTWF until it is set in RTC_ICSR to make sure the access to wake-up auto-
reload counter and to WUCKSEL[2:0] bits is allowed. This step must be skipped in
calendar initialization mode.
If WUCKSEL[2] = 0: WUTWF is set around 1 ck_wut + 1 RTCCLK cycles after WUTE
bit is cleared.
If WUCKSEL[2] = 1: WUTWF is set up to 1 ck_apre + 1 RTCCLK cycles after WUTE bit
is cleared.
3. Program the wake-up auto-reload value WUT[15:0], WUTOCLR[15:0] and the wake-up
clock selection (WUCKSEL[2:0] bits in RTC_CR). Set WUTE in RTC_CR to enable the
timer again. The wake-up timer restarts down-counting.
If WUCKSEL[2] = 0: WUTWF is cleared around 1 ck_wut + 1 RTCCLK cycles after
WUTE bit is set.
If WUCKSEL[2] = 1: WUTWF is cleared up to 1 ck_apre + 1 RTCCLK cycles after
WUTE bit is set.
41.3.12 Reading the calendar
When BYPSHAD control bit is cleared in the RTC_CR register
To read the RTC calendar registers (RTC_SSR, RTC_TR and RTC_DR) properly, the APB1
clock frequency (fPCLK) must be equal to or greater than seven times the RTC clock
frequency (fRTCCLK). This ensures a secure behavior of the synchronization mechanism.
If the APB1 clock frequency is less than seven times the RTC clock frequency, the software
must read the calendar time and date registers twice. If the second read of the RTC_TR
gives the same result as the first read, this ensures that the data is correct. Otherwise a third
read access must be done. In any case the APB1 clock frequency must never be lower than
the RTC clock frequency.
The RSF bit is set in RTC_ICSR register each time the calendar registers are copied into
the RTC_SSR, RTC_TR and RTC_DR shadow registers. The copy is performed every
RTCCLK cycle. To ensure consistency between the 3 values, reading either RTC_SSR or
RTC_TR locks the values in the higher-order calendar shadow registers until RTC_DR is
read. In case the software makes read accesses to the calendar in a time interval smaller
than 1 RTCCLK periods: RSF must be cleared by software after the first calendar read, and
then the software must wait until RSF is set before reading again the RTC_SSR, RTC_TR
and RTC_DR registers.
After waking up from low-power mode (Stop or Standby), RSF must be cleared by software.
The software must then wait until it is set again before reading the RTC_SSR, RTC_TR and
RTC_DR registers.
The RSF bit must be cleared after wake-up and not before entering low-power mode.
After a system reset, the software must wait until RSF is set before reading the RTC_SSR,
RTC_TR and RTC_DR registers. Indeed, a system reset resets the shadow registers to
their default values.

Real-time clock (RTC) RM0438
1410/2187 RM0438 Rev 8
After an initialization (refer to Calendar initialization and configuration on page 1407): the
software must wait until RSF is set before reading the RTC_SSR, RTC_TR and RTC_DR
registers.
After synchronization (refer to Section 41.3.14: RTC synchronization): the software must
wait until RSF is set before reading the RTC_SSR, RTC_TR and RTC_DR registers.
When the BYPSHAD control bit is set in the RTC_CR register (bypass shadow
registers)
Reading the calendar registers gives the values from the calendar counters directly, thus
eliminating the need to wait for the RSF bit to be set. This is especially useful after exiting
from low-power modes (Stop or Standby), since the shadow registers are not updated
during these modes.
When the BYPSHAD bit is set to 1, the results of the different registers might not be
coherent with each other if an RTCCLK edge occurs between two read accesses to the
registers. Additionally, the value of one of the registers may be incorrect if an RTCCLK edge
occurs during the read operation. The software must read all the registers twice, and then
compare the results to confirm that the data is coherent and correct. Alternatively, the
software can just compare the two results of the least-significant calendar register.
Note: While BYPSHAD = 1, instruct ions which read the calendar registers require one extra APB
cycle to complete.
41.3.13 Resetting the RTC
The calendar shadow registers (RTC_SSR, RTC_TR and RTC_DR) and some bits of the
RTC status register (RTC_ICSR) are reset to their default values by all available system
reset sources.
On the contrary, the following registers are reset to their default values by a Backup domain
reset and are not affected by a system reset: the RTC current calendar registers, the RTC
control register (RTC_CR), the prescaler register (RTC_PRER), the RTC calibration register
(RTC_CALR), the RTC shift register (RTC_SHIFTR), the RTC timestamp registers
(RTC_TSSSR, RTC_TSTR and RTC_TSDR), the wake-up timer register (RTC_WUTR),
and the alarm A and alarm B registers (RTC_ALRMASSR/RTC_ALRMAR and
RTC_ALRMBSSR/RTC_ALRMBR).
In addition, when clocked by LSE, the RTC keeps on running under system reset if the reset
source is different from the Backup domain reset one (refer to RCC for details about RTC
clock sources not affected by system reset). When a Backup domain reset occurs, the RTC
is stopped and all the RTC registers are set to their reset values.
41.3.14 RTC synchronization
The RTC can be synchronized to a remote clock with a high degree of precision. After
reading the sub-second field (RTC_SSR or RTC_TSSSR), a calculation can be made of the
precise offset between the times being maintained by the remote clock and the RTC. The
RTC can then be adjusted to eliminate this offset by “shifting” its clock by a fraction of a
second using RTC_SHIFTR.
The RTC can be finely adjusted using the RTC shift control register (RTC_SHIFTR). Writing
to RTC_SHIFTR can shift (either delay or advance) the clock with a resolution of 1 ck_apre
period.

RM0438 Rev 8 1411/2187
RM0438 Real-time clock (RTC)
1482
The shift operation consists in adding the SUBFS[14:0] value to the synchronous prescaler
counter SS[15:0]: this delays the clock.
If at the same time the ADD1S bit is set, this results in adding one second and at the same
time subtracting a fraction of second, so this advances the clock.
As soon as a shift operation is initiated by a write to the RTC_SHIFTR register, the SHPF
flag is set by hardware to indicate that a shift operation is pending. This bit is cleared by
hardware as soon as the shift operation has completed.
Caution: Before initiating a shift operation, the user must check that SS[15] = 0 in order to ensure that
no overflow occurs.
Caution: This synchronization feature is not compatible with the reference clock detection feature:
firmware must not write to RTC_SHIFTR when REFCKON = 1.
41.3.15 RTC reference clock detection
The update of the RTC calendar can be synchronized to a reference clock, RTC_REFIN,
which is usually the mains frequency (50 or 60 Hz). The precision of the RTC_REFIN
reference clock should be higher than the 32.768 kHz LSE clock. When the RTC_REFIN
detection is enabled (REFCKON bit of RTC_CR set to 1), the calendar is still clocked by the
LSE, and RTC_REFIN is used to compensate for the imprecision of the calendar update
frequency (1 Hz).
Each 1 Hz clock edge is compared to the nearest RTC_REFIN clock edge (if one is found
within a given time window). In most cases, the two clock edges are properly aligned. When
the 1 Hz clock becomes misaligned due to the imprecision of the LSE clock, the RTC shifts
the 1 Hz clock a bit so that future 1 Hz clock edges are aligned. Thanks to this mechanism,
the calendar becomes as precise as the reference clock.
The RTC detects if the reference clock source is present by using the 256 Hz clock
(ck_apre) generated from the 32.768 kHz quartz. The detection is performed during a time
window around each of the calendar updates (every 1 s). The window equals 7 ck_apre
periods when detecting the first reference clock edge. A smaller window of 3 ck_apre
periods is used for subsequent calendar updates.
Each time the reference clock is detected in the window, the asynchronous prescaler which
outputs the ck_spre clock is forced to reload. This has no effect when the reference clock
and the 1 Hz clock are aligned because the prescaler is being reloaded at the same
moment. When the clocks are not aligned, the reload shifts future 1 Hz clock edges a little
for them to be aligned with the reference clock.
If the reference clock halts (no reference clock edge occurred during the 3 ck_apre window),
the calendar is updated continuously based solely on the LSE clock. The RTC then waits for
the reference clock using a large 7 ck_apre period detection window centered on the
ck_spre edge.
When the RTC_REFIN detection is enabled, PREDIV_A and PREDIV_S must be set to their
default values:
• PREDIV_A = 0x007F
• PREVID_S = 0x00FF
Note: RTC_REFIN clock detection is  not available in Standby mode.

Real-time clock (RTC) RM0438
1412/2187 RM0438 Rev 8
41.3.16 RTC smooth digital calibration
The RTC frequency can be digitally calibrated with a resolution of about 0.954 ppm with a
range from -487.1 ppm to +488.5 ppm. The correction of the frequency is performed using
series of small adjustments (adding and/or subtracting individual ck_cal pulses).
If LPCAL=0: ck_cal = RTCCLK
If LPCAL=1: ck_cal = ck_apre
These adjustments are fairly well distributed so that the RTC is well calibrated even when
observed over short durations of time.
Calibration ultra-low-power mode
The calibration consumption can be reduced by setting the LPCAL bit in the RTC calibration
register (RTC_CALR). In this case, the calibration mechanism is applied on ck_apre instead
of RTCCLK. The resulting accuracy is the same, but the calibration is performed during a
calibration cycle of about 220 x PREDIV_A x RTCCLK pulses instead of 220 RTCCLK pulses
when LPCAL=0.
Smooth calibration mechanism
The smooth calibration register (RTC_CALR) specifies the number of ck_cal clock cycles to
be masked during the calibration cycle:
• Setting the bit CALM[0] to 1 causes exactly one pulse to be masked during the
calibration cycle.
• Setting CALM[1] to 1 causes two additional cycles to be masked
• Setting CALM[2] to 1 causes four additional cycles to be masked
• and so on up to CALM[8] set to 1 which causes 256 clocks to be masked.
Note: CALM[8:0] (RTC_CALR) specifies the number of ck_cal pulses to be masked during the
calibration cycle. Setting the bit CALM[0] to 1 causes exactly one pulse to be masked during
the calibration cycle at the moment when cal_cnt[19:0] is 0x80000; CALM[1] = 1 causes two
other cycles to be masked (when cal_cnt is 0x40000 and 0xC0000); CALM[2] = 1 causes
four other cycles to be masked (cal_cnt = 0x20000/0x60000/0xA0000/ 0xE0000); and so on
up to CALM[8] = 1 which causes 256 clocks to be masked (cal_cnt = 0xXX800).
While CALM allows the RTC frequency to be reduced by up to 487.1 ppm with fine
resolution, the bit CALP can be used to increase the frequency by 488.5 ppm. Setting CALP
to 1 effectively inserts an extra ck_cal pulse every 211 ck_cal cycles, which means that 512
clocks are added during every calibration cycle.
Using CALM together with CALP, an offset ranging from -511 to +512 ck_cal cycles can be
added during the calibration cycle, which translates to a calibration range of -487.1 ppm to
+488.5 ppm with a resolution of about 0.954 ppm.
The formula to calculate the effective calibrated frequency (FCAL) given the input frequency
(FRTCCLK) is as follows:
FCAL = FRTCCLK x [1 + (CALP x 512 - CALM) / (220 + CALM - CALP x 512)]
Caution: PREDIV_A must be greater or equal to 3.
Calibration when PREDIV_A < 3
The CALP bit can not be set to 1 when the asynchronous prescaler value (PREDIV_A bits in
RTC_PRER register) is less than 3. If CALP was already set to 1 and PREDIV_A bits are

RM0438 Rev 8 1413/2187
RM0438 Real-time clock (RTC)
1482
set to a value less than 3, CALP is ignored and the calibration operates as if CALP was
equal to 0.
It is however possible to perform a calibration with PREDIV_A less than 3, the synchronous
prescaler value (PREDIV_S) should be reduced so that each second is accelerated by 8
ck_cal clock cycles, which is equivalent to adding 256 clock cycles every calibration cycle.
As a result, between 255 and 256 clock pulses (corresponding to a calibration range from
243.3 to 244.1 ppm) can effectively be added during each calibration cycle using only the
CALM bits.
With a nominal RTCCLK frequency of 32768 Hz, when PREDIV_A equals 1 (division factor
of 2), PREDIV_S should be set to 16379 rather than 16383 (4 less). The only other
interesting case is when PREDIV_A equals 0, PREDIV_S should be set to 32759 rather
than 32767 (8 less).
If PREDIV_S is reduced in this way, the formula given the effective frequency of the
calibrated input clock is as follows:
FCAL = FRTCCLK x [1 + (256 - CALM) / (220 + CALM - 256)]
In this case, CALM[7:0] equals 0x100 (the midpoint of the CALM range) is the correct
setting if RTCCLK is exactly 32768.00 Hz.
Verifying the RTC calibration
It is recommended to verify the RTC calibration with LPCAL=0, in order to have a 32 second
calibration cycle.
RTC precision is ensured by measuring the precise frequency of RTCCLK and calculating
the correct CALM value and CALP values. An optional 1 Hz output is provided to allow
applications to measure and verify the RTC precision.
Measuring the precise frequency of the RTC over a limited interval can result in a
measurement error of up to 2 RTCCLK clock cycles over the measurement period,
depending on how the digital calibration cycle is aligned with the measurement period.
However, this measurement error can be eliminated if the measurement period is the same
length as the calibration cycle period. In this case, the only error observed is the error due to
the resolution of the digital calibration.
• By default, the calibration cycle period is 32 seconds.
Using this mode and measuring the accuracy of the 1 Hz output over exactly 32 seconds
guarantees that the measure is within 0.477 ppm (0.5 RTCCLK cycles over 32 seconds,
due to the limitation of the calibration resolution).
• CALW16 bit of the RTC_CALR register can be set to 1 to force a 16- second calibration
cycle period.
In this case, the RTC precision can be measured during 16 seconds with a maximum error
of 0.954 ppm (0.5 RTCCLK cycles over 16 seconds). However, since the calibration
resolution is reduced, the long term RTC precision is also reduced to 0.954 ppm: CALM[0]
bit is stuck at 0 when CALW16 is set to 1.
• CALW8 bit of the RTC_CALR register can be set to 1 to force a 8-second calibration
cycle period.
In this case, the RTC precision can be measured during 8 seconds with a maximum error of
1.907 ppm (0.5 RTCCLK cycles over 8 s). The long term RTC precision is also reduced to
1.907 ppm: CALM[1:0] bits are stuck at 00 when CALW8 is set to 1.

Real-time clock (RTC) RM0438
1414/2187 RM0438 Rev 8
Re-calibration on-the-fly
The calibration register (RTC_CALR) can be updated on-the-fly while RTC_ICSR/INITF = 0,
by using the follow process:
1. Poll the RTC_ICSR/RECALPF (re-calibration pending flag).
2. If it is set to 0, write a new value to  RTC_CALR, if necessary. RECALPF is then
automatically set to 1
3. Within three ck_apre cycles after the writ e operation to RTC_CALR, the new calibration
settings take effect.
41.3.17 Timestamp function
Timestamp is enabled by setting the TSE or ITSE bits of RTC_CR register to 1.
When TSE is set:
The calendar is saved in the timestamp registers (RTC_TSSSR, RTC_TSTR, RTC_TSDR)
when a timestamp event is detected on the RTC_TS pin.
When TAMPTS is set:
The calendar is saved in the timestamp registers (RTC_TSSSR, RTC_TSTR, RTC_TSDR)
when a tamper event is detected on the TAMP_INx pinx.
When ITSE is set:
The calendar is saved in the timestamp registers (RTC_TSSSR, RTC_TSTR, RTC_TSDR)
when an internal timestamp event is detected. The internal timestamp event is generated by
the switch to the VBAT supply.
When a timestamp event occurs, due to internal or external event, the timestamp flag bit
(TSF) in RTC_SR register is set. In case the event is internal, the ITSF flag is also set in
RTC_SR register.
By setting the TSIE bit in the RTC_CR register, an interrupt is generated when a timestamp
event occurs.
If a new timestamp event is detected while the timestamp flag (TSF) is already set, the
timestamp overflow flag (TSOVF) flag is set and the timestamp registers (RTC_TSTR and
RTC_TSDR) maintain the results of the previous event.
Note: TSF is set 2 ck_apre cycles after the ti mestamp event occurs due to synchronization
process.
There is no delay in the setting of TSOVF. This means that if two timestamp events are
close together, TSOVF can be seen as '1' while TSF is still '0'. As a consequence, it is
recommended to poll TSOVF only after TSF has been set.
Caution: If a timestamp event occurs immediately after the TSF bit is supposed to be cleared, then
both TSF and TSOVF bits are set. To avoid masking a timestamp event occurring at the
same moment, the application must not write 0 into TSF bit unless it has already read it to 1.
Optionally, a tamper event can cause a timestamp to be recorded. See the description of the
TAMPTS control bit in the RTC control register (RTC_CR).
41.3.18 Calibration clock output
When the COE bit is set to 1 in the RTC_CR register, a reference clock is provided on the
CALIB device output.

RM0438 Rev 8 1415/2187
RM0438 Real-time clock (RTC)
1482
If the COSEL bit in the RTC_CR register is reset and PREDIV_A = 0x7F, the CALIB
frequency is fRTCCLK/64. This corresponds to a calibration output at 512 Hz for an RTCCLK
frequency at 32.768 kHz. The CALIB duty cycle is irregular: there is a light jitter on falling
edges. It is therefore recommended to use rising edges.
When COSEL is set and “PREDIV_S+1” is a non-zero multiple of 256 (i.e: PREDIV_S[7:0] =
0xFF), the CALIB frequency is fRTCCLK/(256 * (PREDIV_A+1)). This corresponds to a
calibration output at 1 Hz for prescaler default values (PREDIV_A = Ox7F, PREDIV_S =
0xFF), with an RTCCLK frequency at 32.768 kHz.
Note: When the CALIB output is selected, the RTC_ OUT1 pin is automatically configured but the
RTC_OUT2 pin must be set as alternate function.
When COSEL is cleared, the CALIB output is the output of the 6th stage of the
asynchronous prescaler. If LPCAL is changed from 0 to 1, the output can be irregular
(glitch...) during the LPCAL switch. If LPCAL = 1 this output is always available. If LPCAL =
0, no output is present if PREDIV_A is < 0x20.
When COSEL is set, the CALIB output is the output of the 8th stage of the synchronous
prescaler.
41.3.19 Tamper and alarm output
The OSEL[1:0] control bits in the RTC_CR register are used to activate the alarm output
TAMPALRM, and to select the function which is output. These functions reflect the contents
of the corresponding flags in the RTC_SR register.
When the TAMPOE control bit is set in the RTC_CR, all external and internal tamper flags
are ORed and routed to the TAMPALRM output. If OSEL = 00 the TAMPALRM output
reflects only the tampers flags. If OSEL ≠ 00, the signal on TAMPALRM provides both
tamper flags and alarm A, B, or wake-up flag.
The polarity of the TAMPALRM output is determined by the POL control bit in RTC_CR so
that the opposite of the selected flags bit is output when POL is set to 1.
TAMPALRM output
The TAMPALRM pin can be configured in output open drain or output push-pull using the
control bit TAMPALRM_TYPE in the RTC_CR register. It is possible to apply the internal
pull-up in output mode thanks to TAMPALRM_PU in the RTC_CR.
Note: Once the TAMPALRM output is enabled, it has priority over CALIB on RTC_OUT1.
When the TAMPALRM output is selected, the RTC_OUT1 pin is automatically configured
but the RTC_OUT2 pin must be set as alternate function.

Real-time clock (RTC) RM0438
1416/2187 RM0438 Rev 8
41.4 RTC low-power modes
The table below summarizes the RTC pins and functions capability in all modes.
[Table 313](../tables/table_313.md). Effect of low-power modes on RTC
Mode Description
Sleep No effect
RTC interrupts cause the device to exit the Sleep mode.
Stop The RTC remains active when the RTC clock source is LSE or LSI. RTC interrupts
cause the device to exit the Stop mode.
Standby The RTC remains active when the RTC clock source is LSE or LSI. RTC interrupts
cause the device to exit the Standby mode.
Shutdown The RTC remains active when the RTC clock source is LSE. RTC interrupts cause the
device to exit the Shutdown mode.
[Table 314](../tables/table_314.md). RTC pins functionality over modes
Functions
Functional in all low-
power modes except
Standby and Shutdown
modes
Functional in Standby
and Shutdown mode
Functional in VBAT
mode
RTC_TS Yes Yes Yes
RTC_REFIN Yes No No
RTC_OUT1 Yes Yes Yes
RTC_OUT2 Yes Yes No

RM0438 Rev 8 1417/2187
RM0438 Real-time clock (RTC)
1482
41.5 RTC interrupts
The interrupt channel is set in the masked interrupt status register or in the secure masked
interrupt status register depending on its security mode configuration. The interrupt output
or the secure interrupt output is also activated.
[Table 315](../tables/table_315.md). Non-secure interrupt requests
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
mode
Exit from
Shutdown
mode
RTC
Alarm A ALRAF
ALRAIE and
(ALRADPROT=1
and
DECPROT=1)
write 1 in
CALRAF Yes Yes (3) Yes(4)
Alarm B ALRBF
ALRBIE and
(ALRBDPROT=1
and
DECPROT=1)
write 1 in
CALRBF Yes Yes (3) Yes(4)
Timestamp TSF
TSIE and
(TSDPROT=1
and
DECPROT=1)
write 1 in
CTSF Yes Yes (3) Yes(4)
Wakeup timer WUTF
WUTIE and
(WUTDPROT=1
and
DECPROT=1)
write 1 in
CWUTF Yes Yes (3) Yes(4)
1. The event flags are in the RTC_SR register.
2. The interrupt masked flags (resulting from event flags AND enable control bits) are in the RTC_MISR register.
3. Wakeup from Stop and Standby modes is possible only when the RTC clock source is LSE or LSI.
4. Wakeup from Shutdown modes is possible only when the RTC clock source is LSE.

Real-time clock (RTC) RM0438
1418/2187 RM0438 Rev 8
[Table 316](../tables/table_316.md). Secure interrupt requests
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
mode
Exit from
Shutdown
mode
RTC_S
Alarm A ALRAF
ALRAIE and
(ALRADPROT=0
or DECPROT=0)
write 1 in
CALRAF Yes Yes (3) Yes(4)
Alarm B ALRBF
ALRBIE and
(ALRBDPROT=0
or DECPROT=0)
write 1 in
CALRBF Yes Yes (3) Yes(4)
Timestamp TSF
TSIE and
(TSDPROT=0 or
DECPROT=0)
write 1 in
CTSF Yes Yes (3) Yes(4)
Wakeup timer WUTF
WUTIE and
(WUTDPROT=0
or DECPROT=0)
write 1 in
CWUTF Yes Yes (3) Yes(4)
1. The event flags are in the RTC_SR register.
2. The interrupt masked flags (resulting from event flags AND enable control bits) are in the RTC_MISR register.
3. Wakeup from Stop and Standby modes is possible only when the RTC clock source is LSE or LSI.
4. Wakeup from Shutdown modes is possible only when the RTC clock source is LSE.

RM0438 Rev 8 1419/2187
RM0438 Real-time clock (RTC)
1482
41.6 RTC registers
Refer to Section 1.2 on page 77 of the reference manual for a list of abbreviations used in
register descriptions.
The peripheral registers can be accessed by words (32-bit).
41.6.1 RTC time register (RTC_TR)
The RTC_TR is the calendar time shadow register. This register must be written in
initialization mode only. Refer to Calendar initialization and configuration on page 1407 and
Reading the calendar on page 1409.
This register is write protected. The write access procedure is described in RTC register
write protection on page 1407.
This register can be write-protected against non-secure access. Refer to Section 41.3.4:
RTC secure protection modes.
This register can be write-protected against non-privileged access. Refer to Section 41.3.5:
RTC privilege protection modes.
Address offset: 0x00
Backup domain reset value: 0x0000 0000
System reset value: 0x0000 0000 (when BYPSHAD = 0, not affected when BYPSHAD = 1)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. PM HT[1:0] HU[3:0]
rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. MNT[2:0] MNU[3:0] Res. ST[2:0] SU[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:23 Reserved, must be kept at reset value.
Bit 22 PM: AM/PM notation
0: AM or 24-hour format
1: PM
Bits 21:20 HT[1:0]: Hour tens in BCD format
Bits 19:16 HU[3:0]: Hour units in BCD format
Bit 15 Reserved, must be  kept at reset value.
Bits 14:12 MNT[2:0]: Minute tens in BCD format
Bits 11:8 MNU[3:0]: Minute units in BCD format
Bit 7 Reserved, must be kept at reset value.
Bits 6:4 ST[2:0]: Second tens in BCD format
Bits 3:0 SU[3:0]: Second units in BCD format

Real-time clock (RTC) RM0438
1420/2187 RM0438 Rev 8
41.6.2 RTC date register (RTC_DR)
The RTC_DR is the calendar date shadow register. This register must be written in
initialization mode only. Refer to Calendar initialization and configuration on page 1407 and
Reading the calendar on page 1409.
This register is write protected. The write access procedure is described in RTC register
write protection on page 1407.
This register can be write-protected against non-secure access. Refer to Section 41.3.4:
RTC secure protection modes.
This register can be write-protected against non-privileged access. Refer to Section 41.3.5:
RTC privilege protection modes.
Address offset: 0x04
Backup domain reset value: 0x0000 2101
System reset value: 0x0000 2101 (when BYPSHAD = 0, not affected when BYPSHAD = 1)
Note: The calendar is frozen when reaching the maximum value, and can’t roll over.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. YT[3:0] YU[3:0]
rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
WDU[2:0] MT MU[3:0] Res. Res. DT[1:0] DU[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:24 Reserved, must be kept at reset value.
Bits 23:20 YT[3:0]: Year tens in BCD format
Bits 19:16 YU[3:0]: Year units in BCD format
Bits 15:13 WDU[2:0]: Week day units
000: forbidden
001: Monday
...
111: Sunday
Bit 12 MT: Month tens in BCD format
Bits 11:8 MU[3:0]: Month units in BCD format
Bits 7:6 Reserved, must be kept at reset value.
Bits 5:4 DT[1:0]: Date tens in BCD format
Bits 3:0 DU[3:0]: Date units in BCD format

RM0438 Rev 8 1421/2187
RM0438 Real-time clock (RTC)
1482
41.6.3 RTC sub second register (RTC_SSR)
Address offset: 0x08
Backup domain reset value: 0x0000 0000
System reset value: 0x0000 0000 (when BYPSHAD = 0, not affected when BYPSHAD = 1)
41.6.4 RTC initialization control and status register (RTC_ICSR)
This register is write protected. The write access procedure is described in RTC register
write protection on page 1407.
This register can be globally protected, or each bit of this register can be individually
protected against non-secure access. Refer to Section 41.3.4: RTC secure protection
modes.
This register can be globally protected, or each bit of this register can be individually
protected against non-privileged access. Refer to Section 41.3.5: RTC privilege protection
modes.
Address offset: 0x0C
Backup domain reset value: 0x0000 0007
System reset: not affected except INIT, INITF, and RSF bits which are cleared to 0
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
SS[15:0]
rrrrrrrrrrrrrrrr
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 SS[15:0]: Sub second value
SS[15:0] is the value in the synchronous prescaler counter. The fraction of a second is given
by the formula below:
Second fraction = (PREDIV_S - SS) / (PREDIV_S + 1)
Note: SS can be larger than PREDIV_S only after a shift operation. In that case, the correct
time/date is one second less than as indicated by RTC_TR/RTC_DR.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. RECAL
PF
r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. INIT INITF RSF INITS SHPF WUTW
F Res. Res.
r w r r c _ w 0 rrr

Real-time clock (RTC) RM0438
1422/2187 RM0438 Rev 8
Bits 31:17 Reserved, must be kept at reset value.
Bit 16 RECALPF: Recalibration pending Flag
The RECALPF status flag is automatically set to 1 when software writes to the RTC_CALR
register, indicating that the RTC_CALR register is blocked. When the new calibration settings
are taken into account, this bit returns to 0. Refer to Re-calibration on-the-fly.
Bits 15:8 Reserved, must be kept at reset value.
Bit 7 INIT: Initialization mode
0: Free running mode
1: Initialization mode used to program time and date register (RTC_TR and RTC_DR), and
prescaler register (RTC_PRER). Counters are stopped and start counting from the new
value when INIT is reset.
Bit 6 INITF: Initialization flag
When this bit is set to 1, the RTC is in initialization state, and the time, date and prescaler
registers can be updated.
0: Calendar registers update is not allowed
1: Calendar registers update is allowed
Bit 5 RSF: Registers synchronization flag
This bit is set by hardware each time the calendar registers are copied into the shadow
registers (RTC_SSR, RTC_TR and RTC_DR). This bit is cleared by hardware in initialization
mode, while a shift operation is pending (SHPF = 1), or when in bypass shadow register
mode (BYPSHAD = 1). This bit can also be cleared by software.
It is cleared either by software or by hardware in initialization mode.
0: Calendar shadow registers not yet synchronized
1: Calendar shadow registers synchronized
Bit 4 INITS: Initialization status flag
This bit is set by hardware when the calendar year field is different from 0 (Backup domain
reset state).
0: Calendar has not been initialized
1: Calendar has been initialized
Bit 3 SHPF: Shift operation pending
This flag is set by hardware as soon as a shift operation is initiated by a write to the
RTC_SHIFTR register. It is cleared by hardware when the corresponding shift operation has
been executed. Writing to the SHPF bit has no effect.
0: No shift operation is pending
1: A shift operation is pending
Bit 2 WUTWF: Wake-up timer write flag
This bit is set by hardware when WUT value can be changed, after the WUTE bit has been
set to 0 in RTC_CR.
It is cleared by hardware in initialization mode.
0: Wake-up timer configuration update not allowed except in initialization mode
1: Wake-up timer configuration update allowed
Bits 1:0 Reserved, must be kept at reset value.

RM0438 Rev 8 1423/2187
RM0438 Real-time clock (RTC)
1482
41.6.5 RTC prescaler re gister (RTC_PRER)
This register must be written in initialization mode only. The initialization must be performed
in two separate write accesses. Refer to Calendar initialization and configuration on
page 1407.
This register is write protected. The write access procedure is described in RTC register
write protection on page 1407.
This register can be write-protected against non-secure access. Refer to Section 41.3.4:
RTC secure protection modes.
This register can be write-protected against non-privileged access. Refer to Section 41.3.5:
RTC privilege protection modes.
Address offset: 0x10
Backup domain reset value: 0x007F 00FF
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. PREDIV_A[6:0]
rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. PREDIV_S[14:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:23 Reserved, must be kept at reset value.
Bits 22:16 PREDIV_A[6:0]: Asynchronous prescaler factor
This is the asynchronous division factor:
ck_apre frequency = RTCCLK frequency/(PREDIV_A+1)
Bit 15 Reserved, must be  kept at reset value.
Bits 14:0 PREDIV_S[14:0]: Synchronous prescaler factor
This is the synchronous division factor:
ck_spre frequency = ck_apre frequency/(PREDIV_S+1)

Real-time clock (RTC) RM0438
1424/2187 RM0438 Rev 8
41.6.6 RTC wake-up timer register (RTC_WUTR)
This register can be written only when WUTWF is set to 1 in RTC_ICSR.
This register can be protected against non-secure access. Refer to Section 41.3.4: RTC
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 41.3.5: RTC
privilege protection modes.
Address offset: 0x14
Backup domain reset value: 0x0000 FFFF
System reset: not affected
41.6.7 RTC control register (RTC_CR)
This register is write protected. The write access procedure is described in RTC register
write protection on page 1407.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
WUTOCLR[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
WUT[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 WUTOCLR[15:0]: Wake-up auto-reload output clear value
When WUTOCLR[15:0] is different from 0x0000, WUTF is set by hardware when the auto-
reload down-counter reaches 0 and is cleared by hardware when the auto-reload
downcounter reaches WUTOCLR[15:0].
When WUTOCLR[15:0] = 0x0000, WUTF is set by hardware when the WUT down-counter
reaches 0 and is cleared by software.
Bits 15:0 WUT[15:0]: Wake-up auto-reload value bits
When the wake-up timer is enabled (WUTE set to 1), the WUTF flag is set every
(WUT[15:0] + 1) ck_wut cycles. The ck_wut period is selected through WUCKSEL[2:0] bits
of the RTC_CR register.
When WUCKSEL[2] = 1, the wake-up timer becomes 17-bits and WUCKSEL[1] effectively
becomes WUT[16] the most-significant bit to be reloaded into the timer.
The first assertion of WUTF occurs between WUT and (WUT + 2) ck_wut cycles after WUTE
is set. Setting WUT[15:0] to 0x0000 with WUCKSEL[2:0] = 011 (RTCCLK/2) is forbidden.

RM0438 Rev 8 1425/2187
RM0438 Real-time clock (RTC)
1482
This register can be globally protected, or each bit of this register can be individually
protected against non-secure access. Refer to Section 41.3.4: RTC secure protection
modes.
This register can be globally protected, or each bit of this register can be individually
protected against non-privileged access. Refer to Section 41.3.5: RTC privilege protection
modes.
Address offset: 0x18
Backup domain reset value: 0x0000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
OUT2
EN
TAMP
ALRM_
TYPE
TAMP
ALRM_
PU
Res. Res. TAMP
OE
TAMP
TS ITSE COE OSEL[1:0] POL COSEL BKP SUB1H ADD1H
rw rw rw rw rw rw rw rw rw rw rw rw w w
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
TSIE WUTIE ALRB
IE
ALRA
IE TSE WUTE ALRBE ALRAE Res. FMT BYP
SHAD
REFCK
ON
TS
EDGE WUCKSEL[2:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 31 OUT2EN: RTC_OUT2 output enable
Setting this bit allows the RTC outputs to be remapped on RTC_OUT2 as follows:
OUT2EN = 0: RTC output 2 disable
If OSEL ≠ 00 or TAMPOE = 1: TAMPALRM is output on RTC_OUT1
If OSEL = 00 and TAMPOE = 0 and COE = 1: CALIB is output on RTC_OUT1
OUT2EN = 1: RTC output 2 enable
If (OSEL ≠ 00 or TAMPOE = 1) and COE = 0: TAMPALRM is output on RTC_OUT2
If OSEL = 00 and TAMPOE = 0 and COE = 1: CALIB is output on RTC_OUT2
If (OSEL≠ 00 or TAMPOE = 1) and COE = 1: CALIB is output on RTC_OUT2 and
TAMPALRM is output on RTC_OUT1.
Bit 30 TAMPALRM_TYPE: TAMPALRM output type
0: TAMPALRM is push-pull output
1: TAMPALRM is open-drain output
Bit 29 TAMPALRM_PU: TAMPALRM pull-up enable
0: No pull-up is applied on TAMPALRM output
1: A pull-up is applied on TAMPALRM output
Bits 28:27 Reserved, must be kept at reset value.
Bit 26 TAMPOE: Tamper detection output enable on TAMPALRM
0: The tamper flag is not routed on TAMPALRM
1: The tamper flag is routed on TAMPALRM, combined with the signal provided by OSEL and
with the polarity provided by POL.
Bit 25 TAMPTS: Activate timestamp on tamper detection event
0: Tamper detection event does not cause a RTC timestamp to be saved
1: Save RTC timestamp on tamper detection event
TAMPTS is valid even if TSE = 0 in the RTC_CR register. Timestamp flag is set after the
tamper flags, therefore if TAMPTS and TSIE are set, it is recommended to disable the
tamper interrupts in order to avoid servicing 2 interrupts.

Real-time clock (RTC) RM0438
1426/2187 RM0438 Rev 8
Bit 24 ITSE: timestamp on internal event enable
0: internal event timestamp disabled
1: internal event timestamp enabled
Bit 23 COE: Calibration output enable
This bit enables the CALIB output
0: Calibration output disabled
1: Calibration output enabled
Bits 22:21 OSEL[1:0]: Output selection
These bits are used to select the flag to be routed to TAMPALRM output.
00: Output disabled
01: Alarm A output enabled
10: Alarm B output enabled
11: Wake-up output enabled
Bit 20 POL: Output polarity
This bit is used to configure the polarity of TAMPALRM output.
0: The pin is high when ALRAF/ALRBF/WUTF is asserted (depending on OSEL[1:0]), or
when a TAMPxF/ITAMPxF is asserted (if TAMPOE = 1).
1: The pin is low when ALRAF/ALRBF/WUTF is asserted (depending on OSEL[1:0]), or
when a TAMPxF/ITAMPxF is asserted (if TAMPOE = 1).
Bit 19 COSEL: Calibration output selection
When COE = 1, this bit selects which signal is output on CALIB.
0: Calibration output is 512 Hz
1: Calibration output is 1 Hz
These frequencies are valid for RTCCLK at 32.768 kHz and prescalers at their default values
(PREDIV_A = 127 and PREDIV_S = 255). Refer to Section 41.3.18: Calibration clock output.
Bit 18 BKP: Backup
This bit can be written by the user to memorize whether the daylight saving time change has
been performed or not.
Bit 17 SUB1H: Subtract 1 hour (winter time change)
When this bit is set outside initialization mode, 1 hour is subtracted to the calendar time if the
current hour is not 0. This bit is always read as 0.
Setting this bit has no effect when current hour is 0.
0: No effect
1: Subtracts 1 hour to the current time. This can be used for winter time change.
Bit 16 ADD1H: Add 1 hour (summer time change)
When this bit is set outside initialization mode, 1 hour is added to the calendar time. This bit
is always read as 0.
0: No effect
1: Adds 1 hour to the current time. This can be used for summer time change
Bit 15 TSIE: Timestamp interrupt enable
0: Timestamp interrupt disable
1: Timestamp interrupt enable
Bit 14 WUTIE: Wake-up timer interrupt enable
0: Wake-up timer interrupt disabled
1: Wake-up timer interrupt enabled

RM0438 Rev 8 1427/2187
RM0438 Real-time clock (RTC)
1482
Bit 13 ALRBIE: Alarm B interrupt enable
0: Alarm B interrupt disable
1: Alarm B interrupt enable
Bit 12 ALRAIE: Alarm A interrupt enable
0: Alarm A interrupt disabled
1: Alarm A interrupt enabled
Bit 11 TSE: timestamp enable
0: timestamp disable
1: timestamp enable
Bit 10 WUTE: Wake-up timer enable
0: Wake-up timer disabled
1: Wake-up timer enabled
Bit 9 ALRBE: Alarm B enable
0: Alarm B disabled
1: Alarm B enabled
Bit 8 ALRAE: Alarm A enable
0: Alarm A disabled
1: Alarm A enabled
Bit 7 Reserved, must be kept at reset value.
Bit 6 FMT: Hour format
0: 24 hour/day format
1: AM/PM hour format
Bit 5 BYPSHAD: Bypass the shadow registers
0: Calendar values (when reading from RTC_SSR, RTC_TR, and RTC_DR) are taken from
the shadow registers, which are updated once every two RTCCLK cycles.
1: Calendar values (when reading from RTC_SSR, RTC_TR, and RTC_DR) are taken
directly from the calendar counters.
Note: If the frequency of the APB1 clock is less than seven times the frequency of RTCCLK,
BYPSHAD must be set to 1.
Bit 4 REFCKON: RTC_REFIN reference clock detection enable (50 or 60 Hz)
0: RTC_REFIN detection disabled
1: RTC_REFIN detection enabled
Note: PREDIV_S must be 0x00FF.
Bit 3 TSEDGE: Timestamp event active edge
0: RTC_TS input rising edge generates a timestamp event
1: RTC_TS input falling edge generates a timestamp event
TSE must be reset when TSEDGE is changed to avoid unwanted TSF setting.
Bits 2:0 WUCKSEL[2:0]: ck_wut wake-up clock selection
000: RTC/16 clock is selected
001: RTC/8 clock is selected
010: RTC/4 clock is selected
011: RTC/2 clock is selected
10x: ck_spre (usually 1 Hz) clock is selected.
11x: ck_spre (usually 1 Hz) clock is selected. Furthermore, 216 is added to the WUT counter
value.

Real-time clock (RTC) RM0438
1428/2187 RM0438 Rev 8
Note: Bits 6 and 4 of this register can be written in initialization mode only (RTC_ICSR/INITF = 1).
WUT = wake-up unit counter value. WUT = (0x0000 to 0xFFFF) + 0x10000 added when
WUCKSEL[2:1 = 11].
Bits 2 to 0 of this register can be written only when RTC_CR WUTE bit = 0 and RTC_ICSR
WUTWF bit = 1.
It is recommended not to change the hour during the calendar hour increment as it could
mask the incrementation of the calendar hour.
ADD1H and SUB1H changes are effective in the next second.
41.6.8 RTC privilege mode c ontrol register (RTC_PRIVCR)
This register can be written only when the APB access is privileged. This register can be
write-protected, or each bit of this register can be individually write-protected against non-
secure access depending on the RTC_SMCR configuration (refer to Section 41.3.5: RTC
privilege protection modes).
Address offset: 0x1C
Backup domain reset value: 0x0000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PRIV INIT
PRIV
CAL
PRIV Res. Res. Res. Res. Res. Res. Res. Res. Res. TS
PRIV
WUT
PRIV
ALRB
PRIV
ALRA
PRIV
rw rw rw rw rw rw rw
Bits 31:16 Reserved, must be kept at reset value.
Bit 15 PRIV: RTC privilege protection
0: All RTC registers can be written when the APB access is privileged or non-privileged,
except the registers protected by other privilege protection bits.
1: All RTC registers can be written only when the APB access is privileged.
Bit 14 INITPRIV: Initialization privilege protection
0: RTC Initialization mode, calendar and prescalers registers can be written when the APB
access is privileged or non-privileged.
1: RTC Initialization mode, calendar and prescalers registers can be written only when the
APB access is privileged.
Bit 13 CALPRIV: Shift register, Delight saving, calibration and reference clock privilege protection
0: Shift register, Delight saving, calibration and reference clock can be written when the APB
access is privileged or non-privileged.
1: Shift register, Delight saving, calibration and reference clock can be written only when the
APB access is privileged.
Bits 12:4 Reserved, must be kept at reset value.

RM0438 Rev 8 1429/2187
RM0438 Real-time clock (RTC)
1482
Note: Refer to Section 41.3.5: RTC privilege protection modes for details on the read protection.
41.6.9 RTC secure mode cont rol register (RTC_SMCR)
This register can be written only when the APB access is secure.
This register can be globally write-protected, or each bit of this register can be individually
write-protected against non-privileged access depending on the RTC_PRIVCR
configuration (refer to Section 41.3.5: RTC privilege protection modes).
Address offset: 0x20
Backup domain reset value: 0x0000 E00F
System reset: not affected
Bit 3 TSPRIV: Timestamp privilege protection
0: RTC Timestamp configuration and interrupt clear can be written when the APB access is
privileged or non-privileged.
1: RTC Timestamp configuration and interrupt clear can be written only when the APB
access is privileged.
Bit 2 WUTPRIV: Wakeup timer privilege protection
0: RTC Wakeup timer configuration and interrupt clear can be written when the APB access
is privileged or non-privileged.
1: RTC Wakeup timer configuration and interrupt clear can be written only when the APB
access is privileged.
Bit 1 ALRBPRIV: Alarm B privilege protection
0: RTC Alarm B configuration and interrupt clear can be written when the APB access is
privileged or non-privileged.
1: RTC Alarm B configuration and interrupt clear can be written only when the APB access is
privileged.
Bit 0 ALRAPRIV: Alarm A privilege protection
0: RTC Alarm A configuration and interrupt clear can be written when the APB access is
privileged or non-privileged.
1: RTC Alarm A configuration and interrupt clear can be written only when the APB access is
privileged.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DEC
PROT
INIT
DPROT
CAL
DPROT Res. Res. Res. Res. Res. Res. Res. Res. Res. TS
DPROT
WUT
DPROT
ALRB
DPROT
ALRA
DPROT
rw rw rw rw rw rw rw

Real-time clock (RTC) RM0438
1430/2187 RM0438 Rev 8
Note: Refer to Section 41.3.4: RTC secure protection modes for details on the read protection.
Bits 31:16 Reserved, must be kept at reset value.
Bit 15 DECPROT: RTC global protection
0: All RTC registers can be written only when the APB access is secure.
1: All RTC registers can be written when the APB access is secure or non-secure, except the
registers protected by other secure protection bits.
Bit 14 INITDPROT: Initialization protection
0: RTC Initialization mode, calendar and prescalers registers can be written only when the
APB access is secure.
1: RTC Initialization mode, calendar and prescalers registers can be written when the APB
access is secure or non-secure.
Bit 13 CALDPROT: Shift register, daylight saving, calibration and reference clock protection
0: Shift register, daylight saving, calibration and reference clock can be written only when the
APB access is secure.
1: Shift register, daylight saving, calibration and reference clock can be written when the APB
access is secure or non-secure.
Bits 12:4 Reserved, must be kept at reset value.
Bit 3 TSDPROT: Timestamp protection
0: RTC timestamp configuration and interrupt clear can be written only when the APB access
is secure.
1: RTC timestamp configuration and interrupt clear can be written when the APB access is
secure or non-secure.
Bit 2 WUTDPROT: Wakeup timer protection
0: RTC wakeup timer configuration and interrupt clear can be written only when the APB
access is secure.
1: RTC wakeup timer configuration and interrupt clear can be written when the APB access
is secure or non-secure.
Bit 1 ALRBDPROT: Alarm B protection
0: RTC alarm B configuration and interrupt clear can be written only when the APB access is
secure.
1: RTC alarm B configuration and interrupt clear can be written when the APB access is
secure or non-secure.
Bit 0 ALRADPROT: Alarm A protection
0: RTC alarm A configuration and interrupt clear can be written only when the APB access is
secure.
1: RTC alarm A configuration and interrupt clear can be written when the APB access is
secure or non-secure.

RM0438 Rev 8 1431/2187
RM0438 Real-time clock (RTC)
1482
41.6.10 RTC write protect ion register (RTC_WPR)
Address offset: 0x24
Reset value: 0x0000 0000
41.6.11 RTC calibration register (RTC_CALR)
This register is write protected. The write access procedure is described in RTC register
write protection on page 1407.
This register can be write-protected against non-secure access. Refer to Section 41.3.4:
RTC secure protection modes.
This register can be write-protected against non-privileged access. Refer to Section 41.3.5:
RTC privilege protection modes.
Address offset: 0x28
Backup domain reset value: 0x0000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. KEY[7:0]
wwwwwwww
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 KEY[7:0]: Write protection key
This byte is written by software.
Reading this byte always returns 0x00.
Refer to RTC register write protection for a description of how to unlock RTC register write
protection.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CALP CALW8 CALW
16 LPCAL Res. Res. Res. CALM[8:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw

Real-time clock (RTC) RM0438
1432/2187 RM0438 Rev 8
Bits 31:16 Reserved, must be kept at reset value.
Bit 15 CALP: Increase frequency of RTC by 488.5 ppm
0: No RTCCLK pulses are added.
1: One RTCCLK pulse is effectively inserted every 211 pulses (frequency increased by
488.5 ppm).
This feature is intended to be used in conjunction with CALM, which lowers the frequency of
the calendar with a fine resolution. if the input frequency is 32768 Hz, the number of
RTCCLK pulses added during a 32-second window is calculated as follows: (512 × CALP) -
CALM.
Refer to Section 41.3.16: RTC smooth digital calibration.
Bit 14 CALW8: Use an 8-second calibration cycle period
When CALW8 is set to 1, the 8-second calibration cycle period is selected.
Note: CALM[1:0] are stuck at 00 when CALW8 = 1. Refer to Section 41.3.16: RTC smooth
digital calibration.
Bit 13 CALW16: Use a 16-second calibration cycle period
When CALW16 is set to 1, the 16-second calibration cycle period is selected. This bit must
not be set to 1 if CALW8 = 1.
Note: CALM[0] is stuck at 0 when CALW16 = 1. Refer to Section 41.3.16: RTC smooth digital
calibration.
Bit 12 LPCAL: Calibration low-power mode
0:Calibration window is 220 RTCCLK, which is a high-consumption mode. This mode should
be set only when less than 32s calibration window is required.
1:Calibration window is 220 ck_apre, which is the required configuration for ultra-low
consumption mode.
Bits 11:9 Reserved, must be kept at reset value.
Bits 8:0 CALM[8:0]: Calibration minus
The frequency of the calendar is reduced by masking CALM out of 220 RTCCLK pulses (32
seconds if the input frequency is 32768 Hz). This decreases the frequency of the calendar
with a resolution of 0.9537 ppm.
To increase the frequency of the calendar, this feature should be used in conjunction with
CALP. See Section 41.3.16: RTC smooth digital calibration on page 1412.

RM0438 Rev 8 1433/2187
RM0438 Real-time clock (RTC)
1482
41.6.12 RTC shift contro l register (RTC_SHIFTR)
This register is write protected. The write access procedure is described in RTC register
write protection on page 1407.
This register can be protected against non-secure access. Refer to Section 41.3.4: RTC
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 41.3.5: RTC
privilege protection modes.
Address offset: 0x2C
Backup domain reset value: 0x0000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ADD1S Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res.
w
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. SUBFS[14:0]
wwwwwwwwwwwwwww
Bit 31 ADD1S: Add one second
0: No effect
1: Add one second to the clock/calendar
This bit is write only and is always read as zero. Writing to this bit has no effect when a shift
operation is pending (when SHPF = 1, in RTC_ICSR).
This function is intended to be used with SUBFS (see description below) in order to
effectively add a fraction of a second to the clock in an atomic operation.
Bits 30:15 Reserved, must be kept at reset value.
Bits 14:0 SUBFS[14:0]: Subtract a fraction of a second
These bits are write only and is always read as zero. Writing to this bit has no effect when a
shift operation is pending (when SHPF = 1, in RTC_ICSR).
The value which is written to SUBFS is added to the synchronous prescaler counter. Since
this counter counts down, this operation effectively subtracts from (delays) the clock by:
Delay (seconds) = SUBFS / (PREDIV_S + 1)
A fraction of a second can effectively be added to the clock (advancing the clock) when the
ADD1S function is used in conjunction with SUBFS, effectively advancing the clock by:
Advance (seconds) = (1 - (SUBFS / (PREDIV_S + 1))).
Note: Writing to SUBFS causes RS F to be cleared. Software can then wait until RSF = 1 to be
sure that the shadow registers have been updated with the shifted time.

Real-time clock (RTC) RM0438
1434/2187 RM0438 Rev 8
41.6.13 RTC timestamp ti me register (RTC_TSTR)
The content of this register is valid only when TSF is set to 1 in RTC_SR. It is cleared when
TSF bit is reset.
This register can be protected against non-secure access. Refer to Section 41.3.4: RTC
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 41.3.5: RTC
privilege protection modes.
Address offset: 0x30
Backup domain reset value: 0x0000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. PM HT[1:0] HU[3:0]
rrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. MNT[2:0] MNU[3:0] Res. ST[2:0] SU[3:0]
rrrrrrr rrrrrrr
Bits 31:23 Reserved, must be kept at reset value.
Bit 22 PM: AM/PM notation
0: AM or 24-hour format
1: PM
Bits 21:20 HT[1:0]: Hour tens in BCD format.
Bits 19:16 HU[3:0]: Hour units in BCD format.
Bit 15 Reserved, must be  kept at reset value.
Bits 14:12 MNT[2:0]: Minute tens in BCD format.
Bits 11:8 MNU[3:0]: Minute units in BCD format.
Bit 7 Reserved, must be kept at reset value.
Bits 6:4 ST[2:0]: Second tens in BCD format.
Bits 3:0 SU[3:0]: Second units in BCD format.

RM0438 Rev 8 1435/2187
RM0438 Real-time clock (RTC)
1482
41.6.14 RTC timestamp da te register (RTC_TSDR)
The content of this register is valid only when TSF is set to 1 in RTC_SR. It is cleared when
TSF bit is reset.
This register can be protected against non-secure access. Refer to Section 41.3.4: RTC
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 41.3.5: RTC
privilege protection modes.
Address offset: 0x34
Backup domain reset value: 0x0000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
WDU[2:0] MT MU[3:0] Res. Res. DT[1:0] DU[3:0]
rrrrrrrr rrrrrr
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:13 WDU[2:0]: Week day units
Bit 12 MT: Month tens in BCD format
Bits 11:8 MU[3:0]: Month units in BCD format
Bits 7:6 Reserved, must be kept at reset value.
Bits 5:4 DT[1:0]: Date tens in BCD format
Bits 3:0 DU[3:0]: Date units in BCD format

Real-time clock (RTC) RM0438
1436/2187 RM0438 Rev 8
41.6.15 RTC timestamp sub s econd register (RTC_TSSSR)
The content of this register is valid only when TSF is set to 1 in RTC_SR. It is cleared when
the TSF bit is reset.
This register can be protected against non-secure access. Refer to Section 41.3.4: RTC
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 41.3.5: RTC
privilege protection modes.
Address offset: 0x38
Backup domain reset value: 0x0000 0000
System reset: not affected
41.6.16 RTC alarm A re gister (RTC_ALRMAR)
This register can be written only when ALRAE is reset in RTC_CR register, or in initialization
mode.
This register can be protected against non-secure access. Refer to Section 41.3.4: RTC
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 41.3.5: RTC
privilege protection modes.
Address offset: 0x40
Backup domain reset value: 0x0000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
SS[15:0]
rrrrrrrrrrrrrrrr
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 SS[15:0]: Sub second value
SS[15:0] is the value of the synchronous prescaler counter when the timestamp event
occurred.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
MSK4 WDSE
L DT[1:0] DU[3:0] MSK3 PM HT[1:0] HU[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
MSK2 MNT[2:0] MNU[3:0] MSK1 ST[2:0] SU[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 1437/2187
RM0438 Real-time clock (RTC)
1482
Bit 31 MSK4: Alarm A date mask
0: Alarm A set if the date/day match
1: Date/day don’t care in alarm A comparison
Bit 30 WDSEL: Week day selection
0: DU[3:0] represents the date units
1: DU[3:0] represents the week day. DT[1:0] is don’t care.
Bits 29:28 DT[1:0]: Date tens in BCD format
Bits 27:24 DU[3:0]: Date units or day in BCD format
Bit 23 MSK3: Alarm A hours mask
0: Alarm A set if the hours match
1: Hours don’t care in alarm A comparison
Bit 22 PM: AM/PM notation
0: AM or 24-hour format
1: PM
Bits 21:20 HT[1:0]: Hour tens in BCD format
Bits 19:16 HU[3:0]: Hour units in BCD format
Bit 15 MSK2: Alarm A minutes mask
0: Alarm A set if the minutes match
1: Minutes don’t care in alarm A comparison
Bits 14:12 MNT[2:0]: Minute tens in BCD format
Bits 11:8 MNU[3:0]: Minute units in BCD format
Bit 7 MSK1: Alarm A seconds mask
0: Alarm A set if the seconds match
1: Seconds don’t care in alarm A comparison
Bits 6:4 ST[2:0]: Second tens in BCD format.
Bits 3:0 SU[3:0]: Second units in BCD format.

Real-time clock (RTC) RM0438
1438/2187 RM0438 Rev 8
41.6.17 RTC alarm A sub sec ond register (RTC_ALRMASSR)
This register can be written only when ALRAE is reset in RTC_CR register, or in initialization
mode.
This register can be protected against non-secure access. Refer to Section 41.3.4: RTC
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 41.3.5: RTC
privilege protection modes.
Address offset: 0x44
Backup domain reset value: 0x0000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. MASKSS[3:0] Res. Res. Res. Res. Res. Res. Res. Res.
rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. SS[14:0]
rw rw rw rw rw rw rw rw rw rw rw rw w rw rw
Bits 31:28 Reserved, must be kept at reset value.
Bits 27:24 MASKSS[3:0]: Mask the most-significant bits starting at this bit
0:No comparison on sub seconds for alarm A. The alarm is set when the seconds unit is
incremented (assuming that the rest of the fields match).
1:SS[14:1] are don’t care in alarm A comparison. Only SS[0] is compared.
2:SS[14:2] are don’t care in alarm A comparison. Only SS[1:0] are compared.
3:SS[14:3] are don’t care in alarm A comparison. Only SS[2:0] are compared.
...
12:SS[14:12] are don’t care in alarm A comparison. SS[11:0] are compared.
13:SS[14:13] are don’t care in alarm A comparison. SS[12:0] are compared.
14:SS[14] is don’t care in alarm A comparison. SS[13:0] are compared.
15:All 15 SS bits are compared and must match to activate alarm.
The overflow bits of the synchronous counter (bits 15) is never compared. This bit can be
different from 0 only after a shift operation.
Note: The overflow bits of the synchronous counte r (bits 15) is never compared. This bit can
be different from 0 only after a shift operation.
Bits 23:15 Reserved, must be kept at reset value.
Bits 14:0 SS[14:0]: Sub seconds value
This value is compared with the contents of the synchronous prescaler counter to determine
if alarm A is to be activated. Only bits 0 up MASKSS-1 are compared.

RM0438 Rev 8 1439/2187
RM0438 Real-time clock (RTC)
1482
41.6.18 RTC alarm B re gister (RTC_ALRMBR)
This register can be written only when ALRBE is reset in RTC_CR register, or in initialization
mode.
This register can be protected against non-secure access. Refer to Section 41.3.4: RTC
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 41.3.5: RTC
privilege protection modes.
Address offset: 0x48
Backup domain reset value: 0x0000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
MSK4 WD
SEL DT[1:0] DU[3:0] MSK3 PM HT[1:0] HU[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
MSK2 MNT[2:0] MNU[3:0] MSK1 ST[2:0] SU[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 31 MSK4: Alarm B date mask
0: Alarm B set if the date and day match
1: Date and day don’t care in alarm B comparison
Bit 30 WDSEL: Week day selection
0: DU[3:0] represents the date units
1: DU[3:0] represents the week day. DT[1:0] is don’t care.
Bits 29:28 DT[1:0]: Date tens in BCD format
Bits 27:24 DU[3:0]: Date units or day in BCD format
Bit 23 MSK3: Alarm B hours mask
0: Alarm B set if the hours match
1: Hours don’t care in alarm B comparison
Bit 22 PM: AM/PM notation
0: AM or 24-hour format
1: PM
Bits 21:20 HT[1:0]: Hour tens in BCD format
Bits 19:16 HU[3:0]: Hour units in BCD format
Bit 15 MSK2: Alarm B minutes mask
0: Alarm B set if the minutes match
1: Minutes don’t care in alarm B comparison
Bits 14:12 MNT[2:0]: Minute tens in BCD format
Bits 11:8 MNU[3:0]: Minute units in BCD format

Real-time clock (RTC) RM0438
1440/2187 RM0438 Rev 8
41.6.19 RTC alarm B sub second  register (RTC_ALRMBSSR)
This register can be written only when ALRBE is reset in RTC_CR register, or in initialization
mode.
This register can be protected against non-secure access. Refer to Section 41.3.4: RTC
secure protection modes.
This register can be protected against non-privileged access. Refer to Section 41.3.5: RTC
privilege protection modes.
Address offset: 0x4C
Backup domain reset value: 0x0000 0000
System reset: not affected
Bit 7 MSK1: Alarm B seconds mask
0: Alarm B set if the seconds match
1: Seconds don’t care in alarm B comparison
Bits 6:4 ST[2:0]: Second tens in BCD format
Bits 3:0 SU[3:0]: Second units in BCD format
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. MASKSS[3:0] Res. Res. Res. Res. Res. Res. Res. Res.
rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. SS[14:0]
rw rw rw rw rw rw rw rw rw rw rw rw w rw rw
Bits 31:28 Reserved, must be kept at reset value.
Bits 27:24 MASKSS[3:0]: Mask the most-significant bits starting at this bit
0x0: No comparison on sub seconds for alarm B. The alarm is set when the seconds unit is
incremented (assuming that the rest of the fields match).
0x1: SS[14:1] are don’t care in alarm B comparison. Only SS[0] is compared.
0x2: SS[14:2] are don’t care in alarm B comparison. Only SS[1:0] are compared.
0x3: SS[14:3] are don’t care in alarm B comparison. Only SS[2:0] are compared.
...
0xC: SS[14:12] are don’t care in alarm B comparison. SS[11:0] are compared.
0xD: SS[14:13] are don’t care in alarm B comparison. SS[12:0] are compared.
0xE: SS[14] is don’t care in alarm B comparison. SS[13:0] are compared.
0xF: All 15 SS bits are compared and must match to activate alarm.
The overflow bits of the synchronous counter (bits 15) is never compared. This bit can be
different from 0 only after a shift operation.
Bits 23:15 Reserved, must  be kept at reset value.
Bits 14:0 SS[14:0]: Sub seconds value
This value is compared with the contents of the synchronous prescaler counter to determine
if alarm B is to be activated. Only bits 0 up to MASKSS-1 are compared.

RM0438 Rev 8 1441/2187
RM0438 Real-time clock (RTC)
1482
41.6.20 RTC status register (RTC_SR)
This register can be globally protected, or each bit of this register can be individually
protected against non-secure access. Refer to Section 41.3.4: RTC secure protection
modes.
This register can be globally protected, or each bit of this register can be individually
protected against non-privileged access. Refer to Section 41.3.5: RTC privilege protection
modes.
Address offset: 0x50
Backup domain reset value: 0x0000 0000
System reset: not affected
Note: The bits of this register  are cleared few APB clock cycles after setting their corresponding
clear bit in the RTC_SCR register. After clearing the flag, read it until it is read at 0 before
leaving the interrupt routine.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. ITSF TSOVF TSF WUTF ALRBF ALRAF
rrrrrr
Bits 31:6 Reserved, must be kept at reset value.
Bit 5 ITSF: Internal timestamp flag
This flag is set by hardware when a timestamp on the internal event occurs.
Bit 4 TSOVF: Timestamp overflow flag
This flag is set by hardware when a timestamp event occurs while TSF is already set.
It is recommended to check and then clear TSOVF only after clearing the TSF bit. Otherwise,
an overflow might not be noticed if a timestamp event occurs immediately before the TSF bit
is cleared.
Bit 3 TSF: Timestamp flag
This flag is set by hardware when a timestamp event occurs.
If ITSF flag is set, TSF must be cleared together with ITSF.
Bit 2 WUTF: Wake-up timer flag
This flag is set by hardware when the wake-up auto-reload counter reaches 0.
If WUTOCLR[15:0] is different from 0x0000, WUTF is cleared by hardware when the wake-
up auto-reload counter reaches WUTOCLR value.
If WUTOCLR[15:0] is 0x0000, WUTF must be cleared by software.
This flag must be cleared by software at least 1.5 RTCCLK periods before WUTF is set to 1
again.
Bit 1 ALRBF: Alarm B flag
This flag is set by hardware when the time/date registers (RTC_TR and RTC_DR) match the
alarm B register (RTC_ALRMBR).
Bit 0 ALRAF: Alarm A flag
This flag is set by hardware when the time/date registers (RTC_TR and RTC_DR) match the
alarm A register (RTC_ALRMAR).

Real-time clock (RTC) RM0438
1442/2187 RM0438 Rev 8
41.6.21 RTC non-secure masked interr upt status register (RTC_MISR)
This register can be globally protected, or each bit of this register can be individually
protected against non-privileged access. Refer to Section 41.3.5: RTC privilege protection
modes.
Address offset: 0x54
Backup domain reset value: 0x0000 0000
System reset: not affected
Note: The bits of this register  are cleared few APB clock cycles after setting their corresponding
clear bit in the RTC_SCR register. After clearing the flag, read it until it is read at 0 before
leaving the interrupt routine.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. ITS
MF
TSOV
MF
TS
MF
WUT
MF
ALRB
MF
ALRA
MF
rrrrrr
Bits 31:6 Reserved, must be kept at reset value.
Bit 5 ITSMF: Internal timestamp non-secure masked flag
This flag is set by hardware when a timestamp on the internal event occurs and timestamp
non-secure interrupt is raised.
Bit 4 TSOVMF: Timestamp overflow non-secure masked flag
This flag is set by hardware when a timestamp interrupt occurs while TSMF is already set.
It is recommended to check and then clear TSOVF only after clearing the TSF bit. Otherwise,
an overflow might not be noticed if a timestamp event occurs immediately before the TSF bit
is cleared.
Bit 3 TSMF: Timestamp non-secure masked flag
This flag is set by hardware when a timestamp non-secure interrupt occurs.
If ITSF flag is set, TSF must be cleared together with ITSF.
Bit 2 WUTMF: Wake-up timer non-secure masked flag
This flag is set by hardware when the wake-up timer non-secure interrupt occurs.
This flag must be cleared by software at least 1.5 RTCCLK periods before WUTF is set to 1
again.
Bit 1 ALRBMF: Alarm B non-secure masked flag
This flag is set by hardware when the alarm B non-secure interrupt occurs.
Bit 0 ALRAMF: Alarm A masked flag
This flag is set by hardware when the alarm A non-secure interrupt occurs.

RM0438 Rev 8 1443/2187
RM0438 Real-time clock (RTC)
1482
41.6.22 RTC secure masked interrupt  status register (RTC_SMISR)
This register can be globally protected, or each bit of this register can be individually
protected against non-secure access. Refer to Section 41.3.4: RTC secure protection
modes.
This register can be globally protected, or each bit of this register can be individually
protected against non-privileged access. Refer to Section 41.3.5: RTC privilege protection
modes.
Address offset: 0x58
Backup domain reset value: 0x0000 0000
System reset: not affected
Note: The bits of this register  are cleared few APB clock cycles after setting their corresponding
clear bit in the RTC_SCR register. After clearing the flag, read it until it is read at 0 before
leaving the interrupt routine.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. ITS
MF
TSOV
MF
TS
MF
WUT
MF
ALRB
MF
ALRA
MF
rrrrrr
Bits 31:6 Reserved, must be kept at reset value.
Bit 5 ITSMF: Internal timestamp interrupt secure masked flag
This flag is set by hardware when a timestamp on the internal event occurs and timestamp
secure interrupt is raised.
Bit 4 TSOVMF: Timestamp overflow interrupt secure masked flag
This flag is set by hardware when a timestamp secure interrupt occurs while TSMF is already
set.
It is recommended to check and then clear TSOVF only after clearing the TSF bit. Otherwise,
an overflow might not be noticed if a timestamp event occurs immediately before the TSF bit
is cleared.
Bit 3 TSMF: Timestamp interrupt secure masked flag
This flag is set by hardware when a timestamp secure interrupt occurs.
If ITSF flag is set, TSF must be cleared together with ITSF.
Bit 2 WUTMF: Wakeup timer interrupt secure masked flag
This flag is set by hardware when the wakeup timer secure interrupt occurs.
This flag must be cleared by software at least 1.5 RTCCLK periods before WUTF is set to 1
again.
Bit 1 ALRBMF: Alarm B interrupt secure masked flag
This flag is set by hardware when the alarm B secure interrupt occurs.
Bit 0 ALRAMF: Alarm A interrupt secure masked flag
This flag is set by hardware when the alarm A secure interrupt occurs.

Real-time clock (RTC) RM0438
1444/2187 RM0438 Rev 8
41.6.23 RTC status clear  register (RTC_SCR)
This register can be globally protected, or each bit of this register can be individually
protected against non-secure access. Refer to Section 41.3.4: RTC secure protection
modes.
This register can be globally protected, or each bit of this register can be individually
protected against non-privileged access. Refer to Section 41.3.5: RTC privilege protection
modes.
Address offset: 0x5C
Backup domain reset value: 0x0000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CITS
F
CTSOV
F
CTS
F
CWUT
F
CALRB
F
CALRA
F
wwwwww
Bits 31:6 Reserved, must be kept at reset value.
Bit 5 CITSF: Clear internal timestamp flag
Writing 1 in this bit clears the ITSF bit in the RTC_SR register.
Bit 4 CTSOVF: Clear timestamp overflow flag
Writing 1 in this bit clears the TSOVF bit in the RTC_SR register.
It is recommended to check and then clear TSOVF only after clearing the TSF bit. Otherwise,
an overflow might not be noticed if a timestamp event occurs immediately before the TSF bit
is cleared.
Bit 3 CTSF: Clear timestamp flag
Writing 1 in this bit clears the TSOVF bit in the RTC_SR register.
If ITSF flag is set, TSF must be cleared together with ITSF by setting CRSF and CITSF.
Bit 2 CWUTF: Clear wake-up timer flag
Writing 1 in this bit clears the WUTF bit in the RTC_SR register.
Bit 1 CALRBF: Clear alarm B flag
Writing 1 in this bit clears the ALRBF bit in the RTC_SR register.
Bit 0 CALRAF: Clear alarm A flag
Writing 1 in this bit clears the ALRAF bit in the RTC_SR register.

RM0438 Rev 8 1445/2187
RM0438 Real-time clock (RTC)
1482
41.6.24 RTC register map
[Table 317](../tables/table_317.md). RTC register map and reset values
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
0x00 RTC_TR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PM
HT
[1:0] HU[3:0]
Res.MNT[2:0] MNU[3:0]
Res.ST[2:0] SU[3:0]
R e s e t  v a l u e 0000000 0000000 0000000
0x04 RTC_DR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. YT[3:0] YU[3:0] WDU[2:0]
MT MU[3:0]
Res.
Res.
DT
[1:0] DU[3:0]
R e s e t  v a l u e 0000000000100001 000001
0x08 RTC_SSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. SS[15:0]
R e s e t  v a l u e 0000000000000000
0x0C RTC_ICSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
RECALPF
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
INIT
INITF
RSF
INITS
SHPF
WUT WF
Res.
Res.
R e s e t  v a l u e 0 000001
0x10 RTC_PRER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. PREDIV_A[6:0] PREDIV_S[14:0]
R e s e t  v a l u e 11111110000000011111111
0x14 RTC_WUTR WUTOCLR[15:0] WUT[15:0]
R e s e t  v a l u e 00000000000000001111111111111111
0x18 RTC_CR
OUT2EN
TAMPALRM_TYPE
TAMPALRM_PU
Res.
Res.
TAMPOE
TAMPTS
ITSE
COE
O
SEL
[1:0]
POL
COSEL
BKP
SUB1H
ADD1H
TSIE
WUTIE
ALRBIE
ALRAIE
TSE
WUTE
ALRBE
ALRAE
Res.
FMT
BYPSHAD
REFCKON
TSEDGE
WUCK
SEL[2:0]
R e s e t  v a l u e 000 0000000000000000000 0000000
0x1C RTC_PRIVCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
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
INITPRIV
CALPRIV
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TSPRIV
WUTPRIV
ALRBPRIV
ALRAPRIV
R e s e t  v a l u e 000 0000
0x20 RTC_SMCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
DECPROT
INITDPROT
CALDPROT
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TSDPROT
WUTDPROT
ALRBDPROT
ALRADPROT
R e s e t  v a l u e 111 1111
0x24 RTC_WPR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. KEY[7:0]
Reset value 00000000
0x28 RTC_ CALR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CALP
CALW8
CALW16
LPCAL
Res.
Res.
Res. CALM[8:0]
R e s e t  v a l u e 0000 000000000
0x2C RTC_SHIFTR
ADD1S
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. SUBFS[14:0]
R e s e t  v a l u e 0 000000000000000

Real-time clock (RTC) RM0438
1446/2187 RM0438 Rev 8
Refer to Section 2.3 on page 86 for the register boundary addresses.
0x30 RTC_TSTR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PM
HT[1:0]
HU[3:0]
Res.
MNT[2:0]
MNU[3:0]
Res.ST[2:0] SU[3:0]
R e s e t  v a l u e 0000000 0000000 0000000
0x34 RTC_TSDR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.WDU[2:0]
MT MU[3:0]
Res.
Res.
DT
[1:0] DU[3:0]
R e s e t  v a l u e 00000000 000000
0x38 RTC_TSSSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. SS[15:0]
R e s e t  v a l u e 0000000000000000
0x40 RTC_ALRMAR
MSK4
WDSEL
DT
[1:0] DU[3:0]
MSK3
PM
HT
[1:0] HU[3:0]
MSK2
MNT[2:0] MNU[3:0]
MSK1
ST[2:0] SU[3:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x44
RTC_
ALRMASSR
Res.
Res.
Res.
Res.
MASKSS
[3:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. SS[14:0]
R e s e t  v a l u e 0000 000000000000000
0x48 RTC_ALRMBR
MSK4
WDSEL
DT
[1:0] DU[3:0]
MSK3
PM
HT
[1:0] HU[3:0]
MSK2
MNT[2:0] MNU[3:0]
MSK1
ST[2:0] SU[3:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x4C
RTC_
ALRMBSSR
Res.
Res.
Res.
Res.
MASKSS
[3:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. SS[14:0]
R e s e t  v a l u e 0000 000000000000000
0x50 RTC_SR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ITSF
TSOVF
TSF
WUTF
ALRBF
ALRAF
Reset value 000000
0x54 RTC_MISR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ITSMF
TSOVMF
TSMF
WUTMF
ALRBMF
ALRAMF
Reset value 000000
0x58 RTC_SMISR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ITSMF
TSOVMF
TSMF
WUTMF
ALRBMF
ALRAMF
Reset value 000000
0x5C RTC_SCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CITSF
CTSOVF
CTSF
CWUTF
CALRBF
CALRAF
Reset value 000000
[Table 317](../tables/table_317.md). RTC register map and reset values (continued)
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
* [Figure 398: Architectural Diagram](../figures/figure_398.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 308: Configuration Matrix](../tables/table_308.md)
* [Table 309: Configuration Matrix](../tables/table_309.md)
* [Table 310: Configuration Matrix](../tables/table_310.md)
* [Table 311: Configuration Matrix](../tables/table_311.md)
* [Table 312: Configuration Matrix](../tables/table_312.md)
* [Table 313: Configuration Matrix](../tables/table_313.md)
* [Table 314: Configuration Matrix](../tables/table_314.md)
* [Table 315: Configuration Matrix](../tables/table_315.md)
* [Table 316: Configuration Matrix](../tables/table_316.md)
* [Table 317: Configuration Matrix](../tables/table_317.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)