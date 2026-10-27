# Timers (TIM)

## 1. Overview & Key Features
The Timers (TIM) block provides complete operational functionality for the STM32F4 microcontroller.
Documented in [Chapter 20](../chapters/chapter_20.md), [Chapter 21](../chapters/chapter_21.md), [Chapter 22](../chapters/chapter_22.md), [Chapter 23](../chapters/chapter_23.md) (Pages 515 - 585).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 20](../chapters/chapter_20.md), [Chapter 21](../chapters/chapter_21.md), [Chapter 22](../chapters/chapter_22.md), [Chapter 23](../chapters/chapter_23.md)
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
| `TIM` | `0x2C` | Timers (TIM) TIM Register | [TIM.json](../registers_json/TIM.json) |
| `TIM1_CCER` | `0xCC1E` | Timers (TIM) TIM1_CCER Register | [TIM1_CCER.json](../registers_json/TIM1_CCER.json) |
| `TIM1_CCERCC1NE` | `0xCC1E` | Timers (TIM) TIM1_CCERCC1NE Register | [TIM1_CCERCC1NE.json](../registers_json/TIM1_CCERCC1NE.json) |
| `TIM2_OR` | `0x50` | TIM2 option register (TIM2_OR) | [TIM2_OR.json](../registers_json/TIM2_OR.json) |
| `TIM5_OR` | `0x50` | TIM5 option register (TIM5_OR) | [TIM5_OR.json](../registers_json/TIM5_OR.json) |
| `TIMER1` | `0x4845` | Timers (TIM) TIMER1 Register | [TIMER1.json](../registers_json/TIMER1.json) |
| `TIMER2` | `0x0900` | Timers (TIM) TIMER2 Register | [TIMER2.json](../registers_json/TIMER2.json) |
| `TIMX_ARR` | `0x2C` | TIM6 and TIM7 auto-r eload register (TIMX_ARR) | [TIMX_ARR.json](../registers_json/TIMX_ARR.json) |
| `TIMX_BDTR` | `0x44` | TIM1 and TIM8 break and dead-time register (TIMX_BDTR) | [TIMX_BDTR.json](../registers_json/TIMX_BDTR.json) |
| `TIMX_CCER` | `0x20` | TIM10/11/13/14 capture/comp are enable register (TIMX_CCER) | [TIMX_CCER.json](../registers_json/TIMX_CCER.json) |
| `TIMX_CCMR1` | `0x18` | TIM10/11/13/14 capture/compar e mode register 1 (TIMX_CCMR1) | [TIMX_CCMR1.json](../registers_json/TIMX_CCMR1.json) |
| `TIMX_CCMR2` | `0x1C` | TIMx capture/compare m ode register 2 (TIMX_CCMR2) | [TIMX_CCMR2.json](../registers_json/TIMX_CCMR2.json) |
| `TIMX_CCR1` | `0x34` | TIM10/11/13/14 capture/ compare register 1 (TIMX_CCR1) | [TIMX_CCR1.json](../registers_json/TIMX_CCR1.json) |
| `TIMX_CCR2` | `0x38` | TIM9/12 capture/compare register 2 (TIMX_CCR2) | [TIMX_CCR2.json](../registers_json/TIMX_CCR2.json) |
| `TIMX_CCR3` | `0x3C` | TIMx capture/compa re register 3 (TIMX_CCR3) | [TIMX_CCR3.json](../registers_json/TIMX_CCR3.json) |
| `TIMX_CCR4` | `0x40` | TIMx capture/compa re register 4 (TIMX_CCR4) | [TIMX_CCR4.json](../registers_json/TIMX_CCR4.json) |
| `TIMX_CR1` | `0x00` | TIM6 and TIM7 cont rol register 1 (TIMX_CR1) | [TIMX_CR1.json](../registers_json/TIMX_CR1.json) |
| `TIMX_CR2` | `0x04` | TIM6 and TIM7 cont rol register 2 (TIMX_CR2) | [TIMX_CR2.json](../registers_json/TIMX_CR2.json) |
| `TIMX_DCR` | `0x48` | TIMx DMA contro l register (TIMX_DCR) | [TIMX_DCR.json](../registers_json/TIMX_DCR.json) |
| `TIMX_DIER` | `0x0C` | TIM6 and TIM7 DMA/Interr upt enable register (TIMX_DIER) | [TIMX_DIER.json](../registers_json/TIMX_DIER.json) |
| `TIMX_EGR` | `0x14` | TIM6 and TIM7 event ge neration register (TIMX_EGR) | [TIMX_EGR.json](../registers_json/TIMX_EGR.json) |
| `TIMX_RCR` | `0x30` | TIM1 and TIM8 repeti tion counter register (TIMX_RCR) | [TIMX_RCR.json](../registers_json/TIMX_RCR.json) |
| `TIMX_SMCR` | `0x08` | TIM9/12 slave mode c ontrol register (TIMX_SMCR) | [TIMX_SMCR.json](../registers_json/TIMX_SMCR.json) |
| `TIMX_SR` | `0x10` | TIM6 and TIM7 stat us register (TIMX_SR) | [TIMX_SR.json](../registers_json/TIMX_SR.json) |