# Chapter 37: Low-power timer (LPTIM)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 37: Low-power timer (LPTIM).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 1352 - 1378
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Timers (TIM)](../peripherals/timers.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
Low-power timer (LPTIM) RM0438
1352/2187 RM0438 Rev 8
37 Low-power timer (LPTIM)
37.1 LPTIM introduction
The LPTIM is a 16-bit timer that benefits from the ultimate developments in power
consumption reduction. Thanks to its diversity of clock sources, the LPTIM is able to keep
running in all power modes except for Standby mode. Given its capability to run even with
no internal clock source, the LPTIM can be used as a “Pulse Counter” which can be useful
in some applications. The LPTIM capability to wake up the system from low-power modes,
makes it suitable to realize “Timeout functions” with extremely low power consumption.
The LPTIM introduces a flexible clock scheme that provides the needed functionalities and
performance, while minimizing the power consumption.
37.2 LPTIM main features
• 16-bit upcounter
• 3-bit prescaler with 8 possible dividing factors (1,2,4,8,16,32,64,128)
• Selectable clock
– Internal clock sources: configurable internal clock source (see RCC section)
– External clock source over LPTIM input (working with no LP oscillator running,
used by pulse counter application)
• 16-bit ARR autoreload register
• 16-bit compare register
• Continuous/One-shot mode
• Selectable software/hardware input trigger
• Programmable digital glitch filter
• Configurable output: Pulse, PWM
• Configurable I/O polarity
• Encoder mode
• Repetition counter
37.3 LPTIM implementation
[Table 295](../tables/table_295.md) describes LPTIM implementation on STM32L552xx and STM32L562xx devices.
The full set of features is implemented in LPTIM1. LPTIM2 and LPTIM3 support a smaller
set of features, but is otherwise identical to LPTIM1.
[Table 295](../tables/table_295.md). STM32L552xx and STM32L562xx LPTIM features
LPTIM modes/features(1) LPTIM1 LPTIM2 LPTIM3
Encoder mode X - -
External input clock X X X
Wake-up from Stop (2) (3) (2)
1. X = supported.

RM0438 Rev 8 1353/2187
RM0438 Low-power timer (LPTIM)
1378
37.4 LPTIM functional description
37.4.1 LPTIM block diagram
[Figure 386](../figures/figure_386.md). Low-power timer block diagram
1. Some I/Os may not be available, refer to Section 37.4.2: LPTIM pins and internal signals.
37.4.2 LPTIM pins and internal signals
The following tables provide the list of LPTIM pins and internal signals, respectively.
2. Wake-up supported from Stop  0, Stop 1 and Stop 2 modes.
3. Wake-up supported from Stop 0 and Stop 1 modes.
MSv47413V5
LPTIM
Kernel clock domain
IRQ
interface
LPTIM
register
interface
APB clock
domain
32-bit APB bus
Wake-up
APB clock
LPTIM
interrupt
clkmux
16-bit counter
Count mode
16-bit compare
Repetition
counter
1
01
1
0
LPTIM_OUT
lptim_out
Synchronzation
16-bit ARR LPTIM_RCR
Mux trigger
CNTSTRT/
SNGSTRT
Glitch
filter
LPTIM_IN1
Encoder
Up/down
LPTIM_IN2
lptim_in2
lptim_in1
Glitch
filter
LPTIM_ETR
lptim_ext_trigx
Edge
detector
Edge
detector
lptim_ker_ck
Glitch
filter
Prescaler clkpresc
[Table 296](../tables/table_296.md). LPTIM input/output pins
Pin name Pin type Description
LPTIM_IN1 Digital input LPTIM Input 1 from GPIO pin
LPTIM_IN2 Digital input LPTIM Input 2 from GPIO pin
LPTIM_ETR Digital input LPTIM external trigger GPIO pin
LPTIM_OUT Digital output LPTIM Output GPIO pin

Low-power timer (LPTIM) RM0438
1354/2187 RM0438 Rev 8
37.4.3 LPTIM input and trigger mapping
The LPTIM external trigger and input connections are detailed hereafter.
[Table 297](../tables/table_297.md). LPTIM internal signals
Signal name Signal type Description
lptim_pclk Digital inpu t LPTIM APB clock domain
lptim_ker_ck Digital inpu t LPTIM kernel clock
lptim_in1 Digital input Internal LPTIM input 1
lptim_in2 Digital input Internal LPTIM input 2 (1)
1. Only applies to LPTIM1
lptim_ext_trigx Digital input LPT IM external trigger input x
lptim_out Digital output LPTIM counter output
lptim_it Digital output LPTIM global interrupt
lptim_wake-up Digital output LPTIM wake-up event
[Table 298](../tables/table_298.md). LPTIM1 external trigger connections
TRIGSEL External trigger
lptim_ext_trig0 GPIO pin as LPTIM1_ETR alternate function
lptim_ext_trig1 RTC ALARM A
lptim_ext_trig2 RTC ALARM B
lptim_ext_trig3 TAMP1 input detection
lptim_ext_trig4 TAMP2 input detection
lptim_ext_trig5 TAMP3 input detection
lptim_ext_trig6 comp1_out
lptim_ext_trig7 comp2_out
[Table 299](../tables/table_299.md). LPTIM2 external trigger connections
TRIGSEL External trigger
lptim_ext_trig0 GPIO pin as LPTIM2_ETR alternate function
lptim_ext_trig1 RTC ALARM A
lptim_ext_trig2 RTC ALARM B
lptim_ext_trig3 TAMP1 input detection
lptim_ext_trig4 TAMP2 input detection
lptim_ext_trig5 TAMP3 input detection
lptim_ext_trig6 comp1_out
lptim_ext_trig7 comp2_out

RM0438 Rev 8 1355/2187
RM0438 Low-power timer (LPTIM)
1378
37.4.4 LPTIM reset and clocks
The LPTIM can be clocked using several clock sources. It can be clocked using an internal
clock signal which can be any configurable internal clock source selectable through the
RCC (see RCC section for more details). Also, the LPTIM can be clocked using an external
clock signal injected on its external Input1. When clocked with an external clock source, the
LPTIM can run in one of the following configurations:
• The first configuration is when the LPTIM is clocked by an external signal but in the
same time an internal clock signal is provided to the LPTIM from configurable internal
clock source (see RCC section).
• The second configuration is when the LPTIM is solely clocked by an external clock
source through its external Input1. This configuration is the one used to realize Timeout
function or pulse counter function when all the embedded oscillators are turned off after
entering a low-power mode.
Programming the CKSEL and COUNTMODE bits allows controlling whether the LPTIM
uses an external clock source or an internal one.
When configured to use an external clock source, the CKPOL bits are used to select the
external clock signal active edge. If both edges are configured to be active ones, an internal
clock signal must also be provided (first configuration). In this case, the internal clock signal
frequency must be at least four times higher than the external clock signal frequency.
37.4.5 Glitch filter
The LPTIM inputs, either external (mapped to GPIOs) or internal (mapped on the chip-level
to other embedded peripherals), are protected with digital filters that prevent any glitches
and noise perturbations to propagate inside the LPTIM. This is in order to prevent spurious
counts or triggers.
Before activating the digital filters, an internal clock source must first be provided to the
LPTIM. This is necessary to guarantee the proper operation of the filters.
The digital filters are divided into two groups:
• The first group of digital filters protects the LPTIM internal or external inputs. The digital
filters sensitivity is controlled by the CKFLT bits
• The second group of digital filters protects the LPTIM internal or external trigger inputs.
The digital filters sensitivity is controlled by the TRGFLT bits.
[Table 300](../tables/table_300.md). LPTIM3 external trigger connections
TRIGSEL External trigger
lptim_ext_trig0 GPIO pin as LPTIM3_ETR alternate function
lptim_ext_trig1 rtc alarm a
lptim_ext_trig2 rtc alarm b
lptim_ext_trig3 TAMP1 input detection
lptim_ext_trig4 TAMP2 input detection
lptim_ext_trig5 TAMP3 input detection
lptim_ext_trig6 comp1_out
lptim_ext_trig7 comp2_out

Low-power timer (LPTIM) RM0438
1356/2187 RM0438 Rev 8
Note: The digital filters sens itivity is controlled by groups. It is not possible to configure each digital
filter sensitivity separately inside the same group.
The filter sensitivity acts on the number of consecutive equal samples that is detected on
one of the LPTIM inputs to consider a signal level change as a valid transition. [Figure 387](../figures/figure_387.md)
shows an example of glitch filter behavior in case of a two consecutive samples
programmed.
[Figure 387](../figures/figure_387.md). Glitch filter timing diagram
Note: In case no internal clock signal is provided, the digital filter must be deactivated by setting
the CKFLT and TRGFLT bits to 0. In this case, an external analog filter can be used to
protect the LPTIM external inputs against glitches.
37.4.6 Prescaler
The LPTIM 16-bit counter is preceded by a configurable power-of-2 prescaler. The prescaler
division ratio is controlled by the PRESC[2:0] field. The table below lists all the possible
division ratios:
37.4.7 Trigger multiplexer
The LPTIM counter can be started either by software or after the detection of an active edge
on one of the eight trigger inputs.
MS32490V1
CLKMUX
Input
Filter out
2 consecutive samples 2 consecutive samples Filtered
[Table 301](../tables/table_301.md). Prescaler division ratios
Programming Dividing factor
000 /1
001 /2
010 /4
011 /8
100 /16
101 /32
110 /64
111 /128

RM0438 Rev 8 1357/2187
RM0438 Low-power timer (LPTIM)
1378
TRIGEN[1:0] is used to determine the LPTIM trigger source:
• When TRIGEN[1:0] equals 00, the LPTIM counter is started as soon as one of the
CNTSTRT or the SNGSTRT bits is set by software. The three remaining possible
values for the TRIGEN[1:0] are used to configure the active edge used by the trigger
inputs. The LPTIM counter starts as soon as an active edge is detected.
• When TRIGEN[1:0] is different than 00, TRIGSEL[2:0] is used to select which of the
eight trigger inputs is used to start the counter.
The external triggers are considered asynchronous signals for the LPTIM. After a trigger
detection, a two-counter-clock period latency is needed before the timer starts running due
to the synchronization.
If a new trigger event occurs when the timer is already started it is ignored (unless timeout
function is enabled).
Note: The timer must be enabled before settin g the SNGSTRT/CNTSTRT bits. Any write on these
bits when the timer is disabled is discarded by hardware.
Note: When starting the counter by software (TRIGEN[1:0] = 00), there is a delay of 3 kernel clock
cycles between the LPTIM_CR register update (set one of SNGSTRT or CNTSTRT bits)
and the effective start of the counter.
37.4.8 Operating mode
The LPTIM features two operating modes:
• Continuous mode: the timer is free running, the timer is started from a trigger event and
never stops until the timer is disabled
• One-shot mode: the timer is started from a trigger event and stops when an LPTIM
update event is generated.
One-shot mode
To enable the one-shot counting, the SNGSTRT bit must be set.
A new trigger event re-starts the timer. Any trigger event occurring after the counter starts
and before the next LPTIM update event, is discarded.
In case an external trigger is selected, each external trigger event arriving after the
SNGSTRT bit is set, and after the repetition counter has stopped (after the update event),
and if the repetition register content is different from zero, the repetition counter gets
reloaded with the value already contained by the repetition register and a new one-shot
counting cycle is started as shown in [Figure 388](../figures/figure_388.md).

Low-power timer (LPTIM) RM0438
1358/2187 RM0438 Rev 8
[Figure 388](../figures/figure_388.md). LPTIM output waveform, single-counting mode configuration
when repetition register content is different than zero (with PRELOAD = 1)
- Set-once mode activated:
Note that when the WAVE bitfield in the LPTIM_CFGR register is set, the Set-once mode is
activated. In this case, the counter is only started once following the first trigger, and any
subsequent trigger event is discarded as shown in [Figure 389](../figures/figure_389.md).
[Figure 389](../figures/figure_389.md). LPTIM output waveform, single-counting mode configuration
and Set-once mode activated (WAVE bit is set)
In case of software start (TRIGEN[1:0] = 00), the SNGSTRT setting starts the counter for
one-shot counting.
Continuous mode
To enable the continuous counting, the CNTSTRT bit must be set.
In case an external trigger is selected, an external trigger event arriving after CNTSTRT is
set, starts the counter for continuous counting. Any subsequent external trigger event is
discarded as shown in [Figure 390](../figures/figure_390.md).
In case of software start (TRIGEN[1:0] = 00), setting CNTSTRT starts the counter for
continuous counting.
MSv47414V1
LPTIM_RCR
Repetition counter
LPTIM_ARR
Compare
PWM
2 10 2
2
External trigger event
Ignored external trigger event
0
MSv39231V2
PWM
0
Compare
LPTIM_ARR
Discarded trigger
External trigger event

RM0438 Rev 8 1359/2187
RM0438 Low-power timer (LPTIM)
1378
[Figure 390](../figures/figure_390.md). LPTIM output waveform, Continuous counting mode configuration
SNGSTRT and CNTSTRT bits can only be set when the timer is enabled (ENABLE bit set to
1). It is possible to change “on the fly” from One-shot mode to Continuous mode.
If the Continuous mode was previously selected, setting SNGSTRT switches the LPTIM to
the One-shot mode. The counter (if active) stops as soon as an LPTIM update event is
generated.
If the One-shot mode was previously selected, setting CNTSTRT switches the LPTIM to the
Continuous mode. The counter (if active) restarts as soon as it reaches ARR.
37.4.9 Timeout function
The detection of an active edge on one selected trigger input can be used to reset the
LPTIM counter. This feature is controlled through the TIMOUT bit.
The first trigger event starts the timer, any successive trigger event resets the LPTIM
counter and the repetition counter and the timer restarts.
A low-power timeout function can be realized. The timeout value corresponds to the
compare value; if no trigger occurs within the expected time frame, the MCU is waked-up by
the compare match event.
37.4.10 Waveform generation
Two 16-bit registers, the LPTIM_ARR (autoreload register) and LPTIM_CMP (compare
register), are used to generate several different waveforms on LPTIM output
The timer can generate the following waveforms:
• The PWM mode: the LPTIM output is set as soon as the counter value in LPTIM_CNT
exceeds the compare value in LPTIM_CMP . The LPTIM output is reset as soon as a
match occurs between the LPTIM_ARR and the LPTIM_CNT registers.
• The One-pulse mode: the output waveform is similar to the one of the PWM mode for
the first pulse, then the output is permanently reset
• The Set-once mode: the output waveform is similar to the One-pulse mode except that
the output is kept to the last signal level (depends on the output configured polarity).
The above described modes require the LPTIM_ARR register value to be strictly greater
than the LPTIM_CMP register value.
MSv39229V2
PWM
0
Compare
LPTIM_ARR
Discarded triggers
External trigger event

Low-power timer (LPTIM) RM0438
1360/2187 RM0438 Rev 8
The LPTIM output waveform can be configured through the WAVE bit as follow:
• Resetting the WAVE bit to 0 forces the LPTIM to generate either a PWM waveform or a
One pulse waveform depending on which bit is set: CNTSTRT or SNGSTRT.
• Setting the WAVE bit to 1 forces the LPTIM to generate a Set-once mode waveform.
The WAVPOL bit controls the LPTIM output polarity. The change takes effect immediately,
so the output default value changes immediately after the polarity is re-configured, even
before the timer is enabled.
Signals with frequencies up to the LPTIM clock frequency divided by two can be generated.
[Figure 391](../figures/figure_391.md) below shows the three possible waveforms that can be generated on the LPTIM
output. Also, it shows the effect of the polarity change using the WAVPOL bit.
[Figure 391](../figures/figure_391.md). Waveform generation
37.4.11 Register update
The LPTIM_ARR register and LPTIM_CMP register are updated immediately after the APB
bus write operation or in synchronization with the next LPTIM update event if the timer is
already started.
The PRELOAD bit controls how the LPTIM_ARR and the LPTIM_CMP registers are
updated:
• When the PRELOAD bit is reset to 0, the LPTIM_ARR and the LPTIM_CMP registers
are immediately updated after any write access.
• When the PRELOAD bit is set to 1, the LPTIM_ARR and the LPTIM_CMP registers are
updated at next LPTIM update event, if the timer has been already started.
MS32467V2
LPTIM_ARR
Compare
0
PWM
One shot
Set once
PWM
One shot
Set once
Pol = 0
Pol = 1

RM0438 Rev 8 1361/2187
RM0438 Low-power timer (LPTIM)
1378
The LPTIM APB interface and the LPTIM kernel logic use different clocks, so there is some
latency between the APB write and the moment when these values are available to the
counter comparator. Within this latency period, any additional write into these registers must
be avoided.
The ARROK flag and the CMPOK flag in the LPTIM_ISR register indicate when the write
operation is completed to respectively the LPTIM_ARR register and the LPTIM_CMP
register.
After a write to the LPTIM_ARR register or the LPTIM_CMP register, a new write operation
to the same register can only be performed when the previous write operation is completed.
Any successive write before respectively the ARROK flag or the CMPOK flag be set, leads
to unpredictable results.
37.4.12 Counter mode
The LPTIM counter can be used to count external events on the LPTIM input1 or it can be
used to count internal clock cycles. The CKSEL and COUNTMODE bits control which
source is used for updating the counter.
In case the LPTIM is configured to count external events on Input1, the counter can be
updated following a rising edge, falling edge or both edges depending on the value written
to the CKPOL[1:0] bits.
The count modes below can be selected, depending on CKSEL and COUNTMODE values:
• CKSEL = 0: the LPTIM is clocked by an internal clock source
– COUNTMODE = 0
The LPTIM is configured to be clocked by an internal clock source and the LPTIM
counter is configured to be updated following each internal clock pulse.
– COUNTMODE = 1
The LPTIM external Input1 is sampled with the internal clock provided to the
LPTIM.
Consequently, in order not to miss any event, the frequency of the changes on the
external Input1 signal must never exceed the frequency of the internal clock
provided to the LPTIM. Also, the internal clock provided to the LPTIM must not be
prescaled (PRESC[2:0] = 000).
• CKSEL = 1: the LPTIM is clocked by an external clock source
COUNTMODE value is don’t care.
In this configuration, the LPTIM has no need for an internal clock source (except if the
glitch filters are enabled). The signal injected on the LPTIM external input1 is used as
system clock for the LPTIM. This configuration is suitable for operation modes where
no embedded oscillator is enabled.
For this configuration, the LPTIM counter can be updated either on rising edges or
falling edges of the input1 clock signal but not on both rising and falling edges.
Since the signal injected on the LPTIM external input1 is also used to clock the LPTIM
kernel logic, there is some initial latency (after the LPTIM is enabled) before the counter
is incremented. More precisely, the first five active edges on the LPTIM external Input1
(after LPTIM is enable) are lost.

Low-power timer (LPTIM) RM0438
1362/2187 RM0438 Rev 8
37.4.13 Timer enable
The ENABLE bit located in the LPTIM_CR register is used to enable/disable the LPTIM
kernel logic. After setting the ENABLE bit, a delay of two counter clock cycles is needed
before the LPTIM is actually enabled.
The LPTIM_CFGR and LPTIM_IER registers must be modified only when the LPTIM is
disabled.
37.4.14 Timer counter reset
In order to reset the content of LPTIM_CNT register, two reset mechanisms are
implemented:
• The synchronous reset mechanism: the synchronous reset is controlled by the
COUNTRST bit in the LPTIM_CR register. After setting the COUNTRST bitfield to '1',
the reset signal is propagated in the LPTIM kernel clock domain. So it is important to
note that a few clock pulses of the LPTIM kernel logic elapse before the reset is taken
into account. This makes the LPTIM counter count few extra pluses between the time
when the reset is triggered and it become effective. Since the COUNTRST bit is
located in the APB clock domain and the LPTIM counter is located in the LPTIM kernel
clock domain, a delay of 3 clock cycles of the kernel clock is needed to synchronize the
reset signal issued by the APB clock domain when writing '1' to the COUNTRST bit.
Note: The software should ensure that COUNRST bit is '0' before generating every synchronous
reset.
• The asynchronous reset mechanism: the asynchronous reset is controlled by the
RSTARE bit located in the LPTIM_CR register. When this bit is set to '1', any read
access to the LPTIM_CNT register resets its content to zero. Asynchronous reset must
be triggered within a timeframe in which no LPTIM core clock is provided. For example
when LPTIM Input1 is used as external clock source, the asynchronous reset must be
applied only when there is enough insurance that no toggle occurs on the LPTIM
Input1.
To read reliably the content of the LPTIM_CNT register two successive read accesses
must be performed and compared. A read access can be considered reliable when the
value of the two read accesses is equal. Unfortunately when asynchronous reset is
enabled there is no possibility to read twice the LPTIM_CNT register.
Warning: There is no mechanism inside the LPTIM that prevents the
two reset mechanisms from being used simultaneously. The
developer must make sure that these two mechanisms are
used exclusively.

RM0438 Rev 8 1363/2187
RM0438 Low-power timer (LPTIM)
1378
37.4.15 Encoder mode
This mode allows handling signals from quadrature encoders used to detect angular
position of rotary elements. Encoder interface mode acts simply as an external clock with
direction selection. This means that the counter just counts continuously between 0 and the
auto-reload value programmed into the LPTIM_ARR register (0 up to ARR or ARR down to
0 depending on the direction). Therefore LPTIM_ARR must be configured before starting
the counter. From the two external input signals, Input1 and Input2, a clock signal is
generated to clock the LPTIM counter. The phase between those two signals determines
the counting direction.
The Encoder mode is only available when the LPTIM is clocked by an internal clock source.
The signals frequency on both Input1 and Input2 inputs must not exceed the LPTIM internal
clock frequency divided by 4. This is mandatory in order to guarantee a proper operation of
the LPTIM.
Direction change is signalized by the two down and up flags in the LPTIM_ISR register. An
interrupt can be generated for both direction change events if enabled through the DOWNIE
bit.
To activate the Encoder mode the ENC bit has to be set to 1. The LPTIM must first be
configured in Continuous mode.
When Encoder mode is active, the LPTIM counter is modified automatically following the
speed and the direction of the incremental encoder. Therefore, its content always
represents the encoder’s position. The count direction, signaled by the Up and Down flags,
correspond to the rotation direction of the encoder rotor.
According to the edge sensitivity configured using the CKPOL[1:0] bits, different counting
scenarios are possible. The following table summarizes the possible combinations,
assuming that Input1 and Input2 do not switch at the same time.
The following figure shows a counting sequence for Encoder mode where both-edge
sensitivity is configured.
Caution: In this mode the LPTIM must be clocked by an internal clock source, so the CKSEL bit must
be maintained to its reset value which is equal to 0. Also, the prescaler division ratio must be
equal to its reset value which is 1 (PRESC[2:0] bits must be 000).
[Table 302](../tables/table_302.md). Encoder counting scenarios
Active edge
Level on opposite
signal (Input1 for
Input2, Input2 for
Input1)
Input1 signal Input2 signal
Rising Falling Rising Falling
Rising Edge
(Encoder sub-mode 1)
High Down No count Up No count
Low Up No count Down No count
Falling Edge
(Encoder sub-mode 2)
High No count Up No count Down
Low No count Down No count Up
Both Edges
(Encoder sub-mode 3)
High Down Up Up Down
Low Up Down Down Up

Low-power timer (LPTIM) RM0438
1364/2187 RM0438 Rev 8
[Figure 392](../figures/figure_392.md). Encoder mode counting sequence
37.4.16 Repetition counter
The LPTIM features a repetition counter that decrements by 1 each time an LPTIM counter
overflow event occurs. A repetition counter underflow event is generated when the repetition
counter contains zero and the LPTIM counter overflows. Next to each repetition counter
underflow event, the repetition counter gets loaded with the content of the REP[7:0] bitfield
which belongs to the repetition register LPTIM_RCR.
A repetition underflow event is generated on each and every LPTIM counter overflow when
the REP[7:0] register is set to 0.
When PRELOAD = 1, writing to the REP[7:0] bitfield has no effect on the content of the
repetition counter until the next repetition underflow event occurs. The repetition counter
continues to decrement each LPTIM counter overflow event and only when a repetition
underflow event is generated, the new value written into REP[7:0] is loaded into the
repetition counter. This behavior is depicted in [Figure 393](../figures/figure_393.md).
MS32491V1
T1
Counter
up updown
T2

RM0438 Rev 8 1365/2187
RM0438 Low-power timer (LPTIM)
1378
[Figure 393](../figures/figure_393.md). Continuous counting mode when repetition register LPTIM_RCR
different from zero (with PRELOAD = 1)
A repetition counter underflow event is systematically associated with LPTIM preloaded
registers update (refer to Section 37.4.11: Register update for more information).
Repetition counter underflow event is signaled to the software through the update event
(UE) flag mapped into the LPTIM_ISR register. When set, the UE flag can trigger an LPTIM
interrupt if its respective update event interrupt enable (UEIE) control bit, mapped to the
LPTIM_IER register, is set.
The repetition register LPTIM_RCR is located in the APB bus interface clock domain where
the repetition counter itself is located in the LPTIM kernel clock domain. Each time a new
value is written to the LPTIM_RCR register, this new content is propagated from the APB
bus interface clock domain to the LPTIM kernel clock domain. The new written value is then
loaded to the repetition counter immediately after a repetition counter underflow event. The
synchronization delay for the new written content is four APB clock cycles plus three LPTIM
kernel clock cycles and it is signaled by the REPOK flag located in the LPTIM_ISR register
when it is elapsed. When the LPTIM kernel clock cycle is relatively slow, for instance when
the LPTIM kernel is being clocked by the LSI clock source, it can be lengthy to keep polling
on the REPOK flag by software to detect that the synchronization of the LPTIM_RCR
register content is finished. For that reason, the REPOK flag, when set, can generate an
interrupt if its associated REPOKIE control bit in the LPTIM_IER register is set.
Note: After a write to the LPTIM_RCR register, a new write operation to the same register can only
be performed when the previous write operation is completed. Any successive writes before
the REPOK flag is set, lead to unpredictable results.
Caution: When using repetition counter with PRELOAD = 0, LPTIM_RCR register must be changed
at least five counter cycles before the autoreload match event, otherwise an unpredictable
behavior may occur.
37.4.17 Debug mode
When the microcontroller enters debug mode (core halted), the LPTIM counter either
continues to work normally or stops, depending on the timer dedicated bit configuration in
the debug support (DBG) peripheral.
MSv47415V1
LPTIM_RCR
Repetition counter
LPTIM_ARR
Compare
PWM
1 09
9
0
87
Repetition counter underflow event
Preloaded registers updated
4

Low-power timer (LPTIM) RM0438
1366/2187 RM0438 Rev 8
For further details, refer to section debug support (DBG).
37.5 LPTIM low-power modes
37.6 LPTIM interrupts
The following events generate an interrupt/wake-up event, if they are enabled through the
LPTIM_IER register:
• Compare match
• Auto-reload match (whatever the direction if Encoder mode)
• External trigger event
• Autoreload register write completed
• Compare register write completed
• Direction change (Encoder mode), programmable (up / down / both).
• Update Event
• Repetition register update OK
Note: If any bit in the LPTIM_IER register is set af ter that its corresponding flag in the LPTIM_ISR
register (status register) is set, the interrupt is not asserted.
[Table 303](../tables/table_303.md). Effect of low-power modes on the LPTIM
Mode Description
Sleep No effect. LPTIM interrupts cause the device to exit Sleep mode.
Stop
If the LPTIM is clocked by an oscillator available in Stop mode, LPTIM is functional
and the interrupts cause the device to exit the Stop mode (refer to Section 37.3: LPTIM
implementation).
Standby The LPTIM peripheral is powered down and must be reinitialized after exiting Standby
mode.
[Table 304](../tables/table_304.md). Interrupt events
Interrupt event Description
Compare match Interrupt flag is raised when the content of the Counter register
(LPTIM_CNT) matches the content of the compare register (LPTIM_CMP).
Auto-reload match
Interrupt flag is raised when the content of the Counter register
(LPTIM_CNT) matches the content of the Auto-reload register
(LPTIM_ARR).
External trigger event Interrupt flag is rais ed when an external trigger event is detected
Auto-reload register
update OK
Interrupt flag is raised when the write operation to the LPTIM_ARR register
is complete.
Compare register
update OK
Interrupt flag is raised when the write operation to the LPTIM_CMP register
is complete.

RM0438 Rev 8 1367/2187
RM0438 Low-power timer (LPTIM)
1378
37.7 LPTIM registers
Refer to Section 1.2: List of abbreviations for registers on page 77 for a list of abbreviations
used in register descriptions.
The peripheral registers can only be accessed by words (32-bit).
37.7.1 LPTIM interrupt and st atus register (LPTIM_ISR)
Address offset: 0x000
Reset value: 0x0000 0000
Direction change
Used in Encoder mode. Two interrupt flags are embedded to signal
direction change:
– UP flag signals up-counting direction change
– DOWN flag signals down-counting direction change.
Update Event Interrupt flag is raised when the repetition counter underflows (or contains
zero) and the LPTIM counter overflows.
Repetition register
update Ok
REPOK is set by hardware to inform application that the APB bus write
operation to the LPTIM_RCR register has been successfully completed.
[Table 304](../tables/table_304.md). Interrupt events (continued)
Interrupt event Description
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. REP
OK UE DOWN UP ARR
OK
CMP
OK
EXT
TRIG ARRM CMPM
rrrrrrrrr
Bits 31:9 Reserved, must be kept at reset value.
Bit 8 REPOK: Repetition register update Ok
REPOK is set by hardware to inform application that the APB bus write operation to the LPTIM_RCR
register has been successfully completed. REPOK flag can be cleared by writing 1 to the REPOKCF
bit in the LPTIM_ICR register.
Bit 7 UE: LPTIM update event occurred
UE is set by hardware to inform application that an update event was generated. UE flag can be
cleared by writing 1 to the UECF bit in the LPTIM_ICR register.
Bit 6 DOWN: Counter direction change up to down
In Encoder mode, DOWN bit is set by hardware to inform application that the counter direction has
changed from up to down. DOWN flag can be cleared by writing 1 to the DOWNCF bit in the
LPTIM_ICR register.
Note: If the LPTIM does not support Encoder mode  feature, this bit is reserved. Refer to Section 37.3:
LPTIM implementation.

Low-power timer (LPTIM) RM0438
1368/2187 RM0438 Rev 8
37.7.2 LPTIM interrupt clear  register (LPTIM_ICR)
Address offset: 0x004
Reset value: 0x0000 0000
Bit 5 UP: Counter direction change down to up
In Encoder mode, UP bit is set by hardware to inform application that the counter direction has
changed from down to up. UP flag can be cleared by writing 1 to the UPCF bit in the LPTIM_ICR
register.
Note: If the LPTIM does not support Encoder mode  feature, this bit is reserved. Refer to Section 37.3:
LPTIM implementation.
Bit 4 ARROK: Autoreload register update OK
ARROK is set by hardware to inform application that the APB bus write operation to the LPTIM_ARR
register has been successfully completed. ARROK flag can be cleared by writing 1 to the ARROKCF
bit in the LPTIM_ICR register.
Bit 3 CMPOK: Compare register update OK
CMPOK is set by hardware to inform application that the APB bus write operation to the
LPTIM_CMP register has been successfully completed.
Bit 2 EXTTRIG: External trigger edge event
EXTTRIG is set by hardware to inform application that a valid edge on the selected external trigger
input has occurred. If the trigger is ignored because the timer has already started, then this flag is
not set. EXTTRIG flag can be cleared by writing 1 to the EXTTRIGCF bit in the LPTIM_ICR register.
Bit 1 ARRM: Autoreload match
ARRM is set by hardware to inform application that LPTIM_CNT register’s value reached the
LPTIM_ARR register’s value. ARRM flag can be cleared by writing 1 to the ARRMCF bit in the
LPTIM_ICR register.
Bit 0 CMPM: Compare match
The CMPM bit is set by hardware to inform application that LPTIM_CNT register value reached the
LPTIM_CMP register’s value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. REPOK
CF UECF DOWN
CF UPCF ARRO
KCF
CMPO
KCF
EXTTR
IGCF
ARRM
CF
CMPM
CF
wwwwwwwww
Bits 31:9 Reserved, must be kept at reset value.
Bit 8 REPOKCF: Repetition register update OK clear flag
Writing 1 to this bit clears the REPOK flag in the LPTIM_ISR register.
Bit 7 UECF: Update event clear flag
Writing 1 to this bit clear the UE flag in the LPTIM_ISR register.
Bit 6 DOWNCF: Direction change to down clear flag
Writing 1 to this bit clear the DOWN flag in the LPTIM_ISR register.
Note: If the LPTIM does not support Encoder mode feature, this bit is reserved. Refer to Section 37.3.

RM0438 Rev 8 1369/2187
RM0438 Low-power timer (LPTIM)
1378
37.7.3 LPTIM interrupt enab le register (LPTIM_IER)
Address offset: 0x008
Reset value: 0x0000 0000
Bit 5 UPCF: Direction change to UP clear flag
Writing 1 to this bit clear the UP flag in the LPTIM_ISR register.
Note: If the LPTIM does not support Encoder mode feature, this bit is reserved. Refer to Section 37.3.
Bit 4 ARROKCF: Autoreload register update OK clear flag
Writing 1 to this bit clears the ARROK flag in the LPTIM_ISR register
Bit 3 CMPOKCF: Compare register update OK clear flag
Writing 1 to this bit clears the CMPOK flag in the LPTIM_ISR register
Bit 2 EXTTRIGCF: External trigger valid edge clear flag
Writing 1 to this bit clears the EXTTRIG flag in the LPTIM_ISR register
Bit 1 ARRMCF: Autoreload match clear flag
Writing 1 to this bit clears the ARRM flag in the LPTIM_ISR register
Bit 0 CMPMCF: Compare match clear flag
Writing 1 to this bit clears the CMP flag in the LPTIM_ISR register
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. REPOK
IE UEIE DOWNI
E UPIE ARRO
KIE
CMPO
KIE
EXT
TRIGIE
ARRM
IE
CMPM
IE
rw rw rw rw rw rw rw rw rw
Bits 31:9 Reserved, must be kept at reset value.
Bit 8 REPOKIE: Repetition register update OK interrupt Enable
0: Repetition register update OK interrupt disabled
1: Repetition register update OK interrupt enabled
Bit 7 UEIE: Update event interrupt enable
0: Update event interrupt disabled
1: Update event interrupt enabled
Bit 6 DOWNIE: Direction change to down Interrupt Enable
0: DOWN interrupt disabled
1: DOWN interrupt enabled
Note: If the LPTIM does not support Encoder mode feature, this bit is reserved. Refer to Section 37.3.
Bit 5 UPIE: Direction change to UP Interrupt Enable
0: UP interrupt disabled
1: UP interrupt enabled
Note: If the LPTIM does not support Encoder mode feature, this bit is reserved. Refer to Section 37.3.
Bit 4 ARROKIE: Autoreload register update OK Interrupt Enable
0: ARROK interrupt disabled
1: ARROK interrupt enabled

Low-power timer (LPTIM) RM0438
1370/2187 RM0438 Rev 8
Caution: The LPTIM_IER register must only be modified when the LPTIM is disabled (ENABLE bit reset to 0)
37.7.4 LPTIM configuration register (LPTIM_CFGR)
Address offset: 0x00C
Reset value: 0x0000 0000
Bit 3 CMPOKIE: Compare register update OK Interrupt Enable
0: CMPOK interrupt disabled
1: CMPOK interrupt enabled
Bit 2 EXTTRIGIE: External trigger valid edge Interrupt Enable
0: EXTTRIG interrupt disabled
1: EXTTRIG interrupt enabled
Bit 1 ARRMIE: Autoreload match Interrupt Enable
0: ARRM interrupt disabled
1: ARRM interrupt enabled
Bit 0 CMPMIE: Compare match Interrupt Enable
0: CMPM interrupt disabled
1: CMPM interrupt enabled
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. ENC COUNT
MODE
PRE
LOAD
WAV
POL WAVE TIMOUT TRIGEN[1:0] Res.
rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
TRIGSEL[2:0] Res. PRESC[2:0] Res. TRGFLT[1:0] Res. CKFLT[1:0] CKPOL[1:0] CKSEL
rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:30 Reserved, must be kept at reset value.
Bit 29 Reserved, must be  kept at reset value.
Bits 28:25 Reserved, must be kept at reset value.
Bit 24 ENC: Encoder mode enable
The ENC bit controls the Encoder mode
0: Encoder mode disabled
1: Encoder mode enabled
Note: If the LPTIM does not support Encoder mode feature, this bit is reserved. Refer to
Section 37.3.
Bit 23 COUNTMODE: counter mode enabled
The COUNTMODE bit selects which clock source is used by the LPTIM to clock the counter:
0: The counter is incremented following each internal clock pulse
1: The counter is incremented following each valid clock pulse on the LPTIM external Input1
Bit 22 PRELOAD: Registers update mode
The PRELOAD bit controls the LPTIM_ARR, LPTIM_RCR and the LPTIM_CMP registers update
modality
0: Registers are updated after each APB bus write access
1: Registers are updated at the end of the current LPTIM period

RM0438 Rev 8 1371/2187
RM0438 Low-power timer (LPTIM)
1378
Bit 21 WAVPOL: Waveform shape polarity
The WAVPOL bit controls the output polarity
0: The LPTIM output reflects the compare results between LPTIM_CNT and LPTIM_CCRx registers
1: The LPTIM output reflects the inverse of the compare results between LPTIM_CNT and
LPTIM_CCRx registers
Bit 20 WAVE: Waveform shape
The WAVE bit controls the output shape
0: Deactivate Set-once mode
1: Activate the Set-once mode
Bit 19 TIMOUT: Timeout enable
The TIMOUT bit controls the Timeout feature
0: A trigger event arriving when the timer is already started is ignored
1: A trigger event arriving when the timer is already started resets and restarts the LPTIM counter
and the repetition counter
Bits 18:17 TRIGEN[1:0]: Trigger enable and polarity
The TRIGEN bits controls whether the LPTIM counter is started by an external trigger or not. If the
external trigger option is selected, three configurations are possible for the trigger active edge:
00: Software trigger (counting st art is initiated by software)
01: Rising edge is the active edge
10: Falling edge is the active edge
11: Both edges are active edges
Bit 16 Reserved, must be  kept at reset value.
Bits 15:13 TRIGSEL[2:0]: Trigger selector
The TRIGSEL bits select the trigger source that serves as a trigger event for the LPTIM among the
below 8 available sources:
000: lptim_ext_trig0
001: lptim_ext_trig1
010: lptim_ext_trig2
011: lptim_ext_trig3
100: lptim_ext_trig4
101: lptim_ext_trig5
110: lptim_ext_trig6
111: lptim_ext_trig7
See Section 37.4.3: LPTIM input and trigger mapping for details.
Bit 12 Reserved, must be  kept at reset value.
Bits 11:9 PRESC[2:0]: Clock prescaler
The PRESC bits configure the prescaler division factor. It can be one among the following division
factors:
000: /1
001: /2
010: /4
011: /8
100: /16
101: /32
110: /64
111: /128
Bit 8 Reserved, must be kept at reset value.

Low-power timer (LPTIM) RM0438
1372/2187 RM0438 Rev 8
Caution: The LPTIM_CFGR register must only be modified when the LPTIM is disabled (ENABLE bit
reset to 0).
Bits 7:6 TRGFLT[1:0]: Configurable digital filter for trigger
The TRGFLT value sets the number of consecutive equal samples that are detected when a level
change occurs on an internal trigger before it is considered as a valid level transition. An internal
clock source must be present to use this feature
00: Any trigger active level change is considered as a valid trigger
01: Trigger active level change must be stable for at least 2 clock periods before it is considered as
valid trigger.
10: Trigger active level change must be stable for at least 4 clock periods before it is considered as
valid trigger.
11: Trigger active level change must be stable for at least 8 clock periods before it is considered as
valid trigger.
Bit 5 Reserved, must be kept at reset value.
Bits 4:3 CKFLT[1:0]: Configurable digital filter for external clock
The CKFLT value sets the number of consecutive equal samples that are detected when a level
change occurs on an external clock signal before it is considered as a valid level transition. An
internal clock source must be present to use this feature
00: Any external clock signal level change is considered as a valid transition
01: External clock signal level change must be stable for at least 2 clock periods before it is
considered as valid transition.
10: External clock signal level change must be stable for at least 4 clock periods before it is
considered as valid transition.
11: External clock signal level change must be stable for at least 8 clock periods before it is
considered as valid transition.
Bits 2:1 CKPOL[1:0]: Clock polarity
When the LPTIM is clocked by an external clock source, CKPOL bits is used to configure the active
edge or edges used by the counter:
00: The rising edge is the active edge used for counting.
If the LPTIM is configured in Encoder mode (ENC bit is set), the Encoder sub-mode 1 is active.
01: The falling edge is the active edge used for counting.
If the LPTIM is configured in Encoder mode (ENC bit is set), the Encoder sub-mode 2 is active.
10: Both edges are active edges. When both external clock signal edges are considered active
ones, the LPTIM must also be clocked by an internal clock source with a frequency equal to at
least four times the external clock frequency.
If the LPTIM is configured in Encoder mode (ENC bit is set), the Encoder sub-mode 3 is active.
11: Not allowed
Refer to Section 37.4.15: Encoder mode for more details about Encoder sub-modes.
Bit 0 CKSEL: Clock selector
The CKSEL bit selects which clock source the LPTIM uses:
0: LPTIM is clocked by internal clock source (APB clock or any of the embedded oscillators)
1: LPTIM is clocked by an external clock source through the LPTIM external Input1

RM0438 Rev 8 1373/2187
RM0438 Low-power timer (LPTIM)
1378
37.7.5 LPTIM control register (LPTIM_CR)
Address offset: 0x010
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. RST
ARE
COUN
TRST
CNT
STRT
SNG
STRT
ENA
BLE
rw rs rw rw rw
Bits 31:5 Reserved, must be kept at reset value.
Bit 4 RSTARE: Reset after read enable
This bit is set and cleared by software. When RSTARE is set to '1', any read access to LPTIM_CNT
register asynchronously resets LPTIM_CNT register content.
This bit can be set only when the LPTIM is enabled.
Bit 3 COUNTRST: Counter reset
This bit is set by software and cleared by hardware. When set to '1' this bit triggers a synchronous
reset of the LPTIM_CNT counter register. Due to the synchronous nature of this reset, it only takes
place after a synchronization delay of 3 LPTimer core clock cycles (LPTimer core clock can be
different from APB clock).
This bit can be set only when the LPTIM is enabled. It is automatically reset by hardware.
Caution: COUNTRST must never be set to '1' by software before it is already cleared to '0' by
hardware. Software must consequently check that COUNTRST bit is already cleared to '0'
before attempting to set it to '1'.
Bit 2 CNTSTRT: Timer start in Continuous mode
This bit is set by software and cleared by hardware.
In case of software start (TRIGEN[1:0] = 00), setting this bit starts the LPTIM in Continuous mode.
If the software start is disabled (TRIGEN[1:0] different than 00), setting this bit starts the timer in
Continuous mode as soon as an external trigger is detected.
If this bit is set when a single pulse mode counting is ongoing, then the timer does not stop at the
next match between the LPTIM_ARR and LPTIM_CNT registers and the LPTIM counter keeps
counting in Continuous mode.
This bit can be set only when the LPTIM is enabled. It is automatically reset by hardware.
Bit 1 SNGSTRT: LPTIM start in Single mode
This bit is set by software and cleared by hardware.
In case of software start (TRIGEN[1:0] = 00), setting this bit starts the LPTIM in single pulse mode.
If the software start is disabled (TRIGEN[1:0] different than 00), setting this bit starts the LPTIM in
single pulse mode as soon as an external trigger is detected.
If this bit is set when the LPTIM is in continuous counting mode, then the LPTIM stops at the
following match between LPTIM_ARR and LPTIM_CNT registers.
This bit can only be set when the LPTIM is enabled. It is automatically reset by hardware.
Bit 0 ENABLE: LPTIM enable
The ENABLE bit is set and cleared by software.
0: LPTIM is disabled.
1: LPTIM is enabled

Low-power timer (LPTIM) RM0438
1374/2187 RM0438 Rev 8
37.7.6 LPTIM compare register (LPTIM_CMP)
Address offset: 0x014
Reset value: 0x0000 0000
Caution: The LPTIM_CMP register must only be modified when the LPTIM is enabled (ENABLE bit
set to 1).
37.7.7 LPTIM autoreload register (LPTIM_ARR)
Address offset: 0x018
Reset value: 0x0000 0001
Caution: The LPTIM_ARR register must only be modified when the LPTIM is enabled (ENABLE bit
set to 1).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CMP[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 CMP[15:0]: Compare value
CMP is the compare value used by the LPTIM.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ARR[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 ARR[15:0]: Auto reload value
ARR is the autoreload value for the LPTIM.
This value must be strictly greater than the CMP[15:0] value.

RM0438 Rev 8 1375/2187
RM0438 Low-power timer (LPTIM)
1378
37.7.8 LPTIM counter re gister (LPTIM_CNT)
Address offset: 0x01C
Reset value: 0x0000 0000
37.7.9 LPTIM1 option re gister (LPTIM1_OR)
Address offset: 0x020
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CNT[15:0]
rrrrrrrrrrrrrrrr
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 CNT[15:0]: Counter value
When the LPTIM is running, reading the LPTIM_CNT register may return unreliable values. In this
case it is necessary to perform consecutive reads until two returned values are identical.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. OR_1 OR_0
rw rw
Bits 31:2 Reserved, must be kept at reset value.
Bit 1 OR_1: Option register bit 1
0: LPTIM1 input 2 is connected to I/O
1: LPTIM1 input 2 is connected to COMP2_OUT
Bit 0 OR_0: Option register bit 0
0: LPTIM1 input 1 is connected to I/O
1: LPTIM1 input 1 is connected to COMP1_OUT

Low-power timer (LPTIM) RM0438
1376/2187 RM0438 Rev 8
37.7.10 LPTIM2 option register (LPTIM2_OR)
Address offset: 0x020
Reset value: 0x0000 0000
37.7.11 LPTIM3 option register (LPTIM3_OR)
Address offset: 0x020
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. OR_1 OR_0
rw rw
Bits 31:2 Reserved, must be kept at reset value.
Bits 1:0 OR_[1:0]:
00: Input 1 is connected to I/O
01: Input 1 is connected to COMP1_OUT
10: Input 1 is connected to COMP2_OUT
11: Input 1 is connected to COMP1_OUT OR COMP2_OUT
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. OR_1 OR_0
rw rw
Bits 31:2 Reserved, must be kept at reset value.
Bits 1:0 OR_[1:0]:
00: Input 1 is connected to I/O
01: Input 1 is connected to COMP1_OUT
10: Input 1 is connected to COMP2_OUT
11: Input 1 is connected to COMP1_OUT OR COMP2_OUT

RM0438 Rev 8 1377/2187
RM0438 Low-power timer (LPTIM)
1378
37.7.12 LPTIM repetition  register (LPTIM_RCR)
Address offset: 0x028
Reset value: 0x0000 0000
Caution: The LPTIM_RCR register must only be modified when the LPTIM is enabled (ENABLE bit
set to 1). When using repetition counter with PRELOAD = 0, LPTIM_RCR register must be
changed at least five counter cycles before the auto reload match event, otherwise an
unpredictable behavior may occur.
37.7.13 LPTIM register map
The following table summarizes the LPTIM registers.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. REP[7:0]
rw rw rw rw rw rw rw rw
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 REP[7:0]: Repetition register value
REP is the repetition value for the LPTIM.
[Table 305](../tables/table_305.md). LPTIM register map and reset values
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
0x000
LPTIM_ISR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
REPOK
UE
DOWN(1)
UP(1)
ARROK
CMPOK
EXTTRIG
ARRM
CMPM
Reset value 000000000
0x004
LPTIM_ICR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
REPOKCF
UECF
DOWNCF(1)
UPCF(1)
ARROKCF
CMPOKCF
EXTTRIGCF
ARRMCF
CMPMCF
Reset value 000000000
0x008
LPTIM_IER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
REPOKIE
UEIE
DOWNIE(1)
UPIE(1)
ARROKIE
CMPOKIE
EXTTRIGIE
ARRMIE
CMPMIE
Reset value 000000000
0x00C
LPTIM_CFGR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ENC(1)
COUNTMODE
PRELOAD
WAVPOL
WAVE
TIMOUT
TRIGEN
Res.
TRIGSEL[2:0]
Res.
PRESC
Res.
TRGFLT
Res.
CKFLT
CKPOL
CKSEL
Reset value 00000000 000 000 00 00000
0x010
LPTIM_CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
RSTARE
COUNTRST
CNTSTRT
SNGSTRT
ENABLE
Reset value 00000

Low-power timer (LPTIM) RM0438
1378/2187 RM0438 Rev 8
Refer to Section 2.3: Memory organization for the register boundary addresses.
0x014
LPTIM_CMP
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CMP[15:0]
Reset value 0000000000000000
0x018
LPTIM_ARR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ARR[15:0]
Reset value 0000000000000001
0x01C
LPTIM_CNT
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CNT[15:0]
Reset value 0000000000000000
0x020
LPTIM1_OR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OR_1
OR_0
Reset value 00
0x020
LPTIM2_OR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OR_1
OR_0
Reset value 00
0x020
LPTIM3_OR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OR_1
OR_0
Reset value 00
0x028
LPTIM_RCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
REP[7:0]
Reset value 00000000
1. If LPTIM does not support Encoder mode feature, this bit is reserved. Refer to Section 37.3: LPTIM implementation.
[Table 305](../tables/table_305.md). LPTIM register map and reset values (continued)
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
* [Figure 386: Architectural Diagram](../figures/figure_386.md)
* [Figure 387: Architectural Diagram](../figures/figure_387.md)
* [Figure 388: Architectural Diagram](../figures/figure_388.md)
* [Figure 389: Architectural Diagram](../figures/figure_389.md)
* [Figure 390: Architectural Diagram](../figures/figure_390.md)
* [Figure 391: Architectural Diagram](../figures/figure_391.md)
* [Figure 392: Architectural Diagram](../figures/figure_392.md)
* [Figure 393: Architectural Diagram](../figures/figure_393.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 295: Configuration Matrix](../tables/table_295.md)
* [Table 296: Configuration Matrix](../tables/table_296.md)
* [Table 297: Configuration Matrix](../tables/table_297.md)
* [Table 298: Configuration Matrix](../tables/table_298.md)
* [Table 299: Configuration Matrix](../tables/table_299.md)
* [Table 300: Configuration Matrix](../tables/table_300.md)
* [Table 301: Configuration Matrix](../tables/table_301.md)
* [Table 302: Configuration Matrix](../tables/table_302.md)
* [Table 303: Configuration Matrix](../tables/table_303.md)
* [Table 304: Configuration Matrix](../tables/table_304.md)
* [Table 305: Configuration Matrix](../tables/table_305.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)