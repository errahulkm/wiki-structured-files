# Chapter 25: Operational amplifiers (OPAMP)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 25: Operational amplifiers (OPAMP).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 849 - 861
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Operational Amplifier (OPAMP)](../peripherals/opamp.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 849/2187
RM0438 Operational amplifiers (OPAMP)
861
25 Operational amplifiers (OPAMP)
25.1 Introduction
The device embeds two operational amplifiers with two inputs and one output each. The
three I/Os can be connected to the external pins, this enables any type of external
interconnections. The operational amplifier can be configured internally as a follower or as
an amplifier with a non-inverting gain ranging from 2 to 16.
The positive input can be connected to the internal DAC.
The output can be connected to the internal ADC.
25.2 OPAMP main features
• Rail-to-rail input voltage range
• Low input bias current (down to 1 nA)
• Low input offset voltage (1.5 mV after calibration, 3 mV with factory calibration)
• Low-power mode (current consumption reduced to 30 µA instead of 100 µA)
• Fast wakeup time (10 µs in normal mode, 30 µs in low-power mode)
• Gain bandwidth of 1.6 MHz
25.3 OPAMP functional description
The OPAMP has several modes.
Each OPAMP can be individually enabled, when disabled the output is high-impedance.
When enabled, it can be in calibration mode, all input and output of the OPAMP are then
disconnected, or in functional mode.
There are two functional modes, the low-power mode or the normal mode. In functional
mode the inputs and output of the OPAMP are connected as described in the
Section 25.3.3: Signal routing.
25.3.1 OPAMP reset and clocks
The operational amplifier clock is necessary for accessing the registers. When the
application does not need to have read or write access to those registers, the clock can be
switched off using the peripheral clock enable register (see OPAMPEN bit in Section 9.8.19:
RCC APB1 peripheral clock enable register 1 (RCC_APB1ENR1)).
The bit OPAEN enables and disables the OPAMP operation. The OPAMP registers
configurations should be changed before enabling the OPAEN bit in order to avoid spurious
effects on the output.
When the output of the operational amplifier is no more needed the operational amplifier can
be disabled to save power. All the configurations previously set (including the calibration)
are maintained while OPAMP is disabled.

Operational amplifiers (OPAMP) RM0438
850/2187 RM0438 Rev 8
25.3.2 Initial configuration
The default configuration of the operational amplifier is a functional mode where the three
IOs are connected to external pins. In the default mode the operational amplifier uses the
factory trimming values. See electrical characteristics section of the datasheet for factory
trimming conditions, usually the temperature is 30 °C and the voltage is 3 V. The trimming
values can be adjusted, see Section 25.3.5: Calibration for changing the trimming values.
The default configuration uses the normal mode, which provides the highest performance.
Bit OPALPM can be set in order to switch the operational amplifier to low-power mode and
reduced performance. Both normal and low-power mode characteristics are defined in the
section “electrical characteristics” of the datasheet. Before utilization, the bit OPA_RANGE
of OPAMP_CSR must be set to 1 if VDDA is above 2.4V, or kept at 0 otherwise.
As soon as the OPAEN bit in OPAMP_CSR register is set, the operational amplifier is
functional. The two input pins and the output pin are connected as defined in Section 25.3.3:
Signal routing and the default connection settings can be changed.
Note: The inputs and output pins must be conf igured in analog mode (default state) in the
corresponding GPIOx_MODER register.
25.3.3 Signal routing
The routing for the operational amplifier pins is determined by OPAMP_CSR register.
The connections of the two operational amplifiers (OPAMP1 and OPAMP2) are described in
the table below
[Table 202](../tables/table_202.md). Operational amplifier possible connections
Signal Pin Internal comment
OPAMP1_VINM PA1 or dedicated pin (1)
1. The dedicated pin is only avail able on BGA132 and BGA169 package. This configuration provides the
lowest input bias current (see datasheet).
OPAMP1_OUT or
PGA
Controlled by bits OPAMODE
and VM_SEL.
OPAMP1_VINP PA0 DAC1_OUT1 Controlled by bit VP_SEL.
OPAMP1_VOUT PA3 ADC1_IN8
The pin is connected when the
OPAMP is enabled. The ADC
input is controlled by ADC.
OPAMP2_VINM PA7 or dedicated
pinChapter 1.
OPAMP2_OUT or
PGA
Controlled by bits OPAMODE
and VM_SEL.
OPAMP2_VINP PA6 DAC1_OUT2 Controlled by bit VP_SEL
OPAMP2_VOUT PB0 ADC1_IN15
The pin is connected when the
OPAMP is enabled. The ADC
input is controlled by ADC.

RM0438 Rev 8 851/2187
RM0438 Operational amplifiers (OPAMP)
861
25.3.4 OPAMP modes
The operational amplifier inputs and outputs are all accessible on terminals. The amplifiers
can be used in multiple configuration environments:
• Standalone mode (external gain setting mode)
• Follower configuration mode
• PGA modes
Note: The amplifier output pin is directly connec ted to the output pad to minimize the output
impedance. It cannot be used as a general purpose I/O, even if the amplifier is configured
as a PGA and only connected to the ADC channel.
Note: The impedance of the signal must be maintained below a level which avoids the input
leakage to create significant artifacts (due to a resistive drop in the source). Please refer to
the electrical characteristics section in the datasheet for further details.
Standalone mode (external gain setting mode)
The procedure to use the OPAMP in standalone mode is presented hereafter.
Starting from the default value of OPAMP_CSR, and the default state of GPIOx_MODER,
configure bit OPA_RANGE according the VDDA voltage. As soon as the OPAEN bit is set,
the two input pins and the output pin are connected to the operational amplifier.
This default configuration uses the factory trimming values and operates in normal mode
(highest performance). The behavior of the OPAMP can be changed as follows:
• OPALPM can be set to “operational amplifier low-power” mode in order to save power.
• USERTRIM can be set to modify the trimming values for the input offset.
[Figure 176](../figures/figure_176.md). Standalone mode: external gain setting mode
MS35324V1
STM32
GPIO
DAC_OUT
GPIO
ADC
+
-

Operational amplifiers (OPAMP) RM0438
852/2187 RM0438 Rev 8
Follower configuration mode
The procedure to use the OPAMP in follower mode is presented hereafter.
• configure OPAMODE bits as “internal follower”
• configure VP_SEL bits as “GPIO connected to VINP”.
• As soon as the OPAEN bit is set, the signal on pin OPAMP_VINP is copied to pin
OPAMP_VOUT.
Note: The pin corresponding to OPAMP_VINM is free for another usage.
Note: The signal on the operational amplifier output is also seen as an ADC input. As a
consequence, the OPAMP configured in follower mode can be used to perform impedance
adaptation on input signals before feeding them to the ADC input, assuming the input signal
frequency is compatible with the operational amplifier gain bandwidth specification.
[Figure 177](../figures/figure_177.md). Follower configuration
MS35325V1
STM32
GPIO
DAC_OUT
GPIO
ADC
+
-
Always connected to
OPAMP output (can be
used during debug)

RM0438 Rev 8 853/2187
RM0438 Operational amplifiers (OPAMP)
861
Programmable Gain Amplifier mode
The procedure to use the OPAMP to amplify the amplitude of an input signal is
presented hereafter.
• configure OPAMODE bits as “internal PGA enabled”,
• configure PGA_GAIN bits as “internal PGA Gain 2, 4, 8 or 16”,
• configure VM_SEL bits as “inverting not externally connected”,
• configure VP_SEL bits as “GPIO connected to VINP”.
As soon as the OPAEN bit is set, the signal on pin OPAMP_VINP is amplified by the
selected gain and visible on pin OPAMP_VOUT.
Note: To avoid saturation, the input voltage should stay below V DDA divided by the selected gain.
[Figure 178](../figures/figure_178.md). PGA mode, internal gain setting (x2/x4/x8/x16), inverting input not used
MS35326V1
STM32
GPIO
DAC_OUT
GPIO
ADC
+
-
Always connected to
OPAMP output (can be
used during debug)

Operational amplifiers (OPAMP) RM0438
854/2187 RM0438 Rev 8
Programmable Gain Amplifier mode with external filtering
The procedure to use the OPAMP to amplify the amplitude of an input signal, with an
external filtering, is presented hereafter.
• configure OPAMODE bits as “internal PGA enabled”,
• configure PGA_GAIN bits as “internal PGA Gain 2, 4, 8 or 16”,
• configure VM_SEL bits as “GPIO connected to VINM”,
• configure VP_SEL bits as “GPIO connected to VINP”.
Any external connection on VINP can be used in parallel with the internal PGA, for
example a capacitor can be connected between VOUT and VINM for filtering purpose
(see datasheet for the value of resistors used in the PGA resistor network).
[Figure 179](../figures/figure_179.md). PGA mode, internal gain setting (x2/x4/x8/x16), inverting input used for
filtering
1. The gain depends on the cut-off frequency.
25.3.5 Calibration
At startup, the trimming values are initialized with the preset ‘factory’ trimming value.
Each operational amplifier offset can be trimmed by the user. Specific registers allow to
have different trimming values for normal mode and for low-power mode.
The aim of the calibration is to cancel as much as possible the OPAMP inputs offset voltage.
The calibration circuitry allows to reduce the inputs offset voltage to less than +/-1.5 mV
within stable voltage and temperature conditions.
For each operational amplifier and each mode two trimming values need to be trimmed, one
for N differential pair and one for P differential pair.
There are two registers for trimming the offsets for each operational amplifiers, one for
normal mode (OPAMP_OTR) and one low-power mode (OPAMP_LPOTR). Each register is
composed of five bits for P differential pair trimming and five bits for N differential pair
trimming. These are the ‘user’ values.
MS35327V1
STM32
GPIO
DAC_OUT
GPIO
ADC
+
-
Allows optional
low-pass
filtering (1)
Equivalent to

RM0438 Rev 8 855/2187
RM0438 Operational amplifiers (OPAMP)
861
The user is able to switch from ‘factory’ values to ‘user’ trimmed values using the
USERTRIM bit in the OPAMP_CSR register. This bit is reset at startup and so the ‘factory’
value are applied by default to the OPAMP trimming registers.
User is liable to change the trimming values in calibration or in functional mode.
The offset trimming registers are typically configured after the calibration operation is
initialized by setting bit CALON to 1. When CALON = 1 the inputs of the operational
amplifier are disconnected from the functional environment.
• Setting CALSEL to 1 initializes the offset calibration for the P differential pair (low
voltage reference used).
• Resetting CALSEL to 0 initializes the offset calibration for the N differential pair (high
voltage reference used).
When CALON = 1, the bit CALOUT will reflect the influence of the trimming value selected
by CALSEL and OPALPM. When the value of CALOUT switches between two consecutive
trimming values, this means that those two values are the best trimming values. The
CALOUT flag needs up to 1 ms after the trimming value is changed to become steady (see
tOFFTRIMmax delay specification in the electrical characteristics section of the datasheet).
Note: The closer the trimming va lue is to the optimum trimming value, the longer it takes to
stabilize (with a maximum stabilization time remaining below 1 ms in any case).
[Table 203](../tables/table_203.md). Operating modes and calibration
Mode
Control bits Output
OPAEN OPALPM CALON CALSEL V OUT
CALOUT
flag
Normal operating
mode 1 0 0 X analog 0
Low-power mode 1 1 0 X analog 0
Power down 0 X X X Z 0
Offset cal high for
normal mode 1 0 1 0 analog X
Offset cal low for
normal mode 1 0 1 1 analog X
Offset cal high for
low-power mode 1 1 1 0 analog X
Offset cal low for
low-power mode 1 1 1 1 analog X

Operational amplifiers (OPAMP) RM0438
856/2187 RM0438 Rev 8
Calibration procedure
Here are the steps to perform a full calibration of either one of the operational amplifiers:
1. Select correct OPA_RANGE in OPAMP_CSR,  then set the OPAEN bit in OPAMP_CSR
to 1 to enable the operational amplifier.
2. Set the USERTRIM bit in th e OPAMP_CSR register to 1.
3. Choose a calibration mode (refer to [Table 203](../tables/table_203.md): Operating modes and calibration). The
steps 3 to 4 will have to be repeated 4 times. For the first iteration select
– Normal mode, offset cal high (N differential pair)
The above calibration mode correspond to OPALPM=0 and CALSEL=0 in the
OPAMP_CSR register.
4. Increment TRIMOFFSETN[4:0] in OPAMP_ OTR starting from 00000b until CALOUT
changes to 1 in OPAMP_CSR.
Note: CALOUT will switch from 0 to 1 for offset cal high and from 1 to 0 for offset cal low.
Note: Between the write to the OPAMP_OTR regist er and the read of the CALOUT value, make
sure to wait for the tOFFTRIMmax delay specified in the electrical characteristics section of
the datasheet, to get the correct CALOUT value.
The commutation means that the offset is correctly compensated and that the
corresponding trim code must be saved in the OPAMP_OTR register.
Repeat steps 3 to 4 for:
– Normal_mode and offset cal low
– Low power mode and offset cal high
– Low power mode and offset cal low
If a mode is not used it is not necessary to perform the corresponding calibration.
All operational amplifier can be calibrated at the same time.
Note: During the whole calibration phase the exte rnal connection of the operational amplifier
output must not pull up or down currents higher than 500 µA.
During the calibration procedure, it is necessary to set up OPAMODE bits as 00 or 01 (PGA
disable) or 11 (internal follower).
25.4 OPAMP low-power modes
[Table 204](../tables/table_204.md). Effect of low-power modes on the OPAMP
Mode Description
Sleep No effect.
Low-power run No effect.
Low-power sleep No effect.
Stop 0 / Stop 1 No effect, OPAMP registers content is kept.
Stop 2 OPAMP registers content is kept. OPAMP must be disabled before entering
Stop 2 mode.

RM0438 Rev 8 857/2187
RM0438 Operational amplifiers (OPAMP)
861
25.5 OPAMP registers
25.5.1 OPAMP1 control/status register (OPAMP1_CSR)
Address offset: 0x00
Reset value: 0x0000 0000
Standby The OPAMP registers are powered down and must be re-initialized after
exiting Standby or Shutdown mode.Shutdown
[Table 204](../tables/table_204.md). Effect of low-power modes on the OPAMP (continued)
Mode Description
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
OPA_
RANGE Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res.
rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CAL
OUT
USER
TRIM
CAL
SEL CALON Res. VP_
SEL VM_SEL Res. Res. PGA_GAIN OPAMODE OPA
LPM OPAEN
r r wr wr w r wr wr w r wr wr w w r wr w
Bit 31 OPA_RANGE: Operational amplifier power supply range for stability
All AOP must be in power down to allow AOP-RANGE bit write. It applies to all AOP
embedded in the product.
0: Low range (VDDA < 2.4V)
1: High range (VDDA > 2.4V)
Bits 30:16 Reserved, must be kept at reset value.
Bit 15 CALOUT: Operational amplifier calibration output
During calibration mode offset is trimmed when this signal toggle.
Bit 14 USERTRIM: allows to switch from ‘factory’ AOP offset trimmed values to AOP offset ‘user’
trimmed values
This bit is active for both mode normal and low-power.
0: ‘factory’ trim code used
1: ‘user’ trim code used
Bit 13 CALSEL: Calibration selection
0: NMOS calibration (200mV applied on OPAMP inputs)
1: PMOS calibration (VDDA-200mV applied on OPAMP inputs)
Bit 12 CALON: Calibration mode enabled
0: Normal mode
1: Calibration mode (all switches opened by HW)
Bit 11 Reserved, must be  kept at reset value.
Bit 10 VP_SEL: Non inverted input selection
0: GPIO connected to VINP
1: DAC connected to VINP

Operational amplifiers (OPAMP) RM0438
858/2187 RM0438 Rev 8
25.5.2 OPAMP1 offset trimming regi ster in normal mode (OPAMP1_OTR)
Address offset: 0x04
Reset value: 0x0000 XXXX (factory trimmed values)
25.5.3 OPAMP1 offset trimming  register in low-power mode
(OPAMP1_LPOTR)
Address offset: 0x08
Bits 9:8 VM_SEL: Inverting input selection
These bits are used only when OPAMODE = 00, 01 or 10.
00: GPIO connected to VINM (valid also in PGA mode for filtering
01: Dedicated low leakage input, connected to VINM (valid also in PGA mode for filtering)
1x: Inverting input not externally connected. These configurations are valid only when
OPAMODE = 10 (PGA mode)
Bits 7:6 Reserved, must be kept at reset value.
Bits 5:4 PGA_GAIN: Operational amplifier Programmable amplifier gain value
00: internal PGA Gain 2
01: internal PGA Gain 4
10: internal PGA Gain 8
11: internal PGA Gain 16
Bits 3:2 OPAMODE: Operational amplifier PGA mode
00: internal PGA disable
01: internal PGA disable
10: internal PGA enable, gain programmed in PGA_GAIN
11: internal follower
Bit 1 OPALPM: Operational amplifier Low Power Mode
The operational amplifier must be disable to change this configuration.
0: operational amplifier in normal mode
1: operational amplifier in low-power mode
Bit 0 OPAEN: Operational amplifier Enable
0: operational amplifier disabled
1: operational amplifier enabled
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. TRIMOFFSETP[4:0] Res. Res. Res. TRIMOFFSETN[4:0]
rw rw rw rw rw rw rw rw rw rw
Bits 31:13 Reserved, must be kept at reset value.
Bits 12:8 TRIMOFFSETP[4:0]: Trim for PMOS differential pairs
Bits 7:5 Reserved, must be kept at reset value.
Bits 4:0 TRIMOFFSETN[4:0]: Trim for NMOS differential pairs

RM0438 Rev 8 859/2187
RM0438 Operational amplifiers (OPAMP)
861
Reset value: 0x0000 XXXX (factory trimmed values)
25.5.4 OPAMP2 control/status register (OPAMP2_CRS)
Address offset: 0x10
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. TRIMLPOFFSETP[4:0] Res. Res. Res. TRIMLPOFFSETN[4:0]
rw rw rw rw rw rw rw rw rw rw
Bits 31:13 Reserved, must be kept at reset value.
Bits 12:8 TRIMLPOFFSETP[4:0]: Low-power mode trim for PMOS differential pairs
Bits 7:5 Reserved, must be kept at reset value.
Bits 4:0 TRIMLPOFFSETN[4:0]: Low-power mode trim for NMOS differential pairs
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CALOU
T
USERT
RIM
CALSE
L CALON Res. VP_SE
L VM_SEL Res. Res. PGA_GAIN OPAMODE OPALP
M OPAEN
r r wr wr w r wr wr w r wr wr wr wr wr w
Bits 31:16 Reserved, must be kept at reset value.
Bit 15 CALOUT: Operational amplifier calibration output
During calibration mode offset is trimmed when this signal toggle.
Bit 14 USERTRIM: allows to switch from ‘factory’ AOP offset trimmed values to AOP offset ‘user’
trimmed values
This bit is active for both mode normal and low-power.
0: ‘factory’ trim code used
1: ‘user’ trim code used
Bit 13 CALSEL: Calibration selection
0: NMOS calibration (200mV applied on OPAMP inputs)
1: PMOS calibration (VDDA-200mV applied on OPAMP inputs)
Bit 12 CALON: Calibration mode enabled
0: Normal mode
1: Calibration mode (all switches opened by HW)
Bit 11 Reserved, must be  kept at reset value.
Bit 10 VP_SEL: Non inverted input selection
0: GPIO connected to VINP
1: DAC connected to VINP

Operational amplifiers (OPAMP) RM0438
860/2187 RM0438 Rev 8
25.5.5 OPAMP2 offset trimming regi ster in normal mode (OPAMP2_OTR)
Address offset: 0x14
Reset value: 0x0000 XXXX (factory trimmed values)
25.5.6 OPAMP2 offset trimming  register in low-power mode
(OPAMP2_LPOTR)
Address offset: 0x18
Bits 9:8 VM_SEL: Inverting input selection
These bits are used only when OPAMODE = 00, 01 or 10.
00:GPIO connected to VINM (valid also in PGA mode for filtering)
01: Dedicated low leakage input, (available only on BGA132) connected to VINM (valid also
in PGA mode for filtering)
1x: Inverting input not externally connected. These configurations are valid only when
OPAMODE = 10 (PGA mode)
Bits 7:6 Reserved, must be kept at reset value.
Bits 5:4 PGA_GAIN: Operational amplifier Programmable amplifier gain value
00: internal PGA Gain 2
01: internal PGA Gain 4
10: internal PGA Gain 8
11: internal PGA Gain 16
Bits 3:2 OPAMODE: Operational amplifier PGA mode
00: internal PGA disable
01: internal PGA disable
10: internal PGA enable, gain programmed in PGA_GAIN
11: internal follower
Bit 1 OPALPM: Operational amplifier Low Power Mode
The operational amplifier must be disable to change this configuration.
0: operational amplifier in normal mode
1: operational amplifier in low-power mode
Bit 0 OPAEN: Operational amplifier Enable
0: operational amplifier disabled
1: operational amplifier enabled
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. TRIMOFFSETP[4:0] Res. Res. Res. TRIMOFFSETN[4:0]
rw rw rw rw rw rw rw rw rw rw
Bits 31:13 Reserved, must be kept at reset value.
Bits 12:8 TRIMOFFSETP[4:0]: Trim for PMOS differential pairs
Bits 7:5 Reserved, must be kept at reset value.
Bits 4:0 TRIMOFFSETN[4:0]: Trim for NMOS differential pairs

RM0438 Rev 8 861/2187
RM0438 Operational amplifiers (OPAMP)
861
Reset value: 0x0000 XXXX (factory trimmed values)
25.5.7 OPAMP register map
Refer to Section 2.3.2: Memory map and register boundary addresses for the register
boundary addresses.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. TRIMLPOFFSETP[4:0] Res. Res. Res. TRIMLPOFFSETN[4:0]
rw rw rw rw rw rw rw rw rw rw
Bits 31:13 Reserved, must be kept at reset value.
Bits 12:8 TRIMLPOFFSETP[4:0]: Low-power mode trim for PMOS differential pairs
Bits 7:5 Reserved, must be kept at reset value.
Bits 4:0 TRIMLPOFFSETN[4:0]: Low-power mode trim for NMOS differential pairs
[Table 205](../tables/table_205.md). OPAMP register map and reset values
Offset Register
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
0x00 OPAMP1_CSR
OPA_RANGE
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CALOUT
USERTRIM
CALSEL
CALON
Res.
VP_SEL
VM_SEL
Res.
Res.
PGA_GAIN
OPAMODE
OPALPM
OPAEN
R e s e t  v a l u e 0 0000 000 000000
0x04
OPAMP1_OTR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TRIM
OFFSETP[4:0]
Res.
Res.
Res.
TRIM
OFFSETN[4:0]
Reset value (1) (1)
0x08
OPAMP1_
LPOTR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TRIMLP
OFFSETP[4:0]
Res.
Res.
Res.
TRIMLP
OFFSETN[4:0]
Reset value (1) (1)
0x10 OPAMP2_CSR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CALOUT
USERTRIM
CALSEL
CALON
Res.
VP_SEL
VM_SEL
Res.
Res.
PGA_GAIN
OPAMODE
OPALPM
OPAEN
R e s e t  v a l u e 0000 000 000000
0x14
OPAMP2_OTR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TRIM
OFFSETP[4:0]
Res.
Res.
Res.
TRIM
OFFSETN[4:0]
Reset value (1) (1)
0x18
OPAMP2_LPO
TR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
TRIMLP
OFFSETP[4:0]
Res.
Res.
Res.
TRIMLP
OFFSETN[4:0]
Reset value (1) (1)
1. Factory trimmed values.
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 176: Architectural Diagram](../figures/figure_176.md)
* [Figure 177: Architectural Diagram](../figures/figure_177.md)
* [Figure 178: Architectural Diagram](../figures/figure_178.md)
* [Figure 179: Architectural Diagram](../figures/figure_179.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 202: Configuration Matrix](../tables/table_202.md)
* [Table 203: Configuration Matrix](../tables/table_203.md)
* [Table 204: Configuration Matrix](../tables/table_204.md)
* [Table 205: Configuration Matrix](../tables/table_205.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)