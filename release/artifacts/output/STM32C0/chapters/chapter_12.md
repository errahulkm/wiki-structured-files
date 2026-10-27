# Chapter 12: DMA request multiplexer (DMAMUX)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32C0 Reference Manual RM0490 - Chapter 12: DMA request multiplexer (DMAMUX).
* **Document Source**: RM0490 Reference Manual
* **PDF Reference Location**: Pages 243 - 258
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Direct Memory Access Controller (DMA)](../peripherals/dma.md)

## 2. Official Reference Manual Text Content (RM0490 Ingestion)
```text
RM0490 Rev 6 243/1023
RM0490 DMA request multiplexer (DMAMUX)
258
12 DMA request multiplexer (DMAMUX)
12.1 Introduction
A peripheral indicates a request for DMA transfer by setting its DMA request signal. The
DMA request is pending until served by the DMA controller that generates a DMA
acknowledge signal, and the corresponding DMA request signal is deasserted.
In this document, the set of control signals required for the DMA request/acknowledge
protocol is not explicitly shown or described, and it is referred to as DMA request line.
The DMAMUX request multiplexer enables routing a DMA request line between the
peripherals and the DMA controller of the product. The routing function is ensured by a
programmable multi-channel DMA request line multiplexer. Each channel selects a unique
DMA request line, unconditionally or synchronously with events from its DMAMUX
synchronization inputs. The DMAMUX may also be used as a DMA request generator from
programmable events on its input trigger signals.
The number of DMAMUX instances and their main characteristics are specified in
Section 12.3.1.
The assignment of DMAMUX request multiplexer inputs to the DMA request lines from
peripherals and to the DMAMUX request generator outputs, the assignment of DMAMUX
request multiplexer outputs to DMA controller channels, and the assignment of DMAMUX
synchronizations and trigger inputs to internal and external signals depend upon product
implementation. They are detailed in Section 12.3.2.

DMA request multiplexer (DMAMUX) RM0490
244/1023 RM0490 Rev 6
12.2 DMAMUX main features
• Up to 5-channel programmable DMA request line multiplexer output
• 4-channel DMA request generator
• 23 trigger inputs to DMA request generator
• 23 synchronization inputs
• Per DMA request generator channel:
– DMA request trigger input selector
– DMA request counter
– Event overrun flag for selected DMA request trigger input
• Per DMA request line multiplexer channel output:
– Up to 57 input DMA request lines from peripherals
– One DMA request line output
– Synchronization input selector
– DMA request counter
– Event overrun flag for selected synchronization input
– One event output, for DMA request chaining
12.3 DMAMUX implementation
12.3.1 DMAMUX instantiation
DMAMUX is instantiated with the hardware configuration parameters listed in the following
table.
12.3.2 DMAMUX mapping
The mapping of resources to DMAMUX is hardwired.
[Table 48](../tables/table_48.md). DMAMUX instantiation
Feature DMAMUX
Number of DMAMUX output request channels 3/5/7 (1)
1. Seven instances for STM32C091/92 xx devices, five instances for STM32C051/71xx devices, three
instances for STM32C011/31xx devices.
Number of DMAMUX request generator channels 4
Number of DMAMUX request trigger inputs 23
Number of DMAMUX synchronization inputs 23
Number of DMAMUX peripheral request inputs Up to 57

RM0490 Rev 6 245/1023
RM0490 DMA request multiplexer (DMAMUX)
258
[Table 49](../tables/table_49.md). DMAMUX: assignment of multiplexer inputs to resources
DMA
request
MUX input
Resource
DMA
request
MUX input
Resource
DMA
request
MUX input
Resource
1 dmamux_gen0_dma 20 tim1_ch1_dma 39 Reserved
2 dmamux_gen1_dma 21 tim1_ch2_dma 40 tim15_ch1_dma
3 dmamux_gen2_dma 22 tim1_ch3_dma 41 tim15_ch2_dma
4 dmamux_gen3_dma 23 tim1_ch4_dma 42 tim15_trgi_com_dma
5 adc1_dma 24 tim1_trgi_com_dma 43 tim15_up_dma
6 Reserved 25 tim1_up_dma 44 tim16_ch1_dma
7 Reserved 26 tim2_ch1_dma 45 tim16_trgi_com_dma
8 Reserved 27 tim2_ch2_dma 46 tim16_up_dma
9 Reserved 28 tim2_ch3_dma 47 tim17_ch1_dma
10 i2c1_rx_dma 29 tim2_ch4_dma 48 tim17_trgi_com_dma
11 i2c1_tx_dma 30 tim2_trgi_dma 49 tim17_up_dma
12 i2c2_rx_dma 31 tim2_up_dma 50 usart1_rx_dma
13 i2c2_tx_dma 32 tim3_ch1_dma 51 usart1_tx_dma
14 Reserved 33 tim3_ch2_dma 52 usart2_rx_dma
15 Reserved 34 tim3_ch3_dma 53 usart2_tx_dma
16 spi2s1_rx_dma 35 tim3_ ch4_dma 54 usart3_rx_dma
17 spi2s1_tx_dma 36 tim3_t rgi_dma 55 usart3_tx_dma
18 spi2_rx_dma 37 tim3_up_dma 56 usart4_rx_dma
19 spi2_tx_dma 38 Reserved 57 usart4_tx_dma
[Table 50](../tables/table_50.md). DMAMUX: assignment of trigger inputs to resources
Trigger input Resource Trigger input Resource
0 EXTI0 12 EXTI12
1 EXTI1 13 EXTI13
2 EXTI2 14 EXTI14
3 EXTI3 15 EXTI15
4 EXTI4 16 dmamux_evt0
5 EXTI5 17 dmamux_evt1
6 EXTI6 18 dmamux_evt2
7 EXTI7 19 dmamux_evt3
8 EXTI8 20 Reserved
9 EXTI9 21 Reserved
10 EXTI10 22 tim14_trgo
11 EXTI11 23 Reserved

DMA request multiplexer (DMAMUX) RM0490
246/1023 RM0490 Rev 6
[Table 51](../tables/table_51.md). DMAMUX: assignment of synchronization inputs to resources
Trigger input Resource Trigger input Resource
0 EXTI0 12 EXTI12
1 EXTI1 13 EXTI13
2 EXTI2 14 EXTI14
3 EXTI3 15 EXTI15
4 EXTI4 16 dmamux_evt0
5 EXTI5 17 dmamux_evt1
6 EXTI6 18 dmamux_evt2
7 EXTI7 19 dmamux_evt3
8 EXTI8 20 Reserved
9 EXTI9 21 Reserved
10 EXTI10 22 tim14_trgo
11 EXTI11 23 Reserved

RM0490 Rev 6 247/1023
RM0490 DMA request multiplexer (DMAMUX)
258
12.4 DMAMUX functional description
12.4.1 DMAMUX block diagram
[Figure 22](../figures/figure_22.md) shows the DMAMUX block diagram.
[Figure 22](../figures/figure_22.md). DMAMUX block diagram
DMAMUX features two main sub-blocks: the request line multiplexer and the request line
generator.
The implementation assigns:
• DMAMUX request multiplexer sub-block inputs (dmamux_reqx) from peripherals
(dmamux_req_inx) and from channels of the DMAMUX request generator sub-block
(dmamux_req_genx)
• DMAMUX request outputs to channels of DMA controllers (dmamux_req_outx)
• Internal or external signals to DMA request trigger inputs (dmamux_trgx)
• Internal or external signals to synchronization inputs (dmamux_syncx)
MSv39745V1
DMAMUX_C0CR
Channel 0
0 Channel select Ctrl
Channel 1
Channel m
DMAMUX Request multiplexer
p
n+3
n+2
n+p+2
1
0
n
2
1
n+1
Control registers
1
DMAMUX_CmCR
DMAMUX_RGC0CR
DMAMUX_RGC1CR
DMAMUX_RGCnCR
Channel n
Channel 1
Channel 0
Sync
Request generator
AHB slave
interface
32-bit AHB bus
dmamux_hclk
Interrupt
interface
Interrupt:
dmamux_ovr_it
Synchronization inputs:
dmamux_syncx
Trigger inputs:
dmamux_trgx
DMA requests
to DMA controllers:
dmamux_req_outx
DMA channels
events:
dmamux_evtx
DMA requests
from peripherals:
dmamux_req_inx
01s
01s
0
1
m
0
1
m
01t
dmamux_req_genx
dmamux_reqx

DMA request multiplexer (DMAMUX) RM0490
248/1023 RM0490 Rev 6
12.4.2 DMAMUX signals
[Table 52](../tables/table_52.md) lists the DMAMUX signals.
12.4.3 DMAMUX channels
A DMAMUX channel is a request multiplexer channel that can include, depending upon the
selected input of the request multiplexer, an additional DMAMUX request generator
channel.
A DMAMUX request multiplexer channel is connected and dedicated to a single channel of
DMA controller.
Channel configuration procedure
Follow the sequence below to configure a DMAMUX x channel and the related DMA
channel y:
1. Set and configure completely the DMA channel y, except enabling the channel y.
2. Set and configure completely the related DMAMUX y channel.
3. Last, activate the DMA channel y by setting the EN bit in the DMA y channel register.
12.4.4 DMAMUX request line multiplexer
The DMAMUX request multiplexer with its multiple channels ensures the actual routing of
DMA request/acknowledge control signals, named DMA request lines.
Each DMA request line is connected in parallel to all the channels of the DMAMUX request
line multiplexer.
A DMA request is sourced either from the peripherals, or from the DMAMUX request
generator.
The DMAMUX request line multiplexer channel x selects the DMA request line number as
configured by the DMAREQ_ID field in the DMAMUX_CxCR register.
Note: The null value in the fi eld DMAREQ_ID corresponds to no DMA request line selected.
[Table 52](../tables/table_52.md). DMAMUX signals
Signal name Description
dmamux_hclk DMAMUX AHB clock
dmamux_req_inx DMAMUX DMA req uest line inputs from peripherals
dmamux_trgx DMAMUX DMA request triggers inputs (to request generator sub-block)
dmamux_req_genx DMAMUX request gener ator sub-block channels outputs
dmamux_reqx DMAMUX request multiplexer sub-block inputs (from peripheral requests and request generator channels)
dmamux_syncx DMAMUX synchronization input s (to request multiplexer sub-block)
dmamux_req_outx DMAMUX requests  outputs (to DMA controller)
dmamux_evtx DMAMUX events outputs

RM0490 Rev 6 249/1023
RM0490 DMA request multiplexer (DMAMUX)
258
Caution: A same non-null DMAREQ_ID cannot be programmed to different x and y DMAMUX
request multiplexer channels (via DMAMUX_CxCR and DMAMUX_CyCR), except when the
application guarantees that the two connected DMA channels are not simultaneously active.
On top of the DMA request selection, the synchronization mode and/or the event generation
may be configured and enabled, if required.
Synchronization mode and channel event generation
Each DMAMUX request line multiplexer channel x can be individually synchronized by
setting the synchronization enable (SE) bit in the DMAMUX_CxCR register.
DMAMUX has multiple synchronization inputs. The synchronization inputs are connected in
parallel to all the channels of the request multiplexer.
The synchronization input is selected via the SYNC_ID field in the DMAMUX_CxCR register
of a given channel x.
When a channel is in this synchronization mode, the selected input DMA request line is
propagated to the multiplexer channel output, once a programmable rising/falling edge is
detected on the selected input synchronization signal, via the SPOL[1:0] field of the
DMAMUX_CxCR register.
Additionally, internally to the DMAMUX request multiplexer, there is a programmable DMA
request counter, which can be used for the channel request output generation, and for an
event generation. An event generation on the channel x output is enabled through the EGE
bit (event generation enable) of the DMAMUX_CxCR register.
As shown in [Figure 24](../figures/figure_24.md), upon the detected edge of the synchronization input, the pending
selected input DMA request line is connected to the DMAMUX multiplexer channel x output.
Note: If a synchronization event occurs while there is no pending selected input DMA request line,
it is discarded. The following asserted input request lines is not connected to the DMAMUX
multiplexer channel output until a synchronization event occurs again.
From this point on, each time the connected DMAMUX request is served by the DMA
controller (a served request is deasserted), the DMAMUX request counter is decremented.
At its underrun, the DMA request counter is automatically loaded with the value in the
NBREQ field of the DMAMUX_CxCR register and the input DMA request line is
disconnected from the multiplexer channel x output.
Thus, the number of DMA requests transferred to the multiplexer channel x output following
a detected synchronization event, is equal to the value in the NBREQ field, plus one.
Note: The NBREQ field value can be written by so ftware only when both synchronization enable
bit (SE) and event generation enable bit (EGE) of the corresponding multiplexer channel x
are disabled.

DMA request multiplexer (DMAMUX) RM0490
250/1023 RM0490 Rev 6
[Figure 23](../figures/figure_23.md). Synchronization mode of the DMAMUX request line multiplexer channel
[Figure 24](../figures/figure_24.md). Event generation of the DMA request line multiplexer channel
If EGE is enabled, the multiplexer channel generates a channel event, as a pulse of one
AHB clock cycle, when its DMA request counter is automatically reloaded with the value of
the programmed NBREQ field, as shown in [Figure 23](../figures/figure_23.md) and [Figure 24](../figures/figure_24.md).
MSv41974V1
Selected DMA request line transferred to the output
DMA request counter
dmamux_evtx
dmamux_req_outx
dmamux_syncx
Selected
dmamux_reqx
Synchronization event
Input DMA request line connected to output
321 044
DMA request counter underrun
DMA request counter auto-reload to NBREQ
Input DMA request line disconnected from output
Example: DMAMUX_CCRx configured with: NBREQ=4, SE=1, EGE=1, SPOL=01 (rising edge)
Not pending
DMA request pendingDMA requests served
MSv41975V1
DMA request counter
dmamux_evtx
23
DMA request counter reaches zero
Event is generated on the output
DMA request counter auto-reloads with NBREQ value
Example with: DMAMUX_CCRx configured with: NBREQ=3, SE=0, EGE=1
1 0 3 2 1 0 3 2 1 0
SE
EGE
Selected DMA request line transferred to the output
Selected
dmamux_reqx
dmamux_req_outx
Not pending
DMA request pending

RM0490 Rev 6 251/1023
RM0490 DMA request multiplexer (DMAMUX)
258
Note: If EGE is enabled and NBREQ = 0, an even t is generated after each served DMA request.
Note: A synchronization event (edge) is detected if the state following the edge remains stable for
more than two AHB clock cycles.
Upon writing into DMAMUX_CxCR register, the synchronization events are masked during
three AHB clock cycles.
Synchronization overrun and interrupt
If a new synchronization event occurs before the request counter underrun (the internal
request counter programmed via the NBREQ field of the DMAMUX_CxCR register), the
synchronization overrun flag bit SOFx is set in the DMAMUX_CSR register.
Note: The request multiplexer channel x synchronization must be disabled
(DMAMUX_CxCR.SE = 0) when the use of the related channel of the DMA controller is
completed. Else, upon a new detected synchronization event, there is a synchronization
overrun due to the absence of a DMA acknowledge (that is, no served request) received
from the DMA controller.
The overrun flag SOFx is reset by setting the associated clear synchronization overrun flag
bit CSOFx in the DMAMUX_CFR register.
Setting the synchronization overrun flag generates an interrupt if the synchronization
overrun interrupt enable bit SOIE is set in the DMAMUX_CxCR register.
12.4.5 DMAMUX request generator
The DMAMUX request generator produces DMA requests following trigger events on its
DMA request trigger inputs.
The DMAMUX request generator has multiple channels. DMA request trigger inputs are
connected in parallel to all channels.
The outputs of DMAMUX request generator channels are inputs to the DMAMUX request
line multiplexer.
Each DMAMUX request generator channel x has an enable bit GE (generator enable) in the
corresponding DMAMUX_RGxCR register.
The DMA request trigger input for the DMAMUX request generator channel x is selected
through the SIG_ID (trigger signal ID) field in the corresponding DMAMUX_RGxCR register.
Trigger events on a DMA request trigger input can be rising edge, falling edge or either
edge. The active edge is selected through the GPOL (generator polarity) field in the
corresponding DMAMUX_RGxCR register.
Upon the trigger event, the corresponding generator channel starts generating DMA
requests on its output. Each time the DMAMUX generated request is served by the
connected DMA controller (a served request is deasserted), a built-in (inside the DMAMUX
request generator) DMA request counter is decremented. At its underrun, the request
generator channel stops generating DMA requests and the DMA request counter is
automatically reloaded to its programmed value upon the next trigger event.
Thus, the number of DMA requests generated after the trigger event is GNBREQ + 1.

DMA request multiplexer (DMAMUX) RM0490
252/1023 RM0490 Rev 6
Note: The GNBREQ field value can be written by software only when the enable GE bit of the
corresponding generator channel x is disabled.
There is no hardware write protection.
A trigger event (edge) is detected if the state following the edge remains stable for more
than two AHB clock cycles.
Upon writing into DMAMUX_RGxCR register, the trigger events are masked during three
AHB clock cycles.
Trigger overrun and interrupt
If a new DMA request trigger event occurs before the DMAMUX request generator counter
underrun (the internal counter programmed via the GNBREQ field of the DMAMUX_RGxCR
register), and if the request generator channel x was enabled via GE, then the request
trigger event overrun flag bit OFx is asserted by the hardware in the DMAMUX_RGSR
register.
Note: The request generator channel x must be disabled (DMAMUX_RGxCR.GE = 0) when the
usage of the related channel of the DMA controller is completed. Else, upon a new detected
trigger event, there is a trigger overrun due to the absence of an acknowledge (that is, no
served request) received from the DMA.
The overrun flag OFx is reset by setting the associated clear overrun flag bit COFx in the
DMAMUX_RGCFR register.
Setting the DMAMUX request trigger overrun flag generates an interrupt if the DMA request
trigger event overrun interrupt enable bit OIE is set in the DMAMUX_RGxCR register.
12.5 DMAMUX interrupts
An interrupt can be generated upon:
• a synchronization event overrun in each DMA request line multiplexer channel
• a trigger event overrun in each DMA request generator channel
For each case, per-channel in.dividual interrupt enable, status, and clear flag register bits
are available.
[Table 53](../tables/table_53.md). DMAMUX interrupts
Interrupt signal Interrupt event Event flag Clear bit Enable bit
dmamuxovr_it
Synchronization event overrun
on channel x of the
DMAMUX request line multiplexer
SOFx CSOFx SOIE
Trigger event overrun
on channel x of the
DMAMUX request generator
OFx COFx OIE

RM0490 Rev 6 253/1023
RM0490 DMA request multiplexer (DMAMUX)
258
12.6 DMAMUX registers
Refer to the table containing register boundary addresses for the DMAMUX base address.
DMAMUX registers may be accessed per byte (8-bit), half-word (16-bit), or word (32-bit).
The address must be aligned with the data size.
12.6.1 DMAMUX request line multipl exer channel x configuration register
(DMAMUX_CxCR)
Address offset: 0x000 + 0x04 * x (x = 0 to 4)
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. SYNC_ID[4:0] NBREQ[4:0] SPOL[1:0] SE
rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. EGE SOIE Res. Res. DMAREQ_ID[5:0]
rw rw rw rw rw rw rw rw
Bits 31:29 Reserved, must be kept at reset value.
Bits 28:24 SYNC_ID[4:0]: Synchronization identification
Selects the synchronization input (see [Table 51](../tables/table_51.md): DMAMUX: assignment of synchronization
inputs to resources).
Bits 23:19 NBREQ[4:0]: Number of DMA requests minus 1 to forward
Defines the number of DMA requests to forward to the DMA controller after a synchronization
event, and/or the number of DMA requests before an output event is generated.
This field must only be written when both SE and EGE bits are low.
Bits 18:17 SPOL[1:0]: Synchronization polarity
Defines the edge polarity of the selected synchronization input:
00: No event (no synchronization, no detection).
01: Rising edge
10: Falling edge
11: Rising and falling edges
Bit 16 SE: Synchronization enable
0: Synchronization disabled
1: Synchronization enabled
Bits 15:10 Reserved, must be kept at reset value.
Bit 9 EGE: Event generation enable
0: Event generation disabled
1: Event generation enabled
Bit 8 SOIE: Synchronization overrun interrupt enable
0: Interrupt disabled
1: Interrupt enabled
Bits 7:6 Reserved, must be kept at reset value.

DMA request multiplexer (DMAMUX) RM0490
254/1023 RM0490 Rev 6
12.6.2 DMAMUX request line multiplexer  interrupt channel status register
(DMAMUX_CSR)
Address offset: 0x080
Reset value: 0x0000 0000
12.6.3 DMAMUX request line multipl exer interrupt clear flag register
(DMAMUX_CFR)
Address offset: 0x084
Reset value: 0x0000 0000
Bits 5:0 DMAREQ_ID[5:0]: DMA request identification
Selects the input DMA request. See the DMAMUX table about assignments of multiplexer
inputs to resources.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. SOF4 SOF3 SOF2 SOF1 SOF0
rrrrr
Bits 31:5 Reserved, must be kept at reset value.
Bits 4:0 SOF[4:0]: Synchronization overrun event flag
The flag is set when a synchronization event occurs on a DMA request line multiplexer
channel x, while the DMA request counter value is lower than NBREQ.
The flag is cleared by writing 1 to the corresponding CSOFx bit in DMAMUX_CFR register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. CSOF4 CSOF3 CSOF2 CSOF1 CSOF0
wwwww
Bits 31:5 Reserved, must be kept at reset value.
Bits 4:0 CSOF[4:0]: Clear synchronization overrun event flag
Writing 1 in each bit clears the corresponding overrun flag SOFx in the DMAMUX_CSR
register.

RM0490 Rev 6 255/1023
RM0490 DMA request multiplexer (DMAMUX)
258
12.6.4 DMAMUX request generator channel x configuration register
(DMAMUX_RGxCR)
Address offset: 0x100 + 0x04 * x (x = 0 to 3)
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. GNBREQ[4:0] GPOL[1:0] GE
rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. OIE Res. Res. Res. SIG_ID[4:0]
rw rw rw rw rw rw
Bits 31:24 Reserved, must be kept at reset value.
Bits 23:19 GNBREQ[4:0]: Number of DMA requests to be generated (minus 1)
Defines the number of DMA requests to be generated after a trigger event. The actual
number of generated DMA requests is GNBREQ +1.
Note: This field must be written only when GE bit is disabled.
Bits 18:17 GPOL[1:0]: DMA request generator trigger polarity
Defines the edge polarity of the selected trigger input
00: No event, i.e. no trigger detection nor generation.
01: Rising edge
10: Falling edge
11: Rising and falling edges
Bit 16 GE: DMA request generator channel x enable
0: DMA request generator channel x disabled
1: DMA request generator channel x enabled
Bits 15:9 Reserved, must be kept at reset value.
Bit 8 OIE: Trigger overrun interrupt enable
0: Interrupt on a trigger overrun event occurrence is disabled
1: Interrupt on a trigger overrun event occurrence is enabled
Bits 7:5 Reserved, must be kept at reset value.
Bits 4:0 SIG_ID[4:0]: Signal identification
Selects the DMA request trigger input used for the channel x of the DMA request generator

DMA request multiplexer (DMAMUX) RM0490
256/1023 RM0490 Rev 6
12.6.5 DMAMUX request generato r interrupt status register
(DMAMUX_RGSR)
Address offset: 0x140
Reset value: 0x0000 0000
12.6.6 DMAMUX request generator interrupt clear flag register
(DMAMUX_RGCFR)
Address offset: 0x144
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. OF3 OF2 OF1 OF0
rrrr
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 OF[3:0]: Trigger overrun event flag
The flag is set when a new trigger event occurs on DMA request generator channel x, before
the request counter underrun (the internal request counter programmed via the GNBREQ
field of the DMAMUX_RGxCR register).
The flag is cleared by writing 1 to the corresponding COFx bit in the DMAMUX_RGCFR
register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. COF3 COF2 COF1 COF0
wwww
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 COF[3:0]: Clear trigger overrun event flag
Writing 1 in each bit clears the corresponding overrun flag OFx in the DMAMUX_RGSR
register.

RM0490 Rev 6 257/1023
RM0490 DMA request multiplexer (DMAMUX)
258
12.6.7 DMAMUX register map
The following table summarizes the DMAMUX registers and reset values. Refer to the
register boundary address table for the DMAMUX register base address.
[Table 54](../tables/table_54.md). DMAMUX register map and reset values
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
0x000 DMAMUX_C0CR
Res.
Res.
Res.SYNC_ID[4:0] NBREQ[4:0] SPOL[1:0]
SE
Res.
Res.
Res.
Res.
Res.
Res.
EGE
SOIE
Res.
Res.DMAREQ_ID[5:0]
R e s e t  v a l u e 0000000000000 00 000000
0x004 DMAMUX_C1CR
Res.
Res.
Res.SYNC_ID[4:0] NBREQ[4:0] SPOL[1:0]
SE
Res.
Res.
Res.
Res.
Res.
Res.
EGE
SOIE
Res.
Res.
DMAREQ_ID[5:0]
R e s e t  v a l u e 0000000000000 00 000000
0x008 DMAMUX_C2CR
Res.
Res.
Res.SYNC_ID[4:0] NBREQ[4:0] SPOL[1:0]
SE
Res.
Res.
Res.
Res.
Res.
Res.
EGE
SOIE
Res.
Res.
DMAREQ_ID[5:0]
R e s e t  v a l u e 0000000000000 00 000000
0x00C DMAMUX_C3CR
Res.
Res.
Res.SYNC_ID[4:0] NBREQ[4:0] SPOL[1:0]
SE
Res.
Res.
Res.
Res.
Res.
Res.
EGE
SOIE
Res.
Res.
DMAREQ_ID[5:0]
R e s e t  v a l u e 0000000000000 00 000000
0x010 DMAMUX_C4CR
Res.
Res.
Res.SYNC_ID[4:0] NBREQ[4:0] SPOL[1:0]
SE
Res.
Res.
Res.
Res.
Res.
Res.
EGE
SOIE
Res.
Res.
DMAREQ_ID[5:0]
R e s e t  v a l u e 0000000000000 00 000000
0x014 -
0x07C Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x080 DMAMUX_CSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SOF4
SOF3
SOF2
SOF1
SOF0
Reset value 00000
0x084 DMAMUX_CFR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CSOF4
CSOF3
CSOF2
CSOF1
CSOF0
Reset value 00000
0x088 -
0x0FC Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x100 DMAMUX_RG0CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.GNBREQ[4:0] GPOL[1:0]
GE
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OIE
Res.
Res.
Res.SIG_ID[4:0]
R e s e t  v a l u e 00000000 0 00000
0x104 DMAMUX_RG1CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.GNBREQ[4:0] GPOL[1:0]
GE
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OIE
Res.
Res.
Res.SIG_ID[4:0]
R e s e t  v a l u e 00000000 0 00000
0x108 DMAMUX_RG2CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.GNBREQ[4:0] GPOL[1:0]
GE
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OIE
Res.
Res.
Res.SIG_ID[4:0]
R e s e t  v a l u e 00000000 0 00000
0x10C DMAMUX_RG3CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.GNBREQ[4:0] GPOL[1:0]
GE
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OIE
Res.
Res.
Res.SIG_ID[4:0]
R e s e t  v a l u e 00000000 0 00000
0x110 -
0x13C Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x140 DMAMUX_RGSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OF3
OF2
OF1
OF0
Reset value 0000
0x144 DMAMUX_RGCFR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
COF3
COF2
COF1
COF0
Reset value 0000
0x148 -
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

DMA request multiplexer (DMAMUX) RM0490
258/1023 RM0490 Rev 6
Refer to Section 2.2: Memory organization for the register boundary addresses.
[Table 55](../tables/table_55.md). DMAMUX register map and reset values
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
0x000 DMAMUX_C0CR
Res.
Res.
Res.SYNC_ID[4:0] NBREQ[4:0] SPOL[1:0]
SE
Res.
Res.
Res.
Res.
Res.
Res.
EGE
SOIE
Res.
Res.DMAREQ_ID[5:0]
R e s e t  v a l u e 0000000000000 00 000000
0x004 DMAMUX_C1CR
Res.
Res.
Res.SYNC_ID[4:0] NBREQ[4:0] SPOL[1:0]
SE
Res.
Res.
Res.
Res.
Res.
Res.
EGE
SOIE
Res.
Res.
DMAREQ_ID[5:0]
R e s e t  v a l u e 0000000000000 00 000000
0x008 DMAMUX_C2CR
Res.
Res.
Res.SYNC_ID[4:0] NBREQ[4:0] SPOL[1:0]
SE
Res.
Res.
Res.
Res.
Res.
Res.
EGE
SOIE
Res.
Res.
DMAREQ_ID[5:0]
R e s e t  v a l u e 0000000000000 00 000000
0x00C DMAMUX_C3CR
Res.
Res.
Res.SYNC_ID[4:0] NBREQ[4:0] SPOL[1:0]
SE
Res.
Res.
Res.
Res.
Res.
Res.
EGE
SOIE
Res.
Res.
DMAREQ_ID[5:0]
R e s e t  v a l u e 0000000000000 00 000000
0x010 DMAMUX_C4CR
Res.
Res.
Res.SYNC_ID[4:0] NBREQ[4:0] SPOL[1:0]
SE
Res.
Res.
Res.
Res.
Res.
Res.
EGE
SOIE
Res.
Res.
DMAREQ_ID[5:0]
R e s e t  v a l u e 0000000000000 00 000000
0x014 -
0x07C Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x080 DMAMUX_CSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SOF4
SOF3
SOF2
SOF1
SOF0
Reset value 00000
0x084 DMAMUX_CFR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CSOF4
CSOF3
CSOF2
CSOF1
CSOF0
Reset value 00000
0x088 -
0x0FC Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x100 DMAMUX_RG0CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.GNBREQ[4:0] GPOL[1:0]
GE
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OIE
Res.
Res.
Res.SIG_ID[4:0]
R e s e t  v a l u e 00000000 0 00000
0x104 DMAMUX_RG1CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.GNBREQ[4:0] GPOL[1:0]
GE
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OIE
Res.
Res.
Res.SIG_ID[4:0]
R e s e t  v a l u e 00000000 0 00000
0x108 DMAMUX_RG2CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.GNBREQ[4:0] GPOL[1:0]
GE
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OIE
Res.
Res.
Res.SIG_ID[4:0]
R e s e t  v a l u e 00000000 0 00000
0x10C DMAMUX_RG3CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.GNBREQ[4:0] GPOL[1:0]
GE
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OIE
Res.
Res.
Res.SIG_ID[4:0]
R e s e t  v a l u e 00000000 0 00000
0x110 -
0x13C Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x140 DMAMUX_RGSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
OF3
OF2
OF1
OF0
Reset value 0000
0x144 DMAMUX_RGCFR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
COF3
COF2
COF1
COF0
Reset value 0000
0x148 -
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
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 22: Architectural Diagram](../figures/figure_22.md)
* [Figure 23: Architectural Diagram](../figures/figure_23.md)
* [Figure 24: Architectural Diagram](../figures/figure_24.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 48: Configuration Matrix](../tables/table_48.md)
* [Table 49: Configuration Matrix](../tables/table_49.md)
* [Table 50: Configuration Matrix](../tables/table_50.md)
* [Table 51: Configuration Matrix](../tables/table_51.md)
* [Table 52: Configuration Matrix](../tables/table_52.md)
* [Table 53: Configuration Matrix](../tables/table_53.md)
* [Table 54: Configuration Matrix](../tables/table_54.md)
* [Table 55: Configuration Matrix](../tables/table_55.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)