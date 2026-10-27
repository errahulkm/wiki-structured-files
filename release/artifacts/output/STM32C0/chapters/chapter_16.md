# Chapter 16: Analog-to-digital converter (ADC)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32C0 Reference Manual RM0490 - Chapter 16: Analog-to-digital converter (ADC).
* **Document Source**: RM0490 Reference Manual
* **PDF Reference Location**: Pages 287 - 345
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Analog-to-Digital Converter (ADC)](../peripherals/adc.md)

## 2. Official Reference Manual Text Content (RM0490 Ingestion)
```text
RM0490 Rev 6 287/1023
RM0490 Analog-to-digital converter (ADC)
345
16 Analog-to-digital converter (ADC)
16.1 Introduction
The 12-bit ADC is a successive approximation analog-to-digital converter. It has up to 23
multiplexed channels allowing it to measure signals from 19 external and 4 internal sources.
A/D conversion of the various channels can be performed in single, continuous, scan or
discontinuous mode. The result of the ADC is stored in a left-aligned or right-aligned 16-bit
data register.
The analog watchdog feature allows the application to detect if the input voltage goes
outside the user-defined higher or lower thresholds.
An efficient low-power mode is implemented to allow very low consumption at low
frequency.
A built-in hardware oversampler allows analog performances to be improved while off-
loading the related computational burden from the CPU.

Analog-to-digital converter (ADC) RM0490
288/1023 RM0490 Rev 6
16.2 ADC main features
• High performance
– 12-bit, 10-bit, 8-bit or 6-bit configurable resolution
– ADC conversion time: 0.4 µs for 12-bit resolution (2.5Msps), faster conversion
times can be obtained by lowering resolution.
– Self-calibration
– Programmable sampling time
– Data alignment with built-in data coherency
– DMA support
• Low-power
– The application ca n reduce PCLK frequency for low-power operation while still
keeping optimum ADC performance. For example, 0.4 µs conversion time is kept,
whatever the PCLK frequency
– Wait mode: prevents ADC overrun in applications with low PCLK frequency
– Auto off mode: ADC is automatically powered off except during the active
conversion phase. This dramatically reduces the power consumption of the ADC.
• Analog input channels
– Up to 19 external analog inputs
– 1 channel for internal temperature sensor (V SENSE)
– 1 channel for internal reference voltage (V REFINT)
– 2 channels for monitoring internal power supply (V DDA/VSSA)
• Start-of-conversion can be initiated:
– By software
– By hardware triggers with configurable polarity (timer events or GPIO input
events)
• Conversion modes
– Can convert a single channel or can scan a sequence of channels.
– Single mode converts selected inputs once per trigger
– Continuous mode converts selected inputs continuously
– Discontinuous mode
• Interrupt generation at the end of sampling, end of conversion, end of sequence
conversion, and in case of analog watchdog or overrun events
• Analog watchdog
• Oversampler
– 16-bit data register
– Oversampling ratio adjustable from 2 to 256x
– Programmable data shift up to 8-bits
• ADC input range: VSSA ≤ VIN ≤ VREF+

RM0490 Rev 6 289/1023
RM0490 Analog-to-digital converter (ADC)
345
16.3 ADC implementation
[Table 66](../tables/table_66.md). ADC main features
ADC modes/features STM32C011x x STM32C031/51/71/91/92xx
Resolution 12 bits
Maximum sampling speed 2.5 Msps
Hardware offset calibration X
Single-ended inputs X
Differential inputs -
Oversampling mode X
Data register 16 bits
DMA support X
Number of analog watchdogs 3
Number of external channels 13 19
Number of internal channels 4

Analog-to-digital converter (ADC) RM0490
290/1023 RM0490 Rev 6
16.4 ADC functional description
[Figure 30](../figures/figure_30.md) shows the ADC block diagram and [Table 67](../tables/table_67.md) gives the ADC pin description.
[Figure 30](../figures/figure_30.md). ADC block diagram
1. TRGi are mapped at product level. Refer to Table External triggers in Section 16.4.1: ADC pins and internal signals.
MSv68740V5
Input
selection &
scan
control
SMP[2:0]
sampling time
ADC_IN[22:17,
14:11,8:0] Analog input
channels
AUTDLY
Auto-delayed
conversion
ADSTART
SW trigger
EXTEN[1:0]
trigger enable
and edge selection
HW
trigger
EXTSEL[2:0]
trigger selection
LFTRIG
Analog
supply
(VDDA)
start
AHB
interface DMA request
ADC interrupt
ADC_AWDx
_OUT
to analog
watchdogs
AWDxEN
AWDxSGL
AWDCHx[4:0]
LTx[11:0]
HTx[11:0]
DISCEN
Discontinuous
mode enable
VIN
ADCAL self-
calibration
ADSTP
stop conversion
SCANDIR
up/down
SAR ADC
Suppy and
reference
CONVERTED
DATA
APB
interface
ADREADY
EOSMP
EOS
EOC
OVR
AWDx
VIN[X]
AHB
slave
CHSEL[22:0]
CONT
single/continuous
AUTOFF
Auto-off modeADEN/ADDIS
OVRMOD
(overrun mode)
ALIGN
(left/right)
RES[1:0]
(12, 10, 8 bits)
DATA[15:0]
DMAEN
DMACFG
Start & Stop
control
VREFINT
VSENSE
VSSA
VDDA
TRG0
TRG1
TRG2
TRG3
TRG4
TRG5
TRG6
TRG7
TOVS
OVSS[3:0]
OVSR[3:0]
OVSE
Over-
sampler
VREF+

RM0490 Rev 6 291/1023
RM0490 Analog-to-digital converter (ADC)
345
16.4.1 ADC pins a nd internal signals
[Table 67](../tables/table_67.md). ADC input/output pins
Name Signal type Remarks
VDDA Input, analog power supply Analog power supply and positive reference voltage for the ADC
VSSA Input, analog supply ground Ground for analog power supply
VREF+ Input, analog reference positive The higher/positive reference voltage for the ADC.
ADC_INx Analog input signals Up to 19 external analog input channels
[Table 68](../tables/table_68.md). ADC internal input/output signals
Internal signal
name Signal type Description
VIN[x] Analog input channels Connected either to internal channels or to ADC_INi external channels
TRGx Input ADC conversion triggers
VSENSE Input Internal temperatur e sensor output voltage
VREFINT Input Internal voltage reference output voltage
ADC_AWDx_OUT Output Internal analog watchdog output signal connected to on-chip timers (x = Analog watchdog number = 1,2,3)
[Table 69](../tables/table_69.md). External triggers
Name Source EXTSEL[2:0]
TRG0 TIM1_TRGO2 000
TRG1 TIM1_CC4 001
TRG2 TIM2_TRGO (1)
1. Available only on STM32C051/71/91/92xx devices.
010
TRG3 TIM3_TRGO 011
TRG4 TIM15_TRGO (2)
2. Available only on STM32C091/92xx devices.
100
TRG5 Reserved 101
TRG6 Reserved 110
TRG7 EXTI11 111

Analog-to-digital converter (ADC) RM0490
292/1023 RM0490 Rev 6
16.4.2 ADC voltage re gulator (ADVREGEN)
The ADC has a specific internal voltage regulator which must be enabled and stable before
using the ADC.
The ADC internal voltage regulator can be enabled by setting ADVREGEN bit to 1 in the
ADC_CR register. The software must wait for the ADC voltage regulator startup time
(tADCVREG_STUP) before launching a calibration or enabling the ADC. This delay must be
managed by software (for details on tADCVREG_STUP, refer to the device datasheet).
After ADC operations are complete, the ADC is disabled (ADEN = 0). To keep power
consumption low, it is important to disable the ADC voltage regulator before entering low-
power mode (LPRun, LPSleep or Stop mode). Refer to Section : ADC voltage regulator
disable sequence).
Note: When the internal voltage regulator is disa bled, the internal analog calibration is kept.
Analog reference from the power control unit
The internal ADC voltage regulator internally uses an analog reference delivered by the
power control unit through a buffer. This buffer is always enabled when the main voltage
regulator of the power control unit operates in normal Run mode (refer to Reset and clock
control and power control sections).
If the main voltage regulator enters low-power mode (such as Low-power run mode), this
buffer is disabled and the ADC cannot be used.
ADC Voltage regulator enable sequence
To enable the ADC voltage regulator, set ADVREGEN bit to 1 in ADC_CR register.
ADC voltage regulator disable sequence
To disable the ADC voltage regulator, follow the sequence below:
1. Make sure that the ADC is disabled (ADEN = 0).
2. Clear ADVREGEN bi t in ADC_CR register.
16.4.3 Calibration (ADCAL)
The ADC has a calibration feature. During the procedure, the ADC calculates a calibration
factor which is internally applied to the ADC until the next ADC power-off. The application
must not use the ADC during calibration and must wait until it is complete.
Calibration should be performed before starting A/D conversion. It removes the offset error
which may vary from chip to chip due to process variation.
The calibration is initiated by software by setting bit ADCAL to 1. It can be initiated only
when all the following conditions are met:
• the ADC voltage regulator is enabled (ADVREGEN = 1),
• the ADC is disabled (ADEN = 0), and
• the Auto-off mode is disabled (AUTOFF = 0).
ADCAL bit stays at 1 during all the calibration sequence. It is then cleared by hardware as
soon the calibration completes. After this, the calibration factor can be read from the
ADC_DR register (from bits 6 to 0).

RM0490 Rev 6 293/1023
RM0490 Analog-to-digital converter (ADC)
345
The internal analog calibration is kept if the ADC is disabled (ADEN = 0). When the ADC
operating conditions change (VREF+ changes are the main contributor to ADC offset
variations and temperature change to a lesser extend), it is recommended to re-run a
calibration cycle.
The calibration factor is lost in the following cases:
• The power supply is removed from the ADC (for example when the product enters
Standby  mode)
• The ADC peripheral is reset.
The calibration factor is lost each time power is removed from the ADC (for example when
the product enters Standby  mode). Still, it is possible to save and restore the calibration
factor by software to save time when re-starting the ADC (as long as temperature and
voltage are stable during the ADC power-down).
The calibration factor can be written if the ADC is enabled but not converting (ADEN = 1 and
ADSTART = 0). Then, at the next start of conversion, the calibration factor is automatically
injected into the analog ADC. This loading is transparent and does not add any cycle
latency to the start of the conversion.
Software calibration procedure
1. Ensure that ADEN = 0, AUTOFF = 0, ADVREGEN = 1, and DMAEN = 0.
2. Set ADCAL = 1.
3. Wait until ADCAL = 0 (or until EOCAL = 1). This can be handled by interrupt if the
interrupt is enabled by setting the EOCALIE bit in the ADC_IER register.
4. The calibration factor minus one can then be read from bits 6:0 of the ADC_DR or
ADC_CALFACT registers. The resulting calibration factor must be incremented by one
and written back to the ADC_CALFACT register.
5. To reduce the noise effect of the calibrati on factor extraction, the software can make
the average of eight calibration factor values. This step is optional but recommended
for better accuracy.
The averaging procedure is as follows
a) Obtain eight incremented calibration factor values (perform eight times step 2 to
step 4).
b) Calculate the average of these eight val ues and round it up to the nearest integer.
c) Write the result to the ADC_CALFACT  register.
Note: If the resulting ca libration factor is higher than 0x7F, write 0x7F to the ADC_CALFACT
register to avoid overflow.

Analog-to-digital converter (ADC) RM0490
294/1023 RM0490 Rev 6
[Figure 31](../figures/figure_31.md). ADC calibration
Calibration factor forcing software procedure
1. Ensure that ADEN = 1 and ADSTART = 0 (ADC started with no conversion ongoing)
2. Write ADC_CALFACT with the saved calibration factor
3. The calibration factor is used as s oon as a new conversion is launched.
[Figure 32](../figures/figure_32.md). Calibration factor forcing
16.4.4 ADC on-off contro l (ADEN, ADDIS, ADRDY)
At power-up, the ADC is disabled and put in power-down mode (ADEN = 0).
As shown in [Figure 33](../figures/figure_33.md), the ADC needs a stabilization time of tSTAB before it starts
converting accurately.
Two control bits are used to enable or disable the ADC:
• Set ADEN = 1 to enable the ADC. The ADRDY flag is set as soon as the ADC is ready
for operation.
• Set ADDIS = 1 to disable the ADC and put the ADC in power down mode. The ADEN
and ADDIS bits are then automatically cleared by hardware as soon as the ADC is fully
disabled.
MSv33703V2
tCAB
ADCAL
ADC State
ADC_DR[6:0] 0x00
CALIBRATE OFFStartupOFF
by SW by HW
CALIBRATION
FACTORADC_CALFACT[6:0]
MSv31925V2
ADC state
F2
F1 F2
Ready (not converting) Converting channel Ready Converting channel
(Single ended) (Single ended)Updating
calibration
by S/W
Internal calibration
factor[6:0]
Start conversion
(hardware or software)
WRITE ADC_CALFACT
by H/W
CALFACT[6:0]

RM0490 Rev 6 295/1023
RM0490 Analog-to-digital converter (ADC)
345
Conversion can then start either by setting ADSTART to 1 (refer to Section 16.5: Conversion
on external trigger and trigger polarity (EXTSEL, EXTEN)) or when an external trigger event
occurs if triggers are enabled.
Follow this procedure to enable the ADC:
1. Clear the ADRDY bit in ADC_ISR regi ster by programming this bit to 1.
2. Set ADEN = 1 in the ADC_CR register.
3. Wait until ADRDY = 1 in the ADC_ISR regi ster (ADRDY is set after the ADC startup
time). This can be handled by interrupt if the interrupt is enabled by setting the
ADRDYIE bit in the ADC_IER register.
Follow this procedure to disable the ADC:
1. Check that ADSTART = 0 in the ADC_CR regi ster to ensure that no conversion is
ongoing. If required, stop any ongoing conversion by writing 1 to the ADSTP bit in the
ADC_CR register and waiting until this bit is read at 0.
2. Set ADDIS = 1 in the ADC_CR register.
3. If required by the applicati on, wait until ADEN = 0 in the ADC_CR register, indicating
that the ADC is fully disabled (ADDIS is automatically reset once ADEN = 0).
4. Clear the ADRDY bit in ADC_ISR register by programming this bit to 1 (optional).
[Figure 33](../figures/figure_33.md). Enabling/disabling the ADC
Note: In Auto-off mode (AUTOFF = 1) the power-on/off phases are performed automatically, by
hardware and the ADRDY flag is not set.
When the bus clock is much faster than the analog ADC clock (fADC), a minimum delay of
ten fADC clock cycles must be respected between ADEN and ADDIS bit settings.
Caution: The ADEN bit cannot be set while the ADCAL bit is set, and during four ADC clock cycles
after the ADCAL bit is cleared by the hardware (end of calibration).
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

Analog-to-digital converter (ADC) RM0490
296/1023 RM0490 Rev 6
16.4.5 ADC clock ( CKMODE, PRESC[3:0])
The ADC has a dual clock-domain architecture, so that the ADC can be fed with a clock
(ADC asynchronous clock) independent from the APB clock (PCLK).
[Figure 34](../figures/figure_34.md). ADC clock scheme
1. Refer to Section Reset and clock control (RCC) for how the PCLK clock and ADC asynchronous clock are
enabled.
The input clock of the analog ADC can be selected between two different clock sources (see
[Figure 34](../figures/figure_34.md): ADC clock scheme to see how the PCLK clock and the ADC asynchronous clock
are enabled):
a) The ADC clock can be a specific clock source, named “ADC asynchronous clock“
which is independent and asynchronous with the APB clock.
Refer to RCC Section for more information on generating this clock source.
To select this scheme, bits CKMODE[1:0] of the ADC_CFGR2 register must be
reset.
b) The ADC clock can be derived from th e APB clock of the ADC bus interface,
divided by a programmable factor (1, 2 or 4) according to bits CKMODE[1:0].
To select this scheme, bits CKMODE[1:0] of the ADC_CFGR2 register must be
different from “00”.
In option a), the generated ADC clock can eventually be divided by a prescaler (1, 2, 4, 6, 8,
10, 12, 16, 32, 64, 128, 256) when programming the bits PRESC[3:0] in the ADC_CCR
register).
Option a) has the advantage of reaching the maximum ADC clock frequency whatever the
APB clock scheme selected.
Option b) has the advantage of bypassing the clock domain resynchronizations. This can be
useful when the ADC is triggered by a timer and if the application requires that the ADC is
precisely triggered without any uncertainty (otherwise, an uncertainty of the trigger instant is
added by the resynchronizations between the two clock domains).
MSv31926V5
ADITF
Analog
ADC
RCC
(Reset & Clock Controller)
PCLK
ADC
asynchronous
clock
APB interface
Analog ADC
clock (fADC)/1 or /2 or /4 Others
00
Bits CKMODE[1:0]
of ADC_CFGR2
Bits CKMODE[1:0]
of ADC_CFGR2
/1,2,4,6,8,10,12
16,32,64,128,256
Bits PRESC[3:0]
of ADC_CCR

RM0490 Rev 6 297/1023
RM0490 Analog-to-digital converter (ADC)
345
Caution: For correct operation of the ADC analog block, the analog ADC clock (fADC) must have a
duty cycle ranging from 45% to 55%. This is granted when the incoming clock (PCLK or
ADC asynchronous clock) is divided by a factor of two or higher, using one of the scaler
blocks inside the ADC. If it is not the case, some additional rules must be followed:
• When CKMODE[1:0] = 11 (PCLK divided by one), the AHB and APB prescalers in the
RCC must be configured in bypass mode.
• When the analog ADC clock is derived from the HSE or LSE bypass clock, this bypass
clock must have a 45-to-55% duty cycle unless this clock is routed to the ADC through
the PLL.
[Table 70](../tables/table_70.md). Latency between trigger and start of conversion(1)
1. Refer to the device datasheet for the maximum ADC frequency (f ADC).
ADC clock source CKMODE[1:0] Latency between the trigger event and the start of conversion
SYSCLK, or HSIKER
clock(2)
2. Selected with ADCSEL bitfield of the RCC_CCIPR register.
00 Latency is not deterministic (jitter)
PCLK divided by 2 01 Latency is deterministic (no jitter) and equal to 3.25 fADC cycles
PCLK divided by 4 10 Latency is deterministic (no jitter) and equal to 3.125 fADC cycles
PCLK divided by 1 11 Latency is deterministic (no jitter) and equal to 3.5 fADC cycles

Analog-to-digital converter (ADC) RM0490
298/1023 RM0490 Rev 6
16.4.6 ADC connectivity
ADC inputs are connected to the external channels as well as internal sources as described
in [Figure 35](../figures/figure_35.md).
[Figure 35](../figures/figure_35.md). ADC connectivity
1. ADC_IN17 to ADC_IN22 are available only on STM32C031/51/71/91/92xx devices.
MSv68741V5
SAR
ADC1
ADC
ADC_IN2
ADC_IN3
ADC_IN4
ADC_IN5
ADC_IN6
VIN[1]
VIN[2]
STM32C0xx
VIN[0]
VIN[3]
VIN[4]
VIN[5]
VIN[6]
VIN[8]
VIN[9]
VIN[7]
VIN[10]
VIN[11]
VIN[12]
VIN[13]
VIN[14]
VIN[15]
VIN[16]
VIN[17]
VIN[18]
VDDA
ADC_IN7
VIN
VSSA
Channel selection
ADC_IN11
VREFINT
ADC_IN0
ADC_IN1
VSENSE
ADC_IN12
ADC_IN13
ADC_IN14
VDDA
VSSA
ADC_IN17(1)
ADC_IN18(1)
ADC_IN19(1)
ADC_IN20(1)
ADC_IN21(1)
ADC_IN22(1)
VIN[19]
VIN[20]
VIN[21]
VIN[22]
ADC_IN8

RM0490 Rev 6 299/1023
RM0490 Analog-to-digital converter (ADC)
345
16.4.7 Configuring the ADC
The software must write the ADCAL and ADEN bits in the ADC_CR register and configure
the ADC_CFGR1 and ADC_CFGR2 registers only when the ADC is disabled (ADEN must
be cleared).
The software must only write to the ADSTART and ADDIS bits in the ADC_CR register only
if the ADC is enabled and there is no pending request to disable the ADC (ADEN = 1 and
ADDIS = 0).
For all the other control bits in the ADC_IER, ADC_SMPR, ADC_CHSELR and ADC_CCR
registers, refer to the description of the corresponding control bit in Section 16.12: ADC
registers.
ADC_AWDTRx registers can be modified when conversion is ongoing.
The software must only write to the ADSTP bit in the ADC_CR register if the ADC is enabled
(and possibly converting) and there is no pending request to disable the ADC (ADSTART =
1 and ADDIS = 0).
Note: There is no hardware protection preventing software from making write operations forbidden
by the above rules. If such a forbidden write access occurs, the ADC may enter an
undefined state. To recover correct operation in this case, the ADC must be disabled (clear
ADEN = 0 and all the bits in the ADC_CR register).
16.4.8 Channel selection (CHS EL, SCANDIR, CHSELRMOD)
There are up to 23 multiplexed channels:
• Up to 19 analog inputs from GPIO pins (ADC_INx)
• 4 internal analog inputs (temperature sensor, internal reference voltage, analog supply
and analog ground)
It is possible to convert a single channel or a sequence of channels.
The sequence of the channels to be converted can be programmed in the ADC_CHSELR
channel selection register: each analog input channel has a dedicated selection bit
(CHSELx).
The ADC scan sequencer can be used in two different modes:
• Sequencer not fully configurable:
The order in which the channels are scanned is defined by the channel number
(CHSELRMOD bit must be cleared in ADC_CFGR1 register):
– Sequence length configured through CHSELx bits in ADC_CHSELR register
– Sequence direction: the channels are scanned in a forward direction (from the
lowest to the highest channel number) or backward direction (from the highest to
the lowest channel number) depending on the value of SCANDIR bit
(SCANDIR = 0: forward scan, SCANDIR = 1: backward scan)

Analog-to-digital converter (ADC) RM0490
300/1023 RM0490 Rev 6
– Any channel can belong to in these sequences
• Sequencer fully configurable
The CHSELRMOD bit is set in ADC_CFGR1 register.
– Sequencer length is up to 8 channels
– The order in which the channels are sc anned is independent from the channel
number. Any order can be configured through SQ1[3:0] to SQ8[3:0] bits in
ADC_CHSELR register.
– Only channel 0 to channel 14 can be selected in this sequence
– If the sequencer detects SQ x[3:0] = 0b1111, the following SQx[3:0] registers are
ignored.
– If no 0b1111 is programmed in SQx[3:0], the sequencer scans full eight channels.
After programming ADC CHSELR, SCANDIR and CHSELRMOD bits, it is mandatory to wait
for CCRDY flag before starting conversions. It indicates that the new channel setting has
been applied. If a new configuration is required, the CCRDY flag must be cleared prior to
starting the conversion.
The software is allowed to program the CHSEL, SCANDIR, CHSELRMOD bits only when
ADSTART bit is cleared (which ensures that no conversion is ongoing).
Temperature sensor, VREFINT and VDDA and VSSA internal channels
The temperature sensor is connected to channel ADC VIN[9].
The internal voltage reference VREFINT is connected to channel ADC VIN[10].
VDDA channel is connected to ADC VIN[15].
VSSA channel is connected to ADC VIN[16].
16.4.9 Programmable sampl ing time (SMPx[2:0])
Before starting a conversion, the ADC needs to establish a direct connection between the
voltage source to be measured and the embedded sampling capacitor of the ADC. This
sampling time must be enough for the input voltage source to charge the sample and hold
capacitor to the input voltage level.
Having a programmable sampling time allows the conversion speed to be trimmed
according to the input resistance of the input voltage source.
The ADC samples the input voltage for a number of ADC clock cycles that can be modified
using the SMP1[2:0] and SMP2[2:0] bits in the ADC_SMPR register.
Each channel can choose one out of two sampling times configured in SMP1[2:0] and
SMP2[2:0] bitfields, through SMPSELx bits in ADC_SMPR register.
The total conversion time is calculated as follows:
tCONV = Sampling time + 12.5 x ADC clock cycles
Example:
With fADC = 16 MHz and a sampling time of 1.5 ADC clock cycles:
tCONV = 1.5 + 12.5 = 14 ADC clock cycles = 0.875 µs
The ADC indicates the end of the sampling phase by setting the EOSMP flag.

RM0490 Rev 6 301/1023
RM0490 Analog-to-digital converter (ADC)
345
16.4.10 Single conversion mode (CONT  = 0)
In Single conversion mode, the ADC performs a single sequence of conversions, converting
all the channels once. This mode is selected when CONT = 0 in the ADC_CFGR1 register.
Conversion is started by either:
• Setting the ADSTART bit in the ADC_CR register
• Hardware trigger event
Inside the sequence, after each conversion is complete:
• The converted data are stored in the 16-bit ADC_DR register
• The EOC (end of conversion) flag is set
• An interrupt is generated if the EOCIE bit is set
After the sequence of conversions is complete:
• The EOS (end of sequence) flag is set
• An interrupt is generated if the EOSIE bit is set
Then the ADC stops until a new external trigger event occurs or the ADSTART bit is set
again.
Note: To convert a single channel, program a sequence with a length of 1.
16.4.11 Continuous conversion mode (CONT  = 1)
In continuous conversion mode, when a software or hardware trigger event occurs, the ADC
performs a sequence of conversions, converting all the channels once and then
automatically re-starts and continuously performs the same sequence of conversions. This
mode is selected when CONT = 1 in the ADC_CFGR1 register. Conversion is started by
either:
• Setting the ADSTART bit in the ADC_CR register
• Hardware trigger event
Inside the sequence, after each conversion is complete:
• The converted data are stored in the 16-bit ADC_DR register
• The EOC (end of conversion) flag is set
• An interrupt is generated if the EOCIE bit is set
After the sequence of conversions is complete:
• The EOS (end of sequence) flag is set
• An interrupt is generated if the EOSIE bit is set
Then, a new sequence restarts immediately and the ADC continuously repeats the
conversion sequence.
Note: To convert a single channel, program a sequence with a length of 1.
It is not possible to have both discontinuous mode and continuous mode enabled: it is
forbidden to set both bits DISCEN = 1 and CONT = 1.

Analog-to-digital converter (ADC) RM0490
302/1023 RM0490 Rev 6
16.4.12 Starting conversions (ADSTART)
Software starts ADC conversions by setting ADSTART = 1.
When ADSTART is set, the conversion:
• Starts immediately if EXTEN  =  00 (software trigger)
• At the next active edge of the selected hardware trigger if EXTEN ≠ 00
The ADSTART bit is also used to indicate whether an ADC operation is currently ongoing. It
is possible to re-configure the ADC while ADSTART = 0, indicating that the ADC is idle.
The ADSTART bit is cleared by hardware:
• In single mode with software trigger (CONT = 0, EXTEN = 00)
– At any end of conversion sequence (EOS  = 1)
• In discontinuous mode with software trigger (CONT = 0, DISCEN = 1, EXTEN = 00)
– At end of conversion (EOC  = 1)
• In all cases (CONT = x, EXTEN = XX)
– After execution of the ADSTP proc edure invoked by software (see
Section 16.4.14: Stopping an ongoing conversion (ADSTP) on page 304)
Note: In continuous mode (CONT = 1), the ADSTAR T bit is not cleared by hardware when the
EOS flag is set because the sequence is automatically relaunched.
When hardware trigger is selected in single mode (CONT = 0 and EXTEN =  01), ADSTART
is not cleared by hardware when the EOS flag is set (except if DMAEN = 1 and
DMACFG = 0 in which case ADSTART is cleared at end of the DMA transfer). This avoids
the need for software having to set the ADSTART bit again and ensures the next trigger
event is not missed.
After changing channel selection configuration (by programming ADC_CHSELR register or
changing CHSELRMOD or SCANDIR), it is mandatory to wait until CCRDY flag is asserted
before asserting ADSTART, otherwise the value written to ADSTART is ignored.

RM0490 Rev 6 303/1023
RM0490 Analog-to-digital converter (ADC)
345
16.4.13 Timings
The elapsed time between the start of a conversion and the end of conversion is the sum of
the configured sampling time plus the successive approximation time depending on data
resolution:
[Figure 36](../figures/figure_36.md). Analog-to-digital conversion time
1. t SMPL depends on SMP[2:0].
2. t SAR depends on RES[2:0].
3. The synchronization between the analog clock and the di gital clock domains is not described in the above
figure.
[Figure 37](../figures/figure_37.md). ADC conversion timings
1. EXTEN  = 00 or EXTEN ≠ 00.
2. Trigger latency (refer to datasheet for more details).
3. ADC_DR register write latency (refer to datasheet for more details).
tCONV = tSMPL + tSAR = [1.5 |min + 12.5 |12bit] x 1/fADC
tCONV = tSMPL + tSAR = 42.9 ns |min + 357.1 ns |12bit = 0.400 µs |min (for fADC = 35 MHz)
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
tSMPL(1) tSAR(2)
Set by
HW
Cleared
by SW
Set by
HW
Cleared by
HW/SW
MSv33174V2
Ready S0 Conversion 0
tLATR (2)ADSTART(1)
ADC state
ADC_DR
S1 Conversion 1 S2 Conversion 2 S3 Conversion 3
WLATENCY (3) WLATENCY (3) WLATENCY (3)
Data 1Data 0 Data 2

Analog-to-digital converter (ADC) RM0490
304/1023 RM0490 Rev 6
16.4.14 Stopping an ongoing conversion (ADSTP)
The software can decide to stop any ongoing conversions by setting ADSTP = 1 in the
ADC_CR register.
This resets the ADC operation and the ADC is idle, ready for a new operation.
When the ADSTP bit is set by software, any ongoing conversion is aborted and the result is
discarded (ADC_DR register is not updated with the current conversion).
The scan sequence is also aborted and reset (meaning that restarting the ADC would re-
start a new sequence).
Once this procedure is complete, the ADSTP and ADSTART bits are both cleared by
hardware and the software must wait until ADSTART=0 before starting new conversions.
[Figure 38](../figures/figure_38.md). Stopping an ongoing conversion
16.5 Conversion on external trigge r and trigger polarity (EXTSEL,
EXTEN)
A conversion or a sequence of conversion can be triggered either by software or by an
external event (for example timer capture). If the EXTEN[1:0] control bits are not equal to
“0b00”, then external events are able to trigger a conversion with the selected polarity. The
trigger selection is effective once software has set bit ADSTART = 1.
Any hardware triggers which occur while a conversion is ongoing are ignored.
If bit ADSTART = 0, any hardware triggers which occur are ignored.
[Table 71](../tables/table_71.md) provides the correspondence between the EXTEN[1:0] values and the trigger
polarity.
MSv30337V2
DATA N-1
ADC state
ADSTART
set by
SW
RDY SAMPLING CH(N)
ADC_DR
CONVERTING CH(N) RDY
ADSTOP cleared by HWset by SW
cleared by HW
[Table 71](../tables/table_71.md). Configuring the trigger polarity
Source EXTEN[1:0]
Trigger detection disabled 00
Detection on rising edge 01
Detection on falling edge 10
Detection on both rising and falling edges 11

RM0490 Rev 6 305/1023
RM0490 Analog-to-digital converter (ADC)
345
Note: The polarity of the external trigger can be changed only when the ADC is not converting
(ADSTART =  0).
The EXTSEL[2:0] control bits are used to select which of 8 possible events can trigger
conversions.
Refer to [Table 69](../tables/table_69.md): External triggers in Section 16.4.1: ADC pins and internal signals for the
list of all the external triggers that can be used for regular conversion.
The software source trigger events can be generated by setting the ADSTART bit in the
ADC_CR register.
Note: The trigger selection can be changed only wh en the ADC is not converting (ADSTART =  0).
16.5.1 Discontinuous mode (DISCEN)
This mode is enabled by setting the DISCEN bit in the ADC_CFGR1 register.
In this mode (DISCEN = 1), a hardware or software trigger event is required to start each
conversion defined in the sequence. On the contrary, if DISCEN = 0, a single hardware or
software trigger event successively starts all the conversions defined in the sequence.
Example:
• DISCEN = 1, channels to be converted = 0, 3, 7, 10
– 1st trigger: channel 0 is converted and an EOC event is generated
– 2nd trigger: channel 3 is conver ted and an EOC event is generated
– 3rd trigger: channel 7 is conver ted and an EOC event is generated
– 4th trigger: channel 10 is converted and both EOC and EOS events are
generated.
– 5th trigger: channel 0 is conv erted an EOC event is generated
– 6th trigger: channel 3 is conver ted and an EOC event is generated
–. . .
• DISCEN = 0, channels to be converted = 0, 3, 7, 10
– 1st trigger: the complete sequence is conver ted: channel 0, then 3, 7 and 10. Each
conversion generates an EOC event and the last one also generates an EOS
event.
– Any subsequent trigger events restarts the complete sequence.
Note: It is not possible to have  both discontinuous mode and continuous mode enabled: it is
forbidden to set both bits DISCEN = 1 and CONT = 1.
16.5.2 Programmable resolution (R ES) - Fast conversion mode
It is possible to obtain faster conversion times (tSAR) by reducing the ADC resolution.
The resolution can be configured to be either 12, 10, 8, or 6 bits by programming the
RES[1:0] bits in the ADC_CFGR1 register. Lower resolution allows faster conversion times
for applications where high data precision is not required.
Note: The RES[1:0] bit must only be changed when the ADEN bit is reset.
The result of the conversion is always 12 bits wide and any unused LSB bits are read as
zeros.

Analog-to-digital converter (ADC) RM0490
306/1023 RM0490 Rev 6
Lower resolution reduces the conversion time needed for the successive approximation
steps as shown in [Table 72](../tables/table_72.md).
16.5.3 End of conversion, end of  sampling phase (EOC, EOSMP flags)
The ADC indicates each end of conversion (EOC) event.
The ADC sets the EOC flag in the ADC_ISR register as soon as a new conversion data
result is available in the ADC_DR register. An interrupt can be generated if the EOCIE bit is
set in the ADC_IER register. The EOC flag is cleared by software either by writing 1 to it, or
by reading the ADC_DR register.
The ADC also indicates the end of sampling phase by setting the EOSMP flag in the
ADC_ISR register. The EOSMP flag is cleared by software by writing1 to it. An interrupt can
be generated if the EOSMPIE bit is set in the ADC_IER register.
The aim of this interrupt is to allow the processing to be synchronized with the conversions.
Typically, an analog multiplexer can be accessed in hidden time during the conversion
phase, so that the multiplexer is positioned when the next sampling starts.
Note: As there is only a very sh ort time left between the end of the sampling and the end of the
conversion, it is recommenced to use polling or a WFE instruction rather than an interrupt
and a WFI instruction.
16.5.4 End of conversion  sequence (EOS flag)
The ADC notifies the application of each end of sequence (EOS) event.
The ADC sets the EOS flag in the ADC_ISR register as soon as the last data result of a
conversion sequence is available in the ADC_DR register. An interrupt can be generated if
the EOSIE bit is set in the ADC_IER register. The EOS flag is cleared by software by writing
1 to it.
[Table 72](../tables/table_72.md). tSAR timings depending on resolution
RES[1:0]
(bits)
tSAR
(fADC cycles)
tSAR at
fADC = 35 MHz
(ns)
tSMPL(min)
(fADC cycles)
tCONV with min. tSMPL
(fADC cycles)
tCONV(min) at
fADC = 35 MHz
(ns)
12 12.5 357 1.5 14 400
10 10.5  300 1.5 12 343
8 8.5 243 1.5 10 286
6 6.5 186 1.5 8 229

RM0490 Rev 6 307/1023
RM0490 Analog-to-digital converter (ADC)
345
16.5.5 Example timing diagrams  (single/continuous modes
hardware/software triggers)
[Figure 39](../figures/figure_39.md). Single conversions of a sequence, software trigger
1. EXTEN = 00, CONT = 0
2. CHSEL = 0x20601, WAIT = 0, AUTOFF = 0
[Figure 40](../figures/figure_40.md). Continuous conversion of a sequence, software trigger
1. EXTEN = 00, CONT = 1,
2. CHSEL = 0x20601, WAIT = 0, AUTOFF = 0
MSv30338V3
RDY
EOC
SCANDIR
CH9 CH17 CH9
ADC_DR D0 D10 D17 D10 D9 D0
ADC state(2)
ADSTART(1)
EOS
D9 D17
RDYCH0CH10RDY CH17CH10CH0
by S/W by H/W
MSv30339V2
ADSTP
CH9 CH17 STP
D0 D10
CH9
D0 D9
CH10
D17
EOC
SCANDIR
ADC_DR
ADC state(2)
ADSTART(1)
EOS
RDY CH17CH10CH0
by S/W by H/W
RDY CH0 CH10
D9 D17

Analog-to-digital converter (ADC) RM0490
308/1023 RM0490 Rev 6
[Figure 41](../figures/figure_41.md). Single conversions of a sequence, hardware trigger
1. EXTSEL = TRGx (over-frequency), EXTEN = 01 (rising edge), CONT = 0
2. CHSEL = 0xF, SCANDIR = 0, WAIT = 0, AUTOFF = 0
[Figure 42](../figures/figure_42.md). Continuous conversions of a sequence, hardware trigger
1. EXTSEL = TRGx, EXTEN = 10 (falling edge), CONT = 1
2. CHSEL = 0xF, SCANDIR = 0, WAIT = 0, AUTOFF = 0
MSv30340V2
CH1 CH1 CH3 CH0 CH2
D0 D1 D2 D1 D2 D3 D3
CH2
EOC
ADC_DR
ADC state(2)
ADSTART(1)
EOS
RDYRDY CH0 CH3
TRGx(1)
RDY
D0
by H/W
ignored
by S/W
triggered
MSv30341V2
CH1 CH2
D0 D1 D2
CH0 CH2 CH0
D3 D0 D1 D2 D3
STOP
ADC_DR
ADSTP
by H/W
CH1 CH3
ignored
EOC
ADC state(2)
ADSTART(1)
EOS
RDYCH0 CH3
TRGx(1)
RDY
by S/W
triggered

RM0490 Rev 6 309/1023
RM0490 Analog-to-digital converter (ADC)
345
16.5.6 Low frequency trigger mode
Once the ADC is enabled or the last ADC conversion is complete, the ADC is ready to start
a new conversion. The ADC needs to be started at a predefined time (tidle) otherwise ADC
converted data might be corrupted due to the transistor leakage (refer to the device
datasheet for the maximum value of tidle).
If the application has to support a time longer than the maximum tidle value (between one
trigger to another for single conversion mode or between the ADC enable and the first ADC
conversion), then the ADC internal state needs to be rearmed. This mechanism can be
enabled by setting LFTRIG bit to 1 in ADC_CFGR2 register. By setting this bit, any trigger
(software or hardware) sends a rearm command to ADC. The conversion starts after a one
ADC clock cycle delay compared to LFTRIG cleared.
It is not necessary to use this mode when AUTOFF bit is set. For Wait mode, only the first
trigger generates an internal rearm command.
16.6 Data management
16.6.1 Data register and data  alignment (ADC_DR, ALIGN)
At the end of each conversion (when an EOC event occurs), the result of the converted data
is stored in the ADC_DR data register which is 16-bit wide.
The format of the ADC_DR depends on the configured data alignment and resolution.
The ALIGN bit in the ADC_CFGR1 register selects the alignment of the data stored after
conversion. Data can be right-aligned (ALIGN = 0) or left-aligned (ALIGN = 1) as shown in
[Figure 43](../figures/figure_43.md).
[Figure 43](../figures/figure_43.md). Data alignment and resolution (oversampling disabled: OVSE = 0)
16.6.2 ADC overrun (OVR, OVRMOD)
The overrun flag (OVR) indicates a data overrun event, when the converted data was not
read in time by the CPU or the DMA, before the data from a new conversion is available.
The OVR flag is set in the ADC_ISR register if the EOC flag is still at ‘1’ at the time when a
new conversion completes. An interrupt can be generated if the OVRIE bit is set in the
ADC_IER register.
0x0
0x00
0x00
0x00
DR[11:0]
DR[9:0]
DR[7:0]
0x00
DR[11:0]
DR[9:0]
DR[7:0]
DR[5:0]
DR[5:0]
0x0
0x00
0x00
0x0
ALIGN RES
0 0x0
1
0x1
0x2
0x3
0x0
0x1
0x2
0x3
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
MS30342V1

Analog-to-digital converter (ADC) RM0490
310/1023 RM0490 Rev 6
When an overrun condition occurs, the ADC keeps operating and can continue to convert
unless the software decides to stop and reset the sequence by setting the ADSTP bit in the
ADC_CR register.
The OVR flag is cleared by software by writing 1 to it.
It is possible to configure if the data is preserved or overwritten when an overrun event
occurs by programming the OVRMOD bit in the ADC_CFGR1 register:
• OVRMOD = 0
– An overrun event preserves the data regist er from being overwritten: the old data
is maintained and the new conversion is discarded. If OVR remains at 1, further
conversions can be performed but the resulting data is discarded.
• OVRMOD = 1
– The data register is overwritten with the last conversion result and the previous
unread data is lost. If OVR remains at 1, further conversions can be performed
and the ADC_DR register always contains the data from the latest conversion.
[Figure 44](../figures/figure_44.md). Example of overrun (OVR)
MSv30343V3
RDY
EOC
EOS
CH0 CH1 CH2 CH0
D0 D1 D2
CH1 CH2 CH0 STOP
D0
OVR
RDY
D0 D1 D2 D0 D1 D2
ADC_DR read
access
OVERRUN
by S/W by H/W
triggered
ADC_DR
(OVRMOD=0)
ADSTP
ADC state(2)
ADSTART(1)
TRGx(1)
ADC_DR
(OVRMOD=1)

RM0490 Rev 6 311/1023
RM0490 Analog-to-digital converter (ADC)
345
16.6.3 Managing a sequence of data  converted without using the DMA
If the conversions are slow enough, the conversion sequence can be handled by software.
In this case the software must use the EOC flag and its associated interrupt to handle each
data result. Each time a conversion is complete, the EOC bit is set in the ADC_ISR register
and the ADC_DR register can be read. The OVRMOD bit in the ADC_CFGR1 register
should be configured to 0 to manage overrun events as an error.
16.6.4 Managing converted data with out using the DMA without overrun
It may be useful to let the ADC convert one or more channels without reading the data after
each conversion. In this case, the OVRMOD bit must be configured at 1 and the OVR flag
should be ignored by the software. When OVRMOD = 1, an overrun event does not prevent
the ADC from continuing to convert and the ADC_DR register always contains the latest
conversion data.
16.6.5 Managing converted data using the DMA
Since all converted channel values are stored in a single data register, it is efficient to use
DMA when converting more than one channel. This avoids losing the conversion data
results stored in the ADC_DR register.
When DMA mode is enabled (DMAEN bit set in the ADC_CFGR1 register), a DMA request
is generated after the conversion of each channel. This allows the transfer of the converted
data from the ADC_DR register to the destination location selected by the software.
Note: The DMAEN bit in the ADC_CFGR1 register must be set after the ADC calibration phase.
Despite this, if an overrun occurs (OVR = 1) because the DMA could not serve the DMA
transfer request in time, the ADC stops generating DMA requests and the data
corresponding to the new conversion is not transferred by the DMA. Which means that all
the data transferred to the RAM can be considered as valid.
Depending on the configuration of OVRMOD bit, the data is either preserved or overwritten
(refer to Section 16.6.2: ADC overrun (OVR, OVRMOD) on page 309).
The DMA transfer requests are blocked until the software clears the OVR bit.
Two different DMA modes are proposed depending on the application use and are
configured with bit DMACFG in the ADC_CFGR1 register:
• DMA one shot mode (DMACFG = 0).
This mode should be selected when the DMA is programmed to transfer a fixed
number of data words.
• DMA circular mode (DMACFG = 1)
This mode should be selected when programming the DMA in circular mode or double
buffer mode.
DMA one shot mode (DMACFG = 0)
In this mode, the ADC generates a DMA transfer request each time a new conversion data
word is available and stops generating DMA requests once the DMA has reached the last
DMA transfer (when a transfer complete interrupt occurs, see Section 11: Direct memory
access controller (DMA) on page 223) even if a conversion has been started again.

Analog-to-digital converter (ADC) RM0490
312/1023 RM0490 Rev 6
When the DMA transfer is complete (all the transfers configured in the DMA controller have
been done):
• The content of the ADC data register is frozen.
• Any ongoing conversion is aborted and its partial result discarded
• No new DMA request is issued to the DMA controller. This avoids generating an
overrun error if there are still conversions which are started.
• The scan sequence is stopped and reset
• The DMA is stopped
DMA circular mode (DMACFG = 1)
In this mode, the ADC generates a DMA transfer request each time a new conversion data
word is available in the data register, even if the DMA has reached the last DMA transfer.
This allows the DMA to be configured in circular mode to handle a continuous analog input
data stream.
16.7 Low-power features
16.7.1 Wait mode conversion
Wait mode conversion can be used to simplify the software as well as optimizing the
performance of applications clocked at low frequency where there might be a risk of ADC
overrun occurring.
When the WAIT bit is set in the ADC_CFGR1 register, a new conversion can start only if the
previous data has been treated, once the ADC_DR register has been read or if the EOC bit
has been cleared.
This is a way to automatically adapt the speed of the ADC to the speed of the system that
reads the data.
Note: Any hardware triggers which occur while a conversion is ongoing or during the wait time
preceding the read access are ignored.

RM0490 Rev 6 313/1023
RM0490 Analog-to-digital converter (ADC)
345
[Figure 45](../figures/figure_45.md). Wait mode conversion (continuous mode, software trigger)
1. EXTEN = 00, CONT = 1
2. CHSEL = 0x3, SCANDIR = 0, WAIT = 1, AUTOFF = 0
16.7.2 Auto-off mode (AUTOFF)
The ADC has an automatic power management feature which is called auto-off mode, and
is enabled by setting AUTOFF = 1 in the ADC_CFGR1 register.
When AUTOFF = 1, the ADC is always powered off when not converting and automatically
wakes-up when a conversion is started (by software or hardware trigger). A startup-time is
automatically inserted between the trigger event which starts the conversion and the
sampling time of the ADC. The ADC is then automatically disabled once the sequence of
conversions is complete.
Auto-off mode can cause a dramatic reduction in the power consumption of applications
which need relatively few conversions or when conversion requests are timed far enough
apart (for example with a low frequency hardware trigger) to justify the extra power and
extra time used for switching the ADC on and off.
MSv30344V2
ADC_DR
by S/W
ADSTP
EOC
ADC state
ADSTART
EOS
CH1 CH2 STOP CH1CH3 RDYDLYRDY DLY
ADC_DR Read access
DLY DLY
D1 D3 D1D2
by H/W

Analog-to-digital converter (ADC) RM0490
314/1023 RM0490 Rev 6
Auto-off mode can be combined with the wait mode conversion (WAIT = 1) for applications
clocked at low frequency. This combination can provide significant power savings if the ADC
is automatically powered-off during the wait phase and restarted as soon as the ADC_DR
register is read by the application (see [Figure 47](../figures/figure_47.md): Behavior with WAIT = 1, AUTOFF = 1).
[Figure 46](../figures/figure_46.md). Behavior with WAIT = 0, AUTOFF = 1
1. EXTSEL = TRGx, EXTEN = 01 (rising edge), CONT = x, AD START = 1, CHSEL = 0xF, SCANDIR = 0, WAIT = 1,
AUTOFF = 1
[Figure 47](../figures/figure_47.md). Behavior with WAIT = 1, AUTOFF = 1
1. EXTSEL = TRGx, EXTEN = 01 (rising edge), CONT = x, AD START = 1, CHSEL = 0xF, SCANDIR = 0, WAIT = 1,
AUTOFF = 1
MSv30345V2
TRGx
EOC
EOS
ADC_DR Read
access
ADC state
ADC_DR
by H/Wby S/W
triggered
D1 D3 D2 D4
RDY CH1 CH2Startup CH4CH3 OFF Startup
MSv30346V2
D1 D2 D3 D4
TRGx
EOC
EOS
ADC_DR Read
access
ADC state
ADC_DR
RDY CH1 OFFStartup CH2
OFFStartup
DLY
Startup CH3 OFF
DLY DLY
Startup CH1
OFFCH2
DLY
by H/Wby S/W
triggered

RM0490 Rev 6 315/1023
RM0490 Analog-to-digital converter (ADC)
345
16.8 Analog window watchdogs
The three AWD analog watchdogs monitor whether some channels remain within a
configured voltage range (window).
16.8.1 Description of  analog watchdog 1
AWD1 analog watchdog is enabled by setting the AWD1EN bit in the ADC_CFGR1 register.
It is used to monitor that either one selected channel or all enabled channels (see [Table 74](../tables/table_74.md):
Analog watchdog 1 channel selection) remain within a configured voltage range (window) as
shown in [Figure 48](../figures/figure_48.md).
The AWD1 analog watchdog status bit is set if the analog voltage converted by the ADC is
below a lower threshold or above a higher threshold. These thresholds are programmed in
HT1[11:0] and LT1[11:0] bits of ADC_AWD1TR register. An interrupt can be enabled by
setting the AWD1IE bit in the ADC_IER register.
The AWD1 flag is cleared by software by programing it to 1.
When converting data with a resolution of less than 12-bit (according to bits DRES[1:0]), the
LSB of the programmed thresholds must be kept cleared because the internal comparison
is always performed on the full 12-bit raw converted data (left aligned).
[Table 73](../tables/table_73.md) describes how the comparison is performed for all the possible resolutions.
[Table 74](../tables/table_74.md) shows how to configure the AWD1SGL and AWD1EN bits in the ADC_CFGR1
register to enable the analog watchdog on one or more channels.
[Figure 48](../figures/figure_48.md). Analog watchdog guarded area
[Table 73](../tables/table_73.md). Analog watchdog comparison
Resolution
bits
RES[1:0]
Analog Watchdog comparison between:
CommentsRaw converted
data, left aligned(1) Thresholds
00: 12-bit DATA[11:0] LTx[11:0] and HTx[11:0] -
01: 10-bit DATA[11:2],00 LTx[11:0] and HTx[11:0] The us er must configure LTx[1:0] and HTx[1:0] to “00”
10: 8-bit DATA[11:4],0000 LTx[11:0] and HTx[11:0] The user must configure LTx[3:0] and HTx[3:0] to “0000”
11: 6-bit DATA[11:6],000000 LTx[11:0] and HTx[11:0] The user must configure LTx[5:0] and HTx[5:0] to “000000”
1. The watchdog comparison is performed on the raw co nverted data before any alignment calculation.
MS45396V1
Analog voltage
Higher threshold
Lower threshold
Guarded area
HTx
LTx

Analog-to-digital converter (ADC) RM0490
316/1023 RM0490 Rev 6
16.8.2 Description of an alog watchdog 2 and 3
The second and third analog watchdogs are more flexible and can guard several selected
channels by programming the AWDxCHy in ADC_AWDxCR (x = 2, 3).
The corresponding watchdog is enabled when any AWDxCHy bit (x = 2,3) is set in
ADC_AWDxCR register.
When converting data with a resolution of less than 12 bits (configured through DRES[1:0]
bits), the LSB of the programmed thresholds must be kept cleared because the internal
comparison is always performed on the full 12-bit raw converted data (left aligned).
[Table 73](../tables/table_73.md) describes how the comparison is performed for all the possible resolutions.
The AWD2/3 analog watchdog status bit is set if the analog voltage converted by the ADC is
below a low threshold or above a high threshold. These thresholds are programmed in
HTx[11:0] and LTx[11:0] of ADC_AWDxTR registers (x = 2 or 3). An interrupt can be
enabled by setting the AWDxIE bit in the ADC_IER register.
The AWD2 and ADW3 flags are cleared by software by programming them to 1.
16.8.3 ADC_AWDx_OUT output signal generation
Each analog watchdog is associated to an internal hardware signal, ADC_AWDx_OUT (x
being the watchdog number) that is directly connected to the ETR input (external trigger) of
some on-chip timers (refer to the timers section for details on how to select the
ADC_AWDx_OUT signal as ETR).
ADC_AWDx_OUT is activated when the associated analog watchdog is enabled:
• ADC_AWDx_OUT is set when a guarded conversion is outside the programmed
thresholds.
• ADC_AWDx_OUT is reset after the end of the next guarded conversion which is inside
the programmed thresholds. It remains at 1 if the next guarded conversions are still
outside the programmed thresholds.
• ADC_AWDx_OUT is also reset when disabling the ADC (when setting ADDIS to 1).
Note that stopping conversions (ADSTP set), might clear the ADC_AWDx_OUT state.
• ADC_AWDx_OUT state does not change when the ADC converts the none-guarded
channel (see [Figure 51](../figures/figure_51.md))
AWDx flag is set by hardware and reset by software: AWDx flag has no influence on the
generation of ADC_AWDx_OUT (as an example, ADC_AWDx_OUT can toggle while AWDx
flag remains at 1 if the software has not cleared the flag).
The ADC_AWDx_OUT signal is generated by the fADC clock domain. This signal can be
generated even the APB clock is stopped.
[Table 74](../tables/table_74.md). Analog watchdog 1 channel selection
Channels guarded by the analog watchdog AWD1SGL bit AWD1EN bit
None x 0
All channels 0 1
Single(1) channel
1. Selected by the AWD1CH[4:0] bits
11

RM0490 Rev 6 317/1023
RM0490 Analog-to-digital converter (ADC)
345
The AWD comparison is performed at the end of each ADC conversion. The
ADC_AWDx_OUT rising edge and falling edge occurs two fADC clock cycles after the
comparison.
As ADC_AWDx_OUT is generated by the fADC clock domain and AWD flag is generated by
the APB clock domain, the rising edges of these signals are not synchronized.
[Figure 49](../figures/figure_49.md). ADC_AWDx_OUT signal generation
[Figure 50](../figures/figure_50.md). ADC_AWDx_OUT signal generation (AWDx flag not cleared by software)
MSv45362V1
EOC FLAG
ADC STATE RDY
AWDx FLAG
Conversion1
outside
ADC_AWDx_OUT
inside
Cleared
by SW
Conversion2 Conversion3 Conversion4 Conversion5 Conversion6 Conversion7
outsideinside outside outside inside
- Converted channels: 1,2,3,4,5,6,7
- Guarded converted channels: 1,2,3,4,5,6,7
Cleared
by SW
Cleared
by SW
Cleared
by SW
MSv45363V1
EOC FLAG
ADC STATE RDY
AWDx FLAG
Conversion1
outside
ADC_AWDx_OUT
inside
not cleared by SW
Conversion2 Conversion3 Conversion4 Conversion5 Conversion6 Conversion7
outsideinside outside outside inside
- Converted channels: 1,2,3,4,5,6,7
- Guarded converted channels: 1,2,3,4,5,6,7

Analog-to-digital converter (ADC) RM0490
318/1023 RM0490 Rev 6
[Figure 51](../figures/figure_51.md). ADC_AWDx_OUT signal generation (on a single channel)
16.8.4 Analog watchdog threshold control
LTx[11:0] and HTx[11:0] can be changed during an analog-to-digital conversion (that is
between the start of the conversion and the end of conversion of the ADC internal state). If
HTx and LTx bits are programmed during the ADC guarded channel conversion, the
watchdog function is masked for this conversion. This mask is cleared when starting a new
conversion, and the resulting new AWD threshold is applied starting the next ADC
conversion result. AWD comparison is performed at each end of conversion. If the current
ADC data are out of the new threshold interval, this does not generated any interrupt or an
ADC_AWDx_OUT signal. The Interrupt and the ADC_AWDx_OUT generation only occurs
at the end of the ADC conversion that started after the threshold update. If
ADC_AWDx_OUT is already asserted, programming the new threshold does not deassert
the ADC_AWDx_OUT signal.
[Figure 52](../figures/figure_52.md). Analog watchdog threshold update
MSv45364V2
EOC FLAG
ADC STATE
AWDx FLAG
Conversion1
outside
ADC_AWDx_OUT
Cleared
by SW
Conversion2 Conversion1 Conversion2 Conversion1 Conversion2 Conversion1
inside outside outside
Conversion2
EOS FLAG
Cleared
by SW
- Converted channels: 1 and 2
- Only channel 1 is guarded
MSv45365V1
ADC state Conversion Conversion
LTx, HTx XXXX
Comparison Active
XXXY
Masked
Threshold updated
Conversion
Active
XXXZ
Conversion

RM0490 Rev 6 319/1023
RM0490 Analog-to-digital converter (ADC)
345
16.9 Oversampler
The oversampling unit performs data preprocessing to offload the CPU. It can handle
multiple conversions and average them into a single data with increased data width, up to
16-bit.
It provides a result with the following form, where N and M can be adjusted:
It allows the following functions to be performed by hardware: averaging, data rate
reduction, SNR improvement, basic filtering.
The oversampling ratio N is defined using the OVSR[2:0] bits in the ADC_CFGR2 register. It
can range from 2x to 256x. The division coefficient M consists of a right bit shift up to 8 bits.
It is configured through the OVSS[3:0] bits in the ADC_CFGR2 register.
The summation unit can yield a result up to 20 bits (256 x 12-bit), which is first shifted right.
The upper bits of the result are then truncated, keeping only the 16 least significant bits
rounded to the nearest value using the least significant bits left apart by the shifting, before
being finally transferred into the ADC_DR data register.
Note: If the intermediate result after the shifting exceeds 16 bits, the upper bits of the result are
simply truncated.
[Figure 53](../figures/figure_53.md). 20-bit to 16-bit result truncation
[Figure 54](../figures/figure_54.md) gives a numerical example of the processing, from a raw 20-bit accumulated data
to the final 16-bit result.
[Figure 54](../figures/figure_54.md). Numerical example with 5-bit shift and rounding
Result 1M----- Conversion t n()
n0=
nN 1 –=
∑×=
037111519
Raw 20-bit data
Truncation
and rounding
Shifting
015
MS31928V2
0
37111519
Raw 20-bit data:
BF
15
B737 D
1D
MS31929V1
Final result after 5-bits shift
and rounding to nearest

Analog-to-digital converter (ADC) RM0490
320/1023 RM0490 Rev 6
[Table 75](../tables/table_75.md) gives the data format for the various N and M combination, for a raw conversion
data equal to 0xFFF.
The conversion timings in oversampled mode do not change compared to standard
conversion mode: the sample time is maintained equal during the whole oversampling
sequence. New data are provided every N conversion, with an equivalent delay equal to N x
tCONV = N x (tSMPL + tSAR). The flags features are raised as following:
• the end of the sampling phase (EOSMP) is set after each sampling phase
• the end of conversion (EOC) occurs once every N conversions, when the oversampled
result is available
• the end of sequence (EOCSEQ) occurs once the sequence of oversampled data is
completed (i.e. after N x sequence length conversions total)
16.9.1 ADC operating modes supported when oversampling
In oversampling mode, most of the ADC operating modes are available:
• Single or continuous mode conversions, forward or backward scanned sequences
• ADC conversions start either by software or with triggers
• ADC stop during a conversion (abort)
• Data read via CPU or DMA with overrun detection
• Low-power modes (WAIT, AUTOFF)
• Programmable resolution: in this case, the reduced conversion values (as per RES[1:0]
bits in ADC_CFGR1 register) are accumulated, truncated, rounded and shifted in the
same way as 12-bit conversions are
Note: The alignment mode is not available when working with oversampled data. The ALIGN bit in
ADC_CFGR1 is ignored and the data are always provided right-aligned.
[Table 75](../tables/table_75.md). Maximum output results vs N and M. Grayed values indicates truncation
Oversa
mpling
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
2x 0x1FFE 0x1FFE 0x0FFF 0x0800 0x0400 0x0200 0x0100 0x0080 0x0040 0x0020
4x 0x3FFC 0x3FFC 0x1FFE 0x0FFF 0x0800 0x0400 0x0200 0x0100 0x0080 0x0040
8x 0x7FF8 0x7FF8 0x3FFC 0x1FFE 0x0FFF 0x0800 0x0400 0x0200 0x0100 0x0080
16x 0xFFF0 0xFFF0 0x7FF8 0x3FFC 0x1FFE 0x0FFF 0x0800 0x0400 0x0200 0x0100
32x 0x1FFE0 0xFFE0 0xFFF0 0x7FF8 0x3FFC 0x1F FE 0x0FFF 0x0800 0x0400 0x0200
64x 0x3FFC0 0xFFC0 0xFFE0 0xFFF0 0x7FF8 0x3FFC 0x1FFE 0x0FFF 0x0800 0x0400
128x 0x7FF80 0xFF80 0xFFC0 0xFFE0 0xFFF0 0x7FF8 0x3FFC 0x1FFE 0x0FFF 0x0800
256x 0xFFF00 0xFF00 0xFF80 0xFFC0 0xFFE0 0xFFF0 0x7FF8 0x3FFC 0x1FFE 0x0FFF

RM0490 Rev 6 321/1023
RM0490 Analog-to-digital converter (ADC)
345
16.9.2 Analog watchdog
The analog watchdog functionality is available, with the following differences:
• the RES[1:0] bits are ignored, comparison is always done on using the full 12-bits
values HTx[11:0] and LTx[11:0]
• the comparison is performed on the most significant 12 bits of the 16 bits oversampled
results ADC_DR[15:4]
Note: Care must be taken when using high shifting values. This reduces the comparison range.
For instance, if the oversampled result is shifted by 4 bits thus yielding a 12-bit data right-
aligned, the affective analog watchdog comparison can only be performed on 8 bits. The
comparison is done between ADC_DR[11:4] and HTx[7:0] / LTx[[7:0], and HTx[11:8] /
LTx[11:8] must be kept reset.
16.9.3 Triggered mode
The averager can also be used for basic filtering purposes. Although not a very efficient filter
(slow roll-off and limited stop band attenuation), it can be used as a notch filter to reject
constant parasitic frequencies (typically coming from the mains or from a switched mode
power supply). For this purpose, a specific discontinuous mode can be enabled with TOVS
bit in ADC_CFGR2, to be able to have an oversampling frequency defined by a user and
independent from the conversion time itself.
[Figure 55](../figures/figure_55.md) below shows how conversions are started in response to triggers in discontinuous
mode.
If the TOVS bit is set, the content of the DISCEN bit is ignored and considered as 1.
[Figure 55](../figures/figure_55.md). Triggered oversampling mode (TOVS bit = 1)
16.10 Temperature sensor an d internal reference voltage
The temperature sensor can be used to measure the junction temperature (TJ) of the
device. The temperature sensor is internally connected to the ADC VIN[9] input channel
which is used to convert the sensor’s output voltage to a digital value. The sampling time for
the temperature sensor analog pin must be greater than the minimum TS_temp value
specified in the datasheet. When not in use, the sensor can be put in power down mode.
MS33700V1
Ch(N)
0
Ch(N)
1
Ch(N)
2
Ch(N)
3
Trigger Trigger
CONT = 0
(DISCEN = 1)*
TOVS = 0
(DISCEN = 1)*: DISCEN bit is forced to 1 by software when TOVS bit is set
EOC flag set
EOC flag set
CONT = 0
(DISCEN = 1)*
TOVS = 1
Trigger
Ch(N)
0
Ch(N)
1
Ch(N)
2
Ch(N)
3
Trigger
Ch(N)
2
Trigger
Ch(N)
3
Trigger
Ch(N)
2
Trigger
Ch(N)
0
Trigger
Ch(N)
1
Trigger
Ch(N)
1
Ch(N)
0

Analog-to-digital converter (ADC) RM0490
322/1023 RM0490 Rev 6
The internal voltage reference (VREFINT) provides a stable (bandgap) voltage output for the
ADC. VREFINT is internally connected to the ADC VIN[10] input channel. The precise voltage
of VREFINT is individually measured for each part by ST during production test and stored in
the system memory area.
[Figure 56](../figures/figure_56.md) shows the block diagram of connections between the temperature sensor, the
internal voltage reference and the ADC.
The TSEN bit must be set to enable the conversion of ADC VIN[9] (temperature sensor) and
the VREFEN bit must be set to enable the conversion of ADC VIN[10] (VREFINT).
The temperature sensor output voltage changes linearly with temperature. The offset of this
line varies from chip to chip due to process variation (up to 45 °C from one chip to another).
The uncalibrated internal temperature sensor is more suited for applications that detect
temperature variations instead of absolute temperatures. To improve the accuracy of the
temperature sensor measurement, calibration values are stored in system memory for each
device by ST during production.
During the manufacturing process, the calibration data of the temperature sensor and the
internal voltage reference are stored in the system memory area. The user application can
then read them and use them to improve the accuracy of the temperature sensor or the
internal reference. Refer to the datasheet for additional information.
Note: Before entering any Stop mode, the temperat ure sensor and the internal reference voltage
must be disabled by clearing TSEN and VREFEN, respectively.
Main features
• Linearity: ±2 °C max, precision depending on calibration
[Figure 56](../figures/figure_56.md). Temperature sensor and VREFINT channel block diagram
MSv68742V2
VSENSE
TSEN control bit
Address/data bus
converted data
ADC VIN[10]
Temperature
sensor
Internal power
block
ADCVREFEN control bit
ADC VIN[9]
+
-
+
-
VREFINT

RM0490 Rev 6 323/1023
RM0490 Analog-to-digital converter (ADC)
345
Reading the temperature
1. Select the ADC V IN[9] input channel.
2. Select an appropriate sampling time specified in the device datasheet (T S_temp).
3. Set the TSEN bit in the ADC_CCR register  to wake up the temperature sensor from
power down mode and wait for its stabilization time (tSTART).
4. Start the ADC conversion by setting the ADSTART bit in the ADC_CR register (or by
external trigger).
5. Read the resulting V SENSE data in the ADC_DR register.
6. Calculate the temperature using the following formula
Where:
• TS_CAL1 is the temperature sensor calibration value acquired at TS_CAL1_TEMP
(refer to the datasheet for TS_CAL1 value)
• TS_DATA is the actual temperature sensor output value converted by ADC
Refer to the specific device datasheet for more information about TS_CAL1 calibration
point.
• Avg_Slope is the coefficient of the temperature sensor output voltage expressed in
mV/°C (refer to the datasheet for Avg_Slope value).
Note: The sensor has a startup time after waki ng from power down mode before it can output
VSENSE at the correct level. The ADC also has a startup time after power-on, so to minimize
the delay, the ADEN and TSEN bits should be set at the same time.
Calculating the actual VREF+ voltage using the internal reference voltage
VREF+ voltage may be subject to variation or not precisely known. The embedded internal
reference voltage (VREFINT) and its calibration data acquired by the ADC during the
manufacturing process at VREF+_charac can be used to evaluate the actual VREF+ voltage
level.
The following formula gives the actual VREF+ voltage supplying the device:
Where:
• VREF+_Charac is the value of VREF+ voltage characterized at VREFINT during the
manufacturing process. It is specified in the device datasheet.
• VREFINT_CAL is the VREFINT calibration value
• VREFINT_DATA is the actual VREFINT output value converted by ADC
Temperature in °C() Sense_DATA TS_CAL1–Avg_Slope_Code-------------------------------------------------------------------- TS_CAL1_TEMP+=
Avg_Slope_Code Avg_Slope 4096× 3000⁄=
Sense_DATA TS_DATA V DDA× 3.0⁄=
VREF+ VREF _Charac+ VREFINT_CAL VREFINT_DATA⁄×=

Analog-to-digital converter (ADC) RM0490
324/1023 RM0490 Rev 6
Converting a supply-relative ADC measurement to an absolute voltage value
The ADC is designed to deliver a digital value corresponding to the ratio between the analog
power supply and the voltage applied on the converted channel. For most application use
cases, it is necessary to convert this ratio into a voltage independent of VREF+. For
applications where VREF+ is known and ADC converted values are right-aligned you can
use the following formula to get this absolute value:
For applications where VREF+ value is not known, you must use the internal voltage
reference and VREF+ can be replaced by the expression provided in Calculating the actual
VREF+ voltage using the internal reference voltage, resulting in the following formula:
Where:
• VREF+_Charac is the value of VREF+ voltage characterized at VREFINT during the
manufacturing process. It is specified in the device datasheet.
• VREFINT_CAL is the VREFINT calibration value
• ADC_DATAx is the value measured by the ADC on channelx (right-aligned)
• VREFINT_DATA is the actual VREFINT output value converted by the ADC
• NUM_CODES is the number of ADC output codes. For example with 12-bit resolution,
it is 212 = 4096 or with 8-bit resolution, 28 = 256.
Note: If ADC measurements are done using an output format other than 12 bit right-aligned, all the
parameters must first be converted to a compatible format before the calculation is done.
16.11 ADC interrupts
An interrupt can be generated by any of the following events:
• End Of Calibration (EOCAL flag)
• ADC power-up, when the ADC is ready (ADRDY flag)
• End of any conversion (EOC flag)
• End of a sequence of conversions (EOS flag)
• When an analog watchdog detection occurs (AWD1, AWD2, AWD3 flags)
• When the Channel configuration is ready (CCRDY flag)
• When the end of sampling phase occurs (EOSMP flag)
• when a data overrun occurs (OVR flag)
Separate interrupt enable bits are available for flexibility.
VCHANNELx
VREF+
NUM_CODES-------------------------------------- ADC_DATAx×=
VCHANNELx
VREF+_Charac VREFINT_CAL ADC_DATA x××
VREFINT_DATA NUM_CODES×-------------------------------------------------------------------------------------------------------------------------------------=
[Table 76](../tables/table_76.md). ADC interrupts
Interrupt event Event flag Enable control bit
End Of Calibration EOCAL EOCALIE
ADC ready ADRDY ADRDYIE
End of conversion EOC EOCIE

RM0490 Rev 6 325/1023
RM0490 Analog-to-digital converter (ADC)
345
End of sequence of conversions EOS EOSIE
Analog watchdog 1 status bit is set AWD1 AWD1IE
Analog watchdog 2 status bit is set AWD2 AWD2IE
Analog watchdog 3 status bit is set AWD3 AWD3IE
Channel Configuration Ready CCRDY CCRDYIE
End of sampling phase EOSMP EOSMPIE
Overrun OVR OVRIE
[Table 76](../tables/table_76.md). ADC interrupts (continued)
Interrupt event Event flag Enable control bit

Analog-to-digital converter (ADC) RM0490
326/1023 RM0490 Rev 6
16.12 ADC registers
Refer to Section 1.2 for a list of abbreviations used in register descriptions.
16.12.1 ADC interrupt and st atus register (ADC_ISR)
Address offset: 0x00
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. CCRDY Res. EOCAL Res. AWD3 AWD2 AWD1 Res. Res. OVR EOS EOC EOSMP ADRDY
rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1
Bits 31:14 Reserved, must be kept at reset value.
Bit 13 CCRDY: Channel Configuration Ready flag
This flag bit is set by hardware when the channel configuration is applied after programming to
ADC_CHSELR register or changing CHSELRMOD or SCANDIR. It is cleared by software by
programming it to it.
0: Channel configuration update not applied.
1: Channel configuration update is applied.
Note: When the software configures the channels (by programming ADC_CHSELR or changing
CHSELRMOD or SCANDIR), it must wait until the CCRDY flag rises before configuring again
or starting conversions, otherwise the new configuration (or the START bit) is ignored. Once the
flag is asserted, if the software needs to configure again the channels, it must clear the CCRDY
flag before proceeding with a new configuration.
Bit 12 Reserved, must be kept at reset value.
Bit 11 EOCAL: End Of Calibration flag
This bit is set by hardware when calibration is complete. It is cleared by software writing 1 to it.
0: Calibration is not complete
1: Calibration is complete
Bit 10 Reserved, must be kept at reset value.
Bit 9 AWD3: Analog watchdog 3 flag
This bit is set by hardware when the converted voltage crosses the values programmed in
ADC_AWD3TR and ADC_AWD3TR registers. It is cleared by software by programming it to 1.
0: No analog watchdog event occurred (or the flag event was already acknowledged and cleared by
software)
1: Analog watchdog event occurred
Bit 8 AWD2: Analog watchdog 2 flag
This bit is set by hardware when the converted voltage crosses the values programmed in
ADC_AWD2TR and ADC_AWD2TR registers. It is cleared by software programming it it.
0: No analog watchdog event occurred (or the flag event was already acknowledged and cleared by
software)
1: Analog watchdog event occurred

RM0490 Rev 6 327/1023
RM0490 Analog-to-digital converter (ADC)
345
16.12.2 ADC interrupt enab le register (ADC_IER)
Address offset: 0x04
Reset value: 0x0000 0000
Bit 7 AWD1: Analog watchdog 1 flag
This bit is set by hardware when the converted voltage crosses the values programmed in ADC_TR1
and ADC_HR1 registers. It is cleared by software by programming it to 1.
0: No analog watchdog event occurred (or the flag event was already acknowledged and cleared by
software)
1: Analog watchdog event occurred
Bits 6:5 Reserved, must be kept at reset value.
Bit 4 OVR: ADC overrun
This bit is set by hardware when an overrun occurs, meaning that a new conversion has complete
while the EOC flag was already set. It is cleared by software writing 1 to it.
0: No overrun occurred (or the flag event was already acknowledged and cleared by software)
1: Overrun has occurred
Bit 3 EOS: End of sequence flag
This bit is set by hardware at the end of the conversion of a sequence of channels selected by the
CHSEL bits. It is cleared by software writing 1 to it.
0: Conversion sequence not complete (or the flag event was already acknowledged and cleared by
software)
1: Conversion sequence complete
Bit 2 EOC: End of conversion flag
This bit is set by hardware at the end of each conversion of a channel when a new data result is
available in the ADC_DR register. It is cleared by software writing 1 to it or by reading the ADC_DR
register.
0: Channel conversion not complete (or the flag event was already acknowledged and cleared by
software)
1: Channel conversion complete
Bit 1 EOSMP: End of sampling flag
This bit is set by hardware during the conversion, at the end of the sampling phase.It is cleared by
software by programming it to ‘1’.
0: Not at the end of the sampling phase (or the flag event was already acknowledged and cleared by
software)
1: End of sampling phase reached
Bit 0 ADRDY: ADC ready
This bit is set by hardware after the ADC has been enabled (ADEN = 1) and when the ADC reaches
a state where it is ready to accept conversion requests.
It is cleared by software writing 1 to it.
0: ADC not yet ready to start conversion (or the flag event was already acknowledged and cleared
by software)
1: ADC is ready to start conversion

Analog-to-digital converter (ADC) RM0490
328/1023 RM0490 Rev 6
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. CCRDYIE Res. EOCALIE Res. AWD3IE AWD2IE AWD1IE Res. Res. OVRIE EOSIE EOCIE EOSMPIE ADRDYIE
rw rw rw rw rw rw rw rw rw rw
Bits 31:14 Reserved, must be kept at reset value.
Bit 13 CCRDYIE: Channel Configuration Ready Interrupt enable
This bit is set and cleared by software to enable/disable the channel configuration ready interrupt.
0: Channel configuration ready interrupt disabled
1: Channel configuration ready interrupt enabled
Note: The software is allowed to write this bit only  when ADSTART bit is cleared (this ensures that no
conversion is ongoing).
Bit 12 Reserved, must be kept at reset value.
Bit 11 EOCALIE: End of calibration interrupt enable
This bit is set and cleared by software to enable/disable the end of calibration interrupt.
0: End of calibration interrupt disabled
1: End of calibration interrupt enabled
Note: The software is allowed to write this bit only  when ADSTART bit is cleared (this ensures that no
conversion is ongoing).
Bit 10 Reserved, must be kept at reset value.
Bit 9 AWD3IE: Analog watchdog 3 interrupt enable
This bit is set and cleared by software to enable/disable the analog watchdog interrupt.
0: Analog watchdog interrupt disabled
1: Analog watchdog interrupt enabled
Note: The Software is allowed to write this bit only when ADSTART bit is cleared (this ensures that no
conversion is ongoing).
Bit 8 AWD2IE: Analog watchdog 2 interrupt enable
This bit is set and cleared by software to enable/disable the analog watchdog interrupt.
0: Analog watchdog interrupt disabled
1: Analog watchdog interrupt enabled
Note: The Software is allowed to write this bit only when ADSTART bit is cleared (this ensures that no
conversion is ongoing).
Bit 7 AWD1IE: Analog watchdog 1 interrupt enable
This bit is set and cleared by software to enable/disable the analog watchdog interrupt.
0: Analog watchdog interrupt disabled
1: Analog watchdog interrupt enabled
Note: The Software is allowed to write this bit only when ADSTART bit is cleared (this ensures that no
conversion is ongoing).
Bits 6:5 Reserved, must be kept at reset value.

RM0490 Rev 6 329/1023
RM0490 Analog-to-digital converter (ADC)
345
16.12.3 ADC control register (ADC_CR)
Address offset: 0x08
Reset value: 0x0000 0000
Bit 4 OVRIE: Overrun interrupt enable
This bit is set and cleared by software to enable/disable the overrun interrupt.
0: Overrun interrupt disabled
1: Overrun interrupt enabled. An interrupt is generated when the OVR bit is set.
Note: The software is allowed to write this bit only  when ADSTART bit is cleared (this ensures that no
conversion is ongoing).
Bit 3 EOSIE: End of conversion sequence interrupt enable
This bit is set and cleared by software to enable/disable the end of sequence of conversions
interrupt.
0: EOS interrupt disabled
1: EOS interrupt enabled. An interrupt is generated when the EOS bit is set.
Note: The software is allowed to write this bit only  when ADSTART bit is cleared (this ensures that no
conversion is ongoing).
Bit 2 EOCIE: End of conversion interrupt enable
This bit is set and cleared by software to enable/disable the end of conversion interrupt.
0: EOC interrupt disabled
1: EOC interrupt enabled. An interrupt is generated when the EOC bit is set.
Note: The software is allowed to write this bit only  when ADSTART bit is cleared (this ensures that no
conversion is ongoing).
Bit 1 EOSMPIE: End of sampling flag interrupt enable
This bit is set and cleared by software to enable/disable the end of the sampling phase interrupt.
0: EOSMP interrupt disabled.
1: EOSMP interrupt enabled. An interrupt is generated when the EOSMP bit is set.
Note: The software is allowed to write this bit only  when ADSTART bit is cleared (this ensures that no
conversion is ongoing).
Bit 0 ADRDYIE: ADC ready interrupt enable
This bit is set and cleared by software to enable/disable the ADC Ready interrupt.
0: ADRDY interrupt disabled.
1: ADRDY interrupt enabled. An interrupt is generated when the ADRDY bit is set.
Note: The software is allowed to write this bit only  when ADSTART bit is cleared (this ensures that no
conversion is ongoing).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ADCAL Res. Res. ADVREGEN Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
rs rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. ADSTP Res. ADSTART ADDIS ADEN
rs rs rs rs

Analog-to-digital converter (ADC) RM0490
330/1023 RM0490 Rev 6
Bit 31 ADCAL: ADC calibration
This bit is set by software to start the calibration of the ADC.
It is cleared by hardware after calibration is complete.
0: Calibration complete
1: Write 1 to calibrate the ADC. Read at 1 means that a calibration is in progress.
Note: The software is allowed to set ADCAL only when the ADC is disabled (ADCAL  = 0,
ADSTART = 0, ADSTP = 0, ADDIS = 0, AUTOFF = 0, and ADEN = 0).
The software is allowed to update the calibration factor by writing ADC_CALFACT only when
ADEN = 1 and ADSTART = 0 (ADC enabled and no conversion is ongoing).
Bits 30:29 Reserved, must be kept at reset value.
Bit 28 ADVREGEN: ADC Voltage Regulator Enable
This bit is set by software, to enable the ADC internal voltage regulator. The voltage regulator output
is available after tADCVREG_STUP.
It is cleared by software to disable the voltage regulator. It can be cleared only if ADEN is cleared.
0: ADC voltage regulator disabled
1: ADC voltage regulator enabled
Note: The software is allowed to program this bit field only when the ADC is disabled (ADCAL  = 0,
ADSTART = 0, ADSTP = 0, ADDIS = 0 and ADEN = 0).
Bits 27:5 Reserved, must be kept at reset value.
Bit 4 ADSTP: ADC stop conversion command
This bit is set by software to stop and discard an ongoing conversion (ADSTP Command).
It is cleared by hardware when the conversion is effectively discarded and the ADC is ready to
accept a new start conversion command.
0: No ADC stop conversion command ongoing
1: Write 1 to stop the ADC. Read 1 means that an ADSTP command is in progress.
Note: Setting ADSTP to ‘1’ is only effective when ADSTART = 1 and ADDIS = 0 (ADC is enabled and
may be converting and there is no pending request to disable the ADC)
Bit 3 Reserved, must be kept at reset value.
Bit 2 ADSTART: ADC start conversion command
This bit is set by software to start ADC conversion. Depending on the EXTEN [1:0] configuration bits,
a conversion either starts immediately (software trigger configuration) or once a hardware trigger
event occurs (hardware trigger configuration).
It is cleared by hardware:
– In single conversion mode (CONT = 0, DISCEN = 0), when software trigger is selected
(EXTEN = 00): at the assertion of the end of Conversion Sequence (EOS) flag.
– In discontinuous conversion mode (CONT = 0, DISCEN = 1), when the software trigger is selected
(EXTEN = 00): at the assertion of the end of Conversion (EOC) flag.
– In all other cases: after the execution of the ADSTP command, at the same time as the ADSTP bit is
cleared by hardware.
0: No ADC conversion is ongoing.
1: Write 1 to start the ADC. Read 1 means that the ADC is operating and may be converting.
Note: The software is allowed to set ADSTART only when ADEN = 1 and ADDIS = 0 (ADC is enabled
and there is no pending request to disable the ADC).
After writing to ADC_CHSELR register or changing CHSELRMOD or SCANDIRW, it is
mandatory to wait until CCRDY flag is asserted before setting ADSTART, otherwise, the value
written to ADSTART is ignored.

RM0490 Rev 6 331/1023
RM0490 Analog-to-digital converter (ADC)
345
16.12.4 ADC configuration register 1 (ADC_CFGR1)
Address offset: 0x0C
Reset value: 0x0000 0000
The software is allowed to program ADC_CFGR1 only when ADEN is cleared in ADC_CR.
Bit 1 ADDIS: ADC disable command
This bit is set by software to disable the ADC (ADDIS command) and put it into power-down state
(OFF state).
It is cleared by hardware once the ADC is effectively disabled (ADEN is also cleared by hardware at
this time).
0: No ADDIS command ongoing
1: Write 1 to disable the ADC. Read 1 means that an ADDIS command is in progress.
Note: Setting ADDIS to ‘1’ is only effective when ADEN = 1 and ADSTART = 0 (which ensures that no
conversion is ongoing)
Bit 0 ADEN: ADC enable command
This bit is set by software to enable the ADC. The ADC is effectively ready to operate once the
ADRDY flag has been set.
It is cleared by hardware when the ADC is disabled, after the execution of the ADDIS command.
0: ADC is disabled (OFF state)
1: Write 1 to enable the ADC.
Note: The software is allowed to set ADEN only when ADCAL  = 0, ADSTP = 0, ADSTART = 0,
ADDIS = 0, ADEN = 0, and ADVREGEN = 1.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. AWD1CH[4:0] Res. Res. AWD1EN AWD1SGL CHSELRMOD Res. Res. Res. Res. DISCEN
rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
AUTOF
F WAIT CONT OVRMOD EXTEN[1:0] Res. EXTSEL[2:0] ALIGN RES[1:0] SCANDIR DMACFG DMAEN
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 31 Reserved, must be kept at reset value.
Bits 30:26 AWD1CH[4:0]: Analog watchdog channel selection
These bits are set and cleared by software. They select the input channel to be guarded by
the analog watchdog.
00000: ADC analog input Channel 0 monitored by AWD
00001: ADC analog input Channel 1 monitored by AWD
.....
10110: ADC analog input Channel 22 monitored by AWD
Others: Reserved
Note: The channel selected by the AWDCH[4:0]  bits must be also set into the CHSELR
register.
Bits 25:24 Reserved, must  be kept at reset value.

Analog-to-digital converter (ADC) RM0490
332/1023 RM0490 Rev 6
Bit 23 AWD1EN: Analog watchdog enable
This bit is set and cleared by software.
0: Analog watchdog 1 disabled
1: Analog watchdog 1 enabled
Bit 22 AWD1SGL: Enable the watchdog on a single channel or on all channels
This bit is set and cleared by software to enable the analog watchdog on the channel
identified by the AWDCH[4:0] bits or on all the channels
0: Analog watchdog 1 enabled on all channels
1: Analog watchdog 1 enabled on a single channel
Bit 21 CHSELRMOD: Mode selection of the ADC_CHSELR register
This bit is set and cleared by software to control the ADC_CHSELR feature:
0: Each bit of the ADC_CHSELR register enables an input
1: ADC_CHSELR register is able to sequence up to 8 channels
Note: If CCRDY is not yet asserted after channel  configuration (writing ADC_CHSELR register
or changing CHSELRMOD or SCANDIR), the value written to this bit is ignored.
Bits 20:17 Reserved, must  be kept at reset value.
Bit 16 DISCEN: Discontinuous mode
This bit is set and cleared by software to enable/disable discontinuous mode.
0: Discontinuous mode disabled
1: Discontinuous mode enabled
Note: It is not possible to have  both discontinuous mode and continuous mode enabled: it is
forbidden to set both bits DISCEN = 1 and CONT = 1.
Bit 15 AUTOFF: Auto-off mode
This bit is set and cleared by software to enable/disable auto-off mode..
0: Auto-off mode disabled
1: Auto-off mode enabled
Bit 14 WAIT: Wait conversion mode
This bit is set and cleared by software to enable/disable wait conversion mode..
0: Wait conversion mode off
1: Wait conversion mode on
Bit 13 CONT: Single / continuous conversion mode
This bit is set and cleared by software. If it is set, conversion takes place continuously until it
is cleared.
0: Single conversion mode
1: Continuous conversion mode
Note: It is not possible to have  both discontinuous mode and continuous mode enabled: it is
forbidden to set both bits DISCEN = 1 and CONT = 1.

RM0490 Rev 6 333/1023
RM0490 Analog-to-digital converter (ADC)
345
Bit 12 OVRMOD: Overrun management mode
This bit is set and cleared by software and configure the way data overruns are managed.
0: ADC_DR register is preserved with the old data when an overrun is detected.
1: ADC_DR register is overwritten with the last conversion result when an overrun is
detected.
Bits 11:10 EXTEN[1:0]: External trigger enable and polarity selection
These bits are set and cleared by software to select the external trigger polarity and enable
the trigger.
00: Hardware trigger detection disabled (conversions can be started by software)
01: Hardware trigger detection on the rising edge
10: Hardware trigger detection on the falling edge
11: Hardware trigger detection on both the rising and falling edges
Bit 9 Reserved, must be kept at reset value.
Bits 8:6 EXTSEL[2:0]: External trigger selection
These bits select the external event used to trigger the start of conversion (refer to [Table 69](../tables/table_69.md):
External triggers for details):
000: TRG0
001: TRG1
010: TRG2
011: TRG3
100: TRG4
101: TRG5
110: TRG6
111: TRG7
Bit 5 ALIGN: Data alignment
This bit is set and cleared by software to select right or left alignment. Refer to [Figure 43](../figures/figure_43.md):
Data alignment and resolution (oversampling disabled: OVSE = 0) on page 309
0: Right alignment
1: Left alignment
Bits 4:3 RES[1:0]: Data resolution
These bits are written by software to select the resolution of the conversion.
00: 12 bits
01: 10 bits
10: 8 bits
11: 6 bits
Bit 2 SCANDIR: Scan sequence direction
This bit is set and cleared by software to select the direction in which the channels is scanned
in the sequence. It is effective only if CHSELMOD bit is cleared.
0: Upward scan (from CHSEL0 to CHSEL22)
1: Backward scan (from CHSEL22 to CHSEL0)
Note: If CCRDY is not yet asserted after channel  configuration (writing ADC_CHSELR register
or changing CHSELRMOD or SCANDIR), the value written to this bit is ignored.

Analog-to-digital converter (ADC) RM0490
334/1023 RM0490 Rev 6
16.12.5 ADC configuration register 2 (ADC_CFGR2)
Address offset: 0x10
Reset value: 0x0000 0000
The software is allowed to program ADC_CFGR2 only when ADEN is cleared in ADC_CR.
Bit 1 DMACFG: Direct memory access configuration
This bit is set and cleared by software to select between two DMA modes of operation and is
effective only when DMAEN = 1.
0: DMA one shot mode selected
1: DMA circular mode selected
For more details, refer to Section 16.6.5: Managing converted data using the DMA on
page 311.
Bit 0 DMAEN: Direct memory access enable
This bit is set and cleared by software to enable the generation of DMA requests. This allows
the DMA controller to be used to manage automatically the converted data. For more details,
refer to Section 16.6.5: Managing converted data using the DMA on page 311.
0: DMA disabled
1: DMA enabled
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
CKMODE[1:0] LFTRIG Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res.
rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. TOVS OVSS[3:0] OVSR[2:0] Res. OVSE
rw rw rw rw rw rw rw rw rw
Bits 31:30 CKMODE[1:0]: ADC clock mode
These bits are set and cleared by software to define how the analog ADC is clocked:
00: ADCCLK (Asynchronous clock mode), generated at product level (refer to RCC section)
01: PCLK/2 (Synchronous clock mode)
10: PCLK/4 (Synchronous clock mode)
11: PCLK (Synchronous clock mode). This configuration must be enabled only if PCLK has a 50%
duty clock cycle (APB prescaler configured inside the RCC must be bypassed and the system clock
must by 50% duty cycle)
In all synchronous clock modes, there is no jitter in the delay from a timer trigger to the start of a
conversion.
Note: The software is allowed to write these bits only when the ADC is disabled (ADCAL  = 0,
ADSTART = 0, ADSTP = 0, ADDIS = 0 and ADEN = 0).
Bit 29 LFTRIG: Low frequency trigger mode enable
This bit is set and cleared by software.
0: Low Frequency Trigger Mode disabled
1: Low Frequency Trigger Mode enabled
Note: The software is allowed to write this bit only when ADEN bit is cleared.
Bits 28:10 Reserved, must be kept at reset value.

RM0490 Rev 6 335/1023
RM0490 Analog-to-digital converter (ADC)
345
Bit 9 TOVS: Triggered Oversampling
This bit is set and cleared by software.
0: All oversampled conversions for a channel are done consecutively after a trigger
1: Each oversampled conversion for a channel needs a trigger
Note: The software is allowed to write this bit only when ADEN bit is cleared.
Bits 8:5 OVSS[3:0]: Oversampling shift
This bit is set and cleared by software.
0000: No shift
0001: Shift 1-bit
0010: Shift 2-bits
0011: Shift 3-bits
0100: Shift 4-bits
0101: Shift 5-bits
0110: Shift 6-bits
0111: Shift 7-bits
1000: Shift 8-bits
Others: Reserved
Note: The software is allowed to write this bit only when ADEN bit is cleared.
Bits 4:2 OVSR[2:0]: Oversampling ratio
This bit filed defines the number of oversampling ratio.
000: 2x
001: 4x
010: 8x
011: 16x
100: 32x
101: 64x
110: 128x
111: 256x
Starting from 32x, it is mandatory to use OVSS[3:0] to reduce the data size to less than 16 bits to fit
to the ADC_DR register. For example, if OVSR[2:0] is configured to 32x, the data width is 17 bits,
and OVSS[3:0] must be set to 1-bit shift.
Note: The software is allowed to write this bit only when ADEN bit is cleared.
Bit 1 Reserved, must be kept at reset value.
Bit 0 OVSE: Oversampler Enable
This bit is set and cleared by software.
0: Oversampler disabled
1: Oversampler enabled
Note: The software is allowed to write this bit only when ADEN bit is cleared.

Analog-to-digital converter (ADC) RM0490
336/1023 RM0490 Rev 6
16.12.6 ADC sampling time  register (ADC_SMPR)
Address offset: 0x14
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. SMPSEL22 SMPSEL21 SMPSEL20 SMPSEL19 SMPSEL18 SMPSEL17 SMPSEL16 SMPSEL15 SMPSEL14 SMPSEL13 SMPSEL12 SMPSEL11 SMPSEL10 SMPSEL9 SMPSEL8
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
SMPSE
L7
SMPSE
L6
SMPSE
L5
SMPSE
L4
SMPSE
L3
SMPSE
L2
SMPSE
L1
SMPSE
L0 Res. SMP2[2:0] Res. SMP1[2:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 31 Reserved, must be kept at reset value.
Bits 30:8 SMPSELx: Channel-x sampling time selection (x = 22 to 0)
These bits are written by software to define which sampling time is used.
0: Sampling time of CHANNELx use the setting of SMP1[2:0] register.
1: Sampling time of CHANNELx use the setting of SMP2[2:0] register.
Note: The software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).
Refer to Section 16.3: ADC implementation for the maximum number of channels.
Bit 7 Reserved, must be kept at reset value.
Bits 6:4 SMP2[2:0]: Sampling time selection 2
These bits are written by software to select the sampling time that applies to all channels.
000: 1.5 ADC clock cycles
001: 3.5 ADC clock cycles
010: 7.5 ADC clock cycles
011: 12.5 ADC clock cycles
100: 19.5 ADC clock cycles
101: 39.5 ADC clock cycles
110: 79.5 ADC clock cycles
111: 160.5 ADC clock cycles
Note: The software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).
Bit 3 Reserved, must be kept at reset value.
Bits 2:0 SMP1[2:0]: Sampling time selection 1
These bits are written by software to select the sampling time that applies to all channels.
000: 1.5 ADC clock cycles
001: 3.5 ADC clock cycles
010: 7.5 ADC clock cycles
011: 12.5 ADC clock cycles
100: 19.5 ADC clock cycles
101: 39.5 ADC clock cycles
110: 79.5 ADC clock cycles
111: 160.5 ADC clock cycles
Note: The software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).

RM0490 Rev 6 337/1023
RM0490 Analog-to-digital converter (ADC)
345
16.12.7 ADC watchdog threshol d register (ADC_AWD1TR)
Address offset: 0x20
Reset value: 0x0FFF 0000
16.12.8 ADC watchdog threshol d register (ADC_AWD2TR)
Address offset: 0x24
Reset value: 0x0FFF 0000
16.12.9 ADC channel selecti on register (ADC_CHSELR)
Address offset: 0x28
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. HT1[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. LT1[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:28 Reserved, must be kept at reset value.
Bits 27:16 HT1[11:0]: Analog watchdog 1 higher threshold
These bits are written by software to define the higher threshold for the analog watchdog.
Refer to Section 16.8: Analog window watchdogs on page 315.
Bits 15:12 Reserved, must be kept at reset value.
Bits 11:0 LT1[11:0]: Analog watchdog 1 lower threshold
These bits are written by software to define the lower threshold for the analog watchdog.
Refer to Section 16.8: Analog window watchdogs on page 315.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. HT2[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. LT2[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:28 Reserved, must be kept at reset value.
Bits 27:16 HT2[11:0]: Analog watchdog 2 higher threshold
These bits are written by software to define the higher threshold for the analog watchdog.
Refer to Section 16.8: Analog window watchdogs on page 315.
Bits 15:12 Reserved, must be kept at reset value.
Bits 11:0 LT2[11:0]: Analog watchdog 2 lower threshold
These bits are written by software to define the lower threshold for the analog watchdog.
Refer to Section 16.8: Analog window watchdogs on page 315.

Analog-to-digital converter (ADC) RM0490
338/1023 RM0490 Rev 6
The same register can be used in two different modes:
– Each ADC_CHSELR bit enables an input (CHSELRMOD = 0 in ADC_CFGR1). Refer to
the current section.
– ADC_CHSELR is able to sequence up to 8 channels (CHSELRMOD = 1 in
ADC_CFGR1). Refer to next section.
CHSELRMOD = 0 in ADC_CFGR1
16.12.10 ADC channel selection regi ster [alternate] (ADC_CHSELR)
Address offset: 0x28
Reset value: 0x0000 0000
The same register can be used in two different modes:
– Each ADC_CHSELR bit enables an input (CHSELRMOD = 0 in ADC_CFGR1). Refer to
the current previous section.
– ADC_CHSELR is able to sequence up to 8 channels (CHSELRMOD = 1 in
ADC_CFGR1). Refer to this section.
CHSELRMOD = 1 in ADC_CFGR1:
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. CHSEL22 CHSEL21 CHSEL20 CHSEL19 CHSEL18 CHSEL17 CHSEL16
rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CHSEL
15
CHSEL
14
CHSEL
13
CHSEL
12
CHSEL
11
CHSEL
10
CHSEL
9
CHSEL
8
CHSEL
7
CHSEL
6
CHSEL
5
CHSEL
4
CHSEL
3
CHSEL
2
CHSEL
1
CHSEL
0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:23 Reserved, must be kept at reset value.
Bits 22:0 CHSEL[22:0]: Channel-x selection
These bits are written by software and define which channels are part of the sequence of channels
to be converted. Refer to [Figure 35](../figures/figure_35.md): ADC connectivity for ADC inputs connected to external
channels and internal sources.
0: Input Channel-x is not selected for conversion
1: Input Channel-x is selected for conversion
Note: The software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).
If CCRDY is not yet asserted after channel configuration (writing ADC_CHSELR register or
changing CHSELRMOD or SCANDIR), the value written to this bit is ignored.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
SQ8[3:0] SQ7[3:0] SQ6[3:0] SQ5[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
SQ4[3:0] SQ3[3:0] SQ2[3:0] SQ1[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0490 Rev 6 339/1023
RM0490 Analog-to-digital converter (ADC)
345
Bits 31:28 SQ8[3:0]: 8th conversion of the sequence
These bits are programmed by software with the channel number (0...14) assigned to the 8th
conversion of the sequence. 0b1111 indicates the end of the sequence.
When 0b1111 (end of sequence) is programmed to the lower sequence channels, these bits are
ignored.
0000: CH0
0001: CH1
...
1100: CH12
1101: CH13
1110: CH14
1111: No channel selected (End of sequence)
Note: The software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).
Bits 27:24 SQ7[3:0]: 7th conversion of the sequence
These bits are programmed by software with the channel number (0...14) assigned to the 8th
conversion of the sequence. 0b1111 indicates end of the sequence.
When 0b1111 (end of sequence) is programmed to the lower sequence channels, these bits are
ignored.
Refer to SQ8[3:0] for a definition of channel selection.
Note: The software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).
Bits 23:20 SQ6[3:0]: 6th conversion of the sequence
These bits are programmed by software with the channel number (0...14) assigned to the 8th
conversion of the sequence. 0b1111 indicates end of the sequence.
When 0b1111 (end of sequence) is programmed to the lower sequence channels, these bits are
ignored.
Refer to SQ8[3:0] for a definition of channel selection.
Note: The software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).
Bits 19:16 SQ5[3:0]: 5th conversion of the sequence
These bits are programmed by software with the channel number (0...14) assigned to the 8th
conversion of the sequence. 0b1111 indicates end of the sequence.
When 0b1111 (end of sequence) is programmed to the lower sequence channels, these bits are
ignored.
Refer to SQ8[3:0] for a definition of channel selection.
Note: The software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).
Bits 15:12 SQ4[3:0]: 4th conversion of the sequence
These bits are programmed by software with the channel number (0...14) assigned to the 8th
conversion of the sequence. 0b1111 indicates end of the sequence.
When 0b1111 (end of sequence) is programmed to the lower sequence channels, these bits are
ignored.
Refer to SQ8[3:0] for a definition of channel selection.
Note: The software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).

Analog-to-digital converter (ADC) RM0490
340/1023 RM0490 Rev 6
16.12.11 ADC watchdog threshol d register (ADC_AWD3TR)
Address offset: 0x2C
Reset value: 0x0FFF 0000
Bits 11:8 SQ3[3:0]: 3rd conversion of the sequence
These bits are programmed by software with the channel number (0...14) assigned to the 8th
conversion of the sequence. 0b1111 indicates end of the sequence.
When 0b1111 (end of sequence) is programmed to the lower sequence channels, these bits are
ignored.
Refer to SQ8[3:0] for a definition of channel selection.
Note: The software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).
Bits 7:4 SQ2[3:0]: 2nd conversion of the sequence
These bits are programmed by software with the channel number (0...14) assigned to the 8th
conversion of the sequence. 0b1111 indicates end of the sequence.
When 0b1111 (end of sequence) is programmed to the lower sequence channels, these bits are
ignored.
Refer to SQ8[3:0] for a definition of channel selection.
Note: The software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).
Bits 3:0 SQ1[3:0]: 1st conversion of the sequence
These bits are programmed by software with the channel number (0...14) assigned to the 8th
conversion of the sequence. 0b1111 indicates end of the sequence.
When 0b1111 (end of sequence) is programmed to the lower sequence channels, these bits are
ignored.
Refer to SQ8[3:0] for a definition of channel selection.
Note: The software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. HT3[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. LT3[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:28 Reserved, must be kept at reset value.
Bits 27:16 HT3[11:0]: Analog watchdog 3 higher threshold
These bits are written by software to define the higher threshold for the analog watchdog.
Refer to Section 16.8: Analog window watchdogs on page 315.
Bits 15:12 Reserved, must be kept at reset value.
Bits 11:0 LT3[11:0]: Analog watchdog 3lower threshold
These bits are written by software to define the lower threshold for the analog watchdog.
Refer to Section 16.8: Analog window watchdogs on page 315.

RM0490 Rev 6 341/1023
RM0490 Analog-to-digital converter (ADC)
345
16.12.12 ADC data register (ADC_DR)
Address offset: 0x40
Reset value: 0x0000 0000
16.12.13 ADC analog watc hdog 2 configuration register (ADC_AWD2CR)
Address offset: 0xA0
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DATA[15:0]
rrrrrrrrrrrrrrrr
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 DATA[15:0]: Converted data
These bits are read-only. They contain the conversion result from the last converted channel. The
data are left- or right-aligned as shown in [Figure 43](../figures/figure_43.md).
Just after a calibration is complete, DATA[6:0] contains the calibration factor.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. AWD2CH22 AWD2CH21 AWD2CH20 AWD2CH19 AWD2CH18 AWD2CH17 AWD2CH16
rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
AWD2
CH15
AWD2
CH14
AWD2
CH13
AWD2
CH12
AWD2
CH11
AWD2
CH10
AWD2
CH9
AWD2
CH8
AWD2
CH7
AWD2
CH6
AWD2
CH5
AWD2
CH4
AWD2
CH3
AWD2
CH2
AWD2
CH1
AWD2
CH0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:23 Reserved, must be kept at reset value.
Bits 22:0 AWD2CH[22:0]: Analog watchdog channel selection
These bits are set and cleared by software. They enable and select the input channels to be guarded
by analog watchdog 2 (AWD2).
0: ADC analog channel-x is not monitored by AWD2
1: ADC analog channel-x is monitored by AWD2
Note: The channels selected through ADC_AWD2CR must be also configured into the
ADC_CHSELR registers. The software is allowed to write this bit only when ADEN = 0.

Analog-to-digital converter (ADC) RM0490
342/1023 RM0490 Rev 6
16.12.14 ADC Analog Watchdog 3 Conf iguration register (ADC_AWD3CR)
Address offset: 0xA4
Reset value: 0x0000 0000
16.12.15 ADC calibration factor (ADC_CALFACT)
Address offset: 0xB4
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. AWD3CH22 AWD3CH21 AWD3CH20 AWD3CH19 AWD3CH18 AWD3CH17 AWD3CH16
rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
AWD3
CH15
AWD3
CH14
AWD3
CH13
AWD3
CH12
AWD3
CH11
AWD3
CH10
AWD3
CH9
AWD3
CH8
AWD3
CH7
AWD3
CH6
AWD3
CH5
AWD3
CH4
AWD3
CH3
AWD3
CH2
AWD3
CH1
AWD3
CH0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:23 Reserved, must be kept at reset value.
Bits 22:0 AWD3CH[22:0]: Analog watchdog channel selection
These bits are set and cleared by software. They enable and select the input channels to be guarded
by analog watchdog 3 (AWD3).
0: ADC analog channel-x is not monitored by AWD3
1: ADC analog channel-x is monitored by AWD3
Note: The channels selected through ADC_AWD3CR must be also configured into the
ADC_CHSELR registers. The software is allowed to write this bit only when ADEN = 0.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. CALFACT[6:0]
rw rw rw rw rw rw rw
Bits 31:7 Reserved, must be kept at reset value.
Bits 6:0 CALFACT[6:0]: Calibration factor
These bits are written by hardware or by software.
– Once a calibration is complete, they are updated by hardware with the calibration factors.
– Software can write these bits with a new calibration factor. If the new calibration factor is different
from the current one stored into the analog ADC, it is then applied once a new conversion is
launched.
– Just after a calibration is complete, DATA[6:0] contains the calibration factor.
Note: Software can write these bits only when ADEN=1 (ADC is enabled and no calibration is ongoing
and no conversion is ongoing).

RM0490 Rev 6 343/1023
RM0490 Analog-to-digital converter (ADC)
345
16.12.16 ADC common configurat ion register (ADC_CCR)
Address offset: 0x308
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. TSEN VREFEN PRESC[3:0] Res. Res.
rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9 8 7 6 5432 1 0
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
Bits 31:25 Reserved, must  be kept at reset value.
Bit 24 Reserved, must be kept at reset value.
Bit 23 TSEN: Temperature sensor buffer enable
This bit is set and cleared by software to enable/disable the temperature sensor buffer.
0: Temperature sensor buffer disabled
1: Temperature sensor buffer enabled
Note: Software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).
This bit must be cleared before entering low-power modes to avoid unwanted power
consumption.
Bit 22 VREFEN: VREFINT buffer enable
This bit is set and cleared by software to enable/disable the VREFINT buffer.
0: VREFINT buffer disabled
1: VREFINT buffer enabled
Note: Software is allowed to write this bit only when ADSTART  = 0 (which ensures that no
conversion is ongoing).
This bit must be cleared before entering low-power modes to avoid unwanted power
consumption.
Bits 21:18 PRESC[3:0]: ADC prescaler
Set and cleared by software to select the frequency of the clock to the ADC.
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
Other: Reserved
Note: Software is allowed to write these bi ts only when the ADC is disabled (ADCAL = 0,
ADSTART = 0, ADSTP = 0, ADDIS = 0 and ADEN = 0).
Bits 17:0 Reserved, must be kept at reset value.

Analog-to-digital converter (ADC) RM0490
344/1023 RM0490 Rev 6
16.13 ADC register map
The following table summarizes the ADC registers.
[Table 77](../tables/table_77.md). ADC register map and reset values
Offset Register name Reset value
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
ADC_ISR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCRDY
Res.
EOCAL
Res.
AWD3
AWD2
AWD1
Res.
Res.
OVR
EOS
EOC
EOSMP
ADRDY
Reset value 0 0 000 00000
0x04
ADC_IER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CCRDYIE
Res.
EOCALIE
Res.
AWD3IE
AWD2IE
AWD1IE
Res.
Res.
OVRIE
EOSIE
EOCIE
EOSMPIE
ADRDYIE
Reset value 0 0 000 00000
0x08
ADC_CR
ADCAL
Res.
Res.
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
Res.
ADSTP
Res.
ADSTART
ADDIS
ADEN
Reset value 0 0 0 000
0x0C
ADC_CFGR1
Res.AWDCH[4:0]
Res.
Res.
AWD1EN
AWD1SGL
CHSELRMOD
Res.
Res.
Res.
Res.
DISCEN
AUTOFF
WAIT
CONT
OVRMOD
EXTEN[1:0]
Res.
EXTSEL
[2:0]
ALIGN
RES
[1:0]
SCANDIR
DMACFG
DMAEN
Reset value 00000 000 0000000 000000000
0x10
ADC_CFGR2
CKMODE[1:0]
LFTRIG
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TOVS
OVSS[3:0]
OVSR[2:0]
Res.
OVSE
Reset value 000 0000000000
0x14
ADC_SMPR
Res.
SMPSEL22.
SMPSEL21.
SMPSEL20.
SMPSEL19.
SMPSEL18.
SMPSEL17
SMPSEL16
SMPSEL15
SMPSEL14
SMPSEL13
SMPSEL12
SMPSEL11
SMPSEL10
SMPSEL9
SMPSEL8
SMPSEL7
SMPSEL6
SMPSEL5
SMPSEL4
SMPSEL3
SMPSEL2
SMPSEL1
SMPSEL0
Res.
SMP2
[2:0]
Res.
SMP1
[2:0]
R e s e t  v a l u e 00000000000000000000000 000 000
0x18 Reserved Reserved
0x1C Reserved Reserved
0x20
ADC_AWD1TR
Res.
Res.
Res.
Res. HT1[11:0]
Res.
Res.
Res.
Res. LT1[11:0]
Reset value 111111111111 00000000 0000
0x24
ADC_AWD2TR
Res.
Res.
Res.
Res. HT2[11:0]
Res.
Res.
Res.
Res. LT2[11:0]
Reset value 111111111111 00000000 0000
0x28
ADC_CHSELR
(CHSELRMOD=
0)
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CHSEL22
CHSEL21
CHSEL20
CHSEL19
CHSEL18
CHSEL17
CHSEL16
CHSEL15
CHSEL14
CHSEL13
CHSEL12
CHSEL11
CHSEL10
CHSEL9
CHSEL8
CHSEL7
CHSEL6
CHSEL5
CHSEL4
CHSEL3
CHSEL2
CHSEL1
CHSEL0
Reset value 00000000000000000000000

RM0490 Rev 6 345/1023
RM0490 Analog-to-digital converter (ADC)
345
Refer to Section 2.2 for the register boundary addresses.
0x28
ADC_CHSELR
(CHSELRMOD=
1)
SQ8[3:0] SQ7[3:0] SQ6[3:0] SQ5[3:0] SQ4[3:0] SQ3[3:0] SQ2[3:0] SQ1[3:0]
R e s e t  v a l u e 0000000000000000000000000000 0000
0x2C
ADC_AWD3TR
Res.
Res.
Res.
Res. HT3[11:0]
Res.
Res.
Res.
Res. LT3[11:0]
Reset value 111111111111 00000000 0000
0x30
0x34
0x38
0x3C
Reserved Reserved
0x40
ADC_DR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. DATA[15:0]
Reset value 0000000000000000
... Reserved Reserved
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
AWD2CH22
AWD2CH21
AWD2CH20
AWD2CH19
AWD2CH18
AWD2CH17
AWD2CH16
AWD2CH15
AWD2CH14
AWD2CH13
AWD2CH12
AWD2CH11
AWD2CH10
AWD2CH9
AWD2CH8
AWD2CH7
AWD2CH6
AWD2CH5
AWD2CH4
AWD2CH3
AWD2CH2
AWD2CH1
AWD2CH0
Reset value 00000000000000000000000
0xA4
ADC_AWD3CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWD3CH22
AWD3CH21
AWD3CH20
AWD3CH19
AWD3CH18
AWD3CH17
AWD3CH16
AWD3CH15
AWD3CH14
AWD3CH13
AWD3CH12
AWD3CH11
AWD3CH10
AWD3CH9
AWD3CH8
AWD3CH7
AWD3CH6
AWD3CH5
AWD3CH4
AWD3CH3
AWD3CH2
AWD3CH1
AWD3CH0
Reset value 00000000000000000000000
... Reserved Reserved
0xB4
ADC_CALFACT
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. CALFACT[6:0]
Reset value 0000000
... Reserved Reserved
0x308
ADC_CCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TSEN
VREFEN
PRESC3
PRESC2
PRESC1
PRESC0
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Reset value 000000
[Table 77](../tables/table_77.md). ADC register map and reset values (continued)
Offset Register name Reset value
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
* [Figure 30: Architectural Diagram](../figures/figure_30.md)
* [Figure 31: Architectural Diagram](../figures/figure_31.md)
* [Figure 32: Architectural Diagram](../figures/figure_32.md)
* [Figure 33: Architectural Diagram](../figures/figure_33.md)
* [Figure 34: Architectural Diagram](../figures/figure_34.md)
* [Figure 35: Architectural Diagram](../figures/figure_35.md)
* [Figure 36: Architectural Diagram](../figures/figure_36.md)
* [Figure 37: Architectural Diagram](../figures/figure_37.md)
* [Figure 38: Architectural Diagram](../figures/figure_38.md)
* [Figure 39: Architectural Diagram](../figures/figure_39.md)
* [Figure 40: Architectural Diagram](../figures/figure_40.md)
* [Figure 41: Architectural Diagram](../figures/figure_41.md)
* [Figure 42: Architectural Diagram](../figures/figure_42.md)
* [Figure 43: Architectural Diagram](../figures/figure_43.md)
* [Figure 44: Architectural Diagram](../figures/figure_44.md)

## 4. Referenced Configuration Tables in this Chapter
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
* [Table 77: Configuration Matrix](../tables/table_77.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)