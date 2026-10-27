# Chapter 27: Serial peripheral interface / integrated interchip sound (SPI/I2S)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32C0 Reference Manual RM0490 - Chapter 27: Serial peripheral interface / integrated interchip sound (SPI/I2S).
* **Document Source**: RM0490 Reference Manual
* **PDF Reference Location**: Pages 830 - 887
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Serial Peripheral Interface (SPI)](../peripherals/spi.md)

## 2. Official Reference Manual Text Content (RM0490 Ingestion)
```text
Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
830/1023 RM0490 Rev 6
27 Serial peripheral interface / integrated interchip
sound (SPI/I2S)
27.1 Introduction
The SPI/I²S interface can be used to communicate with external devices using the SPI
protocol or the I2S audio protocol. SPI or I2S mode is selectable by software. SPI Motorola
mode is selected by default after a device reset.
The serial peripheral interface (SPI) protocol supports half-duplex, full-duplex and simplex
synchronous, serial communication with external devices. The interface can be configured
as master and in this case it provides the communication clock (SCK) to the external slave
device. The interface is also capable of operating in multimaster configuration.
The integrated interchip sound (I2S) protocol is also a synchronous serial communication
interface. It can operate in slave or master mode with half-duplex communication. It can
address four different audio standards including the Philips I2S standard, the MSB- and
LSB-justified standards and the PCM standard.
27.2 SPI main features
• Master or slave operation
• Full-duplex synchronous transfers on three lines
• Half-duplex synchronous transfer on two lines (with bidirectional data line)
• Simplex synchronous transfers on two lines (with unidirectional data line)
• 4 to 16-bit data size selection
• Multimaster mode capability
• 8 master mode baud rate prescalers up to fPCLK/2
• Slave mode frequency up to fPCLK/2
• NSS management by hardware or software for both master and slave: dynamic change
of master/slave operations
• Programmable clock polarity and phase
• Programmable data order with MSB-first or LSB-first shifting
• Dedicated transmission and reception flags with interrupt capability
• SPI bus busy status flag
• SPI Motorola support
• Hardware CRC feature for reliable communication:
– CRC value can be transmitted as last byte in Tx mode
– Automatic CRC error checking for last received byte
• Master mode fault, overrun flags with interrupt capability
• CRC Error flag
• Two 32-bit embedded Rx and Tx FIFOs with DMA capability
• Enhanced TI and NSS pulse modes support

RM0490 Rev 6 831/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
27.3 I2S main features
• Half-duplex communication (only transmitter or receiver)
• Master or slave operations
• 8-bit programmable linear prescaler to reach accurate audio sample frequencies (from
8 kHz to 192 kHz)
• Data format may be 16-bit, 24-bit, or 32-bit
• Packet frame is fixed to 16-bit (16-bit data frame) or 32-bit (16-bit, 24-bit, 32-bit data
frame) by audio channel
• Programmable clock polarity (steady state)
• Underrun flag in slave transmission mode, overrun flag in reception mode (master and
slave) and Frame Error Flag in reception and transmitter mode (slave only)
• 16-bit register for transmission and reception with one data register for both channel
sides
• Supported I2S protocols:
–I 2S Philips standard
– MSB-justified standa rd (left-justified)
– LSB-justified standard (right-justified)
– PCM standard (with short and long frame synchronization on 16-bit channel frame
or 16-bit data frame extended to 32-bit channel frame)
• Data direction is always MSB first
• DMA capability for transmission and reception (16-bit wide)
• Master clock can be output to drive an external audio component. The ratio is fixed at
256 × fs for all I2S modes, and to 128 x fs for all PCM modes (where fs is the audio
sampling frequency).
27.4 SPI/I2S implementation
The following table describes all the SPI instances and their features embedded in the
devices.
[Table 135](../tables/table_135.md). STM32C0 series SPI/I2S implementation
SPI Features SPI1 SPI2 (1)
1. Applies to STM32C051/71/91/92xx devices only.
Enhanced NSSP & TI modes Yes
Hardware CRC calculation Yes
I2S support Yes No
Data size configuration from 4 to 16 bits
Rx/Tx FIFO size 32 bits

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
832/1023 RM0490 Rev 6
27.5 SPI functional description
27.5.1 General description
The SPI allows synchronous, serial communication between the MCU and external devices.
Application software can manage the communication by polling the status flag or using
dedicated SPI interrupt. The main elements of SPI and their interactions are shown in the
following block diagram [Figure 279](../figures/figure_279.md).
[Figure 279](../figures/figure_279.md). SPI block diagram
Four I/O pins are dedicated to SPI communication with external devices.
• MISO: Master In / Slave Out data. In the general case, this pin is used to transmit data
in slave mode and receive data in master mode.
• MOSI: Master Out / Slave In data. In the general case, this pin is used to transmit data
in master mode and receive data in slave mode.
• SCK: Serial Clock output pin for SPI masters and input pin for SPI slaves.
• NSS: Slave select pin. Depending on the SPI and NSS settings, this pin can be used to
either:
– select an individual slave device for communication
– synchronize the data frame or
– detect a conflict between multiple masters
See Section 27.5.5: Slave select (NSS) pin management for details.
The SPI bus allows the communication between one master device and one or more slave
devices. The bus consists of at least two wires - one for the clock signal and the other for
synchronous data transfer. Other signals can be added depending on the data exchange
between SPI nodes and their slave select signal management.
Shift register
Write
Read
Address and data bus
CRC controller
Internal NSS
CRCEN
CRCNEXT
CRCL
RXONLY
CPOL
CPHA
MOSI
MISO
SCK
NSS
Rx
FIFO
Tx
FIFO
BR[2:0]
MS30117V1
DS[0:3]
BIDIOE
Communication
controller
NSS
logic
Baud rate
generator

RM0490 Rev 6 833/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
27.5.2 Communications betwee n one master and one slave
The SPI allows the MCU to communicate using different configurations, depending on the
device targeted and the application requirements. These configurations use 2 or 3 wires
(with software NSS management) or 3 or 4 wires (with hardware NSS management).
Communication is always initiated by the master.
Full-duplex communication
By default, the SPI is configured for full-duplex communication. In this configuration, the
shift registers of the master and slave are linked using two unidirectional lines between the
MOSI and the MISO pins. During SPI communication, data is shifted synchronously on the
SCK clock edges provided by the master. The master transmits the data to be sent to the
slave via the MOSI line and receives data from the slave via the MISO line. When the data
frame transfer is complete (all the bits are shifted) the information between the master and
slave is exchanged.
[Figure 280](../figures/figure_280.md). Full-duplex single master/ single slave application
1. The NSS pins can be used to provide a hardware c ontrol flow between master and slave. Optionally, the
pins can be left unused by the peripheral. Then the flow has to be handled internally for both master and
slave. For more details see Section 27.5.5: Slave select (NSS) pin management.
Half-duplex communication
The SPI can communicate in half-duplex mode by setting the BIDIMODE bit in the
SPIx_CR1 register. In this configuration, one single cross connection line is used to link the
shift registers of the master and slave together. During this communication, the data is
synchronously shifted between the shift registers on the SCK clock edge in the transfer
direction selected reciprocally by both master and slave with the BDIOE bit in their
SPIx_CR1 registers. In this configuration, the master’s MISO pin and the slave’s MOSI pin
are free for other application uses and act as GPIOs.
Rx shift register
Tx shift register Rx shift register
Tx shift register
SPI clock
generator
Master Slave
MISO
MOSI
SCK
NSS
MISO
MOSI
SCK
NSS(1) (1)
MSv39623V1

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
834/1023 RM0490 Rev 6
[Figure 281](../figures/figure_281.md). Half-duplex single master/ single slave application
1. The NSS pins can be used to provide a hardware c ontrol flow between master and slave. Optionally, the
pins can be left unused by the peripheral. Then the flow has to be handled internally for both master and
slave. For more details see Section 27.5.5: Slave select (NSS) pin management.
2. In this configuration, the master’s MISO pin and the slave’s MOSI pin can be used as GPIOs.
3. A critical situation can happen when communication direction is changed not synchronously between two
nodes working at bidirectionnal mode and new transmitter accesses the common data line while former
transmitter still keeps an opposite value on the line (the value depends on SPI configuration and
communication data). Both nodes then fight while providing opposite output levels on the common line
temporary till next node changes its direction settings correspondingly, too. It is suggested to insert a serial
resistance between MISO and MOSI pins at this mode to protect the outputs and limit the current blowing
between them at this situation.
Simplex communications
The SPI can communicate in simplex mode by setting the SPI in transmit-only or in receive-
only using the RXONLY bit in the SPIx_CR1 register. In this configuration, only one line is
used for the transfer between the shift registers of the master and slave. The remaining
MISO and MOSI pins pair is not used for communication and can be used as standard
GPIOs.
• Transmit-only mode (RXONLY=0): The configuration settings are the same as for full-
duplex. The application has to ignore the information captured on the unused input pin.
This pin can be used as a standard GPIO.
• Receive-only mode (RXONLY=1): The application can disable the SPI output function
by setting the RXONLY bit. In slave configuration, the MISO output is disabled and the
pin can be used as a GPIO. The slave continues to receive data from the MOSI pin
while its slave select signal is active (see 27.5.5: Slave select (NSS) pin management).
Received data events appear depending on the data buffer configuration. In the master
configuration, the MOSI output is disabled and the pin can be used as a GPIO. The
clock signal is generated continuously as long as the SPI is enabled. The only way to
stop the clock is to clear the RXONLY bit or the SPE bit and wait until the incoming
pattern from the MISO pin is finished and fills the data buffer structure, depending on its
configuration.
Rx shift register
Tx shift register Rx shift register
Tx shift register
SPI clock
generator
Master Slave
MISO
MOSI
SCK
NSS
MISO
MOSI
SCK
NSS(1) (1)
(2)
(2)
Nȍ(3)
MSv39624V1

RM0490 Rev 6 835/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
[Figure 282](../figures/figure_282.md). Simplex single master/single slave application (master in transmit-only/
slave in receive-only mode)
1. The NSS pins can be used to provide a hardware c ontrol flow between master and slave. Optionally, the
pins can be left unused by the peripheral. Then the flow has to be handled internally for both master and
slave. For more details see Section 27.5.5: Slave select (NSS) pin management.
2. An accidental input information is captured at the input of transmitter Rx shift register. All the events
associated with the transmitter receive flow must be ignored in standard transmit only mode (e.g. OVR
flag).
3. In this configuration, both t he MISO pins can be used as GPIOs.
Note: Any simplex communication can be alternat ively replaced by a variant of the half-duplex
communication with a constant setting of the transaction direction (bidirectional mode is
enabled while BDIO bit is not changed).
27.5.3 Standard multislave communication
In a configuration with two or more independent slaves, the master uses GPIO pins to
manage the chip select lines for each slave (see [Figure 283](../figures/figure_283.md)). The master must select one of
the slaves individually by pulling low the GPIO connected to the slave NSS input. When this
is done, a standard master and dedicated slave communication is established.
Rx shift register
Tx shift register Rx shift register
Tx shift register
SPI clock
generator
Master Slave
MISO
MOSI
SCK
NSS
MISO
MOSI
SCK
NSS(1) (1)
(2)
MSv39625V1

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
836/1023 RM0490 Rev 6
[Figure 283](../figures/figure_283.md). Master and three independent slaves
1. NSS pin is not used on master side at this configurat ion. It has to be managed internally (SSM=1, SSI=1) to
prevent any MODF error.
2. As MISO pins of the slaves are connected together, al l slaves must have the GPIO configuration of their
MISO pin set as alternate function open-drain (see I/O alternate function input/output section (GPIO)).
27.5.4 Multimaster communication
Unless SPI bus is not designed for a multimaster capability primarily, the user can use build
in feature which detects a potential conflict between two nodes trying to master the bus at
the same time. For this detection, NSS pin is used configured at hardware input mode.
The connection of more than two SPI nodes working at this mode is impossible as only one
node can apply its output on a common data line at time.
When nodes are non active, both stay at slave mode by default. Once one node wants to
overtake control on the bus, it switches itself into master mode and applies active level on
the slave select input of the other node via dedicated GPIO pin. After the session is
completed, the active slave select signal is released and the node mastering the bus
temporary returns back to passive slave mode waiting for next session start.
Rx shift register
Tx shift register Rx shift register
Tx shift register
SPI clock
generator
Master Slave 1
MISO
MOSI
SCK
NSS
MISO
MOSI
SCK
NSS
(1)
Rx shift register
Tx shift register
Slave 2
Rx shift register
Tx shift register
Slave 3
IO1
IO2
IO3
MISO
MOSI
SCK
NSS
MISO
MOSI
SCK
NSS
MSv39626V1

RM0490 Rev 6 837/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
If potentially both nodes raised their mastering request at the same time a bus conflict event
appears (see mode fault MODF event). Then the user can apply some simple arbitration
process (e.g. to postpone next attempt by predefined different time-outs applied at both
nodes).
[Figure 284](../figures/figure_284.md). Multimaster application
1. The NSS pin is configured at hardware input mode at both nodes. Its active level enables the MISO line
output control as the passive node is configured as a slave.
27.5.5 Slave select (NSS) pin management
In slave mode, the NSS works as a standard “chip select” input and lets the slave
communicate with the master. In master mode, NSS can be used either as output or input.
As an input it can prevent multimaster bus collision, and as an output it can drive a slave
select signal of a single slave.
Hardware or software slave select management can be set using the SSM bit in the
SPIx_CR1 register:
• Software NSS management (SSM = 1): in this configuration, slave select information
is driven internally by the SSI bit value in register SPIx_CR1. The external NSS pin is
free for other application uses.
• Hardware NSS management (SSM = 0): in this case, there are two possible
configurations. The configuration used depends on the NSS output configuration
(SSOE bit in register SPIx_CR1).
– NSS output enable (SSM=0,SSOE = 1): this configuration is only used when the
MCU is set as master. The NSS pin is managed by the hardware. The NSS signal
is driven low as soon as the SPI is enabled in master mode (SPE=1), and is kept
low until the SPI is disabled (SPE =0). A pulse can be generated between
continuous communications if NSS pulse mode is activated (NSSP=1). The SPI
cannot work in multimaster configuration with this NSS setting.
– NSS output disable (SSM=0, SSOE = 0): if the microcontroller is acting as the
master on the bus, this configuration allows multimaster capability. If the NSS pin
is pulled low in this mode, the SPI enters master mode fault state and the device is
automatically reconfigured in slave mode. In slave mode, the NSS pin works as a
standard “chip select” input and the slave is selected while NSS line is at low level.
Rx (Tx) shift register
Tx (Rx) shift register Tx (Rx) shift register
Rx (Tx) shift register
SPI clock
generator
Master
(Slave)
Master
(Slave)
MISO
MOSI
SCK
NSS
MISO
MOSI
SCK
NSS
(1)
(1)
MSv39628V1
SPI clock
generator
GPIO
GPIO

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
838/1023 RM0490 Rev 6
[Figure 285](../figures/figure_285.md). Hardware/software slave select management
27.5.6 Communication formats
During SPI communication, receive and transmit operations are performed simultaneously.
The serial clock (SCK) synchronizes the shifting and sampling of the information on the data
lines. The communication format depends on the clock phase, the clock polarity and the
data frame format. To be able to communicate together, the master and slaves devices must
follow the same communication format.
Clock phase and polarity controls
Four possible timing relationships may be chosen by software, using the CPOL and CPHA
bits in the SPIx_CR1 register. The CPOL (clock polarity) bit controls the idle state value of
the clock when no data is being transferred. This bit affects both master and slave modes. If
CPOL is reset, the SCK pin has a low-level idle state. If CPOL is set, the SCK pin has a
high-level idle state.
If the CPHA bit is set, the second edge on the SCK pin captures the first data bit transacted
(falling edge if the CPOL bit is reset, rising edge if the CPOL bit is set). Data are latched on
each occurrence of this clock transition type. If the CPHA bit is reset, the first edge on the
SCK pin captures the first data bit transacted (falling edge if the CPOL bit is set, rising edge
if the CPOL bit is reset). Data are latched on each occurrence of this clock transition type.
The combination of CPOL (clock polarity) and CPHA (clock phase) bits selects the data
capture clock edge.
1
0
NSS Input
SSM control bit
SSI control bit
SSOE control bit
NSS Output
NSS
pin
(used in Master mode and NSS
HW management only)
NSS
Output
Control
Master
mode Slave mode
Non activeOKVdd
NSS
Inp.
ActiveConflictVss
NSS external logic NSS internal logic
GPIO
logic
MSv35526V6

RM0490 Rev 6 839/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
[Figure 286](../figures/figure_286.md), shows an SPI full-duplex transfer with the four combinations of the CPHA and
CPOL bits.
Note: Prior to changing the CPOL/CPHA bits th e SPI must be disabled by resetting the SPE bit.
The idle state of SCK must correspond to the polarity selected in the SPIx_CR1 register (by
pulling up SCK if CPOL=1 or pulling down SCK if CPOL=0).
[Figure 286](../figures/figure_286.md). Data clock timing diagram
1. The order of data bits depends on LSBFIRST bit setting.
Data frame format
The SPI shift register can be set up to shift out MSB-first or LSB-first, depending on the
value of the LSBFIRST bit. The data frame size is chosen by using the DS bits. It can be set
from 4-bit up to 16-bit length and the setting applies for both transmission and reception.
Whatever the selected data frame size, read access to the FIFO must be aligned with the
FRXTH level. When the SPIx_DR register is accessed, data frames are always right-aligned
into either a byte (if the data fits into a byte) or a half-word (see [Figure 287](../figures/figure_287.md)). During
communication, only bits within the data frame are clocked and transferred.
ai17154e
CPHA  =1
CPHA  =0
CPOL = 1
CPOL = 0
MOSI(1)
MISO(1)
NSS (to slave)
Capture strobe
MSBit
MSBit
LSBit
LSBit
CPOL = 1
CPOL = 0
MOSI(1)
MISO(1)
NSS (to slave)
Capture strobe
MSBit
MSBit
LSBit
LSBit

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
840/1023 RM0490 Rev 6
[Figure 287](../figures/figure_287.md). Data alignment when data length is not equal to 8-bit or 16-bit
Note: The minimum data length is 4 bits. If a data leng th of less than 4 bits is selected, it is forced
to an 8-bit data frame size.
27.5.7 Configuration of SPI
The configuration procedure is almost the same for master and slave. For specific mode
setups, follow the dedicated sections. When a standard communication is to be initialized,
perform these steps:
1. Write proper GPIO registers: Config ure GPIO for MOSI, MISO and SCK pins.
2. Write to the SPI_CR1 register:
a) Configure the serial clock baud ra te using the BR[2:0] bits (Note: 4).
b) Configure the CPOL and CPHA bits co mbination to define one of the four
relationships between the data transfer and the serial clock (CPHA must be
cleared in NSSP mode). (Note: 2 - except the case when CRC is enabled at TI
mode).
c) Select simplex or half-duplex mode by  configuring RXONLY or BIDIMODE and
BIDIOE (RXONLY and BIDIMODE cannot be set at the same time).
d) Configure the LSBFIRST bit to define the frame format (Note: 2).
e) Configure the CRCL and CRCEN bits if CRC is needed (while SCK clock signal is
at idle state).
f) Configure SSM and SSI (Notes: 2 & 3).
g) Configure the MSTR bit (in multimaster NSS configuration, avoid conflict state on
NSS if master is configured to prevent MODF error).
3. Write to SPI_CR2 register:
a) Configure the DS[3:0] bits to sele ct the data length for the transfer.
b) Configure SSOE (Notes: 1 & 2 & 3).
c) Set the FRF bit if the TI protocol is required (keep NSSP bit cleared in TI mode).
d) Set the NSSP bit if the NSS pulse mode between two data units is required (keep
CHPA and TI bits cleared in NSSP mode).
e) Configure the FRXTH bit. The RXFIFO threshold must be aligned to the read
access size for the SPIx_DR register.
f) Initialize LDMA_TX and LDMA_RX bi ts if DMA is used in packed mode.
4. Write to SPI_CRCPR register: Configure the CRC polynomial if needed.
5. Write proper DMA registers: Configure DM A streams dedicated for SPI Tx and Rx in
DMA registers if the DMA streams are used.
MS19589V2
XXX
000
Data frame
Data frame
XX
00
Data frame
Data frame
TX
RX
TX
RX
7
7
54 0
0
15 13 014
15 13 014
DS <= 8 bits: data is right-aligned on byte
Example: DS = 5 bit
DS > 8 bits: data is right-aligned on 16 bit
Example: DS = 14 bit
54

RM0490 Rev 6 841/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
Note: (1) Step is not required in slave mode.
(2) Step is not required in TI mode.
(3) Step is not required in NSSP mode.
(4) The step is not required in slave mode except slave working at TI mode
27.5.8  Procedure for enabling SPI
It is recommended to enable the SPI slave before the master sends the clock. If not,
undesired data transmission might occur. The data register of the slave must already
contain data to be sent before starting communication with the master (either on the first
edge of the communication clock, or before the end of the ongoing communication if the
clock signal is continuous). The SCK signal must be settled at an idle state level
corresponding to the selected polarity before the SPI slave is enabled.
The master at full-duplex (or in any transmit-only mode) starts to communicate when the
SPI is enabled and TXFIFO is not empty, or with the next write to TXFIFO.
In any master receive only mode (RXONLY = 1 or BIDIMODE = 1 & BIDIOE = 0), master
starts to communicate and the clock starts running immediately after SPI is enabled.
For handling DMA, follow the dedicated section.
27.5.9 Data transmission and reception procedures
RXFIFO and TXFIFO
All SPI data transactions pass through the 32-bit embedded FIFOs. This enables the SPI to
work in a continuous flow, and prevents overruns when the data frame size is short. Each
direction has its own FIFO called TXFIFO and RXFIFO. These FIFOs are used in all SPI
modes except for receiver-only mode (slave or master) with CRC calculation enabled (see
Section 27.5.14: CRC calculation).
The handling of FIFOs depends on the data exchange mode (duplex, simplex), data frame
format (number of bits in the frame), access size performed on the FIFO data registers (8-bit
or 16-bit), and whether or not data packing is used when accessing the FIFOs (see
Section 27.5.13: TI mode).
A read access to the SPIx_DR register returns the oldest value stored in RXFIFO that has
not been read yet. A write access to the SPIx_DR stores the written data in the TXFIFO at
the end of a send queue. The read access must be always aligned with the RXFIFO
threshold configured by the FRXTH bit in SPIx_CR2 register. FTLVL[1:0] and FRLVL[1:0]
bits indicate the current occupancy level of both FIFOs.
A read access to the SPIx_DR register must be managed by the RXNE event. This event is
triggered when data is stored in RXFIFO and the threshold (defined by FRXTH bit) is
reached. When RXNE is cleared, RXFIFO is considered to be empty. In a similar way, write
access of a data frame to be transmitted is managed by the TXE event. This event is
triggered when the TXFIFO level is less than or equal to half of its capacity. Otherwise TXE
is cleared and the TXFIFO is considered as full. In this way, RXFIFO can store up to four
data frames, whereas TXFIFO can only store up to three when the data frame format is not
greater than 8 bits. This difference prevents possible corruption of 3x 8-bit data frames
already stored in the TXFIFO when software tries to write more data in 16-bit mode into
TXFIFO. Both TXE and RXNE events can be polled or handled by interrupts. See
[Figure 289](../figures/figure_289.md) through [Figure 292](../figures/figure_292.md).

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
842/1023 RM0490 Rev 6
Another way to manage the data exchange is to use DMA (see Communication using DMA
(direct memory addressing)).
If the next data is received when the RXFIFO is full, an overrun event occurs (see
description of OVR flag at Section 27.5.10: SPI status flags). An overrun event can be
polled or handled by an interrupt.
The BSY bit being set indicates ongoing transaction of a current data frame. When the clock
signal runs continuously, the BSY flag stays set between data frames at master but
becomes low for a minimum duration of one SPI clock at slave between each data frame
transfer.
Sequence handling
A few data frames can be passed at single sequence to complete a message. When
transmission is enabled, a sequence begins and continues while any data is present in the
TXFIFO of the master. The clock signal is provided continuously by the master until TXFIFO
becomes empty, then it stops waiting for additional data.
In receive-only modes, half-duplex (BIDIMODE=1, BIDIOE=0) or simplex (BIDIMODE=0,
RXONLY=1) the master starts the sequence immediately when both SPI is enabled and
receive-only mode is activated. The clock signal is provided by the master and it does not
stop until either SPI or receive-only mode is disabled by the master. The master receives
data frames continuously up to this moment.
While the master can provide all the transactions in continuous mode (SCK signal is
continuous) it has to respect slave capability to handle data flow and its content at anytime.
When necessary, the master must slow down the communication and provide either a
slower clock or separate frames or data sessions with sufficient delays. Be aware there is no
underflow error signal for master or slave in SPI mode, and data from the slave is always
transacted and processed by the master even if the slave could not prepare it correctly in
time. It is preferable for the slave to use DMA, especially when data frames are shorter and
bus rate is high.
Each sequence must be encased by the NSS pulse in parallel with the multislave system to
select just one of the slaves for communication. In a single slave system it is not necessary
to control the slave with NSS, but it is often better to provide the pulse here too, to
synchronize the slave with the beginning of each data sequence. NSS can be managed by
both software and hardware (see Section 27.5.5: Slave select (NSS) pin management).
When the BSY bit is set it signifies an ongoing data frame transaction. When the dedicated
frame transaction is finished, the RXNE flag is raised. The last bit is just sampled and the
complete data frame is stored in the RXFIFO.
Procedure for disabling the SPI
When SPI is disabled, it is mandatory to follow the disable procedures described in this
paragraph. It is important to do this before the system enters a low-power mode when the
peripheral clock is stopped. Ongoing transactions can be corrupted in this case. In some
modes the disable procedure is the only way to stop continuous communication running.
Master in full-duplex or transmit only mode can finish any transaction when it stops
providing data for transmission. In this case, the clock stops after the last data transaction.
Special care must be taken in packing mode when an odd number of data frames are
transacted to prevent some dummy byte exchange (refer to Data packing section). Before
the SPI is disabled in these modes, the user must follow standard disable procedure. When

RM0490 Rev 6 843/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
the SPI is disabled at the master transmitter while a frame transaction is ongoing or next
data frame is stored in TXFIFO, the SPI behavior is not guaranteed.
When the master is in any receive only mode, the only way to stop the continuous clock is to
disable the peripheral by SPE=0. This must occur in specific time window within last data
frame transaction just between the sampling time of its first bit and before its last bit transfer
starts (in order to receive a complete number of expected data frames and to prevent any
additional “dummy” data reading after the last valid data frame). Specific procedure must be
followed when disabling SPI in this mode.
Data received but not read remains stored in RXFIFO when the SPI is disabled, and must
be processed the next time the SPI is enabled, before starting a new sequence. To prevent
having unread data, ensure that RXFIFO is empty when disabling the SPI, by using the
correct disabling procedure, or by initializing all the SPI registers with a software reset via
the control of a specific register dedicated to peripheral reset (see the SPIiRST bits in the
RCC_APBiRSTR registers).
Standard disable procedure is based on pulling BSY status together with FTLVL[1:0] to
check if a transmission session is fully completed. This check can be done in specific cases,
too, when it is necessary to identify the end of ongoing transactions, for example:
• When NSS signal is managed by software and master has to provide proper end of
NSS pulse for slave, or
• When transactions’ streams from DMA or FIFO are completed while the last data frame
or CRC frame transaction is still ongoing in the peripheral bus.
The correct disable procedure is (except when receive only mode is used):
1. Wait until FTLVL[1:0] = 00 (n o more data to transmit).
2. Wait until BSY=0 (the last data frame is processed).
3. Disable th e SPI (SPE=0).
4. Read data until FRLVL[1:0] = 00 (read all the received data).
The correct disable procedure for certain receive only modes is:
1. Interrupt the receive flow by disabling SPI  (SPE=0) in the specific time window while
the last data frame is ongoing.
2. Wait until BSY=0 (the last data frame is processed).
3. Read data until FRLVL[1:0] = 00 (read all the received data).
Note: If packing mode is used and an odd number of  data frames with a format less than or equal
to 8 bits (fitting into one byte) has to be received, FRXTH must be set when FRLVL[1:0] =
01, in order to generate the RXNE event to read the last odd data frame and to keep good
FIFO pointer alignment.
Data packing
When the data frame size fits into one byte (less than or equal to 8 bits), data packing is
used automatically when any read or write 16-bit access is performed on the SPIx_DR
register. The double data frame pattern is handled in parallel in this case. At first, the SPI
operates using the pattern stored in the LSB of the accessed word, then with the other half
stored in the MSB. [Figure 288](../figures/figure_288.md) provides an example of data packing mode sequence
handling. Two data frames are sent after the single 16-bit access the SPIx_DR register of
the transmitter. This sequence can generate just one RXNE event in the receiver if the
RXFIFO threshold is set to 16 bits (FRXTH=0). The receiver then has to access both data
frames by a single 16-bit read of SPIx_DR as a response to this single RXNE event. The

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
844/1023 RM0490 Rev 6
RxFIFO threshold setting and the following read access must be always kept aligned at the
receiver side, as data can be lost if it is not in line.
A specific problem appears if an odd number of such “fit into one byte” data frames must be
handled. On the transmitter side, writing the last data frame of any odd sequence with an 8-
bit access to SPIx_DR is enough. The receiver has to change the Rx_FIFO threshold level
for the last data frame received in the odd sequence of frames in order to generate the
RXNE event.
[Figure 288](../figures/figure_288.md). Packing data in FIFO for transmission and reception
1. In this example: Data size DS[3:0] is 4-bit co nfigured, CPOL=0, CPHA=1 and LSBFIRST =0. The Data
storage is always right aligned while the valid bits are performed on the bus only, the content of LSB byte
goes first on the bus, the unused bits are not taken into account on the transmitter side and padded by
zeros at the receiver side.
Communication using DMA (direct memory addressing)
To operate at its maximum speed and to facilitate the data register read/write process
required to avoid overrun, the SPI features a DMA capability, which implements a simple
request/acknowledge protocol.
A DMA access is requested when the TXDMAEN or RXDMAEN enable bit in the SPIx_CR2
register is set. Separate requests must be issued to the Tx and Rx buffers.
• In transmission, a DMA request is issued each time TXE is set to 1. The DMA then
writes to the SPIx_DR register.
• In reception, a DMA request is issued each time RXNE is set to 1. The DMA then reads
the SPIx_DR register.
See [Figure 289](../figures/figure_289.md) through [Figure 292](../figures/figure_292.md).
When the SPI is used only to transmit data, it is possible to enable only the SPI Tx DMA
channel. In this case, the OVR flag is set because the data received is not read. When the
SPI is used only to receive data, it is possible to enable only the SPI Rx DMA channel.
In transmission mode, when the DMA has written all the data to be transmitted (the TCIF
flag is set in the DMA_ISR register), the BSY flag can be monitored to ensure that the SPI
communication is complete. This is required to avoid corrupting the last transmission before
disabling the SPI or entering the Stop mode. The software must first wait until
FTLVL[1:0]=00 and then until BSY=0.
0x04 0x0A SPI fsm
& shift
TXFIFO
SPIx_DR 0x0A
0x04
0x0A 0x04
SPI fsm
& shift
0x0A
0x04
0x04 0x0A
SPIx_DR
16-bit access when write to data register 16-bit access when read from data register
NSS
SCK
MOSI RXFIFO
MS19590V1
SPI_DR= 0x040A when TxE=1 SPI_DR= 0x040A when RxNE=1

RM0490 Rev 6 845/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
When starting communication using DMA, to prevent DMA channel management raising
error events, these steps must be followed in order:
1. Enable DMA Rx buffer in the RXDMAEN bi t in the SPI_CR2 register, if DMA Rx is
used.
2. Enable DMA streams for Tx and Rx in DMA registers, if the streams are used.
3. Enable DMA Tx buffer in the TXDMAEN bit in the SPI_CR2 register, if DMA Tx is used.
4. Enable the SPI by setting the SPE bit.
To close communication it is mandatory to follow these steps in order:
1. Disable DMA streams for Tx and Rx in the DMA registers, if the streams are used.
2. Disable the SPI by following the SPI disable procedure.
3. Disable DMA Tx and Rx buffers by clea ring the TXDMAEN and RXDMAEN bits in the
SPI_CR2 register, if DMA Tx and/or DMA Rx are used.
Packing with DMA
If the transfers are managed by DMA (TXDMAEN and RXDMAEN set in the SPIx_CR2
register) packing mode is enabled/disabled automatically depending on the PSIZE value
configured for SPI TX and the SPI RX DMA channel. If the DMA channel PSIZE value is
equal to 16-bit and SPI data size is less than or equal to 8-bit, then packing mode is
enabled. The DMA then automatically manages the write operations to the SPIx_DR
register.
If data packing mode is used and the number of data to transfer is not a multiple of two, the
LDMA_TX/LDMA_RX bits must be set. The SPI then considers only one data for the
transmission or reception to serve the last DMA transfer (for more details refer to Data
packing on page 843.)

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
846/1023 RM0490 Rev 6
Communication diagrams
Some typical timing schemes are explained in this section. These schemes are valid no
matter if the SPI events are handled by polling, interrupts or DMA. For simplicity, the
LSBFIRST=0, CPOL=0 and CPHA=1 setting is used as a common assumption here. No
complete configuration of DMA streams is provided.
The following numbered notes are common for [Figure 289](../figures/figure_289.md) on page 847 through [Figure 292](../figures/figure_292.md)
on page 850:
1. The slave starts to control MISO line as NSS is active and SPI is enabled, and is
disconnected from the line when one of them is released. Sufficient time must be
provided for the slave to prepare data dedicated to the master in advance before its
transaction starts.
At the master, the SPI peripheral takes control at MOSI and SCK signals (occasionally
at NSS signal as well) only if SPI is enabled. If SPI is disabled the SPI peripheral is
disconnected from GPIO logic, so the levels at these lines depends on GPIO setting
exclusively.
2. At the master, BSY stays active between fr ames if the communication (clock signal) is
continuous. At the slave, BSY signal always goes down for at least one clock cycle
between data frames.
3. The TXE signal is cleared only if TXFIFO is full.
4. The DMA arbitration process starts just after the TXDMAEN bit is set. The TXE
interrupt is generated just after the TXEIE is set. As the TXE signal is at an active level,
data transfers to TxFIFO start, until TxFIFO becomes full or the DMA transfer
completes.
5. If all the data to be sent can fit into Tx FIFO, the DMA Tx TCIF flag can be raised even
before communication on the SPI bus starts. This flag always rises before the SPI
transaction is completed.
6. The CRC value for a package is calculat ed continuously frame by frame in the
SPIx_TXCRCR and SPIx_RXCRCR registers. The CRC information is processed after
the entire data package has completed, either automatically by DMA (Tx channel must
be set to the number of data frames to be processed) or by SW (the user must handle
CRCNEXT bit during the last data frame processing).
While the CRC value calculated in SPIx_TXCRCR is simply sent out by transmitter,
received CRC information is loaded into RxFIFO and then compared with the
SPIx_RXCRCR register content (CRC error flag can be raised here if any difference).
This is why the user must take care to flush this information from the FIFO, either by
software reading out all the stored content of RxFIFO, or by DMA when the proper
number of data frames is preset for Rx channel (number of data frames + number of
CRC frames) (see the settings at the example assumption).
7. In data packed mode, TxE and RxNE even ts are paired and each read/write access to
the FIFO is 16 bits wide until the number of data frames are even. If the TxFIFO is ¾
full FTLVL status stays at FIFO full level. That is why the last odd data frame cannot be
stored before the TxFIFO becomes ½ full. This frame is stored into TxFIFO with an 8-
bit access either by software or automatically by DMA when LDMA_TX control is set.
8. To receive the last odd data frame in packed mode, the Rx threshold must be changed
to 8-bit when the last data frame is processed, either by software setting FRXTH=1 or
automatically by a DMA internal signal when LDMA_RX is set.

RM0490 Rev 6 847/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
[Figure 289](../figures/figure_289.md). Master full-duplex communication
Assumptions for master full-duplex communication example:
• Data size > 8 bit
If DMA is used:
• Number of Tx frames transacted by DMA is set to 3
• Number of Rx frames transacted by DMA is set to 3
See also : Communication diagrams on page 846 for details about common assumptions
and notes.
DTx1
10
DRx1
NSS
SCK
BSY
MOSI MSB MSB MSB DTx2 DTx3
SPE
TXE
00 11 11 00FTLVL
DTx1 DTx2
LSB DRx2 LSB DRx3 LSB
1010 0010 0000 00
RXNE
DRx1 DRx2 DRx3
FRLVL
DMA Tx TICF DMA Rx TICF
11
2 2
3
4
5
Enable Tx/Rx DMA or interrupts
DMA or software control at Tx events
DMA or software control at Rx events
10
DTx3
10
3
MISO
MSv19266V2

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
848/1023 RM0490 Rev 6
[Figure 290](../figures/figure_290.md). Slave full-duplex communication
Assumptions for slave full-duplex communication example:
• Data size > 8 bit
If DMA is used:
• Number of Tx frames transacted by DMA is set to 3
• Number of Rx frames transacted by DMA is set to 3
See also Communication diagrams on page 846 for details about common assumptions and
notes.
DTx1
10
DRx1
NSS
SCK
BSY
MISO MSB MSB MSB DTx2 DTx3
SPE
TXE
00 11 11 00FTLVL
DTx1 DTx2
LSB DRx2 LSB DRx3 LSB
1010 0010 0000 00
RXNE
DRx1 DRx2 DRx3
FRLVL
DMA Tx TICF DMA Rx TICF
1
1
2
3
4
5
Enable Tx/Rx DMA or interrupts
DMA or software control at Tx events
DMA or software control at Rx events
10
DTx3
10
3
MOSI
MSv32123V2

RM0490 Rev 6 849/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
[Figure 291](../figures/figure_291.md). Master full-duplex communication with CRC
Assumptions for master full-duplex communication with CRC example:
• Data size = 16 bit
• CRC enabled
If DMA is used:
• Number of Tx frames transacted by DMA is set to 2
• Number of Rx frames transacted by DMA is set to 3
See also : Communication diagrams on page 846 for details about common assumptions
and notes.
DTx1
10
DRx1
NSS
SCK
BSY
MOSI MSB MSB MSB DTx2 CRC
SPE
TXE
00 11 10 00FTLVL
DTx1 DTx2
LSB DRx2 LSB CRC LSB
1010 0010 0000 00
RXNE
DRx1 DRx2 DRx3
FRLVL
DMA Tx TICF DMA Rx TICF
11
2
3
4
5 6
Enable Tx/Rx DMA or interrupts
DMA or software control at Tx events
DMA or software control at Rx events
MISO
MSv32124V2

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
850/1023 RM0490 Rev 6
[Figure 292](../figures/figure_292.md). Master full-duplex communication in packed mode
Assumptions for master full-duplex communication in packed mode example:
• Data size = 5 bit
• Read/write FIFO is performed mostly by 16-bit access
• FRXTH=0
If DMA is used:
• Number of Tx frames to be transacted by DMA is set to 3
• Number of Rx frames to be transacted by DMA is set to 3
• PSIZE for both Tx and Rx DMA channel is set to 16-bit
• LDMA_TX=1 and LDMA_RX=1
See also : Communication diagrams on page 846 for details about common assumptions
and notes.
4  3  2  1
10
NSS
SCK
BSY
MOSI 5
SPE
TXE
00 11 11 00FTLVL
DTx1-2 DTx3-4
0110 001000 00
RXNE
DRx1-2 DRx3-4 DRx5
FRLVL
DMA Tx TICF DMA Rx TICF
11
2
3
4
5
Enable Tx/Rx DMA or interrupts
DMA or software control at Tx events
DMA or software control at Rx events
10
DTx5
10
7
4  3  2  15 4  3  2  15 4  3  2  15 4  3  2  15
DTx1-2 DTx3-4 DTx5
5  4  3  2 15  4  3  21 5  4  3  2 15  4  3  21 15  4  3  2MISO
DRx1-2 DRx3-4 DRx5
01
FRTHX=1
01 00 01
8
3
MSv32125V2

RM0490 Rev 6 851/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
27.5.10 SPI status flags
Three status flags are provided for the application to completely monitor the state of the SPI
bus.
Tx buffer empty flag (TXE)
The TXE flag is set when transmission TXFIFO has enough space to store data to send.
TXE flag is linked to the TXFIFO level. The flag goes high and stays high until the TXFIFO
level is lower or equal to 1/2 of the FIFO depth. An interrupt can be generated if the TXEIE
bit in the SPIx_CR2 register is set. The bit is cleared automatically when the TXFIFO level
becomes greater than 1/2.
Rx buffer not empty (RXNE)
The RXNE flag is set depending on the FRXTH bit value in the SPIx_CR2 register:
• If FRXTH is set, RXNE goes high and stays high until the RXFIFO level is greater or
equal to 1/4 (8-bit).
• If FRXTH is cleared, RXNE goes high and stays high until the RXFIFO level is greater
than or equal to 1/2 (16-bit).
An interrupt can be generated if the RXNEIE bit in the SPIx_CR2 register is set.
The RXNE is cleared by hardware automatically when the above conditions are no longer
true.
Busy flag (BSY)
The BSY flag is set and cleared by hardware (writing to this flag has no effect).
When BSY is set, it indicates that a data transfer is in progress on the SPI (the SPI bus is
busy).
The BSY flag can be used in certain modes to detect the end of a transfer so that the
software can disable the SPI or its peripheral clock before entering a low-power mode which
does not provide a clock for the peripheral. This avoids corrupting the last transfer.
The BSY flag is also useful for preventing write collisions in a multimaster system.
The BSY flag is cleared under any one of the following conditions:
• When the SPI is correctly disabled
• When a fault is detected in Master mode (MODF bit set to 1)
• In Master mode, when it finishes a data transmission and no new data is ready to be
sent
• In Slave mode, when the BSY flag is set to '0' for at least one SPI clock cycle between
each data transfer.
Note: When the next transmission can be handled imme diately by the master (e.g. if the master is
in Receive-only mode or its Transmit FIFO is not empty), communication is continuous and
the BSY flag remains set to '1' between transfers on the master side. Although this is not the
case with a slave, it is recommended to use always the TXE and RXNE flags (instead of the
BSY flags) to handle data transmission or reception operations.

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
852/1023 RM0490 Rev 6
27.5.11 SPI error flags
An SPI interrupt is generated if one of the following error flags is set and interrupt is enabled
by setting the ERRIE bit.
Overrun flag (OVR)
An overrun condition occurs when data is received by a master or slave and the RXFIFO
has not enough space to store this received data. This can happen if the software or the
DMA did not have enough time to read the previously received data (stored in the RXFIFO)
or when space for data storage is limited e.g. the RXFIFO is not available when CRC is
enabled in receive only mode so in this case the reception buffer is limited into a single data
frame buffer (see Section 27.5.14: CRC calculation).
When an overrun condition occurs, the newly received value does not overwrite the
previous one in the RXFIFO. The newly received value is discarded and all data transmitted
subsequently is lost. Clearing the OVR bit is done by a read access to the SPI_DR register
followed by a read access to the SPI_SR register.
Mode fault (MODF)
Mode fault occurs when the master device has its internal NSS signal (NSS pin in NSS
hardware mode, or SSI bit in NSS software mode) pulled low. This automatically sets the
MODF bit. Master mode fault affects the SPI interface in the following ways:
• The MODF bit is set and an SPI interrupt is generated if the ERRIE bit is set.
• The SPE bit is cleared. This blocks all output from the device and disables the SPI
interface.
• The MSTR bit is cleared, thus forcing the device into slave mode.
Use the following software sequence to clear the MODF bit:
1. Make a read or write access to the SPIx_SR register while the MODF bit is set.
2. Then write to the SPIx_CR1 register.
To avoid any multiple slave conflicts in a system comprising several MCUs, the NSS pin
must be pulled high during the MODF bit clearing sequence. The SPE and MSTR bits can
be restored to their original state after this clearing sequence. As a security, hardware does
not allow the SPE and MSTR bits to be set while the MODF bit is set. In a slave device the
MODF bit cannot be set except as the result of a previous multimaster conflict.
CRC error (CRCERR)
This flag is used to verify the validity of the value received when the CRCEN bit in the
SPIx_CR1 register is set. The CRCERR flag in the SPIx_SR register is set if the value
received in the shift register does not match the receiver SPIx_RXCRCR value. The flag is
cleared by the software.
TI mode frame format error (FRE)
A TI mode frame format error is detected when an NSS pulse occurs during an ongoing
communication when the SPI is operating in slave mode and configured to conform to the TI
mode protocol. When this error occurs, the FRE flag is set in the SPIx_SR register. The SPI
is not disabled when an error occurs, the NSS pulse is ignored, and the SPI waits for the
next NSS pulse before starting a new transfer. The data may be corrupted since the error
detection may result in the loss of two data bytes.

RM0490 Rev 6 853/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
The FRE flag is cleared when SPIx_SR register is read. If the ERRIE bit is set, an interrupt
is generated on the NSS error detection. In this case, the SPI should be disabled because
data consistency is no longer guaranteed and communications should be reinitiated by the
master when the slave SPI is enabled again.
27.5.12 NSS pulse mode
This mode is activated by the NSSP bit in the SPIx_CR2 register and it takes effect only if
the SPI interface is configured as Motorola SPI master (FRF=0) with capture on the first
edge (SPIx_CR1 CPHA = 0, CPOL setting is ignored). When activated, an NSS pulse is
generated between two consecutive data frame transfers when NSS stays at high level for
the duration of one clock period at least. This mode allows the slave to latch data. NSSP
pulse mode is designed for applications with a single master-slave pair.
[Figure 293](../figures/figure_293.md) illustrates NSS pin management when NSSP pulse mode is enabled.
[Figure 293](../figures/figure_293.md). NSSP pulse generation in Motorola SPI master mode
Note: Similar behavior is encountered when CPOL = 0. In this case the sampling edge is the rising
edge of SCK, and NSS assertion and deassertion refer to this sampling edge.
27.5.13 TI mode
TI protocol in master mode
The SPI interface is compatible with the TI protocol. The FRF bit of the SPIx_CR2 register
can be used to configure the SPI to be compliant with this protocol.
The clock polarity and phase are forced to conform to the TI protocol requirements whatever
the values set in the SPIx_CR1 register. NSS management is also specific to the TI protocol
which makes the configuration of NSS management through the SPIx_CR1 and SPIx_CR2
registers (SSM, SSI, SSOE) impossible in this case.
In slave mode, the SPI baud rate prescaler is used to control the moment when the MISO
pin state changes to HiZ when the current transaction finishes (see [Figure 294](../figures/figure_294.md)). Any baud
rate can be used, making it possible to determine this moment with optimal flexibility.
However, the baud rate is generally set to the external master clock baud rate. The delay for
the MISO signal to become HiZ (trelease) depends on internal resynchronization and on the
MS19838V1
MOSI
output
NSS
output
SCK
output
sampling
MISO
input Do not care
MSB
MSB
4-bits to 16-bits
Do not care
LSB
LSB
MSB
MSB
LSB
LSB
4-bits to 16-bits
Do not care
Master continuous transfer (CPOL = 1; CPHA = 0; NSSP= 1)
sampling sampling sampling sampling sampling
tSCK tSCK tSCK tSCK tSCK

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
854/1023 RM0490 Rev 6
baud rate value set in through the BR[2:0] bits in the SPIx_CR1 register. It is given by the
formula:
If the slave detects a misplaced NSS pulse during a data frame transaction the TIFRE flag is
set.
If the data size is equal to 4-bits or 5-bits, the master in full-duplex mode or transmit-only
mode uses a protocol with one more dummy data bit added after LSB. TI NSS pulse is
generated above this dummy bit clock cycle instead of the LSB in each period.
This feature is not available for Motorola SPI communications (FRF bit set to 0).
[Figure 294](../figures/figure_294.md): TI mode transfer shows the SPI communication waveforms when TI mode is
selected.
[Figure 294](../figures/figure_294.md). TI mode transfer
27.5.14 CRC calculation
Two separate CRC calculators are implemented in order to check the reliability of
transmitted and received data. The SPI offers CRC8 or CRC16 calculation independently of
the frame data length, which can be fixed to 8-bit or 16-bit. For all the other data frame
lengths, no CRC is available.
CRC principle
CRC calculation is enabled by setting the CRCEN bit in the SPIx_CR1 register before the
SPI is enabled (SPE = 1). The CRC value is calculated using an odd programmable
polynomial on each bit. The calculation is processed on the sampling clock edge defined by
the CPHA and CPOL bits in the SPIx_CR1 register. The calculated CRC value is checked
automatically at the end of the data block as well as for transfer managed by CPU or by the
DMA. When a mismatch is detected between the CRC calculated internally on the received
data and the CRC sent by the transmitter, a CRCERR flag is set to indicate a data corruption
error. The right procedure for handling the CRC calculation depends on the SPI
configuration and the chosen transfer management.
tbaud_rate
2---------------------- 4t pclk×+ trelease
tbaud_rate
2---------------------- 6t pclk×+<<
MS19835V2
MSB
MISO
NSS
SCK
triggersamplingtriggersamplingtriggersampling
Do not care LSBMOSI
1 or 0 MSB LSB
MSB LSB
MSB LSB
FRAME 1 FRAME 2
t RELEASE

RM0490 Rev 6 855/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
Note: The polynomial value should only be odd. No even values are supported.
CRC transfer managed by CPU
Communication starts and continues normally until the last data frame has to be sent or
received in the SPIx_DR register. Then CRCNEXT bit has to be set in the SPIx_CR1
register to indicate that the CRC frame transaction follows after the transaction of the
currently processed data frame. The CRCNEXT bit must be set before the end of the last
data frame transaction. CRC calculation is frozen during CRC transaction.
The received CRC is stored in the RXFIFO like a data byte or word. That is why in CRC
mode only, the reception buffer has to be considered as a single 16-bit buffer used to
receive only one data frame at a time.
A CRC-format transaction usually takes one more data frame to communicate at the end of
data sequence. However, when setting an 8-bit data frame checked by 16-bit CRC, two
more frames are necessary to send the complete CRC.
When the last CRC data is received, an automatic check is performed comparing the
received value and the value in the SPIx_RXCRC register. Software has to check the
CRCERR flag in the SPIx_SR register to determine if the data transfers were corrupted or
not. Software clears the CRCERR flag by writing '0' to it.
After the CRC reception, the CRC value is stored in the RXFIFO and must be read in the
SPIx_DR register in order to clear the RXNE flag.
CRC transfer managed by DMA
When SPI communication is enabled with CRC communication and DMA mode, the
transmission and reception of the CRC at the end of communication is automatic (with the
exception of reading CRC data in receive only mode). The CRCNEXT bit does not have to
be handled by the software. The counter for the SPI transmission DMA channel has to be
set to the number of data frames to transmit excluding the CRC frame. On the receiver side,
the received CRC value is handled automatically by DMA at the end of the transaction but
user must take care to flush out received CRC information from RXFIFO as it is always
loaded into it. In full-duplex mode, the counter of the reception DMA channel can be set to
the number of data frames to receive including the CRC, which means, for example, in the
specific case of an 8-bit data frame checked by 16-bit CRC:
DMA_RX = Numb_of_data + 2
In receive only mode, the DMA reception channel counter should contain only the amount of
data transferred, excluding the CRC calculation. Then based on the complete transfer from
DMA, all the CRC values must be read back by software from FIFO as it works as a single
buffer in this mode.
At the end of the data and CRC transfers, the CRCERR flag in the SPIx_SR register is set if
corruption occurred during the transfer.
If packing mode is used, the LDMA_RX bit needs managing if the number of data is odd.
Resetting the SPIx_TXCRC and SPIx_RXCRC values
The SPIx_TXCRC and SPIx_RXCRC values are cleared automatically when new data is
sampled after a CRC phase. This allows the use of DMA circular mode (not available in
receive-only mode) in order to transfer data without any interruption, (several data blocks
covered by intermediate CRC checking phases).

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
856/1023 RM0490 Rev 6
If the SPI is disabled during a communication the following sequence must be followed:
1. Disable the SPI
2. Clear the CRCEN bit
3. Enable the CRCEN bit
4. Enable the SPI
Note: When the SPI interface is configured as a sl ave, the NSS internal signal needs to be kept
low during transaction of the CRC phase once the CRCNEXT signal is released. That is why
the CRC calculation cannot be used at NSS Pulse mode when NSS hardware mode should
be applied at slave normally.
At TI mode, despite the fact that clock phase and clock polarity setting is fixed and
independent on SPIx_CR1 register, the corresponding setting CPOL=0 CPHA=1 has to be
kept at the SPIx_CR1 register anyway if CRC is applied. In addition, the CRC calculation
has to be reset between sessions by SPI disable sequence with re-enable the CRCEN bit
described above at both master and slave side, else CRC calculation can be corrupted at
this specific mode.
27.6 SPI interrupts
During SPI communication an interrupt can be generated by the following events:
• Transmit TXFIFO ready to be loaded
• Data received in Receive RXFIFO
• Master mode fault
• Overrun error
• TI frame format error
• CRC protocol error
Interrupts can be enabled and disabled separately.
[Table 136](../tables/table_136.md). SPI interrupt requests
Interrupt event Event flag Enable Control bit
Transmit TXFIFO ready to be loaded TXE TXEIE
Data received in RXFIFO RXNE RXNEIE
Master Mode fault event MODF
ERRIE
Overrun error OVR
TI frame format error FRE
CRC protocol error CRCERR

RM0490 Rev 6 857/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
27.7 I2S functional description
27.7.1 I2S general description
The block diagram of the I2S is shown in [Figure 295](../figures/figure_295.md).
[Figure 295](../figures/figure_295.md). I2S block diagram
1. MCK is mapped on the MISO pin.
The SPI can function as an audio I2S interface when the I2S capability is enabled (by
setting the I2SMOD bit in the SPIx_I2SCFGR register). This interface mainly uses the same
pins, flags and interrupts as the SPI.
Tx buffer
Shift register
16-bit
Communication
Rx buffer
16-bit
MOSI/SD
Master control logic
MISO
SPI
baud rate generator
I2SMOD
LSB first
LSB
First SPE BR2 BR1 BR0 MSTR CPOL CPHA
Bidi
mode
Bidi
OE
CRC
EN
CRC
Next DFF Rxonly SSM SSI
Address and data bus
control
NSS/WS
BSY OVR MODF CRCERR CHSIDE TxE RxNE
I2S clock generator
MCK
I2S_CK
I2S
MOD I2SE
CHDATLEN LENCK POLI2SCFG I2SSTD
MCKOE ODD I2SDIV[7:0]
[1:0] [1:0] [1:0]
UDR
I2SxCLK
MS32126V1
FRE
CK

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
858/1023 RM0490 Rev 6
The I2S shares three common pins with the SPI:
• SD: Serial Data (mapped on the MOSI pin) to transmit or receive the two time-
multiplexed data channels (in half-duplex mode only).
• WS: Word Select (mapped on the NSS pin) is the data control signal output in master
mode and input in slave mode.
• CK: Serial Clock (mapped on the SCK pin) is the serial clock output in master mode
and serial clock input in slave mode.
An additional pin can be used when a master clock output is needed for some external
audio devices:
• MCK: Master Clock (mapped separately) is used, when the I2S is configured in master
mode (and when the MCKOE bit in the SPIx_I2SPR register is set), to output this
additional clock generated at a preconfigured frequency rate equal to 256 × fS for all
I2S modes, and to 128 x fS for all PCM modes, where fS is the audio sampling
frequency.
The I2S uses its own clock generator to produce the communication clock when it is set in
master mode. This clock generator is also the source of the master clock output. Two
additional registers are available in I2S mode. One is linked to the clock generator
configuration SPIx_I2SPR and the other one is a generic I2S configuration register
SPIx_I2SCFGR (audio standard, slave/master mode, data format, packet frame, clock
polarity, etc.).
The SPIx_CR1 register and all CRC registers are not used in the I2S mode. Likewise, the
SSOE bit in the SPIx_CR2 register and the MODF and CRCERR bits in the SPIx_SR are
not used.
The I2S uses the same SPI register for data transfer (SPIx_DR) in 16-bit wide mode.
27.7.2 Supported audio protocols
The three-line bus has to handle only audio data generally time-multiplexed on two
channels: the right channel and the left channel. However there is only one 16-bit register
for transmission or reception. So, it is up to the software to write into the data register the
appropriate value corresponding to each channel side, or to read the data from the data
register and to identify the corresponding channel by checking the CHSIDE bit in the
SPIx_SR register. Channel left is always sent first followed by the channel right (CHSIDE
has no meaning for the PCM protocol).
Four data and packet frames are available. Data may be sent with a format of:
• 16-bit data packed in a 16-bit frame
• 16-bit data packed in a 32-bit frame
• 24-bit data packed in a 32-bit frame
• 32-bit data packed in a 32-bit frame
When using 16-bit data extended on 32-bit packet, the first 16 bits (MSB) are the significant
bits, the 16-bit LSB is forced to 0 without any need for software action or DMA request (only
one read/write operation).
The 24-bit and 32-bit data frames need two CPU read or write operations to/from the
SPIx_DR register or two DMA operations if the DMA is preferred for the application. For 24-
bit data frame specifically, the 8 non-significant bits are extended to 32 bits with 0-bits (by
hardware).

RM0490 Rev 6 859/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
For all data formats and communication standards, the most significant bit is always sent
first (MSB first).
The I2S interface supports four audio standards, configurable using the I2SSTD[1:0] and
PCMSYNC bits in the SPIx_I2SCFGR register.
I2S Philips standard
For this standard, the WS signal is used to indicate which channel is being transmitted. It is
activated one CK clock cycle before the first bit (MSB) is available.
[Figure 296](../figures/figure_296.md). I2S Philips protocol waveforms (16/32-bit full accuracy)
Data are latched on the falling edge of CK (for the transmitter) and are read on the rising
edge (for the receiver). The WS signal is also latched on the falling edge of CK.
[Figure 297](../figures/figure_297.md). I2S Philips standard waveforms (24-bit frame)
This mode needs two write or read operations to/from the SPIx_DR register.
• In transmission mode:
If 0x8EAA33 has to be sent (24-bit):
MS19591V1
CK
WS
SD
Can be 16-bit or 32-bit
MSB MSBLSB
Channel left
Channel
right
transmission reception
MS19592V1
CK
WS
SD
Transmission Reception
24-bit data
MSB LSB
Channel left 32-bit
Channel right
8-bit remaining 0 forced

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
860/1023 RM0490 Rev 6
[Figure 298](../figures/figure_298.md). Transmitting 0x8EAA33
• In reception mode:
If data 0x8EAA33 is received:
[Figure 299](../figures/figure_299.md). Receiving 0x8EAA33
[Figure 300](../figures/figure_300.md). I2S Philips standard (16-bit extended to 32-bit packet frame)
When 16-bit data frame extended to 32-bit channel frame is selected during the I2S
configuration phase, only one access to the SPIx_DR register is required. The 16 remaining
bits are forced by hardware to 0x0000 to extend the data to 32-bit format.
If the data to transmit or the received data are 0x76A3 (0x76A30000 extended to 32-bit), the
operation shown in [Figure 301](../figures/figure_301.md) is required.
[Figure 301](../figures/figure_301.md). Example of 16-bit data frame extended to 32-bit channel frame
MS19593V2
0x8EAA 0x33XX
First write to Data register Second write to Data register
Only the 8 MSBs are sent
to compare the 24 bits.
8 LSBs have no meaning
and can be anything
MS19594V1
0x8EAA 0x33XX
First read to Data register Second read to Data register
Only the 8 MSB are sent
to compare the 24 bits
8 LSBs have no meaning
and can be anything
MS19599V1
CK
WS
SD
Transmission Reception
16-bit data
MSB LSB
Channel left 32-bit Channel right
16-bit remaining 0 forced
MS19595V1
0x76A3
Only one access to SPIx_DR

RM0490 Rev 6 861/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
For transmission, each time an MSB is written to SPIx_DR, the TXE flag is set and its
interrupt, if allowed, is generated to load the SPIx_DR register with the new value to send.
This takes place even if 0x0000 have not yet been sent because it is done by hardware.
For reception, the RXNE flag is set and its interrupt, if allowed, is generated when the first
16 MSB half-word is received.
In this way, more time is provided between two write or read operations, which prevents
underrun or overrun conditions (depending on the direction of the data transfer).
MSB justified standard
For this standard, the WS signal is generated at the same time as the first data bit, which is
the MSBit.
[Figure 302](../figures/figure_302.md). MSB Justified 16-bit or 32-bit full-accuracy length
Data are latched on the falling edge of CK (for transmitter) and are read on the rising edge
(for the receiver).
[Figure 303](../figures/figure_303.md). MSB justified 24-bit frame length
MS30100 V1
CK
WS
SD
Transmission Reception
16- or 32 bit data
MSB LSB
Channel left
Channel right
MSB
MS30101V1
CK
WS
SD
Transmission Reception
24 bit data
MSB LSB
Channel left 32-bit
Channel right
8-bit remaining
0 forced

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
862/1023 RM0490 Rev 6
[Figure 304](../figures/figure_304.md). MSB justified 16-bit extended to 32-bit packet frame
LSB justified standard
This standard is similar to the MSB justified standard (no difference for the 16-bit and 32-bit
full-accuracy frame formats).
The sampling of the input and output signals is the same as for the I2S Philips standard.
[Figure 305](../figures/figure_305.md). LSB justified 16-bit or 32-bit full-accuracy
[Figure 306](../figures/figure_306.md). LSB justified 24-bit frame length
• In transmission mode:
If data 0x3478AE have to be transmitted, two write operations to the SPIx_DR register
are required by software or by DMA. The operations are shown below.
MS30102V1
CK
WS
SD
Transmission Reception
16-bit data
MSB LSB
Channel left 32-bit
Channel right
16-bit remaining
0 forced
MS30103V1
CK
WS
SD
Transmission Reception
16- or 32-bit data
MSB LSB
Channel left
Channel right
MSB
MS30104V1
CK
WS
SD
Transmission
Reception
8-bit data
0 forced
MSB LSB
Channel left 32-bit
Channel right
24-bit remaining

RM0490 Rev 6 863/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
[Figure 307](../figures/figure_307.md). Operations required to transmit 0x3478AE
• In reception mode:
If data 0x3478AE are received, two successive read operations from the SPIx_DR
register are required on each RXNE event.
[Figure 308](../figures/figure_308.md). Operations required to receive 0x3478AE
[Figure 309](../figures/figure_309.md). LSB justified 16-bit extended to 32-bit packet frame
When 16-bit data frame extended to 32-bit channel frame is selected during the I2S
configuration phase, Only one access to the SPIx_DR register is required. The 16 remaining
bits are forced by hardware to 0x0000 to extend the data to 32-bit format. In this case it
corresponds to the half-word MSB.
If the data to transmit or the received data are 0x76A3 (0x0000 76A3 extended to 32-bit),
the operation shown in [Figure 310](../figures/figure_310.md) is required.
0xXX34 0x78AE
First write to Data register
conditioned by TXE=1
Second write to Data register
conditioned by TXE=1
Only the 8 LSB of the
half-word are significant.
A field of 0x00 is forced
instead of the 8 MSBs. MS19596V1
0xXX34 0x78AE
First read from Data register
conditioned by RXNE=1
Second read from Data register
conditioned by RXNE=1
Only the 8 LSB of the
half-word are significant.
A field of 0x00 is forced
instead of the 8 MSBs.
MS19597V1
MS30105V1
CK
WS
SD
Transmission
Reception
16-bit data
0 forced
MSB LSB
Channel left 32-bit
Channel right
16-bit remaining

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
864/1023 RM0490 Rev 6
[Figure 310](../figures/figure_310.md). Example of 16-bit data frame extended to 32-bit channel frame
In transmission mode, when a TXE event occurs, the application has to write the data to be
transmitted (in this case 0x76A3). The 0x000 field is transmitted first (extension on 32-bit).
The TXE flag is set again as soon as the effective data (0x76A3) is sent on SD.
In reception mode, RXNE is asserted as soon as the significant half-word is received (and
not the 0x0000 field).
In this way, more time is provided between two write or read operations to prevent underrun
or overrun conditions.
PCM standard
For the PCM standard, there is no need to use channel-side information. The two PCM
modes (short and long frame) are available and configurable using the PCMSYNC bit in
SPIx_I2SCFGR register.
In PCM mode, the output signals (WS, SD) are sampled on the rising edge of CK signal.
The input signals (WS, SD) are captured on the falling edge of CK.
Note that CK and WS are configured as output in MASTER mode.
[Figure 311](../figures/figure_311.md). PCM standard waveforms (16-bit)
For long frame synchronization, the WS signal assertion time is fixed to 13 bits in master
mode.
For short frame synchronization, the WS synchronization signal is only one cycle long.
0x76A3
Only one access to the SPIx-DR register
MS19598V1
MS30106V1
CK
WS
short frame
SD
WS
long frame
13-bits
MSB LSB MSB

RM0490 Rev 6 865/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
[Figure 312](../figures/figure_312.md). PCM standard waveforms (16-bit extended to 32-bit packet frame)
Note: For both modes (master and slave) and for both synchronizations (short and long), the
number of bits between two consecutive pieces of data (and so two synchronization signals)
needs to be specified (DATLEN and CHLEN bits in the SPIx_I2SCFGR register) even in
slave mode.
27.7.3 Start-up description
TheFigure 313 shows how the serial interface is handled in MASTER mode, when the
SPI/I2S is enabled (via I2SE bit). It shows as well the effect of CKPOL on the generated
signals.
MS30107V1
CK
WS
short frame
SD
WS
long frame
Up to 13-bits
MSB LSB
16 bits

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
866/1023 RM0490 Rev 6
[Figure 313](../figures/figure_313.md). Start sequence in master mode
In slave mode, the way the frame synchronization is detected, depends on the value of
ASTRTEN bit.
If ASTRTEN = 0, when the audio interface is enabled (I2SE = 1), then the hardware waits for
the appropriate transition on the incoming WS signal, using the CK signal.
MSv37520V2
dum: not significant data
WS (O)
SD (O)
CK (O), CKPOL = 0
Left sample Right sample
I2SE
WS (O)
CK (O), CKPOL = 1
SD (O) Left sample Right sample
WS (O)
SD (O) Sample1 Sample 2
Master I2S Philips Standard
Master I2S MSB or LSB justified
Master PCM short frame
I2SE
I2SE
CK (O), CKPOL = 0
CK (O), CKPOL = 1
CK (O), CKPOL = 0
CK (O), CKPOL = 1
dum
dum
dum
I2SE
WS (O)
SD (O) Sample1 Sample 2
Master PCM long frame
CK (O), CKPOL = 0
CK (O), CKPOL = 1
dum

RM0490 Rev 6 867/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
The appropriate transition is a falling edge on WS signal when I2S Philips Standard is used,
or a rising edge for other standards. The falling edge is detected by sampling first WS to 1
and then to 0, and vice-versa for the rising edge detection.
If ASTRTEN = 1, the user has to enable the audio interface before the WS becomes active.
This means that the I2SE bit must be set to 1 when WS = 1 for I2S Philips standard, or when
WS = 0 for other standards.
27.7.4 Clock generator
The I2S bit rate determines the data flow on the I2S data line and the I2S clock signal
frequency.
I2S bit rate = number of bits per channel × number of channels × sampling audio frequency
For a 16-bit audio, left and right channel, the I2S bit rate is calculated as follows:
I2S bit rate = 16 × 2 × fS
It is: I2S bit rate = 32 x 2 x fS if the packet length is 32-bit wide.
[Figure 314](../figures/figure_314.md). Audio sampling frequency definition
When the master mode is configured, a specific action needs to be taken to properly
program the linear divider in order to communicate with the desired audio frequency.
[Figure 315](../figures/figure_315.md). I2S clock generator architecture
1. Where x can be 2 or 3.
MS30108V1
16-or 32-bit left
channel
16-or 32-bit
right channel
32- or 64-bits
sampling point sampling point
FS
FS : audio sampling frequency
MS30109V1
MCKOE ODD
8-bit linear divider
+ reshaping stage
Divider by 4 Div2
I²SDIV[7:0]
I²SMOD
CHLEN
0
1
0
1
MCKOE
CK
MCK
I²SxCLK

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
868/1023 RM0490 Rev 6
[Figure 315](../figures/figure_315.md) presents the communication clock architecture. The I2SxCLK clock is provided
by the reset and clock controller (RCC) of the product. The I2SxCLK clock can be
asynchronous with respect to the SPI/I2S APB clock.
Warning: In addition, it is mandato ry to keep the I2SxCLK frequency
higher or equal to the APB clock used by the SPI/I2S block. If
this condition is not respected the SPI/I2S does not work
properly.
The audio sampling frequency may be 192 kHz, 96 kHz, 48 kHz, 44.1 kHz, 32 kHz,
22.05 kHz, 16 kHz, 11.025 kHz or 8 kHz (or any other value within this range).
In order to reach the desired frequency, the linear divider needs to be programmed
according to the formulas below:
For I2S modes:
When the master clock is generated (MCKOE in the SPIx_I2SPR register is set):
When the master clock is disabled (MCKOE bit cleared):
CHLEN = 0 when the channel frame is 16-bit wide and,
CHLEN = 1 when the channel frame is 32-bit wide.
For PCM modes:
When the master clock is generated (MCKOE in the SPIx_I2SPR register is set):
When the master clock is disabled (MCKOE bit cleared):
CHLEN = 0 when the channel frame is 16-bit wide and,
CHLEN = 1 when the channel frame is 32-bit wide.
Where FS is the audio sampling frequency, and FI2SxCLKis the frequency of the kernel clock
provided to the SPI/I2S block.
Fs FI2SxCLK
256 2 (( I2SDIV )× ODD )+×
-----------------------------------------------------------------------------------------------------------=
Fs FI2SxCLK
32 CHLEN 1 )+(× 2(( I2SDIV )× ODD )+×
------------------------------------------------------------------------------------------------------------------------------------------------------------------=
Fs FI2SxCLK
128 2 (( I2SDIV )× ODD )+×
-----------------------------------------------------------------------------------------------------------=
Fs FI2SxCLK
16 CHLEN 1 )+(× 2(( I2SDIV )× ODD )+×
------------------------------------------------------------------------------------------------------------------------------------------------------------------=

RM0490 Rev 6 869/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
Note: I2SDIV must be strictly higher than 1.
The following table provides example precision values for different clock configurations.
Note: Other configurations are possible  that allow optimum clock precision.
[Table 137](../tables/table_137.md). Audio-frequency precision using 48 MHz clock derived from HSE(1)
SYSCLK
(MHz)
Data
length I2SDIV I2SODD MCLK Target fs (Hz) Real fs (kHz) Error
48 16 8 0 No 96000 93750 2.3438%
48 32 4 0 No 96000 93750 2.3438%
48 16 15 1 No 48000 48387.0968 0.8065%
48 32 8 0 No 48000 46875 2.3438%
48 16 17 0 No 44100 44117.647 0.0400%
48 32 8 1 No 44100 44117.647 0.0400%
48 16 23 1 No 32000 31914.8936 0.2660%
48 32 11 1 No 32000 32608.696 1.9022%
48 16 34 0 No 22050 22058.8235 0.0400%
48 32 17 0 No 22050 22058.8235 0.0400%
48 16 47 0 No 16000 15957.4468 0.2660%
48 32 23 1 No 16000 15957.447 0.2660%
48 16 68 0 No 11025 11029.4118 0.0400%
48 32 34 0 No 11025 11029.412 0.0400%
48 16 94 0 No 8000 7978.7234 0.2660%
48 32 47 0 No 8000 7978.7234 0.2660%
48 16 2 0 Yes 48000 46875 2.3430%
48 32 2 0 Yes 48000 46875 2.3430%
48 16 2 0 Yes 44100 46875 6.2925%
48 32 2 0 Yes 44100 46875 6.2925%
48 16 3 0 Yes 32000 31250 2.3438%
48 32 3 0 Yes 32000 31250 2.3438%
48 16 4 1 Yes 22050 20833.333 5.5178%
48 32 4 1 Yes 22050 20833.333 5.5178%
48 16 6 0 Yes 16000 15625 2.3438%
48 32 6 0 Yes 16000 15625 2.3438%
48 16 8 1 Yes 11025 11029.4118 0.0400%
48 32 8 1 Yes 11025 11029.4118 0.0400%
48 16 11 1 Yes 8000 8152.17391 1.9022%
48 32 11 1 Yes 8000 8152.17391 1.9022%

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
870/1023 RM0490 Rev 6
27.7.5 I 2S master mode
The I2S can be configured in master mode. This means that the serial clock is generated on
the CK pin as well as the Word Select signal WS. Master clock (MCK) may be output or not,
controlled by the MCKOE bit in the SPIx_I2SPR register.
Procedure
1. Select the I2SDIV[7:0] bits in the SPIx_I2SPR  register to define the serial clock baud
rate to reach the proper audio sample frequency. The ODD bit in the SPIx_I2SPR
register also has to be defined.
2. Select the CKPOL bit to define the steady  level for the communication clock. Set the
MCKOE bit in the SPIx_I2SPR register if the master clock MCK needs to be provided
to the external DAC/ADC audio component (the I2SDIV and ODD values should be
computed depending on the state of the MCK output, for more details refer to
Section 27.7.4: Clock generator).
3. Set the I2SMOD bit in the SPIx_I2SCFGR register to activate the I2S functions and
choose the I2S standard through the I2SSTD[1:0] and PCMSYNC bits, the data length
through the DATLEN[1:0] bits and the number of bits per channel by configuring the
CHLEN bit. Select also the I2S master mode and direction (Transmitter or Receiver)
through the I2SCFG[1:0] bits in the SPIx_I2SCFGR register.
4. If needed, select all the potential interrupt sources and the DMA capabilities by writing
the SPIx_CR2 register.
5. The I2SE bit in SPIx_I2SCFGR register must be set.
WS and CK are configured in output mode. MCK is also an output, if the MCKOE bit in
SPIx_I2SPR is set.
Transmission sequence
The transmission sequence begins when a half-word is written into the Tx buffer.
Lets assume the first data written into the Tx buffer corresponds to the left channel data.
When data are transferred from the Tx buffer to the shift register, TXE is set and data
corresponding to the right channel have to be written into the Tx buffer. The CHSIDE flag
indicates which channel is to be transmitted. It has a meaning when the TXE flag is set
because the CHSIDE flag is updated when TXE goes high.
A full frame has to be considered as a left channel data transmission followed by a right
channel data transmission. It is not possible to have a partial frame where only the left
channel is sent.
The data half-word is parallel loaded into the 16-bit shift register during the first bit
transmission, and then shifted out, serially, to the MOSI/SD pin, MSB first. The TXE flag is
set after each transfer from the Tx buffer to the shift register and an interrupt is generated if
the TXEIE bit in the SPIx_CR2 register is set.
For more details about the write operations depending on the I2S standard mode selected,
refer to Section 27.7.2: Supported audio protocols).
To ensure a continuous audio data transmission, it is mandatory to write the SPIx_DR
register with the next data to transmit before the end of the current transmission.
1. This table gives only example valu es for different clock configurations. Other configurations allowing
optimum clock precision are possible.

RM0490 Rev 6 871/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
To switch off the I2S, by clearing I2SE, it is mandatory to wait for TXE = 1 and BSY = 0.
Reception sequence
The operating mode is the same as for transmission mode except for the point 3 (refer to the
procedure described in Section 27.7.5: I2S master mode), where the configuration should
set the master reception mode through the I2SCFG[1:0] bits.
Whatever the data or channel length, the audio data are received by 16-bit packets. This
means that each time the Rx buffer is full, the RXNE flag is set and an interrupt is generated
if the RXNEIE bit is set in SPIx_CR2 register. Depending on the data and channel length
configuration, the audio value received for a right or left channel may result from one or two
receptions into the Rx buffer.
Clearing the RXNE bit is performed by reading the SPIx_DR register.
CHSIDE is updated after each reception. It is sensitive to the WS signal generated by the
I2S cell.
For more details about the read operations depending on the I2S standard mode selected,
refer to Section 27.7.2: Supported audio protocols.
If data are received while the previously received data have not been read yet, an overrun is
generated and the OVR flag is set. If the ERRIE bit is set in the SPIx_CR2 register, an
interrupt is generated to indicate the error.
To switch off the I2S, specific actions are required to ensure that the I2S completes the
transfer cycle properly without initiating a new data transfer. The sequence depends on the
configuration of the data and channel lengths, and on the audio protocol mode selected. In
the case of:
• 16-bit data length extended on 32-bit channel length (DATLEN = 00 and CHLEN = 1)
using the LSB justified mode (I2SSTD = 10)
a) Wait for the second to last RXNE = 1 (n – 1)
b) Then wait 17 I2S clock cycles (using a software loop)
c) Disable the I2S (I2SE = 0)
• 16-bit data length extended on 32-bit channel length (DATLEN = 00 and CHLEN = 1) in
MSB justified, I2S or PCM modes (I2SSTD = 00, I2SSTD = 01 or I2SSTD = 11,
respectively)
a) Wait for the last RXNE
b) Then wait 1 I2S clock cycle (using a software loop)
c) Disable the I2S (I2SE = 0)
• For all other combinations of DATLEN and CHLEN, whatever the audio mode selected
through the I2SSTD bits, carry out the following sequence to switch off the I2S:
a) Wait for the second to last RXNE = 1 (n – 1)
b) Then wait one I2S clock cycle (using a software loop)
c) Disable the I2S (I2SE = 0)
Note: The BSY flag is kept low during transfers.
27.7.6 I 2S slave mode
For the slave configuration, the I2S can be configured in transmission or reception mode.
The operating mode is following mainly the same rules as described for the I2S master

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
872/1023 RM0490 Rev 6
configuration. In slave mode, there is no clock to be generated by the I2S interface. The
clock and WS signals are input from the external master connected to the I2S interface.
There is then no need, for the user, to configure the clock.
The configuration steps to follow are listed below:
1. Set the I2SMOD bit in the SPIx_I2SCFGR register to select I 2S mode and choose the
I2S standard through the I2SSTD[1:0] bits, the data length through the DATLEN[1:0]
bits and the number of bits per channel for the frame configuring the CHLEN bit. Select
also the mode (transmission or reception) for the slave through the I2SCFG[1:0] bits in
SPIx_I2SCFGR register.
2. If needed, select all the potential interrupt sources and the DMA capabilities by writing
the SPIx_CR2 register.
3. The I2SE bit in SPIx_I2SCFGR register must be set.
Transmission sequence
The transmission sequence begins when the external master device sends the clock and
when the NSS_WS signal requests the transfer of data. The slave has to be enabled before
the external master starts the communication. The I2S data register has to be loaded before
the master initiates the communication.
For the I2S, MSB justified and LSB justified modes, the first data item to be written into the
data register corresponds to the data for the left channel. When the communication starts,
the data are transferred from the Tx buffer to the shift register. The TXE flag is then set in
order to request the right channel data to be written into the I2S data register.
The CHSIDE flag indicates which channel is to be transmitted. Compared to the master
transmission mode, in slave mode, CHSIDE is sensitive to the WS signal coming from the
external master. This means that the slave needs to be ready to transmit the first data
before the clock is generated by the master. WS assertion corresponds to left channel
transmitted first.
Note: The I2SE has to be written at least two PC LK cycles before the first clock of the master
comes on the CK line.
The data half-word is parallel-loaded into the 16-bit shift register (from the internal bus)
during the first bit transmission, and then shifted out serially to the MOSI/SD pin MSB first.
The TXE flag is set after each transfer from the Tx buffer to the shift register and an interrupt
is generated if the TXEIE bit in the SPIx_CR2 register is set.
Note that the TXE flag should be checked to be at 1 before attempting to write the Tx buffer.
For more details about the write operations depending on the I2S standard mode selected,
refer to Section 27.7.2: Supported audio protocols.
To secure a continuous audio data transmission, it is mandatory to write the SPIx_DR
register with the next data to transmit before the end of the current transmission. An
underrun flag is set and an interrupt may be generated if the data are not written into the
SPIx_DR register before the first clock edge of the next data communication. This indicates
to the software that the transferred data are wrong. If the ERRIE bit is set into the SPIx_CR2
register, an interrupt is generated when the UDR flag in the SPIx_SR register goes high. In
this case, it is mandatory to switch off the I2S and to restart a data transfer starting from the
left channel.
To switch off the I2S, by clearing the I2SE bit, it is mandatory to wait for TXE = 1 and
BSY = 0.

RM0490 Rev 6 873/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
Reception sequence
The operating mode is the same as for the transmission mode except for the point 1 (refer to
the procedure described in Section 27.7.6: I2S slave mode), where the configuration should
set the master reception mode using the I2SCFG[1:0] bits in the SPIx_I2SCFGR register.
Whatever the data length or the channel length, the audio data are received by 16-bit
packets. This means that each time the RX buffer is full, the RXNE flag in the SPIx_SR
register is set and an interrupt is generated if the RXNEIE bit is set in the SPIx_CR2
register. Depending on the data length and channel length configuration, the audio value
received for a right or left channel may result from one or two receptions into the RX buffer.
The CHSIDE flag is updated each time data are received to be read from the SPIx_DR
register. It is sensitive to the external WS line managed by the external master component.
Clearing the RXNE bit is performed by reading the SPIx_DR register.
For more details about the read operations depending the I2S standard mode selected, refer
to Section 27.7.2: Supported audio protocols.
If data are received while the preceding received data have not yet been read, an overrun is
generated and the OVR flag is set. If the bit ERRIE is set in the SPIx_CR2 register, an
interrupt is generated to indicate the error.
To switch off the I2S in reception mode, I2SE has to be cleared immediately after receiving
the last RXNE = 1.
Note: The external master compon ents should have the capability of sending/receiving data in 16-
bit or 32-bit packets via an audio channel.
27.7.7 I2S status flags
Three status flags are provided for the application to fully monitor the state of the I2S bus.
Busy flag (BSY)
The BSY flag is set and cleared by hardware (writing to this flag has no effect). It indicates
the state of the communication layer of the I2S.
When BSY is set, it indicates that the I2S is busy communicating. There is one exception in
master receive mode (I2SCFG = 11) where the BSY flag is kept low during reception.
The BSY flag is useful to detect the end of a transfer if the software needs to disable the
I2S. This avoids corrupting the last transfer. For this, the procedure described below must
be strictly respected.
The BSY flag is set when a transfer starts, except when the I2S is in master receiver mode.
The BSY flag is cleared:
• When a transfer completes (except in master transmit mode, in which the
communication is supposed to be continuous)
• When the I2S is disabled
When communication is continuous:
• In master transmit mode, the BSY flag is kept high during all the transfers
• In slave mode, the BSY flag goes low for one I2S clock cycle between each transfer
Note: Do not use the BSY flag to handle each data tran smission or reception. It is better to use the
TXE and RXNE flags instead.

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
874/1023 RM0490 Rev 6
Tx buffer empty flag (TXE)
When set, this flag indicates that the Tx buffer is empty and the next data to be transmitted
can then be loaded into it. The TXE flag is reset when the Tx buffer already contains data to
be transmitted. It is also reset when the I2S is disabled (I2SE bit is reset).
RX buffer not empty (RXNE)
When set, this flag indicates that there are valid received data in the RX Buffer. It is reset
when SPIx_DR register is read.
Channel Side flag (CHSIDE)
In transmission mode, this flag is refreshed when TXE goes high. It indicates the channel
side to which the data to transfer on SD has to belong. In case of an underrun error event in
slave transmission mode, this flag is not reliable and I2S needs to be switched off and
switched on before resuming the communication.
In reception mode, this flag is refreshed when data are received into SPIx_DR. It indicates
from which channel side data have been received. Note that in case of error (like OVR) this
flag becomes meaningless and the I2S should be reset by disabling and then enabling it
(with configuration if it needs changing).
This flag has no meaning in the PCM standard (for both Short and Long frame modes).
When the OVR or UDR flag in the SPIx_SR is set and the ERRIE bit in SPIx_CR2 is also
set, an interrupt is generated. This interrupt can be cleared by reading the SPIx_SR status
register (once the interrupt source has been cleared).
27.7.8 I2S error flags
There are three error flags for the I2S cell.
Underrun flag (UDR)
In slave transmission mode this flag is set when the first clock for data transmission appears
while the software has not yet loaded any value into SPIx_DR. It is available when the
I2SMOD bit in the SPIx_I2SCFGR register is set. An interrupt may be generated if the
ERRIE bit in the SPIx_CR2 register is set.
The UDR bit is cleared by a read operation on the SPIx_SR register.
Overrun flag (OVR)
This flag is set when data are received and the previous data have not yet been read from
the SPIx_DR register. As a result, the incoming data are lost. An interrupt may be generated
if the ERRIE bit is set in the SPIx_CR2 register.
In this case, the receive buffer contents are not updated with the newly received data from
the transmitter device. A read operation to the SPIx_DR register returns the previous
correctly received data. All other subsequently transmitted half-words are lost.
Clearing the OVR bit is done by a read operation on the SPIx_DR register followed by a
read access to the SPIx_SR register.
Frame error flag (FRE)
This flag can be set by hardware only if the I2S is configured in Slave mode. It is set if the
external master is changing the WS line while the slave is not expecting this change. If the

RM0490 Rev 6 875/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
synchronization is lost, the following steps are required to recover from this state and
resynchronize the external master device with the I2S slave device:
1. Disable the I2S.
2. Enable it again when the correct level is de tected on the WS line (WS line is high in I2S
mode or low for MSB- or LSB-justified or PCM modes.
Desynchronization between master and slave devices may be due to noisy environment on
the CK communication clock or on the WS frame synchronization line. An error interrupt can
be generated if the ERRIE bit is set. The desynchronization flag (FRE) is cleared by
software when the status register is read.
27.7.9 DMA features
In I2S mode, the DMA works in exactly the same way as it does in SPI mode. There is no
difference except that the CRC feature is not available in I2S mode since there is no data
transfer protection system.
27.8 I2S interrupts
[Table 138](../tables/table_138.md) provides the list of I2S interrupts.
[Table 138](../tables/table_138.md). I2S interrupt requests
Interrupt event Event flag Enable control bit
Transmit buffer empty flag TXE TXEIE
Receive buffer not empty flag RXNE RXNEIE
Overrun error OVR
ERRIEUnderrun error UDR
Frame error flag FRE

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
876/1023 RM0490 Rev 6
27.9 SPI and I2S registers
The peripheral registers can be accessed by half-words (16-bit) or words (32-bit). SPI_DR
in addition can be accessed by 8-bit access.
27.9.1 SPI control re gister 1 (SPIx_CR1)
Address offset: 0x00
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
BIDI
MODE BIDIOE CRCEN CRCNEXT CRCL RXONLY SSM SSI LSBFIRST SPE BR[2:0] MSTR CPOL CPHA
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 15 BIDIMODE: Bidirectional data mode enable.
This bit enables half-duplex communication using common single bidirectional data line.
Keep RXONLY bit clear when bidirectional mode is active.
0: 2-line unidirectional data mode selected
1: 1-line bidirectional data mode selected
Note: This bit is not used in I 2S mode.
Bit 14 BIDIOE: Output enable in bidirectional mode
This bit combined with the BIDIMODE bit selects the direction of transfer in bidirectional
mode.
0: Output disabled (receive-only mode)
1: Output enabled (transmit-only mode)
Note: In master mode, the MOSI pin is used  and in slave mode, the MISO pin is used.
This bit is not used in I2S mode.
Bit 13 CRCEN: Hardware CRC calculation enable
0: CRC calculation disabled
1: CRC calculation enabled
Note: This bit should be written only when SPI is disabled (SPE = ‘0’) for correct operation.
This bit is not used in I2S mode.
Bit 12 CRCNEXT: Transmit CRC next
0: Next transmit value is from Tx buffer.
1: Next transmit value is from Tx CRC register.
Note: This bit has to be written as soon as the last data is written in the SPIx_DR register.
This bit is not used in I2S mode.
Bit 11 CRCL: CRC length
This bit is set and cleared by software to select the CRC length.
0: 8-bit CRC length
1: 16-bit CRC length
Note: This bit should be written only when SPI is disabled (SPE = ‘0’) for correct operation.
This bit is not used in I2S mode.

RM0490 Rev 6 877/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
Bit 10 RXONLY: Receive only mode enabled.
This bit enables simplex communication using a single unidirectional line to receive data
exclusively. Keep BIDIMODE bit clear when receive only mode is active.This bit is also
useful in a multislave system in which this particular slave is not accessed, the output from
the accessed slave is not corrupted.
0: Full-duplex (Transmit and receive)
1: Output disabled (Receive-only mode)
Note: This bit is not used in I 2S mode.
Bit 9 SSM: Software slave management
When the SSM bit is set, the NSS pin input is replaced with the value from the SSI bit.
0: Software slave management disabled
1: Software slave management enabled
Note: This bit is not used in I 2S mode and SPI TI mode.
Bit 8 SSI: Internal slave select
This bit has an effect only when the SSM bit is set. The value of this bit is forced onto the
NSS pin and the I/O value of the NSS pin is ignored.
Note: This bit is not used in I 2S mode and SPI TI mode.
Bit 7 LSBFIRST: Frame format
0: data is transmitted / received with the MSB first
1: data is transmitted / received with the LSB first
Note: 1. This bit should not be changed when communication is ongoing.
2. This bit is not used in I2S mode and SPI TI mode.
Bit 6 SPE: SPI enable
0: Peripheral disabled
1: Peripheral enabled
Note: When disabling the SPI, follow the procedure described in Procedure for disabling the
SPI on page 842.
This bit is not used in I2S mode.
Bits 5:3 BR[2:0]: Baud rate control
000: fPCLK/2
001: fPCLK/4
010: fPCLK/8
011: fPCLK/16
100: fPCLK/32
101: fPCLK/64
110: fPCLK/128
111: fPCLK/256
Note: These bits should not be changed when communication is ongoing.
These bits are not used in I2S mode.
Bit 2 MSTR: Master selection
0: Slave configuration
1: Master configuration
Note: This bit should not be changed when communication is ongoing.
This bit is not used in I2S mode.

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
878/1023 RM0490 Rev 6
27.9.2 SPI control re gister 2 (SPIx_CR2)
Address offset: 0x04
Reset value: 0x0700
Bit 1 CPOL: Clock polarity
0: CK to 0 when idle
1: CK to 1 when idle
Note: This bit should not be changed when communication is ongoing.
This bit is not used in I2S mode and SPI TI mode except the case when CRC is applied
at TI mode.
Bit 0 CPHA: Clock phase
0: The first clock transition is the first data capture edge
1: The second clock transition is the first data capture edge
Note: This bit should not be changed when communication is ongoing.
This bit is not used in I2S mode and SPI TI mode except the case when CRC is applied
at TI mode.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. LDMA_TX LDMA_RX FRXTH DS[3:0] TXEIE RXNEIE ERRIE FRF NSSP SSOE TXDMAEN RXDMAEN
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 15 Reserved, must be kept at reset value.
Bit 14 LDMA_TX: Last DMA transfer for transmission
This bit is used in data packing mode, to define if the total number of data to transmit by DMA
is odd or even. It has significance only if the TXDMAEN bit in the SPIx_CR2 register is set
and if packing mode is used (data length =< 8-bit and write access to SPIx_DR is 16-bit
wide). It has to be written when the SPI is disabled (SPE = 0 in the SPIx_CR1 register).
0: Number of data to transfer is even
1: Number of data to transfer is odd
Note: Refer to Procedure for disabling the SPI on page 842 if the CRCEN bit is set.
This bit is not used in I²S mode.
Bit 13 LDMA_RX: Last DMA transfer for reception
This bit is used in data packing mode, to define if the total number of data to receive by DMA
is odd or even. It has significance only if the RXDMAEN bit in the SPIx_CR2 register is set
and if packing mode is used (data length =< 8-bit and write access to SPIx_DR is 16-bit
wide). It has to be written when the SPI is disabled (SPE = 0 in the SPIx_CR1 register).
0: Number of data to transfer is even
1: Number of data to transfer is odd
Note: Refer to Procedure for disabling the SPI on page 842 if the CRCEN bit is set.
This bit is not used in I²S mode.
Bit 12 FRXTH: FIFO reception threshold
This bit is used to set the threshold of the RXFIFO that triggers an RXNE event
0: RXNE event is generated if the FIFO level is greater than or equal to 1/2 (16-bit)
1: RXNE event is generated if the FIFO level is greater than or equal to 1/4 (8-bit)
Note: This bit is not used in I 2S mode.

RM0490 Rev 6 879/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
Bits 11:8 DS[3:0]: Data size
These bits configure the data length for SPI transfers.
0000: Not used
0001: Not used
0010: Not used
0011: 4-bit
0100: 5-bit
0101: 6-bit
0110: 7-bit
0111: 8-bit
1000: 9-bit
1001: 10-bit
1010: 11-bit
1011: 12-bit
1100: 13-bit
1101: 14-bit
1110: 15-bit
1111: 16-bit
If software attempts to write one of the “Not used” values, they are forced to the value “0111”
(8-bit)
Note: These bits are not used in I 2S mode.
Bit 7 TXEIE: Tx buffer empty interrupt enable
0: TXE interrupt masked
1: TXE interrupt not masked. Used to generate an interrupt request when the TXE flag is set.
Bit 6 RXNEIE: RX buffer not empty interrupt enable
0: RXNE interrupt masked
1: RXNE interrupt not masked. Used to generate an interrupt request when the RXNE flag is
set.
Bit 5 ERRIE: Error interrupt enable
This bit controls the generation of an interrupt when an error condition occurs (CRCERR,
OVR, MODF in SPI mode, FRE at TI mode and UDR, OVR, and FRE in I2S mode).
0: Error interrupt is masked
1: Error interrupt is enabled
Bit 4 FRF: Frame format
0: SPI Motorola mode
1 SPI TI mode
Note: This bit must be written only when the SPI is disabled (SPE=0).
This bit is not used in I2S mode.
Bit 3 NSSP: NSS pulse management
This bit is used in master mode only. it allows the SPI to generate an NSS pulse between two
consecutive data when doing continuous transfers. In the case of a single data transfer, it
forces the NSS pin high level after the transfer.
It has no meaning if CPHA = ’1’, or FRF = ’1’.
0: No NSS pulse
1: NSS pulse generated
Note: 1. This bit must be written only when the SPI is disabled (SPE=0).
2. This bit is not used in I2S mode and SPI TI mode.

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
880/1023 RM0490 Rev 6
27.9.3 SPI status register (SPIx_SR)
Address offset: 0x08
Reset value: 0x0002
Bit 2 SSOE: SS output enable
0: SS output is disabled in master mode and the SPI interface can work in multimaster
configuration
1: SS output is enabled in master mode and when the SPI interface is enabled. The SPI
interface cannot work in a multimaster environment.
Note: This bit is not used in I 2S mode and SPI TI mode.
Bit 1 TXDMAEN: Tx buffer DMA enable
When this bit is set, a DMA request is generated whenever the TXE flag is set.
0: Tx buffer DMA disabled
1: Tx buffer DMA enabled
Bit 0 RXDMAEN: Rx buffer DMA enable
When this bit is set, a DMA request is generated whenever the RXNE flag is set.
0: Rx buffer DMA disabled
1: Rx buffer DMA enabled
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. FTLVL[1:0] FRLVL[1:0] FRE BSY OVR MODF CRCERR UDR CHSIDE TXE RXNE
rrrrrrrr r c _ w 0 r r rr
Bits 15:13 Reserved, must be kept at reset value.
Bits 12:11 FTLVL[1:0]: FIFO transmission level
These bits are set and cleared by hardware.
00: FIFO empty
01: 1/4 FIFO
10: 1/2 FIFO
11: FIFO full (considered as FULL when the FIFO threshold is greater than 1/2)
Note: This bit is not used in I 2S mode.
Bits 10:9 FRLVL[1:0]: FIFO reception level
These bits are set and cleared by hardware.
00: FIFO empty
01: 1/4 FIFO
10: 1/2 FIFO
11: FIFO full
Note: These bits are not used in I²S mode and in SPI receive-only mode while CRC
calculation is enabled.
Bit 8 FRE: Frame format error
This flag is used for SPI in TI slave mode and I2S slave mode. Refer to Section 27.5.11: SPI
error flags and Section 27.7.8: I2S error flags.
This flag is set by hardware and reset when SPIx_SR is read by software.
0: No frame format error
1: A frame format error occurred

RM0490 Rev 6 881/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
Bit 7 BSY: Busy flag
0: SPI (or I2S) not busy
1: SPI (or I2S) is busy in communication or Tx buffer is not empty
This flag is set and cleared by hardware.
Note: The BSY flag must be used with caution: refer to Section 27.5.10: SPI status flags and
Procedure for disabling the SPI on page 842.
Bit 6 OVR: Overrun flag
0: No overrun occurred
1: Overrun occurred
This flag is set by hardware and reset by a software sequence. Refer to I2S error flags on
page 874 for the software sequence.
Bit 5 MODF: Mode fault
0: No mode fault occurred
1: Mode fault occurred
This flag is set by hardware and reset by a software sequence. Refer to Section : Mode fault
(MODF) on page 852 for the software sequence.
Note: This bit is not used in I 2S mode.
Bit 4 CRCERR: CRC error flag
0: CRC value received matches the SPIx_RXCRCR value
1: CRC value received does not match the SPIx_RXCRCR value
Note: This flag is set by hardware and cleared by software writing 0.
This bit is not used in I2S mode.
Bit 3 UDR: Underrun flag
0: No underrun occurred
1: Underrun occurred
This flag is set by hardware and reset by a software sequence. Refer to I2S error flags on
page 874 for the software sequence.
Note: This bit is not used in SPI mode.
Bit 2 CHSIDE: Channel side
0: Channel Left has to be transmitted or has been received
1: Channel Right has to be transmitted or has been received
Note: This bit is not used in SPI mode. It has no significance in PCM mode.
Bit 1 TXE: Transmit buffer empty
0: Tx buffer not empty
1: Tx buffer empty
Bit 0 RXNE: Receive buffer not empty
0: Rx buffer empty
1: Rx buffer not empty

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
882/1023 RM0490 Rev 6
27.9.4 SPI data register (SPIx_DR)
Address offset: 0x0C
Reset value: 0x0000
27.9.5 SPI CRC polynomial register (SPIx_CRCPR)
Address offset: 0x10
Reset value: 0x0007
Note: The polynomial value should be odd only. No even value is supported.
27.9.6 SPI Rx CRC regi ster (SPIx_RXCRCR)
Address offset: 0x14
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DR[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 DR[15:0]: Data register
Data received or to be transmitted
The data register serves as an interface between the Rx and Tx FIFOs. When the data
register is read, RxFIFO is accessed while the write to data register accesses TxFIFO (See
Section 27.5.9: Data transmission and reception procedures).
Note: Data is always right-aligned. Unused bits  are ignored when writing to the register, and
read as zero when the register is read. The Rx threshold setting must always
correspond with the read access currently used.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
CRCPOLY[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:0 CRCPOLY[15:0]: CRC polynomial register
This register contains the polynomial for the CRC calculation.
The CRC polynomial (0x0007) is the reset value of this register. Another polynomial can be
configured as required.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
RXCRC[15:0]
rrrrrrrrrrrrrrrr

RM0490 Rev 6 883/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
27.9.7 SPI Tx CRC re gister (SPIx_TXCRCR)
Address offset: 0x18
Reset value: 0x0000
27.9.8 SPIx_I2S configurati on register (SPIx_I2SCFGR)
Address offset: 0x1C
Reset value: 0x0000
Bits 15:0 RXCRC[15:0]: Rx CRC register
When CRC calculation is enabled, the RXCRC[15:0] bits contain the computed CRC value of
the subsequently received bytes. This register is reset when the CRCEN bit in SPIx_CR1
register is written to 1. The CRC is calculated serially using the polynomial programmed in
the SPIx_CRCPR register.
Only the 8 LSB bits are considered when the CRC frame format is set to be 8-bit length
(CRCL bit in the SPIx_CR1 is cleared). CRC calculation is done based on any CRC8
standard.
The entire 16-bits of this register are considered when a 16-bit CRC frame format is selected
(CRCL bit in the SPIx_CR1 register is set). CRC calculation is done based on any CRC16
standard.
Note: A read to this register when the BSY Flag is set could return an incorrect value.
These bits are not used in I2S mode.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
TXCRC[15:0]
rrrrrrrrrrrrrrrr
Bits 15:0 TXCRC[15:0]: Tx CRC register
When CRC calculation is enabled, the TXCRC[7:0] bits contain the computed CRC value of
the subsequently transmitted bytes. This register is reset when the CRCEN bit of SPIx_CR1
is written to 1. The CRC is calculated serially using the polynomial programmed in the
SPIx_CRCPR register.
Only the 8 LSB bits are considered when the CRC frame format is set to be 8-bit length
(CRCL bit in the SPIx_CR1 is cleared). CRC calculation is done based on any CRC8
standard.
The entire 16-bits of this register are considered when a 16-bit CRC frame format is selected
(CRCL bit in the SPIx_CR1 register is set). CRC calculation is done based on any CRC16
standard.
Note: A read to this register when the BSY flag is set could return an incorrect value.
These bits are not used in I2S mode.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. ASTRTEN I2SMOD I2SE I2SCFG[1:0] PCMSYNC Res. I2SSTD[1:0] CKPOL DATLEN[1:0] CHLEN
rw rw rw rw rw rw rw rw rw rw rw rw
Bits 15:13 Reserved, must  be kept at reset value.

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
884/1023 RM0490 Rev 6
Bit 12 ASTRTEN: Asynchronous start enable.
0: The Asynchronous start is disabled.
When the I2S is enabled in slave mode, the hardware starts the transfer when the I2S clock is
received and an appropriate transition is detected on the WS signal.
1: The Asynchronous start is enabled.
When the I2S is enabled in slave mode, the hardware starts the transfer when the I2S clock is
received and the appropriate level is detected on the WS signal.
Note: The appropriate transition is a falling edge on WS signal when I2S Philips Standard is used,
or a rising edge for other standards.
The appropriate level is a low level on WS signal when I2S Philips Standard is used, or a high
level for other standards.
Please refer to Section 27.7.3: Start-up description for additional information.
Bit 11 I2SMOD: I2S mode selection
0: SPI mode is selected
1: I2S mode is selected
Note: This bit should be configured when the SPI is disabled.
Bit 10 I2SE: I2S enable
0: I2S peripheral is disabled
1: I2S peripheral is enabled
Note: This bit is not used in SPI mode.
Bits 9:8 I2SCFG[1:0]: I2S configuration mode
00: Slave - transmit
01: Slave - receive
10: Master - transmit
11: Master - receive
Note: These bits should be configured when the I2S is disabled.
They are not used in SPI mode.
Bit 7 PCMSYNC: PCM frame synchronization
0: Short frame synchronization
1: Long frame synchronization
Note: This bit has a meaning only if I2SSTD = 11 (PCM standard is used).
It is not used in SPI mode.
Bit 6 Reserved, must be kept at reset value.
Bits 5:4 I2SSTD[1:0]: I2S standard selection
00: I2S Philips standard
01: MSB justified standard (left justified)
10: LSB justified standard (right justified)
11: PCM standard
For more details on I2S standards, refer to Section 27.7.2 on page 858
Note: For correct operation, t hese bits should be configured when the I2S is disabled.
They are not used in SPI mode.

RM0490 Rev 6 885/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
27.9.9 SPIx_I2S prescaler register (SPIx_I2SPR)
Address offset: 0x20
Reset value: 0x0002
Bit 3 CKPOL: Inactive state clock polarity
0: I2S clock inactive state is low level
1: I2S clock inactive state is high level
Note: For correct operation, this bit shou ld be configured when the I2S is disabled.
It is not used in SPI mode.
The bit CKPOL does not affect the CK edge sensitivity used to receive or transmit the SD and
WS signals.
Bits 2:1 DATLEN[1:0]: Data length to be transferred
00: 16-bit data length
01: 24-bit data length
10: 32-bit data length
11: Not allowed
Note: For correct operation, t hese bits should be configured when the I2S is disabled.
They are not used in SPI mode.
Bit 0 CHLEN: Channel length (number of bits per audio channel)
0: 16-bit wide
1: 32-bit wide
The bit write operation has a meaning only if DATLEN = 00 otherwise the channel length is fixed to
32-bit by hardware whatever the value filled in.
Note: For correct operation, this bit shou ld be configured when the I2S is disabled.
It is not used in SPI mode.
1 5 1 4 1 3 1 2 1 1 1 0 9 876543210
Res. Res. Res. Res. Res. Res. MCKOE ODD I2SDIV[7:0]
rw rw rw rw rw rw rw rw rw rw
Bits 15:10 Reserved, must be kept at reset value.
Bit 9 MCKOE: Master clock output enable
0: Master clock output is disabled
1: Master clock output is enabled
Note: This bit should be configured when the I2S is disabled. It is used only when the I2S is in
master mode.
It is not used in SPI mode.
Bit 8 ODD: Odd factor for the prescaler
0: Real divider value is = I2SDIV *2
1: Real divider value is = (I2SDIV * 2) + 1
Refer to Section 27.7.3 on page 865.
Note: This bit should be configured when the I2S is disabled. It is used only when the I2S is in
master mode.
It is not used in SPI mode.

Serial peripheral interface / integrated interchip sound (SPI/I2S) RM0490
886/1023 RM0490 Rev 6
Bits 7:0 I2SDIV[7:0]: I2S linear prescaler
I2SDIV [7:0] = 0 or I2SDIV [7:0] = 1 are forbidden values.
Refer to Section 27.7.3 on page 865.
Note: These bits should be configured when the I2 S is disabled. They are used only when the I2S is
in master mode.
They are not used in SPI mode.

RM0490 Rev 6 887/1023
RM0490 Serial peripheral interface / integrated interchip sound (SPI/I2S)
887
27.9.10 SPI/I2S register map
[Table 139](../tables/table_139.md) shows the SPI/I2S register map and reset values.
Refer to Section 2.2 on page 45 for the register boundary addresses.
[Table 139](../tables/table_139.md). SPI/I2S register map and reset values
Offset Register name
reset value
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
SPIx_CR1
BIDIMODE
BIDIOE
CRCEN
CRCNEXT
CRCL
RXONLY
SSM
SSI
LSBFIRST
SPE BR [2:0]
MSTR
CPOL
CPHA
R e s e t  v a l u e 0000000000000000
0x04
SPIx_CR2
Res.
LDMA_TX
LDMA_RX
FRXTH
DS[3:0]
TXEIE
RXNEIE
ERRIE
FRF
NSSP
SSOE
TXDMAEN
RXDMAEN
R e s e t  v a l u e 000011100000000
0x08
SPIx_SR
Res.
Res.
Res.
FTLVL[1:0]
FRLVL[1:0]
FRE
BSY
OVR
MODF
CRCERR
UDR
CHSIDE
TXE
RXNE
R e s e t  v a l u e 0000000000010
0x0C
SPIx_DR DR[15:0]
R e s e t  v a l u e 0000000000000000
0x10
SPIx_CRCPR CRCPOLY[15:0]
R e s e t  v a l u e 0000000000000111
0x14
SPIx_RXCRCR RXCRC[15:0]
R e s e t  v a l u e 0000000000000000
0x18
SPIx_TXCRCR TXCRC[15:0]
R e s e t  v a l u e 0000000000000000
0x1C
SPIx_I2SCFGR
Res.
Res.
Res.
ASTRTEN
I2SMOD
I2SE
I2SCFG[1:0]
PCMSYNC
Res.
I2SSTD
CKPOL
DATLEN[1:0]
CHLEN
R e s e t  v a l u e 000000 000000
0x20
SPIx_I2SPR
Res.
Res.
Res.
Res.
Res.
Res.
MCKOE
ODD
I2SDIV[7:0]
R e s e t  v a l u e 0000000010
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 279: Architectural Diagram](../figures/figure_279.md)
* [Figure 280: Architectural Diagram](../figures/figure_280.md)
* [Figure 281: Architectural Diagram](../figures/figure_281.md)
* [Figure 282: Architectural Diagram](../figures/figure_282.md)
* [Figure 283: Architectural Diagram](../figures/figure_283.md)
* [Figure 284: Architectural Diagram](../figures/figure_284.md)
* [Figure 285: Architectural Diagram](../figures/figure_285.md)
* [Figure 286: Architectural Diagram](../figures/figure_286.md)
* [Figure 287: Architectural Diagram](../figures/figure_287.md)
* [Figure 288: Architectural Diagram](../figures/figure_288.md)
* [Figure 289: Architectural Diagram](../figures/figure_289.md)
* [Figure 290: Architectural Diagram](../figures/figure_290.md)
* [Figure 291: Architectural Diagram](../figures/figure_291.md)
* [Figure 292: Architectural Diagram](../figures/figure_292.md)
* [Figure 293: Architectural Diagram](../figures/figure_293.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 135: Configuration Matrix](../tables/table_135.md)
* [Table 136: Configuration Matrix](../tables/table_136.md)
* [Table 137: Configuration Matrix](../tables/table_137.md)
* [Table 138: Configuration Matrix](../tables/table_138.md)
* [Table 139: Configuration Matrix](../tables/table_139.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)