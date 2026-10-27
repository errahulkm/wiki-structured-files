# Chapter 21: Analog-to-digital converters (ADC)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32G4 Reference Manual RM0440 - Chapter 21: Analog-to-digital converters (ADC).
* **Document Source**: RM0440 Reference Manual
* **PDF Reference Location**: Pages 591 - 713
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Analog-to-Digital Converter (ADC)](../peripherals/adc.md)

## 2. Official Reference Manual Text Content (RM0440 Ingestion)
```text
RM0440 Rev 9 591/2140
RM0440 Analog-to-digital converters (ADC)
713
21 Analog-to-digital converters (ADC)
21.1 Introduction
This section describes the implementation of up to 5 ADCs:
• ADC1 and ADC2 are tightly coupled and can operate in dual mode (ADC1 is master).
• ADC3 and ADC4 are tightly coupled and can operate in dual mode (ADC3 is master).
• ADC5 is controlled independently.
Each ADC consists of a 12-bit successive approximation analog-to-digital converter.
Each ADC has up to 19 multiplexed channels. A/D conversion of the various channels can
be performed in single, continuous, scan or discontinuous mode. The result of the ADC is
stored in a left-aligned or right-aligned 16-bit data register.
The ADCs are mapped on the AHB bus to allow fast data handling.
The analog watchdog features allow the application to detect if the input voltage goes
outside the user-defined high or low thresholds.
A built-in hardware oversampler allows to improve analog performance while off-loading the
related computational burden from the CPU.
An efficient low-power mode is implemented to allow very low consumption at low
frequency.

Analog-to-digital converters (ADC) RM0440
592/2140 RM0440 Rev 9
21.2 ADC main features
• High-performance features
– Up to 5 ADCs, out of which four of them ((in pairs) can operate in dual mode:
ADC1 is connected to 14 external channels + 4 internal channels
ADC2 is connected to 16 external channels + 2 internal channels
ADC3 is connected to 15 external channels + 3 internal channels
ADC4 is connected to 16 external channels + 2 internal channels
ADC5 is connected to 13 external channels + 5 internal channels
– 12, 10, 8 or 6-bit configurable resolution
– ADC conversion time is independent from the AHB bus clock frequency
– Faster conversion time by lowering resolution
– Manage single-ended or differential inputs
– AHB slave bus interface to allow fast data handling
– Self-calibration
– Channel-wise programmable sampling time
– Flexible sampling time control
– Up to four injected channels (analog inputs assignment to regular or injected
channels is fully configurable)
– Hardware assistant to prepare the context of the injected channels to allow fast
context switching
– Data alignment with in-built data coherency
– Data can be managed by DMA for regular channel conversions
– 4 dedicated data registers for the injected channels
• Oversampler
– 16-bit data register
– Oversampling ratio adjustable from 2 to 256
– Programmable data shift up to 8-bit
• Data preconditioning
– Gain compensation
– Offset compensation
• Low-power features
– Speed adaptive low-power mode to reduce ADC consumption when operating at
low frequency
– Allows slow bus frequency application while keeping optimum ADC performance
– Provides automatic control to avoid ADC overrun in low AHB bus clock frequency

RM0440 Rev 9 593/2140
RM0440 Analog-to-digital converters (ADC)
713
application (auto-delayed mode)
• Number of external analog input channels per ADC
– Up to 5 fast channels from GPIO pads
– Up to 13 slow channels from GPIO pads
• In addition, there are several internal dedicated channels
– The internal reference voltage (V REFINT), connected to ADC1, 3, 4 and 5
– The internal temperature sensor (V TS), connected to ADC1 and 5
–T h e  V BAT monitoring channel (VBAT/3), connected to ADC1, 3 (for category 3
devices only) and 5
– The OPAMP1 internal ou tput connected to ADC1
– The OPAMP2 and OPAMP3 internal outputs connected to ADC2
– The OPAMP3 internal ou tput connected to ADC3
– The OPAMP6 internal output connected to ADC4 (for category 3 devices) or
ADC3 (for category 4 devices)
– The OPAMP4 and OPAMP5 internal outputs connected to ADC5
• Start-of-conversion can be initiated:
– By software for both regular and injected conversions
– By hardware triggers with configurable po larity (internal timers events or GPIO
input events) for both regular and injected conversions
• Conversion modes
– Each ADC can convert a single channel or can scan a sequence of channels
– Single mode converts selected inputs once per trigger
– Continuous mode converts selected inputs continuously
– Discontinuous mode
• Dual ADC mode for ADC1, ADC2, ADC3 and ADC4
• Interrupt generation at ADC ready, the end of sampling, the end of conversion (regular
or injected), end of sequence conversion (regular or injected), analog watchdog 1, 2 or
3 or overrun events
• 3 analog watchdogs per ADC
– Watchdog can perform filtering to ignore out-of-range data
• ADC input range: VREF– ≤ VIN ≤ VREF+
[Figure 82](../figures/figure_82.md) shows the block diagram of one ADC.
Refer to the OPAMP electrical characteristics section of the product datasheet for the ADC
sampling time value to be applied when converting the OPAMP output voltage.
21.3 ADC implementation
[Table 161](../tables/table_161.md). ADC features
ADC modes/features ADC1 ADC2 ADC3 ADC4 ADC5
Dual mode X (coupled toget her) X (coupled together) -

Analog-to-digital converters (ADC) RM0440
594/2140 RM0440 Rev 9
21.4 ADC functional description
21.4.1 ADC block diagram
[Figure 82](../figures/figure_82.md) shows the ADC block diagram and [Table 163](../tables/table_163.md) gives the ADC pin description.
[Figure 82](../figures/figure_82.md). ADC block diagram
MSv46143V4
adc_ext0_trg
CONT
SMPx[2:0]
sampling time
Start & Stop
Control
ADC_INP[18:0]
analog input
channels
AUTDLY
auto delayed
ADSTP
stop conv
S/W trigger
EXTEN[1:0]
trigger enable
and edge selection
h/w
trigger
EXTi mapped
at product level EXTSEL[4:0]
trigger selection
ADEN/ADDIS
ADCAL
Analog Supply (VDDA)
1.62V to 3.6 V
VREF+
1.62 to 3.6 V
ALIGN
left/right
RES[1:0]
12, 10, 8 bits
OVRMOD
overrun mode
DMAEN
adc_dma
adc_it
AHB
adc_awd1
JEXTEN[1:0]
trigger enable
and edge selection
H/W
trigger
JEXTSEL[4:0] trigger
selection
JEXTi mapped
at product level
JL[1:0], JSQx[4:0]
L[3:0], SQx[4:0]
JAUTO
DMACFG
AWD1EN
JAWD1EN
Analog watchdog 1,2,3
AWD1SGL
J S/W trigger
AWD1CH[4:0]
JQM
Injced Context
Queue Mode
LT1[11:0]
HT1[11:0]
JDISCEN
JDISCNUM[2:0]
DISCEN
DISCNUM[2:0]
Discontinuous
mode
AWD1
AWD2CH[18:0]
AWD3CH[18:0]
LT2[7:0]
HT2[7:0]
LT3[7:0]
HT3[7:0]
AWD2
AWD3
.......
.......
slave master
RDATA[15:0]
VREF-
VTS
VREFINT
VBAT/3 VINP[18:0]
VINN[18:0]
JDATA1[15:0]
JDATA2[15:0]
JDATA3[15:0]
JDATA4[15:0]
ROVSM
TROVS
JOVSE
ROVSE
OVSS[3:0]
OVSR[2:0]
Oversampling
options
DEEPPWD
REGADVREGEN
ADCALDIF
JQDIS
SMPTRIG
BULB
SWTRIG
SMPPLUS
AWDFILT[2:0]
OFFSETy[11:0]
OFFSETPOS
SATEN
OFFSETy_CH[4:0]
OFFSETy_EN
DIFSEL[18:0] CALFACT_D/S[6:0]
GCOMPCOEFF
[13:0]
GCOMP
ADC_INN[18:0]
AHB
interface
AREADY
EOSMP
EOC
EOS
OVR
JEOS
JQOVF
AWDx
Input
selection &
scan control
VIN
start
CONVERTED
DATA
Bias & Ref
SAR ADC
Oversampler
/Gain&Offset
adc_ext1_trg
adc_ext2_trg
adc_ext29_trg
adc_ext30_trg
adc_ext31_trg
adc_jext0_trg
adc_jext1_trg
adc_jext2_trg
adc_jext29_trg
adc_jext30_trg
adc_jext31_trg
adc_awd2
adc_awd3
adc_ker_ck
adc_hclk

RM0440 Rev 9 595/2140
RM0440 Analog-to-digital converters (ADC)
713
21.4.2 ADC pins a nd internal signals
[Table 162](../tables/table_162.md). ADC internal input/output signals
Internal signal name Signal
type Description
adc_ext_trg[31:0] Inputs
Up to 32 external trigger inputs for the regular
conversions (can be connected to on-chip timers).
These inputs are shared between the ADC master
and the ADC slave.
adc_jext_trg[31:0] Inputs
Up to 31 external trigger inputs for the injected
conversions (can be connected to on-chip timers).
These inputs are shared between the ADC master
and the ADC slave.
adc_awdx_out Output Internal analog watchdog output signal connected to
on-chip timers (x = Analog watchdog number 1,2,3)
adc_ker_ck Output ADC kernel clock
adc_hclk Input ADC peripheral clock
adc_it Output ADC interrupt
adc_dma Output ADC DMA request
VTS Input Output voltage from internal temperature sensor
VREFINT Input Output voltage from internal reference voltage
VBAT
Input
supply External battery voltage supply
[Table 163](../tables/table_163.md). ADC input/output pins
Pin name Signal type Comments
VREF+ Input, analog reference
positive The higher/positive reference voltage for the ADC
VDDA Input, analog supply Analog power supply equal V DDA
VREF− Input, analog reference
negative
The lower/negative reference voltage for the ADC.
VREF− is internally connected to VSSA
VSSA Input, analog supply
ground
Ground for analog power supply. On device package
which do not have a dedicated VSSA pin, VSSA is
internally connected to VSS.
VINPi Positive analog input
channels for each ADC
Connected either to ADCx_INPi external channels or
to internal channels. This input is converted in single-
ended mode
VINNi Negative analog input
channels for each ADC
Connected either to VREF− or to external channels:
ADCx_INNi and ADCx_INP[i+1].

Analog-to-digital converters (ADC) RM0440
596/2140 RM0440 Rev 9
21.4.3 ADC clocks
Dual clock domain architecture
The dual clock-domain architecture means that the ADC clock is independent from the AHB
bus clock.
The input clock is the same for all ADCs and can be selected between two different clock
sources (see [Figure 83](../figures/figure_83.md): ADC clock scheme):
1. The ADC clock can be a specific clock source, derived from the following clock
sources:
– The system clock
– PLL “P” clock
Refer to RCC Section for more information on how to generate ADC dedicated clock.
To select this scheme, bits CKMODE[1:0] of the ADCx_CCR register must be reset.
2. The ADC clock can be derived from the AHB clock of the ADC bus interface, divided by
a programmable factor (1, 2 or 4). In this mode, a programmable divider factor can be
selected (/1, 2 or 4 according to bits CKMODE[1:0]).
To select this scheme, bits CKMODE[1:0] of the ADCx_CCR register must be different
from 00.
Note: For option 2), a prescaling factor of 1 (C KMODE[1:0] = 01) can be used only if the AHB
prescaler is set (HPRE[3:0] = 0xxx in RCC_CFGR register).
Option 1) has the advantage of reaching the maximum ADC clock frequency whatever the
AHB clock scheme selected. The ADC clock can eventually be divided by the following ratio:
1, 2, 4, 6, 8, 12, 16, 32, 64, 128, 256; using the prescaler configured with bits PRESC[3:0] in
the ADCx_CCR register.
Option 2) has the advantage of bypassing the clock domain resynchronizations. This can be
useful when the ADC is triggered by a timer and if the application requires that the ADC is
precisely triggered without any uncertainty (otherwise, an uncertainty of the trigger instant
time is added by the resynchronizations between the two clock domains).
ADCx_INNi Negative external analog
input signals
Up to 19 analog input channels (x = ADC number = 1,
2, 3, 4 or 5).
Refer to Section 21.4.4: ADC1/2/3/4/5 connectivity for
details.
ADCx_INPi Positive external analog
input signals
Up to 19 analog input channels (x = ADC number = 1,
2, 3, 4 or 5).
Refer to Section 21.4.4: ADC1/2/3/4/5 connectivity for
details
[Table 163](../tables/table_163.md). ADC input/output pins (continued)
Pin name Signal type Comments

RM0440 Rev 9 597/2140
RM0440 Analog-to-digital converters (ADC)
713
Clock ratio constraint between ADC clock and AHB clock
There are generally no constraints to be respected for the ratio between the ADC clock and
the AHB clock except if some injected channels are programmed. In this case, it is
mandatory to respect the following ratio:
• Fadc_hclk ≥ FADC / 4 if the resolution of all channels are 12-bit or 10-bit
• Fadc_hclk ≥ FADC / 3 if there are some channels with resolutions equal to 8-bit (and none
with lower resolution)
• Fadc_hclk ≥ FADC / 2 if there are some channels with resolutions equal to 6-bit
[Figure 83](../figures/figure_83.md). ADC clock scheme
MSv46144V4
Others
00
RCC
(Reset and
clock
controller)
(ADC1, ADC2) or (ADC3, ADC4, ADC5)
AHB interface
Analog ADC1 or 3
(master)
Analog ADC2 or 4
(slave)
Analog ADC5
(single)
/1 or /2 or /4
/1, 2, 4, 6, 8, 10,
12, 16, 32, 64,
128, 256
Bits PRESC[3:0]
of ADCx_CCR
Bits CKMODE[1:0]
of ADCx_CCR
adc_hclk
Bits CKMODE[1:0]
of ADCx_CCR
adc_ker_ck
(1)
(1) Synchronous clock sources
No jitter from trimer to conversion start
ADC12SEL[1:0]
or
ADC345SEL[1:0]
- System clock
- PLL ‘P’ output
(1)
(2)
(2) Asynchronous clock sources
Better ADC frequency tuning independently from system and AHB clock
Fadc

Analog-to-digital converters (ADC) RM0440
598/2140 RM0440 Rev 9
21.4.4 ADC1/2/3/4/5 connectivity
ADC1, ADC2, ADC3, ADC4 and ADC5 are tightly coupled and share some external
channels as described in the below figures.
ADCy_INPx correspond to ADCy_INx pins defined in the product datasheet.
[Figure 84](../figures/figure_84.md). ADC1 connectivity
MSv46145V5
SAR
ADC1
ADC1
ADC12_INP1
ADC12_INP2
ADC1_INP3
ADC1_INP4
ADC1_INP5
ADC12_INP6
VINP[1]
VINN[1]
VINP[2]
Fast channel
VINP[0]
VINN[0] Fast channelVSSA
VINN[2]
VINP[3]
Fast channel
VINN[3]
VINP[4]
Fast channel
VINN[4]
VINP[5]
Fast channel
VINN[5]
VINP[6]
Fast channel
VINN[6] Slow channel
VINP[8]
VINN[8]
VINP[9]
VINP[7]
VINN[7]
VINN[9]
VINP[10]
VINN[10]
VINP[11]
VINN[11]
VINP[12]
VINN[12]
VINP[13]
VINN[13]
VINP[14]
VINN[14]
VINP[15]
VINN[15]
VINP[16]
VINN[16]
VINP[17]
VINN[17]
VINP[18]
VINN[18]VSSA
VSSA
VSSA
VREF+
VREFINT
ADC12_INP7
ADC12_INP8
ADC12_INP9
ADC1_INP10
ADC1_INP11
ADC12_INP14
ADC1_INP15
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
VINP
VINN
VTS
VREF-
Channel selection
VSSA
VBAT/3
VSSA
ADC12_INN1
ADC1_INN2
ADC1_INN3
ADC1_INN4
ADC12_INN5
ADC12_INN6
ADC12_INN7
ADC12_INN8
ADC1_INN9
ADC1_INN10
ADC1_INP12
ADC1_INN11
VSSA
ADC1_INN14
VOPAMP1
internal
output Reserved

RM0440 Rev 9 599/2140
RM0440 Analog-to-digital converters (ADC)
713
[Figure 85](../figures/figure_85.md). ADC2 connectivity
MSv46146V4
SAR
ADC2
ADC2
ADC12_INP1
ADC12_INP2
ADC2_INP3
ADC2_INP4
ADC2_INP5
ADC12_INP6
VINP[1]
VINN[1]
VINP[2]
Fast channel
VINP[0]
VINN[0] Fast channelVSSA
VINN[2]
VINP[3]
Fast channel
VINN[3]
VINP[4]
Fast channel
VINN[4]
VINP[5]
Fast channel
VINN[5]
VINP[6]
Fast channel
VINN[6] Slow channel
VINP[8]
VINN[8]
VINP[9]
VINP[7]
VINN[7]
VINN[9]
VINP[10]
VINN[10]
VINP[11]
VINN[11]
VINP[12]
VINN[12]
VINP[13]
VINN[13]
VINP[14]
VINN[14]
VINP[15]
VINN[15]
VINP[16]
VINN[16]
VINP[17]
VINN[17]
VINP[18]
VINN[18]VSSA
VSSA
VREF+
ADC12_INP7
ADC12_INP8
ADC12_INP9
ADC2_INP10
ADC2_INP11
ADC12_INP14
ADC2_INP15
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
VINP
VINN
VOPAMP2
internal
output
VREF-
Channel selection
VSSA
ADC2_INP12
ADC2_INP13
ADC2_INP17
VSSA
ADC12_INN1
ADC2_INN2
ADC2_INN3
ADC2_INN4
ADC12_INN5
ADC12_INN6
ADC12_INN7
ADC12_INN8
ADC2_INN9
ADC2_INN10
ADC2_INN11
ADC2_INN12
ADC2_INN13
ADC2_INN14
VOPAMP3
internal
output
Reserved

Analog-to-digital converters (ADC) RM0440
600/2140 RM0440 Rev 9
[Figure 86](../figures/figure_86.md). ADC3 connectivity
MSv46147V5
SAR
ADC3
ADC3
ADC3_INP1
ADC3_INP2
ADC3_INP3
ADC3_INP4
ADC3_INP5
ADC345_INP6
VINP[1]
VINN[1]
VINP[2]
Fast channel
VINP[0]
VINN[0] Fast channelVSSA
VINN[2]
VINP[3]
Fast channel
VINN[3]
VINP[4]
Fast channel
VINN[4]
VINP[5]
Fast channel
VINN[5]
VINP[6]
Fast channel
VINN[6] Slow channel
VINP[8]
VINN[8]
VINP[9]
VINP[7]
VINN[7]
VINN[9]
VINP[10]
VINN[10]
VINP[11]
VINN[11]
VINP[12]
VINN[12]
VINP[13]
VINN[13]
VINP[14]
VINN[14]
VINP[15]
VINN[15]
VINP[16]
VINN[16]
VINP[17]
VINN[17]
VINP[18]
VINN[18]VSSA
VSSA
VSSA
VREF+
VREFINT
ADC345_INP7
ADC345_INP8
ADC345_INP9
ADC345_INP10
ADC345_INP11
ADC345_INP14
ADC345_INP15
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
VINP
VINN
VOPAMP3
internal
output
VREF-
Channel selection
ADC3_INP12
VSSA
ADC345_INP16
VBAT/3
VOPAMP6
Internal
output
VSSA
ADC3_INN1
ADC3_INN2
ADC3_INN3
ADC3_INN4
ADC345_INN5
ADC345_INN6
ADC345_INN7
ADC345_INN8
ADC345_INN9
ADC345_INN10
ADC3_INN11
Reserved
(1)
(2)
(1)
(2)
For category 3 devices only
For category 4 devices only
Note: in category 4 devices the ADC345_xxx pins correspond to ADC3_xxx pins.

RM0440 Rev 9 601/2140
RM0440 Analog-to-digital converters (ADC)
713
[Figure 87](../figures/figure_87.md). ADC4 connectivity
MSv46148V1
SAR
ADC4
ADC4
ADC4_INP1
ADC4_INP2
ADC4_INP3
ADC4_INP4
ADC4_INP5
ADC345_INP6
VINP[1]
VINN[1]
VINP[2]
Fast channel
VINP[0]
VINN[0] Fast channelVSSA
VINN[2]
VINP[3]
Fast channel
VINN[3]
VINP[4]
Fast channel
VINN[4]
VINP[5]
Fast channel
VINN[5]
VINP[6]
Fast channel
VINN[6] Slow channel
VINP[8]
VINN[8]
VINP[9]
VINP[7]
VINN[7]
VINN[9]
VINP[10]
VINN[10]
VINP[11]
VINN[11]
VINP[12]
VINN[12]
VINP[13]
VINN[13]
VINP[14]
VINN[14]
VINP[15]
VINN[15]
VINP[16]
VINN[16]
VINP[17]
VINN[17]
VINP[18]
VINN[18]VSSA
VSSA
VSSA
VREF+
VREFINT
ADC345_INP7
ADC345_INP8
ADC345_INP9
ADC345_INP10
ADC345_INP11
ADC345_INP14
ADC345_INP15
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
VINP
VINN
VREF-
Channel selection
ADC45_INP12
ADC345_INP16
VOPAMP6
internal
output
ADC45_INP13
VSSA
ADC4_INN1
ADC4_INN2
ADC4_INN3
ADC4_INN4
ADC345_INN5
ADC345_INN6
ADC345_INN7
ADC345_INN8
ADC345_INN9
ADC345_INN10
ADC45_INN11
ADC45_INN12
ADC345_INN13
ADC345_INN14
ADC345_INN15

Analog-to-digital converters (ADC) RM0440
602/2140 RM0440 Rev 9
[Figure 88](../figures/figure_88.md). ADC5 connectivity
MSv46149V4
SAR
ADC5
ADC5
ADC5_INP1
ADC5_INP2
ADC345_INP6
VINP[1]
VINN[1]
VINP[2]
Fast channel
VINP[0]
VINN[0] Fast channelVSSA
VINN[2]
VINP[3]
Fast channel
VINN[3]
VINP[4]
Fast channel
VINN[4]
VINP[5]
Fast channel
VINN[5]
VINP[6]
Fast channel
VINN[6] Slow channel
VINP[8]
VINN[8]
VINP[9]
VINP[7]
VINN[7]
VINN[9]
VINP[10]
VINN[10]
VINP[11]
VINN[11]
VINP[12]
VINN[12]
VINP[13]
VINN[13]
VINP[14]
VINN[14]
VINP[15]
VINN[15]
VINP[16]
VINN[16]
VINP[17]
VINN[17]
VINP[18]
VINN[18]VSSA
VSSA
VSSA
VREF+
VREFINT
ADC345_INP7
ADC345_INP8
ADC345_INP9
ADC345_INP10
ADC345_INP11
ADC345_INP14
ADC345_INP15
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
Slow channel
VINP
VINN
VREF-
Channel selection
ADC45_INP12
ADC345_INP16
VBAT/3
ADC45_INP13
VSSA
VSSA
VTS
VSSA
ADC5_INN1
VSSAVOPAMP5
internal
output
ADC345_INN6
ADC345_INN7
ADC345_INN8
ADC345_INN9
ADC345_INN10
ADC45_INN11
ADC45_INN12
ADC345_INN13
ADC345_INN14
ADC345_INN15
VOPAMP4
internal
output Reserved

RM0440 Rev 9 603/2140
RM0440 Analog-to-digital converters (ADC)
713
21.4.5 Slave AHB interface
The ADCs implement an AHB slave port for control/status register and data access. The
features of the AHB interface are listed below:
• Word (32-bit) accesses
• Single cycle response
• Response to all read/write accesses to the registers with zero wait states.
The AHB slave interface does not support split/retry requests, and never generates AHB
errors.
21.4.6 ADC Deep-power-down mode (D EEPPWD) and ADC voltage regulator
(ADVREGEN)
By default, the ADC is in Deep-power-down mode where its supply is internally switched off
to reduce the leakage currents (the reset state of bit DEEPPWD is 1 in the ADC_CR
register).
To start ADC operations, follow the sequence below:
1. Exit Deep-power-down mode  by clearing DEEPPWD bit.
2. Enable the ADC voltage r egulator by setting ADVREGEN.
3. Wait for the startup time to configure the ADC (refer to the device datasheet for the
value of the startup time).
When ADC operations are complete, the ADC can be disabled (ADEN = 0). It is possible to
save power by also disabling the ADC voltage regulator. This is done by writing bit
ADVREGEN = 0.
Then, to save more power by reducing the leakage currents, it is also possible to re-enter in
ADC Deep-power-down mode by setting bit DEEPPWD = 1 into ADC_CR register. This is
particularly interesting before entering Stop mode.
Note: Writing DEEPPWD = 1 automatically disa bles the ADC voltage regulator and bit
ADVREGEN is automatically cleared.
When the internal voltage regulator is disabled (ADVREGEN = 0), the internal analog
calibration is kept.
In ADC Deep-power-down mode (DEEPPWD = 1), the internal analog calibration is lost and
it is necessary to either relaunch a calibration or re-apply the calibration factor which was
previously saved (refer to Section 21.4.8: Calibration (ADCAL, ADCALDIF,
ADC_CALFACT)).

Analog-to-digital converters (ADC) RM0440
604/2140 RM0440 Rev 9
21.4.7 Single-ended and diff erential input channels
Channels can be configured to be either single-ended input or differential input by
programming DIFSEL[i] bits in the ADC_DIFSEL register. This configuration must be written
while the ADC is disabled (ADEN = 0). Note that the DIFSEL[i] bits corresponding to single-
ended channels are always programmed at 0.
In single-ended input mode, the analog voltage to be converted for channel “i” is the
difference between the ADCy_INPx external voltage equal to VINP[i] (positive input) and
VREF− (negative input).
In differential input mode, the analog voltage to be converted for channel “i” is the difference
between the ADCy_INPx external voltage positive input equal to VINP[i], and the
ADCy_INNx negative input equal to VINN[i].
The input voltage in differential mode ranges from VREF- to VREF+, which makes a full scale
range of 2xVREF+. When VINP[i] equals VREF-, VINN[i] equals VREF+and the maximum
negative input differential voltage (VREF-) corresponds to 0x000 ADC output. When VINP[i]
equals VREF+, VINN[i] equals VREF- and the maximum positive input differential voltage
(VREF+) corresponds to 0xFFF ADC output. When VINP[i] and VINN[i] are connected together,
the zero input differential voltage corresponds to 0x800 ADC output.
The ADC sensitivity in differential mode is twice smaller than in single-ended mode.
When ADC is configured as differential mode, both inputs should be biased at (VREF+) / 2
voltage. Refer to the device datasheet for the allowed common mode input voltage VCMIN.
The input signals are supposed to be differential (common mode voltage should be fixed).
Internal channels (such as VTS and VREFINT) are used in single-ended mode only.
For a complete description of how the input channels are connected for each ADC, refer to
Section 21.4.4: ADC1/2/3/4/5 connectivity.
Caution: When configuring the channel “i” in differential input mode, its negative input voltage VINN[i]
is connected to another channel. As a consequence, this channel is no longer usable in
single-ended mode or in differential mode and must never be configured to be converted.
Some channels are shared between ADC1/ADC2/ADC3/ADC4/ADC5: this can make the
channel on the other ADC unusable. The only exception is when ADC master and the slave
operate in interleaved mode.
21.4.8 Calibration (ADCAL, ADCALDIF, ADC_CALFACT)
Each ADC provides an automatic calibration procedure which drives all the calibration
sequence including the power-on/off sequence of the ADC. During the procedure, the ADC
calculates a calibration factor which is 7-bit wide and which is applied internally to the ADC
until the next ADC power-off. During the calibration procedure, the application must not use
the ADC and must wait until calibration is complete.
Calibration is preliminary to any ADC operation. It removes the offset error which may vary
from chip to chip due to process or bandgap variation.
The calibration factor to be applied for single-ended input conversions is different from the
factor to be applied for differential input conversions:
• Write ADCALDIF = 0 before launching a calibration to be applied for single-ended input
conversions.
• Write ADCALDIF = 1 before launching a calibration to be applied for differential input
conversions.

RM0440 Rev 9 605/2140
RM0440 Analog-to-digital converters (ADC)
713
The calibration is then initiated by software by setting bit ADCAL = 1. Calibration can only be
initiated when the ADC is disabled (when ADEN = 0). ADCAL bit stays at 1 during all the
calibration sequence. It is then cleared by hardware as soon the calibration completes. At
this time, the associated calibration factor is stored internally in the analog ADC and also in
the bits CALFACT_S[6:0] or CALFACT_D[6:0] of ADC_CALFACT register (depending on
single-ended or differential input calibration)
The internal analog calibration is kept if the ADC is disabled (ADEN = 0). However, if the
ADC is disabled for extended periods, then it is recommended that a new calibration cycle is
run before re-enabling the ADC.
The internal analog calibration is lost each time the power of the ADC is removed (example,
when the product enters in Standby or VBAT mode). In this case, to avoid spending time
recalibrating the ADC, it is possible to re-write the calibration factor into the ADC_CALFACT
register without recalibrating, supposing that the software has previously saved the
calibration factor delivered during the previous calibration.
The calibration factor can be written if the ADC is enabled but not converting (ADEN = 1 and
ADSTART = 0 and JADSTART = 0). Then, at the next start of conversion, the calibration
factor is automatically injected into the analog ADC. This loading is transparent and does
not add any cycle latency to the start of the conversion. It is recommended to recalibrate
when VREF+ voltage changed more than 10%.
Software procedure to calibrate the ADC
1. Ensure DEEPPWD = 0, ADVREGEN = 1 and that  ADC voltage regulator startup time
has elapsed.
2. Ensure that ADEN = 0.
3. Select the input mode for this calibration by setting ADCALDIF = 0 (single-ended input)
or ADCALDIF = 1 (differential input).
4. Set ADCAL.
5. Wait until ADCAL = 0.
6. The calibration factor can be read from ADC_CALFACT register.
[Figure 89](../figures/figure_89.md). ADC calibration
tCAB
ADCAL
ADC State
CALFACT_x[6:0] 0x00 Calibration factor
ADCALDIF 0: Single-ended input     1: Differential input
MSv30263V2
OFF Startup Calibrate OFF
Indicative timingsby S/W by H/W

Analog-to-digital converters (ADC) RM0440
606/2140 RM0440 Rev 9
Software procedure to re-inject a calibration factor into the ADC
1. Ensure ADEN = 1 and ADSTART = 0 and JADSTART = 0 (ADC enabled and no
conversion is ongoing).
2. Write CALFACT_S and CALFACT_D with the new calibration factors.
3. When a conversion is launched, the calibrati on factor is injected into the analog ADC
only if the internal analog calibration factor differs from the one stored in bits
CALFACT_S for single-ended input channel or bits CALFACT_D for differential input
channel.
[Figure 90](../figures/figure_90.md). Updating the ADC calibration factor
Converting single-ended and differential analog inputs with a single ADC
If the ADC is supposed to convert both differential and single-ended inputs, two calibrations
must be performed, one with ADCALDIF = 0 and one with ADCALDIF = 1. The procedure is
the following:
1. Disable the ADC.
2. Calibrate the ADC in single-ended input mode (with ADCALDIF = 0). This updates the
register CALFACT_S[6:0].
3. Calibrate the ADC in  differential input modes (with ADCALDIF = 1). This updates the
register CALFACT_D[6:0].
4. Enable the ADC, configure the channels an d launch the conversions. Each time there
is a switch from a single-ended to a differential inputs channel (and vice-versa), the
calibration is automatically injected into the analog ADC.
WRITE ADC_CALFACT
ADC state
CALFACT_S[6:0] F2
F1Internal
calibration factor[6:0]
Start conversion
(hardware or sofware)
F2
Ready (not converting) Converting channel Ready Converting channel
(Single ended) (Single ended)
MSv30529V2
Updating calibration
by s/w by h/w

RM0440 Rev 9 607/2140
RM0440 Analog-to-digital converters (ADC)
713
[Figure 91](../figures/figure_91.md). Mixing single-ended and differential channels
21.4.9 ADC on-off contro l (ADEN, ADDIS, ADRDY)
First of all, follow the procedure explained in Section 21.4.6: ADC Deep-power-down mode
(DEEPPWD) and ADC voltage regulator (ADVREGEN)).
Once DEEPPWD = 0 and ADVREGEN = 1, the ADC can be enabled and the ADC needs a
stabilization time of tSTAB before it starts converting accurately, as shown in [Figure 92](../figures/figure_92.md). Two
control bits enable or disable the ADC:
• ADEN = 1 enables the ADC. The flag ADRDY is set once the ADC is ready for
operation.
• ADDIS = 1 disables the ADC. ADEN and ADDIS are then automatically cleared by
hardware as soon as the analog ADC is effectively disabled.
Regular conversion can then start either by setting ADSTART = 1 (refer to Section 21.4.18:
Conversion on external trigger and trigger polarity (EXTSEL, EXTEN, JEXTSEL, JEXTEN))
or when an external trigger event occurs, if triggers are enabled.
Injected conversions start by setting JADSTART = 1 or when an external injected trigger
event occurs, if injected triggers are enabled.
Software procedure to enable the ADC
1. Clear the ADRDY bit in the ADC_ISR register by writing 1.
2. Set ADEN.
3. Wait until ADRDY = 1 (ADRDY is set after the ADC startup time). This can be done
using the associated interrupt (setting ADRDYIE = 1).
4. Clear the ADRDY bit in the ADC_ISR register by writing 1 (optional).
Caution: ADEN bit cannot be set when ADCAL is set and during four ADC clock cycles after the
ADCAL bit is cleared by hardware (end of the calibration).
ADC state
CALFACT_S[6:0] F2
F2Internal
calibration factor[6:0]
CONV CH 1
CALFACT_D[6:0] F3
Single ended
inputs channel)
CONV CH3 CONV CH4
(Single inputs
channel)
F3 F2
Trigger event
RDY RDY RDY
MSv30530V2
CONV CH2RDY
(Differential
inputs channel)
(Differential
inputs channel)

Analog-to-digital converters (ADC) RM0440
608/2140 RM0440 Rev 9
Software procedure to disable the ADC
1. Check that both ADSTART = 0 and JADSTART = 0 to ensure that no conversion is
ongoing. If required, stop any regular and injected conversion ongoing by setting
ADSTP = 1 and JADSTP = 1 and then wait until ADSTP = 0 and JADSTP = 0.
2. Set ADDIS.
3. If required by the application, wait unt il ADEN = 0, until the analog ADC is effectively
disabled (ADDIS is automatically reset once ADEN = 0).
[Figure 92](../figures/figure_92.md). Enabling / disabling the ADC
21.4.10 Constraints when wr iting the ADC control bits
The software is allowed to write the RCC control bits to configure and enable the ADC clock
(refer to RCC Section), the DIFSEL[i] control bits in the ADC_DIFSEL register and the
control bits ADCAL and ADEN in the ADC_CR register, only if the ADC is disabled (ADEN
must be equal to 0).
The software is then allowed to write the control bits ADSTART, JADSTART and ADDIS of
the ADC_CR register only if the ADC is enabled and there is no pending request to disable
the ADC (ADEN must be equal to 1 and ADDIS to 0).
For all the other control bits of the ADC_CFGR, ADC_SMPRx, ADC_TRy, ADC_SQRy,
ADC_JDRy, ADC_OFRy, ADC_OFCHRy and ADC_IER registers:
• For control bits related to configuration of regular conversions, the software is allowed
to write them only if the ADC is enabled (ADEN = 1) and if there is no regular
conversion ongoing (ADSTART must be equal to 0).
• For control bits related to configuration of injected conversions, the software is allowed
to write them only if the ADC is enabled (ADEN = 1) and if there is no injected
conversion ongoing (JADSTART must be equal to 0).
• ADC_TRy registers can be modified when an analog-to-digital conversion is ongoing
(refer to Section 21.4.28: Analog window watchdog (AWD1EN, JAWD1EN, AWD1SGL,
AWD1CH, AWD2CH, AWD3CH, AWD_HTx, AWD_LTx, AWDx)for details).
MSv62472V1
tSTAB
ADEN
ADRDY
ADDIS
ADC
state  Converting CH OFF
by H/Wby S/W
REQ
-OFOFF Startup RDY RDY

RM0440 Rev 9 609/2140
RM0440 Analog-to-digital converters (ADC)
713
The software is allowed to write the ADSTP or JADSTP control bits of the ADC_CR register
only if the ADC is enabled, possibly converting, and if there is no pending request to disable
the ADC (ADSTART or JADSTART must be equal to 1 and ADDIS to 0).
The software can write the register ADC_JSQR at any time, when the ADC is enabled
(ADEN = 1) and JADSTART is cleared. The software is allowed to modify on-the-fly the
ADC_JSQR register when JADSTART is set (injected conversions are ongoing) only when
the context queue is enabled (JQDIS = 0 in the ADC_CFGR register). Refer to
Section 21.7.16: ADC injected sequence register (ADC_JSQR) for additional details.
Note: There is no hardware protection to pr event these forbidden write accesses and ADC
behavior may become in an unknown state. To recover from this situation, the ADC must be
disabled (clear ADEN as well as all the bits of ADC_CR register).
21.4.11 Channel selection (ADC_SQRy, ADC_JSQR)
There are up to 19 multiplexed channels per ADC:
• Up to 13 slow analog inputs coming from GPIO pads (ADCx_INP/INN[6:18])
Depending on the products, not all of them are available on GPIO pads.
• The ADCs are connected to the following internal analog inputs:
– The internal reference voltage (V REFINT) is connected to ADC1_INP18,
ADC3_INP18, ADC4_INP18 and ADC5_INP18.
– The internal temperature sensor (V TS) is connected to ADC1_INP16 and
ADC5_INP4.
–T h e  V BAT monitoring channel (VBAT/3) is connected to ADC1_INP17,
ADC3_INP17 and ADC5_INP17.
Note: To convert one of the internal analog channe ls, the corresponding analog sources must first
be enabled by programming bits VREFEN, VBATSEL or VSENSESEL in the ADCx_CCR
registers.
It is possible to organize the conversions in two groups: regular and injected. A group
consists of a sequence of conversions that can be done on any channel and in any order.
For instance, it is possible to implement the conversion sequence in the following order:
ADCx_INP/INN3, ADCx_INP/INN8, ADCx_INP/INN2, ADCx_INN/INP2, ADCx_INP/INN0,
ADCx_INP/INN2, ADCx_INP/INN2, ADCx_INP/INN15.
• A regular group is composed of up to 16 conversions. The regular channels and their
order in the conversion sequence must be selected in the ADC_SQRy registers. The
total number of conversions in the regular group must be written in the L[3:0] bits in the
ADC_SQR1 register.
• An injected group is composed of up to 4 conversions. The injected channels and
their order in the conversion sequence must be selected in the ADC_JSQR register.
The total number of conversions in the injected group must be written in the L[1:0] bits
in the ADC_JSQR register.
ADC_SQRy registers must not be modified while regular conversions can occur. For this,
the ADC regular conversions must be first stopped by writing ADSTP = 1 (refer to
Section 21.4.17: Stopping an ongoing conversion (ADSTP , JADSTP)).
The software is allowed to modify on-the-fly the ADC_JSQR register when JADSTART is set
(injected conversions ongoing) only when the context queue is enabled (JQDIS = 0 in
ADC_CFGR register). Refer to Section 21.4.21: Queue of context for injected conversions

Analog-to-digital converters (ADC) RM0440
610/2140 RM0440 Rev 9
21.4.12 Channel-wise programmabl e sampling time (SMPR1, SMPR2)
Before starting a conversion, the ADC must establish a direct connection between the
voltage source under measurement and the embedded sampling capacitor of the ADC. This
sampling time must be enough for the input voltage source to charge the embedded
capacitor to the input voltage level.
Each channel can be sampled with a different sampling time which is programmable using
the SMP[2:0] bits in the ADC_SMPR1 and ADC registers. It is therefore possible to select
among the following sampling time values:
• SMP = 000: 2.5 ADC clock cycles
• SMP = 001: 6.5 ADC clock cycles
• SMP = 010: 12.5 ADC clock cycles
• SMP = 011: 24.5 ADC clock cycles
• SMP = 100: 47.5 ADC clock cycles
• SMP = 101: 92.5 ADC clock cycles
• SMP = 110: 247.5 ADC clock cycles
• SMP = 111: 640.5 ADC clock cycles
The total conversion time is calculated as follows:
TCONV = Sampling time + 12.5 ADC clock cycles
Example:
With Fadc_ker_ck = 30 MHz and a sampling time of 2.5 ADC clock cycles:
TCONV = (2.5 + 12.5) ADC clock cycles = 15 ADC clock cycles = 500 ns
The ADC notifies the end of the sampling phase by setting the status bit EOSMP (only for
regular conversion).
Constraints on the sampling time
For each channel, SMP[2:0] bits must be programmed to respect a minimum sampling time
as specified in the ADC characteristics section of the datasheets.
Bulb sampling mode
When the BULB bit is set in ADC register, the sampling period starts immediately after the
last ADC conversion. A hardware or software trigger starts the conversion after the sampling
time has been programmed in ADC_SMPR1 register. The very first ADC conversion, after
the ADC is enabled, is performed with the sampling time programmed in SMP bits. The Bulb
mode is effective starting from the second conversion.
The maximum sampling time is limited (refer to the ADC characteristics section of the
datasheet).
The Bulb mode is neither compatible with the continuous conversion mode nor with the
injected channel conversion.
When the BULB bit is set, it is not allowed to set SMPTRIG bit in ADC_CFGR2.

RM0440 Rev 9 611/2140
RM0440 Analog-to-digital converters (ADC)
713
[Figure 93](../figures/figure_93.md). Bulb mode timing diagram
Sampling time control trigger mode
When the SMPTRIG bit is set, the sampling time programmed though SMPx bits is not
applicable. The sampling time is controlled by the trigger signal edge.
When a hardware trigger is selected, each rising edge of the trigger signal starts the
sampling period. A falling edge ends the sampling period and starts the conversion. The
EXTEN[1:0] bits must be set to 01. Hardware triggers with not defined rising and falling
edges (one pulse event) cannot be used in Bulb mode.
When a software trigger is selected, the software trigger is not the ADSTART bit in ADC_CR
but the SWTRIG bit. SWTRIG bit has to be set to start the sampling period, and the
SWTRIG bit has to be cleared to end the sampling period and start the conversion.
EXTEN[1:0] bits must be set to 00.
The maximum sampling time is limited (refer to the ADC characteristics section of the
datasheet).
This mode is neither compatible with the continuous conversion mode, nor with the injected
channel conversion.
When SMPTRIG bit is set, it is not allowed to set BULB bit.
I/O analog switch voltage booster
The resistance of the I/O analog switches increases when the VDDA voltage is too low. The
sampling time must consequently be adapted accordingly (refer to the device datasheet for
the corresponding electrical characteristics). This resistance can be minimized at low VDDA
voltage by enabling an internal voltage booster through the BOOSTEN bit of the
SYSCFG_CFGR1 register.
SMPPLUS control bit
When a sampling time of 2.5 ADC clock cycles is selected, the total conversion time
becomes 15 cycles in 12-bit mode. If the dual interleaved mode is used (see Section :
Interleaved mode with independent injected), the sampling interval cannot be equal to the
value specified since an even number of cycles is required for the conversion. The
SMPPLUS bit can be used to change the sampling time 2.5 ADC clock cycles into 3.5 ADC
clock cycles. In this way, the total conversion time becomes 16 clock cycles, thus making
possible to interleave every 8 cycles.
MSv46157V2
ADC state
Trigger
Normal (discontinuous) mode
idle sample conversion idle conversionsample idle
ADC state
Trigger
BULB (continuous) mode
idle sample conversion conversionsample sample
Sampling time programmed in
SMP bits

Analog-to-digital converters (ADC) RM0440
612/2140 RM0440 Rev 9
21.4.13 Single conversion mode (CONT = 0)
In Single conversion mode, the ADC performs once all the conversions of the channels.
This mode is started with the CONT bit at 0 by either:
• Setting the ADSTART bit in the ADC_CR register (for a regular channel)
• Setting the JADSTART bit in the ADC_CR register (for an injected channel)
• External hardware trigger event (for a regular or injected channel)
Inside the regular sequence, after each conversion is complete:
• The converted data are stored into the 16-bit ADC_DR register
• The EOC (end of regular conversion) flag is set
• An interrupt is generated if the EOCIE bit is set
Inside the injected sequence, after each conversion is complete:
• The converted data are stored into one of the four 16-bit ADC_JDRy registers
• The JEOC (end of injected conversion) flag is set
• An interrupt is generated if the JEOCIE bit is set
After the regular sequence is complete:
• The EOS (end of regular sequence) flag is set
• An interrupt is generated if the EOSIE bit is set
After the injected sequence is complete:
• The JEOS (end of injected sequence) flag is set
• An interrupt is generated if the JEOSIE bit is set
Then the ADC stops until a new external regular or injected trigger occurs or until bit
ADSTART or JADSTART is set again.
Note: To convert a single channel, program a sequence with a length of 1.
21.4.14 Continuous conversion mode (CONT = 1)
This mode applies to regular channels only.
In continuous conversion mode, when a software or hardware regular trigger event occurs,
the ADC performs once all the regular conversions of the channels and then automatically
restarts and continuously converts each conversions of the sequence. This mode is started
with the CONT bit at 1 either by external trigger or by setting the ADSTART bit in the
ADC_CR register.
Inside the regular sequence, after each conversion is complete:
• The converted data are stored into the 16-bit ADC_DR register
• The EOC (end of conversion) flag is set
• An interrupt is generated if the EOCIE bit is set
After the sequence of conversions is complete:
• The EOS (end of sequence) flag is set
• An interrupt is generated if the EOSIE bit is set
Then, a new sequence restarts immediately and the ADC continuously repeats the
conversion sequence.

RM0440 Rev 9 613/2140
RM0440 Analog-to-digital converters (ADC)
713
Note: To convert a single channel, program a sequence with a length of 1.
It is not possible to have both discontinuous mode and continuous mode enabled: it is
forbidden to set both DISCEN = 1 and CONT = 1.
Injected channels cannot be converted continuously. The only exception is when an injected
channel is configured to be converted automatically after regular channels in continuous
mode (using JAUTO bit), refer to Auto-injection mode section).
21.4.15 Starting conversi ons (ADSTART, JADSTART)
Software starts ADC regular conversions by setting ADSTART = 1.
When ADSTART is set, the conversion starts:
• Immediately: if EXTEN[1:0] = 00 (software trigger)
• At the next active edge of the selected regular hardware trigger: if EXTEN[1:0] is not
equal to 00
Software starts ADC injected conversions by setting JADSTART = 1.
When JADSTART is set, the conversion starts:
• Immediately, if JEXTEN[1:0] = 00 (software trigger)
• At the next active edge of the selected injected hardware trigger: if JEXTEN[1:0] is not
equal to 00
Note: In auto-injection mode (JAUTO = 1), use AD START bit to start the regular conversions
followed by the auto-injected conversions (JADSTART must be kept cleared).
ADSTART and JADSTART also provide information on whether any ADC operation is
currently ongoing. It is possible to re-configure the ADC while ADSTART = 0 and
JADSTART = 0 are both true, indicating that the ADC is idle.
ADSTART is cleared by hardware:
• In single mode with software regular trigger (CONT = 0, EXTSEL = 0x0)
– At any end of regular conversion sequence  (EOS assertion) or at any end of
subgroup processing if DISCEN = 1
• In all cases (CONT=x, EXTSEL=x)
– After execution of the ADSTP procedure asserted by the software.
Note: In continuous mode (CONT = 1), ADSTART is not  cleared by hardware with the assertion of
EOS because the sequence is automatically relaunched.
When a hardware trigger is selected in single mode (CONT = 0 and EXTSEL ≠0x00),
ADSTART is not cleared by hardware with the assertion of EOS to help the software which
does not need to reset ADSTART again for the next hardware trigger event. This ensures
that no further hardware triggers are missed.
JADSTART is cleared by hardware:
• In single mode with software injected trigger (JEXTSEL = 0x0)
– At any end of injected conversion seque nce (JEOS assertion) or at any end of
subgroup processing if JDISCEN = 1
• in all cases (JEXTSEL=x)
– After execution of the JADSTP proc edure asserted by the software.
Note: When the software trigger is selected, ADSTART bit should not be set if the EOC flag is still
high.

Analog-to-digital converters (ADC) RM0440
614/2140 RM0440 Rev 9
21.4.16 ADC timing
The elapsed time between the start of a conversion and the end of conversion is the sum of
the configured sampling time plus the successive approximation time depending on data
resolution:
[Figure 94](../figures/figure_94.md). Analog-to-digital conversion time
1. t SMPL depends on SMP[2:0].
2. t SAR depends on RES[2:0].
21.4.17 Stopping an ongoing co nversion (ADSTP, JADSTP)
The software can decide to stop regular conversions ongoing by setting ADSTP = 1 and
injected conversions ongoing by setting JADSTP = 1.
Stopping conversions resets the ongoing ADC operation. Then the ADC can be
reconfigured (ex: changing the channel selection or the trigger) ready for a new operation.
Note that it is possible to stop injected conversions while regular conversions are still
operating and vice-versa. This allows, for instance, re-configuration of the injected
conversion sequence and triggers while regular conversions are still operating (and vice-
versa).
When the ADSTP bit is set by software, any ongoing regular conversion is aborted with
partial result discarded (ADC_DR register is not updated with the current conversion).
When the JADSTP bit is set by software, any ongoing injected conversion is aborted with
partial result discarded (ADC_JDRy register is not updated with the current conversion).
The scan sequence is also aborted and reset (meaning that relaunching the ADC would
restart a new sequence).
Once this procedure is complete, bits ADSTP/ADSTART (in case of regular conversion), or
JADSTP/JADSTART (in case of injected conversion) are cleared by hardware and the
TCONV= TSMPL + TSAR = [2.5 |min + 12.5 |12bit ] x TADC_CLK
TCONV = TSMPL + TSAR = 83.33 ns |min + 416.67 ns |12bit = 500.0 ns (for FADC = 30 MHz)
MSv30532V2
Sampling Ch(N+1)
Sample AIN(N+1)
Data N-1 Data N
ADC state
ADSTART
ADC_DR
Analog channel
Internal S/H
EOSMP
EOC
RDY
Set by
SW
Sampling Ch(N) Converting Ch(N)
Ch(N+1)
Hold AIN(N)
Ch(N)
Sample AIN(N)
Indicative timings
tSMPL
(1) tSAR
(2)
Set by
HW
Cleared
by SW
Set by
HW
Cleared by
HW/SW

RM0440 Rev 9 615/2140
RM0440 Analog-to-digital converters (ADC)
713
software must poll ADSTART (or JADSTART) until the bit is reset before assuming the ADC
is completely stopped.
Note: In auto-injection mode (JAUTO = 1), setting ADSTP bit aborts both regular and injected
conversions (JADSTP must not be used).
[Figure 95](../figures/figure_95.md). Stopping ongoing regular conversions
[Figure 96](../figures/figure_96.md). Stopping ongoing regular and injected conversions
MSv30533V2
C
Trigger
ADC state RDY Convert
Ch(N-1) RDY RDYSample
Ch(N)
REGULAR CONVERSIONS ongoing
(software is not allowed to configure regular conversions selection and triggers)
Cleared by
HW
Set by
SW
Data N-2 Data N-1
JADSTART
ADSTART
ADSTP
ADC_DR
Sample
Ch(N-1)
Trigger
Cleared by
HW
Cleared by
HW
MS30534V1
Sample
Ch(N-1)RDY
ADC_DR DATA N-1
RDY
ADSTP
JADSTART
REGULAR CONVERSIONS ongoing
Convert
Ch(N-1)
Regular trigger
Sample
Ch(M) C
Injected trigger
DATA N-2
RDY
(software is not allowed to configure regular conversions selection and triggers)
Set by
SW INJECTED CONVERSIONS ongoing
(software is not allowed to configure injected conversions selection and triggers)
JADSTP
ADC_JDR DATA M-1
Sampl RDY
ADSTART
Regular trigger
ADC state
Cleared
by HW
Cleared
by HW
Set by
SW
Cleared
by HW
Cleared
by HW
Set by
SW
Set by
SW

Analog-to-digital converters (ADC) RM0440
616/2140 RM0440 Rev 9
21.4.18 Conversion on external trigger and trigger polarity
(EXTSEL, EXTEN, JEXTSEL, JEXTEN)
A conversion or a sequence of conversions can be triggered either by software or by an
external event (e.g. timer capture, input pins). If the EXTEN[1:0] control bits (for a regular
conversion) or JEXTEN[1:0] bits (for an injected conversion) are different from 00, then
external events are able to trigger a conversion with the selected polarity.
When the Injected Queue is enabled (bit JQDIS = 0), injected software triggers are not
possible.
The regular trigger selection is effective once software has set bit ADSTART = 1 and the
injected trigger selection is effective once software has set bit JADSTART = 1.
Any hardware triggers which occur while a conversion is ongoing are ignored.
• If bit ADSTART = 0, any regular hardware triggers which occur are ignored.
• If bit JADSTART = 0, any injected hardware triggers which occur are ignored.
[Table 164](../tables/table_164.md) provides the correspondence between the EXTEN[1:0] and JEXTEN[1:0] values
and the trigger polarity.
Note: The polarity of the regular trigger cannot be changed on-the-fly.
Note: The polarity of the injected trigger can be anticipated and changed on-the-fly when the
queue is enabled (JQDIS = 0). Refer to Section 21.4.21: Queue of context for injected
conversions.
The EXTSEL and JEXTSEL control bits select which out of 32 possible events can trigger
conversion for the regular and injected groups.
A regular group conversion can be interrupted by an injected trigger.
[Table 164](../tables/table_164.md). Configuring the trigger polarity for regular external triggers
EXTEN[1:0] Source
00 Hardware Trigger detection disabl ed, software trigger detection enabled
01 Hardware Trigger with detection on the rising edge
10 Hardware Trigger with detection on the falling edge
11 Hardware Trigger with detection on both the rising and falling edges
[Table 165](../tables/table_165.md). Configuring the trigger polarity for injected external triggers
JEXTEN[1:0] Source
00
– If JQDIS = 1 (Queue disabled): Hardware trigger detection disabled, software
trigger detection enabled
– If JQDIS = 0 (Queue enabled), Hardware and software trigger detection
disabled
01 Hardware Trigger with detection on the rising edge
10 Hardware Trigger with detection on the falling edge
11 Hardware Trigger with detection on both the rising and falling edges

RM0440 Rev 9 617/2140
RM0440 Analog-to-digital converters (ADC)
713
Note: The regular trigger selection cannot be changed on-the-fly.
The injected trigger selection can be anticipated and changed on-the-fly. Refer to
Section 21.4.21: Queue of context for injected conversions on page 624
Each ADC master shares the same input triggers with its ADC slave as described in
[Figure 97](../figures/figure_97.md).
[Figure 97](../figures/figure_97.md). Triggers sharing between ADC master and ADC slave
[Table 166](../tables/table_166.md) to [Table 169](../tables/table_169.md) give all the possible external triggers of the three ADCs for regular
and injected conversions.
MSv46156V1
adc_ext_trg0
adc_ext_trg31
EXTSEL[3:0]
ADC MASTER
adc_ext_trg1
adc_jext_trg0
adc_jext_trg31
Injected sequencer
triggers
adc_jext_trg1
JEXTSEL[4:0]
External regular trigger
External injected trigger
EXTSEL[3:0]
ADC SLAVE
JEXTSEL[4:0]
External regular trigger
External injected trigger
..............
..............
Regular sequencer
triggers
[Table 166](../tables/table_166.md). ADC1/2 - External triggers for regular channels
Name Source Type EXTSEL[4:0]
adc_ext_trg tim1_oc1 Internal signal from on-chip timers 00000
adc_ext_trg1 tim1_oc2 Internal signal from on-chip timers 00001
adc_ext_trg2 tim1_oc3 Internal signal from on-chip timers 00010
adc_ext_trg3 tim2_oc2 Internal signal from on-chip timers 00011
adc_ext_trg4 tim3_trgo Internal signal from on-chip timers 00100
adc_ext_trg5 tim4_oc4 Internal signal from on-chip timers 00101
adc_ext_trg6 EXTI line 11 External pin 00110
adc_ext_trg7 tim8_trgo Internal signal from on-chip timers 00111
adc_ext_trg8 tim8_trgo2 Internal signal from on-chip timers 01000

Analog-to-digital converters (ADC) RM0440
618/2140 RM0440 Rev 9
adc_ext_trg9 tim1_trgo Internal signal from on-chip timers 01001
adc_ext_trg10 tim1_trgo2 Internal signal from on-chip timers 01010
adc_ext_trg11 tim2_trgo Internal signal from on-chip timers 01011
adc_ext_trg12 tim4_trgo Internal signal from on-chip timers 01100
adc_ext_trg13 tim6_trgo Internal signal from on-chip timers 01101
adc_ext_trg14 tim15_trgo Internal signal from on-chip timers 01110
adc_ext_trg15 tim3_oc4 Internal signal from on-chip timers 01111
adc_ext_trg16 tim20_trgo Internal signal from on-chip timers 10000
adc_ext_trg17 tim20_trgo2 Internal signal from on-chip timers 10001
adc_ext_trg18 tim20_oc1 Internal signal from on-chip timers 10010
adc_ext_trg19 tim20_oc2 Internal signal from on-chip timers 10011
adc_ext_trg20 tim20_oc3 Internal signal from on-chip timers 10100
adc_ext_trg21 hrtim_adc_trg1 Internal signal from on-chip timers 10101
adc_ext_trg22 hrtim_adc_trg3 Internal signal from on-chip timers 10110
adc_ext_trg23 hrtim_adc_trg5 Internal signal from on-chip timers 10111
adc_ext_trg24 hrtim_adc_trg6 Internal signal from on-chip timers 11000
adc_ext_trg25 hrtim_adc_trg7 Internal signal from on-chip timers 11001
adc_ext_trg26 hrtim_adc_trg8 Internal signal from on-chip timers 11010
adc_ext_trg27 hrtim_adc_trg9 Internal signal from on-chip timers 11011
adc_ext_trg28 hrtim_adc_trg10 Internal signal from on-chip timers 11100
adc_ext_trg29 lptim_out Internal signal from on-chip timers 11101
adc_ext_trg30 tim7_trgo Internal signal from on-chip timers 11110
adc_ext_trg31 reserved - 11111
[Table 166](../tables/table_166.md). ADC1/2 - External triggers for regular channels (continued)
Name Source Type EXTSEL[4:0]
[Table 167](../tables/table_167.md). ADC1/2 - External trigger for injected channels
Name Source Type JEXTSEL[4:0]
adc_jext_trg0 tim1_trgo Internal signal from on-chip timers 00000
adc_jext_trg1 tim1_oc4 Internal signal from on-chip timers 00001
adc_jext_trg2 tim2_trgo Internal si gnal from on-chip timers 00010
adc_jext_trg3 tim2_oc1 Internal signal from on-chip timers 00011
adc_jext_trg4 tim3_oc4 Internal si gnal from on-chip timers 00100
adc_jext_trg5 tim4_trgo Internal si gnal from on-chip timers 00101
adc_jext_trg6 EXTI line 15 External pin 00110
adc_jext_trg7 tim8_oc4 Internal signal from on-chip timers 00111
adc_jext_trg8 tim1_trgo2 Internal signal from on-chip timers 01000

RM0440 Rev 9 619/2140
RM0440 Analog-to-digital converters (ADC)
713
adc_jext_trg9 tim8_trgo Internal si gnal from on-chip timers 01001
adc_jext_trg10 tim8_trgo2 Internal signal from on-chip timers 01010
adc_jext_trg11 tim3_oc3 Internal signal from on-chip timers 01011
adc_jext_trg12 tim3_trgo Internal si gnal from on-chip timers 01100
adc_jext_trg13 tim3_oc1 Internal si gnal from on-chip timers 01101
adc_jext_trg14 tim6_trgo Internal signal from on-chip timers 01110
adc_jext_trg15 tim15_trgo Internal signal from on-chip timers 01111
adc_jext_trg16 tim20_trg o Internal signal from on-chip timers 10000
adc_jext_trg17 tim20_trgo2 Internal signal from on-chip timers 10001
adc_jext_trg18 tim20_oc4 Internal signal from on-chip timers 10010
adc_jext_trg19 hrtim_adc_t rg2 Internal signal from on-chip timers 10011
adc_jext_trg20 hrtim_adc_t rg4 Internal signal from on-chip timers 10100
adc_jext_trg21 hrtim_adc_t rg5 Internal signal from on-chip timers 10101
adc_jext_trg22 hrtim_adc_t rg6 Internal signal from on-chip timers 10110
adc_jext_trg23 hrtim_adc_trg 7 Internal signal from on-chip timers 10111
adc_jext_trg24 hrtim_adc_trg 8 Internal signal from on-chip timers 11000
adc_jext_trg25 hrtim_adc_trg 9 Internal signal from on-chip timers 11001
adc_jext_trg26 hrtim_adc_trg10 Internal signal from on-chip timers 11010
adc_jext_trg27 tim16_oc1 Internal signal from on-chip timers 11011
adc_jext_trg28 reserved - 11100
adc_jext_trg29 lptim_out Internal signal from on-chip timers 11101
adc_jext_trg30 tim7_trgo Internal si gnal from on-chip timers 11110
adc_jext_trg31 reserved - 11111
[Table 167](../tables/table_167.md). ADC1/2 - External trigger for injected channels (continued)
Name Source Type JEXTSEL[4:0]
[Table 168](../tables/table_168.md). ADC3/4/5 - External triggers for regular channels
Name Source Type EXTSEL[4:0]
adc_ext_trg0 tim3_oc1 Internal signal from on-chip timers 00000
adc_ext_trg1 tim2_oc3 Internal signal from on-chip timers 00001
adc_ext_trg2 tim1_oc3 Internal signal from on-chip timers 00010
adc_ext_trg3 tim8_oc1 Internal signal from on-chip timers 00011
adc_ext_trg4 tim3_trgo Internal signal from on-chip timers 00100
adc_ext_trg5 EXTI line 2 External pin 00101
adc_ext_trg6 tim4_oc1 Internal signal from on-chip timers 00110
adc_ext_trg7 tim8_trgo Internal signal from on-chip timers 00111

Analog-to-digital converters (ADC) RM0440
620/2140 RM0440 Rev 9
adc_ext_trg8 tim8_trgo2 Internal signal from on-chip timers 01000
adc_ext_trg9 tim1_trgo Internal signal from on-chip timers 01001
adc_ext_trg10 tim1_trgo2 Internal signal from on-chip timers 01010
adc_ext_trg11 tim2_trgo Internal signal from on-chip timers 01011
adc_ext_trg12 tim4_trgo Internal signal from on-chip timers 01100
adc_ext_trg13 tim6_trgo Internal signal from on-chip timers 01101
adc_ext_trg14 tim15_trgo Internal signal from on-chip timers 01110
adc_ext_trg15 tim2_oc1 Internal signal from on-chip timers 01111
adc_ext_trg16 tim20_trgo Internal signal from on-chip timers 10000
adc_ext_trg17 tim20_trgo2 Internal signal from on-chip timers 10001
adc_ext_trg18 tim20_oc1 Internal signal from on-chip timers 10010
adc_ext_trg19 hrtim_adc_trg2 Internal signal from on-chip timers 10011
adc_ext_trg20 hrtim_adc_trg4 Internal signal from on-chip timers 10100
adc_ext_trg21 hrtim_adc_trg1 Internal signal from on-chip timers 10101
adc_ext_trg22 hrtim_adc_trg3 Internal signal from on-chip timers 10110
adc_ext_trg23 hrtim_adc_trg5 Internal signal from on-chip timers 10111
adc_ext_trg24 hrtim_adc_trg6 Internal signal from on-chip timers 11000
adc_ext_trg25 hrtim_adc_trg7 Internal signal from on-chip timers 11001
adc_ext_trg26 hrtim_adc_trg8 Internal signal from on-chip timers 11010
adc_ext_trg27 hrtim_adc_trg9 Internal signal from on-chip timers 11011
adc_ext_trg28 hrtim_adc_trg10 Internal signal from on-chip timers 11100
adc_ext_trg29 lptim_out Internal signal from on-chip timers 11101
adc_ext_trg30 tim7_trgo Internal signal from on-chip timers 11110
adc_ext_trg31 reserved - 11111
[Table 168](../tables/table_168.md). ADC3/4/5 - External triggers for regular channels (continued)
Name Source Type EXTSEL[4:0]
[Table 169](../tables/table_169.md). ADC3/4/5 - External triggers for injected channels
Name Source Type JEXTSEL[4:0]
adc_jext_trg0 tim1_trgo Internal si gnal from on-chip timers 00000
adc_jext_trg1 tim1_oc4 Internal si gnal from on-chip timers 00001
adc_jext_trg2 tim2_trgo Internal si gnal from on-chip timers 00010
adc_jext_trg3 tim8_oc2 Internal si gnal from on-chip timers 00011
adc_jext_trg4 tim4_oc3 Internal si gnal from on-chip timers 00100
adc_jext_trg5 tim4_trgo Internal si gnal from on-chip timers 00101
adc_jext_trg6 tim4_oc4 Internal si gnal from on-chip timers 00110
adc_jext_trg7 tim8_oc4 Internal signal from on-chip timers 00111

RM0440 Rev 9 621/2140
RM0440 Analog-to-digital converters (ADC)
713
21.4.19 Injected channel management
Triggered injection mode
To use triggered injection, the JAUTO bit in the ADC_CFGR register must be cleared.
1. Start the conversion of a group of regular ch annels either by an external trigger or by
setting the ADSTART bit in the ADC_CR register.
2. If an external injected trigger occurs, or if  the JADSTART bit in the ADC_CR register is
set during the conversion of a regular group of channels, the current conversion is
adc_jext_trg8 tim1_trgo2 Internal signal from on-chip timers 01000
adc_jext_trg9 tim8_trgo Internal si gnal from on-chip timers 01001
adc_jext_trg10 tim8_trgo2 Internal signal from on-chip timers 01010
adc_jext_trg11 tim1_oc3 Internal signal from on-chip timers 01011
adc_jext_trg12 tim3_trgo Internal si gnal from on-chip timers 01100
adc_jext_trg13 EXTI line 3 External pin 01101
adc_jext_trg14 tim6_trgo Internal signal from on-chip timers 01110
adc_jext_trg15 tim15_trg o Internal signal from on-chip timers 01111
adc_jext_trg16 tim20_trg o Internal signal from on-chip timers 10000
adc_jext_trg17 tim20_trgo2 Internal signal from on-chip timers 10001
adc_jext_trg18 tim20_oc2 Internal signal from on-chip timers 10010
adc_jext_trg19 hrtim_adc_t rg2 Internal signal from on-chip timers 10011
adc_jext_trg20 hrtim_adc_t rg4 Internal signal from on-chip timers 10100
adc_jext_trg21 hrtim_adc_t rg5 Internal signal from on-chip timers 10101
adc_jext_trg22 hrtim_adc_t rg6 Internal signal from on-chip timers 10110
adc_jext_trg23 hrtim_adc_trg 7 Internal signal from on-chip timers 10111
adc_jext_trg24 hrtim_adc_trg 8 Internal signal from on-chip timers 11000
adc_jext_trg25 hrtim_adc_trg 9 Internal signal from on-chip timers 11001
adc_jext_trg26 hrtim_adc_trg10 Internal signal from on-chip timers 11010
adc_jext_trg27 hrtim_adc_trg 1 Internal signal from on-chip timers 11011
adc_jext_trg28 hrtim_adc_t rg3 Internal signal from on-chip timers 11100
adc_jext_trg29 lptim_out Internal signal from on-chip timers 11101
adc_jext_trg30 tim7_trgo Internal si gnal from on-chip timers 11110
adc_jext_trg31 reserved - 11111
[Table 169](../tables/table_169.md). ADC3/4/5 - External triggers for injected channels (continued)
Name Source Type JEXTSEL[4:0]

Analog-to-digital converters (ADC) RM0440
622/2140 RM0440 Rev 9
reset and the injected channel sequence switches are launched (all the injected
channels are converted once).
3. Then, the regular conversion of the regular group of channels is resumed from the last
interrupted regular conversion.
4. If a regular event occurs during an injected conversion, the injected conversion is not
interrupted but the regular sequence is executed at the end of the injected sequence.
[Figure 98](../figures/figure_98.md) shows the corresponding timing diagram.
Note: When using triggered injection, one must ens ure that the interval between trigger events is
longer than the injection sequence. For instance, if the sequence length is 30 ADC clock
cycles (that is two conversions with a sampling time of 2.5 clock periods), the minimum
interval between triggers must be 31 ADC clock cycles.
Auto-injection mode
If the JAUTO bit in the ADC_CFGR register is set, then the channels in the injected group
are automatically converted after the regular group of channels. This can be used to convert
a sequence of up to 20 conversions programmed in the ADC_SQRy and ADC_JSQR
registers.
In this mode, the ADSTART bit in the ADC_CR register must be set to start regular
conversions, followed by injected conversions (JADSTART must be kept cleared). Setting
the ADSTP bit aborts both regular and injected conversions (JADSTP bit must not be used).
In this mode, external trigger on injected channels must be disabled.
If the CONT bit is also set in addition to the JAUTO bit, regular channels followed by injected
channels are continuously converted.
Note: It is not possible to us e both the auto-injected and discontinuous modes simultaneously.
When the DMA is used for exporting regular sequencer’s data in JAUTO mode, it is
necessary to program it in circular mode. If the single-shot mode is selected, the JAUTO
sequence is stopped upon DMA Transfer Complete event.
[Figure 98](../figures/figure_98.md). Injected conversion latency
1. The maximum latency value can be found in the elec trical characteristics of the device datasheet.
MSv43771V1
adc_ker_ck
(1)
Injection event
Reset ADC
SOC
max. latency

RM0440 Rev 9 623/2140
RM0440 Analog-to-digital converters (ADC)
713
21.4.20 Discontinuous mode (DISCEN, DISCNUM, JDISCEN)
Regular group mode
This mode is enabled by setting the DISCEN bit in the ADC_CFGR register.
It is used to convert a short sequence (subgroup) of n conversions (n ≤ 8) that is part of the
sequence of conversions selected in the ADC_SQRy registers. The value of n is specified
by writing to the DISCNUM[2:0] bits in the ADC_CFGR register.
When an external trigger occurs, it starts the next n conversions selected in the ADC_SQRy
registers until all the conversions in the sequence are done. The total sequence length is
defined by the L[3:0] bits in the ADC_SQR1 register.
Example:
• DISCEN = 1, n = 3, channels to be converted = 1, 2, 3, 6, 7, 8, 9, 10, 11
– first trigger: channels converted are 1, 2, 3 (an EOC event is generated at each
conversion).
– second trigger: channels converted are 6,  7, 8 (an EOC event is generated at
each conversion).
– third trigger: channels converted are 9, 10,  11 (an EOC event is generated at each
conversion) and an EOS event is generated after the conversion of channel 11.
– fourth trigger: channels converted are 1, 2, 3 (an EOC event is generated at each
conversion).
–. . .
• DISCEN = 0, channels to be converted = 1, 2, 3, 6, 7, 8, 9, 10,11
– first trigger: the comp lete sequence is converted: channel 1, then 2, 3, 6, 7, 8, 9,
10 and 11. Each conversion generates an EOC event and the last one also
generates an EOS event.
– All the next trigger events relaunch the complete sequence.
Note: The channel numbers referred to in the above example might not be available on all
microcontrollers.
When a regular group is converted in discontinuous mode, no rollover occurs (the last
subgroup of the sequence can have less than n conversions).
When all subgroups are converted, the next trigger starts the conversion of the first
subgroup. In the example above, the fourth trigger reconverts the channels 1, 2 and 3 in the
first subgroup.
It is not possible to have both discontinuous mode and continuous mode enabled. In this
case (if DISCEN = 1, CONT = 1), the ADC behaves as if continuous mode was disabled.

Analog-to-digital converters (ADC) RM0440
624/2140 RM0440 Rev 9
Injected group mode
This mode is enabled by setting the JDISCEN bit in the ADC_CFGR register. It converts the
sequence selected in the ADC_JSQR register, channel by channel, after an external
injected trigger event. This is equivalent to discontinuous mode for regular channels where
‘n’ is fixed to 1.
When an external trigger occurs, it starts the next channel conversions selected in the
ADC_JSQR registers until all the conversions in the sequence are done. The total sequence
length is defined by the JL[1:0] bits in the ADC_JSQR register.
Example:
• JDISCEN = 1, channels to be converted = 1, 2, 3
– first trigger: channel 1 converted (a JEOC event is generated)
– second trigger: channel 2 conver ted (a JEOC event is generated)
– third trigger: channel 3 converted and a JEOC event + a JEOS event are
generated
–. . .
Note: The channel numbers referred to in the above example might not be available on all
microcontrollers.
When all injected channels have been converted, the next trigger starts the conversion of
the first injected channel. In the example above, the fourth trigger reconverts the first
injected channel 1.
It is not possible to use both auto-injected mode and discontinuous mode simultaneously:
the bits DISCEN and JDISCEN must be kept cleared by software when JAUTO is set.
21.4.21 Queue of context for injected conversions
A queue of context is implemented to anticipate up to 2 contexts for the next injected
sequence of conversions. JQDIS bit of ADC_CFGR register must be reset to enable this
feature. Only hardware-triggered conversions are possible when the context queue is
enabled.
This context consists of:
• Configuration of the injected triggers (bits JEXTEN[1:0] and JEXTSEL bits in
ADC_JSQR register)
• Definition of the injected sequence (bits JSQx[4:0] and JL[1:0] in ADC_JSQR register)
All the parameters of the context are defined into a single register ADC_JSQR and this
register implements a queue of 2 buffers, allowing the bufferization of up to 2 sets of
parameters:
• The ADC_JSQR register can be written at any moment even when injected
conversions are ongoing.
• Each data written into the ADC_JSQR register is stored into the Queue of context.
• At the beginning, the Queue is empty and the first write access into the ADC_JSQR
register immediately changes the context and the ADC is ready to receive injected
triggers.
• Once an injected sequence is complete, the Queue is consumed and the context
changes according to the next ADC_JSQR parameters stored in the Queue. This new
context is applied for the next injected sequence of conversions.

RM0440 Rev 9 625/2140
RM0440 Analog-to-digital converters (ADC)
713
• A Queue overflow occurs when writing into register ADC_JSQR while the Queue is full.
This overflow is signaled by the assertion of the flag JQOVF. When an overflow occurs,
the write access of ADC_JSQR register which has created the overflow is ignored and
the queue of context is unchanged. An interrupt can be generated if bit JQOVFIE is set.
• Two possible behaviors are possible when the Queue becomes empty, depending on
the value of the control bit JQM of register ADC_CFGR:
– If JQM = 0, the Queue is empt y just after enabling the ADC, but then it can never
be empty during run operations: the Queue always maintains the last active
context and any further valid start of injected sequence is served according to the
last active context.
– If JQM = 1, the Queue can be empty after the end of an injected sequence or if the
Queue is flushed. When this occurs, there is no more context in the queue and
hardware triggers are disabled. Therefore, any further hardware injected triggers
are ignored until the software re-writes a new injected context into ADC_JSQR
register.
• Reading ADC_JSQR register returns the current ADC_JSQR context which is active at
that moment. When the ADC_JSQR context is empty, JSQi is read as 0x00.
• The Queue is flushed when stopping injected conversions by setting JADSTP = 1 or
when disabling the ADC by setting ADDIS = 1:
– If JQM = 0, the Queue is maintained with the last active context.
– If JQM = 1, the Queue becomes em pty and triggers are ignored.
Note: When configured in discontinuous mode (bit  JDISCEN = 1), only the last trigger of the
injected sequence changes the context and consumes the Queue.The first trigger only
consumes the queue but others are still valid triggers as shown by the discontinuous mode
example below (length = 3 for both contexts):
• 1st trigger, discontinuous. Sequence 1: context 1 consumed, 1st conversion carried out
• 2nd trigger, discontinuous. Sequence 1: 2nd conversion.
• 3rd trigger, discontinuous. Sequence 1: 3rd conversion.
• 4th trigger, discontinuous. Sequence 2: context 2 consumed, 1st conversion carried out.
• 5th trigger, discontinuous. Sequence 2: 2nd conversion.
• 6th trigger, discontinuous. Sequence 2: 3rd conversion.

Analog-to-digital converters (ADC) RM0440
626/2140 RM0440 Rev 9
Behavior when changing the trigger or sequence context
The [Figure 99](../figures/figure_99.md) and [Figure 100](../figures/figure_100.md) show the behavior of the context Queue when changing the
sequence or the triggers.
[Figure 99](../figures/figure_99.md). Example of ADC_JSQR queue of context (sequence change)
1. Parameters:
P1: sequence of 3 conversions, hardware trigger 1
P2: sequence of 1 conversion, hardware trigger 1
P3: sequence of 4 conversions, hardware trigger 1
[Figure 100](../figures/figure_100.md). Example of ADC_JSQR queue of context (trigger change)
1. Parameters:
P1: sequence of 2 conversions, hardware trigger 1
P2: sequence of 1 conversion, hardware trigger 2
P3: sequence of 4 conversions, hardware trigger 1
MS30536V4
JSQR queue
Write ADC_JSQR
Trigger 1
ADC state
ADC J context
(returned by reading
ADC_JSQR)
P1 P2 P3
EMPTY
Conversion1 Conversion2 Conversion3
P1 P1,P2 P2,P3P2 P3
P1 P2 P3EMPTY
RDY RDY RDY Conversion1
MS30537V4
P1 P2 P3
Conversion1 Conversion2RDY RDY RDY Conversion1
P1 P2 P3EMPTY
EMPTY P1 P1,P2 P2,P3P2 P3
Ignored
Ignored
ADC_JSQR queue
Write ADC_JSQR
Trigger 1
ADC state
ADC J context
(returned by reading
ADC_JSQR)
Trigger 2

RM0440 Rev 9 627/2140
RM0440 Analog-to-digital converters (ADC)
713
Queue of context: Behavior when a queue overflow occurs
The [Figure 101](../figures/figure_101.md) and [Figure 102](../figures/figure_102.md) show the behavior of the context Queue if an overflow
occurs before or during a conversion.
[Figure 101](../figures/figure_101.md). Example of ADC_JSQR queue of context with overflow before conversion
1. Parameters:
P1: sequence of 2 conversions, hardware trigger 1
P2: sequence of 1 conversion, hardware trigger 2
P3: sequence of 3 conversions, hardware trigger 1
P4: sequence of 4 conversions, hardware trigger 1
[Figure 102](../figures/figure_102.md). Example of ADC_JSQR queue of context with overflow during conversion
1. Parameters:
P1: sequence of 2 conversions, hardware trigger 1
P2: sequence of 1 conversion, hardware trigger 2
P3: sequence of 3 conversions, hardware trigger 1
P4: sequence of 4 conversions, hardware trigger 1
MS30538V4
ADC_JSQR queue
Write ADC_JSQR
P1 P2
EMPTY
Trigger 1
ADC state Conversion1RDY Conversion2 RDY
P3
JQOVF
Cleared by SW
P1 P1, P2
P4
P2
P2P1EMPTY
P2, P4
=> Overflow,
ignored
JEOS
ADC J context
(returned by
reading
ADC_JSQR)
Trigger 2
Conversion1
MS30539V4
ADC_JSQR
queue
Write ADC_JSQR
P1 P2
EMPTY
Trigger 1
ADC state Conversion1RDY Conversion2 RDY
P3
JQOVF
Cleared by SW
P1 P1, P2
P4
P2
P2P1EMPTY
P2, P4
=> Overflow,
ignored
JEOS
ADC J context
(returned by
reading
ADC_JSQR)
Trigger 2
Conversion1

Analog-to-digital converters (ADC) RM0440
628/2140 RM0440 Rev 9
It is recommended to manage the queue overflows as described below:
• After each P context write into ADC_JSQR register, flag JQOVF shows if the write has
been ignored or not (an interrupt can be generated).
• Avoid Queue overflows by writing the third context (P3) only once the flag JEOS of the
previous context P2 has been set. This ensures that the previous context has been
consumed and that the queue is not full.
Queue of context: Behavior when the queue becomes empty
[Figure 103](../figures/figure_103.md) and [Figure 104](../figures/figure_104.md) show the behavior of the context Queue when the Queue
becomes empty in both cases JQM = 0 or 1.
[Figure 103](../figures/figure_103.md). Example of ADC_JSQR queue of context with empty queue (case JQM = 0)
1. Parameters:
P1: sequence of 1 conversion, hardware trigger 1
P2: sequence of 1 conversion, hardware trigger 1
P3: sequence of 1 conversion, hardware trigger 1
Note: When writing P3, the context changes i mmediately. However, because of internal
resynchronization, there is a latency and if a trigger occurs just after or before writing P3, it
can happen that the conversion is launched considering the context P2. To avoid this
situation, the user must ensure that there is no ADC trigger happening when writing a new
context that applies immediately.
MS30540V5
P1
The queue is not empty
and maintains P2 because JQM=0
Queue not empty
(P3 maintained)
P2 P3
Conversion1 Conversion1RDY RDY RDY RDY Conversion1 Conversion1 ConvRDY
EMPTY P1 P2 P3
P1, P2 P2 P3EMPTY P1ADC_JSQR queue
Write ADC_JSQR
Trigger 1
ADC state
ADC J context
(returned by
reading
ADC_JSQR)

RM0440 Rev 9 629/2140
RM0440 Analog-to-digital converters (ADC)
713
[Figure 104](../figures/figure_104.md). Example of ADC_JSQR queue of context with empty queue (case JQM = 1)
1. Parameters:
P1: sequence of 1 conversion, hardware trigger 1
P2: sequence of 1 conversion, hardware trigger 1
P3: sequence of 1 conversion, hardware trigger 1
Flushing the queue of context
The figures below show the behavior of the context Queue in various situations when the
queue is flushed.
[Figure 105](../figures/figure_105.md). Flushing ADC_JSQR queue of context by setting JADSTP = 1 (JQM = 0)
Case when JADSTP occurs during an ongoing conversion
1. Parameters:
P1: sequence of 1 conversion, hardware trigger 1
P2: sequence of 1 conversion, hardware trigger 1
P3: sequence of 1 conversion, hardware trigger 1
MS30541V3
Ignored
Queue becomes empty and triggers are
ignored because JQM=1P1 P2 P3
EMPTY
Conversion1 Conversion1
P1 P1,P2 P3 P2
P1 P2 P3EMPTY
RDY RDY RDYConversion1
ADC_JSQR
queue
Write ADC_JSQR
Trigger 1
ADC state
ADC J context
(returned by reading
ADC_JSQR)
RDY
EMPTY (0x00)
EMPTY EMPTY
EMPTY
Ignored
MS30542V2
ADC_JSQR
queue
Write ADC_JSQR
P1
P1
P2
EMPTY
Trigger 1
ADC state Conv1 RDY STP
P3
P1 P3
P1, P2 P3 P1
EMPTY
JADSTP
RDY Conversion1 RDY
Queue is flushed and maintains the
last active context (P2 is lost)
(Aborted)
JADSTART
ADC J context
(returned by
reading
ADC_JSQR)
Set by
S/W
Reset by
H/W
Reset by
H/W Set by
S/W

Analog-to-digital converters (ADC) RM0440
630/2140 RM0440 Rev 9
[Figure 106](../figures/figure_106.md). Flushing ADC_JSQR queue of context by setting JADSTP = 1 (JQM = 0)
Case when JADSTP occurs during an ongoing conversion and a new
trigger occurs.
1. Parameters:
P1: sequence of 1 conversion, hardware trigger 1
P2: sequence of 1 conversion, hardware trigger 1
P3: sequence of 1 conversion, hardware trigger 1
[Figure 107](../figures/figure_107.md). Flushing ADC_JSQR queue of context by setting JADSTP = 1 (JQM = 0)
Case when JADSTP occurs outside an ongoing conversion
1. Parameters:
P1: sequence of 1 conversion, hardware trigger 1
P2: sequence of 1 conversion, hardware trigger 1
P3: sequence of 1 conversion, hardware trigger 1
MS30543V2
ADC_JSQR queue
Write ADC_JSQR
P1
P1
P2
EMPTY
Trigger 1
ADC state RDY STP
P3
P1 P3
P1, P2
Conversion1 RDY
P1, P3P1
EMPTY
JADSTP
RDY
P3
RDY
Queue is flushed and maintains
the last active context
(P2 is lost)
(Aborted)
JADSTART
ADC J context
(returned by reading
ADC_JSQR)
Set by
S/W
Reset by
H/W
Conversion1Conv1
Reset by
H/W Set by
S/W
MS30544V3
ADC_JSQR
queue
Write
ADC_JSQR
P1
P1
P2
EMPTY
Trigger 1
ADC state RDY STP
P3
P1 P3
P1, P2
RDY
P1
EMPTY
JADSTP
P3
RDY
Queue is flushed and maintains the
last active context (P2 is lost)
JADSTART
ADC J context
(returned by
reading
ADC_JSQR)
Set by
S/W
Reset
by H/W
Conversion1
Reset
by H/W Set
by S/W

RM0440 Rev 9 631/2140
RM0440 Analog-to-digital converters (ADC)
713
[Figure 108](../figures/figure_108.md). Flushing ADC_JSQR queue of context by setting JADSTP = 1 (JQM = 1)
1. Parameters:
P1: sequence of 1 conversion, hardware trigger 1
P2: sequence of 1 conversion, hardware trigger 1
P3: sequence of 1 conversion, hardware trigger 1
[Figure 109](../figures/figure_109.md). Flushing ADC_JSQR queue of context by setting ADDIS = 1 (JQM = 0)
1. Parameters:
P1: sequence of 1 conversion, hardware trigger 1
P2: sequence of 1 conversion, hardware trigger 1
P3: sequence of 1 conversion, hardware trigger 1
MS30545V2
ADC_JSQR
queue
Write ADC_JSQR
P1
P1
P2
EMPTY
Trigger 1
ADC state RDY STP
P3
P1 P3
P1, P2
EMPTY
JADSTP
RDY
P3
RDY
Queue is flushed and  becomes empty
(P2 is lost)
(Aborted)
JADSTART
ADC J context
(returned by
reading
ADC_JSQR)
Set
by S/W
Reset
by H/W
Conversion1Conv1
Reset
by H/W
Set
by S/W
EMPTY
EMPTY (0x00) EMPTY
Ignored
EMPTY
MS30546V2
ADC_JSQR queue
ADC state RDY
P1
P1, P2
REQ-OFF
P1
ADDIS
Queue is flushed and maintains the
last active context (P2 which was not
consumed is lost)
ADC J context (returned by
reading ADC_JSQR)
Set
by S/W
Reset
by H/W
OFF

Analog-to-digital converters (ADC) RM0440
632/2140 RM0440 Rev 9
[Figure 110](../figures/figure_110.md). Flushing ADC_JSQR queue of context by setting ADDIS = 1 (JQM = 1)
1. Parameters:
P1: sequence of 1 conversion, hardware trigger 1
P2: sequence of 1 conversion, hardware trigger 1
P3: sequence of 1 conversion, hardware trigger 1
Queue of context: Starting the ADC with an empty queue
The following procedure must be followed to start ADC operation with an empty queue, in
case the first context is not known at the time the ADC is initialized. This procedure is only
applicable when JQM bit is reset:
5. Write a dummy ADC_JSQR with JEXTEN[1:0] not equal to 00 (otherwise triggering a
software conversion).
6. Set JADSTART.
7. Set JADSTP.
8. Wait until JADSTART is reset.
9. Set JADSTART.
Disabling the queue
It is possible to disable the queue by setting bit JQDIS = 1 into the ADC_CFGR register.
21.4.22 Programmable resolution (RES) - Fast conversion mode
It is possible to perform faster conversion by reducing the ADC resolution.
The resolution can be configured to be either 12, 10, 8, or 6 bits by programming the control
bits RES[1:0]. [Figure 115](../figures/figure_115.md), [Figure 116](../figures/figure_116.md), [Figure 117](../figures/figure_117.md) and [Figure 118](../figures/figure_118.md) show the conversion result
format with respect to the resolution as well as to the data alignment.
Lower resolution allows faster conversion time for applications where high-data precision is
not required. It reduces the conversion time spent by the successive approximation steps
according to [Table 170](../tables/table_170.md).
MS30547V4
ADC_JSQR
queue
ADC state RDY
P1
P1, P2
REQ-OFF
EMPTY
ADDIS
Queue is flushed and becomes empty
(ADC_JSQR is read as 0x00)
ADC J context (returned
by reading ADC_JSQR)
Set
by S/W
Reset
by H/W
OFF
EMPTY (0x00)

RM0440 Rev 9 633/2140
RM0440 Analog-to-digital converters (ADC)
713
21.4.23 End of conversion, end of  sampling phase (EOC, JEOC, EOSMP)
The ADC notifies the application for each end of regular conversion (EOC) event and each
injected conversion (JEOC) event.
The ADC sets the EOC flag as soon as a new regular conversion data is available in the
ADC_DR register. An interrupt can be generated if bit EOCIE is set. EOC flag is cleared by
the software either by writing 1 to it or by reading ADC_DR.
The ADC sets the JEOC flag as soon as a new injected conversion data is available in one
of the ADC_JDRy register. An interrupt can be generated if bit JEOCIE is set. JEOC flag is
cleared by the software either by writing 1 to it or by reading the corresponding ADC_JDRy
register.
The ADC also notifies the end of Sampling phase by setting the status bit EOSMP (for
regular conversions only). EOSMP flag is cleared by software by writing 1 to it. An interrupt
can be generated if bit EOSMPIE is set.
21.4.24 End of conversi on sequence (EOS, JEOS)
The ADC notifies the application for each end of regular sequence (EOS) and for each end
of injected sequence (JEOS) event.
The ADC sets the EOS flag as soon as the last data of the regular conversion sequence is
available in the ADC_DR register. An interrupt can be generated if bit EOSIE is set. EOS
flag is cleared by the software either by writing 1 to it.
The ADC sets the JEOS flag as soon as the last data of the injected conversion sequence is
complete. An interrupt can be generated if bit JEOSIE is set. JEOS flag is cleared by the
software either by writing 1 to it.
[Table 170](../tables/table_170.md). TSAR timings depending on resolution
RES
(bits)
TSAR
(ADC clock cycles)
TSAR (ns) at
FADC= 30 MHz
TCONV (ADC clock cycles)
(with Sampling Time=
2.5 ADC clock cycles)
TCONV (ns) at
FADC= 30 MHz
12 12.5 ADC clock cycles 416.67 ns 15 ADC clock cycles 500.0 ns
10 10.5 ADC clock cycles 350. 0 ns 13 ADC clock cycles 433.33 ns
8 8.5 ADC clock cycles 203.33 ns 11 ADC clock cycles 366.67 ns
6 6.5 ADC clock cycles 216.67 ns 9 ADC clock cycles 300.0 ns

Analog-to-digital converters (ADC) RM0440
634/2140 RM0440 Rev 9
21.4.25 Timing diagrams exampl e (single/continuous modes,
hardware/software triggers)
[Figure 111](../figures/figure_111.md). Single conversions of a sequence, software trigger
1. EXTEN[1:0] = 00, CONT = 0
2. Channels selected = 1,9, 10, 17; AUTDLY = 0.
[Figure 112](../figures/figure_112.md). Continuous conversion of a sequence, software trigger
1. EXTEN[1:0] = 00, CONT = 1
2. Channels selected = 1,9, 10, 17; AUTDLY = 0.
MS30549V1
RDY
EOC
EOS
CH1
by SW by HW
CH9 RDYCH10 CH17 CH1 CH9 CH10 CH17 RDY
ADC_DR D9 D10 D17 D1 D9 D10 D17
Indicative timings
D1
ADSTART(1)
ADC state(2)
MS30550V1
EOC
EOS
ADSTP
ADC_DR
READY CH1 CH9 CH1CH10 CH17 CH9 CH10 STP READY CH1
D9 D10 D17 D1 D9 D1D1
CH9
by SW by HW Indicative timings
ADC state(2)
ADCSTART(1)

RM0440 Rev 9 635/2140
RM0440 Analog-to-digital converters (ADC)
713
[Figure 113](../figures/figure_113.md). Single conversions of a sequence, hardware trigger
1. TRGx (over-frequency) is selected as trigger source, EXTEN[1:0] = 01, CONT = 0
2. Channels selected = 1, 2, 3, 4; AUTDLY = 0.
[Figure 114](../figures/figure_114.md). Continuous conversions of a sequence, hardware trigger
1. TRGx is selected as trigger source, EXTEN[1:0] = 10, CONT = 1
2. Channels selected = 1, 2, 3, 4; AUTDLY = 0.
MS31013V2
EOC
EOS
TRGX(1)
ADC_DR
RDY CH1 CH2 READYCH3 CH4 CH1 CH2 CH3 CH4 RDY
D2 D3 D4 D1 D2D1
by s/w by h/w
D3 D4
triggered ignored
ADSTART
ADC state(2)
Indicative timings
MS31014V2
EOC
EOS
TRGx(1)
ADC_DR
RDY CH1 CH2 CH1CH3 CH4 CH2 CH3 CH4 CH1 RDY
D2 D3 D4 D1 D2D1
by s/w by h/w Not in scale timings
D3 D4
triggered ignored
STOP
ADSTP
ADSTART
ADC(2)

Analog-to-digital converters (ADC) RM0440
636/2140 RM0440 Rev 9
21.4.26 Data management
Data register, data alignment and offset (ADC_DR, OFFSETy, OFFSETy_CH,
ALIGN)
Data and alignment
At the end of each regular conversion channel (when EOC event occurs), the result of the
converted data is stored into the ADC_DR data register which is 16 bits wide.
At the end of each injected conversion channel (when JEOC event occurs), the result of the
converted data is stored into the corresponding ADC_JDRy data register which is 16 bits
wide.
The ALIGN bit in the ADC_CFGR register selects the alignment of the data stored after
conversion. Data can be right- or left-aligned as shown in [Figure 115](../figures/figure_115.md), [Figure 116](../figures/figure_116.md), [Figure 117](../figures/figure_117.md)
and [Figure 118](../figures/figure_118.md).
Special case: when left-aligned, the data are aligned on a half-word basis except when the
resolution is set to 6-bit. In that case, the data are aligned on a byte basis as shown in
[Figure 117](../figures/figure_117.md) and [Figure 118](../figures/figure_118.md).
Note: Left-alignment is not supported in oversa mpling mode. When ROVSE and/or JOVSE bit is
set, the ALIGN bit value is ignored and the ADC only provides right-aligned data.
Offset
An offset y (y = 1,2,3,4) can be applied to a channel by setting the bit OFFSETy_EN = 1 into
ADC_OFRy register. The channel to which the offset is applied is programmed into the bits
OFFSETy_CH[4:0] of ADC_OFRy register. In this case, the converted value is decreased by
the user-defined offset written in the bits OFFSETy[11:0]. The result may be a negative
value so the read data is signed and the SEXT bit represents the extended sign value.
Note: Offset correction is not su pported in oversampling mode. When ROVSE and/or JOVSE bit is
set, the value of the OFFSETy_EN bit in ADC_OFRy register is ignored (considered as
reset).
[Table 173](../tables/table_173.md) describes how the comparison is performed for all the possible resolutions for
analog watchdog 1.
[Table 171](../tables/table_171.md). Offset computation versus data resolution
Resolution
(bits
RES[1:0])
Subtraction between raw
converted data and offset
Result CommentsRaw
converted
Data, left
aligned
Offset
00: 12-bit DATA[11:0] OFFSET[11:0] Signed
12-bit data -
01: 10-bit DATA[11:2],00 OFFSET[11:0] Signed
10-bit data
The user must configure OFFSET[1:0]
to 00

RM0440 Rev 9 637/2140
RM0440 Analog-to-digital converters (ADC)
713
When reading data from ADC_DR (regular channel) or from ADC_JDRy (injected channel, y
= 1,2,3,4) corresponding to the channel “i”:
• If one of the offsets is enabled (bit OFFSETy_EN = 1) for the corresponding channel,
the read data is signed.
• If none of the four offsets is enabled for this channel, the read data is not signed.
[Figure 115](../figures/figure_115.md), [Figure 116](../figures/figure_116.md), [Figure 117](../figures/figure_117.md) and [Figure 118](../figures/figure_118.md) show alignments for signed and
unsigned data.
[Figure 115](../figures/figure_115.md). Right alignment (offset disabled, unsigned value)
10: 8-bit DATA[11:4],00
00 OFFSET[11:0] Signed
8-bit data
The user must configure OFFSET[3:0]
to 0000
11: 6-bit DATA[11:6],00
0000 OFFSET[11:0] Signed
6-bit data
The user must configure OFFSET[5:0]
to 000000
[Table 171](../tables/table_171.md). Offset computation versus data resolution (continued)
Resolution
(bits
RES[1:0])
Subtraction between raw
converted data and offset
Result CommentsRaw
converted
Data, left
aligned
Offset
0 0 0 0 D11 D10 D9 D8 D7
12-bit data
D6 D5 D4 D3 D2 D1
0000000 D 7
8-bit data
D6 D5 D4 D3 D2 D1
0 0 0 0 0 0 D9 D8 D7
10-bit data
D6 D5 D4 D3 D2 D1
0000000
6-bit data
0D 5 D 4 D 3 D 2 D 1
D0
D0
D0
D0
bit15 bit0bit7
bit15 bit0bit7
bit15 bit0bit7
bit15 bit0bit7
MS31015V1
0
00

Analog-to-digital converters (ADC) RM0440
638/2140 RM0440 Rev 9
[Figure 116](../figures/figure_116.md). Right alignment (offset enabled, signed value)
[Figure 117](../figures/figure_117.md). Left alignment (offset disabled, unsigned value)
SEXT SEXT SEXT SEXT D11 D10 D9 D8 D7
12-bit data
D6 D5 D4 D3 D2 D1
D7
8-bit data
D6 D5 D4 D3 D2 D1
SEXT SEXT SEXT SEXT SEXT SEXT D9 D8 D7
10-bit data
D6 D5 D4 D3 D2 D1
6-bit data
D4 D3 D2 D1
D0
D0
D0
D0
bit15 bit0bit7
bit15 bit0bit7
bit15 bit0bit7
bit15 bit0bit7
MS31016V1
SEXT SEXT SEXT SEXT SEXT SEXT SEXT SEXT
D5SEXT SEXT SEXT SEXT SEXT SEXT SEXT SEXT SEXT SEXT
12-bit data
8-bit data
10-bit data
6-bit data
bit15 bit0bit7
bit15 bit0bit7
bit15 bit0bit7
bit15 bit0bit7
MS31017V1
D11 D10 D9 D8 D7 D6 D5 D4 D3 D2 D1 D0 0 0 0
D7 D6 D5 D4 D3 D2 D1 D0 0 0 0 0 0 0
D9 D8 D7 D6 D5 D4 D3 D2 D1 D0 0 0 0 0 0
0000000 D 4 D 3 D 2 D 1 D 0 0
0
0
0
0D50
0

RM0440 Rev 9 639/2140
RM0440 Analog-to-digital converters (ADC)
713
[Figure 118](../figures/figure_118.md). Left alignment (offset enabled, signed value)
Gain compensation
When GCOMP bit is set in ADC_CFGR2 register, the gain compensation is activated on all
the converted data. After each conversion, data is calculated with the following formula.
As GCOMPCOEFF can be programmed from 0 to 16383, the actual gain compensation
factor can range from 0 to 3.999756.
Before storing the resulting data in RDATA or JDATAx registers, the LSB−1 value is
evaluated to round up the data and minimize the error.
The gain compensation is also effective for the oversampling. When the gain compensation
is used for the oversampling mode, the gain calculation is performed after the accumulation
and right-shift operations to minimize the power consumption (the gain calculation is done
only once instead of at each conversion).
Offset compensation
When SATEN bit is set in ADC_OFRy register during offset operation, data are unsigned. All
the offset data saturate at 0x000 (in 12-bit mode). When OFFSETPOS bit is set, the offset
direction is positive and the data saturate at 0xFFF (in 12-bit mode). In 8-bit mode, data
saturate at 0x00 and 0xFF, respectively.
The analog watchdog comparison is performed on unsigned values, after offset and gain
compensation. For correct watchdog operation, the data after offset compensation must be
in unsigned format (SATEN bit set in ADC_OFRy register).
12-bit data
8-bit data
10-bit data
6-bit data
bit15 bit0bit7
bit15 bit0bit7
bit15 bit0bit7
bit15 bit0bit7
MS31018V1
0
0
0
SEXT D11 D10 D9 D8 D7 D6 D5 D4 D3 D2 D1 D0 0 0
SEXT D7 D6 D5 D4 D3 D2 D1 D0 0 0 0 0 0 0
SEXT D9 D8 D7 D6 D5 D4 D3 D2 D1 D0 0 0 0 0
SEXT SEXT SEXT SEXT SEXT SEXT SEXT D5 D4 D3 D2 D1 D0
0
SEXT SEXT
DATA DATA adc result() GCOMPCOEFF() 4096⁄×=

Analog-to-digital converters (ADC) RM0440
640/2140 RM0440 Rev 9
ADC overrun (OVR, OVRMOD)
The overrun flag (OSR) notifies of that a buffer overrun event occurred when the regular
converted data has not been read (by the CPU or the DMA) before new converted data
became available.
The OVR flag is set if the EOC flag is still 1 at the time when a new conversion completes.
An interrupt can be generated if bit OVRIE = 1.
When an overrun condition occurs, the ADC is still operating and can continue converting
unless the software decides to stop and reset the sequence by setting bit ADSTP = 1.
OVR flag is cleared by software by writing 1 to it.
It is possible to configure if data is preserved or overwritten when an overrun event occurs
by programming the control bit OVRMOD:
• OVRMOD = 0: The overrun event preserves the data register from being overrun: the
old data is maintained and the new conversion is discarded and lost. If OVR remains at
1, any further conversions occur but the result data is also discarded.
• OVRMOD = 1: The data register is overwritten with the last conversion result and the
previous unread data is lost. If OVR remains at 1, any further conversions operate
normally and the ADC_DR register always contains the latest converted data.
[Figure 119](../figures/figure_119.md). Example of overrun (OVR)
Note: There is no overrun detection on the inje cted channels since there is a dedicated data
register for each of the four injected channels.
Managing a sequence of conversions without using the DMA
If the conversions are slow enough, the conversion sequence can be handled by the
software. In this case the software must use the EOC flag and its associated interrupt to
handle each data. Each time a conversion is complete, EOC is set and the ADC_DR
register can be read. OVRMOD should be configured to 0 to manage overrun events as an
error.
Overun
MS31019V1
ADSTART(1)
EOC
EOS
TRGx(1)
ADC state(2)
ADC_DR read access
by s/w by h/w Indicative timingstriggered
RDY CH1 CH2 CH5CH3 CH4 CH6 CH7 STOP RDY
D2D1
D2D1 D6
D3 D4
D3 D4 D5
ADSTP
OVR
ADC_DR
(OVRMOD=0)
ADC_DR
(OVRMOD=1)

RM0440 Rev 9 641/2140
RM0440 Analog-to-digital converters (ADC)
713
Managing conversions without using the DMA and without overrun
It may be useful to let the ADC convert one or more channels without reading the data each
time (if there is an analog watchdog for instance). In this case, the OVRMOD bit must be
configured to 1 and OVR flag should be ignored by the software. An overrun event does not
prevent the ADC from continuing to convert and the ADC_DR register always contains the
latest conversion.
Managing conversions using the DMA
Since converted channel values are stored into a unique data register, it is useful to use
DMA for conversion of more than one channel. This avoids the loss of the data already
stored in the ADC_DR register.
When the DMA mode is enabled (DMAEN bit set in the ADC_CFGR register in single ADC
mode or MDMA different from 00 in dual ADC mode), a DMA request is generated after
each conversion of a channel. This allows the transfer of the converted data from the
ADC_DR register to the destination location selected by the software.
Despite this, if an overrun occurs (OVR = 1) because the DMA could not serve the DMA
transfer request in time, the ADC stops generating DMA requests and the data
corresponding to the new conversion is not transferred by the DMA. Which means that all
the data transferred to the RAM can be considered as valid.
Depending on the configuration of OVRMOD bit, the data is either preserved or overwritten
(refer to Section : ADC overrun (OVR, OVRMOD)).
The DMA transfer requests are blocked until the software clears the OVR bit.
Two different DMA modes are proposed depending on the application use and are
configured with bit DMACFG of the ADC_CFGR register in single ADC mode, or with bit
DMACFG of the ADC_CCR register in dual ADC mode:
• DMA one shot mode (DMACFG = 0).
This mode is suitable when the DMA is programmed to transfer a fixed number of data.
• DMA circular mode (DMACFG = 1)
This mode is suitable when programming the DMA in circular mode.
DMA one shot mode (DMACFG = 0)
In this mode, the ADC generates a DMA transfer request each time a new conversion data
is available and stops generating DMA requests once the DMA has reached the last DMA
transfer (when a transfer complete interrupt occurs - refer to DMA section) even if a
conversion has been started again.
When the DMA transfer is complete (all the transfers configured in the DMA controller have
been done):
• The content of the ADC data register is frozen.
• Any ongoing conversion is aborted with partial result discarded.
• No new DMA request is issued to the DMA controller. This avoids generating an
overrun error if there are still conversions which are started.
• Scan sequence is stopped and reset.
• The DMA is stopped.

Analog-to-digital converters (ADC) RM0440
642/2140 RM0440 Rev 9
DMA circular mode (DMACFG =1 )
In this mode, the ADC generates a DMA transfer request each time a new conversion data
is available in the data register, even if the DMA has reached the last DMA transfer. This
allows configuring the DMA in circular mode to handle a continuous analog input data
stream.
21.4.27 Dynamic low-power features
Auto-delayed conversion mode (AUTDLY)
The ADC implements an auto-delayed conversion mode controlled by the AUTDLY
configuration bit. Auto-delayed conversions are useful to simplify the software as well as to
optimize performance of an application clocked at low frequency where there would be risk
of encountering an ADC overrun.
When AUTDLY = 1, a new conversion can start only if all the previous data of the same
group has been treated:
• For a regular conversion: once the ADC_DR register has been read or if the EOC bit
has been cleared (see [Figure 120](../figures/figure_120.md)).
• For an injected conversion: when the JEOS bit has been cleared (see [Figure 121](../figures/figure_121.md)).
This is a way to automatically adapt the speed of the ADC to the speed of the system which
reads the data.
The delay is inserted after each regular conversion (whatever DISCEN = 0 or 1) and after
each sequence of injected conversions (whatever JDISCEN = 0 or 1).
Note: There is no delay inserted between each c onversions of the injected sequence, except after
the last one.
During a conversion, a hardware trigger event (for the same group of conversions) occurring
during this delay is ignored.
Note: This is not true for software  triggers where it remains possible during this delay to set the
bits ADSTART or JADSTART to restart a conversion: it is up to the software to read the data
before launching a new conversion.
No delay is inserted between conversions of different groups (a regular conversion followed
by an injected conversion or conversely):
• If an injected trigger occurs during the automatic delay of a regular conversion, the
injected conversion starts immediately (see [Figure 121](../figures/figure_121.md)).
• Once the injected sequence is complete, the ADC waits for the delay (if not ended) of
the previous regular conversion before launching a new regular conversion (see
[Figure 123](../figures/figure_123.md)).
The behavior is slightly different in auto-injected mode (JAUTO = 1) where a new regular
conversion can start only when the automatic delay of the previous injected sequence of
conversion has ended (when JEOS has been cleared). This is to ensure that the software
can read all the data of a given sequence before starting a new sequence (see [Figure 124](../figures/figure_124.md)).

RM0440 Rev 9 643/2140
RM0440 Analog-to-digital converters (ADC)
713
To stop a conversion in continuous auto-injection mode combined with autodelay mode
(JAUTO = 1, CONT = 1 and AUTDLY = 1), follow the following procedure:
1. Wait until JEOS = 1 (no more conversions are restarted)
2. Clear JEOS.
3. Set ADSTP .
4. Read the regular data.
If this procedure is not respected, a new regular sequence can restart if JEOS is cleared
after ADSTP has been set.
In AUTDLY mode, a hardware regular trigger event is ignored if it occurs during an already
ongoing regular sequence or during the delay that follows the last regular conversion of the
sequence. It is however considered pending if it occurs after this delay, even if it occurs
during an injected sequence of the delay that follows it. The conversion then starts at the
end of the delay of the injected sequence.
In AUTDLY mode, a hardware injected trigger event is ignored if it occurs during an already
ongoing injected sequence or during the delay that follows the last injected conversion of
the sequence.
[Figure 120](../figures/figure_120.md). AUTODLY = 1, regular conversion in continuous mode, software trigger
1. AUTDLY = 1.
2. Regular configuration: EXTEN[1:0] = 00 (SW trigger), CONT = 1, CHANNELS = 1,2,3.
3. Injected configuration DISABLED.
MS31020V1
Indicative timings
ADC_DR
ADSTART(1)
EOC
EOS
ADC state
ADC_DR read access
by SW by HW
RDY CH1 DLY CH3CH2 DLY DLY CH1 STOP RDY
ADSTP
DLY
D1 D1D2 D3

Analog-to-digital converters (ADC) RM0440
644/2140 RM0440 Rev 9
[Figure 121](../figures/figure_121.md). AUTODLY = 1, regular HW conversions interrupted by injected conversions
(DISCEN = 0; JDISCEN = 0)
1. AUTDLY = 1
2. Regular configuration: EXTEN[1:0] = 01 (HW trigger), CONT = 0, DISCEN = 0, CHANNELS = 1, 2, 3
3. Injected configuration: JEXTEN[1:0] = 01 (HW Trigger), JDISCEN = 0, CHANNELS = 5,6
MS31021V2
Injected
trigger
regular
JEOS
ADC_JDR1
ADC_JDR2
Regular
trigger
injected regular regular
DLY (CH1) DLY (CH2)
DLY (inj)
DLY (CH3)
Not ignored
(occurs during injected sequence)Ignored
DLY (CH1)
regular
Ignored
ADC_DR
EOC
EOS
ADC_DR
read access
by s/w by h/w Indicative timings
RDY CH1 DLY CH5CH2 DLY CH6 CH3 CH1 DLYDLY
D1 D1D2 D3
CH2
D6
D5
injectedregular
ADC state

RM0440 Rev 9 645/2140
RM0440 Analog-to-digital converters (ADC)
713
[Figure 122](../figures/figure_122.md). AUTODLY = 1, regular HW conversions interrupted by injected conversions
(DISCEN = 1, JDISCEN = 1)
1. AUTDLY = 1
2. Regular configuration: EXTEN[1:0] = 01 (HW trigger), CONT = 0, DISCEN = 1, DISCNUM = 1, CHANNELS = 1, 2, 3.
3. Injected configuration: JEXTEN[1:0] = 01 (HW Trigger), JDISCEN = 1, CHANNELS = 5,6
MS31022V1
IgnoredIgnored
Injected trigger
regular
JEOS
ADC_JDR1
ADC_JDR2
Regular trigger
ADC state
injected regularregular
DLY (CH1)
DLY (inj)
Not ignored (occurs during
injected sequence)
Ignored
regular
DLY (CH2)
ADC_DR
EOC
EOS
ADC_DR
read access
by SW by HW Indicative timings
RDY CH1 DLY DLYRDY CH2 RDY CH5 CH6 CH3RDY
D1 D1D2 D3
DLY
D6
D5
regular injected
RDY CH1 DLY RDY CH2
DLY (CH3) DLY (CH1)

Analog-to-digital converters (ADC) RM0440
646/2140 RM0440 Rev 9
[Figure 123](../figures/figure_123.md). AUTODLY = 1, regular continuous conversions interrupted by injected conversions
1. AUTDLY = 1
2. Regular configuration: EXTEN[1:0] = 00 (SW trigger), CONT = 1, DISCEN = 0, CHANNELS = 1, 2, 3
3. Injected configuration: JEXTEN[1:0] = 01 (HW Trigger), JDISCEN = 0, CHANNELS = 5,6
[Figure 124](../figures/figure_124.md). AUTODLY = 1 in auto- injected mode (JAUTO = 1)
1. AUTDLY = 1
2. Regular configuration: EXTEN[1:0] = 00 (SW trigger), CONT = 1, DISCEN = 0, CHANNELS = 1, 2
3. Injected configuration: JAUTO = 1, CHANNELS = 5,6
MS31023V3
regular
Ignored
Injected
trigger
regular
JEOS
ADC_JDR1
ADC_JDR2
injected
DLY (CH1) DLY (CH2)
DLY (inj)
regular
ADC_DR
EOC
EOS
ADC
state
ADC_DR read
access
by s/w by h/w Indicative timings
RDY CH1 DLY CH5CH2 DLY CH6 DLY DLY CH1CH3
D1 D2 D3
D6
D5
regular injected
DLY (CH3)
ADSTART(1)
MS31024V4
regular
JEOS
ADC_JDR1
ADC_JDR2
injected regular
DLY (CH1) DLY (inj)
regular
ADC_DR
EOC
EOS
ADC state
ADC_DR read access
by s/w by h/w Indicative timings
RDY CH1 CH6CH2 CH5 DLY CH1CH3
D1 D2 D3
D6
D5
regular injected
No delayADSTART(1)

RM0440 Rev 9 647/2140
RM0440 Analog-to-digital converters (ADC)
713
21.4.28 Analog window watchdog (A WD1EN, JAWD1EN, AWD1SGL,
AWD1CH, AWD2CH, AWD3CH, AWD_HTx, AWD_LTx, AWDx)
The three AWD analog watchdogs monitor whether some channels remain within a
configured voltage range (window).
[Figure 125](../figures/figure_125.md). Analog watchdog guarded area
AWDx flag and interrupt
An interrupt can be enabled for each of the 3 analog watchdogs by setting AWDxIE in the
ADC_IER register (x = 1,2,3).
AWDx (x = 1,2,3) flag is cleared by software by writing 1 to it.
The ADC conversion result is compared to the lower and higher thresholds before
alignment.
Description of analog watchdog 1
The AWD analog watchdog 1 is enabled by setting the AWD1EN bit in the ADC_CFGR
register. This watchdog monitors whether either one selected channel or all enabled
channels(1) remain within a configured voltage range (window).
[Table 172](../tables/table_172.md) shows how the ADC_CFGR registers should be configured to enable the analog
watchdog on one or more channels.
[Table 172](../tables/table_172.md). Analog watchdog channel selection
The AWD1 analog watchdog status bit is set if the analog voltage converted by the ADC is
below a lower threshold or above a higher threshold.
Channels guarded by the analog
watchdog AWD1SGL bit AWD1EN bit JAWD1EN bit
None x 0 0
All injected channels 0 0 1
All regular channels 0 1 0
All regular and injected channels 0 1 1
Single(1) injected channel
1. Selected by the AWD1CH[4:0] bits. The channels mu st also be programmed to be converted in the
appropriate regular or injected sequence.
101
Single(1) regular channel 1 1 0
Single(1) regular or injected channel 1 1 1
MS45396V1
Analog voltage
Higher threshold
Lower threshold
Guarded area
HTx
LTx

Analog-to-digital converters (ADC) RM0440
648/2140 RM0440 Rev 9
These thresholds are programmed in bits HT1[11:0] and LT1[11:0] of the ADC_TR1 register
for the analog watchdog 1. When converting data with a resolution of less than 12 bits
(according to bits RES[1:0]), the LSB of the programmed thresholds must be kept cleared
because the internal comparison is always performed on the full 12-bit raw converted data
(left aligned).
[Table 173](../tables/table_173.md) describes how the comparison is performed for all the possible resolutions for
analog watchdog 1.
Analog watchdog filter for watchdog 1
When an ADC is configured with only one input channel (selecting several channels in Scan
mode not allowed), a valid ADC conversion data filter can be configured:
• When converted data belong to the interval defined in ADC_TR1, the AWD1 flag
remains cleared.
• If data are out-of-range a number of times higher than the value specified in AWDFILT
bit of ADC_TR1, the AWD1 flag is set an the corresponding interrupt is issued.
Description of analog watchdog 2 and 3
The second and third analog watchdogs are more flexible and can guard several selected
channels by programming the corresponding bits in AWDxCH[18:0] (x=2,3).
The corresponding watchdog is enabled when any bit of AWDxCH[18:0] (x=2,3) is set.
They are limited to a resolution of 8 bits and only the 8 MSBs of the thresholds can be
programmed into HTx[7:0] and LTx[7:0]. [Table 174](../tables/table_174.md) describes how the comparison is
performed for all the possible resolutions.
[Table 173](../tables/table_173.md). Analog watchdog 1 comparison
Resolution(
bit
RES[1:0])
Analog watchdog comparison
between:
Comments
Raw converted data,
left aligned(1)
1. Refer to Section : Gain compensation for additional details on analog watchdog comparison.
Thresholds
00: 12-bit DATA[11:0] LT1[11:0] and
HT1[11:0] -
01: 10-bit DATA[11:2],00 LT1[11:0] and
HT1[11:0]
User must configure LT1[1:0] and HT1[1:0]
to 00
10: 8-bit DATA[11:4],0000 LT1[11:0] and
HT1[11:0]
User must configure LT1[3:0] and HT1[3:0]
to 0000
11: 6-bit DATA[11:6],000000 LT1[11:0] and
HT1[11:0]
User must configure LT1[5:0] and HT1[5:0]
to 000000

RM0440 Rev 9 649/2140
RM0440 Analog-to-digital converters (ADC)
713
ADCy_AWDx_OUT signal output generation
Each analog watchdog is associated to an internal hardware signal ADCy_AWDx_OUT
(y=ADC number, x=watchdog number) which is directly connected to the ETR input
(external trigger) of some on-chip timers. Refer to the on-chip timers section to understand
how to select the ADCy_AWDx_OUT signal as ETR.
ADCy_AWDx_OUT is activated when the associated analog watchdog is enabled:
• ADCy_AWDx_OUT is set when a guarded conversion is outside the programmed
thresholds.
• ADCy_AWDx_OUT is reset after the end of the next guarded conversion which is
inside the programmed thresholds (It remains at 1 if the next guarded conversions are
still outside the programmed thresholds).
• ADCy_AWDx_OUT is also reset when disabling the ADC (when setting ADDIS = 1).
Note that stopping regular or injected conversions (setting ADSTP = 1 or JADSTP = 1)
has no influence on the generation of ADCy_AWDx_OUT.
Note: AWDx flag is set by hardware and reset by software: AWDx flag has no influence on the
generation of ADCy_AWDx_OUT (ex: ADCy_AWDx_OUT can toggle while AWDx flag
remains at 1 if the software did not clear the flag).
[Figure 126](../figures/figure_126.md). ADCy_AWDx_OUT signal generation (on all regular channels)
[Table 174](../tables/table_174.md). Analog watchdog 2 and 3 comparison
Resolution
(bits RES[1:0])
Analog watchdog comparison between:
CommentsRaw converted data,
left aligned(1) Thresholds
00: 12-bit DATA[11:4] LTx[7:0] and HTx[7:0] DATA [3:0] are not relevant for the comparison
01: 10-bit DATA[11:4] LTx[7:0] and HTx[7:0] DATA [3:2] are not relevant for the comparison
10: 8-bit DATA[11:4] LTx[7:0] and HTx[7:0] -
11: 6-bit DATA[11:6],00 LTx[7:0] and HTx[7:0] User  must configure LTx[1:0] and HTx[1:0] to 00
1. Refer to Section : Gain compensation for additional details on analog watchdog comparison.
EOC FLAG
ADC
STATE RDY
AWDx FLAG
Conversion1
outside
ADCy_AWDx_OUT
inside
cleared
by S/W
- Converting regular channels 1,2,3,4,5,6,7
- Regular channels 1,2,3,4,5,6,7 are all guarded
MS31025V1
Conversion2 Conversion3 Conversion4 Conversion5 Conversion6 Conversion7
outsideinside outside outside inside
cleared
by S/W
cleared
by S/W
cleared
by S/W

Analog-to-digital converters (ADC) RM0440
650/2140 RM0440 Rev 9
[Figure 127](../figures/figure_127.md). ADCy_AWDx_OUT signal generation (AWDx flag not cleared by software)
[Figure 128](../figures/figure_128.md). ADCy_AWDx_OUT signal generation (on a single regular channel)
[Figure 129](../figures/figure_129.md). ADCy_AWDx_OUT signal generation (on all injected channels)
EOC FLAG
ADC
STATE RDY
AWDx FLAG
Conversion1
outside
ADCy_AWDx_OUT
inside
not cleared by S/W
- Converting regular channels 1,2,3,4,5,6,7
- Regular channels 1,2,3,4,5,6,7 are all guarded
MS31026V1
Conversion2 Conversion3 Conversion4 Conversion5 Conversion6 Conversion7
outsideinside outside outside inside
EOC FLAG
ADC
STATE
AWDx FLAG
Conversion1
outside
ADCy_AWDx_OUT
cleared
by S/W
- Converting regular channels 1 and 2
- Only channel 1 is guarded
MS31027V1
Conversion2 Conversion1 Conversion2 Conversion1 Conversion2 Conversion1
inside outside outside
cleared
by S/W
Conversion2
EOS FLAG
JEOS FLAG
ADC
STATE
AWDx FLAG
RDY
outside
ADCy_AWDx_OUT
cleared
by S/W
- Converting the injected channels 1, 2, 3, 4
- All injected channels 1, 2, 3, 4 are guarded
MS31028V1
Conversion1 Conversion2 Conversion3 Conversion4 Conversion Conversion
inside outside outside
cleared
by S/W
Conversion
inside outside inside
cleared
by S/W
cleared
by S/W

RM0440 Rev 9 651/2140
RM0440 Analog-to-digital converters (ADC)
713
Analog watchdog threshold control
LTx[11:0] and HTx[11:0] can be changed when an analog-to-digital conversion is ongoing
(that is between the start of conversion and the end of conversion of the ADC internal state).
If LTx[11:0] and HTx[11:0] are updated during the ADC conversion of the ADC guarded
channel, the watchdog function is masked for this conversion. This masking is removed at
the next start of conversion, resulting in a analog watchdog thresholds to be applied from
the next ADC conversion. The analog watchdog comparison is performed at each end of
conversion. If the current ADC data is out of the new interval, no interrupt and AWDx_OUT
signal are issued. The Interrupt and the AWD generation only happen at the end of the
conversion which started after the threshold update. If AWD_xOUT is already asserted,
programming the new thresholds does not deassert the AWDx_OUT signal.
Analog watchdog with gain and offset compensation
When gain and offset compensation are enabled, the analog watchdog compares the
threshold after the compensated data.
Note: When the offset compensation is enabled (OFFSETy_EN set in ADC_OFRy register), data
overflow or underflow can result in a wrong watchdog result. When the saturation is enabled
(SATEN set in ADC_OFRy), the watchdog provides a correct result. However this prevents
from using the signed data format.
21.4.29 Oversampler
The oversampling unit performs data pre-processing to offload the CPU. It is able to handle
multiple conversions and average them into a single data with increased data width, up to
16-bit.
It provides a result with the following form, where N and M can be adjusted:
It allows to perform by hardware the following functions: averaging, data rate reduction,
SNR improvement, basic filtering.
The oversampling ratio N is defined using the OVFS[2:0] bits in the ADC_CFGR2 register,
and can range from 2x to 256x. The division coefficient M consists of a right bit shift up to
8 bits, and is defined using the OVSS[3:0] bits in the ADC_CFGR2 register.
The summation unit can yield a result up to 20 bits (256x 12-bit results), which is first shifted
right. It is then truncated to the 16 least significant bits, rounded to the nearest value using
the least significant bits left apart by the shifting, before being finally transferred into the
ADC_DR data register.
Note: If the intermediary result af ter the shifting exceeds 16-bit, the result is truncated as is,
without saturation.
Result 1
M----- Conversion t n()
n0=
nN 1 –=
∑×=

Analog-to-digital converters (ADC) RM0440
652/2140 RM0440 Rev 9
[Figure 130](../figures/figure_130.md). 20-bit to 16-bit result truncation
[Figure 131](../figures/figure_131.md) gives a numerical example of the processing, from a raw 20-bit accumulated
data to the final 16-bit result.
[Figure 131](../figures/figure_131.md). Numerical example with 5-bit shift and rounding
[Table 175](../tables/table_175.md) gives the data format for the various N and M combinations, for a raw conversion
data equal to 0xFFF.
There are no changes for conversion timings in oversampled mode: the sample time is
maintained equal during the whole oversampling sequence. A new data is provided every N
MS34453V1
Raw 20-bit data
19 15 11 7 3 0
Shifting
15 0
Truncation and rounding
MS34454V1
7D73Raw 20-bit data
19 15 11 7 3
0
FBD1Final result after 5-bit shift
and rounding to nearest
B
15
[Table 175](../tables/table_175.md). Maximum output results versus N and M (gray cells indicate truncation)
Over
sampling
ratio
Max
Raw data
No-shift
OVSS =
0000
1-bit
shift
OVSS =
0001
2-bit
shift
OVSS =
0010
3-bit
shift
OVSS =
0011
4-bit
shift
OVSS =
0100
5-bit
shift
OVSS =
0101
6-bit
shift
OVSS =
0110
7-bit
shift
OVSS =
0111
8-bit
shift
OVSS =
1000
2x 0x1FFE 0x1FFE 0x0FFF 0x0800 0x0400 0x0200 0x0100 0x0080 0x0040 0x020
4x 0x3FFC 0x3FFC 0x1FFE 0x0FFF 0x0800 0x0400 0x0200 0x0100 0x0080 0x0040
8x 0x7FF8 0x7FF8 0x3FFC 0x1FFE 0x0FFF 0x0800 0x0400 0x0200 0x0100 0x0080
16x 0xFFF0 0xFFF0 0x7FF8 0x3FFC 0x1FFE 0x0FFF 0x0800 0x0400 0x0200 0x0100
32x 0x1FFE0 0xFFE0 0xFFF0 0x7FF8 0x3FFC 0x1FFE 0x0FFF 0x0800 0x0400 0x0200
64x 0x3FFC0 0xFFC0 0xFFE0 0xFFF0 0x7FF8 0x3FFC 0x1FFE 0x0FFF 0x0800 0x0400
128x 0x7FF80 0xFF80 0xFFC0 0xFFE0 0xFFF0 0x7FF8 0x3FFC 0x1FFE 0x0FFF 0x0800
256x 0xFFF00 0xFF00 0xFF80 0xFFC0 0xFFE0 0xFFF0 0x7FF8 0x3FFC 0x1FFE 0x0FFF

RM0440 Rev 9 653/2140
RM0440 Analog-to-digital converters (ADC)
713
conversions, with an equivalent delay equal to N x TCONV = N x (tSMPL + tSAR). The flags are
set as follows:
• The end of the sampling phase (EOSMP) is set after each sampling phase
• The end of conversion (EOC) occurs once every N conversions, when the
oversampled result is available
• The end of sequence (EOS) occurs once the sequence of oversampled data is
completed (i.e. after N x sequence length conversions total)
ADC operating modes supported when oversampling (single ADC mode)
In oversampling mode, most of the ADC operating modes are maintained:
• Single or continuous mode conversions
• ADC conversions start either by software or with triggers
• ADC stop during a conversion (abort)
• Data read via CPU or DMA with overrun detection
• Low-power modes (AUTDLY)
• Programmable resolution: in this case, the reduced conversion values (as per RES[1:0]
bits in ADC_CFGR1 register) are accumulated, truncated, rounded and shifted in the
same way as 12-bit conversions are
Note: The alignment mode is not available when working with oversampled data. The ALIGN bit in
ADC_CFGR1 is ignored and the data are always provided right-aligned.
Offset correction is not supported in oversampling mode. When ROVSE and/or JOVSE bit is
set, the value of the OFFSETy_EN bit in ADC_OFRy register is ignored (considered as
reset).
Analog watchdog
The analog watchdog functionality is maintained, with the following difference:
• The RES[1:0] bits are ignored, comparison is always done using the full 12-bit values
HT[11:0] and LT[11:0]
• the comparison is performed on the most significant 12-bit of the 16-bit oversampled
results ADC_DR[15:4]
Note: Care must be taken when using high shifti ng values, since this reduces the comparison
range. For instance, if the oversampled result is shifted by 4 bits, thus yielding a 12-bit data
right-aligned, the effective analog watchdog comparison can only be performed on 8 bits.
The comparison is done between ADC_DR[11:4] and HT[0:7] / LT[[0:7], and HT[11:8] /
LT[11:8] must be kept reset.
Triggered mode
The averager can also be used for basic filtering purpose. Although not a very powerful filter
(slow roll-off and limited stop band attenuation), it can be used as a notch filter to reject
constant parasitic frequencies (typically coming from the mains or from a switched mode
power supply). For this purpose, a specific discontinuous mode can be enabled with
TROVS bit in ADC_CFGR2, to be able to have an oversampling frequency defined by a
user and independent from the conversion time itself.
[Figure 132](../figures/figure_132.md) below shows how conversions are started in response to triggers during
discontinuous mode.
If the TROVS bit is set, the content of the DISCEN bit is ignored and considered as 1.

Analog-to-digital converters (ADC) RM0440
654/2140 RM0440 Rev 9
[Figure 132](../figures/figure_132.md). Triggered regular oversampling mode (TROVS bit = 1)
Injected and regular sequencer management when oversampling
In oversampling mode, it is possible to have differentiated behavior for injected and regular
sequencers. The oversampling can be enabled for both sequencers with some limitations if
they have to be used simultaneously (this is related to a unique accumulation unit).
Oversampling regular channels only
The regular oversampling mode bit ROVSM defines how the regular oversampling
sequence is resumed if it is interrupted by injected conversion:
• In continued mode, the accumulation restarts from the last valid data (prior to the
conversion abort request due to the injected trigger). This ensures that oversampling is
complete whatever the injection frequency (providing at least one regular conversion
can be complete between triggers);
• In resumed mode, the accumulation restarts from 0 (previous conversion results are
ignored). This mode allows to guarantee that all data used for oversampling were
converted back-to-back within a single timeslot. Care must be taken to have a injection
trigger period above the oversampling period length. If this condition is not respected,
the oversampling cannot be complete and the regular sequencer is blocked.
[Figure 133](../figures/figure_133.md) gives examples for a 4x oversampling ratio.
MS34455V2
Ch(N)3
TriggerCONT=0
DISCEN = 1
TROVS = 0 Ch(N)2Ch(N)1Ch(N)0Ch(N)3
Trigger
Ch(N)2Ch(N)1Ch(N)0
Ch(N)2
Trigger
Ch(N)1
Trigger
Ch(N)0
Trigger
Ch(N)3
Trigger
Ch(N)2
Trigger
Ch(N)1
Trigger
Ch(N)0
TriggerCONT=0
DISCEN = 1
TROVS = 1
EOC flag set
EOC flag set

RM0440 Rev 9 655/2140
RM0440 Analog-to-digital converters (ADC)
713
[Figure 133](../figures/figure_133.md). Regular oversampling modes (4x ratio)
Oversampling Injected channels only
The Injected oversampling mode bit JOVSE enables oversampling solely for conversions in
the injected sequencer.
Oversampling regular and Injected channels
It is possible to have both ROVSE and JOVSE bits set. In this case, the regular
oversampling mode is forced to resumed mode (ROVSM bit ignored), as represented on
[Figure 134](../figures/figure_134.md) below.
[Figure 134](../figures/figure_134.md). Regular and injected oversampling modes used simultaneously
MS34456V1
Ch(O)0
Oversampling
continued
Regular channels Ch(M)3Ch(M)2Ch(M)1Ch(N)3Ch(N)2Ch(N)1Ch(N)0 Ch(M)0
Ch(M)1
Oversampling
stopped
Ch(J) Ch(K)
Trigger
Injected channels
Continued mode: ROVSE = 1, JOVSE = 0, ROVSM = 0, TROVS = X
Ch(M)3
Oversampling
resumed
Regular channels Ch(M)2Ch(M)1Ch(M)0Ch(N)3Ch(N)2Ch(N)1Ch(N)0 Ch(M)0
Ch(M)1
Oversampling
aborted
Ch(J) Ch(K)
Trigger
Injected channels
Resumed mode: ROVSE = 1, JOVSE = 0, ROVSM = 1, TROVS = X
Abort
Abort
JEOC
JEOC
MS34457V2
Oversampling
resumed
Regular channels Ch(M)1Ch(M)0Ch(N)3Ch(N)2Ch(N)1Ch(N)0 Ch(M)0
Ch(M)1
Oversampling
aborted
Ch(J)0 Ch(J)1
Trigger
Injected channels
ROVSE = 1, JOVSE = 1, ROVSM = 1, TROVS = 0
Abort
JEOC
Ch(J)2 Ch(J)3

Analog-to-digital converters (ADC) RM0440
656/2140 RM0440 Rev 9
Triggered regular oversampling with injected conversions
It is possible to have triggered regular mode with injected conversions. In this case, the
injected mode oversampling mode must be disabled, and the ROVSM bit is ignored
(resumed mode is forced). The JOVSE bit must be reset. The behavior is represented on
[Figure 135](../figures/figure_135.md) below.
[Figure 135](../figures/figure_135.md). Triggered regular oversampling with injection
Auto-injected mode
It is possible to oversample auto-injected sequences and have all conversions results stored
in registers to save a DMA resource. This mode is available only with both regular and
injected oversampling active: JAUTO = 1, ROVSE = 1 and JOVSE = 1, other combinations
are not supported. The ROVSM bit is ignored in auto-injected mode. The [Figure 136](../figures/figure_136.md) below
shows how the conversions are sequenced.
[Figure 136](../figures/figure_136.md). Oversampling in auto-injected mode
It is possible to have also the triggered mode enabled, using the TROVS bit. In this case,
the ADC must be configured as following: JAUTO = 1, DISCEN = 0, JDISCEN = 0, ROVSE
= 1, JOVSE = 1 and TROVSE = 1.
Dual ADC modes supported when oversampling
It is possible to have oversampling enabled when working in dual ADC configuration, for the
injected simultaneous mode and regular simultaneous mode. In this case, the two ADCs
must be programmed with the very same settings (including oversampling).
All other dual ADC modes are not supported when either regular or injected oversampling is
enabled (ROVSE = 1 or JOVSE = 1).
MS34458V4
Oversampling
resumed
Regular channels Ch(N)1Ch(N)1Ch(N)0
Ch(N)2
Ch(J) Ch(K)
Trigger
Injected channels
ROVSE = 1, JOVSE = 0, ROVSM = 1, TROVS = 1
Abort
Trigger Trigger Trigger Trigger Trigger
Ch(N)0
Resumed
MS34459V1
Regular channels N0
JAUTO =1, ROVSE = 1, JOVSE = 1, ROVSM = X, TROVS = 0
N1 N2 N3
I0 I1 I2 I3 J0 J1 J2 J3 K0 K1 K2 K3 L0 L1 L2 L3
N0 N1 N2 N3
Injected channels

RM0440 Rev 9 657/2140
RM0440 Analog-to-digital converters (ADC)
713
Combined modes summary
The [Table 176](../tables/table_176.md) below summarizes all combinations, including modes not supported.
21.4.30 Dual ADC modes
Dual ADC modes can be used in devices with two ADCs or more (see [Figure 137](../figures/figure_137.md)).
In dual ADC mode the start of conversion is triggered alternately or simultaneously by the
ADCx master to the ADC slave, depending on the mode selected by the bits DUAL[4:0] in
the ADCx_CCR register.
Four possible modes are implemented:
• Injected simultaneous mode
• Regular simultaneous mode
• Interleaved mode
• Alternate trigger mode
It is also possible to use these modes combined in the following ways:
• Injected simultaneous mode + Regular simultaneous mode
• Regular simultaneous mode + Alternate trigger mode
• Injected simultaneous mode + Interleaved mode
In dual ADC mode (when bits DUAL[4:0] in ADCx_CCR register are not equal to zero), the
bits CONT, AUTDLY, DISCEN, DISCNUM[2:0], JDISCEN, JQM, JAUTO of the ADC_CFGR
register are shared between the master and slave ADC: the bits in the slave ADC are
always equal to the corresponding bits of the master ADC.
To start a conversion in dual mode, the user must program the bits EXTEN[1:0], EXTSEL,
JEXTEN[1:0], JEXTSEL of the master ADC only, to configure a software or hardware
trigger, and a regular or injected trigger. (the bits EXTEN[1:0] and JEXTEN[1:0] of the slave
ADC are don’t care).
[Table 176](../tables/table_176.md). Oversampler operating modes summary
Regular
Oversampling
ROVSE
Injected
Oversampling
JOVSE
Oversampler
mode
ROVSM
0 = continued
1 = resumed
Triggered
Regular mode
TROVS
Comment
1 0 0 0 Regular continued mode
1 0 0 1 Not supported
1 0 1 0 Regular resumed mode
1011 Triggered regular resumed
mode
1 1 0 X Not supported
1110 Injected and regular resumed
mode
1 1 1 1 Not supported
0 1 X X Injected oversampling

Analog-to-digital converters (ADC) RM0440
658/2140 RM0440 Rev 9
In regular simultaneous or interleaved modes: once the user sets bit ADSTART or bit
ADSTP of the master ADC, the corresponding bit of the slave ADC is also automatically
set. However, bit ADSTART or bit ADSTP of the slave ADC is not necessary cleared at the
same time as the master ADC bit.
In injected simultaneous or alternate trigger modes: once the user sets bit JADSTART or bit
JADSTP of the master ADC, the corresponding bit of the slave ADC is also automatically
set. However, bit JADSTART or bit JADSTP of the slave ADC is not necessary cleared at
the same time as the master ADC bit.
In dual ADC mode, the converted data of the master and slave ADC can be read in parallel,
by reading the ADC common data register (ADCx_CDR). The status bits can be also read in
parallel by reading the dual-mode status register (ADCx_CSR).

RM0440 Rev 9 659/2140
RM0440 Analog-to-digital converters (ADC)
713
[Figure 137](../figures/figure_137.md). Dual ADC block diagram(1)
1. External triggers also exist on slave ADC but are not shown for the purposes of this diagram.
2. The ADC common data register (ADCx_CDR) contains both the master and slave ADC regular converted data.
MSv36025V2
Regular data register (16-
bits)
Injected data registers (4
x16-bits)
Injected
channels
Regular
channels
Regular data register (16-
bits)
Injected data registers (4
x16-bits)
Injected
channels
Regular
channels
Address/data bus
ADCx_INN2
ADCx_INP2
Dual mode
control
Master ADC
Slave ADC
Start trigger mux.
(regular group)
Start trigger mux.
(injected group)
Internal analog inputs
Internal triggers
Internal analog inputs
ADCx_INN1
ADCx_INP1
ADCx_INN16
ADCx_INP16

Analog-to-digital converters (ADC) RM0440
660/2140 RM0440 Rev 9
Injected simultaneous mode
This mode is selected by programming bits DUAL[4:0] = 00101
This mode converts an injected group of channels. The external trigger source comes from
the injected group multiplexer of the master ADC (selected by the JEXTSEL bits in the
ADC_JSQR register).
Note: Do not convert the same channel on the two ADCs (no overlapping sampling times for the
two ADCs when converting the same channel).
In simultaneous mode, one must convert sequences with the same length or ensure that the
interval between triggers is longer than the longer of the 2 sequences. Otherwise, the ADC
with the shortest sequence may restart while the ADC with the longest sequence is
completing the previous conversions.
Regular conversions can be performed on one or all ADCs. In that case, they are
independent of each other and are interrupted when an injected event occurs. They are
resumed at the end of the injected conversion group.
• At the end of injected sequence of conversion event (JEOS) on the master ADC, the
converted data is stored into the master ADC_JDRy registers and a JEOS interrupt is
generated (if enabled)
• At the end of injected sequence of conversion event (JEOS) on the slave ADC, the
converted data is stored into the slave ADC_JDRy registers and a JEOS interrupt is
generated (if enabled)
• If the duration of the master injected sequence is equal to the duration of the slave
injected one (like in [Figure 138](../figures/figure_138.md)), it is possible for the software to enable only one of the
two JEOS interrupt (ex: master JEOS) and read both converted data (from master
ADC_JDRy and slave ADC_JDRy registers).
[Figure 138](../figures/figure_138.md). Injected simultaneous mode on 4 channels: dual ADC mode
If JDISCEN = 1, each simultaneous conversion of the injected sequence requires an
injected trigger event to occur.
This mode can be combined with AUTDLY mode:
• Once a simultaneous injected sequence of conversions has ended, a new injected
trigger event is accepted only if both JEOS bits of the master and the slave ADC have
been cleared (delay phase). Any new injected trigger events occurring during the
ongoing injected sequence and the associated delay phase are ignored.
• Once a regular sequence of conversions of the master ADC has ended, a new regular
trigger event of the master ADC is accepted only if the master data register (ADC_DR)
has been read. Any new regular trigger events occurring for the master ADC during the
MS31900V1
MASTER ADC
SLAVE ADC
End of  injected sequence on
MASTER and SLAVE ADC
Trigger
CH1
CH15 CH14 CH13 CH12
CH2 CH3 CH4
Sampling
Conversion

RM0440 Rev 9 661/2140
RM0440 Analog-to-digital converters (ADC)
713
ongoing regular sequence and the associated delay phases are ignored.
There is the same behavior for regular sequences occurring on the slave ADC.
Regular simultaneous mode with independent injected
This mode is selected by programming bits DUAL[4:0] = 00110.
This mode is performed on a regular group of channels. The external trigger source comes
from the regular group multiplexer of the master ADC (selected by the EXTSEL bits in the
ADC_CFGR register). A simultaneous trigger is provided to the slave ADC.
In this mode, independent injected conversions are supported. An injection request (either
on master or on the slave) aborts the current simultaneous conversions, which are restarted
once the injected conversion is completed.
Note: Do not convert the same channel on the two ADCs (no overlapping sampling times for the
two ADCs when converting the same channel).
In regular simultaneous mode, one must convert sequences with the same length or ensure
that the interval between triggers is longer than the longer conversion time of the 2
sequences. Otherwise, the ADC with the shortest sequence may restart while the ADC with
the longest sequence is completing the previous conversions.
Software is notified by interrupts when it can read the data:
• At the end of each conversion event (EOC) on the master ADC, a master EOC interrupt
is generated (if EOCIE is enabled) and software can read the ADC_DR of the master
ADC.
• At the end of each conversion event (EOC) on the slave ADC, a slave EOC interrupt is
generated (if EOCIE is enabled) and software can read the ADC_DR of the slave ADC.
• If the duration of the master regular sequence is equal to the duration of the slave one
(like in [Figure 139](../figures/figure_139.md)), it is possible for the software to enable only one of the two EOC
interrupt (ex: master EOC) and read both converted data from the Common Data
register (ADCx_CDR).
It is also possible to read the regular data using the DMA. Two methods are possible:
• Using two DMA channels (one for the master and one for the slave). In this case bits
MDMA[1:0] must be kept cleared.
– Configure the DMA master ADC channel to read ADC_DR from the master. DMA
requests are generated at each EOC event of the master ADC.
– Configure the DMA slave ADC channel to read ADC_DR from the slave. DMA
requests are generated at each EOC event of the slave ADC.
• Using MDMA mode, which leaves one DMA channel free for other uses:
– Configure MDMA[1:0] = 10 or 11 (depending on resolution).
– A single DMA channel is used (the one of  the master). Configure the DMA master
ADC channel to read the common ADC register (ADCx_CDR)
– A single DMA request is generated each time both master and slave EOC events
have occurred. At that time, the slave ADC converted data is available in the
upper half-word of the ADCx_CDR 32-bit register and the master ADC converted
data is available in the lower half-word of ADCx_CDR register.
– Both EOC flags are cleared when the DMA reads the ADCx_CDR register.
Note: In MDMA mode (MDMA[1:0] = 10 or 11), the user must program the same number of
conversions in the master’s sequence as in the slave’s sequence. Otherwise, the remaining
conversions does not generate a DMA request.

Analog-to-digital converters (ADC) RM0440
662/2140 RM0440 Rev 9
[Figure 139](../figures/figure_139.md). Regular simultaneous mode on 16 channels: dual ADC mode
If DISCEN = 1 then each “n” simultaneous conversions of the regular sequence require a
regular trigger event to occur (“n” is defined by DISCNUM).
This mode can be combined with AUTDLY mode:
• Once a simultaneous conversion of the sequence has ended, the next conversion in
the sequence is started only if the common data register, ADCx_CDR (or the regular
data register of the master ADC) has been read (delay phase).
• Once a simultaneous regular sequence of conversions has ended, a new regular
trigger event is accepted only if the common data register (ADCx_CDR) has been read
(delay phase). Any new regular trigger events occurring during the ongoing regular
sequence and the associated delay phases are ignored.
It is possible to use the DMA to handle data in regular simultaneous mode combined with
AUTDLY mode, assuming that multiple-DMA mode is used: bits MDMA must be set to 10 or
11.
When regular simultaneous mode is combined with AUTDLY mode, it is mandatory for the
user to ensure that:
• The number of conversions in the master’s sequence is equal to the number of
conversions in the slave’s.
• For each simultaneous conversions of the sequence, the length of the conversion of
the slave ADC is inferior to the length of the conversion of the master ADC. Note that
the length of the sequence depends on the number of channels to convert and the
sampling time and the resolution of each channels.
Note: This combination of regular simultaneous m ode and AUTDLY mode is restricted to the use
case when only regular channels are programmed: it is forbidden to program injected
channels in this combined mode.
Interleaved mode with independent injected
This mode is selected by programming bits DUAL[4:0] = 00111.
This mode can be started only on a regular group (usually one channel). The external
trigger source comes from the regular channel multiplexer of the master ADC.
After an external trigger occurs:
• The master ADC starts immediately.
• The slave ADC starts after a delay of several ADC clock cycles after the sampling
phase of the master ADC has complete.
The minimum delay which separates two conversions in interleaved mode is configured in
the DELAY bits in the ADCx_CCR register. This delay starts counting one half cycle after the
end of the sampling phase of the master conversion. This way, an ADC cannot start a
ai16054b
End of  regular sequence on
MASTER and SLAVE ADC
MASTER ADC
SLAVE ADC
CH16
CH1
...
...
Sampling
Conversion
Trigger
CH1
CH16 CH14 CH13 CH12
CH2 CH3 CH4

RM0440 Rev 9 663/2140
RM0440 Analog-to-digital converters (ADC)
713
conversion if the complementary ADC is still sampling its input (only one ADC can sample
the input signal at a given time).
• The minimum possible DELAY is 1 to ensure that there is at least one cycle time
between the opening of the analog switch of the master ADC sampling phase and the
closing of the analog switch of the slave ADC sampling phase.
• The maximum DELAY is equal to the number of cycles corresponding to the selected
resolution. However the user must properly calculate this delay to ensure that an ADC
does not start a conversion while the other ADC is still sampling its input.
If the CONT bit is set on both master and slave ADCs, the selected regular channels of both
ADCs are continuously converted.
The software is notified by interrupts when it can read the data at the end of each
conversion event (EOC) on the slave ADC. A slave and master EOC interrupts are
generated (if EOCIE is enabled) and the software can read the ADC_DR of the slave/master
ADC.
Note: It is possible to enable only the EOC in terrupt of the slave and read the common data
register (ADCx_CDR). But in this case, the user must ensure that the duration of the
conversions are compatible to ensure that inside the sequence, a master conversion is
always followed by a slave conversion before a new master conversion restarts. It is
recommended to use the MDMA mode.
It is also possible to have the regular data transferred by DMA. In this case, individual DMA
requests on each ADC cannot be used and it is mandatory to use the MDMA mode, as
following:
• Configure MDMA[1:0] = 10 or 11 (depending on resolution).
• A single DMA channel is used (the one of the master). Configure the DMA master ADC
channel to read the common ADC register (ADCx_CDR).
• A single DMA request is generated each time both master and slave EOC events have
occurred. At that time, the slave ADC converted data is available in the upper half-word
of the ADCx_CDR 32-bit register and the master ADC converted data is available in the
lower half-word of ADCx_CCR register.
• Both EOC flags are cleared when the DMA reads the ADCx_CCR register.
[Figure 140](../figures/figure_140.md). Interleaved mode on 1 channel in continuous conversion mode: dual ADC
mode
MSv31030V5
MASTER ADC
Trigger
Sampling
Conversion
4 ADCCLK
cycles
4 ADCCLK
cycles
SLAVE ADC
End of conversion on master and
slave ADC
0.5 ADCCLK
cycle
0.5 ADCCLK
cycle
CH1 CH1
CH1 CH1

Analog-to-digital converters (ADC) RM0440
664/2140 RM0440 Rev 9
[Figure 141](../figures/figure_141.md). Interleaved mode on 1 channel in single conversion mode: dual ADC
mode
If DISCEN = 1, each “n” simultaneous conversions (“n” is defined by DISCNUM) of the
regular sequence require a regular trigger event to occur.
In this mode, injected conversions are supported. When injection is done (either on master
or on slave), both the master and the slave regular conversions are aborted and the
sequence is restarted from the master (see [Figure 142](../figures/figure_142.md) below).
[Figure 142](../figures/figure_142.md). Interleaved conversion with injection
Alternate trigger mode
This mode is selected by programming bits DUAL[4:0] = 01001.
This mode can be started only on an injected group. The source of external trigger comes
from the injected group multiplexer of the master ADC.
This mode is only possible when selecting hardware triggers: JEXTEN[1:0] must not be 00.
Injected discontinuous mode disabled (JDISCEN = 0 for both ADC)
MSv31031V3
MASTER ADC
Trigger
CH1
Sampling
Conversion
CH1
4 ADCCLK
cycles
CH1
CH1
4 ADCCLK
cycles
SLAVE ADC
End of conversion on
master and slave ADC
End of conversion on
master and slave ADC
0.5 ADCCLK
cycle
0.5 ADCCLK
cycle
MS34460V1
ADC1 (master) CH1 CH1 CH1
CH11
CH1 CH1 CH1
CH2 CH2 CH0CH2 CH2 CH2ADC2 (slave)
Injected trigger Resume (always on master)
read
CDR
read
CDR
read
CDR
read
CDR
conversions
abortedLegend:
Sampling Conversion

RM0440 Rev 9 665/2140
RM0440 Analog-to-digital converters (ADC)
713
1. When the first trigger occurs, all inject ed master ADC channels in the group are
converted.
2. When the second trigger occurs, all injected slave ADC channels in the group are
converted.
3. And so on.
A JEOS interrupt, if enabled, is generated after all injected channels of the master ADC in
the group have been converted.
A JEOS interrupt, if enabled, is generated after all injected channels of the slave ADC in the
group have been converted.
JEOC interrupts, if enabled, can also be generated after each injected conversion.
If another external trigger occurs after all injected channels in the group have been
converted then the alternate trigger process restarts by converting the injected channels of
the master ADC in the group.
[Figure 143](../figures/figure_143.md). Alternate trigger: injected group of each ADC
Note: Regular conversions can be enabled on one or all ADCs. In this case the regular
conversions are independent of each other. A regular conversion is interrupted when the
ADC has to perform an injected conversion. It is resumed when the injected conversion is
finished.
The time interval between 2 trigger events must be greater than or equal to 1 ADC clock
period. The minimum time interval between 2 trigger events that start conversions on the
same ADC is the same as in the single ADC mode.
Injected discontinuous mode enabled (JDISCEN = 1 for both ADC)
ai16059-m
MASTER ADC
SLAVE ADC
JEOC on
master ADC
JEOC on
slave ADC
JEOC,JEOS on
master ADC
JEOC on
master ADC
JEOC on
slave ADC
JEOC, JEOS
on slave ADC
1st trigger
2nd trigger
MASTER ADC
SLAVE ADC
JEOC on
master ADC
JEOC on
slave ADC
JEOC,JEOS on
master ADC
JEOC on
master ADC
JEOC on
slave ADC
JEOC, JEOS
on slave ADC
3rd trigger
4th trigger
Sampling
Conversion

Analog-to-digital converters (ADC) RM0440
666/2140 RM0440 Rev 9
If the injected discontinuous mode is enabled for both master and slave ADCs:
• When the first trigger occurs, the first injected channel of the master ADC is converted.
• When the second trigger occurs, the first injected channel of the slave ADC is
converted.
• And so on.
A JEOS interrupt, if enabled, is generated after all injected channels of the master ADC in
the group have been converted.
A JEOS interrupt, if enabled, is generated after all injected channels of the slave ADC in the
group have been converted.
JEOC interrupts, if enabled, can also be generated after each injected conversions.
If another external trigger occurs after all injected channels in the group have been
converted then the alternate trigger process restarts.
[Figure 144](../figures/figure_144.md). Alternate trigger: 4 injected channels (each ADC) in discontinuous mode
Combined regular/injected simultaneous mode
This mode is selected by programming bits DUAL[4:0] = 00001.
It is possible to interrupt the simultaneous conversion of a regular group to start the
simultaneous conversion of an injected group.
Note: In combined regular/injected simultaneous  mode, one must convert sequences with the
same length or ensure that the interval between triggers is longer than the long conversion
time of the 2 sequences. Otherwise, the ADC with the shortest sequence may restart while
the ADC with the longest sequence is completing the previous conversions.
Combined regular simultaneous + alternate trigger mode
This mode is selected by programming bits DUAL[4:0] = 00010.
It is possible to interrupt the simultaneous conversion of a regular group to start the alternate
trigger conversion of an injected group. [Figure 145](../figures/figure_145.md) shows the behavior of an alternate
trigger interrupting a simultaneous regular conversion.
The injected alternate conversion is immediately started after the injected event. If a regular
conversion is already running, in order to ensure synchronization after the injected
conversion, the regular conversion of all (master/slave) ADCs is stopped and resumed
synchronously at the end of the injected conversion.
ai16060V3
Sampling
Conversion
MASTER ADC
SLAVE ADC
1st trigger
2nd trigger
3rd trigger
4th trigger
5th trigger
6th trigger
7th trigger
8th trigger
JEOC, JEOS on
master ADC
JEOC on
master ADC
JEOC, JEOS on
slave ADC
JEOC on
master ADC
JEOC on
master ADC
JEOC on slave
ADC
JEOC on slave
ADC
JEOC on slave
ADC

RM0440 Rev 9 667/2140
RM0440 Analog-to-digital converters (ADC)
713
Note: In combined regular simultaneous + alternate trigger mode, one must convert sequences
with the same length or ensure that the interval between triggers is longer than the long
conversion time of the 2 sequences. Otherwise, the ADC with the shortest sequence may
restart while the ADC with the longest sequence is completing the previous conversions.
[Figure 145](../figures/figure_145.md). Alternate + regular simultaneous
If a trigger occurs during an injected conversion that has interrupted a regular conversion,
the alternate trigger is served. [Figure 146](../figures/figure_146.md) shows the behavior in this case (note that the 6th
trigger is ignored because the associated alternate conversion is not complete).
[Figure 146](../figures/figure_146.md). Case of trigger occurring during injected conversion
Combined injected simultaneous plus interleaved
This mode is selected by programming bits DUAL[4:0] = 00011
It is possible to interrupt an interleaved conversion with a simultaneous injected event.
In this case the interleaved conversion is interrupted immediately and the simultaneous
injected conversion starts. At the end of the injected sequence the interleaved conversion is
resumed. When the interleaved regular conversion resumes, the first regular conversion
which is performed is alway the master’s one. [Figure 147](../figures/figure_147.md), [Figure 148](../figures/figure_148.md) and [Figure 149](../figures/figure_149.md) show
the behavior using an example.
Caution: In this mode, it is mandatory to use the Common Data Register to read the regular data with
a single read access. On the contrary, master-slave data coherency is not guaranteed.
ADC MASTER reg CH1 CH2 CH3
CH1
CH3 CH4
CH1
ADC MASTER inj
ADC SLAVE reg
ADC SLAVE  inj
1st trigger
2nd trigger
synchronization not lost
CH4 CH6 CH7 CH7 CH8
CH4 CH5
CH8 CH9
ai16062V2-m
ai16063V2
ADC MASTER reg
CH14ADC MASTER inj
ADC SLAVE reg
ADC SLAVE inj
1st trigger
2nd trigger
CH5
CH10
CH14
4th trigger
3rd trigger
CH15
CH14
5th trigger
CH15
6th trigger
(ignored)
CH5
CH11
CH6
CH12
CH2 CH3 CH4
CH8 CH9 CH10
CH4
CH11
CH1
CH7 CH9
CH3

Analog-to-digital converters (ADC) RM0440
668/2140 RM0440 Rev 9
[Figure 147](../figures/figure_147.md). Interleaved single channel CH0 with injected sequence CH11, CH12
[Figure 148](../figures/figure_148.md). Two Interleaved channels (CH1, CH2) with injected sequence CH11, CH12
- case 1: Master interrupted first
[Figure 149](../figures/figure_149.md). Two Interleaved channels (CH1, CH2) with injected sequence CH11, CH12
- case 2: Slave interrupted first
MS34461V1
Legend:
Sampling Conversion
ADC1 (master) CH0 CH0 CH0
CH11
CH0 CH0 CH0
CH0 CH0 CH0CH0 CH0 CH0ADC2 (slave)
read
CDR
read
CDR
read
CDR
read
CDR
CH11
CH12 CH12
Injected trigger Resume
(always restart with the master)
Conversions
aborted
MS34462V1
Legend:
Sampling Conversion
ADC1 (master) CH1 CH1 CH1
CH11
CH1 CH1 CH1
CH2 CH2 CH2CH2 CH2 CH2ADC2 (slave)
read
CDR
read
CDR
read
CDR
read
CDR
CH11
CH12 CH12
Injected trigger Resume
(always restart with the master)
Conversions
aborted
MS34463V2
Legend:
Sampling Conversion
ADC1 (master) CH1 CH1 CH1
CH11
CH1 CH1 CH1
CH2 CH2 CH2CH2 CH2 CH2ADC2 (slave)
read
CDR
read
CDR
read
CDR
read
CDR
CH11
CH12 CH12
Injected trigger Resume
(always restart with the master)
Conversions
aborted

RM0440 Rev 9 669/2140
RM0440 Analog-to-digital converters (ADC)
713
DMA requests in dual ADC mode
In all dual ADC modes, it is possible to use two DMA channels (one for the master, one for
the slave) to transfer the data, like in single mode (refer to [Figure 150](../figures/figure_150.md): DMA Requests in
regular simultaneous mode when MDMA = 00).
[Figure 150](../figures/figure_150.md). DMA Requests in regular simultaneous mode when MDMA = 00
In simultaneous regular and interleaved modes, it is also possible to save one DMA channel
and transfer both data using a single DMA channel. For this MDMA bits must be configured
in the ADCx_CCR register:
• MDMA = 10: A single DMA request is generated each time both master and slave EOC
events have occurred. At that time, two data items are available and the 32-bit register
ADCx_CDR contains the two half-words representing two ADC-converted data items.
The slave ADC data take the upper half-word and the master ADC data take the lower
half-word.
This mode is used in interleaved mode and in regular simultaneous mode when
resolution is 10-bit or 12-bit.
Example:
Interleaved dual mode: a DMA request is generated each time 2 data items are
available:
first DMA request: ADCx_CDR[31:0] = SLV_ADC_DR[15:0] | MST_ADC_DR[15:0]
second DMA request: ADCx_CDR[31:0] = SLV_ADC_DR[15:0] |
MST_ADC_DR[15:0]
MSv31032V2
CH1ADC Master regular
CH2
Trigger Trigger
CH2
CH1
Configuration where each sequence contains only one conversion
ADC Master EOC
ADC Slave regular
ADC Slave EOC
DMA request from ADC Master
DMA request from ADC Slave
DMA reads Master
ADC_DR
DMA reads Mater
ADC_DR
DMA reads Slave
ADC_DR
DMA reads Slave
ADC_DR

Analog-to-digital converters (ADC) RM0440
670/2140 RM0440 Rev 9
[Figure 151](../figures/figure_151.md). DMA requests in regular simultaneous mode when MDMA = 10
[Figure 152](../figures/figure_152.md). DMA requests in interleaved mode when MDMA = 10
MSv31033V3
ADC Master regular
ADC Master EOC
CH1
Trigger
CH1
Trigger
CH2 CH2
Configuration where each sequence contains only one conversion
ADC Slave regular
ADC Slave EOC
DMA request from
ADC Master
DMA request from
ADC Slave
CH2
Trigger
CH2
Trigger
CH1 CH1
MSv31034V2
ADC Master regular
ADC Master EOC
CH1
Trigger
CH1
Trigger
CH2
Configuration where each sequence contains only one conversion
ADC Slave regular
ADC Slave EOC
DMA request from
ADC Master
DMA request from
ADC Slave
Trigger Trigger
CH1 CH1CH1
Trigger
Delay
CH2
Delay Delay
CH2 CH2
Delay
CH2
Delay

RM0440 Rev 9 671/2140
RM0440 Analog-to-digital converters (ADC)
713
Note: When using MDMA mode, the user must take care to configure properly the duration of the
master and slave conversions so that a DMA request is generated and served for reading
both data (master + slave) before a new conversion is available.
• MDMA = 11: This mode is similar to the MDMA = 10. The only differences are that on
each DMA request (two data items are available), two bytes representing two ADC
converted data items are transferred as a half-word.
This mode is used in interleaved and regular simultaneous mode when resolution is 6-
bit or when resolution is 8-bit and data is not signed (offsets must be disabled for all the
involved channels).
Example:
Interleaved dual mode: a DMA request is generated each time 2 data items are
available:
first DMA request: ADCx_CDR[15:0] = SLV_ADC_DR[7:0] | MST_ADC_DR[7:0]
second DMA request: ADCx_CDR[15:0] = SLV_ADC_DR[7:0] |
MST_ADC_DR[7:0]
Overrun detection
In dual ADC mode (when DUAL[4:0] is not equal to 00000), if an overrun is detected on one
of the ADCs, the DMA requests are no longer issued to ensure that all the data transferred
to the RAM are valid (this behavior occurs whatever the MDMA configuration). It may
happen that the EOC bit corresponding to one ADC remains set because the data register
of this ADC contains valid data.
DMA one shot mode/ DMA circular mode when MDMA mode is selected
When MDMA mode is selected (10 or 11), bit DMACFG of the ADCx_CCR register must
also be configured to select between DMA one shot mode and circular mode, as explained
in section Section : Managing conversions using the DMA (bits DMACFG of master and
slave ADC_CFGR are not relevant).
Stopping the conversions in dual ADC modes
The user must set the control bits ADSTP/JADSTP of the master ADC to stop the
conversions of both ADC in dual ADC mode. The other ADSTP control bit of the slave ADC
has no effect in dual ADC mode.
Once both ADC are effectively stopped, the bits ADSTART/JADSTART of the master and
slave ADCs are both cleared by hardware.
21.4.31 Temperature sensor
The temperature sensor can be used to measure the junction temperature (Tj) of the device.
The temperature sensor is internally connected to the ADC input channels which are used
to convert the sensor output voltage to a digital value. When not in use, the sensor can be
put in power down mode. It support the temperature range –40 to 125 °C.
[Figure 153](../figures/figure_153.md) shows the block diagram of connections between the temperature sensor and
the ADC.
The temperature sensor output voltage changes linearly with temperature. The offset of this
line varies from chip to chip due to process variation (up to 45 °C from one chip to another).

Analog-to-digital converters (ADC) RM0440
672/2140 RM0440 Rev 9
The uncalibrated internal temperature sensor is more suited for applications that detect
temperature variations instead of absolute temperatures. To improve the accuracy of the
temperature sensor measurement, calibration values are stored in system memory for each
device by ST during production.
During the manufacturing process, the calibration data of the temperature sensor and the
internal voltage reference are stored in the system memory area. The user application can
then read them and use them to improve the accuracy of the temperature sensor or the
internal reference (refer to the datasheet for additional information).
The temperature sensor is internally connected to the ADC input channel which is used to
convert the sensor’s output voltage to a digital value. Refer to the electrical characteristics
section of the device datasheet for the sampling time value to be applied when converting
the internal temperature sensor.
When not in use, the sensor can be put in power-down mode.
[Figure 153](../figures/figure_153.md) shows the block diagram of the temperature sensor.
[Figure 153](../figures/figure_153.md). Temperature sensor channel block diagram
Reading the temperature
To use the sensor:
1. Select the ADC input channel s that is connected to VTS.
2. Program with the appropriate sampling time (r efer to electrical characteristics section of
the device datasheet).
3. Set the VSENSESEL bit in the ADCx_CCR register to wake up the temperature sensor
from power-down mode.
4. Start the ADC conversion.
5. Read the resulting V TS data in the ADC data register.
6. Calculate the actual temperature using the following formula:
MSv46150V2
VTS
VSENSESEL
control bit
ADCx
ADC input
Address/data busTemperature
sensor
Converted
data
Temperature in °C() TS_CAL2_TEMP TS_CAL1_TEMP–
TS_CAL2 TS_CAL1–-------------------------------------------------------------------------------------------------- TS_DATA TS_CAL1–() TS_CAL1_TEMP+×=

RM0440 Rev 9 673/2140
RM0440 Analog-to-digital converters (ADC)
713
Where:
• TS_CAL2 is the temperature sensor calibration value acquired at TS_CAL2_TEMP.
• TS_CAL1 is the temperature sensor calibration value acquired at TS_CAL1_TEMP.
• TS_DATA is the actual temperature sensor output value converted by ADC.
Refer to the device datasheet for more information about TS_CAL1 and TS_CAL2
calibration points.
Note: The sensor has a startup time after waking from power-down mode before it can output VTS
at the correct level. The ADC also has a startup time after power-on, so to minimize the
delay, the ADEN and VSENSESEL bits should be set at the same time.
The above formula is given for TS_DATA measurement done with the same VREF+voltage
as TS_CAL1/TS_CAL2 values. If VREF+ is different, the formula must be adapted. For
example if VREF+ = 3.3 V and TS_CAL data are acquired at VREF+= 3.0 V, TS_DATA must
be replaced by TS_DATA x (3.3/3.0).
21.4.32 V BAT supply monitoring
The VBATSEL bit in the ADCx_CCR register is used to switch to the battery voltage. As the
VBAT voltage could be higher than VDDA, to ensure the correct operation of the ADC, the
VBAT pin is internally connected to a bridge divider by 3. This bridge is automatically enabled
when VBATSEL is set, to connect VBAT/3 to the ADC input channels. As a consequence, the
converted digital value is one third of the VBAT voltage. To prevent any unwanted
consumption on the battery, it is recommended to enable the bridge divider only when
needed, for ADC conversion.
Refer to the electrical characteristics of the device datasheet for the sampling time value to
be applied when converting the VBAT/3 voltage.
The figure below shows the block diagram of the VBAT sensing feature.
[Figure 154](../figures/figure_154.md). VBAT channel block diagram
1. The VBATSEL bit must be set to enable the conversion of internal channel for V BAT/3.
MSv46151V1
VBAT
VBAT/3
VBATSEL
ADCx
ADC input
Address/data bus

Analog-to-digital converters (ADC) RM0440
674/2140 RM0440 Rev 9
21.4.33 Monitoring the inte rnal voltage reference
It is possible to monitor the internal voltage reference (VREFINT) to have a reference point for
evaluating the ADC VREF+ voltage level.
The internal reference voltage (VREFINT) is internally connected to ADC1_INP18,
ADC3_INP18, ADC4_INP18 and ADC5_INP18.
Refer to the electrical characteristics section of the product datasheet for the sampling time
value to be applied when converting the internal voltage reference voltage.
[Figure 155](../figures/figure_155.md) shows the block diagram of the VREFINT sensing feature.
[Figure 155](../figures/figure_155.md). VREFINT channel block diagram
1. The VREFEN bit into ADCx_CCR register must be set to enable the conversion of internal channels
(VREFINT).
Calculating the actual VREF+ voltage using the internal reference voltage
The power supply voltage applied to the device may be subject to variations or not precisely
known. When VDDA is connected to VREF+, it is possible to compute the actual VDDA voltage
using the embedded internal reference voltage (VREFINT). VREFINT and its calibration data,
acquired by the ADC during the manufacturing process at VDDA_Charac, can be used to
evaluate the actual VDDA voltage level.
The following formula gives the actual VREF+ voltage supplying the device:
Where:
• VREF+_Charac is the value of VREF+ voltage characterized at VREFINT during the
manufacturing process. It is specified in the device datasheet.
• VREFINT_CAL is the VREFINT calibration value
• VREFINT_DATA is the actual VREFINT output value converted by ADC
Converting a supply-relative ADC measurement to an absolute voltage value
The ADC is designed to deliver a digital value corresponding to the ratio between VREF+ and
the voltage applied on the converted channel.
For most applications VDDA value is unknown and ADC converted values are right-aligned.
In this case, it is necessary to convert this ratio into a voltage independent from VDDA:
MSv34467V5
VREFINT
ADCx
ADC input
VREFEN control bit
Internal
power block
VREF+ VREF+_Charac VREFINT_CAL VREFINT_DATA⁄×=

RM0440 Rev 9 675/2140
RM0440 Analog-to-digital converters (ADC)
713
By replacing VREF+ by the formula provided above, the absolute voltage value is given by
the following formula
For applications where VREF+ is known and ADC converted values are right-aligned, the
absolute voltage value can be obtained by using the following formula:
Where:
–V REF+_Charac is the value of VREF+ voltage characterized at VREFINT during the
manufacturing process.
– VREFINT_CAL is the V REFINT calibration value
– ADC_DATA is the value measured by the ADC on channel x (right-aligned)
– VREFINT_DATA is the actual V REFINT output value converted by the ADC
– FULL_SCALE is the maximum digital valu e of the ADC output. For example with
12-bit resolution, it is 212 - 1 = 4095 or with 8-bit resolution, 28 - 1 = 255.
Note: If ADC measurements are done using an output format other than 16-bit right-aligned, all
the parameters must first be converted to a compatible format before the calculation is
done.
21.5 ADC in low-power mode
VCHANNELx
VREF+
FULL_SCALE-------------------------------------ADC_DATA×=
VCHANNELx
VREF+_Charac VREFINT_CAL ADC_DATA××
VREFINT_DATA FULL_SCALE×-------------------------------------------------------------------------------------------------------------------------=
VCHANNELx
VREF+
FULL_SCALE-------------------------------------ADC_DATA×=
[Table 177](../tables/table_177.md). Effect of low-power modes on the ADC
Mode Description
Sleep No effect.
DMA requests are functional.
Low-power run No effect.
Low-power sleep No effect.
DMA requests are functional.
Stop 0/Stop 1
The ADC is not operational. Its state is kept.
The ADC consumes the static current recommended to disable the
peripheral in advance in order to reduce power consumption.
Standby The ADC is powered down and must be reinitialized after exiting Standby or
Shutdown mode.Shutdown

Analog-to-digital converters (ADC) RM0440
676/2140 RM0440 Rev 9
21.6 ADC interrupts
For each ADC, an interrupt can be generated:
• After ADC power-up, when the ADC is ready (flag ADRDY)
• On the end of any conversion for regular groups (flag EOC)
• On the end of a sequence of conversion for regular groups (flag EOS)
• On the end of any conversion for injected groups (flag JEOC)
• On the end of a sequence of conversion for injected groups (flag JEOS)
• When an analog watchdog detection occurs (flag AWD1, AWD2 and AWD3)
• When the end of sampling phase occurs (flag EOSMP)
• When the data overrun occurs (flag OVR)
• When the injected sequence context queue overflows (flag JQOVF)
Separate interrupt enable bits are available for flexibility.
[Table 178](../tables/table_178.md). ADC interrupts per each ADC
Interrupt event Event flag Enable control bit
ADC ready ADRDY ADRDYIE
End of conversion of a regular group EOC EOCIE
End of sequence of conversions of a regular group EOS EOSIE
End of conversion of a injected group JEOC JEOCIE
End of sequence of conversions of an injected group JEOS JEOSIE
Analog watchdog 1 status bit is set AWD1 AWD1IE
Analog watchdog 2 status bit is set AWD2 AWD2IE
Analog watchdog 3 status bit is set AWD3 AWD3IE
End of sampling phase EOSMP EOSMPIE
Overrun OVR OVRIE
Injected context queue overflows JQOVF JQOVFIE

RM0440 Rev 9 677/2140
RM0440 Analog-to-digital converters (ADC)
713
21.7 ADC registers (for each ADC)
Refer to Section 1.2 on page 74 for a list of abbreviations used in register descriptions.
21.7.1 ADC interrupt and st atus register (ADC_ISR)
Address offset: 0x00
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9 8 76543210
Res. Res. Res. Res. Res. JQOVF AWD3 AWD2 AWD1 JEOS JEOC OVR EOS EOC EOSMP ADRDY
rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1
Bits 31:11 Reserved, must  be kept at reset value.
Bit 10 JQOVF: Injected context queue overflow
This bit is set by hardware when an Overflow of the Injected Queue of Context occurs. It is cleared
by software writing 1 to it. Refer to Section 21.4.21: Queue of context for injected conversions for
more information.
0: No injected context queue overflow occurred (or the flag event was already acknowledged and
cleared by software)
1: Injected context queue overflow has occurred
Bit 9 AWD3: Analog watchdog 3 flag
This bit is set by hardware when the converted voltage crosses the values programmed in the fields
LT3[7:0] and HT3[7:0] of ADC_TR3 register. It is cleared by software writing 1 to it.
0: No analog watchdog 3 event occurred (or the flag event was already acknowledged and cleared
by software)
1: Analog watchdog 3 event occurred
Bit 8 AWD2: Analog watchdog 2 flag
This bit is set by hardware when the converted voltage crosses the values programmed in the fields
LT2[7:0] and HT2[7:0] of ADC_TR2 register. It is cleared by software writing 1 to it.
0: No analog watchdog 2 event occurred (or the flag event was already acknowledged and cleared
by software)
1: Analog watchdog 2 event occurred
Bit 7 AWD1: Analog watchdog 1 flag
This bit is set by hardware when the converted voltage crosses the values programmed in the fields
LT1[11:0] and HT1[11:0] of ADC_TR1 register. It is cleared by software. writing 1 to it.
0: No analog watchdog 1 event occurred (or the flag event was already acknowledged and cleared
by software)
1: Analog watchdog 1 event occurred
Bit 6 JEOS: Injected channel end of sequence flag
This bit is set by hardware at the end of the conversions of all injected channels in the group. It is
cleared by software writing 1 to it.
0: Injected conversion sequence not complete (or the flag event was already acknowledged and
cleared by software)
1: Injected conversions complete

Analog-to-digital converters (ADC) RM0440
678/2140 RM0440 Rev 9
Bit 5 JEOC: Injected channel end of conversion flag
This bit is set by hardware at the end of each injected conversion of a channel when a new data is
available in the corresponding ADC_JDRy register. It is cleared by software writing 1 to it or by
reading the corresponding ADC_JDRy register
0: Injected channel conversion not complete (or the flag event was already acknowledged and
cleared by software)
1: Injected channel conversion complete
Bit 4 OVR: ADC overrun
This bit is set by hardware when an overrun occurs on a regular channel, meaning that a new
conversion has completed while the EOC flag was already set. It is cleared by software writing 1 to
it.
0: No overrun occurred (or the flag event was already acknowledged and cleared by software)
1: Overrun has occurred
Bit 3 EOS: End of regular sequence flag
This bit is set by hardware at the end of the conversions of a regular sequence of channels. It is
cleared by software writing 1 to it.
0: Regular Conversions sequence not complete (or the flag event was already acknowledged and
cleared by software)
1: Regular Conversions sequence complete
Bit 2 EOC: End of conversion flag
This bit is set by hardware at the end of each regular conversion of a channel when a new data is
available in the ADC_DR register. It is cleared by software writing 1 to it or by reading the ADC_DR
register
0: Regular channel conversion not complete (or the flag event was already acknowledged and
cleared by software)
1: Regular channel conversion complete
Bit 1 EOSMP: End of sampling flag
This bit is set by hardware during the conversion of any channel (only for regular channels), at the
end of the sampling phase.
0: not at the end of the sampling phase (or the flag event was already acknowledged and cleared by
software)
1: End of sampling phase reached
Bit 0 ADRDY: ADC ready
This bit is set by hardware after the ADC has been enabled (bit ADEN = 1) and when the ADC
reaches a state where it is ready to accept conversion requests.
It is cleared by software writing 1 to it.
0: ADC not yet ready to start conversion (or the flag event was already acknowledged and cleared
by software)
1: ADC is ready to start conversion

RM0440 Rev 9 679/2140
RM0440 Analog-to-digital converters (ADC)
713
21.7.2 ADC interrupt enable register (ADC_IER)
Address offset: 0x04
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. JQOVF
IE AWD3IE AWD2IE AWD1IE JEOSIE JEOCIE OVRIE EOSIE EOCIE EOSMP
IE
ADRDY
IE
rw rw rw rw rw rw rw rw rw rw rw
Bits 31:11 Reserved, must  be kept at reset value.
Bit 10 JQOVFIE: Injected context queue overflow interrupt enable
This bit is set and cleared by software to enable/disable the Injected Context Queue Overflow
interrupt.
0: Injected Context Queue Overflow interrupt disabled
1: Injected Context Queue Overflow interrupt enabled. An interrupt is generated when the JQOVF bit
is set.
Note: The software is allowed to write this bi t only when JADSTART = 0 (which ensures that no
injected conversion is ongoing).
Bit 9 AWD3IE: Analog watchdog 3 interrupt enable
This bit is set and cleared by software to enable/disable the analog watchdog 2 interrupt.
0: Analog watchdog 3 interrupt disabled
1: Analog watchdog 3 interrupt enabled
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
Bit 8 AWD2IE: Analog watchdog 2 interrupt enable
This bit is set and cleared by software to enable/disable the analog watchdog 2 interrupt.
0: Analog watchdog 2 interrupt disabled
1: Analog watchdog 2 interrupt enabled
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
Bit 7 AWD1IE: Analog watchdog 1 interrupt enable
This bit is set and cleared by software to enable/disable the analog watchdog 1 interrupt.
0: Analog watchdog 1 interrupt disabled
1: Analog watchdog 1 interrupt enabled
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
Bit 6 JEOSIE: End of injected sequence of conversions interrupt enable
This bit is set and cleared by software to enable/disable the end of injected sequence of conversions
interrupt.
0: JEOS interrupt disabled
1: JEOS interrupt enabled. An interrupt is generated when the JEOS bit is set.
Note: The software is allowed to write this bi t only when JADSTART = 0 (which ensures that no
injected conversion is ongoing).

Analog-to-digital converters (ADC) RM0440
680/2140 RM0440 Rev 9
Bit 5 JEOCIE: End of injected conversion interrupt enable
This bit is set and cleared by software to enable/disable the end of an injected conversion interrupt.
0: JEOC interrupt disabled.
1: JEOC interrupt enabled. An interrupt is generated when the JEOC bit is set.
Note: The software is allowed to write this bi t only when JADSTART = 0 (which ensures that no
injected conversion is ongoing).
Bit 4 OVRIE: Overrun interrupt enable
This bit is set and cleared by software to enable/disable the Overrun interrupt of a regular
conversion.
0: Overrun interrupt disabled
1: Overrun interrupt enabled. An interrupt is generated when the OVR bit is set.
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no regular
conversion is ongoing).
Bit 3 EOSIE: End of regular sequence of conversions interrupt enable
This bit is set and cleared by software to enable/disable the end of regular sequence of conversions
interrupt.
0: EOS interrupt disabled
1: EOS interrupt enabled. An interrupt is generated when the EOS bit is set.
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no regular
conversion is ongoing).
Bit 2 EOCIE: End of regular conversion interrupt enable
This bit is set and cleared by software to enable/disable the end of a regular conversion interrupt.
0: EOC interrupt disabled.
1: EOC interrupt enabled. An interrupt is generated when the EOC bit is set.
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no regular
conversion is ongoing).
Bit 1 EOSMPIE: End of sampling flag interrupt enable for regular conversions
This bit is set and cleared by software to enable/disable the end of the sampling phase interrupt for
regular conversions.
0: EOSMP interrupt disabled.
1: EOSMP interrupt enabled. An interrupt is generated when the EOSMP bit is set.
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no regular
conversion is ongoing).
Bit 0 ADRDYIE: ADC ready interrupt enable
This bit is set and cleared by software to enable/disable the ADC Ready interrupt.
0: ADRDY interrupt disabled
1: ADRDY interrupt enabled. An interrupt is generated when the ADRDY bit is set.
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).

RM0440 Rev 9 681/2140
RM0440 Analog-to-digital converters (ADC)
713
21.7.3 ADC control register (ADC_CR)
Address offset: 0x08
Reset value: 0x2000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ADCA
L
ADCA
LDIF
DEEP
PWD
ADVREG
EN Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
rs rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. JADST
P ADSTP JADST
ART
ADSTA
RT ADDIS ADEN
rs rs rs rs rs rs
Bit 31 ADCAL: ADC calibration
This bit is set by software to start the calibration of the ADC. Program first the bit ADCALDIF
to determine if this calibration applies for single-ended or differential inputs mode.
It is cleared by hardware after calibration is complete.
0: Calibration complete
1: Write 1 to calibrate the ADC. Read at 1 means that a calibration in progress.
Note: The software is allowed to launch a calibration by setting ADCAL only when ADEN = 0.
The software is allowed to update the calibration factor by writing ADC_CALFACT only
when ADEN = 1 and ADSTART = 0 and JADSTART = 0 (ADC enabled and no
conversion is ongoing)
Bit 30 ADCALDIF: Differential mode for calibration
This bit is set and cleared by software to configure the single-ended or differential inputs
mode for the calibration.
0: Writing ADCAL launches a calibration in single-ended inputs mode.
1: Writing ADCAL launches a calibration in differential inputs mode.
Note: The software is allowed to write this bit only when the ADC is disabled and is not
calibrating (ADCAL = 0, JADSTART = 0, JADSTP = 0, ADSTART = 0, ADSTP = 0,
ADDIS = 0 and ADEN = 0).
Bit 29 DEEPPWD: Deep-power-down enable
This bit is set and cleared by software to put the ADC in Deep-power-down mode.
0: ADC not in Deep-power down
1: ADC in Deep-power-down (default reset state)
Note: The software is allowed to write this bit only when the ADC is disabled (ADCAL = 0,
JADSTART = 0, JADSTP = 0, ADSTART = 0, ADSTP = 0, ADDIS = 0 and ADEN = 0).
Bit 28 ADVREGEN: ADC voltage regulator enable
This bits is set by software to enable the ADC voltage regulator.
Before performing any operation such as launching a calibration or enabling the ADC, the
ADC voltage regulator must first be enabled and the software must wait for the regulator
start-up time.
0: ADC Voltage regulator disabled
1: ADC Voltage regulator enabled.
For more details about the ADC voltage regulator enable and disable sequences, refer to
Section 21.4.6: ADC Deep-power-down mode (DEEPPWD) and ADC voltage regulator
(ADVREGEN).
The software can program this bit field only when the ADC is disabled (ADCAL =0 ,
JADSTART =0 , ADSTART=0 , ADSTP =0 , ADDIS =0  and ADEN =0 ).

Analog-to-digital converters (ADC) RM0440
682/2140 RM0440 Rev 9
Bits 27:6 Reserved, must be kept at reset value.
Bit 5 JADSTP: ADC stop of injected conversion command
This bit is set by software to stop and discard an ongoing injected conversion (JADSTP
Command).
It is cleared by hardware when the conversion is effectively discarded and the ADC injected
sequence and triggers can be re-configured. The ADC is then ready to accept a new start of
injected conversions (JADSTART command).
0: No ADC stop injected conversion command ongoing
1: Write 1 to stop injected conversions ongoing. Read 1 means that an ADSTP command is
in progress.
Note: The software is allowed to set JADSTP only when JADSTART = 1 and ADDIS = 0 (ADC
is enabled and eventually converting an injected conversion and there is no pending
request to disable the ADC)
In Auto-injection mode (JAUTO = 1), setting ADSTP bit aborts both regular and injected
conversions (do not use JADSTP)
Bit 4 ADSTP: ADC stop of regular conversion command
This bit is set by software to stop and discard an ongoing regular conversion (ADSTP
Command).
It is cleared by hardware when the conversion is effectively discarded and the ADC regular
sequence and triggers can be re-configured. The ADC is then ready to accept a new start of
regular conversions (ADSTART command).
0: No ADC stop regular conversion command ongoing
1: Write 1 to stop regular conversions ongoing. Read 1 means that an ADSTP command is in
progress.
Note: The software is allowed to set ADSTP only when ADSTART = 1 and ADDIS = 0 (ADC is
enabled and eventually converting a regular conversion and there is no pending request
to disable the ADC).
In auto-injection mode (JAUTO = 1), setting ADSTP bit aborts both regular and injected
conversions (do not use JADSTP).
In dual ADC regular simultaneous mode and interleaved mode, the bit ADSTP of the
master ADC must be used to stop regular conversions. The other ADSTP bit is inactive.
Bit 3 JADSTART: ADC start of injected conversion
This bit is set by software to start ADC conversion of injected channels. Depending on the
configuration bits JEXTEN[1:0], a conversion starts immediately (software trigger
configuration) or once an injected hardware trigger event occurs (hardware trigger
configuration).
It is cleared by hardware:
– in single conversion mode when software trigger is selected (JEXTSEL =0 x0): at the
assertion of the End of Injected Conversion Sequence (JEOS) flag.
– in all cases: after the execution of the JADSTP command, at the same time that JADSTP is
cleared by hardware.
0: No ADC injected conversion is ongoing.
1: Write 1 to start injected conversions. Read 1 means that the ADC is operating and
eventually converting an injected channel.
Note: The software is allowed to set JADSTART only when ADEN = 1 and ADDIS = 0 (ADC is
enabled and there is no pending request to disable the ADC).
In auto-injection mode (JAUTO = 1), regular and auto-injected conversions are started
by setting bit ADSTART (JADSTART must be kept cleared)

RM0440 Rev 9 683/2140
RM0440 Analog-to-digital converters (ADC)
713
Bit 2 ADSTART: ADC start of regular conversion
This bit is set by software to start ADC conversion of regular channels. Depending on the
configuration bits EXTEN[1:0], a conversion starts immediately (software trigger
configuration) or once a regular hardware trigger event occurs (hardware trigger
configuration).
It is cleared by hardware:
– in single conversion mode when software trigger is selected (EXTSEL =0 x0): at the
assertion of the End of Regular Conversion Sequence (EOS) flag.
– in all cases: after the execution of the ADSTP command, at the same time that ADSTP is
cleared by hardware.
0: No ADC regular conversion is ongoing.
1: Write 1 to start regular conversions. Read 1 means that the ADC is operating and
eventually converting a regular channel.
Note: The software is allowed to set ADSTART only when ADEN = 1 and ADDIS = 0 (ADC is
enabled and there is no pending request to disable the ADC)
In auto-injection mode (JAUTO = 1), regular and auto-injected conversions are started
by setting bit ADSTART (JADSTART must be kept cleared)
Bit 1 ADDIS: ADC disable command
This bit is set by software to disable the ADC (ADDIS command) and put it into power-down
state (OFF state).
It is cleared by hardware once the ADC is effectively disabled (ADEN is also cleared by
hardware at this time).
0: no ADDIS command ongoing
1: Write 1 to disable the ADC. Read 1 means that an ADDIS command is in progress.
Note: The software is allowed to set ADDIS only when ADEN = 1 and both ADSTART = 0 and
JADSTART = 0 (which ensures that no conversion is ongoing)
Bit 0 ADEN: ADC enable control
This bit is set by software to enable the ADC. The ADC is effectively ready to operate once
the flag ADRDY has been set.
It is cleared by hardware when the ADC is disabled, after the execution of the ADDIS
command.
0: ADC is disabled (OFF state)
1: Write 1 to enable the ADC.
Note: The software is allowed to set ADEN only when all bits of ADC_CR registers are 0
(ADCAL = 0, JADSTART = 0, ADSTART = 0, ADSTP = 0, ADDIS = 0 and ADEN = 0)
except for bit ADVREGEN which must be 1 (and the software must have wait for the
startup time of the voltage regulator)

Analog-to-digital converters (ADC) RM0440
684/2140 RM0440 Rev 9
21.7.4 ADC configurati on register (ADC_CFGR)
Address offset: 0x0C
Reset value: 0x8000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
JQDIS AWD1CH[4:0] JAUTO JAWD1
EN
AWD1
EN
AWD1S
GL JQM JDISC
EN DISCNUM[2:0] DISC
EN
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ALIGN AUT
DLY CONT OVR
MOD EXTEN[1:0] EXTSEL[4:0] RES[1:0] Res. DMA
CFG
DMA
EN
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 31 JQDIS: Injected Queue disable
These bits are set and cleared by software to disable the Injected Queue mechanism :
0: Injected Queue enabled
1: Injected Queue disabled
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0 (which
ensures that no regular nor injected conversion is ongoing).
A set or reset of JQDIS bit causes the injected queue to be flushed and the ADC_JSQR register
is cleared.
Bits 30:26 AWD1CH[4:0]: Analog watchdog 1 channel selection
These bits are set and cleared by software. They select the input channel to be guarded by the
analog watchdog.
00000: ADC analog input channel 0 monitored by AWD1
00001: ADC analog input channel 1 monitored by AWD1
.....
10010: ADC analog input channel 18 monitored by AWD1
others: reserved, must not be used
Note: Some channels are not connected physically. Keep the corresponding AWD1CH[4:0] setting to
the reset value.
The channel selected by AWD1CH must be also selected into the SQi or JSQi bits.
The software is allowed to write these bits only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
Bit 25 JAUTO: Automatic injected group conversion
This bit is set and cleared by software to enable/disable automatic injected group conversion after
regular group conversion.
0: Automatic injected group conversion disabled
1: Automatic injected group conversion enabled
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0 (which
ensures that no regular nor injected conversion is ongoing).
When dual mode is enabled (DUAL bits in ADCx_CCR register are not equal to zero), the bit
JAUTO of the slave ADC is no more writable and its content is equal to the bit JAUTO of the
master ADC.

RM0440 Rev 9 685/2140
RM0440 Analog-to-digital converters (ADC)
713
Bit 24 JAWD1EN: Analog watchdog 1 enable on injected channels
This bit is set and cleared by software
0: Analog watchdog 1 disabled on injected channels
1: Analog watchdog 1 enabled on injected channels
Note: The software is allowed to write this bi t only when JADSTART = 0 (which ensures that no
injected conversion is ongoing).
Bit 23 AWD1EN: Analog watchdog 1 enable on regular channels
This bit is set and cleared by software
0: Analog watchdog 1 disabled on regular channels
1: Analog watchdog 1 enabled on regular channels
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no regular
conversion is ongoing).
Bit 22 AWD1SGL: Enable the watchdog 1 on a single channel or on all channels
This bit is set and cleared by software to enable the analog watchdog on the channel identified by
the AWD1CH[4:0] bits or on all the channels
0: Analog watchdog 1 enabled on all channels
1: Analog watchdog 1 enabled on a single channel
Note: The software is allowed to write these bi ts only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
Bit 21 JQM: ADC_JSQR queue mode
This bit is set and cleared by software.
It defines how an empty Queue is managed.
0: ADC_JSQR mode 0: The Queue is never empty and maintains the last written configuration into
ADC_JSQR.
1: ADC_JSQR mode 1: The Queue can be empty and when this occurs, the software and hardware
triggers of the injected sequence are both internally disabled just after the completion of the last valid
injected sequence.
Refer to Section 21.4.21: Queue of context for injected conversions for more information.
Note: The software is allowed to write this bi t only when JADSTART = 0 (which ensures that no
injected conversion is ongoing).
When dual mode is enabled (DUAL bits in ADCx_CCR register are not equal to zero), the bit
JQM of the slave ADC is no more writable and its content is equal to the bit JQM of the master
ADC.
Bit 20 JDISCEN: Discontinuous mode on injected channels
This bit is set and cleared by software to enable/disable discontinuous mode on the injected
channels of a group.
0: Discontinuous mode on injected channels disabled
1: Discontinuous mode on injected channels enabled
Note: The software is allowed to write this bi t only when JADSTART = 0 (which ensures that no
injected conversion is ongoing).
It is not possible to use both auto-injected mode and discontinuous mode simultaneously: the
bits DISCEN and JDISCEN must be kept cleared by software when JAUTO is set.
When dual mode is enabled (bits DUAL of ADCx_CCR register are not equal to zero), the bit
JDISCEN of the slave ADC is no more writable and its content is equal to the bit JDISCEN of
the master ADC.

Analog-to-digital converters (ADC) RM0440
686/2140 RM0440 Rev 9
Bits 19:17 DISCNUM[2:0]: Discontinuous mode channel count
These bits are written by software to define the number of regular channels to be converted in
discontinuous mode, after receiving an external trigger.
000: 1 channel
001: 2 channels
...
111: 8 channels
Note: The software is allowed to write these bi ts only when ADSTART = 0 (which ensures that no
regular conversion is ongoing).
When dual mode is enabled (DUAL bits in ADCx_CCR register are not equal to zero), the bits
DISCNUM[2:0] of the slave ADC are no more writable and their content is equal to the bits
DISCNUM[2:0] of the master ADC.
Bit 16 DISCEN: Discontinuous mode for regular channels
This bit is set and cleared by software to enable/disable Discontinuous mode for regular channels.
0: Discontinuous mode for regular channels disabled
1: Discontinuous mode for regular channels enabled
Note: It is not possible to have both discontinuous mode and continuous mode enabled: it is forbidden
to set both DISCEN = 1 and CONT = 1.
It is not possible to use both auto-injected mode and discontinuous mode simultaneously: the
bits DISCEN and JDISCEN must be kept cleared by software when JAUTO is set.
The software is allowed to write this bit only when ADSTART = 0 (which ensures that no regular
conversion is ongoing).
When dual mode is enabled (DUAL bits in ADCx_CCR register are not equal to zero), the bit
DISCEN of the slave ADC is no more writable and its content is equal to the bit DISCEN of the
master ADC.
Bit 15 ALIGN: Data alignment
This bit is set and cleared by software to select right or left alignment. Refer to Data register, data
alignment and offset (ADC_DR, OFFSETy, OFFSETy_CH, ALIGN).
0: Right alignment
1: Left alignment
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
Bit 14 AUTDLY: Delayed conversion mode
This bit is set and cleared by software to enable/disable the Auto Delayed Conversion mode.
0: Auto-delayed conversion mode off
1: Auto-delayed conversion mode on
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
When dual mode is enabled (DUAL bits in ADCx_CCR register are not equal to zero), the bit
AUTDLY of the slave ADC is no more writable and its content is equal to the bit AUTDLY of the
master ADC.

RM0440 Rev 9 687/2140
RM0440 Analog-to-digital converters (ADC)
713
Bit 13 CONT: Single / continuous conversion mode for regular conversions
This bit is set and cleared by software. If it is set, regular conversion takes place continuously until it
is cleared.
0: Single conversion mode
1: Continuous conversion mode
Note: It is not possible to have both discontinuous mode and continuous mode enabled: it is forbidden
to set both DISCEN = 1 and CONT = 1.
The software is allowed to write this bit only when ADSTART = 0 (which ensures that no regular
conversion is ongoing).
When dual mode is enabled (DUAL bits in ADCx_CCR register are not equal to zero), the bit
CONT of the slave ADC is no more writable and its content is equal to the bit CONT of the
master ADC.
Bit 12 OVRMOD: Overrun mode
This bit is set and cleared by software and configure the way data overrun is managed.
0: ADC_DR register is preserved with the old data when an overrun is detected.
1: ADC_DR register is overwritten with the last conversion result when an overrun is detected.
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no regular
conversion is ongoing).
Bits 11:10 EXTEN[1:0]: External trigger enable and polarity selection for regular channels
These bits are set and cleared by software to select the external trigger polarity and enable the
trigger of a regular group.
00: Hardware trigger detection disabled (conversions can be launched by software)
01: Hardware trigger detection on the rising edge
10: Hardware trigger detection on the falling edge
11: Hardware trigger detection on both the rising and falling edges
Note: The software is allowed to write these bi ts only when ADSTART = 0 (which ensures that no
regular conversion is ongoing).
Bits 9:5 EXTSEL[4:0]: External trigger selection for regular group
These bits select the external event used to trigger the start of conversion of a regular group:
00000: Event 0
00001: Event 1
00010: Event 2
00011: Event 3
00100: Event 4
00101: Event 5
00110: Event 6
00111: Event 7
...
11111: Event 31
Note: The software is allowed to write these bi ts only when ADSTART = 0 (which ensures that no
regular conversion is ongoing).
Bits 4:3 RES[1:0]: Data resolution
These bits are written by software to select the resolution of the conversion.
00: 12-bit
01: 10-bit
10: 8-bit
11: 6-bit
Note: The software is allowed to write these bi ts only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).

Analog-to-digital converters (ADC) RM0440
688/2140 RM0440 Rev 9
21.7.5 ADC configuration register 2 (ADC_CFGR2)
Address offset: 0x10
Reset value: 0x0000 0000
Bit 2 Reserved, must be kept at reset value.
Bit 1 DMACFG: Direct memory access configuration
This bit is set and cleared by software to select between two DMA modes of operation. It is effective
only when DMAEN = 1 (single ADC mode), or MDMA[1:0] ≠ 00 (dual ADC mode).
0: DMA One Shot mode selected
1: DMA Circular mode selected
For more details, refer to Section : Managing conversions using the DMA
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
In dual-ADC modes, this bit is not relevant and replaced by control bit DMACFG of the
ADCx_CCR register.
Bit 0 DMAEN: Direct memory access enable
This bit is set and cleared by software to enable the generation of DMA requests. This allows to use
the DMA to manage automatically the converted data. For more details, refer to Section : Managing
conversions using the DMA.
0: DMA disabled
1: DMA enabled
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
In dual-ADC modes, this bit is not relevant and replaced by control bits MDMA[1:0] of the
ADCx_CCR register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. SMPTRI
G BULB SWTRI
G Res. Res. Res. Res. Res. Res. Res. Res. GCOM
P
rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. ROV
SM TROVS OVSS[3:0] OVSR[2:0] JOVSE ROVSE
rw rw rw rw rw rw rw rw rw rw rw

RM0440 Rev 9 689/2140
RM0440 Analog-to-digital converters (ADC)
713
Bits 31:28 Reserved, must be kept at reset value.
Bit 27 SMPTRIG: Sampling time control trigger mode
This bit is set and cleared by software to enable the sampling time control trigger mode.
0: Sampling time control trigger mode disabled
1: Sampling time control trigger mode enabled
The sampling time starts on the trigger rising edge, and the conversion on the trigger falling edge.
EXTEN[1:0] bits should be set to 01. BULB bit must not be set when the SMPTRIG bit is set.
When EXTEN[1:0] bits are set to 00, set SWTRIG to start the sampling and clear SWTRIG bit to start
the conversion.
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no
conversion is ongoing).
Bit 26 BULB: Bulb sampling mode
This bit is set and cleared by software to enable the bulb sampling mode.
0: Bulb sampling mode disabled
1: Bulb sampling mode enabled. The sampling period starts just after the previous end of
conversion.
SAMPTRIG bit must not be set when the BULB bit is set.
The very first ADC conversion is performed with the sampling time specified in SMPx bits.
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no
conversion is ongoing).
Bit 25 SWTRIG: Software trigger bit for sampling time control trigger mode
This bit is set and cleared by software to enable the bulb sampling mode.
0: Software trigger starts the conversion for sampling time control trigger mode
1: Software trigger starts the sampling for sampling time control trigger mode
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no
conversion is ongoing).
Bits 24:17 Reserved, must be kept at reset value.
Bit 16 GCOMP: Gain compensation mode
This bit is set and cleared by software to enable the gain compensation mode.
0: Regular ADC operating mode
1: Gain compensation enabled and applied on all channels
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no
conversion is ongoing).
Bits 15:11 Reserved, must  be kept at reset value.
Bit 10 ROVSM: Regular Oversampling mode
This bit is set and cleared by software to select the regular oversampling mode.
0: Continued mode: When injected conversions are triggered, the oversampling is temporary
stopped and continued after the injection sequence (oversampling buffer is maintained during
injected sequence)
1: Resumed mode: When injected conversions are triggered, the current oversampling is aborted
and resumed from start after the injection sequence (oversampling buffer is zeroed by injected
sequence start)
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no
conversion is ongoing).

Analog-to-digital converters (ADC) RM0440
690/2140 RM0440 Rev 9
Bit 9 TROVS: Triggered Regular Oversampling
This bit is set and cleared by software to enable triggered oversampling
0: All oversampled conversions for a channel are done consecutively following a trigger
1: Each oversampled conversion for a channel needs a new trigger
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no
conversion is ongoing).
Bits 8:5 OVSS[3:0]: Oversampling shift
This bitfield is set and cleared by software to define the right shifting applied to the raw oversampling
result.
0000: No shift
0001: Shift 1-bit
0010: Shift 2-bits
0011: Shift 3-bits
0100: Shift 4-bits
0101: Shift 5-bits
0110: Shift 6-bits
0111: Shift 7-bits
1000: Shift 8-bits
Other codes reserved
Note: The software is allowed to write these bi ts only when ADSTART = 0 (which ensures that no
conversion is ongoing).
Bits 4:2 OVSR[2:0]: Oversampling ratio
This bitfield is set and cleared by software to define the oversampling ratio.
000: 2x
001: 4x
010: 8x
011: 16x
100: 32x
101: 64x
110: 128x
111: 256x
Note: The software is allowed to write these bi ts only when ADSTART = 0 (which ensures that no
conversion is ongoing).
Bit 1 JOVSE: Injected Oversampling Enable
This bit is set and cleared by software to enable injected oversampling.
0: Injected Oversampling disabled
1: Injected Oversampling enabled
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing)
Bit 0 ROVSE: Regular Oversampling Enable
This bit is set and cleared by software to enable regular oversampling.
0: Regular Oversampling disabled
1: Regular Oversampling enabled
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing)

RM0440 Rev 9 691/2140
RM0440 Analog-to-digital converters (ADC)
713
21.7.6 ADC sample time register 1 (ADC_SMPR1)
Address offset: 0x14
Reset value: 0x0000 0000
21.7.7 ADC sample time register 2 (ADC_SMPR2)
Address offset: 0x18
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
SMPPL
US Res. SMP9[2:0] SMP8[2:0] SMP7[2:0] SMP6[2:0] SMP5[2:1]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
SMP5[
0] SMP4[2:0] SMP3[2:0] SMP2[2:0] SMP1[2:0] SMP0[2:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 31 SMPPLUS: Addition of one clock cycle to the sampling time
1: 2.5 ADC clock cycle sampling time becomes 3.5 ADC clock cycles for the ADC_SMPR1
and ADC_SMPR2 registers.
0: The sampling time remains set to 2.5 ADC clock cycles remains
To make sure no conversion is ongoing, the software is allowed to write this bit only when
ADSTART= 0 and JADSTART= 0.
Bit 30 Reserved, must be  kept at reset value.
Bits 29:0 SMPx[2:0]: Channel x sampling time selection (x = 9 to 0)
These bits are written by software to select the sampling time individually for each channel.
During sample cycles, the channel selection bits must remain unchanged.
000: 2.5 ADC clock cycles
001: 6.5 ADC clock cycles
010: 12.5 ADC clock cycles
011: 24.5 ADC clock cycles
100: 47.5 ADC clock cycles
101: 92.5 ADC clock cycles
110: 247.5 ADC clock cycles
111: 640.5 ADC clock cycles
Note: The software is allowed to write these bits only when ADSTART = 0 and
JADSTART = 0 (which ensures that no conversion is ongoing).
Some channels are not connected physically. Keep the corresponding SMPx[2:0]
setting to the reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. SMP18[2:0] SMP17[2:0] SMP16[2:0] SMP15[2:1]
rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
SMP15[0] SMP14[2:0] SMP13[2:0] SMP12[2:0] SMP11[2:0] SMP10[2:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

Analog-to-digital converters (ADC) RM0440
692/2140 RM0440 Rev 9
21.7.8 ADC watchdog threshol d register 1 (ADC_TR1)
Address offset: 0x20
Reset value: 0x0FFF 0000
Bits 31:27 Reserved, must be kept at reset value.
Bits 26:0 SMPx[2:0]: Channel x sampling time selection (x = 18 to 10)
These bits are written by software to select the sampling time individually for each channel.
During sampling cycles, the channel selection bits must remain unchanged.
000: 2.5 ADC clock cycles
001: 6.5 ADC clock cycles
010: 12.5 ADC clock cycles
011: 24.5 ADC clock cycles
100: 47.5 ADC clock cycles
101: 92.5 ADC clock cycles
110: 247.5 ADC clock cycles
111: 640.5 ADC clock cycles
Note: The software is allowed to write these bits only when ADSTART = 0 and
JADSTART = 0 (which ensures that no conversion is ongoing).
Some channels are not connected physically. Keep the corresponding SMPx[2:0]
setting to the reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. HT1[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. AWDFILT[2:0] LT1[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:28 Reserved, must be kept at reset value.
Bits 27:16 HT1[11:0]: Analog watchdog 1 higher threshold
These bits are written by software to define the higher threshold for the analog watchdog 1.
Refer to Section 21.4.28: Analog window watchdog (AWD1EN, JAWD1EN, AWD1SGL, AWD1CH,
AWD2CH, AWD3CH, AWD_HTx, AWD_LTx, AWDx).
Note: The software is allowed to write these bi ts only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).

RM0440 Rev 9 693/2140
RM0440 Analog-to-digital converters (ADC)
713
21.7.9 ADC watchdog threshol d register 2 (ADC_TR2)
Address offset: 0x24
Reset value: 0x00FF 0000
Bit 15 Reserved, must be kept at reset value.
Bits 14:12 AWDFILT: Analog watchdog filtering parameter
This bit is set and cleared by software.
000: No filtering
001: two consecutive detection generates an AWDx flag or an interrupt
...
111: Eight consecutive detection generates an AWDx flag or an interrupt
Note: The software is allowed to write this bit only when ADSTART = 0 (which ensures that no
conversion is ongoing).
Bits 11:0 LT1[11:0]: Analog watchdog 1 lower threshold
These bits are written by software to define the lower threshold for the analog watchdog 1.
Refer to Section 21.4.28: Analog window watchdog (AWD1EN, JAWD1EN, AWD1SGL, AWD1CH,
AWD2CH, AWD3CH, AWD_HTx, AWD_LTx, AWDx)
Note: The software is allowed to write these bi ts only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. HT2[7:0]
rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. LT2[7:0]
rw rw rw rw rw rw rw rw
Bits 31:24 Reserved, must be kept at reset value.
Bits 23:16 HT2[7:0]: Analog watchdog 2 higher threshold
These bits are written by software to define the higher threshold for the analog watchdog 2.
Refer to Section 21.4.28: Analog window watchdog (AWD1EN, JAWD1EN, AWD1SGL, AWD1CH,
AWD2CH, AWD3CH, AWD_HTx, AWD_LTx, AWDx)
Note: The software is allowed to write these bi ts only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
Bits 15:8 Reserved, must be kept at reset value.
Bits 7:0 LT2[7:0]: Analog watchdog 2 lower threshold
These bits are written by software to define the lower threshold for the analog watchdog 2.
Refer to Section 21.4.28: Analog window watchdog (AWD1EN, JAWD1EN, AWD1SGL, AWD1CH,
AWD2CH, AWD3CH, AWD_HTx, AWD_LTx, AWDx)
Note: The software is allowed to write these bi ts only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).

Analog-to-digital converters (ADC) RM0440
694/2140 RM0440 Rev 9
21.7.10 ADC watchdog threshol d register 3 (ADC_TR3)
Address offset: 0x28
Reset value: 0x00FF 0000
21.7.11 ADC regular sequenc e register 1 (ADC_SQR1)
Address offset: 0x30
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. HT3[7:0]
rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. LT3[7:0]
rw rw rw rw rw rw rw rw
Bits 31:24 Reserved, must be kept at reset value.
Bits 23:16 HT3[7:0]: Analog watchdog 3 higher threshold
These bits are written by software to define the higher threshold for the analog watchdog 3.
Refer to Section 21.4.28: Analog window watchdog (AWD1EN, JAWD1EN, AWD1SGL, AWD1CH,
AWD2CH, AWD3CH, AWD_HTx, AWD_LTx, AWDx)
Note: The software is allowed to write these bi ts only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
Bits 15:8 Reserved, must be kept at reset value.
Bits 7:0 LT3[7:0]: Analog watchdog 3 lower threshold
These bits are written by software to define the lower threshold for the analog watchdog 3.
This watchdog compares the 8-bit of LT3 with the 8 MSB of the converted data.
Note: The software is allowed to write these bi ts only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. SQ4[4:0] Res. SQ3[4:0] Res. SQ2[4]
rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
SQ2[3:0] Res. SQ1[4:0] Res. Res. L[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:29 Reserved, must be kept at reset value.
Bits 28:24 SQ4[4:0]: fourth conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the fourth
in the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bit 23 Reserved, must be kept at reset value.

RM0440 Rev 9 695/2140
RM0440 Analog-to-digital converters (ADC)
713
Note: Some channels are not connected physically  and must not be selected for conversion.
21.7.12 ADC regular sequenc e register 2 (ADC_SQR2)
Address offset: 0x34
Reset value: 0x0000 0000
Bits 22:18 SQ3[4:0]: third conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the third in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bit 17 Reserved, must be kept at reset value.
Bits 16:12 SQ2[4:0]: second conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the second
in the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bit 11 Reserved, must be kept at reset value.
Bits 10:6 SQ1[4:0]: first conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the first in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bits 5:4 Reserved, must be kept at reset value.
Bits 3:0 L[3:0]: Regular channel sequence length
These bits are written by software to define the total number of conversions in the regular
channel conversion sequence.
0000: 1 conversion
0001: 2 conversions
...
1111: 16 conversions
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. SQ9[4:0] Res. SQ8[4:0] Res. SQ7[4]
rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
SQ7[3:0] Res. SQ6[4:0] Res. SQ5[4:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw

Analog-to-digital converters (ADC) RM0440
696/2140 RM0440 Rev 9
Note: Some channels are not connected physically  and must not be selected for conversion.
21.7.13 ADC regular sequenc e register 3 (ADC_SQR3)
Address offset: 0x38
Reset value: 0x0000 0000
Bits 31:29 Reserved, must be kept at reset value.
Bits 28:24 SQ9[4:0]: 9th conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the 9th in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bit 23 Reserved, must be kept at reset value.
Bits 22:18 SQ8[4:0]: 8th conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the 8th in
the regular conversion sequence
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bit 17 Reserved, must be kept at reset value.
Bits 16:12 SQ7[4:0]: 7th conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the 7th in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bit 11 Reserved, must be kept at reset value.
Bits 10:6 SQ6[4:0]: 6th conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the 6th in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bit 5 Reserved, must be kept at reset value.
Bits 4:0 SQ5[4:0]: 5th conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the 5th in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. SQ14[4:0] Res. SQ13[4:0] Res. SQ12[4]
rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
SQ12[3:0] Res. SQ11[4:0] Res. SQ10[4:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:29 Reserved, must be kept at reset value.

RM0440 Rev 9 697/2140
RM0440 Analog-to-digital converters (ADC)
713
Note: Some channels are not connected physically  and must not be selected for conversion.
21.7.14 ADC regular sequenc e register 4 (ADC_SQR4)
Address offset: 0x3C
Reset value: 0x0000 0000
Bits 28:24 SQ14[4:0]: 14th conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the 14th in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bit 23 Reserved, must be kept at reset value.
Bits 22:18 SQ13[4:0]: 13th conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the 13th in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bit 17 Reserved, must be kept at reset value.
Bits 16:12 SQ12[4:0]: 12th conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the 12th in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bit 11 Reserved, must be kept at reset value.
Bits 10:6 SQ11[4:0]: 11th conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the 11th in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bit 5 Reserved, must be kept at reset value.
Bits 4:0 SQ10[4:0]: 10th conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the 10th in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. SQ16[4:0] Res. SQ15[4:0]
rw rw rw rw rw rw rw rw rw rw
Bits 31:11 Reserved, must be kept at reset value.

Analog-to-digital converters (ADC) RM0440
698/2140 RM0440 Rev 9
Note: Some channels are not connected physically  and must not be selected for conversion.
21.7.15 ADC regular da ta register (ADC_DR)
Address offset: 0x40
Reset value: 0x0000 0000
21.7.16 ADC injected seque nce register (ADC_JSQR)
Address offset: 0x4C
Reset value: 0x0000 0000
Bits 10:6 SQ16[4:0]: 16th conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the 16th in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
Bit 5 Reserved, must be kept at reset value.
Bits 4:0 SQ15[4:0]: 15th conversion in regular sequence
These bits are written by software with the channel number (0 to 18) assigned as the 15th in
the regular conversion sequence.
Note: The software is allowed to write these bits only when ADSTART = 0 (which ensures
that no regular conversion is ongoing).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
RDATA[15:0]
rrrrrrrrrrrrrrrr
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 RDATA[15:0]: Regular data converted
These bits are read-only. They contain the conversion result from the last converted regular channel.
The data are left- or right-aligned as described in Section 21.4.26: Data management.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
JSQ4[4:0] Res. JSQ3[4:0] Res. JSQ2[4:1]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
JSQ20 Res. JSQ1[4:0] JEXTEN[1:0] JEXTSEL[4:0] JL[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0440 Rev 9 699/2140
RM0440 Analog-to-digital converters (ADC)
713
Bits 31:27 JSQ4[4:0]: fourth conversion in the injected sequence
These bits are written by software with the channel number (0 to 18) assigned as the fourth
in the injected conversion sequence.c
Note: The software is allowed to write these bits only when JADSTART = 0 (which ensures
that no injected conversion is ongoing), unless the context queue is enabled
(JQDIS = 0 in the ADC_CFGR register).
Bit 26 Reserved, must be kept at reset value.
Bits 25:21 JSQ3[4:0]: third conversion in the injected sequence
These bits are written by software with the channel number (0 to 18) assigned as the third in
the injected conversion sequence.
Note: The software is allowed to write these bits only when JADSTART = 0 (which ensures
that no injected conversion is ongoing), unless the context queue is enabled
(JQDIS = 0 in the ADC_CFGR register).
Bit 20 Reserved, must be kept at reset value.
Bits 19:15 JSQ2[4:0]: second conversion in the injected sequence
These bits are written by software with the channel number (0 to 18) assigned as the second
in the injected conversion sequence.
Note: The software is allowed to write these bits only when JADSTART = 0 (which ensures
that no injected conversion is ongoing), unless the context queue is enabled
(JQDIS = 0 in the ADC_CFGR register).
Bit 14 Reserved, must be kept at reset value.
Bits 13:9 JSQ1[4:0]: first conversion in the injected sequence
These bits are written by software with the channel number (0 to 18) assigned as the first in
the injected conversion sequence.
Note: The software is allowed to write these bits only when JADSTART = 0 (which ensures
that no injected conversion is ongoing), unless the context queue is enabled
(JQDIS = 0 in the ADC_CFGR register).
Bits 8:7 JEXTEN[1:0]: External Trigger Enable and Polarity Selection for injected channels
These bits are set and cleared by software to select the external trigger polarity and enable
the trigger of an injected group.
00: If JQDIS = 0 (queue enabled), Hardware and software trigger detection disabled
00: If JQDIS = 1 (queue disabled), Hardware trigger detection disabled (conversions can be
launched by software)
01: Hardware trigger detection on the rising edge
10: Hardware trigger detection on the falling edge
11: Hardware trigger detection on both the rising and falling edges
Note: The software is allowed to write these bits only when JADSTART = 0 (which ensures
that no injected conversion is ongoing).
If JQM = 1 and if the Queue of Context becomes empty, the software and hardware
triggers of the injected sequence are both internally disabled (refer to Section 21.4.21:
Queue of context for injected conversions)

Analog-to-digital converters (ADC) RM0440
700/2140 RM0440 Rev 9
Note: Some channels are not connected physically  and must not be selected for conversion.
21.7.17 ADC offset y register (ADC_OFRy)
Address offset: 0x60 + 0x04 * (y -1), (y= 1 to 4)
Reset value: 0x0000 0000
Bits 6:2 JEXTSEL[4:0]: External Trigger Selection for injected group
These bits select the external event used to trigger the start of conversion of an injected
group:
00000: Event 0
00001: Event 1
00010: Event 2
00011: Event 3
00100: Event 4
00101: Event 5
00110: Event 6
00111: Event 7
...
11111: Event 31
Note: The software is allowed to write these bits only when JADSTART = 0 (which ensures
that no injected conversion is ongoing).
Bits 1:0 JL[1:0]: Injected channel sequence length
These bits are written by software to define the total number of conversions in the injected
channel conversion sequence.
00: 1 conversion
01: 2 conversions
10: 3 conversions
11: 4 conversions
Note: The software is allowed to write these bits only when JADSTART = 0 (which ensures
that no injected conversion is ongoing).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
OFFSET_
EN OFFSET_CH[4:0] SATEN OFFSE
TPOS Res. Res. Res. Res. Res. Res. Res. Res.
rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. OFFSET[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bit 31 OFFSET_EN: Offset y enable
This bit is written by software to enable or disable the offset programmed into bits
OFFSETy[11:0].
Note: The software is allowed to write this bit only when ADSTART = 0 and JADSTART = 0
(which ensures that no conversion is ongoing).

RM0440 Rev 9 701/2140
RM0440 Analog-to-digital converters (ADC)
713
21.7.18 ADC injected channel y data register (ADC_JDRy)
Address offset: 0x80 + 0x04 * (y - 1), (y = 1 to 4)
Reset value: 0x0000 0000
Bits 30:26 OFFSET_CH[4:0]: Channel selection for the data offset y
These bits are written by software to define the channel to which the offset programmed into
bits OFFSETy[11:0] applies.
Note: The software is allowed to write these bits only when ADSTART = 0 and
JADSTART = 0 (which ensures that no conversion is ongoing).
Some channels are not connected physically and must not be selected for the data
offset y.
Bit 25 SATEN: Saturation enable
This bit is set and cleared by software to enable the saturation at 0x000 and 0xFFF for the
offset function.
0: No saturation control, offset result can be signed
1: Saturation enabled, offset result unsigned and saturated at 0x000 and 0xFFF
Note: The software is allowed to write these bits only when ADSTART = 0 and
JADSTART = 0 (which ensures that no conversion is ongoing).
Bit 24 OFFSETPOS: Positive offset
This bit is set and cleared by software to enable the positive offset.
0: Negative offset
1: Positive offset
Note: The software is allowed to write these bits only when ADSTART = 0 and
JADSTART = 0 (which ensures that no conversion is ongoing).
Bits 23:12 Reserved, must be kept at reset value.
Bits 11:0 OFFSET[11:0]: Data offset y for the channel programmed into bits OFFSETy_CH[4:0]
These bits are written by software to define the offset y to be subtracted from the raw
converted data when converting a channel (can be regular or injected). The channel to which
applies the data offset y must be programmed in the bits OFFSETy_CH[4:0]. The conversion
result can be read from in the ADC_DR (regular conversion) or from in the ADC_JDRyi
registers (injected conversion).
Note: The software is allowed to write these bits only when ADSTART = 0 and
JADSTART = 0 (which ensures that no conversion is ongoing).
If several offset (OFFSETy) point to the same channel, only the offset with the lowest x
value is considered for the subtraction.
Ex: if OFFSET1_CH[4:0]=4 and OFFSET2_CH[4:0]=4, this is OFFSET1[11:0] which is
subtracted when converting channel 4.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
JDATA[15:0]
rrrrrrr r r r rrrrrr
Bits 31:16 Reserved, must  be kept at reset value.

Analog-to-digital converters (ADC) RM0440
702/2140 RM0440 Rev 9
21.7.19 ADC analog wa tchdog 2 configuration register (ADC_AWD2CR)
Address offset: 0xA0
Reset value: 0x0000 0000
21.7.20 ADC analog wa tchdog 3 configuration register (ADC_AWD3CR)
Address offset: 0xA4
Reset value: 0x0000 0000
Bits 15:0 JDATA[15:0]: Injected data
These bits are read-only. They contain the conversion result from injected channel y. The
data are left -or right-aligned as described in Section 21.4.26: Data management.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. AWD2CH[18:16]
rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 987654321 0
AWD2CH[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:19 Reserved, must be kept at reset value.
Bits 18:0 AWD2CH[18:0]: Analog watchdog 2 channel selection
These bits are set and cleared by software. They enable and select the input channels to be guarded
by the analog watchdog 2.
AWD2CH[i] = 0: ADC analog input channel i is not monitored by AWD2
AWD2CH[i] = 1: ADC analog input channel i is monitored by AWD2
When AWD2CH[18:0] = 000..0, the analog watchdog 2 is disabled
Note: The channels selected by AWD2CH must be also selected into the SQi or JSQi bits.
The software is allowed to write these bits only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
Some channels are not connected physically and must not be selected for the analog
watchdog.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. AWD3CH[18:16]
rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
AWD3CH[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:19 Reserved, must be kept at reset value.

RM0440 Rev 9 703/2140
RM0440 Analog-to-digital converters (ADC)
713
21.7.21 ADC differential mode se lection register (ADC_DIFSEL)
Address offset: 0xB0
Reset value: 0x0000 0000
21.7.22 ADC calibrati on factors (ADC_CALFACT)
Address offset: 0xB4
Reset value: 0x0000 0000
Bits 18:0 AWD3CH[18:0]: Analog watchdog 3 channel selection
These bits are set and cleared by software. They enable and select the input channels to be guarded
by the analog watchdog 3.
AWD3CH[i] = 0: ADC analog input channel i is not monitored by AWD3
AWD3CH[i] = 1: ADC analog input channel i is monitored by AWD3
When AWD3CH[18:0] = 000..0, the analog watchdog 3 is disabled
Note: The channels selected by AWD3CH must be also selected into the SQi or JSQi bits.
The software is allowed to write these bits only when ADSTART = 0 and JADSTART = 0 (which
ensures that no conversion is ongoing).
Some channels are not connected physically and must not be selected for the analog
watchdog.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. DIFSEL[18:16]
rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DIFSEL[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw r
Bits 31:19 Reserved, must be kept at reset value.
Bits 18:0 DIFSEL[18:0]: Differential mode for channels 18 to 0.
These bits are set and cleared by software. They allow to select if a channel is configured as single-
ended or differential mode.
DIFSEL[i] = 0: ADC analog input channel is configured in single ended mode
DIFSEL[i] = 1: ADC analog input channel i is configured in differential mode
Note: The DIFSEL bits corresponding to channels that are either connected to a single-ended I/O port
or to an internal channel must be kept their reset value (single-ended input mode).
The software is allowed to write these bits only when the ADC is disabled (ADCAL = 0,
JADSTART = 0, JADSTP = 0, ADSTART = 0, ADSTP = 0, ADDIS = 0 and ADEN = 0).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Re s. Res. Res. Res. Res. CALFACT_D[6:0]
rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 987654321 0
Res. Res. Res. Res. Re s. Res. Res. Res. Res. CALFACT_S[6:0]
rw rw rw rw rw rw rw

Analog-to-digital converters (ADC) RM0440
704/2140 RM0440 Rev 9
21.7.23 ADC Gain compensation Register (ADC_GCOMP)
Address offset: 0xC0
Reset value: 0x0000 0000
Bits 31:23 Reserved, must be kept at reset value.
Bits 22:16 CALFACT_D[6:0]: Calibration Factors in differential mode
These bits are written by hardware or by software.
Once a differential inputs calibration is complete, they are updated by hardware with the calibration
factors.
Software can write these bits with a new calibration factor. If the new calibration factor is different
from the current one stored into the analog ADC, it is then applied once a new differential calibration
is launched.
Note: The software is allowed to write these bits only when ADEN = 1, ADSTART = 0 and
JADSTART = 0 (ADC is enabled and no calibration is ongoing and no conversion is ongoing).
Bits 15:7 Reserved, must be kept at reset value.
Bits 6:0 CALFACT_S[6:0]: Calibration Factors In single-ended mode
These bits are written by hardware or by software.
Once a single-ended inputs calibration is complete, they are updated by hardware with the
calibration factors.
Software can write these bits with a new calibration factor. If the new calibration factor is different
from the current one stored into the analog ADC, it is then applied once a new single-ended
calibration is launched.
Note: The software is allowed to write these bits only when ADEN = 1, ADSTART = 0 and
JADSTART = 0 (ADC is enabled and no calibration is ongoing and no conversion is ongoing).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. GCOMPCOEFF[13:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:14 Reserved, must be kept at reset value.
Bits 13:0 GCOMPCOEFF[13:0]: Gain compensation coefficient
These bits are set and cleared by software to program the gain compensation coefficient.
00 1000 0000 0000: gain factor of 0.5
...
01 0000 0000 0000: gain factor of 1
10 0000 0000 0000: gain factor of 2
11 0000 0000 0000: gain factor of 3
...
The coefficient is divided by 4096 to get the gain factor ranging from 0 to 3.999756.
Note: This gain compensation is only applied when GCOMP bit of ADC_CFGR2 register is 1.

RM0440 Rev 9 705/2140
RM0440 Analog-to-digital converters (ADC)
713
21.8 ADC common registers
These registers define the control and status registers common to master and slave ADCs:
21.8.1 ADCx common status regist er (ADCx_CSR) (x = 12 or 345)
Address offset: 0x300
Reset value: 0x0000 0000
This register provides an image of the status bits of the different ADCs. Nevertheless it is
read-only and does not allow to clear the different status bits. Instead each status bit must
be cleared by writing 0 to it in the corresponding ADC_ISR register.
One interface controls ADC1 and ADC2, while the other interface controls ADC3, ADC4 and
ADC5.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. JQOVF_
SLV
AWD3_
SLV
AWD2_
SLV
AWD1_
SLV
JEOS_
SLV
JEOC_
SLV
OVR_
SLV
EOS_
SLV
EOC_
SLV
EOSMP_
SLV
ADRDY_
SLV
rr r r r r r r r r r
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. JQOVF_
MST
AWD3_
MST
AWD2_
MST
AWD1_
MST
JEOS_
MST
JEOC_
MST
OVR_
MST
EOS_
MST
EOC_
MST
EOSMP_
MST
ADRDY_
MST
rr r r r r r r r r r
Bits 31:27 Reserved, must be kept at reset value.
Bit 26 JQOVF_SLV: Injected Context Queue Overflow flag of the slave ADC
This bit is a copy of the JQOVF bit in the corresponding ADC_ISR register.
Bit 25 AWD3_SLV: Analog watchdog 3 flag of the slave ADC
This bit is a copy of the AWD3 bit in the corresponding ADC_ISR register.
Bit 24 AWD2_SLV: Analog watchdog 2 flag of the slave ADC
This bit is a copy of the AWD2 bit in the corresponding ADC_ISR register.
Bit 23 AWD1_SLV: Analog watchdog 1 flag of the slave ADC
This bit is a copy of the AWD1 bit in the corresponding ADC_ISR register.
Bit 22 JEOS_SLV: End of injected sequence flag of the slave ADC
This bit is a copy of the JEOS bit in the corresponding ADC_ISR register.
Bit 21 JEOC_SLV: End of injected conversion flag of the slave ADC
This bit is a copy of the JEOC bit in the corresponding ADC_ISR register.
Bit 20 OVR_SLV: Overrun flag of the slave ADC
This bit is a copy of the OVR bit in the corresponding ADC_ISR register.
Bit 19 EOS_SLV: End of regular sequence flag of the slave ADC. This bit is a copy of the EOS bit in
the corresponding ADC_ISR register.
Bit 18 EOC_SLV: End of regular conversion of the slave ADC
This bit is a copy of the EOC bit in the corresponding ADC_ISR register.
Bit 17 EOSMP_SLV: End of Sampling phase flag of the slave ADC
This bit is a copy of the EOSMP2 bit in the corresponding ADC_ISR register.

Analog-to-digital converters (ADC) RM0440
706/2140 RM0440 Rev 9
21.8.2 ADCx common control regist er (ADCx_CCR) (x = 12 or 345)
Address offset: 0x308
Reset value: 0x0000 0000
One interface controls ADC1 and ADC2, while the other interface controls ADC3, ADC4 and
ADC5.
Bit 16 ADRDY_SLV: Slave ADC ready
This bit is a copy of the ADRDY bit in the corresponding ADC_ISR register.
Bits 15:11 Reserved, must be kept at reset value.
Bit 10 JQOVF_MST: Injected Context Queue Overflow flag of the master ADC
This bit is a copy of the JQOVF bit in the corresponding ADC_ISR register.
Bit 9 AWD3_MST: Analog watchdog 3 flag of the master ADC
This bit is a copy of the AWD3 bit in the corresponding ADC_ISR register.
Bit 8 AWD2_MST: Analog watchdog 2 flag of the master ADC
This bit is a copy of the AWD2 bit in the corresponding ADC_ISR register.
Bit 7 AWD1_MST: Analog watchdog 1 flag of the master ADC
This bit is a copy of the AWD1 bit in the corresponding ADC_ISR register.
Bit 6 JEOS_MST: End of injected sequence flag of the master ADC
This bit is a copy of the JEOS bit in the corresponding ADC_ISR register.
Bit 5 JEOC_MST: End of injected conversion flag of the master ADC
This bit is a copy of the JEOC bit in the corresponding ADC_ISR register.
Bit 4 OVR_MST: Overrun flag of the master ADC
This bit is a copy of the OVR bit in the corresponding ADC_ISR register.
Bit 3 EOS_MST: End of regular sequence flag of the master ADC
This bit is a copy of the EOS bit in the corresponding ADC_ISR register.
Bit 2 EOC_MST: End of regular conversion of the master ADC
This bit is a copy of the EOC bit in the corresponding ADC_ISR register.
Bit 1 EOSMP_MST: End of Sampling phase flag of the master ADC
This bit is a copy of the EOSMP bit in the corresponding ADC_ISR register.
Bit 0 ADRDY_MST: Master ADC ready
This bit is a copy of the ADRDY bit in the corresponding ADC_ISR register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. VBATS
EL
VSENSES
EL
VREF
EN PRESC[3:0] CKMODE[1:0]
rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 98 7 654321 0
MDMA[1:0] DMA
CFG Res. DELAY[3:0] Res. Res. Res. DUAL[4:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:25 Reserved, must be kept at reset value.

RM0440 Rev 9 707/2140
RM0440 Analog-to-digital converters (ADC)
713
Bit 24 VBATSEL: VBAT selection
This bit is set and cleared by software to control VBAT.
0: VBAT channel disabled.
1: VBAT channel enabled
Bit 23 VSENSESEL: VTS selection
This bit is set and cleared by software to control VTS.
0: Temperature sensor channel disabled
1: Temperature sensor channel enabled
Bit 22 VREFEN: VREFINT enable
This bit is set and cleared by software to enable/disable the VREFINT channel.
0: VREFINT channel disabled
1: VREFINT channel enabled
Bits 21:18 PRESC[3:0]: ADC prescaler
These bits are set and cleared by software to select the frequency of the clock to the ADC.
The clock is common for all the ADCs.
0000: input ADC clock not divided
0001: input ADC clock divided by 2
0010: input ADC clock divided by 4
0011: input ADC clock divided by 6
0100: input ADC clock divided by 8
0101: input ADC clock divided by 10
0110: input ADC clock divided by 12
0111: input ADC clock divided by 16
1000: input ADC clock divided by 32
1001: input ADC clock divided by 64
1010: input ADC clock divided by 128
1011: input ADC clock divided by 256
other: reserved
Note: The software is allowed to write these bits only when the ADC is disabled (ADCAL = 0,
JADSTART = 0, ADSTART = 0, ADSTP = 0, ADDIS = 0 and ADEN = 0). The ADC
prescaler value is applied only when CKMODE[1:0] = 00.
Bits 17:16 CKMODE[1:0]: ADC clock mode
These bits are set and cleared by software to define the ADC clock scheme (which is
common to both master and slave ADCs):
00: adc_ker_ck (x = 123) (Asynchronous clock mode), generated at product level (refer to
Section 6: Reset and clock control (RCC))
01: adc_hclk/1 (Synchronous clock mode). This configuration must be enabled only if the
AHB clock prescaler is set (HPRE[3:0] = 0xxx in RCC_CFGR register) and if the system
clock has a 50% duty cycle.
10: adc_hclk/2 (Synchronous clock mode)
11: adc_hclk/4 (Synchronous clock mode)
In all synchronous clock modes, there is no jitter in the delay from a timer trigger to the start
of a conversion.
Note: The software is allowed to write these bits only when the ADCs are disabled
(ADCAL = 0, JADSTART = 0, ADSTART = 0, ADSTP = 0, ADDIS = 0 and ADEN = 0).

Analog-to-digital converters (ADC) RM0440
708/2140 RM0440 Rev 9
Bits 15:14 MDMA[1:0]: Direct memory access mode for dual ADC mode
This bitfield is set and cleared by software. Refer to the DMA controller section for more
details.
00: MDMA mode disabled
01: Reserved
10: MDMA mode enabled for 12 and 10-bit resolution
11: MDMA mode enabled for 8 and 6-bit resolution
Note: The software is allowed to write these bi ts only when ADSTART = 0 (which ensures that
no regular conversion is ongoing).
Bit 13 DMACFG: DMA configuration (for dual ADC mode)
This bit is set and cleared by software to select between two DMA modes of operation and is
effective only when DMAEN = 1.
0: DMA One Shot mode selected
1: DMA Circular mode selected
For more details, refer to Section : Managing conversions using the DMA
Note: The software is allowed to write these bi ts only when ADSTART = 0 (which ensures that
no regular conversion is ongoing).
Bit 12 Reserved, must be kept at reset value.
Bits 11:8 DELAY: Delay between 2 sampling phases
These bits are set and cleared by software. These bits are used in dual interleaved modes.
Refer to [Table 179](../tables/table_179.md) for the value of ADC resolution versus DELAY bits values.
Note: The software is allowed to write these bits only when the ADCs are disabled
(ADCAL = 0, JADSTART = 0, ADSTART = 0, ADSTP = 0, ADDIS = 0 and ADEN = 0).
Bits 7:5 Reserved, must be kept at reset value.
Bits 4:0 DUAL[4:0]: Dual ADC mode selection
These bits are written by software to select the operating mode.
All the ADCs independent:
00000: Independent mode
00001 to 01001: Dual mode, master and slave ADCs working together
00001: Combined regular simultaneous + injected simultaneous mode
00010: Combined regular simultaneous + alternate trigger mode
00011: Combined Interleaved mode + injected simultaneous mode
00100: Reserved
00101: Injected simultaneous mode only
00110: Regular simultaneous mode only
00111: Interleaved mode only
01001: Alternate trigger mode only
All other combinations are reserved and must not be programmed
Note: The software is allowed to write these bits only when the ADCs are disabled
(ADCAL = 0, JADSTART = 0, ADSTART = 0, ADSTP = 0, ADDIS = 0 and ADEN = 0).
[Table 179](../tables/table_179.md). DELAY bits versus ADC resolution
DELAY bits 12-bit resolution 10-bit reso lution 8-bit resolution 6-bit resolution
0000 1 * T adc_ker_ck 1 * Tadc_ker_ck 1 * Tadc_ker_ck 1 * Tadc_ker_ck
0001 2 * T adc_ker_ck 2 * Tadc_ker_ck 2 * Tadc_ker_ck 2 * Tadc_ker_ck
0010 3 * T adc_ker_ck 3 * Tadc_ker_ck 3 * Tadc_ker_ck 3 * Tadc_ker_ck

RM0440 Rev 9 709/2140
RM0440 Analog-to-digital converters (ADC)
713
0011 4 * T adc_ker_ck 4 * Tadc_ker_ck 4 * Tadc_ker_ck 4 * Tadc_ker_ck
0100 5 * T adc_ker_ck 5 * Tadc_ker_ck 5 * Tadc_ker_ck 5 * Tadc_ker_ck
0101 6 * T adc_ker_ck 6 * Tadc_ker_ck 6 * Tadc_ker_ck 6 * Tadc_ker_ck
0110 7 * T adc_ker_ck 7 * Tadc_ker_ck 7 * Tadc_ker_ck 6 * Tadc_ker_ck
0111 8 * T adc_ker_ck 8 * Tadc_ker_ck 8 * Tadc_ker_ck 6 * Tadc_ker_ck
1000 9 * T adc_ker_ck 9 * Tadc_ker_ck 8 * Tadc_ker_ck 6 * Tadc_ker_ck
1001 10 * T adc_ker_ck 10 * Tadc_ker_ck 8 * Tadc_ker_ck 6 * Tadc_ker_ck
1010 11 * T adc_ker_ck 10 * Tadc_ker_ck 8 * Tadc_ker_ck 6 * Tadc_ker_ck
1011 12 * T adc_ker_ck 10 * Tadc_ker_ck 8 * Tadc_ker_ck 6 * Tadc_ker_ck
others 12 * T adc_ker_ck 10 * Tadc_ker_ck 8 * Tadc_ker_ck 6 * Tadc_ker_ck
[Table 179](../tables/table_179.md). DELAY bits versus ADC resolution (continued)
DELAY bits 12-bit resolution 10-bit reso lution 8-bit resolution 6-bit resolution

Analog-to-digital converters (ADC) RM0440
710/2140 RM0440 Rev 9
21.8.3 ADCx common regular data re gister for dual mode (ADCx_CDR)
(x = 12 or 345)
Address offset: 0x30C
Reset value: 0x0000 0000
One interface controls ADC1 and ADC2, while the other interface controls ADC3, ADC4 and
ADC5.
21.9   ADC register map
The following table summarizes the ADC registers.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
RDATA_SLV[15:0]
rrrrrrr r r r rrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
RDATA_MST[15:0]
rrrrrrr r r r rrrrrr
Bits 31:16 RDATA_SLV[15:0]: Regular data of the slave ADC
In dual mode, these bits contain the regular data of the slave ADC. Refer to Section 21.4.30:
Dual ADC modes.
The data alignment is applied as described in Section : Data register, data alignment and
offset (ADC_DR, OFFSETy, OFFSETy_CH, ALIGN))
Bits 15:0 RDATA_MST[15:0]: Regular data of the master ADC.
In dual mode, these bits contain the regular data of the master ADC. Refer to
Section 21.4.30: Dual ADC modes.
The data alignment is applied as described in Section : Data register, data alignment and
offset (ADC_DR, OFFSETy, OFFSETy_CH, ALIGN))
In MDMA = 11 mode, bits 15:8 contains SLV_ADC_DR[7:0], bits 7:0 contains
MST_ADC_DR[7:0].
[Table 180](../tables/table_180.md). ADC global register map
Offset Register
0x000 - 0x0FC Master ADC1/ADC3
0x100 - 0x1FC Slave ADC2/ADC4
0x200 - 0x2FC Reserved/single ADC5
0x300 - 0x30C Master and slave ADCs common registers

RM0440 Rev 9 711/2140
RM0440 Analog-to-digital converters (ADC)
713
[Table 181](../tables/table_181.md). ADC register map and reset values for each ADC (offset = 0x000
for master ADC, 0x100 for slave ADC)
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
0x00 ADC_ISR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
JQOVF
AWD3
AWD2
AWD1
JEOS
JEOC
OVR
EOS
EOC
EOSMP
ADRDY
Reset value 00000000000
0x04 ADC_IER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
JQOVFIE
AWD3IE
AWD2IE
AWD1IE
JEOSIE
JEOCIE
OVRIE
EOSIE
EOCIE
EOSMPIE
ADRDYIE
Reset value 00000000000
0x08 ADC_CR
ADCAL
ADCALDIF
DEEPPWD
ADVREGEN
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
JADSTP
ADSTP
JADSTART
ADSTART
ADDIS
ADEN
Reset value 0 010 000000
0x0C ADC_CFGR
JQDIS.
AWD1CH[4:0]
JAUTO
JAWD1EN
AWD1EN
AWD1SGL
JQM
JDISCEN
DISCNUM
[2:0]
DISCEN
ALIGN
AUTDLY
CONT
OVRMOD
EXTEN[1:0]
EXTSEL[4:0] RES
[1:0]
Res.
DMACFG
DMAEN
Reset value 1 0000000000000000000000000000 00
0x10 ADC_CFGR2
Res.
Res.
Res.
Res.
SMPTRIG
BULB
SWTRIG
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
GCOMP
Res.
Res.
Res.
Res.
Res.
ROVSM
TROVS
OVSS[3:0] OVSR
[2:0]
JOVSE
ROVSE
Reset value 000 0 00000000000
0x14 ADC_SMPR1
SMPPLUS.
Res.
SMP9
[2:0]
SMP8
[2:0]
SMP7
[2:0]
SMP6
[2:0]
SMP5
[2:0]
SMP4
[2:0]
SMP3
[2:0]
SMP2
[2:0]
SMP1
[2:0]
SMP0
[2:0]
Reset value 0 000000000000000000000000000000
0x18 ADC_SMPR2
Res.
Res.
Res.
Res.
Res.
SMP18
[2:0]
SMP17
[2:0]
SMP16
[2:0]
SMP15
[2:0]
SMP14
[2:0]
SMP13
[2:0]
SMP12
[2:0]
SMP11
[2:0]
SMP10
[2:0]
Reset value 000000000000000000000000000
0x1C Reserved Res.
0x20 ADC_TR1
Res.
Res.
Res.
Res.
HT1[11:0]
Res.
AWDFILT
[2:0] LT1[11:0]
Reset value 111111111111 000000000000
0x24 ADC_TR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
HT2[[7:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
LT2[7:0]
Reset value 11111111 00000000
0x28 ADC_TR3
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
HT3[[7:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
LT3[7:0]
Reset value 11111111 00000000
0x2C Reserved Res.
0x30 ADC_SQR1
Res.
Res.
Res.
SQ4[4:0]
Res.
SQ3[4:0]
Res.
SQ2[4:0]
Res.
SQ1[4:0]
Res.
Res.
L[3:0]
Reset value 00000 00000 00000 00000 0000
0x34 ADC_SQR2
Res.
Res.
Res.
SQ9[4:0]
Res.
SQ8[4:0]
Res.
SQ7[4:0]
Res.
SQ6[4:0]
Res.
SQ5[4:0]
Reset value 00000 00000 00000 00000 00000
0x38 ADC_SQR3
Res.
Res.
Res.
SQ14[4:0]
Res.
SQ13[4:0]
Res.
SQ12[4:0]
Res.
SQ11[4:0]
Res.
SQ10[4:0]
Reset value 00000 00000 00000 00000 00000
0x3C ADC_SQR4
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SQ16[4:0]
Res.
SQ15[4:0]
Reset value 00000 00000
0x40 ADC_DR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
regular RDATA[15:0]
Reset value 0000000000000000

Analog-to-digital converters (ADC) RM0440
712/2140 RM0440 Rev 9
0x44-
0x48 Reserved Res.
0x4C ADC_JSQR JSQ4[4:0]
Res.
JSQ3[4:0]
Res.
JSQ2[4:0]
Res.
JSQ1[4:0]
JEXTEN[1:0]
JEXTSEL
[4:0] JL[1:0]
Reset value 0 0000 00000 00000 00000000000000
0x50-
0x5C Reserved Res.
0x60 ADC_OFR1
OFFSET1_EN
OFFSET1_
CH[4:0]
SATEN
OFFSETPOS
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OFFSET1[11:0]
Reset value 0 0000000 000000000000
0x64 ADC_OFR2
OFFSET2_EN
OFFSET2_
CH[4:0]
SATEN
OFFSETPOS
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OFFSET2[11:0]
Reset value 0 0000000 000000000000
0x68 ADC_OFR3
OFFSET3_EN
OFFSET3_
CH[4:0]
SATEN
OFFSETPOS
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OFFSET3[11:0]
Reset value 0 0000000 000000000000
0x6C ADC_OFR4
OFFSET4_EN
OFFSET4_
CH[4:0]
SATEN
OFFSETPOS
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OFFSET4[11:0]
Reset value 0 0000000 000000000000
0x70-
0x7C Reserved Res.
0x80 ADC_JDR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
JDATA1[15:0]
Reset value 0000000000000000
0x84 ADC_JDR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
JDATA2[15:0]
Reset value 0000000000000000
0x88 ADC_JDR3
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
JDATA3[15:0]
Reset value 0000000000000000
0x8C ADC_JDR4
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
JDATA4[15:0]
Reset value 0000000000000000
0x8C-
0x9C Reserved Res.
0xA0 ADC_AWD2CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWD2CH[18:0]
Reset value 0000000000000000000
0xA4 ADC_AWD3CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWD3CH[18:0]
Reset value 0000000000000000000
0xA8-
0xAC Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
[Table 181](../tables/table_181.md). ADC register map and reset values for each ADC (offset = 0x000
for master ADC, 0x100 for slave ADC) (continued)
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

RM0440 Rev 9 713/2140
RM0440 Analog-to-digital converters (ADC)
713
Refer to Section 2.2 on page 82 for the register boundary addresses.
0xB0 ADC_DIFSEL
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
DIFSEL[18:0]
Reset value 0000000000000000000
0xB4 ADC_CALFACT
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CALFACT_D[6:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CALFACT_S[6:0]
Reset value 0000000 0000000
0xC0 ADC_GCOMP
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
GCOMP[13:0]
Reset value 00000000000000
[Table 181](../tables/table_181.md). ADC register map and reset values for each ADC (offset = 0x000
for master ADC, 0x100 for slave ADC) (continued)
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
[Table 182](../tables/table_182.md). ADC register map and reset values (master and slave ADC
common registers) offset = 0x300
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
0x00 ADCx_CSR
Res.
Res.
Res.
Res.
Res.
JQOVF_SLV
AWD3_SLV
AWD2_SLV
AWD1_SLV
JEOS_SLV
JEOC_SLV
OVR_SLV
EOS_SLV
EOC_SLV
EOSMP_SLV
ADRDY_SLV
Res.
Res.
Res.
Res.
Res.
JQOVF_MST
AWD3_MST
AWD2_MST
AWD1_MST
JEOS_MST
JEOC_MST
OVR_MST
EOS_MST
EOC_MST
EOSMP_MST
ADRDY_MST
slave ADC2 master ADC1
R e s e t  v a l u e 00000000000 00000000000
0x04 Reserved Res.
0x08 ADCx_CCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
VBATSEL
VSENSESEL
VREFEN
PRESC[3:0]
CKMODE[1:0]
MDMA[1:0]
DMACFG
Res.DELAY[3:0]
Res.
Res.
Res. DUAL[4:0]
R e s e t  v a l u e 000000000000 0000 00000
0x0C ADCx_CDR RDATA_SLV[15:0] RDATA_MST[15:0]
R e s e t  v a l u e 00000000000000000000000000000000
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 82: Architectural Diagram](../figures/figure_82.md)
* [Figure 83: Architectural Diagram](../figures/figure_83.md)
* [Figure 84: Architectural Diagram](../figures/figure_84.md)
* [Figure 85: Architectural Diagram](../figures/figure_85.md)
* [Figure 86: Architectural Diagram](../figures/figure_86.md)
* [Figure 87: Architectural Diagram](../figures/figure_87.md)
* [Figure 88: Architectural Diagram](../figures/figure_88.md)
* [Figure 89: Architectural Diagram](../figures/figure_89.md)
* [Figure 90: Architectural Diagram](../figures/figure_90.md)
* [Figure 91: Architectural Diagram](../figures/figure_91.md)
* [Figure 92: Architectural Diagram](../figures/figure_92.md)
* [Figure 93: Architectural Diagram](../figures/figure_93.md)
* [Figure 94: Architectural Diagram](../figures/figure_94.md)
* [Figure 95: Architectural Diagram](../figures/figure_95.md)
* [Figure 96: Architectural Diagram](../figures/figure_96.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 161: Configuration Matrix](../tables/table_161.md)
* [Table 162: Configuration Matrix](../tables/table_162.md)
* [Table 163: Configuration Matrix](../tables/table_163.md)
* [Table 164: Configuration Matrix](../tables/table_164.md)
* [Table 165: Configuration Matrix](../tables/table_165.md)
* [Table 166: Configuration Matrix](../tables/table_166.md)
* [Table 167: Configuration Matrix](../tables/table_167.md)
* [Table 168: Configuration Matrix](../tables/table_168.md)
* [Table 169: Configuration Matrix](../tables/table_169.md)
* [Table 170: Configuration Matrix](../tables/table_170.md)
* [Table 171: Configuration Matrix](../tables/table_171.md)
* [Table 172: Configuration Matrix](../tables/table_172.md)
* [Table 173: Configuration Matrix](../tables/table_173.md)
* [Table 174: Configuration Matrix](../tables/table_174.md)
* [Table 175: Configuration Matrix](../tables/table_175.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)