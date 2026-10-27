# Chapter 52: Debug support (DBG)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 52: Debug support (DBG).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 2006 - 2149
* **Taxonomy Section**: CORE
* **Parent IP Module**: [Debug Support (DBG)](../core/debug.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
Debug support (DBG) RM0438
2006/2187 RM0438 Rev 8
52 Debug support (DBG)
52.1 Introduction
A comprehensive set of debug features is provided to support software development and
system integration:
• Breakpoint debugging of the CPU core
• Code execution tracing
• Software instrumentation
• Cross-triggering
The debug features can be controlled via a JTAG/Serial-wire debug access port, using
industry standard debugging tools. A trace port allows data to be captured for logging and
analysis.
The debug features are based on Arm® Coresight™ components.
– SWJ-DP: JTAG/Serial-wire debug port
– AHB-AP: AHB access port
– ROM table
– System Control Space (SCS)
– Breakpoint Unit (BPU)
– Data Watchpoint and Trace Unit (DWT)
– Instrumentation Trace Macrocell (ITM)
– Embedded Trace Macrocell (ETM)
– Cross Trigger Interface (CTI)
– Trace Port Interface Unit (TPU)
The debug features are accessible by the debugger via the AHB-AP .
Additional information can be found in the Arm® documents referenced in Section 52.12.

RM0438 Rev 8 2007/2187
RM0438 Debug support (DBG)
2149
52.2 DBG functional description
52.2.1 DBG block diagram
[Figure 566](../figures/figure_566.md). Block diagram of debug support infrastructure
52.2.2 DBG pins and internal signals
MSv49702V1
CPU
Cortex®-M33
SWJ-DP
JTAG/Serial-wire port
JTMS/SWDIO
JTDI
JTDO
JTCK/SWCLK
nJTRST DBG_MCU
ETM
ROM
table
CTI
AHB-AP
Core
DWT
AHB
PPB
BPU TRACECK
TRACED[3:0]
Trace port
ITM TPIU
TRACESWO
[Table 446](../tables/table_446.md). JTAG/Serial-wire debug port pins
Pin name
JTAG debug port SW debug port Pin
assignmentType Description Type Description
JTMS/SWDIO I JTAG test mode select IO Serial wire data in/out PA13
JTCK/SWCLK I JTAG test clock I Serial wire clock PA14
JTDI(1) I JTAG test data input - - PA15
JTDO O JTAG test data output - - PB3
nJTRST I JTAG test reset - - PB4
1. TDI is hosted on the same IO as a USBPD-CC line. To avoid pull-up/down conflict, a user option allows to decide whether
the pad is used as TDI or as CC.
[Table 447](../tables/table_447.md). Trace port pins
Pin name Type Description Pin assignment
TRACED0
O
Trace synchronous data out 0
Refer to datasheet
TRACED1 Trace synchronous data out 1
TRACED2 Trace synchronous data out 2
TRACED3 Trace synchronous data out 3
TRACECK Trace clock

Debug support (DBG) RM0438
2008/2187 RM0438 Rev 8
52.2.3 DBG reset and clocks
The debug port (SWJ-DP) is reset by a power-on reset and when waking up from Standby
mode.
The debugger supplies the clock for the debug port via the debug interface pin
JTCK/SWCLK. This clock is used to register the serial input data in both Serial-wire and
JTAG modes, as well as to operate the state machines and internal logic of the debug port.
It must therefore continue to toggle for several cycles after the end of an access, to ensure
that the debug port returns to the idle state.
The SWJ-DP contains an asynchronous interface to the DCLK domain, which covers the
rest of the SWJ-DP and the access port.
The DCLK is a gated version of the system clock.
The DCLK domain is enabled by the debugger using the CDBGPWRUPREQ bit in the
debug port CTRL/STAT register. The clock must be enabled before the debugger can
access any of the debug features on the device. The availability of the clock is reflected in
the CDBGPWRUPACK bit in the debug port CTRL/STAT register. The DCLK is disabled at
power-up, and must be disabled when the debugger is disconnected, to avoid wasting
energy.
The debug and trace components included in the processor are clocked with the processor
clock.
52.2.4 DBG power domains
The debug components are located in the core power domain. This means that debugger
connection is not possible in shutdown or standby low-power modes. To avoid losing the
connection when the device enters standby mode, it is possible to maintain the power to the
core by setting a bit in the DBGMCU_CR register. This also keeps the processor clocks
active, and holds off the reset, so that the debug session is maintained.
52.2.5 Debug and low-power modes
The STM32L552xx and STM32L562xx devices include power saving features that allow the
core power domain to be switched off or stopped when not required. If the power is switched
off, or the core is not clocked, all debug components are inaccessible to the debugger. To
avoid this, power saving mode emulation has been implemented. If emulation is enabled for
a domain, the domain still enters power saving mode, but its clock and power are
maintained. In other words, the domain behaves as if it is in power saving mode, but the
debugger does not lose the connection.
Emulation mode is programmed in the microcontroller debug (DBGMCU) unit. For more
information refer to Section 52.11: Microcontroller debug unit (DBGMCU).
[Table 448](../tables/table_448.md). Single Wire Trace port pins
Pin name Type Description Pin assignment
TRACESWO O Single-wire trace asynchronous data out PB3 (1)
1. TRACESWO is multiplexed with JTDO. This means that sing le-wire trace is only available when using the Serial-wire
debug interface, and not when using JTAG.

RM0438 Rev 8 2009/2187
RM0438 Debug support (DBG)
2149
52.2.6 Security
The trace and debug components allow a high degree of access to the processor and
system during product development. In order to protect user code and ensure that the
debug features can not be used to alter or compromise the normal operation of the finished
product, these features can be disabled, or limited in scope. For example, secure software
debug and trace can be disabled without preventing the debug of non-secure code.
There are four authentication signals used by the system to determine which debug features
are enabled or disabled. These signals are:
• dbgen: global enable for all debug features
0: all debug features are disabled.
1: debug features in non-secure state are enabled. Debug features in secure state are
dependent on the state of the spiden signal.
• spiden: enables debug in secure state when dbgen = 1
0: debug features are disabled in secure state.
1: debug features are enabled in secure state.
• niden: enables trace and performance monitoring (non-invasive debug)
0: trace generation is disabled.
1: trace generation in non-secure state is enabled. Trace generation in secure state is
dependent on the state of the spniden signal.
• spniden: enables trace and performance monitoring in secure state when niden = 1.
0: trace generation is disabled in secure state.
1: trace generation is enabled in secure state.
For detailed information on the behavior of each component according to the state of the
authentication signals, refer to the relevant component chapter, or to the relevant Arm®
technical documentation.
The state of the signals are set according to the read data protection (RDP) level (see
Section 6.7.2: Readout protection (RDP)), as shown in [Table 449](../tables/table_449.md):
[Table 449](../tables/table_449.md). Authentication signal states
RDP level Authentication signal
state Description
0
DBGEN = 1
SPIDEN = 1
NIDEN = 1
SPNIDEN = 1
Debug and trace is enabled whatever the state of
the processor. Debugger access to secure memory
is permitted.
0.5
DBGEN = 1
SPIDEN = 0
NIDEN = 1
SPNIDEN = 0
Debug and trace is enabled when the processor is
in non-secure state. Debugger access to secure
memory is disabled.

Debug support (DBG) RM0438
2010/2187 RM0438 Rev 8
Note: Security features are only relevant when option bit TZEN = 1. If security features are
disabled, the authentication signals are still set according to the RDP level, but since the
processor and all memory are non-secure, SPNIDEN and SPIDEN are redundant.
The state of the authentication signals can be read from the DAUTHSTATUS register in the
system control space (SCS) of the Cortex-M33.
Note that debugger access to secure memory (when permitted) must be performed using
secure transactions on the debug AHB, that is, with the PROT[6] bit set in the AP_CSWR
register.
Debugger access is disabled while the processor is booting from system flash (RSS),
whatever the RDP level, if security features are enabled (TZEN = 1).
52.2.7 Serial-wire and JTAG debug port (SWJ-DP)
The SWJ-DP is a Coresight™ component that implements an external access port for
connecting debugging equipment.
Two types of interface can be configured:
• a 5-pin standard JTAG interface (JTAG-DP)
• a 2-pin (clock + data) Serial-wire debug port (SW-DP)
The two modes are mutually exclusive, since they share the same IO pins.
By default the JTAG-DP is selected after a system or a power-on reset. The five IO pins are
configured by hardware in debug alternative function mode. The SWJ-DP incorporates
pull-up resistors on JTDI, JTMS/SWDIO, and nJTRST, as well as a pull-down resistor on
JTCK/SWCLK.
A debugger can select the SW-DP by transmitting the following serial data sequence on
JTMS/SWDIO:
... (50 or more ones) ..., 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, ... (50 or more ones) ...
JTCK/SWCLK must be cycled for each data bit.
In SW-DP mode, the unused JTAG pins JTDI, JTDO and nJTRST can be used for other
functions. Note that all SWJ port IOs can be reconfigured to other functions by software, but
debugging is no longer possible.
1
DBGEN = 1
SPIDEN = 0
NIDEN = 1
SPNIDEN = 0
Debug and trace is enabled when the processor is
in non-secure state. Debugger access to secure
memory is disabled, as well as to the following
areas: flash memory, SRAM2, Backup registers,
ICACHE, on-the-fly decryption region (OCTOSPI).
2
DBGEN = 0
SPIDEN = 0
NIDEN = 0
SPNIDEN = 0
Debug and trace is disabled.
[Table 449](../tables/table_449.md). Authentication signal states (continued)
RDP level Authentication signal
state Description

RM0438 Rev 8 2011/2187
RM0438 Debug support (DBG)
2149
52.2.8 JTAG debug port
The JTAG-DP implements a TAP state machine (TAPSM), shown in [Figure 567](../figures/figure_567.md), based on
IEEE Std 1149.1-1990. The state machine controls two scan chains, one associated with an
instruction register (IR), and the other one with a number of data registers (DR).
[Figure 567](../figures/figure_567.md). JTAG TAP state machine
MS44486V1
Test-Logic-
Reset
Run-Test/
Idle
Select-
DR-Scan
Shift-DR
Capture-
DR
Exit1-DR
Pause-
DR
Exit2-DR
Update-
DR
Select-
IR-Scan
Shift-IR
Capture-
IR
Exit1-IR
Pause-IR
Exit2-IR
Update-
IR
JTMS=0
JTMS=1
JTMS=1
JTMS=0
JTMS=1
JTMS=0
JTMS=1
JTMS=1
JTMS=0
JTMS=0
JTMS=0
JTMS=1 JTMS=0 JTMS=0 JTMS=1
JTMS=0
JTMS=1
JTMS=1
JTMS=0
JTMS=0
JTMS=1
JTMS=1 JTMS=0
JTMS=0
JTMS=1
JTMS=1 JTMS=0
JTMS=0
JTMS=1
JTMS=1 JTMS=0
JTMS=1

Debug support (DBG) RM0438
2012/2187 RM0438 Rev 8
The operation of the JTAG-DP is as follows:
1. When the TAPSM goes throu gh the Capture-IR state, 0b0001 is transferred onto the
instruction register (IR) scan chain. The IR scan chain is connected between JTDI and
JTDO.
2. While the TAPSM is in the Shif t-IR state, the IR scan chain shifts one bit for each rising
edge of JTCK. This means that on the first tick:
– The LSB of the IR scan chain is output on JTDO.
– Bit[n] of the IR scan chain is transferred to bit[n-1].
– The value on JTDI  is transferred to the MSB of the IR scan chain.
3. When the TAPSM goes through the Update -IR state, the value scanned into the IR
scan chain is transferred into the instruction register.
4. When the TAPSM goes thro ugh the Capture-DR state, a value is transferred from one
of the data registers onto one of the DR scan chains, connected between JTDI and
JTDO.
5. The value held in the instruction register determines which data register, and
associated DR scan chain, is selected.
6. This data is then shifted wh ile the TAPSM is in the Shift-DR state, in the same manner
as the IR shift in the Shift-IR state.
7. When the TAPSM goes through the Update -DR state, the value scanned into the DR
scan chain is transferred into the selected data register.
8. When the TAPSM is in the Run-Test/Idle state, no special actions occurs. The IDCODE
instruction is loaded in IR.
When active, the nJTRST signal resets the state machine asynchronously to the
test-logic-reset state.
The data registers corresponding to the 4-bit IR instructions are listed in [Table 450](../tables/table_450.md).
[Table 450](../tables/table_450.md). JTAG-DP data registers
IR
instruction
DR
register
Scan chain
length Description
0000 to 0111 (BYPASS) 1 Not implemented: BYPASS selected
1000 ABORT 35
ABORT register
– bits 31:1 = reserved
– bit 0 = APABORT: write 1 to generate an AP abort.
1001 (BYPASS) 1 Reserved: BYPASS selected
1010 DPACC 35
Debug port access register
Initiates the debug port and gives access to a debug port register.
– When transferring data IN:
bits 34:3 = DATA[31:0] = 32-bit data to transfer for a write request
bits 2:1 = A[3:2] = 2-bit address of a debug port register
bit 0 = RnW = read request (1) or write request (0)
– When transferring data OUT:
bits 34:3 = DATA[31:0] = 32-bit data read following a read request
bits 2:0 = ACK[2:0] = 3-bit Acknowledge:
– 010 = OK/FAULT
– 001 = WAIT
– others = reserved

RM0438 Rev 8 2013/2187
RM0438 Debug support (DBG)
2149
The DR registers are described in more detail in the Arm® Debug Interface Architecture
Specification [1].
52.2.9 Serial-wire debug port
The Serial-wire debug protocol uses two pins:
• SWCLK: clock from host to target
• SWDIO: bi-directional serial data
Serial data is transferred LSB first, synchronously with the clock.
A transfer comprises three phases:
1. packet request (8 bits) transmitted by the host (see [Table 451](../tables/table_451.md))
2. acknowledge response (3 bits) transmitted by the target (see [Table 452](../tables/table_452.md))
3. data transfer (33 bits) transm itted by the host (in case of a write) or target (in case of a
read) (see [Table 453](../tables/table_453.md))
The data transfer only occurs if the acknowledge response is OK.
Between each phase, if the direction of the data is reversed, a single clock cycle
turn-around time is inserted.
1011 APACC 35
Access port access register
Initiates an access port and gives access to an access port register.
– When transferring data IN:
bits 34:3 = DATA[31:0] = 32-bit data to shift in for a write request
bits 2:1 = A[3:2] = 2-bit sub-address of an access port register
bit 0 = RnW= Read request (1) or write request (0)
– When transferring data OUT:
bits 34:3 = DATA[31:0] = 32-bit data read following a read request
bits 2:0 = ACK[2:0] = 3-bit Acknowledge:
– 010 = OK/FAULT
– 001 = WAIT
– others= reserved
1100 (BYPASS) 1 Reserved: BYPASS selected
1101 (BYPASS) 1 Reserved: BYPASS selected
1110 IDCODE 32 Identification code
0x0BA0 4477: Cortex®-M33 JTAG debug port ID code
1111 BYPASS 1 Bypass
A single JTCK cycle delay is inserted between JTDI and JTDO.
[Table 450](../tables/table_450.md). JTAG-DP data registers (continued)
IR
instruction
DR
register
Scan chain
length Description

Debug support (DBG) RM0438
2014/2187 RM0438 Rev 8
In the case of a FAULT or WAIT ACK response from the target, the data transfer phase is
canceled, unless overrun detection is enabled: in this case the data is ignored by the target
(in the case of a write), or not driven (in the case of a read).
A line reset must be generated by the host when it is first connected, or following a protocol
error. The line reset consists in 50 or more SWCLK cycles with SWDIO high, followed by
two SWCLK cycles with SWDIO low.
For more details on the Serial-wire debug protocol, refer to the Arm® Debug Interface
Architecture Specification [1].
Note: The SWJ-DP implements SWD protocol version 2.
52.2.10 Debug port registers
Both the SW-DP and the JTAG-DP access the debug port (DP) registers listed in [Table 454](../tables/table_454.md).
The debugger can access the DP registers as follows:
1. Program the A(3:2) field in the DPACC register, if using JTAG, with the register address
within the bank. Program the RnW bit to select a read or write. In the case of a write,
program the data field with the write data. If using SWD, the A(3:2) and RnW fields are
[Table 451](../tables/table_451.md). Packet request
Bit field Name Description
0 Start Must be 1.
1 APnDP – 0: DP register access - see Section 52.2.10: Debug port registers
– 1: AP register access - see Section 52.3: Access ports
2R n W – 0: write request
– 1: read request
4:3 A(3:2) Address field of the DP or AP register (refer to [Table 454](../tables/table_454.md) or [Table 455](../tables/table_455.md))
5 Parity Single bit parity of preceding bits
6S t o p 0
7 Park Not driven by host, must  be read as 1 by target.
[Table 452](../tables/table_452.md). ACK response
Bit field Name Description
2:0 ACK
– 000: FAULT
– 010: WAIT
– 100: OK
[Table 453](../tables/table_453.md). Data transfer
Bit field Name Description
31:0 WDATA or RDATA Write or read data
32 Parity Single bit parity of 32 data bits

RM0438 Rev 8 2015/2187
RM0438 Debug support (DBG)
2149
part of the packet request word sent to the SW-DP with the APnDP bit reset (see
[Table 451](../tables/table_451.md)). The write data are sent in the data phase.
2. To access one of the banked DP registers at address 0x4, the register number must
first be written to the DP_SELECTR register at address 0x8. Any subsequent read or
write to address 0x4 access the register corresponding to the contents of the
DP_SELECTR register.
DP debug port identification register (DP_DPIDR)
Address offset: 0x0
Reset value: 0x0BE0 2477 (SW-DP), 0x0BE0 1477 (JTAG-DP)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REVISION[3:0] PARTNO[7:0] Res. Res. Res. MIN
r r r rr rrrrrrr r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
VERSION[3:0] DESIGNER[10:0] Res.
r r r rr rrrrrrrrrr
Bits 31:28 REVISION[3:0]: revision code
0x0 (JTAG-DP): r0p0
0x0 (SW-DP): r0p0
Bits 27:20 PARTNO[7:0]: part number for the debug port
0xBE
Bits 19:17 Reserved, must  be kept at reset value.
Bit 16 MIN: minimal debug port (MINDP) implementation
0x1: MINDP implemented (transaction counter and pushed operations are not supported)
Bits 15:12 VERSION[3:0]: debug port architecture version
0x1 (JTAG-DP): DPv1
0x2 (SW-DP): DPv2
Bits 11:1 DESIGNER[10:0]: JEDEC designer identity code
0x23B: Arm® JEDEC code
Bit 0 Reserved, must be kept at reset value.

Debug support (DBG) RM0438
2016/2187 RM0438 Rev 8
DP abort register (DP_ABORTR)
Address offset: 0x0
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
ORUNERRCLR
WDERRCLR
STKERRCLR
Res.
DAPABORT
www w
Bits 31:5 Reserved, must be kept at reset value.
Bit 4 ORUNERRCLR: overrun error clear
0: no effect
1: STICKYORUN bit cleared in DP_CTRL/STATR register
Bit 3 WDERRCLR: write data error clear
0: no effect
1: WDATAERR bit cleared in DP_CTRL/STATR register
Bit 2 STKERRCLR: sticky error clear
0: no effect
1: STICKYERR bit cleared in DP_CTRL/STATR register
Bit 1 Reserved, must be kept at reset value.
Bit 0 DAPABORT: current AP transaction aborted if excessive number of WAIT responses returned
This bit indicates that the transaction is stalled.
0: no effect
1: transaction aborted

RM0438 Rev 8 2017/2187
RM0438 Debug support (DBG)
2149
DP control and status register (DP_CTRL/STATR)
Address offset: 0x4
Reset value: 0x0000 0000
This register is accessible when DP_SELECTR.DPBANKSEL[3:0] = 0x0.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res.
CDBGPWRUPACK
CDBGPWRUPREQ
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
rr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res.
WDATAERR
READOK
STICKYERR
Res. Res. Res.
STICKYORUN
ORUNDETECT
rrr rr
Bits 31:30 Reserved, must  be kept at reset value.
Bit 29 CDBGPWRUPACK: debug power-up acknowledge
See description in Section 52.2.5: Debug and low-power modes.
0: DCLK gated
1: DCLK enabled
Bit 28 CDBGPWRUPREQ: debug power-up request
Controls the DCLK enable request signal.
0: requests DCLK gating
1: requests DCLK enable
Bits 27:8 Reserved, must be kept at reset value.
Bit 7 WDATAERR: write data error (read-only) in SW-DP
Indicates that there is a parity or framing error on the data phase of a write
or
a write accepted by the DP is then discarded without being submitted to the AP.
This bit is reset by writing 1 to the ABORT.WDERRCLR bit.
0: no error
1: an error occurred
Note: this bit is reserved in JTAG-DP.
Bit 6 READOK: AP read response (read-only) in SW-DP.
Indicates the response to the last AP read access.
0: read not OK
1: read OK
Note: this bit is reserved in JTAG-DP.

Debug support (DBG) RM0438
2018/2187 RM0438 Rev 8
DP data link control register (DP_DLCR)
Address offset: 0x4
Reset value: 0x0000 0000
This register is accessible when DP_SELECTR.DPBANKSEL[3:0] = 0x1.
Bit 5 STICKYERR: transaction error (read-only in SW-DP, read/write in JTAG-DP)
Indicates that an error occurred in an AP transaction.
This bit is reset by writing 1 to the DP_ABORTR.STKERRCLR bit (in SW-DP and JTAG-DP)
0: no error
1: an error occurred
Bits 4:2 Reserved, must be kept at reset value.
Bit 1 STICKYORUN: overrun (read-only in SW-DP, read/write in JTAG-DP).
Indicates that an overrun occurred (new transaction received before previous transaction
completed). This bit is only set if the ORUNDETECT bit is set.
This bit is reset by writing 1 to the DP_ABORTR.ORUNERRCLR bit (in SW-DP and
JTAG-DP)
0: no overrun
1: an overrun occurred
Bit 0 ORUNDETECT: overrun detection mode enable.
0: disabled
1: enabled. In the event of an overrun, the STICKYORUN bit is set and subsequent
transactions are blocked until the STICKYORUN bit is cleared.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res.
TURNROUND[1:0]
WIREMODE[1:0]
Res. Res. Res. Res. Res. Res.
rrrr
Bits 31:10 Reserved, must  be kept at reset value.
Bits 9:8 TURNROUND[1:0]: tristate period for SWDIO
0x0: 1 data bit period
Bits 7:6 WIREMODE[1:0]: SW-DP mode
0x0: synchronous mode
Bits 5:0 Reserved, must be kept at reset value.

RM0438 Rev 8 2019/2187
RM0438 Debug support (DBG)
2149
DP target identification register (DP_TARGETIDR)
Address offset: 0x4
Reset value: 0x0000 0001
This register is accessible when DP_SELECTR.DPBANKSEL[3:0] = 0x2.
DP data link protocol identification register (DP_DLPIDR)
Address offset: 0x4
Reset value: 0x0000 0001
This register is accessible when DP_SELECTR.DPBANKSEL[3:0] = 0x3.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
TREVISION[3:0] TPARTNO[15:4]
r r r rr rrrrrrrrrrr
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
TPARTNO[3:0] TDESIGNER[10:0] Res.
r r r rr rrrrrrrrrr
Bits 31:28 TREVISION[3:0]: target revision
0x1: revision 1
Bits 27:12 TPARTNO[15:0]: target part number
0x0472: STM32L552xx and STM32L562xx
Bits 11:1 TDESIGNER[10:0]: target designer JEDEC code
0x020: STMicroelectronics
Bit 0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
TINSTANCE[3:0] Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
rr r r
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. PROTSVN[3:0]
rrrr
Bits 31:28 TINSTANCE[3:0]: target instance number
Defines the instance number for the device in a multi-drop system.
0x0: instance number 0
Bits 27:4 Reserved, must be kept at reset value.
Bits 3:0 PROTSVN[3:0]: Serial-wire debug protocol version
0x1: version 2

Debug support (DBG) RM0438
2020/2187 RM0438 Rev 8
DP event status (DP_EVENTSTATR)
Address offset: 0x4
Reset value: 0x0000 0001
This register is accessible when DP_SELECTR.DPBANKSEL[3:0] = 0x4.
DP event status register (DP_RESENDR)
Address offset: 0x8
Reset value: 0x0000 0000
DP access port select register (DP_SELECTR)
Address offset: 0x8
Reset value: 0xXXXX XXXX
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. EA
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 EA: event status flag
0: Cortex®-M33 processor halted
1: Cortex®-M33 processor not halted
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
RESEND[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
RESEND[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 RESEND[31:0]: value returned by the last AP read or DP_RDBUFF read
This register is used in the event of a corrupted read transfer.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
APSEL[7:0] Res. Res. Res. Res. Res. Res. Res. Res.
ww w w w w w w
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. APBANKSEL[3:0] DPBANKSEL[3:0]
wwwwwwww

RM0438 Rev 8 2021/2187
RM0438 Debug support (DBG)
2149
DP read buffer register (DP_RDBUFFR)
Address offset: 0xC
Reset value: 0x0000 0000
Bits 31:24 APSEL[7:0]: access port select
Selects the access port for the next transaction.
0x0: AP0 - Cortex®-M33 debug access port (AHB-AP)
others: reserved
Bits 23:8 Reserved, must be kept at reset value.
Bits 7:4 APBANKSEL[3:0]: AP register bank select.
Selects the 4-word register bank on the active AP for the next transaction.
Bits 3:0 DPBANKSEL[3:0]: DP register bank select
Selects the register at address 0x4 of the debug port.
0x0: DP_CTRL/STAT register
0x1: DP_DLCR register
0x2: DP_TARGETID register
0x3: DP_DLPIDR register
0x4: DP_EVENTSTAT register
others: reserved
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
RDBUFF[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
RDBUFF[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 RDBUFF[31:0]: value returned by the last AP read access
The value returned by an AP read access can either be obtained using a second read access
to the same address, that initiates a new transaction on the corresponding bus, or else it can
be read from this register, in which case no new AP transaction occurs.

Debug support (DBG) RM0438
2022/2187 RM0438 Rev 8
52.2.11 Debug port regist er map and reset values
These registers are not on the CPU memory bus, they are only accessed through SW-DP
and JTAG-DP debug interface.
The debug port address is 2-bit wide, defined in the JTAG-DP register DPACC or SW-DP
packet request A[3:2] field.
[Table 454](../tables/table_454.md). Debug port register map and reset values
Offset Register name
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
0x0
DP_DPIDR
REVISION[3:0]
PARTNO[7:0]
Res.
Res.
Res.
MIN
VERSION[3:0]
DESIGNER[10:0]
Res.
R e s e t  v a l u e 000010111110 00010010001110111
0x0
DP_ABORTR
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
ORUNERRCLR
WDERRCLR
STKERRCLR
STKCMPCLR
DAPABORT
Reset value 00000
0x4(1)
DP_CTRL/STATR
Res.
Res.
CDBGPWRUPACK
CDBGPWRUPREQ
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
WDATAERR
READOK
STICKYERR
Res.
Res.
Res.
STICKYORUN
ORUNDETECT
Reset value 0 0 000 00
0x4(2)
DP_DLCR
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
TURNROUND[1:0]
WIREMODE[1:0]
Res.
Res.
Res.
Res.
Res.
Res.
Reset value 0000
0x4(3)
DP_TARGETIDR
TREVISION[3:0]
TPARTNO[15:0] TDESIGNER[10:0]
Res.
R e s e t  v a l u e 0001000001000111001000000100000
0x4(4)
DP_DLPIDR
TINSTANCE[3:0]
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
PROTSVN[3:0]
R e s e t  v a l u e 0000 0001
0x4(5)
DP_EVENTSTATR
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
Res.
Res.
EA
Reset value 1
0x8
DP_RESENDR RESEND[0:31]
R e s e t  v a l u e 00000000000000000000000000000000

RM0438 Rev 8 2023/2187
RM0438 Debug support (DBG)
2149
52.3 Access ports
There is one access port (AP) attached to the DP . It enables access to the debug and trace
features integrated in the Cortex®-M33 processor core via its internal AHB bus.
52.3.1 Access port registers
The access port is of type MEM-AP, that is to say the debug and trace component registers
are mapped in the address space of the AHB. The AP is seen by the debugger as a set of
32-bit registers organized in banks of four registers each. Some of these registers are used
to configure or monitor the AP itself, while others are used to perform a transfer on the bus.
The AP registers are listed in [Table 455](../tables/table_455.md).
The address of the AP registers is composed of the following fields:
• bits [7:4]: content of the DP_SELECTR.APBANKSEL[3:0] field in the DP (see DP
access port select register (DP_SELECTR))
• bits [3:2]: content of the A(3:2) field of the APACC data register in the JTAG-DP (see
[Table 450](../tables/table_450.md)), or of the SW-DP packet request (see [Table 451](../tables/table_451.md)), depending on the debug
interface used
• bits [1:0]: always set to 0
The content of the DP_SELECTR.APSEL[3:0] field in the DP defines which MEM-AP is
being accessed.
The debugger can access the AP registers as follows:
1. Program the DP_SELECTR.APSEL[3:0] field in the DP to choose the AP , and the
APBANKSEL[3:0] field to select the register bank to be accessed (see DP access port
select register (DP_SELECTR)).
2. Program the A(3:2) field in the APACC data  register, if using JTAG, with the register
address within the bank. Program the RnW bit to select a read or write. In the case of a
write, program the DATA field with the write data. If using SWD, the A(3:2) and RnW
0x8
DP_SELECTR APSEL[7:0]
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
APBANKSEL[3:0]
DPBANKSEL[3:0]
R e s e t  v a l u e xxxxxxxx xxxxxxxx
0xC
DP_RDBUFFR RDBUFF[0:31]
R e s e t  v a l u e 00000000000000000000000000000000
1. DP_SELECTR.DPBANKSEL[3:0] = 0x0.
2. DP_SELECTR.DPBANKSEL[3:0] = 0x1.
3. DP_SELECTR.DPBANKSEL[3:0] = 0x2.
4. DP_SELECTR.DPBANKSEL[3:0] = 0x3.
5. DP_SELECTR.DPBANKSEL[3:0] = 0x4.
[Table 454](../tables/table_454.md). Debug port register map and reset values (continued)
Offset Register name
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

Debug support (DBG) RM0438
2024/2187 RM0438 Rev 8
fields are part of the packet request word sent to the SW-DP with the APnDP bit set
(see [Table 451](../tables/table_451.md)). The write data is sent in the data phase.
The debugger can access the memory mapped debug component registers through the AP
registers (using the above AP register access procedure) as follows:
1. Program the transaction target  address in the TAR register.
2. Program the AP_CSWR register, if necessary, with the transfer parameters (AddrInc for
example).
3. Write to or read from the AP_DRWR register  to initiate a bus transaction at the address
held in the AP_TAR register. Alternatively, a read or write to banked data register
AP_BDnR triggers an access to address TAR[31:4] + n, allowing up to four consecutive
addresses to be accessed without changing the address in the AP_TAR register.
For more detailed information on the MEM-AP refer to the Arm® Debug Interface
Architecture Specification [1].
AP control/status word register (AP_CSWR)
Address offset: 0x0
Reset value: 0x0100 00X0
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res.
PROT[6]
Res. Res. PROT[3:0] Res. Res. Res. Res. Res. Res. Res. Res.
rw rw rw rw r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Re s. Res. Res. Res. Res.
DBGSTATUS
ADDRINC[1:0] Res. SIZE[2:0]
r r wr w r wr wr w
Bit 31 Reserved, must be kept at reset value.
Bit 30 PROT[6]: secure transfer request
This field sets the protection attribute HPROT[6] of the bus transfer.
0: secure transfer
1: non-secure transfer
Bits 29:28 Reserved, must  be kept at reset value.
Bits 27:24 PROT[3:0]: bus transfer protection
This field sets the protection attributes HPROT[3:0] of the bus transfer.
0bXXX1: data access (bit 24 is read only)
0bXX0X: non-privilege mode
0bXX1X: privilege mode
0bX0XX: non-bufferable
0bX1XX: bufferable
0b0XXX: non-shareable, no look-up, non-modifiable
0b1XXX: shareable, look-up, modifiable
Bits 23:7 Reserved, must be kept at reset value.

RM0438 Rev 8 2025/2187
RM0438 Debug support (DBG)
2149
AP transfer address register (AP_TAR)
Address offset: 0x04
Reset value: 0xXXXX XXXX
AP data read/write register (AP_DRWR)
Address offset: 0x0C
Reset value: 0xXXXX XXXX
Bit 6 DBGSTATUS: device enable (DEVICEEN) status
0: AHB transfers blocked
1: AHB transfers enabled
Bits 5:4 ADDRINC[1:0]: auto-increment mode
Defines whether TAR address is automatically incremented after a transaction.
0x0: no auto-increment
0x1: address incremented by the size in bytes of the transaction (SIZE field)
other: reserved
Bit 3 Reserved, must be kept at reset value.
Bits 2:0 SIZE[2:0]: size of next memory access transaction
0x0: byte (8-bit)
0x1: halfword (16-bit)
0x2: word (32-bit)
others: reserved
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
TA[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
TA[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 TA[31:0]: address of current transfer
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
TD[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
TD[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 TD[31:0]: data of current transfer

Debug support (DBG) RM0438
2026/2187 RM0438 Rev 8
AP banked data n register (AP_BDnR)
Address offset: 0x10 + 4 * n, (n = 0 to 3)
Reset value: 0x0000 0000
AP configuration register (AP_CFGR)
Address offset: 0xF4
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
TBD[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
TBD[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 TBD[31:0]: banked data of current transfer to address TAR
TA + AP_BDnR address [3:2] + 0b00.
The auto address incrementing is not performed on AP_BD0-3R. Banked transfers are only
supported for word transfers.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. LD LA BE
rrr
Bits 31:3 Reserved, must be kept at reset value.
Bit 2 LD: large data
0: data not larger than 32-bits supported
Bit 1 LA: long address
0: Physical addresses not larger than 32-bits supported
Bit 0 BE: big endian
0: only little-endian supported

RM0438 Rev 8 2027/2187
RM0438 Debug support (DBG)
2149
AP base address register (AP_BASER)
Address offset: 0xF8
Reset value: 0xE00F E003
AP identification register (AP_IDR)
Address offset: 0xFC
Reset value: 0x1477 0015
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
BASEADDR[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
BASEADDR[15:12] Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
FORMAT
ENTRYPRESENT
rrrr rr
Bits 31:12 BASEADDR[31:12]: base address (bits 31 to 12) of the first ROM table
The 12 LSBs are zero since the ROM table must be aligned on a 4-Kbyte boundary.
0xE00FE
Bits 11:2 Reserved, must be kept at reset value.
Bit 1 FORMAT: base-address register format
1: Arm® debug interface v5
Bit 0 ENTRYPRESENT: debug components presence
Indicates that debug components are present on the access port bus.
1: debug components present
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REVISION[3:0] JEDECBANK[3:0] JEDECCODE[6:0]
CLASS[3]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CLASS[2:0] Res. Res. Res. Res. Res. VARIANT[3:0] TYPE[3:0]
rrr rrrrrrrr
Bits 31:28 REVISION[3:0]: revision number
0x1: r0p1
Bits 27:24 JEDECBANK[3:0]: JEDEC bank.
0x4: Arm®
Bits 23:17 JEDECCODE[6:0]: JEDEC code.
0x3B: Arm®

Debug support (DBG) RM0438
2028/2187 RM0438 Rev 8
52.3.2 Access port regist er map and reset values
These registers are not on the CPU memory bus, they are only accessed through SW-DP
and JTAG-DP debug interfaces.
The access port address is 8-bit wide, defined by DP_SELECTR.APBANKSEL[3:0] field
and by JTAG-DP register DPACC or SW-DP packet request A[3:2] field.
Bits 16:13 CLASS[3:0]:
0x8: MEM-AP
Bits 12:8 Reserved, must be kept at reset value.
Bits 7:4 VARIANT[3:0]:
0x1: Cortex®-M33
Bits 3:0 TYPE[3:0]:
0x5: AHB5
[Table 455](../tables/table_455.md). Access port register map and reset values
Offset Register name
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
AP_CSWR
Res.
PROT[6]
Res.
Res.
PROT[3:0]
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
DBGSTATUS
ADDRINC[1:0]
Res.
SIZE[2:0]
Reset value 0 0 0 0 1 X X X 0 0 0
0x04
AP_TAR TA[31:0]
R e s e t  v a l u e XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
0x08 Reserved Reserved
0x0C
AP_DRWR TD[31:0]
R e s e t  v a l u e XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
0x10
AP_BD0R TBD[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x14
AP_BD1R TBD[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x18
AP_BD2R TBD[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x1C
AP_BD3R TBD[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x20 to
0xF0 Reserved Reserved
0xF4
AP_CFGR
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
LD
LA
BE
Reset value 000
0xF8
AP_BASER BASEADDR[31:12]
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
FORMAT
ENTRYPRESENT
R e s e t  v a l u e 11100000000011111110 11

RM0438 Rev 8 2029/2187
RM0438 Debug support (DBG)
2149
Refer to Section 2.3 for the register boundary addresses.
52.4 ROM tables
The ROM table is a CoreSight™ component that  contains the base addresses of all the
Coresight debug components accessible via the AHB-AP. These tables allow a debugger to
discover the topology of the CoreSight system automatically.
There are two ROM tables in the CPU sub-system. The MCU ROM table is pointed to by the
base register in the AHB-AP. It contains the base address pointer for the processor ROM
table and for the TPIU registers.
The MCU ROM table (see [Table 456](../tables/table_456.md)) occupies a 4-Kbyte, 32-bit wide chunk of address
space, from 0xE00F E000 to 0xE00F EFFC.
The processor ROM table contains the base-address pointer for the system control space
(SCS) registers, that allow the debugger to identify the CPU core, as well as for the BPU,
DWT, ITM, ETM and CTI.
The processor ROM table (see [Table 457](../tables/table_457.md)) occupies a 4-Kbyte, 32-bit wide chunk of address
space, from 0xE00F F000 to 0xE00F FFFC.
0xFC
AP_IDR
REVISION[3:0]
JEDECBANK[3:0]
JEDECCODE[6:0] CLASS[3:0]
Res.
Res.
Res.
Res.
Res.
VARIANT[3:0] TYPE[3:0]
R e s e t  v a l u e 0001010001110111000 00010101
[Table 455](../tables/table_455.md). Access port register map and reset values (continued)
Offset Register name
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
[Table 456](../tables/table_456.md). MCU ROM table
Address
in ROM table
Component
name
Component
base address
Component
address offset
Size
(Kbytes) Entry
0xE00F E000 Processor ROM table 0xE00F F000 0x0000 1000 4 0x0000 1003
0xE00F E004 TPIU 0xE004 0000 0xFFF4 2000 4 0xFFF4 2003
0xE00F E008 Reserved - - - 0x1FF0 2002
0xE00F E00C Reserved - - - 0x1FF0 2002
0xE00F F010 Top of table - - - 0x0000 0000
0xE00F F014 to
0xE00F FFC8 Reserved - - - 0x0000 0000
0xE00F FFCC to
0xE00F FFFC ROM table registers - - - See [Table 458](../tables/table_458.md)

Debug support (DBG) RM0438
2030/2187 RM0438 Rev 8
[Table 457](../tables/table_457.md). Processor ROM table
Address
in ROM table
Component
name
Component
base address
Component
address offset
Size
(Kbytes) Entry
0xE00F F000 SCS 0xE000 E000 0xFFF0 F000 4 0xFFF0 F003
0xE00F F004 DWT 0xE000 1000 0xFFF0 2000 4 0xFFF0 2003
0xE00F F008 BPU 0xE000 2000 0xFFF0 3000 4 0xFFF0 3003
0xE00F F00C ITM 0xE000 0000 0xFFF0 1000 4 0xFFF0 1003
0xE00F F010 Reserved - - - 0xFFF4 1002
0xE00F F014 ETM 0xE004 1000 0xFFF4 2000 4 0xFFF4 2003
0xE00F F018 CTI 0xE004 2000 0xFFF4 3000 4 0xFFF4 3003
0xE00F F01C Reserved - - - 0xFFF4 4002
0xE00F F020 Top of table - - - 0x0000 0000
0xE00F F024 to
0xE00F FFC8 Reserved - - - 0x0000 0000
0xE00F FFCC to
0xE00F FFFC ROM table registers - - - See [Table 459](../tables/table_459.md)

RM0438 Rev 8 2031/2187
RM0438 Debug support (DBG)
2149
The topology for the CoreSight components in the Cortex® -M33 is shown in [Figure 568](../figures/figure_568.md).
[Figure 568](../figures/figure_568.md). CoreSight topology
MSv49703V1
Processor ROM table
@0xE00FF000
System control space (SCS)
@0xE000E000AHB-APBase
register
(0xF8)
Register file base0x000
PIDR40xFD0
CIDR30xFFC
Register file base
Breakpoint unit  (BPU)
@0xE0002000
0x000
PIDR40xFD0
CIDR30xFFC
Register file base
Trace port (TPIU)
@0xE0040000
0x000
PIDR40xFD0
CIDR30xFFC
Register file base
Cross trigger (CTI)
@0xE0043000
0x000
PIDR40xFD0
CIDR30xFFC
Register file base
Data watchpoint/trace
(DWT)
@0xE0001000
0x000
PIDR40xFD0
CIDR30xFFC
Register file base
Instrumentation trace
(ITM)
@0xE0000000
0x000
PIDR40xFD0
CIDR30xFFC
Register file base0x000
PIDR40xFD0
CIDR30xFFC
Embedded trace (ETM)
@0xE0041000
Offset: 0xFFF0F0000x000
Top of table
Offset: 0xFFF020000x004
Offset: 0xFFF030000x008
Offset: 0xFFF010000x00C
PIDR40xFD0
CIDR30xFFC
Offset: 0xFFF44000
0x010 Reserved
0x018
Offset: 0xFFF420000x014
0x01C
MCU ROM table
@0xE00FE000
0x000
Top of table
PIDR4
0xFD0
CIDR3
0xFFC
0x004
Offset: 0x00001000
Offset: 0xFFF42000
0xE00FE000

Debug support (DBG) RM0438
2032/2187 RM0438 Rev 8
52.4.1 MCU ROM table registers
MCU ROM memory type register (MCUROM_MEMTYPER)
Address offset: 0xFCC
Reset value: 0x0000 0001
MCU ROM CoreSight peripheral identity register 4 (MCUROM_PIDR4)
Address offset: 0xFD0
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res.
SYSMEM
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 SYSMEM: system memory
0x1: system memory present on this bus
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. 4KCOUNT[3:0] JEP106CON[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 4KCOUNT[3:0]: register file size
0x0: The register file occupies a single 4-Kbyte region.
Bits 3:0 JEP106CON[3:0]: JEP106 continuation code
0x0: STMicroelectronics JEDEC continuation code

RM0438 Rev 8 2033/2187
RM0438 Debug support (DBG)
2149
MCU ROM CoreSight peripheral identity register 0 (MCUROM_PIDR0)
Address offset: 0xFE0
Reset value: 0x0000 0072
MCU ROM CoreSight peripheral identity register 1(MCUROM_PIDR1)
Address offset: 0xFE4
Reset value: 0x0000 0004
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PARTNUM[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PARTNUM[7:0]: part number bits [7:0]
0x72: STM32L552xx and STM32L562xx
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. JEP106ID[3:0] PARTNUM[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 JEP106ID[3:0]: JEP106 identity code bits [3:0]
0x0: STMicroelectronics JEDEC code
Bits 3:0 PARTNUM[11:8]: part number bits [11:8]
0x4: STM32L552xx and STM32L562xx

Debug support (DBG) RM0438
2034/2187 RM0438 Rev 8
MCU ROM CoreSight peripheral identity register 2 (MCUROM_PIDR2)
Address offset: 0xFE8
Reset value: 0x0000 000A
MCU ROM CoreSight peripheral identity register 3 (MCUROM_PIDR3)
Address offset: 0xFEC
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. REVISION[3:0] JEDEC JEP106ID[6:4]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVISION[3:0]: component revision number
0x0: rev r0p0
Bit 3 JEDEC: JEDEC assigned value
1: designer identification specified by JEDEC
Bits 2:0 JEP106ID[6:4]: JEP106 identity code bits [6:4]
0x2: STMicroelectronics JEDEC code
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. REVAND[3:0] CMOD[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVAND[3:0]: metal fix version
0x0: No metal fix
Bits 3:0 CMOD[3:0]: customer modified
0x0: No customer modifications

RM0438 Rev 8 2035/2187
RM0438 Debug support (DBG)
2149
MCU ROM CoreSight component identity register 0 (MCUROM_CIDR0)
Address offset: 0xFF0
Reset value: 0x0000 000D
MCU ROM CoreSight peripheral identity register 1 (MCUROM_CIDR1)
Address offset: 0xFF4
Reset value: 0x0000 0010
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[7:0]: component identification bits [7:0]
0x0D: Common identification value
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. CLASS[3:0] PREAMBLE[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 CLASS[3:0]: Component identification bits [15:12] - component class
0x1: ROM table component
Bits 3:0 PREAMBLE[11:8]: Component identification bits [11:8]
0x0: Common identification value

Debug support (DBG) RM0438
2036/2187 RM0438 Rev 8
MCU ROM CoreSight component identity register 2 (MCUROM_CIDR2)
Address offset: 0xFF8
Reset value: 0x0000 0005
MCU ROM CoreSight component identity register 3 (MCUROM_CIDR3)
Address offset: 0xFFC
Reset value: 0x0000 00B1
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[19:12]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[19:12]: component identification bits [23:16]
0x05: common identification value
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[27:20]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[27:20]: Component identification bits [31:24]
0xB1: Common identification value

RM0438 Rev 8 2037/2187
RM0438 Debug support (DBG)
2149
52.4.2 MCU ROM table regist er map and reset values
Refer to Section 2.3 for register boundary addresses.
[Table 458](../tables/table_458.md). MCU ROM table register map and reset values
Offset Register name
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
0xFCC
MCUROM_
MEMTYPER
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
Res.
Res.
SYSMEM
Reset value 1
0xFD0
MCUROM_PIDR4
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
4KCOUNT[3:0]
JEP106CON[3:0]
Reset value 00000000
0xFD4 to
FDC Reserved Reserved
0xFE0
MCUROM_PIDR0
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
PARTNUM[7:0]
Reset value 01110010
0xFE4
MCUROM_PIDR1
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
JEP106ID[3:0]
PARTNUM[11:8]
Reset value 00000100
0xFE8
MCUROM_PIDR2
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
REVISION[3:0]
JEDEC
JEP106ID[6:4]
Reset value 00001010
0xFEC
MCUROM_PIDR3
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
REVAND[3:0] CMOD[3:0]
Reset value 00000000
0xFF0
MCUROM_CIDR0
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
PREAMBLE[7:0]
Reset value 00001101
0xFF4
MCUROM_CIDR1
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
CLASS[3:0]
PREAMBLE[11:8]
Reset value 00010000
0xFF8
MCUROM_CIDR2
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
PREAMBLE[19:12]
Reset value 00000101
0xFFC
MCUROM_CIDR3
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
PREAMBLE[27:20]
Reset value 10110001

Debug support (DBG) RM0438
2038/2187 RM0438 Rev 8
52.4.3 Processor RO M table registers
CPU ROM memory type register (CPUROM_MEMTYPER)
Address offset: 0xFCC
Reset value: 0x0000 0001
CPU ROM CoreSight peripheral identity register 4 (CPUROM_PIDR4)
Address offset: 0xFD0
Reset value: 0x0000 0004
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res.
SYSMEM
r
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 SYSMEM: system memory
1: system memory present on this bus
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. 4KCOUNT[3:0] JEP106CON[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 4KCOUNT[3:0]: register file size
0x0: The register file occupies a single 4-Kbyte region.
Bits 3:0 JEP106CON[3:0]: JEP106 continuation code
0x4: Arm® JEDEC continuation code

RM0438 Rev 8 2039/2187
RM0438 Debug support (DBG)
2149
CPU ROM CoreSight peripheral identity register 0 (CPUROM_PIDR0)
Address offset: 0xFE0
Reset value: 0x0000 00C9
CPU ROM CoreSight peripheral identity register 1 (CPUROM_PIDR1)
Address offset: 0xFE4
Reset value: 0x0000 00B4
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PARTNUM[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PARTNUM[7:0]: Part number bits [7:0]
0xC9: Cortex®-M33
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. JEP106ID[3:0] PARTNUM[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 JEP106ID[3:0]: JEP106 identity code bits [3:0]
0xB: Arm® JEDEC code
Bits 3:0 PARTNUM[11:8]: part number bits [11:8]
0x4: Cortex®-M33

Debug support (DBG) RM0438
2040/2187 RM0438 Rev 8
CPU ROM CoreSight peripheral identity register 2 (CPUROM_PIDR2)
Address offset: 0xFE8
Reset value: 0x0000 000B
CPU ROM CoreSight peripheral identity register 3 (CPUROM_PIDR3)
Address offset: 0xFEC
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. REVISION[3:0] JEDEC JEP106ID[6:4]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVISION[3:0]: component revision number
0x0: rev r0p0
Bit 3 JEDEC: JEDEC assigned value
1: Designer ID specified by JEDEC
Bits 2:0 JEP106ID[6:4]: JEP106 identity code bits [6:4]
0x3: Arm® JEDEC code
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. REVAND[3:0] CMOD[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVAND[3:0]: metal fix version
0x0: No metal fix
Bits 3:0 CMOD[3:0]: customer modified
0x0: no customer modifications

RM0438 Rev 8 2041/2187
RM0438 Debug support (DBG)
2149
CPU ROM CoreSight component identity register 0 (CPUROM_CIDR0)
Address offset: 0xFF0
Reset value: 0x0000 000D
CPU ROM CoreSight peripheral identity register 1 (CPUROM_CIDR1)
Address offset: 0xFF4
Reset value: 0x0000 0010
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[7:0]: Component identification bits [7:0]
0x0D: Common identification value
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. CLASS[3:0] PREAMBLE[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 CLASS[3:0]: Component identification bits [15:12] - component class
0x1: ROM table component
Bits 3:0 PREAMBLE[11:8]: Component identification bits [11:8]
0x0: Common identification value

Debug support (DBG) RM0438
2042/2187 RM0438 Rev 8
CPU ROM CoreSight component identity register 2 (CPUROM_CIDR2)
Address offset: 0xFF8
Reset value: 0x0000 0005
CPU ROM CoreSight component identity register 3 (CPUROM_CIDR3)
Address offset: 0xFFC
Reset value: 0x0000 00B1
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[19:12]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[19:12]: component identification bits [23:16]
0x05: common identification value
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[27:20]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[27:20]: component identification bits [31:24]
0xB1: common identification value

RM0438 Rev 8 2043/2187
RM0438 Debug support (DBG)
2149
52.4.4 Processor ROM table re gister map and reset values
Refer to Section 2.3 for register boundary addresses.
[Table 459](../tables/table_459.md). CPU ROM table register map and reset values
Offset Register name
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
0xFCC
CPUROM_
MEMTYPER
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
Res.
Res.
SYSMEM
Reset value 1
0xFD4 to
FDC Reserved Reserved
0xFD0
CPUROM_PIDR4
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
4KCOUNT[3:0]
JEP106CON[3:0]
Reset value 00000100
0xFE0
CPUROM_PIDR0
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
PARTNUM[7:0]
Reset value 11001001
0xFE4
CPUROM_PIDR1
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
JEP106ID[3:0]
PARTNUM[11:8]
Reset value 10110100
0xFE8
CPUROM_PIDR2
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
REVISION[3:0]
JEDEC
JEP106ID[6:4]
Reset value 00001011
0xFEC
CPUROM_PIDR3
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
REVAND[3:0] CMOD[3:0]
Reset value 00000000
0xFF0
CPUROM_CIDR0
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
PREAMBLE[7:0]
Reset value 00001101
0xFF4
CPUROM_CIDR1
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
CLASS[3:0]
PREAMBLE[11:8]
Reset value 00010000
0xFF8
CPUROM_CIDR2
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
PREAMBLE[19:12]
Reset value 00000101
0xFFC
CPUROM_CIDR3
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
PREAMBLE[27:20]
Reset value 10110001

Debug support (DBG) RM0438
2044/2187 RM0438 Rev 8
52.5 Data watchpoint and trace unit (DWT)
The DWT provides four comparators that can be used as one of the following:
• watchpoint
• ETM trigger
• PC sampling trigger
• data address sampling trigger
• data comparator (comparator 1 only)
• clock cycle counter comparator (comparator 0 only)
It also contains counters for:
• clock cycles
• folded instructions
• load Store Unit (LSU) operations
• sleep cycles
• number of cycles per instruction
• interrupt overhead
A DWT comparator compares the value held in its DWT_COMPR register with one of the
following:
• a data address
• an instruction address
• a data value
• the cycle count value, for comparator 0 only
For address matching, the comparator can use a mask, so it matches a range of addresses.
On a successful match, the comparator generates one of the following:
• one or more DWT data trace packets, containing one or more of:
– the address of the instruction that caused a data access
– an address offset, bits[15:0] of the data access address
– the matched data value
• a watchpoint debug event, on either the PC value or the accessed data address
• a CMPMATCH[N] event, that signals the match outside the DWT unit
A watchpoint debug event either generates a DebugMonitor exception, or causes the
processor to halt execution and enter Debug state.
For more details on how to use the DWT, refer to the Arm®v8-M Architecture Reference
Manual [4].

RM0438 Rev 8 2045/2187
RM0438 Debug support (DBG)
2149
52.5.1 DWT registers
The DWT registers are located at address range 0xE000 1000 to 0xE000 1FFC.
DWT control register (DWT_CTRLR)
Address offset: 0x000
Reset value: 0x4000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
NUMCOMP[3:0]
NOTRCPKT
NOEXTTRIG
NOCYCCNT
NOPRFCNT
CYCDISS
CYCEVTENA
FOLDEVTENA
LSUEVTENA
SLEEPEVTENA
EXCEVTENA
CPIEVTENA
EXCTRCENA
rrrrrrrr r w r w r w r w r w r w r w r w
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res.
PCSAMPLENA
SYNCTAP[1:0]
CYCTAP
POSTINIT[3:0] POSTRESET[3:0]
CYCCNTENA
rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:28 NUMCOMP[3:0]: number of comparators implemented (read only)
0x4: four comparators
Bit 27 NOTRCPKT: trace sampling and exception tracing support (read only)
0: supported
Bit 26 NOEXTTRIG: external match signal, CMPMATCH support (read only)
0: supported
Bit 25 NOCYCCNT: cycle counter support (read only)
0: supported
Bit 24 NOPRFCNT: profiling counter support (read only)
0: supported
Bit 23 CYCDISS: cycle counter disabled secure.
Controls whether the cycle counter is disabled in secure mode.
0: no effect
1: disable incrementing of the cycle counter when the processor is in secure state
Bit 22 CYCEVTENA: enable for POSTCNT underflow event counter packet generation
0: disabled
1: enabled
Bit 21 FOLDEVTENA: enable for folded instruction counter overflow event generation
0: disabled
1: enabled
Bit 20 LSUEVTENA: enable for LSU counter overflow event generation
0: disabled
1: enabled

Debug support (DBG) RM0438
2046/2187 RM0438 Rev 8
DWT cycle count register (DWT_CYCCNTR)
Address offset: 0x004
Reset value: 0x0000 0000
Bit 19 SLEEPEVTENA: enable for sleep counter overflow event generation
0: disabled
1: enabled
Bit 18 EXCEVTENA: enable for exception overhead counter overflow event generation
0: disabled
1: enabled
Bit 17 CPIEVTENA: enable for CPI counter overflow event generation
0: disabled
1: enabled
Bit 16 EXCTRCENA: enable for exception trace generation
0: disabled
1: enabled
Bits 15:13 Reserved, must  be kept at reset value.
Bit 12 PCSAMPLENA: enable for POSTCNT counter to be used as a timer for periodic PC sample
packet generation
0: disabled
1: enabled
Bits 11:10 SYNCTAP[1:0]: position of the synchronization packet counter tap on the CYCCNT counter
This field determines the synchronization packet rate.
00: disabled, no synchronization packets
01: Tap at CYCCNT[24]
10: Tap at CYCCNT[26]
11: Tap at CYCCNT[28]
Bit 9 CYCTAP: Selects the position of the POSTCNT tap on the CYCCNT counter.
0: Tap at CYCCNT[6]
1: Tap at CYCCNT[10]
Bits 8:5 POSTINIT[3:0]: initial value of the POSTCNT counter
Writes to this field are ignored if POSTCNT counter is enabled. CYCEVTENA or
PCSAMPLENA bits must be reset prior to writing POSTINIT.
Bits 4:1 POSTRESET[3:0]: reload value of the POSTCNT counter
Bit 0 CYCCNTENA: enable CYCCNT counter
0: disabled
1: enabled
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
CYCCNT[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CYCCNT[15:0]
rrrrrrrrrrrrrrrr

RM0438 Rev 8 2047/2187
RM0438 Debug support (DBG)
2149
DWT CPI count register (DWT_CPICNTR)
Address offset: 0x008
Reset value: 0xXXXX XXXX
DWT exception count register (DWT_EXCCNTR)
Address offset: 0x00C
Reset value: 0xXXXX XXXX
Bits 31:0 CYCCNT[31:0]: processor clock-cycle counter
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. CPICNT[7:0]
rw rw rw rw rw rw rw rw
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 CPICNT[7:0]: CPI counter
Counts additional cycles required to execute multi-cycle instructions, except those recorded
by DWT_LSUCNTR, and counts any instruction fetch stalls.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. EXCCNT[7:0]
rw rw rw rw rw rw rw rw
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 EXCCNT[7:0]: exception overhead cycle counter
Counts the number of cycles spent in exception processing.

Debug support (DBG) RM0438
2048/2187 RM0438 Rev 8
DWT sleep count register (DWT_SLPCNTR)
Address offset: 0x010
Reset value: 0xXXXX XXXX
DWT LSU count register (DWT_LSUCNTR)
Address offset: 0x014
Reset value: 0xXXXX XXXX
DWT fold count register (DWT_FOLDCNTR)
Address offset: 0x018
Reset value: 0xXXXX XXXX
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. SLEEPCNT[7:0]
rw rw rw rw rw rw rw rw
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 SLEEPCNT[7:0]: sleep cycle counter
Counts the number of cycles spent in sleep mode (WFI, WFE, sleep-on-exit).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. LSUCNT[7:0]
rw rw rw rw rw rw rw rw
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 LSUCNT[7:0]: load store counter
Counts additional cycles required to execute load and store instructions.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. FOLDCNT[7:0]
rw rw rw rw rw rw rw rw

RM0438 Rev 8 2049/2187
RM0438 Debug support (DBG)
2149
DWT program counter sample register (DWT_PCSR)
Address offset: 0x01C
Reset value: 0xXXXX XXXX
DWT comparator x register (DWT_COMPxR)
Address offset: 0x020 + 0x010 * x, (x = 0 to 3)
Reset value: 0xXXXX XXXX
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 FOLDCNT[7:0]: folded instruction counter
Increments on each instruction that takes 0 cycles.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
EIASAMPLE[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
EIASAMPLE[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 EIASAMPLE[31:0]: executed instruction address sample value.
Samples the current value of the program counter.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
COMP[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
COMP[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 COMP[31:0]: reference value for comparison

Debug support (DBG) RM0438
2050/2187 RM0438 Rev 8
DWT function register 0 (DWT_FUNCTR0)
Address offset: 0x028
Reset value: 0x5800 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ID[4:0] Res. Res.
MATCHED
Res. Res. Res. Res. Res. Res. Res. Res.
rrrrr r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. DATAVSIZE[1:0] Res. Res. Res. Res. ACTION[1:0] MATCH[3:0]
rw rw rw rw rw rw rw rw
Bits 31:27 ID[4:0]: capability identification
Identifies the capability for match for comparator 0.
0b01011: Cycle Counter, Instruction Address, Data Address and Data Address With Value
Bits 26:25 Reserved, must  be kept at reset value.
Bit 24 MATCHED: comparator match
Indicates if a comparator match has occurred since the register was last read.
0: no match
1: a match occurred
Bits 23:12 Reserved, must  be kept at reset value.
Bits 11:10 DATAVSIZE[1:0]: data value size
Defines the size of the object being watched for by Data Value and Data Address
comparators.
0x0: 1 byte
0x1: 2 bytes
0x2: 4 bytes
0x3: reserved
Bits 9:6 Reserved, must be kept at reset value.
Bits 5:4 ACTION[1:0]: action on match
0x0: trigger only
0x1: generate debug event
0x2: For a Cycle Counter, Instruction Address, Data Address, Data Value or Linked Data
Value comparator, generate a Data Trace Match packet. For a Data Address With Value
comparator, generate a Data Trace Data Value packet.
0x3: For a Data Address Limit comparator, generate a Data Trace Data Address packet. For
a Cycle Counter, Instruction Address Limit, or Data Address comparator, generate a Data
Trace PC Value packet. For a Data Address With Value comparator, generate both a Data
Trace PC Value packet and a Data Trace Data Value packet.
Bits 3:0 MATCH[3:0]: match type
Controls the type of match generated by comparator 0.
For possible values of this field, refer to [4].

RM0438 Rev 8 2051/2187
RM0438 Debug support (DBG)
2149
DWT function register 1 (DWT_FUNCTR1)
Address offset: 0x038
Reset value: 0xD000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ID[4:0] Res. Res.
MATCHED
Res. Res. Res. Res. Res. Res. Res. Res.
rrrrr r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. DATAVSIZE[1:0] Res. Res. Res. Res. ACTION[1:0] MATCH[3:0]
rw rw rw rw rw rw rw rw
Bits 31:27 ID[4:0]: capability identification
Identifies the capability for match for comparator 1.
0b11010: Instruction Address, Instruction Address Limit, Data Address, Data Address Limit,
and Data Address With Value
Bits 26:25 Reserved, must  be kept at reset value.
Bit 24 MATCHED: Comparator match
Indicates if a comparator match has occurred since the register was last read.
0: no match
1: a match occurred
Bits 23:12 Reserved, must  be kept at reset value.
Bits 11:10 DATAVSIZE[1:0]: data value size
Defines the size of the object being watched for by Data Value and Data Address
comparators.
0x0: 1 byte
0x1: 2 bytes
0x2: 4 bytes
0x3: reserved
Bits 9:6 Reserved, must be kept at reset value.
Bits 5:4 ACTION[1:0]: action on match
0x0: trigger only
0x1: generate debug event
0x2: For a Cycle Counter, Instruction Address, Data Address, Data Value or Linked Data
Value comparator, generate a Data Trace Match packet. For a Data Address With Value
comparator, generate a Data Trace Data Value packet.
0x3: For a Data Address Limit comparator, generate a Data Trace Data Address packet. For
a Cycle Counter, Instruction Address Limit, or Data Address comparator, generate a Data
Trace PC Value packet. For a Data Address With Value comparator, generate both a Data
Trace PC Value packet and a Data Trace Data Value packet.
Bits 3:0 MATCH[3:0]: match type
Controls the type of match generated by comparator 1.
For possible values of this field, refer to [4].

Debug support (DBG) RM0438
2052/2187 RM0438 Rev 8
DWT function register 2 (DWT_FUNCTR2)
Address offset: 0x048
Reset value: 0x5000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ID[4:0] Res. Res.
MATCHED
Res. Res. Res. Res. Res. Res. Res. Res.
rrrrr r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. DATAVSIZE[1:0] Res. Res. Res. Res. ACTION[1:0] MATCH[3:0]
rw rw rw rw rw rw rw rw
Bits 31:27 ID[4:0]: capability identification
Identifies the capability for MATCH for comparator 2
0b01010: Instruction Address, Data Address, and Data Address With Value
Bits 26:25 Reserved, must  be kept at reset value.
Bit 24 MATCHED: comparator match
Indicates if a comparator match has occurred since the register was last read.
0: no match
1: a match occurred
Bits 23:12 Reserved, must  be kept at reset value.
Bits 11:10 DATAVSIZE[1:0]: Data value size:
Defines the size of the object being watched for by Data Value and Data Address
comparators.
0x0: 1 byte
0x1: 2 bytes
0x2: 4 bytes
0x3: reserved
Bits 9:6 Reserved, must be kept at reset value.
Bits 5:4 ACTION[1:0]: action on match
0x0: trigger only
0x1: Generate debug event
0x2: For a Cycle Counter, Instruction Address, Data Address, Data Value or Linked Data
Value comparator, generate a Data Trace Match packet. For a Data Address With Value
comparator, generate a Data Trace Data Value packet.
0x3: For a Data Address Limit comparator, generate a Data Trace Data Address packet. For
a Cycle Counter, Instruction Address Limit, or Data Address comparator, generate a Data
Trace PC Value packet. For a Data Address With Value comparator, generate both a Data
Trace PC Value packet and a Data Trace Data Value packet.
Bits 3:0 MATCH[3:0]: match type
Controls the type of match generated by comparator 2.
For possible values of this field, refer to [4]

RM0438 Rev 8 2053/2187
RM0438 Debug support (DBG)
2149
DWT function register 3 (DWT_FUNCTR3)
Address offset: 0x058
Reset value: 0xF000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ID[4:0] Res. Res.
MATCHED
Res. Res. Res. Res. Res. Res. Res. Res.
rrrrr r
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. DATAVSIZE[1:0] Res. Res. Res. Res. ACTION[1:0] MATCH[3:0]
rw rw rw rw rw rw rw rw
Bits 31:27 ID[4:0]: capability identification
Identifies the capability for MATCH for comparator 2.
0b11110: Instruction Address, Instruction Address Limit, Data Address, Data Address Limit,
Data value, Linked Data Value, and Data Address With Value
Bits 26:25 Reserved, must  be kept at reset value.
Bit 24 MATCHED: comparator match
Indicates if a comparator match has occurred since the register was last read.
0: no match
1: a match occurred
Bits 23:12 Reserved, must  be kept at reset value.
Bits 11:10 DATAVSIZE[1:0]: data value size
Defines the size of the object being watched for by Data Value and Data Address
comparators.
0x0: 1 byte
0x1: 2 bytes
0x2: 4 bytes
0x3: reserved
Bits 9:6 Reserved, must be kept at reset value.
Bits 5:4 ACTION[1:0]: action on match
0x0: trigger only
0x1: Generate debug event
0x2: For a Cycle Counter, Instruction Address, Data Address, Data Value or Linked Data
Value comparator, generate a Data Trace Match packet. For a Data Address With Value
comparator, generate a Data Trace Data Value packet.
0x3: For a Data Address Limit comparator, generate a Data Trace Data Address packet. For
a Cycle Counter, Instruction Address Limit, or Data Address comparator, generate a Data
Trace PC Value packet. For a Data Address With Value comparator, generate both a Data
Trace PC Value packet and a Data Trace Data Value packet.
Bits 3:0 MATCH[3:0]: match type
Controls the type of match generated by comparator 2.
For possible values of this field, refer to [4]

Debug support (DBG) RM0438
2054/2187 RM0438 Rev 8
DWT device type architecture register (DWT_DEVARCHR)
Address offset: 0xFC8
Reset value: 0x4770 1A02
DWT device type register (DWT_DEVTYPER)
Address offset: 0xFCC
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ARCHITECT[10:0]
PRESEN
T REVISION[3:0]
rrrrrrr r r r rrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ARCHVER[3:0] ARCHPART[11:0]
rrrrrrr r r r rrrrrr
Bits 31:21 ARCHITECT[10:0]: architect JEP106 code
0x23B: JEP106 continuation code 0x4, JEP106 ID code 0x3B. Arm limited.
Bit 20 PRESENT: DWT_DEVARCH register present
0x1: present
Bits 19:16 REVISION[3:0]: architecture revision
0x0: DWT architecture v2.0
Bits 15:12 ARCHVER[3:0]: architecture version
0x1: DWT architecture v2.0
Bits 11:0 ARCHPART[11:0]: architecture part
0xA02: DWT architecture
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. SUB[3:0] MAJOR[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 SUB[3:0]: sub-type
0x0: other
Bits 3:0 MAJOR[3:0]: major type
0x0: miscellaneous

RM0438 Rev 8 2055/2187
RM0438 Debug support (DBG)
2149
DWT CoreSight peripheral identity register 4 (DWT_PIDR4)
Address offset: 0xFD0
Reset value: 0x0000 0004
DWT CoreSight peripheral identity register 0 (DWT_PIDR0)
Address offset: 0xFE0
Reset value: 0x0000 0021
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. 4KCOUNT[3:0] JEP106CON[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 4KCOUNT[3:0]: register file size
0x0: The register file occupies a single 4-Kbyte region.
Bits 3:0 JEP106CON[3:0]: JEP106 continuation code
0x4: Arm® JEDEC code
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PARTNUM[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PARTNUM[7:0]: part number bits [7:0]
0x21: Cortex®-M33 DWT part number

Debug support (DBG) RM0438
2056/2187 RM0438 Rev 8
DWT CoreSight peripheral identity register 1 (DWT_PIDR1)
Address offset: 0xFE4
Reset value: 0x0000 00BD
DWT CoreSight peripheral identity register 2 (DWT_PIDR2)
Address offset: 0xFE8
Reset value: 0x0000 000B
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. JEP106ID[3:0] PARTNUM[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 JEP106ID[3:0]: JEP106 identity code bits [3:0]
0xB: Arm® JEDEC code
Bits 3:0 PARTNUM[11:8]: part number bits [11:8]
0xD: Cortex®-M33 DWT part number
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. REVISION[3:0] JEDEC JEP106ID[6:4]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVISION[3:0]: component revision number
0x0: r0p0
Bit 3 JEDEC: JEDEC assigned value
0x1: designer identification specified by JEDEC
Bits 2:0 JEP106ID[6:4]: JEP106 identity code bits [6:4]
0x3: Arm® JEDEC code

RM0438 Rev 8 2057/2187
RM0438 Debug support (DBG)
2149
DWT CoreSight peripheral identity register 3 (DWT_PIDR3)
Address offset: 0xFEC
Reset value: 0x0000 0000
DWT CoreSight component identity register 0 (DWT_CIDR0)
Address offset: 0xFF0
Reset value: 0x0000 000D
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. REVAND[3:0] CMOD[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVAND[3:0]: metal fix version
0x0: no metal fix
Bits 3:0 CMOD[3:0]: customer modified
0x0: No customer modifications
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[7:0]: component identification bits [7:0]
0x0D: Common identification value

Debug support (DBG) RM0438
2058/2187 RM0438 Rev 8
DWT CoreSight peripheral identity register 1 (DWT_CIDR1)
Address offset: 0xFF4
Reset value: 0x0000 0090
DWT CoreSight component identity register 2 (DWT_CIDR2)
Address offset: 0xFF8
Reset value: 0x0000 0005
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. CLASS[3:0] PREAMBLE[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 CLASS[3:0]: component identification bits [15:12] - component class
0x9: debug component
Bits 3:0 PREAMBLE[11:8]: component identification bits [11:8]
0x0: common identification value
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[19:12]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[19:12]: component identification bits [23:16]
0x05: common identification value

RM0438 Rev 8 2059/2187
RM0438 Debug support (DBG)
2149
DWT CoreSight component identity register 3 (DWT_CIDR3)
Address offset: 0xFFC
Reset value: 0x0000 00B1
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[27:20]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[27:20]: component identification bits [31:24]
0xB1: common identification value

Debug support (DBG) RM0438
2060/2187 RM0438 Rev 8
52.5.2 DWT register map and reset values
The DWT registers are located at address range 0xE000 1000 to 0xE000 1FFC.
[Table 460](../tables/table_460.md). DWT register map and reset values
Offset Register name
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
0x000
DWT_CTRLR
NUMCOMP[3:0]
NOTRCPKT
NOEXTTRIG
NOCYCCNT
NOPRFCNT
CYCDISS
CYCEVTENA
FOLDEVTENA
LSUEVTENA
SLEEPEVTENA
EXCEVTENA
CPIEVTENA
EXCTRCENA
Res.
Res.
Res.
PCSAMPLENA
SYNCTAP[1:0]
CYCTAP
POSTINIT[3:0]
POSTPRESET[3:0]
CYCCNTENA
R e s e t  v a l u e 0100000000000000 0000000000000
0x004
DWT_CYCCNTR CYCCNT[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x008
DWT_CPICNTR
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
CPICNT[7:0]
Reset value XXXXXXXX
0x00C
DWT_EXCCNTR
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
EXCCNT[7:0]
Reset value XXXXXXXX
0x010
DWT_SLPCNTR
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
SLEEPCNT[7:0]
Reset value XXXXXXXX
0x014
DWT_LSUCNTR
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
LSUCNT[7:0]
Reset value XXXXXXXX
0x018
DWT_FOLDCNTR
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
FOLDCNT[7:0]
Reset value XXXXXXXX
0x01C
DWT_PCSR EIASAMPLE[31:0]
Reset value
0x020
DWT_COMP0R COMP[31:0]
R e s e t  v a l u e XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
0x024 Reserved Reserved
0x028
DWT_FUNCTR0 ID[4:0]
Res.
Res.
MATCHED
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
DATAVSIZE[1:0]
Res.
Res.
Res.
Res.
ACTION[1:0]
MATCH[3:0]
R e s e t  v a l u e 01011 0 00 000000
0x030
DWT_COMP1R COMP[31:0]
R e s e t  v a l u e XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
0x034 Reserved Reserved
0x038
DWT_FUNCTR1 ID[4:0]
Res.
Res.
MATCHED
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
DATAVSIZE[1:0]
Res.
Res.
Res.
Res.
ACTION[1:0]
MATCH[3:0]
R e s e t  v a l u e 11010 0 00 000000
0x040
DWT_COMP2R COMP[31:0]
R e s e t  v a l u e XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
0x044 Reserved Reserved

RM0438 Rev 8 2061/2187
RM0438 Debug support (DBG)
2149
0x048
DWT_FUNCTR2 ID[4:0]
Res.
Res.
MATCHED
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
DATAVSIZE[1:0]
Res.
Res.
Res.
Res.
ACTION[1:0]
MATCH[3:0]
R e s e t  v a l u e 01010 0 00 000000
0x050
DWT_COMP3R COMP[31:0]
R e s e t  v a l u e XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
0x054 Reserved Reserved
0x058
DWT_FUNCTR3 ID[4:0]
Res.
Res.
MATCHED
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
DATAVSIZE[1:0]
Res.
Res.
Res.
Res.
ACTION[1:0]
MATCH[3:0]
R e s e t  v a l u e 11110 0 00 000000
0x05C to
0xFC4 Reserved Reserved
0xFC8
DWT_DEVARCHR ARCHITECT[10:0]
PRESENT
REVISION[3:0]
ARCHVER[3:0]
ARCHPART[11:0]
R e s e t  v a l u e 01000111011100000001101000000010
0x0FCC
DWT_DEVTYPER
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
SUB[3:0] MAJOR[3:0]
Reset value 00000000
0xFD0
DWT_PIDR4
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
4KCOUNT[3:0]
JEP106CON[3:0]
Reset value 00000100
0xFD4 to
0xFDC Reserved Reserved
0xFE0
DWT_PIDR0
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
PARTNUM[7:0]
Reset value 00100001
0xFE4
DWT_PIDR1
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
JEP106ID[3:0]
PARTNUM[11:8]
Reset value 10111101
0xFE8
DWT_PIDR2
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
REVISION[3:0]
JEDEC
JEP106ID[6:4]
Reset value 00001011
0xFEC
DWT_PIDR3
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
REVAND[3:0] CMOD[3:0]
Reset value 00000000
[Table 460](../tables/table_460.md). DWT register map and reset values (continued)
Offset Register name
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

Debug support (DBG) RM0438
2062/2187 RM0438 Rev 8
Refer to Section 2.3 for register boundary addresses.
52.6 Instrumentation trace macrocell (ITM)
The ITM generates trace information in packets. Three sources can generate packets. If
multiple sources generate packets at the same time, the ITM arbitrates the order in which
packets are output. The three sources in decreasing order of priority are the following:
• Software trace
The software can write directly to any of 32 x 32-bit ITM stimulus registers to generate
packets. The permission level for each port can be programmed. When software writes
to an enabled stimulus port, the ITM combines the identity of the port, the size of the
write access and the data written, into a packet that it writes to a FIFO. The ITM outputs
packets from the FIFO onto the trace bus. Reading a stimulus port register returns the
status of the stimulus register (empty or pending) in bit 0.
• Hardware trace
The DWT generates trace packets in response to a data trace event, a PC sample or a
performance profiling counter wraparound. The ITM outputs these packets on the trace
bus.
• Local timestamping
The ITM contains a 21-bit counter clocked by the (pre-divided) processor clock. The
counter value is output in a timestamp packet on the trace bus. The counter is reset to
zero every time a timestamp packet is generated. The timestamps thus indicate the
time elapsed since the previous timestamp packet.
For more information on the ITM and how to use it, refer to [4].
0xFF0
DWT_CIDR0
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
PREAMBLE[7:0]
Reset value 00001101
0xFF4
DWT_CIDR1
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
CLASS[3:0] PREAMBLE
[11:8]
Reset value 11100000
0xFF8
DWT_CIDR2
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
PREAMBLE[19:12]
Reset value 00000101
0xFFC
DWT_CIDR3
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
PREAMBLE[27:20]
Reset value 10110001
[Table 460](../tables/table_460.md). DWT register map and reset values (continued)
Offset Register name
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

RM0438 Rev 8 2063/2187
RM0438 Debug support (DBG)
2149
52.6.1 ITM registers
The ITM registers are located at address range 0xE000 0000 to 0xE000 0FFC.
ITM stimulus register x (ITM_STIMRx)
Address offset: 0x000 + 0x004 * x, (x = 0 to 31)
Reset value: 0xXXXX XXXX
ITM trace enable register (ITM_TER)
Address offset: 0xE00
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
STIMULUS[31:16]
wwwwwwwwwwwwwwww
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
STIMULUS[15:0]
wwwwwwwwwwwwww r w r w
Bits 31:0 STIMULUS[31:0]: trace output data
When writing, write data is output on the trace bus as a software event packet.
When reading:
l bit 1 is a disable flag:
– 0: stimulus port and ITM enabled
– 1: stimulus port and ITM disabled
l bit 0 is a FIFO ready indicator:
– 0: stimulus port buffer is full (or port is disabled)
– 1: stimulus port can accept new write data
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
STIMENA[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
STIMENA[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 STIMENA[31:0]: stimulus port enable
Each bit x(0 to 31) enables the stimulus port associated with the ITM_STIMRx register.
0: port disabled
1: port enabled

Debug support (DBG) RM0438
2064/2187 RM0438 Rev 8
ITM trace privilege register (ITM_TPR)
Address offset: 0xE40
Reset value: 0x0000 0000
ITM trace control register (ITM_TCR)
Address offset: 0xE80
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. PRIVMASK[3:0]
rrrr
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 PRIVMASK[3:0]: disable unprivileged access to ITM stimulus ports
Each bit controls eight stimulus ports.
XXX0: unprivileged access permitted on ports 0 to 7
XXX1: only privileged access permitted on ports 0 to 7
XX0X: unprivileged access permitted on ports 8 to 15
XX1X: only privileged access permitted on ports 8 to 15
X0XX: unprivileged access permitted on ports 16 to 23
X1XX: only privileged access permitted on ports 16 to 23
0XXX: unprivileged access permitted on ports 24 to 31
1XXX: only privileged access permitted on ports 24 to 31
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. BUSY TRACEBUSID[6:0]
r r wr wr wr wr wr wr w
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res.
TSPRESCALE[1:0]
Res. Res.
STALLENA
SWOENA
TXENA
SYNCENA
TSENA
ITMENA
rw rw rw r rw rw rw rw

RM0438 Rev 8 2065/2187
RM0438 Debug support (DBG)
2149
Bits 31:24 Reserved, must  be kept at reset value.
Bit 23 BUSY: indicates whether the ITM is currently processing events
0: not busy
1: busy
Bits 22:16 TRACEBUSID[6:0]: identifier for multi-source trace stream formatting
If multi-source trace is in use, the debugger must write a non-zero value to this field.
Note: Different identifiers must be used for each trace source in the system.
Bits 15:10 Reserved, must  be kept at reset value.
Bits 9:8 TSPRESCALE[1:0]: local timestamp prescaler, used with the trace packet reference clock
0x0: no prescaling
0x1: Divide by 4.
0x2: Divide by 16.
0x3: Divide by 64.
Bits 7:6 Reserved, must be kept at reset value.
Bit 5 STALLENA: stall enable
0: Drop hardware source packets and generate an overflow if the ITM output is stalled.
1: Stall the processor to guarantee delivery of data trace packets.
Bit 4 SWOENA: SWO enable
Enables asynchronous clocking of the timestamp counter (read only).
0: Timestamp counter uses processor clock.
Bit 3 TXENA: transmit enable
Enables forwarding of hardware event packets from the DWT unit to the trace port.
0: disabled
1: enabled
Bit 2 SYNCENA: synchronization packet transmission enable
The debugger setting this bit must also configure the DWT_CTRLR.SYNCTAP field for the
correct synchronization speed.
0: disabled
1: enabled
Bit 1 TSENA: local timestamp generation enable
0: disabled
1: enabled
Bit 0 ITMENA: ITM enable
0: disabled
1: enabled

Debug support (DBG) RM0438
2066/2187 RM0438 Rev 8
ITM device type architecture register (ITM_DEVARCHR)
Address offset: 0xFBC
Reset value: 0x4770 1A01
ITM device type register (ITM_DEVTYPER)
Address offset: 0xFCC
Reset value: 0x0000 0043
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ARCHITECT[10:0]
PRESEN
T REVISION[3:0]
rrrrrrr r r r rrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ARCHVER[3:0] ARCHPART[11:0]
rrrrrrr r r r rrrrrr
Bits 31:21 ARCHITECT[10:0]: architect JEP106 code
0x23B: JEP106 continuation code 0x4, JEP106 ID code 0x3B. Arm limited.
Bit 20 PRESENT: DEVARCH register presence
0x1: present
Bits 19:16 REVISION[3:0]: architecture revision
0x0: ITM architecture v2.0
Bits 15:12 ARCHVER[3:0]: architecture version
0x1: ITM architecture v2.0
Bits 11:0 ARCHPART[11:0]: architecture part
0xA01: ITM architecture
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. SUB[3:0] MAJOR[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 SUB[3:0]: sub-type
0x4: associated with a bus, stimulus derived from bus activity
Bits 3:0 MAJOR[3:0]: major type
0x3: trace source

RM0438 Rev 8 2067/2187
RM0438 Debug support (DBG)
2149
ITM CoreSight peripheral identity register 4 (ITM_PIDR4)
Address offset: 0xFD0
Reset value: 0x0000 0004
ITM CoreSight peripheral identity register 0 (ITM_PIDR0)
Address offset: 0xFE0
Reset value: 0x0000 0021
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. 4KCOUNT[3:0] JEP106CON[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 4KCOUNT[3:0]: register file size
0x0: The register file occupies a single 4-Kbyte region.
Bits 3:0 JEP106CON[3:0]: JEP106 continuation code
0x4: Arm® JEDEC code
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PARTNUM[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PARTNUM[7:0]: part number bits [7:0]
0x21: ITM part number

Debug support (DBG) RM0438
2068/2187 RM0438 Rev 8
ITM CoreSight peripheral identity register 1 (ITM_PIDR1)
Address offset: 0xFE4
Reset value: 0x0000 00BD
ITM CoreSight peripheral identity register 2 (ITM_PIDR2)
Address offset: 0xFE8
Reset value: 0x0000 000B
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. JEP106ID[3:0] PARTNUM[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 JEP106ID[3:0]: JEP106 identity code bits [3:0]
0xB: Arm® JEDEC code
Bits 3:0 PARTNUM[11:8]: part number bits [11:8]
0xD: ITM part number
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. REVISION[3:0] JEDEC JEP106ID[6:4]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVISION[3:0]: component revision number
0x0: r0p0
Bit 3 JEDEC: JEDEC assigned value
0x1: designer identification specified by JEDEC
Bits 2:0 JEP106ID[6:4]: JEP106 identity code bits [6:4]
0x3: Arm® JEDEC code

RM0438 Rev 8 2069/2187
RM0438 Debug support (DBG)
2149
ITM CoreSight peripheral identity register 3 (ITM_PIDR3)
Address offset: 0xFEC
Reset value: 0x0000 0000
ITM CoreSight component identity register 0 (ITM_CIDR0)
Address offset: 0xFF0
Reset value: 0x0000 000D
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. REVAND[3:0] CMOD[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVAND[3:0]: metal fix version
0x0: no metal fix
Bits 3:0 CMOD[3:0]: customer modified
0x0: no customer modifications
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[7:0]: Component identification bits [7:0]
0x0D: Common identification value

Debug support (DBG) RM0438
2070/2187 RM0438 Rev 8
ITM CoreSight peripheral identity register 1 (ITM_CIDR1)
Address offset: 0xFF4
Reset value: 0x0000 00E0
ITM CoreSight component identity register 2 (ITM_CIDR2)
Address offset: 0xFF8
Reset value: 0x0000 0005
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. CLASS[3:0] PREAMBLE[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 CLASS[3:0]: Component identification bits [15:12] - component class
0xE: Trace generator component
Bits 3:0 PREAMBLE[11:8]: Component identification bits [11:8]
0x0: Common identification value
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[19:12]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[19:12]: Component identification bits [23:16]
0x05: Common identification value

RM0438 Rev 8 2071/2187
RM0438 Debug support (DBG)
2149
ITM CoreSight component identity register 3 (ITM_CIDR3)
Address offset: 0xFFC
Reset value: 0x0000 00B1
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[27:20]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[27:20]: Component identification bits [31:24]
0xB1: Common identification value

Debug support (DBG) RM0438
2072/2187 RM0438 Rev 8
52.6.2 ITM register map and reset values
The ITM registers are located at address range 0xE000 0000 to 0xE000 0FFC.
[Table 461](../tables/table_461.md). CPU1 ITM register map and reset values
Offset Register name
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
0x000 to
0x07C
ITM_STIM0-31R STIMULUS[31:0]
R e s e t  v a l u e XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
0x07C to
0xDFC Reserved Reserved
0xE00
ITM_TER STIMENA[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x07C to
0xDFC Reserved Reserved
0xE40
ITM_TPR
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
PRIVMASK[3:0]
Reset value 0000
0xE44 to
0xE7C Reserved Reserved
0xE80
ITM_TCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
BUSY
TRACEBUSID[6:0]
Res.
Res.
Res.
Res.
Res.
Res.
TSPRESCALE[1:0]
Res.
Res.
STALLENA
SWOENA
TXENA
SYNCENA
TSENA
ITMENA
R e s e t  v a l u e 00000000 00 000000
0xE84 to
0xFB8 Reserved Reserved
0xFBC
ITM_DEVARCHR ARCHITECT[10:0]
PRESENT
REVISION[3:0]
ARCHVER[3:0]
ARCHPART[3:0]
R e s e t  v a l u e 01000111011100000001101000000001
0xFC0 to
0xFC8 Reserved Reserved
0xFCC
ITM_DEVTYPER
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
SUB[3:0] MAJOR[3:0]
Reset value 01000011
0xFD0
ITM_PIDR4
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
4KCOUNT[3:0]
JEP106CON[3:0]
Reset value 00000100
0xFE0
ITM_PIDR0
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
PARTNUM[7:0]
Reset value 00100001

RM0438 Rev 8 2073/2187
RM0438 Debug support (DBG)
2149
Refer to Section 2.3 for register boundary addresses.
52.7 Breakpoint unit (BPU)
The BPU allows the user to set hardware breakpoints. It contains eight comparators that
monitor the instruction fetch address. If a match occurs, the instruction comparators can be
configured to generate a breakpoint instruction.
For more information on the breakpoint unit and how to use it, refer to [4].
0xFE4
ITM_PIDR1
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
JEP106ID[3:0]
PARTNUM[11:8]
Reset value 10111101
0xFE8
ITM_PIDR2
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
REVISION[3:0]
JEDEC
JEP106ID[6:4]
Reset value 00001011
0xFEC
ITM_PIDR3
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
REVAND[3:0] CMOD[3:0]
Reset value 00000000
0xFF0
ITM_CIDR0
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
PREAMBLE[7:0]
Reset value 00001101
0xFF4
ITM_CIDR1
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
CLASS[3:0]
PREAMBLE[11:8]
Reset value 11100000
0xFF8
ITM_CIDR2
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
PREAMBLE[19:12]
Reset value 00000101
0xFFC
ITM_CIDR3
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
PREAMBLE[27:20]
Reset value 10110001
[Table 461](../tables/table_461.md). CPU1 ITM register map and reset values (continued)
Offset Register name
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

Debug support (DBG) RM0438
2074/2187 RM0438 Rev 8
52.7.1 BPU registers
The BPU registers are located at address range 0xE0002000 to 0xE0002FFC.
BPU control register (BPU_CTRLR)
Address offset: 0x000
Reset value: 0x1000 0080
BPU comparator x register (BPU_COMPxR)
Address offset: 0x008 + 0x004 * x, (x = 0 to 7)
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REV[3:0] Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
rrrr
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. NUM_CODE[6:4] Res. Res. Res. Res. NUM_CODE[3:0] Res. Res. KEY ENABLE
r r r rrrr r w r w
Bits 31:28 REV[3:0]: revision number
0x1: BPU version 2
Bits 27:15 Reserved, must  be kept at reset value.
Bits 11:8 Reserved, must be kept at reset value.
Bits 14:12, 7:4 NUM_CODE[6:0]: number of instruction address comparators supported
0x08: 8 instruction comparators supported
Bits 3:2 Reserved, must be kept at reset value.
Bit 1 KEY: Write protect key
A write to FPB_CTRLR register is ignored if this bit is not set to 1.
Bit 0 ENABLE: FPB enable
0: disabled
1: enabled
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
BPADDR[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
BPADDR[15:1] BE
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:1 BPADDR[31:1]: breakpoint address
Bit 0 BE: breakpoint enable
0: disabled
1: enabled

RM0438 Rev 8 2075/2187
RM0438 Debug support (DBG)
2149
BPU device type architecture register (BPU_DEVARCHR)
Address offset: 0xFBC
Reset value: 0x4770 1A03
BPU device type register (BPU_DEVTYPER)
Address offset: 0xFCC
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ARCHITECT[10:0]
PRESEN
T REVISION[3:0]
rrrrrrr r r r rrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ARCHVER[3:0] ARCHPART[11:0]
rrrrrrr r r r rrrrrr
Bits 31:21 ARCHITECT[10:0]: architect JEP106 code
0x23B: JEP106 continuation code 0x4, JEP106 ID code 0x3B. Arm limited.
Bit 20 PRESENT: DEVARCH register present
0x1: present
Bits 19:16 REVISION[3:0]: architecture revision
0x0: BPU architecture v2.0
Bits 15:12 ARCHVER[3:0]: architecture version
0x1: BPU architecture v2.0
Bits 11:0 ARCHPART[11:0]: architecture part
0xA03: BPU architecture
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. SUB[3:0] MAJOR[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 SUB[3:0]: sub-type
0x0: other
Bits 3:0 MAJOR[3:0]: major type
0x0: miscellaneous

Debug support (DBG) RM0438
2076/2187 RM0438 Rev 8
BPU CoreSight peripheral identity register 4 (BPU_PIDR4)
Address offset: 0xFD0
Reset value: 0x0000 0004
BPU CoreSight peripheral identity register 0 (BPU_PIDR0)
Address offset: 0xFE0
Reset value: 0x0000 0021
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. 4KCOUNT[3:0] JEP106CON[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 4KCOUNT[3:0]: register file size
0x0: The register file occupies a single 4-Kbyte region.
Bits 3:0 JEP106CON[3:0]: JEP106 continuation code
0x4: Arm® JEDEC code
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PARTNUM[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PARTNUM[7:0]: part number bits [7:0]
0x21: BPU part number

RM0438 Rev 8 2077/2187
RM0438 Debug support (DBG)
2149
BPU CoreSight peripheral identity register 1 (BPU_PIDR1)
Address offset: 0xFE4
Reset value: 0x0000 00BD
BPU CoreSight peripheral identity register 2 (BPU_PIDR2)
Address offset: 0xFE8
Reset value: 0x0000 000B
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. JEP106ID[3:0] PARTNUM[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 JEP106ID[3:0]: JEP106 identity code bits [3:0]
0xB: Arm® JEDEC code
Bits 3:0 PARTNUM[11:8]: part number bits [11:8]
0xD: BPU part number
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. REVISION[3:0] JEDEC JEP106ID[6:4]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVISION[3:0]: component revision number
0x0: r0p0
Bit 3 JEDEC: JEDEC assigned value
0x1: designer identification specified by JEDEC
Bits 2:0 JEP106ID[6:4]: JEP106 identity code bits [6:4]
0x3: Arm® JEDEC code

Debug support (DBG) RM0438
2078/2187 RM0438 Rev 8
BPU CoreSight peripheral identity register 3 (BPU_PIDR3)
Address offset: 0xFEC
Reset value: 0x0000 0000
BPU CoreSight component identity register 0 (BPU_CIDR0)
Address offset: 0xFF0
Reset value: 0x0000 000D
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. REVAND[3:0] CMOD[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVAND[3:0]: metal fix version
0x0: no metal fix
Bits 3:0 CMOD[3:0]: customer modified
0x0: no customer modifications
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[7:0]: component identification bits [7:0]
0x0D: common identification value

RM0438 Rev 8 2079/2187
RM0438 Debug support (DBG)
2149
BPU CoreSight peripheral identity register 1 (BPU_CIDR1)
Address offset: 0xFF4
Reset value: 0x0000 0090
BPU CoreSight component identity register 2 (BPU_CIDR2)
Address offset: 0xFF8
Reset value: 0x0000 0005
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. CLASS[3:0] PREAMBLE[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 CLASS[3:0]: component identification bits [15:12] - component class
0x9: debug component
Bits 3:0 PREAMBLE[11:8]: component identification bits [11:8]
0x0: common identification value
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[19:12]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[19:12]: component identification bits [23:16]
0x05: common identification value

Debug support (DBG) RM0438
2080/2187 RM0438 Rev 8
BPU CoreSight component identity register 3 (BPU_CIDR3)
Address offset: 0xFFC
Reset value: 0x0000 00B1
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[27:20]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[27:20]: component identification bits [31:24]
0xB1: common identification value

RM0438 Rev 8 2081/2187
RM0438 Debug support (DBG)
2149
52.7.2 BPU register map and reset values
The BPU registers are located at address range 0xE000 2000 to 0xE000 2FFC.
[Table 462](../tables/table_462.md). CPU1 BPU register map and reset values
Offset Register name
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
0x000
BPU_CTRLR REV[3:0]
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
NUM_CODE[6:4]
Res.
Res.
Res.
Res.
NUM_CODE[3:0]
Res.
Res.
KEY
ENABLE
R e s e t  v a l u e 0001 000 1000 00
0x004 Reserved Reserved
0x008 to
0x024
BPU_COMP0R to
PBU_COMP7R BPADDR[31:1]
ENABLE
R e s e t  v a l u e 00000000000000000000000000000000
0x028 to
0xFB8 Reserved Reserved
0xFBC
BPU_DEVARCHR ARCHITECT[10:0]
PRESENT
REVISION[3:0]
ARCHVER[3:0]
ARCHPART[3:0]
R e s e t  v a l u e 01000111011100000001101000000011
0xFC0 to
0xFC8 Reserved Reserved
0xFCC
BPU_DEVTYPER
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
SUB[3:0] MAJOR[3:0]
Reset value 00000000
0xFD0
BPU_PIDR4
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
4KCOUNT[3:0]
JEP106CON[3:0]
Reset value 00000100
0xFD4 to
0xFDC Reserved Reserved
0xFE0
BPU_PIDR0
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
PARTNUM[7:0]
Reset value 00100001
0xFE4
BPU_PIDR1
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
JEP106ID[3:0]
PARTNUM[11:8]
Reset value 10111101
0xFE8
BPU_PIDR2
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
REVISION[3:0]
JEDEC
JEP106ID[6:4]
Reset value 00001011

Debug support (DBG) RM0438
2082/2187 RM0438 Rev 8
Refer to Section 2.3 for register boundary addresses.
52.8 Embedded Trace Macrocell™ (ETM)
The ETM is a CoreSight component closely coupled to the CPU. The ETM generates trace
packets that allow the execution of the Cortex-M33 core to be traced. In the STM32L552xx
and STM32L562xx, the ETM is configured for instruction trace only. Data accesses are not
included in the trace information.
The ETM receives information from the CPU over the processor trace interface, including:
• number of instructions executed in the same cycle
• changes in program flow
• current processor instruction state
• addresses of memory locations accessed by load and store instructions
• type, direction and size of a transfer
• Condition code information
• exception information
• wait for interrupt state information
For more information, refer to the Arm® CoreSight™ ETM-M33 Technical Reference Manual
[6].
0xFEC
BPU_PIDR3
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
REVAND[3:0] CMOD[3:0]
Reset value 00000000
0xFF0
BPU_CIDR0
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
PREAMBLE[7:0]
Reset value 00001101
0xFF4
BPU_CIDR1
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
CLASS[3:0]
PREAMBLE[11:8]
Reset value 10010000
0xFF8
BPU_CIDR2
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
PREAMBLE[19:12]
Reset value 00000101
0xFFC
BPU_CIDR3
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
PREAMBLE[27:20]
Reset value 10110001
[Table 462](../tables/table_462.md). CPU1 BPU register map and reset values (continued)
Offset Register name
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

RM0438 Rev 8 2083/2187
RM0438 Debug support (DBG)
2149
52.8.1 ETM registers
The ETM registers are located at address range 0xE004 1000 to 0xE004 1FFC.
ETM programming control register (ETM_PRGCTLR)
Address offset: 0x004
Reset value: 0x0000 0000
ETM status register (ETM_STATR)
Address offset: 0x00C
Reset value: 0xXXXX XXXX
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. EN
rw
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 EN: trace unit enable
0: disabled
1: enabled
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
PMSTABLE
IDLE
rr
Bits 31:2 Reserved, must be kept at reset value.
Bit 1 PMSTABLE: stability status
Indicates that the ETM-M33 registers are stable and can be read.
0: not stable
1: stable
Bit 0 IDLE: trace unit status
Indicates that the trace unit is inactive.
0: not idle
1: idle

Debug support (DBG) RM0438
2084/2187 RM0438 Rev 8
ETM configuration register (ETM_CONFIGR)
Address offset: 0x010
Reset value: 0xXXXX XXXX
ETM event control 0 register (ETM_EVENTCTL0R)
Address offset: 0x020
Reset value: 0xXXXX XXXX
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. RS Res. COND[5:0] CCI BB Res. Res. Res.
rw rw rw rw rw rw rw rw rw
Bits 31:13 Reserved, must  be kept at reset value.
Bit 12 RS: return stack enable
0: disabled
1: enabled
Bit 11 Reserved, must be kept at reset value.
Bits 10:5 COND[5:0]: conditional instruction tracing
0x0: conditional instruction tracing disabled
0x1: conditional load instructions traced
0x2: conditional store instructions traced
0x3: conditional load and store instructions traced
0x7: All conditional instructions traced
Bit 4 CCI: cycle counting in instruction trace
0: disabled
1: enabled
Bit 3 BB: branch broadcast mode
0: disabled
1: enabled
Bits 2:0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
TYPE1 Res. Res. Res. SEL1[3:0] TYPE0 Res. Res. Res. SEL0[3:0]
rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 2085/2187
RM0438 Debug support (DBG)
2149
ETM event control 1 register (ETM_EVENTCTL1R)
Address offset: 0x024
Reset value: 0xXXXX XXXX
Bits 31:16 Reserved, must  be kept at reset value.
Bit 15 TYPE1: resource type for event1
0: single selected resource
1: boolean combined resource pair
Bits 14:12 Reserved, must  be kept at reset value.
Bits 11:8 SEL1[3:0]: resource number based on TYPE1
Selects the resource number, based on the value of TYPE1.
When TYPE1 = 0, a single resource from 0-15 defined by SEL1[3:0] is selected.
When TYPE1 = 1, a boolean combined resource pair defined by SEL1[2:0] is selected.
Bit 7 TYPE0: resource type for event0
0: single selected resource
1: boolean combined resource pair
Bits 6:4 Reserved, must be kept at reset value.
Bits 3:0 SEL0[3:0]: resource number based on TYPE0
Selects the resource number, based on the value of TYPE0.
When TYPE0 = 0, a single resource from 0-15 defined by SEL0[3:0] is selected.
When TYPE0 = 1, a boolean combined resource pair defined by SEL0[2:0] is selected.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res.
LPOVERRIDE
ATB Res. Res. Res. Res. Res. Res. Res. Res. Res. INSTEN[1:0]
rw rw rw rw
Bits 31:13 Reserved, must  be kept at reset value.
Bit 12 LPOVERRIDE: low-power state behavior override
0: normal low-power state behaviour
1: The resources and event trace generation are not affected by entry to a low-power state.

Debug support (DBG) RM0438
2086/2187 RM0438 Rev 8
ETM stall control register (ETM_STALLCTLR)
Address offset: 0x02C
Reset value: 0xXXXX XXXX
Bit 11 ATB: ATB trigger enable
0: disabled
1: enabled
Bits 10:2 Reserved, must be kept at reset value.
Bits 1:0 INSTEN[1:0]: instruction event generation
Enables generation of an event element in the instruction stream.
0bX0: Event0 does not cause an event element.
0bX1: Event0 causes an event element when it occurs.
0b0X: Event1 does not cause an event element.
0b1X: Event1 causes an event element when it occurs.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res.
INSTPRIORITY
Res.
ISTALL
Res. Res. Res. Res. LEVEL[3:0]
rw rw rw rw rw rw
Bits 31:11 Reserved, must be kept at reset value.
Bit 10 INSTPRIORITY: instruction trace priority
Prioritizes instruction trace if instruction trace buffer space is less than LEVEL.
0: The ETM must not prioritize instruction trace.
1: The ETM can prioritize instruction trace.
Bit 9 Reserved, must be kept at reset value.
Bit 8 ISTALL: processor stalling
Stalls processor based on instruction trace buffer space.
0: The ETM must not stall the processor.
1: The ETM can stall the processor.
Bits 7:4 Reserved, must be kept at reset value.
Bits 3:0 LEVEL[3:0]: Threshold at which stalling becomes active
This field provides four levels. This level can be varied to optimize the level of invasion
caused by stalling, balanced against the risk of a FIFO overflow.
0x0: zero invasion, but greater risk of FIFO overflow
...
0xF: maximum invasion but less risk of FIFO overflow

RM0438 Rev 8 2087/2187
RM0438 Debug support (DBG)
2149
ETM synchronization period register (ETM_SYNCPR)
Address offset: 0x034
Reset value: 0x0000 000A
ETM cycle count control register (ETM_CCCTLR)
Address offset: 0x038
Reset value: 0xXXXX XXXX
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. PERIOD[4:0]
rrrrr
Bits 31:5 Reserved, must be kept at reset value.
Bits 4:0 PERIOD[4:0]: synchronization period
Defines the number of bytes of trace between trace synchronization requests as a total of the
number of bytes generated by the instruction stream.
0xA: 1024 bytes
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. THRESHOLD[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:12 Reserved, must  be kept at reset value.
Bits 11:0 THRESHOLD[11:0]: instruction trace cycle count threshold
Sets the threshold value for instruction trace cycle counting. The threshold represents the
minimum interval between cycle-count trace packets.

Debug support (DBG) RM0438
2088/2187 RM0438 Rev 8
ETM trace identification register (ETM_TRACEIDR)
Address offset: 0x040
Reset value: 0xXXXX XXXX
ETM ViewInst main control register (ETM_VICTLR)
Address offset: 0x080
Reset value: 0xXXXX XXXX
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Re s. Res. Res. Res. Res. TRACEID[6:0]
rw rw rw rw rw rw rw
Bits 31:7 Reserved, must be kept at reset value.
Bits 6:0 TRACEID[6:0]: Trace identification to output onto the trace bus
This field must be programmed with a unique value to differentiate it from other trace sources
in the system.
Values 0x00 and 0x70-0x7F are reserved.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. EXLEVEL_S[3:0]
rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res.
TRCERR
TRCRESET
SSSTATUS
Res. EVENT[7:0]
rw rw rw rw rw rw rw rw rw rw rw
Bits 31:20 Reserved, must  be kept at reset value.
Bits 19:16 EXLEVEL_S[3:0]: exception level in secure state
Controls whether instruction tracing is enabled for the corresponding exception level, in
secure state.
0bXXX0: instruction trace not generated in secure state, for exception level 0
0bXXX1: instruction trace generated in secure state, for exception level 0
0b0XXX: instruction trace not generated in secure state, for exception level 3
0b1XXX: instruction trace generated in secure state, for exception level 3
Bits 15:12 Reserved, must  be kept at reset value.
Bit 11 TRCERR: trace system error exception
0: The system error exception is traced only if the instruction or exception immediately before
the system error exception is traced.
1: The system error exception is always traced.

RM0438 Rev 8 2089/2187
RM0438 Debug support (DBG)
2149
ETM counter reload value register 0 (ETM_CNTRLDVR0)
Address offset: 0x140
Reset value: 0xXXXX XXXX
ETM identification register 8 (ETM_IDR8)
Address offset: 0x180
Reset value: 0x0000 0000
Bit 10 TRCRESET: trace reset exception
0: The reset exception is traced only if the instruction or exception immediately before the
reset exception is traced.
1: The reset exception is always traced.
Bit 9 SSSTATUS: start/stop logic status
0: stopped
1: started
Bit 8 Reserved, must be kept at reset value.
Bits 7:0 EVENT[7:0]: event selector
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
VALUE[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 VALUE[15:0]: counter reload value
This value is loaded in to the counter each time the reload event occurs.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
MAXSPEC[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
MAXSPEC[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 MAXSPEC[31:0]: maximum speculation depth
Indicates the maximum speculation depth of the instruction trace stream. This is the
maximum number of P0 elements that have not been committed in the trace stream at any
one time.
0x0: The maximum trace speculation depth is zero.

Debug support (DBG) RM0438
2090/2187 RM0438 Rev 8
ETM identification register 9 (ETM_IDR9)
Address offset: 0x184
Reset value: 0x0000 0000
ETM identification register 10 (ETM_IDR10)
Address offset: 0x188
Reset value: 0x0000 0000
ETM identification register 11 (ETM_IDR11)
Address offset: 0x18C
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
NUMP0KEY[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
NUMP0KEY[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 NUMP0KEY[31:0]: number of P0 right-hand keys used
0x0: no P0 right-hand keys used in instruction trace
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
NUMP1KEY[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
NUMP1KEY[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 NUMP1KEY[31:0]: number of P1 right-hand keys used (including normal and special keys)
0x0: no P1 right-hand keys used in instruction trace
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
NUMP1SPC[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
NUMP1SPC[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 NUMP1SPC[31:0]: number of special P1 right-hand keys used
0x0: no special P1 right-hand keys used in any configuration

RM0438 Rev 8 2091/2187
RM0438 Debug support (DBG)
2149
ETM identification register 12 (ETM_IDR12)
Address offset: 0x190
Reset value: 0x0000 0001
ETM identification register 13 (ETM_IDR13)
Address offset: 0x194
Reset value: 0x0000 0000
ETM implementation specific register 0 (ETM_IMSPECR0)
Address offset: 0x1C0
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
NUMCONDKEY[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
NUMCONDKEY[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 NUMCONDKEY[31:0]: number of conditional instruction right-hand keys used (including
normal and special keys)
0x1: one conditional instruction right-hand key implemented
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
NUMCONDSPC[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
NUMCONDSPC[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 NUMCONDSPC[31:0]: number of special conditional instruction right-hand keys used
0x0: no special conditional instruction right-hand keys implemented
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. SUPPORT[3:0]
rrrr

Debug support (DBG) RM0438
2092/2187 RM0438 Rev 8
ETM identification register 0 (ETM_IDR0)
Address offset: 0x1E0
Reset value: 0x2800 06E1
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 SUPPORT[3:0]: implementation specific extension support
0x0: no implementation specific extensions are supported
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res.
COMMOPT
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res.
TRCEXDAT
A
QSUPP[1]
r rr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
QSUPP[0]
Res. CONDTYPE[1:0] NUMEVENT[1:0]
RETSTACK
Res.
TRCCCI
TRCCOND
TRCBB TRCDATA[1:0] INSTP0[1:0] Res.
r rrrrr rrrrrrr
Bits 31:30 Reserved, must  be kept at reset value.
Bit 29 COMMOPT: commit field meaning
Indicates the meaning of the commit field in some packets.
1: commit mode 1
Bits 28:18 Reserved, must  be kept at reset value.
Bit 17 TRCEXDATA: trace data transfers for exceptions
Indicates support for the tracing of data transfers for exceptions and exception returns.
0: not implemented
Bits 16:15 QSUPP[1:0]: Q element support
0: not supported
Bit 14 Reserved, must be kept at reset value.
Bits 13:12 CONDTYPE[1:0]: conditional results tracing
Indicates how conditional results are traced.
0: The trace unit indicates only if a conditional instruction passes or fails its condition code
check
Bits 11:10 NUMEVENT[1:0]: Number of events supported
0x1: two events
Bit 9 RETSTACK: return stack support
1: two entry return stacks
Bit 8 Reserved, must be kept at reset value.
Bit 7 TRCCCI: cycle counting support
1: cycle counting implemented
Bit 6 TRCCOND: conditional instruction support
1: conditional instruction tracing implemented

RM0438 Rev 8 2093/2187
RM0438 Debug support (DBG)
2149
ETM identification register 1 (ETM_IDR1)
Address offset: 0x1E4
Reset value: 0x4100 F421
ETM identification register 2 (ETM_IDR2)
Address offset: 0x1E8
Reset value: 0x0000 0004
Bit 5 TRCBB: branch broadcast support
1: branch broadcast tracing implemented
Bits 4:3 TRCDATA[1:0]: data tracing support
0x0: data tracing not supported
Bits 2:1 INSTP0[1:0]: support for tracing of load and store instructions as P0 elements
0x0: not supported
Bit 0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
DESIGNER[7:0] Res. Res. Res. Res. Res. Res. Res. Res.
rrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. TRCARCHMAJ[3:0] TRCARCHMIN[3:0] REVISION[3:0]
rrrrrrrrrrrr
Bits 31:24 DESIGNER[7:0]: trace unit designer
0x41: Arm®
Bits 23:12 Reserved, must  be kept at reset value.
Bits 11:8 TRCARCHMAJ[3:0]: major trace unit architecture version number
0x4: ETMv4
Bits 7:4 TRCARCHMIN[3:0]: minor trace unit architecture version number
0x2: minor revision 2
Bits 3:0 REVISION[3:0]: implementation revision number
0x1: implementation revision 1
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. CCSIZE[3:0] DVSIZE[4:0] DASIZE[4:1]
rrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DASIZE[0]
VMIDSIZE[4:0] CIDSIZE[4:0] IASIZE[4:0]
rrrrrrrrrrrrrrrr

Debug support (DBG) RM0438
2094/2187 RM0438 Rev 8
ETM identification register 3 (ETM_IDR3)
Address offset: 0x1EC
Reset value: 0x0F09 0004
Bits 31:29 Reserved, must  be kept at reset value.
Bits 28:25 CCSIZE[3:0]: cycle counter size
0x0: 12 bits
Bits 24:20 DVSIZE[4:0]: data value size
0x0: data value size not supported
Bits 19:15 DASIZE[4:0]: data address size.
0x0: data address size not supported
Bits 14:10 VMIDSIZE[4:0]: virtual machine ID size
0x0: virtual machine ID tracing not implemented
Bits 9:5 CIDSIZE[4:0]: context ID size
0x0: context ID tracing not implemented
Bits 4:0 IASIZE[4:0]: instruction address size
0x4: maximum 32-bit address size
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
NOOVERFLOW
NUMPROC[2:0]
SYSSTALL
STALLCTL
SYNCPR
TRCERR
Res. Res. Res. Res. EXLEVEL_S[3:0]
rrrrrrrr rrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. CCITMIN[11:0]
rrrrrrrrrrrr
Bit 31 NOOVERFLOW: ETM_STALLCTLR.NOOVERFLOW implementation
0: not implemented
Bits 30:28 NUMPROC[2:0]: number of processors available for tracing
0x0: one processor
Bit 27 SYSSTALL: system support for stall control of the processor
1: system supports stall control
Bit 26 STALLCTL: stall control support
1: ETM_STALLCTLR implemented
Bit 25 SYNCPR: trace synchronization period support
1: ETM_SYNCPR is read-only for instruction trace only configuration. The trace
synchronization period is fixed.
Bit 24 TRCERR: ETM_VICTLR.TRCERR implementation
0x1: implemented
Bits 23:20 Reserved, must  be kept at reset value.

RM0438 Rev 8 2095/2187
RM0438 Debug support (DBG)
2149
ETM identification register 4 (ETM_IDR4)
Address offset: 0x1F0
Reset value: 0x0011 4000
Bits 19:16 EXLEVEL_S[3:0]: privilege levels implementation
0x9: privilege levels thread and handler implemented
Bits 15:12 Reserved, must  be kept at reset value.
Bits 11:0 CCITMIN[11:0]: minimum value that can be programmed to TRCCCCTLR.THRESHOLD
Defines the minimum cycle counting threshold.
0x4: minimum of four-instruction trace cycles
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
NUMVMIDC[3:0] NUMCIDC[3:0] NUMSSCC[3:0] NUMRSPAIR[3:0]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
NUMPC[3:0] Res. Res. Res.
SUPPDAC
NUMDVC[3:0] NUMACPAIRS[3:0]
rrrr rrrrrrrrr
Bits 31:28 NUMVMIDC[3:0]: number of virtual machine ID (VMID) comparators
0x0: VMID comparators not implemented
Bits 27:24 NUMCIDC[3:0]: number of context ID comparators
0x0: context ID comparators not supported
Bits 23:20 NUMSSCC[3:0]: number of single-shot comparator controls
0x1: one single-shot comparator control implemented
Bits 19:16 NUMRSPAIR[3:0]: number of resource selection pairs
0x1: two resource selection pairs implemented
Bits 15:12 NUMPC[3:0]: number of processor comparator inputs for the DWT
0x4: four processor comparator inputs implemented
Bits 11:9 Reserved, must be kept at reset value.
Bit 8 SUPPDAC: data address comparisons
0: data address comparisons not supported
Bits 7:4 NUMDVC[3:0]: number of data value comparators
0x0: no data value comparators implemented
Bits 3:0 NUMACPAIRS[3:0]: number of address comparator pairs
0x0: no address comparator pairs implemented

Debug support (DBG) RM0438
2096/2187 RM0438 Rev 8
ETM identification register 5 (ETM_IDR5)
Address offset: 0x1F4
Reset value: 0x90C7 0004
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REDFUNCNTR
NUMCNTR[2:0] NUMSEQSTATE[2:0] Res.
LPOVERRIDE
ATBTRIG
TRACEIDSIZE[5:0]
rrrrrrr rrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. NUMEXTINSEL[2:0] NUMEXTIN[8:0]
rrrrrrrrrrrr
Bit 31 REDFUNCNTR: reduced function counter
1: counter 0 implemented as a reduced function counter
Bits 30:28 NUMCNTR[2:0]: number of counters
0x1: one counter implemented.
Bits 27:25 NUMSEQSTATE[2:0]: number of sequencer states
0x0: no sequencer states implemented.
Bit 24 Reserved, must be kept at reset value.
Bit 23 LPOVERRIDE: low-power state override support
1: low-power state override support implemented
Bit 22 ATBTRIG: ATB trigger support
1: ATB trigger support implemented
Bits 21:16 TRACEIDSIZE[5:0]: number of bits of trace identification
0x7: 7-bit trace identification implemented
Bits 15:12 Reserved, must  be kept at reset value.
Bits 11:9 NUMEXTINSEL[2:0]: number of external input selectors
0x0: no external input selectors implemented.
Bits 8:0 NUMEXTIN[8:0]: number of external inputs
0x004: four external inputs implemented.

RM0438 Rev 8 2097/2187
RM0438 Debug support (DBG)
2149
ETM resource register 2 (ETM_RSCTLR2)
Address offset: 0x208
Reset value: 0xXXXX XXXX
ETM resource register 3 (ETM_RSCTLR3)
Address offset: 0x20C
Reset value: 0xXXXX XXXX
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
PAIRINV
INV Res. GROUP[2:0]
rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. SELECT[7:0]
rw rw rw rw rw rw rw rw
Bits 31:22 Reserved, must  be kept at reset value.
Bit 21 PAIRINV: result of a combined pair of resources inversion
0: not inverted
1: inverted
Bit 20 INV: selected resources inversion
0: not inverted
1: inverted
Bit 19 Reserved, must be kept at reset value.
Bits 18:16 GROUP[2:0]: group of resources selection
0x0: external input selectors (select 0-3)
0x1: inputs from processor DWT comparators element (select 0-3)
0x2: counter at zero (select 0)
0x3: single-shot comparator (select 0)
others: reserved
Bits 15:8 Reserved, must be kept at reset value.
Bits 7:0 SELECT[7:0]: more resources selection
Selects one or more resources from the group selected in GROUP[2:0].
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. INV Res. GROUP[2:0]
rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. SELECT[7:0]
rw rw rw rw rw rw rw rw

Debug support (DBG) RM0438
2098/2187 RM0438 Rev 8
ETM single-shot comparator control register 0 (ETM_SSCCR0)
Address offset: 0x280
Reset value: 0xXXXX XXXX
Bits 31:21 Reserved, must  be kept at reset value.
Bit 20 INV: selected resources inversion
0: not inverted
1: inverted
Bit 19 Reserved, must be kept at reset value.
Bits 18:16 GROUP[2:0]: group of resources selection
0x0: external input selectors (select 0-3)
0x1: inputs from processor DWT comparators element (select 0-3)
0x2: counter at zero (select 0)
0x3: single-shot comparator (select 0)
others: reserved
Bits 15:8 Reserved, must be kept at reset value.
Bits 7:0 SELECT[7:0]: more resources selection
Selects one or more resources from the group selected in GROUP[2:0].
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. RST Res. Res. Res. Res. Res. Res. Res. Res.
rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
Bits 31:25 Reserved, must  be kept at reset value.
Bit 24 RST: single-shot comparator reset
Enables the single-shot comparator resource to be reset when it occurs, to enable another
comparator match to be detected.
1: reset enabled
Bits 23:0 Reserved, must be kept at reset value.

RM0438 Rev 8 2099/2187
RM0438 Debug support (DBG)
2149
ETM single-shot comparator status register 0 (ETM_SSCSR0)
Address offset: 0x2A0
Reset value: 0xXXXX XXXX
ETM single-shot processor comparator input control register 0
(ETM_SSPCICR0)
Address offset: 0x2C0
Reset value: 0xXXXX XXXX
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
STATUS
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res.
rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. PC DV DA INST
rrrr
Bit 31 STATUS: single-shot comparator status
Indicates whether any of the selected comparators have matched.
0: no match occurred
1: at least one match occurred
Bits 30:4 Reserved, must be kept at reset value.
Bit 3 PC: processor comparator input sensitivity
1: single-shot comparator sensitive to processor comparator inputs
Bit 2 DV: data value comparator support
0: single-shot data value comparisons not supported
Bit 1 DA: data address comparator support
0: single-shot data address comparisons not supported
Bit 0 INST: instruction address comparator support
0: single-shot instruction address comparisons not supported
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. PC[3:0]
rw rw rw rw

Debug support (DBG) RM0438
2100/2187 RM0438 Rev 8
ETM power-down control register (ETM_PDCR)
Address offset: 0x310
Reset value: 0x0000 0000
ETM power-down status register (ETM_PDSR)
Address offset: 0x314
Reset value: 0x0000 0003
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 PC[3:0]: processor comparator inputs selection for single-shot control
0xXXX0: processor comparator input 0 not selected
0xXXX1: processor comparator input 0 selected
0xXX0X: Processor comparator input 1 not selected
0xXX1X: processor comparator input 1 selected
0xX0XX: processor comparator input 2 not selected
0xX1XX: processor comparator input 2 selected
0x0XXX: processor comparator input 3 not selected
0x1XXX: processor comparator input 3 selected
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. PU Res. Res. Res.
rw
Bits 31:4 Reserved, must be kept at reset value.
Bit 3 PU: power-up request
0: power-up not requested
1: power-up requested
Bits 2:0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
STICKYPD
POWER
rr

RM0438 Rev 8 2101/2187
RM0438 Debug support (DBG)
2149
ETM claim tag set register (ETM_CLAIMSETR)
Address offset: 0xFA0
Reset value: 0x0000 000F
ETM claim tag clear register (ETM_CLAIMCLR)
Address offset: 0xFA4
Reset value: 0x0000 0000
Bits 31:2 Reserved, must be kept at reset value.
Bit 1 STICKYPD: sticky power-down state
0: Trace register power has not been removed since the ETM_PDSR was last read.
1: Trace register power has been removed since the ETM_PDSR was last read.
Bit 0 POWER: ETM power-up status
1: ETM powered up
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CLAIMSET[3:0]
rw rw rw rw
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 CLAIMSET[3:0]: claim tag bits setting
Write:
0000: no effect
xxx1: Sets bit 0.
xx1x: Sets bit 1.
x1xx: Sets bit 2.
1xxx: Sets bit 3.
Read:
0xF: Indicates there are four bits in claim tag.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CLAIMCLR[3:0]
rw rw rw rw

Debug support (DBG) RM0438
2102/2187 RM0438 Rev 8
ETM authentication status register (ETM_AUTHSTATR)
Address offset: 0xFB8
Reset value: 0xXXXX XXXX
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 CLAIMCLR[3:0]: claim tag bits reset
Write:
0000: no effect
xxx1: Clears bit 0.
xx1x: Clears bit 1.
x1xx: Clears bit 2.
1xxx: Clears bit 3.
Read: Returns current value of claim tag.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. SNID[1:0] SID[1:0] NSNID[1:0] NSID[1:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:6 SNID[1:0]: security level for secure non-invasive debug
0x2: secure non-invasive debug disabled
0x3: secure non-invasive debug enabled
Bits 5:4 SID[1:0]: security level for secure invasive debug
0x0: not implemented
Bits 3:2 NSNID[1:0]: security level for non-secure non-invasive debug
0x2: non-secure non-invasive debug disabled
0x3: non-secure non-invasive debug enabled
Bits 1:0 NSID[1:0]: security level for non-secure invasive debug
0x0: not implemented

RM0438 Rev 8 2103/2187
RM0438 Debug support (DBG)
2149
ETM device type architecture register (ETM_DEVARCHR)
Address offset: 0xFBC
Reset value: 0x4772 4A13
ETM CoreSight device type register (ETM_DEVTYPER)
Address offset: 0xFCC
Reset value: 0x0000 0013
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ARCHITECT[10:0]
PRESEN
T REVISION[3:0]
rrrrrrr r r r rrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ARCHVER[3:0] ARCHPART[11:0]
rrrrrrr r r r rrrrrr
Bits 31:21 ARCHITECT[10:0]: architect JEP106 code
0x23B: JEP106 continuation code 0x4, JEP106 ID code 0x3B. Arm limited.
Bit 20 PRESENT: DEVARCH register presence
0x1: present
Bits 19:16 REVISION[3:0]: architecture revision
0x2: ETM architecture v4.2
Bits 15:12 ARCHVER[3:0]: architecture version
0x4: ETM architecture v4.2
Bits 11:0 ARCHPART[11:0]: architecture part
0xA13: ETM architecture
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. SUBTYPE[3:0] MAJORTYPE[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 SUBTYPE[3:0]: device sub-type identifier
0x1: processor trace
Bits 3:0 MAJORTYPE[3:0]: device main type identifier
0x3: trace source

Debug support (DBG) RM0438
2104/2187 RM0438 Rev 8
ETM CoreSight peripheral identity register 4 (ETM_PIDR4)
Address offset: 0xFD0
Reset value: 0x0000 0004
ETM CoreSight peripheral identity register 0 (ETM_PIDR0)
Address offset: 0xFE0
Reset value: 0x0000 0021
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. 4KCOUNT[3:0] JEP106CON[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 4KCOUNT[3:0]: register file size
0x0: The register file occupies a single 4-Kbyte region.
Bits 3:0 JEP106CON[3:0]: JEP106 continuation code
0x4: ® JEDEC code
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PARTNUM[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PARTNUM[7:0]: part number bits [7:0]
0x21: ETM part number

RM0438 Rev 8 2105/2187
RM0438 Debug support (DBG)
2149
ETM CoreSight peripheral identity register 1 (ETM_PIDR1)
Address offset: 0xFE4
Reset value: 0x0000 00B9
ETM CoreSight peripheral identity register 2 (ETM_PIDR2)
Address offset: 0xFE8
Reset value: 0x0000 001B
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. JEP106ID[3:0] PARTNUM[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 JEP106ID[3:0]: JEP106 identity code bits [3:0]
0xB: Arm® JEDEC code
Bits 3:0 PARTNUM[11:8]: part number bits [11:8]
0xD: ETM part number
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. REVISION[3:0] JEDEC JEP106ID[6:4]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVISION[3:0]: component revision number
0x1: r0p1
Bit 3 JEDEC: JEDEC assigned value
0x1: designer identification specified by JEDEC
Bits 2:0 JEP106ID[6:4]: JEP106 identity code bits [6:4]
0x3: Arm® JEDEC code

Debug support (DBG) RM0438
2106/2187 RM0438 Rev 8
ETM CoreSight peripheral identity register 3 (ETM_PIDR3)
Address offset: 0xFEC
Reset value: 0x0000 0000
ETM CoreSight component identity register 0 (ETM_CIDR0)
Address offset: 0xFF0
Reset value: 0x0000 000D
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. REVAND[3:0] CMOD[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVAND[3:0]: metal fix version
0x0: no metal fix
Bits 3:0 CMOD[3:0]: customer modified
0x0: no customer modifications
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[7:0]: component identification bits [7:0]
0x0D: common identification value

RM0438 Rev 8 2107/2187
RM0438 Debug support (DBG)
2149
ETM CoreSight peripheral identity register 1 (ETM_CIDR1)
Address offset: 0xFF4
Reset value: 0x0000 0090
ETM CoreSight component identity register 2 (ETM_CIDR2)
Address offset: 0xFF8
Reset value: 0x0000 0005
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. CLASS[3:0] PREAMBLE[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 CLASS[3:0]: component identification bits [15:12] - component class
0x9: trace generator component
Bits 3:0 PREAMBLE[11:8]: component identification bits [11:8]
0x0: common identification value
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[19:12]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[19:12]: component identification bits [23:16]
0x05: common identification value

Debug support (DBG) RM0438
2108/2187 RM0438 Rev 8
ETM CoreSight component identity register 3 (ETM_CIDR3)
Address offset: 0xFFC
Reset value: 0x0000 00B1
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[27:20]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[27:20]: component identification bits [31:24]
0xB1: common identification value

RM0438 Rev 8 2109/2187
RM0438 Debug support (DBG)
2149
52.8.2 ETM register map and reset values
The ETM registers are accessed by the debugger at address range 0xE0041000 to
0xE0041FFC.
[Table 463](../tables/table_463.md). ETM register map and reset values
Offset Register name
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
0x004
ETM_PRGCTLR
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
Res.
Res.
EN
Reset value 0
0x008 Reserved Reserved
0x00C
ETM_STATR
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
Res.
PMSTABLE
IDLE
Reset value XX
0x010
ETM_CONFIGR
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
RS
Res.
COND[5:0]
CCI
BB
Res.
Res.
Res.
Reset value X XXXXXXXX
0x014 to
0x01C Reserved Reserved
0x020
ETM_
EVENTCTL0R
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
TYPE1
Res.
Res.
Res.
SEL1[3:0]
TYPE0
Res.
Res.
Res.
SEL0[3:0]
R e s e t  v a l u e X XXXXX XXXX
0x024
ETM_
EVENTCTL1R
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
LPOVERRIDE
ATB
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
INSTEN[1:0]
Reset value XX XX
0x028 Reserved Reserved
0x02C
ETM_STALLCTLR
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
INSTPRIORITY
Res.
ISTALL
Res.
Res.
Res.
Res.
LEVEL[3:0]
Reset value XX X X X X
0x030 Reserved Reserved
0x034
ETM_SYNCPR
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
PERIOD[4:0]
Reset value 01010
0x038
ETM_CCCTLR
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
THRESHOLD[11:0]
Reset value XXXXXXXXXXXX
0x03C Reserved Reserved
0x040
ETM_TRACEIDR
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
TRACEID[6:0]
Reset value XXXXXXX
0x044 to
0x07C Reserved Reserved

Debug support (DBG) RM0438
2110/2187 RM0438 Rev 8
0x080
ETM_VICTLR
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
EXLEVEL_S[3:0]
Res.
Res.
Res.
Res.
TRCERR
TRCRESET
SSSTATUS
Res.
EVENT[7:0]
R e s e t  v a l u e XXXX XXX XXXXXXXX
0x084 to
0x13C Reserved Reserved
0x140
ETM_CNTRLDVR0
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
VALUE[15:0]
R e s e t  v a l u e XXXXXXXXXXXXXXXX
0x144 to
0x17C Reserved Reserved
0x180
ETM_IDR8 MAXSPEC[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x184
ETM_IDR9 NUMP0KEY[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x188
ETM_IDR10 NUMP1KEY[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x18C
ETM_IDR11 NUMP1SPC[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x190
ETM_IDR12 NUMCONDKEY[31:0]
R e s e t  v a l u e 00000000000000000000000000000001
0x194
ETM_IDR13 NUMCONDSPC[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x198 to
0x1BC Reserved Reserved
0x1C0
ETM_IMSPECR0
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
SUPPORT[3:0]
Reset value 0000
0x1C4 to
0x1DC Reserved Reserved
0x1E0
ETM_IDR0
Res.
Res.
COMMOPT
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
TRCEXDATA
QSUPP[1:0]
Res.
CONDTYPE[1:0]
NUMEVENT[1:0]
RETSTACK
Res.
TRCCCI
TRCCOND
TRCBB
TRCDATA[1:0]
INSTP0[1:0]
Res.
R e s e t  v a l u e 1 000 00011 1110000
0x1E4
ETM_IDR1 DESIGNER[7:0]
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
TRCARCHMAJ[3:0]
TRCARCHMIN[3:0]
REVISION[3:0]
R e s e t  v a l u e 01000001 010000100001
[Table 463](../tables/table_463.md). ETM register map and reset values (continued)
Offset Register name
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

RM0438 Rev 8 2111/2187
RM0438 Debug support (DBG)
2149
0x1E8
ETM_IDR2
Res.
Res.
Res.
CCSIZE[3:0] DVSIZE[4:0] DASIZE[4:0] VMIDSIZE[4:0] CIDSIZE[4:0] IASIZE[4:0]
R e s e t  v a l u e 00000000000000000000000000100
0x1EC
ETM_IDR3
NOOVERFLOW
NUMPROC[2:0]
SYSSTALL
STALLCTL
SYNCPR
TRCERR
Res.
Res.
Res.
Res.
EXLEVEL_S[3:0]
Res.
Res.
Res.
Res.
CCITMIN[11:0]
R e s e t  v a l u e 00001111 1001 000000000100
0x1F0
ETM_IDR4
NUMVMIDC[3:0]
NUMCIDC[3:0]
NUMSSCC[3:0]
NUMRSPAIR[3:0]
NUMPC[3:0]
Res.
Res.
Res.
SUPPDAC
NUMDVC[3:0]
NUMACPAIRS[3:0]
R e s e t  v a l u e 00000000000100010100 000000000
0x1F4
ETM_IDR5
REDFUNCNTR
NUMCNTR[2:0]
NUMSEQSTATE[2:0]
Res.
LPOVERRIDE
ATBTRIG
TRACEIDSIZE[5:0]
Res.
Res.
Res.
Res.
NUMEXTINSEL[2:0]
NUMEXTIN[8:0]
R e s e t  v a l u e 1001000 11000111 000000000100
0x1F8 to
0x204 Reserved Reserved
0x208
ETM_RSCTLR2
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
PAIRINV
INV
Res.
GROUP[2:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SELECT[7:0]
R e s e t  v a l u e XX XXX XXXXXXXX
0x20C
ETM_RSCTLR3
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
INV
Res.
GROUP[2:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SELECT[7:0]
R e s e t  v a l u e X XXX XXXXXXXX
0x210 to
0x27C Reserved Reserved
0x280
ETM_SSCCR0
Res.
Res.
Res.
Res.
Res.
Res.
Res.
RST
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
Reset value X
0x284 to
0x29C Reserved Reserved
0x2A0
ETM_SSCSR0
STATUS
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
PC
DV
DA
INST
Reset value X XXXX
0x2A4 to
0x2BC Reserved Reserved
0x2C0
ETM_SSPCICR0
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
PC[3:0]
Reset value XXXX
0x2C4 to
0x30C Reserved Reserved
[Table 463](../tables/table_463.md). ETM register map and reset values (continued)
Offset Register name
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

Debug support (DBG) RM0438
2112/2187 RM0438 Rev 8
0x310
ETM_PDCR
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
PU
Res.
Res.
Res.
Reset value 0
0x314
ETM_PDSR
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
Res.
STICKYPD
POWER
Reset value 11
0x318 to
0xF9C Reserved Reserved
0xFA0
ETM_CLAIMSETR
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
CLAIMSET[3:0]
Reset value 1111
0xFA4
ETM_CLAIMCLR
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
CLAIMCLR[3:0]
Reset value 0000
0xFB8
ETM_AUTHSTATR
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
SNID[1:0]
SID[1:0]
NSNID[1:0]
NSID[1:0]
Reset value XXXXXXXX
0xFBC
ETM_DEVARCHR ARCHITECT[10:0]
PRESENT
REVISION[3:0]
ARCHVER[3:0]
ARCHPART[3:0]
R e s e t  v a l u e 01000111011100100100101000010011
0xFC0to
0xFC8 Reserved Reserved
0xFCC
ETM_DEVTYPER
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
SUBTYPE[3:0]
MAJORTYP[3:0]
Reset value 00010011
0xFD0
ETM_PIDR4
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
4KCOUNT[3:0]
JEP106CON[3:0]
Reset value 00000100
0xFD4to
0xFDC Reserved Reserved
0xFE0
ETM_PIDR0
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
PARTNUM[7:0]
Reset value 00100001
[Table 463](../tables/table_463.md). ETM register map and reset values (continued)
Offset Register name
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

RM0438 Rev 8 2113/2187
RM0438 Debug support (DBG)
2149
Refer to Section 2.3 for register boundary addresses.
52.9 Trace port interface unit (TPIU)
The TPIU formats the trace stream and outputs it on the external trace port signals. As
shown in [Figure 569](../figures/figure_569.md), the TPIU has two ATB slave ports for incoming trace data from the
ETM and ITM respectively. The trace port is a synchronous parallel port, comprising a clock
output, TRACECLK, and four data outputs, TRACEDATA(3:0). The trace port width is
programmable in the range 1 to 4. Using a smaller port width reduces the number of test
points/connector pins needed, and frees up IOs for other purposes, at the expenses of
bandwidth restriction of the trace port, and hence of the quantity of trace information that
can be output in real time.
0xFE4
ETM_PIDR1
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
JEP106ID[3:0]
PARTNUM[11:8]
Reset value 10111101
0xFE8
ETM_PIDR2
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
REVISION[3:0]
JEDEC
JEP106ID[6:4]
Reset value 00011011
0xFEC
ETM_PIDR3
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
REVAND[3:0] CMOD[3:0]
Reset value 00000000
0xFF0
ETM_CIDR0
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
PREAMBLE[7:0]
Reset value 00001101
0xFF4
ETM_CIDR1
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
CLASS
PREAMBLE[11:8]
Reset value 10010000
0xFF8
ETM_CIDR2
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
PREAMBLE[19:12]
Reset value 00000101
0xFFC
ETM_CIDR3
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
PREAMBLE[27:20]
Reset value 10110001
[Table 463](../tables/table_463.md). ETM register map and reset values (continued)
Offset Register name
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

Debug support (DBG) RM0438
2114/2187 RM0438 Rev 8
[Figure 569](../figures/figure_569.md). Trace port interface unit (TPIU)
Trace data can also be output on the serial-wire output, TRACESWO.
For more information on the trace port interface in the Cortex®-M33, refer to the Arm®
Cortex®-M33 Technical Reference Manual [5].
52.9.1 TPIU registers
TPIU supported port size register (TPIU_SSPSR)
Address offset: 0x000
Reset value: 0x0000 000F
MSv49704V1
ATB
interface
ATB
interface
APB
interface
Formatter
Trace
output
(serialiser)
ETM ATB
ITM ATB
Cortex-M33 private
peripheral bus
(PPB)
TRACECLK
TRACEDATA(3:0)
TRACESWO
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
PORTSIZE[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PORTSIZE[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 PORTSIZE[31:0]: trace port sizes, from 1 to 32 pins
Bit n-1 when set, indicates that port size n is supported.
0x0000 000F: port sizes 1 to 4 supported

RM0438 Rev 8 2115/2187
RM0438 Debug support (DBG)
2149
TPIU current port size register (TPIU_CSPSR)
Address offset: 0x004
Reset value: 0x0000 0001
TPIU asynchronous clock prescaler register (TPIU_ACPR)
Address offset: 0x010
Reset value: 0x0000 0000
TPIU selected pin protocol register (TPIU_SPPR)
Address offset: 0x0F0
Reset value: 0x0000 0001
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
PORTSIZE[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
PORTSIZE[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 PORTSIZE[31:0]: current trace port size
Bit n-1 when set, indicates that the current port size is n pins. The value of n must be within
the range of supported port sizes (1-4). Only one bit can be set, or unpredictable behavior
may result.
This register must only be modified when the formatter is stopped.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. PRESCALER[12:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:13 Reserved, must  be kept at reset value.
Bits 12:0 PRESCALER[12:0]: baud rate for the asynchronous output, TRACESWO
The baud rate is given by the TRACELKIN frequency divided by (PRESCALER +1).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. TXMODE[1:0]
rw rw

Debug support (DBG) RM0438
2116/2187 RM0438 Rev 8
TPIU formatter and flush status register (TPIU_FFSR)
Address offset: 0x300
Reset value: 0x0000 0008
Bits 31:2 Reserved, must be kept at reset value.
Bits 1:0 TXMODE[1:0]: protocol used for trace output
0x0: parallel trace port mode
0x1: asynchronous SWO using Manchester encoding
0x2: asynchronous SWO using NRZ encoding
0x3: reserved
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
FTNONSTOP
TCPRESENT
FTSTOPPED
FLINPROG
rrrr
Bits 31:4 Reserved, must be kept at reset value.
Bit 3 FTNONSTOP: formatter stop
Indicates whether formatter can be stopped or not.
1: The formatter cannot be stopped.
Bit 2 TCPRESENT: TRACECTL output pin availability
Indicates whether the optional TRACECTL output pin is available for use.
0: TRACECTL pin is not present in this device.
Bit 1 FTSTOPPED: formatter stop
The formatter has received a stop request signal and all trace data and post-amble is sent.
Any additional trace data on the ATB interface is ignored.
0: The formatter has not stopped.
Bit 0 FLINPROG: flush in progress
Indicates whether a flush on the ATB slave port is in progress. This bit reflects the status of
the AFVALIDS output. A flush can be initiated by the flush control bits in the TPIU_FFCR
register.
0: no flush in progress
1: flush in progress

RM0438 Rev 8 2117/2187
RM0438 Debug support (DBG)
2149
TPIU formatter and flush control register (TPIU_FFCR)
Address offset: 0x304
Reset value: 0x0000 0102
TPIU periodic synchronization counter register (TPIU_PSCR)
Address offset: 0x308
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. TRIGIN Res.
FONMAN
Res. Res. Res. Res. ENFCONT Res.
rr w r w
Bits 31:9 Reserved, must be kept at reset value.
Bit 8 TRIGIN: trigger on trigger in
1: Indicates a trigger in the trace stream when the TRIGIN input is asserted.
Bit 7 Reserved, must be kept at reset value.
Bit 6 FONMAN: flush on manual
0: flush completed
1: Generates a flush.
Bits 5:2 Reserved, must be kept at reset value.
Bit 1 ENFCONT: continuous formatting enable
Setting this bit to zero in SWO mode bypasses the formatter and only ITM/DWT trace is
output, ETM trace is discarded.
0: continuous formatting disabled
1: continuous formatting enabled
Bit 0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. PSCOUNT[12:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw

Debug support (DBG) RM0438
2118/2187 RM0438 Rev 8
TPIU claim tag set register (TPIU_CLAIMSETR)
Address offset: 0xFA0
Reset value: 0x0000 000F
TPIU claim tag clear register (TPIU_CLAIMCLR)
Address offset: 0xFA4
Reset value: 0x0000 0000
Bits 31:13 Reserved, must  be kept at reset value.
Bits 12:0 PSCOUNT[12:0]: formatter frames counter
Enables effective use of different sized TPAs without wasting large amounts of the storage
capacity of the capture device. This counter contains the number of formatter frames since
the last synchronization packet of 128 bits. It is a 12-bit counter with a maximum count value
of 4096. This equates to synchronization every 65536 bytes, that is, 4096 packets x 16 bytes
per packet. The default is set up for a synchronization packet every 1024 bytes, that is, every
64 formatter frames. If the formatter is configured for continuous mode, full and half-word
synchronization frames are inserted during normal operation. Under these circumstances,
the count value is the maximum number of complete frames between full synchronization
packets.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CLAIMSET[3:0]
rw rw rw rw
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 CLAIMSET[3:0]: claim tag bits setting
Write:
0000: no effect
xxx1: Sets bit 0.
xx1x: Sets bit 1.
x1xx: Sets bit 2.
1xxx: Sets bit 3.
Read:
0xF: Indicates there are four bits in claim tag.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CLAIMCLR[3:0]
rw rw rw rw

RM0438 Rev 8 2119/2187
RM0438 Debug support (DBG)
2149
TPIU device configuration register (TPIU_DEVIDR)
Address offset: 0xFC8
Reset value: 0x0000 0CA1
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 CLAIMCLR[3:0]: claim tag bits reset
Write:
0000: no effect
xxx1: Clears bit 0.
xx1x: Clears bit 1.
x1xx: Clears bit 2.
1xxx: Clears bit 3.
Read: Returns current value of claim tag.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res.
SWOUARTNRZ
SWOMAN
TCLKDATA
FIFOSIZE[2:0]
CLKRELAT
MAXNUM[4:0]
rrrrrrrrrrrr
Bits 31:12 Reserved, must  be kept at reset value.
Bit 11 SWOUARTNRZ: Serial-wire output, NRZ support
0x1: supported
Bit 10 SWOMAN: Serial-wire output, Manchester encoded format, support
0x1: supported
Bit 9 TCLKDATA: trace clock plus data support
0x0: supported
Bits 8:6 FIFOSIZE[2:0]: FIFO size in powers of 2
0x2: FIFO size = 4 bytes
Bit 5 CLKRELAT: ATB clock and TRACECLKIN relationship (synchronous or asynchronous)
0x1: asynchronous
Bits 4:0 MAXNUM[4:0]: number/type of ATB input port multiplexing
0x1: two input ports

Debug support (DBG) RM0438
2120/2187 RM0438 Rev 8
TPIU device type identifier register (TPIU_DEVTYPER)
Address offset: 0xFCC
Reset value: 0x0000 0011
TPIU CoreSight peripheral identity register 4 (TPIU_PIDR4)
Address offset: 0xFD0
Reset value: 0x0000 0004
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. SUBTYPE[3:0] MAJORTYPE[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 SUBTYPE[3:0]: sub-classification
0x1: trace port component
Bits 3:0 MAJORTYPE[3:0]: major classification
0x1: trace sink component
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. 4KCOUNT[3:0] JEP106CON[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 4KCOUNT[3:0]: register file size
0x0: The register file occupies a single 4-Kbyte region.
Bits 3:0 JEP106CON[3:0]: JEP106 continuation code
0x4: Arm® JEDEC code

RM0438 Rev 8 2121/2187
RM0438 Debug support (DBG)
2149
TPIU CoreSight peripheral identity register 0 (TPIU_PIDR0)
Address offset: 0xFE0
Reset value: 0x0000 0021
TPIU CoreSight peripheral identity register 1 (TPIU_PIDR1)
Address offset: 0xFE4
Reset value: 0x0000 00BD
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PARTNUM[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PARTNUM[7:0]: part number bits [7:0]
0x21: TPIU part number
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. JEP106ID[3:0] PARTNUM[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 JEP106ID[3:0]: JEP106 identity code bits [3:0]
0xB: Arm® JEDEC code
Bits 3:0 PARTNUM[11:8]: part number bits [11:8]
0xD: TPIU part number

Debug support (DBG) RM0438
2122/2187 RM0438 Rev 8
TPIU CoreSight peripheral identity register 2 (TPIU_PIDR2)
Address offset: 0xFE8
Reset value: 0x0000 000B
TPIU CoreSight peripheral identity register 3 (TPIU_PIDR3)
Address offset: 0xFEC
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. REVISION[3:0] JEDEC JEP106ID[6:4]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVISION[3:0]: component revision number
0x0: r0p0
Bit 3 JEDEC: JEDEC assigned value
0x1: designer identification specified by JEDEC
Bits 2:0 JEP106ID[6:4]: JEP106 identity code bits [6:4]
0x3: Arm® JEDEC code
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. REVAND[3:0] CMOD[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVAND[3:0]: metal fix version
0x0: no metal fix
Bits 3:0 CMOD[3:0]: customer modified
0x0: no customer modifications

RM0438 Rev 8 2123/2187
RM0438 Debug support (DBG)
2149
TPIU CoreSight component identity register 0 (TPIU_CIDR0)
Address offset: 0xFF0
Reset value: 0x0000 000D
TPIU CoreSight peripheral identity register 1 (TPIU_CIDR1)
Address offset: 0xFF4
Reset value: 0x0000 0090
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[7:0]: component identification bits [7:0]
0x0D: common identification value
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. CLASS[3:0] PREAMBLE[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 CLASS[3:0]: component ID bits [15:12] - component class
0x9: CoreSight component
Bits 3:0 PREAMBLE[11:8]: component identification bits [11:8]
0x0: common identification value

Debug support (DBG) RM0438
2124/2187 RM0438 Rev 8
TPIU CoreSight component identity register 2 (TPIU_CIDR2)
Address offset: 0xFF8
Reset value: 0x0000 0005
TPIU CoreSight component identity register 3 (TPIU_CIDR3)
Address offset: 0xFFC
Reset value: 0x0000 00B1
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[19:12]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[19:12]: component identification bits [23:16]
0x05: common identification value
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[27:20]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[27:20]: component identification bits [31:24]
0xB1: common identification value

RM0438 Rev 8 2125/2187
RM0438 Debug support (DBG)
2149
52.9.2 TPIU register map and reset values
[Table 464](../tables/table_464.md). CPU1 TPIU register map and reset values
Offset Register name
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
0x000
TPIU_SSPSR PORTSIZE[31:0]
R e s e t  v a l u e 00000000000000000000000000001111
0x004
TPIU_CSPSR PORTSIZE[31:0]
R e s e t  v a l u e 00000000000000000000000000000001
0x008 Reserved Reserved
0x010
TPIU_ACPR
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
PRESCALER[12:0]
Reset value 0000000000000
0x014 to
0x0EC Reserved Reserved
0x0F0
TPIU_SPPR
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
Res.
TXMODE[1:0]
Reset value 01
0x0F4 to
0x2FC Reserved Reserved
0x300
TPIU_FFSR
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
FTNONSTOP
TCPRESENT
FTSTOPPED
FLINPROG
Reset value 1000
0x304
TPIU_FFCR
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
TRIGIN
Res.
FONMAN
Res.
Res.
Res.
Res.
ENFCONT
Res.
Reset value 10 1
0x308
TPIU_PSCR
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
PSCOUNT[12:0]
Reset value 0000000000000
030C to
0xF9C Reserved Reserved
0xFA0
TPIU_CLAIMSETR
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
CLAIMSET[3:0]
Reset value 1111
0xFA4
TPIU_CLAIMCLR
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
CLAIMCLR[3:0]
Reset value 0000
0FA8 to
0xFC4 Reserved Reserved
0xFC8
TPIU_DEVIDR
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
SWONRZ
SWOMAN
TCLKDATA
FIFOSIZE[2:0]
CLKRELAT
MUXNUM[4:0]
Reset value 110010100001

Debug support (DBG) RM0438
2126/2187 RM0438 Rev 8
Refer to Section 2.3 for register boundary addresses.
0xFCC
TPIU_DEVTYPER
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
SUBTYPE[3:0]
MAJORTYPE[3:0]
Reset value 00010001
0xFD0
TPIU_PIDR4
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
4KCOUNT[3:0]
JEP106CON[3:0]
Reset value 00000100
0xFE0
TPIU_PIDR0
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
PARTNUM[7:0]
Reset value 00100001
0xFE4
TPIU_PIDR1
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
JEP106ID[3:0]
PARTNUM[11:8]
Reset value 10111101
0xFE8
TPIU_PIDR2
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
REVISION[3:0]
JEDEC
JEP106ID[6:4]
Reset value 00001011
0xFEC
TPIU_PIDR3
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
REVAND[3:0] CMOD[3:0]
Reset value 00000000
0xFF0
TPIU_CIDR0
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
PREAMBLE[7:0]
Reset value 00001101
0xFF4
TPIU_CIDR1
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
CLASS[3:0]
PREAMBLE[11:8]
Reset value 10010000
0xFF8
TPIU_CIDR2
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
PREAMBLE[19:12]
Reset value 00000101
0xFFC
TPIU_CIDR3
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
PREAMBLE[27:20]
Reset value 10110001
[Table 464](../tables/table_464.md). CPU1 TPIU register map and reset values (continued)
Offset Register name
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

RM0438 Rev 8 2127/2187
RM0438 Debug support (DBG)
2149
52.10 Cross-trigger interface (CTI)
The CTI allows cross triggering between the processor and the ETM (see [Figure 570](../figures/figure_570.md)).
[Figure 570](../figures/figure_570.md). Embedded cross trigger
The CTI enables events from various sources to trigger debug and/or trace activity. For
example, a watchpoint reached in the processor can start or stop code trace, or a trace
comparator can halt the processor.
The trigger input and output signals for the CTI are listed in [Table 465](../tables/table_465.md) and [Table 466](../tables/table_466.md).
MSv49705V1
PPB Cortex-M33 CTI
Cortex-M33
CPU
HALTED
EDBGRQ
ETMEXTIN0
ETMEXTIN1ETM
TRIGIN0
TRIGOUT0
TRIGOUT4
TRIGOUT5
ETMTRIGGER0
ETMTRIGGER1
ETMTRIGGER2 TRIGIN3
TRIGIN2
TRIGIN1
TRIGIN4ETMTRIGOUT0
DWT
DBGRESTART TRIGOUT1
TRIGIN5ETMTRIGOUT1
ETMEXTIN2
ETMEXTIN3
TRIGOUT6
TRIGOUT7
[Table 465](../tables/table_465.md). CTI inputs
Number Source signal Source component Comments
0 HALTED CPU Processor halted - CPU is in debug mode
1 ETMTRIGGER0 DWT DWT comparator output 0
2 ETMTRIGGER1 DWT DWT comparator output 1
3 ETMTRIGGER2 DWT DWT comparator output 2
4 ETMTRIGOUT0 ETM ETM  event output 0
5 ETMTRIGOUT1 ETM ETM  event output 1
6 - - Not used
7 - - Not used
[Table 466](../tables/table_466.md). CTI outputs
Number Source signal Destination component Comments
0 EDBGRQ CPU CPU halt request - Puts CPU in debug mode
1 DBGRESTART CPU CPU restart request - CPU exits debug mode

Debug support (DBG) RM0438
2128/2187 RM0438 Rev 8
For more information on the cross-trigger interface CoreSight component, refer to the Arm®
CoreSight SoC-400 Technical Reference Manual [2].
52.10.1 CTI registers
The register file base address for the CTI is 0xE004 2000.
CTI control register (CTI_CONTROLR)
Address offset: 0x000
Reset value: 0x0000 0000
CTI trigger acknowledge register (CTI_INTACKR)
Address offset: 0x010
Reset value: 0xXXXX XXXX
2 ETMEXTIN0 ETM ETM event input 0
3 ETMEXTIN1 ETM ETM event input 1
4 ETMEXTIN2 ETM ETM event input 2
5 ETMEXTIN3 ETM ETM event input 3
6 - - Not used
7 - - Not used
[Table 466](../tables/table_466.md). CTI outputs (continued)
Number Source signal Destination component Comments
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. GLBEN
rw
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 GLBEN: global CTI enable
0: disabled
1: enabled
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. INTACK[7:0]
wwwwwwww

RM0438 Rev 8 2129/2187
RM0438 Debug support (DBG)
2149
CTI application trigger set register (CTI_APPSETR)
Address offset: 0x014
Reset value: 0x0000 0000
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 INTACK[7:0]: trigger acknowledge
There is one bit of the register for each CTITRIGOUT output. When a 1 is written to a bit in
this register, the corresponding CTITRIGOUT output is acknowledged, causing it to be
cleared.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. APPSET[3:0]
rw rw rw rw
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 APPSET[3:0]: channel event setting
Read:
XXX0: channel 0 event inactive
XXX0: channel 0 event active
XX0X: channel 1 event inactive
XX1X: channel 1 event active
X0XX: channel 2 event inactive
X1XX: channel 2 event active
0XXX: channel 3 event inactive
1XXX: channel 3 event active
Write:
XXX0: no effect
XXX0: Sets event on channel 0.
XX0X: no effect
XX1X: Sets event on channel 1.
X0XX: no effect
X1XX: Sets event on channel 2.
0XXX: no effect
1XXX: Sets event on channel 3.

Debug support (DBG) RM0438
2130/2187 RM0438 Rev 8
CTI application trigger clear register (CTI_APPCLEAR)
Address offset: 0x018
Reset value: 0x0000 0000
CTI application pulse register (CTI_APPPULSER)
Address offset: 0x01C
Reset value: 0xXXXX XXXX
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. APPCLEAR[3:0]
rw rw rw rw
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 APPCLEAR[3:0]: channel event clear
0000: no effect
XXX1: Clears event on channel 0.
XX1X: Clears event on channel 1.
X1XX: Clears event on channel 2.
1XXX: Clears event on channel 3.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. APPPULSE[3:0]
wwww
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 APPPULSE[3:0]: pulse channel event
This register clears itself immediately.
0000: no effect
XXX1: Generates pulse on channel 0.
XX1X: Generates pulse on channel 1.
X1XX: Generates pulse on channel 2.
1XXX: Generates pulse on channel 3.

RM0438 Rev 8 2131/2187
RM0438 Debug support (DBG)
2149
CTI trigger input x enable register (CTI_INENxR)
Address offset: 0x020 + 0x004 * x, (x = 0 to 7)
Reset value: 0x0000 0000
CTI trigger output x enable register (CTI_OUTENxR)
Address offset: 0x0A0 + 0x004 * x, (x = 0 to 7)
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. TRIGINEN[3:0]
rw rw rw rw
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 TRIGINEN[3:0]: trigger input event enable
Enables or disables a cross trigger event on each of the four channels when CTITRIGINx is
activated (x = 0 to 7).
0000: Trigger does not generate events on channels.
XXX1: Trigger x generates events on channel 0.
XX1X: Trigger x generates events on channel 1.
X1XX: Trigger x generates events on channel 2.
1XXX: Trigger x generates events on channel 3.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. TRIGOUTEN[3:0]
rw rw rw rw
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 TRIGOUTEN[3:0]: trigger output event enable
For each channel, defines whether an event on that channel generates a trigger on
CTITRIGOUTx (x = 0 to 7).
0000: Channel events do not generate triggers on trigger outputs.
XXX1: Channel 0 events generate triggers on trigger output x.
XX1X: Channel 1 events generate triggers on trigger output x.
X1XX: Channel 2 events generate triggers on trigger output x.
1XXX: Channel 3 events generate triggers on trigger output x.

Debug support (DBG) RM0438
2132/2187 RM0438 Rev 8
CTI trigger input status register (CTI_TRGISTSR)
Address offset: 0x130
Reset value: 0x0000 0000
CTI trigger output status register (CTI_TRGOSTSR)
Address offset: 0x134
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. TRIGINSTATUS[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 TRIGINSTATUS[7:0]: trigger input status
There is one bit of the register for each CTITRIGINx input. When a bit is set to 1, it indicates
that the corresponding trigger input is active. When it is set to 0, the corresponding trigger
input is inactive.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. TRIGOUTSTATUS[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 TRIGOUTSTATUS[7:0]: trigger output status
There is one bit of the register for each CTITRIGOUT output. When a bit is set to 1, it
indicates that the corresponding trigger output is active. When it is set to 0, the corresponding
trigger output is inactive.

RM0438 Rev 8 2133/2187
RM0438 Debug support (DBG)
2149
CTI channel input status register (CTI_CHINSTSR)
Address offset: 0x138
Reset value: 0x0000 0000
CTI channel output status register (CTI_CHOUTSTSR)
Address offset: 0x13C
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CHINSTATUS[3:0]
rrrr
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 CHINSTATUS[3:0]: channel input status
There is one bit of the register for each channel input. When a bit is set to 1 it indicates that
the corresponding channel input is active. When it is set to 0, the corresponding channel
input is inactive.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CHOUTSTATUS[3:0]
rrrr
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 CHOUTSTATUS[3:0]: channel output status
There is one bit of the register for each channel output. When a bit is set to 1 it indicates that
the corresponding channel output is active. When it is set to 0, the corresponding channel
output is inactive.

Debug support (DBG) RM0438
2134/2187 RM0438 Rev 8
CTI channel gate register (CTI_GATER)
Address offset: 0x140
Reset value: 0x0000 000F
CTI device configuration register (CTI_DEVIDR)
Address offset: 0xFC8
Reset value: 0x0004 0800
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. GATEEN[3:0]
rw rw rw rw
Bits 31:4 Reserved, must be kept at reset value.
Bits 3:0 GATEEN[3:0]: channel output enable
For each channel, defines whether an event on that channel can propagate over the CTM to
other CTIs.
0000: Channels events do not propagate.
XXX1: Channel 0 events propagate.
XX1X: Channel 1 events propagate.
X1XX: Channel 2 events propagate.
1XXX: Channel 3 events propagate.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. NUMCH[3:0]
rrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
NUMTRIG[7:0] Res. Res. Res. EXTMUXNUM[4:0]
rrrrrrr r r r r r r
Bits 31:20 Reserved, must  be kept at reset value.
Bits 19:16 NUMCH[3:0]: number of ECT channels available
0x4: four channels
Bits 15:8 NUMTRIG[7:0]: number of ECT triggers available
0x8: height trigger inputs and height trigger outputs
Bits 7:5 Reserved, must be kept at reset value.
Bits 4:0 EXTMUXNUM[4:0]: number of trigger input/output multiplexers
0x0: none

RM0438 Rev 8 2135/2187
RM0438 Debug support (DBG)
2149
CTI device type identifier register (CTI_DEVTYPER)
Address offset: 0xFCC
Reset value: 0x0000 0014
CTI CoreSight peripheral identity register 4 (CTI_PIDR4)
Address offset: 0xFD0
Reset value: 0x0000 0004
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. SUBTYPE[3:0] MAJORTYPE[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 SUBTYPE[3:0]: sub-classification
0x1: cross-triggering component.
Bits 3:0 MAJORTYPE[3:0]: major classification
0x4: Indicates that this component allows a debugger to control other components in a
CoreSight SoC-400 system.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. 4KCOUNT[3:0] JEP106CON[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 4KCOUNT[3:0]: register file size
0x0: The register file occupies a single 4-Kbyte region.
Bits 3:0 JEP106CON[3:0]: JEP106 continuation code
0x4: Arm® JEDEC code

Debug support (DBG) RM0438
2136/2187 RM0438 Rev 8
CTI CoreSight peripheral identity register 0 (CTI_PIDR0)
Address offset: 0xFE0
Reset value: 0x0000 0006
CTI CoreSight peripheral identity register 1 (CTI_PIDR1)
Address offset: 0xFE4
Reset value: 0x0000 00BD
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PARTNUM[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PARTNUM[7:0]: part number bits [7:0]
0x21: CTI part number
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. JEP106ID[3:0] PARTNUM[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 JEP106ID[3:0]: JEP106 identity code bits [3:0]
0xB: Arm® JEDEC code
Bits 3:0 PARTNUM[11:8]: part number bits [11:8]
0xD: CTI part number

RM0438 Rev 8 2137/2187
RM0438 Debug support (DBG)
2149
CTI CoreSight peripheral identity register 2 (CTI_PIDR2)
Address offset: 0xFE8
Reset value: 0x0000 000B
CTI CoreSight peripheral identity register 3 (CTI_PIDR3)
Address offset: 0xFEC
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. REVISION[3:0] JEDEC JEP106ID[6:4]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVISION[3:0]: component revision number
0x0: r0p0
Bit 3 JEDEC: JEDEC assigned value
0x1: designer identification specified by JEDEC
Bits 2:0 JEP106ID[6:4]: JEP106 identity code bits [6:4]
0x3: Arm® JEDEC code
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. REVAND[3:0] CMOD[3:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 REVAND[3:0]: metal fix version
0x0: no metal fix
Bits 3:0 CMOD[3:0]: customer modified
0x0: no customer modifications

Debug support (DBG) RM0438
2138/2187 RM0438 Rev 8
CTI CoreSight component identity register 0 (CTI_CIDR0)
Address offset: 0xFF0
Reset value: 0x0000 000D
CTI CoreSight peripheral identity register 1 (CTI_CIDR1)
Address offset: 0xFF4
Reset value: 0x0000 0090
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[7:0]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[7:0]: component identification bits [7:0]
0x0D: common identification value
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. CLASS[3:0] PREAMBLE[11:8]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:4 CLASS[3:0]: component identification bits [15:12] - component class
0x9: CoreSight component
Bits 3:0 PREAMBLE[11:8]: component identification bits [11:8]
0x0: common identification value

RM0438 Rev 8 2139/2187
RM0438 Debug support (DBG)
2149
CTI CoreSight component identity register 2 (CTI_CIDR2)
Address offset: 0xFF8
Reset value: 0x0000 0005
CTI CoreSight component identity register 3 (CTI_CIDR3)
Address offset: 0xFFC
Reset value: 0x0000 00B1
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[19:12]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[19:12]: component identification bits [23:16]
0x05: common identification value
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PREAMBLE[27:20]
rrrrrrrr
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:0 PREAMBLE[27:20]: component identification bits [31:24]
0xB1: common identification value

Debug support (DBG) RM0438
2140/2187 RM0438 Rev 8
52.10.2 CTI register map and reset values
[Table 467](../tables/table_467.md). CTI register map and reset values
Offset Register name
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
0x000
CTI_CONTROLR
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
Res.
Res.
GLBEN
Reset value 0
0x004 to
0x00C Reserved Reserved
0x010
CTI_INTACKR
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
INTACK[7:0]
Reset value XXXXXXXX
0x014
CTI_APPSETR
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
APPSET[3:0]
Reset value 0000
0x018
CTI_APPCLEAR
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
APPCLEAR[3:0]
Reset value 0000
0x01C
CTI_APPPULSER
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
APPPULSE[3:0]
Reset value XXXX
0x020 to
0x03C
CTI_INEN0R to
CTI_INEN7R
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
TRIGINEN[3:0]
Reset value 0000
0x040 to
0x09C Reserved Reserved
0x0A0 to
0x0BC
CTI_OUTEN0R to
CTI_OUTEN7R
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
TRIGOUTEN[3:0]
Reset value 0000
0x0C0 to
0x12C Reserved Reserved
0x130
CTI_TRGISTSR
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
TRIGINSTATUS[7:0]
Reset value 00000000
0x134
CTI_TRGOSTSR
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
TRIGOUTSTATUS[7:0]
Reset value 00000000

RM0438 Rev 8 2141/2187
RM0438 Debug support (DBG)
2149
0x138
CTI_CHINSTSR
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
CHISTATUS[3:0]
Reset value 0000
0x13C
CTI_CHOUTSTSR
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
CHOSTATUS[3:0]
Reset value 0000
0x140
CTI_GATER
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
GATEEN[3:0]
Reset value 1111
0x144 to
0xFC4 Reserved Reserved
0xFC8
CTI_DEVIDR
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
NUMCH[3:0] NUMTRIG[7:0]
Res.
Res.
Res.
EXTMUXNUM[4:0]
R e s e t  v a l u e 010000001000 00000
0xFCC
CTI_DEVTYPER
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
SUB[3:0] MAJOR[3:0]
Reset value 00010100
0xFD0
CTI_PIDR4
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
4KCOUNT[3:0]
JEP106CON[3:0]
Reset value 00000100
0xFD4 to
0xFBC Reserved Reserved
0xFE0
CTI_PIDR0
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
PARTNUM[7:0]
Reset value 00000110
0xFE4
CTI_PIDR1
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
JEP106ID[3:0]
PARTNUM[11:8]
Reset value 10111101
0xFE8
CTI_PIDR2
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
REVISION[3:0]
JEDEC
JEP106ID[6:4]
Reset value 00001011
0xFEC
CTI_PIDR3
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
REVAND[3:0] CMOD[3:0]
Reset value 00000000
[Table 467](../tables/table_467.md). CTI register map and reset values (continued)
Offset Register name
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

Debug support (DBG) RM0438
2142/2187 RM0438 Rev 8
Refer to Section 2.3 for register boundary addresses.
52.11 Microcontroller debug unit (DBGMCU)
The DBGMCU is a component containing a number of registers that control the power and
clock behavior in debug mode. It allows the debugger (or the software) to:
• maintain the clock and power to the processor cores when in low power modes (Sleep,
Stop or Standby)
• maintain the clock and power to the system debug and trace components when in low
power modes
• stop the clock to certain peripherals (SMBUS timeout, watchdogs, timers, RTC) when
either processor core is stopped in debug mode
Note: The DBGMCU is not a standard CoreSight  component, consequently it does not appear in
the MCU ROM table.
0xFF0
CTI_CIDR0
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
PREAMBLE[7:0]
Reset value 00001101
0xFF4
CTI_CIDR1
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
CLASS[3:0]
PREAMBLE[11:8]
Reset value 10010000
0xFF8
CTI_CIDR2
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
PREAMBLE[19:12]
Reset value 00000101
0xFFC
CTI_CIDR3
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
PREAMBLE[27:20]
Reset value 10110001
[Table 467](../tables/table_467.md). CTI register map and reset values (continued)
Offset Register name
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

RM0438 Rev 8 2143/2187
RM0438 Debug support (DBG)
2149
52.11.1 DBGMCU registers
The DBGMCU registers are not reset by a system reset, only by a power-on reset. They are
accessible to the debugger via the AHB access port at base address 0xE004 4000.
DBGMCU identity code register (DBGMCU_IDCODE)
Address offset: 0x00
Reset value: 0x2001 6472
DBGMCU configuration register (DBGMCU_CR)
Address offset: 0x04
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REV_ID[15:0]
rrrrrrr r r r rrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. DEV_ID[11:0]
r rrrrrrrrrrr
Bits 31:16 REV_ID[15:0]: revision
0x1000: revision A
0x2000: revision B
0x2001: revision Z
Bits 15:12 Reserved, must  be kept at reset value.
Bits 11:0 DEV_ID[11:0]: device identification
0x472: STM32L552xx and STM32L562xx
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res.
TRACE_MODE[1:0]
TRACE_EN
TRACE_IOEN
Res.
DBG_STANDBY
DBG_STOP
Res.
rw rw rw rw rw rw

Debug support (DBG) RM0438
2144/2187 RM0438 Rev 8
Bits 31:8 Reserved, must be kept at reset value.
Bits 7:6 TRACE_MODE[1:0]: trace pin assignment
0x0: trace pins assigned for asynchronous mode (TRACESWO)
0x1: trace pins assigned for synchronous mode with a port width of 1 (TRACECK,
TRACED0)
0x2: trace pins assigned for synchronous mode with a port width of 2 ((TRACECK,
TRACED0-1)
0x3: trace pins assigned for synchronous mode with a port width of 2 ((TRACECK,
TRACED0-3)
Bit 5 TRACE_EN: trace port and clock enable.
This bit enables the trace port clock, TRACECK.
0: disabled
1: enabled
Bit 4 TRACE_IOEN: trace pin enable
0: disabled - trace pins not assigned
1: enabled - trace pins assigned according to the value of TRACE_MODE field
Bit 3 Reserved, must be kept at reset value.
Bit 2 DBG_STANDBY: Allows debug in Standby mode
0: normal operation.
All clocks are disabled and the core powered down automatically in Standby mode.
1: automatic clock stop/power down disabled
All active clocks and oscillators continue to run during Standby mode, and the core supply is
maintained, allowing full debug capability. On exit from Standby mode, a system reset is
performed.
Bit 1 DBG_STOP: Allows debug in Stop mode
0: normal operation.
All clocks are disabled automatically in Stop mode.
1: automatic clock stop disabled
All active clocks and oscillators continue to run during Stop mode, allowing full debug
capability. On exit from Stop mode, the clock settings are set to the Stop mode exit state.
Bit 0 Reserved, must be kept at reset value.

RM0438 Rev 8 2145/2187
RM0438 Debug support (DBG)
2149
DBGMCU APB1 freeze register 1 (DBGMCU_APB1FZR1)
Address offset: 0x08
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
DBG_LPTIM1_STOP
Res. Res. Res. Res. Res. Res. Res.
DBG_I2C3_STOP
DBG_I2C2_STOP
DBG_I2C1_STOP
Res. Res. Res. Res. Res.
rw rw rw rw
1 51 4 1 3 1 2 1 1 1 0 9 8765 4321 0
Res. Res. Res.
DBG_IWDG_STOP
DBG_WWDG_STOP
DBG_RTC_STOP
Res. Res. Res. Res.
DBG_TIM7_STOP
DBG_TIM6_STOP
DBG_TIM5_STOP
DBG_TIM4_STOP
DBG_TIM3_STOP
DBG_TIM2_STOP
rw rw rw rw rw rw rw rw rw
Bit 31 DBG_LPTIM1_STOP: LPTIM1 stop in debug
0: normal operation. LPTIM1 continues to operate while CPU is in debug mode.
1: stop in debug. LPTIM1 is frozen while CPU is in debug mode.
Bits 30:24 Reserved, must be kept at reset value.
Bit 23 DBG_I2C3_STOP: I2C3 SMBUS timeout stop in debug
0: normal operation. I2C3 SMBUS timeout continues to operate while CPU is in debug mode.
1: stop in debug. I2C3 SMBUS timeout is frozen while CPU is in debug mode.
Bit 22 DBG_I2C2_STOP: I2C2 SMBUS timeout stop in debug
0: normal operation. I2C2 SMBUS timeout continues to operate while CPU is in debug mode.
1: stop in debug. I2C2 SMBUS timeout is frozen while CPU is in debug mode.
Bit 21 DBG_I2C1_STOP: I2C1 SMBUS timeout stop in debug
0: normal operation. I2C1 SMBUS timeout continues to operate while CPU is in debug mode.
1: stop in debug. I2C1 SMBUS timeout is frozen while CPU is in debug mode.
Bits 20:13 Reserved, must be kept at reset value.
Bit 12 DBG_IWDG_STOP: IWDG stop in debug
0: normal operation. IWDG continues to operate while CPU is in debug mode.
1: stop in debug. IWDG is frozen while CPU is in debug mode.
Bit 11 DBG_WWDG_STOP: WWDG stop in debug
0: normal operation. WWDG continues to operate while CPU is in debug mode.
1: stop in debug. WWDG is frozen while CPU is in debug mode.
Bit 10 DBG_RTC_STOP: RTC stop in debug
0: normal operation. RTC continues to operate while CPU is in debug mode.
1: stop in debug. RTC is frozen while CPU is in debug mode.
Bits 9:6 Reserved, must be kept at reset value.

Debug support (DBG) RM0438
2146/2187 RM0438 Rev 8
DBGMCU APB1 freeze register 2 (DGBMCU_APB1FZR2)
Address offset: 0x0C
Reset value: 0x0000 0000
Bit 5 DBG_TIM7_STOP: TIM7 stop in debug
0: normal operation. TIM7 continues to operate while CPU is in debug mode.
1: stop in debug. TIM7 is frozen while CPU is in debug mode.
Bit 4 DBG_TIM6_STOP: TIM6 stop in debug
0: normal operation. TIM6 continues to operate while CPU is in debug mode.
1: stop in debug. TIM6 is frozen while CPU is in debug mode.
Bit 3 DBG_TIM5_STOP: TIM5 stop in debug
0: normal operation. TIM5 continues to operate while CPU is in debug mode.
1: Stop in debug. TIM5 is frozen while CPU is in debug mode.
Bit 2 DBG_TIM4_STOP: TIM4 stop in debug
0: normal operation. TIM4 continues to operate while CPU is in debug mode.
1: stop in debug. TIM4 is frozen while CPU is in debug mode.
Bit 1 DBG_TIM3_STOP: TIM3 stop in debug
0: normal operation. TIM3 continues to operate while CPU is in debug mode.
1: stop in debug. TIM3 is frozen while CPU is in debug mode.
Bit 0 DBG_TIM2_STOP: TIM2 stop in debug
0: normal operation. TIM2 continues to operate while CPU is in debug mode.
1: stop in debug. TIM2 is frozen while CPU is in debug mode.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res.
DBG_LPTIM3_STOP
DBG_LPTIM2_STOP
Res. Res. Res.
DBG_I2C4_STOP
Res.
rw rw rw
Bits 31:7 Reserved, must be kept at reset value.
Bit 6 DBG_LPTIM3_STOP: LPTIM3 stop in debug
0: normal operation. LPTIM2 continues to operate while CPU is in debug mode.
1: stop in debug. LPTIM2 is frozen while CPU is in debug mode.
Bit 5 DBG_LPTIM2_STOP: LPTIM2 stop in debug
0: normal operation. LPTIM2 continues to operate while CPU is in debug mode.
1: stop in debug. LPTIM2 is frozen while CPU is in debug mode.

RM0438 Rev 8 2147/2187
RM0438 Debug support (DBG)
2149
DBGMCU APB2 peripheral freeze register (DBGMCU_APB2FZR)
Address offset: 0x10
Reset value: 0x0000 0000
Bits 4:2 Reserved, must be kept at reset value.
Bit 1 DBG_I2C4_STOP: I2C4 stop in debug
0: normal operation. I2C4 continues to operate while CPU is in debug mode.
1: stop in debug. I2C4 is frozen while CPU is in debug mode.
Bit 0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res.
DBG_TIM17_STOP
DBG_TIM16_STOP
DBG_TIM15_STOP
rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res.
DBG_TIM8_STOP
Res.
DBG_TIM1_STOP
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res.
rw rw
Bits 31:19 Reserved, must be kept at reset value.
Bit 18 DBG_TIM17_STOP: TIM17 stop in debug
0: normal operation. TIM17 continues to operate while CPU is in debug mode.
1: stop in debug. TIM17 is frozen while CPU is in debug mode.
Bit 17 DBG_TIM16_STOP: TIM16 stop in debug
0: normal operation. TIM16 continues to operate while CPU is in debug mode.
1: stop in debug. TIM16 is frozen while CPU is in debug mode.
Bit 16 DBG_TIM15_STOP: TIM15 stop in debug
0: normal operation. TIM15 continues to operate while CPU is in debug mode.
1: stop in debug. TIM15 is frozen while CPU is in debug mode.
Bits 15:14 Reserved, must be kept at reset value.
Bit 13 DBG_TIM8_STOP: TIM8 stop in debug
0: normal operation. TIM8 continues to operate while CPU is in debug mode.
1: stop in debug. TIM8 is frozen while CPU is in debug mode.
Bit 12 Reserved, must be kept at reset value.
Bit 11 DBG_TIM1_STOP: TIM1 stop in debug
0: normal operation. TIM1 continues to operate while CPU is in debug mode.
1: stop in debug. TIM1 is frozen while CPU is in debug mode.
Bits 10:0 Reserved, must be kept at reset value.

Debug support (DBG) RM0438
2148/2187 RM0438 Rev 8
52.11.2 DBGMCU register map
Refer to Section 2.3 for register boundary addresses.
[Table 468](../tables/table_468.md). DBGMCU register map and reset values
Offset Register name
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
DBGMCU_IDCODE REV_ID[15:0]
Res.
Res.
Res.
Res.
DEV_ID[11:0]
R e s e t  v a l u e 0010000000000001 010001110010
0x04
DBGMCU_CR
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
TRACE_MODE[1:0]
TRACE_EN
TRACE_IOEN
Res.
DBG_STANDBY
DBG_STOP
Res.
Reset value 0000 00
0x08
DBGMCU_
APB1FZR1
DBG_LPTIM1_STOP
Res.
Res.
Res.
Res.
Res.
Res.
Res.
DBG_I2C3_STOP
DBG_I2C2_STOP
DBG_I2C1_STOP
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
DBG_IWDG_STOP
DBG_WWDG_STOP
DBG_RTC_STOP
Res.
Res.
Res.
Res.
DBG_TIM7_STOP
DBG_TIM6_STOP
DBG_TIM5_STOP
DBG_TIM4_STOP
DBG_TIM3_STOP
DBG_TIM2_STOP
R e s e t  v a l u e 0 000 000 000000
0x0C
DBGMCU_
APB1FZR2
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
DBG_LPTIM3_STOP
DBG_LPTIM2_STOP
Res.
Res.
Res.
DBG_I2C4_STOP
Res.
Reset value 00 0
0x10
DBGMCU_
APB2FZR
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
DBG_TIM17_STOP
DBG_TIM16_STOP
DBG_TIM15_STOP
Res.
Res.
DBG_TIM8_STOP
Res.
DBG_TIM1_STOP
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
Reset value 0 0 0 0 0

RM0438 Rev 8 2149/2187
RM0438 Debug support (DBG)
2149
52.12 References
1. IHI 0031C (ID080813) - Arm ® Debug Interface Architecture Specification ADIv5.0 to
ADIv5.2, Issue C, 8th Aug 2013
2. DDI 0480F (ID100313) - Arm ® CoreSight™ SoC-400 r3p2 Technical Reference
Manual, Issue G, 16th March 2015
3. DDI 0314H - Arm ® CoreSight™ Components Technical Reference Manual, Issue H, 10
July, 2009
4. DDI 0553A (ID092917) - Arm ® v8-M Architecture Reference Manual, Issue A.f, 29
September 2017
5. 100230_0002_00_en - Arm ® Cortex®-M33 Processor r0p2 Technical Reference
Manual, Issue 0002-00, 10 May 2017
6. 100232_0001_00_en - Arm ® CoreSight™ ETM-M33 r0p1 Technical Reference
Manual, Issue 0001-00, 3 February 2017
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 566: Architectural Diagram](../figures/figure_566.md)
* [Figure 567: Architectural Diagram](../figures/figure_567.md)
* [Figure 568: Architectural Diagram](../figures/figure_568.md)
* [Figure 569: Architectural Diagram](../figures/figure_569.md)
* [Figure 570: Architectural Diagram](../figures/figure_570.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 446: Configuration Matrix](../tables/table_446.md)
* [Table 447: Configuration Matrix](../tables/table_447.md)
* [Table 448: Configuration Matrix](../tables/table_448.md)
* [Table 449: Configuration Matrix](../tables/table_449.md)
* [Table 450: Configuration Matrix](../tables/table_450.md)
* [Table 451: Configuration Matrix](../tables/table_451.md)
* [Table 452: Configuration Matrix](../tables/table_452.md)
* [Table 453: Configuration Matrix](../tables/table_453.md)
* [Table 454: Configuration Matrix](../tables/table_454.md)
* [Table 455: Configuration Matrix](../tables/table_455.md)
* [Table 456: Configuration Matrix](../tables/table_456.md)
* [Table 457: Configuration Matrix](../tables/table_457.md)
* [Table 458: Configuration Matrix](../tables/table_458.md)
* [Table 459: Configuration Matrix](../tables/table_459.md)
* [Table 460: Configuration Matrix](../tables/table_460.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)