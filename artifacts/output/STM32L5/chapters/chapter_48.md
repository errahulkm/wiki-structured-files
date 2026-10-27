# Chapter 48: Secure digital input/output MultiMediaCard interface (SDMMC)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 48: Secure digital input/output MultiMediaCard interface (SDMMC).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 1791 - 1868
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [SDMMC Interface](../peripherals/sdmmc.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 1791/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
48 Secure digital input/outpu t MultiMediaCard interface
(SDMMC)
48.1 SDMMC main features
The SD/SDIO, embedded MultiMediaCard (e•MMC) host interface (SDMMC) provides an
interface between the AHB bus and SD memory cards, SDIO cards and e•MMC devices.
The MultiMediaCard system specifications are available through the MultiMediaCard
Association website at www.jedec.org, published by the MMCA technical committee.
SD memory card and SD I/O card system specifications are available through the SD card
Association website at www.sdcard.org.
The SDMMC features include the following:
• Compliance with Embedded MultiMediaCard System Specification Version 4.51.
Card support for three different databus modes: 1-bit (default), 4-bit and 8-bit.
• Full compatibility with previous versions of MultiMediaCards (backward compatibility).
• Full compliance with SD memory card specifications version 4.1.
(SPI mode and UHS-II mode not supported).
• Full compliance with SDIO card specification version 4.0.
Card support for two different databus modes: 1-bit (default) and 4-bit.
(SPI mode and UHS-II mode not supported).
• Data transfer up to 104 Mbyte/s for the 8-bit mode.
(depending maximum allowed I/O speed).
• Data and command output enable signals to control external bidirectional drivers.
The MultiMediaCard/SD bus connects cards to the host.
The current version of the SDMMC supports only one SD/SDIO/e•MMC card at any one
time and a stack of e•MMC.
48.2 SDMMC bus topology
Communication over the bus is based on command/response and data transfers.
The basic transaction on the SD/SDIO/e•MMC bus is the command/response transaction.
These types of bus transaction transfer their information directly within the command or
response structure. In addition, some operations have a data token.
Data transfers are done in the following ways:
• Block mode: data block(s) with block size 2N bytes with N in the range 0-14
• SDIO multibyte mode: single data block with block size range 1-512 bytes
• e•MMC Stream mode: continuous data stream
Data transfers to/from e•MMC cards are done in data blocks or streams.

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1792/2187 RM0438 Rev 8
[Figure 510](../figures/figure_510.md). SDMMC “no response” and “no data” operations
[Figure 511](../figures/figure_511.md). SDMMC (multiple) block read operation
Note: The Stop Transmission command is not required at the end of a e •MMC multiple block read
with predefined block count.
[Figure 512](../figures/figure_512.md). SDMMC (multiple) block write operation
Note: The Stop Transmission command is not required at the end of an e•MMC multiple block
write with predefined block count.
The SDMMC does not send any data as long as the Busy signal is asserted (SDMMC_D0
pulled low).
MSv40124V1
SDMMC_CMD CMD Response
SDMMC_D
CMD
Operation no response and no data Operation response no data
From host to card
From card to host
MSv40155V1
SDMMC_CMD CMD Response
SDMMC_D
CMD
Block read operation
Multiple block read operation
From host to card
From card to host
Response
Data block CRC Data block CRC Data block CRC
Data stop operation
MSv40156V1
SDMMC_CMD CMD Response
SDMMC_D
CMD
Block write operation
Multiple block write operation
From host to card
From card to host
Response
Data block CRC CRC
status
Data stop operation
Busy Data block CRC CRC
status Busy

RM0438 Rev 8 1793/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
[Figure 513](../figures/figure_513.md). SDMMC (sequential) stream read operation
[Figure 514](../figures/figure_514.md). SDMMC (sequential) stream write operation
Stream data transfer operates only in a 1-bit wide bit bus configuration on SDMMC_D0 in
single data rate modes (DS, HS, and SDR).
48.3 SDMMC operation modes
MSv40157V2
SDMMC_CMD Response
SDMMC_D
CMD
Stream read operation
From host to card
From card to host
Data stream
Data stop operation
ResponseCMD
MSv40158V2
SDMMC_CMD Response
SDMMC_D
CMD
Stream write operation
From host to card
From card to host
Response
Data stream
Data stop operation
Busy
CMD
[Table 383](../tables/table_383.md). SDMMC operation modes SD and SDIO
SDIO bus speed modes(1)(2)
1. SDR single data rate signaling.
2. DDR double data rate signaling (data is sampled on both SDMMC_CK clock edges).
Max bus speed (3)
[Mbyte/s]
3. SDIO bus speed with 4-bit bus width.
Max clock frequency
[MHz](4)
4. Maximum frequency depending on maximum allowed I/O speed.
Signal voltage
[V]
DS (default speed) 12.5 25 3.3
HS (high speed) 25 50 3.3
SDR12 12.5 25 1.8
SDR25 25 50 1.8
DDR50 50 50 1.8
SDR50 50 100 1.8

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1794/2187 RM0438 Rev 8
48.4 SDMMC functional description
The SDMMC consists of three parts:
• The AHB slave interface accesses the SDMMC adapter registers, and generates
interrupt signals and IDMA control signals.
• The SDMMC adapter block provides all functions specific to the e•MMC/SD/SD I/O
card such as the clock generation unit, command and data transfer.
• The internal DMA (IDMA) block with its AHB master interface.
48.4.1 SDMMC block diagram
[Figure 515](../figures/figure_515.md) shows the SDMMC block diagram.
[Figure 515](../figures/figure_515.md). SDMMC block diagram
[Table 384](../tables/table_384.md). SDMMC operation modes e•MMC
e•MMC bus speed modes (1)(2)
1. SDR single data rate signaling.
2. DDR double data rate signaling. (data is  sampled on both SDMMC_CK clock edges).
Max bus speed (3)
[Mbyte/s]
3. e•MMC bus speed with 8-bit bus width.
Max clock frequency
[MHz](4)
4. Maximum frequency depending on maximum allowed I/O speed.
Signal voltage
[V](5)
5. Supported signal voltage level depends on I/O port characteristics, refer to device datasheet.
Legacy compatible 26 26 3/1.8/1.2V
High speed SDR 52 52 3/1.8/1.2V
High speed DDR 104 52 3/1.8/1.2V
MSv41696V4
SDMMC
AHB INTERFACE
SDMMC ADAPTER
Registers
FIFO
Control
unit
Command
path
Response
path
Data transmit
path
Data receive
path
CLK
MUX
IDMA
sdmmc_io_in_ck
SDMMC_CK
SDMMC_D[7:0]
SDMMC_D0DIR
SDMMC_D123DIR
SDMMC_CMD
SDMMC_CDIR
sdmmc_it
32-bit AHB
slave bus
sdmmc_hclk
sdmmc_ker_ck
32-bit AHB
master bus
SDMMC_CKIN
8

RM0438 Rev 8 1795/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
48.4.2 SDMMC pins and internal signals
[Table 385](../tables/table_385.md) lists the SDMMC internal input/output signals, [Table 386](../tables/table_386.md) the SDMMC pins
(alternate functions).
48.4.3 General description
The SDMMC_D[7:0] lines have different operating modes:
• By default, SDMMC_D0 line is used for data transfer. After initialization, the host can
change the databus width.
• For an e•MMC, 1-bit (SDMMC_D0), 4-bit (SDMMC_D[3:0]) or 8-bit (SDMMC_D[7:0])
data bus widths can be used.
• For an SD or an SDIO card, 1-bit (SDMMC_D0) or 4-bit (SDMMC_D[3:0]) can be used.
All data lines operate in push-pull mode.
To allow the connection of an external driver (a voltage switch transceiver), the direction of
data flow on the data lines is indicated with I/O direction signals. The SDMMC_D0DIR signal
indicates the I/O direction for the SDMMC_D0 data line, the SDMMC_D123DIR for the
SDMMC_D[3:1] data lines.
SDMMC_CMD only operates in push-pull mode:
[Table 385](../tables/table_385.md). SDMMC internal input/output signals
Signal name Signal type Description
sdmmc_ker_ck Digital input SDMMC kernel clock
sdmmc_hclk Digital input AHB clock
sdmmc_it Digital output SDMMC global interrupt
sdmmc_io_in_ck Digital input
SD/SDIO/e•MMC card feedback clock. This signal is
internally connected to the SDMMC_CK pin (for DS
and HS modes).
[Table 386](../tables/table_386.md). SDMMC pins
Pin name Pin type Description
SDMMC_CK Digital output Clock to SD/SDIO/ e•MMC card
SDMMC_CKIN Digital input Clock feedback from an external driver for SD/SDIO/e•MMC
card. (for SDR12, SDR25, SDR50, DDR50)
SDMMC_CMD Digital
input/output SD/SDIO/e•MMC card bidirectional command/response signal.
SDMMC_CDIR Digital output SD/SDIO/e•MMC card I/O direction indication for the
SDMMC_CMD signal.
SDMMC_D[7:0] Digital
input/output SD/SDIO/e•MMC card bidirectional data lines.
SDMMC_D0DIR Digital output SD/SDIO/e•MMC card I/O direction indication for the
SDMMC_D0 data line.
SDMMC_D123DIR Digital output SD/SDIO/e•MMC card I/O direction indication for the data lines
SDMMC_D[3:1].

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1796/2187 RM0438 Rev 8
To allow the connection of an external driver (a voltage switch transceiver), the direction of
data flow on the SDMMC_CMD line is indicated with the I/O direction signal SDMMC_CDIR.
SDMMC_CK clock to the card originates from sdmmc_ker_ck:
• When the sdmmc_ker_ck clock has 50 % duty cycle, it can be used even in bypass
mode (CLKDIV = 0).
• When the sdmmc_ker_ck duty cycle is not 50 %, the CLKDIV must be used to divide it
by 2 or more (CLKDIV > 0).
• The phase relation between the SDMMC_CMD / SDMMC_D[7:0] outputs and the
SDMMC_CK can be selected through the NEGEDGE bit. The phase relation depends
on the CLKDIV, NEGEDGE, and DDR settings. See [Figure 516](../figures/figure_516.md).
[Figure 516](../figures/figure_516.md). SDMMC Command and data phase relation
By default, the sdmmc_io_in_ck feedback clock input is selected for sampling incoming
data in the SDMMC receive path. It is derived from the SDMMC_CK pin.
When using an external driver (a voltage switch transceiver), the SDMMC_CKIN feedback
clock input can be selected to sample the receive data.
For an SD/SDIO/e•MMC card, the clock frequency can vary between 0 and 208 MHz
(limited by maximum I/O speed).
MSv40159V2
SDMMC_CMD
SDMMC_Dn
SDMMC_CK
sdmmc_ker_ck
CLKDIV = 0
CLKDIV > 0
DDR = 0
NEGEDGE = 0
CLKDIV > 0
DDR = 0
NEGEDGE = 1
CLKDIV > 0
DDR = 1
NEGEDGE = 0
CLKDIV > 0
DDR = 1
NEGEDGE = 1
[Table 387](../tables/table_387.md). SDMMC Command and data phase selection
CLKDIV
DDR
NEGEDGE
SDMMC_CK Command out Data out
0xx =
sdmmc_ker_ck Generated on sdmmc_ker_ck falling edge
>0
0
0
Generated on
sdmmc_ker_ck
rising edge
Generated on sdmmc_ker_ck falling edge succeeding the SDMMC_CK rising
edge.
1 Generated on the same sdmmc_ker_ck rising edge that generates the
SDMMC_CK falling edge.
1
0 Generated on sdmmc_ker_ck falling edge
succeeding the SDMMC_CK rising edge. Generated on
sdmmc_ker_ck falling edge
succeeding a SDMMC_CK
edge.1
Generated on the same sdmmc_ker_ck rising
edge that generates the SDMMC_CK falling
edge.

RM0438 Rev 8 1797/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
Depending on the selected bus mode (SDR or DDR), one bit or two bits are transferred on
SDMMC_D[7:0] lines with each clock cycle. The SDMMC_CMD line transfers only one bit
per clock cycle.
48.4.4 SDMMC adapter
The SDMMC adapter (see [Figure 515](../figures/figure_515.md): SDMMC block diagram) is a multimedia/secure
digital memory card bus master that provides an interface to a MultiMediaCard stack or to a
secure digital memory card. It consists of the following subunits:
• Control unit
• Data transmit path
• Command path
• Data receive path
• Response path
• Receive data path clock multiplexer
• Adapter register block
• Data FIFO
• Internal DMA (IDMA)
Note: The adapter registers and FIFO use the AH B clock domain (sdmmc_hclk). The control unit,
command path and data transmit path use the SDMMC adapter clock domain
(sdmmc_ker_ck). The response path and data receive path use the SDMMC adapter
feedback clock domain from the sdmmc_io_in_ck, or SDMMC_CKIN.
Adapter register block
The adapter register block contains all system control registers, the SDMMC command and
response registers and the data FIFO.
This block also generates the signals from the corresponding bit location in the SDMMC
Clear register that clear the static flags in the SDMMC adapter.
Control unit
The control unit illustrated in [Figure 517](../figures/figure_517.md), contains the power management functions, the
SDMMC_CK clock management with divider, and the I/O direction management.

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1798/2187 RM0438 Rev 8
[Figure 517](../figures/figure_517.md). Control unit
The power management subunit disables the card bus output signals during the power-off
and power-up phases.
There are three power phases:
• power-off
• power-up
• power-on
The clock management subunit uses the sdmmc_ker_ck to generate the SDMMC_CK and
provides the division control. It also takes care of stopping the SDMMC_CK for flow control,
for example.
The clock outputs are inactive:
• after reset
• during the power-off or power-up phases
• if the power saving mode (register bit PWRSAV) is enabled and the card bus is in the
Idle state for eight clock periods. The clock is stopped eight cycles after both the
command/response CPSM and data path DPSM subunits have enter the Idle phase.
The clock is restarted when the command/response CPSM or data path DPSM is
activated (enabled).
The I/O management subunit takes care of the SDMMC_Dn and SDMMC_CMD I/O
direction signals, which controls the external voltage transceiver.
Command/response path
The command/response path subunit transfers commands and responses on the
SDMMC_CMD line. The command path is clocked on the SDMMC_CK and sends
commands to the card,. The response path is clocked on the sdmmc_rx_ck and receives
responses from the card.
MSv39278V2
Control unit
sdmmc_ker_ck
SDMMC_CK
SDMMC_CDIR
SDMMC_D0DIR
SDMMC_D123DIR
To command/response and data paths
Power
management
IO
management
Clock
management
Registers

RM0438 Rev 8 1799/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
[Figure 518](../figures/figure_518.md). Command/response path
Command/response path state machine (CPSM):
• When the command register is written to and the enable bit is set, command transfer
starts. When the command has been sent the CRC is appended and the command
path state machine (CPSM) sets the status flags and:
– if a response is not required enters the Idle state.
– If a response is required, it waits for the response.
• When the response is received,
– for a response with CRC, the received CRC code and the internally generated
code are compared, and the appropriate status flag is set according the result.
– for a response without CRC, no CRC is che cked, and the appropriate status flag is
not set.
When ever the CPSM is active (not in the Idle state), the CPSMACT bit is set.
MSv40160V2
Command / Response
path
SDMMC_CK
Registers Status
flag
Command
timer
Control
logic
Response
shift
register
CRC
Response
registers
Command
registers
Command
shift
register
CRC out
sdmmc_rx_ck
SDMMC_CMD
To control unit
in

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1800/2187 RM0438 Rev 8
[Figure 519](../figures/figure_519.md). Command path state machine (CPSM)
• Idle: The command path is inactive. When the command control register is written and
the enable bit (CPSMEN) is set, the CPSM activates the SDMMC_CK clock (when
stopped due to power save PWRSAV bit) and moves
– to the Send state when WAITPEND = 0 and BOOTEN = 0.
– to the Pending state when WAITPEND = 1.
– to the Boot state when BOOTEN = 1.
• Send: The command is sent and the CRC is appended.
– When CMDTRANS bit is set or when BOOTEN bit is set and BOOTMODE is
alternative boot, and the DTDIR = receive, the CPSM DataEnable signal is issued
to the DPSM at the end of the command.
– When the CMDTRANS bit is set and th e CMDSUSPEND bit is 0 the interrupt
period is terminated at the end of the command.
– When CMDSTOP bit is set the CPSM Abor t signal is issued to the DPSM at the
end of the command.
– If no response is expected (WAITRESP = 00) the CPSM moves to the Idle state
and the CMDSENT flag is set. When BOOTMODE = 1 and BOOTEN = 0 the
CMDSENT flag is delayed 56 cycles after the command end bit, otherwise the
MSv40161V1
Receive
Wait
Pending
DPSM send CMD
or
WAITPEND = 0
SDMMC_CMD write
and
CPSMEN = 1
and
BOOTEN = 1
SDMMC_CMD write
and
CPSMEN = 1
and
WAITPEND = 0
and
BOOTEN = 0
and
SDMMC_CMD write
and
CPSMEN = 1
and
WAITPEND = 1
Boot
BOOTMODE = 0
and
BOOTEN = 1
Idle
Send
End of CMD
and
WAITRESP = 00
Start bit detected
End of response
or
CRC status error
Reset
BOOTMODE = 1
End of CMD
and
WAITRESP = not 00
BOOTMODE = 0
and
BOOTEN = 0

RM0438 Rev 8 1801/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
CMDSENT flag is generated immediately after the command end bit.
The RESPCMDR and RESPxR registers are not modified.
– If a command response is expected (WAITRESP = not 00) the CPSM moves to
the Wait state and start the response timeout.
• Wait: The command path waits for a response.
– When WAITINT bit is 0 the command timer starts running and the CPSM waits for
a start bit.
a) If a start bit is detected before the ti meout the CPSM moves to the Receive state.
b) If the timeout is reached before the CP SM detect a response start bit, the timeout
flag (CTIMEOUT) is set and the CPSM moves to the Idle state.
The RESPCMDR and RESPxR registers are not modified.
– When WAITINT bit is 1, the timer is disa bled and the CPSM waits for an interrupt
request (response start bit) from one of the cards.
a) When a start bit is detected the CPSM moves to the Receive state.
b) When writing WAITINT to 0 (interrupt mo de abort), the host sends a response by
its self and on detecting the start bit the CPSM move to the Receive state.
• Receive: The command response is received. Depending the response mode bits
WAITRESP in the command control register, the response can be either short or long,
with CRC or without CRC. The received CRC code when present is verified against the
internally generated CRC code.
– When the CMDSUSPEND bit is  set and the SDIO Response bit BS = 0 (response
bit [39]), the interrupt period is started after the response.
When the CMDSUSPEND bit is cleared, or the CMDSUSPEND bit is 1 and the
SDIO Response bit BS = 1 (response bit [39]), there is no interrupt period started.
– When the CMDTRANS bit is set and th e CMDSUSPEND bit is set and the SDIO
Response bit DF= 1 (response bit [32]) the interrupt period is terminated after the
response.
– When the CRC status passes or no CRC is present the CMDREND flag is set, the
CPSM moves to the Idle state.
The RESPCMDR and RESPxR registers are updated with received response.
- When BOOTMODE = 1 and BOOTEN = 0 the CMDREND flag is delayed 56
cycles after the response end bit, otherwise the CMDREND flag is generated
immediately after the response end bit.
- When CMDTRANS bit is set and the DTDIR = transmit, the CPSM DataEnable
signal is issued to the DPSM at the end of the command response.
– When the CRC status fails the CCRCFAIL fl ag is set and the CPSM moves to the
Idle state.
The RESPCMDR and RESPxR registers are updated with received response.
• Pending: According the pending WAITPEND bit in the command register, the CPSM
enters the pending state.
– When DATALENGTH ≤ 5 bytes the CPSM moves to the Sent state and generates
the DataEnable signal to start the data transfer aligned with the CMD12 Stop
Transmission command.
– When DATALENGTH > 5 bytes, the CPSM DataEnable signal is issued to the
DPSM to start the data transfer. The CPSM waits for a send CMD signal from the

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1802/2187 RM0438 Rev 8
DPSM before moving to the Send state. This enables, for example, the CMD12
Stop Transmission command to be sent aligned with the data.
– When writing WAITPEND to 0, th e CPSM moves to the Send state.
• Boot: If the BOOTEN bit is set in the command register, the CPSM enters the Boot
state, and when:
– BOOTMODE = 0 the SDMMC_CMD line is driven low and when CMDTRANS bit
is set and the DTDIR = receive, the CPSM DataEnable signal is issued to the
DPSM. This enables normal boot operation. This state is left at the end of the boot
procedure by clearing the register bit BOOTEN, which cause the SDMMC_CMD
line to be driven high and the CPSM Abort signal is issued to the DPSM, before
moving to the Idle state. The CMDSENT flag is generated 56 cycles after
SDMMC_CMD line is high.
– BOOTMODE = 1, move to the Send stat e. This enables sending of the CMD0
(boot). Clearing BOOTEN has no effect.
Note: The CPSM remains in the Id le state for at least eight SDMMC_CK periods to meet the NCC
and NRC timing constraints. NCC is the minimum delay between two host commands, and
NRC is the minimum delay between the host command and the card response.
The response timeout has a fixed value of 64 SDMMC_CK clock periods.
A command is a token that starts an operation. Commands are sent from the host to either a
single card (addressed command) or all connected cards (broadcast command are
available for e•MMC V3.31 or previous). Commands are transferred serially on the
SDMMC_CMD line. All commands have a fixed length of 48 bits. The general format for a
command token for SD-Memory cards, SDIO cards, and e•MMC cards is shown in [Table 388](../tables/table_388.md).
The command token data is taken from two registers, one containing a 32-bit argument and
the other containing the 6-bit command index (six bits sent to a card).
Next to the command data there are command type (WAITRESP) bits controlling the
command path state machine (CPSM). These bits also determine whether the command
requires a response, and whether the response is short (48 bit) or long (136 bits) long, and if
a CRC is present or not.
A response is a token that is sent from an addressed card or synchronously from all
connected cards to the host as an answer to a previous received command. All responses
are sent via the command line SDMMC_CMD. The response transmission always starts
with the left bit of the bit string corresponding to the response code word. The code length
depends on the response type. Response tokens R1, R2, R3, R4, R5, and R6 have various
[Table 388](../tables/table_388.md). Command token format
Bit position Width Value Description
47 1 0 Start bit
46 1 1 Transmission bit
[45:40] 6 x Command index
[39:8] 32 x Argument
[7:1] 7 x CRC7
0 1 1 End bit

RM0438 Rev 8 1803/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
coding schemes, depending on their content. The general formats for the response tokens
for SD-Memory cards, SDIO cards, and e•MMC cards are shown in [Table 389](../tables/table_389.md), [Table 390](../tables/table_390.md)
and [Table 391](../tables/table_391.md).
A response always starts with a start bit (always 0), followed by the bit indicating the
direction of transmission (card = 0). A value denoted by x in the tables below indicates a
variable entry. Most responses, except some, are protected by a CRC. Every command
code word is terminated by the end bit (always 1).
The response token data is stored in five registers, four containing the 32-bits card status,
OCR register, argument or 127-bits CID or CSD register including internal CRC, and one
register containing the 6-bits command index.
The command/response path operates in a half-duplex mode, so that either commands can
be sent or responses can be received. If the CPSM is not in the Send state, the
[Table 389](../tables/table_389.md). Short response with CRC token format
Bit position Width Value Description
47 1 0 Start bit
46 1 0 Transmission bit
[45:40] 6 x Command index (or reserved 111111)
[39:8] 32 x Argument
[7:1] 7 x CRC7
0 1 1 End bit
[Table 390](../tables/table_390.md). Short response without CRC token format
Bit position Width Value Description
47 1 0 Start bit
46 1 0 Transmission bit
[45:40] 6 x Command index (or reserved 111111)
[39:8] 32 x Argument
[7:1] 7 1111111 (reserved 1111111)
0 1 1 End bit
[Table 391](../tables/table_391.md). Long response with CRC token format
Bit position Width Value Description
135 1 0 Start bit
134 1 0 Transmission bit
[133:128] 6 111111 Reserved
[127:1]
127:8 x CID or CSD slices
7:1 x CRC7 (included in CID or CSD)
0 1 1 End bit

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1804/2187 RM0438 Rev 8
SDMMC_CMD output is in the Hi-Z state. Data sent on SDMMC_CMD are synchronous
with the SDMMC_CK according the NEGEDGE register bit see [Figure 516](../figures/figure_516.md).
The command and short response with CRC, the CRC generator calculates the CRC
checksum for all 40 bits before the CRC code. This includes the start bit, transmission bit,
command index, and command argument (or card status).
For the long response the CRC checksum is calculated only over the 120 bits of R2 CID or
CSD. Note that the start bit, transmission bit and the six reserved bits are not used in the
CRC calculation.
The CRC checksum is a 7-bit value:
CRC[6:0] = remainder [(M(x) * x7) / G(x)]
G(x) = x7 + x3 + 1
M(x) = (first bit) * xn + (second bit) * xn-1+... + (last bit before CRC) * x0
Where n = 39 or 119.
The CPSM can send a number of specific commands to handle various operating modes
when CPSMEN is set, see [Table 392](../tables/table_392.md).
[Table 392](../tables/table_392.md). Specific Commands overview
VSWITCH
BOOTEN
BOOTMOD
CMDTRAN
WAITPEND
CMDSTOP
WAITINT
Description
1xxxxxx S t a r t  v o l t a g e  s w i t c h  s e q u e n c e
01xxxxx S t a r t  n o r m a l  boot
011xxxx S t a r t  a l t e r n a t i v e  b o o t
001xxxx S t o p  a l t e r n a t i v e  boot.
0001xxx S e n d  c o m m a n d  w i t h  a s s o c i a t e d  d a t a  t r a n s f e r .
000011x e•MMC stream data transfer, command
(STOP_TRANSMISSION) pending until end of data transfer.
000010x e•MMC stream data transfer, command different from
(STOP_TRANSMISSION) pending until end of data transfer.
000001x Send command (STOP_TRANSMISSION), stopping any
ongoing data transmission.
0000001 E n t e r  e•MMC wait interrupt (Wait-IRQ) mode.
0000000 A n y  o t h e r  n o n e  s p e c i f i c  c o m m a n d

RM0438 Rev 8 1805/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
The command/response path implements the status flags and associated clear bits shown
in [Table 393](../tables/table_393.md):
The command path error handling is shown in [Table 394](../tables/table_394.md):
Data path
The data path subunit transfers data on the SDMMC_D[7:0] lines to and from cards. The
data transmit path is clocked on the SDMMC_CK and sends data to the card. The data
receive path is clocked on the sdmmc_rx_ck and receives data from the card. [Figure 520](../figures/figure_520.md)
shows the data path block diagram.
[Table 393](../tables/table_393.md). Command path status flags
Flag Description
CMDSENT Set at the end of the command without  response (CPSM moves from Send to Idle).
CMDREND Set at the end of the command response when the CRC is OK (CPSM moves from Receive to
Idle).
CCRCFAIL Set at the end of the command response when the CRC is FAIL (CPSM moves from Receive to
Idle).
CTIMEOUT Set after the command when no response start bit received before the timeout (CPSM moves
from Wait to Idle).
CKSTOP Set after the voltage switch (VSWITCHEN = 1) command response when the CRC is OK and the
SDMMC_CK is stopped (no impact on CPSM).
VSWEND Set after the voltage swit ch (VSWITCH = 1) timeout of 5 ms + 1 ms (no impact on CPSM).
CPSMACT Command transfer in progress (CPSM not in Idle state).
[Table 394](../tables/table_394.md). Command path error handling
Error CPSM state Cause Card action Host action CPSM action
Timeout Wait No start bit in
time Unknown Reset or cycle power
card(1) Move to Idle
CRC status Receive
Negative
status Command ignored Resend command (1)
Move to Idle
Transmission
error Command accepted Resend command (1)
1. When CMDTRANS is set, also a stop_transmission command must be send to move the DPSM to Idle.

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1806/2187 RM0438 Rev 8
[Figure 520](../figures/figure_520.md). Data path
The card data bus width can be programmed in the clock control register bits WIDBUS. The
supported data bus width modes are:
• If the wide bus mode is not enabled, only one bit is transferred over SDMMC_D0.
• If the 4-bit wide bus mode is enabled, data is transferred at four bits over
SDMMC_D[3:0].
• If the 8-bit wide bus mode is enabled, data is transferred at eight bits over
SDMMC_D[7:0].
Next to the data bus width the data sampling mode can be programmed in the clock control
register bit DDR. The supported data sampling modes are:
• Single data rate signaling (SDR), data is clocked on the rising edge of the clock.
• Double data rate signaling (DDR), data is clocked on the both edges of the clock. DDR
mode is only supported in wide bus mode (4-bit wide and 8-bit wide).
Note: The data sampling mode only applies to th e SDMMC_D[7:0] lines. (not applicable to the
SDMMC_CMD line.)
MSv40162V2
Data path
SDMMC_CK
Registers Status
flag
Data
timer
Control
logic
Odd CRC
FIFO
out
sdmmc_rx_ck
SDMMC_D[7:0]
To control unit
Odd receive
shift register
Even CRCEven receive
shift register
Odd transmit
shift register
Even transmit
shift register
Odd CRC
Even CRC
Mux
in

RM0438 Rev 8 1807/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
In DDR mode, data is sampled on both edges of the SDMMC_CK according the following
rules, see also [Figure 521](../figures/figure_521.md) and [Figure 522](../figures/figure_522.md):
• On the rising edge of the clock odd bytes are sampled.
• On the falling edge of the clock even bytes are sampled.
• Data payload size is always a multiple of 2 bytes.
• Two CRC16 are computed per data line
– Odd bits CRC16 clocked on the falling edge of the clock.
– Even bits CRC16 clocked on the rising edge of the clock.
• Start, end bits and idle conditions are full cycle.
• CRC status / boot acknowledgment and busy signaling are full cycle and are only
sampled on the rising edge of the clock.
In DDR mode, the SDMMC_CK clock division must be ≥ 2.
[Figure 521](../figures/figure_521.md). DDR mode data packet clocking
[Figure 522](../figures/figure_522.md). DDR mode CRC status / boot acknowledgment clocking
Data path state machine (DPSM)
Depending on the transfer direction (send or receive), the data path state machine (DPSM)
moves to the Wait_S or Wait_R state when it is enabled:
• Send: the DPSM moves to the Wait_S state. If there is data in the transmit FIFO, the
DPSM moves to the Send state, and the data path subunit starts sending data to a
card.
• Receive: the DPSM moves to the Wait_R state and waits for a start bit. When it
receives a start bit, the DPSM moves to the Receive state, and the data path subunit
starts receiving data from a card.
MSv40163V2
SDMMC_CK
b7
even
b7
odd
0
startSDMMC_D3 crc0
odd
crc0
even
CRC even
CRC odd
Data even
Data odd
b3
even
b3
odd
b7
even
b7
odd
b3
even
b3
odd
Byte 2 Byte 4
b7
even
b7
odd
b3
even
b3
odd
crc15
odd
crc15
even
crc14
odd
crc14
even
1
end
Byte n
b6
even
b6
odd
0
startSDMMC_D2 crc0
odd
crc0
even
b2
even
b2
odd
b6
even
b6
odd
b2
even
b2
odd
b6
even
b6
odd
b2
even
b2
odd
crc15
odd
crc15
even
crc14
odd
crc14
even
1
end
b5
even
b5
odd
0
startSDMMC_D1 crc0
odd
crc0
even
b1
even
b1
odd
b5
even
b5
odd
b1
even
b1
odd
b5
even
b5
odd
b1
even
b1
odd
crc15
odd
crc15
even
crc14
odd
crc14
even
1
end
b4
even
b4
odd
0
startSDMMC_D0 crc0
odd
crc0
even
b0
even
b0
odd
b4
even
b4
odd
b0
even
b0
odd
b4
even
b4
odd
b0
even
b0
odd
crc15
odd
crc15
even
crc14
odd
crc14
even
1
end
Byte 1 BYte 3 Byte n-1
Block length CRC
MSv40164V1
SDMMC_CK
CRC status / boot ack
SDMMC_D0 1
end
0
start

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1808/2187 RM0438 Rev 8
For boot operation with acknowledgment the DPSM moves to the Wait_Ack state and
waits for the boot acknowledgment before moving to the Wait_R state.
The DPSM operates at SDMMC_CK. The DPSM has the following states, as shown in
[Figure 523](../figures/figure_523.md). When ever the DPSM is active (not in the Idle state), the DPSMACT bit is set.
[Figure 523](../figures/figure_523.md). Data path state machine (DPSM)
• Idle state: the data path is inactive, and the SDMMC_D[7:0] outputs are according the
PWRCTRL setting. The DPSM is activated either by sending a command with
CMDTRANS bit set or by setting the DTEN bit, or by detecting Busy on SDMMC_D0
(that is, after a command with R1b response).
When not busy, the DPSM activates the SDMMC_CK clock (when stopped due to
power save PWRSAV bit), loads the data counter with a new (DATALENGTH) value
and:
– When the data direction bit (DTDIR) indicates send, moves to the Wait_S.
– When the data direction bit (DTDIR) indicates receive, moves to the
- Wait_R when BOOTACKEN register bit is clear.
- Wait_Ack when BOOTACKEN register bit is set and start the acknowledgment
timeout.
When busy the DPSM keeps the SDMMC_CK clock active and move to the Busy state.
MSv40189V1
reset
Idle Wait_Ack
R_W
Busy
Wait_S
Send
Wait_R
Receive
Not busy
&
(CRC status
FAIL
or
CPSM Abort)
(CPSM
DataEnable
or
write DTEN=1)
&
DTDIR=0
&
Not busy
Busy
End of data
DATACOUNT=0
or
DTHOLD=1
or
CPSM Abort
&
FIFO empty
(CRC status OK
Or
No CRC)
&
Not busy
End of packet
or
End of data
(DATACOUNT=
0)
or
CPSM Abort
TXFIFOE= not
0
&
DTHOLD=0
DATACOUNT=0
or
CPSM Abort
or
DTHOLD = 1
&
FIFO empty
DATACOUNT not 0
&
Start bit detected
(End of packet)
or
End of data
(DATACOUNT=0)
&
RWSTART=0
End of packet
&
DATACOUNT =
not 0
&
RWSTART=1
CPSM Abort
&
FIFO empty
RWSTOP=1
CPSM Abort
CPSM DataEnable
&
DTDIR=1
&
BOOTACKEN=1
Ack status OK
(CPSM DataEnable or
write DTEN=1)
&
DTDIR=1
&
BOOTACKEN=0
CPSM Abort
&
FIFO empty

RM0438 Rev 8 1809/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
Note: DTEN must not be used  to start data transfer with SD, SDIO and e•MMC cards.
• Wait_Ack state: the data path waits for the boot acknowledgment token.
– The DPSM moves to the Wait_R state if it receives an error free acknowledgment
before a timeout.
– When a pattern different from the acknowledgment is received an
acknowledgment status error is generated, and the ack fail status flag (ACKFAIL)
is set. The DPSM stays in Wait_Ack.
– If it reaches a timeout (ACKTIME) before it  detects a start bit, it sets the timeout
status flag (ACKTIMEOUT). The DPSM stays in Wait_Ack.
– When the CPSM Abort signal is set it moves to the Idle state and sets the
DABORT flag.
• Wait_R state: the data path, if the data counter is not zero and data is not hold, waits
for a start bit on SDMMC_D[n:0]. If the data counter is zero or data is hold, wait for the
FIFO to be empty.
– In block mode, if a start bit is received before a timeout the DPSM moves to the
Receive state and loads the data block counter with DBLOCKSIZE.
– In SDIO multibyte mode, if a start bit is received before a timeout the DPSM
moves to the Receive state and loads the data block counter with DATALENGTH.
– In stream mode, if a start bit is received  before a timeout the DPSM moves to the
Receive state and loads the data counter with DATALENGTH.
– if the data counter (DATACOUNT) equals zero (end of data) the DPSM moves to
the Idle state when the receive FIFO is empty and the DATAEND flag is set.
– If it reaches a timeout (DATATIME) before it  detects a start bit, it sets the timeout
status flag (DTIMEOUT) and the DPSM stays in the Wait_R state.
– If the CPSM Abort signal is set:
If DATACOUNT > 0, the DPSM moves to the Idle state when the FIFO is empty
and when IDMAEN = 0 reset with FIFORST, and sets the DABORT flag.
If DATACOUNT is zero normal operation is continued, there is no DABORT flag
since the transfer has completed normally.
– if the DTHOLD bit is set:
- When DATACOUNT > 0, the DPSM moves to the Idle state when the receive
FIFO is empty and when IDMAEN = 0 reset with FIFORST, and issues the DHOLD
flag. When holding the timeout is disabled. When an CPSM Abort signal is
received during holding, the transfer is aborted.

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1810/2187 RM0438 Rev 8
- When DATACOUNT = 0, the transfer is completed normally and there is no
DHOLD flag.
– When DPSM has been started with DTEN, after an error (DTIMEOUT) the DPSM
moves to the Idle state when the FIFO is empty and when IDMAEN = 0 reset with
FIFORST.
• R_W state: the data path Read Wait the bus.
– The DPSM moves to the Wait_R state when the Read Wait stop bit (RWSTOP) is
set, and start the receive timeout.
– If the CPSM Abort signal is set, wait for the FIFO to be empty and when
IDMAEN = 0 reset with FIFORST, then moves to the Idle state and sets the
DABORT flag.
• Receive state: the data path receives serial data from a card. Pack the data in bytes
and written it to the data FIFO. Depending on the transfer mode selected in the data
control register (DTMODE), the data transfer mode can be either block or stream:
– In block mode, when the data block size (DBLOCKSIZE) number of data bytes are
received, the DPSM waits until it receives the CRC code.
– In SDIO multibyte mode, when the data  block size (DATALENGTH) number of
data bytes are received, the DPSM waits until it receives the CRC code.
a) If the received CRC code matches the internally generated CRC code, the DPSM
moves to the
- R_W state when RWSTART = 1 and DATACOUNT > zero, the DBCKEND flag is
set.
- Wait_R state otherwise.
b) If the received CRC code fails the inte rnally generated CRC code any further data
reception is prevented.
- When not all data has been received (DATACOUNT > 0), the CRC fail status flag
(DCRCFAIL) is set and the DPSM stays in the Receive state.
- When all data has been received (DATACOUNT = 0), wait for the FIFO to be
empty after which the CRC fail status flag (DCRCFAIL) is set and the DPSM
moves to the Idle state.
– In stream mode, the DPSM receives data while the data counter
DATACOUNT > 0. When the counter is zero, the remaining data in the shift
register is written to the data FIFO, and the DPSM moves to the Wait_R state.
– When a FIFO overrun error occurs, the DPSM sets the FIFO overrun error flag
(RXOVERR) and any further data reception is prevented. The DPSM stays in the
Receive state.
– When an CPSM Abort signal is received:
- If the CPSM Abort signal is received before the 2 last bits of the data with
DATACOUNT = 0, the transfer is aborted. The remaining data in the shift register
is written to the data FIFO, wait for the FIFO to be empty and when IDMAEN = 0
reset with FIFORST, then the DPSM moves to the Idle state and the DABORT flag
is set.
- If the CPSM Abort signal is received during or after the 2 last bits of the transfer
with DATACOUNT = 0, the transfer is completed normally. The DPSM stays in the
Receive state no DABORT flag is generated.
– When DPSM has been started with DTEN , after an error (DCRCFAIL when
DATACOUNT > 0, or RXOVERR) the DPSM moves to the Idle state when the
FIFO is empty and when IDMAEN = 0 reset with FIFORST.

RM0438 Rev 8 1811/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
• Wait_S state: the data path waits for data to be available from the FIFO.
– If the data counter DATACOUNT > 0, waits until the data FIFO empty flag
(TXFIFOE) is de-asserted and DTHOLD is not set, and moves to the Send state.
– If the data counter (DATACOUNT) = 0 the DPSM moves to the Idle state.
- When DTHOLD is disabled, the DATAEND flag is set.
- When DTHOLD is enabled, the DHOLD flag is set.
– When DTHOLD is set and the DATACOUNT > 0
- When IDMA is enabled, the DBCKEND flag is set and subsequently the FIFO is
flushed, furthermore the DPSM moves to the Idle state and the DHOLD flag is set.
- When IDMA is disabled the DBCKEND flag is set. Wait for the FIFO to be reset
by software with FIFORST, then DPSM moves to the Idle state and issues the
DHOLD flag.
– When DTHOLD is set and DATACOUNT = 0 the transfer is completed normally.
– When receiving the CPSM Abort signal
- If the CPSM Abort signal is received before the 2 last bits of the data with
DATACOUNT = 0, the transfer is aborted, wait for the FIFO to be empty and when
IDMAEN = 0 reset with FIFORST, then the DPSM moves to the Idle state and sets
the DABORT flag.
- If the CPSM Abort signal is received during or after the 2 last bits of the transfer
with DATACOUNT = 0, normal operation is continued, there is no DABORT flag
since the transfer has completed normally.
Note: The DPSM remains in the Wait_S state for at least two clock periods to meet the N WR timing
requirements, where NWR is the number of clock cycles between the reception of the card
response and the start of the data transfer from the host.
• Send state: the DPSM starts sending data to a card. Depending on the transfer mode
bit in the data control register, the data transfer mode can be either block, SDIO
multibyte or stream:
– In block mode, when the data block size (DBLOCKSIZE) number of data bytes are
send, the DPSM sends an internally generated CRC code and end bit, and moves
to the Busy state and start the transmit timeout.
– In SDIO multibyte mode, when the data  block size (DATALENGTH) number of
data bytes are send, the DPSM sends an internally generated CRC code and end
bit, and moves to the Busy state and start the transmit timeout.
– In stream mode, the DPSM sends data to a card while the data counter
DATACOUNT > 0. When the data counter reaches zero moves to the Busy state
and start the transmit timeout.
Before sending the last stream byte according to DATACOUNT, the DPSM issues
a trigger on the send CMD signal. This signal is used by the CPSM to sent any
pending command (CMD12 Stop Transmission command).
– If a FIFO underrun error occurs, the DPSM sets the FIFO underrun error flag
(TXUNDERR). The DPSM stays in the Send state.
– When receiving the CPSM Abort signal
- If the CPSM Abort signal is received before the 2 last bits of the transfer with
DATACOUNT = 0, the transfer is aborted. The DPSM sends a last data bit
followed by an end bit. The FIFO is disabled/flushed, and the DPSM moves to the
Busy state to wait for not busy before setting the DABORT flag.
- If the CPSM Abort signal is received during or after the 2 last bits of the transfer

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1812/2187 RM0438 Rev 8
with DATACOUNT = 0, the transfer is completed normally, there is no DABORT
flag.
• Busy state: the DPSM waits for the CRC status token when expected, and wait for a
not busy signal:
– If a CRC status token is expected and in dicate “non-erroneous transmission” or
when there is no CRC expected:
- it moves to the Wait_S state when SDMMC_D0 is not low (the card is not busy).
- When the card is busy SDMMC_D0 is low it remains in the Busy state.
– If a CRC status token is expected and indicates “erroneous transmission”.
- When not all data has been send (DATACOUNT > 0). The DPSM waits for not
busy after which the CRC fail status flag (DCRCFAIL) is set. The FIFO is
disabled/flushed and the DPSM stays in the Busy state.
- When all data has been send (DATACOUNT = 0). The DPSM waits for not busy
after which the CRC fail status flag (DCRCFAIL) is set and the DPSM moves to
the Idle state.
– If a CRC status (Ncrc) timeout occurs while the DPSM is in the Busy state, it sets
the data timeout flag (DTIMEOUT) and stays in the Busy state.
– If a busy timeout occurs while the DPSM is in the Busy state, it sets the data
timeout flag (DTIMEOUT) and stays in the Busy state.
– When receiving the CPSM Abort signal in the Busy state:
- If the CPSM Abort signal is received before the 2 last bits of the CRC response
with DATACOUNT > 0, the data transfer is aborted. The DPSM waits for not busy
and the FIFO to be disabled/flushed before moving to the Idle state and the
DABORT flag is set.
- If the CPSM Abort signal is received during or after the 2 last bits of the CRC
response when DATACOUNT = 0 or when no CRC is expected and DATACOUNT
= 0 and there has been no DTIMEOUT error, the DPSM stays in the Busy state no
DABORT flag is generated, since the transfer may completed normally.
- If the CPSM Abort signal is received when a DTIMEOUT error has occurred the
DPSM waits for not busy and the FIFO to be disabled/flushed before moving to the
Idle state and the DABORT flag is set.
– When entering the Busy state due to an abort in the Send state, the DPSM waits
for not busy before moving to the Idle state and the DABORT flag is set.
– When DPSM has been started with DTEN , after an error (DCRCFAIL when
DATACOUNT > 0, or DTIMEOUT) the DPSM moves to the Idle state when the
FIFO is reset.
– When the DPSM has been started due to Busy on SDMMC_D0, waits for not busy
after which the Busy end status flag (BUSYD0END) is set and the DPSM moves to
the Idle state.

RM0438 Rev 8 1813/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
The data timer (DATATIME) is enabled when the DPSM is in the Wait_R or Busy state 2
cycles after the data block end bit, or data read command end bit, or R1b response, and
generates the data timeout error (DTIMEOUT):
• When transmitting data, the timeout occurs
– when a CRC status is expected and no start bit is received withing 8 SDMMC_CK
cycles, the DTIMEOUT flag is set.
– when the Busy state takes longer than the programmed timeout period., the
DTIMEOUT flag is set.
• When receiving data, the timeout occurs
– when there is still data to be received DATACOUNT > 0 and no start bit is received
before the programmed timeout period, the DTIMEOUT flag is set.
• After a R1b response, the timeout occurs
– when the Busy state takes longer than the programmed timeout period., the
DTIMEOUT flag is set.
When DATATIME = 0:
• In receive the start bit must be present 2 cycles after the data block end bit or data read
command end bit.
• In transmit busy is timed out 2 cycles after the CRC token end bit or stream data end
bit.
• After a R1b response busy is timed out 2 cycles after the response end bit.
Data can be transferred from the card to the host (transmit, send) or vice versa (receive).
Data are transferred via the SDMMC_Dn data lines, they are stored in a FIFO.
The data token format is selected with register bits DTMODE according.
The data path implements the status flags and associated clear bits shown in [Table 396](../tables/table_396.md):
[Table 395](../tables/table_395.md). Data token format
Description Start bit Data (1)
1. The total amount of data to transfer is given by DA TALENGTH. Where for Block data the amount of data in
each block is given by DBLOCKSIZE.
CRC16 End bit DTMODE
Block data 0 (DBLOCKSIZE, DATALENGTH) Yes 1 00
SDIO multibyte 0 (DATALENGTH) Yes 1 01
e•MMC stream 0 (DATALENGTH) No 1 10
[Table 396](../tables/table_396.md). Data path status flags and clear bits
Flag Description
DATAEND
TX Set at the end of the complete data transfer when the CRC is OK and busy has finished
and both DTHOLD = 0 and DATACOUNT = 0. (DPSM moves from Wait_S to Idle)
RX Set at the end of the complete data transfer when the CRC is OK and all data has been
read, (DATACOUNT = 0 and FIFO is empty). (DPSM moves from Wait_R to Idle)Boot

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1814/2187 RM0438 Rev 8
DCRCFAIL
TX
Set at the end of the CRC when FAIL and busy has finished. (DPSM stay in Busy when
there is still data to send and wait for CPSM Abort) (DPSM moves from Busy to Idle when
all data has been sent) or DPSM has been started with DTEN
RX Set at the end of the CRC when FAIL and FI FO is empty. (DPSM stays in Receive when
there is still data to be received and wait for CPSM Abort) (DPSM moves from Receive to
Idle when all data has been received or DPSM has been started with DTEN) Boot
ACKFAIL Boot Set at the end of the boot acknowledgment when fail. (DPSM stays in Wait_Ack and wait
for CPSM Abort)
DTIMEOUT
CMD
R1b
Set after the command response no end of busy received before the timeout. (DPSM
stays in Busy and wait for CPSM Abort)
TX
Set when no CRC token start bit received within Ncrc, or no end of busy received before
the timeout. (DPSM stays in Busy and wait for CPSM Abort) (When DPSM has been
started with DTEN move to Idle)
Note: The DCRCFAIL flag may also be set when CRC failed before the busy timeout.
RX Set when no start bit received before the timeout. (DPSM stays in Wait_R and wait for
CPSM Abort) (When DPSM has been started with DTEN move to Idle)Boot
ACKTIMEOUT Boot Set when no start bit received before the timeout. (DPSM stays in Wait_Ack and wait for
CPSM Abort)
DBCKEND
TX
When DTHOLD = 1 and IDMAEN = 0: Set at the end of data block transfer when the CRC
is OK and busy has finished, when data transfer is not complete (DATACOUNT >0).
(DPSM moves from Busy to Wait_S)
RX When RWSTART = 1: Set at the end of data block transfer when the CRC is OK, when
data transfer is not complete (DATACOUNT > 0). (DPSM moves from Receive to R_W)Boot
DHOLD
TX When DTHOLD = 1: Set at the end of data block transfer when the CRC is OK and busy
has finished. (DPSM moves from Wait_S to Idle)
RX
When DTHOLD = 1: Set at the end of data block transfer when the CRC is OK and all
data has been read (FIFO is empty), when data transfer is not complete (DATACOUNT
>0). (DPSM moves from Wait_R to Idle)
DABORT
CMD
R1b
When CPSM Abort event has been sent by the CPSM and busy has finished. (DPSM
moves from Busy to Idle)
TX
When CPSM Abort event has been sent by the CPSM before the 2 last bits of the
transfer. (DPSM moves from any state to Idle)RX
Boot
BUSYD0END CMD
R1b
Set after the command response when end of busy before the timeout. (DPSM moves
from Busy to Idle)
DPSMACT Data transfer in progress. (DPSM not in Idle state)
[Table 396](../tables/table_396.md). Data path status flags and clear bits (continued)
Flag Description

RM0438 Rev 8 1815/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
The data path error handling is shown in [Table 397](../tables/table_397.md):
Data FIFO
The data FIFO (first-in-first-out) subunit contains the transmit and receive data buffer. A
single FIFO is used for either transmit or receive as selected by the DTDIR bit. The FIFO
contain a 32-bit wide, 16-word deep data buffer and control logic. Because the data FIFO
operates in the AHB clock domain (sdmmc_hclk), all signals from the subunits in the
SDMMC clock domain (SDMMC_CK/sdmmc_rx_ck) are resynchronized.
[Table 397](../tables/table_397.md). Data path error handling
Error DPSM state Cause Card action Host action DPSM action
Timeout
Wait_Ack No Ack in
time unknown Card cycle power
Stay in Wait_Ack
(reset the SDMMC with
the RCC.SDMMCxRST
register bit)
Wait_R No start bit
in time
unknown
Stop data reception
Send stop transmission
command
On CPSM Abort move
to Idle
unknown Stop boot procedure
Busy
Busy too
long (due to
data
transfer)
unknown
Stop data reception
Send stop transmission
command
Busy too
long (due to
R1b)
unknown Send reset command
CRC Receive transmission
error Send further data
Stop data reception
Send stop transmission
command
On CPSM Abort move
to Idle
CRC status Busy
Negative
status Ignore further data Stop data transmission
Send stop transmission
command
On CPSM Abort move
to Idletransmission
error wait for further data
Ack status Wait_Ack transmission
error Send boot data Stop boot procedure On CPSM Abort move
to Idle
Overrun Receive FIFO full Send further data
Stop data reception
Send stop transmission
command
On CPSM Abort move
to Idle
Underrun Send FIFO empty Receive further data
Stop data transmission
Send stop transmission
command
On CPSM Abort move
to Idle

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1816/2187 RM0438 Rev 8
The FIFO can be in one of the following states:
• The transmit FIFO refers to the transmit logic and data buffer when sending data out to
the card. (DTDIR = 0)
• The receive FIFO refers to the receive logic and data buffer when receiving data in from
the card. (DTDIR = 1)
The end of a correctly completed SDMMC data transfer from the FIFO is indicated by the
DATAEND flags driven by the data path subunit. Any incorrect (aborted) SDMMC data
transfer from the FIFO is indicated by one of the error flags (DCRCFAIL, DTIMEOUT,
DABORT) driven by the data path subunit, or one of the FIFO error flags (TXUNDERR,
RXOVERR) driven by the FIFO control.
The data FIFO can be accessed in the following ways, see [Table 398](../tables/table_398.md).
Transmit FIFO:
Data can be written to the transmit FIFO when the DPSM has been activated
(DPSMACT = 1).
When IDMAEN = 1 the FIFO is fully handled by the IDMA.
When IDMAEN = 0 the FIFO is controlled by firmware via the AHB slave interface. The
transmit FIFO is accessible via sequential addresses. The transmit FIFO contains a data
output register that holds the data word pointed to by the read pointer. When the data path
subunit has loaded its shift register, it increments the read pointer and drives new data out.
The transmit FIFO is handled in the following way:
1. Write the data length into DATALENGTH  and the block length in DBLOCKSIZE.
– For block data transfer (DTMODE = 0), DATALENGTH must be an integer multiple
of DBLOCKSIZE.
2. Set the SDMMC in transmit mode (DTDIR = 0).
– Configures the FIFO in transmit mode.
3. Enable the data transfer
– either by sending a command from the CPSM with the CMDTRANS bit set
– or by setting DTEN bit
4. When (DPSMACT = 1) write data to the FIFO.
– The DPSM stays in the Wait_S state un til FIFO is full (TXFIFOF = 1), or the
number indicated by DATALENGTH.
[Table 398](../tables/table_398.md). Data FIFO access
Data FIFO access IDMAEN
From firmware via AHB slave interface 0
From IDMA via AHB master interface 1

RM0438 Rev 8 1817/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
- The SDMMC keeps sending data as long as FIFO is not empty, hardware flow
control during data transfer is used to prevent FIFO underrun.
5. Write data to the FIFO.
– When the FIFO is handled by software, wait until the FIFO is half empty
(TXFIFOHE flag), write data to the FIFO until FIFO is full (TXFIFOF = 1), or last
data has been written.
– When the FIFO is handled by the IDMA , the IDMA transfers the FIFO date.
6. When last data has been written wait for end of data (DATAEND flag)
– SDMMC has completely sent all data and the DPSM is disabled (DPSMACT = 0).
In case of a data transfer error or transfer hold when IDMAEN = 0, firmware must stop
writing to the FIFO and flush and reset the FIFO with the FIFORST register bit.
The transmit FIFO status flags are listed in [Table 399](../tables/table_399.md).
Receive FIFO:
Data can be read from the receive FIFO when the DPSM is activated (DPSMACT = 1).
When IDMAEN = 1 the FIFO is fully handled by the IDMA.
When IDMAEN = 0 the FIFO is controlled by firmware via the AHB slave interface.When the
data path subunit receives a word of data, it drives the data on the write databus. The write
pointer is incremented after the write operation completes. On the read side, the contents of
the FIFO word pointed to by the current value of the read pointer is driven onto the read
databus. The receive FIFO is accessible via sequential addresses.
[Table 399](../tables/table_399.md). Transmit FIFO status flags
Flag Description
TXFIFOF Set to high when all transmit FIFO words contain valid data.
TXFIFOE Set to high when the transmit  FIFO does not contain valid data.
TXFIFOHE Set to high when half or more transmit FIFO words are empty.
TXUNDERR Set to high when an underrun error occurs. This flag is cleared by writing to the
SDMMC Clear register.

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1818/2187 RM0438 Rev 8
The receive FIFO is handled in the following way:
1. Write the data length into DATALENGTH  and the block length in DBLOCKSIZE.
– For block data transfer (DTMODE = 0), DATALENGTH must be an integer multiple
of DBLOCKSIZE.
2. Set the SDMMC in receive mode (DTDIR = 1).
– Configures the FIFO in receive mode.
3. Enable the DPSM transfer
– either by sending a command from the CPSM with the CMDTRANS bit set
– or by setting DTEN bit.
4. When (DPSMACT = 1) the FIFO is ready to receive data.
– The DPSM writes the received data to the FIFO.
- The SDMMC keeps receiving data as long as FIFO is not full, hardware flow
control during the data transfer is used to prevent FIFO overrun.
5. Read data from the FIFO.
– When the FIFO is handled by software, wa it until the FIFO is half full (RXFIFOHF
flag), read data from the FIFO until FIFO is empty (RXFIFOE = 1).
- When last data has been received, read data from the FIFO until FIFO is empty
(DATAEND = 1).
– When the FIFO is handled by the IDMA , the IDMA transfers the FIFO date.
6. SDMMC has completely received all data  and the DPSM is disabled (DPSMACT = 0).
In case of a data transfer hold when IDMAEN = 0, the firmware must read the remaining
data until the FIFO is empty and reset the FIFO with the FIFORST register bit. This causes
the DPSM to go to the Idle state (DPSMACT = 0).
In case of a data transfer error when IDMAEN = 0, the firmware must stop reading the FIFO
and flush and reset the FIFO with the FIFORST register bit. This causes the DPSM to go to
the Idle state (DPSMACT = 0).
The receive FIFO status flags are listed in [Table 400](../tables/table_400.md).
CLKMUX unit
The CLKMUX selects the source for clock sdmmc_rx_ck to be used with the received data
and command response. The receive data clock source can be selected by the clock control
register bit SELCLKRX, between:
• sdmmc_io_in_ck bus master main feedback clock.
• SDMMC_CKIN external bus feedback clock.
The sdmmc_io_in_ck is selected when there is no external driver, with DS and HS.
[Table 400](../tables/table_400.md). Receive FIFO status flags
Flag Description
RXFIFOF Set to high when all rece ive FIFO words contain valid data
RXFIFOE Set to high when the receive FIFO does not contain valid data.
RXFIFOHF Set to high when half or more receive FIFO words contain valid data.
RXOVERR Set to high when an overrun error occurs. This flag is cleared by writing to the
SDMMC Clear register.

RM0438 Rev 8 1819/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
The SDMMC_CKIN is selected when there is an external driver with SDR12, SDR25,
SDR50 and DDR50.
[Figure 524](../figures/figure_524.md). CLKMUX unit
The sdmmc_rx_ck source must be changed when the CPSM and DPSM are in the Idle
state.
48.4.5 SDMMC AHB slave interface
The AHB slave interface generates the interrupt requests, and accesses the SDMMC
adapter registers and the data FIFO. It consists of a data path, register decoder, and
interrupt logic.
SDMMC FIFO
The FIFO access is restricted to word access only:
• In transmit FIFO mode
– Data are written to the FIFO in words (32-bits) until all data according
DATALENGTH has been transfered. When the DATALENGTH is not an integer
multiple of 4, the last remaining data (1, 2 or 3 bytes) are written with a word
transfer.
• In receive FIFO mode
– Data are read from the FIFO in words (32-bits) until all data according
DATALENGTH has been transfered. When the DATALENGTH is not an integer
multiple of 4, the last remaining data (1, 2 or 3 bytes) are read with a word transfer
padded with 0 value bytes.
When accessing the FIFO with half word or byte accesses an AHB bus fault is generated.
SDMMC interrupts
The interrupt logic generates an interrupt request signal that is asserted when at least one
of the unmasked status flags is active. A mask register is provided to allow selection of the
conditions that generate an interrupt. A status flag generates the interrupt request if a
corresponding mask flag is set. Some status flags require an implicit clear in the clear
register.
48.4.6 SDMMC AHB master interface
The AHB master interface is used to transfer the data between a memory and the FIFO
using the SDMMC IDMA.
MSv41697V2
CLKMUX
MUX SDMMC_CKIN
sdmmc_io_in_ck
Registers
SDMMC internal receive clock

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1820/2187 RM0438 Rev 8
SDMMC IDMA
Direct memory access (DMA) is used to provide high-speed transfer between the SDMMC
FIFO and the memory. The AHB master optimizes the bandwidth of the system bus. The
SDMMC internal DMA (IDMA) provides one channel to be used either for transmit or
receive.
The IDMA is enabled by the IDMAEN bit and supports burst transfers of 8 beats.
• In transmit burst transfer mode:
– Data are fetched in burst from memory whenever the FIFO is empty for the
number of burst transfers, until all data according DATALENGTH has been
transfered. When the DATALENGTH is not an integer multiple of the burst size the
remaining, smaller then burst size data is transfered using single transfer mode.
When the DATALENGTH is not an integer multiple of 4, the last remaining data (1,
2 or 3 bytes) are fetched with a word transfer.
• In receive burst transfer mode:
– Data are stored in burst in to memory wh enever the FIFO contains the number of
burst transfers, until all data according DATALENGTH has been transfered.
When the DATALENGTH is not an integer multiple of the burst transfer the
remaining, smaller then burst size data, is transfered using single transfer mode.
When the DATALENGTH is not an integer multiple of 4, the last remaining data (1,
2 or 3 bytes) are stored with halfword and or byte transfers.
In addition the IDMA provides the following channel configurations selected by bit
IDMABMODE:
• single buffered channel
• double buffered channel
Single buffered channel
In single buffer configuration the data at the memory side is accessed in a linear matter
starting from the base address IDMABASE0. When the IDMA has finished transferring all
data the and the DPSM has completed the transfer the DATAEND flag is set.
Double buffered channel
In double buffer configuration the data at the memory side is subsequently accessed from 2
buffers, one located from base address IDMABASE0 and a second located from base
address IDMABASE1. This allows firmware to process one memory buffer while the IDMA is
accessing the other memory buffer. The size of the memory buffers is defined by
IDMABSIZE. The buffer size must be an integer multiple of the burst size. It is possible to
update the base address of the buffers on-the-fly when the channel is enabled, the following
rule apply:
• When IDMABACT bit is ‘0’ the IDMA hardware uses the IDMABASE0 to access
memory. When attempting to write to this register by Firmware the write is discarded,
IDMABASE0 data isl not changed. Firmware is authorized to write IDMABASE1.
• When IDMABACT bit is ‘1’ the IDMA hardware uses the IDMABASE1 to access
memory. When attempting to write to this register by Firmware the write is discarded,
IDMABASE1 data is not changed. Firmware is authorized to write IDMABASE0.
When the IDMA has finished transferring the data of one buffer the buffer transfer complete
flag (IDMABTC) is set and the IDMABACT bit toggles where after the IDMA continues

RM0438 Rev 8 1821/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
transferring data from the other buffer. When the IDMA has finished transferring all data and
the DPSM has completed the transfer the DATAEND flag is set.
The IDMABASEn address must be word aligned.
IDMA transfer error management
An IDMA transfer error can occur:
• When reading or writing a reserved address space.
On an IDMA transfer error subsequent IDMA transfers are disabled and an IDMATE flag is
set. Depending when the IDMA transfer error occurs, it normally causes the generation of a
TXUNDERR or RXOVERR error.
The behavior of the IDMATE flag depend on when the IDMA transfer error occurs during the
SDMMC transfer:
• An IDMA transfer error is detected before any SDMMC transfer error (TXUNDERR,
RXOVERR, DCRCFAIL, or DTIMEOUT):
– The IDMATE flag is set at the same ti me as the SDMMC transfer error flag.
– The TXUNDERR, RXOVERR, DCRCFAIL, or  DTIMEOUT interrupt is generated.
• An IDMA transfer error is detected during a STOP_TRANSNMISSION command:
– The IDMATE flag is set at the same time as the DABORT flag.
– The DABORT interrupt is generated.
• An IDMA transfer error is detected at the end of the SDMMC transfer (DHOLD, or
DATAEND).
– The IDMATE flag is set at the end of the SDMMC transfer.
– A SDMMC transfer end interrupt is generated and a DHOLD or DATAEND flag is
set.
The IDMATE is generated on an other SDMMC transfer interrupt (TXUNDERR. RXOVERR,
DCRCFAIL, DTIMEOUT, DABORT, DHOLD, or DATAEND).
48.4.7 AHB and SDMMC_CK clock relation
The AHB must at least have 3x more bandwidth than the SDMMC bus bandwidth: for
example, for SDR50 4-bit mode (50 Mbyte/s), the minimum sdmmc_hclk frequency is
37.5 MHz (150 Mbyte/s).
[Table 401](../tables/table_401.md). AHB and SDMMC_CK clock frequency relation
SDMMC bus mode SDMMC bus
width
Maximum SDMMC_CK
[MHz]
Minimum AHB clock
[MHz]
e•MMC DS 8 26 19.5
e•MMC HS 8 52 39
e•MMC DDR52 8 52 78
SD DS / SDR12 4 25 9.4
SD HS / SDR25 4 50 18.8
SD DDR50 4 50 37.5
SD SDR50 4 100 37.5

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1822/2187 RM0438 Rev 8
48.5 Card functional description
48.5.1 SD I/O mode
The following features are SDMMC specific operations:
• SDIO interrupts
• SDIO suspend/resume operation (write and read suspend)
• SDIO Read Wait operation by stopping the clock
• SDIO Read Wait operation by SDMMC_D2 signaling
SD I/O interrupts
To allow the SD I/O card to interrupt the host, an interrupt function is available on pin 8
(shared with SDMMC_D1 in 4-bit mode) on the SD interface. The use of the interrupt is
optional for each card or function within a card. The SD I/O interrupt is level-sensitive, which
means that the interrupt line must be held active (low) until it is either recognized and acted
upon by the host or deasserted due to the end of the interrupt period. After the host has
serviced the interrupt, the interrupt status bit is cleared via an I/O write to the appropriate bit
in the SD I/O card internal registers. The interrupt output of all SD I/O cards is active low and
the application must provide external pull-up resistors on all data lines (SDMMC_D[3:0]).
In SD 1-bit mode pin 8 is dedicated to the interrupt function (IRQ), and there are no timing
constraints on interrupts.
In SD 4-bit mode the host samples the level of pin 8 (SDMMC_D1/IRQ) into the interrupt
detector only during the interrupt period. At all other times, the host interrupt ignores this
value. The interrupt period begins when interrupts are enabled at the card and SDIOEN bit
is set see register settings in [Table 402](../tables/table_402.md).
In 4-bit mode the card can generate a synchronous or asynchronous interrupt as indicated
by the card CCCR register SAI and EAI bits.
• Synchronous interrupt, require the SDMMC_CK to be active.
• Asynchronous interrupt, can be generated when the SDMMC_CK is stopped, 4 cycles
after the start of the card interrupt period following the last data block.
[Table 402](../tables/table_402.md). SDIO special operation control
Operation mode
SDIOEN
RWMOD
RWSTOP
RWSTART
DTDIR
Interrupt detection 1 X X X X
Suspend/Resume operation X X X X X
Read Wait SDMMC_CK clock stop (START) X 1 0 1 1
Read Wait SDMMC_CK clock stop (STOP) X 1 1 1 1
Read Wait SDMMC_D2 signaling (START) X 0 0 1 1
Read Wait SDMMC_D2 signaling (STOP) X 0 1 1 1

RM0438 Rev 8 1823/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
[Figure 525](../figures/figure_525.md). Asynchronous interrupt generation
The timing of the interrupt period is depending on the bus speed mode.
In DS, HS, SDR12, and SDR25 mode, selected by register bit BUSSPEED, the interrupt
period is synchronous to the SD clock.
• The interrupt period ends at the next clock from the end bit of a command that transfers
data block(s) (Command sent with the CMDTRANS bit is set), or when the DTEN bit is
set.
• The interrupt period resumes 2 SDMMC_CK after the completion of the data block.
• At the data block gap the interrupt period is limited to 2 SDMMC_CK cycles.
Note: DTEN must not be used to start data transfer with SD and e•MMC cards.
[Figure 526](../figures/figure_526.md). Synchronous interrupt period data read
MSv40191V3
SDMMC_CK
SDMMC_CMD
SDMMC_D0
SDMMC_D1
SDMMC_D2
SDMMC_D3
Last dataSE S CRC E
Last dataSE S CRC E
Last dataSE S CRC E
S Data block
Command E
Data1 Asynchronous INTSynchronous
INT Data1
2 CK 4 CK NEAI
Interrupt period
MSv40195V2
SDMMC_CK
SDMMC_D0
SDMMC_D1
SDMMC_D2
SDMMC_D3
DataSE
S Command data
R E
Data1
2 CK
SDMMC_CMD
IRQIRQInterrupt period
DataSE
DataSE DataSE
DataSE DataSE
Data1
2 CK

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1824/2187 RM0438 Rev 8
[Figure 527](../figures/figure_527.md). Synchronous interrupt period data write
In SDR50 and DDR50, selected by register bit BUSSPEED, due to propagation delay from
the card to host, the interrupt period is asynchronous.
• The card interrupt period ends after 0 to 2 SDMMC_CK cycles after the end bit of a
command that transfers data block(s) (Command sent with the CMDTRANS bit is set),
or when the DTEN bit is set. At the host the interrupt period ends after the end bit of a
command that transfers data block(s). A card interrupt issued in the 1 to 2 cycles after
the command end bit are not detected by the host during this interrupt period.
• The card interrupt period resumes 2 to 4 SDMMC_CK after the completion of the last
data block. The host resumes the interrupt period always 2 cycles after the last data
block.
• There is NO interrupt period at the data block gap.
Note: DTEN must not be used to start data transfer with SD and e•MMC cards.
MSv40196V2
SDMMC_CK
SDMMC_D0
SDMMC_D1
SDMMC_D2
SDMMC_D3
DataSE
DataSE
DataSE
S Command data
W E
Data1
2 CK
SDMMC_CMD S RSP E
S CRC status E
IRQIRQInterrupt period
DataSE
DataSE
DataSE
Data1
2 CK

RM0438 Rev 8 1825/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
[Figure 528](../figures/figure_528.md). Asynchronous interrupt period data read
[Figure 529](../figures/figure_529.md). Asynchronous interrupt period data write
When transferring Open-ended multiple block data and using DTMODE “block data transfer
ending with STOP_TRANSMISSION command”, the SDMMC masks the interrupt period
after the last data block until the end of the CMD12 STOP_TRANSMISSION command.
The interrupt period is applicable for both memory and I/O operations.
MSv40940V3
sdmmc_fb_ck
SDMMC_D0
SDMMC_D1
SDMMC_D2
SDMMC_D3
SDMMC_CMD
IRQIRQInterrupt period Data1
2 CK
SDMMC_CK
S Command data
R E
tOP
0 CK – 2 CK
DataSE
DataSE
DataSE
tOP
MSv40192V2
SDMMC_CK
sdmmc_fb_ck
SDMMC_D0
SDMMC_D1
SDMMC_D2
SDMMC_D3
DataSE
DataSE
DataSE
S Command data
W E
Data1
0 CK - 2 CK
tOP
2 CK – 4 CK
SDMMC_CMD S RSP E
S CRC status E
tOP
tOP tOP
IRQIRQInterrupt period

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1826/2187 RM0438 Rev 8
In 4-bit mode interrupts can be differentiated from other signaling according [Table 403](../tables/table_403.md).
SD I/O suspend and resume
This function is NOT supported in SDIO version 4.00 or later.
Within a multifunction SD I/O or a card with both I/O and memory functions, there are
multiple devices (I/O and memory) that share access to the e•MMC/SD bus. To share
access to the host among multiple devices, SD I/O and combo cards optionally implement
the concept of suspend/resume. When a card supports suspend/resume, the host can
temporarily halt (suspend) a data transfer operation to one function or memory to free the
bus for a higher-priority transfer to a different function or memory. After this higher-priority
transfer is complete, the original transfer is restarted (resume) where it left off.
To perform the suspend/resume operation on the bus, the host performs the following steps:
1. Determines the function current ly using the SDMMC_D[3:0] line(s).
2. Requests the lower-priority or slower transaction to suspend.
3. Waits for the transaction suspension to complete.
4. Begins the higher-priority transaction.
5. Waits for the completion of the higher priority transaction.
6. Restores the suspended transaction.
The card receiving a suspend command responds with its current bus status. Only when the
bus has been suspended by the card the bus status indicates suspension completed.
There are different suspend cases conditions:
• Suspend request accepted prior to the start of data transfer.
• Suspend request not accepted, (due to data being transfered at the same time), the
host keeps checking the request until it is accepted (data transfer has suspended).
• Suspend request during write busy.
• Suspend request with write multiple.
• Suspend request during Read Wait.
For the host to know if the bus has been released it must check the status of the suspend
request, suspension completed.
When the bus status of the suspend request response indicates suspension completed, the
card has released the bus. At this time the state of the suspended operation must be saved
where after an other operation can start.
The suspend command must be sent with the CMDSUSPEND bit set. This makes possible
to start the interrupt period after the suspend command response when the bus is
suspended (response bit BS = 0).
[Table 403](../tables/table_403.md). 4-bit mode Start, interrupt, and CRC-status Signaling detection
SDMMC data line Start Interrupt CRC-status
SDMMC_D0 0 1 or CRC-status 0
SDMMC_D1 0 0 X
SDMMC_D2 0 1 or Read Wait X
SDMMC_D3 0 1 X

RM0438 Rev 8 1827/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
The hardware does not save the number of remaining data to be transfered when resuming
the suspended operation. It is up to firmware to determine the data that has been
transferred and resume with the correct remaining number of data bytes.
While receiving data from the card, the SDMMC can suspend the read operation after the
read data block end (DPSM in Wait_R). After receiving the suspend acknowledgment
response from the card the following steps must be taken by firmware:
1. The normal receive process must be stopped by setting DTHOLD bit.
a) The remaining number of data bytes in the FIFO must be read until the receive
FIFO is empty (RXFIFOE flag is set), and when IDMAEN = 0 the FIFO must be
reset with FIFORST.
2. The confirmation that all data has been re ad from the FIFO, and that the suspend is
completed is indicated by the DHOLD flag.
a) The remaining number of data bytes (multi ple of data blocks) still to be read when
resuming the operation must be determined from the remaining number of bytes
indicated by the DATACOUNT.
Note: When a DTIMEOUT flag occurs during the suspend procedure, this must be ignored.
To resume receiving data from the card, the following steps must be taken by firmware:
1. The remaining number of data bytes (multiple of data blocks) must be programmed in
DATALENGTH.
2. The DPSM must be configured to receive data in the DTDIR bit.
3. The resume command must be sent from the CPSM, with the CMDTRANS bit set and
the CMDSUSPEND bit set, which ends the interrupt period when data transfer is
resumed (response bit DF = 1) and enabled the DPSM, after which the card resumes
sending data.
While sending data to the card, the SDMMC can suspend the write operation after the write
data block CRC status end (DPSM in Busy). Before sending the suspend command to the
card the following steps must be taken by firmware:
1. Enable DHOLD flag (and DB CKEND flag when IDMAEN = 0)
2. The DPSM must be prevented from start sending a new data block by setting
DTHOLD.
3. When IDMAEN = 0: When receiving the DB CKEND flag the data transfer is stopped.
Firmware can stop filling the FIFO, after which the FIFO must be reset with FIFORST.
Any bytes still in the FIFO need to be rewritten when resuming the operation.
4. When receiving the DHOLD flag the data tr ansfer is stopped. The remaining number of
data bytes still to be written when resuming must be determined from the remaining
number of bytes indicated by the DATACOUNT.
5. To suspend the card the suspend comma nd must be sent by the CPSM with the
CMDSUSPEND bit set. This makes possible to start the interrupt period after the
suspend command response when the bus is suspended (response bit BS = 0).
To resume sending data to the card, the following steps must be taken by firmware:
1. The remaining number of data bytes must be programmed in DATALENGTH.
2. The DPSM must be configured for transmi ssion with DTDIR set and enabled by having
the CPSM send the resume command with the CMDTRANS bit set and the
CMDSUSPEND bit set. This ends the interrupt period and start the data transfer. The

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1828/2187 RM0438 Rev 8
DPSM either goes to the Wait_S state when SDMMC_D0 does not signal busy, or goes
to the Busy state when busy is signaled.
3. When IDMAEN = 1: The IDMA needs to be reprogrammed for the remaining bytes to
be transfered.
4. When IDMAEN = 0: Firmware must star t filling the FIFO with the remaining data.
SD I/O Read Wait
There are two methods to pause the data transfer during the block gap:
1. Stopping the SDMMC_CK.
2. Using Read Wait si gnaling on SDMMC_D2.
The SDMMC can perform a Read Wait with register settings according [Table 402](../tables/table_402.md).
Depending the SDMMC operation mode (DS, HS, SDR12, SDR25) or (SDR50, DDR) each
method has a different characteristic.
The timing for pause read operation by stopping the SDMMC_CK for DS, HS, SDR12, and
SDR25, the SDMMC_CK may be stopped 2 SDMMC_CK cycles after the end bit. When
ready the host resumes by restarting clock (see [Figure 530](../figures/figure_530.md)).
[Figure 530](../figures/figure_530.md). Clock stop with SDMMC_CK for DS, HS, SDR12, SDR25
The timing for pause read operation by stopping the SDMMC_CK for SDR50 and DDR50,
the SDMMC_CK may be stopped minimum 2 SDMMC_CK cycles and maximum 5
SDMMC_CK cycles, after the end bit. When ready the host resumes by restarting clock, see
[Figure 531](../figures/figure_531.md). (In DDR50 mode the SDMMC_CK must only be stopped after the falling edge,
when the clock line is low.)
[Figure 531](../figures/figure_531.md). Clock stop with SDMMC_CK for DDR50, SDR50
MSv40193V2
SDMMC_CK
Read dataSDMMC_Dn Interrupt period H Read data
2 CK 2 CK 1 CK
MSv40194V2
SDMMC_CK
Read
dataSDMMC_Dn Read
data
10 234 567 567 89 1 0
tOPtOP
2 CK min.
5 CK max.
1
End
0
Start
NAC 8 CK min.

RM0438 Rev 8 1829/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
In Read Wait SDMMC_CK clock stopping, when RWSTART is set, the DSPM stops the
clock after the end bit of the current received data block CRC. The clock start again after
writing 1 to the RWSTOP bit, where after the DPSM waits for a start bit from the card.
As SDMMC_CK is stopped, no command can be issued to the card. During a Read Wait
interval, the SDMMC can still detect SDIO interrupts on SDMMC_D1.
The optional Read Wait signaling on SDMMC_D2 (RW) operation is defined only for the SD
1-bit and 4-bit modes. The Read Wait operation enables the host to signal a card that is
reading multiple registers (IO_RW_EXTENDED, CMD53) to temporarily stall the data
transfer while allowing the host to send commands to any function within the SD I/O device.
To determine when a card supports the Read Wait protocol, the host must test capability bits
in the internal card registers.
The timing for Read Wait with a SDMMC_CK less then 50MHz (DS, HS, SDR12, SDR25) is
based on the interrupt period generated by the card on SDMMC_D1. The host by asserting
SDMMC_D2 low during the interrupt period requests the card to enter Read Wait. To exit
Read Wait the host must raise SDMMC_D2 high during one SDMMC_CK cycles before
making it Hi-Z, see [Figure 532](../figures/figure_532.md).
[Figure 532](../figures/figure_532.md). Read Wait with SDMMC_CK < 50 MHz
For SDR50 with a SDMMC_CK more than 50MHz, and DDR50, the card treats the Read
Wait request on SDMMC_D2 as an asynchronous event. The host by asserting
SDMMC_D2 low after minimum 2 SDMMC_CK cycles and maximum 5 SDMMC_CK cycles,
request the card to enter Read Wait. To exit Read Wait the host must raise SDMMC_D2
high during one SDMMC_CK cycles before making it Hi-Z. The host must raise SDMMC_D2
on the SDMMC_CK clock (see [Figure 533](../figures/figure_533.md)).
MSv40941V2
SDMMC_CK
SDMMC_D1
SDMMC_D2
SDMMC_D3
SDMMC_D0
SDMMC_CMD
2 CK
Read data
2 CK
Read data
2 CK
Read data Read dataRead Wait
Read data Read dataInt period
CMD

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1830/2187 RM0438 Rev 8
[Figure 533](../figures/figure_533.md). Read Wait with SDMMC_CK > 50 MHz
In Read Wait SDMMC_D2 signaling, when RWSTART is set, the DPSM drives SDMMC_D2
after the end bit of the current received data block CRC. The Read Wait signaling on
SDMMC_D2 is removed when writing 1 to the RWSTOP bit. The DPSM remains in R_W
state for two more SDMMC_CK clock cycles to drive SDMMC_D2 to 1 for one clock cycle
(in accordance with SDIO specification), where after the DPSM waits for a start bit from the
card.
During the Read Wait signaling on SDMMC_D2 commands can be issued to the card.
During the Read Wait interval, the SDMMC can detect SDIO interrupts on SDMMC_D1.
48.5.2 CMD12 send timing
CMD12 is used to stop/abort the data transfer, the card data transmission is terminated two
clock cycles after the end bit of the Stop Transmission command.
MSv40948V2
SDMMC_CK
SDMMC_D2
SDMMC_D3
SDMMC_D1
SDMMC_D0
Read data
2 CK min.
Read data Read Wait
01234567 88 88 91 0
tOP tOP
NAC 8 CK min.
1
End
0
Start
Read data0
StartRead data 1
End
5 CK max.
[Table 404](../tables/table_404.md). CMD12 use cases
Data operation Stop Transmissi on command CMD12 Description
SDMMC stream write The data transfer is stopped/aborted by sending the Stop Transmission
command.
SDMMC open ended
multiple block write
The data transfer is stopped/aborted by sending the Stop Transmission
command.
If the card detects an error, the host must abort the operation by sending
the Stop Transmission command.
SDMMC block write with
predefined block count
The Stop Transmission command is not required at the end of this type of
multiple block write. (sending the Stop Transmission command after the
card has received the last block is regarded as an illegal command.)
If the card detects an error, the host must abort the operation by sending
the Stop Transmission command.
SDMMC stream read The data transfer is stopped/aborted by sending the Stop Transmission
command.

RM0438 Rev 8 1831/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
All data write and read commands can be aborted any time by a Stop Transmission
command CMD12. The following data abort procedure applies during an ongoing data
transfer:
1. Load CMD12 Stop Transmission command in registers and set the CMDSTOP bit.
– This causes the CPSM Abort signal to be generated when the command is sent to
the DPSM.
2. Configure the CPSM to send a command immediately (clear WAITPEND bit).
– The card, when sending data, stops data  transfer 2 cycles after the Stop
Transmission command end bit.
The card when no data is being sent, does not start sending any new data.
– The host, when sending data, sends one last data bit followed by an end bit after
the Stop Transmission command end bit.
The host when not sending data, does not start sending any new data.
3. When IDMAEN = 0, the FIFO need to be reset with FIFORST.
– When writing data to the card. On the CM DREND flag, firmware must stop writing
data to the FIFO. Subsequently the FIFO must be reset with FIFORST, this flushes
the FIFO.
– When reading data from the card. On the CMDREND flag, firmware must read the
remaining data from the FIFO. Subsequently the FIFO must be reset with
FIFORST.
4. When IDMAEN = 1, hardware takes care of the FIFO.
– When writing data to the card. On the CPSM Abort signal, hardware stops the
IDMA and subsequently the FIFO is flushed.
– When reading data from the card. On th e CPSM Abort signal, hardware instructs
the IDMA to transfer the remaining data from the FIFO to RAM.
5. When the FIFO is empty/reset the DABORT flag is generated.
Stream operation and CMD12
To stop the stream transfer after the last byte to be transfered, the CMD12 end bit timing
must be sent aligned with the data stream end of last byte. The following write stream data
procedure applies:
SDMMC open ended
multiple block read
The data transfer is stopped/aborted by sending the Stop Transmission
command.
If the card detects an error, the host must abort the operation by sending
the Stop Transmission command.
SDMMC block read with
predefined block count
The Stop Transmission command is not required at the end of this type of
multiple block read. (sending the Stop Transmission command after the
card has transmitted the last block is regarded as an illegal command.)
Transaction can be aborted by sending the Stop Transmission command.
If the card detects an error, the host must abort the operation by sending
the Stop Transmission command.
[Table 404](../tables/table_404.md). CMD12 use cases (continued)
Data operation Stop Transmissi on command CMD12 Description

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1832/2187 RM0438 Rev 8
1. Initialize the stream data in the DPSM, DTMODE = MCC stream data transfer.
2. Send the WRITE_DATA_STREAM command from the CPSM with CMDTRANS = 1.
3. Preload CMD12 in command registers, with the CMDSTOP bit set.
4. Configure the CPSM to send a command only after a wait pending (WAITPEND = 1)
end of last data (according DATALENGTH).
5. Enabling the CPSM to send the STOP_TRANSMISSION command, the stream data
end bit and command end bit are aligned.
– When DATALENGTH > 5 bytes, Command CMD12 is waited in the CPSM to be
aligned with the data transfer end bit.
– When DATALENGHT < 5 bytes, Comman d CMD12 is started before and the
DPSM remains in the Wait_S state to align the data transfer end with the CMD12
end bit.
6. The write stream data can be aborted an y time by clearing the WAITPEND bit. This
causes the Preloaded CMD12 to be sent immediately and stop the write data stream.
[Figure 534](../figures/figure_534.md).  CMD12 stream timing
To stop the read stream transfer after the last byte, the CMD12 end bit timing must occur
after the last data stream byte. The following read stream data procedure applies:
1. Wait for all data to be received by the DPSM and read from the FIFO (DATAEND flag).
– The DPSM does not receive more data than indicated by DATALENGTH, even if
the card is sending more data.
2. Send CMD12 by the CPSM.
– CMD12 stops the card sending data.
Note: The SDMMC does not receive any more data from the card when DATACOUNT = 0, even
when the card continues sending data.
Block operation and CMD12
To stop block transfer at the end of the data, the CMD12 end bit must be sent after the last
block end bit.
When writing data to the card the CMD12 end bit must be sent after the write data block
CRC token end bit. This requires the CMD12 sending to be tied to the data block
transmission timing. To stop an Open-ended Multiple block write, the following procedure
applies:
MSv40942V1
SDMMC_CK
SDMMC_CMD
NST
CMD12
SDMMC_D0 Stream data last byte
E
E

RM0438 Rev 8 1833/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
1. Before starting the data transfer, set DTMODE to “block data transfer ending with
STOP_TRANSMISSION command”.
2. Wait for all data to be sent by the D PSM and the CRC token to be received, (DATAEND
flag).
– The DPSM does not send more data than indicated by DATALENGTH.
3. Send CMD12 by the CPSM.
– CMD12 sets the card to Idle mode.
When reading data from the card the CMD12 end bit must be sent earliest at the same time
as the card read data block last data bit. This requires the CMD12 sending to be tied to the
data block reception timing. The following stop Open-ended Multiple block read data block
procedure applies:
1. Before starting the data transfer, set DTMODE to “block data transfer ending with
STOP_TRANSMISSION command”.
2. Wait for all data to be received by th e DPSM and read from the FIFO (DATAEND flag).
– The DPSM does not receive more data than indicated by DATALENGTH, even if
the card is sending more data.
3. Send CMD12 with CMDS TOP bit set by the CPSM.
– CMD12 stops the Card sending more dat a and set the card to Idle mode. Any
ongoing block transfer is aborted by the Card.
Note: The SDMMC does not receive any more data from the card when DATACOUNT = 0, even
when the card continues sending data.
48.5.3 Sleep (CMD5)
The e•MMC card may be switched between a Sleep state and a Standby state by CMD5. In
the Sleep state the power consumption of the card is minimized and the Vcc power supply
may be switched off.
The CMD5 (SLEEP) is used to initiate the state transition from Standby state to Sleep state.
The card indicates Busy, pulling down SDMMC_D0, during the transition phase. The Sleep
state is reached when the card stops pulling down the SDMMC_DO line.
To set the card into Sleep state the following procedure applies:
1. Enable interrupt on BUSYD0END.
2. Send CMD5 (SLEEP).
3. On BUSYD0END interrupt, card is in Sleep state.
4. Vcc power supply can be switched off.
The CMD5 (AWAKE) is used to initiate the state transition from Sleep state to Standby state.
The card indicates Busy, pulling down SDMMC_D0, during the transition phase. The
Standby state is reached when the card stops pulling down the SDMMC_DO line.
To set the card into Sleep state the following procedure applies:
1. Switch on Vcc power supply and wait unit minimum operating level is reached.
2. Enable interrupt on BUSYD0END.
3. Send CMD5 (AWAKE).
4. On BUSYD0END interrupt card is in Standby state.
The Vcc power supply can be switched off only after the Sleep state has been reached. The
Vcc supply must be reinstalled before CMD5 (AWAKE) is sent.

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1834/2187 RM0438 Rev 8
[Figure 535](../figures/figure_535.md). CMD5 Sleep Awake procedure
48.5.4 Interrupt mode (Wait-IRQ)
The host and card enter and exit interrupt mode (Wait-IRQ) simultaneously. In interrupt
mode there is no data transfer. The only message allowed is an interrupt service request
response from the card or the host. For the interrupt mode to work correctly the
SDMMC_CK frequency must be set in accordance with the achievable SDMMC_CMD data
rate in Open Drain mode, which depend on the capacitive load and pull-up resistor. The
CLKDIV must be set >1, and the SETCLKRX must select either the sdmmc_io_in_ck or
SDMMC_CLKin source.
The host must ensure that the card is in Standby state before issuing the CMD40
(GO_IRQ_STATE). While waiting for an interrupt response the SDMMC_CK clock signal
must be kept active.
A card in interrupt mode (IRQ state):
• is waiting for an internal card interrupt event. Once the event occurs, the card starts to
send the interrupt service request response. The response is sent in open-drain mode.
• while waiting for the internal card interrupt event, the card also monitors the
SDMMC_CMD line for a start bit. Upon detection of a start bit the card aborts the
interrupt mode and switch to Standby state.
The host in interrupt mode (CPSM Wait state waiting for interrupt):
• is waiting for a card interrupt service request response (start bit).
• while waiting for a card interrupt service request response the host may abort the
interrupt mode (by clearing the WAITINT register bit), which causes the host to send a
interrupt service request response R5 with RCA = 0x0000 in open-drain mode.
When sending the interrupt service request response, the sender bit-wise monitors the
SDMMC_CMD bit stream. The sender whose interrupt service request response bit does
not correspond to the bit on the SDMMC_CMD line stops sending. In the case of multiple
senders only one successfully sends its full interrupt service request response. If the host
sends simultaneously, it loses sending after the transmission bit.
To handle the interrupt mode, the following procedure applies:
MSv40943V1
VCC
SDMMC_CMD
SDMMC_D0 BUSY
BUSYD0END
CMD5
sleep RESP CMD5
awake RESP
BUSY
Transistion phase
Sleep state Standby state
Transistion phase
Standby state
Off

RM0438 Rev 8 1835/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
1. Set the SDMMC_CK frequency in accord ance with the achievable SDMMC_CMD data
rate in Open-drain mode, CLKDIV must be set >1, and SETCLKRX must select the
sdmmc_io_in_ck.
2. Load CMD40 (GO_IRQ_STATE) in the command registers.
3. Enable wait for interrupt by setting WAITINT register bit.
4. Configure the CPSM to send a command immediately.
– This causes the CMD40 to be sent and the CPSM to be halted in the Wait state,
waiting for a interrupt service request response.
5. To exit the wait for interrupt state (CPSM Wait state):
– Upon the detection of an interrupt servic e request response start bit the CPSM
moves to the Receive state where the response is received. The complete
reception of the response is indicated by the CMDREND or the command CRC
error flags.
– To abort the interrupt mode the host clears  the WAITINT register bit, which causes
the host to send an interrupt service request response by itself. This moves the
CPSM to the Receive state. The complete reception of the response is indicated
by the CMDREND or the command CRC error flags.
Note: On a simultaneous send inte rrupt service request response start bit collision the host loses
the bus access after the transmission bit.
48.5.5 Boot operation
In boot operation mode the host can read boot data from the card by either one of the two
boot operation functions:
• Normal boot. (keeping CMD line low)
• Alternative boot (sending CMD0 with argument 0xFFFFFFFA)
The boot data can be read according the following configuration options, depending on card
register settings:
• The partition from which boot data is read (EXT_CSD Byte[179])
• The boot data size (EXT_CSD Byte[226])
• The bus configuration during boot (EXT_CSD Byte[177])
• Receiving boot acknowledgment from the card. (EXT_CSD Byte[179])
If boot acknowledgment is enabled the card send pattern 010 on SDMMC_D0 within 50ms
after boot mode has been requested by either CMD line going low or after CMD0 with
argument 0xFFFFFFFA. A boot acknowledgment timeout (ACKTIMEOUT) and
acknowledgment status (ACKFAIL) is provided.
Normal boot operation
If the SDMMC_CMD line is held low for at least 74 clock cycles after card power-up or reset,
before the first command is issued, the card recognizes that boot mode is being initiated.
Within 1 second after the CMD line goes low, the card starts to sent the first boot code data
on the SDMMC_Dn line(s). The host must keep the SDMMC_CMD line low until after all
boot data has been read. The host can terminate boot mode by pulling the SDMMC_CMD
line high.

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1836/2187 RM0438 Rev 8
[Figure 536](../figures/figure_536.md). Normal boot mode operation
To perform the normal boot procedure the following steps needed:
1. Reset the card.
2. if a boot acknowledgment is requested  enable the BOOTACKEN and set the ACKTIME
and enable the ACKFAIL and ACKTIMEOUT interrupt.
3. enable the data reception by setting th e DPSM in receive mode (DTDIR) and the
number of data bytes to be received in DATALENGTH.
4. Enable the DTIMEOUT, DATAEND, a nd CMDSENT interrupts for end of boot
command confirmation.
5. Select the normal boot operation mode in BOOTMODE, and enable boot in BOOTEN.
The boot procedure is started by enabling the CPSM with CPSMEN.This causes:
– the SDMMC_CMD to be  driven low. (BOOTMODE = normal boot).
– the ACK timeout to start.
– DPSM to be enabled.
6. The incorrect reception of the boot ac knowledgment can be detected with ACKFAIL
flag or ACKTIMEOUT flag when enabled.
– when an incorrect boot acknowledgment is received the ACKFAIL flag occurs.
– when the boot acknowledgment is not received in time the ACKTIMEOUT flag
occurs.
7. when all boot data has been received the DATAEND flag occurs.
– when data CRC fails the DCRCFAIL flag is also generated.
– when the data timeout occurs the DTIMEOUT flag is also generated.
8. When last data has been received, read data  from the FIFO until FIFO is empty after
which end of data DATAEND flag is generated.
– SDMMC has completely received all data and the DPSM is disabled.
9. The boot procedure is terminated by firmware clearing BOOTEN, which causes the
SDMMC_CMD line to go high. The CMDSENT flag is generated 56 cycles later to
indicate that a new command can be sent.
– If the boot procedure is aborted by firmw are before all data has been received the
CPSM Abort signal stops data reception and disables the DPSM which triggers an
DABORT flag when enabled.
10. The CMDSENT flag signals the end of the boot procedure and the card is ready to
receive a new command.
MSv40944V2
SDMMC_CK
S010 ESDMMC_Dn E
56 cycles min.
S Block read
+ CRC
CMD1 RESP
E
Boot completed
Block read
+ CRCS
74 cycles
50 ms max.
1 s max.
SDMMC_CMD

RM0438 Rev 8 1837/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
Alternative boot operation
After card power-up or reset, if the host send CMD0 with the argument 0xFFFFFFFA after
74 clock cycles before CMD0 is issued, the card recognizes that boot mode is being
initiated. Within 1 second after the CMD0 with argument 0xFFFFFFFA has been sent, the
card starts to send the first boot code data on the SDMMC_Dn line(s). The master
terminates boot operation by sending CMD0 (Reset).
[Figure 537](../figures/figure_537.md). Alternative boot mode operation
To perform the alternative boot procedure the following steps needed:
1. Move the SDMMC to power-off state, and reset the card.
2. Move the SDMMC to power-on state. This  guarantees the 74 SCDMMC_CK cycles to
be clocked before any command.
3. if a boot acknowledgment is requested  enable the BOOTACKEN and set the ACKTIME
and enable the ACKTIMEOUT flag.
4. enable the data reception by setting th e DPSM in receive mode (DTDIR) and the
number of data to be received in DATALENGTH. Enable the DTIMEOUT and
DATAEND flags.
5. Select the alternative boot operation mode in BOOTMODE, load the CMD0 with the
0xFFFFFFFA argument in the command registers. Enable CMDSENT flag for end of
boot command confirmation, and enable boot in BOOTEN. The boot procedure is
started by enabling the CPSM with CPSMEN. This causes:
– the loaded command and argument to be sent out. (BOOTMODE = alternative
boot).
– the ACK timeout to start.
– DPSM to be enabled.
6. When the command has been sent the CMDSEN T flag is generated, at which time the
BOOTEN bit must be cleared.
7. the reception of the boot acknowledgment  can be detected with ACKFAIL flag when
enabled.
– when the boot acknowledgment is not received in time the ACKTIMEOUT flag
occurs.
8. when all boot data has been received the DATAEND flag occurs.
– when data CRC fails the DCRCFAIL flag is also generated.
– when the data timeout occurs the DTIMEOUT flag is also generated.
MSv40945V2
SDMMC_CK
S010 ESDMMC_Dn E
56 cycles min.
S Block read
+ CRC
CMD1 RESP
E
Boot completed
Block read
+ CRCS
74 cycles
50 ms max.
1 s max.
SDMMC_CMD CMD0
reset
CMD0
boot

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1838/2187 RM0438 Rev 8
9. When last data has been received, read data  from the FIFO until FIFO is empty after
which end of data DATAEND flag is generated.
– SDMMC has completely received all data and the DPSM is disabled.
10. The BOOTEN bit must be cleared, before  terminating the boot procedure by sending
CMD0 (Reset) with BOOTMODE = alternative boot. This causes the CMDSENT flag to
occur 56 cycles after the Command.
– if the boot procedure is aborted by firmw are before all data has been received the
CPSM Abort signal stops the data transfer and disable the DPSM which triggers
an DABORT flag when enabled.
11. The CMDSENT flag signals the end of the boot procedure and the card is ready to
receive a new command. When the RESET command has been sent successfully, the
BOOTMODE control bit has to be cleared to terminate the boot operation.
48.5.6 Response R1b handling
When sending commands which have a R1b response the busy signaling is reflected in the
BUSYD0 register bit and the release of busy with the BUSYD0END flag. The SDMMC_D0
line is sampled at the end of the R1b response and signaled in the BUSYD0 register bit. The
BUSYD0 register bit is reset to not busy when the SDMMC_D0 line release busy, at the
same time the BUSYD0END flag is generated.
[Figure 538](../figures/figure_538.md). Command response R1b busy signaling
The expected maximum busy time must be set in the DATATIME register before sending the
command. When enabled, the DTIMEOUT flag is set when after the R1b response busy
stays active longer then the programmed time.
To detect the SDMMC_D0 busy signaling when sending a Command with R1b response the
following procedure applies:
• Enable CMDREND flag.
• Send Command through CPSM.
• On the CMDREND flag check the BUSYD0 register bit.
– If BUSYD0 signals not busy, signal busy release to firmware
– If BUSYD0 signals busy, wait for BUSYD0END flag
• On BUSYD0END flag signal busy released to firmware.
• On DTIMEOUT flag busy is active longer then programmed time.
MSv40946V1
SDMMC_D0
TBUSY max.
SDMMC_CMD CMD R1b CMD RESP
BUSY
BUSYD0
BUSYD0END

RM0438 Rev 8 1839/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
48.5.7 Reset and card cycle power
Reset
Following reset the SDMMC is in the reset state. In this state the SDMMC is disabled and no
command nor data can be transfered. The SDMMC_D[7:0], and SDMMC_CMD are in HiZ
and the SDMMC_CK is driven low.
Before moving to the power-on state the SDMMC must be configured.
In the power-on state the SDMMC_CK clock is running. First 74 SDMMC_CK cycles are
clocked after which the SDMMC is enabled and command and data can be transfered.
The SDMMC states are controlled by Firmware with the PWRCTL register bits according
[Figure 539](../figures/figure_539.md)..
[Figure 539](../figures/figure_539.md). SDMMC state control
Card cycle power
To perform a card cycle power the following procedure applies:
1. Reset the SDMMC with the RCC.SDMMCxRST r egister bit. This resets the SDMMC to
the reset state and the CPSM and DPSM to the Idle state.
2. Disable the Vcc power to the card.
3. Set the SDMMC in power-cycle state.  This makes that the SDMMC_D[7:0],
SDMMC_CMD and SDMMC_CK are driven low, to prevent the card from being
supplied through the signal lines.
4. After minimum 1 ms enable the Vcc power to the card.
5. After the power ramp period set the SDMM C to the power-off state for minimum 1 ms.
The SDMMC_D[7:0], SDMMC_CMD and SDMMC_CK are set to drive 1.
6. After the 1 ms delay set the SDMMC to power-on state in which the SDMMC_CK clock
is enabled.
7. After 74 SDMMC_CK cycles the first command can be sent to the card.
MSv40947V1
PWRCTRL = 11
PWRCTRL = 11
Reset
Reset
Reset
Reset
SDMMC disabled
Signals HiZ
PWRCTRL = 10
Power-cycle
SDMMC disabled
Signals drive 0
PWRCTRL = 00 Power-off
SDMMC disabled
Signals drive 1
Power-on
SDMMC disabled
Wait 74 cycles
SDMMC_CK > 74 cyles
Reset
Power-on
SDMMC enabled

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1840/2187 RM0438 Rev 8
[Figure 540](../figures/figure_540.md). Card cycle power / power up diagram
48.6 Hardware flow control
The hardware flow control during data transfer functionality is used to avoid FIFO underrun
(TX mode) and overrun (RX mode) errors.
The behavior is to stop SDMMC_CK during data transfer and freeze the SDMMC state
machines. The data transfer is stalled when the FIFO is unable to transmit or receive data.
The data transfer remains stalled until the transmit FIFO is half full or all data according
DATALENGHT has been stored, or until the receive FIFO is half empty. Only state machines
clocked by SDMMC_CK are frozen, the AHB interfaces are still alive. The FIFO can thus be
filled or emptied even if flow control is activated.
To enable hardware flow control during data transfer, the HWFC_EN register bit must be set
to 1. After reset hardware flow control is disabled.
48.7 Ultra-high-speed phase  I (UHS-I) voltage switch
UHS-I mode (SDR12, SDR25, SDR50, and DDR50) requires the support for 1.8 V signaling.
After power up the card starts in 3.3V mode. CMD11 invokes the voltage switch sequence to
MSv39275V1
SDMMC_CMD
SDMMC_Dn
SDMMC_CK
1 ms min
CMD
Card Vcc
Vcc min
Reset Power-cycle Power-on
HiZ
HiZ
0.1 ms min
Power ramp up
1 ms min
74
SDMMC_CK
clocks
Driven ‘0’
Driven ‘0’
Driven ‘0’
Power stable
SDMMC state Power-off
Driven ‘1’

RM0438 Rev 8 1841/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
the 1.8V mode. When the voltage sequence is completed successfully the card enters UHS-
I mode with default SDR12 and card input and output timings are changed.
[Figure 541](../figures/figure_541.md). CMD11 signal voltage switch sequence
To perform the signal voltage switch sequence the following steps are needed:
1. Before starting the Voltage Switch pr ocedure, the SDMMC_CK frequency must be set
in the range 100 kHz - 400 kHz.
2. The host starts the Voltage Switch proc edure by setting the VSWITCHEN bit before
sending the CMD11.
3. The card returns an R1 response.
– if the response CRC is pass, the Voltag e Switch procedure continues the host
does no longer drive the CMD and SDMMC_D[3:0] signals until completion of the
voltage switch sequence. Some cycles after the response the SDMMC_CK is
stopped and the CKSTOP flag is set.
– if the response CRC is fail (CCRCFAIL flag) or no response is received before the
timeout (CTIMEOUT flag), the Voltage Switch procedure is stopped.
4. The card drives CMD and SDMMC_D[3:0] to low at the next clock after the R1
response.
5. The host, after having received the R1 response, may monitor the SDMMC_D0 line
using the BUSYD0 register bit. The SDMMC_D0 line is sampled two SDMMC_CK
clock cycles after the Response. The Firmware may read the BUSYD0 register bit
following the CKSTOP flag.
– When the BUSYD0 is detected low the host firmware switches the Voltage
regulator to 1.8V, after which it instructs the SDMMC to start the timing critical
section of the Voltage Switch sequence by setting register bit VSWITCH. The
hardware continues to stop the SDMMC_CK by holding it low for at least 5 ms.
– When the BUSYD0 is detected high the host aborts the Voltage Switch sequence
and cycle power the card.
6. The card after detecting SDMMC_CK low beg ins switching signaling voltage to 1.8 V.
7. The host SDMMC hardware after at least 5 ms restarts the SDMMC_CK.
8. The card within 1 ms from detecting SDMMC _CK transition drives CMD and DAT[3:0]
high for at least 1 SDMMC_CK cycle and then stop driving CMD and DAT[3:0].
9. The host SDMMC hardware, 1 ms after the SDMMC_CK has been restarted, the
SDMMC_D0 is sampled into BUSYD0 and the VSWEND flag is set.
MSv40950V1
SDMMC_CK
SDMMC_CMD
SDMMC_D[3:0]
Provide SD clock at 3.3 V
3.3 V
0 V
Provide SD clock at 1.8 V
5 ms min.
3.3 V
0 V CMD11 R1
1.8 V
1.8 V
3.3 V
0 V
1.8 V
0 min.
1 ms max.

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1842/2187 RM0438 Rev 8
10. The host, on the VSWEND flag, checks SDMMC_D0 line using the BUSYD0 register
bit, to confirm completion of voltage switch sequence:
– When BUSYD0 is detected high, Voltage Switch has been completed successfully.
– When BUSYD0 is detected low, Voltage Switch has failed, the host cycles the card
power.
The minimum 5 ms time to stop the SDMMC_CK is derived from the internal un-gated
SDMMC_CK clock, which has a maximum frequency of 25 MHz (SD mode), as set by the
clock divider CLKDIV. The >5 ms time is counted by 212 cycles (10.24 ms @ 400 kHz). If a
lower SDMMC_CK frequency is selected by the clock divider CLKDIV the time for the
SDMMC_CK clock to be stopped is longer.
The maximum 1 ms time for the card to drive the SDMMC_Dn and SDMMC_CMD lines high
is derived from the internal ungated SDMMC_CK which has a maximum frequency of
25 MHz (SD mode), as set by the clock divider CLKDIV. The SDMMC checks the lines after
>1 ms time which is counted by 29 cycles (1.28 ms @ 25 MHz). If a lower SDMMC_CK
frequency is selected by the clock divider CLKDIV the time to check the lines is longer.
The signal voltage level is supported through an external voltage translation transceiver like
STMicroelectronics ST6G3244ME.

RM0438 Rev 8 1843/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
[Figure 542](../figures/figure_542.md). Voltage switch transceiver typical application
To interface with an external driver (a voltage switch transceiver), next to the standard
signals the SDMMC uses the following signals:
• SDMMC_CKIN feedback input clock
• SDMMC_CDIR I/O direction control for the CMD signal
• SDMMC_D0DIR I/O direction control for the SDMMC_D0 signal
• SDMMC_D123DIR I/O direction control for the SDMMC_D1, SDMMC_D2 and
SDMMC_D3 signals
The voltage transceiver signals EN and SEL are to be handled through general-purpose
I/O.
The polarity of the SDMMC_CDIR, SDMMC_D0DIR and SDMMC_D123DIR signals can be
selected through SDMMC_POWER.DIRPOL control bit.
48.8 SDMMC interrupts
MSv40951V2
SDMMC_CK
SD Host
SDMMC
SDMMC_CKIN
SDMMC_CDIR
SDMMC_CMD
SDMMC_D0DIR
SDMMC_D0
SDMMC_D123DIR
SDMMC_D1
SDMMC_D2
SDMMC_D3
GPIO
GPIO
Voltage transceiver
DAT123.dir
CLK.h
CLK-f
CMD.dir
CMD.h
DAT0.dir
DAT0.h
DAT1.h
DAT2.h
DAT3.h
Level converter
CMDB
SD Card
CLKB
DAT0B
DAT1B
DAT2B
DAT3B
SEL
EN

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1844/2187 RM0438 Rev 8
[Table 405](../tables/table_405.md). SDMMC interrupts
Interrupt
acronym Interrupt event Event flag Enable control
bit
Interrupt clear
method
Exit from
Sleep
mode
SDMMC Command response CRC fail CCRCFAIL CCRCFAILIE CCRCFAILC Yes
SDMMC Data block CRC fail DCRCFAIL DCRCFAILIE DCRCFAILC Yes
SDMMC Command response timeout C TIMEOUT CTIMEOUTIE CTIMEOUTC Yes
SDMMC Data timeout DTIMEOU T DTIMEOUTIE DTIMEOUTC Yes
SDMMC Transmit FIFO underrun TXUNDERR TXUNDERRIE TXUNDERRC Yes
SDMMC Receive FIFO overrun R XOVERR RXOVERRIE RXOVERRC Yes
SDMMC Command reponse receiv ed CMDREND CMDRENDIE CMDRENDC Yes
SDMMC Comand sent CMDSENT CMDSENTIE CMDSENTC Yes
SDMMC Data transfer ended DATAEND DATAENDIE DATAENDC Yes
SDMMC Data transfer hold DHOLD DHOLDIE DHOLDC Yes
SDMMC Data block sent or receiv ed DBCKEND DBCKENDIE DBCKENDC Yes
SDMMC Data transfer aborted DABORT DABORTIE DABORTC Yes
SDMMC Transmit FIFO half empty TXFIFOHE TXFIFOHEIE N/A Yes
SDMMC Receive FIFO half full RXFIFOHF RXFIFOHFIE N/A Yes
SDMMC Transmit FIFO full TXFIFOF N/A N/A Yes
SDMMC Receive FIFO full RXFIFOF RXFIFOFIE N/A Yes
SDMMC Transmit FIFO empty TXFIFOE TXFIFOEIE N/A Yes
SDMMC Receive FIFO empty RXFIFOE N/A N/A Yes
SDMMC Command response end of busy BUSYD0END BUSYD0ENDIE BUSYD0ENDC Yes
SDMMC SDIO interrupt SDIOIT SDIOITIE SDIOITC Yes
SDMMC Boot acknowledgment fail ACKFAIL ACKFAILIE ACKFAILC Yes
SDMMC Boot acknowledgment timeout ACK TIMEOUT ACKTIMEOUTIE ACKTIMEOUTC Yes
SDMMC Voltage switch timing VSWEND VSWENDIE VSWENDC Yes
SDMMC SDMM_CK stopped in voltage
switch CKSTOP CKSTOPIE CKSTOPC Yes
SDMMC IDMA transfer error IDMATE IDMATEIE IDMATEC Yes
SDMMC IDMA buffer transfer comp lete IDMABTC IDMABTCIE IDMABTCC Yes

RM0438 Rev 8 1845/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
48.9 SDMMC registers
The device communicates to the system via 32-bit control registers accessible via AHB
slave interface.
The peripheral registers have to be accessed by words (32-bit). Byte (8-bit) and half-word
(16-bit) accesses trigger an AHB bus error.
48.9.1 SDMMC power control register (SDMMC_POWER)
Address offset: 0x000
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. DIR
POL
VSWI
TCHEN
VSWI
TCH PWRCTRL[1:0]
rw rw rw rw rw
Bits 31:5 Reserved, must be kept at reset value.
Bit 4 DIRPOL: Data and command direction signals polarity selection
This bit can only be written when the SDMMC is in the power-off state (PWRCTRL = 00).
0: Voltage transceiver I/Os driven as output when direction signal is low.
1: Voltage transceiver I/Os driven as output when direction signal is high.
Bit 3 VSWITCHEN: Voltage switch procedure enable
This bit can only be written by firmware when CPSM is disabled (CPSMEN = 0).
This bit is used to stop the SDMMC_CK after the voltage switch command response:
0: SDMMC_CK clock kept unchanged after successfully received command response.
1: SDMMC_CK clock stopped after successfully received command response.
Bit 2 VSWITCH: Voltage switch sequence start
This bit is used to start the timing critical section of the voltage switch sequence:
0: Voltage switch sequence not started and not active.
1: Voltage switch sequence started or active.
Bits 1:0 PWRCTRL[1:0]: SDMMC state control bits
These bits can only be written when the SDMMC is not in the power-on state
(PWRCTRL ≠ 11).
These bits are used to define the functional state of the SDMMC signals:
00: After reset, Reset: the SDMMC is disabl ed and the clock to the Card is stopped,
SDMMC_D[7:0], and SDMMC_CMD are HiZ and SDMMC_CK is driven low.
When written 00, power-off: the SDMMC is disabled and the clock to the card is
stopped, SDMMC_D[7:0], SDMMC_CMD and SDMMC_CK are driven high.
01: Reserved (When written 01, PWRCTRL value does not change)
10: Power-cycle, the SDMMC is disabled and  the clock to the card is stopped,
SDMMC_D[7:0], SDMMC_CMD and SDMMC_CK are driven low.
11: Power-on: the card is clocked, The first 74 SDMMC_CK cycles the SDMMC is still
disabled. After the 74 cycles the SDMMC is enabled and the SDMMC_D[7:0],
SDMMC_CMD and SDMMC_CK are controlled according the SDMMC operation.
Any further write is ignored, PWRCTRL value keeps 11.

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1846/2187 RM0438 Rev 8
48.9.2 SDMMC clock control register (SDMMC_CLKCR)
Address offset: 0x004
Reset value: 0x0000 0000
This register controls the SDMMC_CK output clock, the sdmmc_rx_ck receive clock, and
the bus width.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. SELCLKRX[1:0] BUS
SPEED DDR HWFC
_EN
NEG
EDGE
rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
WID
BUS[1:0] Res. PWR
SAV Res. Res. CLKDIV[9:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:22 Reserved, must be kept at reset value.
Bits 21:20 SELCLKRX[1:0]: Receive clock selection
These bits can only be written when the CPSM and DPSM are not active (CPSMACT = 0
and DPSMACT = 0)
00: sdmmc_io_in_ck selected as receive clock
01: SDMMC_CKIN feedback clock selected as receive clock
10: Reserved
11: Reserved (select sdmmc_io_in_ck)
Bit 19 BUSSPEED: Bus speed for selection of SDMMC operating modes
This bit can only be written when the CPSM and DPSM are not active (CPSMACT = 0 and
DPSMACT = 0)
0: DS, HS, SDR12, SDR25, Legacy compatible, High speed SDR, High speed DDR bus
speed mode selected
1: SDR50, DDR50 bus speed mode selected
Bit 18 DDR: Data rate signaling selection
This bit can only be written when the CPSM and DPSM are not active (CPSMACT = 0 and
DPSMACT = 0)
DDR rate must only be selected with 4-bit or 8-bit wide bus mode. (WIDBUS > 00). DDR = 1
has no effect when WIDBUS = 00 (1-bit wide bus).
DDR rate must only be selected with clock division > 1 (CLKDIV > 0).
0: SDR Single data rate signaling
1: DDR double data rate signaling
Bit 17 HWFC_EN: Hardware flow control enable
This bit can only be written when the CPSM and DPSM are not active (CPSMACT = 0 and
DPSMACT = 0)
0: Hardware flow control is disabled
1: Hardware flow control is enabled
When Hardware flow control is enabled, the meaning of the TXFIFOE and RXFIFOF flags
change, see SDMMC status register definition in Section 48.9.11.

RM0438 Rev 8 1847/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
Bit 16 NEGEDGE: SDMMC_CK dephasing selection bit for data and command
This bit can only be written when the CPSM and DPSM are not active (CPSMACT = 0 and
DPSMACT = 0).
When clock division = 1 (CLKDIV = 0), this bit has no effect. Data and Command change on
SDMMC_CK falling edge.
0:When clock division >1 (CLKDIV > 0) and DDR = 0:
– Command and data changed on the sdmmc_ker_ck falling edge succeeding the rising
edge of SDMMC_CK.
– SDMMC_CK edge occurs on sdmmc_ker_ck rising edge.
When clock division >1 (CLKDIV > 0) and DDR = 1:
– Command changed on the sdmmc_ker_ck fa lling edge succeeding the rising edge of
SDMMC_CK.
– Data changed on the sdmmc_ker_ck falling edge succeeding a SDMMC_CK edge.
– SDMMC_CK edge occurs on sdmmc_ker_ck rising edge.
1: When clock division >1 (CLKDIV > 0) and DDR = 0:
– Command and data changed on the same sdmmc_ker_ck rising edge generating the
SDMMC_CK falling edge.
When clock division >1 (CLKDIV > 0) and DDR = 1:
– Command changed on the same sdmmc_ker_ck rising edge generating the
SDMMC_CK falling edge.
– Data changed on the SDMMC_CK falling edge succeeding a SDMMC_CK edge.
– SDMMC_CK edge occurs on sdmmc_ker_ck rising edge.
Bits 15:14 WIDBUS[1:0]: Wide bus mode enable bit
This bit can only be written when the CPSM and DPSM are not active (CPSMACT = 0 and
DPSMACT = 0)
00: Default 1-bit wide bus mode: SDMMC_D0 used (Does not support DDR)
01: 4-bit wide bus mode: SDMMC_D[3:0] used
10: 8-bit wide bus mode: SDMMC_D[7:0] used
Bit 13 Reserved, must be kept at reset value.
Bit 12 PWRSAV: Power saving configuration bit
This bit can only be written when the CPSM and DPSM are not active (CPSMACT = 0 and
DPSMACT = 0)
For power saving, the SDMMC_CK clock output can be disabled when the bus is idle by
setting PWRSAV:
0: SDMMC_CK clock is always enabled
1: SDMMC_CK is only enabled when the bus is active
Bits 11:10 Reserved, must be kept at reset value.
Bits 9:0 CLKDIV[9:0]: Clock divide factor
This bit can only be written when the CPSM and DPSM are not active (CPSMACT = 0 and
DPSMACT = 0).
This field defines the divide factor between the input clock (sdmmc_ker_ck) and the output
clock (SDMMC_CK): SDMMC_CK frequency = sdmmc_ker_ck / [2 * CLKDIV].
0x000: SDMMC_CK frequency = sdmmc_ker_ck / 1 (Does not support DDR)
0x001: SDMMC_CK frequency = sdmmc_ker_ck / 2
0x002: SDMMC_CK frequency = sdmmc_ker_ck / 4
0x0XX: ..
0x080: SDMMC_CK frequency = sdmmc_ker_ck / 256
0xXXX: ..
0x3FF: SDMMC_CK frequency = sdmmc_ker_ck / 2046

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1848/2187 RM0438 Rev 8
Note: While the SD/SDIO card or e•MMC is in  identification mode, the SDMMC_CK frequency
must be less than 400 kHz.
The clock frequency can be changed to the maximum card bus frequency when relative
card addresses are assigned to all cards.
At least seven sdmmc_hclk clock periods are needed between two write accesses to this
register. SDMMC_CK can also be stopped during the Read Wait interval for SD I/O cards: in
this case the SDMMC_CLKCR register does not control SDMMC_CK.
48.9.3 SDMMC argument register (SDMMC_ARGR)
Address offset: 0x008
Reset value: 0x0000 0000
This register contains a 32-bit command argument, which is sent to a card as part of a
command message.
48.9.4 SDMMC command re gister (SDMMC_CMDR)
Address offset: 0x00C
Reset value: 0x0000 0000
This register contains the command index and command type bits. The command index is
sent to a card as part of a command message. The command type bits control the
command path state machine (CPSM).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
CMDARG[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CMDARG[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 CMDARG[31:0]: Command argument
These bits can only be written by firmware when CPSM is disabled (CPSMEN = 0).
Command argument sent to a card as part of a command message. If a command contains
an argument, it must be loaded into this register before writing a command to the command
register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res.
CMD
SUS
PEND
rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
BOOT
EN
BOOT
MODE
DT
HOLD
CPSM
EN
WAITP
END
WAIT
INT WAITRESP[1:0] CMD
STOP
CMD
TRANS CMDINDEX[5:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 1849/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
Bits 31:17 Reserved, must  be kept at reset value.
Bit 16 CMDSUSPEND: The CPSM treats the command as a Suspend or Resume command and
signals interrupt period start/end
This bit can only be written by firmware when CPSM is disabled (CPSMEN = 0).
CMDSUSPEND = 1 and CMDTRANS = 0 Suspend command, start interrupt period when
response bit BS = 0.
CMDSUSPEND = 1 and CMDTRANS = 1 Resume command with data, end interrupt period
when response bit DF = 1.
Bit 15 BOOTEN: Enable boot mode procedure
0: Boot mode procedure disabled
1: Boot mode procedure enabled
Bit 14 BOOTMODE: Select the boot mode procedure to be used
This bit can only be written by firmware when CPSM is disabled (CPSMEN = 0)
0: Normal boot mode procedure selected
1: Alternative boot mode procedure selected
Bit 13 DTHOLD: Hold new data block transmission and reception in the DPSM
If this bit is set, the DPSM does not move from the Wait_S state to the Send state or from the
Wait_R state to the Receive state.
Bit 12 CPSMEN: Command path state machine (CPSM) enable bit
This bit is written 1 by firmware, and cleared by hardware when the CPSM enters the Idle
state.
If this bit is set, the CPSM is enabled.
When DTEN = 1, no command is transfered nor boot procedure is started. CPSMEN is
cleared to 0.
During Read Wait with SDMMC_CK stopped no command is sent and CPSMEN is kept 0.
Bit 11 WAITPEND: CPSM waits for end of data transfer (CmdPend internal signal) from DPSM
This bit when set, the CPSM waits for the end of data transfer trigger before it starts sending
a command.
WAITPEND is only taken into account when DTMODE = e•MMC stream data transfer,
WIDBUS = 1-bit wide bus mode, DPSMACT = 1 and DTDIR = from host to card.
Bit 10 WAITINT: CPSM waits for interrupt request
If this bit is set, the CPSM disables command timeout and waits for an card interrupt request
(Response).
If this bit is cleared in the CPSM Wait state, it causes the abort of the interrupt mode.
Bits 9:8 WAITRESP[1:0]: Wait for response bits
This bit can only be written by firmware when CPSM is disabled (CPSMEN = 0).
They are used to configure whether the CPSM is to wait for a response, and if yes, which
kind of response.
00: No response, expect CMDSENT flag
01: Short response, expect CMDREND or CCRCFAIL flag
10: Short response, expect CMDREND flag (No CRC)
11: Long response, expect CMDREND or CCRCFAIL flag

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1850/2187 RM0438 Rev 8
Note: 1 At least seven sdmmc_hclk clock periods ar e needed between two write accesses to this
register.
2 MultiMediaCard can send two kinds of resp onse: short responses, 48 bits, or long
responses,136 bits. SD card and SD I/O card can send only short responses, the argument
can vary according to the type of response: the software distinguishes the type of response
according to the send command.
48.9.5 SDMMC command response register (SDMMC_RESPCMDR)
Address offset: 0x010
Reset value: 0x0000 0000
This register contains the command index field of the last command response received. If
the command response transmission does not contain the command index field (long or
OCR response), the RESPCMD field is unknown, although it must contain 111111b (the
value of the reserved field from the response).
Bit 7 CMDSTOP: The CPSM treats the command as a Stop Transmission command and signals
abort to the DPSM
This bit can only be written by firmware when CPSM is disabled (CPSMEN = 0).
If this bit is set, the CPSM issues the abort signal to the DPSM when the command is sent.
Bit 6 CMDTRANS: The CPSM treats the command as a data transfer command, stops the interrupt
period, and signals DataEnable to the DPSM
This bit can only be written by firmware when CPSM is disabled (CPSMEN = 0).
If this bit is set, the CPSM issues an end of interrupt period and issues DataEnable signal to
the DPSM when the command is sent.
Bits 5:0 CMDINDEX[5:0]: Command index
This bit can only be written by firmware when CPSM is disabled (CPSMEN = 0).
The command index is sent to the card as part of a command message.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. RESPCMD[5:0]
rrrrrr
Bits 31:6 Reserved, must be kept at reset value.
Bits 5:0 RESPCMD[5:0]: Response command index
Read-only bitfield. Contains the command index of the last command response received.

RM0438 Rev 8 1851/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
48.9.6 SDMMC response x re gister (SDMMC_RESPxR)
Address offset: 0x010 + 0x004 * x, (x = 1 to 4)
Reset value: 0x0000 0000
These registers contain the status of a card, which is part of the received response.
The card status size is 32 or 128 bits, depending on the response type.
48.9.7 SDMMC data timer register (SDMMC_DTIMER)
Address offset: 0x024
Reset value: 0x0000 0000
This register contains the data timeout period, in card bus clock periods.
A counter loads the value from this register, and starts decrementing when the data path
state machine (DPSM) enters the Wait_R or Busy state. If the timer reaches 0 while the
DPSM is in either of these states, the timeout status flag is set.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
CARDSTATUS[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CARDSTATUS[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 CARDSTATUS[31:0]: Card status according table below
See [Table 406](../tables/table_406.md).
[Table 406](../tables/table_406.md). Response type and SDMMC_RESPxR registers
Register(1)
1. The most significant bit of t he card status is received first.
Short response Long response
SDMMC_RESP1R Card st atus[31:0] Card status [127:96]
SDMMC_RESP2R all 0 Card status [95:64]
SDMMC_RESP3R all 0 Card status [63:32]
SDMMC_RESP4R all 0 Card status [31:0] (2)
2. The SDMMC_RESP4R register LSB is always 0.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
DATATIME[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DATATIME[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1852/2187 RM0438 Rev 8
Note: A data transfer must be written to the data timer register and the data length register before
being written to the data control register.
48.9.8 SDMMC data length register (SDMMC_DLENR)
Address offset: 0x028
Reset value: 0x0000 0000
This register contains the number of data bytes to be transferred. The value is loaded into
the data counter when data transfer starts.
Note: For a block data transfer, the value in the data  length register must be a multiple of the block
size (see SDMMC_DCTRL). A data transfer must be written to the data timer register and
the data length register before being written to the data control register.
For an SDMMC multibyte transfer the value in the data length register must be between 1
and 512.
Bits 31:0 DATATIME[31:0]: Data and R1b busy timeout period
This bit can only be written when the CPSM and DPSM are not active (CPSMACT = 0 and
DPSMACT = 0).
Data and R1b busy timeout period expressed in card bus clock periods.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. DATALENGTH[24:16]
rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DATALENGTH[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:25 Reserved, must be kept at reset value.
Bits 24:0 DATALENGTH[24:0]: Data length value
This register can only be written by firmware when DPSM is inactive (DPSMACT = 0).
Number of data bytes to be transferred.
When DDR = 1 DATALENGTH is truncated to a multiple of 2. (The last odd byte is not
transfered)
When DATALENGTH = 0 no data are transfered, when requested by a CPSMEN and
CMDTRANS = 1 also no command is transfered. DTEN and CPSMEN are cleared to 0.

RM0438 Rev 8 1853/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
48.9.9 SDMMC data control register (SDMMC_DCTRL)
Address offset: 0x02C
Reset value: 0x0000 0000
This register controls the data path state machine (DPSM).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. FIFO
RST
BOOT
ACK
EN
SDIO
EN
RW
MOD
RW
STOP
RW
START DBLOCKSIZE[3:0] DTM ODE[1:0] DTDIR DTEN
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:14 Reserved, must be kept at reset value.
Bit 13 FIFORST: FIFO reset, flushes any remaining data
This bit can only be written by firmware when IDMAEN= 0 and DPSM is active
(DPSMACT = 1). This bit only takes effect when a transfer error or transfer hold occurs.
0: FIFO not affected.
1: Flush any remaining data and reset the FIFO pointers. This bit is automatically cleared to
0 by hardware when DPSM gets inactive (DPSMACT = 0).
Bit 12 BOOTACKEN: Enable the reception of the boot acknowledgment
This bit can only be written by firmware when DPSM is inactive (DPSMACT = 0).
0: Boot acknowledgment disabled, not expected to be received
1: Boot acknowledgment enabled, expected to be received
Bit 11 SDIOEN: SD I/O interrupt enable functions
This bit can only be written by firmware when DPSM is inactive (DPSMACT = 0).
If this bit is set, the DPSM enables the SD I/O card specific interrupt operation.
Bit 10 RWMOD: Read Wait mode
This bit can only be written by firmware when DPSM is inactive (DPSMACT = 0).
0: Read Wait control using SDMMC_D2
1: Read Wait control stopping SDMMC_CK
Bit 9 RWSTOP: Read Wait stop
This bit is written by firmware and auto cleared by hardware when the DPSM moves from the
R_W state to the Wait_R or Idle state.
0: No Read Wait stop
1: Enable for Read Wait stop when DPSM is in the R_W state.
Bit 8 RWSTART: Read Wait start
If this bit is set, Read Wait operation starts.

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1854/2187 RM0438 Rev 8
48.9.10 SDMMC data counter  register (SDMMC_DCNTR)
Address offset: 0x030
Reset value: 0x0000 0000
This register loads the value from the data length register (see SDMMC_DLENR) when the
DPSM moves from the Idle state to the Wait_R or Wait_S state. As data is transferred, the
counter decrements the value until it reaches 0. The DPSM then moves to the Idle state and
Bits 7:4 DBLOCKSIZE[3:0]: Data block size
This bit can only be written by firmware when DPSM is inactive (DPSMACT = 0).
Define the data block length when the block data transfer mode is selected:
0000: Block length = 20 = 1 byte
0001: Block length = 21 = 2 bytes
0010: Block length = 22 = 4 bytes
0011: Block length = 23 = 8 bytes
0100: Block length = 24 = 16 bytes
0101: Block length = 25 = 32 bytes
0110: Block length = 26 = 64 bytes
0111: Block length = 27 = 128 bytes
1000: Block length = 28 = 256 bytes
1001: Block length = 29 = 512 bytes
1010: Block length = 210 = 1024 bytes
1011: Block length = 211 = 2048 bytes
1100: Block length = 212 = 4096 bytes
1101: Block length = 213 = 8192 bytes
1110: Block length = 214 = 16384 bytes
1111: Reserved
When DATALENGTH is not a multiple of DBLOCKSIZE, the transfered data is truncated at a
multiple of DBLOCKSIZE. (None of the remaining data are transfered.)
When DDR = 1, DBLOCKSIZE = 0000 must not be used. (No data are transfered)
Bits 3:2 DTMODE[1:0]: Data transfer mode selection
This bit can only be written by firmware when DPSM is inactive (DPSMACT = 0).
00: Block data transfer ending on block count.
01: SDIO multibyte data transfer.
10: e•MMC Stream data transfer. (WIDBUS must select 1-bit wide bus mode)
11: Block data transfer ending with STOP_TRANSMISSION command (not to be used with
DTEN initiated data transfers).
Bit 1 DTDIR: Data transfer direction selection
This bit can only be written by firmware when DPSM is inactive (DPSMACT = 0).
0: From host to card.
1: From card to host.
Bit 0 DTEN: Data transfer enable bit
This bit can only be written by firmware when DPSM is inactive (DPSMACT = 0). This bit is
cleared by hardware when data transfer completes.
This bit must only be used to transfer data when no associated data transfer command is
used (must not be used with SD or e•MMC cards).
0: Do not start data transfer without CPSM data transfer command.
1: Start data transfer without CPSM data transfer command.

RM0438 Rev 8 1855/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
when there has been no error, and no transmit data transfer hold, the data status end flag
(DATAEND) is set.
Note: This register must be read only after the data transfer is complete, or hold. When reading
after an error event the read data count value may be different from the real number of data
bytes transfered.
48.9.11 SDMMC status register (SDMMC_STAR)
Address offset: 0x034
Reset value: 0x0000 0000
This register is a read-only register. It contains two types of flag:
• Static flags (bits [28, 21, 11:0]): these bits remain asserted until they are cleared by
writing to the SDMMC interrupt Clear register (see SDMMC_ICR)
• Dynamic flags (bits [20:12]): these bits change state depending on the state of the
underlying logic (for example, FIFO full and empty flags are asserted and deasserted
as data while written to the FIFO)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. DATACOUNT[24:16]
rrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DATACOUNT[15:0]
rrrrrrrrrrrrrrrr
Bits 31:25 Reserved, must be kept at reset value.
Bits 24:0 DATACOUNT[24:0]: Data count value
When read, the number of remaining data bytes to be transferred is returned. Write has no
effect.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. IDMA
BTC
IDMA
TE
CK
STOP
VSW
END
ACK
TIME
OUT
ACK
FAIL SDIOIT BUSY
D0END
BUSY
D0
RX
FIFOE
TX
FIFOE
RX
FIFOF
TX
FIFOF
rrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
RX
FIFO
HF
TX
FIFO
HE
CPSM
ACT
DPSM
ACT
DA
BORT
DBCK
END DHOLD DATA
END
CMD
SENT
CMDR
END
RX
OVERR
TX
UNDER
R
D
TIME
OUT
C
TIME
OUT
DCRC
FAIL
CCRC
FAIL
rrrrrrrrrrrrrrrr
Bits 31:29 Reserved, must  be kept at reset value.
Bit 28 IDMABTC: IDMA buffer transfer complete
The interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 27 IDMATE: IDMA transfer error
The interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 26 CKSTOP: SDMMC_CK stopped in Voltage switch procedure
The interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1856/2187 RM0438 Rev 8
Bit 25 VSWEND: Voltage switch critical timing section completion
The interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 24 ACKTIMEOUT: Boot acknowledgment timeout
The interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 23 ACKFAIL: Boot acknowledgment received (boot acknowledgment check fail)
The interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 22 SDIOIT: SDIO interrupt received
The interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 21 BUSYD0END: end of SDMMC_D0 Busy following a CMD response detected
This indicates only end of busy following a CMD response. This bit does not signal busy due
to data transfer. Interrupt flag is cleared by writing corresponding interrupt clear bit in
SDMMC_ICR.
0: card SDMMC_D0 signal does NOT signal change from busy to not busy.
1: card SDMMC_D0 signal changed from busy to NOT busy.
Bit 20 BUSYD0: Inverted value of SDMMC_D0 line (Busy), sampled at the end of a CMD response
and a second time 2 SDMMC_CK cycles after the CMD response
This bit is reset to not busy when the SDMMCD0 line changes from busy to not busy. This bit
does not signal busy due to data transfer. This is a hardware status flag only, it does not
generate an interrupt.
0: card signals not busy on SDMMC_D0.
1: card signals busy on SDMMC_D0.
Bit 19 RXFIFOE: Receive FIFO empty
This is a hardware status flag only, does not generate an interrupt. This bit is cleared when
one FIFO location becomes full.
Bit 18 TXFIFOE: Transmit FIFO empty
This bit is cleared when one FIFO location becomes full.
Bit 17 RXFIFOF: Receive FIFO full
This bit is cleared when one FIFO location becomes empty.
Bit 16 TXFIFOF: Transmit FIFO full
This is a hardware status flag only, does not generate an interrupt. This bit is cleared when
one FIFO location becomes empty.
Bit 15 RXFIFOHF: Receive FIFO half full
There are at least half the number of words in the FIFO. This bit is cleared when the FIFO
becomes half+1 empty.
Bit 14 TXFIFOHE: Transmit FIFO half empty
At least half the number of words can be written into the FIFO. This bit is cleared when the
FIFO becomes half+1 full.
Bit 13 CPSMACT: Command path state machine active (not in Idle state)
This is a hardware status flag only, does not generate an interrupt.
Bit 12 DPSMACT: Data path state machine active (not in Idle state)
This is a hardware status flag only, does not generate an interrupt.
Bit 11 DABORT: Data transfer aborted by CMD12
Interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.

RM0438 Rev 8 1857/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
Note: FIFO interrupt flags mu st be masked in SDMMC_MASKR when using IDMA mode.
Bit 10 DBCKEND: Data block sent/received
DBCKEND is set when:
- CRC check passed and DPSM moves to the R_W state
or
- IDMAEN = 0 and transmit data transfer hold and DATACOUNT >0 and DPSM moves to
Wait_S.
Interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 9 DHOLD: Data transfer Hold
Interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 8 DATAEND: Data transfer ended correctly
DATAEND is set if data counter DATACOUNT is zero and no errors occur, and no transmit
data transfer hold.
Interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 7 CMDSENT: Command sent (no response required)
Interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 6 CMDREND: Command response received (CRC check passed, or no CRC)
Interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 5 RXOVERR: Received FIFO overrun error
Interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 4 TXUNDERR: Transmit FIFO underrun error
Interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 3 DTIMEOUT: Data timeout
Interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 2 CTIMEOUT: Command response timeout
Interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
The Command Timeout period has a fixed value of 64 SDMMC_CK clock periods.
Bit 1 DCRCFAIL: Data block sent/received (CRC check failed)
Interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.
Bit 0 CCRCFAIL: Command response received (CRC check failed)
Interrupt flag is cleared by writing corresponding interrupt clear bit in SDMMC_ICR.

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1858/2187 RM0438 Rev 8
48.9.12 SDMMC interrupt cl ear register (SDMMC_ICR)
Address offset: 0x038
Reset value: 0x0000 0000
This register is a write-only register. Writing a bit with 1 clears the corresponding bit in the
SDMMC_STAR status register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. IDMA
BTCC
IDMA
TEC
CK
STOPC
VSW
ENDC
ACK
TIME
OUTC
ACK
FAILC
SDIO
ITC
BUSY
D0
ENDC
Res. Res. Res. Res. Res.
rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res.
D
ABORT
C
DBCK
ENDC
DHOLD
C
DATA
ENDC
CMD
SENTC
CMDR
ENDC
RX
OVERR
C
TX
UNDER
RC
D
TIME
OUTC
C
TIME
OUTC
DCRC
FAILC
CCRC
FAILC
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:29 Reserved, must  be kept at reset value.
Bit 28 IDMABTCC: IDMA buffer transfer complete clear bit
Set by software to clear the IDMABTC flag.
0: IDMABTC not cleared
1: IDMABTC cleared
Bit 27 IDMATEC: IDMA transfer error clear bit
Set by software to clear the IDMATE flag.
0: IDMATE not cleared
1: IDMATE cleared
Bit 26 CKSTOPC: CKSTOP flag clear bit
Set by software to clear the CKSTOP flag.
0: CKSTOP not cleared
1: CKSTOP cleared
Bit 25 VSWENDC: VSWEND flag clear bit
Set by software to clear the VSWEND flag.
0: VSWEND not cleared
1: VSWEND cleared
Bit 24 ACKTIMEOUTC: ACKTIMEOUT flag clear bit
Set by software to clear the ACKTIMEOUT flag.
0: ACKTIMEOUT not cleared
1: ACKTIMEOUT cleared
Bit 23 ACKFAILC: ACKFAIL flag clear bit
Set by software to clear the ACKFAIL flag.
0: ACKFAIL not cleared
1: ACKFAIL cleared
Bit 22 SDIOITC: SDIOIT flag clear bit
Set by software to clear the SDIOIT flag.
0: SDIOIT not cleared
1: SDIOIT cleared

RM0438 Rev 8 1859/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
Bit 21 BUSYD0ENDC: BUSYD0END flag clear bit
Set by software to clear the BUSYD0END flag.
0: BUSYD0END not cleared
1: BUSYD0END cleared
Bits 20:12 Reserved, must  be kept at reset value.
Bit 11 DABORTC: DABORT flag clear bit
Set by software to clear the DABORT flag.
0: DABORT not cleared
1: DABORT cleared
Bit 10 DBCKENDC: DBCKEND flag clear bit
Set by software to clear the DBCKEND flag.
0: DBCKEND not cleared
1: DBCKEND cleared
Bit 9 DHOLDC: DHOLD flag clear bit
Set by software to clear the DHOLD flag.
0: DHOLD not cleared
1: DHOLD cleared
Bit 8 DATAENDC: DATAEND flag clear bit
Set by software to clear the DATAEND flag.
0: DATAEND not cleared
1: DATAEND cleared
Bit 7 CMDSENTC: CMDSENT flag clear bit
Set by software to clear the CMDSENT flag.
0: CMDSENT not cleared
1: CMDSENT cleared
Bit 6 CMDRENDC: CMDREND flag clear bit
Set by software to clear the CMDREND flag.
0: CMDREND not cleared
1: CMDREND cleared
Bit 5 RXOVERRC: RXOVERR flag clear bit
Set by software to clear the RXOVERR flag.
0: RXOVERR not cleared
1: RXOVERR cleared
Bit 4 TXUNDERRC: TXUNDERR flag clear bit
Set by software to clear TXUNDERR flag.
0: TXUNDERR not cleared
1: TXUNDERR cleared
Bit 3 DTIMEOUTC: DTIMEOUT flag clear bit
Set by software to clear the DTIMEOUT flag.
0: DTIMEOUT not cleared
1: DTIMEOUT cleared

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1860/2187 RM0438 Rev 8
48.9.13 SDMMC mask re gister (SDMMC_MASKR)
Address offset: 0x03C
Reset value: 0x0000 0000
This register determines which status flags generate an interrupt request by setting the
corresponding bit to 1.
Bit 2 CTIMEOUTC: CTIMEOUT flag clear bit
Set by software to clear the CTIMEOUT flag.
0: CTIMEOUT not cleared
1: CTIMEOUT cleared
Bit 1 DCRCFAILC: DCRCFAIL flag clear bit
Set by software to clear the DCRCFAIL flag.
0: DCRCFAIL not cleared
1: DCRCFAIL cleared
Bit 0 CCRCFAILC: CCRCFAIL flag clear bit
Set by software to clear the CCRCFAIL flag.
0: CCRCFAIL not cleared
1: CCRCFAIL cleared
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. IDMA
BTCIE Res.
CK
STOP
IE
VSW
ENDIE
ACK
TIME
OUTIE
ACK
FAILIE
SDIO
ITIE
BUSY
D0
ENDIE
Res. Res.
TX
FIFO
EIE
RX
FIFO
FIE
Res.
rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
RX
FIFO
HFIE
TX
FIFO
HEIE
Res. Res.
DA
BORT
IE
DBCK
ENDIE
DHOLD
IE
DATA
ENDIE
CMD
SENT
IE
CMDR
ENDIE
RX
OVER
RIE
TX
UNDER
RIE
D
TIME
OUTIE
C
TIME
OUTIE
DCRC
FAILIE
CCRC
FAILIE
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:29 Reserved, must  be kept at reset value.
Bit 28 IDMABTCIE: IDMA buffer transfer complete interrupt enable
Set and cleared by software to enable/disable the interrupt generated when the IDMA has
transferred all data belonging to a memory buffer.
0: IDMA buffer transfer complete interrupt disabled
1: IDMA buffer transfer complete interrupt enabled
Bit 27 Reserved, must be kept at reset value.
Bit 26 CKSTOPIE: Voltage switch clock stopped interrupt enable
Set and cleared by software to enable/disable interrupt caused by voltage switch clock
stopped.
0: Voltage switch clock stopped interrupt disabled
1: Voltage switch clock stopped interrupt enabled
Bit 25 VSWENDIE: Voltage switch critical timing section completion interrupt enable
Set and cleared by software to enable/disable the interrupt generated when voltage switch
critical timing section completion.
0: Voltage switch critical timing section completion interrupt disabled
1: Voltage switch critical timing section completion interrupt enabled

RM0438 Rev 8 1861/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
Bit 24 ACKTIMEOUTIE: Acknowledgment timeout interrupt enable
Set and cleared by software to enable/disable interrupt caused by acknowledgment timeout.
0: Acknowledgment timeout interrupt disabled
1: Acknowledgment timeout interrupt enabled
Bit 23 ACKFAILIE: Acknowledgment fail interrupt enable
Set and cleared by software to enable/disable interrupt caused by acknowledgment fail.
0: Acknowledgment fail interrupt disabled
1: Acknowledgment fail interrupt enabled
Bit 22 SDIOITIE: SDIO mode interrupt received interrupt enable
Set and cleared by software to enable/disable the interrupt generated when receiving the
SDIO mode interrupt.
0: SDIO mode interrupt received interrupt disabled
1: SDIO mode interrupt received interrupt enabled
Bit 21 BUSYD0ENDIE: BUSYD0END interrupt enable
Set and cleared by software to enable/disable the interrupt generated when SDMMC_D0
signal changes from busy to NOT busy following a CMD response.
0: BUSYD0END interrupt disabled
1: BUSYD0END interrupt enabled
Bits 20:19 Reserved, must  be kept at reset value.
Bit 18 TXFIFOEIE: Tx FIFO empty interrupt enable
Set and cleared by software to enable/disable interrupt caused by Tx FIFO empty.
0: Tx FIFO empty interrupt disabled
1: Tx FIFO empty interrupt enabled
Bit 17 RXFIFOFIE: Rx FIFO full interrupt enable
Set and cleared by software to enable/disable interrupt caused by Rx FIFO full.
0: Rx FIFO full interrupt disabled
1: Rx FIFO full interrupt enabled
Bit 16 Reserved, must be kept at reset value.
Bit 15 RXFIFOHFIE: Rx FIFO half full interrupt enable
Set and cleared by software to enable/disable interrupt caused by Rx FIFO half full.
0: Rx FIFO half full interrupt disabled
1: Rx FIFO half full interrupt enabled
Bit 14 TXFIFOHEIE: Tx FIFO half empty interrupt enable
Set and cleared by software to enable/disable interrupt caused by Tx FIFO half empty.
0: Tx FIFO half empty interrupt disabled
1: Tx FIFO half empty interrupt enabled
Bits 13:12 Reserved, must  be kept at reset value.
Bit 11 DABORTIE: Data transfer aborted interrupt enable
Set and cleared by software to enable/disable interrupt caused by a data transfer being
aborted.
0: Data transfer abort interrupt disabled
1: Data transfer abort interrupt enabled
Bit 10 DBCKENDIE: Data block end interrupt enable
Set and cleared by software to enable/disable interrupt caused by data block end.
0: Data block end interrupt disabled
1: Data block end interrupt enabled

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1862/2187 RM0438 Rev 8
Bit 9 DHOLDIE: Data hold interrupt enable
Set and cleared by software to enable/disable the interrupt generated when sending new
data is hold in the DPSM Wait_S state.
0: Data hold interrupt disabled
1: Data hold interrupt enabled
Bit 8 DATAENDIE: Data end interrupt enable
Set and cleared by software to enable/disable interrupt caused by data end.
0: Data end interrupt disabled
1: Data end interrupt enabled
Bit 7 CMDSENTIE: Command sent interrupt enable
Set and cleared by software to enable/disable interrupt caused by sending command.
0: Command sent interrupt disabled
1: Command sent interrupt enabled
Bit 6 CMDRENDIE: Command response received interrupt enable
Set and cleared by software to enable/disable interrupt caused by receiving command
response.
0: Command response received interrupt disabled
1: command Response received interrupt enabled
Bit 5 RXOVERRIE: Rx FIFO overrun error interrupt enable
Set and cleared by software to enable/disable interrupt caused by Rx FIFO overrun error.
0: Rx FIFO overrun error interrupt disabled
1: Rx FIFO overrun error interrupt enabled
Bit 4 TXUNDERRIE: Tx FIFO underrun error interrupt enable
Set and cleared by software to enable/disable interrupt caused by Tx FIFO underrun error.
0: Tx FIFO underrun error interrupt disabled
1: Tx FIFO underrun error interrupt enabled
Bit 3 DTIMEOUTIE: Data timeout interrupt enable
Set and cleared by software to enable/disable interrupt caused by data timeout.
0: Data timeout interrupt disabled
1: Data timeout interrupt enabled
Bit 2 CTIMEOUTIE: Command timeout interrupt enable
Set and cleared by software to enable/disable interrupt caused by command timeout.
0: Command timeout interrupt disabled
1: Command timeout interrupt enabled
Bit 1 DCRCFAILIE: Data CRC fail interrupt enable
Set and cleared by software to enable/disable interrupt caused by data CRC failure.
0: Data CRC fail interrupt disabled
1: Data CRC fail interrupt enabled
Bit 0 CCRCFAILIE: Command CRC fail interrupt enable
Set and cleared by software to enable/disable interrupt caused by command CRC failure.
0: Command CRC fail interrupt disabled
1: Command CRC fail interrupt enabled

RM0438 Rev 8 1863/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
48.9.14 SDMMC acknowledgment ti mer register (SDMMC_ACKTIMER)
Address offset: 0x040
Reset value: 0x0000 0000
This register contains the acknowledgment timeout period, in SDMMC_CK bus clock
periods.
A counter loads the value from this register, and starts decrementing when the data path
state machine (DPSM) enters the Wait_Ack state. If the timer reaches 0 while the DPSM is
in this states, the acknowledgment timeout status flag is set.
Note: The data transfer must be written to the acknowledgment timer register before being written
to the data control register.
48.9.15 SDMMC DMA control register (SDMMC_IDMACTRLR)
Address offset: 0x050
Reset value: 0x0000 0000
The receive and transmit FIFOs can be read or written as 32-bit wide registers. The FIFOs
contain 32 entries on 32 sequential addresses. This enables the CPU to use its load and
store multiple operands to read from/write to the FIFO.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. ACKTIME[24:16]
rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ACKTIME[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:25 Reserved, must be kept at reset value.
Bits 24:0 ACKTIME[24:0]: Boot acknowledgment timeout period
This bit can only be written by firmware when CPSM is disabled (CPSMEN = 0).
Boot acknowledgment timeout period expressed in card bus clock periods.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. IDMAB
ACT
IDMAB
MODE
IDMA
EN
rw rw rw

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1864/2187 RM0438 Rev 8
48.9.16 SDMMC IDMA buffer size  register (SDMMC_IDMABSIZER)
Address offset: 0x054
Reset value: 0x0000 0000
This register contains the buffers size when in double buffer configuration.
Bits 31:3 Reserved, must be kept at reset value.
Bit 2 IDMABACT: Double buffer mode active buffer indication
This bit can only be written by firmware when DPSM is inactive (DPSMACT = 0). When
IDMA is enabled this bit is toggled by hardware.
0: When IDMA is enabled, uses buffer0 and firmware write access to IDMABASE0 is
prohibited.
1: When IDMA is enabled, uses buffer1 and firmware write access to IDMABASE1 is
prohibited.
Bit 1 IDMABMODE: Buffer mode selection
This bit can only be written by firmware when DPSM is inactive (DPSMACT = 0).
0: Single buffer mode.
1: Double buffer mode.
Bit 0 IDMAEN: IDMA enable
This bit can only be written by firmware when DPSM is inactive (DPSMACT = 0).
0: IDMA disabled
1: IDMA enabled
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. IDMABNDT[7:0] Res. Res. Res. Res. Res.
rw rw rw rw rw rw rw rw
Bits 31:13 Reserved, must be kept at reset value.
Bits 12:5 IDMABNDT[7:0]: Number of bytes per buffer
This 8-bit value must be multiplied by 8 to get the size of the buffer in 32-bit words and by 32
to get the size of the buffer in bytes.
Example: IDMABNDT = 0x01: buffer size = 8 words = 32 bytes.
Example: IDMABNDT = 0x80: buffer size = 1024 words = 4 Kbytes
These bits can only be written by firmware when DPSM is inactive (DPSMACT = 0).
Bits 4:0 Reserved, must be kept at reset value.

RM0438 Rev 8 1865/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
48.9.17 SDMMC IDMA buffer  0 base address register
(SDMMC_IDMABASE0R)
Address offset: 0x058
Reset value: 0x0000 0000
This register contains the memory buffer base address in single buffer configuration and the
buffer 0 base address in double buffer configuration.
48.9.18 SDMMC IDMA buffer  1 base address register
(SDMMC_IDMABASE1R)
Address offset: 0x05C
Reset value: 0x0000 0000
This register contains the double buffer configuration second buffer memory base address.
48.9.19 SDMMC data FIFO registers x (SDMMC_FIFORx)
Address offset: 0x080 + 0x004 * x, (x =0 to 15)
Reset value: 0x0000 0000
The receive and transmit FIFOs can be only read or written as word (32-bit) wide registers.
The FIFOs contain 16 entries on sequential addresses. This enables the CPU to use its load
and store multiple operands to read from/write to the FIFO. The FIFO register interface
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
IDMABASE0[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
IDMABASE0[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw r r
Bits 31:0 IDMABASE0[31:0]: Buffer 0 memory base address bits [31:2], must be word aligned (bit [1:0]
are always 0 and read only)
This register can be written by firmware when DPSM is inactive (DPSMACT = 0), and can
dynamically be written by firmware when DPSM active (DPSMACT = 1) and memory buffer 0
is inactive (IDMABACT = ‘1’).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
IDMABASE1[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
IDMABASE1[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw r r
Bits 31:0 IDMABASE1[31:0]: Buffer 1 memory base address, must be word aligned (bit [1:0] are always
0 and read only)
This register can be written by firmware when DPSM is inactive (DPSMACT = 0), and can
dynamically be written by firmware when DPSM active (DPSMACT = 1) and memory buffer
1 is inactive (IDMABACT = ‘0’).

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1866/2187 RM0438 Rev 8
takes care of correct data alignment inside the FIFO, the FIFO register address used by the
CPU does matter.
When accessing SDMMC_FIFOR with half word or byte access an AHB bus fault is
generated.
48.9.20 SDMMC register map
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
FIFODATA[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
FIFODATA[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 FIFODATA[31:0]: Receive and transmit FIFO data
This register can only be read or written by firmware when the DPSM is active
(DPSMACT = 1).
The FIFO data occupies 16 entries of 32-bit words.
[Table 407](../tables/table_407.md). SDMMC register map
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
0x000
SDMMC_
POWER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
DIRPOL
VSWITCHEN
VSWITCH
PWRCTRL[1:0]
Reset value 00000
0x004
SDMMC_
CLKCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SELCLKRX[1:0]
BUSSPEED
DDR
HWFC_EN
NEGEDGE
WIDBUS[1:0]
Res.
PWRSAV
Res.
Res. CLKDIV[9:0]
R e s e t  v a l u e 00000000 0 0000000000
0x008
SDMMC_
ARGR CMDARG[31:0]
R e s e t  v a l u e 00000000000 000000 000000000000000
0x00C
SDMMC_
CMDR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CMDSUSPEND
BOOTEN
BOOTMODE
DTHOLD
CPSMEN
WAITPEND
WAITINT
WAITRESP[1:0]
CMDSTOP
CMDTRANS
CMDINDEX[5:0]
Reset value
0x010
SDMMC_
RESPCMDR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.RESPCMD[5:0]
Reset value 000000
0x014
SDMMC_
RESP1R CARDSTATUS[31:0]
R e s e t  v a l u e 00000000000 000000 000000000000000

RM0438 Rev 8 1867/2187
RM0438 Secure digital input/output MultiMediaCard interface (SDMMC)
1868
0x018
SDMMC_
RESP2R CARDSTATUS[31:0]
R e s e t  v a l u e 00000000000 000000 000000000000000
0x01C
SDMMC_
RESP3R CARDSTATUS[31:0]
R e s e t  v a l u e 00000000000 000000 000000000000000
0x020
SDMMC_
RESP4R CARDSTATUS[31:0]
R e s e t  v a l u e 00000000000 000000 000000000000000
0x024
SDMMC_
DTIMER DATATIME[31:0]
R e s e t  v a l u e 00000000000 000000 000000000000000
0x028
SDMMC_
DLENR
Res.
Res.
Res.
Res.
Res.
Res.
Res. DATALENGTH[24:0]
R e s e t  v a l u e 0000000000000000000000000
0x02C
SDMMC_
DCTRLR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
FIFORST
BOOTACKEN
SDIOEN
RWMOD
RWSTOP
RWSTART
DBLOCK
SIZE[3:0]
DTMODE[1:0]
DTDIR
DTEN
R e s e t  v a l u e 00000000000000
0x030
SDMMC_
DCNTR
Res.
Res.
Res.
Res.
Res.
Res.
Res. DATACOUNT[24:0]
R e s e t  v a l u e 0000000000000000000000000
0x034
SDMMC_
STAR
Res.
Res.
Res.
IDMABTC
IDMATE
CKSTOP
VSWEND
ACKTIMEOUT
ACKFAIL
SDIOIT
BUSYD0END
BUSYD0
RXFIFOE
TXFIFOE
RXFIFOF
TXFIFOF
RXFIFOHF
TXFIFOHE
CPSMACT
DPSMACT
DABORT
DBCKEND
DHOLD
DATAEND
CMDSENT
CMDREND
RXOVERR
TXUNDERR
DTIMEOUT
CTIMEOUT
DCRCFAIL
CCRCFAIL
R e s e t  v a l u e 00000000 000000 000000000000000
0x038
SDMMC_
ICR
Res.
Res.
Res.
IDMABTCC
IDMATEC
CKSTOPC
VSWENDC
ACKTIMEOUTC
ACKFAILC
SDIOITC
BUSYD0ENDC
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
DABORTC
DBCKENDC
DHOLDC
DATAENDC
CMDSENTC
CMDRENDC
RXOVERRC
TXUNDERRC
DTIMEOUTC
CTIMEOUTC
DCRCFAILC
CCRCFAILC
R e s e t  v a l u e 00000000 0000 00000000
0x03C
SDMMC_
MASKR
Res.
Res.
Res.
IDMABTCIE
Res.
CKSTOPIE
VSWENDIE
ACKTIMEOUTIE
ACKFAILIE
SDIOITIE
BUSYD0ENDIE
Res.
Res.
TXFIFOEIE
RXFIFOFIE
Res.
RXFIFOHFIE
TXFIFOHEIE
Res.
Res.
DABORTIE
DBCKENDIE
DHOLDIE
DATAENDIE
CMDSENTIE
CMDRENDIE
RXOVERRIE
TXUNDERRIE
DTIMEOUTIE
CTIMEOUTIE
DCRCFAILIE
CCRCFAILIE
R e s e t  v a l u e 0 000000 00 00 000000000000
0x040
SDMMC_
ACKTIMER
Res.
Res.
Res.
Res.
Res.
Res.
Res. ACKTIME[24:0]
R e s e t  v a l u e 0000000000000000000000000
0x044
- 0x04C Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
[Table 407](../tables/table_407.md). SDMMC register map (continued)
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

Secure digital input/output MultiMediaCard interface (SDMMC) RM0438
1868/2187 RM0438 Rev 8
Refer to Section 2.3: Memory organization for the register boundary addresses.
0x050
SDMMC_
IDMACTRLR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
IDMABACT
IDMABMODE
IDMAEN
Reset value 000
0x054
SDMMC_
IDMABSIZER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. IDMABNDT[7:0]
Res.
Res.
Res.
Res.
Res.
Reset value 00000000
0x058
SDMMC_
IDMABASE0R IDMABASE0[31:0]
R e s e t  v a l u e 00000000000 000000 000000000000000
0x05C
SDMMC_
IDMABASE1R IDMABASE1[31:0]
R e s e t  v a l u e 00000000000 000000 000000000000000
0x060
- 0x07C Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x080 +
0x04 * x,
(x=0..15)
SDMMC_
FIFORx FIFODATA[31:0]
R e s e t  v a l u e 00000000000 000000 000000000000000
[Table 407](../tables/table_407.md). SDMMC register map (continued)
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
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 510: Architectural Diagram](../figures/figure_510.md)
* [Figure 511: Architectural Diagram](../figures/figure_511.md)
* [Figure 512: Architectural Diagram](../figures/figure_512.md)
* [Figure 513: Architectural Diagram](../figures/figure_513.md)
* [Figure 514: Architectural Diagram](../figures/figure_514.md)
* [Figure 515: Architectural Diagram](../figures/figure_515.md)
* [Figure 516: Architectural Diagram](../figures/figure_516.md)
* [Figure 517: Architectural Diagram](../figures/figure_517.md)
* [Figure 518: Architectural Diagram](../figures/figure_518.md)
* [Figure 519: Architectural Diagram](../figures/figure_519.md)
* [Figure 520: Architectural Diagram](../figures/figure_520.md)
* [Figure 521: Architectural Diagram](../figures/figure_521.md)
* [Figure 522: Architectural Diagram](../figures/figure_522.md)
* [Figure 523: Architectural Diagram](../figures/figure_523.md)
* [Figure 524: Architectural Diagram](../figures/figure_524.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 383: Configuration Matrix](../tables/table_383.md)
* [Table 384: Configuration Matrix](../tables/table_384.md)
* [Table 385: Configuration Matrix](../tables/table_385.md)
* [Table 386: Configuration Matrix](../tables/table_386.md)
* [Table 387: Configuration Matrix](../tables/table_387.md)
* [Table 388: Configuration Matrix](../tables/table_388.md)
* [Table 389: Configuration Matrix](../tables/table_389.md)
* [Table 390: Configuration Matrix](../tables/table_390.md)
* [Table 391: Configuration Matrix](../tables/table_391.md)
* [Table 392: Configuration Matrix](../tables/table_392.md)
* [Table 393: Configuration Matrix](../tables/table_393.md)
* [Table 394: Configuration Matrix](../tables/table_394.md)
* [Table 395: Configuration Matrix](../tables/table_395.md)
* [Table 396: Configuration Matrix](../tables/table_396.md)
* [Table 397: Configuration Matrix](../tables/table_397.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)