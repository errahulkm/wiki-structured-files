# Chapter 20: Octo-SPI interface (OCTOSPI)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 20: Octo-SPI interface (OCTOSPI).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 626 - 682
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Serial Peripheral Interface (SPI)](../peripherals/spi.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
Octo-SPI interface (OCTOSPI) RM0438
626/2187 RM0438 Rev 8
20 Octo-SPI interface (OCTOSPI)
20.1 OCTOSPI introduction
The OCTOSPI supports most external serial memories such as serial PSRAMs, serial
NAND and serial NOR flash memories, HyperRAM™ and HyperFlash™ memories, with
the following functional modes:
• indirect mode: all the operations are performed using the OCTOSPI registers to preset
commands, addresses, data, and transfer parameters.
• automatic status-polling mode: the external memory status register is periodically read
and an interrupt can be generated in case of flag setting. This feature is only available
in regular-command protocol.
• memory-mapped mode: the external memory is memory mapped and it is seen by the
system as if it was an internal memory, supporting both read and write operations.
The OCTOSPI supports the following protocols with associated frame formats:
• the regular-command frame format with the command, address, alternate byte, dummy
cycles, and data phase
• the HyperBus™ frame format
20.2 OCTOSPI main features
• Functional modes: indirect, automatic status-polling, and memory-mapped
• Read and write support in memory-mapped mode
• External (P)SRAM memory support
• Support for single, dual, quad, and octal communication
• Dual memory configuration, where eight bits can be sent/received simultaneously by
accessing two quad memories in parallel
• SDR (single-data rate) and DTR (double-transfer rate) support
• Data strobe support
• Fully programmable opcode
• Fully programmable frame format
• Support wrapped-type access to memory in read direction
• HyperBus support
• Integrated FIFO for reception and transmission
• Asynchronous bus clock versus kernel clock support
• 8-, 16-, and 32-bit data accesses allowed
• DMA channel for indirect mode operations
• Interrupt generation on FIFO threshold, timeout, operation complete, and access error
• AHB interface with transaction acceptance limited to one: the interface accepts the next
transfer on AHB bus only once the previous is completed on memory side.

RM0438 Rev 8 627/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
20.3 OCTOSPI implementation
[Table 156](../tables/table_156.md). OCTOSPI implementation
OCTOSPI feature OCTOSPI1
HyperBus standard compliant X
Xccela standard compliant X
XSPI (JESD251C) standard compliant X
AMBA® AHB compliant data interface X
Asynchronous AHB clock versus kernel clock X
Functional modes: indirect, automatic status-polling, and memory-mapped X
Read and write support in memory-mapped mode X
Dual-quad configuration X
SDR (single-data rate) and DTR (double-transfer rate) X
Data strobe (DS,DQS) X
Fully programmable opcode X
Fully programmable frame format X
Integrated FIFO for reception and transmission X
8-, 16-, and 32-bit data accesses X
Interrupt on FIFO threshold, timeout, operation complete, and access error X
Extended CSHT timeout -
Memory-mapped write X
Refresh counter X
Dual chip select -
Extended external memory -
Prefetch disable -
Prefetch hardware software -

Octo-SPI interface (OCTOSPI) RM0438
628/2187 RM0438 Rev 8
20.4 OCTOSPI func tional description
20.4.1 OCTOSPI block diagram
[Figure 74](../figures/figure_74.md). OCTOSPI block diagram in octal configuration
[Figure 75](../figures/figure_75.md). OCTOSPI block diagram in quad configuration
MSv65072V3
OCTOSPI_CLK
OCTOSPI_IO0
OCTOSPI_IO1
OCTOSPI_IO2
OCTOSPI_IO3
CLK
IO0
IO1
IO2
IO3
OCTOSPI_IO4 IO4
AHB
Octo-SPI
memory
OCTOSPI_IO5
OCTOSPI_IO6
OCTOSPI_IO7
OCTOSPI_NCS
IO5
IO6
IO7
NCS
OCTOSPI_DQS
Data
FIFO
Registers/
control
Clock
management
Shift
register
DQS
OCTOSPI_NCLK NCLK
octospi_ker_ck
STM32
DMA signals
Interrupts
5
OCTOSPI
Signal connected or not depending on the board configuration
Delay
block
AHB
5
MSv43486V4
OCTOSPI_CLK
OCTOSPI_IO0
OCTOSPI_IO1
OCTOSPI_IO2
OCTOSPI_IO3
CLK
Q0/SI
Q1/SO
Q2/WP
Q3/HOLD
OCTOSPI_NCS NCS
Quad-SPI
memory
Data FIFO
Registers/
control
Clock
management
Shift
register
STM32
AHB
octospi_ker_ck
DMA signals
Interrupts
5
5
OCTOSPI
Delay
block
AHB

RM0438 Rev 8 629/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
[Figure 76](../figures/figure_76.md). OCTOSPI block diagram in dual-quad configuration
20.4.2 OCTOSPI pins and internal signals
Caution: Use the same configuration (output speed, HSLV(a)) for all OCTOSPI input/output pins to
avoid any data corruption.
MSv43487V4
AHB
OCTOSPI_CLK
OCTOSPI_IO0
OCTOSPI_IO1
OCTOSPI_IO2
OCTOSPI_IO3
CLK
Q0/SI
Q1/SO
Q2/WP
Q3/HOLD
OCTOSPI_NCS NCS
Quad-SPI
memory 1
Data FIFO
Registers/
control
Clock
management
CLK
Q0/SI
Q1/SO
Q2/WP
Q3/HOLD
NCS
OCTOSPI_IO4
OCTOSPI_IO5
OCTOSPI_IO6
OCTOSPI_IO7
Shift
register Quad-SPI
memory 2
STM32
octospi_ker_ck
DMA signals
Interrupts
5
5
OCTOSPI
Delay
block
AHB
[Table 157](../tables/table_157.md). OCTOSPI input/output pins
Pin name Type Description
OCTOSPI_NCLK
Output
OCTOSPI inverted clock to support 1.8 V HyperBus protocol
OCTOSPI_CLK OCTOSPI clock
OCTOSPI_IOn (n = 0 to 7) In put/output OCTOSPI data pins
OCTOSPI_NCS Output Chip select for the memory
OCTOSPI_DQS Input/output Data strobe/ write mask signal from/to the memory
a. When applicable.
[Table 158](../tables/table_158.md). OCTOSPI internal signals
Signal name Type Description
octospi_hclk Input OCTOSPI AHB clock
octospi_ker_ck Input OCTOSPI kernel clock
octospi_dma N/A DMA request signal
octospi_it Output Global interrupt line (see [Table 162](../tables/table_162.md) for the multiple sources of interrupt)

Octo-SPI interface (OCTOSPI) RM0438
630/2187 RM0438 Rev 8
20.4.3 OCTOSPI interface to memory modes
The OCTOSPI supports the following protocols:
• regular-command protocol
• HyperBus protocol
The OCTOSPI uses from 6 to 12 signals to interface with a memory, depending on the
functional mode:
• NCS: chip-select
• CLK: communication clock
• NCLK: inverted clock used only in the 1.8 V HyperBus protocol
• DQS: data strobe used only in regular-command protocol as input only
• IO[3:0]: data bus LSB
• IO[7:4]:
– data bus MSB used in dual-quad and octal configurations
– data bus can be used as possible remap for quad-SPI mode
20.4.4 OCTOSPI regular-command protocol
When in regular-command protocol, the OCTOSPI communicates with the external device
using commands. Each command can include the following phases:
• Instruction phase
• Address phase
• Alternate-byte phase
• Dummy-cycle phase
• Data phase
Any of these phases can be configured to be skipped but, in case of single-phase
command, the only use case supported is instruction-phase-only.
The NCS falls before the start of each command and rises again after each command
finishes.
In memory-mapped mode, both read and write operations are supported: as a
consequence, some of the configuration registers are duplicated to specify write operations
(read operations are configured using regular registers).
[Figure 77](../figures/figure_77.md). SDR read command in octal configuration
The specific regular-command protocol features are configured through the registers in the
0x0100-0x01FC offset range.
MSv43488V1
A[31:24]
NCS
Pre-drive
IO[7:0] ECh        13h
DummyAddress
D0
§ § §
CLK
A[23:16] A[15:8] A[7:0] D1 D2 D3

RM0438 Rev 8 631/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
Instruction phase
During this phase, a 1- to 4-byte instruction is sent to the external device specifying the type
of operation to be performed. The size of the instruction to be sent is configured
by ISIZE[1:0] in OCTOSPI_CCR and the instruction is programmed in INSTRUCTION[31:0]
of OCTOSPI_IR.
The instruction phase can optionally send:
• 1 bit at a time (over IO0, SO single in single-SPI mode)
• 2 bits at a time (over IO0/IO1 in dual-SPI mode)
• 4 bits at a time (over IO0 to IO3 in quad-SPI mode)
• 8 bits at a time (over IO0 to IO7 in octal-SPI mode)
This can be configured using IMODE[2:0] of OCTOSPI_CCR.
The instruction can be sent in DTR mode on each rising and falling edge of the clock, by
setting IDTR in OCTOSPI_CCR.
When IMODE[2:0] = 000 in OCTOSPI_CCR, the instruction phase is skipped, and the
command sequence starts with the address phase, if present.
In memory-mapped mode, the instruction used for the write operation is specified
in OCTOSPI_WIR, and the instruction format is specified in OCTOSPI_WCCR. The
instruction used for the read operation and the instruction format are specified in
OCTOSPI_IR and OCTOSPI_CCR.
Address phase
In the address phase, 1 to 4 bytes are sent to the external device, to indicate the address of
the operation. The number of address bytes to be sent is configured by ADSIZE[1:0]
in OCTOSPI_CCR.
In indirect and automatic status-polling modes, the address bytes to be sent are specified
by ADDRESS[31:0] in OCTOSPI_AR. In memory-mapped mode, the address is given
directly via the AHB (from any master in the system).
The address phase can send:
• 1 bit at a time (over IO0, SO single in single-SPI mode)
• 2 bits at a time (over IO0/IO1 in dual-SPI mode)
• 4 bits at a time (over IO0 to IO3 in quad-SPI mode)
• 8 bits at a time (over IO0 to IO7 in octal-SPI mode)
This can be configured using ADMODE[2:0] in OCTOSPI_CCR.
The address can be sent in DTR mode (on each rising and falling edge of the clock) setting
ADDTR in OCTOSPI_CCR.
When ADMODE[2:0] = 000, the address phase is skipped and the command sequence
proceeds directly to the next phase, if any.
In memory-mapped mode, the address format for the write operation is specified in
OCTOSPI_WCCR. The address format for the read operation is specified in
OCTOSPI_CCR.

Octo-SPI interface (OCTOSPI) RM0438
632/2187 RM0438 Rev 8
Alternate-byte phase
In the alternate-byte phase, 1 to 4 bytes are sent to the external device, generally to control
the mode of operation. The number of alternate bytes to be sent is configured
by ABSIZE[1:0] in OCTOSPI_CCR. The bytes to be sent are specified in OCTOSPI_ABR.
The alternate-byte phase can send:
• 1 bit at a time (over IO0, SO single in single-SPI mode)
• 2 bits at a time (over IO0/IO1 in dual-SPI mode)
• 4 bits at a time (over IO0 to IO3 in quad-SPI mode)
• 8 bits at a time (over IO0 to IO7 in octal-SPI mode)
This can be configured using ABMODE[2:0] in OCTOSPI_CCR.
The alternate bytes can be sent in DTR mode (on each rising and falling edge of the clock)
setting ABDTR in OCTOSPI_CCR.
When ABMODE[2:0] = 000, the alternate-byte phase is skipped and the command
sequence proceeds directly to the next phase, if any.
There may be times when only a single nibble needs to be sent during the alternate-byte
phase rather than a full byte, such as when the dual-SPI mode is used and only two cycles
are used for the alternate bytes.
In this case, the firmware can use the quad-SPI mode (ABMODE[2:0] = 011) and send a
byte with bits 7 and 3 of ALTERNATE[31:0] set to 1 (keeping the IO3 line high), and bits 6
and 2 set to 0 (keeping the IO2 line low), in OCTOSPI_IR.
The upper two bits of the nibble to be sent are then placed in bits 5:4 of ALTERNATE[31:0]
while the lower two bits are placed in bits 1:0. For example, if the nibble 2 (0010) is to be
sent over IO0/IO1, then ALTERNATE[31:0] must be set to 0x8A (1000_1010).
In memory-mapped mode, the alternate bytes used for the write operation are specified in
OCTOSPI_WABR, and the alternate byte format is specified in OCTOSPI_WCCR. The
alternate bytes used for read operation and the alternate byte format are specified in
OCTOSPI_ABR and OCTOSPI_CCR.
Dummy-cycle phase (memory latency)
In the dummy-cycle phase, 1 to 31 cycles are given without any data being sent or received,
in order to give the external device, the time to prepare for the data phase when higher clock
frequencies are used. The number of cycles given during this phase is specified
by DCYC[4:0] in OCTOSPI_TCR. In both SDR and DTR modes, the duration is specified as
a number of full CLK cycles.
When DCYC[4:0] = 00000, the dummy-cycle phase is skipped, and the command sequence
proceeds directly to the data phase, if present.
In order to assure enough “turn-around” time for changing the data signals from the output
mode to the input mode, there must be at least one dummy cycle when using the dual-SPI,
the quad-SPI, or the octal-SPI mode, to receive data from the external device.
In memory-mapped mode, the dummy cycles for the write operations are specified
in OCTOSPI_WTCR. The dummy cycles for the read operation are specified
in OCTOSPI_TCR.

RM0438 Rev 8 633/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
Data phase
During the data phase, any number of bytes can be sent to or received from the external
device.
In indirect mode, the number of bytes to be sent/received is specified in OCTOSPI_DLR. In
this mode, the data to be sent to the external device must be written to OCTOSPI_DR, while
in indirect-read mode the data received from the external device is obtained by reading
OCTOSPI_DR.
In automatic status-polling mode, the number of bytes to be received is specified in
OCTOSPI_DLR, and the data received from the external device can be obtained by reading
OCTOSPI_DR.
In memory-mapped mode, the data read or written, is sent or received directly over the AHB
to the Cortex core or to a DMA.
The data phase can send/receive:
• 1 bit at a time (over IO0/IO1 (SO/SI respectively) in single-SPI mode)
• 2 bits at a time (over IO0/IO1 in dual-SPI mode)
• 4 bits at a time (over IO0 to IO3 in quad-SPI mode)
• 8 bits at a time (over IO0 to IO7 in octal-SPI mode)
This can be configured using DMODE[2:0] in OCTOSPI_CCR.
The data can be sent or received in DTR mode (on each rising and falling edge of the clock)
setting DDTR in OCTOSPI_CCR.
When DMODE[2:0] = 000, the data phase is skipped, and the command sequence finishes
immediately by raising the NCS. This configuration must be used only in indirect-write
mode.
In memory-mapped mode, the data format for the write operation is specified in
OCTOSPI_WCCR. The data format for the read operation is specified in OCTOSPI_CCR.
DQS use
The DQS signal can be used for data strobing during the read transactions when the device
toggles the DQS aligned with the data.
The DQS management can be enabled by setting DQSE in OCTOSPI_CCR.
[Figure 78](../figures/figure_78.md). DTR read in octal-SPI mode with DQS (Macronix mode) example
MSv43489V1
NCS
Dummy
IO[7:0]
Address
§ §§§
CLK
DQS
A[31:24]EEh     11h D1 D0 D3 D2A[23:16] A[15:8] A[7:0]
Word
unit
Word
unit

Octo-SPI interface (OCTOSPI) RM0438
634/2187 RM0438 Rev 8
20.4.5 OCTOSPI regular-comma nd protocol signal interface
Single-SPI mode
The legacy SPI mode allows just a single bit to be sent/received serially. In this mode, the
data is sent to the external device over the SO signal (Single-SPI Output) (whose I/Os are
shared with IO0). The data received from the external device arrives via SI (Single-SPI
Input) (whose I/Os are shared with IO1).
Compared to the SPI legacy mode, I0/SO and I1/SI are respectively equivalent to MOSI and
MISO, having the OCTOSPI generating the clock.
The different phases can each be configured separately to use this single-SPI mode by
setting to 001 the IMODE, ADMODE, ABMODE, and DMODE fields in OCTOSPI_CCR and
OCTOSPI_WCCR.
In each phase configured in single-SPI mode:
• IO0 (SO) is in output mode.
• IO1 (SI) is in input mode (high impedance).
• IO2 is in output mode and forced to 0.
• IO3 is in output mode and forced to 1 (to deactivate the “hold” function).
• IO4 to IO7 are in output mode and forced to 0.
This is the case even for the dummy phase if DMODE[2:0] = 001.
Dual-SPI mode
In dual-SPI mode, two bits are sent/received simultaneously over the IO0/IO1 signals.
The different phases can each be configured separately to use dual-SPI mode by setting
to 010 the IMODE, ADMODE, ABMODE, and DMODE fields in OCTOSPI_CCR and
OCTOSPI_WCCR.
In each phase configured in dual-SPI mode:
• IO0/IO1 are at high-impedance (input) during the data phase for the read operations,
and outputs in all other cases.
• IO2 is in output mode and forced to 0.
• IO3 is in output mode and forced to 1.
• IO4 to IO7 are in output mode and forced to 0.
In the dummy phase when DMODE[2:0] = 010, IO0/IO1 are always high-impedance.
Quad-SPI mode
In quad-SPI mode, four bits are sent/received simultaneously over the IO0/IO1/IO2/IO3
signals.
The different phases can each be configured separately to use the quad-SPI mode by
setting to 011 the IMODE, ADMODE, ABMODE, and DMODE fields in OCTOSPI_CCR and
OCTOSPI_WCCR.
In each phase configured in quad-SPI mode:
• IO0 to IO3 are all at high-impedance (inputs) during the data phase for the read
operations, and outputs in all other cases.
• IO4 to IO7 are in output mode and forced to 0.

RM0438 Rev 8 635/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
In the dummy phase when DMODE[2:0] = 011, IO0 to IO3 are all high-impedance.
Octal-SPI mode
In regular octal-SPI mode, the eight bits are sent/received simultaneously over the IO[0:7]
signals.
The different phases can each be configured separately to use the octal-SPI mode by
setting to 100 the IMODE, ADMODE, ABMODE, and DMODE fields in OCTOSPI_CCR and
OCTOSPI_WCCR.
In each phase that is configured in octal-SPI mode, IO[0:7] are all at high-impedance (input)
during the data phase for read operations, and outputs in all other cases.
In the dummy phase when DMODE[2:0] = 100, IO[0:7] are all high-impedance.
Single-data rate (SDR) mode
By default, all the phases operate in SDR mode.
In this mode, when the OCTOSPI drives the IO0/SO, IO1 to IO7 signals, these signals
transition only with the falling edge of CLK.
When receiving data in SDR mode, the OCTOSPI assumes that the external devices also
send the data using CLK falling edge. By default (when SSHIFT = 0 in OCTOSPI_TCR), the
signals are sampled using the following (rising) edge of CLK.
[Figure 79](../figures/figure_79.md). SDR write command in octo-SPI mode example
Note: Due to internal synchronization, up to six extra dummy clock cycles may be generated by
the Octo-SPI interface after the last data is read.
Double-transfer rate (DTR) mode
Each of the instruction, address, alternate-byte, and data phases can be configured to
operate in DTR mode setting IDTR, ADDTR, ABDTR, and DDTR in OCTOSPI_CCR.
In memory-mapped mode, the DTR mode for each phase of the write operations is specified
in OCTOSPI_WCCR. The DTR mode for each phase of the read operations is specified in
OCTOSPI_CCR.
In DTR mode, when the OCTOSPI drives the IO0/SO and IO1 to IO7 signals in the
instruction, address, and alternate-byte phases, a bit is sent or received on each of the
falling and rising edges of CLK.
When receiving data in DTR mode, the OCTOSPI assumes that the external devices also
send the data using both CLK rising and falling edges. When DDTR = 1 in OCTOSPI_CCR,
the software must clear SSHIFT in OCTOSPI_TCR. Thus, the signals are sampled one half
of a CLK cycle later (on the following, opposite edge).
MSv43490V1
NCS
§ § §§
CLK
IO[7:0] 02h FDh A[31:24] A[23:16] A[15:8] A[7:0] D0 D1 D254 D255

Octo-SPI interface (OCTOSPI) RM0438
636/2187 RM0438 Rev 8
In DTR mode, it is recommended to set DHQC of OCTOSPI_TCR, to shift the outputs by
a quarter of cycle and avoid holding issues on the memory side.
Note: DHQC must not be se t when the prescaler value is 0, as this action leads to unpredictable
behavior.
[Figure 80](../figures/figure_80.md). DTR write in octal-SPI mode (Macronix mode) example
Note: Due to internal synchronization, up to six extra dummy clock cycles may be generated by
the Octo-SPI interface after the last data is read.
Dual-quad configuration
When DMM = 1 in OCTOSPI_CR, the OCTOSPI is in dual-memory configuration: if
DMODE = 011, two external Quad-SPI devices (device A and device B) are used in order to
send/receive eight bits (or 16 bits in DTR mode) every cycle, effectively doubling the
throughput.
Each device (A or B) uses the same CLK and NCS signals, but each has separate IO0 to
IO3 signals.
The dual-quad configuration can be used in conjunction with the single-SPI, dual-SPI, and
quad-SPI modes, as well as with either the SDR or DTR mode.
The device size, as specified by DEVSIZE[4:0] in OCTOSPI_DCR1, must reflect the total
external device capacity that is the double of the size of one individual component.
If address X is even, then the byte that the OCTOSPI gives for address X is the byte at the
address X/2 of device A, and the byte that the OCTOSPI gives for address X + 1 is the byte
at the address X/2 of device B. In other words, the bytes at even addresses are all stored in
device A and the bytes at odd addresses are all stored in device B.
When reading the status registers of the devices in dual-quad configuration, twice as many
bytes must be read compared to the same read in regular-command protocol: if each device
gives eight valid bits after the instruction for fetching the status register, then the OCTOSPI
must be configured with a data length of 2 bytes (16 bits), and the OCTOSPI receives one
byte from each device.
If each device gives a status of 16 bits, then the OCTOSPI must be configured to read
4 bytes to get all the status bits of both devices in dual-quad configuration. The
least-significant byte of the result (in the data register) is the least-significant byte of device
A status register. The next byte is the least-significant byte of device B status register. Then,
the third byte of the data register is the device A second byte. The fourth byte is the device
B second byte (if devices have 16-bit status registers).
An even number of bytes must always be accessed in dual-quad configuration. For this
reason, bit 0 of DL[31:0] in OCTOSPI_DLR is stuck at 1 when DMM = 1.
MSv43491V1
NCS
IO[7:0]
уу у у
CLK
02h FDh A[31:24] A[23:16] A[15:8] A[7:0] D1 D0 D255 D254
Word Unit Word Unit

RM0438 Rev 8 637/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
In dual-quad configuration, the behavior of device A interface signals is basically the same
as in normal mode. Device B interface signals have exactly the same waveforms as
device A ones during the instruction, address, alternate-byte, and dummy-cycle phases. In
other words, each device always receives the same instruction and the same address.
Then, during the data phase, the AIOx and the BIOx buses both transfer data in parallel, but
the data that is sent to (or received from) device A is distinct than the one from device B.
20.4.6 HyperBus protocol
The OCTOSPI can communicate with the external device using the HyperBus protocol.
The HyperBus uses 11 to 12 pins depending on the operating voltage:
• IO[7:0] as bidirectional data bus
• DQS for read and write data strobe and latency insertion
• NCS
• CLK
• NCLK for 1.8 V operations (to support this mode, the device must be powered
with 1.8 V)
The HyperBus does not require any command specification nor any alternate bytes. As a
consequence, a separate register set is used to define the timing of the transaction.
The HyperBus frame is composed of the following phases:
• Command/address phase
• Data phase
The NCS falls before the start of a transaction and rises again after each transaction
finishes.
[Figure 81](../figures/figure_81.md). Example of HyperBus read operation
Note: Due to internal synchronization, up to six extra dummy clock cycles may be generated by
the Octo-SPI interface after the last data is read.
The specific HyperBus features are configured through the registers in the 0x0200-0x02FC
offset range.
MSv71583V1
NCS
t    RWR    =Read write recovery t    ACC    = Initial access
Latency count
Command-Address
47:40 39:32 31:24 23:16 15:8 7:0
High = 2x Latency count
Low = 1x Latency count
Dn
A
Dn
B
Dn+1
A
Dn+1
B
Host drives IO[7:0] and memory drives DQS
DQS and data are
edge aligned.
CLK
DQS
IO[7:0]
Memory drives IO[7:0]
and DQS

Octo-SPI interface (OCTOSPI) RM0438
638/2187 RM0438 Rev 8
Command/address phase
During this initial phase, the OCTOSPI sends 48 bits over IO[7:0] to specify the operations
to be performed with the external device.
The address space is configured through the memory type MTYP[2:0] in OCTOSPI_DCR1.
The total size of the device must be configured through DEVSIZE[4:0] of OCTOSPI_DCR1.
In case of multi-chip product (MCP), the device size is the sum of all the sizes of all the MCP
dies.
Read/write operation with initial latency
The HyperBus read and write operations need to respect two timings:
• tRWR: minimal read/write recovery time for the device (defined by TRWR[7:0]
in OCTOSPI_HLCR)
• tACC: access time for the device (defined by TACC[7:0] in OCTOSPI_HLCR) according
to the memory latency
During the read operation, the DQS is used by the device, in two ways (see [Figure 81](../figures/figure_81.md)):
• during the command/address phase, to request an additional latency
• during the data phase, for data strobing
During the write operation, the DQS is used:
• by the device, during the command/address phase, to request an additional latency.
• by the OCTOSPI, during the data phase, for write data masking.
[Table 159](../tables/table_159.md). Command/address phase description
CA bit Bit name Description
47 R/W# Identifies the transacti on as a read or a write.
46 Address space Indicates if the transaction accesses the memory or the register space.
45 Burst type Indicates if th e burst is linear or wrapped.
44-16 Row and upper column address Selects  the row and the upper column addresses.
15-3 Reserved -
2-0 Lower column address Selects the starting 16-bit word within the half page.

RM0438 Rev 8 639/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
[Figure 82](../figures/figure_82.md). HyperBus write operation with initial latency
Read/write operation with additional latency
If the device needs an additional latency (during refresh period of an SDRAM for example),
DQS must be tied to one during one of the DQS signals, during the command/address
phase.
An additional tACC duration is added by the OCTOSPI to meet the device request.
[Figure 83](../figures/figure_83.md). HyperBus read operation with additional latency
MSv71584V1
NCS
t RWR =Read Write Recovery tACC= Access
Latency count
Command-Address
47:40 39:32 31:24 23:16 15:8 7:0
High = 2x Latency count
Dn
A
Dn
B
Dn+1
A
Dn+1
B
Host drives IO[7:0] and memory drives DQS
Host drives IO[7:0]
and DQS
CLK and data are
center aligned.
Low = 1x Latency count
CLK
DQS
IO[7:0]
MSv71585V1
NCS
tRWR=Read write recovery tACC = AccessAdditional latency
Latency count 1 Latency count 2
Command-Address
47:40 39:32 31:24 23:16 15:8 7:0
High = 2x Latency count
Low = 1x Latency count
Dn
A
Dn
B
Dn+1
A
Dn+1
B
Host drives IO[7:0] and memory drives DQS
DQS and data are
edge aligned.
CLK
DQS
IO[7:0]
Memory drives IO[7:0]
and DQS

Octo-SPI interface (OCTOSPI) RM0438
640/2187 RM0438 Rev 8
[Figure 84](../figures/figure_84.md). HyperBus write operation with additional latency
Fixed-latency mode
Some devices or some applications may not want to operate with a variable latency time as
described above.
The latency can be forced to 2 x tACC by setting LM in OCTOSPI_HLCR.
In this OCTOSPI latency mode, the state of the DQS signal is not taken into account by the
OCTOSPI, and an additional latency is always added, leading to a fixed 2 x tACC latency
time.
Write operation with no latency
Some devices can also require a zero latency for the write operations. This write-zero
latency can be forced by setting WZL in OCTOSPI_HLCR.
[Figure 85](../figures/figure_85.md). HyperBus write operation with no latency (register write)
Latency on page-crossing during the read operations
An additional latency can be needed by some devices for the read operation when crossing
pages.
The initial latency must be respected for any page access, as a consequence, when the first
access is close to the page boundary, a latency is automatically added at the page crossing
to respect the tACC time.
MSv71586V1
NCS
tRWR= Read write recovery
t ACC    = Initial access
Additional latency
Latency count 1 Latency count 2
Command-Address
47:40   39:32 31:24   23:16 15:8 7:0
High = 2x Latency count
Low = 1x Latency count
Dn
A
Dn
B
Dn+1
B
Host drives IO[7:0] and memory drives DQS
CLK and data are
center aligned.
CLK
DQS
IO[7:0]
Host drives IO[7:0]
and DQS
Dn+1
A
MSv71587V1
NCS
Command-Address Data
47:40 39:32 31:24 23:16 15:8 7:0 15:8 7:0
Memory drives DQS but master ignores
CLK
DQS
IO[7:0]

RM0438 Rev 8 641/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
[Figure 86](../figures/figure_86.md). HyperBus read operation page crossing with latency
20.4.7 Specific features
The OCTOSPI supports some specific features, such as:
• Wrap support
• NCS boundary and refresh
Wrap support
The OCTOSPI supports a hybrid wrap as defined by the HyperBus protocol. A hybrid wrap
is also supported in the regular-command protocol.
In hybrid wrap, the transaction can continue after the initial wrap with an incremental
access.
The wrap size supported by the target memory is configured by WRAPSIZE
in OCTOSPI_DCR2.
Wrap is supported only in memory-read direction and only for data size = 4 bytes. Wrapped
reads are supported for both HyperBus and regular-command protocols. To enable
wrapped-read accesses, the dedicated OCTOSPI_WPxxx registers must be programmed
according to the wrapped-read access characteristics. These registers apply for both
HyperBus and regular-command protocols.
If the target memory is not supporting the hybrid wrap, WRAPSIZE must be set to 0.
Note: Hybrid wrap requires that the nonwra pped registers (OCTOSPI_CCR, OCTOSPI_TCR,
OCTOSPI_IR) are set according to the memory configuration to satisfy its correct data
prefetch (initiated after the wrap command).
The wrap operation cannot be interrupted by a refresh. The refresh event is only considered
after the wrap completion.
NCS boundary and refresh
Two processes can be activated to regulate the OCTOSPI transactions:
• NCS boundary
• Refresh
The NCS boundary feature limits a transaction to a boundary of aligned addresses. The size
of the address to be aligned with, is configured by CSBOUND[4:0] in OCTOSPI_DCR3: it is
equal to 2CSBOUND.
As an example, if CSBOUND(4:0] = 0x4, the boundary is set to 24 = 16 bytes. The NCS is
then released each time the LSB address is equal to 0xF, and each time a new transaction
is issued to address the next data.
MSv71588V1
NCS
A0 dd dd    dd    dd
Read from Address = 123457h
DQS
12 clock
initial latency
dd dd    dd    dd
3 clock initial page
crossing latency
dd
9 words
data
dd     dd    dd    dd                     dd
Address
123457
02 46
CLK
IO[7:0] 8A 80 07
Address
123458
Address
12345D
Address
12345E
Address
12345F
Address
123460
Address
123461

Octo-SPI interface (OCTOSPI) RM0438
642/2187 RM0438 Rev 8
If CSBOUND[4:0] = 0, the feature is disabled. A minimum value of three is recommended.
The NCS boundary feature cannot be used for flash memory devices in write mode since a
command is necessary to program another page of the flash memory.
The refresh feature limits the duration of the transactions to the value programmed
by REFRESH[31:0] in OCTOSPI_DCR4. The duration is expressed in number of cycles.
This allows an external RAM to perform its internal refresh operation regularly.
The refresh value must be greater than the minimal transaction size in terms of number of
cycles including the command/address/alternate/dummy phases.
If NCS boundary and refresh are enabled at the same time, the NCS is released on the first
condition met.
Restarting after an interrupted transfer
When a read or write operation is interrupted by a timeout or communication regulation
feature, the Octo-SPI interface, as soon as possible after getting back the port ownership,
reissues the initial command sequence together with the address following the last address
actually accessed before interruption. The transfer initially set goes on and ends
seamlessly.
20.4.8 OCTOSPI operating mode introduction
The OCTOSPI has the following operating modes regardless of the low-level protocol used
(either regular-command or HyperBus):
• indirect mode (read or write)
• automatic status-polling mode (only in regular-command protocol)
• memory-mapped mode
20.4.9 OCTOSPI indirect mode
In indirect mode, the commands are started by writing to the OCTOSPI registers, and data
are transferred by writing or reading the data register, in a similar way to other
communication peripherals.
When FMODE[1:0] = 00 in OCTOSPI_CR, the OCTOSPI is in indirect-write mode: bytes are
sent to the external device during the data phase. Data are provided by writing to
OCTOSPI_DR.
When FMODE[1:0] = 01, the OCTOSPI is in indirect-read mode: bytes are received from the
external device during the data phase. Data are recovered by reading OCTOSPI_DR.
In indirect mode, when the OCTOSPI is configured in DTR mode over eight lanes with DQS
disabled, the given starting address and the data length must be even.
Note: The OCTOSPI_AR register must be updated even if the start address is the same as the
start address of the previous indirect access.
The number of bytes to be read/written is specified in OCTOSPI_DLR:
• If DL[31:0] = 0xFFFF FFFF, the data length is considered undefined and the OCTOSPI
simply continues to transfer data until it reaches the end of the external device (as

RM0438 Rev 8 643/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
defined by DEVSIZE). If no bytes are to be transferred, DMODE[2:0] must be set to 0 in
OCTOSPI_CCR.
• If DL[31:0] = 0xFFFF FFFFF and DEVSIZE[4:0] = 0x1F (its maximum value indicating
at 4-Gbyte device), the transfers continue indefinitely, stopping only after an abort
request or after the OCTOSPI is disabled. After the last memory address is read (at
address 0xFFFF FFFF), reading continues with address = 0x0000 0000.
When the programmed number of bytes to be transmitted or received is reached, the TCF
bit is set in OCTOSPI_SR, and an interrupt is generated if TCIE = 1 in OCTOSPI_CR. In the
case of an undefined number of data, TCF is set when the limit of the external SPI memory
is reached, according to the device size defined in OCTOSPI_DCR1.
Triggering the start of a transfer in regular-command protocol
Depending on the OCTOSPI configuration, there are three different ways to trigger the start
of a transfer in indirect mode when using the regular-command protocol. In general, the start
of transfer is triggered as soon as the software gives the last information that is necessary
for the command. More specifically in indirect mode, a transfer starts when one of the
following sequence of events occurs:
• if no address is necessary (ADMODE[2:0] = 000) and if no data need to be provided by
the software (FMODE[1:0] = 01 or DMODE[2:0] = 000), and at the moment when a
write is performed to INSTRUCTION[31:0] in OCTOSPI_IR
• if an address is necessary (when ADMODE[2:0] ≠ 000) and if no data need to be
provided by the software (when FMODE[1:0] = 01 or DMODE[2:0] = 000), and at the
moment when a write is performed to ADDRESS[31:0] in OCTOSPI_AR
• if data need to be provided by the software (when FMODE[1:0] = 00 and
DMODE[2:0] ≠ 000), and at the moment when a write is performed to DATA[31:0] in
OCTOSPI_DR
A write to OCTOSPI_ABR never triggers the communication start. If alternate bytes are
required, they must have been programmed before.
As soon as a command is started, the BUSY bit is automatically set in OCTOSPI_SR.
Triggering the start of a transfer in HyperBus protocol
Depending on the OCTOSPI configuration, there are different ways to trigger the start of a
command in indirect mode. In general, it is triggered as soon as the firmware gives the last
information that is necessary for the transfer to start, and more specifically, a communication
in indirect mode is triggered by one of the following register settings, when it is the last one
to be executed:
• when a write is performed to ADDRESS[31:0] (OCTOSPI_AR) with
ADMODE[2:0] ≠ 000 in indirect read mode (FMODE[1:0] = 01).
• when a write is performed to DATA[31:0] (OCTOSPI_DR) in indirect-write mode (when
FMODE = 00).
• when a (dummy) write is performed to INSTRUCTION[31:0] (OCTOSPI_IR) for indirect
read mode (with ADMODE[2:0] = 000 and FMODE = 01).
As soon as a transfer is started, the BUSY bit (OCTOSPI_SR[5]) is automatically set.
FIFO and data management
Data in indirect mode passes through a 32-byte FIFO that is internal to the OCTOSPI.
FLEVEL in OCTOSPI_SR indicates how many bytes are currently being held in the FIFO.

Octo-SPI interface (OCTOSPI) RM0438
644/2187 RM0438 Rev 8
AHB burst transactions are supported. Data of the burst are successively written
in OCTOSPI_DR, and immediately transferred in the internal FIFO.
In indirect-write mode (FMODE[1:0] = 00), the software adds data to the FIFO when it writes
in OCTOSPI_DR. A word write adds 4 bytes to the FIFO, a half-word write adds 2 bytes,
and a byte write adds only 1 byte. If the software adds too many bytes to the FIFO (more
than indicated in DL[31:0]), the extra bytes are flushed from the FIFO at the end of the write
operation (when TCF is set).
The byte/half-word accesses to OCTOSPI_DR must be done only to the least significant
byte/halfword of the 32-bit register.
FTHRES is used to define a FIFO threshold after which point the FIFO threshold flag, FTF,
gets set. In indirect-read mode, FTF is set when the number of valid bytes to be read from
the FIFO is above the threshold. FTF is also set if there is any data left in the FIFO after the
last byte is read from the external device, regardless of FTHRES setting. In indirect-write
mode, the FTF is set when the number of empty bytes in the FIFO is above the threshold.
If FTIE = 1, there is an interrupt when the FTF is set. If DMAEN = 1, a DMA transfer is
initiated when the FTF is set. The FTF is cleared by hardware as soon as the threshold
condition is no longer true (after enough data has been transferred by the CPU or DMA).
The last data read in RX FIFO remains valid as long as there is no request for the next line.
This means that, when the application reads several times in a row at the same location, the
data is provided from the RX FIFO and not read again from the distant memory.
20.4.10 OCTOSPI automatic status-polling mode
In automatic status-polling mode, the OCTOSPI periodically starts a command to read a
defined number of status bytes (up to four). The received bytes can be masked to isolate
some status bits and an interrupt can be generated when the selected bits have a defined
value. The automatic status-polling mode must be used only in regular-command protocol.
For HyperBus protocol, it is not exploitable since the read status register into the
HyperFlash memory must be performed in two steps (a write operation followed by a read
operation).
The access to the device begins in the same manner as in indirect-read mode. BUSY in
OCTOSPI_SR goes high at this point and stays high even between the periodic accesses.
The content of MASK[31:0] in OCTOSPI_PSMAR is used to mask the data from the
external device in automatic status-polling mode:
• If the MASK[n] = 0, then bit n of the result is masked and not considered.
• If MASK[n] = 1, and the content of bit[n] is the same as MATCH[n] in
OCTOSPI_PSMAR, then there is a match for bit n.
If PMM = 0 in OCTOSPI_CR, the AND-match mode is activated: SMF is set in
OCTOSPI_SR only when there is a match on all of the unmasked bits.
If PMM = 1 in OCTOSPI_CR, the OR-match mode is activated: SMF gets set if there is a
match on any of the unmasked bits.
An interrupt is called when SMF = 1 if SMIE = 1.
If APMS is set in OCTOSPI_CR, the operation stops and BUSY goes to 0 as soon as a
match is detected. Otherwise, BUSY stays at 1 and the periodic accesses continue until
there is an abort or until the OCTOSPI is disabled (EN = 0).

RM0438 Rev 8 645/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
OCTOSPI_DR contains the latest received status bytes (FIFO deactivated). The content of
this register is not affected by the masking used in the matching logic. FTF in OCTOSPI_SR
is set as soon as a new reading of the status is complete. FTF is cleared as soon as the
data is read.
In automatic status-polling mode, variable latency is not supported. The memory must then
be configured in fixed latency.
20.4.11 OCTOSPI memory-mapped mode
When configured in memory-mapped mode, the external SPI device is seen as an internal
memory.
Note: No more than 256  Mbytes can be addressed even if the external device capacity is larger.
If an access is made to an address outside of the range defined by DEVSIZE[4:0] but still
within the 256 Mbytes range, then an AHB error is given. The effect of this error depends on
the AHB master that attempted the access:
• If it is the Cortex CPU, a hard-fault interrupt is generated.
• If it is a DMA, a DMA transfer error is generated, and the corresponding DMA channel
is automatically disabled.
Byte, half-word, and word access types are all supported.
A support for execute in place (XIP) operation is implemented, where the OCTOSPI
continues to load the bytes to the addresses following the most recent access. If
subsequent accesses are continuous to the bytes that follow, then these operations end up
quickly since their results were prefetched.
By default, the OCTOSPI never stops its prefetch operation. It either keeps the previous
read operation active with the NCS maintained low or it relaunches a new transfer, even
if no access to the external device occurs for a long time.
Since external devices tend to consume more power when the NCS is held low, the
application may want to activate the timeout counter (TCEN = 1 in OCTOSPI_CR): the NCS
is released after a period defined by TIMEOUT[15:0] in OCTOSPI_LPTR, when x cycles
have elapsed without access since the clock is inactive.
BUSY goes high as soon as the first memory-mapped access occurs. Because of the
prefetch operations, BUSY does not fall until there is an abort, or the peripheral is disabled.
It is not recommended to program the flash memory using the memory-mapped writes.
The indirect-write mode fulfills this operation.
However, if the application requires the use of the MCE for encryption (check MCE product
availability), the memory-mapped write mode may be used to program encrypted data to
external flash memory under the following conditions:
• Prefetch must be enabled.
• In block cipher mode, the CPU must write a complete 128-bit data block to prevent the
MCE from initiating read-modify-write operations when only a few bytes need to be

Octo-SPI interface (OCTOSPI) RM0438
646/2187 RM0438 Rev 8
programmed. This precaution avoids incorrect programming operations. There are no
specific constraints to respect if the MCE is used in stream cipher mode.
• Apply the abort sequence to exit memory-mapped mode when the data linked to the
page has been written in the external memory buffers. The abort sequence triggers the
start of the page programming.
• Switch to the automatic status-polling mode to monitor the completion of the page
programing phase.
• Relaunch the write enable command in indirect mode, then switch back to the
memory-mapped mode configuration to continue to program additional pages if any.
It is recommended to add a synchronization barrier between the end of the controller
registers configuration and the first memory-mapped access to the external memory when
the controller is configured in memory-mapped mode.
20.4.12 OCTOSPI confi guration introduction
The OCTOSPI configuration is done in three steps:
1. OCTOSPI system configuration
2. OCTOSPI device configuration
3. OCTOSPI mode configuration
20.4.13 OCTOSPI system configuration
The OCTOSPI is configured using OCTOSPI_CR. The user must program:
• the functional mode with FMODE[1:0]
• the automatic status-polling mode behavior if needed with PMM and APMS
• the FIFO level with FTHRES
• the DMA use with DMAEN
• the timeout counter use with TCEN
• the dual-memory configuration, if needed, with DMM
In case of an interrupt use, the respective enable bit can also be set during this phase.
If the timeout counter is used, the timeout value is programmed in OCTOSPI_LPTR.
The DMA channel must not be enabled during the OCTOSPI configuration: it must be
enabled only when the operation is fully configured, to avoid any unexpected request
generation.
The DMA and OCTOSPI must be configured in a coherent manner regarding data length:
FTHRES value must reflect the DMA burst size.
20.4.14 OCTOSPI device configuration
The parameters related to the external device targeted are configured through
OCTOSPI_DCR1 and OCTOSPI_DCR2.The user must program:
• the device size with DEVSIZE[4:0]
• the chip-select minimum high time with CSHT[2:0]
• the clock mode with FRCK and CKMODE
• the device frequency with PRESCALER[7:0]

RM0438 Rev 8 647/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
DEVSIZE[4:0] defines the size of external memory using the following formula:
Number of bytes in the device = 2DEVSIZE+1
where DEVSIZE+1 is the number of address bits required to address the external device.
The external device capacity can go up to 4 Gbytes (addressed using 32 bits) in indirect
mode, but the addressable space in memory-mapped mode is limited to 256 Mbytes.
If DMM = 1, DEVSIZE[4:0] must reflect the total capacity of the two devices together
considering the above formula (DEVSIZE[4:0] value is so equal to one of the two memory
capacities).
When the OCTOSPI executes two commands, one immediately after the other, it raises the
chip-select signal (NCS) high between the two commands for only one CLK cycle by default.
If the external device requires more time between commands, the chip-select high time
CSHT[2:0] can be used to specify the minimum number of CLK cycles for which the NCS
must remain high.
CKMODE indicates the level that the CLK takes between commands (when NCS = 1).
In HyperBus protocol, the device timing (tACC and tRWR) and the latency mode must be
configured in OCTOSPI_HLCR.
Memory types
External memory providers may present some architecture and slight data formatting
differences between them. The bitfield MTYP[2:0] into the OCTOSPI_CR register allows
targeting the right controller configuration depending on the associated memory type
selected in the application. This is the responsibility of the software developer to align the
controller configuration to fit with the targeted memory type.
The memory types are grouped in a such way:
• D0/D1 data ordering in octal-SPI data mode (DMODE[2:0] = 100) in DTR mode by
configuring MTYP[2:0] = 000. For instance, Micron is using such data ordering. In this
configuration, the DQS is sent with a polarity inverted respect to the clock polarity.
[Figure 87](../figures/figure_87.md). D0/D1 data ordering in octal-SPI DTR mode (Micron) - Read access
• D1/D0 data ordering in octal-SPI data mode (DMODE[2:0] = 100) in DTR mode by
configuring MTYP[2:0] = 001. For instance, Macronix is using this reverse data
ordering in its Octaflash portfolio (this configuration is not adapted to its OctaRAM™
memories). DQS is keeping the same polarity as the clock when reading data from the
MSv71558V1
NCS
Dummy
IO[7:0]
Address
§ §§§
CLK
DQS
A[31:24]EEh     11h D0 D1 D2 D3A[23:16] A[15:8] A[7:0]
Word
unit
Word
unit

Octo-SPI interface (OCTOSPI) RM0438
648/2187 RM0438 Rev 8
memory. Refer to [Figure 78](../figures/figure_78.md): DTR read in octal-SPI mode with DQS (Macronix mode)
example.
• D1/D0 data ordering in octal-SPI data mode (DMODE[2:0] = 100) in DTR mode by
configuring MTYP[2:0] = 011 with specific address phase built with row and column to
fit with Macronix OctaRAM™ memories requirement (refer to [Table 160](../tables/table_160.md): OctaRAM
command address bit assignment (based on 64-Mbyte OctaRAM). This is the controller
which translates internally the targeted address provided by the software in row/column
address formatting to sent to the memory. DQS is keeping the same polarity as the
clock one when reading data from the memory.
[Figure 88](../figures/figure_88.md). OctaRAM read operation with reverse data ordering D1/D0
• HyperBus memories need to be selected when targeted by the application. The
configuration to set depends on the access type:
– HyperBus memory mode: The protocol follows the HyperBus specification.
MTYP[2:0] = 100 is the configuration to use to access the memory space.
– HyperBus register mode (addressing register space): the memory-mapped
accesses in this mode must be noncacheable, or the indirect read/write modes
MSv71560V1
NCS
IO[7:0]
CLK
D1 D0 D3 D2
Word Unit Word Unit
§ §§§
DQS
Command Raw address Column address
Command & Address
[Table 160](../tables/table_160.md). OctaRAM command address bit assignment
(based on 64-Mbyte(1) OctaRAM)
1. Example of 64-Mbyte OctaRAM address assignment:
Row Address [RA12:RA0]: 8K. Column address [CA9:CA0]: 1K. 64-Mbyte density = 8K x 1K x 8 bits
Clock 1st clock 2nd clock 3rd clock
Function Command Row address Column address
SIO[7]
Command
Reserved RA7 CA9 Reserved
SIO[6] Reserved RA6 CA8 Reserved
SIO[5] Reserved RA5 CA7 Reserved
SIO[4] RA12 RA4 CA6 Reserved
SIO[3] RA11 RA3 CA5 CA3
SIO[2] RA10 RA2 CA4 CA2
SIO[1] RA9 RA1 Reserved CA1
SIO[0] RA8 RA0 Reserved CA0 (2)
2. Column address A0 must be always 0.

RM0438 Rev 8 649/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
must be used. The configuration to be set for this particular register space access
is MTYP[2:0] = 101.
• Standard mode. It is the mode to use whenever the targeted memory is not
corresponding to any others configurations described in this section. MTYP[2:0] = 010
for this standard mode.
20.4.15 OCTOSPI regular-co mmand mode configuration
Indirect mode configuration
When FMODE[1:0] = 00, the indirect-write mode is selected and data can be sent to the
external device. When FMODE[1:0] = 01, the indirect-read mode is selected, and data can
be read from the external device.
When the OCTOSPI is used in indirect mode, the frames are constructed in the following
way:
1. Specify a number of data bytes to read or write in OCTOSPI_DLR.
2. Specify the frame timing in OCTOSPI_TCR.
3. Specify the frame format in OCTOSPI_CCR.
4. Specify the instru ction in OCTOSPI_IR.
5. Specify the optional alternate byte to be sent right after the address phase in
OCTOSPI_ABR.
6. Specify the targeted address in OCTOSPI_AR.
7. Enable the DMA channel if needed.
8. Read/write the data from/to the FIFO through OCTOSPI_DR (if no DMA usage).
If neither the address register (OCTOSPI_AR) nor the data register (OCTOSPI_DR) need to
be updated for a particular command, then the command sequence starts as soon as
OCTOSPI_IR is written. This is the case when both ADMODE[2:0] and DMODE[2:0]
equal 000, or if just ADMODE[2:0] = 000 when in indirect-read mode (FMODE[1:0] = 01).
When an address is required (ADMODE[2:0] ≠ 000) and the data register does not need to
be written (FMODE[1:0] = 01 or DMODE[2:0] = 000), the command sequence starts as
soon as the address is updated with a write to OCTOSPI_AR.
In case of data transmission (FMODE[1:0] = 00 and DMODE[2:0] ≠ 000),
the communication start is triggered by a write in the FIFO through OCTOSPI_DR.
Automatic status-polling mode configuration
The automatic status-polling mode is enabled by setting FMODE[1:0] = 10. In this mode, the
programmed frame is sent and data are retrieved periodically.
The maximum amount of data read in each frame is 4 bytes. If more data is requested in
OCTOSPI_DLR, it is ignored, and only 4 bytes are read. The periodicity is specified in
OCTOSPI_PIR.
Once the status data has been retrieved, the following can be processed:
• Set SMF (an interrupt is generated if enabled).
• Stop automatically the periodic retrieving of the status bytes.
The received value can be masked with the value stored in OCTOSPI_PSMKR, and can be
ORed or ANDed with the value stored in OCTOSPI_PSMAR.

Octo-SPI interface (OCTOSPI) RM0438
650/2187 RM0438 Rev 8
In case of a match, SMF is set and an interrupt is generated if enabled. The OCTOSPI can
be automatically stopped if AMPS is set. In any case, the latest retrieved value is available
in OCTOSPI_DR.
When the OCTOSPI is used in automatic status-polling mode, the frames are constructed in
the following way:
1. Specify the input mask in OCTOSPI_PSMKR.
2. Specify the comparison  value in OCTOSPI_PSMAR.
3. Specify the read period in OCTOSPI_PIR.
4. Specify a number of data bytes to read in OCTOSPI_DLR.
5. Specify the frame timing in OCTOSPI_TCR.
6. Specify the frame format in OCTOSPI_CCR.
7. Specify the instru ction in OCTOSPI_IR.
8. Specify the optional alternate byte to be sent right after the address phase in
OCTOSPI_ABR.
9. Specify the optional targeted address in OCTOSPI_AR.
If the address register (OCTOSPI_AR) does not need to be updated for a particular
command, then the command sequence starts as soon as OCTOSPI_CCR is written. This
is the case when ADMODE[2:0] = 000.
When an address is required (ADMODE[2:0] ≠ 000), the command sequence starts as soon
as the address is updated with a write to OCTOSPI_AR.
Memory-mapped mode configuration
In memory-mapped mode, the external device is seen as an internal memory but with some
latency during accesses. Read and write operations are allowed to the external device in
this mode.
It is not recommended to program the flash memory using memory-mapped writes, as the
internal flags for erase or programming status have to be polled. The indirect-write mode
fulfills this operation, possibly in conjunction with the automatic status-polling mode.
The memory-mapped mode is entered by setting FMODE[1:0] = 11 in OCTOSPI_CR.
The programmed instruction and frame are sent when an AHB master accesses the
memory-mapped space.
The FIFO is used as a prefetch buffer to anticipate any linear reads. Any access to
OCTOSPI_DR in this mode returns zero.
The data length register (OCTOSPI_DLR) has no meaning in memory-mapped mode.
When the OCTOSPI is used in memory-mapped mode, the frames are constructed
in the following way:
1. Specify the frame timing in OCTOSPI_TCR for read operation.
2. Specify the frame format in OCTOSPI_CCR for read operation.
3. Specify the instru ction in OCTOSPI_IR.
4. Specify the optional alternate byte to be sent right after the address phase in
OCTOSPI_ABR for read operation.
5. Specify the frame timing in OCTOSPI_WTCR for write operation.
6. Specify the frame format in OCTOSPI_WCCR for write operation.

RM0438 Rev 8 651/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
7. Specify the instruction in OCTOSPI_WIR.
8. Specify the optional alternate byte to be sent right after the address phase in
OCTOSPI_WABR for write operation.
All configuration operations must be completed (ensured by checking BUSY = 0) before the
first access to the memory area: any register write operation when BUSY = 1 has no effect
and is not signaled with an error response. On the first access, the OCTOSPI becomes
busy, and no further configuration is allowed. Then, the only way to get BUSY low is to clear
the ENABLE bit or to abort by setting the ABORT bit.
OCTOSPI delayed data sampling when no DQS is used
By default, when no DQS is used, the OCTOSPI samples the data driven by the external
device one half of a CLK cycle after the external device drives the signal.
In case of any external signal delays, it may be useful to sample the data later. Using
SSHIFT in OCTOSPI_TCR, the sampling of the data can be shifted by half of a CLK cycle.
The firmware must clear SSHIFT when the data phase is configured in DTR mode
(DDTR = 1).
OCTOSPI delayed data sampling when DQS is used
When external DQS is used as a sampling clock, it can be shifted in time to compensate the
data propagation delay.
This shift is performed by a delay hardware element located outside of the controller into the
RCC (RCC_DLYCFGR) or implemented on an external dedicated block delay peripheral
depending on the product (refer to the product reference manual for information about how
to manage and configure the delay).
In configurations where delay does not need to be compensated, the external delay block
can be bypassed by setting DLYBYP in OCTOSPI_DCR1.
Sending the instruction only once (SIOO)
A flash memory can provide a mode where an instruction must be sent only with the first
command sequence, while subsequent commands start directly with the address. The user
can take advantage of this type of features using SIOO in OCTOSPI_CCR.
SIOO is valid for memory-mapped mode only. If this bit is set, the instruction is sent only for
the first command following a write to OCTOSPI_CCR.
Subsequent command sequences skip the instruction phase, until there is a write to
OCTOSPI_CCR. SIOO has no effect when IMODE[1:0] = 00 (no instruction).
The SIOO mode is not supported when any of the communication regulations, NCS
boundary, or refresh features are used.
20.4.16 OCTOSPI HyperBus protocol configuration
Indirect mode configuration (HyperBus)
When FMODE[1:0] = 00, the indirect-write mode is selected and data can be sent to the
external device. When FMODE[1:0] = 01, the indirect-read mode is selected where data can
be read from the external device. ADMODE must be configured with a value different from
000 (for instance ADMODE = 100).

Octo-SPI interface (OCTOSPI) RM0438
652/2187 RM0438 Rev 8
When the OCTOSPI is used in indirect mode, the frames are constructed in the following
way:
1. Specify a number of data bytes to read or write in OCTOSPI_DLR.
2. Specify the targeted address in OCTOSPI_AR.
3. Enable the DMA channel if needed.
4. Read/write the data from/to the FIFO through OCTOSPI_DR (if no DMA usage).
In indirect-read mode, the command sequence starts as soon as the address is updated
with a write to OCTOSPI_AR.
In indirect-write mode, the communication start is triggered by a write in the FIFO through
OCTOSPI_DR.
Memory-mapped mode configuration (HyperBus)
In memory-mapped mode, the external device is seen as an internal memory but with some
latency during the accesses. Read and write operations are allowed to the external device in
this mode.
It is not recommended to program the flash memory using the memory-mapped writes:
the indirect-write mode fulfills this operation.
The memory-mapped mode is entered by setting FMODE[1:0] = 11. The programmed
instruction and frame is sent when an AHB master accesses the memory-mapped space.
The FIFO is used as a prefetch buffer to anticipate any linear reads. Any access to
OCTOSPI_DR in this mode returns zero.
The data length register (OCTOSPI_DLR) has no meaning in memory-mapped mode.
All the configuration operation must be completed before the first access to the memory
area. On the first access, the OCTOSPI becomes busy, and no configuration is allowed.
Then, the only way to get BUSY low is to clear the ENABLE bit, or to abort by setting the
ABORT bit.
20.4.17 OCTOSPI error management
The following errors set the TEF flag in OCTOSPI_SR and generates an interrupt if enabled
(TEIE = 1 in OCTOSPI_CR):
• in indirect or automatic status-polling mode, when a wrong address has been
programmed in OCTOSPI_AR (according to the device size defined by DEVSIZE[4:0]).
• in indirect mode, if the address plus the data length exceed the device size: TEF is set
as soon as the access is triggered.
In memory-mapped mode, the OCTOSPI generates an AHB slave error in the following
situations,:
• The memory-mapped mode is disabled and an AHB read or write request occurs.
• A read or write address exceeds the size of the external memory.
• An abort is received while a read or write burst is ongoing.
• The OCTOSPI is disabled while a read or write burst is requested.
• A write wrap burst is received.
• A write request is received while DQSE = 0 in OCTOSPI_WCCR in octal DTR mode, in
dual-memory configuration, in HyperBus mode.

RM0438 Rev 8 653/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
• A read or write request is received while DMODE[2:0] = 000 (no data phase), except
when MTYP[2:0] is HyperBus.
• Illegal access size when wrap read burst. This means that the AHB bus transfer size
(HSIZE) is different from 4 bytes (only for memory-mapped mode).
• Bit DMM is set in OCTOSPI_CR (dual-memory configuration) and octal mode is set.
20.4.18 OCTOSPI BUSY and ABORT
Once the OCTOSPI starts an operation with the external device, BUSY is automatically set
in OCTOSPI_SR.
In indirect mode, BUSY is reset once the OCTOSPI has completed the requested command
sequence and the FIFO is empty.
In automatic status-polling mode, BUSY goes low only after the last periodic access is
complete, due to a match when APMS = 1 or due to an abort.
After the first access in memory-mapped mode, BUSY goes low only on an abort.
Any operation can be aborted by setting ABORT in OCTOSPI_CR. Once the abort is
completed, BUSY and ABORT are automatically reset, and the FIFO is flushed.
Before setting ABORT, the software must ensure that all the current transactions are
finished using the synchronization barriers. When DMA is enabled to handle the data read
or write operations in OCTOSPI_DR, it is recommended to disable the DMA channel before
aborting the OCTOSPI.
Note: Some devices may misbehave if a write ope ration to a status register is aborted.
20.4.19 OCTOSPI reconfi guration or deactivation
Before any OCTOSPI reconfiguration, the software must ensure that all the transactions are
completed:
• After a memory-mapped write, the software must perform a dummy read followed
by a synchronization barrier, then an abort.
• After a memory-mapped read, the software must perform a synchronization barrier
than an abort.
20.4.20 NCS behavior
By default, NCS is high, deselecting the external device. NCS falls before an operation
begins and rises as soon as it finishes.
When CKMODE = 0 (clock mode 0: CLK stays low when no operation is in progress), NCS
falls one CLK cycle before an operation first rising CLK edge, and NCS rises one CLK cycle
after the operation final rising CLK edge (see the figure below).

Octo-SPI interface (OCTOSPI) RM0438
654/2187 RM0438 Rev 8
[Figure 89](../figures/figure_89.md). NCS when CKMODE = 0 (T = CLK period)
When CKMODE = 1 (clock mode 3: CLK goes high when no operation is in progress) and
when in SDR mode, NCS falls one CLK cycle before an operation first rising CLK edge, and
NCS rises one CLK cycle after the operation final rising CLK edge (see the figure below).
[Figure 90](../figures/figure_90.md). NCS when CKMODE = 1 in SDR mode (T = CLK period)
When the CKMODE = 1 (clock mode 3) and DDTR = 1 (data DTR mode), NCS falls one
CLK cycle before an operation first rising CLK edge, and NCS rises one CLK cycle after the
operation final active rising CLK edge (see the figure below). Because the DTR operations
must finish with a falling edge, CLK is low when NCS rises, and CLK rises back up one half
of a CLK cycle afterwards.
[Figure 91](../figures/figure_91.md). NCS when CKMODE = 1 in DTR mode (T = CLK period)
When the FIFO stays full during a read operation, or if the FIFO stays empty during a write
operation, the operation stalls and CLK stays low until the software services the FIFO. If an
MSv44100V2
NCS
CLK
T T
MSv44101V2
NCS
CLK
T T
MSv44102V2
NCS
CLK
T T
T/2

RM0438 Rev 8 655/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
abort occurs when an operation is stalled, NCS rises just after the abort is requested and
then CLK rises one half of a CLK cycle later (see the figure below).
[Figure 92](../figures/figure_92.md). NCS when CKMODE = 1 with an abort (T = CLK period)
20.5  Address alignment and data number
The table below summarizes the effect of the address alignment and programmed data
number depending on the use case.
MSv44103V2
NCS
CLK
T
T/2
Clock stalled
Abort
[Table 161](../tables/table_161.md). Address alignment cases
Memory type Transaction
type
Constraint
on
address(1)
Impact if constraint
on address not
respected
Constraint
on number
of bytes(1)
Impact if constraint
on bytes not
respected
Single, dual, quad flash
or SRAM (DMM = 0)
IND(2) read
None None None None
MM(3) read
IND write
MM write
Single, dual, quad flash
or SRAM (DMM = 1)
IND read Even ADDR[0] is set to 0. (4) Even DLR[0] is set to 1. (5)
MM read None None None None
IND write Even ADDR[0] is set to 0. (4) Even DLR[0] is set to 1. (5)
MM write Even Slave error Even Last byte is lost.
Octal flash in SDR mode
IND read
None None None None
MM read
IND write
MM write
Octal memory in DTR
mode without WDM(6)
IND read Even ADDR[0] is set to 0. (4) Even DLR[0] is set to 1. (5)
MM read None None None None
IND write Even ADDR[0] is set to 0. (4) Even DLR[0] is set to 1. (5)
MM write Even Slave error Even Last byte is lost.

Octo-SPI interface (OCTOSPI) RM0438
656/2187 RM0438 Rev 8
20.6 OCTOSPI interrupts
An interrupt can be produced on the following events:
• Timeout
• Status match
• FIFO threshold
• Transfer complete
• Transfer error
Separate interrupt enable bits are available to provide more flexibility.
Octal flash or RAM in
DTR mode with WDM
IND read Even ADDR[0] is set to 0. (4) Even DLR[0] is set to 1. (5)
MM read
None None None NoneIND write(7)
MM write
HyperBus
IND read Even ADDR[0] is set to 0. (4) Even DLR[0] is set to 1. (5)
MM read
None None None NoneIND write(7)
MM write
1. To be respected by the software.
2. IND = indirect mode.
3. MM = memory-mapped mode
4. Extra data at transfer start.
5. Extra data at transfer end.
6. WDM = write data mask.
7. If the FTHRES bitfield is set to the maximum value with DLR value greater than the data burst length, and if the DMA is
enabled or the interrupt based on FIFO THRESHOLD Flag is enabled (FTF), the address must be modulo 2 aligned in DTR
mode when the initiator (DMA, CPU, ...) is writing the data with a burst length equal to the FIFO size.
[Table 161](../tables/table_161.md). Address alignment cases (continued)
Memory type Transaction
type
Constraint
on
address(1)
Impact if constraint
on address not
respected
Constraint
on number
of bytes(1)
Impact if constraint
on bytes not
respected
[Table 162](../tables/table_162.md). OCTOSPI interrupt requests
Interrupt event Event flag Enable control bit
Timeout TOF TOIE
Status match SMF SMIE
FIFO threshold FTF FTIE
Transfer complete TCF TCIE
Transfer error TEF TEIE

RM0438 Rev 8 657/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
20.7 OCTOSPI registers
20.7.1 OCTOSPI control register (OCTOSPI_CR)
Address offset: 0x0000
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. FMODE[1:0] Res. Res. Res. Res. PMM APMS Res. TOIE SMIE FTIE TCIE TEIE
rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. FTHRES[4:0] FSEL DMM Res. Res. TCEN DMAE
N ABORT EN
rw rw rw rw rw rw rw rw rw rw rw
Bits 31:30 Reserved, must be kept at reset value.
Bits 29:28 FMODE[1:0]: Functional mode
This bitfield defines the OCTOSPI functional mode of operation.
00: Indirect-write mode
01: Indirect-read mode
10: Automatic status-polling mode (relevant in regular-command protocol only)
11: Memory-mapped mode
If DMAEN = 1 already, then the DMA controller for the corresponding channel must be
disabled before changing the FMODE[1:0] value.
Note: This bitfield can be modified only when BUSY = 0.
Bits 27:24 Reserved, must be kept at reset value.
Bit 23 PMM: Polling match mode
This bit indicates which method must be used to determine a match during the automatic
status-polling mode.
0: AND-match mode, SMF is set if all the unmasked bits received from the device match the
corresponding bits in the match register.
1: OR-match mode, SMF is set if any of the unmasked bits received from the device matches
its corresponding bit in the match register.
Note: This bit can be modified only when BUSY = 0.
Bit 22 APMS: Automatic status-polling mode stop
This bit determines if the automatic status-polling mode is stopped after a match.
0: Automatic status-polling mode is stopped only by abort or by disabling the OCTOSPI.
1: Automatic status-polling mode stops as soon as there is a match.
Note: This bit can be modified only when BUSY = 0.
Bit 21 Reserved, must be kept at reset value.
Bit 20 TOIE: Timeout interrupt enable
This bit enables the timeout interrupt.
0: Interrupt disabled
1: Interrupt enabled

Octo-SPI interface (OCTOSPI) RM0438
658/2187 RM0438 Rev 8
Bit 19 SMIE: Status-match interrupt enable
This bit enables the status-match interrupt.
0: Interrupt disabled
1: Interrupt enabled
Bit 18 FTIE: FIFO threshold interrupt enable
This bit enables the FIFO threshold interrupt.
0: Interrupt disabled
1: Interrupt enabled
Bit 17 TCIE: Transfer complete interrupt enable
This bit enables the transfer complete interrupt.
0: Interrupt disabled
1: Interrupt enabled
Bit 16 TEIE: Transfer error interrupt enable
This bit enables the transfer error interrupt.
0: Interrupt disabled
1: Interrupt enabled
Bits 15:13 Reserved, must be kept at reset value.
Bits 12:8 FTHRES[4:0]: FIFO threshold level
This bitfield defines, in indirect mode, the threshold number of bytes in the FIFO that causes
the FIFO threshold flag FTF in OCTOSPI_SR, to be set.
00000: FTF is set if there are one or more free bytes available to be written to in the FIFO
in indirect-write mode, or if there are one or more valid bytes can be read from the FIFO
in indirect-read mode.
00001: FTF is set if there are two or more free bytes available to be written to in the FIFO
in indirect-write mode, or if there are two or more valid bytes can be read from the FIFO
in indirect-read mode.
...
11111: FTF is set if there are 32 free bytes available to be written to in the FIFO in
indirect-write mode, or if there are 32 valid bytes can be read from the FIFO in indirect-read
mode.
Note: If DMAEN = 1, the DMA controller for the corresponding channel must be disabled
before changing the FTHRES[4:0] value.
Bit 7 FSEL: Flash select
This bit selects the flash memory to be addressed in single-, dual-, quad-SPI mode in
single-memory configuration (when DMM = 0).
0: FLASH 1 selected (data exchanged over IO[3:0])
1: FLASH 2 selected (data exchanged over IO[7:4])
This bit is ignored when DMM = 1 or when octal-SPI mode is selected.
Bit 6 DMM: Dual-memory configuration
This bit activates the dual-memory configuration, where two external devices are used
simultaneously to double the throughput and the capacity
0: Dual-memory configuration disabled
1: Dual-memory configuration enabled
Note: This bit can be modified only when BUSY = 0.
Bits 5:4 Reserved, must be kept at reset value.

RM0438 Rev 8 659/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
20.7.2 OCTOSPI device configurat ion register 1 (OCTOSPI_DCR1)
Address offset: 0x0008
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
Bit 3 TCEN: Timeout counter enable
This bit is valid only when the memory-mapped mode (FMODE[1:0] = 11) is selected. This bit
enables the timeout counter.
0: The timeout counter is disabled, and thus the chip-select (NCS) remains active indefinitely
after an access in memory-mapped mode.
1: The timeout counter is enabled, and thus the chip-select is released in the memory-
mapped mode after TIMEOUT[15:0] cycles of external device inactivity.
Note: This bit can be modified only when BUSY = 0.
Bit 2 DMAEN: DMA enable
In indirect mode, the DMA can be used to input or output data via OCTOSPI_DR. DMA
transfers are initiated when FTF is set.
0: DMA disabled for indirect mode
1: DMA enabled for indirect mode
Note: Resetting the DMAEN bit while a DMA transfer is ongoing, breaks the handshake with
the DMA. Do not write this bit during DMA operation.
Bit 1 ABORT: Abort request
This bit aborts the ongoing command sequence. It is automatically reset once the abort is
completed. This bit stops the current transfer.
0: No abort requested
1: Abort requested
Note: This bit is always read as 0.
Bit 0 EN: Enable
This bit enables the OCTOSPI.
0: OCTOSPI disabled
1: OCTOSPI enabled
Note: The DMA request can be aborted without having received the ACK in case this EN bit is
cleared during the operation.
In case this bit is set to 0 during a DMA transfer, the REQ signal to DMA returns to
inactive state without waiting for the ACK signal from DMA to be active.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. MTYP[2:0] Res. Res. Res. DEVSIZE[4:0]
rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. CSHT[2:0] Res. Res. Res. Res. DLY
BYP Res. FRCK CKMO
DE
rw rw rw rw rw rw
Bits 31:27 Reserved, must  be kept at reset value.

Octo-SPI interface (OCTOSPI) RM0438
660/2187 RM0438 Rev 8
Bits 26:24 MTYP[2:0]: Memory type
This bitfield indicates the type of memory to be supported.
000: Micron mode, D0/D1 ordering in DTR 8-data-bit mode. regular-command protocol in
single-, dual-, quad- and octal-SPI modes.
Note: In this mode, DQS signal polarity is inverted with respect to the memory clock signal.
This is the default value and care must be taken to change MTYP[2:0] for memories different
from Micron.
001: Macronix mode, D1/D0 ordering in DTR 8-data-bit mode. Regular-command protocol
in single-, dual-, quad-, and octal-SPI modes.
010: Standard mode
011: Macronix RAM mode, D1/D0 ordering in DTR 8-data-bit mode. Regular-command
protocol in single-, dual-, quad-, and octal-SPI modes with dedicated address mapping
(address is built with row and column to fit with Macronix requirements).
100: HyperBus memory mode, the protocol follows the HyperBus specification.
101: HyperBus register mode, addressing register space. The memory-mapped accesses in
this mode must be noncacheable, or indirect-read/write modes must be used.
Others: Reserved
Bits 23:21 Reserved, must  be kept at reset value.
Bits 20:16 DEVSIZE[4:0]: Device size
This bitfield defines the size of the external device using the following formula:
Number of bytes in device = 2[DEVSIZE+1].
DEVSIZE + 1 is effectively the number of address bits required to address the external
device. The device capacity can be up to 4 Gbytes (addressed using 32-bits) in indirect
mode, but the addressable space in memory-mapped mode is limited to 256 Mbytes.
In regular-command protocol, if DMM = 1, DEVSIZE[4:0] must reflect the total capacity of the
two devices together considering the above formula (DEVSIZE[4:0] value is so equal to one
of the two memory capacities).
Bits 15:11 Reserved, must  be kept at reset value.
Bits 10:8 CSHT[2:0]: Chip-select high time
CSHT + 1 defines the minimum number of CLK cycles where the chip-select (NCS) must
remain high between commands issued to the external device.
000: NCS stays high for at least 1 cycle between external device commands.
001: NCS stays high for at least 2 cycles between external device commands.
...
111: NCS stays high for at least 8 cycles between external device commands.
Bits 7:4 Reserved, must be kept at reset value.
Bit 3 DLYBYP: Delay block bypass
0: The internal sampling clock (called feedback clock) or the DQS data strobe external signal
is delayed by the delay block (for more details on this block, refer to the dedicated section of
the reference manual as it is not part of the OCTOSPI peripheral).
1: The delay block is bypassed, so the internal sampling clock or the DQS data strobe
external signal is not affected by the delay block. The delay is shorter than when the delay
block is not bypassed, even with the delay value set to minimum value in delay block.
Bit 2 Reserved, must be kept at reset value.

RM0438 Rev 8 661/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
20.7.3 OCTOSPI device configurat ion register 2 (OCTOSPI_DCR2)
Address offset: 0x000C
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
Bit 1 FRCK: Free running clock
This bit configures the free running clock.
0: CLK is not free running.
1: CLK is free running (always provided).
Note: Free running clock mode is intended for delay calibration only. No memory or other
device access is possible when FRCK is set. Once the bit has been set to 1, the BSY bit
is set, the NCS signal remains set to 1 and the clock is sent. The only way to stop the
clock is to perform an abort (which clears the BSY bit). Then, the FRCK bit must be
cleared by software to allow controller transactions to take place with the external
memory.
Bit 0 CKMODE: Clock mode 0/mode 3
This bit indicates the level taken by the CLK between commands (when NCS = 1).
0: CLK must stay low while NCS is high (chip-select released). This is referred to as
clock mode 0.
1: CLK must stay high while NCS is high (chip-select released). This is referred to as
clock mode 3.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. WRAPSIZE[2:0]
rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. PRESCALER[7:0]
rw rw rw rw rw rw rw rw
Bits 31:19 Reserved, must  be kept at reset value.
Bits 18:16 WRAPSIZE[2:0]: Wrap size
This bitfield indicates the wrap size to which the memory is configured. For memories which
have a separate command for wrapped instructions, this bitfield indicates the wrap-size
associated with the command held in the OCTOSPI1_WPIR register.
000: Wrapped reads are not supported by the memory.
010: External memory supports wrap size of 16 bytes.
011: External memory supports wrap size of 32 bytes.
100: External memory supports wrap size of 64 bytes.
101: External memory supports wrap size of 128 bytes.
Others: Reserved
Bits 15:8 Reserved, must be kept at reset value.

Octo-SPI interface (OCTOSPI) RM0438
662/2187 RM0438 Rev 8
20.7.4 OCTOSPI device configurat ion register 3 (OCTOSPI_DCR3)
Address offset: 0x0010
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
20.7.5 OCTOSPI device configurat ion register 4 (OCTOSPI_DCR4)
Address offset: 0x0014
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
Bits 7:0 PRESCALER[7:0]: Clock prescaler
This bitfield defines the scaler factor for generating the CLK based on the kernel clock
(value + 1).
0: FCLK = FKERNEL, kernel clock used directly as OCTOSPI CLK (prescaler bypassed). In this
case, if the DTR mode is used, it is mandatory to provide to the OCTOSPI a kernel clock that
has 50% duty-cycle.
1: FCLK = FKERNEL/2
2: FCLK = FKERNEL/3
...
255: FCLK = FKERNEL/256
For odd clock division factors, the CLK duty cycle is not 50 %. The clock signal remains low
one cycle longer than it stays high.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CSBOUND[4:0]
rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
Bits 31:21 Reserved, must  be kept at reset value.
Bits 20:16 CSBOUND[4:0]: NCS boundary
This bitfield enables the transaction boundary feature. When active, a minimum value of 3 is
recommended. The NCS is released on each boundary of 2CSBOUND bytes.
0: NCS boundary disabled
Others: NCS boundary set to 2CSBOUND bytes
Bits 15:0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REFRESH[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
REFRESH[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 663/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
20.7.6 OCTOSPI status register (OCTOSPI_SR)
Address offset: 0x0020
Reset value: 0x0000 0000
Bits 31:0 REFRESH[31:0]: Refresh rate
This bitfield enables the refresh rate feature. The NCS is released every REFRESH + 1 clock
cycles for writes, and REFRESH + 4 clock cycles for reads. These two values can be
extended with few clock cycles when refresh occurs during a byte transmission in single-,
dual- or quad-SPI mode, because the byte transmission must be completed.
0: Refresh disabled
Others: Maximum communication length is set to REFRESH + 1 clock cycles.
Note: REFRESH count is based on the divided clock period: if OCTOSPI_DCR2
PRESCALER bitfield is changed, the REFRESH field must be updated accordingly.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. FLEVEL[5:0] Res. Res. BUSY TOF SMF FTF TCF TEF
rrrrrr rrrrrr
Bits 31:14 Reserved, must  be kept at reset value.
Bits 13:8 FLEVEL[5:0]: FIFO level
This bitfield gives the number of valid bytes that are being held in the FIFO. FLEVEL = 0
when the FIFO is empty, and 32 when it is full.
In automatic status-polling mode, FLEVEL is zero.
Bits 7:6 Reserved, must be kept at reset value.
Bit 5 BUSY: Busy
This bit is set when an operation is ongoing. It is cleared automatically when the operation
with the external device is finished and the FIFO is empty.
Bit 4 TOF: Timeout flag
This bit is set when timeout occurs. It is cleared by writing 1 to CTOF.
Bit 3 SMF: Status match flag
This bit is set in automatic status-polling mode when the unmasked received data matches
the corresponding bits in the match register (OCTOSPI_PSMAR).
It is cleared by writing 1 to CSMF.
Bit 2 FTF: FIFO threshold flag
In indirect mode, this bit is set when the FIFO threshold has been reached, or if there is any
data left in the FIFO after the reads from the external device are complete.
It is cleared automatically as soon as the threshold condition is no longer true.
In automatic status-polling mode, this bit is set every time the status register is read, and the
bit is cleared when the data register is read.
Bit 1 TCF: Transfer complete flag
This bit is set in indirect mode when the programmed number of data has been transferred or
in any mode when the transfer has been aborted.It is cleared by writing 1 to CTCF.

Octo-SPI interface (OCTOSPI) RM0438
664/2187 RM0438 Rev 8
20.7.7 OCTOSPI flag clear  register (OCTOSPI_FCR)
Address offset: 0x0024
Reset value: 0x0000 0000
20.7.8 OCTOSPI data length register (OCTOSPI_DLR)
Address offset: 0x0040
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
Bit 0 TEF: Transfer error flag
This bit is set in indirect mode when an invalid address is being accessed in indirect mode.
It is cleared by writing 1 to CTEF.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. CTOF CSMF Res. CTCF CTEF
ww ww
Bits 31:5 Reserved, must be kept at reset value.
Bit 4 CTOF: Clear timeout flag
Writing 1 clears the TOF flag in the OCTOSPI_SR register.
Bit 3 CSMF: Clear status match flag
Writing 1 clears the SMF flag in the OCTOSPI_SR register.
Bit 2 Reserved, must be kept at reset value.
Bit 1 CTCF: Clear transfer complete flag
Writing 1 clears the TCF flag in the OCTOSPI_SR register.
Bit 0 CTEF: Clear transfer error flag
Writing 1 clears the TEF flag in the OCTOSPI_SR register.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
DL[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DL[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 665/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
20.7.9 OCTOSPI address re gister (OCTOSPI_AR)
Address offset: 0x0048
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0 and FMODE ≠ 11.
20.7.10 OCTOSPI data register (OCTOSPI_DR)
Address offset: 0x0050
Reset value: 0x0000 0000
Bits 31:0 DL[31:0]: Data length
Number of data to be retrieved (value+1) in indirect and automatic status-polling modes. A
value not greater than three (indicating 4 bytes) must be used for automatic status-polling
mode.
All 1’s in indirect mode means undefined length, where OCTOSPI continues until the end of
the memory, as defined by DEVSIZE.
0x0000_0000: 1 byte is to be transferred.
0x0000_0001: 2 bytes are to be transferred.
0x0000_0002: 3 bytes are to be transferred.
0x0000_0003: 4 bytes are to be transferred.
...
0xFFFF_FFFD: 4,294,967,294 (4G-2) bytes are to be transferred.
0xFFFF_FFFE: 4,294,967,295 (4G-1) bytes are to be transferred.
0xFFFF_FFFF: undefined length; all bytes, until the end of the external device, (as defined
by DEVSIZE) are to be transferred. Continue reading indefinitely if DEVSIZE = 0x1F.
DL[0] is stuck at 1 in dual-memory configuration (DMM = 1) even when 0 is written to this bit,
thus assuring that each access transfers an even number of bytes.
This bitfield has no effect in memory-mapped mode.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ADDRESS[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ADDRESS[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 ADDRESS[31:0]: Address
Address to be sent to the external device. In HyperBus protocol, this field must be even as
this protocol is 16-bit word oriented. In dual-memory configuration, AR[0] is forced to 0.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
DATA[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DATA[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

Octo-SPI interface (OCTOSPI) RM0438
666/2187 RM0438 Rev 8
20.7.11 OCTOSPI polling status mask register (OCTOSPI_PSMKR)
Address offset: 0x0080
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
Bits 31:0 DATA[31:0]: Data
Data to be sent/received to/from the external SPI device
In indirect-write mode, data written to this register is stored on the FIFO before it is sent to the
external device during the data phase. If the FIFO is too full, a write operation is stalled until
the FIFO has enough space to accept the amount of data being written.
In indirect-read mode, reading this register gives (via the FIFO) the data that was received
from the external device. If the FIFO does not have as many bytes as requested by the read
operation and if BUSY = 1, the read operation is stalled until enough data is present or until
the transfer is complete, whichever happens first.
In automatic status-polling mode, this register contains the last data read from the external
device (without masking).
Word, half-word, and byte accesses to this register are supported. In indirect-write mode,
a byte write adds 1 byte to the FIFO, a half-word write 2 bytes, and a word write 4 bytes.
Similarly, in indirect-read mode, a byte read removes 1 byte from the FIFO, a halfword read
2 bytes, and a word read 4 bytes. Accesses in indirect mode must be aligned to the bottom of
this register: A byte read must read DATA[7:0] and a half-word read must read DATA[15:0].
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
MASK[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
MASK[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 MASK[31:0]: Status mask
Mask to be applied to the status bytes received in automatic status-polling mode
For bit n:
0: Bit n of the data received in automatic status-polling mode is masked and its value is not
considered in the matching logic.
1: Bit n of the data received in automatic status-polling mode is unmasked and its value is
considered in the matching logic.

RM0438 Rev 8 667/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
20.7.12 OCTOSPI polling status match register (OCTOSPI_PSMAR)
Address offset: 0x0088
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
20.7.13 OCTOSPI polling interv al register (OCTOSPI_PIR)
Address offset: 0x0090
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
20.7.14 OCTOSPI communication confi guration register (OCTOSPI_CCR)
Address offset: 0x0100
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
MATCH[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
MATCH[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 MATCH[31:0]: Status match
Value to be compared with the masked status register to get a match
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
INTERVAL[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 INTERVAL[15:0]: Polling interval
Number of CLK cycles between a read during the automatic status-polling phases
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
SIOO Res. DQSE Res. DDTR DMODE[2:0] Res. Res. ABSIZE[1:0] ABDTR ABMODE[2:0]
rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. ADSIZE[1:0] AD
DTR ADMODE[2:0] Res. Res. ISIZE[1:0] IDTR IMODE[2:0]
rw rw rw rw rw rw rw rw rw rw rw rw

Octo-SPI interface (OCTOSPI) RM0438
668/2187 RM0438 Rev 8
Bit 31 SIOO: Send instruction only once mode
This bit has no effect when IMODE = 00 (see Sending the instruction only once (SIOO)).
0: Send instruction on every transaction
1: Send instruction only for the first command
Bit 30 Reserved, must be kept at reset value.
Bit 29 DQSE: DQS enable
This bit enables the data strobe management.
0: DQS disabled
1: DQS enabled
Bit 28 Reserved, must be kept at reset value.
Bit 27 DDTR: Data double transfer rate
This bit sets the DTR mode for the data phase.
0: DTR mode disabled for data phase
1: DTR mode enabled for data phase
Bits 26:24 DMODE[2:0]: Data mode
This bitfield defines the data phase mode of operation.
000: No data
001: Data on a single line
010: Data on two lines
011: Data on four lines
100: Data on eight lines
Others: Reserved
Bits 23:22 Reserved, must  be kept at reset value.
Bits 21:20 ABSIZE[1:0]: Alternate-byte size
This bitfield defines the alternate-byte size.
00: 8-bit alternate bytes
01: 16-bit alternate bytes
10: 24-bit alternate bytes
11: 32-bit alternate bytes
Bit 19 ABDTR: Alternate- byte double transfer rate
This bit sets the DTR mode for the alternate-byte phase.
0: DTR mode disabled for the alternate-byte phase
1: DTR mode enabled for the alternate-byte phase
Bits 18:16 ABMODE[2:0]: Alternate-byte mode
This bitfield defines the alternate-byte phase mode of operation.
000: No alternate bytes
001: Alternate bytes on a single line
010: Alternate bytes on two lines
011: Alternate bytes on four lines
100: Alternate bytes on eight lines
Others: Reserved
Bits 15:14 Reserved, must  be kept at reset value.

RM0438 Rev 8 669/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
Bits 13:12 ADSIZE[1:0]: Address size
This bitfield defines the address size.
00: 8-bit address
01: 16-bit address
10: 24-bit address
11: 32-bit address
Bit 11 ADDTR: Address double transfer rate
This bit sets the DTR mode for the address phase.
0: DTR mode disabled for the address phase
1: DTR mode enabled for the address phase
Bits 10:8 ADMODE[2:0]: Address mode
This bitfield defines the address phase mode of operation.
000: No address
001: Address on a single line
010: Address on two lines
011: Address on four lines
100: Address on eight lines
Others: Reserved
Bits 7:6 Reserved, must be kept at reset value.
Bits 5:4 ISIZE[1:0]: Instruction size
This bitfield defines instruction size.
00: 8-bit instruction
01: 16-bit instruction
10: 24-bit instruction
11: 32-bit instruction
Bit 3 IDTR: Instruction double transfer rate
This bit sets the DTR mode for the instruction phase.
0: DTR mode disabled for the instruction phase
1: DTR mode enabled for the instruction phase
Bits 2:0 IMODE[2:0]: Instruction mode
This bitfield defines the instruction phase mode of operation.
000: No instruction
001: Instruction on a single line
010: Instruction on two lines
011: Instruction on four lines
100: Instruction on eight lines
Others: Reserved

Octo-SPI interface (OCTOSPI) RM0438
670/2187 RM0438 Rev 8
20.7.15 OCTOSPI timing configur ation register (OCTOSPI_TCR)
Address offset: 0x0108
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
20.7.16 OCTOSPI instructi on register (OCTOSPI_IR)
Address offset: 0x0110
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. SSHIF
T Res. DHQC Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. DCYC[4:0]
rw rw rw rw rw
Bit 31 Reserved, must be kept at reset value.
Bit 30 SSHIFT: Sample shift
By default, the OCTOSPI samples data 1/2 of a CLK cycle after the data is driven by the
external device.
This bit allows the data to be sampled later in order to consider the external signal delays.
0: No shift
1: 1/2 cycle shift
The software must ensure that SSHIFT = 0 when the data phase is configured in DTR mode
(when DDTR = 1.)
Bit 29 Reserved, must be kept at reset value.
Bit 28 DHQC: Delay hold quarter cycle
0: No delay hold
1: 1/4 cycle hold
Bits 27:5 Reserved, must be kept at reset value.
Bits 4:0 DCYC[4:0]: Number of dummy cycles
This bitfield defines the duration of the dummy phase according to the memory latency.
In both SDR and DTR modes, it specifies a number of CLK cycles (0-31).
It is recommended to have at least six dummy cycles when using memories with DQS
activated.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
INSTRUCTION[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
INSTRUCTION[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 671/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
20.7.17 OCTOSPI alternate by tes register (OCTOSPI_ABR)
Address offset: 0x0120
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
20.7.18 OCTOSPI low-power time out register (OCTOSPI_LPTR)
Address offset: 0x00130
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
Bits 31:0 INSTRUCTION[31:0]: Instruction
Instruction to be sent to the external SPI device
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ALTERNATE[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ALTERNATE[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 ALTERNATE[31:0]: Alternate bytes
Optional data to be sent to the external SPI device right after the address.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
TIMEOUT[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 TIMEOUT[15:0]: Timeout period
After each access in memory-mapped mode, the OCTOSPI prefetches the subsequent bytes
and hold them in the FIFO.
This bitfield indicates how many CLK cycles the OCTOSPI waits after the clock becomes
inactive and until it raises the NCS, putting the external device in a lower-consumption state.

Octo-SPI interface (OCTOSPI) RM0438
672/2187 RM0438 Rev 8
20.7.19 OCTOSPI wrap communi cation configuration register
(OCTOSPI_WPCCR)
Address offset: 0x0140
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. DQSE Res. DDTR DMODE[2:0] Res. Res. ABSIZE[1:0] ABDTR ABMODE[2:0]
rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. ADSIZE[1:0] AD
DTR ADMODE[2:0] Res. Res. ISIZE[1:0] IDTR IMODE[2:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:30 Reserved, must  be kept at reset value.
Bit 29 DQSE: DQS enable
This bit enables the data strobe management.
0: DQS disabled
1: DQS enabled
Bit 28 Reserved, must be kept at reset value.
Bit 27 DDTR: Data double transfer rate
This bit sets the DTR mode for the data phase.
0: DTR mode disabled for the data phase
1: DTR mode enabled for the data phase
Bits 26:24 DMODE[2:0]: Data mode
This bitfield defines the data phase mode of operation.
000: No data
001: Data on a single line
010: Data on two lines
011: Data on four lines
100: Data on eight lines
Others: Reserved
Bits 23:22 Reserved, must  be kept at reset value.
Bits 21:20 ABSIZE[1:0]: Alternate-byte size
This bitfield defines the alternate-byte size.
00: 8-bit alternate bytes
01: 16-bit alternate bytes
10: 24-bit alternate bytes
11: 32-bit alternate bytes
Bit 19 ABDTR: Alternate-byte double transfer rate
This bit sets the DTR mode for the alternate-byte phase.
0: DTR mode disabled for the alternate-byte phase
1: DTR mode enabled for the alternate-byte phase

RM0438 Rev 8 673/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
Bits 18:16 ABMODE[2:0]: Alternate-byte mode
This bitfield defines the alternate-byte phase mode of operation.
000: no alternate bytes
001: alternate bytes on a single line
010: alternate bytes on two lines
011: alternate bytes on four lines
100: alternate bytes on eight lines
Others: reserved
Bits 15:14 Reserved, must  be kept at reset value.
Bits 13:12 ADSIZE[1:0]: Address size
This bitfield defines the address size.
00: 8-bit address
01: 16-bit address
10: 24-bit address
11: 32-bit address
Bit 11 ADDTR: Address double transfer rate
This bit sets the DTR mode for the address phase.
0: DTR mode disabled for address phase
1: DTR mode enabled for address phase
Bits 10:8 ADMODE[2:0]: Address mode
This bitfield defines the address phase mode of operation.
000: No address
001: Address on a single line
010: Address on two lines
011: Address on four lines
100: Address on eight lines
Others: Reserved
Bits 7:6 Reserved, must be kept at reset value.
Bits 5:4 ISIZE[1:0]: Instruction size
This bitfield defines the instruction size.
00: 8-bit instruction
01: 16-bit instruction
10: 24-bit instruction
11: 32-bit instruction
Bit 3 IDTR: Instruction double transfer rate
This bit sets the DTR mode for the instruction phase.
0: DTR mode disabled for the instruction phase
1: DTR mode enabled for the instruction phase
Bits 2:0 IMODE[2:0]: Instruction mode
This bitfield defines the instruction phase mode of operation.
000: No instruction
001: Instruction on a single line
010: Instruction on two lines
011: Instruction on four lines
100: Instruction on eight lines
Others: Reserved

Octo-SPI interface (OCTOSPI) RM0438
674/2187 RM0438 Rev 8
20.7.20 OCTOSPI wrap ti ming configuration register (OCTOSPI_WPTCR)
Address offset: 0x0148
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
20.7.21 OCTOSPI wrap instruct ion register (OCTOSPI_WPIR)
Address offset: 0x0150
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. S
SHIFT Res. DHQC Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. DCYC[4:0]
rw rw rw rw rw
Bit 31 Reserved, must be kept at reset value.
Bit 30 SSHIFT: Sample shift
By default, the OCTOSPI samples data 1/2 of a CLK cycle after the data is driven by the
external device.
This bit allows the data to be sampled later in order to consider the external signal delays.
0: No shift
1: 1/2 cycle shift
The firmware must assure that SSHIFT=0 when the data phase is configured in DTR mode
(when DDTR = 1).
Bit 29 Reserved, must be kept at reset value.
Bit 28 DHQC: Delay hold quarter cycle
Add a quarter cycle delay on the outputs in DTR communication to match hold requirement.
0: No quarter cycle delay
1: 1/4 cycle delay inserted
Bits 27:5 Reserved, must be kept at reset value.
Bits 4:0 DCYC[4:0]: Number of dummy cycles
This bitfield defines the duration of the dummy phase according to the memory latency.
In both SDR and DTR modes, it specifies a number of CLK cycles (0-31). It is recommended
to have at least 5 dummy cycles when using memories with DQS activated.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
INSTRUCTION[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
INSTRUCTION[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 675/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
20.7.22 OCTOSPI wrap alternate bytes register (OCTOSPI_WPABR)
Address offset: 0x0160
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
20.7.23 OCTOSPI write communi cation configuration register
(OCTOSPI_WCCR)
Address offset: 0x0180
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0. Its content has a meaning only when
requesting write operations in memory-mapped mode.
Bits 31:0 INSTRUCTION[31:0]: Instruction
Instruction to be sent to the external SPI device
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ALTERNATE[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ALTERNATE[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 ALTERNATE[31:0]: Alternate bytes
Optional data to be sent to the external SPI device right after the address
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. DQSE Res. DDTR DMODE[2:0] Res. Res. ABSIZE[1:0] ABDTR ABMODE[2:0]
rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. ADSIZE[1:0] ADDTR ADMODE[2:0] Res. Res. ISIZE[1:0] IDTR IMODE[2:0]
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:30 Reserved, must  be kept at reset value.
Bit 29 DQSE: DQS enable
This bit enables the data strobe management.
0: DQS disabled
1: DQS enabled
Bit 28 Reserved, must be kept at reset value.
Bit 27 DDTR: data double transfer rate
This bit sets the DTR mode for the data phase.
0: DTR mode disabled for the data phase
1: DTR mode enabled for the data phase

Octo-SPI interface (OCTOSPI) RM0438
676/2187 RM0438 Rev 8
Bits 26:24 DMODE[2:0]: Data mode
This bitfield defines the data phase mode of operation.
000: No data
001: Data on a single line
010: Data on two lines
011: Data on four lines
100: Data on eight lines
Others: Reserved
Bits 23:22 Reserved, must  be kept at reset value.
Bits 21:20 ABSIZE[1:0]: Alternate-byte size
This bitfield defines the alternate-byte size.
00: 8-bit alternate bytes
01: 16-bit alternate bytes
10: 24-bit alternate bytes
11: 32-bit alternate bytes
Bit 19 ABDTR: Alternate bytes double transfer rate
This bit sets the DTR mode for the alternate-bytes phase.
0: DTR mode disabled for alternate-bytes phase
1: DTR mode enabled for alternate-bytes phase
Bits 18:16 ABMODE[2:0]: Alternate-byte mode
This bitfield defines the alternate-byte phase mode of operation.
000: No alternate bytes
001: Alternate bytes on a single line
010: Alternate bytes on two lines
011: Alternate bytes on four lines
100: Alternate bytes on eight lines
Others: Reserved
Bits 15:14 Reserved, must  be kept at reset value.
Bits 13:12 ADSIZE[1:0]: Address size
This bitfield defines the address size.
00: 8-bit address
01: 16-bit address
10: 24-bit address
11: 32-bit address
Bit 11 ADDTR: Address double transfer rate
This bit sets the DTR mode for the address phase.
0: DTR mode disabled for the address phase
1: DTR mode enabled for the address phase
Bits 10:8 ADMODE[2:0]: Address mode
This bitfield defines the address phase mode of operation.
000: No address
001: Address on a single line
010: Address on two lines
011: Address on four lines
100: Address on eight lines
Others: Reserved
Bits 7:6 Reserved, must be kept at reset value.

RM0438 Rev 8 677/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
20.7.24 OCTOSPI write timing configuration register (OCTOSPI_WTCR)
Address offset: 0x0188
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0. Its content has a meaning only when
requesting write operations in memory-mapped mode.
Bits 5:4 ISIZE[1:0]: Instruction size
This bitfield defines the instruction size.
00: 8-bit instruction
01: 16-bit instruction
10: 24-bit instruction
11: 32-bit instruction
Bit 3 IDTR: Instruction double transfer rate
This bit sets the DTR mode for the instruction phase.
0: DTR mode disabled for instruction phase
1: DTR mode enabled for instruction phase
Bits 2:0 IMODE[2:0]: Instruction mode
This bitfield defines the instruction phase mode of operation.
000: No instruction
001: Instruction on a single line
010: Instruction on two lines
011: Instruction on four lines
100: Instruction on eight lines
Others: Reserved
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. DCYC[4:0]
rw rw rw rw rw
Bits 31:5 Reserved, must be kept at reset value.
Bits 4:0 DCYC[4:0]: Number of dummy cycles
This bitfield defines the duration of the dummy phase according to the memory latency.
In both SDR and DTR modes, it specifies a number of CLK cycles (0-31). It is recommended
to have at least 5 dummy cycles when using memories with DQS activated.

Octo-SPI interface (OCTOSPI) RM0438
678/2187 RM0438 Rev 8
20.7.25 OCTOSPI write instruct ion register (OCTOSPI_WIR)
Address offset: 0x0190
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0. Its content has a meaning only when
requesting write operations in memory-mapped mode.
20.7.26 OCTOSPI write alternate bytes register (OCTOSPI_WABR)
Address offset: 0x01A0
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0. Its content has a meaning only when
requesting write operations in memory-mapped mode.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
INSTRUCTION[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
INSTRUCTION[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 INSTRUCTION[31:0]: Instruction
Instruction to be sent to the external SPI device
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
ALTERNATE[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
ALTERNATE[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 ALTERNATE[31:0]: Alternate bytes
Optional data to be sent to the external SPI device right after the address

RM0438 Rev 8 679/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
20.7.27 OCTOSPI HyperBus late ncy configuration register
(OCTOSPI_HLCR)
Address offset: 0x0200
Reset value: 0x0000 0000
This register can be modified only when BUSY = 0.
20.7.28 OCTOSPI register map
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. TRWR[7:0]
rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
TACC[7:0] Res. Res. Res. Res. Res. Res. WZL LM
rw rw rw rw rw rw rw rw rw rw
Bits 31:24 Reserved, must  be kept at reset value.
Bits 23:16 TRWR[7:0]: Read-write minimum recovery time
Device read-to-write/write-to-read minimum recovery time expressed in number of
communication clock cycles
Bits 15:8 TACC[7:0]: Access time
Device access time according to the memory latency, expressed in number of
communication clock cycles
Bits 7:2 Reserved, must be kept at reset value.
Bit 1 WZL: Write zero latency
This bit enables zero latency on write operations.
0: Latency on write accesses
1: No latency on write accesses
Bit 0 LM: Latency mode
This bit selects the latency mode.
0: Variable initial latency
1: Fixed latency
[Table 163](../tables/table_163.md). OCTOSPI register map and reset values
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
0x0000
OCTOSPI_CR
Res.
Res.
FMDOE[1:0]
Res.
Res.
Res.
Res.
PMM
APMS
Res..
TOIE
SMIE
FTIE
TCIE
TEIE
Res.
Res.
Res.FTHRES[4:0]
FSEL
DMM
Res.
Res.
TCEN
DMAEN
ABORT
EN
R e s e t  v a l u e 00 00 00000 0000000 0000
0x0004 Reserved Reserved
0x0008
OCTOSPI_DCR1
Res.
Res.
Res.
Res.
Res.
MTYP
[2:0]
Res.
Res.
Res.DEVSIZE[4:0]
Res.
Res.
Res.
Res.
Res.
CSHT
[2:0]
Res.
Res.
Res.
Res.
DLYBYP
Res.
FRCK
CKMODE
R e s e t  v a l u e 000 00000 000 0 00

Octo-SPI interface (OCTOSPI) RM0438
680/2187 RM0438 Rev 8
0x000C
OCTOSPI_DCR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
WRAPSIZE
[2:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. PRESCALER[7:0]
R e s e t  v a l u e 000 00000000
0x0010
OCTOSPI_DCR3
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.CSBOUND[4:0]
Res.
Res.
Res.
Res.
Res.
Res.
Res.
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
0x0014
OCTOSPI_DCR4 REFRESH[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x0018-
0x001C Reserved Reserved
0x0020
OCTOSPI_SR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. FLEVEL[5:0]
Res.
Res..
BUSY
TOF
SMF
FTF
TCF
TEF
Reset value 000000 000000
0x0024
OCTOSPI_FCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res..
Res.
CTOF
CSMF
Res.
CTCF
CTEF
Reset value 00 00
0x0028-
0x003C Reserved Reserved
0x0040
OCTOSPI_DLR DL[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x0044 Reserved Reserved
0x0048
OCTOSPI_AR ADDRESS[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x004C Reserved Reserved
0x0050
OCTOSPI_DR DATA[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x0054-
0x007C Reserved Reserved
0x0080
OCTOSPI_
PSMKR MASK[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x0084 Reserved Reserved
0x0088
OCTOSPI_
PSMAR MATCH[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x008C Reserved Reserved
0x0090
OCTOSPI_PIR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. INTERVAL[15:0]
R e s e t  v a l u e 0000000000000000
0x0094-
0x00FC Reserved Reserved
[Table 163](../tables/table_163.md). OCTOSPI register map and reset values (continued)
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

RM0438 Rev 8 681/2187
RM0438 Octo-SPI interface (OCTOSPI)
682
0x0100
OCTOSPI_CCR
SIOO
Res.
DQSE
Res.
DDTR
DMODE
[2:0]
Res.
Res.
ABSIZE
[1:0]
ABDTR
ABMODE
[2:0]
Res.
Res.
ADSIZE
[1:0]
ADDTR
ADMODE
[2:0]
Res.
Res.
ISIZE[1:0]
IDTR
IMODE
[2:0]
R e s e t  v a l u e 0 0 0000 000000 000000 000000
0x0104 Reserved Reserved
0x0108
OCTOSPI_TCR
Res.
SSHIFT
Res.
DHQC
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.DCYC[4:0]
Reset value 0 0 00000
0x010C Reserved Reserved
0x0110
OCTOSPI_IR INSTRUCTION[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x0114-
0x011C Reserved Reserved
0x0120
OCTOSPI_ABR ALTERNATE[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x0124-
0x012C Reserved Reserved
0x0130
OCTOSPI_LPTR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. TIMEOUT[15:0]
R e s e t  v a l u e 0000000000000000
0x0134-
0x013C Reserved Reserved
0x0140
OCTOSPI_
WPCCR
Res.
Res.
DQSE
Res.
DDTR
DMODE
[2:0]
Res.
Res.
ABSIZE
[1:0]
ABDTR
ABMODE
[2:0]
Res.
Res.
ADSIZE
[1:0]
ADDTR
ADMODE
[2:0]
Res.
Res.
ISIZE
[1:0]
IDTR
IMODE
[2:0]
R e s e t  v a l u e 0 0 0000 000000 000000 000000
0x0144 Reserved Reserved
0x0148
OCTOSPI_
WPTCR
Res.
SSHIFT
Res.
DHQC.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.DCYC[4:0]
Reset value 0 0 00000
0x014C Reserved Reserved
0x0150
OCTOSPI_WPIR INSTRUCTION[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x0154-
0x015C Reserved Reserved
0x0160
OCTOSPI_
WPABR ALTERNATE[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x0164-
0x017C Reserved Reserved
0x0180
OCTOSPI_WCCR
Res.
Res.
DQSE
Res.
DDTR
DMODE
[2:0]
Res.
Res.
ABSIZE
[1:0]
ABDTR
ABMODE
[2:0]
Res.
Res.
ADSIZE
[1:0]
ADDTR
ADMODE
[2:0]
Res.
Res.
ISIZE
[1:0]
IDTR
IMODE
[2:0]
R e s e t  v a l u e 0 0 0000 000000 000000 000000
[Table 163](../tables/table_163.md). OCTOSPI register map and reset values (continued)
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

Octo-SPI interface (OCTOSPI) RM0438
682/2187 RM0438 Rev 8
Refer to Section 2.3: Memory organization for the register boundary addresses.
0x0184 Reserved Reserved
0x0188
OCTOSPI_WTCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.DCYC[4:0]
Reset value 00000
0x018C Reserved Reserved
0x0190
OCTOSPI_WIR INSTRUCTION[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x0194-
0x019C Reserved Reserved
0x01A0
OCTOSPI_WABR ALTERNATE[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x01A4-
0x01FC Reserved Reserved
0x0200
OCTOSPI_HLCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. TRWR[7:0] TACC[7:0]
Res.
Res.
Res.
Res.
Res.
Res.
WZL
LM
R e s e t  v a l u e 0000000000000000 00
[Table 163](../tables/table_163.md). OCTOSPI register map and reset values (continued)
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
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 74: Architectural Diagram](../figures/figure_74.md)
* [Figure 75: Architectural Diagram](../figures/figure_75.md)
* [Figure 76: Architectural Diagram](../figures/figure_76.md)
* [Figure 77: Architectural Diagram](../figures/figure_77.md)
* [Figure 78: Architectural Diagram](../figures/figure_78.md)
* [Figure 79: Architectural Diagram](../figures/figure_79.md)
* [Figure 80: Architectural Diagram](../figures/figure_80.md)
* [Figure 81: Architectural Diagram](../figures/figure_81.md)
* [Figure 82: Architectural Diagram](../figures/figure_82.md)
* [Figure 83: Architectural Diagram](../figures/figure_83.md)
* [Figure 84: Architectural Diagram](../figures/figure_84.md)
* [Figure 85: Architectural Diagram](../figures/figure_85.md)
* [Figure 86: Architectural Diagram](../figures/figure_86.md)
* [Figure 87: Architectural Diagram](../figures/figure_87.md)
* [Figure 88: Architectural Diagram](../figures/figure_88.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 156: Configuration Matrix](../tables/table_156.md)
* [Table 157: Configuration Matrix](../tables/table_157.md)
* [Table 158: Configuration Matrix](../tables/table_158.md)
* [Table 159: Configuration Matrix](../tables/table_159.md)
* [Table 160: Configuration Matrix](../tables/table_160.md)
* [Table 161: Configuration Matrix](../tables/table_161.md)
* [Table 162: Configuration Matrix](../tables/table_162.md)
* [Table 163: Configuration Matrix](../tables/table_163.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)