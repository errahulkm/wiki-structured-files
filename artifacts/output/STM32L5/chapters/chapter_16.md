# Chapter 16: Nested vectored interrupt controller (NVIC)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 16: Nested vectored interrupt controller (NVIC).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 528 - 532
* **Taxonomy Section**: CORE
* **Parent IP Module**: [Interrupts and Events (NVIC/EXTI)](../core/interrupts.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
Nested vectored interrupt controller (NVIC) RM0438
528/2187 RM0438 Rev 8
16 Nested vectored interrupt controller (NVIC)
16.1 NVIC main features
• 109 maskable interrupt channels (not including the 16 Cortex®-M33 with FPU interrupt
lines)
• 8 programmable priority levels (3 bits of interrupt priority are used)
• Low-latency exception and interrupt handling
• Power management control
• Implementation of system control registers
The NVIC and the processor core interface are closely coupled, which enables low latency
interrupt processing and efficient processing of late arriving interrupts.
The NVIC registers are banked across secure and non-secure states.
All interrupts including the core exceptions are managed by the NVIC.
16.2 SysTick calibra tion value register
The Cortex®-M33 with TrustZone mainline security extension embeds two SysTick timers.
When TrustZone is activated, two SysTick timer are available:
• SysTick, secure instance.
• SysTick, non-secure instance.
When TrustZone is disabeld, only one SysTick timer is available.
The SysTick timer calibration value (STCALIB) is 0x3E8. It gives a reference time base of
1 ms based on a SysTick clock frequency of 1 MHz. In order to match the 1 ms time base
for an application Running at a given frequency, the SysTick reload value must be
programmed as follows in the SYST_RVR register:
• SysTick clock source is CPU clock HCLK: reload value = (HCLK x STCALIB)-1
• SysTick clock source is external clock (HCLK/8): reload value =
((HCLK/8) x STCALIB)-1
The HCLK refers to AHB frequency value in MHz.
Example: SysTick clock source is CPU clock HCLK of 100 MHz, to match a time base of
1 ms:
• SysTick reload value = (100 x STCALIB) -1 = 0x1869F

RM0438 Rev 8 529/2187
RM0438 Nested vectored interrupt controller (NVIC)
562
16.3 Interrupt an d exception vectors
The grey rows in [Table 109](../tables/table_109.md) describe the vectors without specific position.
[Table 109](../tables/table_109.md). STM32L552xx and STM32L562xx vector table
Position
Priority
Type of
priority Acronym Description Address
- - - - Reserved 0x0000 0000
- -4 Fixed Reset Reset 0x0000 0004
- -2 Fixed NMI Non maskable interrupt. SRAM parity err +
FLASH ECC err + HSE CSS 0x0000 0008
- -3 or
-1 Fixed Secure HardFault Secure hard fault 0x0000 000C
- -1 Fixed Non-secure
HardFault Non-secure hard fault. All classes of fault 0x0000 000C
- 0 Settable MemManage Memory management 0x0000 0010
- 1 Settable BusFault Pre-fetch fault, memory access fault 0x0000 0014
- 2 Settable UsageFault Undefined instruction or illegal state 0x0000 0018
- 3 Settable SecureFault Secure fault 0x0000 001C
- - - - Reserved 0x0000 0020 -
0x0000 0028
- 4 - SVC System service call via SWI instruction 0x0000 002C
- 5 - Debug Monitor Debug monitor 0x0000 0030
- - - - Reserved 0x0000 0034
- 6 Settable PendSV Pendable request for system service 0x0000 0038
- 7 Settable SysTick System tick timer 0x0000 003C
0 8 Settable WWDG Window watchdog interrupt 0x0000 0040
1 9 Settable PDV_PVM PVD/PVM1/PVM2/PVM3/PVM4 through EXTI
lines 16/35/36/37/38 interrupts 0x0000 0044
2 10 Settable RTC RTC global interrupts (EXTI line 17) 0x0000 0048
3 11 Settable RTC_S RTC secure global interrupts (EXTI line 18) 0x0000 004C
4 12 Settable TAMP Tamper global interrupt (EXTI line 19) 0x0000 0050
5 13 Settable TAMP_S Tamper secure global interrupt (EXTI line 20) 0x0000 0054
6 14 Settable FLASH Flash memory global interrupt 0x0000 0058
7 15 Settable FLASH_S Flash memory secure global interrupt 0x0000 005C
8 16 Settable GTZC TZIC secure global interrupt 0x0000 0060
9 17 Settable RCC RCC global interrupt 0x0000 0064
10 18 Settable RCC_S RCC secure global interrupt 0x0000 0068

Nested vectored interrupt controller (NVIC) RM0438
530/2187 RM0438 Rev 8
11 19 Settable EXTI0 EXTI Line0 interrupt 0x0000 006C
12 20 Settable EXTI1 EXTI Line1 interrupt 0x0000 0070
13 21 Settable EXTI2 EXTI Line2 interrupt 0x0000 0074
14 22 Settable EXTI3 EXTI Line3 interrupt 0x0000 0078
15 23 Settable EXTI4 EXTI Line4 interrupt 0x0000 007C
16 24 Settable EXTI5 EXTI Line5 interrupt 0x0000 0080
17 25 Settable EXTI6 EXTI Line6 interrupt 0x0000 0084
18 26 Settable EXTI7 EXTI Line7 interrupt 0x0000 0088
19 27 Settable EXTI8 EXTI Line8 interrupt 0x0000 008C
20 28 Settable EXTI9 EXTI Line9 interrupt 0x0000 0090
21 29 Settable EXTI10 EXTI Line10 interrupt 0x0000 0094
22 30 Settable EXTI11 EXTI Line11 interrupt 0x0000 0098
23 31 Settable EXTI12 EXTI Line12 interrupt 0x0000 009C
24 32 Settable EXTI13 EXTI Line13 interrupt 0x0000 00E4
25 33 Settable EXTI14 EXTI Line14 interrupt 0x0000 00A0
26 34 Settable EXTI15 EXTI Line15 interrupt 0x0000 00A4
27 35 Settable DMAMUX1_OVR DMAMUX 1 overRun interrupt 0x0000 00A8
28 36 Settable DMAMUX1_OVR_S DMAMUX1 secure overRun interrupt 0x0000 00AC
29 37 Settable DMA1_CH1 DMA1 channel 1 interrupt 0x0000 00B0
30 38 Settable DMA1_CH2 DMA1 channel 2 interrupt 0x0000 00B4
31 39 Settable DMA1_CH3 DMA1 channel 3 interrupt 0x0000 00B8
32 40 Settable DMA1_CH4 DMA1 channel 4 interrupt 0x0000 00C0
33 41 Settable DMA1_CH5 DMA1 channel 5 interrupt 0x0000 00C4
34 42 Settable DMA1_CH6 DMA1 channel 6 interrupt 0x0000 00C8
35 43 Settable DMA1_CH7 DMA1 channel 7 interrupt 0x0000 00CC
36 44 Settable DMA1_CH8 DMA1 channel 8 interrupt 0x0000 00D0
37 45 Settable ADC1_2 ADC1_2 global interrupt 0x0000 00D4
38 46 Settable DAC DAC global interrupt 0x0000 00D8
39 47 Settable FDCAN1_IT0 FDCAN1 Interrupt 0 0x0000 00DC
40 48 Settable FDCAN1_IT1 FDCAN1 Interrupt 1 0x0000 00E0
41 49 Settable TIM1_BRK TIM1 break 0x0000 00E4
42 50 Settable TIM1_UP TIM1 update 0x0000 00E8
43 51 Settable TIM1_TRG_COM TIM1 trigger and commutation 0x0000 00EC
[Table 109](../tables/table_109.md). STM32L552xx and STM32L562xx vector table (continued)
Position
Priority
Type of
priority Acronym Description Address

RM0438 Rev 8 531/2187
RM0438 Nested vectored interrupt controller (NVIC)
562
44 52 Settable TIM1_CC TIM1 capture compare interrupt 0x0000 00F0
45 53 Settable TIM2 TIM2 global interrupt 0x0000 00F4
46 54 Settable TIM3 TIM3 global interrupt 0x0000 00F8
47 55 Settable TIM4 TIM4 global interrupt 0x0000 00FC
48 56 Settable TIM5 TIM5 global interrupt 0x0000 0100
49 57 Settable TIM6 TIM6 global interrupt 0x0000 0104
50 58 Settable TIM7 TIM7 global interrupt 0x0000 0108
51 59 Settable TIM8_BRK TIM8 break interrupt 0x0000 010C
52 60 Settable TIM8_UP TIM8 update interrupt 0x0000 0110
53 61 Settable TIM8_TRG_COM TIM8 trigger and commutation interrupt 0x0000 0114
54 62 Settable TIM8_CC TIM8 capture compare interrupt 0x0000 0118
55 63 Settable I2C1_EV I2C1 event interrupt 0x0000 011C
56 64 Settable I2C1_ER I2C1 error interrupt 0x0000 0120
57 65 Settable I2C2_EV I2C2 event interrupt 0x0000 0124
58 66 Settable I2C2_ER I2C2 error interrupt 0x0000 0128
59 67 Settable SPI1 SPI1 global interrupt 0x0000 012C
60 68 Settable SPI2 SPI2 global interrupt 0x0000 0130
61 69 Settable USART1 USART1 global interrupt 0x0000 0134
62 70 Settable USART2 USART2 global interrupt 0x0000 0138
63 71 Settable USART3 USART3 global interrupt 0x0000 013C
64 72 Settable UART4 UART4 global interrupt 0x0000 0140
65 73 Settable UART5 UART5 global interrupt 0x0000 0144
66 74 Settable LPUART1 LPUART1 global interrupt 0x0000 0148
67 75 Settable LPTIM1 LPTIM1 global interrupt 0x0000 014C
68 76 Settable LPTIM2 LPTIM2 global interrupt 0x0000 0150
69 77 Settable TIM15 TIM15 global interrupt 0x0000 0154
70 78 Settable TIM16 TIM16 global interrupt 0x0000 0158
71 79 Settable TIM17 TIM16 global interrupt 0x0000 015C
72 80 Settable COMP COMP1/COMP2 through EXTI lines 21/22
interrupts 0x0000 0160
73 81 Settable USB_FS USB FS global interrupt 0x0000 0164
74 82 Settable CRS Clock recovery syst em global interrupt 0x0000 0168
75 83 Settable FMC FMC global interrupt 0x0000 016C
[Table 109](../tables/table_109.md). STM32L552xx and STM32L562xx vector table (continued)
Position
Priority
Type of
priority Acronym Description Address

Nested vectored interrupt controller (NVIC) RM0438
532/2187 RM0438 Rev 8
76 84 Settable OCTOSPI1 OCTOSPI1 global interrupt 0x0000 0170
77 85 Settable - Reserved 0x0000 0174
78 86 Settable SDMMC1 SDMMC1 global interrupt 0x0000 0178
79 87 Settable - Reserved 0x0000 017C
80 88 Settable DMA2_CH1 DMA2 channel 1 interrupt 0x0000 0180
81 89 Settable DMA2_CH2 DMA2 channel 2 interrupt 0x0000 0184
82 90 Settable DMA2_CH3 DMA2 channel 3 interrupt 0x0000_0188
83 91 Settable DMA2_CH4 DMA2 channel 4 interrupt 0x0000 0174
84 92 Settable DMA2_CH5 DMA2 channel 5 interrupt 0x0000 0178
85 93 Settable DMA2_CH6 DMA2 channel 6 interrupt 0x0000 017C
86 94 Settable DMA2_CH7 DMA2 channel 7 interrupt 0x0000 0180
87 95 Settable DMA2_CH8 DMA2 channel 8 interrupt 0x0000 0184
88 96 Settable I2C3_EV I2C3 event interrupt 0x0000 0188
89 97 Settable I2C3_ER I2C3 error interrupt 0x0000 018C
90 98 Settable SAI1 SAI1 global interrupt 0x0000 0190
91 99 Settable SAI2 SAI2 global interrupt 0x0000 0194
92 100 Settable TSC TSC global interrupt 0x0000 0198
93 101 Settable AES AES global interrupt 0x0000 019C
94 102 Settable RNG RNG global interrupt 0x0000 01A0
95 103 Settable FPU Floating point interrupt 0x0000 01A4
96 104 Settable HASH HASH interrupt 0x0000 01A8
97 105 Settable PKA PKA global interrupt 0x0000 01AC
98 106 Settable LPTIM3 LPTIM3 global interrupt 0x0000 01A0
99 107 Settable SPI3 SPI3 global interrupt 0x0000 01A4
100 108 Settable I2C4_ER I2C4 error interrupt 0x0000 01A8
101 109 Settable I2C4_EV I2C4 event interrupt 0x0000 01AC
102 110 Settable DFSDM1_FLT0 DFSDM1 fi lter 0 global interrupt 0x0000 01B0
103 111 Settable DFSDM1_FLT1 DFSDM1 fi lter 0 global interrupt 0x0000 01B4
104 112 Settable DFSDM1_FLT2 DFSDM1 fi lter 0 global interrupt 0x0000 01B8
105 113 Settable DFSDM1_FLT3 DFSDM1 filter 0 global interrupt 0x0000 01BC
106 114 Settable UCPD1 UCPD1 global interrupt 0x0000 01C0
107 115 Settable ICACHE Instruction cache global interrupt 0x0000 01C4
108 116 Settable OTFDEC1 OTFDEC1 secure global interrupt 0x0000 01C8
[Table 109](../tables/table_109.md). STM32L552xx and STM32L562xx vector table (continued)
Position
Priority
Type of
priority Acronym Description Address
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* [Table 109: Configuration Matrix](../tables/table_109.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)