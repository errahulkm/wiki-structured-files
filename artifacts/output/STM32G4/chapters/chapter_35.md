# Chapter 35: Independent watchdog (IWDG)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32G4 Reference Manual RM0440 - Chapter 35: Independent watchdog (IWDG).
* **Document Source**: RM0440 Reference Manual
* **PDF Reference Location**: Pages 1556 - 1564
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Independent Watchdog (IWDG)](../peripherals/iwdg.md)

## 2. Official Reference Manual Text Content (RM0440 Ingestion)
```text
Independent watchdog (IWDG) RM0440
1556/2140 RM0440 Rev 9
35 Independent watchdog (IWDG)
35.1 Introduction
The devices feature an embedded watchdog peripheral (IWDG) that offers a combination of
high safety level, timing accuracy, and flexibility of use. This peripheral detects and solves
malfunctions due to software failure, and triggers a system reset when the counter reaches
a given timeout value.
The independent watchdog is clocked by its own dedicated low-speed clock (LSI), and stays
active even if the main clock fails.
The IWDG is best suited for applications that require the watchdog to run as a totally
independent process outside the main application, but have lower timing accuracy
constraints. For further information on the window watchdog, refer to Section 36: System
window watchdog (WWDG).
35.2 IWDG main features
• Free-running downcounter
• Clocked from an independent RC oscillator (can operate in Standby and Stop modes)
• Conditional reset
– Reset (if watchdog is activated) when the downcounter value becomes lower than
0x000
– Reset (if watchdog is activated) if th e downcounter is reloaded outside the window
35.3 IWDG functional description
35.3.1 IWDG block diagram
[Figure 529](../figures/figure_529.md) shows the functional blocks of the independent watchdog module.
[Figure 529](../figures/figure_529.md). Independent watchdog block diagram
1. The register interface is located in the  volt age domain. The watchdog function is located in the VDD voltage
domain, still functional in Standby mode.
MS34442V2
IWDG reset
LSI
VCORE
VDD voltage domain
Prescaler register
IWDG_PR
Status register
IWDG_SR
Reload register
IWDG_RLR
Key register
IWDG_KR
12-bit reload value
12-bit downcounter
8-bit
prescaler

RM0440 Rev 9 1557/2140
RM0440 Independent watchdog (IWDG)
1564
When the independent watchdog is started by writing the value 0x0000 CCCC in the IWDG
key register (IWDG_KR), the counter starts counting down from the reset value of 0xFFF.
When it reaches the end of count value (0x000), a reset signal is generated (IWDG reset).
Whenever the key value 0x0000 AAAA is written in the IWDG key register (IWDG_KR), the
IWDG_RLR value is reloaded in the counter, and the watchdog reset is prevented.
Once running, the IWDG cannot be stopped.
35.3.2 Window option
The IWDG can also work as a window watchdog by setting the appropriate window in the
IWDG window register (IWDG_WINR).
If the reload operation is performed while the counter is greater than the value stored in the
IWDG window register (IWDG_WINR), a reset is provided.
The default value of the IWDG window register (IWDG_WINR) is 0x0000 0FFF, so if it is not
updated, the window option is disabled.
As soon as the window value is changed, a reload operation is performed to reset the
downcounter to the IWDG reload register (IWDG_RLR) value, and to ease the cycle number
calculation to generate the next reload.
Configuring the IWDG when the window option is enabled
1. Enable the IWDG by writing 0x0000 CCCC in the IWDG key register (IWDG_KR).
2. Enable register access by writing 0x0000 5555 in the IWDG key register (IWDG_KR).
3. Write the IWDG prescaler by programming IWDG prescaler register (IWDG_PR) from
0 to 7.
4. Write the IWDG reload register (IWDG_RLR).
5. Wait for the registers to be  updated (IWDG_SR = 0x0000 0000).
6. Write to the IWDG window register (IWDG_WINR). This automatically refreshes the
counter value in the IWDG reload register (IWDG_RLR).
Note: Writing the window value allows the counter value to be refreshed by the RLR when the
IWDG status register (IWDG_SR) is set to 0x0000 0000.
Configuring the IWDG when the window option is disabled
When the window option is not used, the IWDG can be configured as follows:
1. Enable the IWDG by writing 0x0000 CCCC in the IWDG key register (IWDG_KR).
2. Enable register access by writing 0x0000 5555 in the IWDG key register (IWDG_KR).
3. Write the prescaler by programming the IWDG prescaler register (IWDG_PR) from 0 to
7.
4. Write the IWDG reload register (IWDG_RLR).
5. Wait for the registers to be  updated (IWDG_SR = 0x0000 0000).
6. Refresh the counter value with IWDG_RLR (IWDG_KR = 0x0000 AAAA).

Independent watchdog (IWDG) RM0440
1558/2140 RM0440 Rev 9
35.3.3 Hardware watchdog
If this feature is enabled through the device option bits, the watchdog is automatically
enabled at power-on, and generates a reset unless the IWDG key register (IWDG_KR) is
written by the software before the counter reaches the end of count, and if the downcounter
is lower than the window value (WIN[11:0]).
35.3.4 Low-power freeze
Depending on the IWDG_STOP and IWDG_STBY options configuration, the IWDG can
continue counting or not during the Stop mode and the Standby mode, respectively. If the
IWDG is kept running during Stop or Standby modes, it can wake up the device from this
mode. Refer to User and read protection option bytes for more details.
35.3.5 Register access protection
Write access to IWDG prescaler register (IWDG_PR), IWDG reload register (IWDG_RLR),
and IWDG window register (IWDG_WINR) is protected. To modify them, first write the code
0x0000 5555 in the IWDG key register (IWDG_KR). A write access to this register with a
different value breaks the sequence, and register access is protected again. This is the case
of the reload operation (writing 0x0000 AAAA).
A status register is available to indicate that an update of the prescaler, or of the
downcounter reload value, or of the window value, is ongoing.
35.3.6 Debug mode
When the device enters Debug mode (core halted), the IWDG counter either continues to
work normally or stops, depending on the configuration of the corresponding bit in
DBGMCU freeze register.

RM0440 Rev 9 1559/2140
RM0440 Independent watchdog (IWDG)
1564
35.4 IWDG registers
Refer to Section 1.2 on page 74 for a list of abbreviations used in register descriptions.
The peripheral registers can be accessed by half-words (16-bit) or words (32-bit).
35.4.1 IWDG key register (IWDG_KR)
Address offset: 0x00
Reset value: 0x0000 0000 (reset by Standby mode)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
KEY[15:0]
wwwwwwwwwwwwwwww
Bits 31:16 Reserved, must be kept at reset value.
Bits 15:0 KEY[15:0]: Key value (write only, read 0x0000)
These bits must be written by software at regular intervals with the key value 0xAAAA,
otherwise the watchdog generates a reset when the counter reaches 0.
Writing the key value 0x5555 to enable access to the IWDG_PR, IWDG_RLR and
IWDG_WINR registers (see Section 35.3.5: Register access protection)
Writing the key value 0xCCCC starts the watchdog (except if the hardware watchdog option
is selected)

Independent watchdog (IWDG) RM0440
1560/2140 RM0440 Rev 9
35.4.2 IWDG prescaler register (IWDG_PR)
Address offset: 0x04
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. PR[2:0]
rw rw rw
Bits 31:3 Reserved, must be kept at reset value.
Bits 2:0 PR[2:0]: Prescaler divider
These bits are write access protected see Section 35.3.5: Register access protection. They
are written by software to select the prescaler divider feeding the counter clock. PVU bit of
the IWDG status register (IWDG_SR) must be reset in order to be able to change the
prescaler divider.
000: divider /4
001: divider /8
010: divider /16
011: divider /32
100: divider /64
101: divider /128
110: divider /256
111: divider /256
Note: Reading this register returns the prescaler value from the V DD voltage domain. This
value may not be up to date/valid if a write operation to this register is ongoing. For this
reason the value read from this register is valid only when the PVU bit in the IWDG
status register (IWDG_SR) is reset.

RM0440 Rev 9 1561/2140
RM0440 Independent watchdog (IWDG)
1564
35.4.3 IWDG reload register (IWDG_RLR)
Address offset: 0x08
Reset value: 0x0000 0FFF (reset by Standby mode)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. RL[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:12 Reserved, must be kept at reset value.
Bits 11:0 RL[11:0]: Watchdog counter reload value
These bits are write access protected see Register access protection. They are written by
software to define the value to be loaded in the watchdog counter each time the value
0xAAAA is written in the IWDG key register (IWDG_KR). The watchdog counter counts
down from this value. The timeout period is a function of this value and the clock prescaler.
Refer to the datasheet for the timeout information.
The RVU bit in the IWDG status register (IWDG_SR) must be reset to be able to change the
reload value.
Note: Reading this register returns the reload value from the V DD voltage domain. This value
may not be up to date/valid if a write operation to this register is ongoing on it. For this
reason the value read from this register is valid only when the RVU bit in the IWDG
status register (IWDG_SR) is reset.

Independent watchdog (IWDG) RM0440
1562/2140 RM0440 Rev 9
35.4.4 IWDG status register (IWDG_SR)
Address offset: 0x0C
Reset value: 0x0000 0000 (not reset by Standby mode)
Note: If several reload, prescaler, or window values are used by the application, it is mandatory to
wait until RVU bit is reset before changing the reload value, to wait until PVU bit is reset
before changing the prescaler value, and to wait until WVU bit is reset before changing the
window value. However, after updating the prescaler and/or the reload/window value it is not
necessary to wait until RVU or PVU or WVU is reset before continuing code execution
except in case of low-power mode entry.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. WVU RVU PVU
rrr
Bits 31:3 Reserved, must be kept at reset value.
Bit 2 WVU: Watchdog counter window value update
This bit is set by hardware to indicate that an update of the window value is ongoing. It is
reset by hardware when the reload value update operation is completed in the VDD voltage
domain (takes up to five  cycles).
Window value can be updated only when WVU bit is reset.
Bit 1 RVU: Watchdog counter reload value update
This bit is set by hardware to indicate that an update of the reload value is ongoing. It is reset
by hardware when the reload value update operation is completed in the VDD voltage domain
(takes up to five  cycles).
Reload value can be updated only when RVU bit is reset.
Bit 0 PVU: Watchdog prescaler value update
This bit is set by hardware to indicate that an update of the prescaler value is ongoing. It is
reset by hardware when the prescaler update operation is completed in the VDD voltage
domain (takes up to five  cycles).
Prescaler value can be updated only when PVU bit is reset.

RM0440 Rev 9 1563/2140
RM0440 Independent watchdog (IWDG)
1564
35.4.5 IWDG window re gister (IWDG_WINR)
Address offset: 0x10
Reset value: 0x0000 0FFF (reset by Standby mode)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. WIN[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:12 Reserved, must be kept at reset value.
Bits 11:0 WIN[11:0]: Watchdog counter window value
These bits are write access protected, see Section 35.3.5, they contain the high limit of the
window value to be compared with the downcounter.
To prevent a reset, the downcounter must be reloaded when its value is lower than the
window register value and greater than 0x0
The WVU bit in the IWDG status register (IWDG_SR) must be reset in order to be able to
change the reload value.
Note: Reading this register returns the reload value from the V DD voltage domain. This value
may not be valid if a write operation to this register is ongoing. For this reason the value
read from this register is valid only when the WVU bit in the IWDG status register
(IWDG_SR) is reset.

Independent watchdog (IWDG) RM0440
1564/2140 RM0440 Rev 9
35.4.6 IWDG register map
The following table gives the IWDG register map and reset values.
Refer to Section 2.2 on page 82 for the register boundary addresses.
[Table 335](../tables/table_335.md). IWDG register map and reset values
Offset Register
name
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
0x00
IWDG_KR
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
KEY[15:0]
R e s e t  v a l u e 0000000000000000
0x04
IWDG_PR
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
PR[2:0]
Reset value 000
0x08
IWDG_RLR
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
Res.
RL[11:0]
Reset value 111111111111
0x0C
IWDG_SR
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
WVU
RVU
PVU
Reset value 000
0x10
IWDG_WINR
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
Res.
WIN[11:0]
Reset value 111111111111
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 529: Architectural Diagram](../figures/figure_529.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 335: Configuration Matrix](../tables/table_335.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)