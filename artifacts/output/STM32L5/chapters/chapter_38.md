# Chapter 38: Infrared interface (IRTIM)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 38: Infrared interface (IRTIM).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 1379 - 1379
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 1379/2187
RM0438 Infrared interface (IRTIM)
1379
38 Infrared interface (IRTIM)
An infrared interface (IRTIM) for remote control is available on the device. It can be used
with an infrared LED to perform remote control functions.
It uses internal connections with TIM16, and TIM17 as shown in [Figure 394](../figures/figure_394.md).
To generate the infrared remote control signals, the IR interface must be enabled and TIM16
channel 1 (TIM16_OC1) and TIM17 channel 1 (TIM17_OC1) must be properly configured to
generate correct waveforms.
The infrared receiver can be implemented easily through a basic input capture mode.
[Figure 394](../figures/figure_394.md). IRTIM internal hardware connections with TIM16 and TIM17
All standard IR pulse modulation modes can be obtained by programming the two timer
output compare channels.
TIM17 is used to generate the high frequency carrier signal, while TIM16 generates the
modulation envelope.
The infrared function is output on the IR_OUT pin. The activation of this function is done
through the GPIOx_AFRx register by enabling the related alternate function bit.
The high sink LED driver capability (only available on the PB9 pin) can be activated through
the I2C_PB9_FMP bit in the SYSCFG_CFGR1 register and used to sink the high current
needed to directly control an infrared LED.
MS30474V2
TIM17_CH1
TIM16_CH1
IRTIM IR_OUT
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 394: Architectural Diagram](../figures/figure_394.md)

## 4. Referenced Configuration Tables in this Chapter
* *No dedicated configuration tables referenced in this chapter text.*

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)