# Chapter 13: Peripherals interconnect matrix

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 13: Peripherals interconnect matrix.
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 469 - 477
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 469/2187
RM0438 Peripherals interconnect matrix
477
13 Peripherals interconnect matrix
13.1 Introduction
Several peripherals have direct connections between them.
This allows autonomous communication and or synchronization between peripherals,
saving CPU resources thus power supply consumption.
In addition, these hardware connections remove software latency and allow design of
predictable system.
Depending on peripherals, these interconnections can operate in Run, Sleep, Low-power
run and sleep, Stop 0, Stop 1 and Stop 2 modes.
13.2 Connection summary
[Table 95](../tables/table_95.md). STM32L552xx and STM32L562xx peripherals interconnect matrix(1) (2)
Source
Destination
TIM1
TIM8
TIM2
TIM3
TIM4
TIM5
TIM6
TIM7
TIM15
TIM16
TIM17
LPTIM1
LPTIM2
LPTIM3
ADC1
ADC2
DFSDM1
OPAMP1
OPAMP2
DAC1
DAC2
COMP1
COMP2
IRTIM
TIM1 - 1111 - - - 1 - - - - - 225 - - - - 9 - -
TIM8 - - 1 - 11 - - - - - - - - 225 - - 44 - 9 -
TIM2 11 - 111 - - - - - - - - 22 - - - 449 - -
TIM3 1 - 1 - 11 - - 1 - - - - - 225 - - - - 99 -
TIM4 1111 - 1 - - - - - - - - 225 - - 44 - - -
TIM5 - 1 - - - - - - - - - - - - - - - - - 44 - - -
TIM6 - - - - - - - - - - - - - - 225 - - 44 - - -
TIM7 - - - - - - - - - - - - - - - - 5 - - 44 - - -
TIM15 1 - - 1 - - - - - - - - - - 22 - - - - - - 9 -
TIM16 - - - - - - - - 1 - - - - - - - 5 - - - - - - 15
TIM17 - - - - - - - - 1 - - - - - - - - - - - - - - 15
LPTIM1 - - - - - - - - - - - - - - - - 5 - - - - - - -
LPTIM2 - - - - - - - - - - - - - - - - - - - - - - - -
LPTIM3 - - - - - - - - - - - - - - - - - - - - - - - -
ADC1 3 - - - - - - - - - - - - - - - 16 - - - - - - -
ADC2 3 - - - - - - - - - - - - - - - 16 - - - - - - -
DFSDM1 66 - - - - - - 666 - - - - - - - - - - - - -
T. Sensor - - - - - - - - - - - - - - 12 12 - - - - - - - -
VBAT - - - - - - - - - - - - - - 12 12 - - - - - - - -
VREFINT - - - - - - - - - - - - - - 12 12 - - - - - - - -

Peripherals interconnect matrix RM0438
470/2187 RM0438 Rev 8
13.3 Interconnection details
13.3.1 From timer (TIM1/TIM2/TIM3/TI M4/TIM5/TIM8/TIM15/TIM16/TIM17) to
timer (TIM1/TIM2/TIM3/TIM4/TIM5/TIM8/TIM15)
Purpose
Some of the TIMx timers are linked together internally for timer synchronization or chaining.
When one timer is configured in Master Mode, it can reset, start, stop or clock the counter of
another timer configured in Slave Mode.
A description of the feature is provided in: Section 34.3.19: Timer synchronization.
The modes of synchronization are detailed in:
• Section 33.3.26: Timer synchronization for advanced-control timers (TIM1/TIM8)
• Section 34.3.18: Timers and external trigger synchronization for general-purpose
timers (TIM2/TIM3/TIM4/TIM5)
• Section 35.4.20: External trigger synchronization (TIM15 only) for general-purpose
timer (TIM15)
OPAMP1 - - - - - - - - - - - - - - 12 12 - - - - - - - -
OPAMP2 - - - - - - - - - - - - - - 12 12 - - - - - - - -
DAC1 - - - - - - - - - - - - - - - - - 12 12 - - - - -
DAC2 - - - - - - - - - - - - - - - - - - - - - - - -
HSE - - - - - - - - - - 7 - - - - - - - - - - - - -
LSE - - 7 - - - - - 77 - - - - - - - - - - - - - -
MSI - - - - - - - - - - 7 - - - - - - - - - - - - -
LSI - - - - - - - - - 7 - - - - - - - - - - - - - -
MCO - - - - - - - - - - 7 - - - - - - - - - - - - -
EXTI - - - - - - - - - - - - - - 225 - - 44 - - -
RTC - - - - - - - - - 7 - 888 - - - - - - - - - -
COMP1 13 13 13 13 - - - - 13 13 13 8 8 8 - - - - - - - - - -
COMP2 13 13 13 13 - - - - 13 13 13 8 8 8 - - - - - - - - - -
SYST ERR 14 14 - - - - - - 14 14 14 - - - - - - - - - - - - -
USB - - 11 - - - - - - - - - - - - - - - - - - - - -
1. Numbers in table are links to corresponding detailed sub-section in Section 13.3: Interconnection details.
2.  The “-” symbol in grayed cells means no interconnect.
[Table 95](../tables/table_95.md). STM32L552xx and STM32L562xx peripherals interconnect matrix(1) (2) (continued)
Source
Destination
TIM1
TIM8
TIM2
TIM3
TIM4
TIM5
TIM6
TIM7
TIM15
TIM16
TIM17
LPTIM1
LPTIM2
LPTIM3
ADC1
ADC2
DFSDM1
OPAMP1
OPAMP2
DAC1
DAC2
COMP1
COMP2
IRTIM

RM0438 Rev 8 471/2187
RM0438 Peripherals interconnect matrix
477
Triggering signals
The output (from Master) is on signal TIMx_TRGO (and TIMx_TRGO2 for TIM1/TIM8)
following a configurable timer event.
The input (to slave) is on signals TIMx_ITR0/ITR1/ITR2/ITR3
The input and output signals for TIM1/TIM8 are shown in [Figure 230](../figures/figure_230.md): Advanced-control
timer block diagram.
The possible master/slave connections are given in:
• [Table 280](../tables/table_280.md): TIMx internal trigger connection
• [Table 285](../tables/table_285.md): TIMx internal trigger connection
• [Table 289](../tables/table_289.md): TIMx Internal trigger connection
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
13.3.2 From timer (TIM1/TIM2/TIM3/TIM4 /TIM6/TIM8/TIM15) and EXTI to ADC
(ADC1/ADC2)
Purpose
General-purpose timers (TIM2/TIM3/TIM4), basic timer (TIM6), advanced-control timers
(TIM1/TIM8), general-purpose timer (TIM15) and EXTI can be used to generate an ADC
triggering event.
TIMx synchronization is described in: Section 33.3.27: ADC synchronization (TIM1/TIM8).
ADC synchronization is described in: Section 21.4.18: Conversion on external trigger and
trigger polarity (EXTSEL, EXTEN, JEXTSEL, JEXTEN).
Triggering signals
The output (from timer) is on signal TIMx_TRGO, TIMx_TRGO2 or TIMx_CCx event.
The input (to ADC) is on signal EXT[15:0], JEXT[15:0].
The connection between timers and ADC is provided in:
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
13.3.3 From ADC1/ADC2 to timer (TIM1/TIM8)
Purpose
ADC1/ADC2 can provide trigger event through watchdog signals to advanced-control timers
(TIM1/TIM8).
A description of the ADC analog watchdog setting is provided in: .
Trigger settings on the timer are provided in: Section 33.3.4: External trigger input.

Peripherals interconnect matrix RM0438
472/2187 RM0438 Rev 8
Triggering signals
The output (from ADC) is on signals ADCn_AWDx_OUT n = 1 (for ADC1,2) x = 1, 2, 3 (3
watchdog per ADC) and the input (to timer) on signal TIMx_ETR (external trigger).
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
13.3.4 From timer (TIM2/TIM4/TIM5/ TIM6/TIM7/TIM8) and EXTI to DAC
(DAC1/DAC2)
Purpose
General-purpose timers (TIM2/TIM4/TIM5), basic timers (TIM6, TIM7), advanced-control
timers (TIM8) and EXTI can be used as triggering event to start a DAC conversion.
Triggering signals
The output (from timer) is on signal TIMx_TRGO directly connected to corresponding DAC
inputs.
Selection of input triggers on DAC is provided in Section 22.4.6: DAC trigger selection
(single and dual mode).
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
13.3.5 From timer (TIM1/TIM3/TIM 4/TIM6/TIM7/TIM8/TIM16/LPTIM1)
and EXTI to DFSDM1
Purpose
General-purpose timers (TIM3/TIM4), basic timers (TIM6/TIM7), advanced-control timers
(TIM1/TIM8), general-purpose timer (TIM16), Low power timer (LPTIM1), EXTI11 and
EXTI15 can be used to generate a triggering event on DFSDM1 module (on each possible
data block DFSDM1_FLT0/DFSDM1_FLT1/DFSDM1_FLT2/DFSDM1_FLT3) and start an
ADC conversion.
DFSDM triggered conversion feature is described in: Section 26.4.15: Launching
conversions.
Triggering signals
The output (from timer) is on signal TIMx_TRGO/TIMx_TRGO2 or TIM16_OC1.
The input (on DFSDM1) is on signal DFSDM1_INTRG[0:8].
The connection between timers, EXTI and DFSDM1 is provided in [Table 209](../tables/table_209.md): DFSDM
triggers connection.
Active power mode
Run, Sleep, Low-power run, Low-power sleep.

RM0438 Rev 8 473/2187
RM0438 Peripherals interconnect matrix
477
13.3.6 From DFSDM1 to timer (TIM1/TIM8/TIM15/TIM16/TIM17)
Purpose
DFSDM1 can generate a timer break on advanced-control timers (TIM1/TIM8) and general-
purpose timers (TIM15/TIM16/TIM17) when a watchdog is activated (minimum or maximum
threshold value crossed by analog signal) or when a short-circuit detection is made.
DFSDM1 watchdog is described in Section 26.4.10: Analog watchdog.
DFSDM1 short-circuit detection is described in Section 26.4.11: Short-circuit detector.
Timer break is described in:
• Section 33.3.16: Using the break function (TIM1/TIM8)
• Section 35.4.13: Using the break function (TIM15/TIM16/TIM17)
Triggering signals
The output (from DFSDM1) is on signals dfsdm1_break[0:3] directly connected to timer and
‘Ored’ with other break input signals of the timer.
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
13.3.7 From HSE, LSE, LSI,  MSI, MCO, RTC to timer
(TIM2/TIM15/TIM16/TIM17)
Purpose
External clocks (HSE, LSE), internal clocks (LSI, MSI), microcontroller output clock (MCO),
GPIO and RTC wakeup interrupt can be used as input to general-purpose timer
(TIM15/16/17) channel 1.
This allows to calibrate the HSI16/MSI system clocks (with TIM15/TIM16 and LSE) or LSI
(with TIM16 and HSE). This is also used to precisely measure LSI (with TIM16 and HSI16)
or MSI (with TIM17 and HSI16) oscillator frequency.
When Low Speed External (LSE) oscillator is used, no additional hardware connections are
required.
This feature is described in Section 9.3.18: Internal/external clock measurement with
TIM15/TIM16/TIM17.
External clock LSE can be used as input to general-purpose timers (TIM2) on TIM2_ETR
pin, see Section 34.4.22: TIM2 option register 1 (TIM2_OR1).
Active power mode
Run, Sleep, Low-power run, Low-power sleep.

Peripherals interconnect matrix RM0438
474/2187 RM0438 Rev 8
13.3.8 From RTC, COMP1, COMP2 to low-power timer
(LPTIM1/LPTIM2/LPTIM3)
Purpose
RTC alarm A/B, RTC_TAMP1/2/3 input detection, COMP1/2_OUT can be used as trigger to
start LPTIM counters (LPTIM1/2/3).
Triggering signals
This trigger feature is described in Section 37.4.7: Trigger multiplexer (and following
sections).
The input selection is described in [Table 298](../tables/table_298.md): LPTIM1 external trigger connections.
Active power mode
Run, Sleep, Low-power run, Low-power sleep, Stop 0, Stop 1, Stop 2 (LPTIM1 only).
13.3.9 From timer (TIM1/TIM2/TIM 3/TIM8/TIM15) to comparators
(COMP1/COMP2)
Purpose
Advanced-control timers (TIM1/TIM8), general-purpose timers (TIM2/TIM3) and general-
purpose timer (TIM15) can be used as blanking window input to COMP1/COMP2
The blanking function is described in Section 24.3.7: Comparator output blanking function.
The blanking sources are given in:
• Section 24.6.1: Comparator 1 control and status register (COMP1_CSR) bits 20:18
BLANKING[2:0]
• Section 24.6.2: Comparator 2 control and status register (COMP2_CSR) bits 20:18
BLANKING[2:0]
Triggering signals
Timer output signal TIMx_Ocx are the inputs to blanking source of COMP1/COMP2.
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
13.3.10 From ADC (ADC1) to ADC (ADC2)
Purpose
ADC1 can be used as a “master” to trigger ADC2 “slave” start of conversion.
In dual ADC mode, the converted data of the master and slave ADCs can be read in
parallel.
Triggering signals
Internal to the ADCs.

RM0438 Rev 8 475/2187
RM0438 Peripherals interconnect matrix
477
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
13.3.11 From USB to timer (TIM2)
Purpose
USB (FS SOF) can generate a trigger to general-purpose timer (TIM2).
Connection of USB to TIM2 is described in [Table 285](../tables/table_285.md): TIMx internal trigger connection.
Triggering signals
Internal signal generated by USB FS Start Of Frame.
Active power mode
Run, Sleep.
13.3.12 From internal analog sour ce to ADC (ADC1/ADC2) and OPAMP
(OPAMP1/OPAM2)
Purpose
Internal temperature sensor (VTS) and VBAT monitoring channel are connected to ADC1
input channels.
Internal reference voltage (VREFINT) is connected to ADC1 input channels.
OPAMP1 and OPAMP2 outputs can be connected to ADC1 or ADC2 input channels through
the GPIO.
DAC1_OUT1 can be connected to OPAMP1_VINP.
DAC1_OUT2 can be connected to OPAMP2_VINP.
This is according:
• Section 21.2: ADC main features
• Section 21.4.11: Channel selection (ADC_SQRy, ADC_JSQR)
• Section [Figure 95](../figures/figure_95.md).: ADC1 connectivity
• [Table 202](../tables/table_202.md): Operational amplifier possible connections
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
13.3.13 From comparators (COMP1/COMP2) to timers
(TIM1/TIM2/TIM3/TIM8/TIM15/TIM16/TIM17)
Purpose
Comparators (COMP1/COMP2) output values can be connected to timers
(TIM1/TIM2/TIM3/TIM8/TIM15/TIM16/TIM17) input captures or TIMx_ETR signals.
The connection to ETR is described in Section 33.3.4: External trigger input.

Peripherals interconnect matrix RM0438
476/2187 RM0438 Rev 8
Comparators (COMP1/COMP2) output values can also generate break input signals for
timers (TIM1/TIM8) on input pins TIMx_BKIN or TIMx_BKIN2 through GPIO alternate
function selection using open drain connection of IO, see Section 33.3.17: Bidirectional
break inputs.
The possible connections are given in:
• Section 33.4.23: TIM1 option register 1 (TIM1_OR1)
• Section 33.4.24: TIM8 option register 1 (TIM8_OR1)
• Section 34.4.22: TIM2 option register 1 (TIM2_OR1)
• Section 34.4.23: TIM3 option register 1 (TIM3_OR1)
• Section 34.4.24: TIM2 option register 2 (TIM2_OR2)
• Section 34.4.25: TIM3 option register 2 (TIM3_OR2)
• Section 35.3: TIM16/TIM17 main features
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
13.3.14 From system errors to ti mers (TIM1/TIM8/TIM15/TIM16/TIM17)
Purpose
CSS, CPU hardfault, RAM parity error, FLASH ECC double error detection, PVD can
generate system errors in the form of timer break toward timers
(TIM1/TIM8/TIM15/TIM16/TIM17).
The purpose of the break function is to protect power switches driven by PWM signals
generated by the timers.
List of possible source of break are described in:
• Section 33.3.16: Using the break function (TIM1/TIM8)
• Section 35.4.13: Using the break function (TIM15/TIM16/TIM17)
• [Figure 341](../figures/figure_341.md): TIM15 block diagram
• [Figure 342](../figures/figure_342.md): TIM16/TIM17 block diagram
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
13.3.15 From timers (TIM16/TIM17) to IRTIM
Purpose
General-purpose timer (TIM16/TIM17) output channel TIMx_OC1 are used to generate the
waveform of infrared signal output.
The functionality is described in Section 38: Infrared interface (IRTIM).
Active power mode
Run, Sleep, Low-power run, Low-power sleep.

RM0438 Rev 8 477/2187
RM0438 Peripherals interconnect matrix
477
13.3.16 From ADC ( ADC1/ADC2) to DFSDM
Purpose
Up to 3 internal ADC results can be directly connected through a parallel bus to DFSDM
input in order to use DFSDM filtering capabilities.
The feature is described as part of DFSDM peripheral description in Section 26.4.6: Parallel
data inputs - Input from internal ADC
The possible connections are given in:
• Section 26.7.1: DFSDM channel y configuration register (DFSDM_CHyCFGR1)
– Bits 13:12 DATMPX[1:0]: Input da ta multiplexer for channel y
• Section 26.7.5: DFSDM channel y data input register (DFSDM_CHyDATINR)
– Bits 31:16 INDAT0[15:0]: Input data for channel y or channel y+1
– Bits 15:0 INDAT0[15:0]: Input data for channel y
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 95: Architectural Diagram](../figures/figure_95.md)
* [Figure 230: Architectural Diagram](../figures/figure_230.md)
* [Figure 341: Architectural Diagram](../figures/figure_341.md)
* [Figure 342: Architectural Diagram](../figures/figure_342.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 95: Configuration Matrix](../tables/table_95.md)
* [Table 202: Configuration Matrix](../tables/table_202.md)
* [Table 209: Configuration Matrix](../tables/table_209.md)
* [Table 280: Configuration Matrix](../tables/table_280.md)
* [Table 285: Configuration Matrix](../tables/table_285.md)
* [Table 289: Configuration Matrix](../tables/table_289.md)
* [Table 298: Configuration Matrix](../tables/table_298.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)