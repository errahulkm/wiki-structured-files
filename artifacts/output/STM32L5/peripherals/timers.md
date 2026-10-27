# Timers (TIM)

## 1. Overview & Key Features
The Timers (TIM) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 33](../chapters/chapter_33.md), [Chapter 34](../chapters/chapter_34.md), [Chapter 35](../chapters/chapter_35.md), [Chapter 36](../chapters/chapter_36.md), [Chapter 37](../chapters/chapter_37.md) (Pages 1072 - 1176).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 33](../chapters/chapter_33.md), [Chapter 34](../chapters/chapter_34.md), [Chapter 35](../chapters/chapter_35.md), [Chapter 36](../chapters/chapter_36.md), [Chapter 37](../chapters/chapter_37.md)
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
| `TIM1` | `0x00` | Counter register 3834 35 36 TIF RM0438 Rev 8 1129/2187 RM0438 Advanced-control timers (TIM1) | [TIM1.json](../registers_json/TIM1.json) |
| `TIM15` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0438 Rev 8 1315/2187 RM0438 General-purpose time rs (TIM15) | [TIM15.json](../registers_json/TIM15.json) |
| `TIM15_ARR` | `0x2C` | TIM15 auto-reloa d register (TIM15_ARR) | [TIM15_ARR.json](../registers_json/TIM15_ARR.json) |
| `TIM15_BDTR` | `0x44` | TIM15 break and dead -time register (TIM15_BDTR) | [TIM15_BDTR.json](../registers_json/TIM15_BDTR.json) |
| `TIM15_CCER` | `0x20` | TIM15 capture/compare enable register (TIM15_CCER) | [TIM15_CCER.json](../registers_json/TIM15_CCER.json) |
| `TIM15_CCMR1` | `0x18` | TIM15 capture/compare m ode register 1 (TIM15_CCMR1) | [TIM15_CCMR1.json](../registers_json/TIM15_CCMR1.json) |
| `TIM15_CCR1` | `0x34` | TIM15 capture/compa re register 1 (TIM15_CCR1) | [TIM15_CCR1.json](../registers_json/TIM15_CCR1.json) |
| `TIM15_CCR2` | `0x38` | TIM15 capture/compa re register 2 (TIM15_CCR2) | [TIM15_CCR2.json](../registers_json/TIM15_CCR2.json) |
| `TIM15_CNT` | `0x24` | Timers (TIM) TIM15_CNT Register | [TIM15_CNT.json](../registers_json/TIM15_CNT.json) |
| `TIM15_CR1` | `0x00` | TIM15 control register 1 (TIM15_CR1) | [TIM15_CR1.json](../registers_json/TIM15_CR1.json) |
| `TIM15_CR2` | `0x04` | TIM15 control register 2 (TIM15_CR2) | [TIM15_CR2.json](../registers_json/TIM15_CR2.json) |
| `TIM15_DCR` | `0x48` | TIM15 DMA cont rol register (TIM15_DCR) | [TIM15_DCR.json](../registers_json/TIM15_DCR.json) |
| `TIM15_DIER` | `0x0C` | TIM15 DMA/interrupt en able register (TIM15_DIER) | [TIM15_DIER.json](../registers_json/TIM15_DIER.json) |
| `TIM15_DMAR` | `0x4C` | Timers (TIM) TIM15_DMAR Register | [TIM15_DMAR.json](../registers_json/TIM15_DMAR.json) |
| `TIM15_EGR` | `0x14` | TIM15 event generation register (TIM15_EGR) | [TIM15_EGR.json](../registers_json/TIM15_EGR.json) |
| `TIM15_OR1` | `0x50` | Timers (TIM) TIM15_OR1 Register | [TIM15_OR1.json](../registers_json/TIM15_OR1.json) |
| `TIM15_OR2` | `0x60` | Timers (TIM) TIM15_OR2 Register | [TIM15_OR2.json](../registers_json/TIM15_OR2.json) |
| `TIM15_PSC` | `0x28` | Timers (TIM) TIM15_PSC Register | [TIM15_PSC.json](../registers_json/TIM15_PSC.json) |
| `TIM15_RCR` | `0x30` | TIM15 repetition co unter register (TIM15_RCR) | [TIM15_RCR.json](../registers_json/TIM15_RCR.json) |
| `TIM15_SMCR` | `0x08` | TIM15 slave mode cont rol register (TIM15_SMCR) | [TIM15_SMCR.json](../registers_json/TIM15_SMCR.json) |
| `TIM15_SR` | `0x10` | TIM15 status register (TIM15_SR) | [TIM15_SR.json](../registers_json/TIM15_SR.json) |
| `TIM16` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0438 Rev 8 1315/2187 RM0438 General-purpose time rs (TIM16) | [TIM16.json](../registers_json/TIM16.json) |
| `TIM16_OR1` | `0x50` | Timers (TIM) TIM16_OR1 Register | [TIM16_OR1.json](../registers_json/TIM16_OR1.json) |
| `TIM16_OR2` | `0x60` | Timers (TIM) TIM16_OR2 Register | [TIM16_OR2.json](../registers_json/TIM16_OR2.json) |
| `TIM17` | `0x04` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0438 Rev 8 1315/2187 RM0438 General-purpose time rs (TIM17) | [TIM17.json](../registers_json/TIM17.json) |
| `TIM17_OR1` | `0x50` | Timers (TIM) TIM17_OR1 Register | [TIM17_OR1.json](../registers_json/TIM17_OR1.json) |
| `TIM17_OR2` | `0x60` | Timers (TIM) TIM17_OR2 Register | [TIM17_OR2.json](../registers_json/TIM17_OR2.json) |
| `TIM1_ARR` | `0x2C` | Timers (TIM) TIM1_ARR Register | [TIM1_ARR.json](../registers_json/TIM1_ARR.json) |
| `TIM1_BDTR` | `0x44` | Timers (TIM) TIM1_BDTR Register | [TIM1_BDTR.json](../registers_json/TIM1_BDTR.json) |
| `TIM1_CCER` | `0x20` | Timers (TIM) TIM1_CCER Register | [TIM1_CCER.json](../registers_json/TIM1_CCER.json) |
| `TIM1_CCERCC1NE` | `0xCC1E` | Timers (TIM) TIM1_CCERCC1NE Register | [TIM1_CCERCC1NE.json](../registers_json/TIM1_CCERCC1NE.json) |
| `TIM1_CCMR1` | `0x18` | Timers (TIM) TIM1_CCMR1 Register | [TIM1_CCMR1.json](../registers_json/TIM1_CCMR1.json) |
| `TIM1_CCMR2` | `0x1C` | Timers (TIM) TIM1_CCMR2 Register | [TIM1_CCMR2.json](../registers_json/TIM1_CCMR2.json) |
| `TIM1_CCMR3` | `0x54` | Timers (TIM) TIM1_CCMR3 Register | [TIM1_CCMR3.json](../registers_json/TIM1_CCMR3.json) |
| `TIM1_CCR1` | `0x34` | Timers (TIM) TIM1_CCR1 Register | [TIM1_CCR1.json](../registers_json/TIM1_CCR1.json) |
| `TIM1_CCR2` | `0x38` | Timers (TIM) TIM1_CCR2 Register | [TIM1_CCR2.json](../registers_json/TIM1_CCR2.json) |
| `TIM1_CCR3` | `0x3C` | Timers (TIM) TIM1_CCR3 Register | [TIM1_CCR3.json](../registers_json/TIM1_CCR3.json) |
| `TIM1_CCR4` | `0x40` | Timers (TIM) TIM1_CCR4 Register | [TIM1_CCR4.json](../registers_json/TIM1_CCR4.json) |
| `TIM1_CCR5` | `0x58` | Timers (TIM) TIM1_CCR5 Register | [TIM1_CCR5.json](../registers_json/TIM1_CCR5.json) |
| `TIM1_CCR6` | `0x5C` | Timers (TIM) TIM1_CCR6 Register | [TIM1_CCR6.json](../registers_json/TIM1_CCR6.json) |
| `TIM1_CNT` | `0x24` | Timers (TIM) TIM1_CNT Register | [TIM1_CNT.json](../registers_json/TIM1_CNT.json) |
| `TIM1_CR1` | `0x00` | Timers (TIM) TIM1_CR1 Register | [TIM1_CR1.json](../registers_json/TIM1_CR1.json) |
| `TIM1_CR2` | `0x04` | Timers (TIM) TIM1_CR2 Register | [TIM1_CR2.json](../registers_json/TIM1_CR2.json) |
| `TIM1_DCR` | `0x48` | Timers (TIM) TIM1_DCR Register | [TIM1_DCR.json](../registers_json/TIM1_DCR.json) |
| `TIM1_DIER` | `0x0C` | Timers (TIM) TIM1_DIER Register | [TIM1_DIER.json](../registers_json/TIM1_DIER.json) |
| `TIM1_DMAR` | `0x4C` | Timers (TIM) TIM1_DMAR Register | [TIM1_DMAR.json](../registers_json/TIM1_DMAR.json) |
| `TIM1_EGR` | `0x14` | Timers (TIM) TIM1_EGR Register | [TIM1_EGR.json](../registers_json/TIM1_EGR.json) |
| `TIM1_OR1` | `0x50` | Timers (TIM) TIM1_OR1 Register | [TIM1_OR1.json](../registers_json/TIM1_OR1.json) |
| `TIM1_OR2` | `0x60` | Timers (TIM) TIM1_OR2 Register | [TIM1_OR2.json](../registers_json/TIM1_OR2.json) |
| `TIM1_OR3` | `0x64` | Timers (TIM) TIM1_OR3 Register | [TIM1_OR3.json](../registers_json/TIM1_OR3.json) |
| `TIM1_PSC` | `0x28` | Timers (TIM) TIM1_PSC Register | [TIM1_PSC.json](../registers_json/TIM1_PSC.json) |
| `TIM1_RCR` | `0x30` | Timers (TIM) TIM1_RCR Register | [TIM1_RCR.json](../registers_json/TIM1_RCR.json) |
| `TIM1_SMCR` | `0x08` | Timers (TIM) TIM1_SMCR Register | [TIM1_SMCR.json](../registers_json/TIM1_SMCR.json) |
| `TIM1_SR` | `0x10` | Timers (TIM) TIM1_SR Register | [TIM1_SR.json](../registers_json/TIM1_SR.json) |
| `TIM2` | `0x0900` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0438 Rev 8 1249/2187 RM0438 General-purpose timers (TIM2) | [TIM2.json](../registers_json/TIM2.json) |
| `TIM2_OR1` | `0x50` | Timers (TIM) TIM2_OR1 Register | [TIM2_OR1.json](../registers_json/TIM2_OR1.json) |
| `TIM2_OR2` | `0x60` | Timers (TIM) TIM2_OR2 Register | [TIM2_OR2.json](../registers_json/TIM2_OR2.json) |
| `TIM3` | `0x4845` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0438 Rev 8 1249/2187 RM0438 General-purpose timers (TIM3) | [TIM3.json](../registers_json/TIM3.json) |
| `TIM3_OR1` | `0x50` | Timers (TIM) TIM3_OR1 Register | [TIM3_OR1.json](../registers_json/TIM3_OR1.json) |
| `TIM3_OR2` | `0x60` | Timers (TIM) TIM3_OR2 Register | [TIM3_OR2.json](../registers_json/TIM3_OR2.json) |
| `TIM4` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0438 Rev 8 1249/2187 RM0438 General-purpose timers (TIM4) | [TIM4.json](../registers_json/TIM4.json) |
| `TIM5` | `0x00` | Offset Register name 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 RM0438 Rev 8 1249/2187 RM0438 General-purpose timers (TIM5) | [TIM5.json](../registers_json/TIM5.json) |
| `TIM6` | `0x00` | 02 03 04 05 06 0732 33 34 35 3631 01 CEN Auto-reload preload register Write a new value in TIMx_ARR RM0438 Rev 8 1345/2187 RM0438 Basic timers (TIM6) | [TIM6.json](../registers_json/TIM6.json) |
| `TIM7` | `0x00` | 02 03 04 05 06 0732 33 34 35 3631 01 CEN Auto-reload preload register Write a new value in TIMx_ARR RM0438 Rev 8 1345/2187 RM0438 Basic timers (TIM7) | [TIM7.json](../registers_json/TIM7.json) |
| `TIM8` | `0x00` | Counter register 3834 35 36 TIF RM0438 Rev 8 1129/2187 RM0438 Advanced-control timers (TIM8) | [TIM8.json](../registers_json/TIM8.json) |
| `TIM8_ARR` | `0x2C` | Timers (TIM) TIM8_ARR Register | [TIM8_ARR.json](../registers_json/TIM8_ARR.json) |
| `TIM8_BDTR` | `0x44` | Timers (TIM) TIM8_BDTR Register | [TIM8_BDTR.json](../registers_json/TIM8_BDTR.json) |
| `TIM8_CCER` | `0x20` | Timers (TIM) TIM8_CCER Register | [TIM8_CCER.json](../registers_json/TIM8_CCER.json) |
| `TIM8_CCMR1` | `0x18` | Timers (TIM) TIM8_CCMR1 Register | [TIM8_CCMR1.json](../registers_json/TIM8_CCMR1.json) |
| `TIM8_CCMR2` | `0x1C` | Timers (TIM) TIM8_CCMR2 Register | [TIM8_CCMR2.json](../registers_json/TIM8_CCMR2.json) |
| `TIM8_CCMR3` | `0x54` | Timers (TIM) TIM8_CCMR3 Register | [TIM8_CCMR3.json](../registers_json/TIM8_CCMR3.json) |
| `TIM8_CCR2` | `0x38` | Timers (TIM) TIM8_CCR2 Register | [TIM8_CCR2.json](../registers_json/TIM8_CCR2.json) |
| `TIM8_CCR3` | `0x3C` | Timers (TIM) TIM8_CCR3 Register | [TIM8_CCR3.json](../registers_json/TIM8_CCR3.json) |
| `TIM8_CCR4` | `0x40` | Timers (TIM) TIM8_CCR4 Register | [TIM8_CCR4.json](../registers_json/TIM8_CCR4.json) |
| `TIM8_CCR5` | `0x58` | Timers (TIM) TIM8_CCR5 Register | [TIM8_CCR5.json](../registers_json/TIM8_CCR5.json) |
| `TIM8_CCR6` | `0x5C` | Timers (TIM) TIM8_CCR6 Register | [TIM8_CCR6.json](../registers_json/TIM8_CCR6.json) |
| `TIM8_CNT` | `0x24` | Timers (TIM) TIM8_CNT Register | [TIM8_CNT.json](../registers_json/TIM8_CNT.json) |
| `TIM8_CR1` | `0x00` | Timers (TIM) TIM8_CR1 Register | [TIM8_CR1.json](../registers_json/TIM8_CR1.json) |
| `TIM8_CR2` | `0x04` | Timers (TIM) TIM8_CR2 Register | [TIM8_CR2.json](../registers_json/TIM8_CR2.json) |
| `TIM8_DCR` | `0x48` | Timers (TIM) TIM8_DCR Register | [TIM8_DCR.json](../registers_json/TIM8_DCR.json) |
| `TIM8_DIER` | `0x0C` | Timers (TIM) TIM8_DIER Register | [TIM8_DIER.json](../registers_json/TIM8_DIER.json) |
| `TIM8_DMAR` | `0x4C` | Timers (TIM) TIM8_DMAR Register | [TIM8_DMAR.json](../registers_json/TIM8_DMAR.json) |
| `TIM8_EGR` | `0x14` | Timers (TIM) TIM8_EGR Register | [TIM8_EGR.json](../registers_json/TIM8_EGR.json) |
| `TIM8_OR2` | `0x60` | Timers (TIM) TIM8_OR2 Register | [TIM8_OR2.json](../registers_json/TIM8_OR2.json) |
| `TIM8_OR3` | `0x64` | Timers (TIM) TIM8_OR3 Register | [TIM8_OR3.json](../registers_json/TIM8_OR3.json) |
| `TIM8_PSC` | `0x28` | Timers (TIM) TIM8_PSC Register | [TIM8_PSC.json](../registers_json/TIM8_PSC.json) |
| `TIM8_RCR` | `0x30` | Timers (TIM) TIM8_RCR Register | [TIM8_RCR.json](../registers_json/TIM8_RCR.json) |
| `TIM8_SMCR` | `0x08` | Timers (TIM) TIM8_SMCR Register | [TIM8_SMCR.json](../registers_json/TIM8_SMCR.json) |
| `TIM8_SR` | `0x10` | Timers (TIM) TIM8_SR Register | [TIM8_SR.json](../registers_json/TIM8_SR.json) |