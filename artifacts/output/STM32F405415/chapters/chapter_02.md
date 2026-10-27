# Chapter 2: List of tables

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32F4 Reference Manual RM0090 - Chapter 2: List of tables.
* **Document Source**: RM0090 Reference Manual
* **PDF Reference Location**: Pages 40 - 46
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0090 Ingestion)
```text
List of tables RM0090
40/1741 RM0090 Rev 22
List of tables
[Table 1](../tables/table_1.md). STM32F4xx register boundary addresses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
[Table 2](../tables/table_2.md). Boot modes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . 69
[Table 3](../tables/table_3.md). Memory mapping vs. Boot mode/physical remap
in STM32F405xx/07xx and STM32F415xx/17xx  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
[Table 4](../tables/table_4.md). Memory mapping vs. Boot mode/physical remap
in STM32F42xxx and STM32F43xxx . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
[Table 5](../tables/table_5.md). Flash module organization (STM32F40x and STM32F 41x) . . . . . . . . . . . . . . . . . . . . . . . . 75
[Table 6](../tables/table_6.md). Flash module - 2 Mbyte dual bank organization (STM32F42xxx and STM32F43xxx) . . . . 77
[Table 7](../tables/table_7.md). 1 Mbyte flash memory sing le bank vs dual bank organization
(STM32F42xxx and STM32F43xxx)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
[Table 8](../tables/table_8.md). 1 Mbyte single bank flash memory organization
(STM32F42xxx and STM32F43xxx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
[Table 9](../tables/table_9.md). 1 Mbyte dual bank flash memory organiz ation (STM32F42xxx and STM32F43xxx) . . . . . 79
[Table 10](../tables/table_10.md). 512 Kbyte single bank flash memory organization
(STM32F42xxx and STM32F43xxx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
[Table 11](../tables/table_11.md). Number of wait states according to CPU clock (HCLK) frequency
(STM32F405xx/07xx and STM32F415xx/17xx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
[Table 12](../tables/table_12.md). Number of wait states according to CPU clock (HCLK) frequency
(STM32F42xxx and STM32F43xxx)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
[Table 13](../tables/table_13.md). Maximum program/erase parallelism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
[Table 14](../tables/table_14.md). Flash interrupt reques t . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
[Table 15](../tables/table_15.md). Option byte organization. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
[Table 16](../tables/table_16.md). Description of the option bytes (STM32F405xx/07xx and STM32F415xx/17xx)  . . . . . . . . 89
[Table 17](../tables/table_17.md). Description of the option bytes
(STM32F42xxx and STM32F43xxx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
[Table 18](../tables/table_18.md). Access versus read protection le vel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
[Table 19](../tables/table_19.md). OTP area organization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
[Table 20](../tables/table_20.md). Flash register map and reset values
(STM32F405xx/07xx and STM32F415xx/17xx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
[Table 21](../tables/table_21.md). Flash register map and reset values (STM32F42xxx and STM32F43xxx). . . . . . . . . . . . 111
[Table 22](../tables/table_22.md). CRC calculation unit register map and reset values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
[Table 23](../tables/table_23.md). Voltage regulator configuration mode versus device operating mode . . . . . . . . . . . . . . . 122
[Table 24](../tables/table_24.md). Low-power mode summary  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 28
[Table 25](../tables/table_25.md). Sleep-now entry and exit  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 129
[Table 26](../tables/table_26.md). Sleep-on-exit entry and exit  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 130
[Table 27](../tables/table_27.md). Stop operating modes
(STM32F405xx/07xx and STM32F415xx/17xx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
[Table 28](../tables/table_28.md). Stop mode entry and exit (for STM32F4 05xx/07xx and STM32F415xx/17xx) . . . . . . . . . 132
[Table 29](../tables/table_29.md). Stop operating modes (STM32F42xxx and STM32F 43xxx). . . . . . . . . . . . . . . . . . . . . . . 134
[Table 30](../tables/table_30.md). Stop mode entry and exit (STM32F42xxx and STM32F43xxx)  . . . . . . . . . . . . . . . . . . . . 136
[Table 31](../tables/table_31.md). Standby mode entry and exit  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
[Table 32](../tables/table_32.md). PWR - register map and reset values for
STM32F405xx/07xx and STM32F415xx/17xx . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
[Table 33](../tables/table_33.md). PWR - register map and reset values fo r STM32F42xxx and STM32F43xxx  . . . . . . . . . 150
[Table 34](../tables/table_34.md). RCC register map and reset values for STM32F42xxx and STM32F43xxx . . . . . . . . . . . 211
[Table 35](../tables/table_35.md). RCC register map and reset values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 6
[Table 36](../tables/table_36.md). Port bit configuration table  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270
[Table 37](../tables/table_37.md). Flexible SWJ-DP pin assignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27 3

RM0090 Rev 22 41/1741
RM0090 List of tables
46
[Table 38](../tables/table_38.md). RTC_AF1 pin  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
[Table 39](../tables/table_39.md). RTC_AF2 pin  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282
[Table 40](../tables/table_40.md). GPIO register map and reset values  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
[Table 41](../tables/table_41.md). SYSCFG register  map and reset values
(STM32F405xx/07xx and STM32F415xx/17xx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296
[Table 42](../tables/table_42.md). SYSCFG register map and reset values (STM32F42xxx and STM32F43xxx). . . . . . . . . 303
[Table 43](../tables/table_43.md). DMA1 request mapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 309
[Table 44](../tables/table_44.md). DMA2 request mapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 310
[Table 45](../tables/table_45.md). Source and destination address . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
[Table 46](../tables/table_46.md). Source and destination address registers in Double buffer mode (DBM=1). . . . . . . . . . . 316
[Table 47](../tables/table_47.md). Packing/unpacking & endian behavior (bit PINC = MINC = 1) . . . . . . . . . . . . . . . . . . . . . 317
[Table 48](../tables/table_48.md). Restriction on NDT versus PSIZE and MSIZE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 318
[Table 49](../tables/table_49.md). FIFO threshold configurations  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 320
[Table 50](../tables/table_50.md). Possible DMA configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 324
[Table 51](../tables/table_51.md). DMA interrupt requests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 326
[Table 52](../tables/table_52.md). DMA register map and reset values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337
[Table 53](../tables/table_53.md). Supported color mode in input . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 344
[Table 54](../tables/table_54.md). Data order in memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345
[Table 55](../tables/table_55.md). Alpha mode configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346
[Table 56](../tables/table_56.md). Supported CLUT color mode  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347
[Table 57](../tables/table_57.md). CLUT data order in memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  347
[Table 58](../tables/table_58.md). Supported color mode in output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  348
[Table 59](../tables/table_59.md). Data order in memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348
[Table 60](../tables/table_60.md). DMA2D interrupt requests  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 353
[Table 61](../tables/table_61.md). DMA2D register map and reset values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371
[Table 62](../tables/table_62.md). Vector table for STM32F405xx/07xx and STM32F41 5xx/17xx. . . . . . . . . . . . . . . . . . . . . 374
[Table 63](../tables/table_63.md). Vector table for STM32F42xxx a nd STM32F43xxx  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377
[Table 64](../tables/table_64.md). External interrupt/event controller register map and reset values. . . . . . . . . . . . . . . . . . . 389
[Table 65](../tables/table_65.md). ADC pins. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 392
[Table 66](../tables/table_66.md). Analog watchdog channel selection .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 395
[Table 67](../tables/table_67.md). Configuring the trigger polarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 399
[Table 68](../tables/table_68.md). External trigger for regular channels. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 400
[Table 69](../tables/table_69.md). External trigger for injected channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 401
[Table 70](../tables/table_70.md). ADC interrupts  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 416
[Table 71](../tables/table_71.md). ADC global register map. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 432
[Table 72](../tables/table_72.md). ADC register map and reset values for each ADC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 433
[Table 73](../tables/table_73.md). ADC register map and reset values (common ADC registers) . . . . . . . . . . . . . . . . . . . . . 434
[Table 74](../tables/table_74.md). DAC pins. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 436
[Table 75](../tables/table_75.md). External triggers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 439
[Table 76](../tables/table_76.md). DAC register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 455
[Table 77](../tables/table_77.md). DCMI pins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . 457
[Table 78](../tables/table_78.md). DCMI signals  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 459
[Table 79](../tables/table_79.md). Positioning of captured data bytes in 32-bit word s (8-bit width) . . . . . . . . . . . . . . . . . . . . 460
[Table 80](../tables/table_80.md). Positioning of captured data bytes in 32-bit word s (10-bit width) . . . . . . . . . . . . . . . . . . . 460
[Table 81](../tables/table_81.md). Positioning of captured data bytes in 32-bit word s (12-bit width) . . . . . . . . . . . . . . . . . . . 461
[Table 82](../tables/table_82.md). Positioning of captured data bytes in 32-bit word s (14-bit width) . . . . . . . . . . . . . . . . . . . 461
[Table 83](../tables/table_83.md). Data storage in monochrome progressive video fo rmat . . . . . . . . . . . . . . . . . . . . . . . . . . 468
[Table 84](../tables/table_84.md). Data storage in RGB progressive video format  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
[Table 85](../tables/table_85.md). Data storage in YCbCr progressive video format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 469
[Table 86](../tables/table_86.md). DCMI interrupts. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 469
[Table 87](../tables/table_87.md). DCMI register map and reset values  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 478
[Table 88](../tables/table_88.md). LTDC registers versus clock domain  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 482

List of tables RM0090
42/1741 RM0090 Rev 22
[Table 89](../tables/table_89.md). LCD-TFT pins and signal interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 83
[Table 90](../tables/table_90.md). Pixel Data mapping versus Colo r Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487
[Table 91](../tables/table_91.md). LTDC interrupt requests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 491
[Table 92](../tables/table_92.md). LTDC register map and reset values  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 512
[Table 93](../tables/table_93.md). Counting direction versus encoder signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 552
[Table 94](../tables/table_94.md). TIMx Internal trigger connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 565
[Table 95](../tables/table_95.md). Output control bits for comp lementary OCx and OCxN channels with
break feature. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 576
[Table 96](../tables/table_96.md). TIM1 and TIM8 register map and reset values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 584
[Table 97](../tables/table_97.md). Counting direction versus encoder signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 613
[Table 98](../tables/table_98.md). TIMx internal trigger connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 628
[Table 99](../tables/table_99.md). Output control bit for standard OCx channels. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 637
[Table 100](../tables/table_100.md). TIM2 to TIM5 register map and reset values  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 644
[Table 101](../tables/table_101.md). TIMx internal trigger connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 670
[Table 102](../tables/table_102.md). Output control bit for standard OCx channels. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 678
[Table 103](../tables/table_103.md). TIM9/12 register map and reset values  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 680
[Table 104](../tables/table_104.md). Output control bit for standard OCx channels. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 687
[Table 105](../tables/table_105.md). TIM10/11/13/14 register map and reset values  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 690
[Table 106](../tables/table_106.md). TIM6 and TIM7 register map and reset values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 703
[Table 107](../tables/table_107.md). Min/max IWDG timeout period (in ms) at 32 kHz (LSI). . . . . . . . . . . . . . . . . . . . . . . . . . . 705
[Table 108](../tables/table_108.md). IWDG register map and reset valu es . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70 8
[Table 109](../tables/table_109.md). Minimum and maximum timeout values at 30 MHz (f PCLK1). . . . . . . . . . . . . . . . . . . . . . . 712
[Table 110](../tables/table_110.md). WWDG register map and reset valu es . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 715
[Table 111](../tables/table_111.md). Number of cycles required to process each 128-bit block
(STM32F415/417xx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 716
[Table 112](../tables/table_112.md). Number of cycles required to process each 128-bit block
(STM32F43xxx)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 716
[Table 113](../tables/table_113.md). Data types. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 736
[Table 114](../tables/table_114.md). CRYP register map and reset values for STM32F 415/417xx. . . . . . . . . . . . . . . . . . . . . . 759
[Table 115](../tables/table_115.md). CRYP register map and reset values for STM32F43 xxx  . . . . . . . . . . . . . . . . . . . . . . . . . 760
[Table 116](../tables/table_116.md). RNG register map and reset map. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 67
[Table 117](../tables/table_117.md). HASH register map and reset values on STM32F 415/417xx . . . . . . . . . . . . . . . . . . . . . . 791
[Table 118](../tables/table_118.md). HASH register map and reset values on STM32F43 xxx  . . . . . . . . . . . . . . . . . . . . . . . . . 792
[Table 119](../tables/table_119.md). Effect of low-power modes on RT C  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 810
[Table 120](../tables/table_120.md). Interrupt control bits  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 811
[Table 121](../tables/table_121.md). RTC register map and reset values  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 832
[Table 122](../tables/table_122.md). Maximum DNF[3:0] value to be compliant with Thd: dat(max)  . . . . . . . . . . . . . . . . . . . . . 847
[Table 123](../tables/table_123.md). SMBus vs. I2C  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 849
[Table 124](../tables/table_124.md). I2C Interrupt requests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . 853
[Table 125](../tables/table_125.md). I2C register map and reset values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 867
[Table 126](../tables/table_126.md). SPI interrupt requests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . 893
[Table 127](../tables/table_127.md). Audio frequency precision (for PLLM VCO = 1 M Hz or 2 MHz) . . . . . . . . . . . . . . . . . . . . 904
[Table 128](../tables/table_128.md). I 2S interrupt requests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91 0
[Table 129](../tables/table_129.md). SPI register map and reset values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 920
[Table 130](../tables/table_130.md). Example of possible audio frequency sampling rang e . . . . . . . . . . . . . . . . . . . . . . . . . . . 931
[Table 131](../tables/table_131.md). Interrupt sources. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 943
[Table 132](../tables/table_132.md). SAI register map and reset values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 958
[Table 133](../tables/table_133.md). Noise detection from sampled data  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 972
[Table 134](../tables/table_134.md). Error calculation for programmed baud rates at f PCLK = 8 MHz or fPCLK = 12 MHz,
oversampling by 16. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 75
[Table 135](../tables/table_135.md). Error calculation for programmed baud rates at f PCLK = 8 MHz or fPCLK =12 MHz,
oversampling by 8. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 976

RM0090 Rev 22 43/1741
RM0090 List of tables
46
[Table 136](../tables/table_136.md). Error calculation for programmed baud rates at f PCLK = 16 MHz or fPCLK = 24 MHz,
oversampling by 16. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 76
[Table 137](../tables/table_137.md). Error calculation for programmed baud rates at f PCLK = 16 MHz or fPCLK = 24 MHz,
oversampling by 8. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 977
[Table 138](../tables/table_138.md). Error calculation for programmed baud rates at fPCLK = 8 MHz or fPCLK = 16 MHz,
oversampling by 16. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 78
[Table 139](../tables/table_139.md). Error calculation for programmed baud rates at fPCLK = 8 MHz or fPCLK = 16 MHz,
oversampling by 8. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 978
[Table 140](../tables/table_140.md). Error calculation for programmed baud rates at fPCLK = 30 MHz or fPCLK = 60 MHz,
oversampling by 16. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 79
[Table 141](../tables/table_141.md). Error calculation for programmed baud rates at fPCLK = 30 MHz or fPCLK = 60 MHz,
oversampling by 8  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 980
[Table 142](../tables/table_142.md). Error calculation for programmed baud rates at fPCLK = 42  MHz or fPCLK = 84 Hz,
oversampling by 16. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 81
[Table 143](../tables/table_143.md). Error calculation for programmed baud rates at fPCLK = 42  MHz or fPCLK = 84 MHz,
oversampling by 8. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 982
[Table 144](../tables/table_144.md). USART receiver’s tolerance when DIV fraction is 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 983
[Table 145](../tables/table_145.md). USART receiver tolerance when DIV_Fraction is  different from 0 . . . . . . . . . . . . . . . . . . 984
[Table 146](../tables/table_146.md). Frame formats  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 986
[Table 147](../tables/table_147.md). USART interrupt requests. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 1001
[Table 148](../tables/table_148.md). USART mode configuration  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1002
[Table 149](../tables/table_149.md). USART register map and reset values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1013
[Table 150](../tables/table_150.md). SDIO I/O definitions  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1018
[Table 151](../tables/table_151.md). Command format  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1022
[Table 152](../tables/table_152.md). Short response format  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 1023
[Table 153](../tables/table_153.md). Long response format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1023
[Table 154](../tables/table_154.md). Command path status flags  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  1023
[Table 155](../tables/table_155.md). Data token format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1026
[Table 156](../tables/table_156.md). Transmit FIFO status flags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 1027
[Table 157](../tables/table_157.md). Receive FIFO status flags  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 1028
[Table 158](../tables/table_158.md). Card status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1038
[Table 159](../tables/table_159.md). SD status  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . 1040
[Table 160](../tables/table_160.md). Speed class code field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1042
[Table 161](../tables/table_161.md). Performance move field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1042
[Table 162](../tables/table_162.md). AU_SIZE field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1042
[Table 163](../tables/table_163.md). Maximum AU size. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1043
[Table 164](../tables/table_164.md). Erase size field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 1043
[Table 165](../tables/table_165.md). Erase timeout field  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . 1043
[Table 166](../tables/table_166.md). Erase offset field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 1044
[Table 167](../tables/table_167.md). Block-oriented write commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 046
[Table 168](../tables/table_168.md). Block-oriented write protection commands. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1047
[Table 169](../tables/table_169.md). Erase commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1047
[Table 170](../tables/table_170.md). I/O mode commands  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 1047
[Table 171](../tables/table_171.md). Lock card  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . 1048
[Table 172](../tables/table_172.md). Application-specific commands  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 048
[Table 173](../tables/table_173.md). R1 response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1049
[Table 174](../tables/table_174.md). R2 response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1049
[Table 175](../tables/table_175.md). R3 response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1050
[Table 176](../tables/table_176.md). R4 response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1050
[Table 177](../tables/table_177.md). R4b response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . 1050
[Table 178](../tables/table_178.md). R5 response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1051
[Table 179](../tables/table_179.md). R6 response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1051

List of tables RM0090
44/1741 RM0090 Rev 22
[Table 180](../tables/table_180.md). Response type and SD IO_RESPx registers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1058
[Table 181](../tables/table_181.md). SDIO register map  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . 1068
[Table 182](../tables/table_182.md). Transmit mailbox mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1084
[Table 183](../tables/table_183.md). Receive mailbox mapping. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1084
[Table 184](../tables/table_184.md). bxCAN register map and reset values  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1109
[Table 185](../tables/table_185.md). Alternate function mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1116
[Table 186](../tables/table_186.md). Management frame format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1118
[Table 187](../tables/table_187.md). Clock range. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1120
[Table 188](../tables/table_188.md). TX interface signal encoding  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1121
[Table 189](../tables/table_189.md). RX interface signal encoding  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1122
[Table 190](../tables/table_190.md). Frame statuses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . 1137
[Table 191](../tables/table_191.md). Destination address filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1143
[Table 192](../tables/table_192.md). Source address filtering  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1144
[Table 193](../tables/table_193.md). Receive descriptor 0 - encoding  for bits 7, 5 and 0 (normal descriptor
format only, EDFE=0) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1174
[Table 194](../tables/table_194.md). Time stamp snapshot dependency  on registers bits  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1206
[Table 195](../tables/table_195.md). Ethernet register map and reset values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1224
[Table 196](../tables/table_196.md). OTG_FS input/output pins  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1231
[Table 197](../tables/table_197.md). Compatibility of ST M32 low power modes with the OTG . . . . . . . . . . . . . . . . . . . . . . . . 1244
[Table 198](../tables/table_198.md). Core global control and status registers (CSRs). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1254
[Table 199](../tables/table_199.md). Host-mode control and status registers (CSRs) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1255
[Table 200](../tables/table_200.md). Device-mode control and status registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1256
[Table 201](../tables/table_201.md). Data FIFO (DFIFO) access register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1257
[Table 202](../tables/table_202.md). Power and clock gating control and status registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1258
[Table 203](../tables/table_203.md). TRDT values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1264
[Table 204](../tables/table_204.md). Minimum duration for soft disconnect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129 2
[Table 205](../tables/table_205.md). OTG_FS register map and reset values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1314
[Table 206](../tables/table_206.md). OTG_HS input/output pins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1372
[Table 207](../tables/table_207.md). Compatibility of ST M32 low power modes with the OTG . . . . . . . . . . . . . . . . . . . . . . . . 1385
[Table 208](../tables/table_208.md). Core global control and status registers (CSRs). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1391
[Table 209](../tables/table_209.md). Host-mode control and status registers (CSRs) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1392
[Table 210](../tables/table_210.md). Device-mode control and status registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1393
[Table 211](../tables/table_211.md). Data FIFO (DFIFO) access register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1395
[Table 212](../tables/table_212.md). Power and clock gating control and status registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . 1395
[Table 213](../tables/table_213.md). TRDT values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1402
[Table 214](../tables/table_214.md). Minimum duration for soft disconnect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143 4
[Table 215](../tables/table_215.md). OTG_HS register map and reset values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1460
[Table 216](../tables/table_216.md). NOR/PSRAM bank selection  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 36
[Table 217](../tables/table_217.md). External memory address. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1536
[Table 218](../tables/table_218.md). Memory mapping and timing registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1536
[Table 219](../tables/table_219.md). NAND bank selections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1537
[Table 220](../tables/table_220.md). Programmable NOR/PSRAM access parameters  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1538
[Table 221](../tables/table_221.md). Nonmultiplexed I/O NOR flash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1538
[Table 222](../tables/table_222.md). Multiplexed I/O NOR flash  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 1539
[Table 223](../tables/table_223.md). Nonmultiplexed I/Os PSRAM/SRAM  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1539
[Table 224](../tables/table_224.md). Multiplexed I/O PSRAM  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 1540
[Table 225](../tables/table_225.md). NOR flash/PSRAM controller: example of supported memories and transactions. . . . . 1540
[Table 226](../tables/table_226.md). FSMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1543
[Table 227](../tables/table_227.md). FSMC_BTRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1544
[Table 228](../tables/table_228.md). FSMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1545
[Table 229](../tables/table_229.md). FSMC_BTRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1546
[Table 230](../tables/table_230.md). FSMC_BWTRx bit fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1546

RM0090 Rev 22 45/1741
RM0090 List of tables
46
[Table 231](../tables/table_231.md). FSMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1548
[Table 232](../tables/table_232.md). FSMC_BTRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1549
[Table 233](../tables/table_233.md). FSMC_BWTRx bit fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1549
[Table 234](../tables/table_234.md). FSMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1551
[Table 235](../tables/table_235.md). FSMC_BTRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1551
[Table 236](../tables/table_236.md). FSMC_BWTRx bit fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1552
[Table 237](../tables/table_237.md). FSMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1553
[Table 238](../tables/table_238.md). FSMC_BTRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1554
[Table 239](../tables/table_239.md). FSMC_BWTRx bit fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1554
[Table 240](../tables/table_240.md). FSMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1556
[Table 241](../tables/table_241.md). FSMC_BTRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1556
[Table 242](../tables/table_242.md). FSMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1561
[Table 243](../tables/table_243.md). FSMC_BTRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1562
[Table 244](../tables/table_244.md). FSMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1563
[Table 245](../tables/table_245.md). FSMC_BTRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1564
[Table 246](../tables/table_246.md). Programmable NAND/PC Card access parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . 1573
[Table 247](../tables/table_247.md). 8-bit NAND flash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . 1573
[Table 248](../tables/table_248.md). 16-bit NAND flash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1574
[Table 249](../tables/table_249.md). 16-bit PC Card  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1574
[Table 250](../tables/table_250.md). Supported memories and transactions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1575
[Table 251](../tables/table_251.md). 16-bit PC-Card signals and access type. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1580
[Table 252](../tables/table_252.md). ECC result relevant bits  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1587
[Table 253](../tables/table_253.md). FSMC register map. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1588
[Table 254](../tables/table_254.md). NOR/PSRAM bank selection  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 95
[Table 255](../tables/table_255.md). NOR/PSRAM External memory address  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1596
[Table 256](../tables/table_256.md). NAND/PC Card memory mapping and timing regist ers . . . . . . . . . . . . . . . . . . . . . . . . . 1596
[Table 257](../tables/table_257.md). NAND bank selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 1597
[Table 258](../tables/table_258.md). SDRAM bank selection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 1597
[Table 259](../tables/table_259.md). SDRAM address mapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1597
[Table 260](../tables/table_260.md). SDRAM address mapping with 8-bit data bus width. . . . . . . . . . . . . . . . . . . . . . . . . . . . 1598
[Table 261](../tables/table_261.md). SDRAM address mapping with 16-bit data bus width.  . . . . . . . . . . . . . . . . . . . . . . . . . . 1599
[Table 262](../tables/table_262.md). SDRAM address mapping with 32-bit data bus width.  . . . . . . . . . . . . . . . . . . . . . . . . . . 1599
[Table 263](../tables/table_263.md). Programmable NOR/PSRAM access parameters  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1601
[Table 264](../tables/table_264.md). Non-multiplexed I/O NOR Flash memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1602
[Table 265](../tables/table_265.md). 16-bit multiplexed I/ O NOR Flash memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1602
[Table 266](../tables/table_266.md). Non-multiplexed I/Os PSRAM/SRAM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1602
[Table 267](../tables/table_267.md). 16-Bit multiplexed I/O PSRAM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1603
[Table 268](../tables/table_268.md). NOR Flash/PSRAM: Example of supported memories and transactions . . . . . . . . . . . . 1604
[Table 269](../tables/table_269.md). FMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 1607
[Table 270](../tables/table_270.md). FMC_BTRx bit fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1607
[Table 271](../tables/table_271.md). FMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 1609
[Table 272](../tables/table_272.md). FMC_BTRx bit fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1610
[Table 273](../tables/table_273.md). FMC_BWTRx bit fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 1610
[Table 274](../tables/table_274.md). FMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 1612
[Table 275](../tables/table_275.md). FMC_BTRx bit fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1613
[Table 276](../tables/table_276.md). FMC_BWTRx bit fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 1613
[Table 277](../tables/table_277.md). FMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 1615
[Table 278](../tables/table_278.md). FMC_BTRx bit fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1615
[Table 279](../tables/table_279.md). FMC_BWTRx bit fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 1616
[Table 280](../tables/table_280.md). FMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 1617
[Table 281](../tables/table_281.md). FMC_BTRx bit fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1618
[Table 282](../tables/table_282.md). FMC_BWTRx bit fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 1618

List of tables RM0090
46/1741 RM0090 Rev 22
[Table 283](../tables/table_283.md). FMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 1620
[Table 284](../tables/table_284.md). FMC_BTRx bit fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1620
[Table 285](../tables/table_285.md). FMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 1625
[Table 286](../tables/table_286.md). FMC_BTRx bit fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1625
[Table 287](../tables/table_287.md). FMC_BCRx bit fields  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 1626
[Table 288](../tables/table_288.md). FMC_BTRx bit fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1627
[Table 289](../tables/table_289.md). Programmable NAND Flash/PC Card access parame ters . . . . . . . . . . . . . . . . . . . . . . . 1636
[Table 290](../tables/table_290.md). 8-bit NAND Flash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1636
[Table 291](../tables/table_291.md). 16-bit NAND Flash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . 1637
[Table 292](../tables/table_292.md). 16-bit PC Card  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1637
[Table 293](../tables/table_293.md). Supported memories and transactions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1638
[Table 294](../tables/table_294.md). 16-bit PC-Card signals and access type. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1643
[Table 295](../tables/table_295.md). ECC result relevant bits  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1650
[Table 296](../tables/table_296.md). SDRAM signals. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1651
[Table 297](../tables/table_297.md). FMC register map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . 1668
[Table 298](../tables/table_298.md). SWJ debug port pins  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 1674
[Table 299](../tables/table_299.md). Flexible SWJ-DP pin assignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1674
[Table 300](../tables/table_300.md). JTAG debug port data registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1678
[Table 301](../tables/table_301.md). 32-bit debug port registers addressed through the shifted value A[3:2]  . . . . . . . . . . . . 1679
[Table 302](../tables/table_302.md). Packet request (8-bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . 1680
[Table 303](../tables/table_303.md). ACK response (3 bits). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1681
[Table 304](../tables/table_304.md). DATA transfer (33 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1681
[Table 305](../tables/table_305.md). SW-DP registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1682
[Table 306](../tables/table_306.md).  Cortex ®-M4 with FPU AHB-AP registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1683
[Table 307](../tables/table_307.md). Core debug registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1684
[Table 308](../tables/table_308.md). Main ITM registers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1687
[Table 309](../tables/table_309.md). Main ETM registers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . 1689
[Table 310](../tables/table_310.md). Asynchronous TRACE pin assignment. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1695
[Table 311](../tables/table_311.md). Synchronous TRACE pin assignment  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1695
[Table 312](../tables/table_312.md). Flexible TRACE pin assignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 96
[Table 313](../tables/table_313.md). Important TPIU registers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1698
[Table 314](../tables/table_314.md). DBG register map and reset values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170 0
[Table 315](../tables/table_315.md). Document revision history  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 1704
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* [Table 1: Configuration Matrix](../tables/table_1.md)
* [Table 2: Configuration Matrix](../tables/table_2.md)
* [Table 3: Configuration Matrix](../tables/table_3.md)
* [Table 4: Configuration Matrix](../tables/table_4.md)
* [Table 5: Configuration Matrix](../tables/table_5.md)
* [Table 6: Configuration Matrix](../tables/table_6.md)
* [Table 7: Configuration Matrix](../tables/table_7.md)
* [Table 8: Configuration Matrix](../tables/table_8.md)
* [Table 9: Configuration Matrix](../tables/table_9.md)
* [Table 10: Configuration Matrix](../tables/table_10.md)
* [Table 11: Configuration Matrix](../tables/table_11.md)
* [Table 12: Configuration Matrix](../tables/table_12.md)
* [Table 13: Configuration Matrix](../tables/table_13.md)
* [Table 14: Configuration Matrix](../tables/table_14.md)
* [Table 15: Configuration Matrix](../tables/table_15.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)