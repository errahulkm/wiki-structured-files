# Chapter 24: Real-time clock (RTC)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32C0 Reference Manual RM0490 - Chapter 24: Real-time clock (RTC).
* **Document Source**: RM0490 Reference Manual
* **PDF Reference Location**: Pages 647 - 677
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Real-Time Clock (RTC)](../peripherals/rtc.md)

## 2. Official Reference Manual Text Content (RM0490 Ingestion)
```text
RM0490 Rev 6 647/1023
RM0490 Real-time clock (RTC)
677
24 Real-time clock (RTC)
24.1 Introduction
The RTC provides an automatic wakeup to manage all low-power modes.
The real-time clock (RTC) is an independent BCD timer/counter. The RTC provides a time-
of-day clock/calendar with programmable alarm interrupts.
As long as the supply voltage remains in the operating range, the RTC never stops,
regardless of the device status (Run mode, low-power mode or under reset).
24.2 RTC main features
The RTC supports the following features (see [Figure 221](../figures/figure_221.md): RTC block diagram):
• Calendar with subsecond, seconds, minutes, hours (12 or 24 format), week day, date,
month, year, in BCD (binary-coded decimal) format.
• Automatic correction for 28, 29 (leap year), 30, and 31 days of the month.
• One programmable alarm.
• On-the-fly correction from 1 to 32767 RTC clock pulses. This can be used to
synchronize it with a master clock.
• Reference clock detection: a more precise second source clock (50 or 60 Hz) can be
used to enhance the calendar precision.
• Digital calibration circuit with 0.95 ppm resolution, to compensate for quartz crystal
inaccuracy.
• Timestamp feature which can be used to save the calendar content. This function can
be triggered by an event on the timestamp pin.
The RTC clock sources can be:
• A 32.768 kHz external crystal (LSE)
• An external resonator or oscillator (LSE)
• The internal low power RC oscillator (LSI, with typical frequency of 32 kHz)
• The high-speed external clock (HSE), divided by a prescaler in the RCC.
The RTC is functional in all low-power modes except Standby and Shutdown when it is
clocked by the LSE or LSI.
All RTC events (Alarm, Timestamp) can generate an interrupt and wakeup the device from
the low-power modes.

Real-time clock (RTC) RM0490
648/1023 RM0490 Rev 6
24.3 RTC functional description
24.3.1 RTC block diagram
[Figure 221](../figures/figure_221.md). RTC block diagram
MSv67530V1
rtc_pclk clock domain
Registers interfacertc_pclk
IRQ interface
rtc_it
Alarm A
RTC_ALRMAR
RTC_ALRMASSR
=
rtc_alra_trg
Shadow registers
RTC_TR,
RTC_DR
Output
control
RTC_OUT1
RTC_OUT2
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
ALARM=
TAMPALARM
RTC_REFIN
RTC_TS
Time stamp registers
RTC_TSTR
RTC_TSDR
RTC_TSSR
Time stamp detection
rtc_ker_ck ck_spre
Smooth
calibration
RTC_CALR
Asynchronous
prescaler
(default = 128)
RTC_PRER
TSF
ck_apre clock domain
ALRAF
rtc_ker_ck clock domain

RM0490 Rev 6 649/1023
RM0490 Real-time clock (RTC)
677
24.3.2 RTC pins and internal signals
• RTC_OUT1 and RTC_OUT2 which selects one of the following two outputs:
– CALIB: 512 Hz or 1 Hz clock output (with an LSE frequency of 32.768 kHz). This
output is enabled by setting the COE bit in the RTC_CR register.
– TAMPALRM: This output is the ALARM output.
ALARM is enabled by configuring the OSEL[1:0] bits in the RTC_CR register which select
the alarm A output.
The RTC kernel clock is usually the LSE at 32.768 kHz although it is possible to select other
clock sources in the RCC (refer to RCC for more details).
The triggers outputs can be used as triggers for other peripherals.
24.3.3 GPIO controlled by the RTC
RTC_OUT1 and RTC_TS are mapped on the same pin.
This pin output mechanism follows the priority order shown in [Table 100](../tables/table_100.md).
[Table 98](../tables/table_98.md). RTC input/output pins
Pin name Signal type Description
RTC_TS Input RTC timestamp input
RTC_REFIN Input RTC 50 or 60 Hz reference clock input
RTC_OUT1 Output RTC output 1
RTC_OUT2 Output RTC output 2
[Table 99](../tables/table_99.md). RTC internal input/output signals
Internal signal name Signal type Description
rtc_ker_ck Input RTC kernel clock, also named RTCCLK in this document
rtc_pclk Input RTC APB clock
rtc_it Output RTC interrupts (refer to Section 24.5: RTC interrupts for details)
rtc_alra_trg Output RTC alarm A event detection trigger

Real-time clock (RTC) RM0490
650/1023 RM0490 Rev 6
In addition, it is possible to output RTC_OUT2 thanks to OUT2EN bit. The different functions
are mapped on RTC_OUT1 or on RTC_OUT2 depending on OSEL, COE and OUT2EN
configuration, as show in table [Table 101](../tables/table_101.md).
[Table 100](../tables/table_100.md). Pin configuration(1)
1. OD: open drain; PP: push-pull.
Pin function
OSEL[1:0]
(ALARM output enable)
COE
(CALIB output enable)
OUT2EN
TAMPALRM_TYPE
TAMPALRM_PU
TSE
(RTC_TS input enable)
TAMPALRM output
Push-Pull 01 Don’t care Don’t care 00 Don’t care
TAMPALRM
output
Open-Drain(2)
2. In this configuration the GPIO must be configured in input.
No pull 01 Don’t care Don’t care 10 Don’t care
Internal
pull-up 01 Don’t care Don’t care 11 Don’t care
CALIB output PP 00 1 0 Don’t care Don’t care Don’t care
RTC_TS input floating
00 0 Don’t care
Don’t
care
Don’t
care 100 1
1Don’t
care 0
Wakeup pin or Standard GPIO
00 0 Don’t care
Don’t
care
Don’t
care 000 1
1Don’t
care 0

RM0490 Rev 6 651/1023
RM0490 Real-time clock (RTC)
677
24.3.4 Clock and prescalers
The RTC clocks must respect this ratio: frequency(PCLK) ≥ 2 × frequency(RTCCLK).
The RTC clock source (RTCCLK) is selected through the clock controller among the LSE
clock, the LSI oscillator clock, and the HSE clock. For more information on the RTC clock
source configuration, refer to Section 6: Reset and clock control (RCC).
A programmable prescaler stage generates a 1 Hz clock which is used to update the
calendar. To minimize power consumption, the prescaler is split into 2 programmable
prescalers (see [Figure 221](../figures/figure_221.md): RTC block diagram):
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
The ck_apre clock is used to clock the binary RTC_SSR subseconds downcounter. When it
reaches 0, RTC_SSR is reloaded with the content of PREDIV_S.
[Table 101](../tables/table_101.md). RTC_OUT mapping
OSEL[1:0] bits
ALARM
output enable)
COE bit (CALIB
output enable)
OUT2EN
bit RTC_OUT1 RTC_OUT2
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
fCK_APRE
fRTCCLK
PREDIV_A 1+---------------------------------------=

Real-time clock (RTC) RM0490
652/1023 RM0490 Rev 6
fck_spre is given by the following formula:
24.3.5 Real-time clock and calendar
The RTC calendar time and date registers are accessed through shadow registers which
are synchronized with PCLK (APB clock). They can also be accessed directly in order to
avoid waiting for the synchronization duration.
• RTC_SSR for the subseconds
• RTC_TR for the time
• RTC_DR for the date
Every RTCCLK periods, the current calendar value is copied into the shadow registers, and
the RSF bit of RTC_ICSR register is set (see Section 24.6.9: RTC shift control register
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
24.3.6 Programmable alarms
The RTC unit provides programmable alarm: alarm A.
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
Alarm A (if enabled by bits OSEL[1:0] in RTC_CR register) can be routed to the TAMPALRM
output. TAMPALRM output polarity can be configured through bit POL the RTC_CR register.
fCK_SPRE
fRTCCLK
PREDIV_S 1+() PREDIV_A 1+()×-----------------------------------------------------------------------------------------------=

RM0490 Rev 6 653/1023
RM0490 Real-time clock (RTC)
677
24.3.7 RTC initialization and configuration
RTC register access
The RTC registers are 32-bit registers. The APB interface introduces two wait states in RTC
register accesses except on read accesses to calendar shadow registers when
BYPSHAD = 0.
RTC register write protection
After Power-on reset, some of the RTC registers are write-protected.
Writing to the protected RTC registers is enabled by writing a key into the Write Protection
register, RTC_WPR.
The following steps are required to unlock the write protection on the protected RTC
registers.
1. Write 0xCA into the RTC_WPR register.
2. Write 0x53 into the RTC_WPR register.
Writing a wrong key reactivates the write protection.
The protection mechanism is not affected by system reset.
Calendar initialization and configuration
To program the initial time and date calendar values, including the time format and the
prescaler configuration, the following sequence is required:
1. Set INIT bit to 1 in the RTC_ ICSR register to enter initialization mode. In this mode, the
calendar counter is stopped and its value can be updated.
2. Poll INITF bit of in the RTC_ICSR regist er. The initialization phase mode is entered
when INITF is set to 1. It takes around 2 RTCCLK clock cycles (due to clock
synchronization).
3. To generate a 1 Hz clock for the calendar counter, program both the prescaler factors
in RTC_PRER register.
4. Load the initial time and date values in the shadow registers (RTC_TR and RTC_DR),
and configure the time format (12 or 24 hours) through the FMT bit in the RTC_CR
register.
5. Exit the initialization mode by clearing the INIT bit. The actual calendar counter value is
then automatically loaded and the counting restarts after 4 RTCCLK clock cycles.
When the initialization sequence is complete, the calendar starts counting.
Note: After a system reset, the application can read the INITS flag in the RTC_ICSR register to
check if the calendar has been initialized or not. If this flag equals 0, the calendar has not
been initialized since the year field is set at its Power-on reset default value (0x00).
To read the calendar after initialization, the software must first check that the RSF flag is set
in the RTC_ICSR register.
Daylight saving time
The daylight saving time management is performed through bits SUB1H, ADD1H, and BKP
of the RTC_CR register.

Real-time clock (RTC) RM0490
654/1023 RM0490 Rev 6
Using SUB1H or ADD1H, the software can subtract or add one hour to the calendar in one
single operation without going through the initialization procedure.
In addition, the software can use the BKP bit to memorize this operation.
Programming the alarm
A similar procedure must be followed to program or update the programmable alarms. The
procedure below is given for alarm A.
1. Clear ALRAE in RTC_CR to disable alarm A.
2. Program the alarm A regist ers (RTC_ALRMASSR/RTC_ALRMAR).
3. Set ALRAE in the RTC_CR register to enable alarm A again.
Note: Each change of the RTC_CR register is taken into account after around 2 RTCCLK clock
cycles due to clock synchronization.
24.3.8 Reading the calendar
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
RTCCLK cycles. To ensure consistency between the 3 values, reading either RTC_SSR or
RTC_TR locks the values in the higher-order calendar shadow registers until RTC_DR is
read. In case the software makes read accesses to the calendar in a time interval smaller
than 1 RTCCLK periods: RSF must be cleared by software after the first calendar read, and
then the software must wait until RSF is set before reading again the RTC_SSR, RTC_TR
and RTC_DR registers.
After waking up from low-power mode (Stop or Standby), RSF must be cleared by software.
The software must then wait until it is set again before reading the RTC_SSR, RTC_TR and
RTC_DR registers.
The RSF bit must be cleared after wakeup and not before entering low-power mode.
After a system reset, the software must wait until RSF is set before reading the RTC_SSR,
RTC_TR and RTC_DR registers. Indeed, a system reset resets the shadow registers to
their default values.
After an initialization (refer to Calendar initialization and configuration on page 653): the
software must wait until RSF is set before reading the RTC_SSR, RTC_TR and RTC_DR
registers.
After synchronization (refer to Section 24.3.10: RTC synchronization): the software must
wait until RSF is set before reading the RTC_SSR, RTC_TR and RTC_DR registers.

RM0490 Rev 6 655/1023
RM0490 Real-time clock (RTC)
677
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
24.3.9 Resetting the RTC
The calendar shadow registers (RTC_SSR, RTC_TR and RTC_DR) and some bits of the
RTC status register (RTC_ICSR) are reset to their default values by all available system
reset sources.
On the contrary, the following registers are reset to their default values by a Power-on reset
and are not affected by a system reset: the RTC current calendar registers, the RTC control
register (RTC_CR), the prescaler register (RTC_PRER), the RTC calibration register
(RTC_CALR), the RTC shift register (RTC_SHIFTR), the RTC timestamp registers
(RTC_TSSSR, RTC_TSTR and RTC_TSDR) and the alarm A registers
(RTC_ALRMASSR/RTC_ALRMAR.
In addition, when clocked by LSE, the RTC keeps on running under system reset if the reset
source is different from the Power-on reset one (refer to RCC for details about RTC clock
sources not affected by system reset). When a Power-on reset occurs, the RTC is stopped
and all the RTC registers are set to their reset values.
24.3.10 RTC synchronization
The RTC can be synchronized to a remote clock with a high degree of precision. After
reading the sub-second field (RTC_SSR or RTC_TSSSR), a calculation can be made of the
precise offset between the times being maintained by the remote clock and the RTC. The
RTC can then be adjusted to eliminate this offset by “shifting” its clock by a fraction of a
second using RTC_SHIFTR.
RTC_SSR contains the value of the synchronous prescaler counter. This allows one to
calculate the exact time being maintained by the RTC down to a resolution of
1 / (PREDIV_S + 1) seconds. As a consequence, the resolution can be improved by
increasing the synchronous prescaler value (PREDIV_S[14:0]. The maximum resolution
allowed (30.52 µs with a 32768 Hz clock) is obtained with PREDIV_S set to 0x7FFF.
However, increasing PREDIV_S means that PREDIV_A must be decreased in order to
maintain the synchronous prescaler output at 1 Hz. In this way, the frequency of the
asynchronous prescaler output increases, which may increase the RTC dynamic
consumption.

Real-time clock (RTC) RM0490
656/1023 RM0490 Rev 6
The RTC can be finely adjusted using the RTC shift control register (RTC_SHIFTR). Writing
to RTC_SHIFTR can shift (either delay or advance) the clock by up to a second with a
resolution of 1 / (PREDIV_S + 1) seconds. The shift operation consists of adding the
SUBFS[14:0] value to the synchronous prescaler counter SS[15:0]: this will delay the clock.
If at the same time the ADD1S bit is set, this results in adding one second and at the same
time subtracting a fraction of second, so this will advance the clock.
Caution: Before initiating a shift operation, the user must check that SS[15] = 0 in order to ensure that
no overflow will occur.
As soon as a shift operation is initiated by a write to the RTC_SHIFTR register, the SHPF
flag is set by hardware to indicate that a shift operation is pending. This bit is cleared by
hardware as soon as the shift operation has completed.
Caution: This synchronization feature is not compatible with the reference clock detection feature:
firmware must not write to RTC_SHIFTR when REFCKON = 1.
24.3.11 RTC referen ce clock detection
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

RM0490 Rev 6 657/1023
RM0490 Real-time clock (RTC)
677
24.3.12 RTC smooth digital calibration
The RTC frequency can be digitally calibrated with a resolution of about 0.954 ppm with a
range from -487.1 ppm to +488.5 ppm. The correction of the frequency is performed using
series of small adjustments (adding and/or subtracting individual RTCCLK pulses). These
adjustments are fairly well distributed so that the RTC is well calibrated even when observed
over short durations of time.
The smooth digital calibration is performed during a calibration cycle of about 220 RTCCLK
pulses, or 32 seconds when the input frequency is 32768 Hz. This cycle is maintained by a
20-bit counter, cal_cnt[19:0], clocked by RTCCLK.
The smooth calibration register (RTC_CALR) specifies the number of RTCCLK clock cycles
to be masked during the calibration cycle:
• Setting the bit CALM[0] to 1 causes exactly one pulse to be masked during the
calibration cycle.
• Setting CALM[1] to 1 causes two additional cycles to be masked
• Setting CALM[2] to 1 causes four additional cycles to be masked
• and so on up to CALM[8] set to 1 which causes 256 clocks to be masked.
Note: CALM[8:0] (RTC_CALR) specifies the number of RTCCLK pulses to be masked during the
calibration cycle. Setting the bit CALM[0] to 1 causes exactly one pulse to be masked during
the calibration cycle at the moment when cal_cnt[19:0] is 0x80000; CALM[1] = 1 causes two
other cycles to be masked (when cal_cnt is 0x40000 and 0xC0000); CALM[2] = 1 causes
four other cycles to be masked (cal_cnt = 0x20000/0x60000/0xA0000/ 0xE0000); and so on
up to CALM[8] = 1 which causes 256 clocks to be masked (cal_cnt = 0xXX800).
While CALM allows the RTC frequency to be reduced by up to 487.1 ppm with fine
resolution, the bit CALP can be used to increase the frequency by 488.5 ppm. Setting CALP
to 1 effectively inserts an extra RTCCLK pulse every 211 RTCCLK cycles, which means that
512 clocks are added during every calibration cycle.
Using CALM together with CALP, an offset ranging from -511 to +512 RTCCLK cycles can
be added during the calibration cycle, which translates to a calibration range of -487.1 ppm
to +488.5 ppm with a resolution of about 0.954 ppm.
The formula to calculate the effective calibrated frequency (FCAL) given the input frequency
(FRTCCLK) is as follows:
FCAL = FRTCCLK x [1 + (CALP x 512 - CALM) / (220 + CALM - CALP x 512)]
Calibration when PREDIV_A < 3
The CALP bit can not be set to 1 when the asynchronous prescaler value (PREDIV_A bits in
RTC_PRER register) is less than 3. If CALP was already set to 1 and PREDIV_A bits are
set to a value less than 3, CALP is ignored and the calibration operates as if CALP was
equal to 0.
To perform a calibration with PREDIV_A less than 3, the synchronous prescaler value
(PREDIV_S) should be reduced so that each second is accelerated by 8 RTCCLK clock
cycles, which is equivalent to adding 256 clock cycles every calibration cycle. As a result,
between 255 and 256 clock pulses (corresponding to a calibration range from 243.3 to
244.1 ppm) can effectively be added during each calibration cycle using only the CALM bits.
With a nominal RTCCLK frequency of 32768 Hz, when PREDIV_A equals 1 (division factor
of 2), PREDIV_S should be set to 16379 rather than 16383 (4 less). The only other

Real-time clock (RTC) RM0490
658/1023 RM0490 Rev 6
interesting case is when PREDIV_A equals 0, PREDIV_S should be set to 32759 rather
than 32767 (8 less).
If PREDIV_S is reduced in this way, the formula given the effective frequency of the
calibrated input clock is as follows:
FCAL = FRTCCLK x [1 + (256 - CALM) / (220 + CALM - 256)]
In this case, CALM[7:0] equals 0x100 (the midpoint of the CALM range) is the correct
setting if RTCCLK is exactly 32768.00 Hz.
Verifying the RTC calibration
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
Re-calibration on-the-fly
The calibration register (RTC_CALR) can be updated on-the-fly while RTC_ICSR/INITF = 0,
by using the follow process:
1. Poll the RTC_ICSR/RECALPF (re-calibration pending flag).
2. If it is set to 0, write a new value to  RTC_CALR, if necessary. RECALPF is then
automatically set to 1
3. Within three ck_apre cycles after the writ e operation to RTC_CALR, the new calibration
settings take effect.
24.3.13 Timestamp function
Timestamp is enabled by setting the TSE or ITSE bits of RTC_CR register to 1.

RM0490 Rev 6 659/1023
RM0490 Real-time clock (RTC)
677
When TSE is set:
The calendar is saved in the timestamp registers (RTC_TSSSR, RTC_TSTR, RTC_TSDR)
when a timestamp event is detected on the RTC_TS pin.
When a timestamp event occurs, the timestamp flag bit (TSF) in RTC_SR register is set.
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
24.3.14 Calibration clock output
When the COE bit is set to 1 in the RTC_CR register, a reference clock is provided on the
CALIB device output.
If the COSEL bit in the RTC_CR register is reset and PREDIV_A = 0x7F, the CALIB
frequency is fRTCCLK/64. This corresponds to a calibration output at 512 Hz for an RTCCLK
frequency at 32.768 kHz. The CALIB duty cycle is irregular: there is a light jitter on falling
edges. It is therefore recommended to use rising edges.
When COSEL is set and “PREDIV_S+1” is a non-zero multiple of 256 (i.e: PREDIV_S[7:0] =
0xFF), the CALIB frequency is fRTCCLK/(256 * (PREDIV_A+1)). This corresponds to a
calibration output at 1 Hz for prescaler default values (PREDIV_A = Ox7F, PREDIV_S =
0xFF), with an RTCCLK frequency at 32.768 kHz.
Note: When COSEL is cleared, the CALI B output is the output of the 6th stage of the
asynchronous prescaler.
When COSEL is set, the CALIB output is the output of the 8th stage of the synchronous
prescaler.
24.3.15 Alarm output
The OSEL[1:0] control bits in the RTC_CR register are used to activate the alarm output
TAMPALRM, and to select the function which is output. These functions reflect the contents
of the corresponding flag in the RTC_SR register.
The polarity of the TAMPALRM output is determined by the POL control bit in RTC_CR so
that the opposite of the selected flags bit is output when POL is set to 1.

Real-time clock (RTC) RM0490
660/1023 RM0490 Rev 6
TAMPALRM output
The TAMPALRM pin can be configured in output open drain or output push-pull using the
control bit TAMPALRM_TYPE in the RTC_CR register. It is possible to apply the internal
pull-up in output mode thanks to TAMPALRM_PU in the RTC_CR.
Note: Once the TAMPALRM output is enabled, it has priority over CALIB on RTC_OUT1.
24.4 RTC low-power modes
The table below summarizes the RTC pins and functions capability in all modes.
24.5 RTC interrupts
The interrupt channel is set in the masked interrupt status register. The interrupt output is
also activated.
[Table 102](../tables/table_102.md). Effect of low-power modes on RTC
Mode Description
Sleep No effect RTC interrupts cause the device to exit the Sleep mode.
Stop The RTC remains active when the RTC clock source is LSE or LSI. RTC interrupts cause the device to exit the Stop mode.
Standby The RTC is powered down and must be re-initialized after exiting Standby mode.
Shutdown The RTC is powered down and must be re-initialized after exiting Shutdown mode.
[Table 103](../tables/table_103.md). RTC pins functionality over modes
Functions
Functional in all low-power
modes except Standby and
Shutdown modes
Functional in Standby and
Shutdown mode
RTC_TS Yes No
RTC_REFIN Yes No
RTC_OUT1 Yes No
RTC_OUT2 Yes No
[Table 104](../tables/table_104.md). Interrupt requests
Interrupt
acronym Interrupt event Event flag(1) Enable control bit(2) Interrupt clear method Exit from Sleep mode Exit from Stop mode Exit from Standby and Shutdown mode
RTC
Alarm A ALRAF ALRAIE write 1 in CALRAF Yes Yes (3) No
Timestamp TSF TSIE write 1 in CTSF Yes Yes (3) No

RM0490 Rev 6 661/1023
RM0490 Real-time clock (RTC)
677
24.6 RTC registers
Refer to Section 1.2 on page 41 of the reference manual for a list of abbreviations used in
register descriptions.
The peripheral registers can be accessed by words (32-bit).
24.6.1 RTC time register (RTC_TR)
The RTC_TR is the calendar time shadow register. This register must be written in
initialization mode only. Refer to Calendar initialization and configuration on page 653 and
Reading the calendar on page 654.
This register is write protected. The write access procedure is described in RTC register
write protection on page 653.
Address offset: 0x00
Power-on reset value: 0x0000 0000
System reset value: 0x0000 0000 (when BYPSHAD = 0, not affected when BYPSHAD = 1)
1. The event flags are in the RTC_SR register.
2. The interrupt masked flags (resulting from event flags AND enable control bits) are in the RTC_MISR register.
3. Wakeup from Stop mode is possible only when the RTC clock source is LSE or LSI.
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

Real-time clock (RTC) RM0490
662/1023 RM0490 Rev 6
24.6.2 RTC date register (RTC_DR)
The RTC_DR is the calendar date shadow register. This register must be written in
initialization mode only. Refer to Calendar initialization and configuration on page 653 and
Reading the calendar on page 654.
This register is write protected. The write access procedure is described in RTC register
write protection on page 653.
Address offset: 0x04
Power-on reset value: 0x0000 2101
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

RM0490 Rev 6 663/1023
RM0490 Real-time clock (RTC)
677
24.6.3 RTC sub second register (RTC_SSR)
Address offset: 0x08
Power-on reset value: 0x0000 0000
System reset value: 0x0000 0000 (when BYPSHAD = 0, not affected when BYPSHAD = 1)
24.6.4 RTC initialization control and status register (RTC_ICSR)
This register is write protected. The write access procedure is described in RTC register
write protection on page 653.
Address offset: 0x0C
Power-on reset value: 0x0000 0007
System reset value: 0bxxxx xxxx xxxx xxxx xxxx xxxx 000x xxxx (not affected, except INIT,
INITF, and RSF bits which are cleared to 0)
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
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. RECALPF
r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. INIT INITF RSF INITS SHPF Res. Res. ALRAWF
rw r rc_w0 r r r
Bits 31:17 Reserved, must be kept at reset value.
Bit 16 RECALPF: Recalibration pending Flag
The RECALPF status flag is automatically set to 1 when software writes to the RTC_CALR
register, indicating that the RTC_CALR register is blocked. When the new calibration settings
are taken into account, this bit returns to 0. Refer to Re-calibration on-the-fly.
Bits 15:8 Reserved, must be kept at reset value.

Real-time clock (RTC) RM0490
664/1023 RM0490 Rev 6
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
This bit is set by hardware when the calendar year field is different from 0 (Power-on reset
state).
0: Calendar has not been initialized
1: Calendar has been initialized
Bit 3 SHPF: Shift operation pending
This flag is set by hardware as soon as a shift operation is initiated by a write to the
RTC_SHIFTR register. It is cleared by hardware when the corresponding shift operation has
been executed. Writing to the SHPF bit has no effect.
0: No shift operation is pending
1: A shift operation is pending
Bits 2:1 Reserved, must be kept at reset value.
Bit 0 ALRAWF: Alarm A write flag
This bit is set by hardware when alarm A values can be changed, after the ALRAE bit has
been set to 0 in RTC_CR.
It is cleared by hardware in initialization mode.
0: Alarm A update not allowed
1: Alarm A update allowed

RM0490 Rev 6 665/1023
RM0490 Real-time clock (RTC)
677
24.6.5 RTC prescaler re gister (RTC_PRER)
This register must be written in initialization mode only. The initialization must be performed
in two separate write accesses. Refer to Calendar initialization and configuration on
page 653.
This register is write protected. The write access procedure is described in RTC register
write protection on page 653.
Address offset: 0x10
Power-on reset value: 0x007F 00FF
System reset: not affected
24.6.6 RTC control register (RTC_CR)
This register is write protected. The write access procedure is described in RTC register
write protection on page 653.
Address offset: 0x18
Power-on reset value: 0x0000 0000
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
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
OUT2
EN
TAMP
ALRM_
TYPE
TAMP
ALRM_
PU
Res. Res. Res. Res. Res. COE OSEL[1:0] POL COSEL BKP SUB1H ADD1H
rw rw rw rw rw rw rw rw rw w w
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
TSIE Res. Res. ALRAIE TSE Res. Res. ALRAE Res. FMT BYPSHAD REFCKON TSEDGE Res. Res. Res.
rw rw rw rw rw rw rw rw

Real-time clock (RTC) RM0490
666/1023 RM0490 Rev 6
Bit 31 OUT2EN: RTC_OUT2 output enable
Setting this bit allows to remap the RTC outputs on RTC_OUT2 as follows:
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
Bits 28:24 Reserved, must be kept at reset value.
Bit 23 COE: Calibration output enable
This bit enables the CALIB output
0: Calibration output disabled
1: Calibration output enabled
Bits 22:21 OSEL[1:0]: Output selection
These bits are used to select the flag to be routed to TAMPALRM output.
00: Output disabled
01: Alarm A output enabled
10: Reserved
11: Reserved
Bit 20 POL: Output polarity
This bit is used to configure the polarity of TAMPALRM output.
0: The pin is high when ALRAF is asserted (depending on OSEL[1:0]).
1: The pin is low when ALRAF is asserted (depending on OSEL[1:0]).
Bit 19 COSEL: Calibration output selection
When COE = 1, this bit selects which signal is output on CALIB.
0: Calibration output is 512 Hz
1: Calibration output is 1 Hz
These frequencies are valid for RTCCLK at 32.768kHz and prescalers at their default values
(PREDIV_A = 127 and PREDIV_S = 255). Refer to Section 24.3.14: Calibration clock output.
Bit 18 BKP: Backup
This bit can be written by the user to memorize whether the daylight saving time change has
been performed or not.
Bit 17 SUB1H: Subtract 1 hour (winter time change)
When this bit is set outside initialization mode, 1 hour is subtracted to the calendar time if the
current hour is not 0. This bit is always read as 0.
Setting this bit has no effect when current hour is 0.
0: No effect
1: Subtracts 1 hour to the current time. This can be used for winter time change.

RM0490 Rev 6 667/1023
RM0490 Real-time clock (RTC)
677
Note: Bits 6 and 4 of this register can be written in initialization mode only (RTC_ICSR/INITF = 1).
It is recommended not to change the hour during the calendar hour increment as it could
mask the incrementation of the calendar hour.
ADD1H and SUB1H changes are effective in the next second.
Bit 16 ADD1H: Add 1 hour (summer time change)
When this bit is set outside initialization mode, 1 hour is added to the calendar time. This bit
is always read as 0.
0: No effect
1: Adds 1 hour to the current time. This can be used for summer time change
Bit 15 TSIE: Timestamp interrupt enable
0: Timestamp interrupt disable
1: Timestamp interrupt enable
Bits 14:13 Reserved, must be kept at reset value.
Bit 12 ALRAIE: Alarm A interrupt enable
0: Alarm A interrupt disabled
1: Alarm A interrupt enabled
Bit 11 TSE: timestamp enable
0: timestamp disable
1: timestamp enable
Bits 10:9 Reserved, must be kept at reset value.
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
Bits 2:0 Reserved, must be kept at reset value.

Real-time clock (RTC) RM0490
668/1023 RM0490 Rev 6
24.6.7 RTC write protectio n register (RTC_WPR)
Address offset: 0x24
Reset value: 0x0000 0000
24.6.8 RTC calibration register (RTC_CALR)
This register is write protected. The write access procedure is described in RTC register
write protection on page 653.
Address offset: 0x28
Power-on reset value: 0x0000 0000
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
CALP CALW8 CALW16 Res. Res. Res. Res. CALM[8:0]
rw rw rw rw rw rw rw rw rw rw rw rw

RM0490 Rev 6 669/1023
RM0490 Real-time clock (RTC)
677
24.6.9 RTC shift control register (RTC_SHIFTR)
This register is write protected. The write access procedure is described in RTC register
write protection on page 653.
Address offset: 0x2C
Power-on reset value: 0x0000 0000
System reset: not affected
Bits 31:16 Reserved, must be kept at reset value.
Bit 15 CALP: Increase frequency of RTC by 488.5 ppm
0: No RTCCLK pulses are added.
1: One RTCCLK pulse is effectively inserted every 211 pulses (frequency increased by
488.5 ppm).
This feature is intended to be used in conjunction with CALM, which lowers the frequency of
the calendar with a fine resolution. if the input frequency is 32768 Hz, the number of
RTCCLK pulses added during a 32-second window is calculated as follows: (512 × CALP) -
CALM.
Refer to Section 24.3.12: RTC smooth digital calibration.
Bit 14 CALW8: Use an 8-second calibration cycle period
When CALW8 is set to 1, the 8-second calibration cycle period is selected.
Note: CALM[1:0] are stuck at 00 when CALW8 = 1. Refer to Section 24.3.12: RTC smooth
digital calibration.
Bit 13 CALW16: Use a 16-second calibration cycle period
When CALW16 is set to 1, the 16-second calibration cycle period is selected. This bit must
not be set to 1 if CALW8 = 1.
Note: CALM[0] is stuck at 0 when CALW16 = 1. Refer to Section 24.3.12: RTC smooth digital
calibration.
Bits 12:9 Reserved, must be kept at reset value.
Bits 8:0 CALM[8:0]: Calibration minus
The frequency of the calendar is reduced by masking CALM out of 220 RTCCLK pulses (32
seconds if the input frequency is 32768 Hz). This decreases the frequency of the calendar
with a resolution of 0.9537 ppm.
To increase the frequency of the calendar, this feature should be used in conjunction with
CALP. See Section 24.3.12: RTC smooth digital calibration on page 657.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ADD1S Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res.
w
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. SUBFS[14:0]
wwwwwwwwwwwwwww

Real-time clock (RTC) RM0490
670/1023 RM0490 Rev 6
24.6.10 RTC timestamp ti me register (RTC_TSTR)
The content of this register is valid only when TSF is set to 1 in RTC_SR. It is cleared when
TSF bit is reset.
Address offset: 0x30
Power-on reset value: 0x0000 0000
System reset: not affected
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

RM0490 Rev 6 671/1023
RM0490 Real-time clock (RTC)
677
24.6.11 RTC timestamp da te register (RTC_TSDR)
The content of this register is valid only when TSF is set to 1 in RTC_SR. It is cleared when
TSF bit is reset.
Address offset: 0x34
Power-on reset value: 0x0000 0000
System reset: not affected
24.6.12 RTC timestamp sub s econd register (RTC_TSSSR)
The content of this register is valid only when TSF is set to 1 in RTC_SR. It is cleared when
the TSF bit is reset.
Address offset: 0x38
Power-on reset value: 0x0000 0000
System reset: not affected
Bit 7 Reserved, must be kept at reset value.
Bits 6:4 ST[2:0]: Second tens in BCD format.
Bits 3:0 SU[3:0]: Second units in BCD format.
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
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
SS[15:0]
rrrrrrrrrrrrrrrr

Real-time clock (RTC) RM0490
672/1023 RM0490 Rev 6
24.6.13 RTC alarm A re gister (RTC_ALRMAR)
This register can be written only when ALRAWF is set to 1 in RTC_ICSR, or in initialization
mode.
This register is write protected. The write access procedure is described in RTC register
write protection on page 653.
Address offset: 0x40
Power-on reset value: 0x0000 0000
System reset: not affected
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 SS[15:0]: Sub second value
SS[15:0] is the value of the synchronous prescaler counter when the timestamp event
occurred.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
MSK4 WDSEL DT[1:0] DU[3:0] MSK3 PM HT[1:0] HU[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
MSK2 MNT[2:0] MNU[3:0] MSK1 ST[2:0] SU[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
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

RM0490 Rev 6 673/1023
RM0490 Real-time clock (RTC)
677
24.6.14 RTC alarm A sub sec ond register (RTC_ALRMASSR)
This register can be written only when ALRAWF is set to 1 in RTC_ICSR, or in initialization
mode.
This register is write protected. The write access procedure is described in RTC register
write protection on page 653.
Address offset: 0x44
Power-on reset value: 0x0000 0000
System reset: not affected
24.6.15 RTC status register (RTC_SR)
Address offset: 0x50
Bit 7 MSK1: Alarm A seconds mask
0: Alarm A set if the seconds match
1: Seconds don’t care in alarm A comparison
Bits 6:4 ST[2:0]: Second tens in BCD format.
Bits 3:0 SU[3:0]: Second units in BCD format.
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

Real-time clock (RTC) RM0490
674/1023 RM0490 Rev 6
Power-on reset value: 0x0000 0000
System reset: not affected
Note: The bits of this register  are cleared few APB clock cycles after setting their corresponding
clear bit in the RTC_SCR register. After clearing the flag, read it until it is read at 0 before
leaving the interrupt routine.
24.6.16 RTC masked interrupt status register (RTC_MISR)
Address offset: 0x54
Power-on reset value: 0x0000 0000
System reset: not affected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. TSOVF TSF Res. Res. ALRAF
rr r
Bits 31:5 Reserved, must be kept at reset value.
Bit 4 TSOVF: Timestamp overflow flag
This flag is set by hardware when a timestamp event occurs while TSF is already set.
It is recommended to check and then clear TSOVF only after clearing the TSF bit. Otherwise,
an overflow might not be noticed if a timestamp event occurs immediately before the TSF bit
is cleared.
Bit 3 TSF: Timestamp flag
This flag is set by hardware when a timestamp event occurs.
Bits 2:1 Reserved, must be kept at reset value.
Bit 0 ALRAF: Alarm A flag
This flag is set by hardware when the time/date registers (RTC_TR and RTC_DR) match the
alarm A register (RTC_ALRMAR).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. TSOVMF TSMF Res. Res. ALRAMF
rr r

RM0490 Rev 6 675/1023
RM0490 Real-time clock (RTC)
677
Note: The bits of this register  are cleared few APB clock cycles after setting their corresponding
clear bit in the RTC_SCR register. After clearing the flag, read it until it is read at 0 before
leaving the interrupt routine.
24.6.17 RTC status clear  register (RTC_SCR)
Address offset: 0x5C
Power-on reset value: 0x0000 0000
System reset: not affected
Bits 31:5 Reserved, must be kept at reset value.
Bit 4 TSOVMF: Timestamp overflow masked flag
This flag is set by hardware when a timestamp interrupt occurs while TSMF is already set.
It is recommended to check and then clear TSOVF only after clearing the TSF bit. Otherwise,
an overflow might not be noticed if a timestamp event occurs immediately before the TSF bit
is cleared.
Bit 3 TSMF: Timestamp masked flag
This flag is set by hardware when a timestamp interrupt occurs.
Bits 2:1 Reserved, must be kept at reset value.
Bit 0 ALRAMF: Alarm A masked flag
This flag is set by hardware when the alarm A interrupt occurs.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CTSOVF CTSF Res. Res. CALRAF
ww w
Bits 31:5 Reserved, must be kept at reset value.
Bit 4 CTSOVF: Clear timestamp overflow flag
Writing 1 in this bit clears the TSOVF bit in the RTC_SR register.
It is recommended to check and then clear TSOVF only after clearing the TSF bit. Otherwise,
an overflow might not be noticed if a timestamp event occurs immediately before the TSF bit
is cleared.
Bit 3 CTSF: Clear timestamp flag
Writing 1 in this bit clears the TSOVF bit in the RTC_SR register.
Bits 2:1 Reserved, must be kept at reset value.
Bit 0 CALRAF: Clear alarm A flag
Writing 1 in this bit clears the ALRAF bit in the RTC_SR register.

Real-time clock (RTC) RM0490
676/1023 RM0490 Rev 6
24.6.18 RTC register map
[Table 105](../tables/table_105.md). RTC register map and reset values
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
Res.
Res.
ALRAWF
R e s e t  v a l u e 0 00000 1
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
0x14 Reserved Res.
0x18 RTC_CR
OUT2EN
TAMPALRM_TYPE
TAMPALRM_PU
Res.
Res.
Res.
Res.
Res.
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
Res.
Res.
ALRAIE
TSE
Res.
Res.
ALRAE
Res.
FMT
BYPSHAD
REFCKON
TSEDGE
Res.
Res.
Res.
R e s e t  v a l u e 000 000000000 00 0 0000
0x20 Reserved Res.
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
Res.
Res.
Res.
Res. CALM[8:0]
R e s e t  v a l u e 000 000000000
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
Res.WDU[1:0]
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

RM0490 Rev 6 677/1023
RM0490 Real-time clock (RTC)
677
Refer to Section 2.2 on page 45 for the register boundary addresses.
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
0x48 -
0x4C Reserved Res.
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
Res.
TSOVF
TSF
Res.
Res.
ALRAF
Reset value 00 0
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
Res.
TSOVMF
TSMF
Res.
Res.
ALRAMF
Reset value 00 0
0x58 Reserved Res.
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
Res.
CTSOVF
CTSF
Res.
Res.
CALRAF
Reset value 00 0
[Table 105](../tables/table_105.md). RTC register map and reset values (continued)
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
* [Figure 221: Architectural Diagram](../figures/figure_221.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 98: Configuration Matrix](../tables/table_98.md)
* [Table 99: Configuration Matrix](../tables/table_99.md)
* [Table 100: Configuration Matrix](../tables/table_100.md)
* [Table 101: Configuration Matrix](../tables/table_101.md)
* [Table 102: Configuration Matrix](../tables/table_102.md)
* [Table 103: Configuration Matrix](../tables/table_103.md)
* [Table 104: Configuration Matrix](../tables/table_104.md)
* [Table 105: Configuration Matrix](../tables/table_105.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)