# Chapter 33: Revision history

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32C0 Reference Manual RM0490 - Chapter 33: Revision history.
* **Document Source**: RM0490 Reference Manual
* **PDF Reference Location**: Pages 1019 - 1023
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0490 Ingestion)
```text
RM0490 Rev 6 1019/1023
RM0490 Revision history
1022
33 Revision history
[Table 180](../tables/table_180.md). Document revision history
Date Revision Changes
12-Apr-2022 1 Initial release.
21-Jul-2022 2
Section Fast programming - row size corrected.
[Table 18](../tables/table_18.md): Organization of option bytes now contains links to option registers
and the duplicated description is removed.
Format of reset values of option registers updated and/or corrected.
Note in bit 16 of FLASH security register (FLASH_SECR) updated.
Updated Section 18.3.18: Clearing the OCxREF signal on an external event.
OC1M[3:0] bitfield description updated in Section 18.4.8: TIMx
capture/compare mode register 1 [alternate] (TIMx_CCMR1)(x = 1, 8),
Section 19.4.8: TIMx capture/compare mode register 1 [alternate]
(TIMx_CCMR1) (x = 2 to 5), Section 20.5.6: TIMx capture/compare mode
register 1 [alternate] (TIMx_CCMR1)(x = 10, 11, 13, 14), and Section 1.7.7:
TIMx capture/compare mode register 1 [alternate]  (TIMx_CCMR1)(x = 16 to
17).
USART2 information in [Table 27](../tables/table_27.md): Device resources enabled in different
operating modes corrected.
Spurious “TIM15” removed from Section 6.2.7: Clock security system (CSS).
Cross-reference to DBG added in WWDG Section 60.4.6: Debug mode.
Section 24.2: RTC main features corrected (spurious “or by a tamper event”
removed).
03-Dec-2022 3
First public release.
Section 5.3.2: Low-power modes, bulleted point Standby mode.
Section 6.2: Clocks, bulleted point TIMx.
[Figure 9](../figures/figure_9.md): Clock tree.
Section 6.3: Low-power modes, removal of “USART2”.
Section Converting a supply-relative ADC measurement to an absolute voltage
value.
[Figure 178](../figures/figure_178.md): Break and Break2 circuitry overview - note under the figure
corrected.
Section 18.3.25: Interfacing with Hall sensors - removal of “TIM4”.
[Figure 26](../figures/figure_26.md): Break circuitry overview - note under the figure corrected.
10-Jul-2024 4
Document device reference from “STM32C0x1” to “STM32C0 series”;
Integration of the information relative to STM32C071xx.
Cover page: added reference to the errata sheets.
Added Section 8: Clock recovery system (CRS) and Section 47: Universal
serial bus full-speed host/device interface (USB).
Memory mapping: Added [Table 1](../tables/table_1.md): Peripherals or functions versus products.
Updated [Figure 2](../figures/figure_2.md): Memory map, [Table 2](../tables/table_2.md): STM32C011xx and STM32C031xx
boundary addresses, and [Table 7](../tables/table_7.md): STM32C0xx peripheral register boundary
addresses; added [Table 4](../tables/table_4.md): STM32C071xx boundary addresses. Promoted
Section 3: Boot modes to the first level and updated. Demoted Section 3.1:
Boot configuration as a subsection. Reworked Section 3.1.4: Empty check. In
the table of boundary addresses, “Code” replaced with “FLASH” and “FLASH
or SRAM”;

Revision history RM0490
1020/1023 RM0490 Rev 6
10-Jul-2024 4
Boot modes: updated Section 3.1: Boot configuration;
FLASH: Section 4.2: FLASH main features, Section 4.3.1: Flash memory
organization (added Section [Table 12](../tables/table_12.md).: Flash memory organization for
STM32C071xx), sections Flash memory page erase, Flash memory bank or
mass erase, Standard programming, and Fast programming; adapted sizes of
PCROP1A_STRT, PCROP1A_END, PCROP1B_STRT, PCROP1B_END,
WRP1A_STRT, WRP1A_END, WRP1B_STRT, WRP1B_END, SEC_SIZE and
PNB bitfields; updated Section 4.5.1: FLASH read protection (RDP),
Section 4.5.6: Forcing boot from main flash memory, and [Table 22](../tables/table_22.md): PCROP
protection, sections Changing the read protection level, Fast programming,
and Option byte loading, registers FLASH_ACR, FLASH_SR, FLASH_CR;
option bytes FLASH_OPTR factory value, BOR_EN reset value; HSI48
division corrected from four to three; BOOT_LOCK bit note modified; all
nBOOTx and nRSTx bits renamed to NBOOTx and NRSTx; Removed section
FLASH empty check;
PWR: updated Section 5.1: Power supplies and voltage references ([Figure 5](../figures/figure_5.md):
Power supply overview), [Table 27](../tables/table_27.md): Device resources enabled in different
operating modes, and registers PWR_CR3, PWR_CR4, PWR_SR1,
PWR_SR2, PWR_SCR, PWR_PUCRC, PWR_PDCRC, PWR_PUCRD,
PWR_PDCRD, PWR_PUCRF, and PWR_PDCRF; Added register PWR_CR2;
corrected PVM_VDDIO2_OUT description;
RCC: Added HSIUSB48 RC oscillator in multiple sections, tables, and figures;
updated [Figure 9](../figures/figure_9.md): Clock tree, added Section 6.2.3: HSIUSB48 clock, updated
registers RCC_CR, RCC_CFGR, RCC_CIER, RCC_CIFR, RCC_CICR,
RCC_APBRSTR1, RCC_APBENR1, RCC_APBSMENR1,
RCC_APBSMENR2, and RCC_CCIPR1 (to RCC_CCIPR); added registers
RCC_CCIPR2 and RCC_CRRCR; Corrected RCC_CFGR bitmap, LSERDYIE
bit name, LSIRDYF bit description, HSIDIV[2:0] and HSIKERDIV[2:0] reset
values in the register map, and missing bits added; updated Section 6.2.15:
Peripheral clock enable registers; RCC_RC register access specified;
HSIUSB48 added to SW[2:0] and SWS[2:0] bitfields; LSIRDYF description
corrected; updated section NRST (external reset); pin name PF2 or NRST
corrected to PF2-NRST; bitfield PINRSTF of RCC_CSR2 register updated;
corrected reference in section External crystal/ceramic resonator (HSE
crystal); updated section External source (HSE bypass) and TIM17;
CRS: added Section 8.4.2: CRS internal signals; updated [Table 70](../tables/table_70.md): CRS
interconnection title;
GPIO: Updated register GPIOx_PUPDR, Section 8.3.14: Low pin count
package adjustment, and Section 8.3.15: Reset pin (PF2-NRST) in GPIO
mode; removed section Boot0 pin (PA14) in GPIO mode;
SYSCFG: Updated registers SYSCFG_CFGR1, SYSCFG_CFGR3,
SYSCFG_ITLINE11, added registers SYSCFG_ITLINE9, SYSCFG_ITLINE15,
SYSCFG_ITLINE24, and SYSCFG_ITLINE25; added register
SYSCFG_ITLINE1; corrected “system reset value” to “reset value” for all
registers; updated register SYSCFG_CFGR3 description; updated [Table 40](../tables/table_40.md):
SYSCFG register map and reset values;
DMAMUX: Updated [Table 42](../tables/table_42.md): DMAMUX: assignment of multiplexer inputs to
resources, [Table 43](../tables/table_43.md): DMAMUX: assignment of trigger inputs to resources, and
[Table 44](../tables/table_44.md): DMAMUX: assignment of synchronization inputs to resources;
Interconnect matrix: Updated [Table 41](../tables/table_41.md): Interconnect matrix and sections
Section 10.3.1 and Section 10.3.2; Added TIM2;
NVIC: Updated [Table 54](../tables/table_54.md): Vector table; added VDDIO2 monitor interrupt;
[Table 180](../tables/table_180.md). Document revision history (continued)
Date Revision Changes

RM0490 Rev 6 1021/1023
RM0490 Revision history
1022
10-Jul-2024 4
EXTI: Updated [Table 58](../tables/table_58.md): EXTI line connections; added registers
EXTI_RTSR2, EXTI_FTSR2, EXTI_SWIER2, EXTI_RPR2, EXTI_FPR2,
EXTI_IMR2, and EXTI_EMR2; updated EXTI_EXTICRx register description by
replacing the “m” substitution of the repeating part of the formula in all bitfield
names and enumerated value descriptions; updated [Table 58](../tables/table_58.md): EXTI line
connections, Section 14.5.14: EXTI CPU wake-up with interrupt mask register
2 (EXTI_IMR2), Section 14.5.15: EXTI CPU wake-up with event mask register
2 (EXTI_EMR2), and Section 14.5.16: EXTI register map
TIMERS: updated [Table 20](../tables/table_20.md).6.20: TIM17 input selection register
(TIM17_TISEL);
I2C: general update;
DBG: Updated Section 30.5.3: SW-DP state machine (reset, idle states, ID
code) (ID code), [Table 176](../tables/table_176.md): DEV_ID bitfield values and the DBG_APB_FZ1
register; added reset value to the DBG_IDCODE register; REV_ID bitfield
definition reported to the errata sheets;
Device electronic signature: Updated Section 31.3: Package data register
(PCKR)
IDWG: Corrected descriptions of the IWDG_SR register bitfields WVU and
RVU;
USART: Extended note in the description of the PRESCALER[3:0] bitfield of
the USART_PRESC register;
USB: updated [Table 47](../tables/table_47.md).4.2: USB pins and internal signals and Section 47.4.5:
Description of USB blocks used in both Device and Host modes; register
description split to USB registers and USB SRAM registers;
Device electronic signature: Corrected all LQPF occurrences to LQFP .
Multiple sections: SPI1/I2S or SPI1 used as instance name of the peripheral
corrected to SPI2S1.
17-Dec-2024 5
Added information specific to STM32C051xx and STM32C09xxx devices;
Document conventions: Added Section 1.3: Register reset value;
Memory and bus architecture: Added Section 2.4: FDCAN RAM, [Table 3](../tables/table_3.md),
[Table 5](../tables/table_5.md), and [Table 6](../tables/table_6.md); updated [Table 7](../tables/table_7.md),
FLASH: Added [Table 11](../tables/table_11.md) and [Table 13](../tables/table_13.md); updated [Table 21](../tables/table_21.md), Section 4.7.6:
FLASH option register (FLASH_OPTR); updates for integrating STM32C051xx
and STM32C09xxx, and FDCAN;
PWR: Updated [Table 27](../tables/table_27.md): Device resources enabled in different operating
modes, Section : Peripheral clock gating; updates for integrating
STM32C051xx and STM32C09xxx;
RCC: Updates for integrating STM32C051xx and STM32C09xxx, and FDCAN;
updated [Figure 9](../figures/figure_9.md): Clock tree, Section 6.2.6: System clock (SYSCLK) selection;
CRS: Added [Table 33](../tables/table_33.md): CRS internal input/output signals; general update;
GPIO: Added Section 8.4: GPIO in low-power modes; updates for integrating
STM32C051xx and STM32C09xxx;
SYSCFG: Added sections Section 9.1.22, Section 9.1.31, Section 9.1.32, and
Section 9.1.33;
DMAMUX: Updates for integrating STM32C051xx and STM32C09xxx;
EXTI: Updates for introducing TIM15, USART3, USART4, and FDCAN;
Interconnect matrix: Updated Section 10.3.1, Section 10.3.2, and
Section 10.3.6;
[Table 180](../tables/table_180.md). Document revision history (continued)
Date Revision Changes

Revision history RM0490
1022/1023 RM0490 Rev 6
17-Dec-2024 5
ADC: Updated software calibration procedure, ADC clock symbol, TSEN and
VREFEN bitfields;
Timers: Update of advanced timer and general-purpose timer sections, with
the addition of TIM15;
I2C: General update, with the deprecated terms master and slave replaced
with controller and target, respectively;
Added Section 28: FD controller area network (FDCAN);
Added Section 32: Important security notice
20-May-2026 6
Removed register index.
SYSCFG: Section 9.1.3: SYSCFG configuration register 3 (SYSCFG_CFGR3)
- bitfields PINMUX1[1:0] for STM32C011xx,and PINMUX2[1:0] and
PINMUX3[1:0] for STM32C071xx;
DMAMUX: Section [Table 51](../tables/table_51.md).: DMAMUX: assignment of synchronization inputs
to resources - tim14_trgo on trigger input 22;
Device electronic signature: Section 31.3: Package data register (PCKR) -
bitfield PKG[3:0] value for STM32C071xx LQFP64_N package;
Section 31.1: Unique device ID register (96 bits) (UID) - UID[31:0];
FLASH: Section 4.3.6: FLASH main memory programming sequences -
Standard programming;
Section 4.4.2: FLASH option byte programming - Modifying user options;
ADC: section Temperature sensor, VREFINT and VDDA and VSSA internal
channels.
CRS: Section 15.4.3: CRC control register (CRC_CR) bitfield TRIM[6:0];
FDCAN: Ranges of time quanta, nominal and data bit rates, number of CAN
standard occurrences of 11 bits, EINT0 and EINT1 bit function descriptions;
USB: Device PLL mentions removed.
[Table 180](../tables/table_180.md). Document revision history (continued)
Date Revision Changes

RM0490 Rev 6 1023/1023
RM0490
1023
IMPORTANT NOTICE – READ CAREFULLY
STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and
improvements to ST products and/or to this document at any time without notice.
In the event of any conflict between the provisions of this document and the provisions of any contractual arrangement in force between the
purchasers and ST, the provisions of such contractual arrangement shall prevail.
The purchasers should obtain the latest relevant information on ST products before placing orders. ST products are sold pursuant to ST’s
terms and conditions of sale in place at the time of order acknowledgment.
The purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application
assistance or the design of the purchasers’ products.
No license, express or implied, to any intellectual property right is granted by ST herein.
Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.
If the purchasers identify an ST product that meets their functional and performance requirements but that is not designated for the
purchasers’ market segment, the purchasers shall contact ST for more information.
ST and the ST logo are trademarks of ST. For additional information about ST trademarks, refer to www.st.com/trademarks. All other
product or service names are the property of their respective owners.
Information in this document supersedes and replaces information previously supplied in any prior versions of this document.
© 2026 STMicroelectronics – All rights reserved
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 2: Architectural Diagram](../figures/figure_2.md)
* [Figure 5: Architectural Diagram](../figures/figure_5.md)
* [Figure 9: Architectural Diagram](../figures/figure_9.md)
* [Figure 26: Architectural Diagram](../figures/figure_26.md)
* [Figure 178: Architectural Diagram](../figures/figure_178.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 1: Configuration Matrix](../tables/table_1.md)
* [Table 2: Configuration Matrix](../tables/table_2.md)
* [Table 3: Configuration Matrix](../tables/table_3.md)
* [Table 4: Configuration Matrix](../tables/table_4.md)
* [Table 5: Configuration Matrix](../tables/table_5.md)
* [Table 6: Configuration Matrix](../tables/table_6.md)
* [Table 7: Configuration Matrix](../tables/table_7.md)
* [Table 11: Configuration Matrix](../tables/table_11.md)
* [Table 12: Configuration Matrix](../tables/table_12.md)
* [Table 13: Configuration Matrix](../tables/table_13.md)
* [Table 18: Configuration Matrix](../tables/table_18.md)
* [Table 20: Configuration Matrix](../tables/table_20.md)
* [Table 21: Configuration Matrix](../tables/table_21.md)
* [Table 22: Configuration Matrix](../tables/table_22.md)
* [Table 27: Configuration Matrix](../tables/table_27.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)