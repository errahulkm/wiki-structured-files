# Chapter 44: Revision history

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32F4 Reference Manual RM0090 - Chapter 44: Revision history.
* **Document Source**: RM0090 Reference Manual
* **PDF Reference Location**: Pages 1704 - 1735
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0090 Ingestion)
```text
Revision history RM0090
1704/1741 RM0090 Rev 22
41 Revision history
[Table 315](../tables/table_315.md). Document revision history
Date Version Changes
15-Sep-2011 1 Initial release.
19-Oct-2012 2
Updated reference documents and added [Table 1](../tables/table_1.md): Applicable products on cover
page.
MEMORY:
Updated Section 2: Memory and bus architecture.
PWR:
Updated VDDA and VREF+ decoupling capacitor in [Figure 7](../figures/figure_7.md): Power supply
overview.
VOSRDY bit changed to read-only in Section 5.4.3: PWR power control/status
register (PWR_CSR).
Removed VDDA in Section 5.2.3: Programmable voltage detector (PVD) and
remove VDDA in PVDO bit description (Section 5.4.3: PWR power control/status
register (PWR_CSR)).
RCC:
Updated [Figure 20](../figures/figure_20.md): Simplified diagram of the reset circuit and minimum reset pulse
duration guaranteed by pulse generator restricted to internal reset sources.
GPIOs:
Updated Section 8.3.1: General-purpose I/O (GPIO).
DMA:
Updated direct mode description in Section 10.2: DMA main features.
Updated direct mode description in Section : Memory-to-peripheral mode, and
Section 10.3.12: FIFO/: Direct mode.
Updated register access in Section 10.5: DMA registers.
Modified Stream2 /Channel 2 in [Table 42](../tables/table_42.md): DMA1 request mapping.
Added note related to EN bit in Section 10.5.5: DMA stream x configuration register
(DMA_SxCR) (x = 0..7). Updated definition of NDT[15:0] bits in Section 10.5.6:
DMA stream x number of data register (DMA_SxNDTR) (x = 0..7).
Interrupts:
Updated number of maskable interrupts to 82 in Section 12.1.1: NVIC featuress.
Updated Section 12.2: External interrupt/event controller (EXTI).

RM0090 Rev 22 1705/1741
RM0090 Revision history
1735
19-Oct-2012 2
(continued)
ADC:
Changed ADCCLK frequency to 30 MHz in Section 13.5: Channel-wise
programmable sampling timee.
Added recovery from ADC sequence in Section 13.8.1: Using the DMA and Section
13.8.2: Managing a sequence of conversions without using the DMA.
Updated AWDIE in Section 13.13.2: ADC control register 1 (ADC_CR1). Added
read and write access in Section 13.13: ADC registers.
Advanced control timers (TIM1 and TIM8):
Updated 16-bit prescaler range in Section 17.2: TIM1 and TIM8 main features.
Updated OC1 block diagram in [Figure 114](../figures/figure_114.md): Output stage of capture/compare
channel (channel 1 to 3).
Updated update event generation in Upcounting mode and Downcounting mode in
Section 17.3.2: Counter modes and Section 17.3.3: Repetition counter.
Updated bits that control the dead-time generation in Section 17.3.11:
Complementary outputs and dead-time insertion.
Updated ways to generate a break in Section 17.3.12: Using the break function.
Changed OCxREF to ETR in the example given in Section 17.3.13: Clearing the
OCxREF signal on an external event and changed
OCREF_CLR to ETRF in [Figure 124](../figures/figure_124.md): Clearing TIMx OCxREF.
Updated configuration for example of counter operation in encoder
interface mode in Section 17.3.16: Encoder interface mode.
Added register access in Section 17.4: TIM1 and TIM8 registers.
Changed definition of ARR[15:0] bits in Section 17.4.12: TIM1 and TIM8 auto-
reload register (TIMx_ARR).
Updated BKE definition in Section 17.4.18: TIM1 and TIM8 break and dead-time
register (TIMx_BDTR).
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1706/1741 RM0090 Rev 22
19-Oct-2012 2
(continued)
General purpose timers (TIM2 to TIM5):
Removed all references to “repetition counter”.
Added [Figure 134](../figures/figure_134.md): General-purpose timer block diagram.
Updated 16-bit prescaler range in Section 18.2: TIM2 to TIM5 main features.
External clock mode 2 ETR restricted to TIM2 to TIM4 in
Section 18.3.3: Clock selection and Section 18.3.6: PWM input mode.
Updated Section 18.3.9: PWM mode and Section 18.3.11: Clearing the OCxREF
signal on an external event.
Updated [Figure 174](../figures/figure_174.md): Master/Slave timer example to change ITR1 to
ITR0.
Updated read and write access to registers in Section 18.4: TIM2 to TIM5
registerss.
Restored bits 15 to 8 of TIMx_SMCR as well as [Table 98](../tables/table_98.md): TIMx internal trigger
connection in Section 14.4.3.
Removed note 1 related to OC1M bits in Section 18.4.13: TIMx capture/compare
register 1 (TIMx_CCR1).
Updated TIMx_CCER bit description for TIM2 to TIM5 in
Section 18.4.9: TIMx capture/compare enable register (TIMx_CCER).
General purpose timers (TIM9 to TIM14):
Updated 16-bit prescaler range in Section 19.2.1: TIM9/TIM12 main features and
Section 19.2.2: TIM10/TIM11 and TIM13/TIM14 main features.
Updated [Figure 181](../figures/figure_181.md): General-purpose timer block diagram (TIM10/11/13/14)) to
remove TRGO trigger controller output.
Added register access in Section 19.4: TIM9 and TIM12 registers
and Section 19.5: TIM10/11/13/14 registers.
Basic timers (TIM6 and TIM7):
Removed all references to “repetition counter”.
Updated 16-bit prescaler range in Section 20.2: TIM6 and TIM7 main features.
HASH:
Updated Section 25.3.1: Duration of the processing.
RNG:
Updated Section 24.1: RNG introduction.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1707/1741
RM0090 Revision history
1735
19-Oct-2012 2
(continued)
RTC:
Updated [Figure 237](../figures/figure_237.md): RTC block diagram.
Added formula to compute fck_apre in [Figure 26](../figures/figure_26.md).3.1: Clock and prescalers.
Updated Section 26.3.9: RTC reference clock detection.
Updated Section : RTC register write protection.
Added RTC_SSR shadow register in Section 26.3.6: Reading the calendar.
Updated description of DC[4:0] bits in Section 26.6.7: RTC calibration register
(RTC_CALIBR).
Renamed RTC_BKxR into RTC_BKPxR in [Table 121](../tables/table_121.md): RTC register map and reset
values.
Added power-on reset value and changed reset value to system
reset value in Section 26.6.11: RTC sub second register (RTC_SSR).
Updated definition of ALARMOUTTYPE in Section 26.6.17: RTC tamper and
alternate function configuration register (RTC_TAFCR).
I2C:
Modified Section 27.3.8: DMA requests.
Updated bit 14 description in Section 27.6.3: I2C Own address register 1
(I2C_OAR1)).
Updated definition of PE bit and note related to SWRST bit; moved
note related to STOP bit to the whole register in Section 27.6.1: I2C Control register
1 (I2C_CR1).
USART:
Section 30.6.6: Control register 3 (USART_CR3)): removed notes
related to UART5 in DMAT and DMAR description.
Updated TTable 142: Error calculation for programmed baud rates at fPCLK = 42
MHz or fPCLK = 84 Hz,  oversampling by 16 and
[Table 143](../tables/table_143.md): Error calculation for programmed baud rates at fPCLK = 42  MHz or
fPCLK = 84 MHz,  oversampling by 8.
SPI/I2S:
Updated Section 28.1: SPI introduction.
Changed I2S simplex communication/mode to half-duplex communication/mode.
Updated flags in reception/transmission modes in Section 28.2.2: I2S features.
Added Frame error flag in [Table 128](../tables/table_128.md): I2S interrupt requests.
Added register access in Section 28.5: SPI and I2S registers.
Updated ERRIE definition in Section 28.5.2: SPI control register 2 (SPI_CR2).
Renamed TIFRFE to FRE and definition updated in Section 28.5.3: SPI status
register (SPI_SR).
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1708/1741 RM0090 Rev 22
19-Oct-2012 2
(continued)
SDIO:
Updated value and description for bits [45:40] and [7:1] in [Table 176](../tables/table_176.md): R4 response.
Updated value at bits [45:40] in [Table 178](../tables/table_178.md): R5 response.
CAN:
Updated [Figure 335](../figures/figure_335.md): Dual CAN block diagram.
Modified definition of CAN2SB bits in Section : CAN filter master register
(CAN_FMR).
Added register access in Section 32.9: CAN registers
ETHERNET:
Updated standard for precision networked clock synchronization in Section 33.1:
Ethernet introduction and Section 33.2.1: MAC core features.
Updated CR bit definition in Section : Ethernet MAC MII address register
(ETH_MACMIIAR).
Replace RTPR by PM bit in [Table 192](../tables/table_192.md): Source address filtering.
USB OTG FS
Updated remote wake-up signaling bit and the resume
interrupt in Section : Suspended state.
Added peripheral register access in Section 34.16: OTG_FS control and status
registerss.
Updated INEPTXSA description in OTG_FS_DIEPTXFx.
Changed PHYSEL from bit 7 to bit 6 of the OTG_FS_GUSBCFG
register.
USB OTG HS
Updated remote wake-up signaling bit and the resume
interrupt in Section : Suspended state.
Added peripheral register access in Section 35.12: OTG_HS control and status
registers.
Updated OTG_HS_CID reset value.
Updated INEPTXSA description in OTG_HS_DIEPTXFx.
Updated FSLSPCS for LS host mode, added PHYSEL in Section : OTG_HS host
configuration register (OTG_HS_HCFG).
Renamed PHYSEL into PHSEL and changed from bit 7 to bit 6 of
the OTG_HS_GUSBCFG register.
Updated OTG_HS_DIEPEACHMSK1 and OTG_HS_DOEPEACHMSK1 reset
values.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1709/1741
RM0090 Revision history
1735
19-Oct-2012 2
(continued)
FSMC:
Updated step b) in Section 36.3.1: Supported memories and transactions.
Updated [Table 196](../tables/table_196.md): FSMC_BTRx bit fields.
Changed Clock divide ration min in [Table 246](../tables/table_246.md): Programmable NAND/PC Card
access parameters.
Updated case of synchronous accesses in Section 36.5: NOR Flash/PSRAM
controller.
Changed minimum value for ADDSET to 0 in [Table 203](../tables/table_203.md), [Table 206](../tables/table_206.md), [Table 207](../tables/table_207.md),
[Table 209](../tables/table_209.md), and [Table 210](../tables/table_210.md).
Move note from [Figure 437](../figures/figure_437.md): Mode1 write accesses and [Figure 436](../figures/figure_436.md): Mode1 read
accesses. Move note from [Figure 439](../figures/figure_439.md): ModeA write accesses to [Figure 438](../figures/figure_438.md):
ModeA read accesses.
Updated Section : WAIT management in asynchronous accesses.
Added register access in Section 36.5.6: NOR/PSRAM control registers and
Section 36.6.2: NAND Flash / PC Card supported memories and transactions.
Removed caution note in Section 36.6.1: External memory interface signalss.
Updated [Table 249](../tables/table_249.md): 16-bit PC Card.
Updated step 3 in Section 36.6.4: NAND Flash operations.
Updated [Figure 455](../figures/figure_455.md): Access to non ‘CE don’t care’ NAND-Flash and note below in
Section 36.6.5: NAND Flash prewait functionality.
Updated access to I/O Space in Section 36.6.7: PC Card/CompactFlash
operationss. Updated [Table 251](../tables/table_251.md): 16-bit PC-Card signals and access type. Updated
BUSTURN bit definition in Section : SRAM/NOR-Flash chip-select timing registers
1..4 (FSMC_BTR1..4)). Changed bits 16 to 19 to BUSTURN in Section :
SRAM/NOR-Flash write timing registers 1..4 (FSMC_BWTR1..4)
DEBUG:
Updated Section 38.4.3: Internal pull-up and pull-down on JTAG pins.
Electronic signature
Updated Section 24: Device electronic signature introduction.
Updated REV_ID[15:0] to add revision Z in Section 24.1: Unique device ID register
(96 bits).
Updated address and example in Section 24.2: Flash size.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1710/1741 RM0090 Rev 22
13-Nov-2012 3
Added STM32F42x and STM32F43x devices.
Removed reference du Flash programming manual on cover page. Added Section
2.3.2: Flash memory overview and Section 3: Embedded Flash memory interface.
Change RTC_50Hz into RTC_REFIN in Section 8.3.2: I/O pin multiplexer and
mapping. Modified RTC alternate function naming in Section 8: General-purpose
I/Os (GPIO) and Section 26: Real-time clock (RTC).
Updated max. input frequency in Section 26.3.1: Clock and prescalers.
Changed bit access type from ‘rw’ to ‘w’ and bit description updated in Section
10.5.3: DMA low interrupt flag clear register (DMA_LIFCR) and Section 10.5.4:
DMA high interrupt flag clear register (DMA_HIFCR).
Updated [Figure 18](../figures/figure_18.md): Frequency measurement with TIM5 in Input capture mode.
Updated Section : Signals synchronization in Section 36: Flexible static memory
controller (FSMC)
Section 34: USB on-the-go full-speed (OTG_FS): updated Section [Figure 389](../figures/figure_389.md).:
USB host-only connection, Section : VBUS valid, and Section : Host detection of a
peripheral connection.
Section 35: USB on-the-go high-speed (OTG_HS): updated Section : VBUS valid,
and Section : Detection of peripheral connection by the host.
19-Feb-2013 4
Updated Section 2: Memory and bus architecture.
Updated [Figure 1](../figures/figure_1.md): System architecture for STM32F405xx/07xx and
STM32F415xx/17xx devices, and [Figure 1](../figures/figure_1.md): System architecture for
STM32F405xx/07xx and STM32F415xx/17xx devices. Updated [Table 4](../tables/table_4.md): Memory
mapping vs. Boot mode/physical remap. Updated [Figure 5](../figures/figure_5.md): Sequential 32-bit
instruction execution. removed note 1 from [Table 13](../tables/table_13.md): Maximum program/erase
parallelism.
PWR:
Updated [Figure 7](../figures/figure_7.md): Power supply overview.
Updated Section 5.1.3: Voltage regulator.
Added ADCDC1 bit in Section 5.5.1: PWR power control register (PWR_CR) for
STM32F42xxx and STM32F43xxx.
SYSCFG:
Added ADCxDC2 bit in Section 8.2.3: SYSCFG peripheral mode configuration
register (SYSCFG_PMC) for STM32F42xxx and STM32F43xxx.
ADC:
Updated Section 13.9.3: Interleaved mode, Section 13.9.4: Alternate trigger mode,
and Section 13.9.5: Combined regular/injected simultaneous mode to describe
case of interrupted conversion.
Updated Section : Temperature sensor, VREFINT and VBAT internal channels,
Section 13.10: Temperature sensor, and Section 13.11: Battery charge monitoring.
RTC:
Updated BKP[31:0] bit description in Section 26.6.20: RTC backup registers
(RTC_BKPxR).
I2C:
Updated Section 27.3.5: Programmable noise filter.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1711/1741
RM0090 Revision history
1735
19-Feb-2013 4
(continued)
FSMC:
Updated write FIFO size in Section 36.1: FSMC main features.
Updated [Figure 434](../figures/figure_434.md): FSMC block diagram.
Updated Section 36.5.4: NOR Flash/PSRAM controller asynchronous transactions.
Modified differences between Mode B and mode 1 in Section : Mode 2/B - NOR
Flash.
Modified differences between Mode C and mode 1 in Section : Mode C - NOR
Flash - OE toggling.
Modified differences between Mode D and mode 1 in Section : Mode D -
asynchronous access with extended address.
Updated NWAIT signal in [Figure 449](../figures/figure_449.md): Asynchronous wait during a read access,
[Figure 450](../figures/figure_450.md): Asynchronous wait during a write access, [Figure 451](../figures/figure_451.md): Wait
configurations, [Figure 452](../figures/figure_452.md): Synchronous multiplexed read mode - NOR, PSRAM
(CRAM), and [Figure 453](../figures/figure_453.md): Synchronous multiplexed write mode - PSRAM (CRAM).
Updated [Table 195](../tables/table_195.md) to [Table 214](../tables/table_214.md).
Updated Section : SRAM/NOR-Flash chip-select control registers 1..4
(FSMC_BCR1..4).
DEBUG
Updated [Figure 485](../figures/figure_485.md): Block diagram of STM32 MCU and Cortex®-M4 with FPU-
level debug support.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1712/1741 RM0090 Rev 22
15-Sep-2013 5
Added STM32F429xx and STM32F439xx part numbers.
Replaced FSMC by FMC added Chrom-ART Accelerator, LCD-TFT and SAI
interface.
Updated [Figure 2](../figures/figure_2.md): System architecture for STM32F42xxx and STM32F43xxx
devices.
PWR:
Updated Section 5.2.2: Brownout reset (BOR).
Added note related to CSS enabling in Entering Stop mode sections in Section
5.3.4: Stop mode (STM32F405xx/07xx and STM32F415xx/17xx) and Section 5.3.5:
Stop mode (STM32F42xxx and STM32F43xxx). Updated Stop mode entry in [Table 27](../tables/table_27.md) and [Table 29](../tables/table_29.md).
Updated WUF bit defienition in PWR_CSR registers. Changed CWUF and CSBF
access type to ‘w’ in PWR_CR register.
RCC: Updated LSEBYP bit definition in RCC_BDCR register.
GPIOs:
Updated description of OSPEEDR bits. Removed frequency value in description of
OSPEEDR bits.Corrected typos: "IDRy[15:0]" replaced with "IDRy" in "GPIOx_IDR"
register, "ODRy[15:0]" replaced with "ODRy" in "GPIOx_ODR" register and
"OTy[1:0]" replaced with "OTy" in "GPIOx_OTYPER" register.
DCMI: Updated Section 15.4: DCMI clocks.
IWDG: Corrected [Figure 213](../figures/figure_213.md): Independent watchdog block diagram.
RTC:
Replaced all occurrences of “power-on reset” with “backup domain reset”. Added
caution note under [Table 121](../tables/table_121.md): RTC register map and reset values. Changed SHPF
bit type to ‘r’ in Section 26.6.4: RTC initialization and status register (RTC_ISR)..
SPI: Updated definition of ERRIE bit in Section 28.5.2: SPI control register 2
(SPI_CR2).
UART:
Updated Section 30.3.8: LIN (local interconnection network) mode.
Removed note in Section 30.3.13: Continuous communication using DMA.
ETHERNET:
Modified ETH_MACA0HR (and ETH_DMABMR reset values.
Updated definitions of TSTS bit in ETH_MACSR, and TSTTR in ETH_PTPTSSR.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1713/1741
RM0090 Revision history
1735
15-Sep-2013 5
(continued)
USB OTG-FS:
Removed note related to VDD range limitation below [Figure 387](../figures/figure_387.md): OTG A-B device
connection and [Figure 388](../figures/figure_388.md): USB peripheral-only connection.
FSMC:
Updated [Table 229](../tables/table_229.md), [Table 232](../tables/table_232.md), [Table 235](../tables/table_235.md), [Table 239](../tables/table_239.md).
Replaced all occurences of DATALAT by DATLAT and SRAM/CRAM by
SRAM/PSRAM in the whole section.
Updated Section 36.1: FSMC main features. Changed bits 27 to 20 of
FSMC_BWTR1..4 to reserved.
Updated Section 36.6.7: PC Card/CompactFlash operations.
Updated WREN bit in [Table 231](../tables/table_231.md), [Table 232](../tables/table_232.md), [Table 233](../tables/table_233.md), [Table 236](../tables/table_236.md), [Table 239](../tables/table_239.md), [Table 242](../tables/table_242.md), [Table 245](../tables/table_245.md), and [Table 249](../tables/table_249.md).
Updated Section 36.5.4: NOR Flash/PSRAM controller asynchronous transactions,
Section : SRAM/NOR-Flash chip-select control registers 1..4 (FSMC_BCR1..4),
Section : SRAM/NOR-Flash chip-select timing registers 1..4 (FSMC_BTR1..4) and
Section : SRAM/NOR-Flash write timing registers 1..4 (FSMC_BWTR1..4).
Updated definition of PWID in Section : PC Card/NAND Flash control registers 2..4
(FSMC_PCR2..4).
FMC:
Updated TRDC definition in Section : SDRAM Timing registers 1,2
(FMC_SDTR1,2).
DEBUG: updated [Figure 487](../figures/figure_487.md): JTAG TAP connections.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1714/1741 RM0090 Rev 22
03-Feb-2014 6
Added note related to over-drive mode unavailable in 1.8 to 2.1 V VDD range in
Section 3.5.1: Relation between CPU clock frequency and Flash memory read
time.
Updated maximum CPU frequency in Section 3.5.2: Adaptive real-time memory
accelerator (ART Accelerator™).
PWR:
Updated Run mode/ over-drive mode in Section 5.1.4: Voltage regulator for
STM32F42xxx and STM32F43xxx.
RCC for STM32F42/43xx:
Changed APB1/2 and AHB maximum frequencies.xw
GPIOs:
Updated [Figure 27](../figures/figure_27.md): Selecting an alternate function on STM32F42xxx and
STM32F43xxx.
DMA:
Updated Section 10.3.7: Pointer incrementation and Section 10.3.11: Single and
burst transfers..
INTERRUPTS AND EVENTS:
Updated [Table 62](../tables/table_62.md): Vector table for STM32F42xxx and STM32F43xxx.
ADC:
Updated Section 13.3.10: Discontinuous mode/Section : Regular group.
DCMI:
Updated Section 15.5.2: DCMI physical interface.
LTDC:
Updated resolution in note below [Figure 82](../figures/figure_82.md): LCD-TFT Synchronous timings.
TIM1 and 8:
Added note related to IC1F in Section 17.4.7: TIM1 and TIM8 capture/compare
mode register 1 (TIMx_CCMR1).
TIM2 to 5:
Updated note related to IC1F in Section 18.4.7: TIMx capture/compare mode
register 1 (TIMx_CCMR1).
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1715/1741
RM0090 Revision history
1735
03-Feb-2014 6
(continued)
TIM9 to 14:
Updated note related to IC1F in Section 19.5.5: TIM10/11/13/14 capture/compare
mode register 1 (TIMx_CCMR1).
RTC:
Updated Section 26.3.11: RTC smooth digital calibration.
Changed ALRBIE to ALRBE (bit 9) in Section 26.6.3: RTC control register
(RTC_CR).
I2C:
Introduced Sm (standard mode) and Fm (fast mode) acronyms.
FSMC:
Updated BUSTURN definition in [Table 245](../tables/table_245.md): FSMC_BTRx bit fields.
FMC:
Added Mobile LPSDR SDRAM.
Updated Section : SDRAM initialization and Section : SDRAM controller read cycle
and [Figure 476](../figures/figure_476.md): NAND Flash/PC Card controller waveforms for common memory
access.
Updated Section : SRAM/NOR-Flash chip-select control registers 1..4
(FMC_BCR1..4), Section : SRAM/NOR-Flash chip-select timing registers 1..4
(FMC_BTR1..4), Section : SRAM/NOR-Flash write timing registers 1..4
(FMC_BWTR1..4), Section : SDRAM Timing registers 1,2 (FMC_SDTR1,2) and
Section : SDRAM Refresh Timer register (FMC_SDRTR).
Removed mention “default valeur after reset” in Section : Common memory space
timing register 2..4 (FMC_PMEM2..4), Section : Attribute memory space timing
registers 2..4 (FMC_PATT2..4), and Section : I/O space timing register 4
(FMC_PIO4).
Updated BUSTURN definition in [Table 288](../tables/table_288.md): FMC_BTRx bit fields.
Updated REV_ID bits in Section 38.6.1: MCU device ID code.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1716/1741 RM0090 Rev 22
15-May-2014 7
Embedded Flash memory interface:
Updated Section : Physical remap in STM32F42xxx and STM32F43xxx. Updated
bank 2 selection in Section 2.4: Boot configuration. Updated notes related to MERx
and SER bits in Section : Mass Erase. Updated Section 3.7.5: Proprietary code
readout protection (PCROP). Updated FLASH_OPTCR register reset value for
STM32F42/43xx in Section 3.9.10: Flash option control register (FLASH_OPTCR)
for STM32F42xxx and STM32F43xxx and Section 3.9.11: Flash option control
register (FLASH_OPTCR1) for STM32F42xxx and STM32F43xxx.
RCC (STM32F42/43xx):
Updated PPLN caution note in Section 6.3.2: RCC PLL configuration register
(RCC_PLLCFGR)
SYSCFG
Updated MEM_MODE in Section 9.3.1: SYSCFG memory remap register
(SYSCFG_MEMRMP)
LTDC:
Changed resolution do XGA (1024x768) in Section 16.2: LTDC main features,
Section 16.4.1: LTDC Global configuration parameters, and updated Section
16.7.3: LTDC Active Width Configuration Register (LTDC_AWCR).
RTC
Added note in Section 26.3.14: Calibration clock output.
TIMER 1/8:
Removed note related to IC1F bits in Section 17.4.7: TIM1 and TIM8
capture/compare mode register 1 (TIMx_CCMR1),
TIM2 to 5:
Replaced IC2S by CC2S.
Updated [Figure 161](../figures/figure_161.md): Output stage of capture/compare channel (channel 1).
Removed note related to IC1F bits in Section 18.4.7: TIMx capture/compare mode
register 1 (TIMx_CCMR1).
TIM9 to 14:
Removed note related to IC1F bits in Section 19.5.5: TIM10/11/13/14
capture/compare mode register 1 (TIMx_CCMR1).
USB OTG-HS:
Updated DSPD definition in Section : OTG_HS device configuration register
(OTG_HS_DCFG).
FSMC
Updated DATLAT bits definition in Section : SRAM/NOR-Flash chip-select timing
registers 1..4 (FSMC_BTR1..4).
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1717/1741
RM0090 Revision history
1735
15-May-2014 7
(continued)
FMC
Updated [Figure 474](../figures/figure_474.md): Synchronous multiplexed read mode waveforms - NOR,
PSRAM (CRAM). Updated DATLAT bits definition in Section : SRAM/NOR-Flash
chip-select timing registers 1..4 (FMC_BTR1..4).
Updated FMC_BWTRx register address offsets in [Table 297](../tables/table_297.md): FMC register map.
DEBUG
Added revision code ‘3’ in Section : DBGMCU_IDCODE.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1718/1741 RM0090 Rev 22
14-Oct-2014 8
Memory and bus architecture:
Updated [Table 3](../tables/table_3.md): Memory mapping vs. Boot mode/physical remap  in
STM32F405xx/07xx and STM32F415xx/17xx and [Table 4](../tables/table_4.md): Memory mapping vs.
Boot mode/physical remap  in STM32F42xxx and STM32F43xxx.
RCC (STM32F40/41xx) and RCC (STM32F42/43xx):
Removed all references to Flash programming manual. Changed
RCC_AHB1LPENR, RCC_APB1LPENR, RCC_APB2LPENR, RCC_PLLI2SCFGR
and RCC_APB2LPENR reset values.
Updated access type to “r” for bits 24 to 31 in RCC_CSR.
GPIOs:
Updated [Figure 27](../figures/figure_27.md): Selecting an alternate function on STM32F42xxx and
STM32F43xxx.
IWDG
Update note in [Table 107](../tables/table_107.md): Min/max IWDG timeout period (in ms) at 32 kHz (LSI).
CRYPTO and HASH
Removed STM32F405/407xx and STM32F42xx from the whole sections.
Removed STM32F405/407xx and STM32F42xx from the whole section.
TIM10/11/13/14
Added TIMx_DIER description in Section 19.5: TIM10/11/13/14 registers.
ETHERNET:
Updated [Table 187](../tables/table_187.md): Clock range.
USB OTG FS:
Removed TRDT formula in Section 34.17.7: Worst case response time and added
[Table 203](../tables/table_203.md): TRDT values.
USB OTG HS:
Removed TRDT formula in Section 35.13.8: Worst case response time and added
[Table 213](../tables/table_213.md): TRDT values.
FSMC:
Updated EXTMOD definition in Section : SRAM/NOR-Flash chip-select control
registers 1..4 (FSMC_BCR1..4).
Updated ADDSET definition in Section : SRAM/NOR-Flash chip-select timing
registers 1..4 (FSMC_BTR1..4) and Section : SRAM/NOR-Flash write timing
registers 1..4 (FSMC_BWTR1..4).
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1719/1741
RM0090 Revision history
1735
14-Oct-2014 8
(continued)
FMC:
Modified step 7 in Section : SDRAM initialization.
Modified SDRAM refresh rate equations and example in Section : SDRAM Refresh
Timer register (FMC_SDRTR) and updated definition of COUNT bits.
Updated EXTMOD definition in Section : SRAM/NOR-Flash chip-select control
registers 1..4 (FMC_BCR1..4).
Updated ADDSET definition in Section : SRAM/NOR-Flash chip-select timing
registers 1..4 (FMC_BTR1..4) and Section : SRAM/NOR-Flash write timing
registers 1..4 (FMC_BWTR1..4).
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1720/1741 RM0090 Rev 22
16-Mar-2015 9
PWR:
Updated Section 5.1.2: Battery backup domain.
Updated [Table 23](../tables/table_23.md): Low-power mode summary to add Return from ISR as entry
condition.
Added Section : Entering low-power mode and Section : Exiting low-power mode.
Updated Section : Entering Sleep mode, Section : Exiting Sleep mode, [Table 24](../tables/table_24.md):
Sleep-now entry and exit and [Table 25](../tables/table_25.md): Sleep-on-exit entry and exit.
Updated Section : Entering Stop mode (for STM32F405xx/07xx and
STM32F415xx/17xx), Section : Exiting Stop mode (for STM32F405xx/07xx and
STM32F415xx/17xx) and [Table 27](../tables/table_27.md): Stop mode entry and exit (for
STM32F405xx/07xx and STM32F415xx/17xx). Updated Section : Entering Stop
mode (STM32F42xxx and STM32F43xxx), Section : Exiting Stop mode
(STM32F42xxx and STM32F43xxx) and [Table 29](../tables/table_29.md): Stop mode entry and exit
(STM32F42xxx and STM32F43xxx).
Updated Section : Entering Standby mode, Section : Exiting Standby mode and
[Table 30](../tables/table_30.md): Standby mode entry and exit.
RCC:
Updated bits 24 to 31 access type in Section 7.3.21: RCC clock control & status
register (RCC_CSR).
GPIOs:
Added port A reset value in Section 8.4.3: GPIO port output speed register
(GPIOx_OSPEEDR)  (x = A..I/J/K).
DMA:
Update FTH[1:0] description in Section 10.5.10: DMA stream x FIFO control
register (DMA_SxFCR) (x = 0..7).
TIM2/5:
Register format changed to 32 bits instead of 16 in Section 18.4.10: TIMx counter
(TIMx_CNT) and Section 18.4.12: TIMx auto-reload register (TIMx_ARR).
TIM9 to 14:
Updated [Table 101](../tables/table_101.md): TIMx internal trigger connection
WWDG:
Updated [Figure 214](../figures/figure_214.md): Watchdog block diagram and Section 22.4: How to program
the watchdog timeout.
Updated [Figure 215](../figures/figure_215.md): Window watchdog timing diagram
RNG:
Replaced PLL48CLK by RNG_CLK in the whole section.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1721/1741
RM0090 Revision history
1735
16-Mar-2015 9
(continued)
I2C2:
Updated FREQ[5:0] description in Section 27.6.2: I2C Control register 2
(I2C_CR2).
USART:
Removed note related to RXNEIE in Section : Reception using DMA
FSMC:
Updated [Figure 474](../figures/figure_474.md): Synchronous multiplexed read mode waveforms - NOR,
PSRAM (CRAM).
USB OTG FS
Updated [Table 203](../tables/table_203.md): TRDT values
FMC
Updated FMC_NL in [Figure 456](../figures/figure_456.md): FMC block diagram.
Updated ‘Memory wait’ and ‘Memory data bus high-z’ parameters in [Table 289](../tables/table_289.md):
Programmable NAND Flash/PC Card access parameters.
Updated Section : Common memory space timing register 2..4 (FMC_PMEM2..4).
Updated [Figure 476](../figures/figure_476.md): NAND Flash/PC Card controller waveforms for common
memory access.
DEBUG:
Updated REV_ID[15:0) and JTAG ID code in Section 38.6.1: MCU device ID code
and Section 38.6.2: Boundary scan TAP, respectively
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1722/1741 RM0090 Rev 22
28-Jul-2015 10
Embedded Flash memory interface
Updated Section 3.7.5: Proprietary code readout protection (PCROP),
Power controller (PWR)
Added the last sentence in Subsection: Entering low-power mode of Section 5.3:
Low-power modes,
Added the bullet points about the interrupt in mode entry in [Table 24](../tables/table_24.md): Sleep-now
entry and exit, [Table 25](../tables/table_25.md): Sleep-on-exit entry and exit, [Table 27](../tables/table_27.md): Stop mode entry
and exit (for STM32F405xx/07xx and STM32F415xx/17xx), [Table 29](../tables/table_29.md): Stop mode
entry and exit (STM32F42xxx and STM32F43xxx)
Added the last point to Mode entry, on return from ISR in [Table 30](../tables/table_30.md): Standby mode
entry and exit,
Added the note in Section: Entering sleep mode in Section 5.3.3: Sleep mode.
General-purpose I/Os (GPIO)
Updated OSPEED[1:0] definition of GPIOx_OSPEEDR register in Section 8.4.3:
GPIO port output speed register (GPIOx_OSPEEDR)  (x = A..I/J/K)
LCD-TFT Controller (LTDC)
Corrected the bit field for WHSTPOS in the second bullet point in Section: Window
in Section 16.4.2: Layer programmable parameters.
Advanced-control timers (TIM1&TIM8)
Added the note in Section 17.3.20: Timer synchronization,
Updated ETF[3:0] description in Section 17.4.3: TIM1 and TIM8 slave mode control
register (TIMx_SMCR),
Updated IC1F[3:0] description in Section 17.4.7: TIM1 and TIM8 capture/compare
mode register 1 (TIMx_CCMR1),
Added the note to MMS2 bit description in Section 17.4.8: TIM1 and TIM8
capture/compare mode register 2 (TIMx_CCMR2),
Added the note to SMS[2:0] bit description in Section 17.4.3: TIM1 and TIM8 slave
mode control register (TIMx_SMCR).
General-purpose timers (TIM2 to TIM5)
Added the note in Section 18.3.15: Timer synchronization,
Updated SMS[2:0] description in Section 18.4.3: TIMx slave mode control register
(TIMx_SMCR),
Added the note to MMS2 bit description in Section 18.4.2: TIMx control register 2
(TIMx_CR2),
Added the note to SMS[2:0] bit description in Section 18.4.3: TIMx slave mode
control register (TIMx_SMCR).
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1723/1741
RM0090 Revision history
1735
28-Jul-2015 10
(Continued)
General-purpose timers (TIM9 to TIM14)
Added the note in Section 19.3.12: Timer synchronization (TIM9/12),
Added the note to MMS2 bit description,
Added the note to SMS[2:0] bit description in Section 19.4.2: TIM9/12 slave mode
control register (TIMx_SMCR).
Window watchdog (WWDG)
Updated.[Figure 214](../figures/figure_214.md): Watchdog block diagram
Controller area network (bxCAN)
Replaced tCAN with tq,
Flexible static memory controller (FSMC)
Added the paragraph about Cross boundary page for Cellular RAM 1.5 in Section
36.5.5: Synchronous transactions,
Updated MEMHIZx, MEMHOLDx, MEMSETx bit field descriptions for
FSMC_PME2..4 register in Section 36.5.5: Synchronous transactions,
Updated ATTSET, ATTHOLD, ATTHIZ bit field descriptions for FSMC_PATT2..4
register in Section 36.5.5: Synchronous transactions,
Updated IRS and IFS bit descriptions for FMC_SR2..4 in Section 36.5.5:
Synchronous transactions,
Renamed ADDSET as ADDSET[3:0] and MTYP as MTYP[1:0],
Addition of CPSIZE in FSMC_BCRx bit fields in [Table 226](../tables/table_226.md): FSMC_BCRx bit fields,
[Table 228](../tables/table_228.md): FSMC_BCRx bit fields, [Table 231](../tables/table_231.md): FSMC_BCRx bit fields, [Table 234](../tables/table_234.md):
FSMC_BCRx bit fields, [Table 237](../tables/table_237.md): FSMC_BCRx bit fields, [Table 240](../tables/table_240.md): FSMC_BCRx
bit fields, [Table 242](../tables/table_242.md): FSMC_BCRx bit fields,
Added CPIZE[2:0] in FMC_BCR1...4 registers in ,Section 36.5.6: NOR/PSRAM
control registers Section NOR/PSRAM control re
Added CPSIZE[2:0] for FMC_BCRx registers in Section 36.6.9: FSMC register
map.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1724/1741 RM0090 Rev 22
28-Jul-2015 10
(Continued)
Flexible memory controller (FMC)
Added the paragraph about Cross boundary page for Cellular RAM 1.5 in Section
37.5.5: Synchronous transactions,
Updated BUSTURN bit field description for FMC_BTR1..4 register in Section
37.5.6: NOR/PSRAM controller registers,
Updated MEMHIZx, MEMHOLDx, MEMSETx bit field descriptions for
FMC_PME2..4 register in Section 37.6.8: NAND Flash/PC Card controller registers,
Updated ATTSET, ATTHOLD, ATTHIZ bit field descriptions for FMC_PATT2..4
register in Section 37.6.8: NAND Flash/PC Card controller registers,
Updated IRS and IFS bit descriptions for FMC_SR2..4 in Section 37.6.8: NAND
Flash/PC Card controller registers,
Updated the section SDRAM initialization with the last item in the numbered list in
Section 37.7.5: SDRAM controller registers,
Renamed ADDSET as ADDSET[3:0] and MTYP as MTYP[1:0],
Addition of CPSIZE in [Table 269](../tables/table_269.md): FMC_BCRx bit fields, [Table 271](../tables/table_271.md): FMC_BCRx bit
fields, [Table 274](../tables/table_274.md): FMC_BCRx bit fields, [Table 277](../tables/table_277.md): FMC_BCRx bit fields, [Table 280](../tables/table_280.md):
FMC_BCRx bit fields, [Table 283](../tables/table_283.md): FMC_BCRx bit fields, [Table 285](../tables/table_285.md): FMC_BCRx bit
fields, [Table 287](../tables/table_287.md): FMC_BCRx bit fields,
Added the paragraph about Cross boundary page for Cellular RAM 1.5 in Section
37.5.5: Synchronous transactions,
Added CPIZE[2:0] in FMC_BCR1...4 registers in Section 37.5.6: NOR/PSRAM
controller registers,
Added CPSIZE[2:0] for FMC_BCRx registers in Section 37.8: FMC register map.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1725/1741
RM0090 Revision history
1735
20-Oct-2015 11
Reset and clock controller (RCC)
Updated STM32F405/407/415/417xx [Figure 21](../figures/figure_21.md): Clock tree.
Updated
General purpose I/O (GPIOs)
Changed definition of OSPEEDR bits in Section 8.4.3: GPIO port output speed
register (GPIOx_OSPEEDR)  (x = A..I/J/K).
LCD-TFT display controller (LTDC):
Changed LRDC_IER into LTDC_IER in Section 16.5: LTDC interrupts.
Updated AHBP[11:0], AAV[11:0 and TOTALW[11:0 in [Table 92](../tables/table_92.md): LTDC register map
and reset values.
Controller area network (bxCAN):
Updated Section 32.3.4: Acceptance filters and Section 32.7.4: Identifier filtering.
Flexible static memory controller (FSMC)
Updated BUSTURN description in Section : SRAM/NOR-Flash write timing
registers 1..4 (FSMC_BWTR1..4) and Section : SRAM/NOR-Flash chip-select
timing registers 1..4 (FSMC_BTR1..4)
Updated note related to IRS and IFS bits in Section : FIFO status and interrupt
register 2..4 (FSMC_SR2..4).
Flexible memory controller (FMC)
Updated paragraph related to the cacheable read FIFO in Section : SDRAM
controller read cycle.
Updated BUSTURN description in Section : SRAM/NOR-Flash write timing
registers 1..4 (FMC_BWTR1..4) and Section : SRAM/NOR-Flash chip-select timing
registers 1..4 (FMC_BTR1..4).
Updated note related to IRS and IFS bits in Section : FIFO status and interrupt
register 2..4 (FMC_SR2..4).
Real-time clock (RTC2)
Updated WUCKSEL prescaler input in [Figure 237](../figures/figure_237.md): RTC block diagram.
Updated 3rd step in Section : Programming the wakeup timer.
Updated WUTWF bit definition in Section 26.6.4: RTC initialization and status
register (RTC_ISR).
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1726/1741 RM0090 Rev 22
17-May-2016 12
Flash memory interface
Removed note related to boot from Bank 2 in Section 2.4: Boot configuration.
Updated notes in Section 3.7.3: Read protection (RDP).
Changed number of LATENCY bits in Section 3.9.2: Flash access control register
(FLASH_ACR) for STM32F42xxx and STM32F43xxx
In [Table 9](../tables/table_9.md): 1 Mbyte dual bank Flash memory organization (STM32F42xxx and
STM32F43xxx): updated sector 19 size and option bytes (bank 2) address range.
Power control (PWR)
Removed reference to low-power mode in Section 5.1.4: Voltage regulator for
STM32F42xxx and STM32F43xxx, Section : Entering Stop mode (STM32F42xxx
and STM32F43xxx) and Section : Exiting Stop mode (STM32F42xxx and
STM32F43xxx).
Analog-to-digital converter (ADC)
Added note related to ADC_HTR and ADC_LTR register programming in Section
13.13.7: ADC watchdog higher threshold register (ADC_HTR) and Section 13.13.8:
ADC watchdog lower threshold register (ADC_LTR).
Chrom-Art Accelerator™  controller (DMA2D)
Updated Section 11.3.12: DMA2D transfer control (start, suspend, abort and
completion).
Section 11.5.8: DMA2D foreground PFC control register (DMA2D_FGPFCCR):
updated START bit access type
Section 11.5.10: DMA2D background PFC control register (DMA2D_BGPFCCR):
updated START bit access and description.
LCD-TFT controller (LTDC)
Updated Section 16.3.2: LTDC reset and clocks.
Modified LCD_DE description in [Table 89](../tables/table_89.md): LCD-TFT pins and signal interface.
Modified Section 16.7.15: LTDC Layerx Window Horizontal Position Configuration
Register (LTDC_LxWHPCR) (where x=1..2) and Section 16.7.16: LTDC Layerx
Window Vertical Position Configuration Register (LTDC_LxWVPCR) (where
x=1..2).
General-purpose timers (TIM2 to TIM5)
Updated Section 18.4.11: TIMx prescaler (TIMx_PSC).
General-purpose timers (TIM9 to TIM14)
Added OPM bit in Section 19.5.1: TIM10/11/13/14 control register 1 (TIMx_CR1).
Updated Section 19.4.9: TIM9/12 prescaler (TIMx_PSC) and Section 19.5.8:
TIM10/11/13/14 prescaler (TIMx_PSC).
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1727/1741
RM0090 Revision history
1735
17-May-2016 12
(continued)
General-purpose timers (TIM6 and TIM7)
Updated Section 20.4.7: TIM6 and TIM7 prescaler (TIMx_PSC).
Real-time clock (RTC)
Updated conditions for running under System reset in Section 26.3.7: Resetting the
RTC.
Updated Section 26.3.14: Calibration clock output.
Added note related to TSE in Section 26.6.3: RTC control register (RTC_CR).
Updated caution note related to TAMP1TRG in Section 26.6.17: RTC tamper and
alternate function configuration register (RTC_TAFCR) register.
Universal synchronous asynchronous receiver transmitter (USART)
Replaced all occurrences of nCTS by CTS, nRTS by RTS and SCLK by CK.
Flexible static memory controller (FSMC)
Updated Section 36.3: AHB interface.
Added note related to the hold phase delay below [Figure 454](../figures/figure_454.md): NAND/PC Card
controller timing for common memory access.
Updated Section 36.6.5: NAND Flash prewait functionality.
Updated BUSTURN description in Section : SRAM/NOR-Flash chip-select timing
registers 1..4 (FSMC_BTR1..4).
Updated MEMHOLDx in Section : Common memory space timing register 2..4
(FSMC_PMEM2..4) and ATTHOLD in Section : Attribute memory space timing
registers 2..4 (FSMC_PATT2..4).
Flexible memory controller (FMC)
Updated Section 37.3: AHB interface.
Added note related to the hold phase delay below [Figure 476](../figures/figure_476.md): NAND Flash/PC
Card controller waveforms for common memory access.
Updated Section 37.6.5: NAND Flash prewait functionality.
Updated BUSTURN description in Section : SRAM/NOR-Flash chip-select timing
registers 1..4 (FMC_BTR1..4).
Updated MEMHOLDx in Section : Common memory space timing register 2..4
(FMC_PMEM2..4) and ATTHOLD in Section : Attribute memory space timing
registers 2..4 (FMC_PATT2..4).
Debug (DBG)
Updated value to be programmed to the ETM Trace Start/stop register to enable the
trace in Section 38.15.4: ETM configuration example.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1728/1741 RM0090 Rev 22
20-Sep-2016 13
Analog-to-digital converter (ADC)
Updated DMA mode 1 and DMA mode 3 description in Section 13.9: Multi ADC
mode.
LCD-TFT controller
Updated values to be programmed to LTDC_SSCR in Section : Example of
Synchronous timings configuration
Updated Section 16.4.2: Layer programmable parameters/Windowing.
Advanced-control timers (TIM1 and TIM8)
Updated Section 17.3.21: Debug mode.
Extended Section 17.4.20: TIM1 and TIM8 DMA address for full transfer
(TIMx_DMAR) to 32 bits.
Updated [Table 95](../tables/table_95.md): Output control bits for complementary OCx and OCxN channels
with  break feature output state for MOE = 0.
Updated TIM1 and TIM8 auto-reload register (TIMx_ARR) reset value.
Updated TIMx_CCR1/2/3/4 description when CC1 channel is configured as inputs
and changed bit access type to rw/ro.
General-purpose timers (TIM2 to TIM5)
Updated TIMx auto-reload register (TIMx_ARR) reset value.
Updated TIMx_CCR1/2/3/4 description when CC1 channel is configured as inputs
and changed bit access type to rw/ro.
General-purpose timers (TIM9 to TIM14)
Updated TIM9/12 auto-reload register (TIMx_ARR) and TIM10/11/13/14 auto-
reload register (TIMx_ARR) reset value.
Updated TIMx_CCR1 description when CC1 channel is configured as inputs and
changed bit access type to rw/ro.
Basic timers (TIM6 to TIM7)
Updated TIM6 and TIM7 auto-reload register (TIMx_ARR).
Secure digital input/output interface (SDIO)
Updated Section 31.1: SDIO main features up to 50 MHz.
Updated Section 31.3: SDIO functional description SDIO_CK description.
Updated note removing 48 MHz in Section 31.9.1: SDIO power control register
(SDIO_POWER), Section 31.9.2: SDI clock control register (SDIO_CLKCR),
Section 31.9.4: SDIO command register (SDIO_CMD) and Section 31.9.9: SDIO
data control register (SDIO_DCTRL).
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1729/1741
RM0090 Revision history
1735
20-Sep-2016 13
(continued)
FMC
Update BUSTURN bit description in Section : SRAM/NOR-Flash chip-select timing
registers 1..4 (FMC_BTR1..4) and Section : SRAM/NOR-Flash write timing
registers 1..4 (FMC_BWTR1..4).
Debug support
Specified behavior of timers with complementary outputs in Section 38.16.2: Debug
support for timers, watchdog, bxCAN and I2C.
Updated DBG_TIMx_STOP bit description in Section 38.16.4: Debug MCU APB1
freeze register (DBGMCU_APB1_FZ) and Section 38.16.4: Debug MCU APB1
freeze register (DBGMCU_APB1_FZ).
Electronic signature
Updated Section 24.1: Unique device ID register (96 bits).
21-Apr-2017 14
Updated:
– Section 5.5.2: PWR power control/status register (PWR_CSR) for STM32F42xxx
and STM32F43xxx
– Section 6.3.14: RCC APB2 peripheral clock enable register (RCC_APB2ENR)
– Section 14.3.5: DAC output voltage
– Section 38.6.1: MCU device ID code
– [Figure 237](../figures/figure_237.md): RTC block diagram
Deleted:
– Section 7.3.15: RCC APB2 peripheral clock enable register(RCC_APB2ENR)
18-Jul-2017 15
Updated:
– Section 3.9.10: Flash option control register (FLASH_OPTCR) for STM32F42xxx
and STM32F43xxx
– OTG_FS USB configuration register (OTG_FS_GUSBCFG)
– [Table 142](../tables/table_142.md): Error calculation for programmed baud rates at fPCLK = 42  MHz or
fPCLK = 84 Hz,  oversampling by 16 and [Table 143](../tables/table_143.md): Error calculation for
programmed baud rates at fPCLK = 42  MHz or fPCLK = 84 MHz,  oversampling
by 8.
23-Apr-2018 16
Updated:
– Section 30.6.1: Status register (USART_SR)
– Section 34.16.4: Device-mode registers
– Section 34.17.6: Operational model
– Section 35.12.4: Device-mode registers
– Section 34: USB on-the-go full-speed (OTG_FS)
– [Table 199](../tables/table_199.md): Host-mode control and status registers (CSRs)
– [Table 205](../tables/table_205.md): OTG_FS register map and reset values
– [Table 210](../tables/table_210.md): Device-mode control and status registers
– [Table 215](../tables/table_215.md): OTG_HS register map and reset values
Added:
– [Figure 412](../figures/figure_412.md): SOF trigger output to TIM2 ITR1 connection
– RXOLNY register changed from SPI_CR2 to SPI_CR1 in Section 28.3.4:
Configuring the SPI for half-duplex communication and Unidirectional receive-
only procedure (BIDIMODE=0 and RXONLY=1)
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1730/1741 RM0090 Rev 22
07-Jun-2018 17
Updated:
– [Figure 16](../figures/figure_16.md): Clock tree (STM32F42xxx an STM32F43xxx) and [Figure 21](../figures/figure_21.md): Clock
tree (STM32F405xx/07xx and STM32F415xx/17xx)
– [Figure 27](../figures/figure_27.md): Selecting an alternate function on STM32F42xxx and STM32F43xxx
– [Table 61](../tables/table_61.md): Vector table for STM32F405xx/07xx and STM32F415xx/17xx and [Table 62](../tables/table_62.md): Vector table for STM32F42xxx and STM32F43xxx
– Section 29.17.5: SAI xInterrupt mask register (SAI_xIM) where x is A or B
– Section 38.6.1: MCU device ID code
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1731/1741
RM0090 Revision history
1735
25-Feb-2019 18
Section 6: Reset and clock control for STM32F42xxx and STM32F43xxx (RCC)
Updated OTGHSULPILPEN bit description in RCC AHB1 peripheral clock enable in
low power mode register (RCC_AHB1LPENR) and OTGHSULPIEN bit description
in RCC AHB1 peripheral clock register (RCC_AHB1ENR).
Section 7: Reset and clock control for   STM32F405xx/07xx and
STM32F415xx/17xx(RCC):
Updated RCC APB2 peripheral clock enabled in low power mode register
(RCC_APB2LPENR) reset value.
Updated OTGHSULPILPEN bit description in RCC AHB1 peripheral clock enable in
low power mode register (RCC_AHB1LPENR) and OTGHSULPIEN bit description
in RCC AHB1 peripheral clock enable register (RCC_AHB1ENR).
Section 13: Analog-to-digital converter (ADC)
Update Section : Dual ADC mode.
Section 17: Advanced-control timers (TIM1 and TIM8)
Updated [Figure 113](../figures/figure_113.md): Capture/compare channel 1 main circuit.
[Figure 19](../figures/figure_19.md): General-purpose timers (TIM9 to TIM14)
Updated [Figure 194](../figures/figure_194.md): Capture/compare channel 1 main circuit.
Section 34: USB on-the-go full-speed (OTG_FS)
Updated Section : SETUP and OUT data transfers and Updated Section : IN data
transfers. Modified [Table 200](../tables/table_200.md): Device-mode control and status registers.
Section 35: USB on-the-go high-speed (OTG_HS)
Updated [Table 208](../tables/table_208.md): Core global control and status registers (CSRs) and [Table 210](../tables/table_210.md):
Device-mode control and status registers.
Updated Section : OTG_HS device IN endpoint transmit FIFO size register
(OTG_HS_DIEPTXFx) (x = 1..5, where x is the FIFO_number), Section : OTG
device endpoint-x control register (OTG_HS_DIEPCTLx) (x = 0..5, where x =
Endpoint_number), Section : OTG_HS device endpoint-x control register
(OTG_HS_DOEPCTLx) (x = 1..5, where x = Endpoint_number), Section : OTG_HS
device endpoint-x interrupt register (OTG_HS_DIEPINTx) (x = 0..5, where x =
Endpoint_number), Section : OTG_HS device endpoint-x interrupt register
(OTG_HS_DOEPINTx) (x = 0..5, where x = Endpoint_number), Section : OTG_HS
device endpoint-x DMA address register (OTG_HS_DIEPDMAx /
OTG_HS_DOEPDMAx) (x = 0..5, where x = Endpoint_number).
Updated Section : SETUP and OUT data transfers and Section : IN data transfers.
Section 38: Debug support (DBG)
Updated REV_ID in DBGMCU_CR register.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1732/1741 RM0090 Rev 22
25-Feb-2021 19
Updated:
– Section 2: Memory and bus architecture:
– [Figure 1](../figures/figure_1.md): System architecture for STM32F405xx/07xx and STM32F415xx/17xx
devices
– [Figure 2](../figures/figure_2.md): System architecture for STM32F42xxx and STM32F43xxx devices
– Section 3: Embedded Flash memory interface:
– [Table 16](../tables/table_16.md): Description of the option bytes (STM32F405xx/07xx and
STM32F415xx/17xx)
– [Table 17](../tables/table_17.md): Description of the option bytes  (STM32F42xxx and STM32F43xxx)
– Section 12: Interrupts and events:
– [Table 61](../tables/table_61.md): Vector table for STM32F405xx/07xx and STM32F415xx/17xx
– [Table 62](../tables/table_62.md): Vector table for STM32F42xxx and STM32F43xxx
– Section 13: Analog-to-digital converter (ADC):
– Section 13.3.5: Continuous conversion mode
– Section 13.8.1: Using the DMA
– Section 13.10: Temperature sensor
– Section 17: Advanced-control timers (TIM1 and TIM8):
– [Figure 86](../figures/figure_86.md): Advanced-control timer block diagram
– Section 17.4.9: TIM1 and TIM8 capture/compare enable register (TIMx_CCER)
– Section 27: Inter-integrated circuit (I2C) interface:
– Section 27.6.2: I2C Control register 2 (I2C_CR2)
– Section 27.6.8: I2C Clock control register (I2C_CCR)
– Section 31: Secure digital input/output interface (SDIO):
– Section 31.9.2: SDI clock control register (SDIO_CLKCR)
– Section 32: Controller area network (bxCAN):
– Section 32.4.1: Initialization mode
– Section 33: Ethernet (ETH): media access control (MAC) with DMA controller:
– Section : TxDMA operation: default (non-OSF) mode
– Section : Normal Tx DMA descriptors
– Section 35: USB on-the-go high-speed (OTG_HS):
– Section : Host port power
– Section : OTG_HS core interrupt register (OTG_HS_GINTSTS)
– Section : OTG_HS all endpoints interrupt mask register (OTG_HS_DAINTMSK)
– [Table 215](../tables/table_215.md): OTG_HS register map and reset values
– Section 35.13.2: Host initialization
– [Figure 416](../figures/figure_416.md): Transmit FIFO write task
– [Figure 417](../figures/figure_417.md): Receive FIFO read task
– [Figure 426](../figures/figure_426.md): Receive FIFO packet read in slave mode
– [Figure 427](../figures/figure_427.md): Processing a SETUP packet
– Section 38: Debug support (DBG):
– Section : DBGMCU_IDCODE
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1733/1741
RM0090 Revision history
1735
05-Feb-2024 20
Section : Introduction:
– Mentioned that the microcontrollers include ST state-of-the-art patented
technology
– Added errata sheets in the list of reference documents.
Section 2: Memory and bus architecture
– Section 2.3.1: Embedded SRAM, updated the SRAM that can be accessed
through System or I-Code/D-Code bus.
Section 3.4: Embedded flash memory in STM32F42xxx and STM32F43xxx
– Updated Bank 2 section 14 base address in [Table 12](../tables/table_12.md): Flash module - 2 Mbyte
dual bank organization (STM32F42xxx and STM32F43xxx).
– Specified that dual bank organization is not available on 512 Kbyte devices, and
added [Table 16](../tables/table_16.md): 512 Kbyte single bank flash memory organization
(STM32F42xxx and STM32F43xxx).
– Updated Section 3.8.2: Program/erase parallelism.
–I n  Section 3.9.3: Read protection (RDP), added note concerning RDP when
debugger is connected through JTAG/SWD.
Section 5: Power controller (PWR)
– Updated [Figure 12](../figures/figure_12.md): Power-on reset/power-down reset waveform.
– Updated no external battery use case in Section 5.1.2: Battery backup domain.
– Updated DBP bit description in PWR power control register (PWR_CR) for
STM32F405xx/07xx and STM32F415xx/17xx and PWR power control register
(PWR_CR) for STM32F42xxx and STM32F43xxx.
– Updated BRE bit description in PWR power control/status register (PWR_CSR)
for STM32F405xx/07xx and STM32F415xx/17xx and PWR power control/status
register (PWR_CSR) for STM32F42xxx and STM32F43xxx.
Section 6: Reset and clock control for   STM32F42xxx and STM32F43xxx and
NA(RCC)
– Updated Section 6.1.1: System reset and Section 6.1.3: Backup domain reset.
– Updated ethernet PTP clock in [Figure 16](../figures/figure_16.md): Clock tree.
– Added note regarding backup domain reset in BDRST bit of RCC Backup domain
control register (RCC_BDCR).
– Added register reset values in [Table 38](../tables/table_38.md): RCC register map and reset values for
STM32F42xxx and STM32F43xxx
Section 7: Reset and clock control for   STM32F405xx/07xx and
STM32F415xx/17xx(RCC)
– Updated Section 7.1.1: System reset and Section 7.1.3: Backup domain reset.
– Updated ethernet PTP clock in [Figure 21](../figures/figure_21.md): Clock tree
– Added note regarding backup domain reset in BDRST bit of RCC Backup domain
control register (RCC_BDCR).
– Added register reset values in [Table 39](../tables/table_39.md): RCC register map and reset values for
STM32F405xx/07xx and STM32F415xx/17xx
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

Revision history RM0090
1734/1741 RM0090 Rev 22
05-Feb-2024 20
(continued)
Section 10: DMA controller (DMA)
Updated DMA stream x FIFO control register (DMA_SxFCR) (x = 0..7) address
offset.
Section 12: Interrupts and events
Changed Pending register (EXTI_PR) reset value to 0x0000 0000.
Section 17: Advanced-control timers (TIM1 and TIM8)
Updated Section 17.3.7: PWM input mode.
Updated SMS in Section 17.4.3: TIM1 and TIM8 slave mode control register
(TIMx_SMCR).
Updated OC1PE in Section 17.4.7: TIM1 and TIM8 capture/compare mode register
1 (TIMx_CCMR1).
Section 22: Window watchdog (WWDG)
Updated tWWDG equation in Section 22.4: How to program the watchdog timeout.
Section 26: Real-time clock (RTC)
– Updated HSE clock in [Figure 237](../figures/figure_237.md): RTC block diagram (NA devices).
– Updated Section 26.3.6: Reading the calendar.
Section 29: Serial audio interface (SAI)
– In the whole section, replaced TDM by free protocol mode.
–I n  Section 29.18.4: SAI x frame configuration register (SAI_XFRCR) where x is A
or B, specified that FRL[7:0] must be configured when the audio block is
disabled.
Section 34: USB on-the-go full-speed (OTG_FS)
– Updated [Figure 392](../figures/figure_392.md): Device-mode FIFO address mapping and AHB FIFO
access mapping.
– Modified OTG_FS USB configuration register
(OTG_FS_GUSBCFG)OTG_FS_GUSBCFG reset value.
Section 33: Ethernet (ETH): media access control (MAC) with DMA controller
Updated bits that control the checksum in Section : Transmit checksum offload
Section 38: Debug support (DBG)
Removed note on APB bridge write buffer after [Table 302](../tables/table_302.md): Flexible SWJ-DP pin
assignment
Updated REV_ID[15:0] in Section : DBGMCU_IDCODE
Section 39: Device electronic signature
Updated Section 39.1: Unique device ID register (96 bits)
Added Section 40: Important security notice.
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes

RM0090 Rev 22 1735/1741
RM0090 Revision history
1735
07-Jun-2024 21
Updated the note in Bit[11:0] description of Section 18.6.8: I2C Clock control
register (I2C_CCR).
Fixed typo in Section 10.1.3: Interrupt and exception vectors.
04-May-2026 22
Updated:
– Section 3.9.8: Flash control register (FLASH_CR) for  STM32F42xxx and
STM32F43xxx
– Section 5.1.3: Voltage regulator for STM32F405xx/07xx and STM32F415xx/17xx
– Section 13.13.1: ADC status register (ADC_SR)
– Section 26.6.21: RTC register map
– Fixed typo in Section 27: Inter-integrated circuit (I2C) interface
– OTG_FS Host non-periodic transmit FIFO size register
(OTG_FS_HNPTXFSIZ)/Endpoint 0 Transmit FIFO size (OTG_FS_DIEPTXF0)
in Section 34: USB on-the-go full-speed (OTG_FS)
[Table 315](../tables/table_315.md). Document revision history (continued)
Date Version Changes
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 1: Architectural Diagram](../figures/figure_1.md)
* [Figure 2: Architectural Diagram](../figures/figure_2.md)
* [Figure 5: Architectural Diagram](../figures/figure_5.md)
* [Figure 7: Architectural Diagram](../figures/figure_7.md)
* [Figure 12: Architectural Diagram](../figures/figure_12.md)
* [Figure 16: Architectural Diagram](../figures/figure_16.md)
* [Figure 18: Architectural Diagram](../figures/figure_18.md)
* [Figure 19: Architectural Diagram](../figures/figure_19.md)
* [Figure 20: Architectural Diagram](../figures/figure_20.md)
* [Figure 21: Architectural Diagram](../figures/figure_21.md)
* [Figure 26: Architectural Diagram](../figures/figure_26.md)
* [Figure 27: Architectural Diagram](../figures/figure_27.md)
* [Figure 82: Architectural Diagram](../figures/figure_82.md)
* [Figure 86: Architectural Diagram](../figures/figure_86.md)
* [Figure 113: Architectural Diagram](../figures/figure_113.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 1: Configuration Matrix](../tables/table_1.md)
* [Table 3: Configuration Matrix](../tables/table_3.md)
* [Table 4: Configuration Matrix](../tables/table_4.md)
* [Table 9: Configuration Matrix](../tables/table_9.md)
* [Table 12: Configuration Matrix](../tables/table_12.md)
* [Table 13: Configuration Matrix](../tables/table_13.md)
* [Table 16: Configuration Matrix](../tables/table_16.md)
* [Table 17: Configuration Matrix](../tables/table_17.md)
* [Table 23: Configuration Matrix](../tables/table_23.md)
* [Table 24: Configuration Matrix](../tables/table_24.md)
* [Table 25: Configuration Matrix](../tables/table_25.md)
* [Table 27: Configuration Matrix](../tables/table_27.md)
* [Table 29: Configuration Matrix](../tables/table_29.md)
* [Table 30: Configuration Matrix](../tables/table_30.md)
* [Table 38: Configuration Matrix](../tables/table_38.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)