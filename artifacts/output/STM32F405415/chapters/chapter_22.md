# Chapter 22: General-purpose timers (TIM9 to TIM14)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32F4 Reference Manual RM0090 - Chapter 22: General-purpose timers (TIM9 to TIM14).
* **Document Source**: RM0090 Reference Manual
* **PDF Reference Location**: Pages 646 - 691
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Timers (TIM)](../peripherals/timers.md)

## 2. Official Reference Manual Text Content (RM0090 Ingestion)
```text
General-purpose timers (TIM9 to TIM14) RM0090
646/1741 RM0090 Rev 22
19 General-purpose timers (TIM9 to TIM14)
This section applies to the whole STM32F4xx family, unless otherwise specified.
19.1 TIM9 to TIM14 introduction
The TIM9 to TIM14 general-purpose timers consist of a 16-bit auto-reload counter driven by
a programmable prescaler.
They may be used for a variety of purposes, including measuring the pulse lengths of input
signals (input capture) or generating output waveforms (output compare, PWM).
Pulse lengths and waveform periods can be modulated from a few microseconds to several
milliseconds using the timer prescaler and the RCC clock controller prescalers.
The TIM9 to TIM14 timers are completely independent, and do not share any resources.
They can be synchronized together as described in Section 19.3.12.
19.2 TIM9 to TIM14 main features
19.2.1 TIM9/TIM12  main features
The features of the TIM9 to TIM14 general-purpose timers include:
• 16-bit auto-reload upcounter
• 16-bit programmable prescaler used to divide the counter clock frequency by any factor
between 1 and 65536 (can be changed “on the fly”)
• Up to 2 independent channels for:
– Input capture
– Output compare
– PWM generation (edge-aligned mode)
– One-pulse mode output
• Synchronization circuit to control the timer with external signals and to interconnect
several timers together
• Interrupt generation on the following events:
– Update: counter overflow, counter initializ ation (by software or internal trigger)
– Trigger event (counter start, stop, initialization or count by internal trigger)
– Input capture
– Output compare

RM0090 Rev 22 647/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
[Figure 180](../figures/figure_180.md). General-purpose timer block diagram (TIM9 and TIM12)
19.2.2 TIM10/TIM11 and TI M13/TIM14 main features
The features of general-purpose timers TIM10/TIM11 and TIM13/TIM14 include:
• 16-bit auto-reload upcounter
• 16-bit programmable prescaler used to divide the counter clock frequency by any factor
between 1 and 65536 (can be changed “on the fly”)
• independent channel for:
– Input capture
– Output compare
– PWM generation (edge-aligned mode)
– One-pulse mode output
• Interrupt generation on the following events:
– Update: counter overflow, coun ter initialization (by software)
– Input capture
– Output compare
U
U
U
CC1I
CC2I
Trigger
controller
+/-
Stop, Clear
TI1FP1
TI2FP2
ITR0
ITR1
ITR2 TRGI
Output
control
OC1REF
OC2REF
U
UI
Reset, enable, up, count
CK_PSC
IC1
IC2 IC2PS
IC1PS
TI1FP1
TGI
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
OC2
TIMx_CH1
TIMx_CH2
Slave
controller
mode
PSC
prescaler CNT counter
Internal clock (CK_INT)
CK_CNT
ITR3
ai17190b
Input filter &
edge detector
Capture/Compare 1 register
Notes:
Reg Preload registers transferred
to active registers on U event
according to control bit
Event
Interrupt
Auto-reload register
Capture/Compare 2 registerPrescaler
Prescaler
Input filter &
edge detector
Output
control

General-purpose timers (TIM9 to TIM14) RM0090
648/1741 RM0090 Rev 22
[Figure 181](../figures/figure_181.md). General-purpose timer block diagram (TIM10/11/13/14)
Autoreload register
Capture/Compare 1 register
U
U
CC1I
Stop, Clear
output
control
OC1OC1REF
U
UI
IC1
PrescalerInput filter &
edge detector
IC1PS
TI1FP1
Reg
event
Notes:
Preload registers transferred
to active registers on U event
according to control bit
interrupt & DMA output
CC1I
TI1
TIMx_CH1
prescaler counter
+/-CK_PSC PSC CNTCK_CNT
Internal clock (CK_INT)
ai17725c
Trigger
Controller
Enable
counter
TIMx_CH1

RM0090 Rev 22 649/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
19.3 TIM9 to TIM14 functional description
19.3.1 Time-base unit
The main block of the timer is a 16-bit counter with its related auto-reload register. The
counters counts up.
The counter clock can be divided by a prescaler.
The counter, the auto-reload register and the prescaler register can be written or read by
software. This is true even when the counter is running.
The time-base unit includes:
• Counter register (TIMx_CNT)
• Prescaler register (TIMx_PSC)
• Auto-reload register (TIMx_ARR)
The auto-reload register is preloaded. Writing to or reading from the auto-reload register
accesses the preload register. The content of the preload register are transferred into the
shadow register permanently or at each update event (UEV), depending on the auto-reload
preload enable bit (ARPE) in TIMx_CR1 register. The update event is sent when the counter
reaches the overflow and if the UDIS bit equals 0 in the TIMx_CR1 register. It can also be
generated by software. The generation of the update event is described in details for each
configuration.
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
[Figure 182](../figures/figure_182.md) and [Figure 183](../figures/figure_183.md) give some examples of the counter behavior when the prescaler
ratio is changed on the fly.

General-purpose timers (TIM9 to TIM14) RM0090
650/1741 RM0090 Rev 22
[Figure 182](../figures/figure_182.md). Counter timing diagram with prescaler division change from 1 to 2
[Figure 183](../figures/figure_183.md). Counter timing diagram with prescaler division change from 1 to 4
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

RM0090 Rev 22 651/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
19.3.2 Counter modes
Upcounting mode
In upcounting mode, the counter counts from 0 to the auto-reload value (content of the
TIMx_ARR register), then restarts from 0 and generates a counter overflow event.
Setting the UG bit in the TIMx_EGR register (by software or by using the slave mode
controller on TIM9 and TIM12) also generates an update event.
The UEV event can be disabled by software by setting the UDIS bit in the TIMx_CR1
register. This is to avoid updating the shadow registers while writing new values in the
preload registers. Then no update event occurs until the UDIS bit has been written to 0.
However, the counter restarts from 0, as well as the counter of the prescaler (but the
prescale rate does not change). In addition, if the URS bit (update request selection) in
TIMx_CR1 register is set, setting the UG bit generates an update event UEV but without
setting the UIF flag (thus no interrupt is sent). This is to avoid generating both update and
capture interrupts when clearing the counter on the capture event.
When an update event occurs, all the registers are updated and the update flag (UIF bit in
TIMx_SR register) is set (depending on the URS bit):
• The auto-reload shadow register is updated with the preload value (TIMx_ARR),
• The buffer of the prescaler is reloaded with the preload value (content of the TIMx_PSC
register).
The following figures show some examples of the counter behavior for different clock
frequencies when TIMx_ARR=0x36.
[Figure 184](../figures/figure_184.md). Counter timing diagram, internal clock divided by 1
00 02 03 04 05 06 0733 34 35 3631
MS31078V3
CK_PSC
CNT_EN
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag (UIF)
0132

General-purpose timers (TIM9 to TIM14) RM0090
652/1741 RM0090 Rev 22
[Figure 185](../figures/figure_185.md). Counter timing diagram, internal clock divided by 2
[Figure 186](../figures/figure_186.md). Counter timing diagram, internal clock divided by 4
[Figure 187](../figures/figure_187.md). Counter timing diagram, internal clock divided by N
MS31079V3
CK_PSC
CNT_EN
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag (UIF)
0034 0035 0036 0000 0001 0002 0003
MS31080V3
CK_PSC
CNT_EN
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag (UIF)
0000 00010035 0036
MS31081V3
CK_PSC
Timerclock = CK_CNT
Counter register
Update event (UEV)
Counter overflow
Update interrupt flag (UIF)
001F 20

RM0090 Rev 22 653/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
[Figure 188](../figures/figure_188.md). Counter timing diagram, update event when ARPE=0 (TIMx_ARR not
preloaded)
[Figure 189](../figures/figure_189.md). Counter timing diagram, update event when ARPE=1 (TIMx_ARR
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

General-purpose timers (TIM9 to TIM14) RM0090
654/1741 RM0090 Rev 22
19.3.3 Clock selection
The counter clock can be provided by the following clock sources:
• Internal clock (CK_INT)
• External clock mode1 (for TIM9 and TIM12): external input pin (TIx)
• Internal trigger inputs (ITRx) (for TIM9 and TIM12): connecting the trigger output from
another timer. Refer to Using one timer as prescaler for another timer for more details.
Internal clock source (CK_INT)
The internal clock source is the default clock source for TIM10/TIM11 and TIM13/TIM14.
For TIM9 and TIM12, the internal clock source is selected when the slave mode controller is
disabled (SMS=’000’). The CEN bit in the TIMx_CR1 register and the UG bit in the
TIMx_EGR register are then used as control bits and can be changed only by software
(except for UG which remains cleared). As soon as the CEN bit is programmed to 1, the
prescaler is clocked by the internal clock CK_INT.
[Figure 190](../figures/figure_190.md) shows the behavior of the control circuit and of the upcounter in normal mode,
without prescaler.
[Figure 190](../figures/figure_190.md). Control circuit in normal mode, internal clock divided by 1
External clock source mode 1(TIM9 and TIM12)
This mode is selected when SMS=’111’ in the TIMx_SMCR register. The counter can count
at each rising or falling edge on a selected input.
Internal clock
Counter clock = CK_CNT = CK_PSC
Counter register
CEN=CNT_EN
UG
CNT_INIT
MS31085V2
00 02 03 04 05 06 0732 33 34 35 3631 01

RM0090 Rev 22 655/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
[Figure 191](../figures/figure_191.md). TI2 external clock connection example
For example, to configure the upcounter to count in response to a rising edge on the TI2
input, use the following procedure:
1. Configure channel 2 to detect rising edges on the TI2 input by writing CC2S = ‘01’ in
the TIMx_CCMR1 register.
2. Configure the input filter duration by wr iting the IC2F[3:0] bits in the TIMx_CCMR1
register (if no filter is needed, keep IC2F=’0000’).
3. Select the rising edge polarity by writin g CC2P=’0’ and CC2NP=’0’ in the TIMx_CCER
register.
4. Configure the timer in external clock mode 1 by writing SMS=’111’ in the TIMx_SMCR
register.
5. Select TI2 as the trigger input source by  writing TS=’110’ in the TIMx_SMCR register.
6. Enable the counter by writing CEN=’1’ in the TIMx_CR1 register.
Note: The capture prescaler is not used for triggering, so no need to configure it.
When a rising edge occurs on TI2, the counter counts once and the TIF flag is set.
The delay between the rising edge on TI2 and the actual clock of the counter is due to the
resynchronization circuit on TI2 input.
[Figure 192](../figures/figure_192.md). Control circuit in external clock mode 1
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
MS37337V1
(internal clock)
TI1F or
TI2F oror
Counter clock = CK_CNT = CK_PSC
Counter register 35 3634
TI2
CNT_EN
TIF
Write TIF = 0
MS31087V3

General-purpose timers (TIM9 to TIM14) RM0090
656/1741 RM0090 Rev 22
19.3.4 Capture/compare channels
Each Capture/Compare channel is built around a capture/compare register (including a
shadow register), a input stage for capture (with digital filter, multiplexing and prescaler) and
an output stage (with comparator and output control).
[Figure 193](../figures/figure_193.md) to [Figure 195](../figures/figure_195.md) give an overview of a capture/compare channel.
The input stage samples the corresponding TIx input to generate a filtered signal TIxF.
Then, an edge detector with polarity selection generates a signal (TIxFPx) which can be
used as trigger input by the slave mode controller or as the capture command. It is
prescaled before the capture register (ICxPS).
[Figure 193](../figures/figure_193.md). Capture/compare channel (example: channel 1 input stage)
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

RM0090 Rev 22 657/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
[Figure 194](../figures/figure_194.md). Capture/compare channel 1 main circuit
[Figure 195](../figures/figure_195.md). Output stage of capture/compare channel (channel 1)
The capture/compare block is made of one preload register and one shadow register. Write
and read always access the preload register.
In capture mode, captures are actually done in the shadow register, which is copied into the
preload register.
In compare mode, the content of the preload register is copied into the shadow register
which is compared to the counter.
19.3.5 Input capture mode
In Input capture mode, the Capture/Compare registers (TIMx_CCRx) are used to latch the
value of the counter after a transition detected by the corresponding ICx signal. When a
capture occurs, the corresponding CCXIF flag (TIMx_SR register) is set and an interrupt or
a DMA request can be sent if they are enabled. If a capture occurs while the CCxIF flag was
already high, then the over-capture flag CCxOF (TIMx_SR register) is set. CCxIF can be
MS31089V3
CC1E
Capture /compare shadow register
Comparator
Capture/compare preload register
Counter
IC1PS
CC1S[0]
CC1S[1]
Capture
Input
mode
S
R
Read CCR1H
Read CCR1L
read_in_progress
capture_transfer CC1S[0]
CC1S[1]
S
R
write CCR1H
write CCR1L
write_in_progress
Output
mode
UEV
OC1PE
(from time
base unit)
compare_transfer
APB Bus
8 8
high
low
(if 16-bit)
MCU-peripheral interface
TIMx_CCMR1
OC1PE
CNT>CCR1
CNT=CCR1
TIMx_EGR
CC1G
ai17720
Output
mode
controller
CNT > CCR2
CNT = CCR2
TIMx_CCMR1
OC2M[2:0]
0
1
CC1P
TIMx_CCER
Output
enable
circuit
OC1
CC1E TIMx_CCER
To the master
mode controller
OC1_REF

General-purpose timers (TIM9 to TIM14) RM0090
658/1741 RM0090 Rev 22
cleared by software by writing it to ‘0’ or by reading the captured data stored in the
TIMx_CCRx register. CCxOF is cleared when the user writes it to ‘0’.
The following example shows how to capture the counter value in TIMx_CCR1 when TI1
input rises. To do this, use the following procedure:
1. Select the active input: TIMx_CCR1 must be  linked to the TI1 input, so write the CC1S
bits to ‘01’ in the TIMx_CCMR1 register. As soon as CC1S becomes different from ‘00’,
the channel is configured in input mode and the TIMx_CCR1 register becomes read-
only.
2. Program the needed input filter duration wit h respect to the signal connected to the
timer (by programming the ICxF bits in the TIMx_CCMRx register if the input is one of
the TIx inputs). Let us imagine that, when toggling, the input signal is not stable during
at least five internal clock cycles. We must program a filter duration longer than these 5
clock cycles. We can validate a transition on TI1 when eight consecutive samples with
the new level have been detected (sampled at fDTS frequency). Then write IC1F bits to
‘0011’ in the TIMx_CCMR1 register.
3. Select the edge of the active transition on the TI1 channel by programming CC1P and
CC1NP bits to ‘00’ in the TIMx_CCER register (rising edge in this case).
4. Program the input prescaler. In our example, we wish the capture to be performed at
each valid transition, so the prescaler is disabled (write IC1PS bits to ‘00’ in the
TIMx_CCMR1 register).
5. Enable capture from the counter into the ca pture register by setting the CC1E bit in the
TIMx_CCER register.
6. If needed, enable the related interrupt request by setting the CC1IE bit in the
TIMx_DIER register.
When an input capture occurs:
• The TIMx_CCR1 register gets the value of the counter on the active transition.
• CC1IF flag is set (interrupt flag). CC1OF is also set if at least two consecutive captures
occurred whereas the flag was not cleared.
• An interrupt is generated depending on the CC1IE bit.
In order to handle the overcapture, it is recommended to read the data before the
overcapture flag. This is to avoid missing an overcapture which could happen after reading
the flag and before reading the data.
Note: IC interrupt requests can be generated by software by setting the corresponding CCxG bit in
the TIMx_EGR register.

RM0090 Rev 22 659/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
19.3.6 PWM input mode (only for TIM9/12)
This mode is a particular case of input capture mode. The procedure is the same except:
• Two ICx signals are mapped on the same TIx input.
• These 2 ICx signals are active on edges with opposite polarity.
• One of the two TIxFP signals is selected as trigger input and the slave mode controller
is configured in reset mode.
For example, the user can measure the period (in TIMx_CCR1 register) and the duty cycle
(in TIMx_CCR2 register) of the PWM applied on TI1 using the following procedure
(depending on CK_INT frequency and prescaler value):
1. Select the active input for TIMx_CCR1: write the CC1S bits to ‘01’ in the TIMx_CCMR1
register (TI1 selected).
2. Select the active polarity for TI1FP1 (u sed both for capture in TIMx_CCR1 and counter
clear): program the CC1P and CC1NP bits to ‘00’ (active on rising edge).
3. Select the active input for TIMx_CCR2: write the CC2S bits to ‘10’ in the TIMx_CCMR1
register (TI1 selected).
4. Select the active polarity for TI1FP2 (use d for capture in TIMx_CCR2): write the CC2P
bit to '1' and the CC2NP bit to '0' (active on falling edge).
5. Select the valid trigger input: write the TS bits to ‘101’ in the TIMx_SMCR register
(TI1FP1 selected).
6. Configure the slave mode controller in reset mode: write the SMS bits to ‘100’ in the
TIMx_SMCR register.
7. Enable the captures: write the CC1E and CC2E bits to ‘1’ in the TIMx_CCER register.
[Figure 196](../figures/figure_196.md). PWM input mode timing
1. The PWM input mode can be used only with the TIMx _CH1/TIMx_CH2 signals due to the fact that only
TI1FP1 and TI2FP2 are connected to the slave mode controller.
TI1
TIMx_CNT 0000 0001 0002 0003 0004 00000004
TIMx_CCR1
TIMx_CCR2
0004
0002
IC1 capture
IC2 capture
reset counter
IC2 capture
pulse wi d th
IC1 capture
period
measurementmeasurement
ai15413

General-purpose timers (TIM9 to TIM14) RM0090
660/1741 RM0090 Rev 22
19.3.7 Forced output mode
In output mode (CCxS bits = ‘00’ in the TIMx_CCMRx register), each output compare signal
(OCxREF and then OCx) can be forced to active or inactive level directly by software,
independently of any comparison between the output compare register and the counter.
To force an output compare signal (OCXREF/OCx) to its active level, the user just needs to
write ‘101’ in the OCxM bits in the corresponding TIMx_CCMRx register. Thus OCXREF is
forced high (OCxREF is always active high) and OCx get opposite value to CCxP polarity
bit.
For example: CCxP=’0’ (OCx active high) => OCx is forced to high level.
The OCxREF signal can be forced low by writing the OCxM bits to ‘100’ in the
TIMx_CCMRx register.
Anyway, the comparison between the TIMx_CCRx shadow register and the counter is still
performed and allows the flag to be set. Interrupt requests can be sent accordingly. This is
described in the output compare mode section below.
19.3.8 Output compare mode
This function is used to control an output waveform or indicating when a period of time has
elapsed.
When a match is found between the capture/compare register and the counter, the output
compare function:
1. Assigns the corresponding output pin to a programmable value defined by the output
compare mode (OCxM bits in the TIMx_CCMRx register) and the output polarity (CCxP
bit in the TIMx_CCER register). The output pin can keep its level (OCXM=’000’), be set
active (OCxM=’001’), be set inactive (OCxM=’010’) or can toggle (OCxM=’011’) on
match.
2. Sets a flag in the interrupt status re gister (CCxIF bit in the TIMx_SR register).
3. Generates an interrupt if the corresponding  interrupt mask is set (CCXIE bit in the
TIMx_DIER register).
The TIMx_CCRx registers can be programmed with or without preload registers using the
OCxPE bit in the TIMx_CCMRx register.
In output compare mode, the update event UEV has no effect on OCxREF and OCx output.
The timing resolution is one count of the counter. Output compare mode can also be used to
output a single pulse (in One-pulse mode).
Procedure:
1. Select the counter clock (i nternal, external, prescaler).
2. Write the desired data in the TIMx_ARR and TIMx_CCRx registers.
3. Set the CCxIE bit if an inte rrupt request is to be generated.
4. Select the output mode. For example:
– Write OCxM = ‘011’ to toggle OC x output pin when CNT matches CCRx
– Write OCxPE = ‘0’ to disable preload register
– Write CCxP = ‘0’ to sele ct active high polarity
– Write CCxE = ‘1’ to enable the output
5. Enable the counter by setting the CEN bit in the TIMx_CR1 register.

RM0090 Rev 22 661/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
The TIMx_CCRx register can be updated at any time by software to control the output
waveform, provided that the preload register is not enabled (OCxPE=’0’, else TIMx_CCRx
shadow register is updated only at the next update event UEV). An example is given in
[Figure 197](../figures/figure_197.md).
[Figure 197](../figures/figure_197.md). Output compare mode, toggle on OC1.
19.3.9 PWM mode
Pulse Width Modulation mode allows the user to generate a signal with a frequency
determined by the value of the TIMx_ARR register and a duty cycle determined by the value
of the TIMx_CCRx register.
The PWM mode can be selected independently on each channel (one PWM per OCx
output) by writing ‘110’ (PWM mode 1) or ‘111’ (PWM mode 2) in the OCxM bits in the
TIMx_CCMRx register. Enable the corresponding preload register by setting the OCxPE bit
in the TIMx_CCMRx register, and eventually the auto-reload preload register by setting the
ARPE bit in the TIMx_CR1 register.
As the preload registers are transferred to the shadow registers only when an update event
occurs, before starting the counter, the user has to initialize all the registers by setting the
UG bit in the TIMx_EGR register.
The OCx polarity is software programmable using the CCxP bit in the TIMx_CCER register.
It can be programmed as active high or active low. The OCx output is enabled by the CCxE
bit in the TIMx_CCER register. Refer to the TIMx_CCERx register description for more
details.
In PWM mode (1 or 2), TIMx_CNT and TIMx_CCRx are always compared to determine
whether TIMx_CNT ≤TIMx_CCRx.
The timer is able to generate PWM in edge-aligned mode only since the counter is
upcounting.
PWM edge-aligned mode
In the following example, we consider PWM mode 1. The reference PWM signal OCxREF is
high as long as TIMx_CNT < TIMx_CCRx else it becomes low. If the compare value in
MS31092V2
OC1REF= OC1
TIM1_CNT B200 B2010039
TIM1_CCR1 003A
Write B201h in the CC1R register
Match detected on CCR1
Interrupt generated if enabled
003B
B201
003A

General-purpose timers (TIM9 to TIM14) RM0090
662/1741 RM0090 Rev 22
TIMx_CCRx is greater than the auto-reload value (in TIMx_ARR) then OCxREF is held at
‘1’. If the compare value is 0 then OCxRef is held at ‘0’. [Figure 198](../figures/figure_198.md) shows some edge-
aligned PWM waveforms in an example where TIMx_ARR=8.
[Figure 198](../figures/figure_198.md). Edge-aligned PWM waveforms (ARR=8)
19.3.10 One-pulse mode
One-pulse mode (OPM) is a particular case of the previous modes. It allows the counter to
be started in response to a stimulus and to generate a pulse with a programmable length
after a programmable delay.
Starting the counter can be controlled through the slave mode controller. Generating the
waveform can be done in output compare mode or PWM mode. Select One-pulse mode by
setting the OPM bit in the TIMx_CR1 register. This makes the counter stop automatically at
the next update event UEV.
A pulse can be correctly generated only if the compare value is different from the counter
initial value. Before starting (when the timer is waiting for the trigger), the configuration must
be as follows:
CNT < CCRx≤ ARR (in particular, 0 < CCRx)
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

RM0090 Rev 22 663/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
[Figure 199](../figures/figure_199.md). Example of one pulse mode.
For example the user may want to generate a positive pulse on OC1 with a length of tPULSE
and after a delay of tDELAY as soon as a positive edge is detected on the TI2 input pin.
Use TI2FP2 as trigger 1:
1. Map TI2FP2 to TI2 by writing CC2S =’01’ in the TIMx_CCMR1 register.
2. TI2FP2 must detect a rising edge, writ e CC2P=’0’ and CC2NP = ‘0’ in the TIMx_CCER
register.
3. Configure TI2FP2 as trigger for the slave mo de controller (TRGI) by writing TS=’110’ in
the TIMx_SMCR register.
4. TI2FP2 is used to start the counter by wr iting SMS to ‘110’ in the TIMx_SMCR register
(trigger mode).
The OPM waveform is defined by writing the compare registers (taking into account the
clock frequency and the counter prescaler).
• The tDELAY is defined by the value written in the TIMx_CCR1 register.
• The tPULSE is defined by the difference between the auto-reload value and the compare
value (TIMx_ARR - TIMx_CCR1).
• Let us say the user wants to build a waveform with a transition from ‘0’ to ‘1’ when a
compare match occurs and a transition from ‘1’ to ‘0’ when the counter reaches the
auto-reload value. To do this enable PWM mode 2 by writing OC1M=’111’ in the
TIMx_CCMR1 register. The user can optionally enable the preload registers by writing
OC1PE=’1’ in the TIMx_CCMR1 register and ARPE in the TIMx_CR1 register. In this
case the user has to write the compare value in the TIMx_CCR1 register, the auto-
reload value in the TIMx_ARR register, generate an update by setting the UG bit and
wait for external trigger event on TI2. CC1P is written to ‘0’ in this example.
The user only wants one pulse (Single mode), so write '1 in the OPM bit in the TIMx_CR1
register to stop the counter at the next update event (when the counter rolls over from the
auto-reload value back to 0). When OPM bit in the TIMx_CR1 register is set to '0', so the
Repetitive mode is selected.
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

General-purpose timers (TIM9 to TIM14) RM0090
664/1741 RM0090 Rev 22
Particular case: OCx fast enable
In One-pulse mode, the edge detection on TIx input set the CEN bit which enables the
counter. Then the comparison between the counter and the compare value makes the
output toggle. But several clock cycles are needed for these operations and it limits the
minimum delay tDELAY min we can get.
If the user wants to output a waveform with the minimum delay, set the OCxFE bit in the
TIMx_CCMRx register. Then OCxRef (and OCx) are forced in response to the stimulus,
without taking in account the comparison. Its new level is the same as if a compare match
had occurred. OCxFE acts only if the channel is configured in PWM1 or PWM2 mode.
19.3.11 TIM9/12 external trigger synchronization
The TIM9/12 timers can be synchronized with an external trigger in several modes: Reset
mode, Gated mode and Trigger mode.
Slave mode: Reset mode
The counter and its prescaler can be reinitialized in response to an event on a trigger input.
Moreover, if the URS bit from the TIMx_CR1 register is low, an update event UEV is
generated. Then all the preloaded registers (TIMx_ARR, TIMx_CCRx) are updated.
In the following example, the upcounter is cleared in response to a rising edge on TI1 input:
1. Configure the channel 1 to detect rising edges on TI1. Configure the input filter duration
(in this example, no need of any filter, IC1F = 0000 kept). The capture prescaler is not
used for triggering, so there’s no need to configure it. The CC1S bits select the input
capture source only, CC1S = ‘01’ in the TIMx_CCMR1 register. Program CC1P and
CC1NP to ‘00’ in TIMx_CCER register to validate the polarity (and detect rising edges
only).
2. Configure the timer in rese t mode by writing SMS=’100’ in TIMx_SMCR register. Select
TI1 as the input source by writing TS=’101’ in TIMx_SMCR register.
3. Start the counter by writing CE N=’1’ in the TIMx_CR1 register.
The counter starts counting on the internal clock, then behaves normally until TI1 rising
edge. When TI1 rises, the counter is cleared and restarts from 0. In the meantime, the
trigger flag is set (TIF bit in the TIMx_SR register) and an interrupt request can be sent if
enabled (depending on the TIE bit in TIMx_DIER register).
The following figure shows this behavior when the auto-reload register TIMx_ARR=0x36.
The delay between the rising edge on TI1 and the actual reset of the counter is due to the
resynchronization circuit on TI1 input.

RM0090 Rev 22 665/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
[Figure 200](../figures/figure_200.md). Control circuit in reset mode
Slave mode: Gated mode
The counter can be enabled depending on the level of a selected input.
In the following example, the upcounter counts only when TI1 input is low:
1. Configure the channel 1 to detect low levels on TI1. Configure the input filter duration
(in this example, no need of any filter, IC1F=’0000’ kept). The capture prescaler is not
used for triggering, so there’s no need to configure it. The CC1S bits select the input
capture source only, CC1S=’01’ in TIMx_CCMR1 register. Program CC1P=’1’ and
CC1NP= ‘0’ in TIMx_CCER register to validate the polarity (and detect low level only).
2. Configure the timer in gated mode by writing SMS=’101’ in TIMx_SMCR register.
Select TI1 as the input source by writing TS=’101’ in TIMx_SMCR register.
3. Enable the counter by writ ing CEN=’1’ in the TIMx_CR1 register (in gated mode, the
counter does not start if CEN=’0’, whatever is the trigger input level).
The counter starts counting on the internal clock as long as TI1 is low and stops as soon as
TI1 becomes high. The TIF flag in the TIMx_SR register is set both when the counter starts
or stops.
The delay between the rising edge on TI1 and the actual stop of the counter is due to the
resynchronization circuit on TI1 input.
MS31401V2
00
Counter clock = ck_cnt = ck_psc
Counter register 01 02 03 00 01 02 0332 33 34 35 36
UG
TI1
3130
TIF

General-purpose timers (TIM9 to TIM14) RM0090
666/1741 RM0090 Rev 22
[Figure 201](../figures/figure_201.md). Control circuit in gated mode
Slave mode: Trigger mode
The counter can start in response to an event on a selected input.
In the following example, the upcounter starts in response to a rising edge on TI2 input:
1. Configure the channel 2 to detect rising edges on TI2. Configure the input filter duration
(in this example, no need of any filter, IC2F=’0000’ kept). The capture prescaler is not
used for triggering, so there’s no need to configure it. The CC2S bits are configured to
select the input capture source only, CC2S=’01’ in TIMx_CCMR1 register. Program
CC2P=’1’ and CC2NP=’0’ in TIMx_CCER register to validate the polarity (and detect
low level only).
2. Configure the timer in trigger mode by  writing SMS=’110’ in TIMx_SMCR register.
Select TI2 as the input source by writing TS=’110’ in TIMx_SMCR register.
When a rising edge occurs on TI2, the counter starts counting on the internal clock and the
TIF flag is set.
The delay between the rising edge on TI2 and the actual start of the counter is due to the
resynchronization circuit on TI2 input.
[Figure 202](../figures/figure_202.md). Control circuit in trigger mode
MS31402V1
TI1
cnt_en
Write TIF=0
37
Counter clock = ck_cnt = ck_psc
Counter register 3832 33 34 35 363130
TIF
MS31403V1
TI2
cnt_en
37
Counter clock = ck_cnt = ck_psc
Counter register 3834 35 36
TIF

RM0090 Rev 22 667/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
19.3.12 Timer synchronization (TIM9/12)
The TIM timers are linked together internally for timer synchronization or chaining. Refer to
Section 18.3.15: Timer synchronization for details.
Note: The clock of the slave timer must be enabled prior to receive events from the master timer,
and must not be changed on-the-fly while triggers are received from the master timer.
19.3.13 Debug mode
When the microcontroller enters debug mode (Cortex®-M4 with FPU core halted), the TIMx
counter either continues to work normally or stops, depending on DBG_TIMx_STOP
configuration bit in DBG module. For more details, refer to Section 38.16.2: Debug support
for timers, watchdog, bxCAN and I2C.

General-purpose timers (TIM9 to TIM14) RM0090
668/1741 RM0090 Rev 22
19.4 TIM9 and TIM12 registers
Refer to Section 2.2 for a list of abbreviations used in register descriptions.
The peripheral registers have to be written by half-words (16 bits) or words (32 bits). Read
accesses can be done by bytes (8 bits), half-words (16 bits) or words (32 bits).
19.4.1 TIM9/12 control register 1 (TIMx_CR1)
Address offset: 0x00
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved
CKD[1:0] ARPE
Reserved
OPM URS UDIS CEN
rw rw rw rw rw rw rw
Bits 15:10 Reserved, must be kept at reset value.
Bits 9:8 CKD: Clock division
This bit-field indicates the division ratio between the timer clock (CK_INT) frequency and
sampling clock used by the digital filters (TIx),
00: tDTS = tCK_INT
01: tDTS = 2 × tCK_INT
10: tDTS = 4 × tCK_INT
11: Reserved
Bit 7 ARPE: Auto-reload preload enable
0: TIMx_ARR register is not buffered.
1: TIMx_ARR register is buffered.
Bits 6:4 Reserved, must be kept at reset value.
Bit 3 OPM: One-pulse mode
0: Counter is not stopped on the update event
1: Counter stops counting on the next update event (clearing the CEN bit).
Bit 2 URS: Update request source
This bit is set and cleared by software to select the UEV event sources.
0: Any of the following events generates an update interrupt if enabled:
– Counter overflow
– Setting the UG bit
1: Only counter overflow generates an update interrupt if enabled.
Bit 1 UDIS: Update disable
This bit is set and cleared by software to enable/disable update event (UEV) generation.
0: UEV enabled. An UEV is generated by one of the following events:
– Counter overflow
– Setting the UG bit
Buffered registers are then loaded with their preload values.
1: UEV disabled. No UEV is generated, shadow registers keep their value (ARR, PSC,
CCRx). The counter and the prescaler are reinitialized if the UG bit is set.
Bit 0 CEN: Counter enable
0: Counter disabled
1: Counter enabled
CEN is cleared automatically in one-pulse mode, when an update event occurs.

RM0090 Rev 22 669/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
19.4.2 TIM9/12 slave mode c ontrol register (TIMx_SMCR)
Address offset: 0x08
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved
MSM TS[2:0]
Res.
SMS[2:0]
rw rw rw rw rw rw rw
Bits 15:8 Reserved, must be kept at reset value.
Bit 7 MSM: Master/Slave mode
0: No action
1: The effect of an event on the trigger input (TRGI) is delayed to allow a perfect
synchronization between the current timer and its slaves (through TRGO). It is useful in
order to synchronize several timers on a single external event.
Bits 6:4 TS: Trigger selection
This bit field selects the trigger input to be used to synchronize the counter.
000: Internal Trigger 0 (ITR0)
001: Internal Trigger 1 (ITR1)
010: Internal Trigger 2 (ITR2)
011: Internal Trigger 3 (ITR3)
100: TI1 Edge Detector (TI1F_ED)
101: Filtered Timer Input 1 (TI1FP1)
110: Filtered Timer Input 2 (TI2FP2)
111: Reserved.
See [Table 101](../tables/table_101.md) for more details on the meaning of ITRx for each timer.
Note: These bits must be changed only when they are not used (e.g. when SMS=’000’) to
avoid wrong edge detections at the transition.

General-purpose timers (TIM9 to TIM14) RM0090
670/1741 RM0090 Rev 22
19.4.3 TIM9/12 Interrupt enab le register (TIMx_DIER)
Address offset: 0x0C
Reset value: 0x0000
Bit 3 Reserved, must be kept at reset value.
Bits 2:0 SMS: Slave mode selection
When external signals are selected, the active edge of the trigger signal (TRGI) is linked to
the polarity selected on the external input (see Input control register and Control register
descriptions.
000: Slave mode disabled - if CEN = 1 then the prescaler is clocked directly by the internal
clock
001: Reserved
010: Reserved
011: Reserved
100: Reset mode - Rising edge of the selected trigger input (TRGI) reinitializes the counter
and generates an update of the registers
101: Gated mode - The counter clock is enabled when the trigger input (TRGI) is high. The
counter stops (but is not reset) as soon as the trigger becomes low. Counter starts and stops
are both controlled
110: Trigger mode - The counter starts on a rising edge of the trigger TRGI (but it is not
reset). Only the start of the counter is controlled
111: External clock mode 1 - Rising edges of the selected trigger (TRGI) clock the counter
Note: The Gated mode must not be used if TI 1F_ED is selected as the trigger input
(TS=’100’). Indeed, TI1F_ED outputs 1 pulse for each transition on TI1F, whereas the
Gated mode checks the level of the trigger signal.
Note: The clock of the slave timer must be enab led prior to receive events from the master
timer, and must not be changed on-the-fly while triggers are received from the master
timer.
[Table 101](../tables/table_101.md). TIMx internal trigger connection
Slave TIM ITR0 (TS = 000) ITR1 (TS = 001) ITR2 (TS = 010) ITR3 (TS = 011)
TIM9 TIM2_TRGO TIM3_TRGO TIM10_OC TIM11_OC
TIM12 TIM4_TRGO TIM5_TRGO TIM13_OC TIM14_OC
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved
TIE
Res
CC2IE CC1IE UIE
rw rw rw rw
Bits 15:7 Reserved, must be kept at reset value.
Bit 6 TIE: Trigger interrupt enable
0: Trigger interrupt disabled.
1: Trigger interrupt enabled.
Bit 5:3 Reserved, must be kept at reset value.

RM0090 Rev 22 671/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
Bit 2 CC2IE: Capture/Compare 2 interrupt enable
0: CC2 interrupt disabled.
1: CC2 interrupt enabled.
Bit 1 CC1IE: Capture/Compare 1 interrupt enable
0: CC1 interrupt disabled.
1: CC1 interrupt enabled.
Bit 0 UIE: Update interrupt enable
0: Update interrupt disabled.
1: Update interrupt enabled.

General-purpose timers (TIM9 to TIM14) RM0090
672/1741 RM0090 Rev 22
19.4.4 TIM9/12 status register (TIMx_SR)
Address offset: 0x10
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved
CC2OF CC1OF
Reserved
TIF
Reserved
CC2IF CC1IF UIF
rc_w0 rc_w0 rc_w0 rc_w0 rc_w0 rc_w0
Bits 15:11 Reserved, must be kept at reset value.
Bit 10 CC2OF: Capture/compare 2 overcapture flag
refer to CC1OF description
Bit 9 CC1OF: Capture/Compare 1 overcapture flag
This flag is set by hardware only when the corresponding channel is configured in input
capture mode. It is cleared by software by writing it to ‘0’.
0: No overcapture has been detected.
1: The counter value has been captured in TIMx_CCR1 register while CC1IF flag was
already set
Bits 8:7 Reserved, must be kept at reset value.
Bit 6 TIF: Trigger interrupt flag
This flag is set by hardware on trigger event (active edge detected on TRGI input when the
slave mode controller is enabled in all modes but gated mode. It is set when the counter
starts or stops when gated mode is selected. It is cleared by software.
0: No trigger event occurred.
1: Trigger interrupt pending.
Bits 5:3 Reserved, must be kept at reset value.
Bit 2 CC2IF: Capture/Compare 2 interrupt flag
refer to CC1IF description
Bit 1 CC1IF: Capture/compare 1 interrupt flag
If channel CC1 is configured as output:
This flag is set by hardware when the counter matches the compare value. It is cleared by
software.
0: No match.
1: The content of the counter TIMx_CNT matches the content of the TIMx_CCR1 register.
When the contents of TIMx_CCR1 are greater than the contents of TIMx_ARR, the CC1IF
bit goes high on the counter overflow.
If channel CC1 is configured as input:
This bit is set by hardware on a capture. It is cleared by software or by reading the
TIMx_CCR1 register.
0: No input capture occurred.
1: The counter value has been captured in TIMx_CCR1 register (an edge has been detected
on IC1 which matches the selected polarity).

RM0090 Rev 22 673/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
19.4.5 TIM9/12 event genera tion register (TIMx_EGR)
Address offset: 0x14
Reset value: 0x0000
Bit 0 UIF: Update interrupt flag
This bit is set by hardware on an update event. It is cleared by software.
0: No update occurred.
1: Update interrupt pending. This bit is set by hardware when the registers are updated:
– At overflow and if UDIS=’0’ in the TIMx_CR1 register.
– When CNT is reinitialized by software using the UG bit in TIMx_EGR register, if URS=’0’ and
UDIS=’0’ in the TIMx_CR1 register.
– When CNT is reinitialized by a trigger event (refer to the synchro control register
description), if URS=’0’ and UDIS=’0’ in the TIMx_CR1 register.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved
TG
Reserved
CC2G CC1G UG
w www
Bits 15:7 Reserved, must be kept at reset value.
Bit 6 TG: Trigger generation
This bit is set by software in order to generate an event, it is automatically cleared by
hardware.
0: No action
1: The TIF flag is set in the TIMx_SR register. Related interrupt can occur if enabled
Bits 5:3 Reserved, must be kept at reset value.
Bit 2 CC2G: Capture/compare 2 generation
refer to CC1G description
Bit 1 CC1G: Capture/compare 1 generation
This bit is set by software to generate an event, it is automatically cleared by hardware.
0: No action
1: A capture/compare event is generated on channel 1:
If channel CC1 is configured as output:
the CC1IF flag is set, the corresponding interrupt is sent if enabled.
If channel CC1 is configured as input:
The current counter value is captured in the TIMx_CCR1 register. The CC1IF flag is set, the
corresponding interrupt is sent if enabled. The CC1OF flag is set if the CC1IF flag was
already high.
Bit 0 UG: Update generation
This bit can be set by software, it is automatically cleared by hardware.
0: No action
1: Re-initializes the counter and generates an update of the registers. The prescaler counter
is also cleared and the prescaler ratio is not affected. The counter is cleared.

General-purpose timers (TIM9 to TIM14) RM0090
674/1741 RM0090 Rev 22
19.4.6 TIM9/12 capture/compare mode register 1 (TIMx_CCMR1)
Address offset: 0x18
Reset value: 0x0000
The channels can be used in input (capture mode) or in output (compare mode). The
direction of a channel is defined by configuring the corresponding CCxS bits. All the other
bits in this register have different functions in input and output modes. For a given bit, OCxx
describes its function when the channel is configured in output mode, ICxx describes its
function when the channel is configured in input mode. Take care that the same bit can have
different meanings for the input stage and the output stage.
Output compare mode
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. OC2M[2:0] OC2PE OC2FE
CC2S[1:0]
Res. OC1M[2:0] OC1PE OC1FE
CC1S[1:0]
IC2F[3:0] IC2PSC[1:0] IC1F[3:0] IC1PSC[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 15 Reserved, must be kept at reset value.
Bits 14:12 OC2M[2:0]: Output compare 2 mode
Bit 11 OC2PE: Output compare 2 preload enable
Bit 10 OC2FE: Output compare 2 fast enable
Bits 9:8 CC2S[1:0]: Capture/Compare 2 selection
This bitfield defines the direction of the channel (input/output) as well as the used input.
00: CC2 channel is configured as output
01: CC2 channel is configured as input, IC2 is mapped on TI2
10: CC2 channel is configured as input, IC2 is mapped on TI1
11: CC2 channel is configured as input, IC2 is mapped on TRC. This mode works only if an
internal trigger input is selected through the TS bit (TIMx_SMCR register
Note: The CC2S bits are writable only when the channel is OFF (CC2E = 0 in TIMx_CCER).
Bit 7 Reserved, must be kept at reset value.

RM0090 Rev 22 675/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
Bits 6:4 OC1M: Output compare 1 mode
These bits define the behavior of the output reference signal OC1REF from which OC1 and
OC1N are derived. OC1REF is active high whereas the active levels of OC1 and OC1N
depend on the CC1P and CC1NP bits, respectively.
000: Frozen - The comparison between the output compare register TIMx_CCR1 and the
counter TIMx_CNT has no effect on the outputs.(this mode is used to generate a timing
base).
001: Set channel 1 to active level on match. The OC1REF signal is forced high when the
TIMx_CNT counter matches the capture/compare register 1 (TIMx_CCR1).
010: Set channel 1 to inactive level on match. The OC1REF signal is forced low when the
TIMx_CNT counter matches the capture/compare register 1 (TIMx_CCR1).
011: Toggle - OC1REF toggles when TIMx_CNT=TIMx_CCR1
100: Force inactive level - OC1REF is forced low
101: Force active level - OC1REF is forced high
110: PWM mode 1 - In upcounting, channel 1 is active as long as TIMx_CNT<TIMx_CCR1
else it is inactive. In downcounting, channel 1 is inactive (OC1REF=‘0) as long as
TIMx_CNT>TIMx_CCR1, else it is active (OC1REF=’1’)
111: PWM mode 2 - In upcounting, channel 1 is inactive as long as TIMx_CNT<TIMx_CCR1
else it is active. In downcounting, channel 1 is active as long as TIMx_CNT>TIMx_CCR1
else it is inactive.
Note: In PWM mode 1 or 2, the OCREF leve l changes only when the result of the
comparison changes or when the output compare mode switches from “frozen” mode
to “PWM” mode.
Bit 3 OC1PE: Output compare 1 preload enable
0: Preload register on TIMx_CCR1 disabled. TIMx_CCR1 can be written at anytime, the
new value is taken into account immediately
1: Preload register on TIMx_CCR1 enabled. Read/Write operations access the preload
register. TIMx_CCR1 preload value is loaded into the active register at each update event
Bit 2 OC1FE: Output compare 1 fast enable
This bit is used to accelerate the effect of an event on the trigger in input on the CC output.
0: CC1 behaves normally depending on the counter and CCR1 values even when the
trigger is ON. The minimum delay to activate the CC1 output when an edge occurs on the
trigger input is 5 clock cycles
1: An active edge on the trigger input acts like a compare match on the CC1 output. Then,
OC is set to the compare level independently of the result of the comparison. Delay to
sample the trigger input and to activate CC1 output is reduced to 3 clock cycles. OC1FE
acts only if the channel is configured in PWM1 or PWM2 mode.
Bits 1:0 CC1S: Capture/Compare 1 selection
This bitfield defines the direction of the channel (input/output) as well as the used input.
00: CC1 channel is configured as output
01: CC1 channel is configured as input, IC1 is mapped on TI1
10: CC1 channel is configured as input, IC1 is mapped on TI2
11: CC1 channel is configured as input, IC1 is mapped on TRC. This mode works only if an
internal trigger input is selected through the TS bit (TIMx_SMCR register)
Note: The CC1S bits are writable only when the channel is OFF (CC1E = 0 in TIMx_CCER).

General-purpose timers (TIM9 to TIM14) RM0090
676/1741 RM0090 Rev 22
Input capture mode
Bits 15:12 IC2F: Input capture 2 filter
Bits 11:10 IC2PSC[1:0]: Input capture 2 prescaler
Bits 9:8 CC2S: Capture/compare 2 selection
This bitfield defines the direction of the channel (input/output) as well as the used input.
00: CC2 channel is configured as output
01: CC2 channel is configured as input, IC2 is mapped on TI2
10: CC2 channel is configured as input, IC2 is mapped on TI1
11: CC2 channel is configured as input, IC2 is mapped on TRC. This mode works only if an
internal trigger input is selected through the TS bit (TIMx_SMCR register)
Note: The CC2S bits are writable only when the channel is OFF (CC2E = 0 in TIMx_CCER).
Bits 7:4 IC1F: Input capture 1 filter
This bitfield defines the frequency used to sample the TI1 input and the length of the digital
filter applied to TI1. The digital filter is made of an event counter in which N consecutive
events are needed to validate a transition on the output:
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
Bits 3:2 IC1PSC: Input capture 1 prescaler
This bitfield defines the ratio of the prescaler acting on the CC1 input (IC1).
The prescaler is reset as soon as CC1E=’0’ (TIMx_CCER register).
00: no prescaler, capture is done each time an edge is detected on the capture input
01: capture is done once every 2 events
10: capture is done once every 4 events
11: capture is done once every 8 events
Bits 1:0 CC1S: Capture/Compare 1 selection
This bitfield defines the direction of the channel (input/output) as well as the used input.
00: CC1 channel is configured as output
01: CC1 channel is configured as input, IC1 is mapped on TI1
10: CC1 channel is configured as input, IC1 is mapped on TI2
11: CC1 channel is configured as input, IC1 is mapped on TRC. This mode is working only if
an internal trigger input is selected through TS bit (TIMx_SMCR register)
Note: The CC1S bits are writable only when the channel is OFF (CC1E = 0 in TIMx_CCER).

RM0090 Rev 22 677/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
19.4.7 TIM9/12 capture/compare enable register (TIMx_CCER)
Address offset: 0x20
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved
CC2NP
Res.
CC2P CC2E CC1NP
Res.
CC1P CC1E
rw rw rw rw rw rw
Bits 15:8 Reserved, must be kept at reset value.
Bit 7 CC2NP: Capture/Compare 2 output Polarity
refer to CC1NP description
Bits 6 Reserved, must be kept at reset value.
Bit 5 CC2P: Capture/Compare 2 output Polarity
refer to CC1P description
Bit 4 CC2E: Capture/Compare 2 output enable
refer to CC1E description
Bit 3 CC1NP: Capture/Compare 1 complementary output Polarity
CC1 channel configured as output: CC1NP must be kept cleared
CC1 channel configured as input: CC1NP is used in conjunction with CC1P to define
TI1FP1/TI2FP1 polarity (refer to CC1P description).
Bit 2 Reserved, must be kept at reset value.
Bit 1 CC1P: Capture/Compare 1 output Polarity.
CC1 channel configured as output:
0: OC1 active high.
1: OC1 active low.
CC1 channel configured as input:
CC1NP/CC1P bits select TI1FP1 and TI2FP1 polarity for trigger or capture operations.
00: noninverted/rising edge
Circuit is sensitive to TIxFP1 rising edge (capture, trigger in reset, external clock or trigger
mode), TIxFP1 is not inverted (trigger in gated mode, encoder mode).
01: inverted/falling edge
Circuit is sensitive to TIxFP1 falling edge (capture, trigger in reset, external clock or trigger
mode), TIxFP1 is inverted (trigger in gated mode, encoder mode).
10: reserved, do not use this configuration.
Note: 11: noninverted/both edges
Circuit is sensitive to both TIxFP1 rising and falling edges (capture, trigger in reset,
external clock or trigger mode), TIxFP1 is not inverted (trigger in gated mode). This
configuration must not be used for encoder mode.
Bit 0 CC1E: Capture/Compare 1 output enable.
CC1 channel configured as output:
0: Off - OC1 is not active.
1: On - OC1 signal is output on the corresponding output pin.
CC1 channel configured as input:
This bit determines if a capture of the counter value can actually be done into the input
capture/compare register 1 (TIMx_CCR1) or not.
0: Capture disabled.
1: Capture enabled.

General-purpose timers (TIM9 to TIM14) RM0090
678/1741 RM0090 Rev 22
Note: The states of the external I/O pins connec ted to the standard OCx channels depend on the
state of the OCx channel and on the GPIO registers.
19.4.8 TIM9/12 counter (TIMx_CNT)
Address offset: 0x24
Reset value: 0x0000
19.4.9 TIM9/12 prescaler (TIMx_PSC)
Address offset: 0x28
Reset value: 0x0000
19.4.10 TIM9/12 auto-rel oad register (TIMx_ARR)
Address offset: 0x2C
Reset value: 0xFFFF
[Table 102](../tables/table_102.md). Output control bit for standard OCx channels
CCxE bit OCx output state
0 Output disabled (OCx=’0’, OCx_EN=’0’)
1 OCx=OCxREF + Polarity, OCx_EN=’1’
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CNT[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 CNT[15:0]: Counter value
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PSC[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 PSC[15:0]: Prescaler value
The counter clock frequency CK_CNT is equal to fCK_PSC / (PSC[15:0] + 1).
PSC contains the value to be loaded in the active prescaler register at each update event
(including when the counter is cleared through UG bit of TIMx_EGR register or through
trigger controller when configured in “reset mode”).
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ARR[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 ARR[15:0]: Auto-reload value
ARR is the value to be loaded into the actual auto-reload register.
Refer to the Section 19.3.1: Time-base unit for more details about ARR update and
behavior.
The counter is blocked while the auto-reload value is null.

RM0090 Rev 22 679/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
19.4.11 TIM9/12 capture/compare register 1 (TIMx_CCR1)
Address offset: 0x34
Reset value: 0x0000
19.4.12 TIM9/12 capture/compare register 2 (TIMx_CCR2)
Address offset: 0x38
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CCR1[15:0]
rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro
Bits 15:0 CCR1[15:0]: Capture/Compare 1 value
If channel CC1 is configured as output:
CCR1 is the value to be loaded into the actual capture/compare 1 register (preload value).
It is loaded permanently if the preload feature is not selected in the TIMx_CCMR1 register
(OC1PE bit). Else the preload value is copied into the active capture/compare 1 register
when an update event occurs.
The active capture/compare register contains the value to be compared to the TIMx_CNT
counter and signaled on the OC1 output.
If channel CC1is configured as input:
CCR1 is the counter value transferred by the last input capture 1 event (IC1). The
TIMx_CCR1 register is read-only and cannot be programmed.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CCR2[15:0]
rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro
Bits 15:0 CCR2[15:0]: Capture/Compare 2 value
If channel CC2 is configured as output:
CCR2 is the value to be loaded into the actual capture/compare 2 register (preload value).
It is loaded permanently if the preload feature is not selected in the TIMx_CCMR2 register
(OC2PE bit). Else the preload value is copied into the active capture/compare 2 register
when an update event occurs.
The active capture/compare register contains the value to be compared to the TIMx_CNT
counter and signalled on the OC2 output.
If channel CC2 is configured as input:
CCR2 is the counter value transferred by the last input capture 2 event (IC2). The
TIMx_CCR2 register is read-only and cannot be programmed.

General-purpose timers (TIM9 to TIM14) RM0090
680/1741 RM0090 Rev 22
19.4.13 TIM9/12 register map
TIM9/12 registers are mapped as 16-bit addressable registers as described below. The
reserved memory areas are highlighted in gray in the table.
[Table 103](../tables/table_103.md). TIM9/12 register map and reset values
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
TIMx_CR1
Reserved
CKD
[1:0]
ARPEReserved
OPM
URS
UDIS
CEN
Reset value 000 0000
0x08
TIMx_SMCR
Reserved
MSM
TS[2:0]
Reserved
SMS[2:0]
Reset value 0000 000
0x0C
TIMx_DIER
Reserved
TIEReserved
CC2IE
CC1IE
UIE
Reset value 00 0 0
0x10
TIMx_SR
Reserved
CC2OF
CC1OF
Reserved
TIFReserved
CC2IF
CC1IF
UIF
Reset value 00 0 000
0x14
TIMx_EGR
Reserved
TGReserved
CC2G
CC1G
UG
Reset value 00 0 0
0x18
TIMx_CCMR1
Output compare
mode Reserved
OC2M
[2:0]
OC2PE
OC2FE
CC2S
[1:0]
Reserved
OC1M
[2:0]
OC1PE
OC1FE
CC1
S
[1:0]
Reset value 0 0 0 0 0 0 0 0 0 0 0 0 0 0
TIMx_CCMR1
Input capture
mode Reserved
IC2F[3:0]
IC2
PSC
[1:0]
CC2S
[1:0] IC1F[3:0]
IC1
PSC
[1:0]
CC1
S
[1:0]
Reset value 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0x1C Reserved
0x20
TIMx_CCER
Reserved
CC2NP
Reserved
CC2P
CC2E
CC1NP
Reserved
CC1P
CC1E
Reset value 00 0 00 0
0x24
TIMx_CNT
Reserved
CNT[15:0]
Reset value 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0x28
TIMx_PSC
Reserved
PSC[15:0]
Reset value 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0x2C
TIMx_ARR
Reserved
ARR[15:0]
Reset value 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0x30 Reserved
0x34
TIMx_CCR1
Reserved
CCR1[15:0]
Reset value 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

RM0090 Rev 22 681/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
Refer to Section 2.3: Memory map for the register boundary addresses.
0x38
TIMx_CCR2
Reserved
CCR2[15:0]
Reset value 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0x3C to
0x4C Reserved
[Table 103](../tables/table_103.md). TIM9/12 register map and reset values (continued)
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

General-purpose timers (TIM9 to TIM14) RM0090
682/1741 RM0090 Rev 22
19.5 TIM10/11/13/14 registers
The peripheral registers have to be written by half-words (16 bits) or words (32 bits). Read
accesses can be done by bytes (8 bits), half-words (16 bits) or words (32 bits).
19.5.1 TIM10/11/13/14 contro l register 1 (TIMx_CR1)
Address offset: 0x00
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved
CKD[1:0] ARPE
Reserved
OPM URS UDIS CEN
rw rw rw rw rw rw rw
Bits 15:10 Reserved, must be kept at reset value.
Bits 9:8 CKD: Clock division
This bit-field indicates the division ratio between the timer clock (CK_INT) frequency and
sampling clock used by the digital filters (TIx),
00: tDTS = tCK_INT
01: tDTS = 2 × tCK_INT
10: tDTS = 4 × tCK_INT
11: Reserved
Bit 7 ARPE: Auto-reload preload enable
0: TIMx_ARR register is not buffered
1: TIMx_ARR register is buffered
Bits 6:4 Reserved, must be kept at reset value.
Bit 3 OPM: One-pulse mode
0: Counter is not stopped on the update event
1: Counter stops counting on the next update event (clearing the CEN bit).
Bit 2 URS: Update request source
This bit is set and cleared by software to select the update interrupt (UEV) sources.
0: Any of the following events generate an UEV if enabled:
– Counter overflow
– Setting the UG bit
1: Only counter overflow generates an UEV if enabled.
Bit 1 UDIS: Update disable
This bit is set and cleared by software to enable/disable update interrupt (UEV) event
generation.
0: UEV enabled. An UEV is generated by one of the following events:
– Counter overflow
– Setting the UG bit.
Buffered registers are then loaded with their preload values.
1: UEV disabled. No UEV is generated, shadow registers keep their value (ARR, PSC,
CCRx). The counter and the prescaler are reinitialized if the UG bit is set.
Bit 0 CEN: Counter enable
0: Counter disabled
1: Counter enabled

RM0090 Rev 22 683/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
19.5.2 TIM10/11/13/14 Interrupt enable register (TIMx_DIER)
Address offset: 0x0C
Reset value: 0x0000
19.5.3 TIM10/11/13/14 stat us register (TIMx_SR)
Address offset: 0x10
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved
CC1IE UIE
rw rw
Bits 15:2 Reserved, must be kept at reset value.
Bit 1 CC1IE: Capture/Compare 1 interrupt enable
0: CC1 interrupt disabled
1: CC1 interrupt enabled
Bit 0 UIE: Update interrupt enable
0: Update interrupt disabled
1: Update interrupt enabled
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved
CC1OF
Reserved
CC1IF UIF
rc_w0 rc_w0 rc_w0
Bits 15:10 Reserved, must be kept at reset value.
Bit 9 CC1OF: Capture/Compare 1 overcapture flag
This flag is set by hardware only when the corresponding channel is configured in input
capture mode. It is cleared by software by writing it to ‘0’.
0: No overcapture has been detected.
1: The counter value has been captured in TIMx_CCR1 register while CC1IF flag was
already set
Bits 8:2 Reserved, must be kept at reset value.
Bit 1 CC1IF: Capture/compare 1 interrupt flag
If channel CC1 is configured as output:
This flag is set by hardware when the counter matches the compare value. It is cleared by
software.
0: No match.
1: The content of the counter TIMx_CNT matches the content of the TIMx_CCR1 register.
When the contents of TIMx_CCR1 are greater than the contents of TIMx_ARR, the CC1IF bit
goes high on the counter overflow.
If channel CC1 is configured as input:
This bit is set by hardware on a capture. It is cleared by software or by reading the
TIMx_CCR1 register.
0: No input capture occurred.
1: The counter value has been captured in TIMx_CCR1 register (an edge has been detected
on IC1 which matches the selected polarity).

General-purpose timers (TIM9 to TIM14) RM0090
684/1741 RM0090 Rev 22
19.5.4 TIM10/11/13/14 event ge neration register (TIMx_EGR)
Address offset: 0x14
Reset value: 0x0000
19.5.5 TIM10/11/13/14 capture/compar e mode register 1 (TIMx_CCMR1)
Address offset: 0x18
Reset value: 0x0000
The channels can be used in input (capture mode) or in output (compare mode). The
direction of a channel is defined by configuring the corresponding CCxS bits. All the other
bits of this register have a different function in input and in output mode. For a given bit,
OCxx describes its function when the channel is configured in output, ICxx describes its
function when the channel is configured in input. So take care that the same bit can have a
different meaning for the input stage and for the output stage.
Bit 0 UIF: Update interrupt flag
This bit is set by hardware on an update event. It is cleared by software.
0: No update occurred.
1: Update interrupt pending. This bit is set by hardware when the registers are updated:
– At overflow and if UDIS=’0’ in the TIMx_CR1 register.
– When CNT is reinitialized by software us ing the UG bit in TIMx_EGR register, if
URS=’0’ and UDIS=’0’ in the TIMx_CR1 register.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved
CC1G UG
ww
Bits 15:2 Reserved, must be kept at reset value.
Bit 1 CC1G: Capture/compare 1 generation
This bit is set by software in order to generate an event, it is automatically cleared by
hardware.
0: No action
1: A capture/compare event is generated on channel 1:
If channel CC1 is configured as output:
CC1IF flag is set, Corresponding interrupt or is sent if enabled.
If channel CC1 is configured as input:
The current value of the counter is captured in TIMx_CCR1 register. The CC1IF flag is set,
the corresponding interrupt is sent if enabled. The CC1OF flag is set if the CC1IF flag was
already high.
Bit 0 UG: Update generation
This bit can be set by software, it is automatically cleared by hardware.
0: No action
1: Re-initialize the counter and generates an update of the registers. Note that the prescaler
counter is cleared too (anyway the prescaler ratio is not affected). The counter is cleared.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved OC1M[2:0] OC1PE OC1FE
CC1S[1:0]
Reserved
IC1F[3:0] IC1PSC[1:0]
rw rw rw rw rw rw rw rw

RM0090 Rev 22 685/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
Output compare mode
Bits 15:7 Reserved, must be kept at reset value.
Bits 6:4 OC1M: Output compare 1 mode
These bits define the behavior of the output reference signal OC1REF from which OC1 is
derived. OC1REF is active high whereas OC1 active level depends on CC1P bit.
000: Frozen. The comparison between the output compare register TIMx_CCR1 and the
counter TIMx_CNT has no effect on the outputs.
001: Set channel 1 to active level on match. OC1REF signal is forced high when the counter
TIMx_CNT matches the capture/compare register 1 (TIMx_CCR1).
010: Set channel 1 to inactive level on match. OC1REF signal is forced low when the
counter TIMx_CNT matches the capture/compare register 1 (TIMx_CCR1).
011: Toggle - OC1REF toggles when TIMx_CNT = TIMx_CCR1.
100: Force inactive level - OC1REF is forced low.
101: Force active level - OC1REF is forced high.
110: PWM mode 1 - Channel 1 is active as long as TIMx_CNT < TIMx_CCR1 else inactive.
111: PWM mode 2 - Channel 1 is inactive as long as TIMx_CNT < TIMx_CCR1 else active.
Note: In PWM mode 1 or 2, the OCREF level changes when the result of the comparison
changes or when the output compare mode switches from frozen to PWM mode.
Bit 3 OC1PE: Output compare 1 preload enable
0: Preload register on TIMx_CCR1 disabled. TIMx_CCR1 can be written at anytime, the
new value is taken in account immediately.
1: Preload register on TIMx_CCR1 enabled. Read/Write operations access the preload
register. TIMx_CCR1 preload value is loaded in the active register at each update event.
Bit 2 OC1FE: Output compare 1 fast enable
This bit is used to accelerate the effect of an event on the trigger in input on the CC output.
0: CC1 behaves normally depending on counter and CCR1 values even when the trigger is
ON. The minimum delay to activate CC1 output when an edge occurs on the trigger input is
5 clock cycles.
1: An active edge on the trigger input acts like a compare match on CC1 output. OC is then
set to the compare level independently of the result of the comparison. Delay to sample the
trigger input and to activate CC1 output is reduced to 3 clock cycles. OC1FE acts only if the
channel is configured in PWM1 or PWM2 mode.
Bits 1:0 CC1S: Capture/Compare 1 selection
This bit-field defines the direction of the channel (input/output) as well as the used input.
00: CC1 channel is configured as output.
01: CC1 channel is configured as input, IC1 is mapped on TI1.
10:
11:
Note: CC1S bits are writable only when the channel is OFF (CC1E = 0 in TIMx_CCER).

General-purpose timers (TIM9 to TIM14) RM0090
686/1741 RM0090 Rev 22
Input capture mode
Bits 15:8 Reserved, must be kept at reset value.
Bits 7:4 IC1F: Input capture 1 filter
This bit-field defines the frequency used to sample TI1 input and the length of the digital filter
applied to TI1. The digital filter is made of an event counter in which N consecutive events
are needed to validate a transition on the output:
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
Bits 3:2 IC1PSC: Input capture 1 prescaler
This bit-field defines the ratio of the prescaler acting on CC1 input (IC1).
The prescaler is reset as soon as CC1E=’0’ (TIMx_CCER register).
00: no prescaler, capture is done each time an edge is detected on the capture input
01: capture is done once every 2 events
10: capture is done once every 4 events
11: capture is done once every 8 events
Bits 1:0 CC1S: Capture/Compare 1 selection
This bit-field defines the direction of the channel (input/output) as well as the used input.
00: CC1 channel is configured as output
01: CC1 channel is configured as input, IC1 is mapped on TI1
10: Reserved
11: Reserved
Note: CC1S bits are writable only when the channel is OFF (CC1E = 0 in TIMx_CCER).

RM0090 Rev 22 687/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
19.5.6 TIM10/11/13/14 capture/comp are enable register (TIMx_CCER)
Address offset: 0x20
Reset value: 0x0000
Note: The state of the external I/O pins connec ted to the standard OCx channels depends on the
OCx channel state and the GPIO registers.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved
CC1NP
Res.
CC1P CC1E
rw rw rw
Bits 15:4 Reserved, must be kept at reset value.
Bit 3 CC1NP: Capture/Compare 1 complementary output Polarity.
CC1 channel configured as output: CC1NP must be kept cleared.
CC1 channel configured as input: CC1NP bit is used in conjunction with CC1P to define
TI1FP1 polarity (refer to CC1P description).
Bit 2 Reserved, must be kept at reset value.
Bit 1 CC1P: Capture/Compare 1 output Polarity.
CC1 channel configured as output:
0: OC1 active high
1: OC1 active low
CC1 channel configured as input:
The CC1P bit selects TI1FP1 and TI2FP1 polarity for trigger or capture operations.
00: noninverted/rising edge
Circuit is sensitive to TI1FP1 rising edge (capture mode), TI1FP1 is not inverted.
01: inverted/falling edge
Circuit is sensitive to TI1FP1 falling edge (capture mode), TI1FP1 is inverted.
10: reserved, do not use this configuration.
11: noninverted/both edges
Circuit is sensitive to both TI1FP1 rising and falling edges (capture mode), TI1FP1 is not
inverted.
Bit 0 CC1E: Capture/Compare 1 output enable.
CC1 channel configured as output:
0: Off - OC1 is not active
1: On - OC1 signal is output on the corresponding output pin
CC1 channel configured as input:
This bit determines if a capture of the counter value can actually be done into the input
capture/compare register 1 (TIMx_CCR1) or not.
0: Capture disabled
1: Capture enabled
[Table 104](../tables/table_104.md). Output control bit for standard OCx channels
CCxE bit OCx output state
0 Output Disabled (OCx=’0’, OCx_EN=’0’)
1 OCx=OCxREF + Polarity, OCx_EN=’1’

General-purpose timers (TIM9 to TIM14) RM0090
688/1741 RM0090 Rev 22
19.5.7 TIM10/11/13/14 counter (TIMx_CNT)
Address offset: 0x24
Reset value: 0x0000
19.5.8 TIM10/11/13/14 prescaler (TIMx_PSC)
Address offset: 0x28
Reset value: 0x0000
19.5.9 TIM10/11/13/14 auto-reload register (TIMx_ARR)
Address offset: 0x2C
Reset value: 0xFFFF
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CNT[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 CNT[15:0]: Counter value
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PSC[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 PSC[15:0]: Prescaler value
The counter clock frequency CK_CNT is equal to fCK_PSC / (PSC[15:0] + 1).
PSC contains the value to be loaded in the active prescaler register at each update event
(including when the counter is cleared through UG bit of TIMx_EGR register or through
trigger controller when configured in “reset mode”).
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ARR[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 ARR[15:0]: Auto-reload value
ARR is the value to be loaded in the actual auto-reload register.
Refer to Section 19.3.1: Time-base unit for more details about ARR update and behavior.
The counter is blocked while the auto-reload value is null.

RM0090 Rev 22 689/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
19.5.10 TIM10/11/13/14 capture/ compare register 1 (TIMx_CCR1)
Address offset: 0x34
Reset value: 0x0000
19.5.11 TIM11 option re gister 1 (TIM11_OR)
Address offset: 0x50
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CCR1[15:0]
rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro rw/ro
Bits 15:0 CCR1[15:0]: Capture/Compare 1 value
If channel CC1 is configured as output:
CCR1 is the value to be loaded in the actual capture/compare 1 register (preload value).
It is loaded permanently if the preload feature is not selected in the TIMx_CCMR1 register (bit
OC1PE). Else the preload value is copied in the active capture/compare 1 register when an
update event occurs.
The active capture/compare register contains the value to be compared to the counter
TIMx_CNT and signaled on OC1 output.
If channel CC1is configured as input:
CCR1 is the counter value transferred by the last input capture 1 event (IC1). The TIMx_CCR1
register is read-only and cannot be programmed.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Reserved
TI1_RMP[1:0]
rw
Bits 15:2 Reserved, must be kept at reset value.
Bits 1:0 TI1_RMP[1:0]: TIM11 Input 1 remapping capability
Set and cleared by software.
00,01,11: TIM11 Channel1 is connected to the GPIO (refer to the Alternate function mapping
table in the datasheets).
10: HSE_RTC clock (HSE divided by programmable prescaler) is connected to the
TIM11_CH1 input for measurement purposes

General-purpose timers (TIM9 to TIM14) RM0090
690/1741 RM0090 Rev 22
19.5.12 TIM10/11/13/14 register map
TIMx registers are mapped as 16-bit addressable registers as described in the table below.
[Table 105](../tables/table_105.md). TIM10/11/13/14 register map and reset values
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
TIMx_CR1
Reserved
CKD
[1:0]
ARPE
Reserve
d
OPM
URS
UDIS
CEN
Reset value 000 000 0
0x08
TIMx_SMCR
Reserved
Reset value
0x0C
TIMx_DIER
Reserved
CC1IE
UIE
Reset value 00
0x10
TIMx_SR
Reserved
CC1OF Reserved
CC1IF
UIF
Reset value 00 0
0x14
TIMx_EGR
Reserved
CC1G
UG
Reset value 00
0x18
TIMx_CCMR1
Output compare
mode Reserved
OC1M
[2:0]
OC1PE
OC1FE
CC1S
[1:0]
Reset value 000000 0
TIMx_CCMR1
Input capture
mode Reserved
IC1F[3:0]
IC1
PSC
[1:0]
CC1S
[1:0]
Reset value 0000000 0
0x1C Reserved
0x20
TIMx_CCER
Reserved
CC1NP
Reserved
CC1P
CC1E
Reset value 00 0
0x24
TIMx_CNT
Reserved
CNT[15:0]
R e s e t  v a l u e 000000000000000 0
0x28
TIMx_PSC
Reserved
PSC[15:0]
R e s e t  v a l u e 000000000000000 0
0x2C
TIMx_ARR
Reserved
ARR[15:0]
R e s e t  v a l u e 000000000000000 0
0x30 Reserved
0x34
TIMx_CCR1
Reserved
CCR1[15:0]
R e s e t  v a l u e 000000000000000 0
0x38 to
0x4C Reserved

RM0090 Rev 22 691/1741
RM0090 General-purpose timers (TIM9 to TIM14)
691
Refer to Section 2.3: Memory map for the register boundary addresses.
0x50
TIMx_OR
Reserved
TI1_RMP
Reset value 00
[Table 105](../tables/table_105.md). TIM10/11/13/14 register map and reset values (continued)
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
* [Figure 180: Architectural Diagram](../figures/figure_180.md)
* [Figure 181: Architectural Diagram](../figures/figure_181.md)
* [Figure 182: Architectural Diagram](../figures/figure_182.md)
* [Figure 183: Architectural Diagram](../figures/figure_183.md)
* [Figure 184: Architectural Diagram](../figures/figure_184.md)
* [Figure 185: Architectural Diagram](../figures/figure_185.md)
* [Figure 186: Architectural Diagram](../figures/figure_186.md)
* [Figure 187: Architectural Diagram](../figures/figure_187.md)
* [Figure 188: Architectural Diagram](../figures/figure_188.md)
* [Figure 189: Architectural Diagram](../figures/figure_189.md)
* [Figure 190: Architectural Diagram](../figures/figure_190.md)
* [Figure 191: Architectural Diagram](../figures/figure_191.md)
* [Figure 192: Architectural Diagram](../figures/figure_192.md)
* [Figure 193: Architectural Diagram](../figures/figure_193.md)
* [Figure 194: Architectural Diagram](../figures/figure_194.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 101: Configuration Matrix](../tables/table_101.md)
* [Table 102: Configuration Matrix](../tables/table_102.md)
* [Table 103: Configuration Matrix](../tables/table_103.md)
* [Table 104: Configuration Matrix](../tables/table_104.md)
* [Table 105: Configuration Matrix](../tables/table_105.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)