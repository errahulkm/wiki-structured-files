# Timers (TIM)

## 1. Overview & Key Features
The Timers (TIM) block provides complete operational functionality for the STM32G4 microcontroller.
Documented in [Chapter 28](../chapters/chapter_28.md), [Chapter 29](../chapters/chapter_29.md), [Chapter 30](../chapters/chapter_30.md), [Chapter 31](../chapters/chapter_31.md), [Chapter 32](../chapters/chapter_32.md), [Chapter 33](../chapters/chapter_33.md) (Pages 881 - 1143).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 28](../chapters/chapter_28.md), [Chapter 29](../chapters/chapter_29.md), [Chapter 30](../chapters/chapter_30.md), [Chapter 31](../chapters/chapter_31.md), [Chapter 32](../chapters/chapter_32.md), [Chapter 33](../chapters/chapter_33.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Timers (TIM) Architectural Block Diagram](../figures/timers_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Timers (TIM) Configuration & Parameter Matrix](../tables/timers_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `TIM` | `0x24` | Timers (TIM) TIM Register | [TIM.json](../registers_json/TIM.json) |
| `TIM1` | `0x00` | Counter register 01 02 03 00 01 02 0332 33 34 35 36 UG tim_ti1 3130 TIF RM0440 Rev 9 1229/2140 RM0440 Advanced-control timers (TIM1) | [TIM1.json](../registers_json/TIM1.json) |
| `TIM15` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0440 Rev 9 1483/88 RM0440 General purpose time rs (TIM15) | [TIM15.json](../registers_json/TIM15.json) |
| `TIM15_AF1` | `0x060` | TIM15 alternate func tion register 1 (TIM15_AF1) | [TIM15_AF1.json](../registers_json/TIM15_AF1.json) |
| `TIM15_AF2` | `0x064` | TIM15 alternate func tion register 2 (TIM15_AF2) | [TIM15_AF2.json](../registers_json/TIM15_AF2.json) |
| `TIM15_ARR` | `0x2C` | TIM15 autorelo ad register (TIM15_ARR) | [TIM15_ARR.json](../registers_json/TIM15_ARR.json) |
| `TIM15_BDTR` | `0x44` | TIM15 break and dead -time register (TIM15_BDTR) | [TIM15_BDTR.json](../registers_json/TIM15_BDTR.json) |
| `TIM15_CCER` | `0x20` | TIM15 capture/compare enable register (TIM15_CCER) | [TIM15_CCER.json](../registers_json/TIM15_CCER.json) |
| `TIM15_CCMR1` | `0x18` | TIM15 capture/compare m ode register 1 (TIM15_CCMR1) | [TIM15_CCMR1.json](../registers_json/TIM15_CCMR1.json) |
| `TIM15_CCR1` | `0x34` | TIM15 capture/compa re register 1 (TIM15_CCR1) | [TIM15_CCR1.json](../registers_json/TIM15_CCR1.json) |
| `TIM15_CCR2` | `0x38` | TIM15 capture/compa re register 2 (TIM15_CCR2) | [TIM15_CCR2.json](../registers_json/TIM15_CCR2.json) |
| `TIM15_CNT` | `0x24` | Timers (TIM) TIM15_CNT Register | [TIM15_CNT.json](../registers_json/TIM15_CNT.json) |
| `TIM15_CR1` | `0x00` | TIM15 control register 1 (TIM15_CR1) | [TIM15_CR1.json](../registers_json/TIM15_CR1.json) |
| `TIM15_CR2` | `0x04` | TIM15 control register 2 (TIM15_CR2) | [TIM15_CR2.json](../registers_json/TIM15_CR2.json) |
| `TIM15_DCR` | `0x3DC` | TIM15 DMA cont rol register (TIM15_DCR) | [TIM15_DCR.json](../registers_json/TIM15_DCR.json) |
| `TIM15_DIER` | `0x0C` | TIM15 DMA/interrupt en able register (TIM15_DIER) | [TIM15_DIER.json](../registers_json/TIM15_DIER.json) |
| `TIM15_DMAR` | `0x3E0` | Timers (TIM) TIM15_DMAR Register | [TIM15_DMAR.json](../registers_json/TIM15_DMAR.json) |
| `TIM15_DTR2` | `0x054` | TIM15 timer deadti me register 2 (TIM15_DTR2) | [TIM15_DTR2.json](../registers_json/TIM15_DTR2.json) |
| `TIM15_EGR` | `0x14` | TIM15 event generation register (TIM15_EGR) | [TIM15_EGR.json](../registers_json/TIM15_EGR.json) |
| `TIM15_PSC` | `0x28` | Timers (TIM) TIM15_PSC Register | [TIM15_PSC.json](../registers_json/TIM15_PSC.json) |
| `TIM15_RCR` | `0x30` | TIM15 repetition co unter register (TIM15_RCR) | [TIM15_RCR.json](../registers_json/TIM15_RCR.json) |
| `TIM15_SMCR` | `0x08` | TIM15 slave mode cont rol register (TIM15_SMCR) | [TIM15_SMCR.json](../registers_json/TIM15_SMCR.json) |
| `TIM15_SR` | `0x10` | TIM15 status register (TIM15_SR) | [TIM15_SR.json](../registers_json/TIM15_SR.json) |
| `TIM15_TISEL` | `0x5C` | TIM15 input selectio n register (TIM15_TISEL) | [TIM15_TISEL.json](../registers_json/TIM15_TISEL.json) |
| `TIM16` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0440 Rev 9 1483/88 RM0440 General purpose time rs (TIM16) | [TIM16.json](../registers_json/TIM16.json) |
| `TIM17` | `0x04` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0440 Rev 9 1483/88 RM0440 General purpose time rs (TIM17) | [TIM17.json](../registers_json/TIM17.json) |
| `TIM2` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0440 Rev 9 1403/2140 RM0440 General-purpose timers (TIM2) | [TIM2.json](../registers_json/TIM2.json) |
| `TIM20` | `0x000` | Counter register 01 02 03 00 01 02 0332 33 34 35 36 UG tim_ti1 3130 TIF RM0440 Rev 9 1229/2140 RM0440 Advanced-control timers (TIM20) | [TIM20.json](../registers_json/TIM20.json) |
| `TIM3` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0440 Rev 9 1403/2140 RM0440 General-purpose timers (TIM3) | [TIM3.json](../registers_json/TIM3.json) |
| `TIM4` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0440 Rev 9 1403/2140 RM0440 General-purpose timers (TIM4) | [TIM4.json](../registers_json/TIM4.json) |
| `TIM5` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0440 Rev 9 1403/2140 RM0440 General-purpose timers (TIM5) | [TIM5.json](../registers_json/TIM5.json) |
| `TIM6` | `0x00` | 02 03 04 05 06 07F1 F2 F3 F4 F5F0 01 CEN Auto-reload preload register Write a new value in TIMx_ARR Auto-reload shadow register F5 36 RM0440 Rev 9 1519/2140 RM0440 Basic timers (TIM6) | [TIM6.json](../registers_json/TIM6.json) |
| `TIM7` | `0x00` | 02 03 04 05 06 07F1 F2 F3 F4 F5F0 01 CEN Auto-reload preload register Write a new value in TIMx_ARR Auto-reload shadow register F5 36 RM0440 Rev 9 1519/2140 RM0440 Basic timers (TIM7) | [TIM7.json](../registers_json/TIM7.json) |
| `TIM8` | `0x00` | Counter register 01 02 03 00 01 02 0332 33 34 35 36 UG tim_ti1 3130 TIF RM0440 Rev 9 1229/2140 RM0440 Advanced-control timers (TIM8) | [TIM8.json](../registers_json/TIM8.json) |
| `TIMX_CCMR1` | `0x00` | TIMx capture/compare m ode register 1 (TIMX_CCMR1) | [TIMX_CCMR1.json](../registers_json/TIMX_CCMR1.json) |
| `TIMX_CCMR2` | `0x00` | TIMx capture/compare m ode register 2 (TIMX_CCMR2) | [TIMX_CCMR2.json](../registers_json/TIMX_CCMR2.json) |
| `TIMX_CCMR3` | `0x00` | TIMx capture/compare mode register 3 (TIMX_CCMR3) | [TIMX_CCMR3.json](../registers_json/TIMX_CCMR3.json) |
| `TIM_CH1` | `0xCC1E` | Timers (TIM) TIM_CH1 Register | [TIM_CH1.json](../registers_json/TIM_CH1.json) |
| `TIM_TI1_IN0` | `0x00` | tim_ker_ck DMA interface IRQ interface tim_pclk 32-bit APB bus tim_cc1_dma tim_upd_dma tim_trgi_dma tim_com_dma tim_it Trigger controller Slave controller mode DTG registers DTG Output control Output control Repetition counter UEV UEV (TIM_TI1_IN0) | [TIM_TI1_IN0.json](../registers_json/TIM_TI1_IN0.json) |