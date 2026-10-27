# Chapter 50: Revision history

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32G4 Reference Manual RM0440 - Chapter 50: Revision history.
* **Document Source**: RM0440 Reference Manual
* **PDF Reference Location**: Pages 2125 - 2140
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0440 Ingestion)
```text
RM0440 Rev 9 2125/2140
RM0440 Revision history
2133
50 Revision history
[Table 462](../tables/table_462.md). Document revision history
Date Revision Changes
06-May-2019 1 Initial release.
10-Oct-2019 2
Document convention section
– Updated [Table 2](../tables/table_2.md): Product specific features.
System architecture section
– Updated Section 2.1: System architecture replacing FMC by FSMC.
– Updated [Figure 2](../figures/figure_2.md): Memory map replacing FMC by FSMC.
Memory organization section
– Updated [Table 3](../tables/table_3.md): Memory map and peripheral register boundary addresses
– Updated [Table 2](../tables/table_2.md).4: Embedded SRAM SRAM2 (mapped at address 0x2000 4000).
– Updated [Table 7](../tables/table_7.md): Flash module - 512/256/128 KB dual bank organization (64 bits
read width).
– Updated [Table 8](../tables/table_8.md): Flash module - 512/256/128 KB single bank organization (128 bits
read width).
Power control section
– Updated Section 6.1: Power supplies.
Reset and clock control section
– Updated [Figure 17](../figures/figure_17.md): Clock tree.
Updated FMC into FSMC in:
– Section 7.4.10: AHB3 peripheral reset register (RCC_AHB3RSTR).
– Section 7.4.16: AHB3 peripheral clock enable register(RCC_AHB3ENR).
– Section 7.4.22: AHB3 peripheral clocks enable in Sleep and Stop modes register
(RCC_AHB3SMENR).
System controller configuration section
– Updated Section 10.2.1: SYSCFG memory remap register (SYSCFG_MEMRMP)
bits[2:0] description.
Peripherals interconnect matrix section
– Updated [Table 84](../tables/table_84.md): Interconnect 11 on-chip source FLTxSRC[1:0] = 01 column.
Nested vectored interrupt controller section
– Updated [Table 100](../tables/table_100.md): STM32G4 series vector table.
Flexible static memory controller (FSMC) section
– Updated Section 19: Flexible static memory controller (FSMC).
CORDIC co-processor (CORDIC) section
– Updated Section 17: CORDIC coprocessor (CORDIC).
Analog digital converter (ADC) section
– Updated Section 21.4.33: Monitoring the internal voltage reference.
– Updated Section : Sampling time control trigger mode.

Revision history RM0440
2126/2140 RM0440 Rev 9
10-Oct-2019 2 (cont’d)
Digital analog converter (DAC) section
– Updated Section 22: Digital-to-analog converter (DAC).
Comparator section
– Updated Section 24.6.2: COMP register map.
AES hardware accelerator (AES)
- Updated Section 27: AES hardware accelerator (AES).
USB power delivery interface (UCPD)section
– Updated Section 46: USB Type-C®/USB Power Delivery interface (UCPD).
Debug section
– Updated Section 47.4.2: Flexible SWJ-DP pin assignment.
– Updated Section 47.8.3: SW-DP state machine (reset, idle states, ID code) ID code
by 0x2BA01477.
– Updated [Table 459](../tables/table_459.md): Flexible TRACE pin assignment.
– Updated [Table 447](../tables/table_447.md): JTAG debug port data registers.
26-Mar-2020 3
Added Category 4 devices (STM32G491, STM32G4A1) in:
– [Table 1](../tables/table_1.md): STM32G4 series memory density.
– [Table 2](../tables/table_2.md): Product specific features.
– Section 2.4: Embedded SRAM.
– Section 2.4.1: Parity check.
– [Table 4](../tables/table_4.md): CCM SRAM organization.
– Section 2.5: Flash memory overview.
– Section 4: Embedded flash memory (FLASH) for category 4 devices.
– [Table 92](../tables/table_92.md): DMAMUX instantiation.
Embedded Flash memory (FLASH) section:
Updated:
– Number of wait states according to CPU clock (HCLK) frequency tables for all
categories.
– [Table 11](../tables/table_11.md): Option byte organization.
– [Table 21](../tables/table_21.md): Option byte organization.
– Section 3.4.2: Option bytes programming ‘activating dual bank mode (switching from
DBANK=0 to DBANK=1)’ paragraph.
– Section 4.7.6: Flash control register (FLASH_CR) PNB[7:0] bits.
– ‘User and read protection option bytes’ and Section 4.7.8: Flash option register
(FLASH_OPTR) register description adding PB4_PUPEN bit.
– Section 5.7.14: FLASH register map.
Power control section:
Updated:
– [Table 38](../tables/table_38.md): Range 1 boost mode configuration removing the lower SYSCLK limits.
– Section 6.4.2: Power control register 2 (PWR_CR2) PLS[2:0] bit description.
Reset and clock control section:
Updated:
– [Figure 17](../figures/figure_17.md): Clock tree.
– [Table 51](../tables/table_51.md): RCC register map and reset values.
Peripherals interconnect matrix section:
– Updated [Table 62](../tables/table_62.md): STM32G4 series peripherals interconnect matrix.
[Table 462](../tables/table_462.md). Document revision history (continued)
Date Revision Changes

RM0440 Rev 9 2127/2140
RM0440 Revision history
2133
26-Mar-2020 3 (cont’d)
DMA request multiplexer (DMAMUX) section:
– Updated Section 13.3.2: DMAMUX mapping;
Analog digital converter section:
Updated:
– Section 21.2: ADC main features.
– [Figure 83](../figures/figure_83.md): ADC clock scheme.
– [Figure 86](../figures/figure_86.md): ADC3 connectivity.
– Section 21.4.7: Single-ended and differential input channels.
Comparator section:
Updated [Figure 168](../figures/figure_168.md): Comparator block diagram.
Operational amplifier section:
Updated:
– [Table 204](../tables/table_204.md): Operational amplifier possible connection.
– Section 25.3.7: Calibration procedure.
– Section 25.3.8: Timer controlled Multiplexer mode procedure.
– Section 25.5.1: OPAMP1 control/status register (OPAMP1_CSR).
– Section 25.5.2: OPAMP2 control/status register (OPAMP2_CSR).
– Section 25.5.3: OPAMP3 control/status register (OPAMP3_CSR).
– Section 25.5.4: OPAMP4 control/status register (OPAMP4_CSR).
– Section 25.5.5: OPAMP5 control/status register (OPAMP5_CSR).
– Section 25.5.6: OPAMP6 control/status register (OPAMP6_CSR).
FD controller area network section:
Updated Section 44.4.7: FDCAN nominal bit timing and prescaler register
(FDCAN_NBTP) note.
Debug support section:
Updated:
– Section 47.4.3: Internal pull-up and pull-down on JTAG pins.
– Section 47.6.1: MCU device ID code.
– Section 47.6.2: Boundary scan TAP.
Device electronic signature section:
– Added Section 48.3: Package data register.
[Table 462](../tables/table_462.md). Document revision history (continued)
Date Revision Changes

Revision history RM0440
2128/2140 RM0440 Rev 9
14-Apr-2020 4
Embedded Flash memory (FLASH) section:
Updated:
– [Table 9](../tables/table_9.md): Number of wait states according to CPU clock (HCLK) frequency.
– [Table 19](../tables/table_19.md): Number of wait states according to CPU clock (HCLK) frequency.
– [Table 29](../tables/table_29.md): Number of wait states according to CPU clock (HCLK) frequency.
– Section 5.4.1: Option bytes description ‘Securable memory area option bytes’
paragraph.
– Section 5.7.13: Flash securable area register (FLASH_SEC1R).
Reset and clock control (RCC) section:
Updated:
– Section 7.2.4: PLL.
– Section 7.4.4: PLL configuration register (RCC_PLLCFGR) PLLN[6:0] and PLLM[3:0]
description.
High-resolution timer (HRTIM) section:
– Updated Section 27.3.1: General description.
20-Nov-2020 5
Memory map section:
Updated [Table 3](../tables/table_3.md): Memory map and peripheral register boundary addresses USB SRAM
to 1 Kbyte.
Updated [Figure 2](../figures/figure_2.md): Memory map.
Embedded Flash section:
Updated for category 3 devices:
– ‘User and read protection option bytes’ register bit 29,28 name at NRST_MODE.
– ‘Securable memory area Bank 1 option bytes’ register BOOT_LOCK description
removing caution.
– Section 3.7.17: Flash securable area bank1 register (FLASH_SEC1R) BOOT_LOCK
description.
Updated for category 4 devices:
– ‘User and read protection option bytes’ register bit 29,28 name at NRST_MODE.
– ‘Securable memory area option bytes’ register BOOT_LOCK description removing
caution.
– Section 4.7.1: Flash access control register (FLASH_ACR) reset value.
– Section 4.7.13: Flash securable area register (FLASH_SEC1R) BOOT_LOCK
description.
– Section 4.7.14: FLASH register map
Updated for category 2 devices:
– ‘User and read protection option bytes’ register bit 29,28 name at NRST_MODE.
– ‘Securable memory area option bytes’ register BOOT_LOCK description removing
caution.
– Section 5.7.13: Flash securable area register (FLASH_SEC1R) BOOT_LOCK
description.
Updated ‘rw’ to ‘r’ for all option bytes.
[Table 462](../tables/table_462.md). Document revision history (continued)
Date Revision Changes

RM0440 Rev 9 2129/2140
RM0440 Revision history
2133
20-Nov-2020 5 (cont’d)
Replaced ‘default’ by ‘production value’ for RDP level 0 instead of RDP level 1 in:
– [Table 12](../tables/table_12.md): Flash memory read protection status.
– [Figure 4](../figures/figure_4.md): Changing the read protection (RDP) level.
– [Table 22](../tables/table_22.md): Flash memory read protection status.
– [Figure 7](../figures/figure_7.md): Changing the read protection (RDP) level.
– [Table 32](../tables/table_32.md): Flash memory read protection status.
– [Figure 10](../figures/figure_10.md): Changing the read protection (RDP) level.
Power control (PWR) section:
Updated Section 6.4.22: Power control register (PWR_CR5).
Reset and clock control (RCC) section:
Updated
– Section 7.2.11: ADC clock.
– Section 7.4.19: APB2 peripheral clock enable register (RCC_APB2ENR) SPI4EN bit
description.
Peripherals interconnect matrix section:
– Updated [Table 75](../tables/table_75.md): Interconnect 2.
DMA request multiplexer (DMAMUX) section:
Updated:
– Section 13.3.2: DMAMUX mapping.
– Section 13.6.1: DMAMUX request line multiplexer channel x configuration register
(DMAMUX_CxCR).
Nested vectored interrupt controller (NVIC) section:
Updated [Table 100](../tables/table_100.md): STM32G4 series vector table.
Analog-to-digital converters (ADC) section:
Updated Section 21.2: ADC main features.
High-resolution timer (HRTIM) section:
Updated:
– [Table 223](../tables/table_223.md): EExFLTR[3:0] codes depending on UDM bit setting.
– [Table 224](../tables/table_224.md): External events features.
– Section 27.3.8: External events global conditioning.
– Section 27.3.9: External event filtering in timing units.
– Section 27.5.28: HRTIM timer x output 1 reset register (HRTIM_RSTx1R) (x = A to F).
– Section 27.5.66: HRTIM ADC trigger 1 register (HRTIM_ADC1R).
– Section 27.5.67: HRTIM ADC trigger 2 register (HRTIM_ADC2R).
– Section 27.5.68: HRTIM ADC trigger 3 register (HRTIM_ADC3R) adding note.
General-purpose timers (TIM2/TIM3/TIM4/TIM5) section:
Updated [Table 302](../tables/table_302.md): TIM2/TIM3/TIM4/TIM5 register map and reset values.
General purpose timers (TIM15/TIM16/TIM17):
Updated:
– Section 31.8.19: TIMx option register 1 (TIMx_OR1)(x = 16 to 17) address offset to
0x68.
– Section 31.8.22: TIM16/TIM17 register map.
Debug support (DBG) section:
– Updated Section 47.6.1: MCU device ID code REV_ID[15:0] bits description.
[Table 462](../tables/table_462.md). Document revision history (continued)
Date Revision Changes

Revision history RM0440
2130/2140 RM0440 Rev 9
08-Feb-2021 6
Embedded Flash section:
Updated:
– Section 3.5.3: Write protection (WRP).
– Section 3.5.4: Securable memory area.
– Section 3.7.1: Flash access control register (FLASH_ACR) reset value
– Section 4.5.3: Write protection (WRP).
– Section 4.5.4: Securable memory area.
– Section 5.4.1: Option bytes description securable memory area option bytes
paragraph.
– Section 5.5.3: Write protection (WRP).
– Section 5.5.4: Securable memory area.
– Section 5.7.1: Flash access control register (FLASH_ACR) reset value.
Filter math accelerator (FMAC) section:
Updated Section 18.4: FMAC registers
Analog digital converter section:
Updated:
– [Table 181](../tables/table_181.md): ADC register map and reset values for each ADC (offset = 0x000  for
master ADC, 0x100 for slave ADC) ADC_CFGR2 address.
– Section 21.7.6: ADC sample time register 1 (ADC_SMPR1) SMPPLUS bit.
Operational amplifier (OPAMP) section:
– Updated [Table 204](../tables/table_204.md): Operational amplifier possible connection.
USB Type-C™ / USB Power Delivery interface (UCPD) section:
Updated:
– Section 46.8.3: UCPD control register (UCPD_CR).
– Section 46.8.15: UCPD register map.
Removed UCPD configuration register 3 (UCPD_CFGR3).
Debug support (DBG) section:
Updated Section 47.4.2: Flexible SWJ-DP pin assignment removing note.
[Table 462](../tables/table_462.md). Document revision history (continued)
Date Revision Changes

RM0440 Rev 9 2131/2140
RM0440 Revision history
2133
04-Feb-2022 7
Updated:
– Related documents
– Section 2.2: Memory organization
– [Table 7](../tables/table_7.md): Flash module - 512/256/128 KB dual bank organization (64 bits read width)
– [Table 8](../tables/table_8.md): Flash module - 512/256/128 KB single bank organization (128 bits read
width)
– Section 3: Embedded flash memory (FLASH) for category 3 devices
– Section 3.4.1: Option bytes description
– Section 3.7.5: Flash status register (FLASH_SR)
– Section 3.7.8: Flash option register (FLASH_OPTR)
– Section 4: Embedded flash memory (FLASH) for category 4 devices
– Section 4.4.1: Option bytes description
– Section 4.7.5: Flash status register (FLASH_SR)
– Section 4.7.8: Flash option register (FLASH_OPTR)
– [Table 18](../tables/table_18.md): Flash module - 256/512 Kbytes organization (64 bits read width)
– [Table 28](../tables/table_28.md): Flash module - 32/64/128 Kbytes organization (64-bit read width)
– Section 5: Embedded flash memory (FLASH) for category 2 devices
– Section 5.4.1: Option bytes description
– Section 5.7.5: Flash status register (FLASH_SR)
– Section 5.7.8: Flash option register (FLASH_OPTR)
– Section 6.2.3: Peripheral Voltage Monitoring (PVM)
– Section 6.4.2: Power control register 2 (PWR_CR2)
– [Table 51](../tables/table_51.md): RCC register map and reset values
– Section 9.3.15: Using PB8 as GPIO
– Section 9.4.1: GPIO port mode register (GPIOx_MODER) (x =A to G)
– Section 10.2.2: SYSCFG configuration register 1 (SYSCFG_CFGR1)
– [Table 100](../tables/table_100.md): STM32G4 series vector table
– Section 18.4.7: FMAC write data register (FMAC_WDATA)
– Section 18.4.8: FMAC read data register (FMAC_RDATA)
– [Figure 151](../figures/figure_151.md): DMA requests in regular simultaneous mode when MDMA = 10
– Section 24.6.1: Comparator x control and status register (COMP_CxCSR)
– Section 24.6.2: COMP register map
– Section 25.3.7: Calibration
– Section 27.5.68: HRTIM ADC trigger 3 register (HRTIM_ADC3R)
– Section 27.5.81: HRTIM fault input register 4 (HRTIM_FLTINR4)
– [Table 245](../tables/table_245.md): HRTIM register map and reset values – common functions
– Section 42.5.9: Data transmission and reception procedures
– [Figure 546](../figures/figure_546.md): Transfer bus diagrams for I2C target receiver  (mandatory events only)
– [Table 402](../tables/table_402.md): CAN subsystem I/O signals
– [Figure 670](../figures/figure_670.md): Message RAM configuration
– Section 44.4.3: FDCAN data bit timing and prescaler register (FDCAN_DBTP)
Added:
– Section 21.5: ADC in low-power mode
– [Table 177](../tables/table_177.md): Effect of low-power modes on the ADC
– Section 31.4.18: 6-step PWM generation
[Table 462](../tables/table_462.md). Document revision history (continued)
Date Revision Changes

Revision history RM0440
2132/2140 RM0440 Rev 9
12-Feb-2024 8
Updated Section 2.2.2: Memory map and register boundary addresses, Section 3.5.1:
Read protection (RDP), Section 5.7.6: Flash control register (FLASH_CR),
Section 7.4.1: Clock control register (RCC_CR), Section 7.4.20: AHB1 peripheral clocks
enable in Sleep and Stop modes register (RCC_AHB1SMENR), Section 9.3: GPIO
functional description, Section 8.7.1: CRS control register (CRS_CR), Section 12.2:
DMA main features, Section 21.4.10: Constraints when writing the ADC control bits,
Section 21.7.16: ADC injected sequence register (ADC_JSQR), Section 24.5: COMP
interrupts, Section 28.2: Main features, Section 28.3.17: Fault protection,
Section 30.5.10: TIMx capture/compare mode register 2 [alternate] (TIMx_CCMR2)(x =
2 to 5), Section 31.7.3: TIM15 slave mode control register (TIM15_SMCR),
Section 37.3.4: Clock and prescalers, note in sections 37.6.18 and 37.6.19,
Section 41.4.2: LPUART signals, Section 42.3: I2S main features, Section 42.7.1: I2S
general description, Power-down (Sleep mode), Rx handling, Standard message ID
filtering, Extended message ID filtering, and Section 44.3.7: FIFO acknowledge
handling.
Updated User and read protection option bytes in sections 3, 4, and 5.
Reorganized description of registers in Section 28: High-resolution timer (HRTIM) and
in Section 43: Serial audio interface (SAI).
Updated [Table 11](../tables/table_11.md): Option byte organization, [Table 31](../tables/table_31.md): Option byte organization,
[Table 51](../tables/table_51.md): RCC register map and reset values, [Table 55](../tables/table_55.md): Effect of low-power modes on
CRS, [Table 100](../tables/table_100.md): STM32G4 series vector table, tables 166 to 169, [Table 198](../tables/table_198.md): VREFBUF
register map and reset values, tables in Section 28.3.2: HRTIM pins and internal
signals, [Table 260](../tables/table_260.md): HRTIM register map and reset values – common functions,
[Table 402](../tables/table_402.md): CAN subsystem I/O signals, [Table 424](../tables/table_424.md): Bulk double-buffering memory
buffers usage, and [Table 441](../tables/table_441.md): Type-C sequence (source: 3A); cable/sink connected (Rd
on CC1; Ra on CC2).
Added footnote to [Table 5](../tables/table_5.md): Boot modes.
Added [Table 371](../tables/table_371.md): USART/UART input/output pins, [Table 372](../tables/table_372.md): USART internal
input/output signals, [Table 381](../tables/table_381.md): LPUART input/output pins, and [Table 382](../tables/table_382.md): LPUART
internal input/output signals.
Updated figures in Section 20: Quad-SPI interface (QUADSPI), [Figure 83](../figures/figure_83.md): ADC clock
scheme, figures 99 to 104, [Figure 156](../figures/figure_156.md): Dual-channel DAC block diagram, [Figure 171](../figures/figure_171.md):
Standalone mode: external gain setting mode, [Figure 244](../figures/figure_244.md): Latency to external events
(counter reset and output set), [Figure 245](../figures/figure_245.md): Latency to external events (output reset on
external event), [Figure 385](../figures/figure_385.md): General-purpose timer block diagram, [Figure 591](../figures/figure_591.md): LPUART
block diagram, [Figure 543](../figures/figure_543.md): Transfer bus diagrams for I2C target transmitter (mandatory
events only), [Figure 546](../figures/figure_546.md): Transfer bus diagrams for I2C target receiver  (mandatory
events only), [Figure 553](../figures/figure_553.md): Transfer bus diagrams for I2C controller transmitter
(mandatory events only), [Figure 556](../figures/figure_556.md): Transfer bus diagrams for I2C controller receiver
(mandatory events only), [Figure 529](../figures/figure_529.md): Independent watchdog block diagram,
[Figure 530](../figures/figure_530.md): Watchdog block diagram, and [Figure 663](../figures/figure_663.md): CAN subsystem..
Added Section 49: Important security notice.
Minor text edits across the whole document.
[Table 462](../tables/table_462.md). Document revision history (continued)
Date Revision Changes

RM0440 Rev 9 2133/2140
RM0440 Revision history
2133
14-Mar-2025 9
Rearranged sequence of sections.
Updated Introduction. Section 3.3.1: Flash memory organization, Section 3.4.1: Option
bytes description, Modifying user options, Flash securable area bank1 register
(FLASH_SEC1R), Section 3.5.4: Securable memory area, Section 3.7.17: Flash
securable area bank1 register (FLASH_SEC1R), Section 4.4.1: Option bytes
description, Modifying user options, Section 4.5.6: Forcing boot from flash memory,
Section 4.7.12: Flash WRP area B address register (FLASH_WRP1BR),
Section 4.7.13: Flash securable area register (FLASH_SEC1R), Section 5.4.1: Option
bytes description, Section 5.5.6: Forcing boot from flash memory, Section 5.7.12: Flash
WRP area B address register (FLASH_WRP1BR), Section 5.7.13: Flash securable area
register (FLASH_SEC1R), Section 7.1.2: System reset, Section 7.2.7: System clock
(SYSCLK) selection. Section 9.3.2: I/O pin alternate function multiplexer and mapping,
Section 15.5.6: Pending register 1 (EXTI_PR1), Section 15.5.12: Pending register 2
(EXTI_PR2), Auto-injection mode, Analog watchdog filter for watchdog 1, ADC
configuration register (ADC_CFGR), Section 22.4.11: DAC sawtooth wave generation,
Section 22.4.13: DAC channel buffer calibration, Section 22.7.23: DAC sawtooth mode
register (DAC_STMODR), Section 40.5.7: USART baud rate generation, and
Section 48.3: Package data register.
Replaced SQRx and JSQRx by ADC_SQRy and ADC_JSQR registers, when referring
to registers, JSQRi and SQRi registers by JSQi and SQi bits, when referring to bits in
Section 21: Analog-to-digital converters (ADC).
Updated [Table 1](../tables/table_1.md): STM32G4 series memory density, [Table 28](../tables/table_28.md): Flash module -
32/64/128 Kbytes organization (64-bit read width), [Table 99](../tables/table_99.md): DMAMUX register map
and reset values for category 3 and 4 devices, and [Table 265](../tables/table_265.md): Interconnect to the
tim_ti3 input multiplexer.
Added footnote to Section 13.6.1: DMAMUX request line multiplexer channel x
configuration register (DMAMUX_CxCR) and [Table 98](../tables/table_98.md): DMAMUX register map and
reset values for category 2 devices.
Updated [Figure 17](../figures/figure_17.md): Clock tree and [Figure 379](../figures/figure_379.md): Measuring time interval between edges
on three signals.
Minor text edits across the whole document.
[Table 462](../tables/table_462.md). Document revision history (continued)
Date Revision Changes

Index RM0440
2134/2140 RM0440 Rev 9
Index
A
ADC_AWD2CR  . . . . . . . . . . . . . . . . . . . . . . .702
ADC_AWD3CR  . . . . . . . . . . . . . . . . . . . . . . .702
ADC_CALFACT . . . . . . . . . . . . . . . . . . . . . . .703
ADC_CFGR . . . . . . . . . . . . . . . . . . . . . . . . . .684
ADC_CFGR2 . . . . . . . . . . . . . . . . . . . . . . . . .688
ADC_CR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .681
ADC_DIFSEL . . . . . . . . . . . . . . . . . . . . . . . . .703
ADC_DR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .698
ADC_GCOMP  . . . . . . . . . . . . . . . . . . . . . . . .704
ADC_IER  . . . . . . . . . . . . . . . . . . . . . . . . . . . .679
ADC_ISR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .677
ADC_JDRy . . . . . . . . . . . . . . . . . . . . . . . . . . .701
ADC_JSQR  . . . . . . . . . . . . . . . . . . . . . . . . . .698
ADC_OFRy  . . . . . . . . . . . . . . . . . . . . . . . . . .700
ADC_SMPR1 . . . . . . . . . . . . . . . . . . . . . . . . .691
ADC_SMPR2 . . . . . . . . . . . . . . . . . . . . . . . . .691
ADC_SQR1  . . . . . . . . . . . . . . . . . . . . . . . . . .694
ADC_SQR2  . . . . . . . . . . . . . . . . . . . . . . . . . .695
ADC_SQR3  . . . . . . . . . . . . . . . . . . . . . . . . . .696
ADC_SQR4  . . . . . . . . . . . . . . . . . . . . . . . . . .697
ADC_TR1 . . . . . . . . . . . . . . . . . . . . . . . . . . . .692
ADC_TR2 . . . . . . . . . . . . . . . . . . . . . . . . . . . .693
ADC_TR3 . . . . . . . . . . . . . . . . . . . . . . . . . . . .694
ADCx_CCR  . . . . . . . . . . . . . . . . . . . . . . . . . .706
ADCx_CDR  . . . . . . . . . . . . . . . . . . . . . . . . . .710
ADCx_CSR  . . . . . . . . . . . . . . . . . . . . . . . . . .705
AES_CR . . . . . . . . . . . . . . . . . . . . . . . . . . . . .869
AES_DINR . . . . . . . . . . . . . . . . . . . . . . . . . . .873
AES_DOUTR . . . . . . . . . . . . . . . . . . . . . . . . .873
AES_IVR0  . . . . . . . . . . . . . . . . . . . . . . . . . . .876
AES_IVR1  . . . . . . . . . . . . . . . . . . . . . . . . . . .876
AES_IVR2  . . . . . . . . . . . . . . . . . . . . . . . . . . .876
AES_IVR3  . . . . . . . . . . . . . . . . . . . . . . . . . . .877
AES_KEYR0  . . . . . . . . . . . . . . . . . . . . . . . . .874
AES_KEYR1  . . . . . . . . . . . . . . . . . . . . . . . . .875
AES_KEYR2  . . . . . . . . . . . . . . . . . . . . . . . . .875
AES_KEYR3  . . . . . . . . . . . . . . . . . . . . . . . . .875
AES_KEYR4  . . . . . . . . . . . . . . . . . . . . . . . . .877
AES_KEYR5  . . . . . . . . . . . . . . . . . . . . . . . . .877
AES_KEYR6  . . . . . . . . . . . . . . . . . . . . . . . . .878
AES_KEYR7  . . . . . . . . . . . . . . . . . . . . . . . . .878
AES_SR . . . . . . . . . . . . . . . . . . . . . . . . . . . . .872
AES_SUSPxR  . . . . . . . . . . . . . . . . . . . . . . . .878
C
COMP_C1CSR  . . . . . . . . . . . . . . . . . . . . . . .772
COMP_C2CSR . . . . . . . . . . . . . . . . . . . . . . . 772
COMP_C3CSR . . . . . . . . . . . . . . . . . . . . . . . 772
COMP_C4CSR . . . . . . . . . . . . . . . . . . . . . . . 772
COMP_C5CSR . . . . . . . . . . . . . . . . . . . . . . . 772
COMP_C6CSR . . . . . . . . . . . . . . . . . . . . . . . 772
COMP_C7CSR . . . . . . . . . . . . . . . . . . . . . . . 772
CORDIC_CSR . . . . . . . . . . . . . . . . . . . . . . . . 475
CORDIC_RDATA  . . . . . . . . . . . . . . . . . . . . . 478
CORDIC_WDATA . . . . . . . . . . . . . . . . . . . . . 477
CRC_CR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 458
CRC_DR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 457
CRC_IDR  . . . . . . . . . . . . . . . . . . . . . . . . . . . 457
CRC_INIT  . . . . . . . . . . . . . . . . . . . . . . . . . . . 459
CRC_POL . . . . . . . . . . . . . . . . . . . . . . . . . . . 459
CRS_CFGR . . . . . . . . . . . . . . . . . . . . . . . . . . 340
CRS_CR  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 339
CRS_ICR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343
CRS_ISR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
D
DAC_CCR . . . . . . . . . . . . . . . . . . . . . . . . . . . 754
DAC_CR  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 742
DAC_DHR12L1 . . . . . . . . . . . . . . . . . . . . . . . 747
DAC_DHR12L2 . . . . . . . . . . . . . . . . . . . . . . . 749
DAC_DHR12LD  . . . . . . . . . . . . . . . . . . . . . . 750
DAC_DHR12R1  . . . . . . . . . . . . . . . . . . . . . . 747
DAC_DHR12R2  . . . . . . . . . . . . . . . . . . . . . . 748
DAC_DHR12RD  . . . . . . . . . . . . . . . . . . . . . . 750
DAC_DHR8R1  . . . . . . . . . . . . . . . . . . . . . . . 748
DAC_DHR8R2  . . . . . . . . . . . . . . . . . . . . . . . 749
DAC_DHR8RD  . . . . . . . . . . . . . . . . . . . . . . . 751
DAC_DOR1 . . . . . . . . . . . . . . . . . . . . . . . . . . 751
DAC_DOR2 . . . . . . . . . . . . . . . . . . . . . . . . . . 752
DAC_MCR . . . . . . . . . . . . . . . . . . . . . . . . . . . 755
DAC_SHHR . . . . . . . . . . . . . . . . . . . . . . . . . . 757
DAC_SHRR . . . . . . . . . . . . . . . . . . . . . . . . . . 758
DAC_SHSR1 . . . . . . . . . . . . . . . . . . . . . . . . . 756
DAC_SHSR2 . . . . . . . . . . . . . . . . . . . . . . . . . 757
DAC_SR  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 752
DAC_STMODR . . . . . . . . . . . . . . . . . . . . . . . 760
DAC_STR1  . . . . . . . . . . . . . . . . . . . . . . . . . . 759
DAC_STR2  . . . . . . . . . . . . . . . . . . . . . . . . . . 759
DAC_SWTRGR . . . . . . . . . . . . . . . . . . . . . . . 746
DBGMCU_APB1FZR1  . . . . . . . . . . . . . . . . 2109
DBGMCU_APB1FZR2  . . . . . . . . . . . . . . . . 2111
DBGMCU_APB2FZR  . . . . . . . . . . . . . . . . . 2111
DBGMCU_CR . . . . . . . . . . . . . . . . . . . . . . . 2108
DBGMCU_IDCODE  . . . . . . . . . . . . . . . . . . 2095

RM0440 Index
RM0440 Rev 9 2135/2140
DMA_CCRx  . . . . . . . . . . . . . . . . . . . . . . . . . .411
DMA_CMARx . . . . . . . . . . . . . . . . . . . . . . . . .415
DMA_CNDTRx . . . . . . . . . . . . . . . . . . . . . . . .413
DMA_CPARx . . . . . . . . . . . . . . . . . . . . . . . . .414
DMA_IFCR . . . . . . . . . . . . . . . . . . . . . . . . . . .409
DMA_ISR . . . . . . . . . . . . . . . . . . . . . . . . . . . .407
DMAMUX_CFR  . . . . . . . . . . . . . . . . . . . . . . .430
DMAMUX_CSR  . . . . . . . . . . . . . . . . . . . . . . .430
DMAMUX_CxCR  . . . . . . . . . . . . . . . . . . . . . .429
DMAMUX_RGCFR  . . . . . . . . . . . . . . . . . . . .432
DMAMUX_RGSR . . . . . . . . . . . . . . . . . . . . . .432
DMAMUX_RGxCR . . . . . . . . . . . . . . . . . . . . .431
E
EXTI_EMR1 . . . . . . . . . . . . . . . . . . . . . . . . . .446
EXTI_EMR2 . . . . . . . . . . . . . . . . . . . . . . . . . .450
EXTI_FTSR1  . . . . . . . . . . . . . . . . . . . . . . . . .447
EXTI_FTSR2  . . . . . . . . . . . . . . . . . . . . . . . . .451
EXTI_IMR1 . . . . . . . . . . . . . . . . . . . . . . . . . . .446
EXTI_IMR2 . . . . . . . . . . . . . . . . . . . . . . . . . . .449
EXTI_PR1  . . . . . . . . . . . . . . . . . . . . . . . . . . .449
EXTI_PR2  . . . . . . . . . . . . . . . . . . . . . . . . . . .452
EXTI_RTSR1 . . . . . . . . . . . . . . . . . . . . . . . . .446
EXTI_RTSR2 . . . . . . . . . . . . . . . . . . . . . . . . .450
EXTI_SWIER1 . . . . . . . . . . . . . . . . . . . . . . . .448
EXTI_SWIER2 . . . . . . . . . . . . . . . . . . . . . . . .451
F
FDCAN_CCCR  . . . . . . . . . . . . . . . . . . . . . .1987
FDCAN_CKDIV  . . . . . . . . . . . . . . . . . . . . . .2012
FDCAN_CREL . . . . . . . . . . . . . . . . . . . . . . .1984
FDCAN_DBTP . . . . . . . . . . . . . . . . . . . . . . .1984
FDCAN_ECR . . . . . . . . . . . . . . . . . . . . . . . .1992
FDCAN_ENDN . . . . . . . . . . . . . . . . . . . . . . .1984
FDCAN_HPMS  . . . . . . . . . . . . . . . . . . . . . .2003
FDCAN_IE . . . . . . . . . . . . . . . . . . . . . . . . . .1998
FDCAN_ILE . . . . . . . . . . . . . . . . . . . . . . . . .2001
FDCAN_ILS . . . . . . . . . . . . . . . . . . . . . . . . .2000
FDCAN_IR . . . . . . . . . . . . . . . . . . . . . . . . . .1995
FDCAN_NBTP . . . . . . . . . . . . . . . . . . . . . . .1988
FDCAN_PSR . . . . . . . . . . . . . . . . . . . . . . . .1993
FDCAN_RWD  . . . . . . . . . . . . . . . . . . . . . . .1986
FDCAN_RXF0A . . . . . . . . . . . . . . . . . . . . . .2005
FDCAN_RXF0S . . . . . . . . . . . . . . . . . . . . . .2004
FDCAN_RXF1A . . . . . . . . . . . . . . . . . . . . . .2006
FDCAN_RXF1S . . . . . . . . . . . . . . . . . . . . . .2005
FDCAN_RXGFC  . . . . . . . . . . . . . . . . . . . . .2001
FDCAN_TDCR . . . . . . . . . . . . . . . . . . . . . . .1995
FDCAN_TEST  . . . . . . . . . . . . . . . . . . . . . . .1985
FDCAN_TOCC . . . . . . . . . . . . . . . . . . . . . . .1991
FDCAN_TOCV . . . . . . . . . . . . . . . . . . . . . . .1992
FDCAN_TSCC  . . . . . . . . . . . . . . . . . . . . . . 1990
FDCAN_TSCV  . . . . . . . . . . . . . . . . . . . . . . 1990
FDCAN_TXBAR  . . . . . . . . . . . . . . . . . . . . . 2008
FDCAN_TXBC  . . . . . . . . . . . . . . . . . . . . . . 2006
FDCAN_TXBCF  . . . . . . . . . . . . . . . . . . . . . 2010
FDCAN_TXBCIE . . . . . . . . . . . . . . . . . . . . . 2011
FDCAN_TXBCR  . . . . . . . . . . . . . . . . . . . . . 2009
FDCAN_TXBRP  . . . . . . . . . . . . . . . . . . . . . 2007
FDCAN_TXBTIE . . . . . . . . . . . . . . . . . . . . . 2010
FDCAN_TXBTO  . . . . . . . . . . . . . . . . . . . . . 2009
FDCAN_TXEFA  . . . . . . . . . . . . . . . . . . . . . 2012
FDCAN_TXEFS  . . . . . . . . . . . . . . . . . . . . . 2011
FDCAN_TXFQS  . . . . . . . . . . . . . . . . . . . . . 2007
FDCAN_XIDAM . . . . . . . . . . . . . . . . . . . . . . 2003
FLASH_ACR . . . . . . . . . . . . . . . . . 130, 174, 214
FLASH_CR  . . . . . . . . . . . . . . . . . . 134, 178, 218
FLASH_ECCR . . . . . . . . . . . . . . . . 136, 180, 220
FLASH_KEYR . . . . . . . . . . . . . . . . 132, 175, 216
FLASH_OPTKEYR  . . . . . . . . . . . . 132, 176, 216
FLASH_OPTR . . . . . . . . . . . . . . . . 138, 181, 221
FLASH_PCROP1ER . . . . . . . . . . . 141, 183, 223
FLASH_PCROP1SR . . . . . . . . . . . 140, 183, 223
FLASH_PCROP2ER . . . . . . . . . . . . . . . . . . . 143
FLASH_PCROP2SR . . . . . . . . . . . . . . . . . . . 142
FLASH_PDKEYR  . . . . . . . . . . . . . 131, 175, 215
FLASH_SEC1R . . . . . . . . . . . . . . . 145, 185, 225
FLASH_SEC2R . . . . . . . . . . . . . . . . . . . . . . . 145
FLASH_SR  . . . . . . . . . . . . . . . . . . 132, 176, 216
FLASH_WRP1AR . . . . . . . . . . . . . 141, 184, 224
FLASH_WRP1BR . . . . . . . . . . . . . 142, 184, 224
FLASH_WRP2AR . . . . . . . . . . . . . . . . . . . . . 143
FLASH_WRP2BR . . . . . . . . . . . . . . . . . . . . . 144
FMAC_CR . . . . . . . . . . . . . . . . . . . . . . . . . . . 502
FMAC_PARAM . . . . . . . . . . . . . . . . . . . . . . . 501
FMAC_RDATA  . . . . . . . . . . . . . . . . . . . . . . . 505
FMAC_SR . . . . . . . . . . . . . . . . . . . . . . . . . . . 503
FMAC_WDATA . . . . . . . . . . . . . . . . . . . . . . . 504
FMAC_X1BUFCFG . . . . . . . . . . . . . . . . . . . . 499
FMAC_X2BUFCFG . . . . . . . . . . . . . . . . . . . . 499
FMAC_YBUFCFG . . . . . . . . . . . . . . . . . . . . . 500
FMC_BCRx . . . . . . . . . . . . . . . . . . . . . . . . . . 542
FMC_BTRx  . . . . . . . . . . . . . . . . . . . . . . . . . . 544
FMC_BWTRx  . . . . . . . . . . . . . . . . . . . . . . . . 547
FMC_ECCR  . . . . . . . . . . . . . . . . . . . . . . . . . 560
FMC_PATT . . . . . . . . . . . . . . . . . . . . . . . . . . 559
FMC_PCR . . . . . . . . . . . . . . . . . . . . . . . . . . . 555
FMC_PCSCNTR . . . . . . . . . . . . . . . . . . . . . . 549
FMC_PMEM  . . . . . . . . . . . . . . . . . . . . . . . . . 558
FMC_SR  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 557

Index RM0440
2136/2140 RM0440 Rev 9
G
GPIOx_AFRH . . . . . . . . . . . . . . . . . . . . . . . . .360
GPIOx_AFRL . . . . . . . . . . . . . . . . . . . . . . . . .359
GPIOx_BRR . . . . . . . . . . . . . . . . . . . . . . . . . .361
GPIOx_BSRR  . . . . . . . . . . . . . . . . . . . . . . . .357
GPIOx_IDR  . . . . . . . . . . . . . . . . . . . . . . . . . .357
GPIOx_LCKR . . . . . . . . . . . . . . . . . . . . . . . . .358
GPIOx_MODER . . . . . . . . . . . . . . . . . . . . . . .355
GPIOx_ODR  . . . . . . . . . . . . . . . . . . . . . . . . .357
GPIOx_OSPEEDR . . . . . . . . . . . . . . . . . . . . .356
GPIOx_OTYPER  . . . . . . . . . . . . . . . . . . . . . .355
GPIOx_PUPDR  . . . . . . . . . . . . . . . . . . . . . . .356
H
HRTIM_ADC1R  . . . . . . . . . . . . . . . . . . . . . .1107
HRTIM_ADC2R  . . . . . . . . . . . . . . . . . . . . . .1110
HRTIM_ADC3R  . . . . . . . . . . . . . . . . . . . . . .1112
HRTIM_ADC4R  . . . . . . . . . . . . . . . . . . . . . .1114
HRTIM_ADCER . . . . . . . . . . . . . . . . . . . . . .1124
HRTIM_ADCPS1 . . . . . . . . . . . . . . . . . . . . .1128
HRTIM_ADCPS2 . . . . . . . . . . . . . . . . . . . . .1129
HRTIM_ADCUR . . . . . . . . . . . . . . . . . . . . . .1127
HRTIM_BDMADR  . . . . . . . . . . . . . . . . . . . .1123
HRTIM_BDMUPR  . . . . . . . . . . . . . . . . . . . .1121
HRTIM_BDTxUPR . . . . . . . . . . . . . . . . . . . .1122
HRTIM_BMCMPR  . . . . . . . . . . . . . . . . . . . .1102
HRTIM_BMCR . . . . . . . . . . . . . . . . . . . . . . .1098
HRTIM_BMPER . . . . . . . . . . . . . . . . . . . . . .1102
HRTIM_BMTRGR  . . . . . . . . . . . . . . . . . . . .1100
HRTIM_CHPxR  . . . . . . . . . . . . . . . . . . . . . .1055
HRTIM_CMP1CxR . . . . . . . . . . . . . . . . . . . .1021
HRTIM_CMP1xR . . . . . . . . . . . . . . . . . . . . .1019
HRTIM_CMP2xR . . . . . . . . . . . . . . . . . . . . .1021
HRTIM_CMP3xR . . . . . . . . . . . . . . . . . . . . .1023
HRTIM_CMP4xR . . . . . . . . . . . . . . . . . . . . .1024
HRTIM_CNTxR  . . . . . . . . . . . . . . . . . . . . . .1017
HRTIM_CPT1ACR . . . . . . . . . . . . . . . . . . . .1056
HRTIM_CPT1BCR . . . . . . . . . . . . . . . . . . . .1058
HRTIM_CPT1CCR . . . . . . . . . . . . . . . . . . . .1060
HRTIM_CPT1DCR . . . . . . . . . . . . . . . . . . . .1062
HRTIM_CPT1ECR . . . . . . . . . . . . . . . . . . . .1064
HRTIM_CPT1FCR . . . . . . . . . . . . . . . . . . . .1066
HRTIM_CPT1xR  . . . . . . . . . . . . . . . . . . . . .1025
HRTIM_CPT2ACR . . . . . . . . . . . . . . . . . . . .1068
HRTIM_CPT2BCR . . . . . . . . . . . . . . . . . . . .1070
HRTIM_CPT2CCR . . . . . . . . . . . . . . . . . . . .1072
HRTIM_CPT2DCR . . . . . . . . . . . . . . . . . . . .1074
HRTIM_CPT2ECR . . . . . . . . . . . . . . . . . . . .1076
HRTIM_CPT2FCR . . . . . . . . . . . . . . . . . . . .1078
HRTIM_CPT2xR  . . . . . . . . . . . . . . . . . . . . .1026
HRTIM_CR1 . . . . . . . . . . . . . . . . . . . . . . . . .1088
HRTIM_CR2  . . . . . . . . . . . . . . . . . . . . . . . . 1090
HRTIM_DLLCR . . . . . . . . . . . . . . . . . . . . . . 1116
HRTIM_DTxR  . . . . . . . . . . . . . . . . . . . . . . . 1027
HRTIM_EECR1 . . . . . . . . . . . . . . . . . . . . . . 1103
HRTIM_EECR2 . . . . . . . . . . . . . . . . . . . . . . 1105
HRTIM_EECR3 . . . . . . . . . . . . . . . . . . . . . . 1106
HRTIM_EEFxR1  . . . . . . . . . . . . . . . . . . . . . 1040
HRTIM_EEFxR2  . . . . . . . . . . . . . . . . . . . . . 1042
HRTIM_FLTINR1  . . . . . . . . . . . . . . . . . . . . 1117
HRTIM_FLTINR2  . . . . . . . . . . . . . . . . . . . . 1119
HRTIM_FLTINR3  . . . . . . . . . . . . . . . . . . . . 1130
HRTIM_FLTINR4  . . . . . . . . . . . . . . . . . . . . 1132
HRTIM_FLTxR  . . . . . . . . . . . . . . . . . . . . . . 1083
HRTIM_ICR . . . . . . . . . . . . . . . . . . . . . . . . . 1093
HRTIM_IER . . . . . . . . . . . . . . . . . . . . . . . . . 1094
HRTIM_ISR . . . . . . . . . . . . . . . . . . . . . . . . . 1091
HRTIM_MCMP1R . . . . . . . . . . . . . . . . . . . . 1003
HRTIM_MCMP2R . . . . . . . . . . . . . . . . . . . . 1004
HRTIM_MCMP3R . . . . . . . . . . . . . . . . . . . . 1004
HRTIM_MCMP4R . . . . . . . . . . . . . . . . . . . . 1005
HRTIM_MCNTR  . . . . . . . . . . . . . . . . . . . . . 1002
HRTIM_MCR . . . . . . . . . . . . . . . . . . . . . . . . . 995
HRTIM_MDIER . . . . . . . . . . . . . . . . . . . . . . 1000
HRTIM_MICR  . . . . . . . . . . . . . . . . . . . . . . . . 999
HRTIM_MISR  . . . . . . . . . . . . . . . . . . . . . . . . 998
HRTIM_MPER . . . . . . . . . . . . . . . . . . . . . . . 1002
HRTIM_MREP . . . . . . . . . . . . . . . . . . . . . . . 1003
HRTIM_ODISR  . . . . . . . . . . . . . . . . . . . . . . 1096
HRTIM_ODSR . . . . . . . . . . . . . . . . . . . . . . . 1097
HRTIM_OENR . . . . . . . . . . . . . . . . . . . . . . . 1095
HRTIM_OUTxR . . . . . . . . . . . . . . . . . . . . . . 1080
HRTIM_PERxR . . . . . . . . . . . . . . . . . . . . . . 1017
HRTIM_REPxR . . . . . . . . . . . . . . . . . . . . . . 1019
HRTIM_RSTAR . . . . . . . . . . . . . . . . . . . . . . 1043
HRTIM_RSTBR . . . . . . . . . . . . . . . . . . . . . . 1045
HRTIM_RSTCR . . . . . . . . . . . . . . . . . . . . . . 1047
HRTIM_RSTDR . . . . . . . . . . . . . . . . . . . . . . 1049
HRTIM_RSTER . . . . . . . . . . . . . . . . . . . . . . 1051
HRTIM_RSTFR . . . . . . . . . . . . . . . . . . . . . . 1053
HRTIM_RSTx1R . . . . . . . . . . . . . . . . . . . . . 1032
HRTIM_RSTx2R . . . . . . . . . . . . . . . . . . . . . 1037
HRTIM_SETx1R  . . . . . . . . . . . . . . . . . . . . . 1029
HRTIM_SETx2R  . . . . . . . . . . . . . . . . . . . . . 1034
HRTIM_TIMxCR  . . . . . . . . . . . . . . . . . . . . . 1006
HRTIM_TIMxCR2  . . . . . . . . . . . . . . . . . . . . 1084
HRTIM_TIMxDIER  . . . . . . . . . . . . . . . . . . . 1013
HRTIM_TIMxEEFR3 . . . . . . . . . . . . . . . . . . 1087
HRTIM_TIMxICR . . . . . . . . . . . . . . . . . . . . . 1012
HRTIM_TIMxISR . . . . . . . . . . . . . . . . . . . . . 1010

RM0440 Index
RM0440 Rev 9 2137/2140
I
I2C_CR1  . . . . . . . . . . . . . . . . . . . . . . . . . . .1675
I2C_CR2  . . . . . . . . . . . . . . . . . . . . . . . . . . .1677
I2C_ICR . . . . . . . . . . . . . . . . . . . . . . . . . . . .1685
I2C_ISR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .1683
I2C_OAR1  . . . . . . . . . . . . . . . . . . . . . . . . . .1679
I2C_OAR2  . . . . . . . . . . . . . . . . . . . . . . . . . .1680
I2C_PECR  . . . . . . . . . . . . . . . . . . . . . . . . . .1686
I2C_RXDR . . . . . . . . . . . . . . . . . . . . . . . . . .1686
I2C_TIMEOUTR . . . . . . . . . . . . . . . . . . . . . .1682
I2C_TIMINGR  . . . . . . . . . . . . . . . . . . . . . . .1681
I2C_TXDR  . . . . . . . . . . . . . . . . . . . . . . . . . .1687
IWDG_KR  . . . . . . . . . . . . . . . . . . . . . . . . . .1559
IWDG_PR  . . . . . . . . . . . . . . . . . . . . . . . . . .1560
IWDG_RLR  . . . . . . . . . . . . . . . . . . . . . . . . .1561
IWDG_SR  . . . . . . . . . . . . . . . . . . . . . . . . . .1562
IWDG_WINR  . . . . . . . . . . . . . . . . . . . . . . . .1563
L
LPTIM_ARR . . . . . . . . . . . . . . . . . . . . . . . . .1551
LPTIM_CFGR  . . . . . . . . . . . . . . . . . . . . . . .1546
LPTIM_CMP . . . . . . . . . . . . . . . . . . . . . . . . .1551
LPTIM_CNT . . . . . . . . . . . . . . . . . . . . . . . . .1552
LPTIM_CR . . . . . . . . . . . . . . . . . . . . . . . . . .1549
LPTIM_ICR  . . . . . . . . . . . . . . . . . . . . . . . . .1545
LPTIM_IER . . . . . . . . . . . . . . . . . . . . . . . . . .1545
LPTIM_ISR . . . . . . . . . . . . . . . . . . . . . . . . . .1544
LPTIM1_OR . . . . . . . . . . . . . . . . . . . . . . . . .1552
LPUART_BRR . . . . . . . . . . . . . . . . . . . . . . .1815
LPUART_CR1  . . . . . . . . . . . . . . . . . .1804, 1807
LPUART_CR2  . . . . . . . . . . . . . . . . . . . . . . .1810
LPUART_CR3  . . . . . . . . . . . . . . . . . . . . . . .1812
LPUART_ICR . . . . . . . . . . . . . . . . . . . . . . . .1823
LPUART_ISR . . . . . . . . . . . . . . . . . . .1816, 1820
LPUART_PRESC . . . . . . . . . . . . . . . . . . . . .1825
LPUART_RDR . . . . . . . . . . . . . . . . . . . . . . .1824
LPUART_RQR . . . . . . . . . . . . . . . . . . . . . . .1815
LPUART_TDR  . . . . . . . . . . . . . . . . . . . . . . .1824
O
OPAMP1_CSR . . . . . . . . . . . . . . . . . . . . . . . .788
OPAMP2_CSR . . . . . . . . . . . . . . . . . . . . . . . .791
OPAMP3_CSR . . . . . . . . . . . . . . . . . . . . . . . .794
OPAMP4_CSR . . . . . . . . . . . . . . . . . . . . . . . .797
OPAMP5_CSR . . . . . . . . . . . . . . . . . . . . . . . .800
OPAMP6_CSR . . . . . . . . . . . . . . . . . . . . . . . .803
OPAMPx_TCMR  . 806, 808, 810, 812, 814, 816
P
PWR_CR1 . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
PWR_CR2 . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
PWR_CR3 . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
PWR_CR4 . . . . . . . . . . . . . . . . . . . . . . . . . . . 256
PWR_CR5 . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
PWR_PDCRA . . . . . . . . . . . . . . . . . . . . . . . . 260
PWR_PDCRB . . . . . . . . . . . . . . . . . . . . . . . . 261
PWR_PDCRC . . . . . . . . . . . . . . . . . . . . . . . . 262
PWR_PDCRD . . . . . . . . . . . . . . . . . . . . . . . . 263
PWR_PDCRE . . . . . . . . . . . . . . . . . . . . . . . . 264
PWR_PDCRF  . . . . . . . . . . . . . . . . . . . . . . . . 265
PWR_PDCRG . . . . . . . . . . . . . . . . . . . . . . . . 266
PWR_PUCRA . . . . . . . . . . . . . . . . . . . . . . . . 260
PWR_PUCRB . . . . . . . . . . . . . . . . . . . . . . . . 261
PWR_PUCRC . . . . . . . . . . . . . . . . . . . . . . . . 262
PWR_PUCRD . . . . . . . . . . . . . . . . . . . . . . . . 263
PWR_PUCRE . . . . . . . . . . . . . . . . . . . . . . . . 264
PWR_PUCRF  . . . . . . . . . . . . . . . . . . . . . . . . 265
PWR_PUCRG . . . . . . . . . . . . . . . . . . . . . . . . 266
PWR_SCR  . . . . . . . . . . . . . . . . . . . . . . . . . . 259
PWR_SR1 . . . . . . . . . . . . . . . . . . . . . . . . . . . 257
PWR_SR2 . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
Q
QUADSPI_ABR . . . . . . . . . . . . . . . . . . . . . . . 586
QUADSPI_AR . . . . . . . . . . . . . . . . . . . . . . . . 586
QUADSPI_CCR  . . . . . . . . . . . . . . . . . . . . . . 584
QUADSPI_CR . . . . . . . . . . . . . . . . . . . . . . . . 578
QUADSPI_DCR  . . . . . . . . . . . . . . . . . . . . . . 581
QUADSPI_DLR . . . . . . . . . . . . . . . . . . . . . . . 583
QUADSPI_DR . . . . . . . . . . . . . . . . . . . . . . . . 587
QUADSPI_FCR . . . . . . . . . . . . . . . . . . . . . . . 583
QUADSPI_LPTR . . . . . . . . . . . . . . . . . . . . . . 589
QUADSPI_PIR  . . . . . . . . . . . . . . . . . . . . . . . 588
QUADSPI_PSMAR . . . . . . . . . . . . . . . . . . . . 588
QUADSPI_PSMKR . . . . . . . . . . . . . . . . . . . . 587
QUADSPI_SR . . . . . . . . . . . . . . . . . . . . . . . . 582
R
RCC_AHB1ENR  . . . . . . . . . . . . . . . . . . . . . . 305
RCC_AHB1RSTR . . . . . . . . . . . . . . . . . . . . . 297
RCC_AHB1SMENR  . . . . . . . . . . . . . . . . . . . 313
RCC_AHB2ENR  . . . . . . . . . . . . . . . . . . . . . . 306
RCC_AHB2RSTR . . . . . . . . . . . . . . . . . . . . . 298
RCC_AHB2SMENR  . . . . . . . . . . . . . . . . . . . 315
RCC_AHB3ENR  . . . . . . . . . . . . . . . . . . . . . . 308
RCC_AHB3RSTR . . . . . . . . . . . . . . . . . . . . . 300
RCC_AHB3SMENR  . . . . . . . . . . . . . . . . . . . 317
RCC_APB1ENR1  . . . . . . . . . . . . . . . . . . . . . 309

Index RM0440
2138/2140 RM0440 Rev 9
RCC_APB1ENR2 . . . . . . . . . . . . . . . . . . . . . .311
RCC_APB1RSTR1  . . . . . . . . . . . . . . . . . . . .301
RCC_APB1RSTR2  . . . . . . . . . . . . . . . . . . . .303
RCC_APB1SMENR1 . . . . . . . . . . . . . . . . . . .317
RCC_APB1SMENR2 . . . . . . . . . . . . . . . . . . .320
RCC_APB2ENR . . . . . . . . . . . . . . . . . . . . . . .312
RCC_APB2RSTR  . . . . . . . . . . . . . . . . . . . . .303
RCC_APB2SMENR . . . . . . . . . . . . . . . . . . . .321
RCC_BDCR . . . . . . . . . . . . . . . . . . . . . . . . . .325
RCC_CCIPR  . . . . . . . . . . . . . . . . . . . . . . . . .322
RCC_CCIPR2  . . . . . . . . . . . . . . . . . . . . . . . .329
RCC_CFGR . . . . . . . . . . . . . . . . . . . . . . . . . .289
RCC_CICR . . . . . . . . . . . . . . . . . . . . . . . . . . .296
RCC_CIER . . . . . . . . . . . . . . . . . . . . . . . . . . .294
RCC_CIFR . . . . . . . . . . . . . . . . . . . . . . . . . . .295
RCC_CR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .287
RCC_CRRCR  . . . . . . . . . . . . . . . . . . . . . . . .328
RCC_CSR  . . . . . . . . . . . . . . . . . . . . . . . . . . .327
RCC_ICSCR  . . . . . . . . . . . . . . . . . . . . . . . . .288
RCC_PLLCFGR . . . . . . . . . . . . . . . . . . . . . . .291
RNG_CR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .829
RNG_DR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .830
RNG_SR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .829
RTC_ALRMAR . . . . . . . . . . . . . . . . . . . . . . .1601
RTC_ALRMASSR  . . . . . . . . . . . . . . . . . . . .1602
RTC_ALRMBR . . . . . . . . . . . . . . . . . . . . . . .1603
RTC_ALRMBSSR  . . . . . . . . . . . . . . . . . . . .1604
RTC_CALR  . . . . . . . . . . . . . . . . . . . . . . . . .1597
RTC_CR . . . . . . . . . . . . . . . . . . . . . . . . . . . .1593
RTC_DR . . . . . . . . . . . . . . . . . . . . . . . . . . . .1589
RTC_ICSR . . . . . . . . . . . . . . . . . . . . . . . . . .1590
RTC_MISR . . . . . . . . . . . . . . . . . . . . . . . . . .1605
RTC_PRER  . . . . . . . . . . . . . . . . . . . . . . . . .1592
RTC_SCR  . . . . . . . . . . . . . . . . . . . . . . . . . .1606
RTC_SHIFTR . . . . . . . . . . . . . . . . . . . . . . . .1598
RTC_SR . . . . . . . . . . . . . . . . . . . . . . . . . . . .1604
RTC_SSR  . . . . . . . . . . . . . . . . . . . . . . . . . .1590
RTC_TR . . . . . . . . . . . . . . . . . . . . . . . . . . . .1588
RTC_TSDR  . . . . . . . . . . . . . . . . . . . . . . . . .1599
RTC_TSSSR  . . . . . . . . . . . . . . . . . . . . . . . .1600
RTC_TSTR  . . . . . . . . . . . . . . . . . . . . . . . . .1599
RTC_WPR . . . . . . . . . . . . . . . . . . . . . . . . . .1596
RTC_WUTR . . . . . . . . . . . . . . . . . . . . . . . . .1593
S
SAI_ACLRFR . . . . . . . . . . . . . . . . . . . . . . . .1933
SAI_ACR1  . . . . . . . . . . . . . . . . . . . . . . . . . .1923
SAI_ACR2  . . . . . . . . . . . . . . . . . . . . . . . . . .1925
SAI_ADR  . . . . . . . . . . . . . . . . . . . . . . . . . . .1934
SAI_AFRCR . . . . . . . . . . . . . . . . . . . . . . . . .1927
SAI_AIM . . . . . . . . . . . . . . . . . . . . . . . . . . . .1929
SAI_ASLOTR  . . . . . . . . . . . . . . . . . . . . . . . 1928
SAI_ASR . . . . . . . . . . . . . . . . . . . . . . . . . . . 1931
SAI_BCLRFR  . . . . . . . . . . . . . . . . . . . . . . . 1944
SAI_BCR1 . . . . . . . . . . . . . . . . . . . . . . . . . . 1934
SAI_BCR2 . . . . . . . . . . . . . . . . . . . . . . . . . . 1937
SAI_BDR . . . . . . . . . . . . . . . . . . . . . . . . . . . 1945
SAI_BFRCR  . . . . . . . . . . . . . . . . . . . . . . . . 1939
SAI_BIM  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1941
SAI_BSLOTR  . . . . . . . . . . . . . . . . . . . . . . . 1940
SAI_BSR . . . . . . . . . . . . . . . . . . . . . . . . . . . 1942
SAI_PDMCR . . . . . . . . . . . . . . . . . . . . . . . . 1946
SAI_PDMDLY  . . . . . . . . . . . . . . . . . . . . . . . 1947
SPIx_CR1  . . . . . . . . . . . . . . . . . . . . . . . . . . 1874
SPIx_CR2  . . . . . . . . . . . . . . . . . . . . . . . . . . 1876
SPIx_CRCPR  . . . . . . . . . . . . . . . . . . . . . . . 1880
SPIx_DR  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1880
SPIx_I2SCFGR . . . . . . . . . . . . . . . . . . . . . . 1881
SPIx_I2SPR  . . . . . . . . . . . . . . . . . . . . . . . . 1883
SPIx_RXCRCR . . . . . . . . . . . . . . . . . . . . . . 1880
SPIx_SR  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1878
SPIx_TXCRCR  . . . . . . . . . . . . . . . . . . . . . . 1881
SYSCFG_CFGR1 . . . . . . . . . . . . . . . . . . . . . 365
SYSCFG_CFGR2 . . . . . . . . . . . . . . . . . . . . . 373
SYSCFG_EXTICR1  . . . . . . . . . . . . . . . . . . . 367
SYSCFG_EXTICR2  . . . . . . . . . . . . . . . . . . . 368
SYSCFG_EXTICR3  . . . . . . . . . . . . . . . . . . . 369
SYSCFG_EXTICR4  . . . . . . . . . . . . . . . . . . . 371
SYSCFG_MEMRMP . . . . . . . . . . . . . . . . . . . 364
SYSCFG_SCSR  . . . . . . . . . . . . . . . . . . . . . . 372
SYSCFG_SKR  . . . . . . . . . . . . . . . . . . . . . . . 374
SYSCFG_SWPR . . . . . . . . . . . . . . . . . . . . . . 374
T
TAMP_BKPxR . . . . . . . . . . . . . . . . . . . . . . . 1623
TAMP_CR1 . . . . . . . . . . . . . . . . . . . . . . . . . 1616
TAMP_CR2 . . . . . . . . . . . . . . . . . . . . . . . . . 1617
TAMP_FLTCR . . . . . . . . . . . . . . . . . . . . . . . 1618
TAMP_IER  . . . . . . . . . . . . . . . . . . . . . . . . . 1619
TAMP_MISR . . . . . . . . . . . . . . . . . . . . . . . . 1621
TAMP_SCR . . . . . . . . . . . . . . . . . . . . . . . . . 1622
TAMP_SR . . . . . . . . . . . . . . . . . . . . . . . . . . 1620
TIM15_AF1  . . . . . . . . . . . . . . . . . . . . . . . . . 1477
TIM15_AF2  . . . . . . . . . . . . . . . . . . . . . . . . . 1479
TIM15_ARR . . . . . . . . . . . . . . . . . . . . . . . . . 1470
TIM15_BDTR  . . . . . . . . . . . . . . . . . . . . . . . 1472
TIM15_CCER  . . . . . . . . . . . . . . . . . . . . . . . 1466
TIM15_CCMR1 . . . . . . . . . . . . . . . . . 1462 -1463
TIM15_CCR1  . . . . . . . . . . . . . . . . . . . . . . . 1471
TIM15_CCR2  . . . . . . . . . . . . . . . . . . . . . . . 1472
TIM15_CNT . . . . . . . . . . . . . . . . . . . . . . . . . 1469
TIM15_CR1 . . . . . . . . . . . . . . . . . . . . . . . . . 1453

RM0440 Index
RM0440 Rev 9 2139/2140
TIM15_CR2  . . . . . . . . . . . . . . . . . . . . . . . . .1454
TIM15_DCR . . . . . . . . . . . . . . . . . . . . . . . . .1480
TIM15_DIER  . . . . . . . . . . . . . . . . . . . . . . . .1458
TIM15_DMAR  . . . . . . . . . . . . . . . . . . . . . . .1480
TIM15_DTR2  . . . . . . . . . . . . . . . . . . . . . . . .1475
TIM15_EGR . . . . . . . . . . . . . . . . . . . . . . . . .1461
TIM15_PSC  . . . . . . . . . . . . . . . . . . . . . . . . .1469
TIM15_RCR . . . . . . . . . . . . . . . . . . . . . . . . .1470
TIM15_SMCR  . . . . . . . . . . . . . . . . . . . . . . .1456
TIM15_SR  . . . . . . . . . . . . . . . . . . . . . . . . . .1459
TIM15_TISEL . . . . . . . . . . . . . . . . . . . . . . . .1476
TIMx_AF1 . . . . . . . . . . . . . . . . 1277 , 1398, 1502
TIMx_AF2 . . . . . . . . . . . . . . . . 1280 , 1399, 1505
TIMx_ARR  . . . . . . . . . . 1263 , 1388, 1496, 1528
TIMx_BDTR . . . . . . . . . . . . . . . . . . . .1267, 1498
TIMx_CCER . . . . . . . . . . . . . . 1258 , 1385, 1492
TIMx_CCMR1  . .1249, 1251, 1377, 1379, 1489-
1490
TIMx_CCMR2  . . . . . . . . 1254 -1255, 1381-1382
TIMx_CCMR3  . . . . . . . . . . . . . . . . . . . . . . .1273
TIMx_CCR1 . . . . . . . . . . 1264, 1389-1390, 1497
TIMx_CCR2 . . . . . . . . . . . . . . . 1264, 1390-1391
TIMx_CCR3 . . . . . . . . . . . . . . . 1265, 1392-1393
TIMx_CCR4 . . . . . . . . . . . . . . . 1266, 1394-1395
TIMx_CCR5 . . . . . . . . . . . . . . . . . . . . . . . . .1271
TIMx_CCR6 . . . . . . . . . . . . . . . . . . . . . . . . .1272
TIMx_CNT  . . . . . .1262, 1386-1387, 1495, 1527
TIMx_CR1  . . . . . . . . . . 1235 , 1366, 1484, 1524
TIMx_CR2  . . . . . . . . . . 1236 , 1367, 1485, 1526
TIMx_DCR . . . . . . . . . . . . . . . 1282 , 1400, 1506
TIMx_DIER . . . . . . . . . . 1244 , 1373, 1486, 1526
TIMx_DMAR . . . . . . . . . . . . . . 1283 , 1401, 1506
TIMx_DTR2  . . . . . . . . . . . . . . . . . . . .1274, 1501
TIMx_ECR  . . . . . . . . . . . . . . . . . . . . .1275, 1396
TIMx_EGR . . . . . . . . . . 1248 , 1376, 1488, 1527
TIMx_OR1  . . . . . . . . . . . . . . . . . . . . . . . . . .1505
TIMx_PSC  . . . . . . . . . . 1262 , 1387, 1495, 1528
TIMx_RCR . . . . . . . . . . . . . . . . . . . . .1263, 1496
TIMx_SMCR . . . . . . . . . . . . . . . . . . . .1240, 1369
TIMx_SR  . . . . . . . . . . . 1245 , 1374, 1487, 1527
TIMx_TISEL . . . . . . . . . . . . . . 1276 , 1397, 1502
U
UCPD_CFGR1 . . . . . . . . . . . . . . . . . . . . . . .2071
UCPD_CFGR2 . . . . . . . . . . . . . . . . . . . . . . .2073
UCPD_CR  . . . . . . . . . . . . . . . . . . . . . . . . . .2073
UCPD_ICR . . . . . . . . . . . . . . . . . . . . . . . . . .2080
UCPD_IMR  . . . . . . . . . . . . . . . . . . . . . . . . .2076
UCPD_RX_ORDEXTR1  . . . . . . . . . . . . . . .2084
UCPD_RX_ORDEXTR2  . . . . . . . . . . . . . . .2085
UCPD_RX_ORDSETR  . . . . . . . . . . . . . . . .2082
UCPD_RX_PAYSZR . . . . . . . . . . . . . . . . . . 2083
UCPD_RXDR  . . . . . . . . . . . . . . . . . . . . . . . 2084
UCPD_SR . . . . . . . . . . . . . . . . . . . . . . . . . . 2077
UCPD_TX_ORDSETR  . . . . . . . . . . . . . . . . 2081
UCPD_TX_PAYSZR . . . . . . . . . . . . . . . . . . 2081
UCPD_TXDR  . . . . . . . . . . . . . . . . . . . . . . . 2082
USART_BRR . . . . . . . . . . . . . . . . . . . . . . . . 1755
USART_CR1 . . . . . . . . . . . . . . . . . . . 1740, 1743
USART_CR2 . . . . . . . . . . . . . . . . . . . . . . . . 1747
USART_CR3 . . . . . . . . . . . . . . . . . . . . . . . . 1751
USART_GTPR  . . . . . . . . . . . . . . . . . . . . . . 1755
USART_ICR  . . . . . . . . . . . . . . . . . . . . . . . . 1769
USART_ISR  . . . . . . . . . . . . . . . . . . . 1758, 1764
USART_PRESC  . . . . . . . . . . . . . . . . . . . . . 1772
USART_RDR  . . . . . . . . . . . . . . . . . . . . . . . 1771
USART_RQR  . . . . . . . . . . . . . . . . . . . . . . . 1757
USART_RTOR  . . . . . . . . . . . . . . . . . . . . . . 1756
USART_TDR . . . . . . . . . . . . . . . . . . . . . . . . 1771
USB_ADDRn_RX  . . . . . . . . . . . . . . . . . . . . 2046
USB_ADDRn_TX  . . . . . . . . . . . . . . . . . . . . 2045
USB_BCDR . . . . . . . . . . . . . . . . . . . . . . . . . 2039
USB_BTABLE . . . . . . . . . . . . . . . . . . . . . . . 2038
USB_CNTR . . . . . . . . . . . . . . . . . . . . . . . . . 2032
USB_COUNTn_RX . . . . . . . . . . . . . . . . . . . 2046
USB_COUNTn_TX  . . . . . . . . . . . . . . . . . . . 2045
USB_DADDR  . . . . . . . . . . . . . . . . . . . . . . . 2037
USB_EPnR  . . . . . . . . . . . . . . . . . . . . . . . . . 2040
USB_FNR  . . . . . . . . . . . . . . . . . . . . . . . . . . 2037
USB_ISTR . . . . . . . . . . . . . . . . . . . . . . . . . . 2034
USB_LPMCSR  . . . . . . . . . . . . . . . . . . . . . . 2038
V
VREFBUF_CCR  . . . . . . . . . . . . . . . . . . . . . . 767
VREFBUF_CSR  . . . . . . . . . . . . . . . . . . . . . . 766
W
WWDG_CFR . . . . . . . . . . . . . . . . . . . . . . . . 1569
WWDG_CR . . . . . . . . . . . . . . . . . . . . . . . . . 1569
WWDG_SR . . . . . . . . . . . . . . . . . . . . . . . . . 1570

RM0440
2140/2140 RM0440 Rev 9
IMPORTANT NOTICE – READ CAREFULLY
STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and
improvements to ST products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on
ST products before placing orders. ST products are sold pursuant to ST’s terms and conditions of sale in place at the time of order
acknowledgment.
Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or
the design of purchasers’ products.
No license, express or implied, to any intellectual property right is granted by ST herein.
Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.
ST and the ST logo are trademarks of ST. For additional information about ST trademarks, refer to www.st.com/trademarks. All other
product or service names are the property of their respective owners.
Information in this document supersedes and replaces information previously supplied in any prior versions of this document.
© 2025 STMicroelectronics – All rights reserved
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 2: Architectural Diagram](../figures/figure_2.md)
* [Figure 4: Architectural Diagram](../figures/figure_4.md)
* [Figure 7: Architectural Diagram](../figures/figure_7.md)
* [Figure 10: Architectural Diagram](../figures/figure_10.md)
* [Figure 17: Architectural Diagram](../figures/figure_17.md)
* [Figure 83: Architectural Diagram](../figures/figure_83.md)
* [Figure 86: Architectural Diagram](../figures/figure_86.md)
* [Figure 151: Architectural Diagram](../figures/figure_151.md)
* [Figure 156: Architectural Diagram](../figures/figure_156.md)
* [Figure 168: Architectural Diagram](../figures/figure_168.md)
* [Figure 171: Architectural Diagram](../figures/figure_171.md)
* [Figure 244: Architectural Diagram](../figures/figure_244.md)
* [Figure 245: Architectural Diagram](../figures/figure_245.md)
* [Figure 379: Architectural Diagram](../figures/figure_379.md)
* [Figure 385: Architectural Diagram](../figures/figure_385.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 1: Configuration Matrix](../tables/table_1.md)
* [Table 2: Configuration Matrix](../tables/table_2.md)
* [Table 3: Configuration Matrix](../tables/table_3.md)
* [Table 4: Configuration Matrix](../tables/table_4.md)
* [Table 5: Configuration Matrix](../tables/table_5.md)
* [Table 7: Configuration Matrix](../tables/table_7.md)
* [Table 8: Configuration Matrix](../tables/table_8.md)
* [Table 9: Configuration Matrix](../tables/table_9.md)
* [Table 11: Configuration Matrix](../tables/table_11.md)
* [Table 12: Configuration Matrix](../tables/table_12.md)
* [Table 18: Configuration Matrix](../tables/table_18.md)
* [Table 19: Configuration Matrix](../tables/table_19.md)
* [Table 21: Configuration Matrix](../tables/table_21.md)
* [Table 22: Configuration Matrix](../tables/table_22.md)
* [Table 28: Configuration Matrix](../tables/table_28.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)