# Chapter 26: Digital filter for sigma delta modulators (DFSDM)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 26: Digital filter for sigma delta modulators (DFSDM).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 862 - 919
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
Digital filter for sigma delta modulators (DFSDM) RM0438
862/2187 RM0438 Rev 8
26 Digital filter for sigma delta modulators (DFSDM)
26.1 Introduction
Digital filter for sigma delta modulators (DFSDM) is a high-performance module dedicated to
interface external Σ∆ modulators. It is featuring up to 4 external digital serial interfaces
(channels) and up to 4 digital filters with flexible Sigma Delta stream digital processing
options to offer up to 24-bit final ADC resolution. DFSDM also features optional parallel data
stream input from internal ADC peripherals or from device memory.
An external Σ∆ modulator provides digital data stream of converted analog values from the
external Σ∆ modulator analog input. This digital data stream is sent into a DFSDM input
channel through a serial interface. DFSDM supports several standards to connect various
Σ∆ modulator outputs: SPI interface and Manchester coded 1-wire interface (both with
adjustable parameters). DFSDM module supports the connection of up to 4 multiplexed
input digital serial channels which are shared with up to 4 DFSDM modules. DFSDM
module also supports alternative parallel data inputs from up to 4 internal 16-bit data
channels (from internal ADCs or from device memory).
DFSDM is converting an input data stream into a final digital data word which represents an
analog input value on a Σ∆ modulator analog input. The conversion is based on a
configurable digital process: the digital filtering and decimation of the input serial data
stream.
The conversion speed and resolution are adjustable according to configurable parameters
for digital processing: filter type, filter order, length of filter, integrator length. The maximum
output data resolution is up to 24 bits. There are two conversion modes: single conversion
mode and continuous mode. The data can be automatically stored in a system RAM buffer
through DMA, thus reducing the software overhead.
A flexible timer triggering system can be used to control the start of conversion of DFSDM.
This timing control is capable of triggering simultaneous conversions or inserting a
programmable delay between conversions.
DFSDM features an analog watchdog function. Analog watchdog can be assigned to any of
the input channel data stream or to final output data. Analog watchdog has its own digital
filtering of input data stream to reach the required speed and resolution of watched data.
To detect short-circuit in control applications, there is a short-circuit detector. This block
watches each input channel data stream for occurrence of stable data for a defined time
duration (several 0’s or 1’s in an input data stream).
An extremes detector block watches final output data and stores maximum and minimum
values from the output data values. The extremes values stored can be restarted by
software.
Two power modes are supported: normal mode and stop mode.

RM0438 Rev 8 863/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
26.2 DFSDM main features
• Up to 4 multiplexed input digital serial channels:
– configurable SPI interface to connect various Σ∆ modulators
– configurable Manchester coded 1 wire interface support
– clock output for Σ∆ modulator(s)
• Alternative inputs from up to 4 internal digital parallel channels:
– inputs with up to 16 bit resolution
– internal sources: ADCs data or me mory (CPU/DMA write) data streams
• Adjustable digital signal processing:
–S i n c x filter: filter order/type (1..5), oversampling ratio (up to 1..1024)
– integrator: oversampling ratio (1..256)
• Up to 24-bit output data resolution:
– right bit-shifter on final data (0..31 bits)
• Signed output data format
• Automatic data offset correction (offset stored in register by user)
• Continuous or single conversion
• Start-of-conversion synchronization with:
– software trigger
– internal timers
– external events
– start-of-conversion synchronously with first DFSDM filter (DFSDM_FLT0)
• Analog watchdog feature:
– low value and high value data threshold registers
– own configurable Sinc x digital filter (order = 1..3, oversampling ratio = 1..32)
– input from output data register or from one or more input digital serial channels
– continuous monitoring independently from standard conversion
• Short-circuit detector to detect saturated analog input values (bottom and top ranges):
– up to 8-bit counter to detect 1..256 c onsecutive 0’s or 1’s on input data stream
– monitoring continuously each channel (4 serial channel transceiver outputs)
• Break generation on analog watchdog event or short-circuit detector event
• Extremes detector:
– store minimum and maximum values of output data values
– refreshed by software
• Pulse skipper feature to support beamforming applications (delay line like behavior)
• DMA may be used to read the conversion data
• Interrupts: end of conversion, overrun, analog watchdog, short-circuit, channel clock
absence
• “regular” or “injected” conversions:
– “regular” conversions can be requested at  any time or even in continuous mode
without having any impact on the timing of “injected” conversions
– “injected” conversions for precise timi ng and with high conversion priority

Digital filter for sigma delta modulators (DFSDM) RM0438
864/2187 RM0438 Rev 8
26.3 DFSDM implementation
This section describes the configuration implemented in DFSDMx.
[Table 206](../tables/table_206.md). DFSDM1 implementation
DFSDM features DFSDM1
Number of channels 4
Number of filters 4
Input from internal ADC X
Supported trigger sources 32 (1)
1. Refer to [Table 209](../tables/table_209.md): DFSDM triggers connection for available trigger sources.
Pulses skipper X

RM0438 Rev 8 865/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
26.4 DFSDM functional description
26.4.1 DFSDM block diagram
[Figure 180](../figures/figure_180.md). Single DFSDM block diagram
1. This example shows 4 DFSD M filters and 4 input channels.
MSv47474V1
Control unit
Interrupt,
break
Interrupts and events:
1) end of conversion
2) analog watchdog
3) short circuit detection
4) overrun
Data output
Configuration
registers
DMA, interrupt, break
control, clock control
Filter 3
config
Analog watchdog 3
High threshold
Low threshold
Filter 0
config
Analog watchdog 0
High threshold
Low threshold
Extremes
detector 3
Maximum value
Minimum value
Extremes
detector 0
Maximum value
Minimum value
DFSDM data 3
Right bit-shift
count
Calibration data
correction unit
4 watchdog filters
4 watchdog comparatorsConfig
Status
Short circuit
detector 3
1's, 0's counter
threshold
Short circuit
detector 0
1's, 0's counter
threshold
Interrupt,
break
CKIN0
DATIN0
CKOUT
CKIN7
DATIN7 Sincx filter 3
Filter
order
Oversampling
ratio
Integrator unit 3
Oversampling
ratio
Sincx filter 0
Filter
order
Oversampling
ratio
Integrator unit 0
Oversampling
ratioClock 0
Data 0
16
Clock 3
Data 3
16
EXTRG[1:0]
DFSDM data 0
Right bit-shift
count
Calibration data
correction unit
Parallel input data
register 3
Sample 1 Sample 0
Parallel input data
register 0
Sample 1 Sample 0
ADC 0
ADC 3
APB bus
16
16
APB bus
Channel multiplexer
Pulse
skipper
Serial transceiver 3
Clock
control
Mode
control
Serial transceiver 0
Clock
control
Mode
control Pulse
skipper

Digital filter for sigma delta modulators (DFSDM) RM0438
866/2187 RM0438 Rev 8
26.4.2 DFSDM pins and internal signals
[Table 207](../tables/table_207.md). DFSDM external pins
Name Signal Type Remarks
VDD Power supply Digital power supply.
VSS Power supply Digital ground power supply.
CKIN[3:0] Clock input Clock signal provided from external Σ∆ modulator. FT input.
DATIN[3:0] Data input Data signal provided from external Σ∆ modulator. FT input.
CKOUT Clock output Clock output to provide clock signal into external Σ∆
modulator.
EXTRG[1:0] External trigger
signal
Input trigger from two EXTI signals to start analog
conversion (from GPIOs: EXTI11, EXTI15).
[Table 208](../tables/table_208.md). DFSDM internal signals
Name Signal Type Remarks
dfsdm_jtrg[31:0]
Internal/
external trigger
signal
Input trigger from internal/external trigger sources in order
to start analog conversion (from internal sources:
synchronous input, from external sources: asynchronous
input with synchronization). See [Table 209](../tables/table_209.md) for details.
dfsdm_break[3:0] break signal
output
Break signals event generation from Analog watchdog or
short-circuit detector
dfsdm_dma[3:0] DMA request
signal
DMA request signal from each DFSDM_FLTx (x=0..3):
end of injected conversion event.
dfsdm_it[3:0] Interrupt
request signal Interrupt signal for each DFSDM_FLTx (x=0..3)
dfsdm_dat_adc[15:0] ADC input
data Up to 4 internal ADC data buses as parallel inputs.
[Table 209](../tables/table_209.md). DFSDM triggers connection
Trigger name Trigger source
dfsdm_jtrg0 TIM1_TRGO
dfsdm_jtrg1 TIM1_TRGO2
dfsdm_jtrg2 TIM8_TRGO
dfsdm_jtrg3 TIM8_TRGO2
dfsdm_jtrg[23:9] Reserved
dfsdm_jtrg24 EXTI11
dfsdm_jtrg25 EXTI15
dfsdm_jtrg26 LPTIMER1
dfsdm_jtrg[31:27] Reserved

RM0438 Rev 8 867/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
26.4.3 DFSDM reset and clocks
DFSDM on-off control
The DFSDM interface is globally enabled by setting DFSDMEN=1 in the
DFSDM_CH0CFGR1 register. Once DFSDM is globally enabled, all input channels (y=0..3)
and digital filters DFSDM_FLTx (x=0..3) start to work if their enable bits are set (channel
enable bit CHEN in DFSDM_CHyCFGR1 and DFSDM_FLTx enable bit DFEN in
DFSDM_FLTxCR1).
Digital filter x DFSDM_FLTx (x=0..3) is enabled by setting DFEN=1 in the
DFSDM_FLTxCR1 register. Once DFSDM_FLTx is enabled (DFEN=1), both Sincx digital
filter unit and integrator unit are reinitialized.
By clearing DFEN, any conversion which may be in progress is immediately stopped and
DFSDM_FLTx is put into stop mode. All register settings remain unchanged except
DFSDM_FLTxAWSR and DFSDM_FLTxISR (which are reset).
Channel y (y=0..3) is enabled by setting CHEN=1 in the DFSDM_CHyCFGR1 register.
Once the channel is enabled, it receives serial data from the external Σ∆ modulator or
parallel internal data sources (ADCs or CPU/DMA wire from memory).
DFSDM must be globally disabled (by DFSDMEN=0 in DFSDM_CH0CFGR1) before
stopping the system clock to enter in the STOP mode of the device.
DFSDM clocks
The internal DFSDM clock fDFSDMCLK, which is used to drive the channel transceivers,
digital processing blocks (digital filter, integrator) and next additional blocks (analog
watchdog, short-circuit detector, extremes detector, control block) is generated by the RCC
block and is derived from the system clock SYSCLK or peripheral clock PCLK2 (see
Section 9.8.32: RCC peripherals independent clock configuration register 2
(RCC_CCIPR2)). The DFSDM clock is automatically stopped in stop mode (if DFEN = 0 for
all DFSDM_FLTx, x=0..3).
The DFSDM serial channel transceivers can receive an external serial clock to sample an
external serial data stream. The internal DFSDM clock must be at least 4 times faster than
the external serial clock if standard SPI coding is used, and 6 times faster than the external
serial clock if Manchester coding is used.
DFSDM can provide one external output clock signal to drive external Σ∆ modulator(s) clock
input(s). It is provided on CKOUT pin. This output clock signal must be in the range
specified in given device datasheet and is derived from DFSDM clock or from audio clock
(see CKOUTSRC bit in DFSDM_CH0CFGR1 register) by programmable divider in the
range 2 - 256 (CKOUTDIV in DFSDM_CH0CFGR1 register). The audio clock source is the
clock selected by RCC configuration (see ).
[Table 210](../tables/table_210.md). DFSDM break connection
Break name Break destination
dfsdm_break[0] TIM1/TIM15 break
dfsdm_break[1] TIM1 break2 / TIM16 break
dfsdm_break[2] TIM8/TIM17 break
dfsdm_break[3] TIM8 break2

Digital filter for sigma delta modulators (DFSDM) RM0438
868/2187 RM0438 Rev 8
26.4.4 Serial channel transceivers
There are 4 multiplexed serial data channels which can be selected for conversion by each
filter or Analog watchdog or Short-circuit detector. Those serial transceivers receive data
stream from external Σ∆ modulator. Data stream can be sent in SPI format or Manchester
coded format (see SITP[1:0] bits in DFSDM_CHyCFGR1 register).
The channel is enabled for operation by setting CHEN=1 in DFSDM_CHyCFGR1 register.
Channel inputs selection
Serial inputs (data and clock signals) from DATINy and CKINy pins can be redirected from
the following channel pins. This serial input channel redirection is set by CHINSEL bit in
DFSDM_CHyCFGR1 register.
Channel redirection can be used to collect audio data from PDM (pulse density modulation)
stereo microphone type. PDM stereo microphone has one data and one clock signal. Data
signal provides information for both left and right audio channel (rising clock edge samples
for left channel and falling clock edge samples for right channel).
Configuration of serial channels for PDM microphone input:
• PDM microphone signals (data, clock) will be connected to DFSDM input serial channel
y (DATINy, CKOUT) pins.
• Channel y will be configured: CHINSEL = 0 (input from given channel pins: DATINy,
CKINy).
• Channel (y-1) (modulo 4) will be configured: CHINSEL = 1 (input from the following
channel ((y-1)+1) pins: DATINy, CKINy).
• Channel y: SITP[1:0] = 0 (rising edge to strobe data) => left audio channel on channel
y.
• Channel (y-1): SITP[1:0] = 1 (falling edge to strobe data) => right audio channel on
channel y-1.
• Two DFSDM filters will be assigned to channel y and channel (y-1) (to filter left and
right channels from PDM microphone).

RM0438 Rev 8 869/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
[Figure 181](../figures/figure_181.md). Input channel pins redirection
Output clock generation
A clock signal can be provided on CKOUT pin to drive external Σ∆ modulator clock inputs.
The frequency of this CKOUT signal is derived from DFSDM clock or from audio clock (see
CKOUTSRC bit in DFSDM_CH0CFGR1 register) divided by a predivider (see CKOUTDIV
bits in DFSDM_CH0CFGR1 register). If the output clock is stopped, then CKOUT signal is
set to low state (output clock can be stopped by CKOUTDIV=0 in DFSDM_CHyCFGR1
register or by DFSDMEN=0 in DFSDM_CH0CFGR1 register). The output clock stopping is
performed:
• 4 system clocks after DFSDMEN is cleared (if CKOUTSRC=0)
• 1 system clock and 3 audio clocks after DFSDMEN is cleared (if CKOUTSRC=1)
Before changing CKOUTSRC the software has to wait for CKOUT being stopped to avoid
glitch on CKOUT pin. The output clock signal frequency must be in the range 0 - 20 MHz.
MSv41632V1
FLTx
FLT(x+1)
DATAIN0
DATIN(y-1)
DATINy
DATIN(ymax)
CHINSEL
RCH
FLT0
FLT(xmax)
CKIN(ymax)
CKINy
CKIN(y-1)
CKIN0
.
.
.
.
.
.
CH(ymax)Decode
CHyDecode
CH(y-1)Decode
.
.
.
CH0Decode
(. . .)
.
.
.
.
.
.
.
.
.
.
.
.
(. . .)
.
.
.

Digital filter for sigma delta modulators (DFSDM) RM0438
870/2187 RM0438 Rev 8
SPI data input format operation
In SPI format, the data stream is sent in serial format through data and clock signals. Data
signal is always provided from DATINy pin. A clock signal can be provided externally from
CKINy pin or internally from a signal derived from the CKOUT signal source.
In case of external clock source selection (SPICKSEL[1:0]=0) data signal (on DATINy pin) is
sampled on rising or falling clock edge (of CKINy pin) according SITP[1:0] bits setting (in
DFSDM_CHyCFGR1 register).
Internal clock sources - see SPICKSEL[1:0] in DFSDM_CHyCFGR1 register:
• CKOUT signal:
– For connection to external Σ∆ modulator which uses directly its clock input (from
CKOUT) to generate its output serial communication clock.
– Sampling point: on rising/fallin g edge according SITP[1:0] setting.
• CKOUT/2 signal (generated on CKOUT rising edge):
– For connection to external Σ∆ modulator which divides its clock input (from
CKOUT) by 2 to generate its output serial communication clock (and this output
clock change is active on each clock input rising edge).
– Sampling point: on each second CKOUT falling edge.
• CKOUT/2 signal (generated on CKOUT falling edge):
– For connection to external Σ∆ modulator which divides its clock input (from
CKOUT) by 2 to generate its output serial communication clock (and this output
clock change is active on each clock input falling edge).
– Sampling point: on each second CKOUT rising edge.
Note: An internal clock source can only be used when the external Σ∆ modulator uses CKOUT
signal as a clock input (to have synchronous clock and data operation).
Internal clock source usage can save CKINy pin connection (CKINy pins can be used for
other purpose).
The clock source signal frequency must be in the range 0 - 20 MHz for SPI coding and less
than fDFSDMCLK/4.
Manchester coded data input format operation
In Manchester coded format, the data stream is sent in serial format through DATINy pin
only. Decoded data and clock signal are recovered from serial stream after Manchester
decoding. There are two possible settings of Manchester codings (see SITP[1:0] bits in
DFSDM_CHyCFGR1 register):
• signal rising edge = log 0; signal falling edge = log 1
• signal rising edge = log 1; signal falling edge = log 0
The recovered clock signal frequency for Manchester coding must be in the range
0 - 10 MHz and less than fDFSDMCLK/6.
To correctly receive Manchester coded data, the CKOUTDIV divider (in
DFSDM_CH0CFGR1 register) must be set with respect to expected Manchester data rate
according formula:

RM0438 Rev 8 871/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
Where TINCKOUT is the input clock into CKOUT before division by CKOUTDIV divider.
CKOUTDIV 1+() TINCKOUT×() TManchester clock 2 CKOUTDIV× TINCKOUT×()<<

Digital filter for sigma delta modulators (DFSDM) RM0438
872/2187 RM0438 Rev 8
[Figure 182](../figures/figure_182.md). Channel transceiver timing diagrams
MS30766V3
SITP = 0
CKOUTDATINy
SITP = 1
tsu th
tsu th
tftrtwl twh
SPI timing : SPICKSEL = 1, 2, 3
recovered clock
SITP = 2
DATINy
SITP = 3
Manchester timing
recovered data 11000
SITP = 00
CKINyDATINy
SITP = 01
tsu th
tsu th
tftrtwl twh
SPI timing : SPICKSEL = 0
SPICKSEL=2
SPICKSEL=1
(SPICKSEL=0)
SPICKSEL=3

RM0438 Rev 8 873/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
Clock absence detection
Channels serial clock inputs can be checked for clock absence/presence to ensure the
correct operation of conversion and error reporting. Clock absence detection can be
enabled or disabled on each input channel y by bit CKABEN in DFSDM_CHyCFGR1
register. If enabled, then this clock absence detection is performed continuously on a given
channel. A clock absence flag is set (CKABF[y] = 1) and an interrupt can be invoked (if
CKABIE=1) in case of an input clock error (see CKABF[3:0] in DFSDM_FLT0ISR register
and CKABEN in DFSDM_CHyCFGR1). After a clock absence flag clearing (by CLRCKABF
in DFSDM_FLT0ICR register), the clock absence flag is refreshed. Clock absence status bit
CKABF[y] is set also by hardware when corresponding channel y is disabled (if CHEN[y] = 0
then CKABF[y] is held in set state).
When a clock absence event has occurred, the data conversion (and/or analog watchdog
and short-circuit detector) provides incorrect data. The user should manage this event and
discard given data while a clock absence is reported.
The clock absence feature is available only when the system clock is used for the CKOUT
signal (CKOUTSRC=0 in DFSDM_CH0CFGR1 register).
When the transceiver is not yet synchronized, the clock absence flag is set and cannot be
cleared by CLRCKABF[y] bit (in DFSDM_FLT0ICR register). The software sequence
concerning clock absence detection feature should be:
• Enable given channel by CHEN = 1
• Try to clear the clock absence flag (by CLRCKABF = 1) until the clock absence flag is
really cleared (CKABF = 0). At this time, the transceiver is synchronized (signal clock is
valid) and is able to receive data.
• Enable the clock absence feature CKABEN = 1 and the associated interrupt CKABIE =
1 to detect if the SPI clock is lost or Manchester data edges are missing.
If SPI data format is used, then the clock absence detection is based on the comparison of
an external input clock with an output clock generation (CKOUT signal). The external input
clock signal into the input channel must be changed at least once per 8 signal periods of
CKOUT signal (which is controlled by CKOUTDIV field in DFSDM_CH0CFGR1 register).
[Figure 183](../figures/figure_183.md). Clock absence timing diagram for SPI
If Manchester data format is used, then the clock absence means that the clock recovery is
unable to perform from Manchester coded signal. For a correct clock recovery, it is first
necessary to receive data with 1 to 0 or 0 to 1 transition (see [Figure 185](../figures/figure_185.md) for Manchester
synchronization).
MS30767V2
CKOUT
SPI clock presence
timing
01234567
max. 8 periods
CKINy
last clock change
CKABF[y]
error reported
restart counting
20

Digital filter for sigma delta modulators (DFSDM) RM0438
874/2187 RM0438 Rev 8
The detection of a clock absence in Manchester coding (after a first successful
synchronization) is based on changes comparison of coded serial data input signal with
output clock generation (CKOUT signal). There must be a voltage level change on DATINy
pin during 2 periods of CKOUT signal (which is controlled by CKOUTDIV bits in
DFSDM_CH0CFGR1 register). This condition also defines the minimum data rate to be able
to correctly recover the Manchester coded data and clock signals.
The maximum data rate of Manchester coded data must be less than the CKOUT signal.
So to correctly receive Manchester coded data, the CKOUTDIV divider must be set
according the formula:
Where TINCKOUT is the input clock into CKOUT before division by CKOUTDIV divider.
A clock absence flag is set (CKABF[y] = 1) and an interrupt can be invoked (if CKABIE=1) in
case of an input clock recovery error (see CKABF[3:0] in DFSDM_FLT0ISR register and
CKABEN in DFSDM_CHyCFGR1). After a clock absence flag clearing (by CLRCKABF in
DFSDM_FLT0ICR register), the clock absence flag is refreshed.
[Figure 184](../figures/figure_184.md). Clock absence timing diagram for Manchester coding
CKOUTDIV 1+() TINCKOUT×() TManchester clock 2 CKOUTDIV× TINCKOUT×()<<
MS30768V2
CKOUT
recovered clock
SITP = 2
DATINy
SITP = 3
Manchester clock presence
timing
recovered data 1??00
01
last data change
CKABF[y]
error reported
restart counting
max. 2 periods
000

RM0438 Rev 8 875/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
Manchester/SPI code synchronization
The Manchester coded stream must be synchronized the first time after enabling the
channel (CHEN=1 in DFSDM_CHyCFGR1 register). The synchronization ends when a data
transition from 0 to 1 or from 1 to 0 (to be able to detect valid data edge) is received. The
end of the synchronization can be checked by polling CKABF[y]=0 for a given channel after
it has been cleared by CLRCKABF[y] in DFSDM_FLT0ICR, following the software sequence
detailed hereafter:
CKABF[y] flag is cleared by setting CLRCKABF[y] bit. If channel y is not yet synchronized
the hardware immediately set the CKABF[y] flag. Software is then reading back the
CKABF[y] flag and if it is set then perform again clearing of this flag by setting
CLRCKABF[y] bit. This software sequence (polling of CKABF[y] flag) continues until
CKABF[y] flag is set (signalizing that Manchester stream is synchronized). To be able to
synchronize/receive Manchester coded data the CKOUTDIV divider (in
DFSDM_CH0CFGR1 register) must be set with respect to expected Manchester data rate
according the formula below.
Where TINCKOUT is the input clock into CKOUT before division by CKOUTDIV divider.
SPI coded stream is synchronized after first detection of clock input signal (valid
rising/falling edge).
Note: When the transceiver is not yet synchronized, the clock absence flag is set and cannot be
cleared by CLRCKABF[y] bit (in DFSDM_FLT0ICR register).
CKOUTDIV 1+() TINCKOUT×() TManchester clock 2 CKOUTDIV× TINCKOUT×()<<

Digital filter for sigma delta modulators (DFSDM) RM0438
876/2187 RM0438 Rev 8
[Figure 185](../figures/figure_185.md). First conversion for Manchester coding (Manchester synchronization)
External serial clock frequency measurement
The measuring of a channel serial clock input frequency provides a real data rate from an
external Σ∆ modulator, which is important for application purposes.
An external serial clock input frequency can be measured by a timer counting DFSDM
clocks (fDFSDMCLK) during one conversion duration. The counting starts at the first input data
clock after a conversion trigger (regular or injected) and finishes by last input data clock
before conversion ends (end of conversion flag is set). Each conversion duration (time
between first serial sample and last serial sample) is updated in counter CNVCNT[27:0] in
register DFSDM_FLTxCNVTIMR when the conversion finishes (JEOCF=1 or REOCF=1).
The user can then compute the data rate according to the digital filter settings (FORD,
FOSR, IOSR, FAST). The external serial frequency measurement is stopped only if the filter
is bypassed (FOSR=0, only integrator is active, CNVCNT[27:0]=0 in
DFSDM_FLTxCNVTIMR register).
In case of parallel data input (Section 26.4.6: Parallel data inputs) the measured frequency
is the average input data rate during one conversion.
MS30769V2
recovered clock
SITP = 2
DATINy
SITP = 3
Manchester timing
data from
modulator 11000
CHEN
first data bit toggle - end of Manchester synchronization
first conversion
start trigger
recovered data 110??
real start of first conversion
CKABF[y]
clearing of CKABF[y] flag by software polling

RM0438 Rev 8 877/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
Note: When conversion is interrupted (e.g. by disabling/enabling the selected channel) the
interruption time is also counted in CNVCNT[27:0]. Therefore it is recommended to not
interrupt the conversion for correct conversion duration result.
Conversion times:
injected conversion or regular conversion with FAST = 0 (or first conversion if
FAST=1):
for Sincx filters (x=1..5):
t = CNVCNT/fDFSDMCLK = [FOSR * (IOSR-1 + FORD) + FORD] / fCKIN
for FastSinc filter:
t = CNVCNT/fDFSDMCLK = [FOSR * (IOSR-1 + 4) + 2] / fCKIN
regular conversion with FAST = 1 (except first conversion):
for Sincx and FastSinc filters:
t = CNVCNT/fDFSDMCLK = [FOSR * IOSR] / fCKIN
in case if FOSR = FOSR[9:0]+1 = 1 (filter bypassed, active only integrator):
t = IOSR / fCKIN (... but CNVCNT=0)
where:
• fCKIN is the channel input clock frequency (on given channel CKINy pin) or input data
rate (in case of parallel data input)
• FOSR is the filter oversampling ratio: FOSR = FOSR[9:0]+1 (see DFSDM_FLTxFCR
register)
• IOSR is the integrator oversampling ratio: IOSR = IOSR[7:0]+1 (see DFSDM_FLTxFCR
register)
• FORD is the filter order: FORD = FORD[2:0] (see DFSDM_FLTxFCR register)
Channel offset setting
Each channel has its own offset setting (in register) which is finally subtracted from each
conversion result (injected or regular) from a given channel. Offset correction is performed
after the data right bit shift. The offset is stored as a 24-bit signed value in OFFSET[23:0]
field in DFSDM_CHyCFGR2 register.
Data right bit shift
To have the result aligned to a 24-bit value, each channel defines a number of right bit shifts
which will be applied on each conversion result (injected or regular) from a given channel.
The data bit shift number is stored in DTRBS[4:0] bits in DFSDM_CHyCFGR2 register.
The right bit-shift is rounding the result to nearest integer value. The sign of shifted result is
maintained, in order to have valid 24-bit signed format of result data.
Pulses skipper
Purpose of the pulses skipper is to implement delay line like behavior for given input
channel(s). Given number of samples from input serial data stream (serial stream only) can
be discarded before they enter into the filter. This data discarding is performed by skipping
given number of sampling input clock pulses (given serial data samples are then not
sampled by filter). The sampling clock is gated by pulses skipper function for given number
of clock pulses. When given clock pulses are skipped then the filtering continues for
following input data. With comparison to non skipped data stream this operation causes that

Digital filter for sigma delta modulators (DFSDM) RM0438
878/2187 RM0438 Rev 8
the final output sample (and next samples) from filter will be calculated from later input data.
This final sample then looks a bit in forward - because it is calculated from newer input
samples than the “non-skipped” sample. The final “skipped sample” is converted later
because the skipped input data samples must be replaced by followed input data samples.
The final data buffers behavior (skipped and non-skipped output data buffers comparison)
looks like the non-skipped data stream is a bit delayed - both data buffers will be phase
shifted.
Number of clock pulses to be skipped should be written into PLSSKP[5:0] field in
DFSDM_CHyDLYR register. Once PLSSKP[5:0] field is written the execution of pulses
skipping is started on given channel. PLSSKP[5:0] field can be read in order to check the
progress of pulses skipper. When PLSSKP[5:0]=0 means that pulses skipping has been
executed.
Up to 63 clock pulses can be skip with a single write operation into PLSSKP[5:0]. If more
pulses need to be skipped, then user has to write several times into the PLSSKP[5:0] field.
The application software should handle cumulative skipped clock number per each filter.
26.4.5 Configuring the input serial interface
The following parameters must be configured for the input serial interface:
• Output clock predivider. There is a programmable predivider to generate the output
clock from DFSDM clock (2 - 256). It is defined by CKOUTDIV[7:0] bits in
DFSDM_CH0CFGR1 register.
• Serial interface type and input clock phase. Selection of SPI or Manchester coding
and sampling edge of input clock. It is defined by SITP [1:0] bits in
DFSDM_CHyCFGR1 register.
• Input clock source. External source from CKINy pin or internal from CKOUT pin. It is
defined by SPICKSEL[1:0] field in DFSDM_CHyCFGR1 register.
• Final data right bit-shift. Defines the final data right bit shift to have the result aligned
to a 24-bit value. It is defined by DTRBS[4:0] in DFSDM_CHyCFGR2 register.
• Channel offset per channel. Defines the analog offset of a given serial channel (offset
of connected external Σ∆ modulator). It is defined by OFFSET[23:0] bits in
DFSDM_CHyCFGR2 register.
• short-circuit detector and clock absence per channel enable. To enable or disable
the short-circuit detector (by SCDEN bit) and the clock absence monitoring (by
CKABEN bit) on a given serial channel in register DFSDM_CHyCFGR1.
• Analog watchdog filter and short-circuit detector threshold settings. To configure
channel analog watchdog filter parameters and channel short-circuit detector
parameters. Configurations are defined in DFSDM_CHyAWSCDR register.
26.4.6 Parallel data inputs
Each input channel provides a register for 16-bit parallel data input (besides serial data
input). Each 16-bit parallel input can be sourced from internal data sources only:
• internal ADC results
• direct CPU/DMA writing.
The selection for using serial or parallel data input for a given channel is done by field
DATMPX[1:0] of DFSDM_CHyCFGR1 register. In DATMPX[1:0] is also defined the parallel
data source: internal ADC or direct write by CPU/DMA.

RM0438 Rev 8 879/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
Each channel contains a 32-bit data input register DFSDM_CHyDATINR in which it can be
written a 16-bit data. Data are in 16-bit signed format. Those data can be used as input to
the digital filter which is accepting 16-bit parallel data.
If serial data input is selected (DATMPX[1:0] = 0), the DFSDM_CHyDATINR register is write
protected.
Input from internal ADC
In case of ADC data parallel input (DATMPX[1:0]=1) the ADC[y+1] result is assigned to
channel y input (ADC1 is filling DFSDM_CHDATIN0R register, ADC2 is filling
DFSDM_CHDATIN1R register, ... , ADC8 is filling DFSDM_CHDATIN7R register). End of
conversion event from ADC[y+1] causes update of channel y data (parallel data from
ADC[y+1] are put as next sample to digital filter). Data from ADC[y+1] is written into
DFSDM_CHyDATINR register (field INDAT0[15:0]) when end of conversion event occurred.
The setting of data packing mode (DATPACK[1:0] in the DFSDM_CHyCFGR1 register) has
no effect in case of ADC data input.
Note: Extension of ADC specification:  in case the internal ADC is configured in interleaved mode
(e.g. ADC1 together with ADC2 - see ADC specification) then each result from ADC1 or
from ADC2 will come to the same 16-bit bus - to the bus of ADC1 - which is coming into
DFSDM channel 0 (fixed connection). So there will be double input data rate into DFSDM
channel 0 (even samples come from ADC1 and odd samples from ADC2). Channel 1
associated with ADC2 will be free.
Input from memory (direct CPU/DMA write)
The direct data write into DFSDM_CHyDATINR register by CPU or DMA (DATMPX[1:0]=2)
can be used as data input in order to process digital data streams from memory or
peripherals.
Data can be written by CPU or DMA into DFSDM_CHyDATINR register:
1. CPU data write:
Input data are written directly by CPU into DFSDM_CHyDATINR register.
2. DMA data write:
The DMA should be configured in memory-to-memory transfer mode to transfer data
from memory buffer into DFSDM_CHyDATINR register. The destination memory
address is the address of DFSDM_CHyDATINR register. Data are transferred at DMA
transfer speed from memory to DFSDM parallel input.
This DMA transfer is different from DMA used to read DFSDM conversion results. Both
DMA can be used at the same time - first DMA (configured as memory-to-memory
transfer) for input data writings and second DMA (configured as peripheral-to-memory
transfer) for data results reading.
The accesses to DFSDM_CHyDATINR can be either 16-bit or 32-bit wide, allowing to load
respectively one or two samples in one write operation. 32-bit input data register
(DFSDM_CHyDATINR) can be filled with one or two 16-bit data samples, depending on the
data packing operation mode defined in field DATPACK[1:0] of DFSDM_CHyCFGR1
register:
1. Standard mode (DATPACK[1:0]=0):
Only one sample is stored in field INDAT0[15:0] of DFSDM_CHyDATINR register which
is used as input data for channel y. The upper 16 bits (INDAT1[15:0]) are ignored and
write protected. The digital filter must perform one input sampling (from INDAT0[15:0])

Digital filter for sigma delta modulators (DFSDM) RM0438
880/2187 RM0438 Rev 8
to empty data register after it has been filled by CPU/DMA. This mode is used together
with 16-bit CPU/DMA access to DFSDM_CHyDATINR register to load one sample per
write operation.
2. Interleaved mode (DATPACK[1:0]=1):
DFSDM_CHyDATINR register is used as a two sample buffer. The first sample is
stored in INDAT0[15:0] and the second sample is stored in INDAT1[15:0]. The digital
filter must perform two input samplings from channel y to empty DFSDM_CHyDATINR
register. This mode is used together with 32-bit CPU/DMA access to
DFSDM_CHyDATINR register to load two samples per write operation.
3. Dual mode (DATPACK[1:0]=2):
Two samples are written into DFSDM_CHyDATINR register. The data INDAT0[15:0] is
for channel y, the data in INDAT1[15:0] is for channel y+1. The data in INDAT1[15:0] is
automatically copied INDAT0[15:0] of the following (y+1) channel data register
DFSDM_CH[y+1]DATINR). The digital filters must perform two samplings - one from
channel y and one from channel (y+1) - in order to empty DFSDM_CHyDATINR
registers.
Dual mode setting (DATPACK[1:0]=2) is available only on even channel numbers (y =
0, 2). If odd channel (y = 1, 3) is set to Dual mode then both INDAT0[15:0] and
INDAT1[15:0] parts are write protected for this channel. If even channel is set to Dual
mode then the following odd channel must be set into Standard mode
(DATPACK[1:0]=0) for correct cooperation with even channels.
See [Figure 186](../figures/figure_186.md) for DFSDM_CHyDATINR registers data modes and assignments of data
samples to channels.
[Figure 186](../figures/figure_186.md). DFSDM_CHyDATINR registers operation modes and assignment
The write into DFSDM_CHyDATINR register to load one or two samples must be performed
after the selected input channel (channel y) is enabled for data collection (starting
conversion for channel y). Otherwise written data are lost for next processing.
For example: for single conversion and interleaved mode, do not start writing pair of data
samples into DFSDM_CHyDATINR before the single conversion is started (any data
present in the DFSDM_CHyDATINR before starting a conversion is discarded).
26.4.7 Channel selection
There are 4 multiplexed channels which can be selected for conversion using the injected
channel group and/or using the regular channel.
The injected channel group is a selection of any or all of the 4 channels. JCHG[3:0] in the
DFSDM_FLTxJCHGR register selects the channels of the injected group, where JCHG[y]=1
means that channel y is selected.
MSv40123V1
Ch1 (sample 0) Ch0 (sample 0)
Unused Ch1 (sample 0)
Ch3 (sample 0) Ch2 (sample 0)
Unused Ch3 (sample 0)
y = 0
y = 1
y = 2
y = 3
0151631
Ch0 (sample 1) Ch0 (sample 0)
Ch1 (sample 1) Ch1 (sample 0)
Ch2 (sample 1) Ch2 (sample 0)
Ch3 (sample 1) Ch3 (sample 0)
0151631
Unused Ch0 (sample 0)
Unused Ch1 (sample 0)
Unused Ch2 (sample 0)
Unused Ch3 (sample 0)
0151631
Standard mode Interleaved mode Dual mode

RM0438 Rev 8 881/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
Injected conversions can operate in scan mode (JSCAN=1) or single mode (JSCAN=0). In
scan mode, each of the selected channels is converted, one after another. The lowest
channel (channel 0, if selected) is converted first, followed immediately by the next higher
channel until all the channels selected by JCHG[3:0] have been converted. In single mode
(JSCAN=0), only one channel from the selected channels is converted, and the channel
selection is moved to the next channel. Writing to JCHG[3:0] if JSCAN=0 resets the channel
selection to the lowest selected channel.
Injected conversions can be launched by software or by a trigger. They are never
interrupted by regular conversions.
The regular channel is a selection of just one of the 4 channels. RCH[1:0] in the
DFSDM_FLTxCR1 register indicates the selected channel.
Regular conversions can be launched only by software (not by a trigger). A sequence of
continuous regular conversions is temporarily interrupted when an injected conversion is
requested.
Performing a conversion on a disabled channel (CHEN=0 in DFSDM_CHyCFGR1 register)
causes that the conversion will never end - because no input data is provided (with no clock
signal). In this case, it is necessary to enable a given channel (CHEN=1 in
DFSDM_CHyCFGR1 register) or to stop the conversion by DFEN=0 in DFSDM_FLTxCR1
register.
26.4.8 Digital filt er configuration
DFSDM contains a Sincx type digital filter implementation. This Sincx filter performs an input
digital data stream filtering, which results in decreasing the output data rate (decimation)
and increasing the output data resolution. The Sincx digital filter is configurable in order to
reach the required output data rates and required output data resolution. The configurable
parameters are:
• Filter order/type: (see FORD[2:0] bits in DFSDM_FLTxFCR register):
–F a s t S i n c
–S i n c 1
–S i n c 2
–S i n c 3
–S i n c 4
–S i n c 5
• Filter oversampling/decimation ratio (see FOSR[9:0] bits in DFSDM_FLTxFCR
register):
– FOSR = 1-1024 -  for FastSinc filter and Sinc x filter x = FORD = 1..3
– FOSR = 1-215 -  for Sinc x filter x = FORD = 4
– FOSR = 1-73 -  for Sinc x filter x = FORD = 5
The filter has the following transfer function (impulse response in H domain):
• Sincx filter type:
• FastSinc filter type:
Hz() 1z FOSR––
1z 1––
-----------------------------
⎝⎠
⎜⎟
⎛⎞ x
=
Hz() 1z FOSR––
1z 1––
-----------------------------
⎝⎠
⎜⎟
⎛⎞ 2
1z 2F O S R⋅()–+()⋅=

Digital filter for sigma delta modulators (DFSDM) RM0438
882/2187 RM0438 Rev 8
[Figure 187](../figures/figure_187.md). Example: Sinc3 filter response
For more information about Sinc filter type properties and usage, it is recommended to study
the theory about digital filters (more resources can be downloaded from internet).
26.4.9 Integrator unit
The integrator performs additional decimation and a resolution increase of data coming from
the digital filter. The integrator simply performs the sum of data from a digital filter for a given
number of data samples from a filter.
The integrator oversampling ratio parameter defines how many data counts will be summed
to one data output from the integrator. IOSR can be set in the range 1-256 (see IOSR[7:0]
bits description in DFSDM_FLTxFCR register).
[Table 211](../tables/table_211.md). Filter maximum output resolution (peak data values from filter output)
for some FOSR values
FOSR Sinc 1 Sinc2 FastSinc Sinc 3 Sinc4 Sinc5
x +/- x +/- x 2  +/- 2x2  +/- x3 +/- x4  +/- x5
4 +/- 4 +/- 16 +/- 32 +/- 64 +/- 256 +/- 1024
8 +/- 8 +/- 64 +/- 128 +/- 512 +/- 4096 -
32 +/- 32 +/- 1024 +/- 2048 +/- 32768 +/- 1048576 +/- 33554432
64 +/- 64 +/- 4096 +/- 8192 +/- 262144 +/- 16777216 +/- 1073741824
128 +/- 128 +/- 16384 +/- 32768 +/- 2097152 +/- 268435456
256 +/- 256 +/- 65536 +/- 131072 +/- 16777216 Result can overflow on full scale
input (> 32-bit signed integer)1024 +/- 1024 +/- 1048576 +/- 2097152 +/- 1073741824
Normalized frequency (fIN/fDATA)
Gain (dB)
MS30770V1

RM0438 Rev 8 883/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
26.4.10 Analog watchdog
The analog watchdog purpose is to trigger an external signal (break or interrupt) when an
analog signal reaches or crosses given maximum and minimum threshold values. An
interrupt/event/break generation can then be invoked.
Each analog watchdog will supervise serial data receiver outputs (after the analog watchdog
filter on each channel) or data output register (current injected or regular conversion result)
according to AWFSEL bit setting (in DFSDM_FLTxCR1 register). The input channels to be
monitored or not by the analog watchdog x will be selected by AWDCH[3:0] in
DFSDM_FLTxCR2 register.
Analog watchdog conversions on input channels are independent from standard
conversions. In this case, the analog watchdog uses its own filters and signal processing on
each input channel independently from the main injected or regular conversions. Analog
watchdog conversions are performed in a continuous mode on the selected input channels
in order to watch channels also when main injected or regular conversions are paused
(RCIP = 0, JCIP = 0).
There are high and low threshold registers which are compared with given data values (set
by AWHT[23:0] bits in DFSDM_FLTxAWHTR register and by AWLT[23:0] bits in
DFSDM_FLTxAWLTR register).
[Table 212](../tables/table_212.md). Integrator maximum output resolution (peak data values from integrator
output) for some IOSR values and FOSR = 256 and Sinc3 filter type (largest data)
IOSR Sinc 1 Sinc2 FastSinc Sinc 3 Sinc4 Sinc5
x +/- FOSR. x +/- FOSR 2. x +/- 2.FOSR 2. x +/- FOSR 3. x +/- FOSR 4. x +/- FOSR 5. x
4 - - - +/- 67 108 864 - -
32 - - - +/- 536 870 912 - -
128 - - - +/- 2 147 483
648 --
256 - - - +/- 2 32 --

Digital filter for sigma delta modulators (DFSDM) RM0438
884/2187 RM0438 Rev 8
There are 2 options for comparing the threshold registers with the data values
• Option1: in this case, the input data are taken from final output data register
(AWFSEL=0). This option is characterized by:
– high input data resolution (up to 24-bits)
– slow response time - inappropriate for fast response applications like overcurrent
detection
– for the comparison the final data are taken after bit shifting and offset data
correction
– final data are available only after main regular or injected conversions are
performed
– can be used in case of parallel input data source (DATMPX[1:0] ≠ 0 in
DFSDM_CHyCFGR1 register)
• Option2: in this case, the input data are taken from any serial data receivers output
(AWFSEL=1). This option is characterized by:
– input serial data are processed by dedicated analog watchdog Sinc x channel
filters with configurable oversampling ratio (1..32) and filter order (1..3) (see
AWFOSR[4:0] and AWFORD[1:0] bits setting in DFSDM_CHyAWSCDR register)
– lower resolution (up to 16-bit)
– fast response time - appropriate for applications which require a fast response like
overcurrent/overvoltage detection)
– data are available in continuous mode inde pendently from main regular or injected
conversions activity
In case of input channels monitoring (AWFSEL=1), the data for comparison to threshold is
taken from channels selected by AWDCH[3:0] field (DFSDM_FLTxCR2 register). Each of
the selected channels filter result is compared to one threshold value pair (AWHT[23:0] /
AWLT[23:0]). In this case, only higher 16 bits (AWHT[23:8] / AWLT[23:8]) define the 16-bit
threshold compared with the analog watchdog filter output because data coming from the
analog watchdog filter is up to a 16-bit resolution. Bits AWHT[7:0] / AWLT[7:0] are not taken
into comparison in this case (AWFSEL=1).
Parameters of the analog watchdog filter configuration for each input channel are set in
DFSDM_CHyAWSCDR register (filter order AWFORD[1:0] and filter oversampling ratio
AWFOSR[4:0]).
Each input channel has its own comparator which compares the analog watchdog data
(from analog watchdog filter) with analog watchdog threshold values (AWHT/AWLT). When
several channels are selected (field AWDCH[3:0] field of DFSDM_FLTxCR2 register),
several comparison requests may be received simultaneously. In this case, the channel
request with the lowest number is managed first and then continuing to higher selected
channels. For each channel, the result can be recorded in a separate flag (fields
AWHTF[3:0], AWLTF[3:0] of DFSDM_FLTxAWSR register). Each channel request is
executed in 8 DFSDM clock cycles. So, the bandwidth from each channel is limited to 8
DFSDM clock cycles (if AWDCH[3:0] = 0x0F). Because the maximum input channel
sampling clock frequency is the DFSDM clock frequency divided by 4, the configuration
AWFOSR = 0 (analog watchdog filter is bypassed) cannot be used for analog watchdog
feature at this input clock speed. Therefore user must properly configure the number of
watched channels and analog watchdog filter parameters with respect to input sampling
clock speed and DFSDM frequency.

RM0438 Rev 8 885/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
Analog watchdog filter data for given channel y is available for reading by firmware on field
WDATA[15:0] in DFSDM_CHyWDATR register. That analog watchdog filter data is
converted continuously (if CHEN=1 in DFSDM_CHyCFGR1 register) with the data rate
given by the analog watchdog filter setting and the channel input clock frequency.
The analog watchdog filter conversion works like a regular Fast Continuous Conversion
without the intergator. The number of serial samples needed for one result from analog
watchdog filter output (at channel input clock frequency fCKIN):
first conversion:
for Sincx filters (x=1..5): number of samples = [FOSR * FORD + FORD + 1]
for FastSinc filter: number of samples = [FOSR * 4 + 2 + 1]
next conversions:
for Sincx and FastSinc filters: number of samples = [FOSR * IOSR]
where:
FOSR ....... filter oversampling ratio: FOSR = AWFOSR[4:0]+1 (see DFSDM_CHyAWSCDR
register)
FORD ....... the filter order: FORD = AWFORD[1:0] (see DFSDM_CHyAWSCDR register)
In case of output data register monitoring (AWFSEL=0), the comparison is done after a right
bit shift and an offset correction of final data (see OFFSET[23:0] and DTRBS[4:0] fields in
DFSDM_CHyCFGR2 register). A comparison is performed after each injected or regular
end of conversion for the channels selected by AWDCH[3:0] field (in DFSDM_FLTxCR2
register).
The status of an analog watchdog event is signalized in DFSDM_FLTxAWSR register where
a given event is latched. AWHTF[y]=1 flag signalizes crossing AWHT[23:0] value on
channel y. AWLTF[y]=1 flag signalizes crossing AWLT[23:0] value on channel y. Latched
events in DFSDM_FLTxAWSR register are cleared by writing ‘1’ into the corresponding
clearing bit CLRAWHTF[y] or CLRAWLTF[y] in DFSDM_FLTxAWCFR register.
The global status of an analog watchdog is signalized by the AWDF flag bit in
DFSDM_FLTxISR register (it is used for the fast detection of an interrupt source). AWDF=1
signalizes that at least one watchdog occurred (AWHTF[y]=1 or AWLTF[y]=1 for at least one
channel). AWDF bit is cleared when all AWHTF[3:0] and AWLTF[3:0] are cleared.
An analog watchdog event can be assigned to break output signal. There are four break
outputs to be assigned to a high or low threshold crossing event (dfsdm_break[3:0]). The
break signal assignment to a given analog watchdog event is done by BKAWH[3:0] and
BKAWL[3:0] fields in DFSDM_FLTxAWHTR and DFSDM_FLTxAWLTR register.
26.4.11 Short-circuit detector
The purpose of a short-circuit detector is to signalize with a very fast response time if an
analog signal reached saturated values (out of full scale ranges) and remained on this value
given time. This behavior can detect short-circuit or open circuit errors (e.g. overcurrent or
overvoltage). An interrupt/event/break generation can be invoked.
Input data into a short-circuit detector is taken from channel transceiver outputs.
There is an upcounting counter on each input channel which is counting consecutive 0’s or
1’s on serial data receiver outputs. A counter is restarted if there is a change in the data
stream received - 1 to 0 or 0 to 1 change of data signal. If this counter reaches a short-circuit
threshold register value (SCDT[7:0] bits in DFSDM_CHyAWSCDR register), then a short-

Digital filter for sigma delta modulators (DFSDM) RM0438
886/2187 RM0438 Rev 8
circuit event is invoked. Each input channel has its short-circuit detector. Any channel can
be selected to be continuously monitored by setting the SCDEN bit (in DFSDM_CHyCFGR1
register) and it has its own short-circuit detector settings (threshold value in SCDT[7:0] bits,
status bit SCDF[3:0], status clearing bits CLRSCDF[3:0]). Status flag SCDF[y] is cleared
also by hardware when corresponding channel y is disabled (CHEN[y] = 0).
On each channel, a short-circuit detector event can be assigned to break output signal
dfsdm_break[3:0]. There are four break outputs to be assigned to a short-circuit detector
event. The break signal assignment to a given channel short-circuit detector event is done
by BKSCD[3:0] field in DFSDM_CHyAWSCDR register.
Short circuit detector cannot be used in case of parallel input data channel selection
(DATMPX[1:0] ≠ 0 in DFSDM_CHyCFGR1 register).
Four break outputs are totally available (shared with the analog watchdog function).
26.4.12 Extreme detector
The purpose of an extremes detector is to collect the minimum and maximum values of final
output data words (peak to peak values).
If the output data word is higher than the value stored in the extremes detector maximum
register (EXMAX[23:0] bits in DFSDM_FLTxEXMAX register), then this register is updated
with the current output data word value and the channel from which the data is stored is in
EXMAXCH[1:0] bits (in DFSDM_FLTxEXMAX register) .
If the output data word is lower than the value stored in the extremes detector minimum
register (EXMIN[23:0] bits in DFSDM_FLTxEXMIN register), then this register is updated
with the current output data word value and the channel from which the data is stored is in
EXMINCH[1:0] bits (in DFSDM_FLTxEXMIN register).
The minimum and maximum register values can be refreshed by software (by reading given
DFSDM_FLTxEXMAX or DFSDM_FLTxEXMIN register). After refresh, the extremes
detector minimum data register DFSDM_FLTxEXMIN is filled with 0x7FFFFF (maximum
positive value) and the extremes detector maximum register DFSDM_FLTxEXMAX is filled
with 0x800000 (minimum negative value).
The extremes detector performs a comparison after a right bit shift and an offset data
correction. For each extremes detector, the input channels to be considered into computing
the extremes value are selected in EXCH[3:0] bits (in DFSDM_FLTxCR2 register).
26.4.13 Data unit block
The data unit block is the last block of the whole processing path: External Σ∆ modulators -
Serial transceivers - Sinc filter - Integrator - Data unit block.
The output data rate depends on the serial data stream rate, and filter and integrator
settings. The maximum output data rate is:
Datarate samples s ⁄ fCKIN
FOSR IOSR 1– FORD+() FORD 1+()+⋅----------------------------------------------------------------------------------------------------------= ...FAST = 0, Sincx filter
Datarate samples s ⁄ fCKIN
FOSR IOSR 1– 4+() 21+()+⋅-----------------------------------------------------------------------------------= ...FAST = 0, FastSinc filter

RM0438 Rev 8 887/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
or
Maximum output data rate in case of parallel data input:
or
or
The right bit-shift of final data is performed in this module because the final data width is 24-
bit and data coming from the processing path can be up to 32 bits. This right bit-shift is
configurable in the range 0-31 bits for each selected input channel (see DTRBS[4:0] bits in
DFSDM_CHyCFGR2 register). The right bit-shift is rounding the result to nearest integer
value. The sign of shifted result is maintained - to have valid 24-bit signed format of result
data.
In the next step, an offset correction of the result is performed. The offset correction value
(OFFSET[23:0] stored in register DFSDM_CHyCFGR2) is subtracted from the output data
for a given channel. Data in the OFFSET[23:0] field is set by software by the appropriate
calibration routine.
Due to the fact that all operations in digital processing are performed on 32-bit signed
registers, the following conditions must be fulfilled not to overflow the result:
FOSR FORD . IOSR <= 2 31 ... for Sinc x filters, x = 1..5)
2 . FOSR 2 . IOSR <= 2 31 ... for FastSinc filter)
Note: In case of filter and integrator bypass (I OSR[7:0]=0, FOSR[9:0]=0), the input data rate
(fDATAIN_RATE) must be limited to be able to read all output data:
fDATAIN_RATE ≤ fAPB
where fAPB is the bus frequency to which the DFSDM peripheral is connected.
26.4.14 Signed data format
Each DFSDM input serial channel can be connected to one external Σ∆ modulator. An
external Σ∆ modulator can have 2 differential inputs (positive and negative) which can be
used for a differential or single-ended signal measurement.
A Σ∆ modulator output is always assumed in a signed format (a data stream of zeros and
ones from a Σ∆ modulator represents values -1 and +1).
Datarate samples s ⁄ fCKIN
FOSR IOSR⋅----------------------------------= ...FAST = 1
Datarate samples s ⁄ fDATAIN_RATE
FOSR IOSR 1– FORD+() FORD 1+()+⋅----------------------------------------------------------------------------------------------------------= ...FAST = 0, Sincx filter
Datarate samples s ⁄ fDATAIN_RATE
FOSR IOSR 1– 4+() 21+()+⋅-----------------------------------------------------------------------------------= ...FAST = 0, FastSinc filter
Datarate samples s ⁄ fDATAIN_RATE
FOSR IOSR⋅------------------------------------= ...FAST=1 or any filter bypass case F OSR 1=()
where: fDATAIN_RATE...input data rate from ADC or from CPU/DMA

Digital filter for sigma delta modulators (DFSDM) RM0438
888/2187 RM0438 Rev 8
Signed data format in registers: Data is in a signed format in registers for final output data,
analog watchdog, extremes detector, offset correction. The msb of output data word
represents the sign of value (two’s complement format).
26.4.15 Launching conversions
Injected conversions can be launched using the following methods:
• Software: writing ‘1’ to JSWSTART in the DFSDM_FLTxCR1 register.
• Trigger: JEXTSEL[4:0] selects the trigger signal while JEXTEN activates the trigger
and selects the active edge at the same time (see the DFSDM_FLTxCR1 register).
• Synchronous with DFSDM_FLT0 if JSYNC=1: for DFSDM_FLTx (x>0), an injected
conversion is automatically launched when in DFSDM_FLT0; the injected conversion is
started by software (JSWSTART=1 in DFSDM_FLT0CR2 register). Each injected
conversion in DFSDM_FLTx (x>0) is always executed according to its local
configuration settings (JSCAN, JCHG, etc.).
If the scan conversion is enabled (bit JSCAN=1) then, each time an injected conversion is
triggered, all of the selected channels in the injected group (JCHG[3:0] bits in
DFSDM_FLTxJCHGR register) are converted sequentially, starting with the lowest channel
(channel 0, if selected).
If the scan conversion is disabled (bit JSCAN=0) then, each time an injected conversion is
triggered, only one of the selected channels in the injected group (JCHG[3:0] bits in
DFSDM_FLTxJCHGR register) is converted and the channel selection is then moved to the
next selected channel. Writing to the JCHG[3:0] bits when JSCAN=0 sets the channel
selection to the lowest selected injected channel.
Only one injected conversion can be ongoing at a given time. Thus, any request to launch
an injected conversion is ignored if another request for an injected conversion has already
been issued but not yet completed.
Regular conversions can be launched using the following methods:
• Software: by writing ‘1’ to RSWSTART in the DFSDM_FLTxCR1 register.
• Synchronous with DFSDM_FLT0 if RSYNC=1: for DFSDM_FLTx (x>0), a regular
conversion is automatically launched when in DFSDM_FLT0; a regular conversion is
started by software (RSWSTART=1 in DFSDM_FLT0CR2 register). Each regular
conversion in DFSDM_FLTx (x>0) is always executed according to its local
configuration settings (RCONT, RCH, etc.).
Only one regular conversion can be pending or ongoing at a given time. Thus, any request
to launch a regular conversion is ignored if another request for a regular conversion has
already been issued but not yet completed. A regular conversion can be pending if it was
interrupted by an injected conversion or if it was started while an injected conversion was in
progress. This pending regular conversion is then delayed and is performed when all
injected conversion are finished. Any delayed regular conversion is signalized by RPEND bit
in DFSDM_FLTxRDATAR register.
26.4.16 Continuous and fast continuous modes
Setting RCONT in the DFSDM_FLTxCR1 register causes regular conversions to execute in
continuous mode. RCONT=1 means that the channel selected by RCH[1:0] is converted
repeatedly after ‘1’ is written to RSWSTART.

RM0438 Rev 8 889/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
The regular conversions executing in continuous mode can be stopped by writing ‘0’ to
RCONT. After clearing RCONT, the on-going conversion is stopped immediately.
In continuous mode, the data rate can be increased by setting the FAST bit in the
DFSDM_FLTxCR1 register. In this case, the filter does not need to be refilled by new fresh
data if converting continuously from one channel because data inside the filter is valid from
previously sampled continuous data. The speed increase depends on the chosen filter
order. The first conversion in fast mode (FAST=1) after starting a continuous conversion by
RSWSTART=1 takes still full time (as when FAST=0), then each subsequent conversion is
finished in shorter intervals.
Conversion time in continuous mode:
if FAST = 0 (or first conversion if FAST=1):
for Sincx filters:
t = CNVCNT/fDFSDMCLK = [FOSR * (IOSR-1 + FORD) + FORD] / fCKIN
for FastSinc filter:
t = CNVCNT/fDFSDMCLK = [FOSR * (IOSR-1 + 4) + 2] / fCKIN
if FAST = 1 (except first conversion):
for Sincx and FastSinc filters:
t = CNVCNT/fDFSDMCLK = [FOSR * IOSR] / fCKIN
in case FOSR = FOSR[9:0]+1 = 1 (filter bypassed, only integrator active):
t = IOSR / fCKIN (... but CNVCNT=0)
Continuous mode is not available for injected conversions. Injected conversions can be
started by timer trigger to emulate the continuous mode with precise timing.
If a regular continuous conversion is in progress (RCONT=1) and if a write access to
DFSDM_FLTxCR1 register requesting regular continuous conversion (RCONT=1) is
performed, then regular continuous conversion is restarted from the next conversion cycle
(like new regular continuous conversion is applied for new channel selection - even if there
is no change in DFSDM_FLTxCR1 register).
26.4.17 Request precedence
An injected conversion has a higher precedence than a regular conversion. A regular
conversion which is already in progress is immediately interrupted by the request of an
injected conversion; this regular conversion is restarted after the injected conversion
finishes.
An injected conversion cannot be launched if another injected conversion is pending or
already in progress: any request to launch an injected conversion (either by JSWSTART or
by a trigger) is ignored as long as bit JCIP is ‘1’ (in the DFSDM_FLTxISR register).
Similarly, a regular conversion cannot be launched if another regular conversion is pending
or already in progress: any request to launch a regular conversion (using RSWSTART) is
ignored as long as bit RCIP is ‘1’ (in the DFSDM_FLTxISR register).
However, if an injected conversion is requested while a regular conversion is already in
progress, the regular conversion is immediately stopped and an injected conversion is
launched. The regular conversion is then restarted and this delayed restart is signalized in
bit RPEND.
Injected conversions have precedence over regular conversions in that a injected
conversion can temporarily interrupt a sequence of continuous regular conversions. When

Digital filter for sigma delta modulators (DFSDM) RM0438
890/2187 RM0438 Rev 8
the sequence of injected conversions finishes, the continuous regular conversions start
again if RCONT is still set (and RPEND bit will signalize the delayed start on the first regular
conversion result).
Precedence also matters when actions are initiated by the same write to DFSDM, or if
multiple actions are pending at the end of another action. For example, suppose that, while
an injected conversion is in process (JCIP=1), a single write operation to DFSDM_FLTxCR1
writes ‘1’ to RSWSTART, requesting a regular conversion. When the injected sequence
finishes, the precedence dictates that the regular conversion is performed next and its
delayed start is signalized in RPEND bit.
26.4.18 Power optimization in run mode
In order to reduce the consumption, the DFSDM filter and integrator are automatically put
into idle when not used by conversions (RCIP=0, JCIP=0).
26.5 DFSDM interrupts
In order to increase the CPU performance, a set of interrupts related to the CPU event
occurrence has been implemented:
• End of injected conversion interrupt:
– enabled by JEOCIE bit in DFSDM_FLTxCR2 register
– indicated in JEOCF bit in DFSDM_FLTxISR register
– cleared by reading DFSDM_FLTxJDATAR register (injected data)
– indication of which channel end of conver sion occurred, reported in JDATACH[1:0]
bits in DFSDM_FLTxJDATAR register
• End of regular conversion interrupt:
– enabled by REOCIE bit in DFSDM_FLTxCR2 register
– indicated in REOCF bit in DFSDM_FLTxISR register
– cleared by reading DFSDM_FLTxRDATAR register (regular data)
– indication of which channel end of conversion occurred, reported in
RDATACH[1:0] bits in DFSDM_FLTxRDATAR register
• Data overrun interrupt for injected conversions:
– occurred when injected converted data were not read from DFSDM_FLTxJDATAR
register (by CPU or DMA) and were overwritten by a new injected conversion
– enabled by JOVRIE bit in DFSDM_FLTxCR2 register
– indicated in JOVRF bit in DFSDM_FLTxISR register
– cleared by writing ‘1’ into CLRJOV RF bit in DFSDM_FLTxICR register
• Data overrun interrupt for regular conversions:
– occurred when regular converted data were not read from DFSDM_FLTxRDATAR
register (by CPU or DMA) and were overwritten by a new regular conversion
– enabled by ROVRIE bit in DFSDM_FLTxCR2 register
– indicated in ROVRF bit in DFSDM_FLTxISR register
– cleared by writing ‘1’ into CLRROV RF bit in DFSDM_FLTxICR register
• Analog watchdog interrupt:

RM0438 Rev 8 891/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
– occurred when converted data (output data or data from analog watchdog filter -
according to AWFSEL bit setting in DFSDM_FLTxCR1 register) crosses
over/under high/low thresholds in DFSDM_FLTxAWHTR / DFSDM_FLTxAWLTR
registers
– enabled by AWDIE bit in DFSDM_FLTxCR2 register (on selected channels
AWDCH[3:0])
– indicated in AWDF bit in DFSDM_FLTxISR register
– separate indication of high or low analog  watchdog threshold error by AWHTF[3:0]
and AWLTF[3:0] fields in DFSDM_FLTxAWSR register
– cleared by writing ‘1’ into corresponding  CLRAWHTF[3:0] or CLRAWLTF[3:0] bits
in DFSDM_FLTxAWCFR register
• Short-circuit detector interrupt:
– occurred when the number of stable data crosses over thresholds in
DFSDM_CHyAWSCDR register
– enabled by SCDIE bit in DFSDM_FLTxCR2 register (on channel selected by
SCDEN bi tin DFSDM_CHyCFGR1 register)
– indicated in SCDF[3:0] bits in DFSDM_FLTxISR register (which also reports the
channel on which the short-circuit detector event occurred)
– cleared by writing ‘1’ into the corresponding CLRSCDF[3:0] bit in
DFSDM_FLTxICR register
• Channel clock absence interrupt:
– occurred when there is clock absence on CKINy pin (see Clock absence detection
in Section 26.4.4: Serial channel transceivers)
– enabled by CKABIE bit in DFSDM_FLTx CR2 register (on channels selected by
CKABEN bit in DFSDM_CHyCFGR1 register)
– indicated in CKABF[y] bit in DFSDM_FLTxISR register
– cleared by writing ‘1’ into CLRCKABF [y] bit in DFSDM_FLTxICR register
[Table 213](../tables/table_213.md). DFSDM interrupt requests
Interrupt event Event flag Event/Interrupt clearing
method
Interrupt enable
control bit
End of injected conversion JEOCF reading DFSDM_FLTxJDATAR JEOCIE
End of regular conversion REOCF reading DFSDM_FLTxRDATAR REOCIE
Injected data overrun JOVRF writing CLRJOVRF = 1 JOVRIE
Regular data overrun ROVRF writing CLRROVRF = 1 ROVRIE
Analog watchdog
AWDF,
AWHTF[3:0],
AWLTF[3:0]
writing CLRAWHTF[3:0] = 1
writing CLRAWLTF[3:0] = 1
AWDIE,
(AWDCH[3:0])
short-circuit detector SCDF[3:0] writing CLRSCDF[3:0] = 1 SCDIE,
(SCDEN)
Channel clock absence CKABF[3:0] writing CLRCKABF[3:0] = 1 CKABIE,
(CKABEN)

Digital filter for sigma delta modulators (DFSDM) RM0438
892/2187 RM0438 Rev 8
26.6 DFSDM DMA transfer
To decrease the CPU intervention, conversions can be transferred into memory using a
DMA transfer. A DMA transfer for injected conversions is enabled by setting bit JDMAEN=1
in DFSDM_FLTxCR1 register. A DMA transfer for regular conversions is enabled by setting
bit RDMAEN=1 in DFSDM_FLTxCR1 register.
Note: With a DMA transfer, the interrupt flag is automatically cleared at the end of the injected or
regular conversion (JEOCF or REOCF bit in DFSDM_FLTxISR register) because DMA is
reading DFSDM_FLTxJDATAR or DFSDM_FLTxRDATAR register.
26.7 DFSDM channel y registers (y=0..3)
Word access (32-bit) must be used for registers write access except DFSDM_CHyDATINR
register. Write access to DFSDM_CHyDATINR register can be either word access (32-bit)
or half-word access (16-bit).
26.7.1 DFSDM channel y configurat ion register (DFSDM_CHyCFGR1)
This register specifies the parameters used by channel y.
Address offset: 0x00 + 0x20 * y, (y = 0 to 3)
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
DFSDM
EN
CKOUT
SRC Res. Res. Res. Res. Res. Res. CKOUTDIV[7:0]
rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DATPACK[1:0] DATMPX[1:0] Res. Res. Res. CHIN
SEL CHEN CKAB
EN SCDEN Res. SPICKSEL[1:0] SITP[1:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bit 31 DFSDMEN: Global enable for DFSDM interface
0: DFSDM interface disabled
1: DFSDM interface enabled
If DFSDM interface is enabled, then it is started to operate according to enabled y channels and
enabled x filters settings (CHEN bit in DFSDM_CHyCFGR1 and DFEN bit in DFSDM_FLTxCR1).
Data cleared by setting DFSDMEN=0:
–all registers DFSDM_FLTxISR are set to reset state (x = 0..3)
–all registers DFSDM_FLTxAWSR are set to reset state (x = 0..3)
Note: DFSDMEN is present only in DFSDM_CH0CFGR1 register (channel y=0)
Bit 30 CKOUTSRC: Output serial clock source selection
0: Source for output clock is from system clock
1: Source for output clock is from audio clock
This value can be modified only when DFSDMEN=0 (in DFSDM_CH0CFGR1 register).
Note: CKOUTSRC is present only in DF SDM_CH0CFGR1 register (channel y=0)
Bits 29:24 Reserved, must be kept at reset value.

RM0438 Rev 8 893/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
Bits 23:16 CKOUTDIV[7:0]: Output serial clock divider
0: Output clock generation is disabled (CKOUT signal is set to low state)
1- 255: Defines the division of system clock for the serial clock output for CKOUT signal in range 2 -
256 (Divider = CKOUTDIV+1).
CKOUTDIV also defines the threshold for a clock absence detection.
This value can only be modified when DFSDMEN=0 (in DFSDM_CH0CFGR1 register).
If DFSDMEN=0 (in DFSDM_CH0CFGR1 register) then CKOUT signal is set to low state (setting is
performed one DFSDM clock cycle after DFSDMEN=0).
Note: CKOUTDIV is present only in DFSDM_CH0CFGR1 register (channel y=0)
Bits 15:14 DATPACK[1:0]: Data packing mode in DFSDM_CHyDATINR register.
0:Standard: input data in DFSDM_CHyDATINR register are stored only in INDAT0[15:0]. To empty
DFSDM_CHyDATINR register one sample must be read by the DFSDM filter from channel y.
1: Interleaved: input data in DFSDM_CHyDATINR register are stored as two samples:
–first sample in INDAT0[15:0] (assigned to channel y)
–second sample INDAT1[15:0] (assigned to channel y)
To empty DFSDM_CHyDATINR register, two samples must be read by the digital filter from
channel y (INDAT0[15:0] part is read as first sample and then INDAT1[15:0] part is read as next
sample).
2: Dual: input data in DFSDM_CHyDATINR register are stored as two samples:
–first sample INDAT0[15:0] (assigned to channel y)
–second sample INDAT1[15:0] (assigned to channel y+1)
To empty DFSDM_CHyDATINR register first sample must be read by the digital filter from channel
y and second sample must be read by another digital filter from channel y+1. Dual mode is
available only on even channel numbers (y = 0, 2), for odd channel numbers (y = 1, 3)
DFSDM_CHyDATINR is write protected. If an even channel is set to dual mode then the following
odd channel must be set into standard mode (DATPACK[1:0]=0) for correct cooperation with even
channel.
3: Reserved
This value can be modified only when CHEN=0 (in DFSDM_CHyCFGR1 register).
Bits 13:12 DATMPX[1:0]: Input data multiplexer for channel y
0:Data to channel y are taken from external serial inputs as 1-bit values. DFSDM_CHyDATINR
register is write protected.
1: Data to channel y are taken from internal analog to digital converter ADCy+1 output register
update as 16-bit values (if ADCy+1 is available). Data from ADCs are written into INDAT0[15:0]
part of DFSDM_CHyDATINR register.
2:Data to channel y are taken from internal DFSDM_CHyDATINR register by direct CPU/DMA write.
There can be written one or two 16-bit data samples according DATPACK[1:0] bit field setting.
3:Reserved
This value can be modified only when CHEN=0 (in DFSDM_CHyCFGR1 register).
Bits 11:9 Reserved, must be kept at reset value.
Bit 8 CHINSEL: Channel inputs selection
0: Channel inputs are taken from pins of the same channel y.
1: Channel inputs are taken from pins of the following channel (channel (y+1) modulo 8).
This value can be modified only when CHEN=0 (in DFSDM_CHyCFGR1 register).
Bit 7 CHEN: Channel y enable
0: Channel y disabled
1: Channel y enabled
If channel y is enabled, then serial data receiving is started according to the given channel setting.

Digital filter for sigma delta modulators (DFSDM) RM0438
894/2187 RM0438 Rev 8
26.7.2 DFSDM channel y configurat ion register (DFSDM_CHyCFGR2)
This register specifies the parameters used by channel y.
Address offset: 0x04 + 0x20 * y, (y = 0 to 3)
Reset value: 0x0000 0000
Bit 6 CKABEN: Clock absence detector enable on channel y
0: Clock absence detector disabled on channel y
1: Clock absence detector enabled on channel y
Bit 5 SCDEN: Short-circuit detector enable on channel y
0: Input channel y will not be guarded by the short-circuit detector
1: Input channel y will be continuously guarded by the short-circuit detector
Bit 4 Reserved, must be  kept at reset value.
Bits 3:2 SPICKSEL[1:0]: SPI clock select for channel y
0:clock coming from external CKINy input - sampling point according SITP[1:0]
1:clock coming from internal CKOUT output - sampling point according SITP[1:0]
2:clock coming from internal CKOUT - sampling point on each second CKOUT falling edge.
For connection to external Σ∆ modulator which divides its clock input (from CKOUT) by 2 to
generate its output serial communication clock (and this output clock change is active on each
clock input rising edge).
3:clock coming from internal CKOUT output - sampling point on each second CKOUT rising edge.
For connection to external Σ∆ modulator which divides its clock input (from CKOUT) by 2 to
generate its output serial communication clock (and this output clock change is active on each
clock input falling edge).
This value can be modified only when CHEN=0 (in DFSDM_CHyCFGR1 register).
Bits 1:0 SITP[1:0]: Serial interface type for channel y
00: SPI with rising edge to strobe data
01: SPI with falling edge to strobe data
10: Manchester coded input on DATINy pin: rising edge = logic 0, falling edge = logic 1
11: Manchester coded input on DATINy pin: rising edge = logic 1, falling edge = logic 0
This value can only be modified when CHEN=0 (in DFSDM_CHyCFGR1 register).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
OFFSET[23:8]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
OFFSET[7:0] DTRBS[4:0] Res. Res. Res.
rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 895/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
26.7.3 DFSDM channel y analog watchdog a nd short-circuit detector register
(DFSDM_CHyAWSCDR)
Short-circuit detector and analog watchdog settings for channel y.
Address offset: 0x08 + 0x20 * y, (y = 0 to 3)
Reset value: 0x0000 0000
Bits 31:8 OFFSET[23:0]: 24-bit calibration offset for channel y
For channel y, OFFSET is applied to the results of each conversion from this channel.
This value is set by software.
Bits 7:3 DTRBS[4:0]: Data right bit-shift for channel y
0-31: Defines the shift of the data result coming from the integrator - how many bit shifts to the right
will be performed to have final results. Bit-shift is performed before offset correction. The data shift is
rounding the result to nearest integer value. The sign of shifted result is maintained (to have valid
24-bit signed format of result data).
This value can be modified only when CHEN=0 (in DFSDM_CHyCFGR1 register).
Bits 2:0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. AWFORD[1:0] Res. AWFOSR[4:0]
rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
BKSCD[3:0] Res. Res. Res. Res. SCDT[7:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:24 Reserved, must be kept at reset value.
Bits 23:22 AWFORD[1:0]: Analog watchdog Sinc filter order on channel y
0: FastSinc filter type
1: Sinc1 filter type
2: Sinc2 filter type
3: Sinc3 filter type
Sincx filter type transfer function:
FastSinc filter type transfer function:
This bit can be modified only when CHEN=0 (in DFSDM_CHyCFGR1 register).
Bit 21 Reserved, must be  kept at reset value.
Bits 20:16 AWFOSR[4:0]: Analog watchdog filter oversampling ratio (decimation rate) on channel y
0 - 31: Defines the length of the Sinc type filter in the range 1 - 32 (AWFOSR + 1). This number is
also the decimation ratio of the analog data rate.
This bit can be modified only when CHEN=0 (in DFSDM_CHyCFGR1 register).
Note: If AWFOSR = 0 then the filt er has no effect (filter bypass).
Hz() 1z FOSR––
1z 1––
-----------------------------
⎝⎠
⎜⎟
⎛⎞ x
=
Hz() 1z FOSR––
1z 1––
-----------------------------
⎝⎠
⎜⎟
⎛⎞ 2
1z 2F O S R⋅()–+()⋅=

Digital filter for sigma delta modulators (DFSDM) RM0438
896/2187 RM0438 Rev 8
26.7.4 DFSDM channel y watchdog  filter data register
(DFSDM_CHyWDATR)
This register contains the data resulting from the analog watchdog filter associated to the
input channel y.
Address offset: 0x0C + 0x20 * y, (y = 0 to 3)
Reset value: 0x0000 0000
26.7.5 DFSDM channel y data input  register (DFSDM_CHyDATINR)
This register contains 16-bit input data to be processed by DFSDM filter module. Write
access can be either word access (32-bit) or half-word access (16-bit).
Address offset: 0x10 + 0x20 * y, (y = 0 to 3)
Reset value: 0x0000 0000
Bits 15:12 BKSCD[3:0]: Break signal assignment for short-circuit detector on channel y
BKSCD[i] = 0: Break i signal not assigned to short-circuit detector on channel y
BKSCD[i] = 1: Break i signal assigned to short-circuit detector on channel y
Bits 11:8 Reserved, must be kept at reset value.
Bits 7:0 SCDT[7:0]: short-circuit detector threshold for channel y
These bits are written by software to define the threshold counter for the short-circuit detector. If this
value is reached, then a short-circuit detector event occurs on a given channel.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
WDATA[15:0]
r r r rr rrrrrrrrrrr
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 WDATA[15:0]: Input channel y watchdog data
Data converted by the analog watchdog filter for input channel y. This data is continuously converted
(no trigger) for this channel, with a limited resolution (OSR=1..32/sinc order = 1..3).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
INDAT1[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
INDAT0[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 897/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
26.7.6 DFSDM channel y delay register (DFSDM_CHyDLYR)
Address offset: 0x14 + 0x20 * y, (y = 0 to 7)
Reset value: 0x0000 0000
Bits 31:16 INDAT1[15:0]: Input data for channel y or channel y+1
Input parallel channel data to be processed by the digital filter if DATMPX[1:0]=1 or DATMPX[1:0]=2.
Data can be written by CPU/DMA (if DATMPX[1:0]=2) or directly by internal ADC (if
DATMPX[1:0]=1).
If DATPACK[1:0]=0 (standard mode)
INDAT0[15:0] is write protected (not used for input sample).
If DATPACK[1:0]=1 (interleaved mode)
Second channel y data sample is stored into INDAT1[15:0]. First channel y data sample is stored
into INDAT0[15:0]. Both samples are read sequentially by DFSDM_FLTx filter as two channel y
data samples.
If DATPACK[1:0]=2 (dual mode).
For even y channels: sample in INDAT1[15:0] is automatically copied into INDAT0[15:0] of
channel (y+1).
For odd y channels: INDAT1[15:0] is write protected.
See Section 26.4.6: Parallel data inputs for more details.
INDAT0[15:1] is in the16-bit signed format.
Bits 15:0 INDAT0[15:0]: Input data for channel y
Input parallel channel data to be processed by the digital filter if DATMPX[1:0]=1 or DATMPX[1:0]=2.
Data can be written by CPU/DMA (if DATMPX[1:0]=2) or directly by internal ADC (if
DATMPX[1:0]=1).
If DATPACK[1:0]=0 (standard mode)
Channel y data sample is stored into INDAT0[15:0].
If DATPACK[1:0]=1 (interleaved mode)
First channel y data sample is stored into INDAT0[15:0]. Second channel y data sample is stored
into INDAT1[15:0]. Both samples are read sequentially by DFSDM_FLTx filter as two channel y
data samples.
If DATPACK[1:0]=2 (dual mode).
For even y channels: Channel y data sample is stored into INDAT0[15:0].
For odd y channels: INDAT0[15:0] is write protected.
See Section 26.4.6: Parallel data inputs for more details.
INDAT0[15:0] is in the16-bit signed format.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. PLSSKP[5:0]
rw rw rw rw rw rw

Digital filter for sigma delta modulators (DFSDM) RM0438
898/2187 RM0438 Rev 8
26.8 DFSDM filter x mo dule registers (x=0..3)
Word access (32-bit) must be used for registers write access except DFSDM_CHyDATINR
register.
26.8.1 DFSDM filter x control register 1 (DFSDM_FLTxCR1)
Address offset: 0x100 + 0x80 * x, (x = 0 to 3)
Reset value: 0x0000 0000
Bits 31:6 Reserved, must be kept at reset value.
Bits 5:0 PLSSKP[5:0]: Pulses to skip for input data skipping function
0-63: Defines the number of serial input samples that will be skipped. Skipping is applied
immediately after writing to this field. Reading of PLSSKP[5:0] returns current value of pulses which
will be skipped. If PLSSKP[5:0]=0 then all required data samples were already skipped.
Note: User can update PLSSKP[5:0] al so when PLSSKP[5:0] is not zero.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. AWF
SEL FAST Res. Res. Res. RCH[1:0] Res. Res. RDMA
EN Res. RSYNC RCON
T
RSW
START Res.
rw rw rw rw rw rw rw rt_w1
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. JEXTEN[1:0] JEXTSEL[4:0] Res. Res. JDMA
EN JSCAN JSYNC Res. JSW
START DFEN
rw rw rw rw rw rw rw rw rw rw rt_w1 rw
Bit 31 Reserved, must be  kept at reset value.
Bit 30 AWFSEL: Analog watchdog fast mode select
0: Analog watchdog on data output value (after the digital filter). The comparison is done after offset
correction and shift
1: Analog watchdog on channel transceivers value (after watchdog filter)
Bit 29 FAST: Fast conversion mode selection for regular conversions
0: Fast conversion mode disabled
1: Fast conversion mode enabled
When converting a regular conversion in continuous mode, having enabled the fast mode causes
each conversion (except the first) to execute faster than in standard mode. This bit has no effect on
conversions which are not continuous.
This bit can be modified only when DFEN=0 (DFSDM_FLTxCR1).
if FAST=0 (or first conversion in continuous mode if FAST=1):
t = [FOSR * (IOSR-1 + FORD) + FORD] / fCKIN..... for Sincx filters
t = [FOSR * (IOSR-1 + 4) + 2] / fCKIN..... for FastSinc filter
if FAST=1 in continuous mode (except first conversion):
t = [FOSR * IOSR] / fCKIN
in case if FOSR = FOSR[9:0]+1 = 1 (filter bypassed, active only integrator):
t = IOSR / fCKIN (... but CNVCNT=0)
where: fCKIN is the channel input clock frequency (on given channel CKINy pin) or input data rate in
case of parallel data input.
Bits 28:26 Reserved, must be kept at reset value.

RM0438 Rev 8 899/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
Bits 25:24 RCH[1:0]: Regular channel selection
0: Channel 0 is selected as the regular channel
1: Channel 1 is selected as the regular channel
...
3: Chanel 3 is selected as the regular channel
Writing this bit when RCIP=1 takes effect when the next regular conversion begins. This is
especially useful in continuous mode (when RCONT=1). It also affects regular conversions which
are pending (due to ongoing injected conversion).
Bits 23:22 Reserved, must be kept at reset value.
Bit 21 RDMAEN: DMA channel enabled to read data for the regular conversion
0: The DMA channel is not enabled to read regular data
1: The DMA channel is enabled to read regular data
This bit can be modified only when DFEN=0 (DFSDM_FLTxCR1).
Bit 20 Reserved, must be  kept at reset value.
Bit 19 RSYNC: Launch regular conversion synchronously with DFSDM_FLT0
0: Do not launch a regular conversion synchronously with DFSDM_FLT0
1: Launch a regular conversion in this DFSDM_FLTx at the very moment when a regular conversion
is launched in DFSDM_FLT0
This bit can be modified only when DFEN=0 (DFSDM_FLTxCR1).
Bit 18 RCONT: Continuous mode selection for regular conversions
0: The regular channel is converted just once for each conversion request
1: The regular channel is converted repeatedly after each conversion request
Writing ‘0’ to this bit while a continuous regular conversion is already in progress stops the
continuous mode immediately.
Bit 17 RSWSTART: Software start of a conversion on the regular channel
0: Writing ‘0’ has no effect
1: Writing ‘1’ makes a request to start a conversion on the regular channel and causes RCIP to
become ‘1’. If RCIP=1 already, writing to RSWSTART has no effect. Writing ‘1’ has no effect if
RSYNC=1.
This bit is always read as ‘0’.
Bits 16:15 Reserved, must be kept at reset value.
Bits 14:13 JEXTEN[1:0]: Trigger enable and trigger edge selection for injected conversions
00: Trigger detection is disabled
01: Each rising edge on the selected trigger makes a request to launch an injected conversion
10: Each falling edge on the selected trigger makes a request to launch an injected conversion
11: Both rising edges and falling edges on the selected trigger make requests to launch injected
conversions
This bit can be modified only when DFEN=0 (DFSDM_FLTxCR1).

Digital filter for sigma delta modulators (DFSDM) RM0438
900/2187 RM0438 Rev 8
Bits 12:8 JEXTSEL[4:0]: Trigger signal selection for launching injected conversions
0x0-0x1F: Trigger inputs selected by the following table (internal or external trigger).
This bit can be modified only when DFEN=0 (DFSDM_FLTxCR1).
Note: synchronous trigger has latency up to one f DFSDMCLK clock cycle (with deterministic jitter),
asynchronous trigger has latency 2-3 fDFSDMCLK clock cycles (with jitter up to 1 cycle).
DFSDM_FLTx
0x00 dfsdm_jtrg0
0x01 dfsdm_jtrg1
...
0x1E dfsdm_jtrg30
0x1F dfsdm_jtrg31
Refer to [Table 209](../tables/table_209.md): DFSDM triggers connection.
Bits 7:6 Reserved, must be kept at reset value.
Bit 5 JDMAEN: DMA channel enabled to read data for the injected channel group
0: The DMA channel is not enabled to read injected data
1: The DMA channel is enabled to read injected data
This bit can be modified only when DFEN=0 (DFSDM_FLTxCR1).
Bit 4 JSCAN: Scanning conversion mode for injected conversions
0: One channel conversion is performed from the injected channel group and next the selected
channel from this group is selected.
1: The series of conversions for the injected group channels is executed, starting over with the
lowest selected channel.
This bit can be modified only when DFEN=0 (DFSDM_FLTxCR1).
Writing JCHG if JSCAN=0 resets the channel selection to the lowest selected channel.
Bit 3 JSYNC: Launch an injected conversion synchronously with the DFSDM_FLT0 JSWSTART trigger
0: Do not launch an injected conversion synchronously with DFSDM_FLT0
1: Launch an injected conversion in this DFSDM_FLTx at the very moment when an injected
conversion is launched in DFSDM_FLT0 by its JSWSTART trigger
This bit can be modified only when DFEN=0 (DFSDM_FLTxCR1).
Bit 2 Reserved, must be kept at reset value.
Bit 1 JSWSTART: Start a conversion of the injected group of channels
0: Writing ‘0’ has no effect.
1: Writing ‘1’ makes a request to convert the channels in the injected conversion group, causing
JCIP to become ‘1’ at the same time. If JCIP=1 already, then writing to JSWSTART has no effect.
Writing ‘1’ has no effect if JSYNC=1.
This bit is always read as ‘0’.
Bit 0 DFEN: DFSDM_FLTx enable
0: DFSDM_FLTx is disabled. All conversions of given DFSDM_FLTx are stopped immediately and
all DFSDM_FLTx functions are stopped.
1: DFSDM_FLTx is enabled. If DFSDM_FLTx is enabled, then DFSDM_FLTx starts operating
according to its setting.
Data which are cleared by setting DFEN=0:
–register DFSDM_FLTxISR is set to the reset state
–register DFSDM_FLTxAWSR is set to the reset state

RM0438 Rev 8 901/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
26.8.2 DFSDM filter x control register 2 (DFSDM_FLTxCR2)
Address offset: 0x104 + 0x80 * x, (x = 0 to 3)
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. AWDCH[3:0]
rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. EXCH[3:0] Res. CKAB
IE SCDIE AWDIE ROVR
IE
JOVR
IE
REOC
IE
JEOC
IE
rw rw rw rw rw rw rw rw rw rw rw
Bits 31:20 Reserved, must be kept at reset value.
Bits 19:16 AWDCH[3:0]: Analog watchdog channel selection
These bits select the input channel to be guarded continuously by the analog watchdog.
AWDCH[y] = 0: Analog watchdog is disabled on channel y
AWDCH[y] = 1: Analog watchdog is enabled on channel y
Bits 15:12 Reserved, must be kept at reset value.
Bits 11:8 EXCH[3:0]: Extremes detector channel selection
These bits select the input channels to be taken by the Extremes detector.
EXCH[y] = 0: Extremes detector does not accept data from channel y
EXCH[y] = 1: Extremes detector accepts data from channel y
Bit 7 Reserved, must be kept at reset value.
Bit 6 CKABIE: Clock absence interrupt enable
0: Detection of channel input clock absence interrupt is disabled
1: Detection of channel input clock absence interrupt is enabled
Please see the explanation of CKABF[3:0] in DFSDM_FLTxISR.
Note: CKABIE is present only in DF SDM_FLT0CR2 register (filter x=0)
Bit 5 SCDIE: Short-circuit detector interrupt enable
0: short-circuit detector interrupt is disabled
1: short-circuit detector interrupt is enabled
Please see the explanation of SCDF[3:0] in DFSDM_FLTxISR.
Note: SCDIE is present only in DF SDM_FLT0CR2 register (filter x=0)
Bit 4 AWDIE: Analog watchdog interrupt enable
0: Analog watchdog interrupt is disabled
1: Analog watchdog interrupt is enabled
Please see the explanation of AWDF in DFSDM_FLTxISR.
Bit 3 ROVRIE: Regular data overrun interrupt enable
0: Regular data overrun interrupt is disabled
1: Regular data overrun interrupt is enabled
Please see the explanation of ROVRF in DFSDM_FLTxISR.

Digital filter for sigma delta modulators (DFSDM) RM0438
902/2187 RM0438 Rev 8
26.8.3 DFSDM filter x interrupt and status register (DFSDM_FLTxISR)
Address offset: 0x108 + 0x80 * x, (x = 0 to 3)
Reset value: 0x00FF 0000
Bit 2 JOVRIE: Injected data overrun interrupt enable
0: Injected data overrun interrupt is disabled
1: Injected data overrun interrupt is enabled
Please see the explanation of JOVRF in DFSDM_FLTxISR.
Bit 1 REOCIE: Regular end of conversion interrupt enable
0: Regular end of conversion interrupt is disabled
1: Regular end of conversion interrupt is enabled
Please see the explanation of REOCF in DFSDM_FLTxISR.
Bit 0 JEOCIE: Injected end of conversion interrupt enable
0: Injected end of conversion interrupt is disabled
1: Injected end of conversion interrupt is enabled
Please see the explanation of JEOCF in DFSDM_FLTxISR.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. SCDF[3:0] Res. Res. Res. Res. CKABF[3:0]
rrrr rrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. RCIP JCIP Res. Res. Res. Res. Res. Res. Res. Res. AWDF ROVRF JOVRF REOCF JEOCF
rr rrrrr
Bits 31:28 Reserved, must be kept at reset value.
Bits 27:24 SCDF[3:0]: short-circuit detector flag
SDCF[y]=0: No short-circuit detector event occurred on channel y
SDCF[y]=1: The short-circuit detector counter reaches, on channel y, the value programmed in the
DFSDM_CHyAWSCDR registers
This bit is set by hardware. It can be cleared by software using the corresponding CLRSCDF[y] bit in
the DFSDM_FLTxICR register. SCDF[y] is cleared also by hardware when CHEN[y] = 0 (given
channel is disabled).
Note: SCDF[3:0] is present only in DFSDM_FLT0ISR register (filter x=0)
Bits 23:20 Reserved, must be kept at reset value.
Bits 19:16 CKABF[3:0]: Clock absence flag
CKABF[y]=0: Clock signal on channel y is present.
CKABF[y]=1: Clock signal on channel y is not present.
Given y bit is set by hardware when clock absence is detected on channel y. It is held at
CKABF[y]=1 state by hardware when CHEN=0 (see DFSDM_CHyCFGR1 register). It is held at
CKABF[y]=1 state by hardware when the transceiver is not yet synchronized.It can be cleared by
software using the corresponding CLRCKABF[y] bit in the DFSDM_FLTxICR register.
Note: CKABF[3:0] is present only in DF SDM_FLT0ISR register (filter x=0)
Bit 15 Reserved, must be  kept at reset value.

RM0438 Rev 8 903/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
Note: For each of the flag bits, an interrupt can be enabled by setting the corresponding bit in
DFSDM_FLTxCR2. If an interrupt is called, the flag must be cleared before exiting the
interrupt service routine.
All the bits of DFSDM_FLTxISR are automatically reset when DFEN=0.
Bit 14 RCIP: Regular conversion in progress status
0: No request to convert the regular channel has been issued
1: The conversion of the regular channel is in progress or a request for a regular conversion is
pending
A request to start a regular conversion is ignored when RCIP=1.
Bit 13 JCIP: Injected conversion in progress status
0: No request to convert the injected channel group (neither by software nor by trigger) has been
issued
1: The conversion of the injected channel group is in progress or a request for a injected conversion
is pending, due either to ‘1’ being written to JSWSTART or to a trigger detection
A request to start an injected conversion is ignored when JCIP=1.
Bits 12:5 Reserved, must be kept at reset value.
Bit 4 AWDF: Analog watchdog
0: No Analog watchdog event occurred
1: The analog watchdog block detected voltage which crosses the value programmed in the
DFSDM_FLTxAWLTR or DFSDM_FLTxAWHTR registers.
This bit is set by hardware. It is cleared by software by clearing all source flag bits AWHTF[3:0] and
AWLTF[3:0] in DFSDM_FLTxAWSR register (by writing ‘1’ into the clear bits in
DFSDM_FLTxAWCFR register).
Bit 3 ROVRF: Regular conversion overrun flag
0: No regular conversion overrun has occurred
1: A regular conversion overrun has occurred, which means that a regular conversion finished while
REOCF was already ‘1’. RDATAR is not affected by overruns
This bit is set by hardware. It can be cleared by software using the CLRROVRF bit in the
DFSDM_FLTxICR register.
Bit 2 JOVRF: Injected conversion overrun flag
0: No injected conversion overrun has occurred
1: An injected conversion overrun has occurred, which means that an injected conversion finished
while JEOCF was already ‘1’. JDATAR is not affected by overruns
This bit is set by hardware. It can be cleared by software using the CLRJOVRF bit in the
DFSDM_FLTxICR register.
Bit 1 REOCF: End of regular conversion flag
0: No regular conversion has completed
1: A regular conversion has completed and its data may be read
This bit is set by hardware. It is cleared when the software or DMA reads DFSDM_FLTxRDATAR.
Bit 0 JEOCF: End of injected conversion flag
0: No injected conversion has completed
1: An injected conversion has completed and its data may be read
This bit is set by hardware. It is cleared when the software or DMA reads DFSDM_FLTxJDATAR.

Digital filter for sigma delta modulators (DFSDM) RM0438
904/2187 RM0438 Rev 8
26.8.4 DFSDM filter x interrupt fl ag clear register (DFSDM_FLTxICR)
Address offset: 0x10C + 0x80 * x, (x = 0 to 3)
Reset value: 0x0000 0000
Note: The bits of DFSDM_FLTxICR are always read as ‘0’.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. CLRSCDF[3:0] Res. Res. Res. Res. CLRCKABF[3:0]
rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CLRR
OVRF
CLRJ
OVRF Res. Res.
rc_w1 rc_w1
Bits 31:28 Reserved, must be kept at reset value.
Bits 27:24 CLRSCDF[3:0]: Clear the short-circuit detector flag
CLRSCDF[y]=0: Writing ‘0’ has no effect
CLRSCDF[y]=1: Writing ‘1’ to position y clears the corresponding SCDF[y] bit in the
DFSDM_FLTxISR register
Note: CLRSCDF[3:0] is present only in DFSDM_FLT0ICR register (filter x=0)
Bits 23:20 Reserved, must be kept at reset value.
Bits 19:16 CLRCKABF[3:0]: Clear the clock absence flag
CLRCKABF[y]=0: Writing ‘0’ has no effect
CLRCKABF[y]=1: Writing ‘1’ to position y clears the corresponding CKABF[y] bit in the
DFSDM_FLTxISR register. When the transceiver is not yet synchronized, the clock absence flag is
set and cannot be cleared by CLRCKABF[y].
Note: CLRCKABF[3:0] is present only in  DFSDM_FLT0ICR register (filter x=0)
Bits 15:4 Reserved, must be kept at reset value.
Bit 3 CLRROVRF: Clear the regular conversion overrun flag
0: Writing ‘0’ has no effect
1: Writing ‘1’ clears the ROVRF bit in the DFSDM_FLTxISR register
Bit 2 CLRJOVRF: Clear the injected conversion overrun flag
0: Writing ‘0’ has no effect
1: Writing ‘1’ clears the JOVRF bit in the DFSDM_FLTxISR register
Bits 1:0 Reserved, must be kept at reset value.

RM0438 Rev 8 905/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
26.8.5 DFSDM filter x injected ch annel group selection register
(DFSDM_FLTxJCHGR)
Address offset: 0x110 + 0x80 * x, (x = 0 to 3)
Reset value: 0x0000 0001
26.8.6 DFSDM filter x contro l register (DFSDM_FLTxFCR)
Address offset: 0x114 + 0x80 * x, (x = 0 to 3)
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. JCHG[3:0]
rw rw rw rw
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 JCHG[3:0]: Injected channel group selection
JCHG[y]=0: channel y is not part of the injected group
JCHG[y]=1: channel y is part of the injected group
If JSCAN=1, each of the selected channels is converted, one after another. The lowest channel
(channel 0, if selected) is converted first and the sequence ends at the highest selected channel.
If JSCAN=0, then only one channel is converted from the selected channels, and the channel
selection is moved to the next channel. Writing JCHG, if JSCAN=0, resets the channel selection to
the lowest selected channel.
At least one channel must always be selected for the injected group. Writes causing all JCHG bits to
be zero are ignored.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
FORD[2:0] Res. Res. Res. FOSR[9:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. IOSR[7:0]
rw rw rw rw rw rw rw rw

Digital filter for sigma delta modulators (DFSDM) RM0438
906/2187 RM0438 Rev 8
26.8.7 DFSDM filter x data register for injected group
(DFSDM_FLTxJDATAR)
Address offset: 0x118 + 0x80 * x, (x = 0 to 3)
Reset value: 0x0000 0000
Bits 31:29 FORD[2:0]: Sinc filter order
0: FastSinc filter type
1: Sinc1 filter type
2: Sinc2 filter type
3: Sinc3 filter type
4: Sinc4 filter type
5: Sinc5 filter type
6-7: Reserved
Sincx filter type transfer function:
FastSinc filter type transfer function:
This bit can only be modified when DFEN=0 (DFSDM_FLTxCR1).
Bits 28:26 Reserved, must be kept at reset value.
Bits 25:16 FOSR[9:0]: Sinc filter oversampling ratio (decimation rate)
0 - 1023: Defines the length of the Sinc type filter in the range 1 - 1024 (FOSR = FOSR[9:0] +1). This
number is also the decimation ratio of the output data rate from filter.
This bit can only be modified when DFEN=0 (DFSDM_FLTxCR1)
Note: If FOSR = 0, then  the filter has no effect (filter bypass).
Bits 15:8 Reserved, must be kept at reset value.
Bits 7:0 IOSR[7:0]: Integrator oversampling ratio (averaging length)
0- 255: The length of the Integrator in the range 1 - 256 (IOSR + 1). Defines how many samples
from Sinc filter will be summed into one output data sample from the integrator. The output data rate
from the integrator will be decreased by this number (additional data decimation ratio).
This bit can only be modified when DFEN=0 (DFSDM_FLTxCR1)
Note: If IOSR = 0, then the Integrator has no effect (Integrator bypass).
Hz() 1z FOSR––
1z 1––
-----------------------------
⎝⎠
⎜⎟
⎛⎞ x
=
Hz() 1z FOSR––
1z 1––
-----------------------------
⎝⎠
⎜⎟
⎛⎞ 2
1z 2F O S R⋅()–+()⋅=
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
JDATA[23:8]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
JDATA[7:0] Res. Res. Res. Res. Res. Res. JDATACH[1:0]
rrrrrrrr rr

RM0438 Rev 8 907/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
Note: DMA may be used to read the data from this register. Half-word accesses may be used to
read only the MSBs of conversion data.
Reading this register also clears JEOCF in DFSDM_FLTxISR. Thus, the firmware must not
read this register if DMA is activated to read data from this register.
26.8.8 DFSDM filter x data regi ster for the regular channel
(DFSDM_FLTxRDATAR)
Address offset: 0x11C + 0x80 * x, (x = 0 to 3)
Reset value: 0x0000 0000
Note: Half-word accesses may be used to read only the MSBs of conversion data.
Reading this register also clears REOCF in DFSDM_FLTxISR.
Bits 31:8 JDATA[23:0]: Injected group conversion data
When each conversion of a channel in the injected group finishes, its resulting data is stored in this
field. The data is valid when JEOCF=1. Reading this register clears the corresponding JEOCF.
Bits 7:2 Reserved, must be kept at reset value.
Bits 1:0 JDATACH[1:0]: Injected channel most recently converted
When each conversion of a channel in the injected group finishes, JDATACH[1:0] is updated to
indicate which channel was converted. Thus, JDATA[23:0] holds the data that corresponds to the
channel indicated by JDATACH[1:0].
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
RDATA[23:8]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
RDATA[7:0] Res. Res. Res. RPEND Res. Res. RDATACH[1:0]
rrrrrrrr r rr
Bits 31:8 RDATA[23:0]: Regular channel conversion data
When each regular conversion finishes, its data is stored in this register. The data is valid when
REOCF=1. Reading this register clears the corresponding REOCF.
Bits 7:5 Reserved, must be kept at reset value.
Bit 4 RPEND: Regular channel pending data
Regular data in RDATA[23:0] was delayed due to an injected channel trigger during the conversion
Bits 3:2 Reserved, must be kept at reset value.
Bits 1:0 RDATACH[1:0]: Regular channel most recently converted
When each regular conversion finishes, RDATACH[1:0] is updated to indicate which channel was
converted (because regular channel selection RCH[1:0] in DFSDM_FLTxCR1 register can be
updated during regular conversion). Thus RDATA[23:0] holds the data that corresponds to the
channel indicated by RDATACH[1:0].

Digital filter for sigma delta modulators (DFSDM) RM0438
908/2187 RM0438 Rev 8
26.8.9 DFSDM filter x analog watchdog high threshold register
(DFSDM_FLTxAWHTR)
Address offset: 0x120 + 0x80 * x, (x = 0 to 3)
Reset value: 0x0000 0000
26.8.10 DFSDM filter x analog watchdog low threshold register
(DFSDM_FLTxAWLTR)
Address offset: 0x124 + 0x80 * x, (x = 0 to 3)
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
AWHT[23:8]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
AWHT[7:0] Res. Res. Res. Res. BKAWH[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:8 AWHT[23:0]: Analog watchdog high threshold
These bits are written by software to define the high threshold for the analog watchdog.
Note: In case channel transceivers monitor (AWFSEL=1 ), the higher 16 bits (AWHT[23:8]) define the
16-bit threshold as compared with the analog watchdog filter output (because data coming from
the analog watchdog filter are up to a 16-bit resolution). Bits AWHT[7:0] are not taken into
comparison in this case.
Bits 7:4 Reserved, must be kept at reset value.
Bits 3:0 BKAWH[3:0]: Break signal assignment to analog watchdog high threshold event
BKAWH[i] = 0: Break i signal is not assigned to an analog watchdog high threshold event
BKAWH[i] = 1: Break i signal is assigned to an analog watchdog high threshold event
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
AWLT[23:8]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
AWLT[7:0] Res. Res. Res. Res. BKAWL[3:0]
rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 909/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
26.8.11 DFSDM filter x anal og watchdog status register
(DFSDM_FLTxAWSR)
Address offset: 0x128 + 0x80 * x, (x = 0 to 3)
Reset value: 0x0000 0000
Note: All the bits of DFSDM_FLTxAWSR are automatically reset when DFEN=0.
Bits 31:8 AWLT[23:0]: Analog watchdog low threshold
These bits are written by software to define the low threshold for the analog watchdog.
Note: In case channel transceivers monitor (AWFSEL=1), only the higher 16 bits (AWLT[23:8]) define
the 16-bit threshold as compared with the analog watchdog filter output (because data coming
from the analog watchdog filter are up to a 16-bit resolution). Bits AWLT[7:0] are not taken into
comparison in this case.
Bits 7:4 Reserved, must be kept at reset value.
Bits 3:0 BKAWL[3:0]: Break signal assignment to analog watchdog low threshold event
BKAWL[i] = 0: Break i signal is not assigned to an analog watchdog low threshold event
BKAWL[i] = 1: Break i signal is assigned to an analog watchdog low threshold event
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. AWHTF[3:0] Res. Res. Res. Res. AWLTF[3:0]
rrrr rrrr
Bits 31:12 Reserved, must be kept at reset value.
Bits 11:8 AWHTF[3:0]: Analog watchdog high threshold flag
AWHTF[y]=1 indicates a high threshold error on channel y. It is set by hardware. It can be cleared by
software using the corresponding CLRAWHTF[y] bit in the DFSDM_FLTxAWCFR register.
Bits 7:4 Reserved, must be kept at reset value.
Bits 3:0 AWLTF[3:0]: Analog watchdog low threshold flag
AWLTF[y]=1 indicates a low threshold error on channel y. It is set by hardware. It can be cleared by
software using the corresponding CLRAWLTF[y] bit in the DFSDM_FLTxAWCFR register.

Digital filter for sigma delta modulators (DFSDM) RM0438
910/2187 RM0438 Rev 8
26.8.12 DFSDM filter x analog  watchdog clear flag register
(DFSDM_FLTxAWCFR)
Address offset: 0x12C + 0x80 * x, (x = 0 to 3)
Reset value: 0x0000 0000
26.8.13 DFSDM filter x extrem es detector maximum register
(DFSDM_FLTxEXMAX)
Address offset: 0x130 + 0x80 * x, (x = 0 to 3)
Reset value: 0x8000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. CLRAWHTF[3:0] Res. Res. Res. Res. CLRAWLTF[3:0]
rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1
Bits 31:12 Reserved, must be kept at reset value.
Bits 11:8 CLRAWHTF[3:0]: Clear the analog watchdog high threshold flag
CLRAWHTF[y]=0: Writing ‘0’ has no effect
CLRAWHTF[y]=1: Writing ‘1’ to position y clears the corresponding AWHTF[y] bit in the
DFSDM_FLTxAWSR register
Bits 7:4 Reserved, must be kept at reset value.
Bits 3:0 CLRAWLTF[3:0]: Clear the analog watchdog low threshold flag
CLRAWLTF[y]=0: Writing ‘0’ has no effect
CLRAWLTF[y]=1: Writing ‘1’ to position y clears the corresponding AWLTF[y] bit in the
DFSDM_FLTxAWSR register
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
EXMAX[23:8]
rs_r rc_r rc_r rc_r rc_r rc_r rc_r rc_r rc_r rc_r rc_r rc_r rc_r rc_r rc_r rc_r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
EXMAX[7:0] Res. Res. Res. Res. Res. Res. EXMAXCH[1:0]
rc_r rc_r rc_r rc_r rc_r rc_r rc_r rc_r r r
Bits 31:8 EXMAX[23:0]: Extremes detector maximum value
These bits are set by hardware and indicate the highest value converted by DFSDM_FLTx.
EXMAX[23:0] bits are reset to value (0x800000) by reading of this register.
Bits 7:2 Reserved, must be kept at reset value.
Bits 1:0 EXMAXCH[1:0]: Extremes detector maximum data channel.
These bits contains information about the channel on which the data is stored into EXMAX[23:0].
Bits are cleared by reading of this register.

RM0438 Rev 8 911/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
26.8.14 DFSDM filter x extrem es detector minimum register
(DFSDM_FLTxEXMIN)
Address offset: 0x134 + 0x80 * x, (x = 0 to 3)
Reset value: 0x7FFF FF00
26.8.15 DFSDM filter x conversion ti mer register (DFSDM_FLTxCNVTIMR)
Address offset: 0x138 + 0x80 * x, (x = 0 to 3)
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
EXMIN[23:8]
rc_r rs_r rs_r rs_r rs_r rs_r rs_r rs_r rs_r rs_r rs_r rs_r rs_r rs_r rs_r rs_r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
EXMIN[7:0] Res. Res. Res. Res. Res. Res. EXMINCH[1:0]
rs_r rs_r rs_r rs_r rs_r rs_r rs_r rs_r r r
Bits 31:8 EXMIN[23:0]: Extremes detector minimum value
These bits are set by hardware and indicate the lowest value converted by DFSDM_FLTx.
EXMIN[23:0] bits are reset to value (0x7FFFFF) by reading of this register.
Bits 7:2 Reserved, must be kept at reset value.
Bits 1:0 EXMINCH[1:0]: Extremes detector minimum data channel
These bits contain information about the channel on which the data is stored into EXMIN[23:0]. Bits
are cleared by reading of this register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
CNVCNT[27:12]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CNVCNT[11:0] Res. Res. Res. Res.
rrrrrrrrrrrr

Digital filter for sigma delta modulators (DFSDM) RM0438
912/2187 RM0438 Rev 8
26.8.16 DFSDM register map
The following table summarizes the DFSDM registers.
Bits 31:4 CNVCNT[27:0]: 28-bit timer counting conversion time t = CNVCNT[27:0] / fDFSDMCLK
The timer has an input clock from DFSDM clock (system clock fDFSDMCLK). Conversion time
measurement is started on each conversion start and stopped when conversion finishes (interval
between first and last serial sample). Only in case of filter bypass (FOSR[9:0] = 0) is the conversion
time measurement stopped and CNVCNT[27:0] = 0. The counted time is:
if FAST=0 (or first conversion in continuous mode if FAST=1):
t = [FOSR * (IOSR-1 + FORD) + FORD] / fCKIN..... for Sincx filters
t = [FOSR * (IOSR-1 + 4) + 2] / fCKIN..... for FastSinc filter
if FAST=1 in continuous mode (except first conversion):
t = [FOSR * IOSR] / fCKIN
in case if FOSR = FOSR[9:0]+1 = 1 (filter bypassed, active only integrator):
CNVCNT = 0 (counting is stopped, conversion time: t = IOSR / fCKIN)
where: fCKIN is the channel input clock frequency (on given channel CKINy pin) or input data rate in
case of parallel data input (from internal ADC or from CPU/DMA write)
Note: When conversion is interrupted (e.g. by disabl e/enable selected channel) the timer counts also
this interruption time.
Bits 3:0 Reserved, must be kept at reset value.
[Table 214](../tables/table_214.md). DFSDM register map and reset values
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
DFSDM_
CH0CFGR1
DFSDMEN
CKOUTSRC
Res.
Res.
Res.
Res.
Res.
Res.
CKOUTDIV[7:0]
DATPACK[1:0]
DATMPX[1:0]
Res.
Res.
Res.
CHINSEL
CHEN
CKABEN
SCDEN
Res.
SPICKSEL
[1:0]
SITP[1:0]
r e s e t  v a l u e 00 000000000000 0000 0000
0x04
DFSDM_
CH0CFGR2 OFFSET[23:0] DTRBS[4:0]
Res.
Res.
Res.
reset value 0 0
0x08
DFSDM_
CH0AWSCDR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWFORD
[1:0]
Res.
AWFOSR[4:0] BKSCD[3:0]
Res.
Res.
Res.
Res.
SCDT[7:0]
r e s e t  v a l u e 00 000000000 00000000
0x0C
DFSDM_
CH0WDATR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
WDATA[15:0]
r e s e t  v a l u e 0000000000000000
0x10
DFSDM_
CH0DATINR INDAT1[15:0] INDAT0[15:0]
r e s e t  v a l u e 00000000000000000000000000000000
0x14
DFSDM_
CH0DLYR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PLSSKP[5:0]
reset value 000000
0x18 -
0x1C Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.

RM0438 Rev 8 913/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
0x20
DFSDM_
CH1CFGR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
DATPACK[1:0]
DATMPX[1:0]
Res.
Res.
Res.
CHINSEL
CHEN
CKABEN
SCDEN
Res.
SPICKSEL
[1:0]
SITP[1:0]
r e s e t  v a l u e 0000 0000 0000
0x24
DFSDM_
CH1CFGR2 OFFSET[23:0] DTRBS[4:0]
Res.
Res.
Res.
r e s e t  v a l u e 00000000000000000000000000000
0x28
DFSDM_
CH1AWSCDR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWFORD[1:0]
Res.
AWFOSR[4:0] BKSCD[3:0]
Res.
Res.
Res.
Res.
SCDT[7:0]
r e s e t  v a l u e 00 000000000 00000000
0x2C
DFSDM_
CH1WDATR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
WDATA[15:0]
r e s e t  v a l u e 00000000000000000
0x30
DFSDM_
CH1DATINR INDAT1[15:0] INDAT0[15:0]
r e s e t  v a l u e 00000000000000000000000000000000
0x34
DFSDM_
CH1DLYR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PLSSKP[5:0]
reset value 000000
0x38 -
0x3C Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x40
DFSDM_
CH2CFGR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
DATPACK[1:0]
DATMPX[1:0]
Res.
Res.
Res.
CHINSEL
CHEN
CKABEN
SCDEN
Res.
SPICKSEL[1:0]
SITP[1:0]
r e s e t  v a l u e 0000 0000 0000
0x44
DFSDM_
CH2CFGR2 OFFSET[23:0] DTRBS[4:0]
Res.
Res.
Res.
r e s e t  v a l u e 00000000000000000000000000000
0x48
DFSDM_
CH2AWSCDR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWFORD[1:0]
Res.
AWFOSR[4:0] BKSCD[3:0]
Res.
Res.
Res.
Res.
SCDT[7:0]
r e s e t  v a l u e 00 000000000 00000000
0x4C
DFSDM_
CH2WDATR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
WDATA[15:0]
r e s e t  v a l u e 0000000000000000
0x50
DFSDM_
CH2DATINR INDAT1[15:0] INDAT0[15:0]
r e s e t  v a l u e 00000000000000000000000000000000
0x54
DFSDM_
CH2DLYR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PLSSKP[5:0]
reset value 000000
0x58 -
0x5C Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
[Table 214](../tables/table_214.md). DFSDM register map and reset values (continued)
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

Digital filter for sigma delta modulators (DFSDM) RM0438
914/2187 RM0438 Rev 8
0x60
DFSDM_
CH3CFGR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
DATPACK[1:0]
DATMPX[1:0]
Res.
Res.
Res.
CHINSEL
CHEN
CKABEN
SCDEN
Res.
SPICKSEL[1:0]
SITP[1:0]
r e s e t  v a l u e 0000 0000 0000
0x64
DFSDM_
CH3CFGR2 OFFSET[23:0] DTRBS[4:0]
Res.
Res.
Res.
r e s e t  v a l u e 00000000000000000000000000000
0x68
DFSDM_
CH3AWSCDR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWFORD[1:0]
Res.
AWFOSR[4:0] BKSCD[3:0]
Res.
Res.
Res.
Res.
SCDT[7:0]
r e s e t  v a l u e 00 000000000 00000000
0x6C
DFSDM_
CH3WDATR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
WDATA[15:0]
r e s e t  v a l u e 0000000000000000
0x70
DFSDM_
CH3DATINR INDAT1[15:0] INDAT0[15:0]
r e s e t  v a l u e 00000000000000000000000000000000
0x74
DFSDM_
CH3DLYR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PLSSKP[5:0]
reset value 000000
0x78 -
0xFC Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x100
DFSDM_
FLT0CR1
Res.
AWFSEL
FAST
Res.
Res.
Res.
RCH[1:0]
Res.
Res.
RDMAEN
Res.
RSYNC
RCONT
RSW START
Res.
Res.
JEXTEN[1:0]
JEXTSEL[4:0]
Res.
Res.
JDMAEN
JSCAN
JSYNC
Res.
JSW START
DFEN
r e s e t  v a l u e 00 00 0 000 0000000 000 00
0x104
DFSDM_
FLT0CR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWDCH[3:0]
Res.
Res.
Res.
Res.
EXCH[3:0]
Res.
CKABIE
SCDIE
AWDIE
ROVRIE
JOVRIE
REOCIE
JEOCIE
r e s e t  v a l u e 0000 0000 0000000
0x108
DFSDM_
FLT0ISR
Res.
Res.
Res.
Res.
SCDF[3:0]
Res.
Res.
Res.
Res.
CKABF[3:0]
Res.
RCIP
JCIP
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWDF
ROVRF
JOVRF
REOCF
JEOCF
r e s e t  v a l u e 0000 1111 00 00000
0x10C
DFSDM_
FLT0ICR
Res.
Res.
Res.
Res.
CLRSCDF
[3:0]
Res.
Res.
Res.
Res.
CLRCKABF
[3:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CLR ROVRF
CLR JOVRF
Res.
Res.
r e s e t  v a l u e 0000 0000 00
0x110
DFSDM_
FLT0JCHGR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
JCHG[3:0]
reset value 0001
0x114
DFSDM_
FLT0FCR
FORD[2:0]
Res.
Res.
Res.
FOSR[9:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
IOSR[7:0]
r e s e t  v a l u e 000 0000000000 00000000
[Table 214](../tables/table_214.md). DFSDM register map and reset values (continued)
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

RM0438 Rev 8 915/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
0x118
DFSDM_
FLT0JDATAR JDATA[23:0]
Res.
Res.
Res.
Res.
Res.
Res.
JDATACH [1:0]
r e s e t  v a l u e 000000000000000000000000 00
0x11C
DFSDM_
FLT0RDATAR RDATA[23:0]
Res.
Res.
Res.
RPEND
Res.
Res.
RDATACH[1:0]
r e s e t  v a l u e 000000000000000000000000 0 00
0x120
DFSDM_
FLT0AWHTR AWHT[23:0]
Res.
Res.
Res.
Res.
BKAWH[3:0]
r e s e t  v a l u e 000000000000000000000000 0000
0x124
DFSDM_
FLT0AWLTR AWLT[23:0]
Res.
Res.
Res.
Res.
BKAWL[3:0]
r e s e t  v a l u e 000000000000000000000000 0000
0x128
DFSDM_
FLT0AWSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWHTF[3:0]
Res.
Res.
Res.
Res.
AWLTF[3:0]
reset value 0000 0000
0x12C
DFSDM_
FLT0AWCFR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CLRAWHTF
[3:0]
Res.
Res.
Res.
Res.
CLRAWLTF
[3:0]
reset value 0000 0000
0x130
DFSDM_
FLT0EXMAX EXMAX[23:0]
Res.
Res.
Res.
Res.
Res.
Res.
EXMAXCH[1:0]
r e s e t  v a l u e 100000000000000000000000 00
0x134
DFSDM_
FLT0EXMIN EXMIN[23:0]
Res.
Res.
Res.
Res.
Res.
Res.
EXMINCH[1:0]
r e s e t  v a l u e 011111111111111111111111 00
0x138
DFSDM_
FLT0CNVTIMR CNVCNT[27:0]
Res.
Res.
Res.
Res.
r e s e t  v a l u e 0000000000000000000000000000
0x13C -
0x17C Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x180
DFSDM_
FLT1CR1
Res.
AWFSEL
FAST
Res.
Res.
Res.
RCH[1:0]
Res.
Res.
RDMAEN
Res.
RSYNC
RCONT
RSW START
Res.
Res.
JEXTEN[1:0]
JEXTSEL[4:0]
Res.
Res.
JDMAEN
JSCAN
JSYNC
Res.
JSW START
DFEN
r e s e t  v a l u e 00 00 0 000 0000000 000 00
0x184
DFSDM_
FLT1CR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWDCH[3:0]
Res.
Res.
Res.
Res.
EXCH[3:0]
Res.
Res.
Res.
AWDIE
ROVRIE
JOVRIE
REOCIE
JEOCIE
r e s e t  v a l u e 0000 0000 00000
[Table 214](../tables/table_214.md). DFSDM register map and reset values (continued)
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

Digital filter for sigma delta modulators (DFSDM) RM0438
916/2187 RM0438 Rev 8
0x188
DFSDM_
FLT1ISR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
RCIP
JCIP
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWDF
ROVRF
JOVRF
REOCF
JEOCF
r e s e t  v a l u e 00 00000
0x18C
DFSDM_
FLT1ICR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CLR ROVRF
CLR JOVRF
Res.
Res.
reset value 00
0x190
DFSDM_
FLT1JCHGR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
JCHG[3:0]
reset value 0001
0x194
DFSDM_
FLT1FCR
FORD[2:0]
Res.
Res.
Res.
FOSR[9:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
IOSR[7:0]
r e s e t  v a l u e 000 0000000000 00000000
0x198
DFSDM_
FLT1JDATAR JDATA[23:0]
Res.
Res.
Res.
Res.
Res.
Res.
JDATACH[1:0]
r e s e t  v a l u e 000000000000000000000000 00
0x19C
DFSDM_
FLT1RDATAR RDATA[23:0]
Res.
Res.
Res.
RPEND
Res.
Res.
RDATACH[1:0]
r e s e t  v a l u e 000000000000000000000000 0 00
0x1A0
DFSDM_
FLT1AWHTR AWHT[23:0]
Res.
Res.
Res.
Res.
BKAWH[3:0]
r e s e t  v a l u e 000000000000000000000000 0000
0x1A4
DFSDM_
FLT1AWLTR AWLT[23:0]
Res.
Res.
Res.
Res.
BKAWL[3:0]
r e s e t  v a l u e 000000000000000000000000 0000
0x1A8
DFSDM_
FLT1AWSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWHTF[3:0]
Res.
Res.
Res.
Res.
AWLTF[3:0]
reset value 0000 0000
0x1AC
DFSDM_
FLT1AWCFR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CLRAWHTF
[3:0]
Res.
Res.
Res.
Res.
CLRAWLTF
[3:0]
reset value 0000 0000
0x1B0
DFSDM_
FLT1EXMAX EXMAX[23:0]
Res.
Res.
Res.
Res.
Res.
Res.
EXMAXCH[1:0]
r e s e t  v a l u e 100000000000000000000000 00
0x1B4
DFSDM_
FLT1EXMIN EXMIN[23:0]
Res.
Res.
Res.
Res.
Res.
Res.
EXMINCH[1:0]
r e s e t  v a l u e 011111111111111111111111 00
[Table 214](../tables/table_214.md). DFSDM register map and reset values (continued)
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

RM0438 Rev 8 917/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
0x1B8
DFSDM_
FLT1CNVTIMR CNVCNT[27:0]
Res.
Res.
Res.
Res.
r e s e t  v a l u e 0000000000000000000000000000
0x1BC -
0x1FC Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x200
DFDM_
FLT2CR1
Res.
AWFSEL
FAST
Res.
Res.
Res.
RCH[1:0]
Res.
Res.
RDMAEN
Res.
RSYNC
RCONT
RSW START
Res.
Res.
JEXTEN[1:0]
JEXTSEL[4:0]
Res.
Res.
JDMAEN
JSCAN
JSYNC
Res.
JSW START
DFEN
r e s e t  v a l u e 00 00 0 000 0000000 000 00
0x204
DFSDM_
FLT2CR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWDCH[3:0]
Res.
Res.
Res.
Res.
EXCH[3:0]
Res.
Res.
Res.
AWDIE
ROVRIE
JOVRIE
REOCIE
JEOCIE
r e s e t  v a l u e 0000 0000 00000
0x208
DFSDM_
FLT2ISR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
RCIP
JCIP
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWDF
ROVRF
JOVRF
REOCF
JEOCF
r e s e t  v a l u e 00 00000
0x20C
DFSDM_
FLT2ICR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CLR ROVRF
CLR JOVRF
Res.
Res.
reset value 00
0x210
DFSDM_
FLT2JCHGR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
JCHG[3:0]
reset value 0001
0x214
DFSDM_
FLT2FCR
FORD[2:0]
Res.
Res.
Res.
FOSR[9:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
IOSR[7:0]
r e s e t  v a l u e 000 0000000000 00000000
0x218
DFSDM_
FLT2JDATAR JDATA[23:0]
Res.
Res.
Res.
Res.
Res.
Res.
JDATACH[1:0]
r e s e t  v a l u e 000000000000000000000000 00
0x21C
DFSDM_
FLT2RDATAR RDATA[23:0]
Res.
Res.
Res.
RPEND
Res.
Res.
RDATACH[1:0]
r e s e t  v a l u e 000000000000000000000000 0 00
0x220
DFSDM_
FLT2AWHTR AWHT[23:0]
Res.
Res.
Res.
Res.
BKAWH[3:0]
r e s e t  v a l u e 000000000000000000000000 0000
0x224
DFSDM_
FLT2AWLTR AWLT[23:0]
Res.
Res.
Res.
Res.
BKAWL[3:0]
r e s e t  v a l u e 000000000000000000000000 0000
0x228
DFSDM_
FLT2AWSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWHTF[3:0]
Res.
Res.
Res.
Res.
AWLTF[3:0]
reset value 0000 0000
[Table 214](../tables/table_214.md). DFSDM register map and reset values (continued)
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

Digital filter for sigma delta modulators (DFSDM) RM0438
918/2187 RM0438 Rev 8
0x22C
DFSDM_
FLT2AWCFR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CLRAWHTF
[3:0]
Res.
Res.
Res.
Res.
CLRAWLTF
[3:0]
reset value 0000 0000
0x230
DFSDM_
FLT2EXMAX EXMAX[23:0]
Res.
Res.
Res.
Res.
Res.
Res.
EXMAXCH[1:0]
r e s e t  v a l u e 100000000000000000000000 00
0x234
DFSDM_
FLT2EXMIN EXMIN[23:0]
Res.
Res.
Res.
Res.
Res.
Res.
EXMINCH[1:0]
r e s e t  v a l u e 011111111111111111111111 00
0x238
DFSDM_
FLT2CNVTIMR CNVCNT[27:0]
Res.
Res.
Res.
Res.
r e s e t  v a l u e 0000000000000000000000000000
0x23C -
0x27C Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x280
DFSDM_
FLT3CR1
Res.
AWFSEL
FAST
Res.
Res.
Res.
RCH[1:0]
Res.
Res.
RDMAEN
Res.
RSYNC
RCONT
RSW START
Res.
Res.
JEXTEN[1:0]
JEXTSEL[4:0]
Res.
Res.
JDMAEN
JSCAN
JSYNC
Res.
JSW START
DFEN
r e s e t  v a l u e 00 00 0 000 0000000 000 00
0x284
DFSDM_
FLT3CR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWDCH[3:0]
Res.
Res.
Res.
Res.
EXCH[3:0]
Res.
Res.
Res.
AWDIE
ROVRIE
JOVRIE
REOCIE
JEOCIE
r e s e t  v a l u e 0000 0000 00000
0x288
DFSDM_
FLT3ISR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
RCIP
JCIP
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWDF
ROVRF
JOVRF
REOCF
JEOCF
r e s e t  v a l u e 00 00000
0x28C
DFSDM_
FLT3ICR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CLR ROVRF
CLR JOVRF
Res.
Res.
reset value 00
0x290
DFSDM_
FLT3JCHGR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
JCHG[3:0]
reset value 0001
0x294
DFSDM_
FLT3FCR
FORD[2:0]
Res.
Res.
Res.
FOSR[9:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
IOSR[7:0]
r e s e t  v a l u e 000 0000000000 00000000
0x298
DFSDM_
FLT3JDATAR JDATA[23:0]
Res.
Res.
Res.
Res.
Res.
Res.
JDATACH[1:0]
r e s e t  v a l u e 000000000000000000000000 00
[Table 214](../tables/table_214.md). DFSDM register map and reset values (continued)
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

RM0438 Rev 8 919/2187
RM0438 Digital filter for sigma delta modulators (DFSDM)
919
Refer to Section 2.3 on page 86 for the register boundary addresses.
0x29C
DFSDM_
FLT3RDATAR RDATA[23:0]
Res.
Res.
Res.
RPEND
Res.
Res.
RDATACH[1:0]
r e s e t  v a l u e 000000000000000000000000 0 00
0x2A0
DFSDM_
FLT3AWHTR AWHT[23:0]
Res.
Res.
Res.
Res.
BKAWH[3:0]
r e s e t  v a l u e 000000000000000000000000 0000
0x2A4
DFSDM_
FLT3AWLTR AWLT[23:0]
Res.
Res.
Res.
Res.
BKAWL[3:0]
r e s e t  v a l u e 000000000000000000000000 0000
0x2A8
DFSDM_
FLT3AWSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
AWHTF[3:0]
Res.
Res.
Res.
Res.
AWLTF[3:0]
reset value 0000 0000
0x2AC
DFSDM_
FLT3AWCFR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CLRAWHTF
[3:0]
Res.
Res.
Res.
Res.
CLRAWLTF
[3:0]
reset value 0000 0000
0x2B0
DFSDM_
FLT3EXMAX EXMAX[23:0]
Res.
Res.
Res.
Res.
Res.
Res.
EXMAXCH[1:0]
r e s e t  v a l u e 100000000000000000000000 00
0x2B4
DFSDM_
FLT3EXMIN EXMIN[23:0]
Res.
Res.
Res.
Res.
Res.
Res.
EXMINCH[1:0]
r e s e t  v a l u e 011111111111111111111111 00
0x2B8
DFSDM_
FLT3CNVTIMR CNVCNT[27:0]
Res.
Res.
Res.
Res.
r e s e t  v a l u e 0000000000000000000000000000
0x2BC -
0x3FC Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
[Table 214](../tables/table_214.md). DFSDM register map and reset values (continued)
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
* [Figure 180: Architectural Diagram](../figures/figure_180.md)
* [Figure 181: Architectural Diagram](../figures/figure_181.md)
* [Figure 182: Architectural Diagram](../figures/figure_182.md)
* [Figure 183: Architectural Diagram](../figures/figure_183.md)
* [Figure 184: Architectural Diagram](../figures/figure_184.md)
* [Figure 185: Architectural Diagram](../figures/figure_185.md)
* [Figure 186: Architectural Diagram](../figures/figure_186.md)
* [Figure 187: Architectural Diagram](../figures/figure_187.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 206: Configuration Matrix](../tables/table_206.md)
* [Table 207: Configuration Matrix](../tables/table_207.md)
* [Table 208: Configuration Matrix](../tables/table_208.md)
* [Table 209: Configuration Matrix](../tables/table_209.md)
* [Table 210: Configuration Matrix](../tables/table_210.md)
* [Table 211: Configuration Matrix](../tables/table_211.md)
* [Table 212: Configuration Matrix](../tables/table_212.md)
* [Table 213: Configuration Matrix](../tables/table_213.md)
* [Table 214: Configuration Matrix](../tables/table_214.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)