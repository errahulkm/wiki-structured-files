# Chapter 55: Revision history

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 55: Revision history.
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 2155 - 2187
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 2155/2187
RM0438 Revision history
2177
55 Revision history
[Table 469](../tables/table_469.md). Document revision history
Date Revision Changes
08-Oct-2018 1 Initial release.
12-Apr-2019 2
Added:
– Section 6.5.7: Flash registers privileged and unprivileged modes
– Section 8.3.4: Upper voltage threshold monitoring
– Section 8.3.5: Temperature threshold monitoring
– Section 20.3: OCTOSPI implementation
– Section 42.3.3: TAMP register write protection
– Section 43.4.2: I2C pins and internal signals
– Section 35.9.12: I2C autonomous mode control register (I2C_AUTOCR)
– Section 52.9.14: I2C version register (I2C_VERR)
– Section 52.9.15: I2C identification register (I2C_IPIDR)
– Section 52.9.16: I2C size identification register (I2C_SIDR)
– Section 48.8: SDMMC interrupts
Updated:
– [Table 4](../tables/table_4.md): STM32L552xx and STM32L562xx memory map and peripheral register
boundary addresses
– [Table 7](../tables/table_7.md): Boot modes when TrustZone is enabled (TZEN=1)
– [Table 8](../tables/table_8.md): Boot space versus RDP protection
– Major changes to all sections (including figures, tables and registers) of Section 5:
Global TrustZone® controller (GTZC)
– Section 6.1: Introduction
– Section 6.2: FLASH main features
– [Table 31](../tables/table_31.md): Flash module - 512 KB dual bank organization (64 bits read width)
– [Table 33](../tables/table_33.md): Flash module - 512 KB single bank organization (128 bits read width)
– Section 6.3.5: Flash program and erase operations
– Section 6.3.8: Flash errors flags
– Section 6.4.2: Option bytes programming
– Section 6.5.1: TrustZone security protection
– Section 6.5.2: Secure watermark-based area protection
– [Table 37](../tables/table_37.md): Secure watermark-based area
– [Table 22](../tables/table_22.md): Secure hide protection
– Section 5.5.4: Secure proprietary code readout protection (PCROP)
– Section 6.5.4: Secure block-based area (SECBB) protection
– Section 6.5.6: Flash security attribute state
– Section 6.7: FLASH memory protection
– Section 6.7.1: Write protection (WRP)
– Major updates on content and tables of subsections of Section 6.7.2: Readout
protection (RDP)

Revision history RM0438
2156/2187 RM0438 Rev 8
12-Apr-2019 2
(continued)
Updated:
– [Table 43](../tables/table_43.md): Flash memory readout protection status (TZEN=0)
– [Table 44](../tables/table_44.md): Access status versus protection level and execution modes when TZEN=0
– [Table 45](../tables/table_45.md): Flash memory readout protection status (TZEN=1)
– [Table 46](../tables/table_46.md): Access status versus protection level and execution modes when TZEN=1
– Section 6.9.8: Flash status register (FLASH_SECSR)
– Section 6.9.12: Flash option register (FLASH_OPTR)
– Section 7.4.2: ICACHE reset and clocks
– Section 7.4.5: ICACHE enable
– Section 7.4.7: Address remapping
– [Figure 20](../figures/figure_20.md): ICACHE remapping address mechanism
– [Table 61](../tables/table_61.md): ICACHE register map and reset values
– Section 8: Power control (PWR)
– Section 8.2.5: Dynamic voltage scaling management
– [Table 67](../tables/table_67.md): Functionalities depending on the working mode
– Section 8.5: PWR TrustZone security
– Section 11.6.6: GPIO port output data register (GPIOx_ODR) (x = A to H)
– Section 11.6.12: GPIO secure configuration register (GPIOx_SECCFGR) (x = A to
H)
– [Table 91](../tables/table_91.md): GPIO register map and reset values
– Section 12.2: SYSCFG TrustZone security and privilege
– Section [Table 93](../tables/table_93.md).: BOOSTEN and ANASWVDD set/reset
– Section 14.4.5: DMA channels
– Section 14.6.3: DMA channel x configuration register (DMA_CCRx)
– [Table 101](../tables/table_101.md): DMAMUX instantiation
– Section 15.4.6: DMAMUX request line multiplexer
– Section 15.6.4: DMAMUX request generator channel x configuration register
(DMAMUX_RGxCR)
– Section 15.6.5: DMAMUX request generator interrupt status register
(DMAMUX_RGSR)
– [Table 109](../tables/table_109.md): STM32L552xx and STM32L562xx vector table
– All registers and tables of Section 18.4: CRC registers
– [Table 119](../tables/table_119.md): CRC register map and reset values
– Section 20.1: OCTOSPI introduction
– Section 20.4.1: OCTOSPI block diagram including all figures
– Section 20.4.3: OCTOSPI interface to memory modes
– Section 20.4.5: OCTOSPI regular-command protocol signal interface
– Section 20.4.7: Specific features
– Section 20.4.8: OCTOSPI operating mode introduction
– Section 20.4.10: OCTOSPI automatic status-polling mode
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

RM0438 Rev 8 2157/2187
RM0438 Revision history
2177
12-Apr-2019 2
(continued)
Updated:
– Section 20.4.12: OCTOSPI configuration introduction
– Section 20.4.14: OCTOSPI device configuration
– Section 20.4.15: OCTOSPI regular-command mode configuration
– Section 20.4.17: OCTOSPI error management
– Section 20.4.18: OCTOSPI BUSY and ABORT
– Section 20.7.1: OCTOSPI control register (OCTOSPI_CR)
– Section 20.7.2: OCTOSPI device configuration register 1 (OCTOSPI_DCR1)
– Section 20.7.5: OCTOSPI device configuration register 4 (OCTOSPI_DCR4)
– Section 21.2: ADC main features
– Section 21.4.7: Single-ended and differential input channels
– Section 21.4.9: ADC on-off control (ADEN, ADDIS, ADRDY)
– Section 21.4.12: Channel-wise programmable sampling time (SMPR1, SMPR2)
– Section 21.4.16: ADC timing
– [Table 171](../tables/table_171.md): TSAR timings depending on resolution
– [Table 175](../tables/table_175.md): Analog watchdog 2 and 3 comparison
– [Table 174](../tables/table_174.md): Analog watchdog 1 comparison
– [Figure 136](../figures/figure_136.md): ADCy_AWDx_OUT signal generation (on all injected channels)
– Section 21.4.31: Dual ADC modes
– [Figure 147](../figures/figure_147.md): Interleaved mode on 1 channel in continuous conversion mode: dual
ADC mode
– [Figure 148](../figures/figure_148.md): Interleaved mode on 1 channel in single conversion mode: dual ADC
mode
– Section 21.4.34: Monitoring the internal voltage reference
– Section 22.4.13: Dual DAC channel conversion modes (if dual channels are
available)
– Section 22.7.17: DAC channel1 sample and hold sample time register
(DAC_SHSR1)
– Section 22.7.18: DAC channel2 sample and hold sample time register
(DAC_SHSR2)
– Section 24.6.1: Comparator 1 control and status register (COMP1_CSR)
– Section 24.6.2: Comparator 2 control and status register (COMP2_CSR)
– [Table 206](../tables/table_206.md): DFSDM1 implementation
– Major changes to all sections (including figures, tables and registers) of Section 28:
True random number generator (RNG)
– Section 29.4.5: AES decryption round key preparation
– Section 29.4.8: AES basic chaining modes (ECB, CBC)
– Section 29.4.10: AES Galois/counter mode (GCM)
– [Figure 215](../figures/figure_215.md): Message construction in GMAC mode
– [Figure 216](../figures/figure_216.md): GMAC authentication mode
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

Revision history RM0438
2158/2187 RM0438 Rev 8
12-Apr-2019 2
(continued)
Updated:
– [Figure 217](../figures/figure_217.md): Message construction in CCM mode
– Section 29.4.12: AES counter with CBC-MAC (CCM)
– Section 29.4.14: AES key registers
– Section 29.4.16: AES DMA interface
– Section 29.7.2: AES status register (AES_SR)
– Section 30.6.4: HASH digest registers
– Section 30.6.7: HASH context swap registers
– Major changes to all sections (including figures, tables and registers) of Section 32:
Public key accelerator (PKA)
– Section 33.3.8: PWM input mode
– Section 33.4.2: TIMx control register 2 (TIMx_CR2)(x = 1, 8)
– Section 33.4.20: TIMx break and dead-time register (TIMx_BDTR)(x = 1, 8)
– Section 33.4.21: TIMx DMA control register (TIMx_DCR)(x = 1, 8)
– [Figure 291](../figures/figure_291.md): General-purpose timer block diagram
– [Figure 317](../figures/figure_317.md): Capture/Compare channel 1 main circuit
– Section 34.3.3: Clock selection
– [Figure 318](../figures/figure_318.md): Output stage of Capture/Compare channel (channel 1)
– Section 34.4.1: TIMx control register 1 (TIMx_CR1)(x = 2 to 5)
– Section 34.4.2: TIMx control register 2 (TIMx_CR2)(x = 2 to 5)
– Section 34.4.5: TIMx status register (TIMx_SR)(x = 2 to 5)
– Section 34.4.7: TIMx capture/compare mode register 1 (TIMx_CCMR1)(x = 2 to 5)
– Section 34.4.8: TIMx capture/compare mode register 1 [alternate] (TIMx_CCMR1) (x
= 2 to 5)
– Section 34.4.9: TIMx capture/compare mode register 2 (TIMx_CCMR2)(x = 2 to 5)
– Section 34.4.11: TIMx capture/compare enable register (TIMx_CCER)(x = 2 to 5)
– Section 34.4.12: TIMx counter (TIMx_CNT)(x = 2 to 5)
– Section 34.4.13: TIMx counter [alternate] (TIMx_CNT)(x = 2 to 5)
– [Figure 341](../figures/figure_341.md): TIM15 block diagram
– [Figure 368](../figures/figure_368.md): Output redirection
– Section 35.5.2: TIM15 control register 2 (TIM15_CR2)
– Section 35.5.5: TIM15 status register (TIM15_SR)
– Section 35.5.7: TIM15 capture/compare mode register 1 (TIM15_CCMR1)
– Section 35.5.8: TIM15 capture/compare mode register 1 [alternate] (TIM15_CCMR1)
– Section 35.5.9: TIM15 capture/compare enable register (TIM15_CCER)
– Section 35.5.16: TIM15 break and dead-time register (TIM15_BDTR)
– Section 35.6.3: TIMx DMA/interrupt enable register (TIMx_DIER)(x = 16 to 17)
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

RM0438 Rev 8 2159/2187
RM0438 Revision history
2177
12-Apr-2019 2
(continued)
Updated:
–
– Section 35.6.4: TIMx status register (TIMx_SR)(x = 16 to 17)
– Section 35.6.6: TIMx capture/compare mode register 1  (TIMx_CCMR1)(x = 16 to
17)
– Section 35.6.7: TIMx capture/compare mode register 1 [alternate]  (TIMx_CCMR1)(x
= 16 to 17)
– Section 35.6.8: TIMx capture/compare enable register (TIMx_CCER)(x = 16 to 17)
– Section 35.6.14: TIMx break and dead-time register (TIMx_BDTR)(x = 16 to 17)
– All registers on Section 36.4: TIM6/TIM7 registers
– [Figure 386](../figures/figure_386.md): Low-power timer block diagram
– [Table 303](../tables/table_303.md): Effect of low-power modes on the LPTIM
– Section 37.7.1: LPTIM interrupt and status register (LPTIM_ISR)
– Section 37.7.2: LPTIM interrupt clear register (LPTIM_ICR)
– Section 37.7.3: LPTIM interrupt enable register (LPTIM_IER)
– Section 37.7.4: LPTIM configuration register (LPTIM_CFGR)
– Major changes to all sections (including figures, tables and registers) of Section 39:
Independent watchdog (IWDG)
– [Table 309](../tables/table_309.md): RTC internal input/output signals
– Section 41.6.2: RTC date register (RTC_DR)
– [Figure 399](../figures/figure_399.md): TAMP block diagram
– [Table 319](../tables/table_319.md): TAMP internal input/output signals
– [Table 320](../tables/table_320.md): TAMP interconnection
– Section 42.3.6: Tamper detection
– Section 42.6.1: TAMP control register 1 (TAMP_CR1)
– Section 42.6.11: TAMP interrupt enable register (TAMP_IER)
– Section 42.6.12: TAMP status register (TAMP_SR)
– Section 42.6.13: TAMP non-secure masked interrupt status register (TAMP_MISR)
– Section 42.6.14: TAMP secure masked interrupt status register (TAMP_SMISR)
– [Table 342](../tables/table_342.md): Effect of low-power modes to I2C
– [Table 343](../tables/table_343.md): I2C interrupt requests
– Section 43.9.2: I2C control register 2 (I2C_CR2)
– Section 43.9.3: I2C own address 1 register (I2C_OAR1)
– [Table 344](../tables/table_344.md): I2C register map and reset values
– Section 44: Universal synchronous/asynchronous receiver transmitter
(USART/UART)
– Section 44.5.4: USART FIFOs and thresholds
– Section 44.5.6: USART receiver
– [Figure 452](../figures/figure_452.md): Reception using DMA
– [Table 354](../tables/table_354.md): USART interrupt requests
– Registers and tables of Section 44.8: USART registers
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

Revision history RM0438
2160/2187 RM0438 Rev 8
12-Apr-2019 2
(continued)
Updated:
– Section 45.4.4: LPUART FIFOs and thresholds
– [Figure 466](../figures/figure_466.md): Reception using DMA
– [Table 365](../tables/table_365.md): LPUART interrupt requests
– Registers and tables of Section 45.7: LPUART registers
– Section 46.2: SPI main features
– Section 46.3: SPI implementation
– Section  :
– [Figure 498](../figures/figure_498.md): SAI_ADR format in TDM mode, 32-bit slot width
– Section 47.4.12: SPDIF output
– Section 48.4.4: SDMMC adapter
– [Table 396](../tables/table_396.md): Data path status flags and clear bits
– Section 48.4.6: SDMMC AHB master interface
– Section 54.5.8: Hardware flow control
– Section 48.5.2: CMD12 send timing
– Section 48.9.10: SDMMC data counter register (SDMMC_DCNTR)
– Section 48.9.11: SDMMC status register (SDMMC_STAR)
– Major changes to all sections (including figures, tables and registers) of Section 49:
FD controller area network (FDCAN)
– [Table 423](../tables/table_423.md): STM32L552xx and STM32L562xx USB implementation
– Section 50.6.1: Common registers
– Section 50.6.2: Buffer descriptor table
– Section [Table 433](../tables/table_433.md).: USB register map and reset values
– Section 51.8.3: UCPD control register (UCPD_CR)
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

RM0438 Rev 8 2161/2187
RM0438 Revision history
2177
12-Jun-2019 3
Added:
– Section 8.2.6: VDD12 domain and external SMPS
– [Table 262](../tables/table_262.md): ECC Fp scalar multiplication (Fast Mode)
– [Figure 25](../figures/figure_25.md): Internal main regulator overview
– Section 47.3: SAI implementation
– [Table 356](../tables/table_356.md): STM32L5 Series SAI features
– [Table 373](../tables/table_373.md): External synchronization selection
– [Table 374](../tables/table_374.md): MCLK_x activation conditions
– [Table 377](../tables/table_377.md): TDM frame configuration examples
Updated:
– Section 6.2: FLASH main features
– Section 6.3.6: Flash main memory erase sequences
– Section 6.3.8: Flash errors flags
– [Table 35](../tables/table_35.md): User option byte organization mapping
– Section 6.4.2: Option bytes programming
– Section 6.5.1: TrustZone security protection
– [Table 36](../tables/table_36.md): Default secure option bytes after TZEN activation
– [Table 22](../tables/table_22.md): Secure hide protection
– [Table 38](../tables/table_38.md): Secure, HDP protections summary
– Section 6.7: FLASH memory protection
– Section 6.7.1: Write protection (WRP)
– [Table 47](../tables/table_47.md): Flash access versus RDP level when TrustZone is active (TZEN=1)
– [Table 48](../tables/table_48.md): Flash access versus RDP level when TrustZone is disabled (TZEN=0)
– [Table 49](../tables/table_49.md): Flash mass erase versus RDP level when TrustZone is active (TZEN = 1)
– Section 6.9.7: Flash status register (FLASH_NSSR)
– Section 6.9.8: Flash status register (FLASH_SECSR)
– Section 6.9.10: Flash secure control register (FLASH_SECCR)
– Section 6.9.12: Flash option register (FLASH_OPTR)
– Section 6.9.17: Flash secure watermak1 register 2 (FLASH_SECWM1R2)
– Section 6.9.21: Flash secure watermak2 register 2 (FLASH_SECWM2R2)
– [Table 53](../tables/table_53.md): Flash interface - register map and reset values
– Section 8.1: Power supplies and supply domains
– Section 8.2.2: Embedded SMPS step down converter
– Section 8.2.3: SMPS step down converter power supply scheme
– Section 9.8.10: RCC AHB1 peripheral reset register (RCC_AHB1RSTR)
– [Table 82](../tables/table_82.md): RCC register map and reset values
– [Table 86](../tables/table_86.md): Effect of low-power modes on CRS
– Section 12.3.11: SYSCFG RSS command register (SYSCFG_RSSCMDR)
– [Table 94](../tables/table_94.md): SYSCFG register map and reset values
– Section 20.4.15: OCTOSPI regular-command mode configuration
– Section 20.7.1: OCTOSPI control register (OCTOSPI_CR)
– Section 20.7.2: OCTOSPI device configuration register 1 (OCTOSPI_DCR1)
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

Revision history RM0438
2162/2187 RM0438 Rev 8
12-Jun-2019 3
(continued)
Updated (cont):
– Section 24.6.1: Comparator 1 control and status register (COMP1_CSR)
– [Table 195](../tables/table_195.md): COMP1 input plus assignment
– [Table 201](../tables/table_201.md): COMP register map and reset values
– Section 28.2: RNG main features
– Section 28.3.3: Random number generation
– Section 28.3.5: RNG operation
– Section 28.5: RNG processing time
– [Table 28](../tables/table_28.md).5: RNG processing time
– [Table 223](../tables/table_223.md): RNG configurations
– Section 28.7.4: RNG health test control register (RNG_HTCR)
– Section 29.1: Introduction
– Section 29.4.3: AES cryptographic core
– Section 29.4.4: AES procedure to perform a cipher operation
– Section 29.4.8: AES basic chaining modes (ECB, CBC)
– Section 29.4.12: AES counter with CBC-MAC (CCM)
– [Table 232](../tables/table_232.md): AES interrupt requests
– Section 30.4.5: Message digest computing
– Section 30.6.1: HASH control register (HASH_CR)
– Section 30.6.2: HASH data input register (HASH_DIN)
– Major changes to all Section 31: On-the-fly decryption engine (OTFDEC)
– Major changes to all Section 32: Public key accelerator (PKA)
– External clock source mode 2 on Section 33.3.5: Clock selection
– Section 33.4.5: TIMx status register (TIMx_SR)(x = 1, 8)
– Section 33.4.11: TIMx capture/compare enable register (TIMx_CCER)(x = 1, 8)
– Major changes to all Section 37: Low-power timer (LPTIM)
– Section 42.2: TAMP main features
– [Table 320](../tables/table_320.md): TAMP interconnection
– Section 44.8.9: USART interrupt and status register (USART_ISR)
– Section 44.8.12: USART receive data register (USART_RDR)
– Section 44.8.13: USART transmit data register (USART_TDR)
– Major changes to all Section 47: Serial audio interface (SAI)
– Major changes to all Section 51: USB Type-C®/USB Power Delivery interface
(UCPD)
– Section 52.11.1: DBGMCU registers
Deleted:
– Sections ECC complete addition, ECC double base ladder and ECC projective to
affine from Section 22: Public key accelerator (PKA)
– Tables Modular exponentiation (protected mode), ECC complete addition, ECC
double base ladder, ECC projective to affine from Section 22: Public key accelerator
(PKA)
– Section Secure proprietary code readout protection (PCROP) from Section 5:
Embedded flash memory (FLASH)
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

RM0438 Rev 8 2163/2187
RM0438 Revision history
2177
11-Oct-2019 4
Updated:
– Section 2: Memory and bus architecture introduction
– [Figure 2](../figures/figure_2.md): Memory map based on IDAU mapping.
– Section 3: Boot configuration
– Section 5.3.5: TrustZone illegal access controller (TZIC)
– Section 5.3.6: Power-on/reset state
– Section 5.3.5: TrustZone illegal access controller (TZIC)
– Section 5.5.6: GTZC_TZSC external memory x non-secure watermark register 1
(GTZC_TZSC_MPCWMxANSR)
– Section 5.5.7: GTZC_TZSC external memory x non-secure watermark register 2
(GTZC_TZSC_MPCWMxBNSR)
– Section 5.6.2: GTZC_MPCBB1 lock register 1(GTZC_MPCBB1_LCKVTR1)
– Section : Rules for modifying specific option bytes
– Section : Level 1: readout protection
– Section : Level 2: no debug
– Section : Level 1: readout protection
– Section : Level 2: no debug
– Section 6.9.15: Flash secure boot address 0 register (FLASH_SECBOOTADD0R)
– Section 8.2.2: Embedded SMPS step down converter
– [Table 62](../tables/table_62.md): SMPS modes summary
– Section 8.2.3: SMPS step down converter power supply scheme
– Section 8.2.4: SMPS step down converter versus low-power mode
– Section 8.2.5: Dynamic voltage scaling management
– Section 9.3: Clocks introduction
– Section 9.3.3: MSI clock
– Caution note in Section 9.8.4: RCC PLL configuration register (RCC_PLLCFGR)
– Section 10.1: CRS introduction
– Section 10.4.4: Frequency error measurement
– Section 10.4.6: CRS initialization and configuration
– Section 10.7: CRS registers
– Section 11.3: GPIO functional description
– Section 11.4: TrustZone security
– Section 11.6.3: GPIO port output speed register (GPIOx_OSPEEDR) (x = A to H)
– Section 17.6.7: EXTI privilege configuration register (EXTI_PRIVCFGR1)
– Section 17.6.16: EXTI lock register (EXTI_LOCKR)
– Section 17.6.16: EXTI lock register (EXTI_LOCKR)
– Section 19.6.4: NOR flash/PSRAM controller asynchronous transactions
– Section 19.6.5: Synchronous transactions
– [Figure 93](../figures/figure_93.md): ADC block diagram
– [Table 165](../tables/table_165.md): ADC internal input/output signals
– Section 21.4.7: Single-ended and differential input channels
– Section 21.4.11: Channel selection (ADC_SQRy, ADC_JSQR)
– Section 21.4.20: Discontinuous mode (DISCEN, DISCNUM, JDISCEN)
– Section 21.4.26: Data management
– Section 21.4.29: Analog window watchdog (AWD1EN, JAWD1EN, AWD1SGL,
AWD1CH, AWD2CH, AWD3CH, AWD_HTx, AWD_LTx, AWDx)
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

Revision history RM0438
2164/2187 RM0438 Rev 8
11-Oct-2019 4
(continued)
– Section 21.7.6: ADC sample time register 1 (ADC_SMPR1)
– Section 21.7.7: ADC sample time register 2 (ADC_SMPR2)
– Section 21.7.11: ADC regular sequence register 1 (ADC_SQR1)
– Section 21.7.12: ADC regular sequence register 2 (ADC_SQR2)
– Section 21.7.13: ADC regular sequence register 3 (ADC_SQR3)
– Section 21.7.14: ADC regular sequence register 4 (ADC_SQR4)
– Section 21.7.16: ADC injected sequence register (ADC_JSQR)
– Section 21.7.17: ADC offset y register (ADC_OFRy)
– Section 21.7.19: ADC analog watchdog 2 configuration register (ADC_AWD2CR)
– Section 21.7.20: ADC analog watchdog 3 configuration register (ADC_AWD3CR)
– Section 21.7.21: ADC differential mode selection register (ADC_DIFSEL)
– Section 22.3: DAC implementation
– Section 22.4.6: DAC trigger selection
– Section 22.4.10: DAC channel modes
– Section 22.4.11: DAC channel buffer calibration
– Section 22.4.13: Dual DAC channel conversion modes (if dual channels are
available)
– [Table 190](../tables/table_190.md): DAC interrupts
– Section 22.7.1: DAC control register (DAC_CR)
– Section 26.2: DFSDM main features
– Section 26.4.3: DFSDM reset and clocks
– Section 26.7: DFSDM channel y registers (y=0..3) introduction
– Section 26.7.5: DFSDM channel y data input register (DFSDM_CHyDATINR)
– Section 26.8: DFSDM filter x module registers (x=0..3) introduction
– [Table 216](../tables/table_216.md): Spread spectrum deviation versus AHB clock frequency
– Section 28.2: RNG main features
– Section 28.3.5: RNG operation
– Section 28.5: RNG processing time
– Section 28.7.3: RNG data register (RNG_DR)
– [Figure 211](../figures/figure_211.md): CTR encryption
– Section 30: Hash processor (HASH)
– Section 33.3.3: Repetition counter
– [Table 285](../tables/table_285.md): TIMx internal trigger connection
– Section 35.5: TIM15 registers introduction
– Section 35.6: TIM16/TIM17 registers introduction
– [Figure 386](../figures/figure_386.md): Low-power timer block diagram
– Section 37.4.16: Repetition counter
– Section 37.6: LPTIM interrupts
– Section 37.7.8: LPTIM counter register (LPTIM_CNT)
– Section 40: System window watchdog (WWDG)
– Section 42.6.2: TAMP control register 2 (TAMP_CR2)
– [Table 354](../tables/table_354.md): USART interrupt requests
– [Table 44](../tables/table_44.md).8: USART registers introduction
– [Table 45](../tables/table_45.md).7: LPUART registers introduction
– [Table 371](../tables/table_371.md): SAI internal input/output signals
– [Figure 497](../figures/figure_497.md): Start-up sequence
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

RM0438 Rev 8 2165/2187
RM0438 Revision history
2177
11-Oct-2019 4
(continued)
– [Table 381](../tables/table_381.md): SAI interrupt sources
– Section 47.6: SAI registers introduction
Added
– Section 6.5.5: Forcing boot from a secure memory address
– Section 10.3: CRS implementation
Deleted:
– 3.6.3 GTZC_MPCBBx lock register 2 (GTZC_MPCBBx_LCKVTR2) (x = 1 to 2)
13-Feb-2020 5
Updated cover page.
Updated Section 2: Memory and bus architecture introduction.
Updated Section 2.1: System architecture introduction.
Updated [Figure 1](../figures/figure_1.md): System architecture.
Updated Section 3: Boot configuration.
Added Section 4: System security.
FLASH:
Updated Section 6.3.1: Flash memory organization.
Updated [Table 31](../tables/table_31.md): Flash module - 512 KB dual bank organization (64 bits read width).
Updated [Table 33](../tables/table_33.md): Flash module - 512 KB single bank organization (128 bits read
width).
Updated Section 6.3.5: Flash program and erase operations.
Updated Section 6.3.6: Flash main memory erase sequences.
Updated Section 6.3.7: Flash main memory programming sequences.
Updated Section 6.3.8: Flash errors flags.
Updated Section 6.4.1: Option bytes description.
Updated Section 6.4.2: Option bytes programming.
Updated Section 6.5.1: TrustZone security protection.
Updated Section 6.5.3: Secure hide protection (HDP).
Updated [Table 38](../tables/table_38.md): Secure, HDP protections summary.
Updated Section 6.5.4: Secure block-based area (SECBB) protection.
Added Section 6.6: Secure system memory.
Updated Section 6.7.2: Readout protection (RDP).
Updated [Table 43](../tables/table_43.md): Flash memory readout protection status (TZEN=0).
Updated [Table 45](../tables/table_45.md): Flash memory readout protection status (TZEN=1).
Updated [Table 50](../tables/table_50.md): Flash system memory, RSS and OTP accesses.
Updated Section 6.9.7: Flash status register (FLASH_NSSR).
Updated Section 6.9.11: Flash ECC register (FLASH_ECCR).
PWR:
Updated [Figure 21](../figures/figure_21.md): STM32L552xx and STM32L562xx power supply overview.
Updated [Figure 22](../figures/figure_22.md): STM32L552xxxP and STM32L562xxxP power supply overview.
Updated [Table 64](../tables/table_64.md): SMPS step down converter versus low-power modes.
Updated Section 8.2.6: VDD12 domain and external SMPS.
Updated Section 8.3.4: Upper voltage threshold monitoring.
Updated Section 8.3.5: Temperature threshold monitoring.
RCC:
Updated Section 9.8.1: RCC clock control register (RCC_CR).
Added Section 9.8.33: OCTOSPI delay configuration register (RCC_DLYCFGR).
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

Revision history RM0438
2166/2187 RM0438 Rev 8
13-Feb-2020 5
(continued)
SYSCFG:
Updated Section 12.3.11: SYSCFG RSS command register (SYSCFG_RSSCMDR).
NVIC:
Updated Section 16.1: NVIC main features.
OCTOSPI:
Updated entire Section 20: Octo-SPI interface (OCTOSPI).
ADC:
Updated Section 21.2: ADC main features.
Updated Section : Reading the temperature.
Updated Section : Calculating the actual VREF+ voltage using the internal reference
voltage.
VREFBUF:
Added Section 23.3: VREFBUF trimming.
Updated Section 23.4.2: VREFBUF calibration control register (VREFBUF_CCR).
RNG:
Updated Section 28.1: RNG introduction.
Updated Section 28.3.3: Random number generation.
Updated Section 28.6.3: Data collection.
PKA:
Added Section 32.3.3: PKA reset and clocks.
Updated [Table 258](../tables/table_258.md): Arithmetic comparison.
Updated [Table 269](../tables/table_269.md): Modular exponentiation computation times.
Updated [Table 270](../tables/table_270.md): ECC scalar multiplication computation times.
Updated [Table 271](../tables/table_271.md): ECDSA signature average computation times.
Updated [Table 272](../tables/table_272.md): ECDSA verification average computation times.
Updated [Table 274](../tables/table_274.md): Montgomery parameters average computation times.
USART:
Updated [Table 44](../tables/table_44.md).8.6: USART guard time and prescaler register (USART_GTPR).
LPUART:
Added [Table 45](../tables/table_45.md).3: LPUART implementation.
FDCAN:
Updated [Figure 550](../figures/figure_550.md): Message RAM configuration.
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

RM0438 Rev 8 2167/2187
RM0438 Revision history
2177
29-Apr-2020 6
Memory and bus architecture:
Updated Section 2: Memory and bus architecture.
Updated Section 2.1: System architecture.
Updated Section 2.2: TrustZone security architecture.
Updated [Table 1](../tables/table_1.md): Example of memory map security attribution versus SAU regions
configuration.
Updated Section 2.2.1: Default TrustZone security state.
Updated Section 2.2.2: TrustZone peripheral classification.
Updated [Table 2](../tables/table_2.md): Securable peripherals by TZSC.
Updated [Table 3](../tables/table_3.md): TrustZone-aware peripherals.
Memory organization:
Updated Section 2: Memory and bus architecture.
Updated Section 2.1: System architecture.
Embedded SRAM:
Updated Section 2.4.1: SRAM2 parity check.
Updated Section 2.4.2: SRAM2 Write protection.
Updated Section 2.4.4: SRAM2 Erase.
Embedded flash memory:
Updated Section 6.7.2: Readout protection (RDP) notes.
Updated Reset value by ST production value and SWAP_BANK bit description in
Section 6.9.12: Flash option register (FLASH_OPTR).
Updated Reset value by ST production value in:
– Section 6.9.13: Flash non-secure boot address 0 register (FLASH_NSBOOTADD0R)
– Section 6.9.14: Flash non-secure boot address 1 register (FLASH_NSBOOTADD1R)
– Section 6.9.15: Flash secure boot address 0 register (FLASH_SECBOOTADD0R).
– Section 6.9.16: Flash bank 1 secure watermak1 register (FLASH_SECWM1R1).
– Section 6.9.17: Flash secure watermak1 register 2 (FLASH_SECWM1R2).
– Section 6.9.18: Flash WPR1 area A address register (FLASH_WRP1AR).
– Section 6.9.19: Flash WPR1 area B address register (FLASH_WRP1BR).
– Section 6.9.20: Flash secure watermak2 register (FLASH_SECWM2R1)
– Section 6.9.21: Flash secure watermak2 register 2 (FLASH_SECWM2R2)
– Section 6.9.22: Flash WPR2 area A address register (FLASH_WRP2AR)
– Section 6.9.23: Flash WPR2 area B address register (FLASH_WRP2BR)
– [Table 53](../tables/table_53.md): Flash interface - register map and reset values
ICACHE:
Added Section 7.3: ICACHE implementation.
Updated [Figure 18](../figures/figure_18.md): ICACHE block diagram.
Updated Section 7.4.3: ICACHE TAG memory.
Updated [Table 55](../tables/table_55.md): TAG memory dimensioning parameters for n-way set associative
operating mode (default).
Updated [Figure 19](../figures/figure_19.md): ICACHE TAG and data memories functional view.
Updated [Table 56](../tables/table_56.md): TAG memory dimensioning parameters for direct-mapped cache
mode.
Updated Section 7.4.5: ICACHE enable.
Updated [Table 61](../tables/table_61.md): ICACHE register map and reset values.
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

Revision history RM0438
2168/2187 RM0438 Rev 8
29-Apr-2020 6
(continued)
SYSTEM SECURITY:
Updated Section 4.6.6: Managing security in TrustZone-aware peripherals ‘General-
purpose I/Os (GPIO)’ paragraph.
Added [Table 16](../tables/table_16.md): Summary of the I/Os that can be secured and connected to a non-
secure peripheral.
PWR:
Updated Section 8.2.2: Embedded SMPS step down converter:
Updated [Table 62](../tables/table_62.md): SMPS modes summary note 1.
Removed below the table.
Updated Section 8.2.4: SMPS step down converter versus low-power mode.
Updated [Table 64](../tables/table_64.md): SMPS step down converter versus low-power modes.
Added notes below the table.
Moved Section 8.2.1: Voltage regulator before Section 8.2.2: Embedded SMPS step
down converter.
Updated Section 8.2.6: VDD12 domain and external SMPS.
SYSCFG:
Updated [Table 92](../tables/table_92.md): TrustZone security and privilege register accesses.
TSC:
Updated Section 27.3.2: Surface charge transfer acquisition overview.
Updated Section 27.3.4: Charge transfer acquisition sequence.
Updated [Figure 191](../figures/figure_191.md): Charge transfer acquisition sequence.
PKA:
Updated Section 32.7.4: PKA RAM adding note.
IRTIM:
Added [Figure 394](../figures/figure_394.md): IRTIM internal hardware connections with TIM16 and TIM17.
USART:
Replaced ‘microcontroller’ by ‘device’ in the whole document.
Updated Section 44.4: USART implementation and Section 45.3: LPUART
implementation.
Updated PSC bitfield description in USART_GTPR register.
Updated SBKF bit description in USART_ISR and LPUART_ISR registers.
Updated decimal and hexadecimal notation for values in Section : How to derive
USARTDIV from USART_BRR register values.
SDMMC:
Updated Section 48.1: SDMMC main features.
DEBUG:
Updated Section 52.11.1: DBGMCU registers:
– DBGMCU identity code register (DBGMCU_IDCODE)
– DBGMCU APB1 freeze register 1 (DBGMCU_APB1FZR1)
– DBGMCU APB1 freeze register 2 (DGBMCU_APB1FZR2)
Updated [Table 468](../tables/table_468.md): DBGMCU register map and reset values.
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

RM0438 Rev 8 2169/2187
RM0438 Revision history
2177
07-Dec-2020 7
Updated:
System security:
– Section 4.4.1: Introduction
– Section 4.4.3: Immutable root of trust in system flash memory
– Section : Securing peripherals with TZSC
– [Table 10](../tables/table_10.md): MPCWMx instances
– Section : General-purpose I/Os (GPIO)
– [Table 16](../tables/table_16.md): Summary of the I/Os that can be secured and connected to a non-secure
peripheral
– Section : Extended interrupts and event controller (EXTI)
– Section 4.6.7: Activating TrustZone security
– [Figure 8](../figures/figure_8.md): Flash memory secure hide protection (HDP) area
– Section : Response to tampers
– Section 4.9.1: Introduction
– Section 4.11.2: Recommended option byte settings
– [Figure 13](../figures/figure_13.md): External flash memory protection using SFI
Embedded flash memory (FLASH):
– Section 6.7.2: Readout protection (RDP)
– Section 6.9.12: Flash option register (FLASH_OPTR)
– [Table 53](../tables/table_53.md): Flash interface - register map and reset values
Power control (PWR):
– Section 8.2.2: Embedded SMPS step down converter
– Section 8.2.6: VDD12 domain and external SMPS
– Section 8.3.1: Power-on reset (POR) / power-down reset (PDR) / brown-out reset
(BOR)
– Section 8.3.2: Programmable voltage detector (PVD)
– [Table 67](../tables/table_67.md): Functionalities depending on the working mode
– Section : I/O states in Low-power run mode
– Section 8.6.3: Power control register 3 (PWR_CR3)
Clock recovery system (CRS):
– Section 10.7.1: CRS control register (CRS_CR)
Direct memory access controller (DMA):
– Section 14.6.3: DMA channel x configuration register (DMA_CCRx)
– Section 14.6.4: DMA channel x number of data to transfer register (DMA_CNDTRx)
– Section 14.6.5: DMA channel x peripheral address register (DMA_CPARx)
– Section 14.6.6: DMA channel x memory 0 address register (DMA_CM0ARx)
– Section 14.6.7: DMA channel x memory 1 address register (DMA_CM1ARx)
DMA request multiplexer (DMAMUX):
– Section 15.4.6: DMAMUX request line multiplexer
Octo-SPI interface (OCTOSPI):
– Major updates in the whole section
Analog-to-digital converters (ADC):
– Section 21.4.6: ADC Deep-power-down mode (DEEPPWD) and ADC voltage
regulator (ADVREGEN)
– Section 21.4.7: Single-ended and differential input channels
– [Figure 103](../figures/figure_103.md): Stopping ongoing regular and injected conversions
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

Revision history RM0438
2170/2187 RM0438 Rev 8
07-Dec-2020 7
(continued)
Update (continued):
Analog-to-digital converters (ADC) (continued):
– Section 21.4.19: Injected channel management
– [Figure 129](../figures/figure_129.md): AUTODLY = 1, regular HW conversions interrupted by injected
conversions (DISCEN = 1, JDISCEN = 1)
– [Figure 132](../figures/figure_132.md): Analog watchdog guarded area
– Section 21.4.34: Monitoring the internal voltage reference
Digital-to-analog converter (DAC):
– In this section, DAC_OUTx was replaced by DACxOUTy
– [Figure 163](../figures/figure_163.md): Dual-channel DAC block diagram
– [Table 185](../tables/table_185.md): DAC input/output pins
Voltage reference buffer (VREFBUF):
– Section 23.4.2: VREFBUF calibration control register (VREFBUF_CCR)
AES hardware accelerator (AES):
– Section : GCM processing
– Section 29.5: AES interrupts
– Section 29.7.1: AES control register (AES_CR)
– Section 29.7.17: AES suspend registers (AES_SUSPxR)
– [Table 235](../tables/table_235.md): AES register map and reset values
Hash processor (HASH):
– In this section “NBLW” is now referred to as “NBLW[4:0]”
– Section 30.4.5: Message digest computing
– Section : HMAC processing
– Section 30.6.1: HASH control register (HASH_CR)
– Section 30.6.7: HASH context swap registers
– [Table 240](../tables/table_240.md): HASH register map and reset values
On-the-fly decryption engine (OTFDEC):
– Section : OTFDEC architecture
– Section 31.5.1: OTFDEC initialization process
– Section 31.6.1: OTFDEC control register (OTFDEC_CR)
– Section 31.6.2: OTFDEC privileged access control configuration register
(OTFDEC_PRIVCFGR)
– Section 31.6.3: OTFDEC region x configuration register (OTFDEC_RxCFGR)
Public key accelerator (PKA):
– Section 32.3.4: PKA public key acceleration
– Section : Montgomery space and fast mode operations
– Section 32.3.6: PKA procedure to perform an operation
– Section : Using precomputed Montgomery parameters (PKA fast mode)
– Section 32.5.1: Supported elliptic curves
– [Table 268](../tables/table_268.md): Family of supported curves for ECC operations
– [Table 269](../tables/table_269.md): Modular exponentiation computation times
– [Table 273](../tables/table_273.md): Point on elliptic curve Fp check average computation times
– [Table 274](../tables/table_274.md): Montgomery parameters average computation times
– [Table 275](../tables/table_275.md): PKA interrupt requests
– Section 32.7.2: PKA status register (PKA_SR)
– Section 32.7.3: PKA clear flag register (PKA_CLRFR)
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

RM0438 Rev 8 2171/2187
RM0438 Revision history
2177
07-Dec-2020 7
(continued)
Update (continued):
General-purpose timers (TIM2/TIM3/TIM4/TIM5):
– [Figure 315](../figures/figure_315.md): Control circuit in external clock mode 2
Universal synchronous/asynchronous receiver transmitter (USART/UART):
– Section 44.2: USART main features
– [Table 346](../tables/table_346.md): USART / LPUART features
– Section 44.5.7: USART baud rate generation
– [Figure 454](../figures/figure_454.md): RS232 RTS flow control
– [Figure 455](../figures/figure_455.md): RS232 CTS flow control
– Section 44.6: USART in low-power modes
– Section 44.7: USART interrupts
– Section 44.8.8: USART request register (USART_RQR)
– Section 44.8.9: USART interrupt and status register (USART_ISR)
– Section 44.8.10: USART interrupt and status register [alternate] (USART_ISR)
Low-power universal asynchronous receiver transmitter (LPUART):
– [Table 346](../tables/table_346.md): USART / LPUART features
– [Table 360](../tables/table_360.md): Error calculation for programmed baud rates at
lpuart_ker_ck_pres = 32.768 kHz
– Section 45.5: LPUART in low-power modes
– [Table 364](../tables/table_364.md): Effect of low-power modes on the LPUART
– [Table 365](../tables/table_365.md): LPUART interrupt requests
Serial peripheral interface (SPI):
– [Table 367](../tables/table_367.md): STM32L552xx and STM32L562xx SPI implementation
– Section 46.4.2: Communications between one master and one slave
Serial audio interface (SAI):
– [Table 370](../tables/table_370.md): SAI features
Secure digital input/output MultiMediaCard interface (SDMMC):
– Section 48.9.2: SDMMC clock control register (SDMMC_CLKCR)
FD controller area network (FDCAN):
– Section 49.3.6: Message RAM
– [Figure 550](../figures/figure_550.md): Message RAM configuration
USB Type-C™ / USB Power Delivery interface (UCPD):
– Section 51.1: UCPD introduction
– Section 51.2: UCPD main features
– Section 51.4.6: UCPD Type-C pull-ups (Rp) and pull-downs (Rd)
– Section 51.8.1: UCPD configuration register 1 (UCPD_CFGR1)
– Section 51.8.3: UCPD control register (UCPD_CR)
– Section [Table 445](../tables/table_445.md).: UCPD register map and reset values
Added:
– [Table 15](../tables/table_15.md): Summary of the I/Os that cannot be connected to a non-secure peripheral
when secure
– Section 51.7.3: UCPD configuration register 2 (UCPD_CFGR3)
Deleted:
–O n  Section 45.3: LPUART implementation: Table USART /LPUART features
–O n  Section 48.4: SDMMC functional description: Section Hardware flow control
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

Revision history RM0438
2172/2187 RM0438 Rev 8
03-Jun-2025 8
Cover page:
Added patented technology notice.
Added errata sheet reference.
Documentation conventions:
Updated Section 1.1: General information.
Updated Section 1.2: List of abbreviations for registers.
Added Section 1.3: Register reset value.
Memory and bus architecture:
Updated Section : Embedded bootloader and RSS.
Memory and bus architecture:
Updated Section : Embedded bootloader and RSS.
FLASH:
Updated Section 6.3.1: Flash memory organization.
Added [Table 30](../tables/table_30.md): Flash module - 256 KB dual bank organization (64 bits read width).
Updated [Table 31](../tables/table_31.md): Flash module - 512 KB dual bank organization (64 bits read width).
Added [Table 32](../tables/table_32.md): Flash module - 256 KB single bank organization (128 bits read width).
Updated [Table 33](../tables/table_33.md): Flash module - 512 KB single bank organization (128 bits read
width).
ICACHE:
Whole section re-edited.
PWR:
Updated Section 8.1.4: Battery backup domain.
Updated Section 8.2.3: SMPS step down converter power supply scheme.
Updated [Figure 24](../figures/figure_24.md): SMPS step down converter power supply scheme.
Updated Section 8.3.2: Programmable voltage detector (PVD).
Updated Section 8.6.2: Power control register 2 (PWR_CR2).
Updated Section 8.6.6: Power status register 2 (PWR_SR2).
RCC:
Updated Section 9.1.2: System reset.
Updated Section : Software calibration.
Updated Section 9.8.8: RCC clock interrupt flag register (RCC_CIFR).
Updated Section 9.8.29: RCC Backup domain control register (RCC_BDCR).
CRS:
Whole section re-edited.
RCC:
Updated Section 11.3.2: I/O pin alternate function multiplexer and mapping.
DMAMUX:
Updated Section 15.3.2: DMAMUX mapping.
Updated Section 15.4.6: DMAMUX request line multiplexer.
Updated Section 15.4.7: DMAMUX request generator.
NVIC:
Updated [Table 109](../tables/table_109.md): STM32L552xx and STM32L562xx vector table.
CRC:
Updated Section 18.2: CRC main features.
Updated [Table 51](../tables/table_51.md): CRC calculation unit block diagram.
Updated Section 18.3.3: CRC operation.
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

RM0438 Rev 8 2173/2187
RM0438 Revision history
2177
03-Jun-2025 8
(continued)
Updated introduction to Section 18.4: CRC registers.
FSMC:
Updated [Figure 70](../figures/figure_70.md): Synchronous multiplexed read mode waveforms - NOR, PSRAM
(CRAM).
Updated [Figure 71](../figures/figure_71.md): Synchronous multiplexed write mode waveforms - PSRAM
(CRAM).
Updated Section : PSRAM chip select counter register (FMC_PCSCNTR).
OCTOSPI:
Whole section re-edited.
ADC:
Updated [Figure 94](../figures/figure_94.md): ADC clock scheme.
Updated [Figure 95](../figures/figure_95.md): ADC1 connectivity.
Updated Section 21.4.6: ADC Deep-power-down mode (DEEPPWD) and ADC voltage
regulator (ADVREGEN).
Updated [Figure 100](../figures/figure_100.md): Enabling / disabling the ADC.
Updated Section 21.4.10: Constraints when writing the ADC control bits.
Updated Section : Auto-injection mode.
Updated Section : Analog watchdog.
Updated [Figure 142](../figures/figure_142.md): Triggered regular oversampling with injection.
Updated [Figure 151](../figures/figure_151.md): Alternate trigger: 4 injected channels (each ADC) in
discontinuous mode.
Updated [Figure 158](../figures/figure_158.md): DMA requests in regular simultaneous mode when MDMA = 10.
Added Section 21.5: ADC in low-power mode.
Updated Section 21.7.4: ADC configuration register (ADC_CFGR).
Updated Section 21.7.16: ADC injected sequence register (ADC_JSQR).
Updated Section 21.8.1: ADC common status register (ADC_CSR).
Updated Section 21.8.2: ADC common control register (ADC_CCR).
Updated Section 21.8.3: ADC common regular data register for dual mode
(ADC_CDR).
ADC:
Updated Section 22.2: DAC main features.
Updated Section 22.3: DAC implementation.
Updated [Figure 163](../figures/figure_163.md): Dual-channel DAC block diagram.
Updated [Figure 166](../figures/figure_166.md): Timing diagram for conversion with trigger disabled TEN = 0.
Added Section 22.4.12: DAC channel conversion modes.
COMP:
Updated Section 24.6.2: Comparator 2 control and status register (COMP2_CSR).
DFSDM:
Updated Section 26.3: DFSDM implementation.
Updated Section 26.4.3: DFSDM reset and clocks.
Updated Section : Manchester coded data input format operation.
Updated Section : Clock absence detection.
Updated Section : Manchester/SPI code synchronization.
TSC:
Updated Section 27.2: TSC main features.
Updated [Figure 189](../figures/figure_189.md): Surface charge transfer analog I/O group structure.
Updated [Figure 215](../figures/figure_215.md): Acquisition sequence summary.
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

Revision history RM0438
2174/2187 RM0438 Rev 8
03-Jun-2025 8
(continued)
Updated Section 27.3.3: Reset and clocks.
RNG:
Whole section re-edited.
AES:
Updated Section : Suspend/resume operations in ECB/CBC modes.
Updated Section : CTR encryption and decryption.
Updated [Figure 214](../figures/figure_214.md): GCM authenticated encryption.
Updated [Table 229](../tables/table_229.md): Initialization of AES_IVRx registers in GCM mode.
Updated Section : GCM processing.
Updated [Table 230](../tables/table_230.md): Initialization of AES_IVRx registers in CCM mode.
Updated Section : DMA operation in different operating modes.
Updated Section 29.5: AES interrupts.
HASH:
Updated Section 30.4.5: Message digest computing.
Updated Section 30.4.7: HMAC operation.
OTFDEC:
Updated Section 31.3.3: OTFDEC on-the-fly decryption.
Replaced Non-Tustzone by Nonsecure in Section 31.6: OTFDEC registers.
PKA:
Updated Section 32.4.5: Modular and Montgomery multiplication.
TIM1/TIM8:
Updated [Figure 254](../figures/figure_254.md): Control circuit in normal mode, internal clock divided by 1.
Updated Section 33.3.16: Using the break function.
Updated Section 33.3.18: Clearing the OCxREF signal on an external event.
Updated [Figure 282](../figures/figure_282.md): Retriggerable one pulse mode.
Updated Section 33.3.22: Encoder interface mode.
Updated Section 33.3.25: Interfacing with Hall sensors.
Updated Section 33.4.3: TIMx slave mode control register (TIMx_SMCR)(x = 1, 8).
Updated Section 33.4.8: TIMx capture/compare mode register 1 [alternate]
(TIMx_CCMR1)(x = 1, 8).
Updated Section 33.4.20: TIMx break and dead-time register (TIMx_BDTR)(x = 1, 8).
TIM2/TIM3/TIM4/TIM5:
Updated [Figure 254](../figures/figure_254.md): Control circuit in normal mode, internal clock divided by 1.
Updated Section 34.3.12: Clearing the OCxREF signal on an external event.
Updated Section 34.3.15: Encoder interface mode.
Updated Section : Slave mode: Trigger mode.
Updated Section 34.4.8: TIMx capture/compare mode register 1 [alternate]
(TIMx_CCMR1) (x = 2 to 5).
Updated Section 34.4.11: TIMx capture/compare enable register (TIMx_CCER)(x = 2
to 5).
TIM15/TIM16/TIM17:
Updated [Figure 352](../figures/figure_352.md): Control circuit in normal mode, internal clock divided by 1.
Updated Section 35.4.13: Using the break function.
Added Section 35.4.15: 6-step PWM generation.
Updated [Figure 371](../figures/figure_371.md): Retriggerable one pulse mode.
Added Section 35.5.3: TIM15 slave mode control register (TIM15_SMCR).
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

RM0438 Rev 8 2175/2187
RM0438 Revision history
2177
03-Jun-2025 8
(continued)
Added Section 35.5.4: TIM15 DMA/interrupt enable register (TIM15_DIER).
Added Section 35.5.8: TIM15 capture/compare mode register 1 [alternate]
(TIM15_CCMR1).
Added Section 35.5.9: TIM15 capture/compare enable register (TIM15_CCER).
Added Section 35.5.16: TIM15 break and dead-time register (TIM15_BDTR).
Added Section 35.6.7: TIMx capture/compare mode register 1 [alternate]
(TIMx_CCMR1)(x = 16 to 17).
Added Section 35.6.9: TIMx counter (TIMx_CNT)(x = 16 to 17).
Added Section 35.6.14: TIMx break and dead-time register (TIMx_BDTR)(x = 16 to
17).
TIM6/TIM7:
Updated Section 36.3.2: Counting mode.
TIM6/TIM7:
Updated [Figure 386](../figures/figure_386.md): Low-power timer block diagram.
Updated Section 37.4.3: LPTIM input and trigger mapping.
Updated Section 37.4.5: Glitch filter.
Updated Section 37.4.7: Trigger multiplexer.
Updated introduction to Section 37.7: LPTIM registers.
Updated Section 37.7.5: LPTIM control register (LPTIM_CR).
Updated Section 37.7.8: LPTIM counter register (LPTIM_CNT).
WWDG:
Updated [Figure 396](../figures/figure_396.md): Watchdog block diagram.
Updated Section 40.4: WWDG interrupts.
Updated Section 40.5.2: WWDG configuration register (WWDG_CFR).
RTC:
Updated Section 41.3.4: RTC secure protection modes.
Updated Section 41.3.6: Clock and prescalers.
Updated Section 41.3.8: Calendar ultra-low power mode.
Updated Section 41.3.19: Tamper and alarm output.
Updated Section 41.6.20: RTC status register (RTC_SR).
Updated Section 41.6.21: RTC non-secure masked interrupt status register
(RTC_MISR).
Updated Section 41.6.22: RTC secure masked interrupt status register (RTC_SMISR).
TAMP:
Updated Section : Active tamper detection.
Updated Section 42.6.1: TAMP control register 1 (TAMP_CR1).
I2C:
Whole section re-edited.
USART/UART:
Updated [Table 346](../tables/table_346.md): USART / LPUART features.
Updated Section 44.5.2: USART signals.
Added [Table 347](../tables/table_347.md): USART/UART input/output pins
Added [Table 348](../tables/table_348.md): USART internal input/output signals
Updated Section 44.5.5: USART transmitter
Updated Section 44.5.6: USART receiver
Updated Section : Overrun error
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

Revision history RM0438
2176/2187 RM0438 Rev 8
03-Jun-2025 8
(continued)
Updated Section 44.5.13: USART LIN (local interconnection network) mode.
Updated [Figure 443](../figures/figure_443.md): USART example of synchronous master transmission.
Updated [Figure 451](../figures/figure_451.md): Transmission using DMA.
Updated [Figure 452](../figures/figure_452.md): Reception using DMA.
Updated [Figure 455](../figures/figure_455.md): RS232 CTS flow control.
Updated Section 44.5.21: USART low-power management.
Updated Section 44.8.3: USART control register 2 (USART_CR2).
Updated Section 44.8.9: USART interrupt and status register (USART_ISR).
Updated Section 44.8.10: USART interrupt and status register [alternate]
(USART_ISR).
Updated Section 44.8.14: USART prescaler register (USART_PRESC).
LPUART:
Updated [Table 356](../tables/table_356.md): Instance implementation on STM32L552xx and STM32L562xx.
Updated [Figure 458](../figures/figure_458.md): LPUART block diagram.
Added [Table 358](../tables/table_358.md): LPUART input/output pins.
Added [Table 359](../tables/table_359.md): LPUART internal input/output signals.
Updated Section 45.4.6: LPUART receiver.
Updated [Figure 465](../figures/figure_465.md): Transmission using DMA.
Updated [Figure 466](../figures/figure_466.md): Reception using DMA.
Updated [Figure 468](../figures/figure_468.md): RS232 RTS flow control.
Updated [Figure 469](../figures/figure_469.md): RS232 CTS flow control.
Updated Section 45.4.14: LPUART low-power management.
Updated Section 45.7.3: LPUART control register 2 (LPUART_CR2).
Updated Section 45.7.7: LPUART interrupt and status register (LPUART_ISR).
Updated Section 45.7.8: LPUART interrupt and status register [alternate]
(LPUART_ISR).
Updated Section 45.7.12: LPUART prescaler register (LPUART_PRESC).
SAI:
Whole section re-edited.
SDMMC:
Updated Section 48.3: SDMMC operation modes.
Updated Section 48.4.4: SDMMC adapter.
Updated Section : Normal boot operation.
Updated Section 48.9.2: SDMMC clock control register (SDMMC_CLKCR).
Updated Section 48.9.3: SDMMC argument register (SDMMC_ARGR).
FDCAN:
Whole section re-edited.
USB:
Updated [Table 425](../tables/table_425.md): Bulk double-buffering memory buffers usage.
UCPD:
Updated Section 51.1: UCPD introduction.
Updated Section 51.2: UCPD main features.
Updated [Table 434](../tables/table_434.md): UCPD implementation.
Updated [Table 435](../tables/table_435.md): UCPD signals on pins.
Updated Section 51.4.2: UCPD reset and clocks.
Updated Section 51.4.8: UCPD fast role swap (FRS).
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

RM0438 Rev 8 2177/2187
RM0438 Revision history
2177
03-Jun-2025 8
(continued)
Updated [Table 442](../tables/table_442.md): Type-C sequence (source: 3A); cable/sink connected (Rd on CC1;
Ra on CC2).
Removed section UCPD configuration register 3 (UCPD_CFGR3).
Updated Section 51.8.3: UCPD control register (UCPD_CR).
DEBUG:
Updated Section 52.2.9: Serial-wire debug port.
Updated Section : DP event status register (DP_RESENDR).
[Table 469](../tables/table_469.md). Document revision history (continued)
Date Revision Changes

Index RM0438
2178/2187 RM0438 Rev 8
Index
A
ADC_AWD2CR  . . . . . . . . . . . . . . . . . . . . . . .785
ADC_AWD3CR  . . . . . . . . . . . . . . . . . . . . . . .786
ADC_CALFACT . . . . . . . . . . . . . . . . . . . . . . .787
ADC_CFGR . . . . . . . . . . . . . . . . . . . . . . . . . .768
ADC_CFGR2 . . . . . . . . . . . . . . . . . . . . . . . . .772
ADC_CR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .765
ADC_DIFSEL . . . . . . . . . . . . . . . . . . . . . . . . .786
ADC_DR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .781
ADC_IER  . . . . . . . . . . . . . . . . . . . . . . . . . . . .763
ADC_ISR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .761
ADC_JDRy . . . . . . . . . . . . . . . . . . . . . . . . . . .785
ADC_JSQR  . . . . . . . . . . . . . . . . . . . . . . . . . .782
ADC_OFRy  . . . . . . . . . . . . . . . . . . . . . . . . . .784
ADC_SMPR1 . . . . . . . . . . . . . . . . . . . . . . . . .774
ADC_SMPR2 . . . . . . . . . . . . . . . . . . . . . . . . .775
ADC_SQR1  . . . . . . . . . . . . . . . . . . . . . . . . . .778
ADC_SQR2  . . . . . . . . . . . . . . . . . . . . . . . . . .779
ADC_SQR3  . . . . . . . . . . . . . . . . . . . . . . . . . .780
ADC_SQR4  . . . . . . . . . . . . . . . . . . . . . . . . . .781
ADC_TR1 . . . . . . . . . . . . . . . . . . . . . . . . . . . .776
ADC_TR2 . . . . . . . . . . . . . . . . . . . . . . . . . . . .776
ADC_TR3 . . . . . . . . . . . . . . . . . . . . . . . . . . . .777
ADCx_CCR  . . . . . . . . . . . . . . . . . . . . . . . . . .789
ADCx_CDR  . . . . . . . . . . . . . . . . . . . . . . . . . .792
ADCx_CSR  . . . . . . . . . . . . . . . . . . . . . . . . . .787
AES_CR . . . . . . . . . . . . . . . . . . . . . . . . . . . . .989
AES_DINR . . . . . . . . . . . . . . . . . . . . . . . . . . .993
AES_DOUTR . . . . . . . . . . . . . . . . . . . . . . . . .993
AES_IVR0  . . . . . . . . . . . . . . . . . . . . . . . . . . .995
AES_IVR1  . . . . . . . . . . . . . . . . . . . . . . . . . . .996
AES_IVR2  . . . . . . . . . . . . . . . . . . . . . . . . . . .996
AES_IVR3  . . . . . . . . . . . . . . . . . . . . . . . . . . .996
AES_KEYR0  . . . . . . . . . . . . . . . . . . . . . . . . .994
AES_KEYR1  . . . . . . . . . . . . . . . . . . . . . . . . .994
AES_KEYR2  . . . . . . . . . . . . . . . . . . . . . . . . .995
AES_KEYR3  . . . . . . . . . . . . . . . . . . . . . . . . .995
AES_KEYR4  . . . . . . . . . . . . . . . . . . . . . . . . .997
AES_KEYR5  . . . . . . . . . . . . . . . . . . . . . . . . .997
AES_KEYR6  . . . . . . . . . . . . . . . . . . . . . . . . .997
AES_KEYR7  . . . . . . . . . . . . . . . . . . . . . . . . .998
AES_SR . . . . . . . . . . . . . . . . . . . . . . . . . . . . .991
AES_SUSPxR  . . . . . . . . . . . . . . . . . . . . . . . .998
AP_BASER  . . . . . . . . . . . . . . . . . . . . . . . . .2027
AP_BDnR . . . . . . . . . . . . . . . . . . . . . . . . . . .2026
AP_CFGR  . . . . . . . . . . . . . . . . . . . . . . . . . .2026
AP_CSWR . . . . . . . . . . . . . . . . . . . . . . . . . .2024
AP_DRWR . . . . . . . . . . . . . . . . . . . . . . . . . .2025
AP_IDR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2027
AP_TAR  . . . . . . . . . . . . . . . . . . . . . . . . . . . 2025
B
BPU_CIDR0  . . . . . . . . . . . . . . . . . . . . . . . . 2078
BPU_CIDR1  . . . . . . . . . . . . . . . . . . . . . . . . 2079
BPU_CIDR2  . . . . . . . . . . . . . . . . . . . . . . . . 2079
BPU_CIDR3  . . . . . . . . . . . . . . . . . . . . . . . . 2080
BPU_COMPxR  . . . . . . . . . . . . . . . . . . . . . . 2074
BPU_CTRLR . . . . . . . . . . . . . . . . . . . . . . . . 2074
BPU_DEVARCHR . . . . . . . . . . . . . . . . . . . . 2075
BPU_DEVTYPER  . . . . . . . . . . . . . . . . . . . . 2075
BPU_PIDR0  . . . . . . . . . . . . . . . . . . . . . . . . 2076
BPU_PIDR1  . . . . . . . . . . . . . . . . . . . . . . . . 2077
BPU_PIDR2  . . . . . . . . . . . . . . . . . . . . . . . . 2077
BPU_PIDR3  . . . . . . . . . . . . . . . . . . . . . . . . 2078
BPU_PIDR4  . . . . . . . . . . . . . . . . . . . . . . . . 2076
C
C1ROM_CIDR3 . . . . . . . . . . . . . . . . . 2037, 2043
COMP1_CSR  . . . . . . . . . . . . . . . . . . . . . . . . 843
COMP2_CSR  . . . . . . . . . . . . . . . . . . . . . . . . 845
CPUROM_CIDR0  . . . . . . . . . . . . . . . . . . . . 2041
CPUROM_CIDR1  . . . . . . . . . . . . . . . . . . . . 2041
CPUROM_CIDR2  . . . . . . . . . . . . . . . . . . . . 2042
CPUROM_CIDR3  . . . . . . . . . . . . . . . . . . . . 2042
CPUROM_MEMTYPER  . . . . . . . . . . . . . . . 2038
CPUROM_PIDR0  . . . . . . . . . . . . . . . . . . . . 2039
CPUROM_PIDR1  . . . . . . . . . . . . . . . . . . . . 2039
CPUROM_PIDR2  . . . . . . . . . . . . . . . . . . . . 2040
CPUROM_PIDR3  . . . . . . . . . . . . . . . . . . . . 2040
CPUROM_PIDR4  . . . . . . . . . . . . . . . . . . . . 2038
CRC_CR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 567
CRC_DR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 566
CRC_IDR  . . . . . . . . . . . . . . . . . . . . . . . . . . . 566
CRC_INIT  . . . . . . . . . . . . . . . . . . . . . . . . . . . 568
CRC_POL . . . . . . . . . . . . . . . . . . . . . . . . . . . 568
CRS_CFGR . . . . . . . . . . . . . . . . . . . . . . . . . . 430
CRS_CR  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 429
CRS_ICR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 433
CRS_ISR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 431
CTI_APPCLEAR . . . . . . . . . . . . . . . . . . . . . 2130
CTI_APPPULSER . . . . . . . . . . . . . . . . . . . . 2130
CTI_APPSETR  . . . . . . . . . . . . . . . . . . . . . . 2129
CTI_CHINSTSR  . . . . . . . . . . . . . . . . . . . . . 2133
CTI_CHOUTSTSR  . . . . . . . . . . . . . . . . . . . 2133
CTI_CIDR0  . . . . . . . . . . . . . . . . . . . . . . . . . 2138

RM0438 Index
RM0438 Rev 8 2179/2187
CTI_CIDR1 . . . . . . . . . . . . . . . . . . . . . . . . . .2138
CTI_CIDR2 . . . . . . . . . . . . . . . . . . . . . . . . . .2139
CTI_CIDR3 . . . . . . . . . . . . . . . . . . . . . . . . . .2139
CTI_CONTROLR . . . . . . . . . . . . . . . . . . . . .2128
CTI_DEVIDR  . . . . . . . . . . . . . . . . . . . . . . . .2134
CTI_DEVTYPER  . . . . . . . . . . . . . . . . . . . . .2135
CTI_GATER . . . . . . . . . . . . . . . . . . . . . . . . .2134
CTI_INENxR  . . . . . . . . . . . . . . . . . . . . . . . .2131
CTI_INTACKR  . . . . . . . . . . . . . . . . . . . . . . .2128
CTI_OUTENxR  . . . . . . . . . . . . . . . . . . . . . .2131
CTI_PIDR0 . . . . . . . . . . . . . . . . . . . . . . . . . .2136
CTI_PIDR1 . . . . . . . . . . . . . . . . . . . . . . . . . .2136
CTI_PIDR2 . . . . . . . . . . . . . . . . . . . . . . . . . .2137
CTI_PIDR3 . . . . . . . . . . . . . . . . . . . . . . . . . .2137
CTI_PIDR4 . . . . . . . . . . . . . . . . . . . . . . . . . .2135
CTI_TRGISTSR . . . . . . . . . . . . . . . . . . . . . .2132
CTI_TRGOSTSR . . . . . . . . . . . . . . . . . . . . .2132
D
DAC_CCR  . . . . . . . . . . . . . . . . . . . . . . . . . . .827
DAC_CR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .816
DAC_DHR12L1  . . . . . . . . . . . . . . . . . . . . . . .821
DAC_DHR12L2  . . . . . . . . . . . . . . . . . . . . . . .822
DAC_DHR12LD . . . . . . . . . . . . . . . . . . . . . . .824
DAC_DHR12R1 . . . . . . . . . . . . . . . . . . . . . . .820
DAC_DHR12R2 . . . . . . . . . . . . . . . . . . . . . . .822
DAC_DHR12RD . . . . . . . . . . . . . . . . . . . . . . .823
DAC_DHR8R1 . . . . . . . . . . . . . . . . . . . . . . . .821
DAC_DHR8R2 . . . . . . . . . . . . . . . . . . . . . . . .823
DAC_DHR8RD . . . . . . . . . . . . . . . . . . . . . . . .824
DAC_DOR1  . . . . . . . . . . . . . . . . . . . . . . . . . .825
DAC_DOR2  . . . . . . . . . . . . . . . . . . . . . . . . . .825
DAC_MCR . . . . . . . . . . . . . . . . . . . . . . . . . . .827
DAC_SHHR . . . . . . . . . . . . . . . . . . . . . . . . . .829
DAC_SHRR . . . . . . . . . . . . . . . . . . . . . . . . . .830
DAC_SHSR1  . . . . . . . . . . . . . . . . . . . . . . . . .829
DAC_SHSR2  . . . . . . . . . . . . . . . . . . . . . . . . .829
DAC_SR . . . . . . . . . . . . . . . . . . . . . . . . . . . . .825
DAC_SWTRGR  . . . . . . . . . . . . . . . . . . . . . . .820
DBGMCU_APB1LFZR . . . . . . . . . . . . . . . . .2145
DBGMCU_APB2FZR . . . . . . . . . . . . . . . . . .2147
DBGMCU_CR  . . . . . . . . . . . . . . . . . . . . . . .2143
DBGMCU_IDCODE . . . . . . . . . . . . . . . . . . .2143
DFSDM_CHyAWSCDR . . . . . . . . . . . . . . . . .895
DFSDM_CHyCFGR1 . . . . . . . . . . . . . . . . . . .892
DFSDM_CHyCFGR2 . . . . . . . . . . . . . . . . . . .894
DFSDM_CHyDATINR  . . . . . . . . . . . . . . . . . .896
DFSDM_CHyDLYR  . . . . . . . . . . . . . . . . . . . .897
DFSDM_CHyWDATR  . . . . . . . . . . . . . . . . . .896
DFSDM_FLTxAWCFR . . . . . . . . . . . . . . . . . .910
DFSDM_FLTxAWHTR . . . . . . . . . . . . . . . . . .908
DFSDM_FLTxAWLTR . . . . . . . . . . . . . . . . . . 908
DFSDM_FLTxAWSR . . . . . . . . . . . . . . . . . . . 909
DFSDM_FLTxCNVTIMR . . . . . . . . . . . . . . . . 911
DFSDM_FLTxCR1  . . . . . . . . . . . . . . . . . . . . 898
DFSDM_FLTxCR2  . . . . . . . . . . . . . . . . . . . . 901
DFSDM_FLTxEXMAX . . . . . . . . . . . . . . . . . . 910
DFSDM_FLTxEXMIN  . . . . . . . . . . . . . . . . . . 911
DFSDM_FLTxFCR  . . . . . . . . . . . . . . . . . . . . 905
DFSDM_FLTxICR . . . . . . . . . . . . . . . . . . . . . 904
DFSDM_FLTxISR . . . . . . . . . . . . . . . . . . . . . 902
DFSDM_FLTxJCHGR . . . . . . . . . . . . . . . . . . 905
DFSDM_FLTxJDATAR . . . . . . . . . . . . . . . . . 906
DFSDM_FLTxRDATAR . . . . . . . . . . . . . . . . . 907
DGBMCU_APB1HFZR  . . . . . . . . . . . . . . . . 2146
DMA_CCRx . . . . . . . . . . . . . . . . . . . . . . . . . . 495
DMA_CM0ARx  . . . . . . . . . . . . . . . . . . . 501 -502
DMA_CNDTRx  . . . . . . . . . . . . . . . . . . . . . . . 500
DMA_CPARx . . . . . . . . . . . . . . . . . . . . . . . . . 501
DMA_IFCR  . . . . . . . . . . . . . . . . . . . . . . . . . . 494
DMA_ISR  . . . . . . . . . . . . . . . . . . . . . . . . . . . 490
DMAMUX_CCFR  . . . . . . . . . . . . . . . . . . . . . 520
DMAMUX_CSR . . . . . . . . . . . . . . . . . . . . . . . 520
DMAMUX_CxCR . . . . . . . . . . . . . . . . . . . . . . 519
DMAMUX_RGCFR  . . . . . . . . . . . . . . . . . . . . 523
DMAMUX_RGSR  . . . . . . . . . . . . . . . . . . . . . 522
DMAMUX_RGxCR  . . . . . . . . . . . . . . . . . . . . 521
DP_ABORTR  . . . . . . . . . . . . . . . . . . . . . . . 2016
DP_CTRL/STATR . . . . . . . . . . . . . . . . . . . . 2017
DP_DLCR  . . . . . . . . . . . . . . . . . . . . . . . . . . 2018
DP_DLPIDR  . . . . . . . . . . . . . . . . . . . . . . . . 2019
DP_DPIDR  . . . . . . . . . . . . . . . . . . . . . . . . . 2015
DP_EVENTSTATR  . . . . . . . . . . . . . . . . . . . 2020
DP_RDBUFFR  . . . . . . . . . . . . . . . . . . . . . . 2021
DP_RESENDR  . . . . . . . . . . . . . . . . . . . . . . 2020
DP_SELECTR . . . . . . . . . . . . . . . . . . . . . . . 2020
DP_TARGETIDR . . . . . . . . . . . . . . . . . . . . . 2019
DWT_CIDR0 . . . . . . . . . . . . . . . . . . . . . . . . 2057
DWT_CIDR1 . . . . . . . . . . . . . . . . . . . . . . . . 2058
DWT_CIDR2 . . . . . . . . . . . . . . . . . . . . . . . . 2058
DWT_CIDR3 . . . . . . . . . . . . . . . . . . . . . . . . 2059
DWT_COMPxR . . . . . . . . . . . . . . . . . . . . . . 2049
DWT_CPICNTR  . . . . . . . . . . . . . . . . . . . . . 2047
DWT_CTRLR  . . . . . . . . . . . . . . . . . . . . . . . 2045
DWT_CYCCNTR . . . . . . . . . . . . . . . . . . . . . 2046
DWT_DEVARCHR  . . . . . . . . . . . . . . . . . . . 2054
DWT_DEVTYPER . . . . . . . . . . . . . . . . . . . . 2054
DWT_EXCCNTR . . . . . . . . . . . . . . . . . . . . . 2047
DWT_FOLDCNTR . . . . . . . . . . . . . . . . . . . . 2048
DWT_FUNCTR0 . . . . . . . . . . . . . . . . . . . . . 2050
DWT_FUNCTR1 . . . . . . . . . . . . . . . . . . . . . 2051
DWT_FUNCTR2 . . . . . . . . . . . . . . . . . . . . . 2052
DWT_FUNCTR3 . . . . . . . . . . . . . . . . . . . . . 2053

Index RM0438
2180/2187 RM0438 Rev 8
DWT_LSUCNTR  . . . . . . . . . . . . . . . . . . . . .2048
DWT_PCSR . . . . . . . . . . . . . . . . . . . . . . . . .2049
DWT_PIDR0  . . . . . . . . . . . . . . . . . . . . . . . .2055
DWT_PIDR1  . . . . . . . . . . . . . . . . . . . . . . . .2056
DWT_PIDR2  . . . . . . . . . . . . . . . . . . . . . . . .2056
DWT_PIDR3  . . . . . . . . . . . . . . . . . . . . . . . .2057
DWT_PIDR4  . . . . . . . . . . . . . . . . . . . . . . . .2055
DWT_SLPCNTR  . . . . . . . . . . . . . . . . . . . . .2048
E
ETM_AUTHSTATR  . . . . . . . . . . . . . . . . . . .2102
ETM_CCCTLR . . . . . . . . . . . . . . . . . . . . . . .2087
ETM_CIDR0 . . . . . . . . . . . . . . . . . . . . . . . . .2106
ETM_CIDR1 . . . . . . . . . . . . . . . . . . . . . . . . .2107
ETM_CIDR2 . . . . . . . . . . . . . . . . . . . . . . . . .2107
ETM_CIDR3 . . . . . . . . . . . . . . . . . . . . . . . . .2108
ETM_CLAIMCLR . . . . . . . . . . . . . . . . . . . . .2101
ETM_CLAIMSETR . . . . . . . . . . . . . . . . . . . .2101
ETM_CNTRLDVR0  . . . . . . . . . . . . . . . . . . .2089
ETM_CONFIGR . . . . . . . . . . . . . . . . . . . . . .2084
ETM_DEVARCHR . . . . . . . . . . . . . . . . . . . .2103
ETM_DEVTYPER  . . . . . . . . . . . . . . . . . . . .2103
ETM_EVENTCTL0R  . . . . . . . . . . . . . . . . . .2084
ETM_EVENTCTL1R  . . . . . . . . . . . . . . . . . .2085
ETM_IDR0 . . . . . . . . . . . . . . . . . . . . . . . . . .2092
ETM_IDR1 . . . . . . . . . . . . . . . . . . . . . . . . . .2093
ETM_IDR10 . . . . . . . . . . . . . . . . . . . . . . . . .2090
ETM_IDR11 . . . . . . . . . . . . . . . . . . . . . . . . .2090
ETM_IDR12 . . . . . . . . . . . . . . . . . . . . . . . . .2091
ETM_IDR13 . . . . . . . . . . . . . . . . . . . . . . . . .2091
ETM_IDR2 . . . . . . . . . . . . . . . . . . . . . . . . . .2093
ETM_IDR3 . . . . . . . . . . . . . . . . . . . . . . . . . .2094
ETM_IDR4 . . . . . . . . . . . . . . . . . . . . . . . . . .2095
ETM_IDR5 . . . . . . . . . . . . . . . . . . . . . . . . . .2096
ETM_IDR8 . . . . . . . . . . . . . . . . . . . . . . . . . .2089
ETM_IDR9 . . . . . . . . . . . . . . . . . . . . . . . . . .2090
ETM_IMSPECR0 . . . . . . . . . . . . . . . . . . . . .2091
ETM_PDCR . . . . . . . . . . . . . . . . . . . . . . . . .2100
ETM_PDSR  . . . . . . . . . . . . . . . . . . . . . . . . .2100
ETM_PIDR0 . . . . . . . . . . . . . . . . . . . . . . . . .2104
ETM_PIDR1 . . . . . . . . . . . . . . . . . . . . . . . . .2105
ETM_PIDR2 . . . . . . . . . . . . . . . . . . . . . . . . .2105
ETM_PIDR3 . . . . . . . . . . . . . . . . . . . . . . . . .2106
ETM_PIDR4 . . . . . . . . . . . . . . . . . . . . . . . . .2104
ETM_PRGCTLR  . . . . . . . . . . . . . . . . . . . . .2083
ETM_RSCTLR2 . . . . . . . . . . . . . . . . . . . . . .2097
ETM_RSCTLR3 . . . . . . . . . . . . . . . . . . . . . .2097
ETM_SSCCR0 . . . . . . . . . . . . . . . . . . . . . . .2098
ETM_SSCSR0 . . . . . . . . . . . . . . . . . . . . . . .2099
ETM_SSPCICR0  . . . . . . . . . . . . . . . . . . . . .2099
ETM_STALLCTLR . . . . . . . . . . . . . . . . . . . .2086
ETM_STATR . . . . . . . . . . . . . . . . . . . . . . . . 2083
ETM_SYNCPR  . . . . . . . . . . . . . . . . . . . . . . 2087
ETM_TRACEIDR  . . . . . . . . . . . . . . . . . . . . 2088
ETM_VICTLR  . . . . . . . . . . . . . . . . . . . . . . . 2088
EXTI_EMR1  . . . . . . . . . . . . . . . . . . . . . . . . . 558
EXTI_EMR2  . . . . . . . . . . . . . . . . . . . . . . . . . 559
EXTI_EXTICRn . . . . . . . . . . . . . . . . . . . . . . . 554
EXTI_FPR1 . . . . . . . . . . . . . . . . . . . . . . . . . . 547
EXTI_FPR2 . . . . . . . . . . . . . . . . . . . . . . . . . . 552
EXTI_FTSR1 . . . . . . . . . . . . . . . . . . . . . . . . . 544
EXTI_FTSR2 . . . . . . . . . . . . . . . . . . . . . . . . . 550
EXTI_IMR1  . . . . . . . . . . . . . . . . . . . . . . . . . . 557
EXTI_IMR2  . . . . . . . . . . . . . . . . . . . . . . . . . . 559
EXTI_LOCKRG . . . . . . . . . . . . . . . . . . . . . . . 557
EXTI_PRIVCFGR1  . . . . . . . . . . . . . . . . . . . . 549
EXTI_PRIVCFGR2  . . . . . . . . . . . . . . . . . . . . 553
EXTI_RPR1 . . . . . . . . . . . . . . . . . . . . . . . . . . 546
EXTI_RPR2 . . . . . . . . . . . . . . . . . . . . . . . . . . 551
EXTI_RTSR1 . . . . . . . . . . . . . . . . . . . . . . . . . 543
EXTI_RTSR2 . . . . . . . . . . . . . . . . . . . . . . . . . 549
EXTI_SECCFGR1 . . . . . . . . . . . . . . . . . . . . . 548
EXTI_SECCFGR2 . . . . . . . . . . . . . . . . . . . . . 553
EXTI_SWIER1 . . . . . . . . . . . . . . . . . . . . . . . . 545
EXTI_SWIER2 . . . . . . . . . . . . . . . . . . . . . . . . 551
F
FDCAN_CCCR  . . . . . . . . . . . . . . . . . . . . . . 1905
FDCAN_CKDIV . . . . . . . . . . . . . . . . . . . . . . 1930
FDCAN_CREL  . . . . . . . . . . . . . . . . . . . . . . 1902
FDCAN_DBTP  . . . . . . . . . . . . . . . . . . . . . . 1902
FDCAN_ECR  . . . . . . . . . . . . . . . . . . . . . . . 1910
FDCAN_ENDN  . . . . . . . . . . . . . . . . . . . . . . 1902
FDCAN_HPMS  . . . . . . . . . . . . . . . . . . . . . . 1921
FDCAN_IE . . . . . . . . . . . . . . . . . . . . . . . . . . 1916
FDCAN_ILE . . . . . . . . . . . . . . . . . . . . . . . . . 1919
FDCAN_ILS . . . . . . . . . . . . . . . . . . . . . . . . . 1918
FDCAN_IR  . . . . . . . . . . . . . . . . . . . . . . . . . 1913
FDCAN_NBTP  . . . . . . . . . . . . . . . . . . . . . . 1906
FDCAN_PSR . . . . . . . . . . . . . . . . . . . . . . . . 1911
FDCAN_RWD . . . . . . . . . . . . . . . . . . . . . . . 1904
FDCAN_RXF0A  . . . . . . . . . . . . . . . . . . . . . 1923
FDCAN_RXF0S  . . . . . . . . . . . . . . . . . . . . . 1922
FDCAN_RXF1A  . . . . . . . . . . . . . . . . . . . . . 1924
FDCAN_RXF1S  . . . . . . . . . . . . . . . . . . . . . 1923
FDCAN_RXGFC . . . . . . . . . . . . . . . . . . . . . 1919
FDCAN_TDCR  . . . . . . . . . . . . . . . . . . . . . . 1913
FDCAN_TEST . . . . . . . . . . . . . . . . . . . . . . . 1903
FDCAN_TOCC  . . . . . . . . . . . . . . . . . . . . . . 1909
FDCAN_TOCV  . . . . . . . . . . . . . . . . . . . . . . 1910
FDCAN_TSCC  . . . . . . . . . . . . . . . . . . . . . . 1908
FDCAN_TSCV  . . . . . . . . . . . . . . . . . . . . . . 1908

RM0438 Index
RM0438 Rev 8 2181/2187
FDCAN_TXBAR . . . . . . . . . . . . . . . . . . . . . .1926
FDCAN_TXBC . . . . . . . . . . . . . . . . . . . . . . .1924
FDCAN_TXBCF . . . . . . . . . . . . . . . . . . . . . .1928
FDCAN_TXBCIE  . . . . . . . . . . . . . . . . . . . . .1929
FDCAN_TXBCR . . . . . . . . . . . . . . . . . . . . . .1927
FDCAN_TXBRP . . . . . . . . . . . . . . . . . . . . . .1925
FDCAN_TXBTIE  . . . . . . . . . . . . . . . . . . . . .1928
FDCAN_TXBTO . . . . . . . . . . . . . . . . . . . . . .1927
FDCAN_TXEFA . . . . . . . . . . . . . . . . . . . . . .1930
FDCAN_TXEFS . . . . . . . . . . . . . . . . . . . . . .1929
FDCAN_TXFQS . . . . . . . . . . . . . . . . . . . . . .1925
FDCAN_XIDAM . . . . . . . . . . . . . . . . . . . . . .1921
FLASH_ACR  . . . . . . . . . . . . . . . . . . . . . . . . .213
FLASH_ECCR . . . . . . . . . . . . . . . . . . . . . . . .223
FLASH_LVEKEYR . . . . . . . . . . . . . . . . . . . . .216
FLASH_NSBOOTADD0R  . . . . . . . . . . . . . . .227
FLASH_NSBOOTADD1R  . . . . . . . . . . . . . . .228
FLASH_NSCR . . . . . . . . . . . . . . . . . . . . . . . .220
FLASH_NSKEYR . . . . . . . . . . . . . . . . . . . . . .215
FLASH_NSSR  . . . . . . . . . . . . . . . . . . . . . . . .217
FLASH_OPTKEYR  . . . . . . . . . . . . . . . . . . . .216
FLASH_OPTR  . . . . . . . . . . . . . . . . . . . . . . . .225
FLASH_PDKEYR . . . . . . . . . . . . . . . . . . . . . .214
FLASH_PRIVCFGR . . . . . . . . . . . . . . . . . . . .238
FLASH_SECBB1Rx . . . . . . . . . . . . . . . . . . . .237
FLASH_SECBB2Rx . . . . . . . . . . . . . . . . . . . .237
FLASH_SECBOOTADD0R  . . . . . . . . . . . . . .228
FLASH_SECCR . . . . . . . . . . . . . . . . . . . . . . .222
FLASH_SECHDPCR . . . . . . . . . . . . . . . . . . .238
FLASH_SECKEYR  . . . . . . . . . . . . . . . . . . . .215
FLASH_SECSR . . . . . . . . . . . . . . . . . . . . . . .218
FLASH_SECWM1R1 . . . . . . . . . . . . . . . . . . .229
FLASH_SECWM1R2 . . . . . . . . . . . . . . . . . . .230
FLASH_SECWM2R1 . . . . . . . . . . . . . . . . . . .233
FLASH_SECWM2R2 . . . . . . . . . . . . . . . . . . .234
FLASH_WRP1AR  . . . . . . . . . . . . . . . . . . . . .231
FLASH_WRP1BR  . . . . . . . . . . . . . . . . . . . . .232
FLASH_WRP2AR  . . . . . . . . . . . . . . . . . . . . .235
FLASH_WRP2BR  . . . . . . . . . . . . . . . . . . . . .236
FMC_BCRx  . . . . . . . . . . . . . . . . . . . . . . . . . .605
FMC_BTRx  . . . . . . . . . . . . . . . . . . . . . . . . . .607
FMC_BWTRx . . . . . . . . . . . . . . . . . . . . . . . . .610
FMC_ECCR . . . . . . . . . . . . . . . . . . . . . . . . . .623
FMC_PATT  . . . . . . . . . . . . . . . . . . . . . . . . . .622
FMC_PCR  . . . . . . . . . . . . . . . . . . . . . . . . . . .618
FMC_PCSCNTR  . . . . . . . . . . . . . . . . . . . . . .612
FMC_PMEM . . . . . . . . . . . . . . . . . . . . . . . . . .621
FMC_SR  . . . . . . . . . . . . . . . . . . . . . . . . . . . .620
G
GPIOx_AFRH . . . . . . . . . . . . . . . . . . . . . . . . .451
GPIOx_AFRL  . . . . . . . . . . . . . . . . . . . . . . . . 450
GPIOx_BRR  . . . . . . . . . . . . . . . . . . . . . . . . . 452
GPIOx_BSRR  . . . . . . . . . . . . . . . . . . . . . . . . 448
GPIOx_IDR . . . . . . . . . . . . . . . . . . . . . . . . . . 448
GPIOx_LCKR  . . . . . . . . . . . . . . . . . . . . . . . . 449
GPIOx_MODER  . . . . . . . . . . . . . . . . . . . . . . 446
GPIOx_ODR  . . . . . . . . . . . . . . . . . . . . . . . . . 448
GPIOx_OSPEEDR  . . . . . . . . . . . . . . . . . . . . 447
GPIOx_OTYPER . . . . . . . . . . . . . . . . . . . . . . 446
GPIOx_PUPDR . . . . . . . . . . . . . . . . . . . . . . . 447
GTZC_MPCBB1_LCKVTR1  . . . . . . . . . . . . . 151
GTZC_MPCBB2_LCKVTR1  . . . . . . . . . . . . . 151
GTZC_MPCBBx_CR . . . . . . . . . . . . . . . . . . . 150
GTZC_MPCBBx_VCTRy  . . . . . . . . . . . . . . . 152
GTZC_TZIC_FCR1 . . . . . . . . . . . . . . . . . . . . 166
GTZC_TZIC_FCR2 . . . . . . . . . . . . . . . . . . . . 169
GTZC_TZIC_FCR3 . . . . . . . . . . . . . . . . . . . . 171
GTZC_TZIC_IER1 . . . . . . . . . . . . . . . . . . . . . 154
GTZC_TZIC_IER2 . . . . . . . . . . . . . . . . . . . . . 157
GTZC_TZIC_IER3 . . . . . . . . . . . . . . . . . . . . . 159
GTZC_TZIC_SR1  . . . . . . . . . . . . . . . . . . . . . 160
GTZC_TZIC_SR2  . . . . . . . . . . . . . . . . . . . . . 163
GTZC_TZIC_SR3  . . . . . . . . . . . . . . . . . . . . . 165
GTZC_TZSC_CR  . . . . . . . . . . . . . . . . . . . . . 136
GTZC_TZSC_MPCWMxANSR . . . . . . . . . . . 147
GTZC_TZSC_MPCWMxBNSR . . . . . . . . . . . 147
GTZC_TZSC_PRIVCFGR1 . . . . . . . . . . . . . . 142
GTZC_TZSC_PRIVCFGR2 . . . . . . . . . . . . . . 145
GTZC_TZSC_SECCFGR1  . . . . . . . . . . . . . . 137
GTZC_TZSC_SECCFGR2  . . . . . . . . . . . . . . 140
H
HASH_CR . . . . . . . . . . . . . . . . . . . . . . . . . . 1014
HASH_CSRx . . . . . . . . . . . . . . . . . . . . . . . . 1021
HASH_DIN  . . . . . . . . . . . . . . . . . . . . . . . . . 1016
HASH_HRAx . . . . . . . . . . . . . . . . . . . . . . . . 1018
HASH_HRx . . . . . . . . . . . . . . . . . . . . 1018 -1019
HASH_IMR  . . . . . . . . . . . . . . . . . . . . . . . . . 1019
HASH_SR . . . . . . . . . . . . . . . . . . . . . . . . . . 1020
HASH_STR . . . . . . . . . . . . . . . . . . . . . . . . . 1017
I
I2C_CR1  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1533
I2C_CR2  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1536
I2C_ICR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1544
I2C_ISR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1541
I2C_OAR1 . . . . . . . . . . . . . . . . . . . . . . . . . . 1538
I2C_OAR2 . . . . . . . . . . . . . . . . . . . . . . . . . . 1538
I2C_PECR . . . . . . . . . . . . . . . . . . . . . . . . . . 1545
I2C_RXDR . . . . . . . . . . . . . . . . . . . . . . . . . . 1545
I2C_TIMEOUTR  . . . . . . . . . . . . . . . . . . . . . 1540

Index RM0438
2182/2187 RM0438 Rev 8
I2C_TIMINGR  . . . . . . . . . . . . . . . . . . . . . . .1539
I2C_TXDR  . . . . . . . . . . . . . . . . . . . . . . . . . .1546
ICACHE_CR  . . . . . . . . . . . . . . . . . . . . . . . . .253
ICACHE_CRRx  . . . . . . . . . . . . . . . . . . . . . . .256
ICACHE_FCR  . . . . . . . . . . . . . . . . . . . . . . . .255
ICACHE_HMONR  . . . . . . . . . . . . . . . . . . . . .256
ICACHE_IER  . . . . . . . . . . . . . . . . . . . . . . . . .255
ICACHE_MMONR  . . . . . . . . . . . . . . . . . . . . .256
ICACHE_SR . . . . . . . . . . . . . . . . . . . . . . . . . .254
ITM_CIDR0  . . . . . . . . . . . . . . . . . . . . . . . . .2069
ITM_CIDR1  . . . . . . . . . . . . . . . . . . . . . . . . .2070
ITM_CIDR2  . . . . . . . . . . . . . . . . . . . . . . . . .2070
ITM_CIDR3  . . . . . . . . . . . . . . . . . . . . . . . . .2071
ITM_DEVARCHR . . . . . . . . . . . . . . . . . . . . .2066
ITM_DEVTYPER  . . . . . . . . . . . . . . . . . . . . .2066
ITM_PIDR0  . . . . . . . . . . . . . . . . . . . . . . . . .2067
ITM_PIDR1  . . . . . . . . . . . . . . . . . . . . . . . . .2068
ITM_PIDR2  . . . . . . . . . . . . . . . . . . . . . . . . .2068
ITM_PIDR3  . . . . . . . . . . . . . . . . . . . . . . . . .2069
ITM_PIDR4  . . . . . . . . . . . . . . . . . . . . . . . . .2067
ITM_STIMRx  . . . . . . . . . . . . . . . . . . . . . . . .2063
ITM_TCR  . . . . . . . . . . . . . . . . . . . . . . . . . . .2064
ITM_TER  . . . . . . . . . . . . . . . . . . . . . . . . . . .2063
ITM_TPR  . . . . . . . . . . . . . . . . . . . . . . . . . . .2064
IWDG_KR  . . . . . . . . . . . . . . . . . . . . . . . . . .1383
IWDG_PR  . . . . . . . . . . . . . . . . . . . . . . . . . .1384
IWDG_RLR  . . . . . . . . . . . . . . . . . . . . . . . . .1385
IWDG_SR  . . . . . . . . . . . . . . . . . . . . . . . . . .1386
IWDG_WINR  . . . . . . . . . . . . . . . . . . . . . . . .1387
L
LPTIM_ARR . . . . . . . . . . . . . . . . . . . . . . . . .1374
LPTIM_CFGR  . . . . . . . . . . . . . . . . . . . . . . .1370
LPTIM_CMP . . . . . . . . . . . . . . . . . . . . . . . . .1374
LPTIM_CNT . . . . . . . . . . . . . . . . . . . . . . . . .1375
LPTIM_CR . . . . . . . . . . . . . . . . . . . . . . . . . .1373
LPTIM_ICR  . . . . . . . . . . . . . . . . . . . . . . . . .1368
LPTIM_IER . . . . . . . . . . . . . . . . . . . . . . . . . .1369
LPTIM_ISR . . . . . . . . . . . . . . . . . . . . . . . . . .1367
LPTIM_RCR . . . . . . . . . . . . . . . . . . . . . . . . .1377
LPTIM1_OR . . . . . . . . . . . . . . . . . . . . . . . . .1375
LPTIM2_OR . . . . . . . . . . . . . . . . . . . . . . . . .1376
LPTIM3_OR . . . . . . . . . . . . . . . . . . . . . . . . .1376
LPUART_BRR . . . . . . . . . . . . . . . . . . . . . . .1675
LPUART_CR1  . . . . . . . . . . . . . . . . . .1664, 1667
LPUART_CR2  . . . . . . . . . . . . . . . . . . . . . . .1670
LPUART_CR3  . . . . . . . . . . . . . . . . . . . . . . .1672
LPUART_ICR . . . . . . . . . . . . . . . . . . . . . . . .1683
LPUART_ISR . . . . . . . . . . . . . . . . . . .1676, 1680
LPUART_PRESC . . . . . . . . . . . . . . . . . . . . .1685
LPUART_RDR . . . . . . . . . . . . . . . . . . . . . . .1684
LPUART_RQR  . . . . . . . . . . . . . . . . . . . . . . 1675
LPUART_TDR . . . . . . . . . . . . . . . . . . . . . . . 1684
M
MCUROM_CIDR0 . . . . . . . . . . . . . . . . . . . . 2035
MCUROM_CIDR1 . . . . . . . . . . . . . . . . . . . . 2035
MCUROM_CIDR2 . . . . . . . . . . . . . . . . . . . . 2036
MCUROM_CIDR3 . . . . . . . . . . . . . . . . . . . . 2036
MCUROM_MEMTYPER . . . . . . . . . . . . . . . 2032
MCUROM_PIDR0 . . . . . . . . . . . . . . . . . . . . 2033
MCUROM_PIDR1 . . . . . . . . . . . . . . . . . . . . 2033
MCUROM_PIDR2 . . . . . . . . . . . . . . . . . . . . 2034
MCUROM_PIDR3 . . . . . . . . . . . . . . . . . . . . 2034
MCUROM_PIDR4 . . . . . . . . . . . . . . . . . . . . 2032
O
OCTOSPI_ABR . . . . . . . . . . . . . . . . . . . . . . . 671
OCTOSPI_AR . . . . . . . . . . . . . . . . . . . . . . . . 665
OCTOSPI_CCR  . . . . . . . . . . . . . . . . . . . . . . 667
OCTOSPI_CR . . . . . . . . . . . . . . . . . . . . . . . . 657
OCTOSPI_DCR1  . . . . . . . . . . . . . . . . . . . . . 659
OCTOSPI_DCR2  . . . . . . . . . . . . . . . . . . . . . 661
OCTOSPI_DCR3  . . . . . . . . . . . . . . . . . . . . . 662
OCTOSPI_DCR4  . . . . . . . . . . . . . . . . . . . . . 662
OCTOSPI_DLR . . . . . . . . . . . . . . . . . . . . . . . 664
OCTOSPI_DR . . . . . . . . . . . . . . . . . . . . . . . . 665
OCTOSPI_FCR . . . . . . . . . . . . . . . . . . . . . . . 664
OCTOSPI_HLCR  . . . . . . . . . . . . . . . . . . . . . 679
OCTOSPI_IR . . . . . . . . . . . . . . . . . . . . . . . . . 670
OCTOSPI_LPTR . . . . . . . . . . . . . . . . . . . . . . 671
OCTOSPI_PIR  . . . . . . . . . . . . . . . . . . . . . . . 667
OCTOSPI_PSMAR . . . . . . . . . . . . . . . . . . . . 667
OCTOSPI_PSMKR . . . . . . . . . . . . . . . . . . . . 666
OCTOSPI_SR . . . . . . . . . . . . . . . . . . . . . . . . 663
OCTOSPI_TCR . . . . . . . . . . . . . . . . . . . . . . . 670
OCTOSPI_WABR . . . . . . . . . . . . . . . . . . . . . 678
OCTOSPI_WCCR . . . . . . . . . . . . . . . . . . . . . 675
OCTOSPI_WIR . . . . . . . . . . . . . . . . . . . . . . . 678
OCTOSPI_WPABR . . . . . . . . . . . . . . . . . . . . 675
OCTOSPI_WPCCR . . . . . . . . . . . . . . . . . . . . 672
OCTOSPI_WPIR . . . . . . . . . . . . . . . . . . . . . . 674
OCTOSPI_WPTCR . . . . . . . . . . . . . . . . . . . . 674
OCTOSPI_WTCR . . . . . . . . . . . . . . . . . . . . . 677
OPAMP1_CSR  . . . . . . . . . . . . . . . . . . . . . . . 857
OPAMP1_LPOTR . . . . . . . . . . . . . . . . . 858 -860
OPAMP1_OTR  . . . . . . . . . . . . . . . . . . . . . . . 858
OTFDEC_CR  . . . . . . . . . . . . . . . . . . . . . . . 1032
OTFDEC_ICR . . . . . . . . . . . . . . . . . . . . . . . 1040
OTFDEC_IER  . . . . . . . . . . . . . . . . . . . . . . . 1041
OTFDEC_ISR  . . . . . . . . . . . . . . . . . . . . . . . 1039
OTFDEC_PRIVCFGR . . . . . . . . . . . . . . . . . 1033

RM0438 Index
RM0438 Rev 8 2183/2187
OTFDEC_RxCFGR  . . . . . . . . . . . . . . . . . . .1033
OTFDEC_RxENDADDR  . . . . . . . . . . . . . . .1035
OTFDEC_RxKEYR0  . . . . . . . . . . . . . . . . . .1037
OTFDEC_RxKEYR1  . . . . . . . . . . . . . . . . . .1038
OTFDEC_RxKEYR2  . . . . . . . . . . . . . . . . . .1038
OTFDEC_RxKEYR3  . . . . . . . . . . . . . . . . . .1039
OTFDEC_RxNONCER0  . . . . . . . . . . . . . . .1036
OTFDEC_RxNONCER1  . . . . . . . . . . . . . . .1037
OTFDEC_RxSTARTADDR  . . . . . . . . . . . . .1035
P
PKA_CLRFR  . . . . . . . . . . . . . . . . . . . . . . . .1070
PKA_CR . . . . . . . . . . . . . . . . . . . . . . . . . . . .1068
PKA_SR . . . . . . . . . . . . . . . . . . . . . . . . . . . .1069
PWR_CR1  . . . . . . . . . . . . . . . . . . . . . . . . . . .299
PWR_CR2  . . . . . . . . . . . . . . . . . . . . . . . . . . .300
PWR_CR3  . . . . . . . . . . . . . . . . . . . . . . . . . . .301
PWR_CR4  . . . . . . . . . . . . . . . . . . . . . . . . . . .303
PWR_PDCRA  . . . . . . . . . . . . . . . . . . . . . . . .308
PWR_PDCRB  . . . . . . . . . . . . . . . . . . . . . . . .310
PWR_PDCRC  . . . . . . . . . . . . . . . . . . . . . . . .311
PWR_PDCRD  . . . . . . . . . . . . . . . . . . . . . . . .312
PWR_PDCRE  . . . . . . . . . . . . . . . . . . . . . . . .313
PWR_PDCRF  . . . . . . . . . . . . . . . . . . . . . . . .314
PWR_PDCRG  . . . . . . . . . . . . . . . . . . . . . . . .316
PWR_PDCRH  . . . . . . . . . . . . . . . . . . . . . . . .317
PWR_PRIVCFGR  . . . . . . . . . . . . . . . . . . . . .319
PWR_PUCRA  . . . . . . . . . . . . . . . . . . . . . . . .308
PWR_PUCRB  . . . . . . . . . . . . . . . . . . . . . . . .309
PWR_PUCRC  . . . . . . . . . . . . . . . . . . . . . . . .310
PWR_PUCRD  . . . . . . . . . . . . . . . . . . . . . . . .311
PWR_PUCRE  . . . . . . . . . . . . . . . . . . . . . . . .313
PWR_PUCRF  . . . . . . . . . . . . . . . . . . . . . . . .314
PWR_PUCRG  . . . . . . . . . . . . . . . . . . . . . . . .315
PWR_PUCRH  . . . . . . . . . . . . . . . . . . . . . . . .316
PWR_SCR . . . . . . . . . . . . . . . . . . . . . . . . . . .307
PWR_SECCFGR . . . . . . . . . . . . . . . . . . . . . .317
PWR_SR1  . . . . . . . . . . . . . . . . . . . . . . . . . . .304
PWR_SR2  . . . . . . . . . . . . . . . . . . . . . . . . . . .306
R
RCC_AHB1ENR  . . . . . . . . . . . . . . . . . . . . . .373
RCC_AHB1RSTR  . . . . . . . . . . . . . . . . . . . . .364
RCC_AHB1SECSR  . . . . . . . . . . . . . . . . . . . .407
RCC_AHB1SMENR . . . . . . . . . . . . . . . . . . . .382
RCC_AHB2ENR  . . . . . . . . . . . . . . . . . . . . . .374
RCC_AHB2RSTR  . . . . . . . . . . . . . . . . . . . . .365
RCC_AHB2SECSR  . . . . . . . . . . . . . . . . . . . .408
RCC_AHB2SMENR . . . . . . . . . . . . . . . . . . . .384
RCC_AHB3ENR  . . . . . . . . . . . . . . . . . . . . . .376
RCC_AHB3RSTR  . . . . . . . . . . . . . . . . . . . . .367
RCC_AHB3SECSR . . . . . . . . . . . . . . . . . . . . 410
RCC_AHB3SMENR  . . . . . . . . . . . . . . . . . . . 386
RCC_APB1ENR1  . . . . . . . . . . . . . . . . . . . . . 377
RCC_APB1ENR2  . . . . . . . . . . . . . . . . . . . . . 379
RCC_APB1RSTR1  . . . . . . . . . . . . . . . . . . . . 368
RCC_APB1RSTR2  . . . . . . . . . . . . . . . . . . . . 370
RCC_APB1SECSR1 . . . . . . . . . . . . . . . . . . . 411
RCC_APB1SECSR2 . . . . . . . . . . . . . . . . . . . 414
RCC_APB1SMENR1  . . . . . . . . . . . . . . . . . . 387
RCC_APB1SMENR2  . . . . . . . . . . . . . . . . . . 390
RCC_APB2ENR  . . . . . . . . . . . . . . . . . . . . . . 381
RCC_APB2RSTR  . . . . . . . . . . . . . . . . . . . . . 371
RCC_APB2SECSR . . . . . . . . . . . . . . . . . . . . 415
RCC_APB2SMENR  . . . . . . . . . . . . . . . . . . . 391
RCC_BDCR  . . . . . . . . . . . . . . . . . . . . . . . . . 395
RCC_CCIPR1 . . . . . . . . . . . . . . . . . . . . . . . . 393
RCC_CCIPR2 . . . . . . . . . . . . . . . . . . . . . . . . 401
RCC_CFGR  . . . . . . . . . . . . . . . . . . . . . . . . . 349
RCC_CICR  . . . . . . . . . . . . . . . . . . . . . . . . . . 363
RCC_CIER  . . . . . . . . . . . . . . . . . . . . . . . . . . 360
RCC_CIFR  . . . . . . . . . . . . . . . . . . . . . . . . . . 361
RCC_CR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345
RCC_CRRCR  . . . . . . . . . . . . . . . . . . . . . . . . 400
RCC_CSR . . . . . . . . . . . . . . . . . . . . . . . . . . . 398
RCC_DLYCFGR . . . . . . . . . . . . . . . . . . . . . . 402
RCC_ICSCR . . . . . . . . . . . . . . . . . . . . . . . . . 348
RCC_PLLCFGR  . . . . . . . . . . . . . . . . . . . . . . 352
RCC_PLLSAI1CFGR  . . . . . . . . . . . . . . . . . . 355
RCC_PLLSAI2CFGR  . . . . . . . . . . . . . . . . . . 358
RCC_SECCFGR . . . . . . . . . . . . . . . . . . . . . . 403
RCC_SECSR  . . . . . . . . . . . . . . . . . . . . . . . . 405
RNG_CR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 948
RNG_DR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 951
RNG_HTCR  . . . . . . . . . . . . . . . . . . . . . . . . . 952
RNG_SR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 950
RTC_ALRMAR  . . . . . . . . . . . . . . . . . . . . . . 1436
RTC_ALRMASSR . . . . . . . . . . . . . . . . . . . . 1438
RTC_ALRMBR  . . . . . . . . . . . . . . . . . . . . . . 1439
RTC_ALRMBSSR . . . . . . . . . . . . . . . . . . . . 1440
RTC_CALR . . . . . . . . . . . . . . . . . . . . . . . . . 1431
RTC_CR  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1424
RTC_DR  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1420
RTC_ICSR  . . . . . . . . . . . . . . . . . . . . . . . . . 1421
RTC_MISR  . . . . . . . . . . . . . . . . . . . . . . . . . 1442
RTC_PRER . . . . . . . . . . . . . . . . . . . . . . . . . 1423
RTC_PRIVCR . . . . . . . . . . . . . . . . . . . . . . . 1428
RTC_SCR . . . . . . . . . . . . . . . . . . . . . . . . . . 1444
RTC_SHIFTR  . . . . . . . . . . . . . . . . . . . . . . . 1433
RTC_SMCR  . . . . . . . . . . . . . . . . . . . . . . . . 1429
RTC_SMISR  . . . . . . . . . . . . . . . . . . . . . . . . 1443
RTC_SR  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1441
RTC_SSR  . . . . . . . . . . . . . . . . . . . . . . . . . . 1421

Index RM0438
2184/2187 RM0438 Rev 8
RTC_TR . . . . . . . . . . . . . . . . . . . . . . . . . . . .1419
RTC_TSDR  . . . . . . . . . . . . . . . . . . . . . . . . .1435
RTC_TSSSR  . . . . . . . . . . . . . . . . . . . . . . . .1436
RTC_TSTR  . . . . . . . . . . . . . . . . . . . . . . . . .1434
RTC_WPR . . . . . . . . . . . . . . . . . . . . . . . . . .1431
RTC_WUTR . . . . . . . . . . . . . . . . . . . . . . . . .1424
S
SAI_ACLRFR . . . . . . . . . . . . . . . . . . . . . . . .1773
SAI_ACR1  . . . . . . . . . . . . . . . . . . . . . . . . . .1762
SAI_ACR2  . . . . . . . . . . . . . . . . . . . . . . . . . .1765
SAI_ADR  . . . . . . . . . . . . . . . . . . . . . . . . . . .1774
SAI_AFRCR . . . . . . . . . . . . . . . . . . . . . . . . .1767
SAI_AIM . . . . . . . . . . . . . . . . . . . . . . . . . . . .1769
SAI_ASLOTR . . . . . . . . . . . . . . . . . . . . . . . .1768
SAI_ASR  . . . . . . . . . . . . . . . . . . . . . . . . . . .1771
SAI_BCLRFR . . . . . . . . . . . . . . . . . . . . . . . .1784
SAI_BCR1  . . . . . . . . . . . . . . . . . . . . . . . . . .1774
SAI_BCR2  . . . . . . . . . . . . . . . . . . . . . . . . . .1777
SAI_BDR  . . . . . . . . . . . . . . . . . . . . . . . . . . .1785
SAI_BFRCR . . . . . . . . . . . . . . . . . . . . . . . . .1779
SAI_BIM . . . . . . . . . . . . . . . . . . . . . . . . . . . .1781
SAI_BSLOTR . . . . . . . . . . . . . . . . . . . . . . . .1780
SAI_BSR  . . . . . . . . . . . . . . . . . . . . . . . . . . .1782
SAI_GCR . . . . . . . . . . . . . . . . . . . . . . . . . . .1762
SAI_PDMCR  . . . . . . . . . . . . . . . . . . . . . . . .1786
SAI_PDMDLY  . . . . . . . . . . . . . . . . . . . . . . .1787
SDMMC_ACKTIMER . . . . . . . . . . . . . . . . . .1863
SDMMC_ARGR . . . . . . . . . . . . . . . . . . . . . .1848
SDMMC_CLKCR . . . . . . . . . . . . . . . . . . . . .1846
SDMMC_CMDR . . . . . . . . . . . . . . . . . . . . . .1848
SDMMC_DCNTR . . . . . . . . . . . . . . . . . . . . .1854
SDMMC_DCTRL  . . . . . . . . . . . . . . . . . . . . .1853
SDMMC_DLENR . . . . . . . . . . . . . . . . . . . . .1852
SDMMC_DTIMER  . . . . . . . . . . . . . . . . . . . .1851
SDMMC_FIFORx . . . . . . . . . . . . . . . . . . . . .1865
SDMMC_ICR . . . . . . . . . . . . . . . . . . . . . . . .1858
SDMMC_IDMABASE0R  . . . . . . . . . . . . . . .1865
SDMMC_IDMABASE1R  . . . . . . . . . . . . . . .1865
SDMMC_IDMABSIZER  . . . . . . . . . . . . . . . .1864
SDMMC_IDMACTRLR . . . . . . . . . . . . . . . . .1863
SDMMC_MASKR . . . . . . . . . . . . . . . . . . . . .1860
SDMMC_POWER  . . . . . . . . . . . . . . . . . . . .1845
SDMMC_RESPCMDR . . . . . . . . . . . . . . . . .1850
SDMMC_RESPxR . . . . . . . . . . . . . . . . . . . .1851
SDMMC_STAR  . . . . . . . . . . . . . . . . . . . . . .1855
SPIx_CR1  . . . . . . . . . . . . . . . . . . . . . . . . . .1714
SPIx_CR2  . . . . . . . . . . . . . . . . . . . . . . . . . .1716
SPIx_CRCPR . . . . . . . . . . . . . . . . . . . . . . . .1720
SPIx_DR  . . . . . . . . . . . . . . . . . . . . . . . . . . .1719
SPIx_RXCRCR  . . . . . . . . . . . . . . . . . . . . . .1720
SPIx_SR  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1718
SPIx_TXCRCR  . . . . . . . . . . . . . . . . . . . . . . 1720
SYSCFG_CFGR1 . . . . . . . . . . . . . . . . . . . . . 459
SYSCFG_CFGR2 . . . . . . . . . . . . . . . . . . . . . 463
SYSCFG_CNSLCKR  . . . . . . . . . . . . . . . . . . 461
SYSCFG_CSLOCKR  . . . . . . . . . . . . . . . . . . 462
SYSCFG_FPUIMR  . . . . . . . . . . . . . . . . . . . . 461
SYSCFG_RSSCMDR . . . . . . . . . . . . . . . . . . 466
SYSCFG_SCSR  . . . . . . . . . . . . . . . . . . . . . . 464
SYSCFG_SECCFGR  . . . . . . . . . . . . . . . . . . 458
SYSCFG_SKR  . . . . . . . . . . . . . . . . . . . . . . . 465
SYSCFG_SWPR . . . . . . . . . . . . . . . . . . . . . . 465
SYSCFG_SWPR2 . . . . . . . . . . . . . . . . . . . . . 466
T
TAMP_BKPxR . . . . . . . . . . . . . . . . . . . . . . . 1480
TAMP_CFGR  . . . . . . . . . . . . . . . . . . . . . . . 1479
TAMP_COUNTR . . . . . . . . . . . . . . . . . . . . . 1479
TAMP_CR1 . . . . . . . . . . . . . . . . . . . . . . . . . 1456
TAMP_CR2 . . . . . . . . . . . . . . . . . . . . . . . . . 1458
TAMP_CR3 . . . . . . . . . . . . . . . . . . . . . . . . . 1461
TAMP_FLTCR . . . . . . . . . . . . . . . . . . . . . . . 1462
TAMP_IER  . . . . . . . . . . . . . . . . . . . . . . . . . 1472
TAMP_MISR . . . . . . . . . . . . . . . . . . . . . . . . 1475
TAMP_PRIVCR . . . . . . . . . . . . . . . . . . . . . . 1471
TAMP_SCR . . . . . . . . . . . . . . . . . . . . . . . . . 1477
TAMP_SMISR . . . . . . . . . . . . . . . . . . . . . . . 1476
TAMP_SR . . . . . . . . . . . . . . . . . . . . . . . . . . 1473
TIM1_OR1 . . . . . . . . . . . . . . . . . . . . . . . . . . 1162
TIM1_OR2 . . . . . . . . . . . . . . . . . . . . . . . . . . 1165
TIM1_OR3 . . . . . . . . . . . . . . . . . . . . . . . . . . 1167
TIM15_ARR . . . . . . . . . . . . . . . . . . . . . . . . . 1305
TIM15_BDTR  . . . . . . . . . . . . . . . . . . . . . . . 1307
TIM15_CCER  . . . . . . . . . . . . . . . . . . . . . . . 1302
TIM15_CCMR1 . . . . . . . . . . . . . . . . . 1298 -1299
TIM15_CCR1  . . . . . . . . . . . . . . . . . . . . . . . 1306
TIM15_CCR2  . . . . . . . . . . . . . . . . . . . . . . . 1307
TIM15_CNT . . . . . . . . . . . . . . . . . . . . . . . . . 1305
TIM15_CR1 . . . . . . . . . . . . . . . . . . . . . . . . . 1290
TIM15_CR2 . . . . . . . . . . . . . . . . . . . . . . . . . 1291
TIM15_DCR  . . . . . . . . . . . . . . . . . . . . . . . . 1310
TIM15_DIER  . . . . . . . . . . . . . . . . . . . . . . . . 1294
TIM15_DMAR  . . . . . . . . . . . . . . . . . . . . . . . 1310
TIM15_EGR  . . . . . . . . . . . . . . . . . . . . . . . . 1297
TIM15_OR1 . . . . . . . . . . . . . . . . . . . . . . . . . 1311
TIM15_OR2 . . . . . . . . . . . . . . . . . . . . . . . . . 1311
TIM15_PSC . . . . . . . . . . . . . . . . . . . . . . . . . 1305
TIM15_RCR  . . . . . . . . . . . . . . . . . . . . . . . . 1306
TIM15_SMCR  . . . . . . . . . . . . . . . . . . . . . . . 1293
TIM15_SR . . . . . . . . . . . . . . . . . . . . . . . . . . 1295
TIM16_OR1 . . . . . . . . . . . . . . . . . . . . . . . . . 1332

RM0438 Index
RM0438 Rev 8 2185/2187
TIM16_OR2  . . . . . . . . . . . . . . . . . . . . . . . . .1333
TIM17_OR1  . . . . . . . . . . . . . . . . . . . . . . . . .1334
TIM17_OR2  . . . . . . . . . . . . . . . . . . . . . . . . .1335
TIM2_OR1  . . . . . . . . . . . . . . . . . . . . . . . . . .1244
TIM2_OR2  . . . . . . . . . . . . . . . . . . . . . . . . . .1245
TIM3_OR1  . . . . . . . . . . . . . . . . . . . . . . . . . .1244
TIM3_OR2  . . . . . . . . . . . . . . . . . . . . . . . . . .1245
TIM8_OR1  . . . . . . . . . . . . . . . . . . . . . . . . . .1162
TIM8_OR2  . . . . . . . . . . . . . . . . . . . . . . . . . .1168
TIM8_OR3  . . . . . . . . . . . . . . . . . . . . . . . . . .1170
TIMx_ARR  . . . . . . . . . . 1153 , 1241, 1327, 1350
TIMx_BDTR . . . . . . . . . . . . . . . . . . . .1156, 1329
TIMx_CCER . . . . . . . . . . . . . . 1149 , 1238, 1324
TIMx_CCMR1  . . 1143-1144, 1232, 1234, 1321-
1322
TIMx_CCMR2  . . . . . . . . 1147 -1148, 1236-1237
TIMx_CCMR3  . . . . . . . . . . . . . . . . . . . . . . .1163
TIMx_CCR1 . . . . . . . . . . . . . . 1154 , 1241, 1328
TIMx_CCR2 . . . . . . . . . . . . . . . . . . . .1155, 1241
TIMx_CCR3 . . . . . . . . . . . . . . . . . . . .1155, 1242
TIMx_CCR4 . . . . . . . . . . . . . . . . . . . .1156, 1242
TIMx_CCR5 . . . . . . . . . . . . . . . . . . . . . . . . .1164
TIMx_CCR6 . . . . . . . . . . . . . . . . . . . . . . . . .1165
TIMx_CNT  . . . . . .1153, 1239-1240, 1326, 1349
TIMx_CR1  . . . . . . . . . . 1132 , 1223, 1316, 1346
TIMx_CR2  . . . . . . . . . . 1133 , 1224, 1317, 1348
TIMx_DCR . . . . . . . . . . . . . . . 1160 , 1243, 1331
TIMx_DIER . . . . . . . . . . 1138 , 1229, 1318, 1348
TIMx_DMAR . . . . . . . . . . . . . . 1161 , 1244, 1332
TIMx_EGR . . . . . . . . . . 1142 , 1231, 1320, 1349
TIMx_PSC  . . . . . . . . . . 1153 , 1240, 1327, 1350
TIMx_RCR . . . . . . . . . . . . . . . . . . . . .1154, 1328
TIMx_SMCR . . . . . . . . . . . . . . . . . . . .1136, 1226
TIMx_SR  . . . . . . . . . . . 1140 , 1230, 1319, 1349
TPIU_ACPR . . . . . . . . . . . . . . . . . . . . . . . . .2115
TPIU_CIDR0  . . . . . . . . . . . . . . . . . . . . . . . .2123
TPIU_CIDR1  . . . . . . . . . . . . . . . . . . . . . . . .2123
TPIU_CIDR2  . . . . . . . . . . . . . . . . . . . . . . . .2124
TPIU_CIDR3  . . . . . . . . . . . . . . . . . . . . . . . .2124
TPIU_CLAIMCLR . . . . . . . . . . . . . . . . . . . . .2118
TPIU_CLAIMSETR  . . . . . . . . . . . . . . . . . . .2118
TPIU_CSPSR . . . . . . . . . . . . . . . . . . . . . . . .2115
TPIU_DEVIDR . . . . . . . . . . . . . . . . . . . . . . .2119
TPIU_DEVTYPER  . . . . . . . . . . . . . . . . . . . .2120
TPIU_FFCR . . . . . . . . . . . . . . . . . . . . . . . . .2117
TPIU_FFSR  . . . . . . . . . . . . . . . . . . . . . . . . .2116
TPIU_PIDR0  . . . . . . . . . . . . . . . . . . . . . . . .2121
TPIU_PIDR1  . . . . . . . . . . . . . . . . . . . . . . . .2121
TPIU_PIDR2  . . . . . . . . . . . . . . . . . . . . . . . .2122
TPIU_PIDR3  . . . . . . . . . . . . . . . . . . . . . . . .2122
TPIU_PIDR4  . . . . . . . . . . . . . . . . . . . . . . . .2120
TPIU_PSCR . . . . . . . . . . . . . . . . . . . . . . . . .2117
TPIU_SPPR  . . . . . . . . . . . . . . . . . . . . . . . . 2115
TPIU_SSPSR  . . . . . . . . . . . . . . . . . . . . . . . 2114
TSC_CR  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 928
TSC_ICR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 932
TSC_IER . . . . . . . . . . . . . . . . . . . . . . . . . . . . 931
TSC_IOASCR . . . . . . . . . . . . . . . . . . . . . . . . 933
TSC_IOCCR  . . . . . . . . . . . . . . . . . . . . . . . . . 934
TSC_IOGCSR . . . . . . . . . . . . . . . . . . . . . . . . 935
TSC_IOGxCR  . . . . . . . . . . . . . . . . . . . . . . . . 935
TSC_IOHCR  . . . . . . . . . . . . . . . . . . . . . . . . . 933
TSC_IOSCR  . . . . . . . . . . . . . . . . . . . . . . . . . 934
TSC_ISR . . . . . . . . . . . . . . . . . . . . . . . . . . . . 932
U
UCPD_CFGR1  . . . . . . . . . . . . . . . . . . . . . . 1989
UCPD_CFGR2  . . . . . . . . . . . . . . . . . . . . . . 1991
UCPD_CR . . . . . . . . . . . . . . . . . . . . . . . . . . 1991
UCPD_ICR  . . . . . . . . . . . . . . . . . . . . . . . . . 1998
UCPD_IMR  . . . . . . . . . . . . . . . . . . . . . . . . . 1994
UCPD_RX_ORDEXTR1  . . . . . . . . . . . . . . . 2002
UCPD_RX_ORDEXTR2  . . . . . . . . . . . . . . . 2003
UCPD_RX_ORDSETR  . . . . . . . . . . . . . . . . 2000
UCPD_RX_PAYSZR . . . . . . . . . . . . . . . . . . 2001
UCPD_RXDR  . . . . . . . . . . . . . . . . . . . . . . . 2002
UCPD_SR . . . . . . . . . . . . . . . . . . . . . . . . . . 1995
UCPD_TX_ORDSETR  . . . . . . . . . . . . . . . . 1999
UCPD_TX_PAYSZR . . . . . . . . . . . . . . . . . . 1999
UCPD_TXDR  . . . . . . . . . . . . . . . . . . . . . . . 2000
USART_BRR . . . . . . . . . . . . . . . . . . . . . . . . 1615
USART_CR1 . . . . . . . . . . . . . . . . . . . 1600, 1603
USART_CR2 . . . . . . . . . . . . . . . . . . . . . . . . 1607
USART_CR3 . . . . . . . . . . . . . . . . . . . . . . . . 1611
USART_GTPR  . . . . . . . . . . . . . . . . . . . . . . 1615
USART_ICR  . . . . . . . . . . . . . . . . . . . . . . . . 1629
USART_ISR  . . . . . . . . . . . . . . . . . . . 1618, 1624
USART_PRESC  . . . . . . . . . . . . . . . . . . . . . 1632
USART_RDR  . . . . . . . . . . . . . . . . . . . . . . . 1631
USART_RQR  . . . . . . . . . . . . . . . . . . . . . . . 1617
USART_RTOR  . . . . . . . . . . . . . . . . . . . . . . 1616
USART_TDR . . . . . . . . . . . . . . . . . . . . . . . . 1631
USB_ADDRn_RX  . . . . . . . . . . . . . . . . . . . . 1964
USB_ADDRn_TX  . . . . . . . . . . . . . . . . . . . . 1963
USB_BCDR . . . . . . . . . . . . . . . . . . . . . . . . . 1957
USB_BTABLE . . . . . . . . . . . . . . . . . . . . . . . 1956
USB_CNTR . . . . . . . . . . . . . . . . . . . . . . . . . 1950
USB_COUNTn_RX . . . . . . . . . . . . . . . . . . . 1964
USB_COUNTn_TX  . . . . . . . . . . . . . . . . . . . 1963
USB_DADDR  . . . . . . . . . . . . . . . . . . . . . . . 1955
USB_EPnR  . . . . . . . . . . . . . . . . . . . . . . . . . 1958
USB_FNR  . . . . . . . . . . . . . . . . . . . . . . . . . . 1955
USB_ISTR . . . . . . . . . . . . . . . . . . . . . . . . . . 1952

Index RM0438
2186/2187 RM0438 Rev 8
USB_LPMCSR . . . . . . . . . . . . . . . . . . . . . . .1956
V
VREFBUF_CCR . . . . . . . . . . . . . . . . . . . . . . .836
VREFBUF_CSR . . . . . . . . . . . . . . . . . . . . . . .835
W
WWDG_CFR  . . . . . . . . . . . . . . . . . . . . . . . .1393
WWDG_CR  . . . . . . . . . . . . . . . . . . . . . . . . .1392
WWDG_SR  . . . . . . . . . . . . . . . . . . . . . . . . .1393

RM0438 Rev 8 2187/2187
RM0438
2187
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
* [Figure 1: Architectural Diagram](../figures/figure_1.md)
* [Figure 2: Architectural Diagram](../figures/figure_2.md)
* [Figure 8: Architectural Diagram](../figures/figure_8.md)
* [Figure 13: Architectural Diagram](../figures/figure_13.md)
* [Figure 18: Architectural Diagram](../figures/figure_18.md)
* [Figure 19: Architectural Diagram](../figures/figure_19.md)
* [Figure 20: Architectural Diagram](../figures/figure_20.md)
* [Figure 21: Architectural Diagram](../figures/figure_21.md)
* [Figure 22: Architectural Diagram](../figures/figure_22.md)
* [Figure 24: Architectural Diagram](../figures/figure_24.md)
* [Figure 25: Architectural Diagram](../figures/figure_25.md)
* [Figure 70: Architectural Diagram](../figures/figure_70.md)
* [Figure 71: Architectural Diagram](../figures/figure_71.md)
* [Figure 93: Architectural Diagram](../figures/figure_93.md)
* [Figure 94: Architectural Diagram](../figures/figure_94.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 1: Configuration Matrix](../tables/table_1.md)
* [Table 2: Configuration Matrix](../tables/table_2.md)
* [Table 3: Configuration Matrix](../tables/table_3.md)
* [Table 4: Configuration Matrix](../tables/table_4.md)
* [Table 7: Configuration Matrix](../tables/table_7.md)
* [Table 8: Configuration Matrix](../tables/table_8.md)
* [Table 10: Configuration Matrix](../tables/table_10.md)
* [Table 15: Configuration Matrix](../tables/table_15.md)
* [Table 16: Configuration Matrix](../tables/table_16.md)
* [Table 22: Configuration Matrix](../tables/table_22.md)
* [Table 28: Configuration Matrix](../tables/table_28.md)
* [Table 30: Configuration Matrix](../tables/table_30.md)
* [Table 31: Configuration Matrix](../tables/table_31.md)
* [Table 32: Configuration Matrix](../tables/table_32.md)
* [Table 33: Configuration Matrix](../tables/table_33.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)