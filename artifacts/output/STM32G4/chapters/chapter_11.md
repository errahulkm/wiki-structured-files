# Chapter 11: Peripherals interconnect matrix

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32G4 Reference Manual RM0440 - Chapter 11: Peripherals interconnect matrix.
* **Document Source**: RM0440 Reference Manual
* **PDF Reference Location**: Pages 376 - 396
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0440 Ingestion)
```text
Peripherals interconnect matrix RM0440
376/2140 RM0440 Rev 9
11 Peripherals interconnect matrix
11.1 Introduction
Several peripherals have direct connections between them.
This allows autonomous communication and or synchronization between peripherals,
saving CPU resources thus power supply consumption.
In addition, these hardware connections remove software latency and allow design of
predictable system.
Depending on peripherals, these interconnections can operate in Run, Sleep, Low-power
run and sleep, Stop 0 and Stop 1 modes.

RM0440 Rev 9 377/2140
RM0440 Peripherals interconnect matrix
396
11.2 Connection summary
[Table 62](../tables/table_62.md). STM32G4 series peripherals interconnect matrix(1) (2)
Source
Destination
TIM1
TIM2
TIM3
TIM4
TIM5
TIM6
TIM7
TIM8
TIM15
TIM16
TIM17
TIM20
LPTIM1
HRTIM
ADC1
ADC2
ADC3
ADC4
ADC5
OPAMP1
OPAMP2
OPAMP3
OPAMP4
OPAMP5
OPAMP6
DAC1
DAC2
DAC3
DAC4
COMP1
COMP2
COMP3
COMP4
COMP5
COMP6
COMP7
IRTIM
TIM1 - 1111 - - 11 - - 1 - 10
14 19 19 19 19 19 - - - - - - - - 20 - 15 15 15 15 15 15 15 -
TIM2 1 - 1
2 - 1
2 - - 11 - - 1 - 10 19 19 19 19 19 - - - - - - 20 20 20 20 15 15 15 - 15 15 - -
TIM3 1 1
2 - 1
2
1
2 - - 11 - - 1 - 10 19 19 19 19 19 - - - - - - 20 20 20 20 15 15 15 15 15 - 15 -
TIM4 1 1
2
1
2 - 1 - - 11 - - 1 - - 19 19 19 19 19 - - - - - - 20 20 20 20 - - - - - - - -
TIM5 1 1
2 1 1
2 - - - 11 - - 1 - - - - - - - - - - - - - - - - - - - - - - - - -
TIM6 - - - - - - - - - - - - - 10
13 19 19 19 19 19 - - - - - - 20 20 20 20 - - - - - - - -
TIM7 - - - - - - - - - - - - - 10
12 19 19 19 19 19 - - - - - - 20 20 20 20 - - - - - - - -
TIM8 11111 - - - 1 - - 1 - - 19 19 19 19 19 - - - - - - 20 20 - 20 15 15 15 15 15 15 15 -
TIM15 11111 - - 1 - - - 1 - 10 19 19 19 19 19 - - - - - - 20 20 20 20 - - - 15 - 15 15 -
TIM16 11111 - - 11 - - 1 - 12
13 19 19 - - - - - - - - - - - - - - - - - - - - 16
TIM17 11111 - - 11 - - 1 - 12
13 - - - - - - - - - - - - - - - - - - - - - - 16
TIM20 11111 - - 11 - - 1 - - 19 19 19 19 19 - - - - - - - - - - 15 15 15 15 15 15 15 -
LPTIM1 - - - - - - - - - - - - - - 19 19 19 19 19 - - - - - - - - - - - - - - - - - -
HRTIM 11111 - - 11 - - 1 - - 19 19 19 19 19 - - - - - - 20 20 20 20 - - - - - - - -
ADC1 2 - 2 - - - - 2 - - - - - 10 - - - - - - - - - - - - - - - - - - - - - - -
ADC2 2 - 2 - - - - 2 - - - - - 10 - - - - - - - - - - - - - - - - - - - - - - -
ADC3 2 - - - - - - 2 - - - 2 - 10 - - - - - - - - - - - - - - - - - - - - - - -
ADC4 2 - - - - - - 2 - - - 2 - 10 - - - - - - - - - - - - - - - - - - - - - - -
ADC5 2 - - - - - - 2 - - - 2 - 10 - - - - - - - - - - - - - - - - - - - - - - -
T. Sensor - - - - - - - - - - - - - - 21 - - - 21 - - - - - - - - - - - - - - - - - -
VBAT - - - - - - - - - - - - - - 21 - 21 - 21 - - - - - - - - - - - - - - - - - -
VREFINT - - - - - - - - - - - - - - 21 - 21 21 21 - - - - - - - - - - 23 23 23 23 23 23 23 -
OPAMP1 - - - - - - - - - - - - - - 21
24 - - - - - - - - - - - - - - - - - - - - - -
OPAMP2 - - - - - - - - - - - - - - - 21
24 - - - - - - - - - - - - - - - - - - - - -
OPAMP3 - - - - - - - - - - - - - - 21
24
21
24
21
24 - - - - - - - - - - - - - - - - - - - -
OPAMP4 - - - - - - - - - - - - - - 21
24 - - 21
24
21
24 - - - - - - - - - - - - - - - - - -
OPAMP5 - - - - - - - - - - - - - - - - - - 21
24 - - - - - - - - - - - - - - - - - -

Peripherals interconnect matrix RM0440
378/2140 RM0440 Rev 9
OPAMP6 - - - - - - - - - - - - - - 21
24
21
24 - 21
24 - - - - - - - - - - - - - - - - - - -
DAC1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 22
23
22
23
22
23
22
23
22
23 - - -
DAC2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 22
23
22
23 -
DAC3 - - - - - - - - - - - - - - - - - - - 22
24 - 22
24 - - 22
24 - - - - 22
23
22
23
22
23
22
23 - - - -
DAC4 - - - - - - - - - - - - - - - - - - - - - - 22
24
22
24 - - - - - - - - - 22
23
22
23
22
23 -
HSE - - - - - - - - - 44 - - - - - - - - - - - - - - - - - - - - - - - - - -
LSE - 2 - - 4 - - - 444 - - - - - - - - - - - - - - - - - - - - - - - - - -
HSI16 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
LSI - - - - 4 - - - - 44 - - - - - - - - - - - - - - - - - - - - - - - - - -
MCO - - - - - - - - - 44 - - - - - - - - - - - - - - - - - - - - - - - - - -
EXTI - - - - - - - - - - - - - - 19 19 19 19 19 - - - - - - 20 20 20 20 - - - - - - - -
RTC - - - - 4 - - - - 44 - 17 - - - - - - - - - - - - - - - - - - - - - - - -
COMP1
2
3
4
8
9
2
3
4
5
7
2
3
4
5
2
4
5
2
4
5
- -
2
3
4
8
9
3
4
8
3
8
3
8
2
3
4
8
9
17 10
11 - - - - - - - - - - - - - - - - - - - - - - -
COMP2
2
3
4
8
9
2
3
4
5
7
2
3
4
5
2
4
5
2
4
5
- -
2
3
4
8
9
3
5
8
3
8
3
8
2
3
4
8
9
17 10
11 - - - - - - - - - - - - - - - - - - - - - - -
COMP3
2
3
4
8
9
2
3
4
5
2
3
4
5
6
2
4
5
2
4
5
- -
2
3
4
8
9
3
5
8
3
8
3
8
2
3
4
8
9
17 10
11 - - - - - - - - - - - - - - - - - - - - - - -
COMP4
2
3
4
8
9
2
3
4
5
6
2
3
4
5
2
4
5
2
4
5
- -
2
3
4
8
9
3
8
3
8
3
8
2
3
4
8
9
17 10
11 - - - - - - - - - - - - - - - - - - - - - - -
COMP5
2
3
8
9
2
3
4
2
3
4
5
2
4
5
6
2
4
5
- -
2
3
8
9
3
4
8
3
8
3
4
8
2
3
8
9
- 10
11 - - - - - - - - - - - - - - - - - - - - - - -
[Table 62](../tables/table_62.md). STM32G4 series peripherals interconnect matrix(1) (2) (continued)
Source
Destination
TIM1
TIM2
TIM3
TIM4
TIM5
TIM6
TIM7
TIM8
TIM15
TIM16
TIM17
TIM20
LPTIM1
HRTIM
ADC1
ADC2
ADC3
ADC4
ADC5
OPAMP1
OPAMP2
OPAMP3
OPAMP4
OPAMP5
OPAMP6
DAC1
DAC2
DAC3
DAC4
COMP1
COMP2
COMP3
COMP4
COMP5
COMP6
COMP7
IRTIM

RM0440 Rev 9 379/2140
RM0440 Peripherals interconnect matrix
396
11.3 Interconnection details
11.3.1 From timer (TIMx,  HRTIM) to timer (TIMx)
The HRTIM burst operation can be triggered by on chip event coming from other general
purpose timer.
COMP6
2
3
8
9
2
3
5
2
3
4
5
2
4
5
2
4
5
- -
2
3
8
9
3
5
8
3
5
8
3
8
2
3
8
9
- 10
11 - - - - - - - - - - - - - - - - - - - - - - -
COMP7
2
3
8
9
2
3
2
3
4
5
2
4
5
2
4
5
- -
2
3
8
9
3
4
5
8
3
8
3
8
2
3
8
9
- 10
11 - - - - - - - - - - - - - - - - - - - - - - -
SYST ERR 18 - - - - - - 18 18 18 18 18 - 18 - - - - - - - - - - - - - - - - - - - - - - -
1. Numbers inside table link to corre sponding interconnect number detailed in Section 11.3: Interconnection details.
2.  The “-” symbol in grayed cells means no interconnect.
[Table 62](../tables/table_62.md). STM32G4 series peripherals interconnect matrix(1) (2) (continued)
Source
Destination
TIM1
TIM2
TIM3
TIM4
TIM5
TIM6
TIM7
TIM8
TIM15
TIM16
TIM17
TIM20
LPTIM1
HRTIM
ADC1
ADC2
ADC3
ADC4
ADC5
OPAMP1
OPAMP2
OPAMP3
OPAMP4
OPAMP5
OPAMP6
DAC1
DAC2
DAC3
DAC4
COMP1
COMP2
COMP3
COMP4
COMP5
COMP6
COMP7
IRTIM
[Table 63](../tables/table_63.md). Interconnect 1
Timer input
trigger
signal
Timer input trigger source assignment
TIM1 TIM2 TIM3 TIM4 TIM5 TIM8 TIM15 TIM20
timx_itr0 - tim1_trgo tim1_trgo tim1_trg o tim1_trgo tim1_trgo tim1_trgo tim1_trgo
timx_itr1 tim2_trgo - tim2_t rgo tim2_trgo tim2_trgo tim 2_trgo tim2_trgo tim2_trgo
timx_itr2 tim3_trgo tim3_trgo - tim3_trgo tim3_trgo tim3_trgo t im3_trgo tim3_trgo
timx_itr3 tim4_trgo tim4_trgo tim4_trgo - tim4_trgo tim4_trgo t im4_trgo tim4_trgo
timx_itr4 tim5_trgo tim5_trgo tim5_trgo t im5_trgo - tim5_trgo tim5_trgo tim5_trgo
timx_itr5 tim8_trgo tim8_trgo tim8_trgo t im8_trgo tim8_trgo - tim8_trgo tim8_trgo
timx_itr6 tim15_trgo tim15_trgo tim15_trgo t im15_trgo tim15_trgo tim15_trgo - tim15_trgo
timx_itr7 tim16_oc tim16_oc tim16_oc tim16_oc tim16_oc tim16_oc xtim16_oc tim16_oc
timx_itr8 tim17_oc tim17_oc tim17_oc tim17_oc tim17_oc tim17_oc tim17_oc tim17_oc
timx_itr9 tim20_trgo tim20_trgo tim20_trgo t im20_trgo tim20_trgo tim20_trgo tim20_trgo -
timx_itr10 hrtim_out_
scout2
hrtim_out_
scout2
hrtim_out_
scout2
hrtim_out_
scout2
hrtim_out_
scout2
hrtim_out_
scout2
hrtim_out_
scout2
hrtim_out_
scout2

Peripherals interconnect matrix RM0440
380/2140 RM0440 Rev 9
The burst mode controller counter can be clocked by general purpose timers as well as
shown in the [Table 64](../tables/table_64.md).
The HRTIM can be synchronized by external sources as shown in the [Table 66](../tables/table_66.md).
Some of the TIMx timers are linked together internally for timer synchronization or chaining.
When one timer is configured in Master Mode, it can reset, start, stop or clock the counter of
another timer configured in Slave Mode.
A description of the feature is provided in: Section 29.3.30: Timer synchronization.
The modes of synchronization are detailed in:
• Section 29.3.30: Timer synchronization for advanced-control timers
(TIM1/TIM8/TIM20)
• Section 30.4.23: Timer synchronization for general-purpose timers
(TIM2/TIM3/TIM4/TIM5)
• Section 31.4.26: Timer synchronization (TIM15 only) for general-purpose timer (TIM15)
[Table 64](../tables/table_64.md). Interconnect 12
HRTIM Burst mode trigger event/ clock signal HRTIM Burst mode trigger event/ clock signal
assignment
hrtim_bm_trg tim7_trgo
hrtim_bm_ck1 tim16_oc
hrtim_bm_ck2 tim17_oc
hrtim_bm_ck3 tim7_trgo‘
[Table 65](../tables/table_65.md). Interconnect 13
HRTIM update enable signal HRTIM update enable assignment
hrtim_upd_en1 tim16_oc
hrtim_upd_en2 tim17_oc
hrtim_upd_en3 tim6_oc
[Table 66](../tables/table_66.md). Interconnect 14
HRTIM synchronization signals HRTIM synchronization signal assignment
hrtim_in_sync2 tim1_trgo
hrtim_in_sync3 HRTIM_SCIN

RM0440 Rev 9 381/2140
RM0440 Peripherals interconnect matrix
396
Triggering signals
The output (from Master) is on signal TIMx_TRGO (and TIMx_TRGO2 for
TIM1/TIM8/TIM20) following a configurable timer event.
The input (to slave) is on signals TIMx_ITRx
The input and output signals for TIM1/TIM8/TIM20 are shown in [Figure 296](../figures/figure_296.md): Advanced-
control timer block diagram.
The possible master/slave connections are given in:
• [Table 267](../tables/table_267.md): Internal trigger connection
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
11.3.2 From timer (TIMx, HR TIM) and EXTI to ADC (ADCx)
[Table 67](../tables/table_67.md). Interconnect 19
ADC trigger selection
EXTSEL[4:0] or
JEXTSEL[4:0]
ADC triggers signals assignment
ADC1/2 ADC3/4/5
Regular Injected Regular Injected
0 tim1_cc1 tim1_trgo tim3_cc1 tim1_trgo
1 tim1_cc2 tim1_cc4 tim2_cc3 tim1_cc4
2 tim1_cc3 tim2_trgo tim1_cc3 tim2_trgo
3 tim2_cc2 tim2_cc1 tim8_cc1 tim8_cc2
4 tim3_trgo tim3_cc4 tim3_trgo tim4_cc3
5 tim4_cc4 tim4_trgo exti2 tim4_trgo
6 exti11 exti15 tim4_cc1 tim4_cc4
7 tim8_trgo tim8_cc4 tim8_trgo tim8_cc4
8 tim8_trgo2 tim1_trgo2 tim8_trgo2 tim1_trgo2
9 tim1_trgo tim8_trgo tim1_trgo tim8_trgo
10 tim1_trgo2 tim8_trgo2 tim1_trgo2 tim8_trgo2
11 tim2_trgo tim3_cc3 tim2_trgo tim1_cc3
12 tim4_trgo tim3_trgo tim4_trgo tim3_trgo
13 tim6_trgo tim3_cc1 tim6_trgo exti3
14 tim15_trgo tim6_trg o tim15_trgo tim6_trgo
15 tim3_cc4 tim15_trgo tim2_cc1 tim15_trgo
16 tim20_trgo tim20_trgo tim20_trgo tim20_trgo
17 tim20_trgo2 tim20_trgo2 tim20_trgo2 tim20_trgo2
18 tim20_cc1 tim20_cc4 tim20_cc1 tim20_cc2
19 tim20_cc2 hrtim_adc_trg2 hrtim_adc_trg2 hrtim_adc_trg2

Peripherals interconnect matrix RM0440
382/2140 RM0440 Rev 9
Timers (TIMx, HRTIM) can be used to generate an ADC triggering event.
TIMx synchronization is described in: Section 29.3.31: ADC triggers (TIM1/TIM8).
ADC synchronization is described in: Section 21.4.18: Conversion on external trigger and
trigger polarity (EXTSEL, EXTEN, JEXTSEL, JEXTEN).
Triggering signals
The output (from timer) is on signal TIMx_TRGO, TIMx_TRGO2 or TIMx_CCx event.
The input (to ADC) is on signal EXT[15:0], JEXT[15:0].
The connection between timers and ADC is provided in:
• [Table 166](../tables/table_166.md): ADC1/2 - External triggers for regular channels
• [Table 167](../tables/table_167.md): ADC1/2 - External trigger for injected channels
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
20 tim20_cc3 hrtim_adc_trg4 hrtim_adc_trg4 hrtim_adc_trg4
21 hrtim_adc_trg1 hrtim_adc_trg 5 hrtim_adc_trg1 hrtim_adc_trg5
22 hrtim_adc_trg3 hrtim_adc_trg 6 hrtim_adc_trg3 hrtim_adc_trg6
23 hrtim_adc_trg5 hrtim_adc_trg 7 hrtim_adc_trg5 hrtim_adc_trg7
24 hrtim_adc_trg6 hrtim_adc_trg 8 hrtim_adc_trg6 hrtim_adc_trg8
25 hrtim_adc_trg7 hrtim_adc_trg 9 hrtim_adc_trg7 hrtim_adc_trg9
26 hrtim_adc_trg8 hrtim_adc_trg10 hrtim_adc_trg8 hrtim_adc_trg10
27 hrtim_adc_trg9 TIM16_CC1 hr tim_adc_trg9 hrtim_adc_trg1
28 hrtim_adc_trg10 - hrtim_ adc_trg10 hrtim_adc_trg3
29 lptim_out lptim_out lptim_out lptim_out
30 tim7_trgo tim7_trgo tim7_trgo tim7_trgo
3 1 ----
[Table 67](../tables/table_67.md). Interconnect 19 (continued)
ADC trigger selection
EXTSEL[4:0] or
JEXTSEL[4:0]
ADC triggers signals assignment
ADC1/2 ADC3/4/5
Regular Injected Regular Injected

RM0440 Rev 9 383/2140
RM0440 Peripherals interconnect matrix
396
11.3.3 From ADC (ADCx) to timer (TIMx, HRTIM)
See please [Table 75](../tables/table_75.md): Interconnect 2 and [Table 83](../tables/table_83.md).: Interconnect 10
ADCs Analog watchdogs are connected to TIM1/8/20 for digital power applications (cycle-
bycycle current regulation with ADC).
A description of the ADC analog watchdog setting is provided in: Section 21.4.28: Analog
window watchdog (AWD1EN, JAWD1EN, AWD1SGL, AWD1CH, AWD2CH, AWD3CH,
AWD_HTx, AWD_LTx, AWDx).
Trigger settings on the timer are provided in: Section 29.3.6: External trigger input.
Triggering signals
The output (from ADC) is on signals ADCn_AWDx_OUT and the input (to timer) on signal
TIMx_ETR (external trigger) or hrtim_eevx[4:1].
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
11.3.4 From timer (TIMx, HRT IM) and EXTI to DAC (DACx)
[Table 68](../tables/table_68.md). Interconnect 20
DAC trigger
selection
(TSELx[3:0],
STRSTTRIG
SELx[3:0])
DAC triggers signals assignment
DAC1 DAC2 DAC3 DAC4
Update/
reset Inc Update/
reset Inc Update
/reset Inc Update/
reset Inc
0 sw - sw - sw - sw -
1 tim8_trgo tim8_trgo tim8_trgo tim8_trg o tim1_trgo tim1_trgo tim8_trgo tim8_trgo
2 tim7_trgo tim7_trgo tim7_trgo tim7_trg o tim7_trgo tim7_trgo tim7_trgo tim7_trgo
3 tim15_trgo tim15_trgo tim15_trgo tim15_trgo t im15_trgo tim15_trgo ti m15_trgo tim15_trgo
4 tim2_trgo tim2_trgo tim2_trgo tim2_trg o tim2_trgo tim2_trgo tim2_trgo tim2_trgo
5 tim4_trgo tim4_trgo tim4_trgo tim4_trg o tim4_trgo tim4_trgo tim4_trgo tim4_trgo
6 exti9 exti10 exti9 exti10 exti9 exti10 exti9 exti10
7 tim6_trgo tim6_trgo tim6_trgo tim6_trg o tim6_trgo tim6_trgo tim6_trgo tim6_trgo
8 tim3_trgo tim3_trgo tim3_trgo tim3_trg o tim3_trgo tim3_trgo tim3_trgo tim3_trgo
9 hrtim_dac_
reset_trg1
hrtim_step
_trig1
hrtim_dac_
reset_trg1
hrtim_step
_trig1
hrtim_dac
_reset_trg
1
hrtim_step
_trig1
hrtim_dac
_reset_trg
1
hrtim_step
_trig1
10 hrtim_dac_
reset_trg2
hrtim_step
_trig2
hrtim_dac_
reset_trg2
hrtim_step
_trig2
hrtim_dac
_reset_trg
2
hrtim_stept
rig_2
hrtim_rst_
_trig_2
hrtim_step
_trig2
11 hrtim_dac_
reset_trg3
hrtim_step
_trig3
hrtim_dac_
reset_trg3
hrtim_step
_trig3
hrtim_dac
_reset_trg
3
hrtim_step
_trig3
hrtim_dac
_reset_trg
3
hrtim_step
_trig3

Peripherals interconnect matrix RM0440
384/2140 RM0440 Rev 9
Timers (TIMx, HRTIM) and EXTI can be used as triggering event to start a DAC conversion.
Triggering signals
The output (from timer) is on signal TIMx_TRGO directly connected to corresponding DAC
inputs.
Selection of input triggers on DAC is provided in Section 22.4.7: DAC trigger selection
(single and dual mode).
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
11.3.5 From HSE, LS E, LSI, HSI16, MCO, RTC to timer (TIMx)
See please [Table 77](../tables/table_77.md): Interconnect 4 and [Table 75](../tables/table_75.md): Interconnect 2
External clocks (HSE, LSE), internal clocks (LSI, HSI16), microcontroller output clock
(MCO), GPIO and RTC wakeup interrupt can be used as input to timer (TIMx).
This allows to calibrate the HSI16 and precisely measure the LSI oscillator frequency.
When Low Speed External (LSE) oscillator is used, no additional hardware connections are
required.
This feature is described in Section 7.2.16: Internal/external clock measurement with
TIM5/TIM15/TIM16/TIM17.
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
12 hrtim_dac_
reset_trg4
hrtim_step
_trig4
hrtim_dac_
reset_trg4
hrtim_step
_trig4
hrtim_dac
_reset_trg
4
hrtim_step
_trig4
hrtim_dac
_reset_trg
4
hrtim_step
_trig4
13 hrtim_dac_
reset_trg5
hrtim_step
_trig5
hrtim_dac_
reset_trg5
hrtim_step
_trig5
hrtim_dac
_reset_trg
5
hrtim_step
_trig5
hrtim_dac
_reset_trg
5
hrtim_step
_trig5
14 hrtim_dac_
reset_trg6
hrtim_step
_trig6
hrtim_dac_
reset_trg6
hrtim_step
_trig6
hrtim_dac
_reset_trg
6
hrtim_step
_trig6
hrtim_dac
_reset_trg
6
hrtim_step
_trig6
15 hrtim_dac_
trg1 - hrtim_dac_
trg2 - hrtim_dac
_trg3 - hrtim_dac
_trg1 -
[Table 68](../tables/table_68.md). Interconnect 20 (continued)
DAC trigger
selection
(TSELx[3:0],
STRSTTRIG
SELx[3:0])
DAC triggers signals assignment
DAC1 DAC2 DAC3 DAC4
Update/
reset Inc Update/
reset Inc Update
/reset Inc Update/
reset Inc

RM0440 Rev 9 385/2140
RM0440 Peripherals interconnect matrix
396
11.3.6 From RTC, COMPx to low-power timer (LPTIM1)
RTC alarm A/B, RTC_TAMP1/2/3 input detection, COMPx_OUT can be used as trigger to
start LPTIM counters (LPTIM1).
Triggering signals
This trigger feature is described in Section 33.4.6: Trigger multiplexer (and following
sections).
The input selection is described in [Table 327](../tables/table_327.md): LPTIM1 external trigger connection.
Active power mode
Run, Sleep, Low-power run, Low-power sleep, Stop 0, Stop 1.
[Table 69](../tables/table_69.md). Interconnect 17
LPTIM trigger input signal (TRIGSEL[3:0]) LPTIM1 trigger source assignment
lptim1_ext_trig0 LPTIM1_ETR
lptim1_ext_trig1 rtc_alra_trg
lptim1_ext_trig2 rtc_alrb_trg
lptim1_ext_trig3 RTC_TAMP1
lptim1_ext_trig4 RTC_TAMP2
lptim1_ext_trig5 RTC_TAMP3
lptim1_ext_trig6 comp1_out
lptim1_ext_trig7 comp2_out
lptim1_ext_trig8 comp3_out
lptim1_ext_trig9 comp4_out
lptim1_ext_trig10 comp5_out
lptim1_ext_trig11 comp6_out
lptim1_ext_trig12 comp7_out

Peripherals interconnect matrix RM0440
386/2140 RM0440 Rev 9
11.3.7 From timer (TIMx)  to comparators (COMPx)
Timers (TIMx) can be used as blanking window to COMPx (x = 1...7)
The blanking function is described in Section 24.3.6: COMP output blanking.
The blanking sources are given in comparators control and status register (COMP_CxCSR)
bits BLANKSEL[2:0].
Triggering signals
Timer output signal TIMx_Ocx are the inputs to blanking source of COMPx.
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
11.3.8 From internal analog source to ADC (ADCx), comparator (COMPx)
and OPAMP (OPAMPx)
[Table 71](../tables/table_71.md) provides the ADC channels mapping on GPIOs or internal connections to
temperature sensor (VTS), internal reference voltage VREFINT, VBAT/3 or opampxint_vout.
[Table 70](../tables/table_70.md). Interconnect 15
Comparator blanking
signal BLANKSEL[2:0]
Comparator blanking source assignment
COMP1 COMP2 COMP3 COMP4 COMP5 COMP6 COMP7
1 tim1_oc5 tim1_oc5 tim1_oc5 tim3 _oc4 tim2_oc3 tim8_oc5 tim1_oc5
2 tim2_oc3 tim2_oc3 tim3_oc3 tim8 _oc5 tim8_oc5 tim2_oc4 tim8_oc5
3 tim3_oc3 tim3_oc3 tim2_oc4 tim15_ oc1 tim3_oc3 tim15_oc2 tim3_oc3
4 tim8_oc5 tim8_oc5 tim8_oc5 tim1_oc 5 tim1_oc5 tim1_oc5 tim15_oc2
5 tim20_oc5 tim20_oc5 tim20_oc5 tim20_oc5 tim20_oc5 tim20_oc5 tim20_oc5
6 tim15_oc1 tim15_oc1 tim15_oc1 tim15_oc1 tim15_oc1 tim15_oc1 tim15_oc1
7 tim4_oc3 tim4_oc3 tim4_oc3 tim4 _oc3 tim4_oc3 tim4_oc3 tim4_oc3
[Table 71](../tables/table_71.md). Interconnect 21
ADC channel
number
ADC channel source assignment
ADC1 ADC2 ADC3 ADC4 ADC5
I N 0 -----
IN1 PA0 PA0 PB1/OPAMP3
_VOUT PE14 PA8/OPAMP5
_VOUT
IN2 PA1 PA1 PE9 PE15 PA9
IN3 PA2/OPAMP1
_VOUT
PA6/OPAMP2
_VOUT PE13 PB12/OPAMP4
_VOUT
opamp5_int
_vout(1)
IN4 PA3 PA7 PE7 PB14 Temp sensor

RM0440 Rev 9 387/2140
RM0440 Peripherals interconnect matrix
396
The DAC outputs are available on GPIOs or can be internally connected to comparators and
operational amplifiers.
IN5 PB14 PC4 PB13 PB15 opamp4_int
_vout(1)
IN6 PC0 PC0 PE8 PE8 PE8
IN7 PC1 PC1 PD10 PD10 PD10
IN8 PC2 PC2 PD11 PD11 PD11
IN9 PC3 PC3 PD12 PD12 PD12
IN10 PF0 PF1 PD13 PD13 PD13
IN11 PB12/OPAMP4
_VOUT PC5 PD14 PD14 PD14
IN12 PB1/OPAMP3
_VOUT PB2 PB0 PD8 PD8
IN13 opamp1_int
_vout(1) PA5 opamp3_int
_vout(1) PD9 PD9
IN14 PB11/OPAMP6
_VOUT
PB11/OPAMP6
_VOUT PE10 PE10 PE10
IN15 PB0 PB15 PE11 PE11 PE11
IN16 Temp sensor opamp2_int
_vout(1) PE12 PE12 PE12
IN17 V BAT/3 PA4
VBAT/3(2)
opamp6_int_
vout(1)(3)
opamp6_int
_vout(1) VBAT/3
IN18 V REFINT
opamp3_int
_vout(1) VREFINT VREFINT VREFINT
1. Internal OPAMP output connected directly to ADC input only (no available externally on a pin).
2. For Category 3 devices only.
3. For Category 4 devices only.
[Table 72](../tables/table_72.md). Interconnect 22
Destination
Source
DAC1 DAC2 DAC3 DAC4
CH1 CH2 CH1 CH1 CH2 CH1 CH2
GPIO PA4 PA5 PA6 - - - -
COMP1 x - - x - - -
COMP2 - x - - x - -
[Table 71](../tables/table_71.md). Interconnect 21 (continued)
ADC channel
number
ADC channel source assignment
ADC1 ADC2 ADC3 ADC4 ADC5

Peripherals interconnect matrix RM0440
388/2140 RM0440 Rev 9
COMP3 x - - x - - -
COMP4 x - - - x - -
C O M P 5 -x---x-
COMP6 - - x - - x
COMP7 - - x - - x -
OPAMP1 - - - x - - -
O P A M P 2-------
OPAMP3 - - - - x - -
O P A M P 4-----x-
O P A M P 5------x
OPAMP6 - - - x - - -
[Table 72](../tables/table_72.md). Interconnect 22 (continued)
Destination
Source
DAC1 DAC2 DAC3 DAC4
CH1 CH2 CH1 CH1 CH2 CH1 CH2
[Table 73](../tables/table_73.md). Interconnect 23
Comparator
input/output
signals
Comparators input/output signals assignment
GPIO DAC output (1) VREFINT scaler
COMP1
INP PA1 PB1 - - - - - - - - -
INM PA0 PA4 - - -
DAC1_
CH1
PA4
DAC3_
CH1
VREF
INT
3/4
VREF
INT
1/2
VREF
INT
1/4
VREF
INT
OUT PA0 PF4 PA6 PA11 PB8 - - - - - -
COMP2
I N P P A 3 P A 7 - - - - - --- -
INM PA2 PA5 - - -
DAC1_
CH2
PA5
DAC3_
CH2
VREF
INT
3/4
VREF
INT
1/2
VREF
INT
1/4
VREF
INT
OUT PA2 PA7 PA12 PB9 - - - - - - -
COMP3
I N P P C 1 P A 0 - - - - - --- -
INM PC0 PF1 - - -
DAC1_
CH1
PA4
DAC3_
CH1
VREF
INT
3/4
VREF
INT
1/2
VREF
INT
1/4
VREF
INT
OUT PC2 PB7 PB15 - - - - - - - -

RM0440 Rev 9 389/2140
RM0440 Peripherals interconnect matrix
396
COMP4
INP PB0 PE7 - - - - - - - - -
INM PB2 PE8 - - -
DAC1_
CH1
PA4
DAC3_
CH2
VREF
INT
3/4
VREF
INT
1/2
VREF
INT
1/4
VREF
INT
OUT PB1 PB6 PB14 - - - - - - - -
COMP5
I N P P D 1 2 P B 1 3 - - - - - --- -
INM PD13 PB10 - - -
DAC1_
CH2
PA5
DAC4_
CH1
VREF
INT
3/4
VREF
INT
1/2
VREF
INT
1/4
VREF
INT
O U T P C 7 P A 9 - - - - - --- -
COMP6
INP PD11 PB11 - - - - - - - - -
INM PD10 PB15 - - -
DAC2_
CH1
PA6
DAC4_
CH2
VREF
INT
3/4
VREF
INT
1/2
VREF
INT
1/4
VREF
INT
O U T P C 6 P A 1 0 - - - - - --- -
COMP7
I N P P D 1 4 P B 1 4 - - - - - --- -
INM PD15 PB12 - - -
DAC2_
CH1
PA6
DAC4_
CH1
VREF
INT
3/4
VREF
INT
1/2
VREF
INT
1/4
VREF
INT
O U T P C 8 P A 8 - - - - - --- -
1. It is an internal connection.
[Table 73](../tables/table_73.md). Interconnect 23 (continued)
Comparator
input/output
signals
Comparators input/output signals assignment
GPIO DAC output (1) VREFINT scaler
[Table 74](../tables/table_74.md). Interconnect 24
Operational amplifier
input/output signals
Operational amplifier input/output signals assignment
GPIO DAC output ADC input on
GPIO
ADC internal
input
OPAMP1
VINP PA1 PA3 PA7 - DAC3_CH1 - -
VINM PA3 PC5 - - - - -
VOUT PA2 - - - ADC1_IN3 ADC1_IN13
OPAMP2
VINP PA7 PB14 PB0 PD14 - - -
VINM PA5 PC5 - - - - -
VOUT PA6 - - - ADC2_IN3 ADC2_IN16
OPAMP3
VINP PB0 PB13 PA1 - DAC3_CH2 - -
VINM PB2 PB10 - - - - -
VOUT PB1 - - - - ADC3_IN1/
ADC1_IN12
ADC2_IN18/
ADC3_IN13

Peripherals interconnect matrix RM0440
390/2140 RM0440 Rev 9
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
11.3.9 From comparators (COM Px) to timers (TIMx, HRTIM)
Comparators (COMPx) output values can be connected to:
• Timers (TIMx) input captures or TIMx_ETR signals or TIMx_OCREFCLR signals.
• hrtim_eevx[4:1] and hrtim_in_fltx[4:1]
Comparators (COMPx) output values can also generate break input signals for timers
(TIMx) see Section 30.3.17: Bidirectional break inputs.
OPAMP4
VINP PB13 PD11 PB11 - DAC4_CH1 - -
VINM PB10 PD8 - - - - -
VOUT PB12 - - - - ADC4_IN3/
ADC1_IN11 ADC5_IN5
OPAMP5
VINP PB14 PD12 PC3 - DAC4_CH2 - -
VINM PB15 PA3 - - - - -
VOUT PA8 - - - ADC5_IN1 ADC5_IN3
OPAMP6
VINP PB12 PD9 PB13 - DAC3_CH1 - -
VINM PA1 PB1 - - - - -
VOUT PB11 - - - - ADC12_IN14 ADC4_IN17
[Table 74](../tables/table_74.md). Interconnect 24 (continued)
Operational amplifier
input/output signals
Operational amplifier input/output signals assignment
GPIO DAC output ADC input on
GPIO
ADC internal
input
[Table 75](../tables/table_75.md). Interconnect 2
Timer external
trigger input
signal
Timer external trigger signals assignment
TIM1 TIM2 TIM3 TIM4 TIM5 TIM8 TIM20
timx_etr0 TIM1_
ETR
TIM2_
ETR
TIM3_
ETR
TIM4_
ETR
TIM5_
ETR
TIM8_
ETR
TIM20_
ETR
timx_etr1 comp1_
out
comp1_
out
comp1_
out
comp1_
out
comp1_
out
comp1_
out
comp1_
out
timx_etr2 comp2_
out
comp2_
out
comp2_
out
comp2_
out
comp2_
out
comp2_
out
comp2_
out
timx_etr3 comp3_
out
comp3_
out
comp3_
out
comp3_
out
comp3_
out
comp3_
out
comp3_
out
timx_etr4 comp4_
out
comp4_
out
comp4_
out
comp4_
out
comp4_
out
comp4_
out
comp4_
out
timx_etr5 comp5_
out
comp5_
out
comp5_
out
comp5_
out
comp5_
out
comp5_
out
comp5_
out

RM0440 Rev 9 391/2140
RM0440 Peripherals interconnect matrix
396
timx_etr6 comp6_
out
comp6_
out
comp6_
out
comp6_
out
comp6_
out
comp6_
out
comp6_
out
timx_etr7 comp7_
out
comp7_
out
comp7_
out
comp7_
out
comp7_
out
comp7_
out
comp7_
out
timx_etr8 adc1_
awd1 tim3_etr tim2_etr tim3_
etr
tim2_
etr
adc2_
awd1
adc3_
awd1
timx_etr9 adc1_
awd2 tim4_etr tim4_etr tim5_
etr
tim3_
etr
adc2_
awd2
adc3_
awd2
timx_etr10 adc1_
awd3 tim5_etr - - - adc2_
awd3
adc3_
awd3
timx_etr11 adc4_
awd1
lse_
css_out
adc2_
awd1 -- adc3_
awd1
adc5_
awd1
timx_etr12 adc4_
awd2 - adc2_
awd2 -- adc3_
awd2
adc5_
awd2
timx_etr13 adc4_
awd3 - adc2_
awd3 -- adc3_
awd3
adc5_
awd3
[Table 75](../tables/table_75.md). Interconnect 2 (continued)
Timer external
trigger input
signal
Timer external trigger signals assignment
TIM1 TIM2 TIM3 TIM4 TIM5 TIM8 TIM20
[Table 76](../tables/table_76.md). Interconnect 3
Timer
OCREF
clear
signal
Timer OCREF clear signals assignment
TIM1 TIM2 TIM3 TIM8 TIM15 TIM16 TIM17 TIM20
timx_
ocref_clr0 comp1_out comp1_out comp1_out comp1_out comp1_out comp1_out comp1_out comp1_out
timx_
ocref_clr1 comp2_out comp2_out comp2_out comp2_out comp2_out comp2_out comp2_out comp2_out
timx_
ocref_lr2 comp3_out comp3_out comp3_out comp3_out comp3_out comp3_out comp3_out comp3_out
timx_
ocref_clr3 comp4_out comp4_out comp4_out comp4_out comp4_out comp4_out comp4_out comp4_out
timx_
ocref_clr4 comp5_out comp5_out comp5_out comp5_out comp5_out comp5_out comp5_out comp5_out
timx_
ocref_clr5 comp6_out comp6_out comp6_out comp6_out comp6_out comp6_out comp6_out comp6_out
timx_
ocref_clr6 comp7_out comp7_out comp7_out comp7_out comp7_out comp7_out comp7_out comp7_out

Peripherals interconnect matrix RM0440
392/2140 RM0440 Rev 9
[Table 77](../tables/table_77.md). Interconnect 4
Timer
TI1
input
signal
Timer TI1 signals assignment
TIM1 TIM2 TIM3 TIM4 TIM5 TI M8 TIM15 TIM16 TIM17 TIM20
timx_
ti1_in0
TIM1
external
TI1 input
pins
TIM2
external
TI1 input
pins
TIM3
external
TI1 input
pins
TIM4
external
TI1 input
pins
TIM5
external
TI1 input
pins
TIM8
external
TI1 input
pins
TIM15
external
TI1 input
pins
TIM16
external
TI1 input
pins
TIM17
external
TI1 input
pins
TIM20
external
TI1 input
pins
timx_
ti1_in1
comp1_
out
comp1_
out
comp1_
out
comp1_
out LSI comp1_
out
lse_
css_out
comp6_
out
comp5_
out
comp1_
out
timx_
ti1_in2
comp2_
out
comp2_
out
comp2_
out
comp2_
out
lse_
css_out
comp2_
out
comp1_
out MCO MCO comp2_
out
timx_
ti1_in3
comp3_
out
comp3_
out
comp3_
out
comp3_
out
rtc_
Wakeup
comp3_
out
comp2_
out
HSE_Di
v32
HSE_Di
v32
comp3_
out
timx_
ti1_in4
comp4_
out
comp4_
out
comp4_
out
comp4_
out
comp1_
out
comp4_
out
comp5_
out
rtc_
Wakeup
rtc_
Wakeup
comp4_
out
timx_
ti1_in5 - comp5_
out
comp5_
out
comp5_
out
comp2_
out - comp7_
out
lse_
css_out
lse_
css_out -
timx_
ti1_in6 -- comp6_
out
comp6_
out
comp3_
out -- L S I L S I -
timx_
ti1_in7 -- comp7_
out
comp7_
out
comp4_
out -----
timx_
ti1_in8 ---- comp5_
out -----
timx_
ti1_in9 ---- comp6_
out -----
timx_
ti1_in10 ---- comp7_
out -----

RM0440 Rev 9 393/2140
RM0440 Peripherals interconnect matrix
396
[Table 78](../tables/table_78.md). Interconnect 5
Timer
TI2 input
signal
Timer TI2 signals assignment
TIM1 TIM2 TIM3 TIM4 TIM5 TIM8 TIM15 TIM20
timx_
ti2_in0
TIM1
external
TI2 input
pins
TIM2
external
TI2 input
pins
TIM3
external
TI2 input
pins
TIM4
external
TI2 input
pins
TIM5
external
TI2 input
pins
TIM8
external
TI2 input
pins
TIM15
external
TI2 input
pins
TIM20
external
TI2 input
pins
timx_
ti2_in1 - comp1_out comp1_out comp1_out comp1_out - comp2_out -
timx_
ti2_in2 - comp2_out comp2_out comp2_out comp2_out - comp3_out -
timx_
ti2_in3 - comp3_out comp3_out comp3_out comp3_out - comp6_out -
timx_
ti2_in4 - comp4_out comp4_out comp4_out comp4_out - comp7_out -
timx_
ti2_in5 - comp6_out comp5_out comp5_out comp5_out - - -
timx_
ti2_in6 - - comp6_out comp6_out comp6_out - - -
timx_
ti2_in7 - - comp7_out comp7_out comp7_out - - -
[Table 79](../tables/table_79.md). Interconnect 6
Timer TI3
input signal
Timer TI3 signals assignment
TIM1 TIM2 TIM3 TIM4 TIM5 TIM8 TIM20
timx_
ti3_in0
TIM1
external TI3
input pins
TIM2
external TI3
input pins
TIM3
external TI3
input pins
TIM4
external TI3
input pins
TIM5
external TI3
input pins
TIM8
external TI3
input pins
TIM20
external TI3
input pins
timx_
ti3_in1 - comp4_out comp3_out comp5_out - - -
[Table 80](../tables/table_80.md). Interconnect 7
Timer TI4
input signal
Timer TI4 signals assignment
TIM1 TIM2 TIM3 TIM4 TIM5 TIM8 TIM20
timx_
ti4_in0
TIM1
external TI4
input pins
TIM2
external TI4
input pins
TIM3
external TI4
input pins
TIM4
external TI4
input pins
TIM5
external TI4
input pins
TIM8
external TI4
input pins
TIM20
external TI4
input pins
timx_
ti4_in1 - comp1_out - comp6_out - - -
timx_
ti4_in2 - comp2_out - - - - -

Peripherals interconnect matrix RM0440
394/2140 RM0440 Rev 9
The timer break input features two channels:
• A break channel which gathers both application fault (from input pins and built-in
comparators) and system-level fault (clock failure, parity error, ...).
• A break2 channel which only includes application faults (from input pins and built-in
comparators).
Refer to [Table 81](../tables/table_81.md), [Table 82](../tables/table_82.md) and [Table 85](../tables/table_85.md).
[Table 81](../tables/table_81.md). Interconnect 8
Timer break signals assignment
TIM1 break
(tim1_bk)
TIM8 break
(tim8_bk)
TIM15 break
(tim15_bk)
TIM16 break
(tim16_bk)
TIM17 break
(tim17_bk)
TIM20 break
(tim20_bk)
Timer break
signal sources
TIM1_BKIN
pin
TIM8_BKIN
pin
TIM15_BKIN
pin
TIM16_BKIN
pin
TIM17_BKIN
pin
TIM20_BKIN
pin
comp1_out comp1_out comp1_out comp1_out comp1_out comp1_out
comp2_out comp2_out comp2_out comp2_out comp2_out comp2_out
comp3_out comp3_out comp3_out comp3_out comp3_out comp3_out
comp4_out comp4_out comp4_out comp4_out comp4_out comp4_out
comp5_out comp5_out comp5_out comp5_out comp5_out comp5_out
comp6_out comp6_out comp6_out comp6_out comp6_out comp6_out
comp7_out comp7_out comp7_out comp7_out comp7_out comp7_out
[Table 82](../tables/table_82.md). Interconnect 9
Timer break2 signals assignment
TIM1 break2
(tim1_bk2)
TIM8 break2
(tim8_bk2)
TIM20 break2
(tim20_bk2)
Timer break2
signal source
TIM1_BKIN2 pin TIM8_BKIN2  pin TIM20_BKIN2 pin
comp1_out comp1_out comp1_out
comp2_out comp2_out comp2_out
comp3_out comp3_out comp3_out
comp4_out comp4_out comp4_out
comp5_out comp5_out comp5_out
comp6_out comp6_out comp6_out
comp7_out comp7_out comp7_out

RM0440 Rev 9 395/2140
RM0440 Peripherals interconnect matrix
396
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
[Table 83](../tables/table_83.md). Interconnect 10
HRTIM external
event input signal
HRTIM external event signal assignment
EExSRC[1:0]=0
(from GPIO pin) EExSRC[1:0]=1 EExSRC[1:0]=2 EExSRC[1:0]=3
hrtim_eev1[4:1] HRTIM_EEV1 comp2_out tim1_trgo adc1_AWD1
hrtim_eev2[4:1] HRTIM_EEV2 comp4_out tim2_trgo adc1_AWD2
hrtim_eev3[4:1] HRTIM_EEV3 comp6_out tim3_trgo adc1_AWD3
hrtim_eev4[4:1] HRTIM_EEV4 comp1_out comp5_out adc2_AWD1
hrtim_eev5[4:1] HRTIM_EEV5 comp3_out comp7_out adc2_AWD2
hrtim_eev6[4:1] HRTIM_EEV6 comp2_out comp1_out adc2_AWD3
hrtim_eev7[4:1] HRTIM_EEV7 comp4_out tim7_trgo adc3_AWD1
hrtim_eev8[4:1] HRTIM_EEV8 comp6_out comp3_out adc4_AWD1
hrtim_eev9[4:1] HRTIM_EEV9 comp5_out tim15_trgo comp4_out
hrtim_eev10[4:1] HRTIM_EEV10 comp7_out tim6_trgo adc5_AWD1
[Table 84](../tables/table_84.md). Interconnect 11
Fault channel External Input
FLTxSRC[1:0] = 00
On-chip source
FLTxSRC[1:0] = 01
External Input
FLTxSRC[1:0] = 10
On-chip source
FLTxSRC[1:0] = 11
hrtim_flt1[4:1] HRTIM_FLT1 comp2_out EEV1_muxout N/A
hrtim_flt2[4:1] HRTIM_FLT2 comp4_out EEV2_muxout N/A
hrtim_flt3[4:1] HRTIM_FLT3 comp6_out EEV3_muxout N/A
hrtim_flt4[4:1] HRTIM_FLT4 comp1_out EEV4_muxout N/A
hrtim_flt5[4:1] HRTIM_FLT5 comp3_out EEV5_muxout N/A
hrtim_flt6[4:1] HRTIM_FLT6 comp5_out EEV6_muxout N/A

Peripherals interconnect matrix RM0440
396/2140 RM0440 Rev 9
11.3.10 From system errors to  timers (TIMx) and HRTIM
TIMx (TIM1/TIM8/TIM20/TIM15/TIM16/TIM17) break inputs and HRTIM system fault input
gather MCU internal fault events coming from:
• the clock failure event generated by the clock security system (CSS),
• the PVD output,
• the SRAM parity error signal,
• the Cortex-M4 LOCKUP (Hardfault) output
• Flash ECC double error detection
The purpose of the break function is to protect power switches driven by PWM signals
generated by the timers.
The functionality is described in:
• Section 29.3.18: Using the break function (TIM1/TIM8/TIM20)
• Section 31.4.15: Using the break function (TIM15/TIM16/TIM17/TIM20)
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
11.3.11 From timers (TIM16/TIM17) to IRTIM
General-purpose timer (TIM16/TIM17) output channel TIMx_OC1 are used to generate the
waveform of infrared signal output.
The functionality is described in Section 34: Infrared interface (IRTIM).
Active power mode
Run, Sleep, Low-power run, Low-power sleep.
[Table 85](../tables/table_85.md). Interconnect 18
System error signal surce
System error signals to timer signals assignment
TIM1 TIM8 TIM15 TIM16 TIM17 TIM20 HRTIM
Flash ECC error
tim1_bk tim8_bk tim15_bk tim16_bk tim17_bk tim20_bk hrtim_sys_flt
PVD output
SRAM1/
CCM SRAM parity
Cortex®-M4 Lockup
(hardfault)
Clock security system (CSS)
[Table 86](../tables/table_86.md). Interconnect 16
IRTIM control signal IRTIM control signals assignment
modulation envelope signal tim16_oc1
carrier signal tim17_oc1
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 296: Architectural Diagram](../figures/figure_296.md)

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