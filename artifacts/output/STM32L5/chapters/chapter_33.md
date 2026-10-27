# Chapter 33: Advanced-control timers (TIM1/TIM8)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 33: Advanced-control timers (TIM1/TIM8).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 1072 - 1176
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Timers (TIM)](../peripherals/timers.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
Advanced-control timers (TIM1/TIM8) RM0438
1072/2187 RM0438 Rev 8
33 Advanced-control timers (TIM1/TIM8)
33.1 TIM1/TIM8 introduction
The advanced-control timers (TIM1/TIM8) consist of a 16-bit auto-reload counter driven by a
programmable prescaler.
It may be used for a variety of purposes, including measuring the pulse lengths of input
signals (input capture) or generating output waveforms (output compare, PWM,
complementary PWM with dead-time insertion).
Pulse lengths and waveform periods can be modulated from a few microseconds to several
milliseconds using the timer prescaler and the RCC clock controller prescalers.
The advanced-control (TIM1/TIM8) and general-purpose (TIMy) timers are completely
independent, and do not share any resources. They can be synchronized together as
described in Section 33.3.26: Timer synchronization.
33.2 TIM1/TIM8 main features
TIM1/TIM8 timer features include:
• 16-bit up, down, up/down auto-reload counter.
• 16-bit programmable prescaler allowing dividing (also “on the fly”) the counter clock
frequency either by any factor between 1 and 65536.
• Up to 6 independent channels for:
– Input Capture (but channels 5 and 6)
– Output Compare
– PWM generation (Edge and Center-aligned Mode)
– One-pulse mode output
• Complementary outputs with programmable dead-time
• Synchronization circuit to control the timer with external signals and to interconnect
several timers together.
• Repetition counter to update the timer registers only after a given number of cycles of
the counter.
• 2 break inputs to put the timer’s output signals in a safe user selectable configuration.
• Interrupt/DMA generation on the following events:
– Update: counter overflow /underflow, counter initialization (by software or
internal/external trigger)
– Trigger event (counter start, stop, initialization or count by internal/external trigger)
– Input capture
– Output compare
• Supports incremental (quadrature) encoder and Hall-sensor circuitry for positioning
purposes
• Trigger input for external clock or cycle-by-cycle current management

RM0438 Rev 8 1073/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
[Figure 230](../figures/figure_230.md). Advanced-control timer block diagram
1. See [Figure 274](../figures/figure_274.md): Break and Break2 circuitry overview for details
U
U
U
CC1I
CC2I
Trigger
controller
+/-
Stop, clear or up/down
TI1FP1
TI2FP2
ITR0
ITR1
ITR2 TRGI
Output
controlDTG
TRGO
OC1REF
OC2REF
REP register
URepetition
counter
UI
Reset, enable, up/down, count
CK_PSC
IC1
IC2 IC2PS
IC1PS
TI1FP1
TRG
TRC
TRC
ITR
TRC
TI1F_ED
CC1I
CC2I
TI1FP2
TI2FP1
TI2FP2
TI1
TI2
TIMx_CH1
TIMx_CH2
OC1
TIMx_CH1
TIMx_CH1N
OC1N
to other timersto DAC/ADC
Slave
controller
mode
PSC
prescaler CNT counter
Internal clock (CK_INT)
CK_CNT
CK_TIM18 from RCC
ITR3
MSv62399V1
XOR
DTG registers
Input filter &
edge detector
Capture/Compare 1 register
Notes:
Reg Preload registers transferred
to active registers on U event
according to control bit
Event
Interrupt & DMA output
TIMx_BKIN
Internal sources
Auto-reload register
Capture/Compare 2 registerPrescaler
Prescaler
Output
control
Encoder
Interface
Polarity selection &
edgedetector & prescaler
Input
filter
ETRF
ETRP
ETRTIMx_ETR
U
U
CC3I
CC4I
Output
controlDTG
OC3REF
OC4REF
IC3
IC4 IC4PS
IC3PS
TI3FP3
TRC
TRC
CC3I
CC4I
TI3FP4
TI4FP3
TI4FP4
OC3
OC4
TIMx_CH3
TIMx_CH4
TIMx_CH3N
OC3N
Capture/Compare 3 register
Capture/Compare 4 registerPrescaler
Prescaler
Output
control
DTG
OC2
TIMx_CH2
TIMx_CH2N
OC2N
TI3
TI4
TIMx_CH3
TIMx_CH4
OC5REF OC5
Capture/Compare 5 register Output
control
OC6REF OC6
Capture/Compare 6 register Output
control
Break and Break2 circuitry (1)
TIMx_BKIN2
ETRF
Input filter &
edge detector
Input filter &
edge detector
Input filter &
edge detector
SBIF
BIF
B2IF
BRK request
BRK2 request

Advanced-control timers (TIM1/TIM8) RM0438
1074/2187 RM0438 Rev 8
33.3 TIM1/TIM8 functional description
33.3.1 Time-base unit
The main block of the programmable advanced-control timer is a 16-bit counter with its
related auto-reload register. The counter can count up, down or both up and down. The
counter clock can be divided by a prescaler.
The counter, the auto-reload register and the prescaler register can be written or read by
software. This is true even when the counter is running.
The time-base unit includes:
• Counter register (TIMx_CNT)
• Prescaler register (TIMx_PSC)
• Auto-reload register (TIMx_ARR)
• Repetition counter register (TIMx_RCR)
The auto-reload register is preloaded. Writing to or reading from the auto-reload register
accesses the preload register. The content of the preload register are transferred into the
shadow register permanently or at each update event (UEV), depending on the auto-reload
preload enable bit (ARPE) in TIMx_CR1 register. The update event is sent when the counter
reaches the overflow (or underflow when downcounting) and if the UDIS bit equals 0 in the
TIMx_CR1 register. It can also be generated by software. The generation of the update
event is described in detailed for each configuration.
The counter is clocked by the prescaler output CK_CNT, which is enabled only when the
counter enable bit (CEN) in TIMx_CR1 register is set (refer also to the slave mode controller
description to get more details on counter enabling).
Note that the counter starts counting 1 clock cycle after setting the CEN bit in the TIMx_CR1
register.
Prescaler description
The prescaler can divide the counter clock frequency by any factor between 1 and 65536. It
is based on a 16-bit counter controlled through a 16-bit register (in the TIMx_PSC register).
It can be changed on the fly as this control register is buffered. The new prescaler ratio is
taken into account at the next update event.
[Figure 231](../figures/figure_231.md) and [Figure 232](../figures/figure_232.md) give some examples of the counter behavior when the prescaler
ratio is changed on the fly:

RM0438 Rev 8 1075/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
[Figure 231](../figures/figure_231.md). Counter timing diagram with prescaler division change from 1 to 2
[Figure 232](../figures/figure_232.md). Counter timing diagram with prescaler division change from 1 to 4
CK_PSC
00
CEN
Timerclock = CK_CNT
Counter register
Update event (UEV)
0
Prescaler control register 10
Write a new value in TIMx_PSC
Prescaler buffer 10
Prescaler counter 0 10 10 1 0 1
01 02 03FA FBF7 F8 F9 FC
MS31076V2
0
30
0 12 301 2 3
MS31077V2
CK_PSC
CEN
Timerclock = CK_CNT
Counter register
Update event (UEV)
Prescaler control register
Write a new value in TIMx_PSC
Prescaler buffer
Prescaler counter
00 01FA FBF7 F8 F9 FC
30

Advanced-control timers (TIM1/TIM8) RM0438
1076/2187 RM0438 Rev 8
33.3.2 Counter modes
Upcounting mode
In upcounting mode, the counter counts from 0 to the auto-reload value (content of the
TIMx_ARR register), then restarts from 0 and generates a counter overflow event.
If the repetition counter is used, the update event (UEV) is generated after upcounting is
repeated for the number of times programmed in the repetition counter register
(TIMx_RCR) + 1. Else the update event is generated at each counter overflow.
Setting the UG bit in the TIMx_EGR register (by software or by using the slave mode
controller) also generates an update event.
The UEV event can be disabled by software by setting the UDIS bit in the TIMx_CR1
register. This is to avoid updating the shadow registers while writing new values in the
preload registers. Then no update event occurs until the UDIS bit has been written to 0.
However, the counter restarts from 0, as well as the counter of the prescaler (but the
prescale rate does not change). In addition, if the URS bit (update request selection) in
TIMx_CR1 register is set, setting the UG bit generates an update event UEV but without
setting the UIF flag (thus no interrupt or DMA request is sent). This is to avoid generating
both update and capture interrupts when clearing the counter on the capture event.
When an update event occurs, all the registers are updated and the update flag (UIF bit in
TIMx_SR register) is set (depending on the URS bit):
• The repetition counter is reloaded with the content of TIMx_RCR register,
• The auto-reload shadow register is updated with the preload value (TIMx_ARR),
• The buffer of the prescaler is reloaded with the preload value (content of the TIMx_PSC
register).
The following figures show some examples of the counter behavior for different clock
frequencies when TIMx_ARR=0x36.

RM0438 Rev 8 1077/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
[Figure 233](../figures/figure_233.md). Counter timing diagram, internal clock divided by 1
[Figure 234](../figures/figure_234.md). Counter timing diagram, internal clock divided by 2
00 02 03 04 05 06 0732 33 34 35 3631
MS31078V2
CK_PSC
CNT_EN
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag
(UIF)
01
MS31079V2
CK_PSC
CNT_EN
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag
(UIF)
0034 0035 0036 0000 0001 0002 0003

Advanced-control timers (TIM1/TIM8) RM0438
1078/2187 RM0438 Rev 8
[Figure 235](../figures/figure_235.md). Counter timing diagram, internal clock divided by 4
[Figure 236](../figures/figure_236.md). Counter timing diagram, internal clock divided by N
0000 00010035 0036
MS31080V2
CK_PSC
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag
(UIF)
CNT_EN
001F 20
MS31081V2
CK_PSC
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag
(UIF)

RM0438 Rev 8 1079/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
[Figure 237](../figures/figure_237.md). Counter timing diagram, update event when ARPE=0 (TIMx_ARR not
preloaded)
[Figure 238](../figures/figure_238.md). Counter timing diagram, update event when ARPE=1 (TIMx_ARR
preloaded)
FF 36
MS31082V3
CK_PSC
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag (UIF)
00 02 03 04 05 06 0732 33 34 35 3631 01
CEN
Auto-reload preload register
Write a new value in TIMx_ARR
MS31083V2
F5 36
CK_PSC
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag
(UIF)
00 02 03 04 05 06 07F1 F2 F3 F4 F5F0 01
CEN
Auto-reload preload
register
Write a new value in TIMx_ARR
Auto-reload shadow
register F5 36

Advanced-control timers (TIM1/TIM8) RM0438
1080/2187 RM0438 Rev 8
Downcounting mode
In downcounting mode, the counter counts from the auto-reload value (content of the
TIMx_ARR register) down to 0, then restarts from the auto-reload value and generates a
counter underflow event.
If the repetition counter is used, the update event (UEV) is generated after downcounting is
repeated for the number of times programmed in the repetition counter register
(TIMx_RCR) + 1. Else the update event is generated at each counter underflow.
Setting the UG bit in the TIMx_EGR register (by software or by using the slave mode
controller) also generates an update event.
The UEV update event can be disabled by software by setting the UDIS bit in TIMx_CR1
register. This is to avoid updating the shadow registers while writing new values in the
preload registers. Then no update event occurs until UDIS bit has been written to 0.
However, the counter restarts from the current auto-reload value, whereas the counter of the
prescaler restarts from 0 (but the prescale rate doesn’t change).
In addition, if the URS bit (update request selection) in TIMx_CR1 register is set, setting the
UG bit generates an update event UEV but without setting the UIF flag (thus no interrupt or
DMA request is sent). This is to avoid generating both update and capture interrupts when
clearing the counter on the capture event.
When an update event occurs, all the registers are updated and the update flag (UIF bit in
TIMx_SR register) is set (depending on the URS bit):
• The repetition counter is reloaded with the content of TIMx_RCR register.
• The buffer of the prescaler is reloaded with the preload value (content of the TIMx_PSC
register).
• The auto-reload active register is updated with the preload value (content of the
TIMx_ARR register). Note that the auto-reload is updated before the counter is
reloaded, so that the next period is the expected one.
The following figures show some examples of the counter behavior for different clock
frequencies when TIMx_ARR=0x36.

RM0438 Rev 8 1081/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
[Figure 239](../figures/figure_239.md). Counter timing diagram, internal clock divided by 1
[Figure 240](../figures/figure_240.md). Counter timing diagram, internal clock divided by 2
36 34 33 32 31 30 2F04 03 02 01 0005
MS31184V1
CK_PSC
CNT_EN
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter underflow
(cnt_udf)
Update interrupt flag
(UIF)
35
MS31185V1
CK_PSC
CNT_EN
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter underflow
Update interrupt flag
(UIF)
0002 0001 0000 0036 0035 0034 0033

Advanced-control timers (TIM1/TIM8) RM0438
1082/2187 RM0438 Rev 8
[Figure 241](../figures/figure_241.md). Counter timing diagram, internal clock divided by 4
[Figure 242](../figures/figure_242.md). Counter timing diagram, internal clock divided by N
0000 00010001 0000
MS31186V1
CK_PSC
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter underflow
Update interrupt flag
(UIF)
CNT_EN
001F20
MS31187V1
CK_PSC
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter underflow
Update interrupt flag
(UIF)
36

RM0438 Rev 8 1083/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
[Figure 243](../figures/figure_243.md). Counter timing diagram, update event when repetition counter is not used
Center-aligned mode (up/down counting)
In center-aligned mode, the counter counts from 0 to the auto-reload value (content of the
TIMx_ARR register) – 1, generates a counter overflow event, then counts from the auto-
reload value down to 1 and generates a counter underflow event. Then it restarts counting
from 0.
Center-aligned mode is active when the CMS bits in TIMx_CR1 register are not equal to
'00'. The Output compare interrupt flag of channels configured in output is set when: the
counter counts down (Center aligned mode 1, CMS = "01"), the counter counts up (Center
aligned mode 2, CMS = "10") the counter counts up and down (Center aligned mode 3,
CMS = "11").
In this mode, the DIR direction bit in the TIMx_CR1 register cannot be written. It is updated
by hardware and gives the current direction of the counter.
The update event can be generated at each counter overflow and at each counter underflow
or by setting the UG bit in the TIMx_EGR register (by software or by using the slave mode
controller) also generates an update event. In this case, the counter restarts counting from
0, as well as the counter of the prescaler.
The UEV update event can be disabled by software by setting the UDIS bit in the TIMx_CR1
register. This is to avoid updating the shadow registers while writing new values in the
preload registers. Then no update event occurs until UDIS bit has been written to 0.
However, the counter continues counting up and down, based on the current auto-reload
value.
In addition, if the URS bit (update request selection) in TIMx_CR1 register is set, setting the
UG bit generates an UEV update event but without setting the UIF flag (thus no interrupt or
FF 36
MS31188V1
CK_PSC
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter underflow
Update interrupt flag
(UIF)
0002030405 30 2F 3233343536 3101
CEN
Auto-reload preload
register
Write a new value in TIMx_ARR

Advanced-control timers (TIM1/TIM8) RM0438
1084/2187 RM0438 Rev 8
DMA request is sent). This is to avoid generating both update and capture interrupts when
clearing the counter on the capture event.
When an update event occurs, all the registers are updated and the update flag (UIF bit in
TIMx_SR register) is set (depending on the URS bit):
• The repetition counter is reloaded with the content of TIMx_RCR register
• The buffer of the prescaler is reloaded with the preload value (content of the TIMx_PSC
register)
• The auto-reload active register is updated with the preload value (content of the
TIMx_ARR register). Note that if the update source is a counter overflow, the auto-
reload is updated before the counter is reloaded, so that the next period is the expected
one (the counter is loaded with the new value).
The following figures show some examples of the counter behavior for different clock
frequencies.
[Figure 244](../figures/figure_244.md). Counter timing diagram, internal clock divided by 1, TIMx_ARR = 0x6
1. Here, center-aligned mode 1 is used (for more details refer to Section 33.4: TIM1/TIM8 registers).
MS31189V3
CK_PSC
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag (UIF)
CEN
Counter underflow
00020304 05 06 01 02 03 0401 05 0304

RM0438 Rev 8 1085/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
[Figure 245](../figures/figure_245.md). Counter timing diagram, internal clock divided by 2
[Figure 246](../figures/figure_246.md). Counter timing diagram, internal clock divided by 4, TIMx_ARR=0x36
MS31190V1
CK_PSC
CNT_EN
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter underflow
Update interrupt flag
(UIF)
0003 0002 0001 0000 0001 0002 0003
0034 0035
MS31191V1
CK_PSC
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag
(UIF)
CNT_EN
Note: Here, center_aligned mode 2 or 3 is updated with an UIF on overflow
0036 0035

Advanced-control timers (TIM1/TIM8) RM0438
1086/2187 RM0438 Rev 8
[Figure 247](../figures/figure_247.md). Counter timing diagram, internal clock divided by N
[Figure 248](../figures/figure_248.md). Counter timing diagram, update event with ARPE=1 (counter underflow)
001F20
MS31192V1
CK_PSC
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter underflow
Update interrupt flag
(UIF)
01
FD 36
MS31193V1
CK_PSC
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter underflow
Update interrupt flag
(UIF)
00 02 03 04 05 06 0701
CEN
Auto-reload preload
register
Write a new value in TIMx_ARR
06 05 04 03 02 01
FD 36Auto-reload active
register

RM0438 Rev 8 1087/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
[Figure 249](../figures/figure_249.md). Counter timing diagram, Update event with ARPE=1 (counter overflow)
33.3.3 Repetition counter
Section 33.3.1: Time-base unit describes how the update event (UEV) is generated with
respect to the counter overflows/underflows. It is actually generated only when the repetition
counter has reached zero. This can be useful when generating PWM signals.
This means that data are transferred from the preload registers to the shadow registers
(TIMx_ARR auto-reload register, TIMx_PSC prescaler register, but also TIMx_CCRx
capture/compare registers in compare mode) every N+1 counter overflows or underflows,
where N is the value in the TIMx_RCR repetition counter register.
The repetition counter is decremented:
• At each counter overflow in upcounting mode,
• At each counter underflow in downcounting mode,
• At each counter overflow and at each counter underflow in center-aligned mode.
Although this limits the maximum number of repetition to 32768 PWM cycles, it makes
it possible to update the duty cycle twice per PWM period. When refreshing compare
registers only once per PWM period in center-aligned mode, maximum resolution is
2xTck, due to the symmetry of the pattern.
The repetition counter is an auto-reload type; the repetition rate is maintained as defined by
the TIMx_RCR register value (refer to [Figure 250](../figures/figure_250.md)). When the update event is generated by
software (by setting the UG bit in TIMx_EGR register) or by hardware through the slave
mode controller, it occurs immediately whatever the value of the repetition counter is and the
repetition counter is reloaded with the content of the TIMx_RCR register.
MS31194V1
FD 36
CK_PSC
Timer clock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag
(UIF)
36 34 33 32 31 30 2FF8 F9 FA FB FCF7 35
CEN
Auto-reload preload
register
Write a new value in TIMx_ARR
Auto-reload active
register FD 36

Advanced-control timers (TIM1/TIM8) RM0438
1088/2187 RM0438 Rev 8
In Center aligned mode, for odd values of RCR, the update event occurs either on the
overflow or on the underflow depending on when the RCR register was written and when
the counter was launched: if the RCR was written before launching the counter, the UEV
occurs on the underflow. If the RCR was written after launching the counter, the UEV occurs
on the overflow.
For example, for RCR = 3, the UEV is generated each 4th overflow or underflow event
depending on when the RCR was written.
[Figure 250](../figures/figure_250.md). Update rate examples depending on mode and TIMx_RCR register settings
MSv31195V1
UEV
UEV
UEV
UEV
UEV
Counter-aligned mode Edge-aligned mode
Upcounting Downcounting
(by SW)(by SW)(by SW)
TIMx_RCR = 3
and
re-synchronization
TIMx_RCR = 3
TIMx_RCR = 2
TIMx_RCR = 1
TIMx_RCR = 0
Counter
TIMx_CNT
UEV Update event: Preload registers transferred to active registers and update interrupt generated
Update Event if the repetition counter underflow occurs when the counter is equal to the auto-reload value.

RM0438 Rev 8 1089/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.3.4 External trigger input
The timer features an external trigger input ETR. It can be used as:
• external clock (external clock mode 2, see Section 33.3.5)
• trigger for the slave mode (see Section 33.3.26)
• PWM reset input for cycle-by-cycle current regulation (see Section 33.3.7)
[Figure 251](../figures/figure_251.md) below describes the ETR input conditioning. The input polarity is defined with the
ETP bit in TIMxSMCR register. The trigger can be prescaled with the divider programmed
by the ETPS[1:0] bitfield and digitally filtered with the ETF[3:0] bitfield.
[Figure 251](../figures/figure_251.md). External trigger input block
The ETR input comes from multiple sources: input pins (default configuration), comparator
outputs and analog watchdogs. The selection is done with:
• the ETRSEL[2:0] bitfield in the TIMx_OR2 register
• the ETR_ADC1_RMP bitfield in the TIMxOR1[1:0] register
[Figure 252](../figures/figure_252.md). TIM1 ETR input circuitry
[Figure 253](../figures/figure_253.md). TIM8 ETR input circuitry
MS34403V2
To the Output mode controller
To the CK_PSC circuitry
To the Slave mode controller
0
1
ETR input ETR
ETP
TIMx_SMCR
Divider
/1, /2, /4, /8
ETPS[1:0]
TIMx_SMCR
Filter
downcounter
ETF[3:0]
TIMx_SMCR
ETRP
fDTS
MSv37631V1
ADC1_AWD3
ADC1_AWD2
ADC1_AWD1
NC
TIM1_OR1[1:0]
ETR inputs from
AF controller
TIM1_OR2[16:14]
ETR legacy mode
COMP1
COMP2
NC
NC
NC
NC
NC
ETR input
MS34469V1
ETR inputs from AF controller
TIM8_OR2[16:14]
COMP1
COMP2
NC
NC
NC
NC
NC
ETR input

Advanced-control timers (TIM1/TIM8) RM0438
1090/2187 RM0438 Rev 8
33.3.5 Clock selection
The counter clock can be provided by the following clock sources:
• Internal clock (CK_INT)
• External clock mode1: external input pin
• External clock mode2: external trigger input ETR
• Encoder mode
Internal clock source (CK_INT)
If the slave mode controller is disabled (SMS=000), then the CEN, DIR (in the TIMx_CR1
register) and UG bits (in the TIMx_EGR register) are actual control bits and can be changed
only by software (except UG which remains cleared automatically). As soon as the CEN bit
is written to 1, the prescaler is clocked by the internal clock CK_INT.
[Figure 254](../figures/figure_254.md) shows the behavior of the control circuit and the upcounter in normal mode,
without prescaler.
[Figure 254](../figures/figure_254.md). Control circuit in normal mode, internal clock divided by 1
External clock source mode 1
This mode is selected when SMS=111 in the TIMx_SMCR register. The counter can count at
each rising or falling edge on a selected input.
MSv31085V3
Internal clock
Counter clock = CK_CNT = CK_PSC
Counter register
CEN=CNT_EN
UG
Counter initialization (internal)
00 02 03 04 05 06 0732 33 34 35 3631 01

RM0438 Rev 8 1091/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
[Figure 255](../figures/figure_255.md). TI2 external clock connection example
For example, to configure the upcounter to count in response to a rising edge on the TI2
input, use the following procedure:
1. Configure channel 2 to detect rising edges on the TI2 input by writing CC2S = ‘01’ in
the TIMx_CCMR1 register.
2. Configure the input filter duration by wr iting the IC2F[3:0] bits in the TIMx_CCMR1
register (if no filter is needed, keep IC2F=0000).
3. Select rising edge polarity by writ ing CC2P=0 and CC2NP=0 in the TIMx_CCER
register.
4. Configure the timer in external clock mode 1 by writing SMS=111 in the TIMx_SMCR
register.
5. Select TI2 as the trigger input source by  writing TS=110 in the TIMx_SMCR register.
6. Enable the counter by writing CEN=1 in the TIMx_CR1 register.
Note: The capture prescaler is not used for trigge ring, so the user does not need to configure it.
When a rising edge occurs on TI2, the counter counts once and the TIF flag is set.
The delay between the rising edge on TI2 and the actual clock of the counter is due to the
resynchronization circuit on TI2 input.
External clock
mode 1
Internal clock
mode
TRGI
CK_INT
CK_PSC
TIMx_SMCR
SMS[2:0]
ITRx
TI1_ED
TI1FP1
TI2FP2
TIMx_SMCR
TS[2:0]
TI2 0
1
TIMx_CCER
CC2P
Filter
ICF[3:0]
TIMx_CCMR1
Edge
detector
TI2F_Rising
TI2F_Falling
110
0xx
100
101
MS31196V1
(internal clock)
TI1F or
TI2F oror
Encoder
mode
ETRF 111
External clock
mode 2
ETRF
ECE

Advanced-control timers (TIM1/TIM8) RM0438
1092/2187 RM0438 Rev 8
[Figure 256](../figures/figure_256.md). Control circuit in external clock mode 1
External clock source mode 2
This mode is selected by writing ECE=1 in the TIMx_SMCR register.
The counter can count at each rising or falling edge on the external trigger input ETR.
The [Figure 257](../figures/figure_257.md) gives an overview of the external trigger input block.
[Figure 257](../figures/figure_257.md). External trigger input block
For example, to configure the upcounter to count each 2 rising edges on ETR, use the
following procedure:
Counter clock = CK_CNT = CK_PSC
Counter register 35 3634
TI2
CNT_EN
TIF
Write TIF=0
MS31087V2
External clock
mode 1
Internal clock
mode
TRGI
CK_INT
CK_PSC
TIMx_SMCR
SMS[2:0]
MS33116V1
(internal clock)
TI1F or
TI2F oror
Encoder
mode
External clock
mode 2
ETRF
ECE
0
1
TIMx_SMCR
ETP
ETR pin
ETR
Divider
/1, /2, /4, /8 Filter
downcounterf
ETRP
TIMx_SMCR
ETPS[1:0]
TIMx_SMCR
ETF[3:0]
DTS

RM0438 Rev 8 1093/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
1. As no filter is needed in this example, write ETF[3:0]=0000 in the TIMx_SMCR register.
2. Set the prescaler by writing ETPS [1:0]=01 in the TIMx_SMCR register
3. Select rising edge detection on the ETR pin by writing ETP=0 in the TIMx_SMCR
register
4. Enable external clock mode 2 by wr iting ECE=1 in the TIMx_SMCR register.
5. Enable the counter by writing CEN=1 in the TIMx_CR1 register.
The counter counts once each 2 ETR rising edges.
The delay between the rising edge on ETR and the actual clock of the counter is due to the
resynchronization circuit on the ETRP signal. As a consequence, the maximum frequency
which can be correctly captured by the counter is at most ¼ of TIMxCLK frequency. When
the ETRP signal is faster, the user should apply a division of the external signal by proper
ETPS prescaler setting.
[Figure 258](../figures/figure_258.md). Control circuit in external clock mode 2
MSv33111V3
34 35 36
fCK_INT
CNT_EN
ETR
ETRP
ETRF
Counter clock =
CK_CNT =CK_PSC
Counter register

Advanced-control timers (TIM1/TIM8) RM0438
1094/2187 RM0438 Rev 8
33.3.6 Capture/compare channels
Each Capture/Compare channel is built around a capture/compare register (including a
shadow register), an input stage for capture (with digital filter, multiplexing, and prescaler,
except for channels 5 and 6) and an output stage (with comparator and output control).
[Figure 259](../figures/figure_259.md) to [Figure 262](../figures/figure_262.md) give an overview of one Capture/Compare channel.
The input stage samples the corresponding TIx input to generate a filtered signal TIxF.
Then, an edge detector with polarity selection generates a signal (TIxFPx) which can be
used as trigger input by the slave mode controller or as the capture command. It is
prescaled before the capture register (ICxPS).
[Figure 259](../figures/figure_259.md). Capture/compare channel (example: channel 1 input stage)
The output stage generates an intermediate waveform which is then used for reference:
OCxRef (active high). The polarity acts at the end of the chain.
0
1
Divider
/1, /2, /4, /8
ICPS[1:0]
TI1F_ED
To the slave mode controller
TI1FP1
11
01
CC1S[1:0]
IC1TI2FP1
TRC
(from slave mode
controller)
10
IC1PS
0
1
MS33115V1
TI1
TIMx_CCER
CC1P/CC1NP
Filter
downcounter
ICF[3:0]
TIMx_CCMR1
Edge
detector
TI1F_Rising
TI1F_Falling
TIMx_CCMR1
TIMx_CCER
TI2F_Rising
(from channel 2)
TI2F_Falling
(from channel 2)
TI1F
f
CC1E
DTS

RM0438 Rev 8 1095/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
[Figure 260](../figures/figure_260.md). Capture/compare channel 1 main circuit
[Figure 261](../figures/figure_261.md). Output stage of capture/compare channel (channel 1, idem ch. 2 and 3)
1. OCxREF, where x is the rank of the complementary channel
MSv63030V1
CC1E
compare shadow register
Comparator
Capture/compare preload register
Counter
IC1PS
CC1S[0]
CC1S[1]
Capture
Input mode
CC1S[0]
CC1S[1]
Output mode
UEV
OC1PE
(from time
base unit)
Compare
transfer
APB Bus
16/32-bit
MCU-peripheral interface
TIMx_CCMR1
OC1PE
CNT>CCR1
CNT=CCR1
TIMx_EGR
CC1G
MS35909V2
Output
mode
controller
CNT>CCR1
CNT=CCR1
TIM1_CCMR1
OC1M[3:0]
OC1REF
OC1CE
Dead-time
generator
OC1_DT
OC1N_DT
DTG[7:0]
TIM1_BDTR
‘0’
‘0’
CC1E
TIM1_CCER
CC1NE
0
1
CC1P
TIM1_CCER
0
1
CC1NP
TIM1_CCER
OC1
Output
enable
circuit
OC1N
CC1E TIM1_CCERCC1NE
OSSI
TIM1_BDTR
MOE OSSR
0x
10
11
11
01
x0
Output
selector
OCxREF
OC1REFC
To the master mode
controller
Output
enable
circuit
OC5REF
(1)
ETRF
OIS1N
TIM1_CR2
OIS1

Advanced-control timers (TIM1/TIM8) RM0438
1096/2187 RM0438 Rev 8
[Figure 262](../figures/figure_262.md). Output stage of capture/compare channel (channel 4)
[Figure 263](../figures/figure_263.md). Output stage of capture/compare channel (channel 5, idem ch. 6)
1. Not available externally.
The capture/compare block is made of one preload register and one shadow register. Write
and read always access the preload register.
In capture mode, captures are actually done in the shadow register, which is copied into the
preload register.
In compare mode, the content of the preload register is copied into the shadow register
which is compared to the counter.
33.3.7 Input capture mode
In Input capture mode, the Capture/Compare Registers (TIMx_CCRx) are used to latch the
value of the counter after a transition detected by the corresponding ICx signal. When a
capture occurs, the corresponding CCXIF flag (TIMx_SR register) is set and an interrupt or
a DMA request can be sent if they are enabled. If a capture occurs while the CCxIF flag was
already high, then the over-capture flag CCxOF (TIMx_SR register) is set. CCxIF can be
MS35911V2
Output
mode
controller
CNT > CCR4
CNT = CCR4
TIM1_CCMR2
OC4M[3:0]
0
1
CC4P
TIM1_CCER
Output
enable
circuit
OC4
CC4E TIM1_CCER
To the master
mode controller
OC4REF
OC4CE
0
1
CC4E
TIM1_CCER
‘0’
TIM1_BDTROSSIMOE
OIS4 TIM1_CR2
ETRF
Output
selector
OC3REF
OC4REFC
MS35910V2
Output
mode
controller
CNT > CCR5
CNT = CCR5
TIM1_CCMR2
OC5M[3:0]
0
1
CC5P
TIM1_CCER
Output
enable
circuit
OC5
CC5E TIM1_CCER
To the master
mode controller
OC5REF
OC5CE
0
1
CC5E
TIM1_CCER
‘0’
TIM1_BDTROSSIMOE
OIS5 TIM1_CR2
(1)
ETRF

RM0438 Rev 8 1097/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
cleared by software by writing it to ‘0’ or by reading the captured data stored in the
TIMx_CCRx register. CCxOF is cleared when written with ‘0’.
The following example shows how to capture the counter value in TIMx_CCR1 when TI1
input rises. To do this, use the following procedure:
1. Select the active input: TIMx_CCR1 must be  linked to the TI1 input, so write the CC1S
bits to 01 in the TIMx_CCMR1 register. As soon as CC1S becomes different from 00,
the channel is configured in input and the TIMx_CCR1 register becomes read-only.
2. Program the appropriate input filter duration in relation with the signal connected to the
timer (when the input is one of the TIx (ICxF bits in the TIMx_CCMRx register). Let’s
imagine that, when toggling, the input signal is not stable during at must 5 internal clock
cycles. We must program a filter duration longer than these 5 clock cycles. We can
validate a transition on TI1 when 8 consecutive samples with the new level have been
detected (sampled at fDTS frequency). Then write IC1F bits to 0011 in the
TIMx_CCMR1 register.
3. Select the edge of the active transitio n on the TI1 channel by writing CC1P and CC1NP
bits to 0 in the TIMx_CCER register (rising edge in this case).
4. Program the input prescaler. In our example, we wish the capture to be performed at
each valid transition, so the prescaler is disabled (write IC1PS bits to ‘00’ in the
TIMx_CCMR1 register).
5. Enable capture from the counter into the ca pture register by setting the CC1E bit in the
TIMx_CCER register.
6. If needed, enable the related interrupt request by setting the CC1IE bit in the
TIMx_DIER register, and/or the DMA request by setting the CC1DE bit in the
TIMx_DIER register.
When an input capture occurs:
• The TIMx_CCR1 register gets the value of the counter on the active transition.
• CC1IF flag is set (interrupt flag). CC1OF is also set if at least two consecutive captures
occurred whereas the flag was not cleared.
• An interrupt is generated depending on the CC1IE bit.
• A DMA request is generated depending on the CC1DE bit.
In order to handle the overcapture, it is recommended to read the data before the
overcapture flag. This is to avoid missing an overcapture which could happen after reading
the flag and before reading the data.
Note: IC interrupt and/or DMA requests can be generated by software by setting the
corresponding CCxG bit in the TIMx_EGR register.
33.3.8 PWM input mode
This mode is a particular case of input capture mode. The procedure is the same except:
• Two ICx signals are mapped on the same TIx input.
• These 2 ICx signals are active on edges with opposite polarity.
• One of the two TIxFP signals is selected as trigger input and the slave mode controller
is configured in reset mode.
For example, the user can measure the period (in TIMx_CCR1 register) and the duty cycle
(in TIMx_CCR2 register) of the PWM applied on TI1 using the following procedure
(depending on CK_INT frequency and prescaler value):

Advanced-control timers (TIM1/TIM8) RM0438
1098/2187 RM0438 Rev 8
1. Select the active input for TIMx_CCR1: write the CC1S bits to 01 in the TIMx_CCMR1
register (TI1 selected).
2. Select the active polarity for TI1FP1 (u sed both for capture in TIMx_CCR1 and counter
clear): write the CC1P and CC1NP bits to ‘0’ (active on rising edge).
3. Select the active input fo r TIMx_CCR2: write the CC2S bits to 10 in the TIMx_CCMR1
register (TI1 selected).
4. Select the active polarity for TI1FP2 (use d for capture in TIMx_CCR2): write the CC2P
and CC2NP bits to CC2P/CC2NP=’10’ (active on falling edge).
5. Select the valid trigger input: write the TS bits to 101 in the TIMx_SMCR register
(TI1FP1 selected).
6. Configure the slave mode controller in reset mode: write the SMS bits to 0100 in the
TIMx_SMCR register.
7. Enable the captures: write the CC1E and CC2E bits to ‘1’ in the TIMx_CCER register.
[Figure 264](../figures/figure_264.md). PWM input mode timing
33.3.9 Forced output mode
In output mode (CCxS bits = 00 in the TIMx_CCMRx register), each output compare signal
(OCxREF and then OCx/OCxN) can be forced to active or inactive level directly by software,
independently of any comparison between the output compare register and the counter.
To force an output compare signal (OCXREF/OCx) to its active level, user just needs to
write 0101 in the OCxM bits in the corresponding TIMx_CCMRx register. Thus OCXREF is
forced high (OCxREF is always active high) and OCx get opposite value to CCxP polarity
bit.
For example: CCxP=0 (OCx active high) => OCx is forced to high level.
The OCxREF signal can be forced low by writing the OCxM bits to 0100 in the
TIMx_CCMRx register.
Anyway, the comparison between the TIMx_CCRx shadow register and the counter is still
performed and allows the flag to be set. Interrupt and DMA requests can be sent
accordingly. This is described in the output compare mode section below.

RM0438 Rev 8 1099/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.3.10 Output compare mode
This function is used to control an output waveform or indicate when a period of time has
elapsed. Channels 1 to 4 can be output, while Channel 5 and 6 are only available inside the
device (for instance, for compound waveform generation or for ADC triggering).
When a match is found between the capture/compare register and the counter, the output
compare function:
• Assigns the corresponding output pin to a programmable value defined by the output
compare mode (OCxM bits in the TIMx_CCMRx register) and the output polarity (CCxP
bit in the TIMx_CCER register). The output pin can keep its level (OCXM=0000), be set
active (OCxM=0001), be set inactive (OCxM=0010) or can toggle (OCxM=0011) on
match.
• Sets a flag in the interrupt status register (CCxIF bit in the TIMx_SR register).
• Generates an interrupt if the corresponding interrupt mask is set (CCXIE bit in the
TIMx_DIER register).
• Sends a DMA request if the corresponding enable bit is set (CCxDE bit in the
TIMx_DIER register, CCDS bit in the TIMx_CR2 register for the DMA request
selection).
The TIMx_CCRx registers can be programmed with or without preload registers using the
OCxPE bit in the TIMx_CCMRx register.
In output compare mode, the update event UEV has no effect on OCxREF and OCx output.
The timing resolution is one count of the counter. Output compare mode can also be used to
output a single pulse (in One Pulse mode).
Procedure
1. Select the counter clock (i nternal, external, prescaler).
2. Write the desired data in the TIMx_ARR and TIMx_CCRx registers.
3. Set the CCxIE bit if an inte rrupt request is to be generated.
4. Select the output mode. For example:
– Write OCxM = 0011 to toggle OCx output pin when CNT matches CCRx
– Write OCxPE = 0 to disable preload register
– Write CCxP = 0 to select active high polarity
– Write CCxE = 1 to enable the output
5. Enable the counter by setting the CEN bit in the TIMx_CR1 register.
The TIMx_CCRx register can be updated at any time by software to control the output
waveform, provided that the preload register is not enabled (OCxPE=’0’, else TIMx_CCRx
shadow register is updated only at the next update event UEV). An example is given in
[Figure 265](../figures/figure_265.md).

Advanced-control timers (TIM1/TIM8) RM0438
1100/2187 RM0438 Rev 8
[Figure 265](../figures/figure_265.md). Output compare mode, toggle on OC1
33.3.11 PWM mode
Pulse Width Modulation mode allows a signal to be generated with a frequency determined
by the value of the TIMx_ARR register and a duty cycle determined by the value of the
TIMx_CCRx register.
The PWM mode can be selected independently on each channel (one PWM per OCx
output) by writing ‘0110’ (PWM mode 1) or ‘0111’ (PWM mode 2) in the OCxM bits in the
TIMx_CCMRx register. The corresponding preload register must be enabled by setting the
OCxPE bit in the TIMx_CCMRx register, and eventually the auto-reload preload register (in
upcounting or center-aligned modes) by setting the ARPE bit in the TIMx_CR1 register.
As the preload registers are transferred to the shadow registers only when an update event
occurs, before starting the counter, all registers must be initialized by setting the UG bit in
the TIMx_EGR register.
OCx polarity is software programmable using the CCxP bit in the TIMx_CCER register. It
can be programmed as active high or active low. OCx output is enabled by a combination of
the CCxE, CCxNE, MOE, OSSI and OSSR bits (TIMx_CCER and TIMx_BDTR registers).
Refer to the TIMx_CCER register description for more details.
In PWM mode (1 or 2), TIMx_CNT and TIMx_CCRx are always compared to determine
whether TIMx_CCRx ≤ TIMx_CNT or TIMx_CNT ≤ TIMx_CCRx (depending on the direction
of the counter).
The timer is able to generate PWM in edge-aligned mode or center-aligned mode
depending on the CMS bits in the TIMx_CR1 register.
MS31092V1
OC1REF= OC1
TIM1_CNT B200 B2010039
TIM1_CCR1 003A
Write B201h in the CC1R register
Match detected on CCR1
Interrupt generated if enabled
003B
B201
003A

RM0438 Rev 8 1101/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
PWM edge-aligned mode
• Upcounting configuration
Upcounting is active when the DIR bit in the TIMx_CR1 register is low. Refer to the
Upcounting mode on page 1076.
In the following example, we consider PWM mode 1. The reference PWM signal
OCxREF is high as long as TIMx_CNT < TIMx_CCRx else it becomes low. If the
compare value in TIMx_CCRx is greater than the auto-reload value (in TIMx_ARR)
then OCxREF is held at ‘1’. If the compare value is 0 then OCxRef is held at ‘0’.
[Figure 266](../figures/figure_266.md) shows some edge-aligned PWM waveforms in an example where
TIMx_ARR=8.
[Figure 266](../figures/figure_266.md). Edge-aligned PWM waveforms (ARR=8)
• Downcounting configuration
Downcounting is active when DIR bit in TIMx_CR1 register is high. Refer to the
Downcounting mode on page 1080
In PWM mode 1, the reference signal OCxRef is low as long as
TIMx_CNT > TIMx_CCRx else it becomes high. If the compare value in TIMx_CCRx is
greater than the auto-reload value in TIMx_ARR, then OCxREF is held at ‘1’. 0% PWM
is not possible in this mode.
PWM center-aligned mode
Center-aligned mode is active when the CMS bits in TIMx_CR1 register are different from
‘00’ (all the remaining configurations having the same effect on the OCxRef/OCx signals).
The compare flag is set when the counter counts up, when it counts down or both when it
counts up and down depending on the CMS bits configuration. The direction bit (DIR) in the
MS31093V1
Counter register
‘1’
0 12 3 456 780 1
OCXREF
CCxIF
OCXREF
CCxIF
OCXREF
CCxIF
OCXREF
CCxIF
CCRx=4
CCRx=8
CCRx>8
CCRx=0
‘0’

Advanced-control timers (TIM1/TIM8) RM0438
1102/2187 RM0438 Rev 8
TIMx_CR1 register is updated by hardware and must not be changed by software. Refer to
the Center-aligned mode (up/down counting) on page 1083.
[Figure 267](../figures/figure_267.md) shows some center-aligned PWM waveforms in an example where:
• TIMx_ARR=8,
• PWM mode is the PWM mode 1,
• The flag is set when the counter counts down corresponding to the center-aligned
mode 1 selected for CMS=01 in TIMx_CR1 register.
[Figure 267](../figures/figure_267.md). Center-aligned PWM waveforms (ARR=8)
Hints on using center-aligned mode
• When starting in center-aligned mode, the current up-down configuration is used. It
means that the counter counts up or down depending on the value written in the DIR bit
CCxIF
0123456787654321 01Counter register
CCRx = 4
OCxREF
CMS=01
CMS=10
CMS=11
CCxIF
CCRx=7
OCxREF
CMS=10 or 11
CCxIF
CCRx=8
OCxREF
CMS=01
CMS=10
CMS=11
‘1’
CCxIF
CCRx>8
OCxREF
CMS=01
CMS=10
CMS=11
‘1’
CCxIF
CCRx=0
OCxREF
CMS=01
CMS=10
CMS=11
‘0’
AI14681b

RM0438 Rev 8 1103/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
in the TIMx_CR1 register. Moreover, the DIR and CMS bits must not be changed at the
same time by the software.
• Writing to the counter while running in center-aligned mode is not recommended as it
can lead to unexpected results. In particular:
– The direction is not updated if a value gr eater than the auto-reload value is written
in the counter (TIMx_CNT>TIMx_ARR). For example, if the counter was counting
up, it continues to count up.
– The direction is updated if 0 or the TIMx _ARR value is written in the counter but no
Update Event UEV is generated.
• The safest way to use center-aligned mode is to generate an update by software
(setting the UG bit in the TIMx_EGR register) just before starting the counter and not to
write the counter while it is running.
33.3.12 Asymmetric PWM mode
Asymmetric mode allows two center-aligned PWM signals to be generated with a
programmable phase shift. While the frequency is determined by the value of the
TIMx_ARR register, the duty cycle and the phase-shift are determined by a pair of
TIMx_CCRx register. One register controls the PWM during up-counting, the second during
down counting, so that PWM is adjusted every half PWM cycle:
– OC1REFC (or OC2REFC) is contro lled by TIMx_CCR1 and TIMx_CCR2
– OC3REFC (or OC4REFC) is contro lled by TIMx_CCR3 and TIMx_CCR4
Asymmetric PWM mode can be selected independently on two channel (one OCx output
per pair of CCR registers) by writing ‘1110’ (Asymmetric PWM mode 1) or ‘1111’
(Asymmetric PWM mode 2) in the OCxM bits in the TIMx_CCMRx register.
Note: The OCxM[3:0] bit field is split into two pa rts for compatibility reasons, the most significant
bit is not contiguous with the 3 least significant ones.
When a given channel is used as asymmetric PWM channel, its complementary channel
can also be used. For instance, if an OC1REFC signal is generated on channel 1
(Asymmetric PWM mode 1), it is possible to output either the OC2REF signal on channel 2,
or an OC2REFC signal resulting from asymmetric PWM mode 1.
[Figure 268](../figures/figure_268.md) represents an example of signals that can be generated using Asymmetric PWM
mode (channels 1 to 4 are configured in Asymmetric PWM mode 1). Together with the
deadtime generator, this allows a full-bridge phase-shifted DC to DC converter to be
controlled.

Advanced-control timers (TIM1/TIM8) RM0438
1104/2187 RM0438 Rev 8
[Figure 268](../figures/figure_268.md). Generation of 2 phase-shifted PWM signals with 50% duty cycle
33.3.13 Combined PWM mode
Combined PWM mode allows two edge or center-aligned PWM signals to be generated with
programmable delay and phase shift between respective pulses. While the frequency is
determined by the value of the TIMx_ARR register, the duty cycle and delay are determined
by the two TIMx_CCRx registers. The resulting signals, OCxREFC, are made of an OR or
AND logical combination of two reference PWMs:
– OC1REFC (or OC2REFC) is contro lled by TIMx_CCR1 and TIMx_CCR2
– OC3REFC (or OC4REFC) is contro lled by TIMx_CCR3 and TIMx_CCR4
Combined PWM mode can be selected independently on two channels (one OCx output per
pair of CCR registers) by writing ‘1100’ (Combined PWM mode 1) or ‘1101’ (Combined PWM
mode 2) in the OCxM bits in the TIMx_CCMRx register.
When a given channel is used as combined PWM channel, its complementary channel must
be configured in the opposite PWM mode (for instance, one in Combined PWM mode 1 and
the other in Combined PWM mode 2).
Note: The OCxM[3:0] bit field is split into two pa rts for compatibility reasons, the most significant
bit is not contiguous with the 3 least significant ones.
[Figure 269](../figures/figure_269.md) represents an example of signals that can be generated using Asymmetric PWM
mode, obtained with the following configuration:
– Channel 1 is configured in Combined PWM mode 2,
– Channel 2 is configured in PWM mode 1,
– Channel 3 is configured in Combined PWM mode 2,
– Channel 4 is configured in PWM mode 1.
MS33117V1
Counter register
OC1REFC
CCR1=0
CCR2=8
CCR3=3
CCR4=5
01234567 0 12345678 11
OC3REFC

RM0438 Rev 8 1105/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
[Figure 269](../figures/figure_269.md). Combined PWM mode on channel 1 and 3
33.3.14 Combined 3-phase PWM mode
Combined 3-phase PWM mode allows one to three center-aligned PWM signals to be
generated with a single programmable signal ANDed in the middle of the pulses. The
OC5REF signal is used to define the resulting combined signal. The 3-bits GC5C[3:1] in the
TIMx_CCR5 allow selection on which reference signal the OC5REF is combined. The
resulting signals, OCxREFC, are made of an AND logical combination of two reference
PWMs:
– If GC5C1 is set, OC1REFC is controlled by TIMx_CCR1 and TIMx_CCR5
– If GC5C2 is set, OC2REFC is controlled by TIMx_CCR2 and TIMx_CCR5
– If GC5C3 is set, OC3REFC is controlled by TIMx_CCR3 and TIMx_CCR5
Combined 3-phase PWM mode can be selected independently on channels 1 to 3 by setting
at least one of the 3-bits GC5C[3:1].
MS31094V1
OC1REF
OC2REF
OC1REF’
OC2REF’
OC1REFC
OC1REFC’
OC1REFC = OC1REF AND OC2REF
OC1REFC’ = OC1REF’ OR OC2REF’
OC1
OC2
OC1’
OC2’

Advanced-control timers (TIM1/TIM8) RM0438
1106/2187 RM0438 Rev 8
[Figure 270](../figures/figure_270.md). 3-phase combined PWM signals with multiple trigger pulses per period
The TRGO2 waveform shows how the ADC can be synchronized on given 3-phase PWM
signals. Refer to Section 33.3.27: ADC synchronization for more details.
33.3.15 Complementary output s and dead-time insertion
The advanced-control timers (TIM1/TIM8) can output two complementary signals and
manage the switching-off and the switching-on instants of the outputs.
This time is generally known as dead-time and it has to be adjusted depending on the
devices that are connected to the outputs and their characteristics (intrinsic delays of level-
shifters, delays due to power switches...)
The polarity of the outputs (main output OCx or complementary OCxN) can be selected
independently for each output. This is done by writing to the CCxP and CCxNP bits in the
TIMx_CCER register.
The complementary signals OCx and OCxN are activated by a combination of several
control bits: the CCxE and CCxNE bits in the TIMx_CCER register and the MOE, OISx,
OISxN, OSSI and OSSR bits in the TIMx_BDTR and TIMx_CR2 registers. Refer to
[Table 281](../tables/table_281.md): Output control bits for complementary OCx and OCxN channels with break
feature on page 1152 for more details. In particular, the dead-time is activated when
switching to the idle state (MOE falling down to 0).
ARR
OC5
OC1
OC2
OC3
OC5ref
OC1refC
OC6
OC4
TRGO2
100 xxx
001 100
Preload
GC5C[3:0] xxx
Counter
MS33102V1
OC2refC
OC3refC
Active
OC4ref
OC6ref

RM0438 Rev 8 1107/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Dead-time insertion is enabled by setting both CCxE and CCxNE bits, and the MOE bit if the
break circuit is present. There is one 10-bit dead-time generator for each channel. From a
reference waveform OCxREF, it generates 2 outputs OCx and OCxN. If OCx and OCxN are
active high:
• The OCx output signal is the same as the reference signal except for the rising edge,
which is delayed relative to the reference rising edge.
• The OCxN output signal is the opposite of the reference signal except for the rising
edge, which is delayed relative to the reference falling edge.
If the delay is greater than the width of the active output (OCx or OCxN) then the
corresponding pulse is not generated.
The following figures show the relationships between the output signals of the dead-time
generator and the reference signal OCxREF. (we suppose CCxP=0, CCxNP=0, MOE=1,
CCxE=1 and CCxNE=1 in these examples)
[Figure 271](../figures/figure_271.md). Complementary output with dead-time insertion
[Figure 272](../figures/figure_272.md). Dead-time waveforms with delay greater than the negative pulse
delay
delay
OCxREF
OCx
OCxN
MS31095V1
MS31096V1
delay
OCxREF
OCx
OCxN

Advanced-control timers (TIM1/TIM8) RM0438
1108/2187 RM0438 Rev 8
[Figure 273](../figures/figure_273.md). Dead-time waveforms with delay greater than the positive pulse
The dead-time delay is the same for each of the channels and is programmable with the
DTG bits in the TIMx_BDTR register. Refer to Section 33.4.20: TIMx break and dead-time
register (TIMx_BDTR)(x = 1, 8) for delay calculation.
Re-directing OCxREF to OCx or OCxN
In output mode (forced, output compare or PWM), OCxREF can be re-directed to the OCx
output or to OCxN output by configuring the CCxE and CCxNE bits in the TIMx_CCER
register.
This allows a specific waveform to be sent (such as PWM or static active level) on one
output while the complementary remains at its inactive level. Other alternative possibilities
are to have both outputs at inactive level or both outputs active and complementary with
dead-time.
Note: When only OCxN is enabled (CCxE=0, CC xNE=1), it is not complemented and becomes
active as soon as OCxREF is high. For example, if CCxNP=0 then OCxN=OCxRef. On the
other hand, when both OCx and OCxN are enabled (CCxE=CCxNE=1) OCx becomes
active when OCxREF is high whereas OCxN is complemented and becomes active when
OCxREF is low.
33.3.16 Using the break function
The purpose of the break function is to protect power switches driven by PWM signals
generated with the TIM1 and TIM8 timers. The two break inputs are usually connected to
fault outputs of power stages and 3-phase inverters. When activated, the break circuitry
shuts down the PWM outputs and forces them to a predefined safe state. A number of
internal MCU events can also be selected to trigger an output shut-down.
The break features two channels. A break channel which gathers both system-level fault
(clock failure, parity error,...) and application fault (from input pins and built-in comparator),
and can force the outputs to a predefined level (either active or inactive) after a deadtime
duration. A break2 channel which only includes application faults and is able to force the
outputs to an inactive state.
MS31097V1
delay
OCxREF
OCx
OCxN

RM0438 Rev 8 1109/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
The output enable signal and output levels during break are depending on several control
bits:
– the MOE bit in TIMx_BDTR register allows  the outputs to be enabled/disabled by
software and is reset in case of break or break2 event.
– the OSSI bit in the TIMx_BDTR register  defines whether the timer controls the
output in inactive state or releases the control to the GPIO controller (typically to
have it in Hi-Z mode)
– the OISx and OISxN bits in  the TIMx_CR2 register which are setting the output
shut-down level, either active or inactive. The OCx and OCxN outputs cannot be
set both to active level at a given time, whatever the OISx and OISxN values.
Refer to [Table 281](../tables/table_281.md): Output control bits for complementary OCx and OCxN
channels with break feature on page 1152 for more details.
When exiting from reset, the break circuit is disabled and the MOE bit is low. The break
functions can be enabled by setting the BKE and BK2E bits in the TIMx_BDTR register. The
break input polarities can be selected by configuring the BKP and BK2P bits in the same
register. BKE/BK2E and BKP/BK2P can be modified at the same time. When the BKE/BK2E
and BKP/BK2P bits are written, a delay of 1 APB clock cycle is applied before the writing is
effective. Consequently, it is necessary to wait 1 APB clock period to correctly read back the
bit after the write operation.
Because MOE falling edge can be asynchronous, a resynchronization circuit has been
inserted between the actual signal (acting on the outputs) and the synchronous control bit
(accessed in the TIMx_BDTR register). It results in some delays between the asynchronous
and the synchronous signals. In particular, if MOE is set to 1 whereas it was low, a delay
must be inserted (dummy instruction) before reading it correctly. This is because the write
acts on the asynchronous signal whereas the read reflects the synchronous signal.
The break can be generated from multiple sources which can be individually enabled and
with programmable edge sensitivity, using the TIMx_OR2 and TIMx_OR3 registers.
The sources for break (BRK) channel are:
• An external source connected to one of the BKIN pin (as per selection done in the
GPIO alternate function registers), with polarity selection and optional digital filtering
• An internal source:
–t h e  C o r t e x®-M33 LOCKUP output
– the PVD output
– the SRAM parity error signal
– a flash memory ECC dual error detection
– a clock failure event generated by the CSS detector
– the output from a comparator, with polarity selection and optional digital filtering
– the analog watchdog output of the DFSDM1 peripheral
The sources for break2 (BRK2) are:
• An external source connected to one of the BKIN pin (as per selection done in the
GPIO alternate function registers), with polarity selection and optional digital filtering
• An internal source coming from a comparator output.
Break events can also be generated by software using BG and B2G bits in the TIMx_EGR
register. The software break generation using BG and B2G is active whatever the BKE and
BK2E enable bits values.

Advanced-control timers (TIM1/TIM8) RM0438
1110/2187 RM0438 Rev 8
All sources are ORed before entering the timer BRK or BRK2 inputs, as per [Figure 274](../figures/figure_274.md)
below.
[Figure 274](../figures/figure_274.md). Break and Break2 circuitry overview
Note: An asynchronous (clockless) operation is only guaranteed when the programmable filter is
disabled. If it is enabled, a fail safe clock mode (for example by using the internal PLL and/or
the CSS) must be used to guarantee that break events are handled.
MS34405V4
COMP2 output
DFSDM
BREAK output
BK2DFBKxE
BK2CMP2E
BK2CMP2P
COMP1 output
BK2CMP1E
BK2CMP1P
BKIN2 inputs
from AF
controller
BK2INE
BK2INP
BK2F[3:0]
Filter
BK2P
Software break requests: B2G
BK2E
Application break requests
B2IF flag
BRK2 request
COMP2 output
DFSDM
BREAK output
BKDFBKxE
BKCMP2E
BKCMP2P
COMP1 output
BKCMP1E
BKCMP1P
BKIN inputs
from AF
controller
BKINE
BKINP
BKF[3:0]
Filter
BKP
BKE
Application break requests
BRK request
ECC LOCK
Parity LOCK
PVD LOCK
Lockup LOCK
Double ECC Error
RAM parity Error
PVD
Core Lockup
CSS
BIF flag
SBIF flag
System break requests
Software break requests: BG

RM0438 Rev 8 1111/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
When one of the breaks occurs (selected level on one of the break inputs):
• The MOE bit is cleared asynchronously, putting the outputs in inactive state, idle state
or even releasing the control to the GPIO controller (selected by the OSSI bit). This
feature is enabled even if the MCU oscillator is off.
• Each output channel is driven with the level programmed in the OISx bit in the
TIMx_CR2 register as soon as MOE=0. If OSSI=0, the timer releases the output control
(taken over by the GPIO controller), otherwise the enable output remains high.
• When complementary outputs are used:
– The outputs are first put in inactive state (depending on the polarity). This is done
asynchronously so that it works even if no clock is provided to the timer.
– If the timer clock is still present, then the dead-time generator is reactivated in
order to drive the outputs with the level programmed in the OISx and OISxN bits
after a dead-time. Even in this case, OCx and OCxN cannot be driven to their
active level together. Note that because of the resynchronization on MOE, the
dead-time duration is slightly longer than usual (around 2 ck_tim clock cycles).
– If OSSI=0, the timer releases the output control (taken over by the GPIO controller
which forces a Hi-Z state), otherwise the enable outputs remain or become high as
soon as one of the CCxE or CCxNE bits is high.
• The break status flag (SBIF, BIF and B2IF bits in the TIMx_SR register) is set. An
interrupt is generated if the BIE bit in the TIMx_DIER register is set.
• If the AOE bit in the TIMx_BDTR register is set, the MOE bit is automatically set again
at the next update event (UEV). As an example, this can be used to perform a
regulation. Otherwise, MOE remains low until the application sets it to ‘1’ again. In this
case, it can be used for security and the break input can be connected to an alarm from
power drivers, thermal sensors or any security components.
Note: If the MOE is reset by the CPU while the AOE bit is set, the outputs are in idle state and
forced to inactive level or Hi-Z depending on OSSI value.
If both the MOE and AOE bits are reset by the CPU, the outputs are in disabled state and
driven with the level programmed in the OISx bit in the TIMx_CR2 register.
Note: The break inputs are active on level. Thus, the MOE cannot be set while the break input is
active (neither automatically nor by software). In the meantime, the status flag BIF and B2IF
cannot be cleared.
In addition to the break input and the output management, a write protection has been
implemented inside the break circuit to safeguard the application. It allows the configuration
of several parameters to be freezed (dead-time duration, OCx/OCxN polarities and state
when disabled, OCxM configurations, break enable and polarity). The application can
choose from 3 levels of protection selected by the LOCK bits in the TIMx_BDTR register.
Refer to Section 33.4.20: TIMx break and dead-time register (TIMx_BDTR)(x = 1, 8). The
LOCK bits can be written only once after an MCU reset.
[Figure 275](../figures/figure_275.md) shows an example of behavior of the outputs in response to a break.

Advanced-control timers (TIM1/TIM8) RM0438
1112/2187 RM0438 Rev 8
[Figure 275](../figures/figure_275.md). Various output behavior in response to a break event on BRK (OSSI = 1)
delay delay delay
delay delay delay
delay
delay
OCxREF
OCx
(OCxN not implemented, CCxP=0, OISx=1)
OCx
(OCxN not implemented, CCxP=0, OISx=0)
OCx
(OCxN not implemented, CCxP=1, OISx=1)
OCx
(OCxN not implemented, CCxP=1, OISx=0)
OCx
OCxN
(CCxE=1, CCxP=0, OISx=0, CCxNE=1, CCxNP=0, OISxN=1)
OCx
OCxN
(CCxE=1, CCxP=0, OISx=1, CCxNE=1, CCxNP=1, OISxN=1)
OCx
OCxN
(CCxE=1, CCxP=0, OISx=0, CCxNE=0, CCxNP=0, OISxN=1)
OCx
OCxN
(CCxE=1, CCxP=0, OISx=1, CCxNE=0, CCxNP=0, OISxN=0)
OCx
OCxN
(CCxE=1, CCxP=0, CCxNE=0, CCxNP=0, OISx=OISxN=0 or OISx=OISxN=1)
MS31098V1
BREAK (MOE     )

RM0438 Rev 8 1113/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
The two break inputs have different behaviors on timer outputs:
– The BRK input can either disable (inactive  state) or force the PWM outputs to a
predefined safe state.
– BRK2 can only disable (inact ive state) the PWM outputs.
The BRK has a higher priority than BRK2 input, as described in [Table 277](../tables/table_277.md).
Note: BRK2 must only be used with OSSR = OSSI = 1.
[Figure 276](../figures/figure_276.md) gives an example of OCx and OCxN output behavior in case of active signals on
BRK and BRK2 inputs. In this case, both outputs have active high polarities (CCxP =
CCxNP = 0 in TIMx_CCER register).
[Figure 276](../figures/figure_276.md). PWM output state following BRK and BRK2 pins assertion (OSSI=1)
[Table 277](../tables/table_277.md). Behavior of timer outputs versus BRK/BRK2 inputs
BRK BRK2 Timer outputs
state
Typical use case
OCxN output
(low side switches)
OCx output
(high side switches)
Active X
– Inactive then
forced output
state (after a
deadtime)
– Outputs disabled
if OSSI = 0
(control taken
over by GPIO
logic)
ON after deadtime
insertion OFF
Inactive Active Inactive OFF OFF
MS34106V1
BRK2
BRK
OCx
I/O state
Deadtime Deadtime
Active Inactive Idle

Advanced-control timers (TIM1/TIM8) RM0438
1114/2187 RM0438 Rev 8
[Figure 277](../figures/figure_277.md). PWM output state following BRK assertion (OSSI=0)
33.3.17 Bidirectional break inputs
The TIM1/TIM8 are featuring bidirectional break I/Os, as represented on [Figure 278](../figures/figure_278.md).
They allow the following:
• A board-level global break signal available for signaling faults to external MCUs or gate
drivers, with a unique pin being both an input and an output status pin
• Internal break sources and multiple external open drain comparator outputs ORed
together to trigger a unique break event, when multiple internal and external break
sources must be merged
The break and break2 inputs are configured in bidirectional mode using the BKBID and
BK2BID bits in the TIMxBDTR register. The BKBID programming bits can be locked in read-
only mode using the LOCK bits in the TIMxBDTR register (in LOCK level 1 or above).
The bidirectional mode is available for both the break and break2 inputs, and require the I/O
to be configured in open-drain mode with active low polarity (using BKINP, BKP , BK2INP
and BK2P bits). Any break request coming either from system (e.g. CSS), from on-chip
peripherals or from break inputs forces a low level on the break input to signal the fault
event. The bidirectional mode is inhibited if the polarity bits are not correctly set (active high
polarity), for safety purposes.
The break software events (BG and B2G) also cause the break I/O to be forced to '0' to
indicate to the external components that the timer has entered in break state. However, this
is valid only if the break is enabled (BK(2)E = 1). When a software break event is generated
with BK(2)E = 0, the outputs are put in safe state and the break flag is set, but there is no
effect on the break(2) I/O.
A safe disarming mechanism prevents the system to be definitively locked-up (a low level on
the break input triggers a break which enforces a low level on the same input).
When the BKDSRM (BK2DSRM) bit is set to 1, this releases the break output to clear a fault
signal and to give the possibility to re-arm the system.
At no point the break protection circuitry can be disabled:
• The break input path is always active: a break event is active even if the BKDSRM
(BK2DSRM) bit is set and the open drain control is released. This prevents the PWM
output to be re-started as long as the break condition is present.
• The BK(2)DSRM bit cannot disarm the break protection as long as the outputs are
enabled (MOE bit is set) (see [Table 278](../tables/table_278.md))
MS34107V1
BRK
OCx
I/O state
Deadtime
Active Inactive Disabled
I/O state defined by the GPIO controller (HI-Z)
I/O state defined by the GPIO controller (HI-Z)

RM0438 Rev 8 1115/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Arming and re-arming break circuitry
The break circuitry (in input or bidirectional mode) is armed by default (peripheral reset
configuration).
The following procedure must be followed to re-arm the protection after a break (break2)
event:
• The BKDSRM (BK2DSRM) bit must be set to release the output control
• The software must wait until the system break condition disappears (if any) and clear
the SBIF status flag (or clear it systematically before re-arming)
• The software must poll the BKDSRM (BK2DSRM) bit until it is cleared by hardware
(when the application break condition disappears)
From this point, the break circuitry is armed and active, and the MOE bit can be set to re-
enable the PWM outputs.
[Figure 278](../figures/figure_278.md). Output redirection (BRK2 request not represented)
33.3.18 Clearing the OCxREF  signal on an external event
The OCxREF signal for a given channel can be reset by applying a high level on the ETRF
input (OCxCE enable bit set to 1 in the corresponding TIMx_CCMRx register). OCxREF
remains low until the next transition to the active state, on the following PWM cycle. This
[Table 278](../tables/table_278.md). Break protection disarming conditions
MOE BKDIR
(BK2DIR)
BKDSRM
(BK2DSRM) Break protection state
0 0 X Armed
0 1 0 Armed
0 1 1 Disarmed
1 X X Armed
MSv42028V2
BKIN inputs from
AF controller
BKF[3:0]
Filter
BKP
BKE
BRK
request
BIF flag
SBIF flagSystem break request
Peripheral
break sources
AF
controller
mode control logic
MOE BKBID BKBDSRM
BRK request
System break request
Bidirectional
Break I/O
Other break inputs
Application break requests
Vss
Bidirectional
AF input
(active low)
AF output
(open drain)
Software break
requests: BG

Advanced-control timers (TIM1/TIM8) RM0438
1116/2187 RM0438 Rev 8
function can be used only in the output compare and PWM modes. It does not work in
forced mode. For example, the OCxREF signal can be connected to the output of a
comparator to be used for current handling.
When ETRF is chosen, ETR must be configured as follows:
1. The External Trigger Prescaler should be kept off: bits ETPS[1:0] of the TIMx_SMCR
register set to ‘00’.
2. The external clock mode 2 must be disabl ed: bit ECE of the TIMx_SMCR register set to
‘0’.
3. The External Trigger Polarity (ETP) and the External Trigger Filter (ETF) can be
configured according to the user needs.
[Figure 279](../figures/figure_279.md) shows the behavior of the OCxREF signal when the ETRF Input becomes High,
for both values of the enable bit OCxCE. In this example, the timer TIMx is programmed in
PWM mode.
[Figure 279](../figures/figure_279.md). Clearing TIMx OCxREF
Note: In case of a PWM with a 100% duty cycle (i f CCRx>ARR), then OCxREF is enabled again at
the next counter overflow.
MS33105V2
(CCRx)
Counter (CNT)
ETRF
OCxREF
(OCxCE = ‘0’)
OCxREF
(OCxCE = ‘1’)
ocref_clr_int
becomes high
ocref_clr_int
still high

RM0438 Rev 8 1117/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.3.19 6-step PWM generation
When complementary outputs are used on a channel, preload bits are available on the
OCxM, CCxE and CCxNE bits. The preload bits are transferred to the shadow bits at the
COM commutation event. Thus one can program in advance the configuration for the next
step and change the configuration of all the channels at the same time. COM can be
generated by software by setting the COM bit in the TIMx_EGR register or by hardware (on
TRGI rising edge).
A flag is set when the COM event occurs (COMIF bit in the TIMx_SR register), which can
generate an interrupt (if the COMIE bit is set in the TIMx_DIER register) or a DMA request
(if the COMDE bit is set in the TIMx_DIER register).
The [Figure 280](../figures/figure_280.md) describes the behavior of the OCx and OCxN outputs when a COM event
occurs, in 3 different examples of programmed configurations.
[Figure 280](../figures/figure_280.md). 6-step generation, COM example (OSSR=1)

Advanced-control timers (TIM1/TIM8) RM0438
1118/2187 RM0438 Rev 8
33.3.20 One-pulse mode
One-pulse mode (OPM) is a particular case of the previous modes. It allows the counter to
be started in response to a stimulus and to generate a pulse with a programmable length
after a programmable delay.
Starting the counter can be controlled through the slave mode controller. Generating the
waveform can be done in output compare mode or PWM mode. One-pulse mode is selected
by setting the OPM bit in the TIMx_CR1 register. This makes the counter stop automatically
at the next update event UEV.
A pulse can be correctly generated only if the compare value is different from the counter
initial value. Before starting (when the timer is waiting for the trigger), the configuration must
be:
• In upcounting: CNT < CCRx ≤ ARR (in particular, 0 < CCRx)
• In downcounting: CNT > CCRx
[Figure 281](../figures/figure_281.md). Example of one pulse mode.
For example one may want to generate a positive pulse on OC1 with a length of tPULSE and
after a delay of tDELAY as soon as a positive edge is detected on the TI2 input pin.
Let’s use TI2FP2 as trigger 1:
1. Map TI2FP2 to TI2 by writing CC2S =’01’ in the TIMx_CCMR1 register.
2. TI2FP2 must detect a rising edge, writ e CC2P=’0’ and CC2NP=’0’ in the TIMx_CCER
register.
3. Configure TI2FP2 as trigger for the slave mode controller (TRGI) by writing TS=110 in
the TIMx_SMCR register.
4. TI2FP2 is used to start the counter by wr iting SMS to ‘110’ in the TIMx_SMCR register
(trigger mode).
MS31099V1
TI2
OC1REF
Counter
t
0
TIM1_ARR
TIM1_CCR1
OC1
tDELAY tPULSE

RM0438 Rev 8 1119/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
The OPM waveform is defined by writing the compare registers (taking into account the
clock frequency and the counter prescaler).
• The tDELAY is defined by the value written in the TIMx_CCR1 register.
• The tPULSE is defined by the difference between the auto-reload value and the compare
value (TIMx_ARR - TIMx_CCR1).
• Let’s say one want to build a waveform with a transition from ‘0’ to ‘1’ when a compare
match occurs and a transition from ‘1’ to ‘0’ when the counter reaches the auto-reload
value. To do this PWM mode 2 must be enabled by writing OC1M=111 in the
TIMx_CCMR1 register. Optionally the preload registers can be enabled by writing
OC1PE=’1’ in the TIMx_CCMR1 register and ARPE in the TIMx_CR1 register. In this
case one has to write the compare value in the TIMx_CCR1 register, the auto-reload
value in the TIMx_ARR register, generate an update by setting the UG bit and wait for
external trigger event on TI2. CC1P is written to ‘0’ in this example.
In our example, the DIR and CMS bits in the TIMx_CR1 register should be low.
Since only 1 pulse (Single mode) is needed, a 1 must be written in the OPM bit in the
TIMx_CR1 register to stop the counter at the next update event (when the counter rolls over
from the auto-reload value back to 0). When OPM bit in the TIMx_CR1 register is set to '0',
so the Repetitive Mode is selected.
Particular case: OCx fast enable:
In One-pulse mode, the edge detection on TIx input set the CEN bit which enables the
counter. Then the comparison between the counter and the compare value makes the
output toggle. But several clock cycles are needed for these operations and it limits the
minimum delay tDELAY min we can get.
If one wants to output a waveform with the minimum delay, the OCxFE bit can be set in the
TIMx_CCMRx register. Then OCxRef (and OCx) are forced in response to the stimulus,
without taking in account the comparison. Its new level is the same as if a compare match
had occurred. OCxFE acts only if the channel is configured in PWM1 or PWM2 mode.
33.3.21 Retriggerable one pulse mode
This mode allows the counter to be started in response to a stimulus and to generate a
pulse with a programmable length, but with the following differences with Non-retriggerable
one pulse mode described in Section 33.3.20:
– The pulse starts as soon as the trigger occurs (no programmable delay)
– The pulse is extended if a new trigger oc curs before the previous one is completed
The timer must be in Slave mode, with the bits SMS[3:0] = ‘1000’ (Combined Reset + trigger
mode) in the TIMx_SMCR register, and the OCxM[3:0] bits set to ‘1000’ or ‘1001’ for
retriggerable OPM mode 1 or 2.
If the timer is configured in Up-counting mode, the corresponding CCRx must be set to 0
(the ARR register sets the pulse length). If the timer is configured in Down-counting mode,
CCRx must be above or equal to ARR.
Note: The OCxM[3:0] and SMS[3:0] bit fields are split into two parts for compatibility reasons, the
most significant bit are not contiguous with the 3 least significant ones.
This mode must not be used with center-aligned PWM modes. It is mandatory to have
CMS[1:0] = 00 in TIMx_CR1.

Advanced-control timers (TIM1/TIM8) RM0438
1120/2187 RM0438 Rev 8
[Figure 282](../figures/figure_282.md). Retriggerable one pulse mode
33.3.22 Encoder interface mode
To select Encoder Interface mode write SMS=‘001’ in the TIMx_SMCR register if the
counter is counting on TI2 edges only, SMS=’010’ if it is counting on TI1 edges only and
SMS=’011’ if it is counting on both TI1 and TI2 edges.
Select the TI1 and TI2 polarity by programming the CC1P and CC2P bits in the TIMx_CCER
register. When needed, the input filter can be programmed as well. CC1NP and CC2NP
must be kept low.
The two inputs TI1 and TI2 are used to interface to a quadrature encoder. Refer to
[Table 279](../tables/table_279.md). The counter is clocked by each valid transition on TI1FP1 or TI2FP2 (TI1 and TI2
after input filter and polarity selection, TI1FP1=TI1 if not filtered and not inverted,
TI2FP2=TI2 if not filtered and not inverted) assuming that it is enabled (CEN bit in
TIMx_CR1 register written to ‘1’). The sequence of transitions of the two inputs is evaluated
and generates count pulses as well as the direction signal. Depending on the sequence the
counter counts up or down, the DIR bit in the TIMx_CR1 register is modified by hardware
accordingly. The DIR bit is calculated at each transition on any input (TI1 or TI2), whatever
the counter is counting on TI1 only, TI2 only or both TI1 and TI2.
Encoder interface mode acts simply as an external clock with direction selection. This
means that the counter just counts continuously between 0 and the auto-reload value in the
TIMx_ARR register (0 to ARR or ARR down to 0 depending on the direction). So the
TIMx_ARR must be configured before starting. In the same way, the capture, compare,
repetition counter, trigger output features continue to work as normal. Encoder mode and
External clock mode 2 are not compatible and must not be selected together.
Note: The prescaler must be set to zero when encoder mode is enabled
In this mode, the counter is modified automatically following the speed and the direction of
the quadrature encoder and its content, therefore, always represents the encoder’s position.
The count direction correspond to the rotation direction of the connected sensor. The table
summarizes the possible combinations, assuming TI1 and TI2 do not switch at the same
time.
MS33106V2
TRGI
Counter
Output

RM0438 Rev 8 1121/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
A quadrature encoder can be connected directly to the MCU without external interface logic.
However, comparators are normally be used to convert the encoder’s differential outputs to
digital signals. This greatly increases noise immunity. The third encoder output which
indicate the mechanical zero position, may be connected to an external interrupt input and
trigger a counter reset.
The [Figure 283](../figures/figure_283.md) gives an example of counter operation, showing count signal generation
and direction control. It also shows how input jitter is compensated where both edges are
selected. This might occur if the sensor is positioned near to one of the switching points. For
this example we assume that the configuration is the following:
• CC1S=’01’ (TIMx_CCMR1 register, TI1FP1 mapped on TI1).
• CC2S=’01’ (TIMx_CCMR1 register, TI2FP2 mapped on TI2)
• CC1P=’0’ and CC1NP=’0’ (TIMx_CCER register, TI1FP1 non-inverted, TI1FP1=TI1).
• CC2P=’0’ and CC2NP=’0’ (TIMx_CCER register, TI1FP2 non-inverted, TI1FP2= TI2).
• SMS=’011’ (TIMx_SMCR register, both inputs are active on both rising and falling
edges).
• CEN=’1’ (TIMx_CR1 register, Counter enabled).
[Figure 283](../figures/figure_283.md). Example of counter operation in encoder interface mode.
[Table 279](../tables/table_279.md). Counting direction versus encoder signals
Active edge
Level on
opposite
signal (TI1FP1
for TI2,
TI2FP2 for
TI1)
TI1FP1 signal TI2FP2 signal
Rising Falling Rising Falling
Counting on
TI1 only
High Down Up No Count No Count
Low Up Down No Count No Count
Counting on
TI2 only
High No Count No Count Up Down
Low No Count No Count Down Up
Counting on
TI1 and TI2
High Down Up Up Down
Low Up Down Down Up
TI1
backwardjitter jitter
up down up
TI2
Counter
forward forward
MS33107V1

Advanced-control timers (TIM1/TIM8) RM0438
1122/2187 RM0438 Rev 8
[Figure 284](../figures/figure_284.md) gives an example of counter behavior when TI1FP1 polarity is inverted (same
configuration as above except CC1P=’1’).
[Figure 284](../figures/figure_284.md). Example of encoder interface mode with TI1FP1 polarity inverted.
The timer, when configured in Encoder Interface mode provides information on the sensor’s
current position. Dynamic information can be obtained (speed, acceleration, deceleration)
by measuring the period between two encoder events using a second timer configured in
capture mode. The output of the encoder which indicates the mechanical zero can be used
for this purpose. Depending on the time between two events, the counter can also be read
at regular times. This can be done by latching the counter value into a third input capture
register if available (then the capture signal must be periodic and can be generated by
another timer). when available, it is also possible to read its value through a DMA request.
The IUFREMAP bit in the TIMx_CR1 register forces a continuous copy of the update
interrupt flag (UIF) into the timer counter register’s bit 31 (TIMxCNT[31]). This allows both
the counter value and a potential roll-over condition signaled by the UIFCPY flag to be read
in an atomic way. It eases the calculation of angular speed by avoiding race conditions
caused, for instance, by a processing shared between a background task (counter reading)
and an interrupt (update interrupt).
There is no latency between the UIF and UIFCPY flag assertions.
In 32-bit timer implementations, when the IUFREMAP bit is set, bit 31 of the counter is
overwritten by the UIFCPY flag upon read access (the counter’s most significant bit is only
accessible in write mode).
33.3.23 UIF bit remapping
The IUFREMAP bit in the TIMx_CR1 register forces a continuous copy of the Update
Interrupt Flag UIF into the timer counter register’s bit 31 (TIMxCNT[31]). This allows both
the counter value and a potential roll-over condition signaled by the UIFCPY flag to be read
in an atomic way. In particular cases, it can ease the calculations by avoiding race
conditions, caused for instance by a processing shared between a background task
(counter reading) and an interrupt (Update Interrupt).
There is no latency between the UIF and UIFCPY flags assertion.
TI1
backwardjitter jitter
updown
TI2
Counter
forward forward
MS33108V1
down

RM0438 Rev 8 1123/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.3.24 Timer input XOR function
The TI1S bit in the TIMx_CR2 register, allows the input filter of channel 1 to be connected to
the output of an XOR gate, combining the three input pins TIMx_CH1, TIMx_CH2 and
TIMx_CH3.
The XOR output can be used with all the timer input functions such as trigger or input
capture. It is convenient to measure the interval between edges on two input signals, as per
[Figure 285](../figures/figure_285.md) below.
[Figure 285](../figures/figure_285.md). Measuring time interval between edges on 3 signals
33.3.25 Interfacing with Hall sensors
This is done using the advanced-control timers (TIM1 or TIM8) to generate PWM signals to
drive the motor and another timer TIMx (TIM2, TIM3, TIM4) referred to as “interfacing timer”
in [Figure 286](../figures/figure_286.md). The “interfacing timer” captures the 3 timer input pins (CC1, CC2, CC3)
connected through a XOR to the TI1 input channel (selected by setting the TI1S bit in the
TIMx_CR2 register).
The slave mode controller is configured in reset mode; the slave input is TI1F_ED. Thus,
each time one of the 3 inputs toggles, the counter restarts counting from 0. This creates a
time base triggered by any change on the Hall inputs.
On the “interfacing timer”, capture/compare channel 1 is configured in capture mode,
capture signal is TRC (See [Figure 259](../figures/figure_259.md): Capture/compare channel (example: channel 1
input stage) on page 1094). The captured value, which corresponds to the time elapsed
between 2 changes on the inputs, gives information about motor speed.
The “interfacing timer” can be used in output mode to generate a pulse which changes the
configuration of the channels of the advanced-control timer (TIM1 or TIM8) (by triggering a
COM event). The TIM1 timer is used to generate PWM signals to drive the motor. To do this,
the interfacing timer channel must be programmed so that a positive pulse is generated
after a programmed delay (in output compare or PWM mode). This pulse is sent to the
advanced-control timer (TIM1 or TIM8) through the TRGO output.
MS33109V1
TI1
TI2
XOR
Counter
TI3
TIMx

Advanced-control timers (TIM1/TIM8) RM0438
1124/2187 RM0438 Rev 8
Example: one wants to change the PWM configuration of the advanced-control timer TIM1
after a programmed delay each time a change occurs on the Hall inputs connected to one of
the TIMx timers.
• Configure 3 timer inputs ORed to the TI1 input channel by writing the TI1S bit in the
TIMx_CR2 register to ‘1’,
• Program the time base: write the TIMx_ARR to the max value (the counter must be
cleared by the TI1 change. Set the prescaler to get a maximum counter period longer
than the time between 2 changes on the sensors,
• Program the channel 1 in capture mode (TRC selected): write the CC1S bits in the
TIMx_CCMR1 register to ‘11’. The digital filter can also be programmed if needed,
• Program the channel 2 in PWM 2 mode with the desired delay: write the OC2M bits to
‘111’ and the CC2S bits to ‘00’ in the TIMx_CCMR1 register,
• Select OC2REF as trigger output on TRGO: write the MMS bits in the TIMx_CR2
register to ‘101’,
In the advanced-control timer TIM1, the right ITR input must be selected as trigger input, the
timer is programmed to generate PWM signals, the capture/compare control signals are
preloaded (CCPC=1 in the TIMx_CR2 register) and the COM event is controlled by the
trigger input (CCUS=1 in the TIMx_CR2 register). The PWM control bits (CCxE, OCxM) are
written after a COM event for the next step (this can be done in an interrupt subroutine
generated by the rising edge of OC2REF).
The [Figure 286](../figures/figure_286.md) describes this example.

RM0438 Rev 8 1125/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
[Figure 286](../figures/figure_286.md). Example of Hall sensor interface

Advanced-control timers (TIM1/TIM8) RM0438
1126/2187 RM0438 Rev 8
33.3.26 Timer synchronization
The TIMx timers are linked together internally for timer synchronization or chaining. Refer to
Section 34.3.19: Timer synchronization for details. They can be synchronized in several
modes: Reset mode, Gated mode, and Trigger mode.
Slave mode: Reset mode
The counter and its prescaler can be reinitialized in response to an event on a trigger input.
Moreover, if the URS bit from the TIMx_CR1 register is low, an update event UEV is
generated. Then all the preloaded registers (TIMx_ARR, TIMx_CCRx) are updated.
In the following example, the upcounter is cleared in response to a rising edge on TI1 input:
• Configure the channel 1 to detect rising edges on TI1. Configure the input filter duration
(in this example, we do not need any filter, so we keep IC1F=0000). The capture
prescaler is not used for triggering, so it does not need to be configured. The CC1S bits
select the input capture source only, CC1S = 01 in the TIMx_CCMR1 register. Write
CC1P=0 and CC1NP=’0’ in TIMx_CCER register to validate the polarity (and detect
rising edges only).
• Configure the timer in reset mode by writing SMS=100 in TIMx_SMCR register. Select
TI1 as the input source by writing TS=101 in TIMx_SMCR register.
• Start the counter by writing CEN=1 in the TIMx_CR1 register.
The counter starts counting on the internal clock, then behaves normally until TI1 rising
edge. When TI1 rises, the counter is cleared and restarts from 0. In the meantime, the
trigger flag is set (TIF bit in the TIMx_SR register) and an interrupt request, or a DMA
request can be sent if enabled (depending on the TIE and TDE bits in TIMx_DIER register).
The following figure shows this behavior when the auto-reload register TIMx_ARR=0x36.
The delay between the rising edge on TI1 and the actual reset of the counter is due to the
resynchronization circuit on TI1 input.
[Figure 287](../figures/figure_287.md). Control circuit in reset mode
MS31401V1
00
Counter clock = ck_cnt = ck_psc
Counter register 01 02 03 00 01 02 0332 33 34 35 36
UG
TI1
3130
TIF

RM0438 Rev 8 1127/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Slave mode: Gated mode
The counter can be enabled depending on the level of a selected input.
In the following example, the upcounter counts only when TI1 input is low:
• Configure the channel 1 to detect low levels on TI1. Configure the input filter duration
(in this example, we do not need any filter, so we keep IC1F=0000). The capture
prescaler is not used for triggering, so it does not need to be configured. The CC1S bits
select the input capture source only, CC1S=01 in TIMx_CCMR1 register. Write
CC1P=1 and CC1NP=’0’ in TIMx_CCER register to validate the polarity (and detect
low level only).
• Configure the timer in gated mode by writing SMS=101 in TIMx_SMCR register. Select
TI1 as the input source by writing TS=101 in TIMx_SMCR register.
• Enable the counter by writing CEN=1 in the TIMx_CR1 register (in gated mode, the
counter doesn’t start if CEN=0, whatever is the trigger input level).
The counter starts counting on the internal clock as long as TI1 is low and stops as soon as
TI1 becomes high. The TIF flag in the TIMx_SR register is set both when the counter starts
or stops.
The delay between the rising edge on TI1 and the actual stop of the counter is due to the
resynchronization circuit on TI1 input.
[Figure 288](../figures/figure_288.md). Control circuit in Gated mode
Slave mode: Trigger mode
The counter can start in response to an event on a selected input.
In the following example, the upcounter starts in response to a rising edge on TI2 input:
• Configure the channel 2 to detect rising edges on TI2. Configure the input filter duration
(in this example, we do not need any filter, so we keep IC2F=0000). The capture
prescaler is not used for triggering, so it does not need to be configured. The CC2S bits
are configured to select the input capture source only, CC2S=01 in TIMx_CCMR1
MS31402V1
TI1
cnt_en
Write TIF=0
37
Counter clock = ck_cnt = ck_psc
Counter register 3832 33 34 35 363130
TIF

Advanced-control timers (TIM1/TIM8) RM0438
1128/2187 RM0438 Rev 8
register. Write CC2P=1 and CC2NP=0 in TIMx_CCER register to validate the polarity
(and detect low level only).
• Configure the timer in trigger mode by writing SMS=110 in TIMx_SMCR register. Select
TI2 as the input source by writing TS=110 in TIMx_SMCR register.
When a rising edge occurs on TI2, the counter starts counting on the internal clock and the
TIF flag is set.
The delay between the rising edge on TI2 and the actual start of the counter is due to the
resynchronization circuit on TI2 input.
[Figure 289](../figures/figure_289.md). Control circuit in trigger mode
Slave mode: Combined reset + trigger mode
In this case, a rising edge of the selected trigger input (TRGI) reinitializes the counter,
generates an update of the registers, and starts the counter.
This mode is used for one-pulse mode.
Slave mode: external clock mode 2 + trigger mode
The external clock mode 2 can be used in addition to another slave mode (except external
clock mode 1 and encoder mode). In this case, the ETR signal is used as external clock
input, and another input can be selected as trigger input (in reset mode, gated mode or
trigger mode). It is recommended not to select ETR as TRGI through the TS bits of
TIMx_SMCR register.
MS31403V1
TI2
cnt_en
37
Counter clock = ck_cnt = ck_psc
Counter register 3834 35 36
TIF

RM0438 Rev 8 1129/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
In the following example, the upcounter is incremented at each rising edge of the ETR
signal as soon as a rising edge of TI1 occurs:
1. Configure the external trigger input circui t by programming the TIMx_SMCR register as
follows:
– ETF = 0000: no filter
– ETPS = 00: prescaler disabled
– ETP = 0: detection of rising edges on ET R and ECE=1 to enable the external clock
mode 2.
2. Configure the channel 1 as follows , to detect rising edges on TI:
– IC1F = 0000: no filter.
– The capture prescaler is not used for triggering and does not need to be
configured.
– CC1S = 01 in TIMx_CCMR1 register to select only the input capture source
– CC1P = 0 and CC1NP = 0 in TIMx_CCER register to validate the polarity (and
detect rising edge only).
3. Configure the timer in trigger mode by wr iting SMS=110 in TIMx_SMCR register. Select
TI1 as the input source by writing TS=101 in TIMx_SMCR register.
A rising edge on TI1 enables the counter and sets the TIF flag. The counter then counts on
ETR rising edges.
The delay between the rising edge of the ETR signal and the actual reset of the counter is
due to the resynchronization circuit on ETRP input.
[Figure 290](../figures/figure_290.md). Control circuit in external clock mode 2 + trigger mode
Note: The clock of the slave peripherals (timer , ADC, ...) receiving the TRGO or the TRGO2
signals must be enabled prior to receive events from the master timer, and the clock
frequency (prescaler) must not be changed on-the-fly while triggers are received from the
master timer.
MS33110V1
34 35 36
TIF
Counter register
Counter clock = CK_CNT = CK_PSC
ETR
CEN/CNT_EN
TI1

Advanced-control timers (TIM1/TIM8) RM0438
1130/2187 RM0438 Rev 8
33.3.27 ADC synchronization
The timer can generate an ADC triggering event with various internal signals, such as reset,
enable or compare events. It is also possible to generate a pulse issued by internal edge
detectors, such as:
– Rising and falling edges of OC4ref
– Rising edge on OC5ref or falling edge on OC6ref
The triggers are issued on the TRGO2 internal line which is redirected to the ADC. There is
a total of 16 possible events, which can be selected using the MMS2[3:0] bits in the
TIMx_CR2 register.
An example of an application for 3-phase motor drives is given in [Figure 270](../figures/figure_270.md) on page 1106.
Note: The clock of the slave peripherals (timer , ADC, ...) receiving the TRGO or the TRGO2
signals must be enabled prior to receive events from the master timer, and the clock
frequency (prescaler) must not be changed on-the-fly while triggers are received from the
master timer.
Note: The clock of the ADC must be enabled prior to receive events from the master timer, and
must not be changed on-the-fly while triggers are received from the timer.
33.3.28 DMA burst mode
The TIMx timers have the capability to generate multiple DMA requests upon a single event.
The main purpose is to be able to re-program part of the timer multiple times without
software overhead, but it can also be used to read several registers in a row, at regular
intervals.
The DMA controller destination is unique and must point to the virtual register TIMx_DMAR.
On a given timer event, the timer launches a sequence of DMA requests (burst). Each write
into the TIMx_DMAR register is actually redirected to one of the timer registers.
The DBL[4:0] bits in the TIMx_DCR register set the DMA burst length. The timer recognizes
a burst transfer when a read or a write access is done to the TIMx_DMAR address), i.e. the
number of transfers (either in half-words or in bytes).
The DBA[4:0] bits in the TIMx_DCR registers define the DMA base address for DMA
transfers (when read/write access are done through the TIMx_DMAR address). DBA is
defined as an offset starting from the address of the TIMx_CR1 register:
Example:
00000: TIMx_CR1
00001: TIMx_CR2
00010: TIMx_SMCR
As an example, the timer DMA burst feature is used to update the contents of the CCRx
registers (x = 2, 3, 4) upon an update event, with the DMA transferring half words into the
CCRx registers.

RM0438 Rev 8 1131/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
This is done in the following steps:
1. Configure the corresponding DMA channel as follows:
– DMA channel peripheral address is the DMAR register address
– DMA channel memory address is the address of the buffer in the RAM containing
the data to be transferred by DMA into CCRx registers.
– Number of data to transfer = 3 (See note below).
– Circular mode disabled.
2. Configure the DCR register by configur ing the DBA and DBL bit fields as follows:
DBL = 3 transfers, DBA = 0xE.
3. Enable the TIMx update DMA request (s et the UDE bit in the DIER register).
4. Enable TIMx
5. Enable the DMA channel
This example is for the case where every CCRx register to be updated once. If every CCRx
register is to be updated twice for example, the number of data to transfer should be 6. Let's
take the example of a buffer in the RAM containing data1, data2, data3, data4, data5 and
data6. The data is transferred to the CCRx registers as follows: on the first update DMA
request, data1 is transferred to CCR2, data2 is transferred to CCR3, data3 is transferred to
CCR4 and on the second update DMA request, data4 is transferred to CCR2, data5 is
transferred to CCR3 and data6 is transferred to CCR4.
Note: A null value can be written to the reserved registers.
33.3.29 Debug mode
When the microcontroller enters debug mode (Cortex®-M33 core halted), the TIMx counter
either continues to work normally or stops, depending on DBG_TIMx_STOP configuration
bit in DBG module.
For safety purposes, when the counter is stopped, the outputs are disabled (as if the MOE
bit was reset). The outputs can either be forced to an inactive state (OSSI bit = 1), or have
their control taken over by the GPIO controller (OSSI bit = 0), typically to force a Hi-Z.
For more details, refer to section Debug support (DBG).

Advanced-control timers (TIM1/TIM8) RM0438
1132/2187 RM0438 Rev 8
33.4 TIM1/TIM8 registers
Refer to for a list of abbreviations used in register descriptions.
The peripheral registers can be accessed by half-words (16-bit) or words (32-bit).
33.4.1 TIMx control regist er 1 (TIMx_CR1)(x = 1, 8)
Address offset: 0x00
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. UIFRE
MAP Res. CKD[1:0] ARPE CMS[1:0] DIR OPM URS UDIS CEN
rw rw rw rw rw rw rw rw rw rw rw
Bits 15:12 Reserved, must be kept at reset value.
Bit 11 UIFREMAP: UIF status bit remapping
0: No remapping. UIF status bit is not copied to TIMx_CNT register bit 31.
1: Remapping enabled. UIF status bit is copied to TIMx_CNT register bit 31.
Bit 10 Reserved, must be kept at reset value.
Bits 9:8 CKD[1:0]: Clock division
This bit-field indicates the division ratio between the timer clock (CK_INT) frequency and the
dead-time and sampling clock (tDTS)used by the dead-time generators and the digital filters
(ETR, TIx):
00: tDTS=tCK_INT
01: tDTS=2*tCK_INT
10: tDTS=4*tCK_INT
11: Reserved, do not program this value
Note: t DTS = 1/fDTS, tCK_INT = 1/fCK_INT.
Bit 7 ARPE: Auto-reload preload enable
0: TIMx_ARR register is not buffered
1: TIMx_ARR register is buffered
Bits 6:5 CMS[1:0]: Center-aligned mode selection
00: Edge-aligned mode. The counter counts up or down depending on the direction bit
(DIR).
01: Center-aligned mode 1. The counter counts up and down alternatively. Output compare
interrupt flags of channels configured in output (CCxS=00 in TIMx_CCMRx register) are
set only when the counter is counting down.
10: Center-aligned mode 2. The counter counts up and down alternatively. Output compare
interrupt flags of channels configured in output (CCxS=00 in TIMx_CCMRx register) are
set only when the counter is counting up.
11: Center-aligned mode 3. The counter counts up and down alternatively. Output compare
interrupt flags of channels configured in output (CCxS=00 in TIMx_CCMRx register) are
set both when the counter is counting up or down.
Note: Switch from edge-aligned mode to center-aligned mode as long as the counter is
enabled (CEN=1) is not allowed

RM0438 Rev 8 1133/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.4.2 TIMx control regist er 2 (TIMx_CR2)(x = 1, 8)
Address offset: 0x04
Reset value: 0x0000 0000
Bit 4 DIR: Direction
0: Counter used as upcounter
1: Counter used as downcounter
Note: This bit is read only when the timer is configured in Center-aligned mode or Encoder
mode.
Bit 3 OPM: One pulse mode
0: Counter is not stopped at update event
1: Counter stops counting at the next update event (clearing the bit CEN)
Bit 2 URS: Update request source
This bit is set and cleared by software to select the UEV event sources.
0: Any of the following events generate an update interrupt or DMA request if enabled.
These events can be:
– Counter overflow/underflow
– Setting the UG bit
– Update generation through the slave mode controller
1: Only counter overflow/underflow generates an update interrupt or DMA request if
enabled.
Bit 1 UDIS: Update disable
This bit is set and cleared by software to enable/disable UEV event generation.
0: UEV enabled. The Update (UEV) event is generated by one of the following events:
– Counter overflow/underflow
– Setting the UG bit
– Update generation through the slave mode controller
Buffered registers are then loaded with their preload values.
1: UEV disabled. The Update event is not generated, shadow registers keep their value
(ARR, PSC, CCRx). However the counter and the prescaler are reinitialized if the UG bit
is set or if a hardware reset is received from the slave mode controller.
Bit 0 CEN: Counter enable
0: Counter disabled
1: Counter enabled
Note: External clock, gated mode and encoder mode can work only if the CEN bit has been
previously set by software. However trigger mode can set the CEN bit automatically by
hardware.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. MMS2[3:0] Res. OIS6 Res. OIS5
rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. OIS4 OIS3N OIS3 OIS2N OIS2 OIS1N OIS1 TI1S MMS[2:0] CCDS CCUS Res. CCPC
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:24 Reserved, must be kept at reset value.

Advanced-control timers (TIM1/TIM8) RM0438
1134/2187 RM0438 Rev 8
Bits 23:20 MMS2[3:0]: Master mode selection 2
These bits allow the information to be sent to ADC for synchronization (TRGO2) to be
selected. The combination is as follows:
0000: Reset - the UG bit from the TIMx_EGR register is used as trigger output (TRGO2). If
the reset is generated by the trigger input (slave mode controller configured in reset
mode), the signal on TRGO2 is delayed compared to the actual reset.
0001: Enable - the Counter Enable signal CNT_EN is used as trigger output (TRGO2). It is
useful to start several timers at the same time or to control a window in which a slave
timer is enabled. The Counter Enable signal is generated by a logic AND between the
CEN control bit and the trigger input when configured in Gated mode. When the
Counter Enable signal is controlled by the trigger input, there is a delay on TRGO2,
except if the Master/Slave mode is selected (see the MSM bit description in
TIMx_SMCR register).
0010: Update - the update event is selected as trigger output (TRGO2). For instance, a
master timer can then be used as a prescaler for a slave timer.
0011: Compare pulse - the trigger output sends a positive pulse when the CC1IF flag is to
be set (even if it was already high), as soon as a capture or compare match occurs
(TRGO2).
0100: Compare - OC1REFC signal is used as trigger output (TRGO2)
0101: Compare - OC2REFC signal is used as trigger output (TRGO2)
0110: Compare - OC3REFC signal is used as trigger output (TRGO2)
0111: Compare - OC4REFC signal is used as trigger output (TRGO2)
1000: Compare - OC5REFC signal is used as trigger output (TRGO2)
1001: Compare - OC6REFC signal is used as trigger output (TRGO2)
1010: Compare Pulse - OC4REFC rising or falling edges generate pulses on TRGO2
1011: Compare Pulse - OC6REFC rising or falling edges generate pulses on TRGO2
1100: Compare Pulse - OC4REFC or OC6REFC rising edges generate pulses on TRGO2
1101: Compare Pulse - OC4REFC rising or OC6REFC falling edges generate pulses on
TRGO2
1110: Compare Pulse - OC5REFC or OC6REFC rising edges generate pulses on TRGO2
1111: Compare Pulse - OC5REFC rising or OC6REFC falling edges generate pulses on
TRGO2
Note: The clock of the slave timer or ADC must  be enabled prior to receive events from the
master timer, and must not be changed on-the-fly while triggers are received from the
master timer.
Bit 19 Reserved, must be kept at reset value.
Bit 18 OIS6: Output Idle state 6 (OC6 output)
Refer to OIS1 bit
Bit 17 Reserved, must be kept at reset value.
Bit 16 OIS5: Output Idle state 5 (OC5 output)
Refer to OIS1 bit
Bit 15 Reserved, must be kept at reset value.
Bit 14 OIS4: Output Idle state 4 (OC4 output)
Refer to OIS1 bit
Bit 13 OIS3N: Output Idle state 3 (OC3N output)
Refer to OIS1N bit
Bit 12 OIS3: Output Idle state 3 (OC3 output)
Refer to OIS1 bit

RM0438 Rev 8 1135/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Bit 11 OIS2N: Output Idle state 2 (OC2N output)
Refer to OIS1N bit
Bit 10 OIS2: Output Idle state 2 (OC2 output)
Refer to OIS1 bit
Bit 9 OIS1N: Output Idle state 1 (OC1N output)
0: OC1N=0 after a dead-time when MOE=0
1: OC1N=1 after a dead-time when MOE=0
Note: This bit can not be modified as long as LOCK level 1, 2 or 3 has been programmed
(LOCK bits in TIMx_BDTR register).
Bit 8 OIS1: Output Idle state 1 (OC1 output)
0: OC1=0 (after a dead-time if OC1N is implemented) when MOE=0
1: OC1=1 (after a dead-time if OC1N is implemented) when MOE=0
Note: This bit can not be modified as long as LOCK level 1, 2 or 3 has been programmed
(LOCK bits in TIMx_BDTR register).
Bit 7 TI1S: TI1 selection
0: The TIMx_CH1 pin is connected to TI1 input
1: The TIMx_CH1, CH2 and CH3 pins are connected to the TI1 input (XOR combination)
Bits 6:4 MMS[2:0]: Master mode selection
These bits allow selected information to be sent in master mode to slave timers for
synchronization (TRGO). The combination is as follows:
000: Reset - the UG bit from the TIMx_EGR register is used as trigger output (TRGO). If the
reset is generated by the trigger input (slave mode controller configured in reset mode)
then the signal on TRGO is delayed compared to the actual reset.
001: Enable - the Counter Enable signal CNT_EN is used as trigger output (TRGO). It is
useful to start several timers at the same time or to control a window in which a slave
timer is enable. The Counter Enable signal is generated by a logic AND between CEN
control bit and the trigger input when configured in gated mode. When the Counter
Enable signal is controlled by the trigger input, there is a delay on TRGO, except if the
master/slave mode is selected (see the MSM bit description in TIMx_SMCR register).
010: Update - The update event is selected as trigger output (TRGO). For instance a master
timer can then be used as a prescaler for a slave timer.
011: Compare Pulse - The trigger output send a positive pulse when the CC1IF flag is to be
set (even if it was already high), as soon as a capture or a compare match occurred.
(TRGO).
100: Compare - OC1REFC signal is used as trigger output (TRGO)
101: Compare - OC2REFC signal is used as trigger output (TRGO)
110: Compare - OC3REFC signal is used as trigger output (TRGO)
111: Compare - OC4REFC signal is used as trigger output (TRGO)
Note: The clock of the slave timer or ADC must  be enabled prior to receive events from the
master timer, and must not be changed on-the-fly while triggers are received from the
master timer.
Bit 3 CCDS: Capture/compare DMA selection
0: CCx DMA request sent when CCx event occurs
1: CCx DMA requests sent when update event occurs

Advanced-control timers (TIM1/TIM8) RM0438
1136/2187 RM0438 Rev 8
33.4.3 TIMx slave m ode control register
(TIMx_SMCR)(x = 1, 8)
Address offset: 0x08
Reset value: 0x0000 0000
Bit 2 CCUS: Capture/compare control update selection
0: When capture/compare control bits are preloaded (CCPC=1), they are updated by setting
the COMG bit only
1: When capture/compare control bits are preloaded (CCPC=1), they are updated by setting
the COMG bit or when an rising edge occurs on TRGI
Note: This bit acts only on channels that have a complementary output.
Bit 1 Reserved, must be kept at reset value.
Bit 0 CCPC: Capture/compare preloaded control
0: CCxE, CCxNE and OCxM bits are not preloaded
1: CCxE, CCxNE and OCxM bits are preloaded, after having been written, they are updated
only when a commutation event (COM) occurs (COMG bit set or rising edge detected on
TRGI, depending on the CCUS bit).
Note: This bit acts only on channels that have a complementary output.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. SMS[3]
rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
ETP ECE ETPS[1:0] ETF[3:0] MSM TS[2:0] Res. SMS[2:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:17 Reserved, must be kept at reset value.
Bit 15 ETP: External trigger polarity
This bit selects whether ETR or ETR is used for trigger operations
0: ETR is non-inverted, active at high level or rising edge.
1: ETR is inverted, active at low level or falling edge.
Bit 14 ECE: External clock enable
This bit enables External clock mode 2.
0: External clock mode 2 disabled
1: External clock mode 2 enabled. The counter is clocked by any active edge on the ETRF
signal.
Note: Setting the ECE bit has the same effect as selecting external clock mode 1 with TRGI
connected to ETRF (SMS=111 and TS=111).
It is possible to simultaneously use external clock mode 2 with the following slave
modes: reset mode, gated mode and trigger mode. Nevertheless, TRGI must not be
connected to ETRF in this case (TS bits must not be 111).
If external clock mode 1 and external clock mode 2 are enabled at the same time, the
external clock input is ETRF.

RM0438 Rev 8 1137/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Bits 13:12 ETPS[1:0]: External trigger prescaler
External trigger signal ETRP frequency must be at most 1/4 of fCK_INT frequency. A
prescaler can be enabled to reduce ETRP frequency. It is useful when inputting fast external
clocks.
00: Prescaler OFF
01: ETRP frequency divided by 2
10: ETRP frequency divided by 4
11: ETRP frequency divided by 8
Bits 11:8 ETF[3:0]: External trigger filter
This bit-field then defines the frequency used to sample ETRP signal and the length of the
digital filter applied to ETRP. The digital filter is made of an event counter in which N
consecutive events are needed to validate a transition on the output:
0000: No filter, sampling is done at fDTS
0001: fSAMPLING=fCK_INT, N=2
0010: fSAMPLING=fCK_INT, N=4
0011: fSAMPLING=fCK_INT, N=8
0100: fSAMPLING=fDTS/2, N=6
0101: fSAMPLING=fDTS/2, N=8
0110: fSAMPLING=fDTS/4, N=6
0111: fSAMPLING=fDTS/4, N=8
1000: fSAMPLING=fDTS/8, N=6
1001: fSAMPLING=fDTS/8, N=8
1010: fSAMPLING=fDTS/16, N=5
1011: fSAMPLING=fDTS/16, N=6
1100: fSAMPLING=fDTS/16, N=8
1101: fSAMPLING=fDTS/32, N=5
1110: fSAMPLING=fDTS/32, N=6
1111: fSAMPLING=fDTS/32, N=8
Bit 7 MSM: Master/slave mode
0: No action
1: The effect of an event on the trigger input (TRGI) is delayed to allow a perfect
synchronization between the current timer and its slaves (through TRGO). It is useful if
we want to synchronize several timers on a single external event.
Bits 6:4 TS[2:0]: Trigger selection
This bit-field selects the trigger input to be used to synchronize the counter.
000: Internal Trigger 0 (ITR0)
001: Internal Trigger 1 (ITR1)
010: Internal Trigger 2 (ITR2)
011: Internal Trigger 3 (ITR3)
100: TI1 Edge Detector (TI1F_ED)
101: Filtered Timer Input 1 (TI1FP1)
110: Filtered Timer Input 2 (TI2FP2)
111: External Trigger input (ETRF)
See [Table 280](../tables/table_280.md): TIMx internal trigger connection on page 1138 for more details on ITRx
meaning for each Timer.
Note: These bits must be changed only when they are not used (e.g. when SMS=000) to
avoid wrong edge detections at the transition.
Note: The other bit is at position 16 in the same register
Bit 3 Reserved, must be kept at reset value.

Advanced-control timers (TIM1/TIM8) RM0438
1138/2187 RM0438 Rev 8
33.4.4 TIMx DMA/interrupt enable register
(TIMx_DIER)(x = 1, 8)
Address offset: 0x0C
Reset value: 0x0000
Bits 16, 2, 1, 0 SMS[3:0]: Slave mode selection
When external signals are selected the active edge of the trigger signal (TRGI) is linked to
the polarity selected on the external input (refer to ETP bit in TIMx_SMCR for tim_etr_in and
CCxP/CCxNP bits in TIMx_CCER register for tim_ti1fp1 and tim_ti2fp2).
0000: Slave mode disabled - if CEN = ‘1’ then the prescaler is clocked directly by the internal
clock.
0001: Encoder mode 1 - Counter counts up/down on TI1FP1 edge depending on TI2FP2
level.
0010: Encoder mode 2 - Counter counts up/down on TI2FP2 edge depending on TI1FP1
level.
0011: Encoder mode 3 - Counter counts up/down on both TI1FP1 and TI2FP2 edges
depending on the level of the other input.
0100: Reset Mode - Rising edge of the selected trigger input (TRGI) reinitializes the counter
and generates an update of the registers.
0101: Gated Mode - The counter clock is enabled when the trigger input (TRGI) is high. The
counter stops (but is not reset) as soon as the trigger becomes low. Both start and stop of
the counter are controlled.
0110: Trigger Mode - The counter starts at a rising edge of the trigger TRGI (but it is not
reset). Only the start of the counter is controlled.
0111: External Clock Mode 1 - Rising edges of the selected trigger (TRGI) clock the counter.
1000: Combined reset + trigger mode - Rising edge of the selected trigger input (TRGI)
reinitializes the counter, generates an update of the registers and starts the counter.
Codes above 1000: Reserved.
Note: The gated mode must not be used if TI1F_E D is selected as the trigger input (TS=100).
Indeed, TI1F_ED outputs 1 pulse for each transition on TI1F, whereas the gated mode
checks the level of the trigger signal.
Note: The clock of the slave peripherals (timer, ADC, ...) receiving the TRGO or the TRGO2
signals must be enabled prior to receive events from the master timer, and the clock
frequency (prescaler) must not be changed on-the-fly while triggers are received from
the master timer.
[Table 280](../tables/table_280.md). TIMx internal trigger connection
Slave TIM ITR0 (TS = 000) ITR1 (TS = 001) ITR2 (TS = 010) ITR3 (TS = 011)
TIM1 TIM15 TIM2 TIM3 TIM4
TIM8 TIM1 TIM2 TIM4 TIM5
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. TDE COMDE CC4DE CC3DE CC2DE CC1DE UDE BIE TIE COMIE CC4IE CC3IE CC2IE CC1IE UIE
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 15 Reserved, must be kept at reset value.
Bit 14 TDE: Trigger DMA request enable
0: Trigger DMA request disabled
1: Trigger DMA request enabled

RM0438 Rev 8 1139/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Bit 13 COMDE: COM DMA request enable
0: COM DMA request disabled
1: COM DMA request enabled
Bit 12 CC4DE: Capture/Compare 4 DMA request enable
0: CC4 DMA request disabled
1: CC4 DMA request enabled
Bit 11 CC3DE: Capture/Compare 3 DMA request enable
0: CC3 DMA request disabled
1: CC3 DMA request enabled
Bit 10 CC2DE: Capture/Compare 2 DMA request enable
0: CC2 DMA request disabled
1: CC2 DMA request enabled
Bit 9 CC1DE: Capture/Compare 1 DMA request enable
0: CC1 DMA request disabled
1: CC1 DMA request enabled
Bit 8 UDE: Update DMA request enable
0: Update DMA request disabled
1: Update DMA request enabled
Bit 7 BIE: Break interrupt enable
0: Break interrupt disabled
1: Break interrupt enabled
Bit 6 TIE: Trigger interrupt enable
0: Trigger interrupt disabled
1: Trigger interrupt enabled
Bit 5 COMIE: COM interrupt enable
0: COM interrupt disabled
1: COM interrupt enabled
Bit 4 CC4IE: Capture/Compare 4 interrupt enable
0: CC4 interrupt disabled
1: CC4 interrupt enabled
Bit 3 CC3IE: Capture/Compare 3 interrupt enable
0: CC3 interrupt disabled
1: CC3 interrupt enabled
Bit 2 CC2IE: Capture/Compare 2 interrupt enable
0: CC2 interrupt disabled
1: CC2 interrupt enabled
Bit 1 CC1IE: Capture/Compare 1 interrupt enable
0: CC1 interrupt disabled
1: CC1 interrupt enabled
Bit 0 UIE: Update interrupt enable
0: Update interrupt disabled
1: Update interrupt enabled

Advanced-control timers (TIM1/TIM8) RM0438
1140/2187 RM0438 Rev 8
33.4.5 TIMx status regist er (TIMx_SR)(x = 1, 8)
Address offset: 0x10
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CC6IF CC5IF
rc_w0 rc_w0
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. SBIF CC4OF CC3OF CC2OF CC1OF B2IF BIF TIF COMIF CC4IF CC3IF CC2IF CC1IF UIF
rc_w0 rc_w0 rc_w0 rc_w0 rc_w0 rc_w0 rc_w0 rc_w0 rc_w0 rc_w0 rc_w0 rc_w0 rc_w0 rc_w0
Bits 31:18 Reserved, must be kept at reset value.
Bit 17 CC6IF: Compare 6 interrupt flag
Refer to CC1IF description (Note: Channel 6 can only be configured as output)
Bit 16 CC5IF: Compare 5 interrupt flag
Refer to CC1IF description (Note: Channel 5 can only be configured as output)
Bits 15:14 Reserved, must be kept at reset value.
Bit 13 SBIF: System Break interrupt flag
This flag is set by hardware as soon as the system break input goes active. It can be
cleared by software if the system break input is not active.
This flag must be reset to re-start PWM operation.
0: No break event occurred.
1: An active level has been detected on the system break input. An interrupt is generated if
BIE=1 in the TIMx_DIER register.
Bit 12 CC4OF: Capture/Compare 4 overcapture flag
Refer to CC1OF description
Bit 11 CC3OF: Capture/Compare 3 overcapture flag
Refer to CC1OF description
Bit 10 CC2OF: Capture/Compare 2 overcapture flag
Refer to CC1OF description
Bit 9 CC1OF: Capture/Compare 1 overcapture flag
This flag is set by hardware only when the corresponding channel is configured in input
capture mode. It is cleared by software by writing it to ‘0’.
0: No overcapture has been detected.
1: The counter value has been captured in TIMx_CCR1 register while CC1IF flag was
already set
Bit 8 B2IF: Break 2 interrupt flag
This flag is set by hardware as soon as the break 2 input goes active. It can be cleared by
software if the break 2 input is not active.
0: No break event occurred.
1: An active level has been detected on the break 2 input. An interrupt is generated if BIE=1
in the TIMx_DIER register.

RM0438 Rev 8 1141/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Bit 7 BIF: Break interrupt flag
This flag is set by hardware as soon as the break input goes active. It can be cleared by
software if the break input is not active.
0: No break event occurred.
1: An active level has been detected on the break input. An interrupt is generated if BIE=1 in
the TIMx_DIER register.
Bit 6 TIF: Trigger interrupt flag
This flag is set by hardware on the TRG trigger event (active edge detected on TRGI input
when the slave mode controller is enabled in all modes but gated mode. It is set when the
counter starts or stops when gated mode is selected. It is cleared by software.
0: No trigger event occurred.
1: Trigger interrupt pending.
Bit 5 COMIF: COM interrupt flag
This flag is set by hardware on COM event (when Capture/compare Control bits - CCxE,
CCxNE, OCxM - have been updated). It is cleared by software.
0: No COM event occurred.
1: COM interrupt pending.
Bit 4 CC4IF: Capture/Compare 4 interrupt flag
Refer to CC1IF description
Bit 3 CC3IF: Capture/Compare 3 interrupt flag
Refer to CC1IF description
Bit 2 CC2IF: Capture/Compare 2 interrupt flag
Refer to CC1IF description
Bit 1 CC1IF: Capture/Compare 1 interrupt flag
This flag is set by hardware. It is cleared by software (input capture or output compare
mode) or by reading the TIMx_CCR1 register (input capture mode only).
0: No compare match / No input capture occurred
1: A compare match or an input capture occurred.
If channel CC1 is configured as output: this flag is set when the content of the counter
TIMx_CNT matches the content of the TIMx_CCR1 register. When the content of
TIMx_CCR1 is greater than the content of TIMx_ARR, the CC1IF bit goes high on the
counter overflow (in up-counting and up/down-counting modes) or underflow (in down-
counting mode). There are 3 possible options for flag setting in center-aligned mode, refer
to the CMS bits in the TIMx_CR1 register for the full description.
If channel CC1 is configured as input: this bit is set when counter value has been
captured in TIMx_CCR1 register (an edge has been detected on IC1, as per the edge
sensitivity defined with the CC1P and CC1NP bits setting, in TIMx_CCER).
Bit 0 UIF: Update interrupt flag
This bit is set by hardware on an update event. It is cleared by software.
0: No update occurred.
1: Update interrupt pending. This bit is set by hardware when the registers are updated:
– At overflow or underflow regarding the repetition counter value (update if repetition
counter = 0) and if the UDIS=0 in the TIMx_CR1 register.
– When CNT is reinitialized by software using the UG bit in TIMx_EGR register, if URS=0
and UDIS=0 in the TIMx_CR1 register.
– When CNT is reinitialized by a trigger event (refer to Section 33.4.3: TIMx slave mode
control register (TIMx_SMCR)(x = 1, 8)), if URS=0 and UDIS=0 in the TIMx_CR1 register.

Advanced-control timers (TIM1/TIM8) RM0438
1142/2187 RM0438 Rev 8
33.4.6 TIMx event generation regi ster (TIMx_EGR)(x = 1, 8)
Address offset: 0x14
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. B2G BG TG COMG CC4G CC3G CC2G CC1G UG
wwwwwwwww
Bits 15:9 Reserved, must be kept at reset value.
Bit 8 B2G: Break 2 generation
This bit is set by software in order to generate an event, it is automatically cleared by
hardware.
0: No action
1: A break 2 event is generated. MOE bit is cleared and B2IF flag is set. Related interrupt
can occur if enabled.
Bit 7 BG: Break generation
This bit is set by software in order to generate an event, it is automatically cleared by
hardware.
0: No action
1: A break event is generated. MOE bit is cleared and BIF flag is set. Related interrupt or
DMA transfer can occur if enabled.
Bit 6 TG: Trigger generation
This bit is set by software in order to generate an event, it is automatically cleared by
hardware.
0: No action
1: The TIF flag is set in TIMx_SR register. Related interrupt or DMA transfer can occur if
enabled.
Bit 5 COMG: Capture/Compare control update generation
This bit can be set by software, it is automatically cleared by hardware
0: No action
1: When CCPC bit is set, it allows CCxE, CCxNE and OCxM bits to be updated.
Note: This bit acts only on channels having a complementary output.
Bit 4 CC4G: Capture/Compare 4 generation
Refer to CC1G description
Bit 3 CC3G: Capture/Compare 3 generation
Refer to CC1G description
Bit 2 CC2G: Capture/Compare 2 generation
Refer to CC1G description

RM0438 Rev 8 1143/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.4.7 TIMx capture/compare mode register 1 (TIMx_CCMR1)(x = 1, 8)
Address offset: 0x18
Reset value: 0x0000 0000
The same register can be used for input capture mode (this section) or for output compare
mode (next section). The direction of a channel is defined by configuring the corresponding
CCxS bits. All the other bits of this register have a different function for input capture and for
output compare modes. It is possible to combine both modes independently (e.g. channel 1
in input capture mode and channel 2 in output compare mode).
Input capture mode:
Bit 1 CC1G: Capture/Compare 1 generation
This bit is set by software in order to generate an event, it is automatically cleared by
hardware.
0: No action
1: A capture/compare event is generated on channel 1:
If channel CC1 is configured as output:
CC1IF flag is set, Corresponding interrupt or DMA request is sent if enabled.
If channel CC1 is configured as input:
The current value of the counter is captured in TIMx_CCR1 register. The CC1IF flag is set,
the corresponding interrupt or DMA request is sent if enabled. The CC1OF flag is set if the
CC1IF flag was already high.
Bit 0 UG: Update generation
This bit can be set by software, it is automatically cleared by hardware.
0: No action
1: Reinitialize the counter and generates an update of the registers. The prescaler internal
counter is also cleared (the prescaler ratio is not affected). The counter is cleared if the
center-aligned mode is selected or if DIR=0 (upcounting), else it takes the auto-reload
value (TIMx_ARR) if DIR=1 (downcounting).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9 8 7654321 0
IC2F[3:0] IC2PSC[1:0] CC2S[1:0] IC1F[3:0] IC1PSC[1:0] CC1S[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:12 IC2F[3:0]: Input capture 2 filter
Refer to IC1F[3:0] description.
Bits 11:10 IC2PSC[1:0]: Input capture 2 prescaler
Refer to IC1PSC[1:0] description.

Advanced-control timers (TIM1/TIM8) RM0438
1144/2187 RM0438 Rev 8
33.4.8 TIMx capture/compare m ode register 1 [alternate]
(TIMx_CCMR1)(x = 1, 8)
Address offset: 0x18
Reset value: 0x0000 0000
The same register can be used for output compare mode (this section) or for input capture
mode (previous section). The direction of a channel is defined by configuring the
Bits 9:8 CC2S[1:0]: Capture/Compare 2 selection
This bit-field defines the direction of the channel (input/output) as well as the used input.
00: CC2 channel is configured as output
01: CC2 channel is configured as input, IC2 is mapped on TI2
10: CC2 channel is configured as input, IC2 is mapped on TI1
11: CC2 channel is configured as input, IC2 is mapped on TRC. This mode is working only if an
internal trigger input is selected through TS bit (TIMx_SMCR register)
Note: CC2S bits are writable only when the channel is OFF (CC2E = ‘0’ in TIMx_CCER).
Bits 7:4 IC1F[3:0]: Input capture 1 filter
This bit-field defines the frequency used to sample TI1 input and the length of the digital filter applied
to TI1. The digital filter is made of an event counter in which N consecutive events are needed to
validate a transition on the output:
0000: No filter, sampling is done at fDTS
0001: fSAMPLING=fCK_INT, N=2
0010: fSAMPLING=fCK_INT, N=4
0011: fSAMPLING=fCK_INT, N=8
0100: fSAMPLING=fDTS/2, N=6
0101: fSAMPLING=fDTS/2, N=8
0110: fSAMPLING=fDTS/4, N=6
0111: fSAMPLING=fDTS/4, N=8
1000: fSAMPLING=fDTS/8, N=6
1001: fSAMPLING=fDTS/8, N=8
1010: fSAMPLING=fDTS/16, N=5
1011: fSAMPLING=fDTS/16, N=6
1100: fSAMPLING=fDTS/16, N=8
1101: fSAMPLING=fDTS/32, N=5
1110: fSAMPLING=fDTS/32, N=6
1111: fSAMPLING=fDTS/32, N=8
Bits 3:2 IC1PSC[1:0]: Input capture 1 prescaler
This bit-field defines the ratio of the prescaler acting on CC1 input (IC1). The prescaler is reset as
soon as CC1E=’0’ (TIMx_CCER register).
00: no prescaler, capture is done each time an edge is detected on the capture input
01: capture is done once every 2 events
10: capture is done once every 4 events
11: capture is done once every 8 events
Bits 1:0 CC1S[1:0]: Capture/Compare 1 Selection
This bit-field defines the direction of the channel (input/output) as well as the used input.
00: CC1 channel is configured as output
01: CC1 channel is configured as input, IC1 is mapped on TI1
10: CC1 channel is configured as input, IC1 is mapped on TI2
11: CC1 channel is configured as input, IC1 is mapped on TRC. This mode is working only if an
internal trigger input is selected through TS bit (TIMx_SMCR register)
Note: CC1S bits are writable only when the channel is OFF (CC1E = ‘0’ in TIMx_CCER).

RM0438 Rev 8 1145/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
corresponding CCxS bits. All the other bits of this register have a different function for input
capture and for output compare modes. It is possible to combine both modes independently
(e.g. channel 1 in input capture mode and channel 2 in output compare mode).
Output compare mode:
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. OC2M[3] Res. Res. Res. Res. Res. Res. Res. OC1M[3]
rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9 8 7654321 0
OC2
CE OC2M[2:0] OC2
PE
OC2
FE CC2S[1:0] OC1
CE OC1M[2:0] OC1
PE
OC1
FE CC1S[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:25 Reserved, must be kept at reset value.
Bits 23:17 Reserved, must be kept at reset value.
Bit 15 OC2CE: Output Compare 2 clear enable
Refer to OC1CE description.
Bits 24, 14:12 OC2M[3:0]: Output Compare 2 mode
Refer to OC1M[3:0] description.
Bit 11 OC2PE: Output Compare 2 preload enable
Refer to OC1PE description.
Bit 10 OC2FE: Output Compare 2 fast enable
Refer to OC1FE description.
Bits 9:8 CC2S[1:0]: Capture/Compare 2 selection
This bit-field defines the direction of the channel (input/output) as well as the used input.
00: CC2 channel is configured as output
01: CC2 channel is configured as input, IC2 is mapped on TI2
10: CC2 channel is configured as input, IC2 is mapped on TI1
11: CC2 channel is configured as input, IC2 is mapped on TRC. This mode is working only if
an internal trigger input is selected through the TS bit (TIMx_SMCR register)
Note: CC2S bits are writable only when the ch annel is OFF (CC2E = ‘0’ in TIMx_CCER).
Bit 7 OC1CE: Output Compare 1 clear enable
0: OC1Ref is not affected by the ETRF input
1: OC1Ref is cleared as soon as a High level is detected on ETRF input

Advanced-control timers (TIM1/TIM8) RM0438
1146/2187 RM0438 Rev 8
Bits 16, 6:4 OC1M[3:0]: Output Compare 1 mode
These bits define the behavior of the output reference signal OC1REF from which OC1 and
OC1N are derived. OC1REF is active high whereas OC1 and OC1N active level depends
on CC1P and CC1NP bits.
0000: Frozen - The comparison between the output compare register TIMx_CCR1 and the
counter TIMx_CNT has no effect on the outputs. This mode can be used when the
timer serves as a software timebase. When the frozen mode is enabled during timer
operation, the output keeps the state (active or inactive) it had before entering the
frozen state.
0001: Set channel 1 to active level on match. OC1REF signal is forced high when the
counter TIMx_CNT matches the capture/compare register 1 (TIMx_CCR1).
0010: Set channel 1 to inactive level on match. OC1REF signal is forced low when the
counter TIMx_CNT matches the capture/compare register 1 (TIMx_CCR1).
0011: Toggle - OC1REF toggles when TIMx_CNT=TIMx_CCR1.
0100: Force inactive level - OC1REF is forced low.
0101: Force active level - OC1REF is forced high.
0110: PWM mode 1 - In upcounting, channel 1 is active as long as TIMx_CNT<TIMx_CCR1
else inactive. In downcounting, channel 1 is inactive (OC1REF=‘0’) as long as
TIMx_CNT>TIMx_CCR1 else active (OC1REF=’1’).
0111: PWM mode 2 - In upcounting, channel 1 is inactive as long as
TIMx_CNT<TIMx_CCR1 else active. In downcounting, channel 1 is active as long as
TIMx_CNT>TIMx_CCR1 else inactive.
1000: Retriggerable OPM mode 1 - In up-counting mode, the channel is active until a trigger
event is detected (on TRGI signal). Then, a comparison is performed as in PWM
mode 1 and the channels becomes active again at the next update. In down-counting
mode, the channel is inactive until a trigger event is detected (on TRGI signal). Then,
a comparison is performed as in PWM mode 1 and the channels becomes inactive
again at the next update.
1001: Retriggerable OPM mode 2 - In up-counting mode, the channel is inactive until a
trigger event is detected (on TRGI signal). Then, a comparison is performed as in
PWM mode 2 and the channels becomes inactive again at the next update. In down-
counting mode, the channel is active until a trigger event is detected (on TRGI
signal). Then, a comparison is performed as in PWM mode 1 and the channels
becomes active again at the next update.
1010: Reserved,
1011: Reserved,
1100: Combined PWM mode 1 - OC1REF has the same behavior as in PWM mode 1.
OC1REFC is the logical OR between OC1REF and OC2REF.
1101: Combined PWM mode 2 - OC1REF has the same behavior as in PWM mode 2.
OC1REFC is the logical AND between OC1REF and OC2REF.
1110: Asymmetric PWM mode 1 - OC1REF has the same behavior as in PWM mode 1.
OC1REFC outputs OC1REF when the counter is counting up, OC2REF when it is
counting down.
1111: Asymmetric PWM mode 2 - OC1REF has the same behavior as in PWM mode 2.
OC1REFC outputs OC1REF when the counter is counting up, OC2REF when it is
counting down.
Note: These bits can not be modified as long as LOCK level 3 has been programmed (LOCK
bits in TIMx_BDTR register) and CC1S=’00’ (the channel is configured in output).
Note: In PWM mode, the OCREF level changes  only when the result of the comparison
changes or when the output compare mode switches from “frozen” mode to “PWM”
mode.
Note: On channels having a complementary output, th is bit field is preloaded. If the CCPC bit
is set in the TIMx_CR2 register then the OC1M active bits take the new value from the
preloaded bits only when a COM event is generated.
Note: The OC1M[3] bit is not contiguous, located in bit 16.

RM0438 Rev 8 1147/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.4.9 TIMx capture/compare mode register 2 (TIMx_CCMR2)(x = 1, 8)
Address offset: 0x1C
Reset value: 0x0000 0000
The same register can be used for input capture mode (this section) or for output compare
mode (next section). The direction of a channel is defined by configuring the corresponding
CCxS bits. All the other bits of this register have a different function for input capture and for
output compare modes. It is possible to combine both modes independently (e.g. channel 1
in input capture mode and channel 2 in output compare mode).
Input capture mode:
Bit 3 OC1PE: Output Compare 1 preload enable
0: Preload register on TIMx_CCR1 disabled. TIMx_CCR1 can be written at anytime, the
new value is taken in account immediately.
1: Preload register on TIMx_CCR1 enabled. Read/Write operations access the preload
register. TIMx_CCR1 preload value is loaded in the active register at each update event.
Note: These bits can not be modified as long as LOCK level 3 has been programmed (LOCK
bits in TIMx_BDTR register) and CC1S=’00’ (the channel is configured in output).
Bit 2 OC1FE: Output Compare 1 fast enable
This bit decreases the latency between a trigger event and a transition on the timer output.
It must be used in one-pulse mode (OPM bit set in TIMx_CR1 register), to have the output
pulse starting as soon as possible after the starting trigger.
0: CC1 behaves normally depending on counter and CCR1 values even when the trigger is
ON. The minimum delay to activate CC1 output when an edge occurs on the trigger input
is 5 clock cycles.
1: An active edge on the trigger input acts like a compare match on CC1 output. Then, OC is
set to the compare level independently from the result of the comparison. Delay to
sample the trigger input and to activate CC1 output is reduced to 3 clock cycles. OCFE
acts only if the channel is configured in PWM1 or PWM2 mode.
Bits 1:0 CC1S[1:0]: Capture/Compare 1 selection
This bit-field defines the direction of the channel (input/output) as well as the used input.
00: CC1 channel is configured as output
01: CC1 channel is configured as input, IC1 is mapped on TI1
10: CC1 channel is configured as input, IC1 is mapped on TI2
11: CC1 channel is configured as input, IC1 is mapped on TRC. This mode is working only if
an internal trigger input is selected through TS bit (TIMx_SMCR register)
Note: CC1S bits are writable only when the ch annel is OFF (CC1E = ‘0’ in TIMx_CCER).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
IC4F[3:0] IC4PSC[1:0] CC4S[1:0] IC3F[3:0] IC3PSC[1:0] CC3S[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:12 IC4F[3:0]: Input capture 4 filter
Refer to IC1F[3:0] description.

Advanced-control timers (TIM1/TIM8) RM0438
1148/2187 RM0438 Rev 8
33.4.10 TIMx capture/compare mode register 2 [alternate]
(TIMx_CCMR2)(x = 1, 8)
Address offset: 0x1C
Reset value: 0x0000 0000
The same register can be used for output compare mode (this section) or for input capture
mode (previous section). The direction of a channel is defined by configuring the
corresponding CCxS bits. All the other bits of this register have a different function for input
capture and for output compare modes. It is possible to combine both modes independently
(e.g. channel 1 in input capture mode and channel 2 in output compare mode).
Output compare mode
Bits 11:10 IC4PSC[1:0]: Input capture 4 prescaler
Refer to IC1PSC[1:0] description.
Bits 9:8 CC4S[1:0]: Capture/Compare 4 selection
This bit-field defines the direction of the channel (input/output) as well as the used input.
00: CC4 channel is configured as output
01: CC4 channel is configured as input, IC4 is mapped on TI4
10: CC4 channel is configured as input, IC4 is mapped on TI3
11: CC4 channel is configured as input, IC4 is mapped on TRC. This mode is working only if
an internal trigger input is selected through TS bit (TIMx_SMCR register)
Note: CC4S bits are writable only when the c hannel is OFF (CC4E = ‘0’ in TIMx_CCER).
Bits 7:4 IC3F[3:0]: Input capture 3 filter
Refer to IC1F[3:0] description.
Bits 3:2 IC3PSC[1:0]: Input capture 3 prescaler
Refer to IC1PSC[1:0] description.
Bits 1:0 CC3S[1:0]: Capture/compare 3 selection
This bit-field defines the direction of the channel (input/output) as well as the used input.
00: CC3 channel is configured as output
01: CC3 channel is configured as input, IC3 is mapped on TI3
10: CC3 channel is configured as input, IC3 is mapped on TI4
11: CC3 channel is configured as input, IC3 is mapped on TRC. This mode is working only if
an internal trigger input is selected through TS bit (TIMx_SMCR register)
Note: CC3S bits are writable only when the c hannel is OFF (CC3E = ‘0’ in TIMx_CCER).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. OC4M[3] Res. Res. Res. Res. Res. Res. Res. OC3M[3]
rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
OC4
CE OC4M[2:0] OC4
PE
OC4
FE CC4S[1:0] OC3
CE OC3M[2:0] OC3
PE
OC3
FE CC3S[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:25 Reserved, must be kept at reset value.
Bits 23:17 Reserved, must be kept at reset value.
Bit 15 OC4CE: Output compare 4 clear enable
Refer to OC1CE description.

RM0438 Rev 8 1149/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.4.11 TIMx capture/compare enable register
(TIMx_CCER)(x = 1, 8)
Address offset: 0x20
Reset value: 0x0000 0000
Bits 24, 14:12 OC4M[3:0]: Output compare 4 mode
Refer to OC3M[3:0] description.
Bit 11 OC4PE: Output compare 4 preload enable
Refer to OC1PE description.
Bit 10 OC4FE: Output compare 4 fast enable
Refer to OC1FE description.
Bits 9:8 CC4S[1:0]: Capture/Compare 4 selection
This bit-field defines the direction of the channel (input/output) as well as the used input.
00: CC4 channel is configured as output
01: CC4 channel is configured as input, IC4 is mapped on TI4
10: CC4 channel is configured as input, IC4 is mapped on TI3
11: CC4 channel is configured as input, IC4 is mapped on TRC. This mode is working only if
an internal trigger input is selected through TS bit (TIMx_SMCR register)
Note: CC4S bits are writable only when the channel is OFF (CC4E = ‘0’ in TIMx_CCER).
Bit 7 OC3CE: Output compare 3 clear enable
Refer to OC1CE description.
Bits 16, 6:4 OC3M[3:0]: Output compare 3 mode
Refer to OC1M[3:0] description.
Bit 3 OC3PE: Output compare 3 preload enable
Refer to OC1PE description.
Bit 2 OC3FE: Output compare 3 fast enable
Refer to OC1FE description.
Bits 1:0 CC3S[1:0]: Capture/Compare 3 selection
This bit-field defines the direction of the channel (input/output) as well as the used input.
00: CC3 channel is configured as output
01: CC3 channel is configured as input, IC3 is mapped on TI3
10: CC3 channel is configured as input, IC3 is mapped on TI4
11: CC3 channel is configured as input, IC3 is mapped on TRC. This mode is working only if
an internal trigger input is selected through TS bit (TIMx_SMCR register)
Note: CC3S bits are writable only when the channel is OFF (CC3E = ‘0’ in TIMx_CCER).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CC6P CC6E Res. Res. CC5P CC5E
rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CC4NP Res. CC4P CC4E CC3NP CC3NE CC3P CC3E CC2NP CC2NE CC2P CC2E CC1NP CC1NE CC1P CC1E
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:22 Reserved, must be kept at reset value.

Advanced-control timers (TIM1/TIM8) RM0438
1150/2187 RM0438 Rev 8
Bit 21 CC6P: Capture/Compare 6 output polarity
Refer to CC1P description
Bit 20 CC6E: Capture/Compare 6 output enable
Refer to CC1E description
Bits 19:18 Reserved, must be kept at reset value.
Bit 17 CC5P: Capture/Compare 5 output polarity
Refer to CC1P description
Bit 16 CC5E: Capture/Compare 5 output enable
Refer to CC1E description
Bit 15 CC4NP: Capture/Compare 4 complementary output polarity
Refer to CC1NP description
Bit 14 Reserved, must be  kept at reset value.
Bit 13 CC4P: Capture/Compare 4 output polarity
Refer to CC1P description
Bit 12 CC4E: Capture/Compare 4 output enable
Refer to CC1E description
Bit 11 CC3NP: Capture/Compare 3 complementary output polarity
Refer to CC1NP description
Bit 10 CC3NE: Capture/Compare 3 complementary output enable
Refer to CC1NE description
Bit 9 CC3P: Capture/Compare 3 output polarity
Refer to CC1P description
Bit 8 CC3E: Capture/Compare 3 output enable
Refer to CC1E description
Bit 7 CC2NP: Capture/Compare 2 complementary output polarity
Refer to CC1NP description
Bit 6 CC2NE: Capture/Compare 2 complementary output enable
Refer to CC1NE description
Bit 5 CC2P: Capture/Compare 2 output polarity
Refer to CC1P description
Bit 4 CC2E: Capture/Compare 2 output enable
Refer to CC1E description

RM0438 Rev 8 1151/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Bit 3 CC1NP: Capture/Compare 1 complementary output polarity
CC1 channel configured as output:
0: OC1N active high.
1: OC1N active low.
CC1 channel configured as input:
This bit is used in conjunction with CC1P to define the polarity of TI1FP1 and TI2FP1. Refer
to CC1P description.
Note: This bit is not writable as soon as LOCK level 2 or 3 has been programmed (LOCK bits
in TIMx_BDTR register) and CC1S=”00” (channel configured as output).
On channels having a complementary output, this bit is preloaded. If the CCPC bit is set in the
TIMx_CR2 register then the CC1NP active bit takes the new value from the preloaded bit only
when a Commutation event is generated.
Bit 2 CC1NE: Capture/Compare 1 complementary output enable
0: Off - OC1N is not active. OC1N level is then function of MOE, OSSI, OSSR, OIS1, OIS1N
and CC1E bits.
1: On - OC1N signal is output on the corresponding output pin depending on MOE, OSSI,
OSSR, OIS1, OIS1N and CC1E bits.
On channels having a complementary output, this bit is preloaded. If the CCPC bit is set in the
TIMx_CR2 register then the CC1NE active bit takes the new value from the preloaded bit only
when a Commutation event is generated.
Bit 1 CC1P: Capture/Compare 1 output polarity
0: OC1 active high (output mode) / Edge sensitivity selection (input mode, see below)
1: OC1 active low (output mode) / Edge sensitivity selection (input mode, see below)
When CC1 channel is configured as input, both CC1NP/CC1P bits select the active polarity
of TI1FP1 and TI2FP1 for trigger or capture operations.
CC1NP=0, CC1P=0: non-inverted/rising edge. The circuit is sensitive to TIxFP1 rising edge
(capture or trigger operations in reset, external clock or trigger mode),
TIxFP1 is not inverted (trigger operation in gated mode or encoder
mode).
CC1NP=0, CC1P=1: inverted/falling edge. The circuit is sensitive to TIxFP1 falling edge
(capture or trigger operations in reset, external clock or trigger mode),
TIxFP1 is inverted (trigger operation in gated mode or encoder mode).
CC1NP=1, CC1P=1: non-inverted/both edges/ The circuit is sensitive to both TIxFP1 rising
and falling edges (capture or trigger operations in reset, external clock
or trigger mode), TIxFP1is not inverted (trigger operation in gated
mode). This configuration must not be used in encoder mode.
CC1NP=1, CC1P=0: The configuration is reserved, it must not be used.
Note: This bit is not writable as soon as LOCK level 2 or 3 has been programmed (LOCK bits
in TIMx_BDTR register).
On channels having a complementary output, this bit is preloaded. If the CCPC bit is
set in the TIMx_CR2 register then the CC1P active bit takes the new value from the
preloaded bit only when a Commutation event is generated.
Bit 0 CC1E: Capture/Compare 1 output enable
0: Capture mode disabled / OC1 is not active (see below)
1: Capture mode enabled / OC1 signal is output on the corresponding output pin
When CC1 channel is configured as output, the OC1 level depends on MOE, OSSI,
OSSR, OIS1, OIS1N and CC1NE bits, regardless of the CC1E bits state. Refer to [Table 281](../tables/table_281.md)
for details.
Note: On channels having a complementary output, this bit is preloaded. If the CCPC bit is
set in the TIMx_CR2 register then the CC1E active bit takes the new value from the
preloaded bit only when a Commutation event is generated.

Advanced-control timers (TIM1/TIM8) RM0438
1152/2187 RM0438 Rev 8
Note: The state of the external I/O pins connec ted to the complementary OCx and OCxN channels
depends on the OCx and OCxN channel state and the GPIO registers.
[Table 281](../tables/table_281.md). Output control bits for complementary OCx and OCxN channels with break feature
Control bits Output states (1)
MOE bit OSSI bit OSSR bit CCxE bit CCxNE bi t OCx output state OCxN output state
1X
X0 0 Output disabled (not driven by the timer: Hi-Z)
OCx=0, OCxN=0
00 1
Output disabled (not driven
by the timer: Hi-Z)
OCx=0
OCxREF + Polarity
OCxN = OCxREF xor CCxNP
01 0 OCxREF + Polarity
OCx=OCxREF xor CCxP
Output Disabled (not driven by
the timer: Hi-Z)
OCxN=0
X1 1 OCREF + Polarity + dead-
time
Complementary to OCREF (not
OCREF) + Polarity + dead-time
10 1
Off-State (output enabled
with inactive state)
OCx=CCxP
OCxREF + Polarity
OCxN = OCxREF x or CCxNP
11 0 OCxREF + Polarity
OCx=OCxREF xor CCxP
Off-State (output enabled with
inactive state)
OCxN=CCxNP
0
0
X
XX
Output disabled (not driven by the timer: Hi-Z).
1
00
0 1 Off-State (output enable d with inactive state)
Asynchronously: OCx=CCxP, OCxN=CCxNP (if BRK or
BRK2 is triggered).
Then (this is valid only if BRK is triggered), if the clock is
present: OCx=OISx and OCxN=OISxN after a dead-time,
assuming that OISx and OISxN do not correspond to OCX
and OCxN both in active state (may cause a short circuit
when driving switches in half-bridge configuration).
Note: BRK2 can only be used if OSSI = OSSR = 1.
10
11
1. When both outputs of a channel are not used (control taken ov er by GPIO), the OISx, OISxN, CCxP and CCxNP bits must
be kept cleared.

RM0438 Rev 8 1153/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.4.12 TIMx counter (TIMx_CNT)(x = 1, 8)
Address offset: 0x24
Reset value: 0x0000 0000
33.4.13 TIMx prescaler (TIMx_PSC)(x = 1, 8)
Address offset: 0x28
Reset value: 0x0000
33.4.14 TIMx auto-reload re gister (TIMx_ARR)(x = 1, 8)
Address offset: 0x2C
Reset value: 0xFFFF
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
UIF
CPY Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res.
r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CNT[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 31 UIFCPY: UIF copy
This bit is a read-only copy of the UIF bit of the TIMx_ISR register. If the UIFREMAP bit in
the TIMxCR1 is reset, bit 31 is reserved and read at 0.
Bits 30:16 Reserved, must be kept at reset value.
Bits 15:0 CNT[15:0]: Counter value
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PSC[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 PSC[15:0]: Prescaler value
The counter clock frequency (CK_CNT) is equal to fCK_PSC / (PSC[15:0] + 1).
PSC contains the value to be loaded in the active prescaler register at each update event
(including when the counter is cleared through UG bit of TIMx_EGR register or through
trigger controller when configured in “reset mode”).
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ARR[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 ARR[15:0]: Auto-reload value
ARR is the value to be loaded in the actual auto-reload register.
Refer to the Section 33.3.1: Time-base unit on page 1074 for more details about ARR
update and behavior.
The counter is blocked while the auto-reload value is null.

Advanced-control timers (TIM1/TIM8) RM0438
1154/2187 RM0438 Rev 8
33.4.15 TIMx repetition counter register (TIMx_RCR)(x = 1, 8)
Address offset: 0x30
Reset value: 0x0000
33.4.16 TIMx capture/compare register 1
(TIMx_CCR1)(x = 1, 8)
Address offset: 0x34
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
REP[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 REP[15:0]: Repetition counter value
These bits allow the user to set-up the update rate of the compare registers (i.e. periodic
transfers from preload to active registers) when preload registers are enable, as well as the
update interrupt generation rate, if this interrupt is enable.
Each time the REP_CNT related downcounter reaches zero, an update event is generated
and it restarts counting from REP value. As REP_CNT is reloaded with REP value only at
the repetition update event U_RC, any write to the TIMx_RCR register is not taken in
account until the next repetition update event.
It means in PWM mode (REP+1) corresponds to:
the number of PWM periods in edge-aligned mode
the number of half PWM period in center-aligned mode.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CCR1[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 CCR1[15:0]: Capture/Compare 1 value
If channel CC1 is configured as output: CCR1 is the value to be loaded in the actual
capture/compare 1 register (preload value).
It is loaded permanently if the preload feature is not selected in the TIMx_CCMR1 register
(bit OC1PE). Else the preload value is copied in the active capture/compare 1 register when
an update event occurs.
The active capture/compare register contains the value to be compared to the counter
TIMx_CNT and signaled on OC1 output.
If channel CC1 is configured as input: CR1 is the counter value transferred by the last
input capture 1 event (IC1). The TIMx_CCR1 register is read-only and cannot be
programmed.

RM0438 Rev 8 1155/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.4.17 TIMx capture/compare register 2
(TIMx_CCR2)(x = 1, 8)
Address offset: 0x38
Reset value: 0x0000
33.4.18 TIMx capture/compare register 3
(TIMx_CCR3)(x = 1, 8)
Address offset: 0x3C
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CCR2[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 CCR2[15:0]: Capture/Compare 2 value
If channel CC2 is configured as output: CCR2 is the value to be loaded in the actual
capture/compare 2 register (preload value).
It is loaded permanently if the preload feature is not selected in the TIMx_CCMR1 register
(bit OC2PE). Else the preload value is copied in the active capture/compare 2 register when
an update event occurs.
The active capture/compare register contains the value to be compared to the counter
TIMx_CNT and signaled on OC2 output.
If channel CC2 is configured as input: CCR2 is the counter value transferred by the last
input capture 2 event (IC2). The TIMx_CCR2 register is read-only and cannot be
programmed.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CCR3[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 CCR3[15:0]: Capture/Compare value
If channel CC3 is configured as output: CCR3 is the value to be loaded in the actual
capture/compare 3 register (preload value).
It is loaded permanently if the preload feature is not selected in the TIMx_CCMR2 register
(bit OC3PE). Else the preload value is copied in the active capture/compare 3 register when
an update event occurs.
The active capture/compare register contains the value to be compared to the counter
TIMx_CNT and signalled on OC3 output.
If channel CC3 is configured as input: CCR3 is the counter value transferred by the last
input capture 3 event (IC3). The TIMx_CCR3 register is read-only and cannot be
programmed.

Advanced-control timers (TIM1/TIM8) RM0438
1156/2187 RM0438 Rev 8
33.4.19 TIMx capture/compare register 4
(TIMx_CCR4)(x = 1, 8)
Address offset: 0x40
Reset value: 0x0000
33.4.20 TIMx break and dead-time register
(TIMx_BDTR)(x = 1, 8)
Address offset: 0x44
Reset value: 0x0000 0000
Note: As the bits BK2BID, BKBID, BK2DSRM, BKDSRM, BK2P, BK2E, BK2F[3:0], BKF[3:0],
AOE, BKP, BKE, OSSI, OSSR and DTG[7:0] can be write-locked depending on the LOCK
configuration, it can be necessary to configure all of them during the first write access to the
TIMx_BDTR register.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CCR4[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 CCR4[15:0]: Capture/Compare value
If channel CC4 is configured as output: CCR4 is the value to be loaded in the actual
capture/compare 4 register (preload value).
It is loaded permanently if the preload feature is not selected in the TIMx_CCMR2 register
(bit OC4PE). Else the preload value is copied in the active capture/compare 4 register when
an update event occurs.
The active capture/compare register contains the value to be compared to the counter
TIMx_CNT and signalled on OC4 output.
If channel CC4 is configured as input: CCR4 is the counter value transferred by the last
input capture 4 event (IC4). The TIMx_CCR4 register is read-only and cannot be
programmed.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. BK2BID BKBID BK2
DSRM
BK
DSRM BK2P BK2E BK2F[3:0] BKF[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0987 6 5 43210
MOE AOE BKP BKE OSSR OSSI LOCK[1:0] DTG[7:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:30 Reserved, must be kept at reset value.
Bit 29 BK2BID: Break2 bidirectional
Refer to BKBID description

RM0438 Rev 8 1157/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Bit 28 BKBID: Break Bidirectional
0: Break input BRK in input mode
1: Break input BRK in bidirectional mode
In the bidirectional mode (BKBID bit set to 1), the break input is configured both in input
mode and in open drain output mode. Any active break event asserts a low logic level on the
Break input to indicate an internal break event to external devices.
Note: This bit cannot be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Note: Any write operatio n to this bit takes a delay of 1 APB clock cycle to become effective.
Bit 27 BK2DSRM: Break2 Disarm
Refer to BKDSRM description
Bit 26 BKDSRM: Break Disarm
0: Break input BRK is armed
1: Break input BRK is disarmed
This bit is cleared by hardware when no break source is active.
The BKDSRM bit must be set by software to release the bidirectional output control (open-
drain output in Hi-Z state) and then be polled it until it is reset by hardware, indicating that the
fault condition has disappeared.
Note: Any write operatio n to this bit takes a delay of 1 APB clock cycle to become effective.
Bit 25 BK2P: Break 2 polarity
0: Break input BRK2 is active low
1: Break input BRK2 is active high
Note: This bit cannot be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Note: Any write operatio n to this bit takes a delay of 1 APB clock cycle to become effective.
Bit 24 BK2E: Break 2 enable
This bit enables the complete break 2 protection (including all sources connected to bk_acth
and BKIN sources, as per [Figure 274](../figures/figure_274.md): Break and Break2 circuitry overview).
0: Break2 function disabled
1: Break2 function enabled
Note: The BKIN2 must only be used with OSSR = OSSI = 1.
Note: This bit cannot be modified when LOCK level 1 has been programmed (LOCK bits in
TIMx_BDTR register).
Note: Any write operatio n to this bit takes a delay of 1 APB clock cycle to become effective.

Advanced-control timers (TIM1/TIM8) RM0438
1158/2187 RM0438 Rev 8
Bits 23:20 BK2F[3:0]: Break 2 filter
This bit-field defines the frequency used to sample BRK2 input and the length of the digital
filter applied to BRK2. The digital filter is made of an event counter in which N consecutive
events are needed to validate a transition on the output:
0000: No filter, BRK2 acts asynchronously
0001: fSAMPLING=fCK_INT, N=2
0010: fSAMPLING=fCK_INT, N=4
0011: fSAMPLING=fCK_INT, N=8
0100: fSAMPLING=fDTS/2, N=6
0101: fSAMPLING=fDTS/2, N=8
0110: fSAMPLING=fDTS/4, N=6
0111: fSAMPLING=fDTS/4, N=8
1000: fSAMPLING=fDTS/8, N=6
1001: fSAMPLING=fDTS/8, N=8
1010: fSAMPLING=fDTS/16, N=5
1011: fSAMPLING=fDTS/16, N=6
1100: fSAMPLING=fDTS/16, N=8
1101: fSAMPLING=fDTS/32, N=5
1110: fSAMPLING=fDTS/32, N=6
1111: fSAMPLING=fDTS/32, N=8
Note: This bit cannot be modified when LOCK level 1 has been programmed (LOCK bits in
TIMx_BDTR register).
Bits 19:16 BKF[3:0]: Break filter
This bit-field defines the frequency used to sample BRK input and the length of the digital
filter applied to BRK. The digital filter is made of an event counter in which N consecutive
events are needed to validate a transition on the output:
0000: No filter, BRK acts asynchronously
0001: fSAMPLING=fCK_INT, N=2
0010: fSAMPLING=fCK_INT, N=4
0011: fSAMPLING=fCK_INT, N=8
0100: fSAMPLING=fDTS/2, N=6
0101: fSAMPLING=fDTS/2, N=8
0110: fSAMPLING=fDTS/4, N=6
0111: fSAMPLING=fDTS/4, N=8
1000: fSAMPLING=fDTS/8, N=6
1001: fSAMPLING=fDTS/8, N=8
1010: fSAMPLING=fDTS/16, N=5
1011: fSAMPLING=fDTS/16, N=6
1100: fSAMPLING=fDTS/16, N=8
1101: fSAMPLING=fDTS/32, N=5
1110: fSAMPLING=fDTS/32, N=6
1111: fSAMPLING=fDTS/32, N=8
Note: This bit cannot be modified when LOCK level 1 has been programmed (LOCK bits in
TIMx_BDTR register).

RM0438 Rev 8 1159/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Bit 15 MOE: Main output enable
This bit is cleared asynchronously by hardware as soon as one of the break inputs is active
(BRK or BRK2). It is set by software or automatically depending on the AOE bit. It is acting
only on the channels which are configured in output.
0: In response to a break 2 event. OC and OCN outputs are disabled
In response to a break event or if MOE is written to 0: OC and OCN outputs are disabled
or forced to idle state depending on the OSSI bit.
1: OC and OCN outputs are enabled if their respective enable bits are set (CCxE, CCxNE in
TIMx_CCER register).
See OC/OCN enable description for more details (Section 33.4.11: TIMx capture/compare
enable register (TIMx_CCER)(x = 1, 8)).
Bit 14 AOE: Automatic output enable
0: MOE can be set only by software
1: MOE can be set by software or automatically at the next update event (if none of the break
inputs BRK and BRK2 is active)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 13 BKP: Break polarity
0: Break input BRK is active low
1: Break input BRK is active high
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Note: Any write operatio n to this bit takes a delay of 1 APB clock cycle to become effective.
Bit 12 BKE: Break enable
This bit enables the complete break protection (including all sources connected to bk_acth
and BRK sources, as per [Figure 274](../figures/figure_274.md): Break and Break2 circuitry overview).
0: Break function disabled
1: Break function enabled
Note: This bit cannot be modified when LOCK level 1 has been programmed (LOCK bits in
TIMx_BDTR register).
Note: Any write operatio n to this bit takes a delay of 1 APB clock cycle to become effective.
Bit 11 OSSR: Off-state selection for Run mode
This bit is used when MOE=1 on channels having a complementary output which are
configured as outputs. OSSR is not implemented if no complementary output is implemented
in the timer.
See OC/OCN enable description for more details (Section 33.4.11: TIMx capture/compare
enable register (TIMx_CCER)(x = 1, 8)).
0: When inactive, OC/OCN outputs are disabled (the timer releases the output control which
is taken over by the GPIO logic, which forces a Hi-Z state).
1: When inactive, OC/OCN outputs are enabled with their inactive level as soon as CCxE=1
or CCxNE=1 (the output is still controlled by the timer).
Note: This bit can not be modified as soon as the LOCK level 2 has been programmed (LOCK
bits in TIMx_BDTR register).

Advanced-control timers (TIM1/TIM8) RM0438
1160/2187 RM0438 Rev 8
33.4.21 TIMx DMA control register
(TIMx_DCR)(x = 1, 8)
Address offset: 0x48
Reset value: 0x0000
Bit 10 OSSI: Off-state selection for Idle mode
This bit is used when MOE=0 due to a break event or by a software write, on channels
configured as outputs.
See OC/OCN enable description for more details (Section 33.4.11: TIMx capture/compare
enable register (TIMx_CCER)(x = 1, 8)).
0: When inactive, OC/OCN outputs are disabled (the timer releases the output control which
is taken over by the GPIO logic and which imposes a Hi-Z state).
1: When inactive, OC/OCN outputs are first forced with their inactive level then forced to their
idle level after the deadtime. The timer maintains its control over the output.
Note: This bit can not be modified as soon as the LOCK level 2 has been programmed (LOCK
bits in TIMx_BDTR register).
Bits 9:8 LOCK[1:0]: Lock configuration
These bits offer a write protection against software errors.
00: LOCK OFF - No bit is write protected.
01: LOCK Level 1 = DTG bits in TIMx_BDTR register, OISx and OISxN bits in TIMx_CR2
register and BK2BID, BKBID, BK2DSRM, BKDSRM, BK2P, BK2E, BK2F[3:0], BKF[3:0],
AOE, BKP, BKE, OSSI, OSSR and DTG[7:0] bits in TIMx_BDTR register can no longer
be written.
10: LOCK Level 2 = LOCK Level 1 + CC Polarity bits (CCxP/CCxNP bits in TIMx_CCER
register, as long as the related channel is configured in output through the CCxS bits) as
well as OSSR and OSSI bits can no longer be written.
11: LOCK Level 3 = LOCK Level 2 + CC Control bits (OCxM and OCxPE bits in
TIMx_CCMRx registers, as long as the related channel is configured in output through
the CCxS bits) can no longer be written.
Note: The LOCK bits can be written only once  after the reset. Once the TIMx_BDTR register
has been written, their content is frozen until the next reset.
Bits 7:0 DTG[7:0]: Dead-time generator setup
This bit-field defines the duration of the dead-time inserted between the complementary
outputs. DT correspond to this duration.
DTG[7:5] = 0xx => DT = DTG[7:0] x tDTG with tDTG =t DTS.
DTG[7:5] = 10x => DT = (64 + DTG[5:0]) x tDTG with tDTG =2xt DTS.
DTG[7:5] = 110 => DT = (32 + DTG[4:0]) x tDTG with tDTG =8xt DTS.
DTG[7:5] = 111 => DT = (32 + DTG[4:0]) x tDTG with tDTG =1 6xt DTS.
Example if tDTS = 125 ns (8 MHz), dead-time possible values are:
0 to 15875 ns by 125 ns steps,
16 μs to 31750 ns  by 250 ns steps,
32 μs to 63 μs by 1 μs steps,
64 μs to 126 μs by 2 μs steps
Note: This bit-field can not be modified as long  as LOCK level 1, 2 or 3 has been programmed
(LOCK bits in TIMx_BDTR register).
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. DBL[4:0] Res. Res. Res. DBA[4:0]
rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 1161/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.4.22 TIMx DMA addr ess for full transfer
(TIMx_DMAR)(x = 1, 8)
Address offset: 0x4C
Reset value: 0x0000 0000
Bits 15:13 Reserved, must be kept at reset value.
Bits 12:8 DBL[4:0]: DMA burst length
This 5-bit vector defines the length of DMA transfers (the timer recognizes a burst transfer
when a read or a write access is done to the TIMx_DMAR address), i.e. the number of
transfers. Transfers can be in half-words or in bytes (see example below).
00000: 1 transfer
00001: 2 transfers
00010: 3 transfers
...
10001: 18 transfers
Example: Let us consider the following transfer: DBL = 7 bytes & DBA = TIMx_CR1.
– If DBL = 7 bytes and DBA = TIMx_CR1 represents the address of the byte to be
transferred, the address of the transfer should be given by the following equation:
(TIMx_CR1 address) + DBA + (DMA index), where DMA index = DBL
In this example, 7 bytes are added to (TIMx_CR1 address) + DBA, which gives us the
address from/to which the data is copied. In this case, the transfer is done to 7 registers
starting from the following address: (TIMx_CR1 address) + DBA
According to the configuration of the DMA Data Size, several cases may occur:
– If the DMA Data Size is configured in half-words, 16-bit data is transferred to each of the 7
registers.
– If the DMA Data Size is configured in bytes, the data is also transferred to 7 registers: the
first register contains the first MSB byte, the second register, the first LSB byte and so on.
So with the transfer Timer, one also has to specify the size of data transferred by DMA.
Bits 7:5 Reserved, must be kept at reset value.
Bits 4:0 DBA[4:0]: DMA base address
This 5-bits vector defines the base-address for DMA transfers (when read/write access are
done through the TIMx_DMAR address). DBA is defined as an offset starting from the
address of the TIMx_CR1 register.
Example:
00000: TIMx_CR1,
00001: TIMx_CR2,
00010: TIMx_SMCR,
...
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
DMAB[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DMAB[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

Advanced-control timers (TIM1/TIM8) RM0438
1162/2187 RM0438 Rev 8
33.4.23 TIM1 option re gister 1 (TIM1_OR1)
Address offset: 0x50
Reset value: 0x0000 0000
33.4.24 TIM8 option re gister 1 (TIM8_OR1)
Address offset: 0x50
Reset value: 0x0000 0000
Bits 31:0 DMAB[31:0]: DMA register for burst accesses
A read or write operation to the DMAR register accesses the register located at the address
(TIMx_CR1 address) + (DBA + DMA index) x 4
where TIMx_CR1 address is the address of the control register 1, DBA is the DMA base
address configured in TIMx_DCR register, DMA index is automatically controlled by the DMA
transfer, and ranges from 0 to DBL (DBL configured in TIMx_DCR).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. TI1_
RMP Res. Res. ETR_ADC1_RMP
[1:0]
rw rw rw
Bits 31:5 Reserved, must be kept at reset value.
Bit 4 TI1_RMP: Input Capture 1 remap
0: TIM1 input capture 1 is connected to I/O
1: TIM1 input capture 1 is connected to COMP1 output.
Bits 3:2 Reserved, must be kept at reset value.
Bits 1:0 ETR_ADC1_RMP[1:0]: External trigger remap on ADC1 analog watchdog
00 : TIM1_ETR is not connected to ADC1 AWDx. This configuration must be selected when
the ETR comes from the I/O.
01 : TIM1_ETR is connected to ADC1 AWD1.
10 : TIM1_ETR is connected to ADC1 AWD2.
11 : TIM1_ETR is connected to ADC1 AWD3.
Note: ADC1 AWDx sources are ‘ORed’ with the TIM1_ETR input signals. When ADC1 AWDx
is used, it is necessary to make sure that the corresponding TIM1_ETR input pin is not
enabled in the alternate function controller. Refer to [Figure 252](../figures/figure_252.md): TIM1 ETR input
circuitry.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. TI1_
RMP Res. Res. Res. Res.
rw

RM0438 Rev 8 1163/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.4.25 TIMx capture/compare mode register 3
(TIMx_CCMR3)(x = 1, 8)
Address offset: 0x54
Reset value: 0x0000 0000
The channels 5 and 6 can only be configured in output.
Output compare mode:
Bits 31:5 Reserved, must be kept at reset value.
Bit 4 TI1_RMP: Input Capture 1 remap
0: TIM8 input capture 1 is connected to I/O
1: TIM8 input capture 1 is connected to COMP2 output.
Bits 3:0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. OC6M[3] Res. Res. Res. Res. Res. Res. Res. OC5M[3]
rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9 8 7654321 0
OC6
CE OC6M[2:0] OC6
PE OC6FE Res. Res. OC5
CE OC5M[2:0] OC5PE OC5FE Res. Res.
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:25 Reserved, must be kept at reset value.
Bits 23:17 Reserved, must be kept at reset value.
Bit 15 OC6CE: Output compare 6 clear enable
Refer to OC1CE description.
Bits 24, 14, 13, 12 OC6M[3:0]: Output compare 6 mode
Refer to OC1M description.
Bit 11 OC6PE: Output compare 6 preload enable
Refer to OC1PE description.
Bit 10 OC6FE: Output compare 6 fast enable
Refer to OC1FE description.
Bits 9:8 Reserved, must be kept at reset value.
Bit 7 OC5CE: Output compare 5 clear enable
Refer to OC1CE description.
Bits 16, 6, 5, 4 OC5M[3:0]: Output compare 5 mode
Refer to OC1M description.
Bit 3 OC5PE: Output compare 5 preload enable
Refer to OC1PE description.
Bit 2 OC5FE: Output compare 5 fast enable
Refer to OC1FE description.
Bits 1:0 Reserved, must be kept at reset value.

Advanced-control timers (TIM1/TIM8) RM0438
1164/2187 RM0438 Rev 8
33.4.26 TIMx capture/compare register 5
(TIMx_CCR5)(x = 1, 8)
Address offset: 0x58
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
GC5C3 GC5C2 GC5C1 Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res.
rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CCR5[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 31 GC5C3: Group Channel 5 and Channel 3
Distortion on Channel 3 output:
0: No effect of OC5REF on OC3REFC
1: OC3REFC is the logical AND of OC3REFC and OC5REF
This bit can either have immediate effect or be preloaded and taken into account after an
update event (if preload feature is selected in TIMxCCMR2).
Note: it is also possible to apply this distortion on combined PWM signals.
Bit 30 GC5C2: Group Channel 5 and Channel 2
Distortion on Channel 2 output:
0: No effect of OC5REF on OC2REFC
1: OC2REFC is the logical AND of OC2REFC and OC5REF
This bit can either have immediate effect or be preloaded and taken into account after an
update event (if preload feature is selected in TIMxCCMR1).
Note: it is also possible to apply this distortion on combined PWM signals.
Bit 29 GC5C1: Group Channel 5 and Channel 1
Distortion on Channel 1 output:
0: No effect of OC5REF on OC1REFC5
1: OC1REFC is the logical AND of OC1REFC and OC5REF
This bit can either have immediate effect or be preloaded and taken into account after an
update event (if preload feature is selected in TIMxCCMR1).
Note: it is also possible to apply this distortion on combined PWM signals.
Bits 28:16 Reserved, must be kept at reset value.
Bits 15:0 CCR5[15:0]: Capture/Compare 5 value
CCR5 is the value to be loaded in the actual capture/compare 5 register (preload value).
It is loaded permanently if the preload feature is not selected in the TIMx_CCMR3 register
(bit OC5PE). Else the preload value is copied in the active capture/compare 5 register when
an update event occurs.
The active capture/compare register contains the value to be compared to the counter
TIMx_CNT and signaled on OC5 output.

RM0438 Rev 8 1165/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
33.4.27 TIMx capture/compare register 6
(TIMx_CCR6)(x = 1, 8)
Address offset: 0x5C
Reset value: 0x0000
33.4.28 TIM1 option re gister 2 (TIM1_OR2)
Address offset: 0x60
Reset value: 0x0000 0001
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CCR6[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 CCR6[15:0]: Capture/Compare 6 value
CCR6 is the value to be loaded in the actual capture/compare 6 register (preload value).
It is loaded permanently if the preload feature is not selected in the TIMx_CCMR3 register
(bit OC6PE). Else the preload value is copied in the active capture/compare 6 register when
an update event occurs.
The active capture/compare register contains the value to be compared to the counter
TIMx_CNT and signaled on OC6 output.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res.
ETR
SEL
[2]
rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ETRSEL[1:0] Res. Res. BK
CMP2P
BK
CMP1P BKINP BKDF1
BK0E Res. Res. Res. Res. Res. BK
CMP2E
BK
CMP1E BKINE
rw rw rw rw rw rw rw rw rw
Bits 31:17 Reserved, must be kept at reset value.
Bits 16:14 ETRSEL[2:0]: ETR source selection
These bits select the ETR input source.
000: ETR input is connected to I/O
001: COMP1 output
010: COMP2 output
011: ADC1 AWD1
100: ADC1 AWD2
101: ADC1 AWD3
Others: Reserved
Note: These bits can not be modified as long as LOCK level 1 has been programmed (LOCK
bits in TIMx_BDTR register).
Bits 13:12 Reserved, must be kept at reset value.

Advanced-control timers (TIM1/TIM8) RM0438
1166/2187 RM0438 Rev 8
Bit 11 BKCMP2P: BRK COMP2 input polarity
This bit selects the COMP2 input sensitivity. It must be programmed together with the BKP
polarity bit.
0: COMP2 input polarity is not inverted (active low if BKP=0, active high if BKP=1)
1: COMP2 input polarity is inverted (active high if BKP=0, active low if BKP=1)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 10 BKCMP1P: BRK COMP1 input polarity
This bit selects the COMP1 input sensitivity. It must be programmed together with the BKP
polarity bit.
0: COMP1 input polarity is not inverted (active low if BKP=0, active high if BKP=1)
1: COMP1 input polarity is inverted (active high if BKP=0, active low if BKP=1)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 9 BKINP: BRK BKIN input polarity
This bit selects the BKIN alternate function input sensitivity. It must be programmed together
with the BKP polarity bit.
0: BKIN input polarity is not inverted (active low if BKP=0, active high if BKP=1)
1: BKIN input polarity is inverted (active high if BKP=0, active low if BKP=1)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 8 BKDF1BK0E: BRK dfsdm1_break[0] enable
This bit enables the dfsdm1_break[0] for the timer’s BRK input. dfsdm1_break[0] output is
‘ORed’ with the other BRK sources.
0: dfsdm1_break[0] input disabled
1: dfsdm1_break[0] input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bits 7:3 Reserved, must be kept at reset value.
Bit 2 BKCMP2E: BRK COMP2 enable
This bit enables the COMP2 for the timer’s BRK input. COMP2 output is ‘ORed’ with the
other BRK sources.
0: COMP2 input disabled
1: COMP2 input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 1 BKCMP1E: BRK COMP1 enable
This bit enables the COMP1 for the timer’s BRK input. COMP1 output is ‘ORed’ with the
other BRK sources.
0: COMP1 input disabled
1: COMP1 input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).

RM0438 Rev 8 1167/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Note: Refer to [Figure 252](../figures/figure_252.md): TIM1 ETR input circuitry and to [Figure 274](../figures/figure_274.md): Break and Break2 circuitry
overview.
33.4.29 TIM1 option re gister 3 (TIM1_OR3)
Address offset: 0x64
Reset value: 0x0000 0001
Bit 0 BKINE: BRK BKIN input enable
This bit enables the BKIN alternate function input for the timer’s BRK input. BKIN input is
‘ORed’ with the other BRK sources.
0: BKIN input disabled
1: BKIN input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res.
BK2
CMP2
P
BK2
CMP1
P
BK2
INP
BK2DF1
BK1E Res. Res. Res. Res. Res. BK2
CMP2E
BK2
CMP1E BK2INE
rw rw rw rw rw rw rw
Bits 31:12 Reserved, must be kept at reset value.
Bit 11 BK2CMP2P: BRK2 COMP2 input polarity
This bit selects the COMP2 input sensitivity. It must be programmed together with the BK2P
polarity bit.
0: COMP2 input polarity is not inverted (active low if BK2P=0, active high if BK2P=1)
1: COMP2 input polarity is inverted (active high if BK2P=0, active low if BK2P=1)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 10 BK2CMP1P: BRK2 COMP1 input polarity
This bit selects the COMP1 input sensitivity. It must be programmed together with the BK2P
polarity bit.
0: COMP1 input polarity is not inverted (active low if BK2P=0, active high if BK2P=1)
1: COMP1 input polarity is inverted (active high if BK2P=0, active low if BK2P=1)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 9 BK2INP: BRK2 BKIN2 input polarity
This bit selects the BKIN2 alternate function input sensitivity. It must be programmed
together with the BK2P polarity bit.
0: BKIN2 input polarity is not inverted (active low if BK2P=0, active high if BK2P=1)
1: BKIN2 input polarity is inverted (active high if BK2P=0, active low if BK2P=1)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).

Advanced-control timers (TIM1/TIM8) RM0438
1168/2187 RM0438 Rev 8
Note: Refer to [Figure 274](../figures/figure_274.md): Break and Break2 circuitry overview.
33.4.30 TIM8 option re gister 2 (TIM8_OR2)
Address offset: 0x60
Reset value: 0x0000 0001
Bit 8 BK2DF1BK1E: BRK2 dfsdm1_break[1] enable
This bit enables the dfsdm1_break[1] for the timer’s BRK2 input. dfsdm1_break[1] output is
‘ORed’ with the other BRK2 sources.
0: dfsdm1_break[1] input disabled
1: dfsdm1_break[1] input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bits 7:3 Reserved, must be kept at reset value.
Bit 2 BK2CMP2E: BRK2 COMP2 enable
This bit enables the COMP2 for the timer’s BRK2 input. COMP2 output is ‘ORed’ with the
other BRK2 sources.
0: COMP2 input disabled
1: COMP2 input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 1 BK2CMP1E: BRK2 COMP1 enable
This bit enables the COMP1 for the timer’s BRK2 input. COMP1 output is ‘ORed’ with the
other BRK2 sources.
0: COMP1 input disabled
1: COMP1 input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 0 BK2INE: BRK2 BKIN input enable
This bit enables the BKIN2 alternate function input for the timer’s BRK2 input. BKIN2 input is
‘ORed’ with the other BRK2 sources.
0: BKIN2 input disabled
1: BKIN2 input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. ETRSEL
[2]
rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
ETRSEL[1:0] Res. Res.
BK
CMP2
P
BK
CMP1
P
BKINP BKDF1
BK2E Res. Res. Res. Res. Res. BK
CMP2E
BK
CMP1E BKINE
rw rw rw rw rw rw rw rw rw
Bits 31:17 Reserved, must be kept at reset value.

RM0438 Rev 8 1169/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Bits 16:14 ETRSEL[2:0]: ETR source selection
These bits select the ETR input source.
000: ETR input is connected to I/O
001: COMP1 output
010: COMP2 output
Others: Reserved
Note: These bits can not be modified as long as LOCK level 1 has been programmed (LOCK
bits in TIMx_BDTR register).
Bits 13:12 Reserved, must be kept at reset value.
Bit 11 BKCMP2P: BRK COMP2 input polarity
This bit selects the COMP2 input sensitivity. It must be programmed together with the BKP
polarity bit.
0: COMP2 input polarity is not inverted (active low if BKP=0, active high if BKP=1)
1: COMP2 input polarity is inverted (active high if BKP=0, active low if BKP=1)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 10 BKCMP1P: BRK COMP1 input polarity
This bit selects the COMP1 input sensitivity. It must be programmed together with the BKP
polarity bit.
0: COMP1 input polarity is not inverted (active low if BKP=0, active high if BKP=1)
1: COMP1 input polarity is inverted (active high if BKP=0, active low if BKP=1)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 9 BKINP: BRK BKIN input polarity
This bit selects the BKIN alternate function input sensitivity. It must be programmed together
with the BKP polarity bit.
0: BKIN input polarity is not inverted (active low if BKP=0, active high if BKP=1)
1: BKIN input polarity is inverted (active high if BKP=0, active low if BKP=1)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 8 BKDF1BK2E: BRK dfsdm1_break[2] enable
This bit enables the dfsdm1_break[2] for the timer’s BRK input. dfsdm1_break[2] output is
‘ORed’ with the other BRK sources.
0: dfsdm1_break[2] input disabled
1: dfsdm1_break[2] input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bits 7:3 Reserved, must be kept at reset value.
Bit 2 BKCMP2E: BRK COMP2 enable
This bit enables the COMP2 for the timer’s BRK input. COMP2 output is ‘ORed’ with the
other BRK sources.
0: COMP2 input disabled
1: COMP2 input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).

Advanced-control timers (TIM1/TIM8) RM0438
1170/2187 RM0438 Rev 8
Note: Refer to [Figure 253](../figures/figure_253.md): TIM8 ETR input circuitry and to [Figure 274](../figures/figure_274.md): Break and Break2 circuitry
overview.
33.4.31 TIM8 option re gister 3 (TIM8_OR3)
Address offset: 0x64
Reset value: 0x0000 0001
Bit 1 BKCMP1E: BRK COMP1 enable
This bit enables the COMP1 for the timer’s BRK input. COMP1 output is ‘ORed’ with the
other BRK sources.
0: COMP1 input disabled
1: COMP1 input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 0 BKINE: BRK BKIN input enable
This bit enables the BKIN alternate function input for the timer’s BRK input. BKIN input is
‘ORed’ with the other BRK sources.
0: BKIN input disabled
1: BKIN input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res.
BK2
CMP2
P
BK2
CMP1
P
BK2
INP
BK2DF1
BK3E Res. Res. Res. Res. Res. BK2
CMP2E
BK2
CMP1E BK2INE
rw rw rw rw rw rw rw
Bits 31:12 Reserved, must be kept at reset value.
Bit 11 BK2CMP2P: BRK2 COMP2 input polarity
This bit selects the COMP2 input sensitivity. It must be programmed together with the BK2P
polarity bit.
0: COMP2 input polarity is not inverted (active low if BK2P=0, active high if BK2P=1)
1: COMP2 input polarity is inverted (active high if BK2P=0, active low if BK2P=1)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 10 BK2CMP1P: BRK2 COMP1 input polarity
This bit selects the COMP1 input sensitivity. It must be programmed together with the BK2P
polarity bit.
0: COMP1 input polarity is not inverted (active low if BK2P=0, active high if BK2P=1)
1: COMP1 input polarity is inverted (active high if BK2P=0, active low if BK2P=1)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).

RM0438 Rev 8 1171/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
Note: Refer to [Figure 274](../figures/figure_274.md): Break and Break2 circuitry overview.
Bit 9 BK2INP: BRK2 BKIN2 input polarity
This bit selects the BKIN2 alternate function input sensitivity. It must be programmed
together with the BK2P polarity bit.
0: BKIN2 input polarity is not inverted (active low if BK2P=0, active high if BK2P=1)
1: BKIN2 input polarity is inverted (active high if BK2P=0, active low if BK2P=1)
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 8 BK2DF1BK3E: BRK2 dfsdm1_break[3] enable
This bit enables the dfsdm1_break[3] for the timer’s BRK2 input. dfsdm1_break[3] output is
‘ORed’ with the other BRK2 sources.
0: dfsdm1_break[3] input disabled
1: dfsdm1_break[3] input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bits 7:3 Reserved, must be kept at reset value.
Bit 2 BK2CMP2E: BRK2 COMP2 enable
This bit enables the COMP2 for the timer’s BRK2 input. COMP2 output is ‘ORed’ with the
other BRK2 sources.
0: COMP2 input disabled
1: COMP2 input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 1 BK2CMP1E: BRK2 COMP1 enable
This bit enables the COMP1 for the timer’s BRK2 input. COMP1 output is ‘ORed’ with the
other BRK2 sources.
0: COMP1 input disabled
1: COMP1 input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).
Bit 0 BK2INE: BRK2 BKIN input enable
This bit enables the BKIN2 alternate function input for the timer’s BRK2 input. BKIN2 input is
‘ORed’ with the other BRK2 sources.
0: BKIN2 input disabled
1: BKIN2 input enabled
Note: This bit can not be modified as long as LOCK level 1 has been programmed (LOCK bits
in TIMx_BDTR register).

Advanced-control timers (TIM1/TIM8) RM0438
1172/2187 RM0438 Rev 8
33.4.32 TIM1 register map
TIM1 registers are mapped as 16-bit addressable registers as described in the table below:
[Table 282](../tables/table_282.md). TIM1 register map and reset values
Offset Register
name
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
TIM1_CR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
UIFREMAP
Res.
CKD
[1:0]
ARPE
CMS
[1:0]
DIR
OPM
URS
UDIS
CEN
Reset value 0 0000000000
0x04
TIM1_CR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
MMS2[3:0]
Res.
OIS6
Res.
OIS5
Res.
OIS4
OIS3N
OIS3
OIS2N
OIS2
OIS1N
OIS1
TI1S
MMS
[2:0]
CCDS
CCUS
Res.
CCPC
Reset value 0000 0 0 0000000000000 0
0x08
TIM1_SMCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SMS[3]
ETP
ECE
ETP
S
[1:0]
ETF[3:0]
MSM
TS[2:0]
Res.
SMS[2:0]
Reset value 0000000000000 000
0x0C
TIM1_DIER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TDE
COMDE
CC4DE
CC3DE
CC2DE
CC1DE
UDE
BIE
TIE
COMIE
CC4IE
CC3IE
CC2IE
CC1IE
UIE
Reset value 000000000000000
0x10
TIM1_SR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CC6IF
CC5IF
Res.
Res.
SBIF
CC4OF
CC3OF
CC2OF
CC1OF
B2IF
BIF
TIF
COMIF
CC4IF
CC3IF
CC2IF
CC1IF
UIF
Reset value 00 0 0000000000000
0x14
TIM1_EGR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
B2G
BG
TG
COMG
CC4G
CC3G
CC2G
CC1G
UG
Reset value 000000000
0x18
TIM1_CCMR1
Output
Compare mode
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OC2M[3]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OC1M[3]
OC2CE
OC2M
[2:0]
OC2PE
OC2FE
CC2
S
[1:0]
OC1CE
OC1M
[2:0]
OC1PE
OC1FE
CC1
S
[1:0]
Reset value 0 00000000000000000
TIM1_CCMR1
Input Capture
mode
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
IC2F[3:0]
IC2
PSC
[1:0]
CC2
S
[1:0]
IC1F[3:0]
IC1
PSC
[1:0]
CC1
S
[1:0]
Reset value 0000000000000000
0x1C
TIM1_CCMR2
Output
Compare mode
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OC4M[3]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OC3M[3]
OC4CE
OC4M
[2:0]
OC4PE
OC4FE
CC4
S
[1:0]
OC3CE
OC3M
[2:0]
OC3PE
OC3FE
CC3
S
[1:0]
Reset value 0 00000000000000000
TIM1_CCMR2
Input Capture
mode
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
IC4F[3:0]
IC4
PSC
[1:0]
CC4
S
[1:0]
IC3F[3:0]
IC3
PSC
[1:0]
CC3
S
[1:0]
Reset value 0000000000000000
0x20
TIM1_CCER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CC6P
CC6E
Res.
Res.
CC5P
CC5E
CC4NP
Res.
CC4P
CC4E
CC3NP
CC3NE
CC3P
CC3E
CC2NP
CC2NE
CC2P
CC2E
CC1NP
CC1NE
CC1P
CC1E
Reset value 00 00 0 00000000000000

RM0438 Rev 8 1173/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
0x24
TIM1_CNT
UIFCP
Res.
Res.
Res.
Res.
Res.
Res.
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
Reset value 0 0000000000000000
0x28
TIM1_PSC
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PSC[15:0]
Reset value 0000000000000000
0x2C
TIM1_ARR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
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
Reset value 1111111111111111
0x30
TIM1_RCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
REP[15:0]
Reset value 0000000000000000
0x34
TIM1_CCR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCR1[15:0]
Reset value 0000000000000000
0x38
TIM1_CCR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCR2[15:0]
Reset value 0000000000000000
0x3C
TIM1_CCR3
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCR3[15:0]
Reset value 0000000000000000
0x40
TIM1_CCR4
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCR4[15:0]
Reset value 0000000000000000
0x44
TIM1_BDTR
Res.
Res.
BK2BID
BKBID
BK2DSRM
BKDSRM
BK2P
BK2E
BK2F[3:0] BKF[3:0]
MOE
AOE
BKP
BKE
OSSR
OSSI
LOC
K
[1:0]
DT[7:0]
Reset value 0 0 0 0 00000000000000000000000000
0x48
TIM1_DCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
DBL[4:0]
Res.
Res.
Res.
DBA[4:0]
Reset value 00000 00000
0x4C
TIM1_DMAR DMAB[31:0]
Reset value 0000000000000000
0x50
TIM1_OR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TI1_RMP
Res.
Res.
ETR_ADC1_RMP
Reset value 00 0
0x54
TIM1_CCMR3
Output
Compare mode
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OC6M[3]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OC5M[3]
OC6CE
OC6M
[2:0]
OC6PE
OC6FE
Res.
Res.
OC5CE
OC5M
[2:0]
OC5PE
OC5FE
Res.
Res.
Reset value 0 0000000 000000
[Table 282](../tables/table_282.md). TIM1 register map and reset values (continued)
Offset Register
name
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

Advanced-control timers (TIM1/TIM8) RM0438
1174/2187 RM0438 Rev 8
Refer to Section 2.3 on page 86 for the register boundary addresses.
33.4.33 TIM8 register map
TIM8 registers are mapped as 16-bit addressable registers as described in the table below:
0x58
TIM1_CCR5
GC5C3
GC5C2
GC5C1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCR5[15:0]
Reset value 000 0000000000000000
0x5C
TIM1_CCR6
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCR6[15:0]
Reset value 0000000000000000
0x60
TIM1_OR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ETRSEL
[2:0]
Res.
Res.
BKCMP2P
BKCMP1P
BKINP
BKDF1BK0E
Res.
Res.
Res.
Res.
Res.
BKCMP2E
BKCMP1E
BKINE
Reset value 000 0000 001
0x64
TIM1_OR3
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
BK2CMP2P
BK2CMP1P
BK2INP
BK2DF1BK1E
Res.
Res.
Res.
Res.
Res.
BK2CMP2E
BK2CMP1E
BK2INE
Reset value 0000 001
[Table 282](../tables/table_282.md). TIM1 register map and reset values (continued)
Offset Register
name
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
[Table 283](../tables/table_283.md). TIM8 register map and reset values
Offset Register
name
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
TIM8_CR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
UIFREMA
Res.
CKD
[1:0]
ARPE
CMS
[1:0]
DIR
OPM
URS
UDIS
CEN
Reset value 0 0000000000
0x04
TIM8_CR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
MMS2[3:0]
Res.
OIS6
Res.
OIS5
Res.
OIS4
OIS3N
OIS3
OIS2N
OIS2
OIS1N
OIS1
TI1S
MMS
[2:0]
CCDS
CCUS
Res.
CCPC
Reset value 0000 0 0 0000000000000 0
0x08
TIM8_SMCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SMS[3]
ETP
ECE
ETP
S
[1:0]
ETF[3:0]
MSM
TS[2:0]
Res.
SMS[2:0]
Reset value 0000000000000 000
0x0C
TIM8_DIER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TDE
COMDE
CC4DE
CC3DE
CC2DE
CC1DE
UDE
BIE
TIE
COMIE
CC4IE
CC3IE
CC2IE
CC1IE
UIE
Reset value 000000000000000
0x10
TIM8_SR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CC6IF
CC5IF
Res.
Res.
SBIF
CC4OF
CC3OF
CC2OF
CC1OF
B2IF
BIF
TIF
COMIF
CC4IF
CC3IF
CC2IF
CC1IF
UIF
Reset value 00 00000000000000

RM0438 Rev 8 1175/2187
RM0438 Advanced-control timers (TIM1/TIM8)
1176
0x14
TIM8_EGR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
B2G
BG
TG
COMG
CC4G
CC3G
CC2G
CC1G
UG
Reset value 000000000
0x18
TIM8_CCMR1
Output
Compare mode
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OC2M[3]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OC1M[3]
OC2CE
OC2M
[2:0]
OC2PE
OC2FE
CC2
S
[1:0]
OC1CE
OC1M
[2:0]
OC1PE
OC1FE
CC1
S
[1:0]
Reset value 0 00000000000000000
TIM8_CCMR1
Input Capture
mode
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
IC2F[3:0]
IC2
PSC
[1:0]
CC2
S
[1:0]
IC1F[3:0]
IC1
PSC
[1:0]
CC1
S
[1:0]
Reset value 0000000000000000
0x1C
TIM8_CCMR2
Output
Compare mode
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OC4M[3]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OC3M[3]
OC4CE
OC4M
[2:0]
OC4PE
OC4FE
CC4
S
[1:0]
OC3CE
OC3M
[2:0]
OC3PE
OC3FE
CC3
S
[1:0]
Reset value 0 00000000000000000
TIM8_CCMR2
Input Capture
mode
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
IC4F[3:0]
IC4
PSC
[1:0]
CC4
S
[1:0]
IC3F[3:0]
IC3
PSC
[1:0]
CC3
S
[1:0]
Reset value 0000000000000000
0x20
TIM8_CCER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CC6P
CC6E
Res.
Res.
CC5P
CC5E
CC4NP
Res.
CC4P
CC4E
CC3NP
CC3NE
CC3P
CC3E
CC2NP
CC2NE
CC2P
CC2E
CC1NP
CC1NE
CC1P
CC1E
Reset value 00 000 00000000000000
0x24
TIM8_CNT
UIFCPY
Res.
Res.
Res.
Res.
Res.
Res.
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
Reset value 0 0000000000000000
0x28
TIM8_PSC
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PSC[15:0]
Reset value 0000000000000000
0x2C
TIM8_ARR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
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
Reset value 1111111111111111
0x30
TIM8_RCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
REP[15:0]
Reset value 0000000000000000
0x34
TIMx_CCR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCR1[15:0]
Reset value 0000000000000000
0x38
TIM8_CCR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCR2[15:0]
Reset value 0000000000000000
0x3C
TIM8_CCR3
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCR3[15:0]
Reset value 0000000000000000
0x40
TIM8_CCR4
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCR4[15:0]
Reset value 0000000000000000
[Table 283](../tables/table_283.md). TIM8 register map and reset values (continued)
Offset Register
name
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

Advanced-control timers (TIM1/TIM8) RM0438
1176/2187 RM0438 Rev 8
Refer to Section 2.3 on page 86 for the register boundary addresses.
0x44
TIM8_BDTR
Res.
Res.
BK2BID
BKBID
BK2DSRM
BKDSRM
BK2P
BK2E
BK2F[3:0] BKF[3:0]
MOE
AOE
BKP
BKE
OSSR
OSSI
LOC
K
[1:0]
DT[7:0]
Reset value 000000000000000000000000000000
0x48
TIM8_DCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
DBL[4:0]
Res.
Res.
Res.
DBA[4:0]
Reset value 00000 00000
0x4C
TIM8_DMAR DMAB[31:0]
Reset value 0000000000000000
0x54
TIM8_CCMR3
Output
Compare mode
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OC6M[3]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OC5M[3]
OC6CE
OC6M
[2:0]
OC6PE
OC6FE
Res.
Res.
OC5CE
OC5M
[2:0]
OC5PE
OC5FE
Res.
Res.
Reset value 0 0000000 000000
0x58
TIM8_CCR5
GC5C3
GC5C2
GC5C1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCR5[15:0]
Reset value 000 0000000000000000
0x5C
TIM8_CCR6
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCR6[15:0]
Reset value 0000000000000000
0x60
TIM8_OR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ETRSEL
[2:0]
Res.
Res.
BKCMP2P
BKCMP1P
BKINP
BKDF1BK2E
Res.
Res.
Res.
Res.
Res.
BKCMP2E
BKCMP1E
BKINE
Reset value 000 0000 001
0x64
TIM8_OR3
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
BK2CMP2P
BK2CMP1P
BK2INP
BK2DF1BK3E
Res.
Res.
Res.
Res.
Res.
BK2CMP2E
BK2CMP1E
BK2INE
Reset value 0000 001
[Table 283](../tables/table_283.md). TIM8 register map and reset values (continued)
Offset Register
name
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
* [Figure 230: Architectural Diagram](../figures/figure_230.md)
* [Figure 231: Architectural Diagram](../figures/figure_231.md)
* [Figure 232: Architectural Diagram](../figures/figure_232.md)
* [Figure 233: Architectural Diagram](../figures/figure_233.md)
* [Figure 234: Architectural Diagram](../figures/figure_234.md)
* [Figure 235: Architectural Diagram](../figures/figure_235.md)
* [Figure 236: Architectural Diagram](../figures/figure_236.md)
* [Figure 237: Architectural Diagram](../figures/figure_237.md)
* [Figure 238: Architectural Diagram](../figures/figure_238.md)
* [Figure 239: Architectural Diagram](../figures/figure_239.md)
* [Figure 240: Architectural Diagram](../figures/figure_240.md)
* [Figure 241: Architectural Diagram](../figures/figure_241.md)
* [Figure 242: Architectural Diagram](../figures/figure_242.md)
* [Figure 243: Architectural Diagram](../figures/figure_243.md)
* [Figure 244: Architectural Diagram](../figures/figure_244.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 277: Configuration Matrix](../tables/table_277.md)
* [Table 278: Configuration Matrix](../tables/table_278.md)
* [Table 279: Configuration Matrix](../tables/table_279.md)
* [Table 280: Configuration Matrix](../tables/table_280.md)
* [Table 281: Configuration Matrix](../tables/table_281.md)
* [Table 282: Configuration Matrix](../tables/table_282.md)
* [Table 283: Configuration Matrix](../tables/table_283.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)