# Chapter 10: Interconnect matrix

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32C0 Reference Manual RM0490 - Chapter 10: Interconnect matrix.
* **Document Source**: RM0490 Reference Manual
* **PDF Reference Location**: Pages 218 - 222
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0490 Ingestion)
```text
Interconnect matrix RM0490
218/1023 RM0490 Rev 6
10 Interconnect matrix
10.1 Introduction
Several peripherals have direct connections between them.
This allows autonomous communication and/or synchronization between peripherals,
saving CPU resources thus power consumption.
In addition, these hardware connections remove software latency and allow design of
predictable systems.
Depending on peripherals, these interconnections can operate in Run, Sleep, and Stop
mode.
For availability of peripherals on different STM32C0 series products, refer to Section 1.5:
Availability of peripherals.
10.2 Connection summary
The numbers in the following table are links to corresponding sub-sections in Section 10.3:
Interconnection details.The “-” symbol in grayed cells means “no interconnection”.
[Table 42](../tables/table_42.md). Interconnect matrix
Destination ►
Source ▼
TIM1
TIM2
TIM3
TIM14
TIM15
TIM16
TIM17
ADC1
DMAMUX
IRTIM
TIM1 - 10.3.1 10.3.1 - - - - 10.3.2 - -
TIM2 10.3.1 - 10.3.1 - 10.3.1 - - 10.3.2 - -
TIM3 10.3.1 10.3.1 - - 10.3.1 - - 10.3.2 - -
TIM14 - 10.3.1 - - - - - 10.3.8 -
TIM15 10.3.1 10.3.1 10.3.1 - - - - 10.3.2 10.3.8 -
TIM16 - - - - 10.3.1 - - - - 10.3.7
TIM17 10.3.1 - - - 10.3.1 - - - - 10.3.7
USART1 - - - - - - - - - 10.3.7
USART2 - - - - - - - - - 10.3.7
ADC 10.3.3 - - - - - - - - -
Temp. sensor - - - - - - - 10.3.5 - -
VREFINT - - - - - - - 10.3.5 - -
HSE - - - 10.3.4 - - 10.3.4 - - -
LSE - - - - - 10.3.4 - - - -
LSI - - - - - 10.3.4 - - - -
MCO - - - 10.3.4 - - 10.3.4 - - -

RM0490 Rev 6 219/1023
RM0490 Interconnect matrix
222
10.3 Interconnection details
10.3.1 From TIM1, TIM2, TIM3, TIM14, TIM15, and TIM17, to TIM1, TIM2,
and TIM3
Purpose
Some of the TIMx timers are linked together internally for timer synchronization or chaining.
When one timer is configured in master mode, it can reset, start, stop or clock the counter of
another timer configured in slave mode.
A description of the feature is provided in: Section 18.3.19: Timer synchronization.
The modes of synchronization are detailed in:
• Section 17.3.26: Timer synchronization for advanced-control timer TIM1
• Section 18.3.18: Timers and external trigger synchronization for general-purpose
timers TIM2/TIM3
• Section 20.4.20: External trigger synchronization (TIM15 only) for general-purpose
timer TIM15
Triggering signals
The output (from master) is on signal TIMx_TRGO (and TIMx_TRGOx), following a
configurable timer event.
With TIM14, TIM16 and TIM17 timers that do not have a trigger output, the output
compare 1 is used instead.
The input (to slave) is on signals TIMx_ITR0/ITR1/ITR2/ITR3.
The input and output signals for TIM1 are shown in [Figure 57](../figures/figure_57.md): Advanced-control timer block
diagram.
The possible master/slave connections are given in [Table 81](../tables/table_81.md): TIM1 internal trigger
connection.
Relevant power modes
These interconnections operate in Run and Sleep modes.
MCO2 - - - 10.3.4 - 10.3.4 10.3.4 - - -
EXTI - - - - - - - 10.3.2 10.3.2 -
RTC - - - 10.3.4 - - - - - -
SYST ERR 10.3.6 - - - 10.3.6 10.3.6 10.3.6 - - -
[Table 42](../tables/table_42.md). Interconnect matrix (continued)
Destination ►
Source ▼
TIM1
TIM2
TIM3
TIM14
TIM15
TIM16
TIM17
ADC1
DMAMUX
IRTIM

Interconnect matrix RM0490
220/1023 RM0490 Rev 6
10.3.2 From TIM1, TIM2, TIM3 , TIM15, and EXTI, to ADC
Purpose
The general-purpose timer TIM3, TIM15, advanced-control timer TIM1, and EXTI can be
used to generate an ADC triggering event.
TIMx synchronization is described in: Section 17.3.27: ADC synchronization.
ADC synchronization is described in: Section 16.5: Conversion on external trigger and
trigger polarity (EXTSEL, EXTEN).
Triggering signals
The output (from timer) is on signal TIMx_TRGO, TIMx_TRGO2 or TIMx_CCx event.
The input (to ADC) is on signal TRG[7:0].
The connection between timers and ADC is provided in [Table 69](../tables/table_69.md): External triggers.
Relevant power modes
These interconnections operate in Run and Sleep modes.
10.3.3 From ADC to TIM1
Purpose
ADC can provide trigger event through watchdog signals to the advanced-control timer
TIM1.
A description of the ADC analog watchdog setting is provided in: Section 16.8: Analog
window watchdogs.
Trigger settings on the timer are provided in: Section 17.3.4: External trigger input.
Triggering signals
The output (from ADC) is on signals ADC_AWDx_OUT x = 1, 2, 3 (three watchdogs per
ADC) and the input (to timer) on signal TIMx_ETR (external trigger).
Relevant power modes
This interconnection operates in Run and Sleep modes.
10.3.4 From HSE, LSE, LSI, MC O, MCO2, and RTC, to TIM14,
TIM16, and TIM17
Purpose
External clocks (HSE, LSE), internal clock (LSI), microcontroller output clock (MCO and
MCO2), RTC clock, and GPIO can be selected as inputs to capture channel 1 of some of
TIM14/16/TIM17 timers.
The timers allow calibrating or precisely measuring internal clocks such as HSI48 or LSI,
using accurate clocks such as LSE or HSE/32 for timing reference. See details in
Section 6.2.14: Internal/external clock measurement with TIM14/TIM16/TIM17.

RM0490 Rev 6 221/1023
RM0490 Interconnect matrix
222
When low-speed external (LSE) oscillator is used, no additional hardware connections are
required.
Relevant power modes
These interconnections operate in Run and Sleep modes.
10.3.5 From internal analog sources to ADC
Purpose
The internal temperature sensor output voltage VTS and the internal reference voltage
VREFINT channel are connected to ADC input channels.
More information is in:
• Section 16.2: ADC main features
• Section 16.4.8: Channel selection (CHSEL, SCANDIR, CHSELRMOD)
• [Figure 16](../figures/figure_16.md).10: Temperature sensor and internal reference voltage
Relevant power modes
These interconnections operate in Run and Sleep modes.
10.3.6 From system errors to TI M1, TIM15, TIM16, and TIM17
Purpose
CSS, CPU HardFault, and RAM parity error can generate system errors in the form of timer
break toward TIM1, TIM16, and TIM17.
The purpose of the break function is to protect power switches driven by PWM signals from
the timers.
The relevant information is in:
• Section 17.3.16: Using the break function (TIM1)
• Section 20.4.13: Using the break function (TIM15/TIM16/TIM17)
• [Figure 182](../figures/figure_182.md): TIM15 block diagram
• [Figure 183](../figures/figure_183.md): TIM16/TIM17 block diagram
Relevant power modes
These interconnections operate in Run and Sleep modes.
10.3.7 From TIM16, TIM17, US ART1, and USART2, to IRTIM
Purpose
TIMx_OC1 output channel of TIM17 timer, associated with USART1 or USART2
transmission signal, can generate the infrared output waveform.
The functionality is described in Section 21: Infrared interface (IRTIM).
Relevant power modes
These interconnections operate in Run and Sleep modes.

Interconnect matrix RM0490
222/1023 RM0490 Rev 6
10.3.8 From TIM14 and EXTI to DMAMUX
Purpose
TIM14 general-purpose timer and EXTI can be used as triggering event to DMAMUX.
Relevant power modes
These interconnections operate in Run and Sleep modes.
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 16: Architectural Diagram](../figures/figure_16.md)
* [Figure 57: Architectural Diagram](../figures/figure_57.md)
* [Figure 182: Architectural Diagram](../figures/figure_182.md)
* [Figure 183: Architectural Diagram](../figures/figure_183.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 42: Configuration Matrix](../tables/table_42.md)
* [Table 69: Configuration Matrix](../tables/table_69.md)
* [Table 81: Configuration Matrix](../tables/table_81.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)