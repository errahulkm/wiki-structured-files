# Chapter 1: Contents

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32F4 Reference Manual RM0090 - Chapter 1: Contents.
* **Document Source**: RM0090 Reference Manual
* **PDF Reference Location**: Pages 2 - 39
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0090 Ingestion)
```text
Contents RM0090
2/1741 RM0090 Rev 22
Contents
1 Documentation conventions  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
1.1 List of abbreviations for registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
1.2 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
1.3 Peripheral availability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
2 Memory and bus architecture  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
2.1 System architecture  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
2.1.1 I-bus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
2.1.2 D-bus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
2.1.3 S-bus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
2.1.4 DMA memory bus  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
2.1.5 DMA peripheral bus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
2.1.6 Ethernet DMA bus  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
2.1.7 USB OTG HS DMA bus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
2.1.8 LCD-TFT controller DMA bus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
2.1.9 DMA2D bus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
2.1.10 BusMatrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
2.1.11 AHB/APB bridges (APB)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
2.2 Memory organization  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
2.3 Memory map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
2.3.1 Embedded SRAM  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
2.3.2 Flash memory overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
2.3.3 Bit banding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
2.4 Boot configuration  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
3 Embedded flash memory interfac e  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
3.1 Introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
3.2 Main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
3.3 Embedded flash memory in
STM32F405xx/07xx and STM32F415xx/17xx . . . . . . . . . . . . . . . . . . . . . 74
3.4 Embedded flash memory in STM32F42xxx and STM32F43xxx  . . . . . . . 76
3.5 Read interface  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
3.5.1 Relation between CPU clock frequenc y and flash memory read time . . 80

RM0090 Rev 22 3/1741
RM0090 Contents
39
3.5.2 Adaptive real-time memory accelerato r (ART Accelerator™)  . . . . . . . . 82
3.6 Erase and program operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
3.6.1 Unlocking the Flash control register  . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
3.6.2 Program/erase parallelism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
3.6.3 Erase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
3.6.4 Programming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
3.6.5 Read-while-write (RWW) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
3.6.6 Interrupts  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
3.7 Option bytes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
3.7.1 Description of user option bytes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
3.7.2 Programming user option bytes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
3.7.3 Read protection (RDP)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
3.7.4 Write protections  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
3.7.5 Proprietary code readout protection (PCRO P)  . . . . . . . . . . . . . . . . . . . 95
3.8 One-time programmable bytes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
3.9 Flash interface registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
3.9.1 Flash access control register (FLASH_ACR)
for STM32F405xx/07xx and STM32F415xx/17xx  . . . . . . . . . . . . . . . . . 98
3.9.2 Flash access control register (FLASH_ACR)
for STM32F42xxx and STM32F43xxx . . . . . . . . . . . . . . . . . . . . . . . . . . 99
3.9.3 Flash key register (FLASH_KEYR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
3.9.4 Flash option key register (FLASH_OPTKEYR) . . . . . . . . . . . . . . . . . . 100
3.9.5 Flash status regi ster (FLASH_SR) for
STM32F405xx/07xx and STM32F415xx/17xx . . . . . . . . . . . . . . . . . . . 101
3.9.6 Flash status register (FLASH_SR) for
STM32F42xxx and STM32F43xxx  . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
3.9.7 Flash control register (FLASH_CR) for
STM32F405xx/07xx and STM32F415xx/17xx . . . . . . . . . . . . . . . . . . . 103
3.9.8 Flash control register (FLASH_CR) for
STM32F42xxx and STM32F43xxx  . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
3.9.9 Flash option control register (FLASH_OPTCR) for
STM32F405xx/07xx and STM32F415xx/17xx . . . . . . . . . . . . . . . . . . . 106
3.9.10 Flash option control register (FLASH_OPTCR)
for STM32F42xxx and STM32F43xxx . . . . . . . . . . . . . . . . . . . . . . . . . 108
3.9.11 Flash option control register (FLASH_OPTCR1)
for STM32F42xxx and STM32F43xxx . . . . . . . . . . . . . . . . . . . . . . . . . 110
3.9.12 Flash interface register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
4 CRC calculation unit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113

Contents RM0090
4/1741 RM0090 Rev 22
4.1 CRC introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .113
4.2 CRC main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .113
4.3 CRC functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .114
4.4 CRC registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .114
4.4.1 Data register (CRC_DR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
4.4.2 Independent data register (CRC_IDR)  . . . . . . . . . . . . . . . . . . . . . . . . 114
4.4.3 Control register (CRC_CR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
4.4.4 CRC register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
5 Power controller (PWR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
5.1 Power supplies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .116
5.1.1 Independent A/D converte r supply and reference voltage . . . . . . . . . . 117
5.1.2 Battery backup domain  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
5.1.3 Voltage regulator for STM32F405xx/07xx and STM32F415xx/17xx . . 120
5.1.4 Voltage regulator fo r STM32F42xxx and STM32F43xxx . . . . . . . . . . . 121
5.2 Power supply supervisor  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
5.2.1 Power-on reset (POR)/power-down reset (PDR) . . . . . . . . . . . . . . . . . 124
5.2.2 Brownout reset (BOR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
5.2.3 Programmable voltage detector (PVD)  . . . . . . . . . . . . . . . . . . . . . . . . 125
5.3 Low-power modes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
5.3.1 Slowing down system clocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
5.3.2 Peripheral clock gating  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
5.3.3 Sleep mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
5.3.4 Stop mode (STM32F405xx/07xx and STM32F415xx/17xx)  . . . . . . . . 130
5.3.5 Stop mode (STM32F42xxx and STM32F43xxx)  . . . . . . . . . . . . . . . . . 133
5.3.6 Standby mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
5.3.7 Programming the RTC alternate f unctions to wake up the device from
the Stop and Standby modes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
5.4 Power control registers (STM32F405xx/07xx and STM32F415xx/17xx) 141
5.4.1 PWR power control register (PWR_CR)
for STM32F405xx/07xx and STM32F415xx/17xx  . . . . . . . . . . . . . . . . 141
5.4.2 PWR power control/status register (PWR_CSR)
for STM32F405xx/07xx and STM32F415xx/17xx  . . . . . . . . . . . . . . . . 142
5.5 Power control registers (STM32F42xxx and STM32F43xxx) . . . . . . . . . 145
5.5.1 PWR power control register (PWR_CR)
for STM32F42xxx and STM32F43xxx . . . . . . . . . . . . . . . . . . . . . . . . . 145
5.5.2 PWR power control/status register (PWR_CSR)
for STM32F42xxx and STM32F43xxx . . . . . . . . . . . . . . . . . . . . . . . . . 148

RM0090 Rev 22 5/1741
RM0090 Contents
39
5.6 PWR register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
6 Reset and clock control for
STM32F42xxx and STM32F43xxx (RCC) . . . . . . . . . . . . . . . . . . . . . . . 151
6.1 Reset  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
6.1.1 System reset  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
6.1.2 Power reset  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
6.1.3 Backup domain reset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
6.2 Clocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
6.2.1 HSE clock  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
6.2.2 HSI clock  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
6.2.3 PLL configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
6.2.4 LSE clock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
6.2.5 LSI clock  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
6.2.6 System clock (SYSCLK ) selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
6.2.7 Clock security system (CSS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
6.2.8 RTC/AWU clock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
6.2.9 Watchdog clock  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
6.2.10 Clock-out capability  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
6.2.11 Internal/external clock measurement using TIM5/TIM11 . . . . . . . . . . . 159
6.3 RCC registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
6.3.1 RCC clock control register (RCC_CR) . . . . . . . . . . . . . . . . . . . . . . . . . 162
6.3.2 RCC PLL configuration register (RCC_PLLCFGR) . . . . . . . . . . . . . . . 164
6.3.3 RCC clock configuration register (RCC_CFGR)  . . . . . . . . . . . . . . . . . 166
6.3.4 RCC clock interrupt register (RCC_CIR) . . . . . . . . . . . . . . . . . . . . . . . 168
6.3.5 RCC AHB1 peripheral reset register (RCC_AHB1RSTR) . . . . . . . . . . 171
6.3.6 RCC AHB2 peripheral reset register (RCC_AHB2RSTR) . . . . . . . . . . 174
6.3.7 RCC AHB3 peripheral reset register (RCC_AHB3RSTR) . . . . . . . . . . 175
6.3.8 RCC APB1 periph eral reset register (RCC_APB1RSTR)  . . . . . . . . . . 175
6.3.9 RCC APB2 periph eral reset register (RCC_APB2RSTR)  . . . . . . . . . . 179
6.3.10 RCC AHB1 peripheral clock register  (RCC_AHB1ENR) . . . . . . . . . . . 181
6.3.11 RCC AHB2 peripheral clock enable register (RCC_AHB2ENR)  . . . . . 183
6.3.12 RCC AHB3 peripheral clock enable register (RCC_AHB3ENR)  . . . . . 184
6.3.13 RCC APB1 peripheral clock enable register (RCC_APB1ENR)  . . . . . 184
6.3.14 RCC APB2 peripheral clock enable register (RCC_APB2ENR)  . . . . . 188
6.3.15 RCC AHB1 peripheral clock enable in low power mode register
(RCC_AHB1LPENR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190

Contents RM0090
6/1741 RM0090 Rev 22
6.3.16 RCC AHB2 peripheral clock enable in low power mode register
(RCC_AHB2LPENR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
6.3.17 RCC AHB3 peripheral clock enable in low power mode register
(RCC_AHB3LPENR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
6.3.18 RCC APB1 peripheral  clock enable in low power mode register
(RCC_APB1LPENR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
6.3.19 RCC APB2 peripher al clock enabled in low power mode register
(RCC_APB2LPENR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
6.3.20 RCC Backup domain control register (RCC_BDCR) . . . . . . . . . . . . . . 200
6.3.21 RCC clock control & status register (RCC_CSR)  . . . . . . . . . . . . . . . . 201
6.3.22 RCC spread spectrum clock generation register (RCC_SSCGR) . . . . 203
6.3.23 RCC PLLI2S configuration register (RCC_PLLI2SCFGR)  . . . . . . . . . 204
6.3.24 RCC PLL configuration register (RCC _PLLSAICFGR)  . . . . . . . . . . . . 207
6.3.25 RCC Dedicated Clock Configuratio n Register (RCC_DCKCFGR)  . . . 208
6.3.26 RCC register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
7 Reset and clock control for
STM32F405xx/07xx and STM32F415xx/17xx(RCC)  . . . . . . . . . . . . . . 214
7.1 Reset  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
7.1.1 System reset  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
7.1.2 Power reset  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215
7.1.3 Backup domain reset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215
7.2 Clocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
7.2.1 HSE clock  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218
7.2.2 HSI clock  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219
7.2.3 PLL configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220
7.2.4 LSE clock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220
7.2.5 LSI clock  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
7.2.6 System clock (SYSCLK ) selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
7.2.7 Clock security system (CSS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
7.2.8 RTC/AWU clock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
7.2.9 Watchdog clock  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
7.2.10 Clock-out capability  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
7.2.11 Internal/external clock measurement using TIM5/TIM11 . . . . . . . . . . . 223
7.3 RCC registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225
7.3.1 RCC clock control register (RCC_CR) . . . . . . . . . . . . . . . . . . . . . . . . . 225
7.3.2 RCC PLL configuration register (RCC_PLLCFGR) . . . . . . . . . . . . . . . 227
7.3.3 RCC clock configuration register (RCC_CFGR)  . . . . . . . . . . . . . . . . . 229

RM0090 Rev 22 7/1741
RM0090 Contents
39
7.3.4 RCC clock interrupt register (RCC_CIR) . . . . . . . . . . . . . . . . . . . . . . . 231
7.3.5 RCC AHB1 peripheral reset register (RCC_AHB1RSTR) . . . . . . . . . . 234
7.3.6 RCC AHB2 peripheral reset register (RCC_AHB2RSTR) . . . . . . . . . . 237
7.3.7 RCC AHB3 peripheral reset register (RCC_AHB3RSTR) . . . . . . . . . . 238
7.3.8 RCC APB1 periph eral reset register (RCC_APB1RSTR)  . . . . . . . . . . 238
7.3.9 RCC APB2 periph eral reset register (RCC_APB2RSTR)  . . . . . . . . . . 241
7.3.10 RCC AHB1 peripheral clock enable register (RCC_AHB1ENR)  . . . . . 243
7.3.11 RCC AHB2 peripheral clock enable register (RCC_AHB2ENR)  . . . . . 245
7.3.12 RCC AHB3 peripheral clock enable register (RCC_AHB3ENR)  . . . . . 246
7.3.13 RCC APB1 peripheral  clock enable register
(RCC_APB1ENR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246
7.3.14 RCC APB2 peripheral clock enable register (RCC_APB2ENR)  . . . . . 249
7.3.15 RCC AHB1 peripheral clock enable in low power mode register
(RCC_AHB1LPENR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251
7.3.16 RCC AHB2 peripheral clock enable in low power mode register
(RCC_AHB2LPENR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
7.3.17 RCC AHB3 peripheral clock enable in low power mode register
(RCC_AHB3LPENR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
7.3.18 RCC APB1 peripheral  clock enable in low power mode register
(RCC_APB1LPENR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255
7.3.19 RCC APB2 peripheral cloc k enabled in low power mode
register (RCC_APB2LPENR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
7.3.20 RCC Backup domain control register (RCC_BDCR) . . . . . . . . . . . . . . 260
7.3.21 RCC clock control & status register (RCC_CSR)  . . . . . . . . . . . . . . . . 261
7.3.22 RCC spread spectrum clock generation register (RCC_SSCGR) . . . . 263
7.3.23 RCC PLLI2S configuration register (RCC_PLLI2SCFGR)  . . . . . . . . . 264
7.3.24 RCC register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266
8 General-purpose I/Os (GPIO) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
8.1 GPIO introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
8.2 GPIO main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
8.3 GPIO functional description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
8.3.1 General-purpose I/O (GPIO)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
8.3.2 I/O pin multiplexer and mapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
8.3.3 I/O port control registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
8.3.4 I/O port data registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
8.3.5 I/O data bitwise handling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
8.3.6 GPIO locking mechanism  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
8.3.7 I/O alternate function input/output  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277

Contents RM0090
8/1741 RM0090 Rev 22
8.3.8 External interrupt/wake-up li nes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
8.3.9 Input configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
8.3.10 Output configuration  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
8.3.11 Alternate function configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
8.3.12 Analog configuration  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
8.3.13 Using the OSC32_IN/OSC32_O UT pins as GPIO PC14/PC15
port pins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
8.3.14 Using the OSC_IN/OSC_OUT pins as  GPIO PH0/PH1 port pins  . . . . 280
8.3.15 Selection of RTC_AF1 and RTC_AF2 alternate functions . . . . . . . . . . 281
8.4 GPIO registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 283
8.4.1 GPIO port mode register (GPIOx_MODER) (x = A..I/J/K) . . . . . . . . . . 283
8.4.2 GPIO port output type register (GPIOx_OTYPER)
(x = A..I/J/K) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 283
8.4.3 GPIO port output spee d register (GPIOx_OSPEEDR)
(x = A..I/J/K) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 284
8.4.4 GPIO port pull-up/pull- down register (GPIOx_PUPDR)
(x = A..I/J/K) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 284
8.4.5 GPIO port input data register (GPIOx_IDR) (x = A..I/J/K)  . . . . . . . . . . 285
8.4.6 GPIO port output data register (GPIOx_ODR) (x = A..I/J/K)  . . . . . . . . 285
8.4.7 GPIO port bit set/reset register (GPIOx_BSRR) (x = A..I/J/K) . . . . . . . 286
8.4.8 GPIO port configuratio n lock register (GPIOx_LCKR)
(x = A..I/J/K) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
8.4.9 GPIO alternate function low register  (GPIOx_AFRL) (x = A..I/J/K)  . . . 287
8.4.10 GPIO alternate function  high register (GPIOx_AFRH)
(x = A..I/J) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288
8.4.11 GPIO register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
9 System configuration controll er (SYSCFG)  . . . . . . . . . . . . . . . . . . . . 291
9.1 I/O compensation cell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
9.2 SYSCFG registers for STM32F405xx/07xx and STM32F415xx/17xx  . . 291
9.2.1 SYSCFG memory remap register (SYSCFG_MEMRMP) . . . . . . . . . . 291
9.2.2 SYSCFG peripheral mode  configuration register (SYSCFG_PMC)  . . 292
9.2.3 SYSCFG external interrup t configuration register 1
(SYSCFG_EXTICR1)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
9.2.4 SYSCFG external interrup t configuration register 2
(SYSCFG_EXTICR2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
9.2.5 SYSCFG external interrup t configuration register 3
(SYSCFG_EXTICR3)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294
9.2.6 SYSCFG external interrup t configuration register 4
(SYSCFG_EXTICR4)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295

RM0090 Rev 22 9/1741
RM0090 Contents
39
9.2.7 Compensation ce ll control register (SYSCFG_CMPCR) . . . . . . . . . . . 295
9.2.8 SYSCFG register maps for
STM32F405xx/07xx and STM32F415xx/17xx . . . . . . . . . . . . . . . . . . . 296
9.3 SYSCFG registers for STM32F42xxx and STM32F43xxx . . . . . . . . . . . 296
9.3.1 SYSCFG memory remap register (SYSCFG_MEMRMP) . . . . . . . . . . 296
9.3.2 SYSCFG peripheral mode  configuration register (SYSCFG_PMC)  . . 298
9.3.3 SYSCFG external interrup t configuration register 1
(SYSCFG_EXTICR1)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 299
9.3.4 SYSCFG external interrup t configuration register 2
(SYSCFG_EXTICR2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
9.3.5 SYSCFG external interrup t configuration register 3
(SYSCFG_EXTICR3)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
9.3.6 SYSCFG external interrup t configuration register 4
(SYSCFG_EXTICR4)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301
9.3.7 Compensation ce ll control register (SYSCFG_CMPCR) . . . . . . . . . . . 302
9.3.8 SYSCFG register maps for STM3 2F42xxx and STM32F43xxx . . . . . . 303
10 DMA controller (DMA) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
10.1 DMA introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
10.2 DMA main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
10.3 DMA functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306
10.3.1 General description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306
10.3.2 DMA transactions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 308
10.3.3 Channel selection  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309
10.3.4 Arbiter  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 310
10.3.5 DMA streams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
10.3.6 Source, destination and transfer modes  . . . . . . . . . . . . . . . . . . . . . . . 311
10.3.7 Pointer incrementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314
10.3.8 Circular mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
10.3.9 Double buffer mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
10.3.10 Programmable data width, packing/unpa cking, endianess  . . . . . . . . . 316
10.3.11 Single and burst transfers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 318
10.3.12 FIFO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319
10.3.13 DMA transfer completion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321
10.3.14 DMA transfer suspension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 322
10.3.15 Flow controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 322
10.3.16 Summary of the possible DMA configurations . . . . . . . . . . . . . . . . . . . 324
10.3.17 Stream configuration procedure  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 324

Contents RM0090
10/1741 RM0090 Rev 22
10.3.18 Error management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
10.4 DMA interrupts  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 326
10.5 DMA registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 327
10.5.1 DMA low interrupt status register (DMA_LISR) . . . . . . . . . . . . . . . . . . 327
10.5.2 DMA high interrupt status register (D MA_HISR) . . . . . . . . . . . . . . . . . 328
10.5.3 DMA low interrupt flag clear register (DMA_LIFCR)  . . . . . . . . . . . . . . 329
10.5.4 DMA high interrupt flag clear register  (DMA_HIFCR)  . . . . . . . . . . . . . 329
10.5.5 DMA stream x configuration register (DMA_SxCR) (x = 0..7)  . . . . . . . 330
10.5.6 DMA stream x number of data regi ster (DMA_SxNDTR) (x = 0..7) . . . 333
10.5.7 DMA stream x peripheral address register (DMA_SxPAR) (x = 0..7)  . 333
10.5.8 DMA stream x memory 0 address r egister (DMA_SxM0AR) (x = 0..7)  334
10.5.9 DMA stream x memory 1 address r egister (DMA_SxM1AR) (x = 0..7)  334
10.5.10 DMA stream x FIFO control register  (DMA_SxFCR) (x = 0..7)  . . . . . . 335
10.5.11 DMA register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337
11 Chrom-Art Accelerator™ controller (DMA2D)  . . . . . . . . . . . . . . . . . . 341
11.1 DMA2D introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
11.2 DMA2D main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342
11.3 DMA2D functional description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342
11.3.1 General description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342
11.3.2 DMA2D control  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343
11.3.3 DMA2D foreground and background FIFOs  . . . . . . . . . . . . . . . . . . . . 343
11.3.4 DMA2D foreground and background pixel format converter (PFC) . . . 344
11.3.5 DMA2D foreground and background CLUT interface  . . . . . . . . . . . . . 346
11.3.6 DMA2D blender . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347
11.3.7 DMA2D output PFC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347
11.3.8 DMA2D output FIFO  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348
11.3.9 DMA2D AHB master port timer  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348
11.3.10 DMA2D transactions  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 349
11.3.11 DMA2D configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 349
11.3.12 DMA2D transfer control (start, suspend, abort and completion)  . . . . . 352
11.3.13 Watermark . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 353
11.3.14 Error management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 353
11.3.15 AHB dead time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 353
11.4 DMA2D interrupts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 353
11.5 DMA2D registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 354

RM0090 Rev 22 11/1741
RM0090 Contents
39
11.5.1 DMA2D control register (DMA2D_CR)  . . . . . . . . . . . . . . . . . . . . . . . . 354
11.5.2 DMA2D Interrupt Status Register (DMA2D_ISR)  . . . . . . . . . . . . . . . . 356
11.5.3 DMA2D interrupt flag clear register (DMA2D_IFCR) . . . . . . . . . . . . . . 357
11.5.4 DMA2D foreground memory address register (DMA2D_FGMAR)  . . . 358
11.5.5 DMA2D foreground offset register (DMA2D_FGOR) . . . . . . . . . . . . . . 358
11.5.6 DMA2D background memory address register (DMA2D_BGMAR)  . . 359
11.5.7 DMA2D background offset register (DMA2D_BGOR) . . . . . . . . . . . . . 359
11.5.8 DMA2D foreground PFC control register (DMA2D_FGPFCCR) . . . . . 360
11.5.9 DMA2D foreground color register (D MA2D_FGCOLR) . . . . . . . . . . . . 362
11.5.10 DMA2D background PFC control register (DMA2D_BGPFCCR)  . . . . 363
11.5.11 DMA2D background color register (DMA2D_BGCOLR) . . . . . . . . . . . 365
11.5.12 DMA2D foreground CLUT memory address register
(DMA2D_FGCMAR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 365
11.5.13 DMA2D background CLUT memory address register
(DMA2D_BGCMAR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 366
11.5.14 DMA2D output PFC control register (DMA2D_OPFCCR) . . . . . . . . . . 366
11.5.15 DMA2D output color register (DMA2D_OCOLR) . . . . . . . . . . . . . . . . . 367
11.5.16 DMA2D output memory address regi ster (DMA2D_OMAR)  . . . . . . . . 368
11.5.17 DMA2D output offset register (DMA2D_OOR)  . . . . . . . . . . . . . . . . . . 369
11.5.18 DMA2D number of line register (DMA2D_NLR)  . . . . . . . . . . . . . . . . . 369
11.5.19 DMA2D line watermark register (DMA2D_LWR) . . . . . . . . . . . . . . . . . 370
11.5.20 DMA2D AHB master timer config uration register (DMA2D_AMTCR)  . 370
11.5.21 DMA2D register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371
12 Interrupts and events  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373
12.1 Nested vectored interrupt controller (NVIC) . . . . . . . . . . . . . . . . . . . . . . 373
12.1.1 NVIC features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373
12.1.2 SysTick calibration value register  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373
12.1.3 Interrupt and exception vectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373
12.2 External interrupt/event controller (EXTI) . . . . . . . . . . . . . . . . . . . . . . . . 373
12.2.1 EXTI main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 381
12.2.2 EXTI block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 382
12.2.3 Wake-up event management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 382
12.2.4 Functional description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 382
12.2.5 External interrupt/event line mapping  . . . . . . . . . . . . . . . . . . . . . . . . . 384
12.3 EXTI registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 386
12.3.1 Interrupt mask register (EXTI_IMR) . . . . . . . . . . . . . . . . . . . . . . . . . . . 386

Contents RM0090
12/1741 RM0090 Rev 22
12.3.2 Event mask register (EXTI_EM R)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 386
12.3.3 Rising trigger selection register (EXTI_RTSR)  . . . . . . . . . . . . . . . . . . 387
12.3.4 Falling trigger selection register (EXTI_ FTSR)  . . . . . . . . . . . . . . . . . . 387
12.3.5 Software interrupt event register (EXTI_ SWIER)  . . . . . . . . . . . . . . . . 388
12.3.6 Pending register (EXTI_PR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 388
12.3.7 EXTI register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 389
13 Analog-to-digital con verter (ADC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 390
13.1 ADC introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 390
13.2 ADC main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 390
13.3 ADC functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 391
13.3.1 ADC on-off control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 392
13.3.2 ADC clock  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 392
13.3.3 Channel selection  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 392
13.3.4 Single conversion mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393
13.3.5 Continuous conversion mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 394
13.3.6 Timing diagram  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 394
13.3.7 Analog watchdog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 394
13.3.8 Scan mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 395
13.3.9 Injected channel management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 396
13.3.10 Discontinuous mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 397
13.4 Data alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 398
13.5 Channel-wise programmable sampling time  . . . . . . . . . . . . . . . . . . . . . 399
13.6 Conversion on external trigger and trigger polarity  . . . . . . . . . . . . . . . . 399
13.7 Fast conversion mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 401
13.8 Data management  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 402
13.8.1 Using the DMA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 402
13.8.2 Managing a sequence of conversions without using the DMA  . . . . . . 402
13.8.3 Conversions without DMA and without overrun detection . . . . . . . . . . 403
13.9 Multi ADC mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 403
13.9.1 Injected simultaneous mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 406
13.9.2 Regular simultaneous mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 407
13.9.3 Interleaved mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 409
13.9.4 Alternate trigger mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 410
13.9.5 Combined regular/injected  simultaneous mode . . . . . . . . . . . . . . . . . . 412
13.9.6 Combined regular simultaneous + alternate trigger mode . . . . . . . . . . 413

RM0090 Rev 22 13/1741
RM0090 Contents
39
13.10 Temperature sensor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 414
13.11 Battery charge monitoring  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 416
13.12 ADC interrupts  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 416
13.13 ADC registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 417
13.13.1 ADC status register (ADC_SR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 417
13.13.2 ADC control register 1 (ADC_CR1) . . . . . . . . . . . . . . . . . . . . . . . . . . . 418
13.13.3 ADC control register 2 (ADC_CR2) . . . . . . . . . . . . . . . . . . . . . . . . . . . 420
13.13.4 ADC sample time register 1 (ADC_SMPR1) . . . . . . . . . . . . . . . . . . . . 422
13.13.5 ADC sample time register 2 (ADC_SMPR2) . . . . . . . . . . . . . . . . . . . . 422
13.13.6 ADC injected channel data offset register x (ADC_JOFRx) (x=1..4) . . 423
13.13.7 ADC watchdog higher threshold register (ADC_HTR) . . . . . . . . . . . . . 423
13.13.8 ADC watchdog lower threshold register (ADC_LTR) . . . . . . . . . . . . . . 424
13.13.9 ADC regular sequence register 1 (ADC_ SQR1)  . . . . . . . . . . . . . . . . . 424
13.13.10 ADC regular sequence register 2 (ADC_ SQR2)  . . . . . . . . . . . . . . . . . 425
13.13.11 ADC regular sequence register 3 (ADC_ SQR3)  . . . . . . . . . . . . . . . . . 425
13.13.12 ADC injected sequence register (ADC_JSQR)  . . . . . . . . . . . . . . . . . . 426
13.13.13 ADC injected data register x (ADC_JDRx ) (x= 1..4)  . . . . . . . . . . . . . . 427
13.13.14 ADC regular data register (ADC_DR)  . . . . . . . . . . . . . . . . . . . . . . . . . 427
13.13.15 ADC Common status register (ADC_CSR) . . . . . . . . . . . . . . . . . . . . . 428
13.13.16 ADC common control register (ADC_CCR) . . . . . . . . . . . . . . . . . . . . . 429
13.13.17 ADC common regular data register for dual and triple modes
(ADC_CDR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 432
13.13.18 ADC register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 432
14 Digital-to-analog converter (DAC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435
14.1 DAC introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435
14.2 DAC main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435
14.3 DAC functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
14.3.1 DAC channel enable  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
14.3.2 DAC output buffer enable  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
14.3.3 DAC data format  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
14.3.4 DAC conversion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 438
14.3.5 DAC output voltage  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 439
14.3.6 DAC trigger selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 439
14.3.7 DMA request  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440
14.3.8 Noise generation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440
14.3.9 Triangle-wave generation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 441

Contents RM0090
14/1741 RM0090 Rev 22
14.4 Dual DAC channel conversion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 442
14.4.1 Independent trigger without wave generatio n  . . . . . . . . . . . . . . . . . . . 443
14.4.2 Independent trigger with single LFSR gene ration  . . . . . . . . . . . . . . . . 443
14.4.3 Independent trigger with different LFSR generation  . . . . . . . . . . . . . . 443
14.4.4 Independent trigger with single triangle generation . . . . . . . . . . . . . . . 444
14.4.5 Independent trigger with different triangle generation . . . . . . . . . . . . . 444
14.4.6 Simultaneous software start  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 444
14.4.7 Simultaneous trigger without wave generat ion  . . . . . . . . . . . . . . . . . . 445
14.4.8 Simultaneous trigger with single LFSR ge neration  . . . . . . . . . . . . . . . 445
14.4.9 Simultaneous trigger with different LFSR  generation  . . . . . . . . . . . . . 445
14.4.10 Simultaneous trigger with single triang le generation . . . . . . . . . . . . . . 446
14.4.11 Simultaneous trigger with different triangle generation  . . . . . . . . . . . . 446
14.5 DAC registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 447
14.5.1 DAC control register (DAC_CR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 447
14.5.2 DAC software trigger register (DAC_SWTRIGR)  . . . . . . . . . . . . . . . . 450
14.5.3 DAC channel1 12-bit right- aligned data holding register
(DAC_DHR12R1)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 450
14.5.4 DAC channel1 12-bit left aligned data holding register
(DAC_DHR12L1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 451
14.5.5 DAC channel1 8-bit righ t aligned data holding register
(DAC_DHR8R1)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 451
14.5.6 DAC channel2 12-bit right aligned data holding register
(DAC_DHR12R2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 452
14.5.7 DAC channel2 12-bit left a ligned data holding register
(DAC_DHR12L2) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 452
14.5.8 DAC channel2 8-bit right-aligned data holding register
(DAC_DHR8R2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 452
14.5.9 Dual DAC 12-bit right-aligned data holding register
(DAC_DHR12RD)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 453
14.5.10 DUAL DAC 12-bit left aligned data holding register
(DAC_DHR12LD)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 453
14.5.11 DUAL DAC 8-bit right aligned data holding register
(DAC_DHR8RD)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 454
14.5.12 DAC channel1 data output register (DAC_DOR1) . . . . . . . . . . . . . . . . 454
14.5.13 DAC channel2 data output register (DAC_DOR2) . . . . . . . . . . . . . . . . 454
14.5.14 DAC status register (DAC_SR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 455
14.5.15 DAC register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 455
15 Digital camera interface (DCMI)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 457

RM0090 Rev 22 15/1741
RM0090 Contents
39
15.1 DCMI introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 457
15.2 DCMI main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 457
15.3 DCMI pins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 457
15.4 DCMI clocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 457
15.5 DCMI functional overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 458
15.5.1 DMA interface  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 459
15.5.2 DCMI physical interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 459
15.5.3 Synchronization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 461
15.5.4 Capture modes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 463
15.5.5 Crop feature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 465
15.5.6 JPEG format  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 467
15.5.7 FIFO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 467
15.6 Data format description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 467
15.6.1 Data formats  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 467
15.6.2 Monochrome format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
15.6.3 RGB format  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
15.6.4 YCbCr format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
15.7 DCMI interrupts  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 469
15.8 DCMI register description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 469
15.8.1 DCMI control register 1 (DCMI_CR)  . . . . . . . . . . . . . . . . . . . . . . . . . . 469
15.8.2 DCMI status register (DCMI_SR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 471
15.8.3 DCMI raw interrupt status register (DCMI_RIS)  . . . . . . . . . . . . . . . . . 472
15.8.4 DCMI interrupt enable register (DCMI_IER)  . . . . . . . . . . . . . . . . . . . . 473
15.8.5 DCMI masked interrupt st atus register (DCMI_MIS) . . . . . . . . . . . . . . 474
15.8.6 DCMI interrupt clear register (DCMI_ICR) . . . . . . . . . . . . . . . . . . . . . . 475
15.8.7 DCMI embedded synchron ization code register (DCMI_ESCR) . . . . . 475
15.8.8 DCMI embedded synchr onization unmask register (DCMI_ESUR)  . . 476
15.8.9 DCMI crop window start (DCMI_CWSTRT) . . . . . . . . . . . . . . . . . . . . . 477
15.8.10 DCMI crop window size (DCMI_CWSIZE) . . . . . . . . . . . . . . . . . . . . . . 477
15.8.11 DCMI data register (DCMI_ DR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 478
15.8.12 DCMI register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 478
16 LCD-TFT controller (LTDC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 480
16.1 Introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 480
16.2 LTDC main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 480
16.3 LTDC functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 481

Contents RM0090
16/1741 RM0090 Rev 22
16.3.1 LTDC block diagram  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 481
16.3.2 LTDC reset and clocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 481
16.3.3 LCD-TFT pins and signal interface  . . . . . . . . . . . . . . . . . . . . . . . . . . . 483
16.4 LTDC programmable parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 483
16.4.1 LTDC Global configuration parameters  . . . . . . . . . . . . . . . . . . . . . . . . 483
16.4.2 Layer programmable parameters  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 486
16.5 LTDC interrupts  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 490
16.6 LTDC programming procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 492
16.7 LTDC registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 493
16.7.1 LTDC Synchronization Size Confi guration Register (LTDC_SSCR)  . . 493
16.7.2 LTDC Back Porch Configuration Register (LTDC_BPCR) . . . . . . . . . . 493
16.7.3 LTDC Active Width Configuration Register (LTDC_AWCR) . . . . . . . . . 494
16.7.4 LTDC Total Width Configuration Regi ster (LTDC_TWCR) . . . . . . . . . . 495
16.7.5 LTDC Global Control Regi ster (LTDC_GCR) . . . . . . . . . . . . . . . . . . . . 495
16.7.6 LTDC Shadow Reload Configuration Register (LTDC_SRCR)  . . . . . . 497
16.7.7 LTDC Background Color Configuratio n Register (LTDC_BCCR)  . . . . 497
16.7.8 LTDC Interrupt Enable Register (LTDC_IER)   . . . . . . . . . . . . . . . . . . . 498
16.7.9 LTDC Interrupt Status Register (LTDC_ISR) . . . . . . . . . . . . . . . . . . . . 499
16.7.10 LTDC Interrupt Clear Regi ster (LTDC_ICR) . . . . . . . . . . . . . . . . . . . . . 499
16.7.11 LTDC Line Interrupt Position Configuration Register (LTDC_LIPCR)  . 500
16.7.12 LTDC Current Position Status Register (LTDC_CPSR) . . . . . . . . . . . . 500
16.7.13 LTDC Current Display Status Register  (LTDC_CDSR)  . . . . . . . . . . . . 501
16.7.14 LTDC Layerx Control Register (LTDC_LxCR) (where x=1..2) . . . . . . . 502
16.7.15 LTDC Layerx Window Horizontal  Position Configuration Register
(LTDC_LxWHPCR) (where x=1..2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . 503
16.7.16 LTDC Layerx Window Vertical  Position Configuration Register
(LTDC_LxWVPCR) (where x=1..2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . 504
16.7.17 LTDC Layerx Color Keying Conf iguration Register (LTDC_LxCKCR)
(where x=1..2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 505
16.7.18 LTDC Layerx Pixel Format Co nfiguration Register (LTDC_LxPFCR)
(where x=1..2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 505
16.7.19 LTDC Layerx Constant Alpha Configuration Register (LTDC_LxCACR)
(where x=1..2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 506
16.7.20 LTDC Layerx Default Color Co nfiguration Register (LTDC_LxDCCR)
(where x=1..2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 506
16.7.21 LTDC Layerx Blending Factors Co nfiguration Register (LTDC_LxBFCR)
(where x=1..2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 508
16.7.22 LTDC Layerx Color Frame Buff er Address Register (LTDC_LxCFBAR)
(where x=1..2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 509

RM0090 Rev 22 17/1741
RM0090 Contents
39
16.7.23 LTDC Layerx Color Frame Buffer Length Register (LTDC_LxCFBLR)
(where x=1..2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 509
16.7.24 LTDC Layerx ColorFrame Buffer Line Number Register
(LTDC_LxCFBLNR) (where x=1..2) . . . . . . . . . . . . . . . . . . . . . . . . . . . 510
16.7.25 LTDC Layerx CLUT Writ e Register (LTDC_LxCLUTWR)
(where x=1..2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 511
16.7.26 LTDC register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 512
17 Advanced-control timers (TIM1 and TIM8)  . . . . . . . . . . . . . . . . . . . . . 515
17.1 TIM1 and TIM8 introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 515
17.2 TIM1 and TIM8 main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 515
17.3 TIM1 and TIM8 functional description  . . . . . . . . . . . . . . . . . . . . . . . . . . 517
17.3.1 Time-base unit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 517
17.3.2 Counter modes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 519
17.3.3 Repetition counter  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 528
17.3.4 Clock selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 531
17.3.5 Capture/compare channels  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 534
17.3.6 Input capture mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 537
17.3.7 PWM input mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 538
17.3.8 Forced output mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 538
17.3.9 Output compare mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 539
17.3.10 PWM mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 540
17.3.11 Complementary outputs an d dead-time insertion  . . . . . . . . . . . . . . . . 543
17.3.12 Using the break function  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 545
17.3.13 Clearing the OCxREF signal on an external event  . . . . . . . . . . . . . . . 548
17.3.14 6-step PWM generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 549
17.3.15 One-pulse mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 550
17.3.16 Encoder interface mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 551
17.3.17 Timer input XOR function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 554
17.3.18 Interfacing with Hall sensors  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 554
17.3.19 TIMx and external trigger synchronization  . . . . . . . . . . . . . . . . . . . . . . 556
17.3.20 Timer synchronization  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 559
17.3.21 Debug mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 559
17.4 TIM1 and TIM8 registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 560
17.4.1 TIM1 and TIM8 control register 1 (TIMx_ CR1)  . . . . . . . . . . . . . . . . . . 560
17.4.2 TIM1 and TIM8 control register 2 (TIMx_ CR2)  . . . . . . . . . . . . . . . . . . 561
17.4.3 TIM1 and TIM8 slave mode control register (TIMx_SMCR)  . . . . . . . . 563
17.4.4 TIM1 and TIM8 DMA/interrupt enable register (TIMx_DIER) . . . . . . . . 565

Contents RM0090
18/1741 RM0090 Rev 22
17.4.5 TIM1 and TIM8 status register (TIMx_SR) . . . . . . . . . . . . . . . . . . . . . . 567
17.4.6 TIM1 and TIM8 event generation regist er (TIMx_EGR) . . . . . . . . . . . . 568
17.4.7 TIM1 and TIM8 capture/compare mode register 1 (TIMx_CCMR1)  . . 569
17.4.8 TIM1 and TIM8 capture/compare mode register 2 (TIMx_CCMR2)  . . 572
17.4.9 TIM1 and TIM8 capture/compare enable register (TIMx_CCER)  . . . . 574
17.4.10 TIM1 and TIM8 counter (T IMx_CNT) . . . . . . . . . . . . . . . . . . . . . . . . . . 577
17.4.11 TIM1 and TIM8 prescaler (TIMx_PSC)  . . . . . . . . . . . . . . . . . . . . . . . . 577
17.4.12 TIM1 and TIM8 auto-reload register (T IMx_ARR) . . . . . . . . . . . . . . . . 577
17.4.13 TIM1 and TIM8 repetiti on counter register (TIMx_RCR)  . . . . . . . . . . . 578
17.4.14 TIM1 and TIM8 capture/compare register 1 (TIMx_CCR1) . . . . . . . . . 578
17.4.15 TIM1 and TIM8 capture/compare register 2 (TIMx_CCR2) . . . . . . . . . 579
17.4.16 TIM1 and TIM8 capture/compare register 3 (TIMx_CCR3) . . . . . . . . . 579
17.4.17 TIM1 and TIM8 capture/compare register 4 (TIMx_CCR4) . . . . . . . . . 580
17.4.18 TIM1 and TIM8 break and dead-time register (TIMx_BDTR)  . . . . . . . 580
17.4.19 TIM1 and TIM8 DMA control register (TIMx_DCR)  . . . . . . . . . . . . . . . 582
17.4.20 TIM1 and TIM8 DMA address for full transfer (TIMx_DMAR)  . . . . . . . 583
17.4.21 TIM1 and TIM8 register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 584
18 General-purpose timers (TIM2 to TIM5) . . . . . . . . . . . . . . . . . . . . . . . . 586
18.1 TIM2 to TIM5 introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 586
18.2 TIM2 to TIM5 main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 586
18.3 TIM2 to TIM5 functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . 588
18.3.1 Time-base unit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 588
18.3.2 Counter modes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 589
18.3.3 Clock selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 599
18.3.4 Capture/compare channels  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 602
18.3.5 Input capture mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 604
18.3.6 PWM input mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 605
18.3.7 Forced output mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 606
18.3.8 Output compare mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 606
18.3.9 PWM mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 607
18.3.10 One-pulse mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 610
18.3.11 Clearing the OCxREF signal on an external event  . . . . . . . . . . . . . . . 611
18.3.12 Encoder interface mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 612
18.3.13 Timer input XOR function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 615
18.3.14 Timers and external trigger synchronizat ion  . . . . . . . . . . . . . . . . . . . . 615
18.3.15 Timer synchronization  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 618

RM0090 Rev 22 19/1741
RM0090 Contents
39
18.3.16 Debug mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 623
18.4 TIM2 to TIM5 registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 624
18.4.1 TIMx control register 1 (TIMx_CR1)  . . . . . . . . . . . . . . . . . . . . . . . . . . 624
18.4.2 TIMx control register 2 (TIMx_CR2)  . . . . . . . . . . . . . . . . . . . . . . . . . . 625
18.4.3 TIMx slave mode control register (TIM x_SMCR) . . . . . . . . . . . . . . . . . 626
18.4.4 TIMx DMA/Interrup t enable register (TIMx_DIER) . . . . . . . . . . . . . . . . 629
18.4.5 TIMx status register (TIMx_SR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 630
18.4.6 TIMx event generation regi ster (TIMx_EGR) . . . . . . . . . . . . . . . . . . . . 631
18.4.7 TIMx capture/compare mode register 1 (TIMx_CCMR1) . . . . . . . . . . . 632
18.4.8 TIMx capture/compare mode register 2 (TIMx_CCMR2) . . . . . . . . . . . 635
18.4.9 TIMx capture/compare enable register  (TIMx_CCER)  . . . . . . . . . . . . 636
18.4.10 TIMx counter (TIMx_CNT) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 638
18.4.11 TIMx prescaler (TIMx_PSC)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 638
18.4.12 TIMx auto-reload register (TIMx_ARR)  . . . . . . . . . . . . . . . . . . . . . . . . 638
18.4.13 TIMx capture/compare register 1 (TIMx_CCR1)  . . . . . . . . . . . . . . . . . 639
18.4.14 TIMx capture/compare register 2 (TIMx_CCR2)  . . . . . . . . . . . . . . . . . 639
18.4.15 TIMx capture/compare register 3 (TIMx_CCR3)  . . . . . . . . . . . . . . . . . 640
18.4.16 TIMx capture/compare register 4 (TIMx_CCR4)  . . . . . . . . . . . . . . . . . 640
18.4.17 TIMx DMA control register (TIMx_DCR)  . . . . . . . . . . . . . . . . . . . . . . . 641
18.4.18 TIMx DMA address for full transfer (TIM x_DMAR)  . . . . . . . . . . . . . . . 641
18.4.19 TIM2 option register (TIM2_OR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 642
18.4.20 TIM5 option register (TIM5_OR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 643
18.4.21 TIMx register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 644
19 General-purpose timers (TIM9 to TIM14) . . . . . . . . . . . . . . . . . . . . . . . 646
19.1 TIM9 to TIM14 introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 646
19.2 TIM9 to TIM14 main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 646
19.2.1 TIM9/TIM12 main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 646
19.2.2 TIM10/TIM11 and TIM13/TIM14 main featur es  . . . . . . . . . . . . . . . . . . 647
19.3 TIM9 to TIM14 functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . 649
19.3.1 Time-base unit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 649
19.3.2 Counter modes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 651
19.3.3 Clock selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 654
19.3.4 Capture/compare channels  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 656
19.3.5 Input capture mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 657
19.3.6 PWM input mode (only for TIM9/12)  . . . . . . . . . . . . . . . . . . . . . . . . . . 659
19.3.7 Forced output mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 660

Contents RM0090
20/1741 RM0090 Rev 22
19.3.8 Output compare mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 660
19.3.9 PWM mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 661
19.3.10 One-pulse mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 662
19.3.11 TIM9/12 external trigger synchronization . . . . . . . . . . . . . . . . . . . . . . . 664
19.3.12 Timer synchronization (TIM9/ 12) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 667
19.3.13 Debug mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 667
19.4 TIM9 and TIM12 registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 668
19.4.1 TIM9/12 control register 1 (TIMx_CR1) . . . . . . . . . . . . . . . . . . . . . . . . 668
19.4.2 TIM9/12 slave mode control register (TIMx_SMCR) . . . . . . . . . . . . . . 669
19.4.3 TIM9/12 Interrupt enable register (TIMx_DIER)  . . . . . . . . . . . . . . . . . 670
19.4.4 TIM9/12 status register (TIMx_SR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . 672
19.4.5 TIM9/12 event generation register (TIMx_EGR)  . . . . . . . . . . . . . . . . . 673
19.4.6 TIM9/12 capture/compare mode regi ster 1 (TIMx_CCMR1) . . . . . . . . 674
19.4.7 TIM9/12 capture/compare enable regi ster (TIMx_CCER) . . . . . . . . . . 677
19.4.8 TIM9/12 counter (TIMx_CNT)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 678
19.4.9 TIM9/12 prescaler (TIMx_PSC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 678
19.4.10 TIM9/12 auto-reload register (TIMx_ARR)  . . . . . . . . . . . . . . . . . . . . . 678
19.4.11 TIM9/12 capture/compare register 1 (TIMx_CCR1)  . . . . . . . . . . . . . . 679
19.4.12 TIM9/12 capture/compare register 2 (TIMx_CCR2)  . . . . . . . . . . . . . . 679
19.4.13 TIM9/12 register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 680
19.5 TIM10/11/13/14 registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 682
19.5.1 TIM10/11/13/14 control register 1 (TIMx_ CR1)  . . . . . . . . . . . . . . . . . . 682
19.5.2 TIM10/11/13/14 Interrupt enable regist er (TIMx_DIER) . . . . . . . . . . . . 683
19.5.3 TIM10/11/13/14 status register (TIMx_SR)  . . . . . . . . . . . . . . . . . . . . . 683
19.5.4 TIM10/11/13/14 event generation regist er (TIMx_EGR)  . . . . . . . . . . . 684
19.5.5 TIM10/11/13/14 capture/compare mode register 1 (TIMx_CCMR1)  . . 684
19.5.6 TIM10/11/13/14 capture/compare enable register (TIMx_CCER)  . . . . 687
19.5.7 TIM10/11/13/14 counter (TIMx_CNT)  . . . . . . . . . . . . . . . . . . . . . . . . . 688
19.5.8 TIM10/11/13/14 prescaler (TIMx_PSC) . . . . . . . . . . . . . . . . . . . . . . . . 688
19.5.9 TIM10/11/13/14 auto-reload register (T IMx_ARR) . . . . . . . . . . . . . . . . 688
19.5.10 TIM10/11/13/14 capture/compare register 1 (TIMx_CCR1) . . . . . . . . . 689
19.5.11 TIM11 option register 1 (TIM11_OR) . . . . . . . . . . . . . . . . . . . . . . . . . . 689
19.5.12 TIM10/11/13/14 register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 690
20 Basic timers (TIM6 and TIM7) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 692
20.1 TIM6 and TIM7 introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 692
20.2 TIM6 and TIM7 main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 692

RM0090 Rev 22 21/1741
RM0090 Contents
39
20.3 TIM6 and TIM7 functional description  . . . . . . . . . . . . . . . . . . . . . . . . . . 693
20.3.1 Time-base unit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 693
20.3.2 Counting mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 695
20.3.3 Clock source  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 697
20.3.4 Debug mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 698
20.4 TIM6 and TIM7 registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 698
20.4.1 TIM6 and TIM7 control register 1 (TIMx_ CR1)  . . . . . . . . . . . . . . . . . . 698
20.4.2 TIM6 and TIM7 control register 2 (TIMx_ CR2)  . . . . . . . . . . . . . . . . . . 700
20.4.3 TIM6 and TIM7 DMA/Interrupt enable register (TIMx_DIER)  . . . . . . . 700
20.4.4 TIM6 and TIM7 status register (TIMx_SR) . . . . . . . . . . . . . . . . . . . . . . 701
20.4.5 TIM6 and TIM7 event generation regist er (TIMx_EGR) . . . . . . . . . . . . 701
20.4.6 TIM6 and TIM7 counter (TIMx_CNT) . . . . . . . . . . . . . . . . . . . . . . . . . . 701
20.4.7 TIM6 and TIM7 prescaler (TIMx_PSC)  . . . . . . . . . . . . . . . . . . . . . . . . 702
20.4.8 TIM6 and TIM7 auto-reload register (T IMx_ARR) . . . . . . . . . . . . . . . . 702
20.4.9 TIM6 and TIM7 register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 703
21 Independent watchdog (IWDG)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 704
21.1 IWDG introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 704
21.2 IWDG main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 704
21.3 IWDG functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 704
21.3.1 Hardware watchdog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 704
21.3.2 Register access protection  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 704
21.3.3 Debug mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 705
21.4 IWDG registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 706
21.4.1 Key register (IWDG_KR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 706
21.4.2 Prescaler register (IWDG_PR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 706
21.4.3 Reload register (IWDG_RLR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 707
21.4.4 Status register (IWDG_SR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 707
21.4.5 IWDG register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 708
22 Window watchdog (WWDG) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 709
22.1 WWDG introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 709
22.2 WWDG main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 709
22.3 WWDG functional description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 709
22.4 How to program the watchdog timeout . . . . . . . . . . . . . . . . . . . . . . . . . . .711
22.5 Debug mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 712

Contents RM0090
22/1741 RM0090 Rev 22
22.6 WWDG registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 713
22.6.1 Control register (WWDG_CR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 713
22.6.2 Configuration register (WWDG_CFR) . . . . . . . . . . . . . . . . . . . . . . . . . 714
22.6.3 Status register (WWDG_SR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 714
22.6.4 WWDG register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 715
23 Cryptographic processor (CRYP)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 716
23.1 CRYP introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 716
23.2 CRYP main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 716
23.3 CRYP functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 718
23.3.1 DES/TDES cryptographic core  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 719
23.3.2 AES cryptograph ic core . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 724
23.3.3 Data type . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 735
23.3.4 Initialization vectors - CRYP_IV0...1(L/R)  . . . . . . . . . . . . . . . . . . . . . . 738
23.3.5 CRYP busy state  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 739
23.3.6 Procedure to perform an encryption or  a decryption . . . . . . . . . . . . . . 740
23.3.7 Context swapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 741
23.4 CRYP interrupts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 743
23.5 CRYP DMA interface  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 744
23.6 CRYP registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 744
23.6.1 CRYP control register (CRYP_CR) for STM32F415/417xx . . . . . . . . . 744
23.6.2 CRYP control register (CRYP_CR) for STM32F415/417xx . . . . . . . . . 746
23.6.3 CRYP status register (CRYP_SR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 749
23.6.4 CRYP data input register (CRYP_DIN)  . . . . . . . . . . . . . . . . . . . . . . . . 750
23.6.5 CRYP data output register (CRYP_DOUT) . . . . . . . . . . . . . . . . . . . . . 751
23.6.6 CRYP DMA control register (CRYP_DMACR) . . . . . . . . . . . . . . . . . . . 752
23.6.7 CRYP interrupt mask set/c lear register (CRYP_IMSCR) . . . . . . . . . . . 752
23.6.8 CRYP raw interrupt status register (CRYP_RISR)  . . . . . . . . . . . . . . . 753
23.6.9 CRYP masked interrupt status regist er (CRYP_MISR) . . . . . . . . . . . . 753
23.6.10 CRYP key registers (CRYP_K0...3(L/R)R)  . . . . . . . . . . . . . . . . . . . . . 754
23.6.11 CRYP initialization vector registers (CRYP_IV0...1(L/R)R) . . . . . . . . . 756
23.6.12 CRYP context swap registers (CRYP_CSGCMCCM0..7R and
CRYP_CSGCM0..7R) for STM32F42xxx and STM32F43xxx . . . . . . . 758
23.6.13 CRYP register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 759
24 Random number generator (RNG ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 763
24.1 RNG introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 763

RM0090 Rev 22 23/1741
RM0090 Contents
39
24.2 RNG main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 763
24.3 RNG functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 763
24.3.1 Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 764
24.3.2 Error management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 764
24.4 RNG registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 764
24.4.1 RNG control register (RNG_CR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 765
24.4.2 RNG status register (RNG_SR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 765
24.4.3 RNG data register (RNG_DR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 766
24.4.4 RNG register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 767
25 Hash processor (HASH)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 768
25.1 HASH introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 768
25.2 HASH main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 768
25.3 HASH functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 769
25.3.1 Duration of the processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 771
25.3.2 Data type . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 771
25.3.3 Message digest computing  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 773
25.3.4 Message padding  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 774
25.3.5 Hash operation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 775
25.3.6 HMAC operation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 775
25.3.7 Context swapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 776
25.3.8 HASH interrupt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 778
25.4 HASH registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 778
25.4.1 HASH control register (HASH_CR) for STM32F415/417xx . . . . . . . . . 778
25.4.2 HASH control register (HASH_CR) for STM32F43xxx  . . . . . . . . . . . . 781
25.4.3 HASH data input register (HASH_DIN) . . . . . . . . . . . . . . . . . . . . . . . . 784
25.4.4 HASH start register (HASH_STR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 785
25.4.5 HASH digest registers (HASH_HR0..4/5/6/7)  . . . . . . . . . . . . . . . . . . . 786
25.4.6 HASH interrupt enable register (HASH_IMR)  . . . . . . . . . . . . . . . . . . . 788
25.4.7 HASH status register (HASH_SR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 789
25.4.8 HASH context swap registers (HASH_CSRx) . . . . . . . . . . . . . . . . . . . 790
25.4.9 HASH register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 791
26 Real-time clock (RTC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 794
26.1 Introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 794
26.2 RTC main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 795

Contents RM0090
24/1741 RM0090 Rev 22
26.3 RTC functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 797
26.3.1 Clock and prescalers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 797
26.3.2 Real-time clock and calendar  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 798
26.3.3 Programmable alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 798
26.3.4 Periodic auto-wakeup  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 798
26.3.5 RTC initialization and configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . 799
26.3.6 Reading the calendar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 801
26.3.7 Resetting the RTC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 802
26.3.8 RTC synchronization   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 802
26.3.9 RTC reference clock detection  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 803
26.3.10 RTC coarse digital calibration   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 804
26.3.11 RTC smooth digital calibration   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 805
26.3.12 Timestamp function  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 807
26.3.13 Tamper detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 807
26.3.14 Calibration clock output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 809
26.3.15 Alarm output  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 809
26.4 RTC and low-power modes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 810
26.5 RTC interrupts  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 810
26.6 RTC registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 812
26.6.1 RTC time register (RTC_TR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 812
26.6.2 RTC date register (RTC_DR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 813
26.6.3 RTC control register (RTC_CR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 814
26.6.4 RTC initialization and status register (RTC_ISR) . . . . . . . . . . . . . . . . . 816
26.6.5 RTC prescaler register (RTC_PRER)  . . . . . . . . . . . . . . . . . . . . . . . . . 819
26.6.6 RTC wake-up timer register (RTC_WUTR) . . . . . . . . . . . . . . . . . . . . . 819
26.6.7 RTC calibration register (RTC_CALIBR) . . . . . . . . . . . . . . . . . . . . . . . 820
26.6.8 RTC alarm A register (RTC_ALRMAR)  . . . . . . . . . . . . . . . . . . . . . . . . 821
26.6.9 RTC alarm B register (RTC_ALRMBR) . . . . . . . . . . . . . . . . . . . . . . . . 822
26.6.10 RTC write protection register (RTC_WPR)  . . . . . . . . . . . . . . . . . . . . . 823
26.6.11 RTC sub second register (RTC_SSR) . . . . . . . . . . . . . . . . . . . . . . . . . 823
26.6.12 RTC shift control register (RTC_SHIFTR) . . . . . . . . . . . . . . . . . . . . . . 824
26.6.13 RTC time stamp time register (RTC_TSTR)  . . . . . . . . . . . . . . . . . . . . 824
26.6.14 RTC time stamp date register (RTC_TSDR) . . . . . . . . . . . . . . . . . . . . 825
26.6.15 RTC timestamp sub second register (RTC_TSSSR) . . . . . . . . . . . . . . 826
26.6.16 RTC calibration register (RTC_CALR) . . . . . . . . . . . . . . . . . . . . . . . . . 826
26.6.17 RTC tamper and alternate function configuration register
(RTC_TAFCR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 828

RM0090 Rev 22 25/1741
RM0090 Contents
39
26.6.18 RTC alarm A sub second  register (RTC_ALRMASSR)  . . . . . . . . . . . . 830
26.6.19 RTC alarm B sub second register (RTC_ALRMBSSR) . . . . . . . . . . . . 831
26.6.20 RTC backup registers (RTC_BKPxR)  . . . . . . . . . . . . . . . . . . . . . . . . . 832
26.6.21 RTC register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 832
27 Inter-integrated circuit (I2C) interface . . . . . . . . . . . . . . . . . . . . . . . . . 835
27.1 I 2C introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 835
27.2 I 2C main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 835
27.3 I 2C functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 836
27.3.1 Mode selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 836
27.3.2 I2C target mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 839
27.3.3 I2C controller mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 841
27.3.4 Error conditions  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 846
27.3.5 Programmable noise filter  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 847
27.3.6 SDA/SCL line control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 848
27.3.7 SMBus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 848
27.3.8 DMA requests  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 851
27.3.9 Packet error checking  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 852
27.4 I 2C interrupts  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 853
27.5 I 2C debug mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 855
27.6 I 2C registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 855
27.6.1 I 2C Control register 1 (I2C_CR1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 855
27.6.2 I 2C Control register 2 (I2C_CR2) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 857
27.6.3 I 2C Own address register 1 (I2C_OAR1) . . . . . . . . . . . . . . . . . . . . . . . 859
27.6.4 I 2C Own address register 2 (I2C_OAR2) . . . . . . . . . . . . . . . . . . . . . . . 859
27.6.5 I 2C Data register (I2C_DR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 860
27.6.6 I 2C Status register 1 (I2C_SR1)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 860
27.6.7 I 2C Status register 2 (I2C_SR2)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 863
27.6.8 I 2C Clock control register (I2C_CCR)  . . . . . . . . . . . . . . . . . . . . . . . . . 865
27.6.9 I 2C TRISE register (I2C_TRISE)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 866
27.6.10 I 2C FLTR register (I2C_FLTR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 866
27.6.11 I2C register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 867
28 Serial peripheral interface (SPI ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 868
28.1 SPI introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 868
28.2 SPI and I 2S main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 869

Contents RM0090
26/1741 RM0090 Rev 22
28.2.1 SPI features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 869
28.2.2 I 2S features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 869
28.3 SPI functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 871
28.3.1 General description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 871
28.3.2 Configuring the SPI in slave mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . 875
28.3.3 Configuring the SPI in master mode  . . . . . . . . . . . . . . . . . . . . . . . . . . 877
28.3.4 Configuring the SPI for half-duplex commu nication . . . . . . . . . . . . . . . 879
28.3.5 Data transmission and reception procedur es  . . . . . . . . . . . . . . . . . . . 880
28.3.6 CRC calculation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 886
28.3.7 Status flags  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 887
28.3.8 Disabling the SPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 888
28.3.9 SPI communication using DMA (direct memory addressing) . . . . . . . . 889
28.3.10 Error flags  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 891
28.3.11 SPI interrupts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 893
28.4 I 2S functional description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 894
28.4.1 I 2S general description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 894
28.4.2 I2S full duplex  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 895
28.4.3 Supported audio protocols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 896
28.4.4 Clock generator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 902
28.4.5 I 2S master mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 904
28.4.6 I 2S slave mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 906
28.4.7 Status flags  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 908
28.4.8 Error flags  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 909
28.4.9 I 2S interrupts  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 910
28.4.10 DMA features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 910
28.5 SPI and I 2S registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .911
28.5.1 SPI control register 1 (SPI_CR1) (not used in I 2S mode)  . . . . . . . . . . 911
28.5.2 SPI control register 2 (SPI_CR2) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 913
28.5.3 SPI status register (SPI_SR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 914
28.5.4 SPI data register (SPI_DR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 915
28.5.5 SPI CRC polynomial register  (SPI_CRCPR) (not used in I2S
mode) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 916
28.5.6 SPI RX CRC register ( SPI_RXCRCR) (not used in I2S mode)  . . . . . . 916
28.5.7 SPI TX CRC register (S PI_TXCRCR) (not used in I2S mode) . . . . . . . 916
28.5.8 SPI_I 2S configuration register (SPI_I2SCFGR) . . . . . . . . . . . . . . . . . . 917
28.5.9 SPI_I 2S prescaler register (SPI_I2SPR)  . . . . . . . . . . . . . . . . . . . . . . . 918
28.5.10 SPI register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 920

RM0090 Rev 22 27/1741
RM0090 Contents
39
29 Serial audio interface (SAI) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 921
29.1 Introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 921
29.2 Main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 922
29.3 Functional block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 923
29.4 Main SAI modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 924
29.5 SAI synchronization mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 925
29.6 Audio data size . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 925
29.7 Frame synchronization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 925
29.7.1 Frame length  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 926
29.7.2 Frame synchronization polari ty  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 926
29.7.3 Frame synchronization active level length  . . . . . . . . . . . . . . . . . . . . . . 927
29.7.4 Frame synchronization offset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 927
29.7.5 FS signal role . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 927
29.8 Slot configuration  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 928
29.9 SAI clock generator  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 930
29.10 Internal FIFOs  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 931
29.11 AC’97 link controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 934
29.12 Specific features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 935
29.12.1 Mute mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 935
29.12.2 MONO/STEREO function  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 935
29.12.3 Companding mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 936
29.12.4 Output data line management on an inacti ve slot  . . . . . . . . . . . . . . . . 937
29.13 Error flags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 939
29.13.1 FIFO overrun/underrun (OVRUDR) . . . . . . . . . . . . . . . . . . . . . . . . . . . 939
29.13.2 Anticipated frame synchronisation dete ction (AFSDET)  . . . . . . . . . . . 941
29.13.3 Late frame synchronization detection  . . . . . . . . . . . . . . . . . . . . . . . . . 941
29.13.4 Codec not ready (CNRDY AC’97)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 942
29.13.5 Wrong clock configuration in master mode (with NODIV = 0) . . . . . . . 942
29.14 Interrupt sources  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 943
29.15 Disabling the SAI  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 943
29.16 SAI DMA interface  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 944
29.17 SAI registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 945
29.17.1 SAI x configuration register 1 (SAI_x CR1) where x is A or B . . . . . . . . 945
29.17.2 SAI x configuration register 2 (SAI_x CR2) where x is A or B . . . . . . . . 948
29.17.3 SAI x frame configuration register (SAI_XFRCR) where x is A or B  . . 950

Contents RM0090
28/1741 RM0090 Rev 22
29.17.4 SAI x slot register (SAI_xSLOTR) where x is A or B  . . . . . . . . . . . . . . 952
29.17.5 SAI x interrupt mask register (SAI_xIM ) where x is A or B . . . . . . . . . . 953
29.17.6 SAI x status register (SAI_xSR) where x is A or B . . . . . . . . . . . . . . . . 955
29.17.7 SAI x clear flag register (SAI_xCLRFR) where X is A or B  . . . . . . . . . 957
29.17.8 SAI x data register (SAI_xDR) where x is A or B . . . . . . . . . . . . . . . . . 958
29.17.9 SAI register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 958
30 Universal synchronous  asynchronous receiver
transmitter (USART)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 960
30.1 USART introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 960
30.2 USART main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 960
30.3 USART functional description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 961
30.3.1 USART character description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 964
30.3.2 Transmitter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 965
30.3.3 Receiver . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 968
30.3.4 Fractional baud rate generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 973
30.3.5 USART receiver tolerance to clock deviation . . . . . . . . . . . . . . . . . . . . 983
30.3.6 Multiprocessor communication  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 984
30.3.7 Parity control  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 986
30.3.8 LIN (local interconnection network) mode . . . . . . . . . . . . . . . . . . . . . . 987
30.3.9 USART synchronous mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 989
30.3.10 Single-wire half-duplex communication . . . . . . . . . . . . . . . . . . . . . . . . 991
30.3.11 Smartcard  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 992
30.3.12 IrDA SIR ENDEC block  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 994
30.3.13 Continuous communication using DMA . . . . . . . . . . . . . . . . . . . . . . . . 996
30.3.14 Hardware flow control  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 998
30.4 USART interrupts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1001
30.5 USART mode configuration  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1002
30.6 USART registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1002
30.6.1 Status register (USART_SR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1002
30.6.2 Data register (USART_DR)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1005
30.6.3 Baud rate register (USART_BRR) . . . . . . . . . . . . . . . . . . . . . . . . . . . 1005
30.6.4 Control register 1 (USART_CR1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1005
30.6.5 Control register 2 (USART_CR2) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1008
30.6.6 Control register 3 (USART_CR3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1009
30.6.7 Guard time and prescaler register (U SART_GTPR)  . . . . . . . . . . . . . 1012
30.6.8 USART register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1013

RM0090 Rev 22 29/1741
RM0090 Contents
39
31 Secure digital input/output interface (SDI O) . . . . . . . . . . . . . . . . . . . 1014
31.1 SDIO main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1014
31.2 SDIO bus topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1015
31.3 SDIO functional description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1017
31.3.1 SDIO adapter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1018
31.3.2 SDIO APB2 interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1028
31.4 Card functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1029
31.4.1 Card identification mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1029
31.4.2 Card reset  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1029
31.4.3 Operating voltage range validation  . . . . . . . . . . . . . . . . . . . . . . . . . . 1029
31.4.4 Card identification process  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1030
31.4.5 Block write . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1031
31.4.6 Block read  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1031
31.4.7 Stream access, stream write and stre am read (MultiMediaCard only)  . . .
1032
31.4.8 Erase: group erase and sector erase  . . . . . . . . . . . . . . . . . . . . . . . . 1033
31.4.9 Wide bus selection or deselection . . . . . . . . . . . . . . . . . . . . . . . . . . . 1034
31.4.10 Protection management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1034
31.4.11 Card status register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1037
31.4.12 SD status register  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1040
31.4.13 SD I/O mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1044
31.4.14 Commands and responses  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1045
31.5 Response formats  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1048
31.5.1 R1 (normal response command) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1049
31.5.2 R1b  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1049
31.5.3 R2 (CID, CSD register)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1049
31.5.4 R3 (OCR register)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1049
31.5.5 R4 (Fast I/O)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1050
31.5.6 R4b  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1050
31.5.7 R5 (interrupt request) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1051
31.5.8 R6  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1051
31.6 SDIO I/O card-specific operations  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1052
31.6.1 SDIO I/O read wait operation by SDIO _D2 signaling  . . . . . . . . . . . . 1052
31.6.2 SDIO read wait operation by stopping SDIO_CK  . . . . . . . . . . . . . . . 1052
31.6.3 SDIO suspend/resume operation  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1053
31.6.4 SDIO interrupts  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1053

Contents RM0090
30/1741 RM0090 Rev 22
31.7 CE-ATA specific operations  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1053
31.7.1 Command completion signal disable . . . . . . . . . . . . . . . . . . . . . . . . . 1053
31.7.2 Command completion signal enable  . . . . . . . . . . . . . . . . . . . . . . . . . 1053
31.7.3 CE-ATA interrupt  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1054
31.7.4 Aborting CMD61  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1054
31.8 HW flow control  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1054
31.9 SDIO registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1054
31.9.1 SDIO power control register (SDIO_POWE R) . . . . . . . . . . . . . . . . . . 1054
31.9.2 SDI clock control register (SDIO_CLKCR)  . . . . . . . . . . . . . . . . . . . . 1055
31.9.3 SDIO argument register (SDIO_ARG) . . . . . . . . . . . . . . . . . . . . . . . . 1056
31.9.4 SDIO command register (SDIO_CMD)  . . . . . . . . . . . . . . . . . . . . . . . 1056
31.9.5 SDIO command re sponse register (SDIO_RESPCMD)  . . . . . . . . . . 1057
31.9.6 SDIO response 1..4 regi ster (SDIO_RESPx)  . . . . . . . . . . . . . . . . . . 1058
31.9.7 SDIO data timer register (SDIO_DTIMER)  . . . . . . . . . . . . . . . . . . . . 1058
31.9.8 SDIO data length register (SDIO_DLEN)  . . . . . . . . . . . . . . . . . . . . . 1059
31.9.9 SDIO data control register (SDIO_DCTRL) . . . . . . . . . . . . . . . . . . . . 1060
31.9.10 SDIO data counter register (SDIO_DCOUNT)  . . . . . . . . . . . . . . . . . 1061
31.9.11 SDIO status register (SDIO_STA)  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1061
31.9.12 SDIO interrupt clear register (SDIO_ICR)  . . . . . . . . . . . . . . . . . . . . . 1063
31.9.13 SDIO mask register (SDIO_MASK) . . . . . . . . . . . . . . . . . . . . . . . . . . 1064
31.9.14 SDIO FIFO counter register (SDIO_FIFOCNT) . . . . . . . . . . . . . . . . . 1067
31.9.15 SDIO data FIFO register (SDIO_FIFO) . . . . . . . . . . . . . . . . . . . . . . . 1067
31.9.16 SDIO register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1068
32 Controller area network (bxC AN) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1069
32.1 bxCAN introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1069
32.2 bxCAN main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1069
32.3 bxCAN general description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1070
32.3.1 CAN 2.0B active core  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1070
32.3.2 Control, status and configuration registers  . . . . . . . . . . . . . . . . . . . . 1071
32.3.3 Tx mailboxes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1071
32.3.4 Acceptance filters  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1071
32.4 bxCAN operating modes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1072
32.4.1 Initialization mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1073
32.4.2 Normal mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1073
32.4.3 Sleep mode (low-power)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1073

RM0090 Rev 22 31/1741
RM0090 Contents
39
32.5 Test mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1074
32.5.1 Silent mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1074
32.5.2 Loop back mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1075
32.5.3 Loop back combined with silent mode . . . . . . . . . . . . . . . . . . . . . . . . 1075
32.6 Debug mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1076
32.7 bxCAN functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1076
32.7.1 Transmission handling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1076
32.7.2 Time triggered communication mode . . . . . . . . . . . . . . . . . . . . . . . . . 1078
32.7.3 Reception handling  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1078
32.7.4 Identifier filtering  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1080
32.7.5 Message storage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1084
32.7.6 Error management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1086
32.7.7 Bit timing  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1086
32.8 bxCAN interrupts  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1088
32.9 CAN registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1090
32.9.1 Register access protection  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1090
32.9.2 CAN control and status registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1090
32.9.3 CAN mailbox registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1099
32.9.4 CAN filter registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1104
32.9.5 bxCAN register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1109
33 Ethernet (ETH): media access control (MAC) with
DMA controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1113
33.1 Ethernet introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1113
33.2 Ethernet main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1113
33.2.1 MAC core features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1114
33.2.2 DMA features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1115
33.2.3 PTP features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1115
33.3 Ethernet pins  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1116
33.4 Ethernet functional description: SMI, MII and RMII  . . . . . . . . . . . . . . . .1117
33.4.1 Station management interface: SMI  . . . . . . . . . . . . . . . . . . . . . . . . . 1117
33.4.2 Media-independent interface: MII  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1120
33.4.3 Reduced media-independent interface: RM II  . . . . . . . . . . . . . . . . . . 1122
33.4.4 MII/RMII selection  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1123
33.5 Ethernet functional description: MAC 802.3 . . . . . . . . . . . . . . . . . . . . . .1124
33.5.1 MAC 802.3 frame format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1125

Contents RM0090
32/1741 RM0090 Rev 22
33.5.2 MAC frame transmission . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1128
33.5.3 MAC frame reception . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1135
33.5.4 MAC interrupts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1140
33.5.5 MAC filtering  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1141
33.5.6 MAC loopback mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1144
33.5.7 MAC management counters: MMC . . . . . . . . . . . . . . . . . . . . . . . . . . 1144
33.5.8 Power management: PMT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1145
33.5.9 Precision time protocol (IEEE1588 PTP) . . . . . . . . . . . . . . . . . . . . . . 1148
33.6 Ethernet functional description: DMA controller operation . . . . . . . . . . .1154
33.6.1 Initialization of a transfer using DMA . . . . . . . . . . . . . . . . . . . . . . . . . 1155
33.6.2 Host bus burst access . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1155
33.6.3 Host data buffer alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1156
33.6.4 Buffer size calculations  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1156
33.6.5 DMA arbiter  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1157
33.6.6 Error response to DMA  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1157
33.6.7 Tx DMA configuration  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1157
33.6.8 Rx DMA configuration  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1169
33.6.9 DMA interrupts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1179
33.7 Ethernet interrupts  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1180
33.8 Ethernet register descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1181
33.8.1 MAC register description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1181
33.8.2 MMC register description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1198
33.8.3 IEEE 1588 time stamp registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1204
33.8.4 DMA register description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1210
33.8.5 Ethernet register maps  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1224
34 USB on-the-go full-speed (OTG_FS) . . . . . . . . . . . . . . . . . . . . . . . . . 1228
34.1 OTG_FS introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1228
34.2 OTG_FS main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1229
34.2.1 General features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1229
34.2.2 Host-mode features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1230
34.2.3 Peripheral-mode features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1230
34.3 OTG_FS functional description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1231
34.3.1 OTG pins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1231
34.3.2 OTG full-speed core  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1231
34.3.3 Full-speed OTG PHY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1232

RM0090 Rev 22 33/1741
RM0090 Contents
39
34.4 OTG dual role device (DRD)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1233
34.4.1 ID line detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1233
34.4.2 HNP dual role device . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1233
34.4.3 SRP dual role device . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1234
34.5 USB peripheral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1234
34.5.1 SRP-capable peripheral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1235
34.5.2 Peripheral states  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1235
34.5.3 Peripheral endpoints  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1236
34.6 USB host  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1238
34.6.1 SRP-capable host  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1239
34.6.2 USB host states . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1239
34.6.3 Host channels  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1241
34.6.4 Host scheduler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1242
34.7 SOF trigger . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1243
34.7.1 Host SOFs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1243
34.7.2 Peripheral SOFs  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1244
34.8 OTG low-power modes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1244
34.9 Dynamic update of the OTG_FS_HFIR register . . . . . . . . . . . . . . . . . . 1245
34.10 USB data FIFOs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1246
34.11 Peripheral FIFO architecture  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1247
34.11.1 Peripheral Rx FIFO  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1247
34.11.2 Peripheral Tx FIFOs  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1248
34.12 Host FIFO architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1248
34.12.1 Host Rx FIFO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1248
34.12.2 Host Tx FIFOs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1249
34.13 FIFO RAM allocation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1249
34.13.1 Device mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1249
34.13.2 Host mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1250
34.14 USB system performance  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1250
34.15 OTG_FS interrupts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1251
34.16 OTG_FS control and status registers . . . . . . . . . . . . . . . . . . . . . . . . . . 1253
34.16.1 CSR memory map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1254
34.16.2 OTG_FS global registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1259
34.16.3 Host-mode registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1280
34.16.4 Device-mode registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1290

Contents RM0090
34/1741 RM0090 Rev 22
34.16.5 OTG_FS power and clock gating control register
(OTG_FS_PCGCCTL) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1313
34.16.6 OTG_FS register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1314
34.17 OTG_FS programming model  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1323
34.17.1 Core initialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1323
34.17.2 Host initialization  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1324
34.17.3 Device initialization  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1324
34.17.4 Host programming model  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1325
34.17.5 Device programming model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1341
34.17.6 Operational model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1343
34.17.7 Worst case response time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1361
34.17.8 OTG programming model  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1362
35 USB on-the-go high-speed (OTG_HS) . . . . . . . . . . . . . . . . . . . . . . . . 1369
35.1 OTG_HS introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1369
35.2 OTG_HS main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1369
35.2.1 General features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1370
35.2.2 Host-mode features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1371
35.2.3 Peripheral-mode features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1371
35.3 OTG_HS functional description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1371
35.3.1 OTG pins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1372
35.3.2 High-speed OTG PHY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1372
35.3.3 Embedded Full-speed OTG PHY  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1373
35.4 OTG dual-role device . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1373
35.4.1 ID line detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1373
35.4.2 HNP dual role device . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1373
35.4.3 SRP dual-role device . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1374
35.5 USB functional description in peripheral mode  . . . . . . . . . . . . . . . . . . 1374
35.5.1 SRP-capable peripheral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1374
35.5.2 Peripheral states  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1375
35.5.3 Peripheral endpoints  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1376
35.6 USB functional description on host mode  . . . . . . . . . . . . . . . . . . . . . . 1379
35.6.1 SRP-capable host  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1379
35.6.2 USB host states . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1380
35.6.3 Host channels  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1381
35.6.4 Host scheduler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1383

RM0090 Rev 22 35/1741
RM0090 Contents
39
35.7 SOF trigger . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1384
35.7.1 Host SOFs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1384
35.7.2 Peripheral SOFs  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1384
35.8 OTG_HS low-power modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1385
35.9 Dynamic update of the OTG_HS_HFIR register  . . . . . . . . . . . . . . . . . 1386
35.10 FIFO RAM allocation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1387
35.10.1 Peripheral mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1387
35.10.2 Host mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1387
35.11 OTG_HS interrupts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1388
35.12 OTG_HS control and status registers  . . . . . . . . . . . . . . . . . . . . . . . . . 1390
35.12.1 CSR memory map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1390
35.12.2 OTG_HS global registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1395
35.12.3 Host-mode registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1418
35.12.4 Device-mode registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1431
35.12.5 OTG_HS power and clock gating control register
(OTG_HS_PCGCCTL)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1460
35.12.6 OTG_HS register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1460
35.13 OTG_HS programming model  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1475
35.13.1 Core initialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1475
35.13.2 Host initialization  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1476
35.13.3 Device initialization  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1477
35.13.4 DMA mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1477
35.13.5 Host programming model  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1477
35.13.6 Device programming model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1503
35.13.7 Operational model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1505
35.13.8 Worst case response time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1524
35.13.9 OTG programming model  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1526
36 Flexible static memory controller (FSMC)   . . . . . . . . . . . . . . . . . . . . 1532
36.1 FSMC main features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1532
36.2 Block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1533
36.3 AHB interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1533
36.3.1 Supported memories and transactions  . . . . . . . . . . . . . . . . . . . . . . . 1534
36.4 External device address mapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1535
36.4.1 NOR/PSRAM address mapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1535
36.4.2 NAND/PC Card address mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . 1536

Contents RM0090
36/1741 RM0090 Rev 22
36.5 NOR flash/PSRAM controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1537
36.5.1 External memory interface signals . . . . . . . . . . . . . . . . . . . . . . . . . . . 1538
36.5.2 Supported memories and transactions  . . . . . . . . . . . . . . . . . . . . . . . 1540
36.5.3 General timing rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1541
36.5.4 NOR flash/PSRAM controller asynchronous transactions . . . . . . . . . 1542
36.5.5 Synchronous transactions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1559
36.5.6 NOR/PSRAM control registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1565
36.6 NAND flash/PC Card controller  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1572
36.6.1 External memory interface signals . . . . . . . . . . . . . . . . . . . . . . . . . . . 1573
36.6.2 NAND flash / PC Card supported me mories and transactions  . . . . . 1575
36.6.3 Timing diagrams for NAND and PC Card  . . . . . . . . . . . . . . . . . . . . . 1575
36.6.4 NAND flash operations  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1576
36.6.5 NAND flash prewait functionality . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1577
36.6.6 Computation of the error correction code (ECC)
in NAND flash memory  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1578
36.6.7 PC Card/CompactFlash operations . . . . . . . . . . . . . . . . . . . . . . . . . . 1579
36.6.8 NAND flash/PC Card control registers . . . . . . . . . . . . . . . . . . . . . . . . 1581
36.6.9 FSMC register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1588
37 Flexible memory controller (FMC) . . . . . . . . . . . . . . . . . . . . . . . . . . . 1590
37.1 FMC main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1590
37.2 Block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1591
37.3 AHB interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1592
37.3.1 Supported memories and transactions  . . . . . . . . . . . . . . . . . . . . . . . 1593
37.4 External device address mapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1594
37.4.1 NOR/PSRAM address mapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1595
37.4.2 NAND Flash memory/PC Card address m apping . . . . . . . . . . . . . . . 1596
37.4.3 SDRAM address mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1597
37.5 NOR Flash/PSRAM controller  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1600
37.5.1 External memory interface signals . . . . . . . . . . . . . . . . . . . . . . . . . . . 1601
37.5.2 Supported memories and transactions  . . . . . . . . . . . . . . . . . . . . . . . 1603
37.5.3 General timing rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1605
37.5.4 NOR Flash/PSRAM controller asynchron ous transactions  . . . . . . . . 1605
37.5.5 Synchronous transactions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1622
37.5.6 NOR/PSRAM controller registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1628
37.6 NAND Flash/PC Card controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1635
37.6.1 External memory interface signals . . . . . . . . . . . . . . . . . . . . . . . . . . . 1636

RM0090 Rev 22 37/1741
RM0090 Contents
39
37.6.2 NAND Flash / PC Card supported memories and transactions . . . . . 1638
37.6.3 Timing diagrams for NAND Flash memory and PC Card  . . . . . . . . . 1638
37.6.4 NAND Flash operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1639
37.6.5 NAND Flash prewait functionality  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1640
37.6.6 Computation of the error correction code (ECC)
in NAND Flash memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1641
37.6.7 PC Card/CompactFlash operations . . . . . . . . . . . . . . . . . . . . . . . . . . 1642
37.6.8 NAND Flash/PC Card controller registers . . . . . . . . . . . . . . . . . . . . . 1644
37.7 SDRAM controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1651
37.7.1 SDRAM controller main features . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1651
37.7.2 SDRAM External memory interface signals . . . . . . . . . . . . . . . . . . . . 1651
37.7.3 SDRAM controller functional description . . . . . . . . . . . . . . . . . . . . . . 1652
37.7.4 Low power modes  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1659
37.7.5 SDRAM controller registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1662
37.8 FMC register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1668
38 Debug support (DBG) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1671
38.1 Overview  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1671
38.2 Reference Arm® documentation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1672
38.3 SWJ debug port (serial wire and JTAG) . . . . . . . . . . . . . . . . . . . . . . . . 1672
38.3.1 Mechanism to select the JTAG-DP or the SW-DP . . . . . . . . . . . . . . . 1673
38.4 Pinout and debug port pins  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1673
38.4.1 SWJ debug port pins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1674
38.4.2 Flexible SWJ-DP pin assignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1674
38.4.3 Internal pull-up and pull-down on JTAG pins . . . . . . . . . . . . . . . . . . . 1674
38.4.4 Using serial wire and releasing th e unused debug pins as GPIOs  . . 1675
38.5 STM32F4xx JTAG TAP connection  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1675
38.6 ID codes and locking mechanism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1676
38.6.1 MCU device ID code  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1676
38.6.2 Boundary scan TAP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1677
38.6.3 Cortex ®-M4 with FPU TAP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1678
38.6.4 Cortex ®-M4 with FPU JEDEC-106 ID code . . . . . . . . . . . . . . . . . . . . 1678
38.7 JTAG debug port  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1678
38.8 SW debug port . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1680
38.8.1 SW protocol introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1680
38.8.2 SW protocol sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1680

Contents RM0090
38/1741 RM0090 Rev 22
38.8.3 SW-DP state machine (reset, idle states, ID code)  . . . . . . . . . . . . . . 1681
38.8.4 DP and AP read/write accesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1681
38.8.5 SW-DP registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1682
38.8.6 SW-AP registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1682
38.9 AHB-AP (AHB access port) - valid for both JTAG-DP
and SW-DP  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1683
38.10 Core debug  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1683
38.11 Capability of the debugger host to connect under system reset  . . . . . 1684
38.12 FPB (Flash patch breakpoint) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1685
38.13 DWT (data watchpoint trigger) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1686
38.14 ITM (instrumentation trace macrocell)  . . . . . . . . . . . . . . . . . . . . . . . . . 1686
38.14.1 General description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1686
38.14.2 Time stamp packets, synchronization  and overflow packets . . . . . . . 1686
38.15 ETM (Embedded Trace Macrocell™) . . . . . . . . . . . . . . . . . . . . . . . . . . 1688
38.15.1 ETM general description  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1688
38.15.2 ETM signal protocol and packet types . . . . . . . . . . . . . . . . . . . . . . . . 1688
38.15.3 Main ETM registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1689
38.15.4 ETM configuration example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1689
38.16 MCU debug component (DBGMCU)  . . . . . . . . . . . . . . . . . . . . . . . . . . 1689
38.16.1 Debug support for low-power modes . . . . . . . . . . . . . . . . . . . . . . . . . 1689
38.16.2 Debug support for time rs, watchdog, bxCAN and I2C . . . . . . . . . . . . 1690
38.16.3 Debug MCU configuration register  . . . . . . . . . . . . . . . . . . . . . . . . . . 1690
38.16.4 Debug MCU APB1 freeze  register (DBGMCU_APB1_FZ)  . . . . . . . . 1692
38.16.5 Debug MCU APB2 Freeze register (DBGMCU_APB2_FZ) . . . . . . . . 1693
38.17 TPIU (trace port interface unit) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1694
38.17.1 Introduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1694
38.17.2 TRACE pin assignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1695
38.17.3 TPUI formatter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1696
38.17.4 TPUI frame synchronization packets . . . . . . . . . . . . . . . . . . . . . . . . . 1697
38.17.5 Transmission of the synchronization fr ame packet  . . . . . . . . . . . . . . 1697
38.17.6 Synchronous mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1697
38.17.7 Asynchronous mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1698
38.17.8 TRACECLKIN connection inside the STM32F4xx . . . . . . . . . . . . . . . 1698
38.17.9 TPIU registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1698
38.17.10 Example of configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1699
38.18 DBG register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1700

RM0090 Rev 22 39/1741
RM0090 Contents
39
39 Device electronic signature  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1701
39.1 Unique device ID register (96 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1701
39.2 Flash size . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1702
40 Important security notice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1703
41 Revision history  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1704
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* *No dedicated configuration tables referenced in this chapter text.*

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)