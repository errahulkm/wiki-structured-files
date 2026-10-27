# Timers (TIM)

## 1. Overview & Key Features
The Timers (TIM) block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 17](../chapters/chapter_17.md), [Chapter 18](../chapters/chapter_18.md), [Chapter 19](../chapters/chapter_19.md), [Chapter 20](../chapters/chapter_20.md) (Pages 346 - 444).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 17](../chapters/chapter_17.md), [Chapter 18](../chapters/chapter_18.md), [Chapter 19](../chapters/chapter_19.md), [Chapter 20](../chapters/chapter_20.md)
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
| `TIM1` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 Advanced-control timer (TIM1) | [TIM1.json](../registers_json/TIM1.json) |
| `TIM14` | `0x00` | TIM1_CNT B200 B2010039 TIM1_CCR1 003A Write B201h in the CC1R register Match detected on CCR1 Interrupt generated if enabled 003B B201 003A RM0490 Rev 6 531/1023 RM0490 General-purpos e timers (TIM14) | [TIM14.json](../registers_json/TIM14.json) |
| `TIM14_ARR` | `0x2C` | TIM14 auto-reloa d register (TIM14_ARR) | [TIM14_ARR.json](../registers_json/TIM14_ARR.json) |
| `TIM14_CCER` | `0x20` | TIM14 capture/compare enable register (TIM14_CCER) | [TIM14_CCER.json](../registers_json/TIM14_CCER.json) |
| `TIM14_CCMR1` | `0x18` | TIM14 capture/compare m ode register 1 (TIM14_CCMR1) | [TIM14_CCMR1.json](../registers_json/TIM14_CCMR1.json) |
| `TIM14_CCR1` | `0x34` | TIM14 capture/compa re register 1 (TIM14_CCR1) | [TIM14_CCR1.json](../registers_json/TIM14_CCR1.json) |
| `TIM14_CR1` | `0x00` | TIM14 control re gister 1 (TIM14_CR1) | [TIM14_CR1.json](../registers_json/TIM14_CR1.json) |
| `TIM14_DIER` | `0x0C` | TIM14 Interrupt enab le register (TIM14_DIER) | [TIM14_DIER.json](../registers_json/TIM14_DIER.json) |
| `TIM14_EGR` | `0x14` | TIM14 event generati on register (TIM14_EGR) | [TIM14_EGR.json](../registers_json/TIM14_EGR.json) |
| `TIM14_SR` | `0x10` | TIM14 status register (TIM14_SR) | [TIM14_SR.json](../registers_json/TIM14_SR.json) |
| `TIM14_TISEL` | `0x68` | TIM14 timer input sel ection register (TIM14_TISEL) | [TIM14_TISEL.json](../registers_json/TIM14_TISEL.json) |
| `TIM15` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0490 Rev 6 609/1023 RM0490 General-purpose time rs (TIM15) | [TIM15.json](../registers_json/TIM15.json) |
| `TIM15_AF1` | `0x60` | TIM15 alternate register 1 (TIM15_AF1) | [TIM15_AF1.json](../registers_json/TIM15_AF1.json) |
| `TIM15_ARR` | `0x2C` | TIM15 auto-reloa d register (TIM15_ARR) | [TIM15_ARR.json](../registers_json/TIM15_ARR.json) |
| `TIM15_BDTR` | `0x44` | TIM15 break and dead -time register (TIM15_BDTR) | [TIM15_BDTR.json](../registers_json/TIM15_BDTR.json) |
| `TIM15_CCER` | `0x20` | enable register (TIM15_CCER) | [TIM15_CCER.json](../registers_json/TIM15_CCER.json) |
| `TIM15_CCMR1` | `0x18` | TIM15 capture/compare m ode register 1 (TIM15_CCMR1) | [TIM15_CCMR1.json](../registers_json/TIM15_CCMR1.json) |
| `TIM15_CCR1` | `0x34` | TIM15 capture/compa re register 1 (TIM15_CCR1) | [TIM15_CCR1.json](../registers_json/TIM15_CCR1.json) |
| `TIM15_CCR2` | `0x38` | TIM15 capture/compa re register 2 (TIM15_CCR2) | [TIM15_CCR2.json](../registers_json/TIM15_CCR2.json) |
| `TIM15_CNT` | `0x24` | Timers (TIM) TIM15_CNT Register | [TIM15_CNT.json](../registers_json/TIM15_CNT.json) |
| `TIM15_CR1` | `0x00` | Timers (TIM) TIM15_CR1 Register | [TIM15_CR1.json](../registers_json/TIM15_CR1.json) |
| `TIM15_CR2` | `0x04` | TIM15 control register 2 (TIM15_CR2) | [TIM15_CR2.json](../registers_json/TIM15_CR2.json) |
| `TIM15_DCR` | `0x48` | TIM15 DMA cont rol register (TIM15_DCR) | [TIM15_DCR.json](../registers_json/TIM15_DCR.json) |
| `TIM15_DIER` | `0x0C` | TIM15 DMA/interrupt en able register (TIM15_DIER) | [TIM15_DIER.json](../registers_json/TIM15_DIER.json) |
| `TIM15_DMAR` | `0x4C` | Timers (TIM) TIM15_DMAR Register | [TIM15_DMAR.json](../registers_json/TIM15_DMAR.json) |
| `TIM15_EGR` | `0x14` | TIM15 event generation register (TIM15_EGR) | [TIM15_EGR.json](../registers_json/TIM15_EGR.json) |
| `TIM15_PSC` | `0x28` | Timers (TIM) TIM15_PSC Register | [TIM15_PSC.json](../registers_json/TIM15_PSC.json) |
| `TIM15_RCR` | `0x30` | TIM15 repetition co unter register (TIM15_RCR) | [TIM15_RCR.json](../registers_json/TIM15_RCR.json) |
| `TIM15_SMCR` | `0x08` | control register (TIM15_SMCR) | [TIM15_SMCR.json](../registers_json/TIM15_SMCR.json) |
| `TIM15_SR` | `0x10` | TIM15 status register (TIM15_SR) | [TIM15_SR.json](../registers_json/TIM15_SR.json) |
| `TIM15_TISEL` | `0x68` | TIM15 input selectio n register (TIM15_TISEL) | [TIM15_TISEL.json](../registers_json/TIM15_TISEL.json) |
| `TIM16` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0490 Rev 6 609/1023 RM0490 General-purpose time rs (TIM16) | [TIM16.json](../registers_json/TIM16.json) |
| `TIM16_AF1` | `0x60` | TIM16 alternate func tion register 1 (TIM16_AF1) | [TIM16_AF1.json](../registers_json/TIM16_AF1.json) |
| `TIM16_TISEL` | `0x68` | TIM16 input selectio n register (TIM16_TISEL) | [TIM16_TISEL.json](../registers_json/TIM16_TISEL.json) |
| `TIM17` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0490 Rev 6 609/1023 RM0490 General-purpose time rs (TIM17) | [TIM17.json](../registers_json/TIM17.json) |
| `TIM17_AF1` | `0x60` | TIM17 alternate func tion register 1 (TIM17_AF1) | [TIM17_AF1.json](../registers_json/TIM17_AF1.json) |
| `TIM17_TISEL` | `0x68` | TIM17 input selectio n register (TIM17_TISEL) | [TIM17_TISEL.json](../registers_json/TIM17_TISEL.json) |
| `TIM1_AF1` | `0x60` | TIM1 alternate functi on option register 1 (TIM1_AF1) | [TIM1_AF1.json](../registers_json/TIM1_AF1.json) |
| `TIM1_AF2` | `0x64` | TIM1 Alternate func tion register 2 (TIM1_AF2) | [TIM1_AF2.json](../registers_json/TIM1_AF2.json) |
| `TIM1_ARR` | `0x2C` | TIM1 auto-reload register (TIM1_ARR) | [TIM1_ARR.json](../registers_json/TIM1_ARR.json) |
| `TIM1_BDTR` | `0x44` | TIM1 break and dead-time register (TIM1_BDTR) | [TIM1_BDTR.json](../registers_json/TIM1_BDTR.json) |
| `TIM1_CCER` | `0x20` | enable register (TIM1_CCER) | [TIM1_CCER.json](../registers_json/TIM1_CCER.json) |
| `TIM1_CCERCC1NE` | `0xCC1E` | Timers (TIM) TIM1_CCERCC1NE Register | [TIM1_CCERCC1NE.json](../registers_json/TIM1_CCERCC1NE.json) |
| `TIM1_CCMR1` | `0x18` | TIM1 capture/compare m ode register 1 (TIM1_CCMR1) | [TIM1_CCMR1.json](../registers_json/TIM1_CCMR1.json) |
| `TIM1_CCMR2` | `0x1C` | TIM1 capture/compare m ode register 2 (TIM1_CCMR2) | [TIM1_CCMR2.json](../registers_json/TIM1_CCMR2.json) |
| `TIM1_CCMR3` | `0x54` | TIM1 capture/compare mode register 3 (TIM1_CCMR3) | [TIM1_CCMR3.json](../registers_json/TIM1_CCMR3.json) |
| `TIM1_CCR1` | `0x34` | TIM1 capture/compare register 1 (TIM1_CCR1) | [TIM1_CCR1.json](../registers_json/TIM1_CCR1.json) |
| `TIM1_CCR2` | `0x38` | TIM1 capture/compare register 2 (TIM1_CCR2) | [TIM1_CCR2.json](../registers_json/TIM1_CCR2.json) |
| `TIM1_CCR3` | `0x3C` | TIM1 capture/compare register 3 (TIM1_CCR3) | [TIM1_CCR3.json](../registers_json/TIM1_CCR3.json) |
| `TIM1_CCR4` | `0x40` | TIM1 capture/compare register 4 (TIM1_CCR4) | [TIM1_CCR4.json](../registers_json/TIM1_CCR4.json) |
| `TIM1_CCR5` | `0x58` | TIM1 capture/compare register 5 (TIM1_CCR5) | [TIM1_CCR5.json](../registers_json/TIM1_CCR5.json) |
| `TIM1_CCR6` | `0x5C` | TIM1 capture/compare register 6 (TIM1_CCR6) | [TIM1_CCR6.json](../registers_json/TIM1_CCR6.json) |
| `TIM1_CNT` | `0x24` | Timers (TIM) TIM1_CNT Register | [TIM1_CNT.json](../registers_json/TIM1_CNT.json) |
| `TIM1_CR1` | `0x00` | Timers (TIM) TIM1_CR1 Register | [TIM1_CR1.json](../registers_json/TIM1_CR1.json) |
| `TIM1_CR2` | `0x04` | TIM1 control re gister 2 (TIM1_CR2) | [TIM1_CR2.json](../registers_json/TIM1_CR2.json) |
| `TIM1_DCR` | `0x48` | TIM1 DMA control register (TIM1_DCR) | [TIM1_DCR.json](../registers_json/TIM1_DCR.json) |
| `TIM1_DIER` | `0x0C` | TIM1 DMA/interrupt enable register (TIM1_DIER) | [TIM1_DIER.json](../registers_json/TIM1_DIER.json) |
| `TIM1_DMAR` | `0x4C` | Timers (TIM) TIM1_DMAR Register | [TIM1_DMAR.json](../registers_json/TIM1_DMAR.json) |
| `TIM1_EGR` | `0x14` | TIM1 event generati on register (TIM1_EGR) | [TIM1_EGR.json](../registers_json/TIM1_EGR.json) |
| `TIM1_PSC` | `0x28` | Timers (TIM) TIM1_PSC Register | [TIM1_PSC.json](../registers_json/TIM1_PSC.json) |
| `TIM1_RCR` | `0x30` | TIM1 repetition c ounter register (TIM1_RCR) | [TIM1_RCR.json](../registers_json/TIM1_RCR.json) |
| `TIM1_SMCR` | `0x08` | control register (TIM1_SMCR) | [TIM1_SMCR.json](../registers_json/TIM1_SMCR.json) |
| `TIM1_SR` | `0x10` | TIM1 status register (TIM1_SR) | [TIM1_SR.json](../registers_json/TIM1_SR.json) |
| `TIM1_TISEL` | `0x68` | TIM1 timer input sel ection register (TIM1_TISEL) | [TIM1_TISEL.json](../registers_json/TIM1_TISEL.json) |
| `TIM2` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0490 Rev 6 517/1023 RM0490 General-purpose timers (TIM2) | [TIM2.json](../registers_json/TIM2.json) |
| `TIM2_AF1` | `0x60` | TIM2 alternate functi on option register 1 (TIM2_AF1) | [TIM2_AF1.json](../registers_json/TIM2_AF1.json) |
| `TIM2_TISEL` | `0x68` | TIM2 timer input sel ection register (TIM2_TISEL) | [TIM2_TISEL.json](../registers_json/TIM2_TISEL.json) |
| `TIM3` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0490 Rev 6 517/1023 RM0490 General-purpose timers (TIM3) | [TIM3.json](../registers_json/TIM3.json) |
| `TIM3_AF1` | `0x60` | TIM3 alternate functi on option register 1 (TIM3_AF1) | [TIM3_AF1.json](../registers_json/TIM3_AF1.json) |
| `TIM3_TISEL` | `0x68` | TIM3 timer input sel ection register (TIM3_TISEL) | [TIM3_TISEL.json](../registers_json/TIM3_TISEL.json) |
| `TIMX_ARR` | `0x2C` | TIMx auto-reload regi ster (TIMX_ARR) | [TIMX_ARR.json](../registers_json/TIMX_ARR.json) |
| `TIMX_BDTR` | `0x44` | TIMx break and dead-time re gister (TIMX_BDTR) | [TIMX_BDTR.json](../registers_json/TIMX_BDTR.json) |
| `TIMX_CCER` | `0x20` | enable register (TIMX_CCER) | [TIMX_CCER.json](../registers_json/TIMX_CCER.json) |
| `TIMX_CCERCC1NE` | `0xCC1E` | Timers (TIM) TIMX_CCERCC1NE Register | [TIMX_CCERCC1NE.json](../registers_json/TIMX_CCERCC1NE.json) |
| `TIMX_CCMR1` | `0x18` | TIMx capture/compare mode register 1 (TIMX_CCMR1) | [TIMX_CCMR1.json](../registers_json/TIMX_CCMR1.json) |
| `TIMX_CCMR2` | `0x1C` | TIMx capture/compare mode re gister 2 (TIMX_CCMR2) | [TIMX_CCMR2.json](../registers_json/TIMX_CCMR2.json) |
| `TIMX_CCR1` | `0x34` | TIMx capture/compare regi ster 1 (TIMX_CCR1) | [TIMX_CCR1.json](../registers_json/TIMX_CCR1.json) |
| `TIMX_CCR2` | `0x38` | TIMx capture/compare regi ster 2 (TIMX_CCR2) | [TIMX_CCR2.json](../registers_json/TIMX_CCR2.json) |
| `TIMX_CCR3` | `0x3C` | TIMx capture/compare regi ster 3 (TIMX_CCR3) | [TIMX_CCR3.json](../registers_json/TIMX_CCR3.json) |
| `TIMX_CCR4` | `0x40` | TIMx capture/compare regi ster 4 (TIMX_CCR4) | [TIMX_CCR4.json](../registers_json/TIMX_CCR4.json) |
| `TIMX_CH1` | `0xCC1E` | Timers (TIM) TIMX_CH1 Register | [TIMX_CH1.json](../registers_json/TIMX_CH1.json) |
| `TIMX_CNT` | `0x24` | writing any of the counter registers (TIMX_CNT) | [TIMX_CNT.json](../registers_json/TIMX_CNT.json) |
| `TIMX_CR1` | `0x00` | Timers (TIM) TIMX_CR1 Register | [TIMX_CR1.json](../registers_json/TIMX_CR1.json) |
| `TIMX_CR1ADDRESS` | `0x00` | A read or write operation to the DMAR register accesses the register located at the address (TIMX_CR1ADDRESS) | [TIMX_CR1ADDRESS.json](../registers_json/TIMX_CR1ADDRESS.json) |
| `TIMX_CR2` | `0x04` | TIMx control register 2 (TIMX_CR2) | [TIMX_CR2.json](../registers_json/TIMX_CR2.json) |
| `TIMX_DCR` | `0x48` | TIMx DMA control regi ster (TIMX_DCR) | [TIMX_DCR.json](../registers_json/TIMX_DCR.json) |
| `TIMX_DIER` | `0x0C` | TIMx DMA/interrupt enable re gister (TIMX_DIER) | [TIMX_DIER.json](../registers_json/TIMX_DIER.json) |
| `TIMX_DMAR` | `0x4C` | Timers (TIM) TIMX_DMAR Register | [TIMX_DMAR.json](../registers_json/TIMX_DMAR.json) |
| `TIMX_EGR` | `0x14` | TIMx event generation regi ster (TIMX_EGR) | [TIMX_EGR.json](../registers_json/TIMX_EGR.json) |
| `TIMX_PSC` | `0x28` | Timers (TIM) TIMX_PSC Register | [TIMX_PSC.json](../registers_json/TIMX_PSC.json) |
| `TIMX_PSCPRESCALERREGISTER` | `0x00` | This means that data are transferred from the preload registers to the shadow registers (TIMX_PSCPRESCALERREGISTER) | [TIMX_PSCPRESCALERREGISTER.json](../registers_json/TIMX_PSCPRESCALERREGISTER.json) |
| `TIMX_RCR` | `0x30` | TIMx repetition counter register (TIMX_RCR) | [TIMX_RCR.json](../registers_json/TIMX_RCR.json) |
| `TIMX_SMCR` | `0x08` | TIMx slave mode control re gister (TIMX_SMCR) | [TIMX_SMCR.json](../registers_json/TIMX_SMCR.json) |
| `TIMX_SR` | `0x10` | TIMx status regist er (TIMX_SR) | [TIMX_SR.json](../registers_json/TIMX_SR.json) |
| `TIMY` | `0x4845` | Timers (TIM) TIMY Register | [TIMY.json](../registers_json/TIMY.json) |
| `TIMZ` | `0x0900` | Timers (TIM) TIMZ Register | [TIMZ.json](../registers_json/TIMZ.json) |