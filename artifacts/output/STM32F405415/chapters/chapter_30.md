# Chapter 30: Inter-integrated circuit (I2C) interface

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32F4 Reference Manual RM0090 - Chapter 30: Inter-integrated circuit (I2C) interface.
* **Document Source**: RM0090 Reference Manual
* **PDF Reference Location**: Pages 835 - 867
* **Taxonomy Section**: PERIPHERALS
* **Parent IP Module**: [Inter-Integrated Circuit (I2C)](../peripherals/i2c.md)

## 2. Official Reference Manual Text Content (RM0090 Ingestion)
```text
RM0090 Rev 22 835/1741
RM0090 Inter-integrated circuit (I2C) interface
867
27 Inter-integrated circuit (I2C) interface
This section applies to the whole STM32F4xx family, unless otherwise specified.
27.1 I 2C introduction
I2C (inter-integrated circuit) bus interface serves as an interface between the microcontroller
and the serial I2C bus. It provides multicontroller capability, and controls all I2C bus-specific
sequencing, protocol, arbitration, and timing. It supports the standard mode (Sm, up to
100 kHz) and Fm mode (Fm, up to 400 kHz).
It can be used for a variety of purposes, including CRC generation and verification, SMBus
(system management bus) and PMBus® (power management bus).
Depending on specific device implementation, DMA capability can be available for reduced
CPU overload.
27.2 I 2C main features
• Parallel-bus/I2C protocol converter
• Multicontroller capability: the same interface can act as controller or target
• I2C controller features:
– Clock generation
– Start and stop generation
• I2C target features:
– Programmable I 2C address detection
– Dual addressing capability to acknowledge two target addresses
– Stop bit detection
• Generation and detection of 7-bit/10-bit addressing and General Call
• Supports different communication speeds:
– Standard (up to 100 kHz)
– Fast (up to 400 kHz)
• Analog noise filter
• Programmable digital noise filter for STM32F42xxx and STM32F43xxx
• Status flags:
– Transmitter/Receiver mode flag
– End-of-Byte transmission flag
–I 2C busy flag
• Error flags:
– Arbitration lost condition for controller mode
– Acknowledgment failu re after address/ data transmission
– Detection of misplaced start or stop condition
– Overrun/underrun if clock stretching is disabled
• Two interrupt vectors:

Inter-integrated circuit (I2C) interface RM0090
836/1741 RM0090 Rev 22
– One interrupt for successful address/ data communication
– One interrupt for error condition
• Optional clock stretching
• 1-byte buffer with DMA capability
• Configurable PEC (packet error checking) generation or verification:
– PEC value can be transmitted as last byte in Tx mode
– PEC error checking for last received byte
• SMBus 2.0 compatibility:
– 25 ms clock low timeout delay
– 10 ms controller cumulative clock low extend time
– 25 ms target cumulative clock low extend time
– Hardware PEC generation/verification with ACK control
– Address Resolution Protocol (ARP) supported
• PMBus compatibility
Note: Some of the above features may be not ava ilable in some products. Refer to the product
datasheet to identify the specific features supported by the I2C interface implementation.
27.3 I 2C functional description
In addition to receiving and transmitting data, this interface converts them from serial to
parallel format and vice versa. The interrupts are enabled or disabled by software. The
interface is connected to the I2C bus by a data pin (SDA) and by a clock pin (SCL). It can be
connected with a standard (up to 100 kHz) or fast (up to 400 kHz) I2C bus.
27.3.1 Mode selection
The interface can operate in one of the four following modes:
• Target transmitter
• Target receiver
• Controller transmitter
• Controller receiver
By default, it operates in target mode. The interface automatically switches from target to
controller, after it generates a START condition and from controller to target, if an arbitration
loss or a Stop generation occurs, allowing multicontroller capability.
Communication flow
In controller mode, the I2C interface initiates a data transfer and generates the clock signal.
A serial data transfer always begins with a start condition and ends with a stop condition.
Both start and stop conditions are generated in controller mode by software.
In target mode, the interface is capable of recognizing its own addresses (7 or 10-bit), and
the General Call address. The General Call address detection can be enabled or disabled
by software.
Data and addresses are transferred as 8-bit bytes, MSB first. The first byte(s) following the
start condition contain the address (one in 7-bit mode, two in 10-bit mode). The address is
always transmitted in controller mode.

RM0090 Rev 22 837/1741
RM0090 Inter-integrated circuit (I2C) interface
867
A ninth clock pulse follows the 8 clock cycles of a byte transfer, during which the receiver
must send an acknowledge bit to the transmitter. Refer to [Figure 238](../figures/figure_238.md).
[Figure 238](../figures/figure_238.md). I2C bus protocol
Acknowledge can be enabled or disabled by software. The I2C interface addresses (dual
addressing 7-bit/ 10-bit and/or general call address) can be selected by software.
The block diagram of the I2C interface is shown in [Figure 239](../figures/figure_239.md).
MS19854V1
SDA
SCL
Start
condition
Stop
condition
MSB ACK
12 8 9

Inter-integrated circuit (I2C) interface RM0090
838/1741 RM0090 Rev 22
[Figure 239](../figures/figure_239.md). I2C block diagram for STM32F40x/41x
Data shift register
Comparator
Own address register
Clock control
Status registers
Control registers
Control
Clock
control
Data
control
SCL
logic
Dual address register
Data register
PEC register
Interrupts
PEC calculation
SMBA
SDA
Register (CCR)
(SR1&SR2)
(CR1&CR2)
DMA requests & ACK
MS30035V1
Noise
filter
Noise
filter

RM0090 Rev 22 839/1741
RM0090 Inter-integrated circuit (I2C) interface
867
[Figure 240](../figures/figure_240.md). I2C block diagram for STM32F42x/43x
1. SMBA is an optional signal in SMBus mode. This signal is not applicable if SMBus is disabled.
27.3.2 I 2C target mode
By default the I2C interface operates in target mode. To switch from default target mode to
controller mode a Start condition generation is needed.
The peripheral input clock must be programmed in the I2C_CR2 register to generate correct
timings. The peripheral input clock frequency must be at least:
• 2 MHz in Sm mode
• 4 MHz in Fm mode
As soon as a start condition is detected, the address is received from the SDA line and sent
to the shift register. Then it is compared with the address of the interface (OAR1) and with
OAR2 (if ENDUAL=1) or the General Call address (if ENGC = 1).
Note: In 10-bit addressing mode, the comparison includes the header sequence (11110xx0),
where xx denotes the two most significant bits of the address.
Data shift register
Comparator
Own address register
Clock control
Status registers
Control registers
Control
Clock
control
Data
control
SCL
logic
Dual address register
Data register
PEC register
Interrupts
PEC calculation
SMBA
SDA
Register (CCR)
(SR1&SR2)
(CR1&CR2)
DMA requests & ACK
MS30035V1
Noise
filter
Noise
filter

Inter-integrated circuit (I2C) interface RM0090
840/1741 RM0090 Rev 22
Header or address not matched: the interface ignores it and waits for another Start
condition.
Header matched (10-bit mode only): the interface generates an acknowledge pulse if the
ACK bit is set and waits for the 8-bit target address.
Address matched: the interface generates in sequence:
• An acknowledge pulse if the ACK bit is set
• The ADDR bit is set by hardware and an interrupt is generated if the ITEVTEN bit is
set.
• If ENDUAL=1, the software has to read the DUALF bit to check which target address
has been acknowledged.
In 10-bit mode, after receiving the address sequence the target is always in Receiver mode.
It enters Transmitter mode on receiving a repeated Start condition followed by the header
sequence with matching address bits and the least significant bit set (11110xx1).
The TRA bit indicates whether the target is in Receiver or Transmitter mode.
Target transmitter
Following the address reception and after clearing ADDR, the target sends bytes from the
DR register to the SDA line via the internal shift register.
The target stretches SCL low until ADDR is cleared and DR filled with the data to send (see
[Figure 241](../figures/figure_241.md) Transfer sequencing EV1 EV3).
When the acknowledge pulse is received:
• The TxE bit is set by hardware with an interrupt if the ITEVTEN and the ITBUFEN bits
are set.
If TxE is set and some data were not written in the I2C_DR register before the end of the
next data transmission, the BTF bit is set and the interface waits until BTF is cleared by a
read to I2C_SR1 followed by a write to the I2C_DR register, stretching SCL low.
[Figure 241](../figures/figure_241.md). Transfer sequence diagram for target transmitter
1. The EV1 and EV3_1 events stretch SCL low until the end of the corresponding software sequence.
2. The EV3 event stretches SCL low if the software sequence is not completed before the end of the next byte
7-bit target transmitter
10-bit target transmitter
S Address AD a t a 1
.....
EV1 EV3-1 EV3
S r Data1 A ....
EV1 EV3_1 EV3 EV3 EV3-2
ai18209V4
Data2AA DataN NA P
EV3-2EV3 EV3
S Header A Address A
EV1
Header A DataN NA P
Legend: S=Start,  S r  = Repeated Start, P= Stop, A= Acknowledge, NA= Non-acknowledge
EVx: Event (with interrupt if ITEVTEN=1)
EV3-1: TxE=1, shift register empty, data register empty, write Data1 in DR.
EV3-1: TxE=1, shift register not empty, data register empty, cleared by writing DR.
EV3-2: AF=1, AF is cleared by writing ‘0’ in AF bit of SR1 register.
EV1: ADDR=1, cleared by reading SR1 followed by reading SR2

RM0090 Rev 22 841/1741
RM0090 Inter-integrated circuit (I2C) interface
867
transmission.
Target receiver
Following the address reception and after clearing ADDR, the target receives bytes from the
SDA line into the DR register via the internal shift register. After each byte the interface
generates in sequence:
• An acknowledge pulse if the ACK bit is set
• The RxNE bit is set by hardware and an interrupt is generated if the ITEVTEN and
ITBUFEN bit is set.
If RxNE is set and the data in the DR register are not read before the end of the next data
reception, the BTF bit is set and the interface waits until BTF is cleared by a read from the
I2C_DR register, stretching SCL low (see [Figure 242](../figures/figure_242.md) Transfer sequencing).
[Figure 242](../figures/figure_242.md). Transfer sequence diagram for target receiver
1. The EV1 event stretches SCL low until t he end of the corresponding software sequence.
2. The EV2 event stretches SCL low if the software sequence is not completed before the end of the next byte
reception.
3. After checking the SR1 register content, the user  should perform the complete clearing sequence for each
flag found set.
Thus, for ADDR and STOPF flags, the following sequence is required inside the I2C interrupt routine:
READ SR1
if (ADDR = 1) {READ SR1; READ SR2}
if (STOPF = 1) {READ SR1; WRITE CR1}
The purpose is to make sure that both ADDR and STOPF flags are cleared if both are found set.
Closing target communication
After the last data byte is transferred a Stop Condition is generated by the controller. The
interface detects this condition and sets:
• The STOPF bit and generates an interrupt if the ITEVTEN bit is set.
The STOPF bit is cleared by a read of the SR1 register followed by a write to the CR1
register (see EV4 in [Figure 242](../figures/figure_242.md)).
27.3.3 I 2C controller mode
In controller mode, the I2C interface initiates a data transfer and generates the clock signal.
A serial data transfer always begins with a Start condition and ends with a Stop condition.
7-bit target receiver
10-bit target receiver
Legend: S= Start,  S r  = Repeated Start, P= Stop, A= Acknowledge,
EVx= Event (with interrupt if ITEVTEN=1)
EV1: ADDR=1, cleared by reading SR1 followed by reading SR2
EV2:  RxNE=1 cleared by reading DR register.
EV4: STOPF=1, cleared by reading SR1 register followed by writing to the CR1 register
A Data2 A .... .
DataN A P
AA
.... .
DataN
ai18208V3
S Address Data1 A
EV1 EV2 EV2 EV2 EV4
EV2 EV4
A P
EV2
Data1AddressAS Header

Inter-integrated circuit (I2C) interface RM0090
842/1741 RM0090 Rev 22
Controller mode is selected as soon as the Start condition is generated on the bus with a
START bit.
The following is the required sequence in controller mode.
• Program the peripheral input clock in I2C_CR2 register in order to generate correct
timings
• Configure the clock control registers
• Configure the rise time register
• Program the I2C_CR1 register to enable the peripheral
• Set the START bit in the I2C_CR1 register to generate a Start condition
The peripheral input clock frequency must be at least:
• 2 MHz in Sm mode
• 4 MHz in Fm mode
SCL controller clock generation
The CCR bits are used to generate the high and low level of the SCL clock, starting from the
generation of the rising and falling edge (respectively). As a target may stretch the SCL line,
the peripheral checks the SCL input from the bus at the end of the time programmed in
TRISE bits after rising edge generation.
• If the SCL line is low, it means that a target is stretching the bus, and the high level
counter stops until the SCL line is detected high. This guarantees the minimum HIGH
period of the SCL clock parameter.
• If the SCL line is high, the high level counter keeps on counting.
Indeed, the feedback loop from the SCL rising edge generation by the peripheral to the SCL
rising edge detection by the peripheral takes time even if no target stretches the clock. This
loopback duration is linked to the SCL rising time (impacting SCL VIH input detection), plus
delay due to the noise filter present on the SCL input path, plus delay due to internal SCL
input synchronization with APB clock. The maximum time used by the feedback loop is
programmed in the TRISE bits, so that the SCL frequency remains stable whatever the SCL
rising time.
Start condition
Setting the START bit causes the interface to generate a Start condition and to switch to
controller mode (MSL bit set) when the BUSY bit is cleared.
Note: In controller mode, setting the START bit causes the interface to generate a ReStart
condition at the end of the current byte transfer.
Once the Start condition is sent, the SB bit is set by hardware and an interrupt is generated
if the ITEVTEN bit is set. Then the controller waits for a read of the SR1 register followed by
a write in the DR register with the target address (see [Figure 243](../figures/figure_243.md) and [Figure 244](../figures/figure_244.md) Transfer
sequencing EV5).

RM0090 Rev 22 843/1741
RM0090 Inter-integrated circuit (I2C) interface
867
Target address transmission
Then the target address is sent to the SDA line via the internal shift register.
• In 10-bit addressing mode, sending the header sequence causes the following event:
– The ADD10 bit is set by hardware and an interrupt is generated if the ITEVTEN bit
is set.
Then the controller waits for a read of the SR1 register followed by a write in the DR
register with the second address byte (see [Figure 243](../figures/figure_243.md) and [Figure 244](../figures/figure_244.md) Transfer
sequencing).
– The ADDR bit is set by hardware and an interrupt is generated if the ITEVTEN bit
is set.
Then the controller waits for a read of the SR1 register followed by a read of the SR2
register (see [Figure 243](../figures/figure_243.md) and [Figure 244](../figures/figure_244.md) Transfer sequencing).
• In 7-bit addressing mode, one address byte is sent.
As soon as the address byte is sent, the ADDR bit is set by hardware and an interrupt
is generated if the ITEVTEN bit is set. Then the controller waits for a read of the SR1
register followed by a read of the SR2 register (see [Figure 243](../figures/figure_243.md) and [Figure 244](../figures/figure_244.md) Transfer
sequencing).
The controller can decide to enter Transmitter or Receiver mode depending on the LSB of
the target address sent.
• In 7-bit addressing mode
– To enter Transmitter mode, a controller sends the target address with LSB reset.
– To enter Receiver mode, a controller sends the target address with LSB set.
• In 10-bit addressing mode
– To enter Transmitter mode, a controller sends the header (11110xx0) and then the
target address, where xx denotes the two most significant bits of the address.
– To enter Receiver mode, a controller sends the header (11110xx0) and then the
target address. Then it should send a repeated Start condition followed by the
header (11110xx1), where xx denotes the two most significant bits of the address.
The TRA bit indicates whether the controller is in Receiver or Transmitter mode.
Controller transmitter
Following the address transmission and after clearing ADDR, the controller sends bytes
from the DR register to the SDA line via the internal shift register.
The controller waits until the first data byte is written into I2C_DR (see [Figure 243](../figures/figure_243.md) Transfer
sequencing EV8_1).
When the acknowledge pulse is received, the TxE bit is set by hardware and an interrupt is
generated if the ITEVTEN and ITBUFEN bits are set.
If TxE is set and a data byte was not written in the DR register before the end of the last data
transmission, BTF is set and the interface waits until BTF is cleared by a write to I2C_DR,
stretching SCL low.
Closing the communication
After the last byte is written to the DR register, the STOP bit is set by software to generate a
stop condition (see [Figure 243](../figures/figure_243.md) Transfer sequencing EV8_2). The interface automatically
goes back to target mode (MSL bit cleared).

Inter-integrated circuit (I2C) interface RM0090
844/1741 RM0090 Rev 22
Note: Stop condition should be programmed during EV8_2 event, when either TxE or BTF is set.
[Figure 243](../figures/figure_243.md). Transfer sequence diagram for controller transmitter
1. The EV5, EV6, EV9, EV8_1 and EV8_2 events stretch SCL low until the end of the corresponding software sequence.
2. The EV8 event stretches SCL low if the software sequence is not complete before the end of the next byte transmission.
Controller receiver
Following the address transmission and after clearing ADDR, the I2C interface enters
controller receiver mode. In this mode the interface receives bytes from the SDA line into
the DR register via the internal shift register. After each byte the interface generates in
sequence:
1. An acknowledge pulse if the ACK bit is set
2. The RxNE bit is set and an interrupt is generated if the ITEVTEN and ITBUFEN bits are
set (see [Figure 244](../figures/figure_244.md) Transfer sequencing EV7).
If the RxNE bit is set and the data in the DR register is not read before the end of the last
data reception, the BTF bit is set by hardware and the interface waits until BTF is cleared by
a read in the DR register, stretching SCL low.
Closing the communication
The controller sends a NACK for the last byte received from the target. After receiving this
NACK, the target releases the control of the SCL and SDA lines. Then the controller can
send a Stop/Restart condition.
1. To generate the nonacknowledge pulse after the last received data byte, the ACK bit
must be cleared just after reading the second last data byte (after second last RxNE
event).
2. In order to generate the Stop/Restart condi tion, software must set the STOP/START bit
after reading the second last data byte (after the second last RxNE event).
3. In case a single byte has to be received, the Acknowledge disable is made during EV6
(before ADDR flag is cleared) and the STOP condition generation is made after EV6.
After the Stop condition generation, the interface goes automatically back to target mode
(MSL bit cleared).
7-bit controller transmitter
A .... .
.... .
ai18210V3
S Address A Data1 Data2 AD a t a N A P
EV5 EV6 EV8_1 EV8 EV8 EV8 EV8_2
DataN A P
EV8_2
Data1 A
EV8 EV8EV8_1EV6
S
EV5
Header A Address A
EV9
10-bit controller transmitter
Legend: S = Start, SR = Repeated start, P = stop, A = Acknowledge
EVx = Event (with interrupt if ITEVTEN = 1)
EV5: SB=1, cleared by reading SR1 register followed by writing DR register with address
EV6: ADDR=1, cleared by reading SR1 register followed by reading SR2
EV8_1: TxE=1, shift register empty, data register empty, write Data1 in DR
EV8: TxE=1, shift register not empty, data register empty, cleared by writing DR register
EV_2: TxE=1, BTF=1, Program stop request, TxE and BTF are cleared by hardware by the stop condition
EV9: ADD10=1, cleared by reading SR1 register followed by writing DR register.

RM0090 Rev 22 845/1741
RM0090 Inter-integrated circuit (I2C) interface
867
[Figure 244](../figures/figure_244.md). Transfer sequence diagram for controller receiver
1. If a single byte is received, it is NA.
2. The EV5, EV6 and EV9 events stretch SCL low until the end of the corresponding software sequence.
3. The EV7 event stretches SCL low if the software sequence is not completed before the end of the next byte
reception.
4. The EV7_1 software sequence must be completed before the ACK pulse of the current byte transfer.
The procedures described below are recommended if the EV7-1 software sequence is not
completed before the ACK pulse of the current byte transfer.
These procedures must be followed to make sure that the ACK bit is set low on time before
the end of the last data reception, and the STOP bit is set high after the last data reception
without reception of supplementary data.
For 2-byte reception:
• Wait until ADDR = 1 (SCL stretched low until the ADDR flag is cleared)
• Set ACK low, set POS high
• Clear ADDR flag
• Wait until BTF = 1 (Data 1 in DR, Data2 in shift register, SCL stretched low until a data
1 is read)
• Set STOP high
• Read data 1 and 2
7-bit controller receiver
10-bit controller receiver
S Address A D ata1 A (1) Da ta 2 A
.....
DataN NA P
EV5 EV6 EV7 E V7 EV 7_1 EV7
S Header A Address A
EV5 E V9 EV6
S r Header A Data1 A (1)
.....
EV5 EV6 EV7
Data2 A
EV7
DataN NA P
EV7_1 EV7
ai17540e
Legend: S=Start, Sr=Repeated start, P=Stop, A=Acknowledge, NA=Non-acknowledge, Evx=Event (with interrupt if ITEVFEN=1)
EV5: SB=1, cleared by reading SR1 register followed by writing DR register
EV6: ADDR=1, cleared by reading SR1 register followed by reading SR2. In 10-bit controller receiver mode this sequence must be
followed by writing CR2 with START=1. For the reception of 1 byte, the Acknowledge disable must be performed during the EV6
event (before clearing the ADDR flag)
EV7: RxNE=1 cleared by reading DR register
EV7_1: RxNE=1 cleared by reading DR register, program ACK=0 and STOP request
EV9:: ADD10=1 cleared by reading SR1 register, followed by writing DR register

Inter-integrated circuit (I2C) interface RM0090
846/1741 RM0090 Rev 22
For N > 2 -byte reception, from N-2 data reception
• Wait until BTF = 1 (data N-2 in DR, data N-1 in shift register, SCL stretched low until
data N-2 is read)
• Set ACK low
• Read data N-2
• Wait until BTF = 1 (data N-1 in DR, data N in shift register, SCL stretched low until a
data N-1 is read)
• Set STOP high
• Read data N-1 and N
27.3.4 Error conditions
The following are the error conditions which may cause communication to fail.
Bus error (BERR)
This error occurs when the I2C interface detects an external Stop or Start condition during
an address or a data transfer. In this case:
• the BERR bit is set and an interrupt is generated if the ITERREN bit is set
• in target mode: data are discarded and the lines are released by hardware:
– in case of a misplaced Start, the target considers it is a restart and waits for an
address, or a Stop condition
– in case of a misplaced Stop, the target  behaves like for a Stop condition and the
lines are released by hardware
• In controller mode: the lines are not released and the state of the current transmission
is not affected. It is up to the software to abort or not the current transmission
Acknowledge failure (AF)
This error occurs when the interface detects a nonacknowledge bit. In this case:
• the AF bit is set and an interrupt is generated if the ITERREN bit is set
• a transmitter which receives a NACK must reset the communication:
– If target: lines are released by hardware
– If controller: a Stop or repeated Start condition must be generated by software
Arbitration lost (ARLO)
This error occurs when the I2C interface detects an arbitration lost condition. In this case
• the ARLO bit is set by hardware and an interrupt is generated if the ITERREN bit is set
• the I2C Interface goes automatically back to target mode (the MSL bit is cleared). When
the I2C loses the arbitration, it is not able to acknowledge its target address in the same
transfer, but it can acknowledge it after a repeated Start from the winning controller.
• lines are released by hardware

RM0090 Rev 22 847/1741
RM0090 Inter-integrated circuit (I2C) interface
867
Overrun/underrun error (OVR)
An overrun error can occur in target mode when clock stretching is disabled and the I2C
interface is receiving data. The interface has received a byte (RxNE=1) and the data in DR
has not been read, before the next byte is received by the interface. In this case,
• The last received byte is lost.
• In case of overrun error, software should clear the RxNE bit and the transmitter should
re-transmit the last received byte.
Underrun error can occur in target mode when clock stretching is disabled and the I2C
interface is transmitting data. The interface has not updated the DR with the next byte
(TxE = 1), before the clock comes for the next byte. In this case,
• The same byte in the DR register is sent again.
• The user should make sure that data received on the receiver side during an underrun
error are discarded and that the next bytes are written within the clock low time
specified in the I2C bus standard.
For the first byte to be transmitted, the DR must be written after ADDR is cleared and before
the first SCL rising edge. If not possible, the receiver must discard the first data.
27.3.5 Programmable noise filter
The programmable noise filter is available on STM32F42xxx and STM32F43xxx devices
only.
In Fm mode, the I2C standard requires that spikes are suppressed to a length of 50 ns on
SDA and SCL lines.
An analog noise filter is implemented in the SDA and SCL I/Os. This filter is enabled by
default and can be disabled by setting the ANOFF bit in the I2C_FLTR register.
A digital noise filter can be enabled by configuring the DNF[3:0] bits to a non-zero value.
This suppresses the spikes on SDA and SCL inputs with a length of up to DNF[3:0] *
TPCLK1.
Enabling the digital noise filter increases the SDA hold time by (DNF[3:0] +1)* TPCLK.
To be compliant with the maximum hold time of the I2C-bus specification version 2.1
(Thd:dat), the DNF bits must be programmed using the constraints shown in [Table 122](../tables/table_122.md), and
assuming that the analog filter is disabled.
Note: DNF[3:0] must  only be configured when the I2C is disabled (PE = 0). If the analog filter is
also enabled, the digital filter is added to the analog filter.
[Table 122](../tables/table_122.md). Maximum DNF[3:0] value to be compliant with Thd:dat(max)
PCLK1 frequency
Maximum DNF value
Sm mode Fm mode
2 ≤ FPCLK1 ≤ 52 0
5 < FPCLK1 ≤ 10 12 0
10 < FPCLK1 ≤ 20 15 1
20 < FPCLK1 ≤ 30 15 7

Inter-integrated circuit (I2C) interface RM0090
848/1741 RM0090 Rev 22
Note: For each frequency range, the constraint is given based on the worst case which is the
minimum frequency of the range. Higher DNF values can be used if the system can support
maximum hold time violation.
27.3.6 SDA/SCL line control
• If clock stretching is enabled:
– Transmitter mode: If TxE=1 and BTF=1: the interface holds the clock line low
before transmission to wait for the microcontroller to write the byte in the Data
register (both buffer and shift register are empty).
– Receiver mode: If RxNE=1 and BTF=1: t he interface holds the clock line low after
reception to wait for the microcontroller to read the byte in the Data register (both
buffer and shift register are full).
• If clock stretching is disabled in target mode:
– Overrun error in case of RxNE=1 and no read of DR has been done before the
next byte is received. The last received byte is lost.
– Underrun error in case TxE=1 and no write into DR has been done before the next
byte must be transmitted. The same byte is sent again.
– Write collision not managed.
27.3.7 SMBus
Introduction
The System Management Bus (SMBus) is a two-wire interface through which various
devices can communicate with each other and with the rest of the system. It is based on I2C
principles of operation. SMBus provides a control bus for system and power management
related tasks. A system may use SMBus to pass messages to and from devices instead of
toggling individual control lines.
The SMBus specification refers to three types of devices. A target is a device that is
receiving or responding to a command. A controller is a device that issues commands,
generates the clocks, and terminates the transfer. A host is a specialized controller that
provides the main interface to the system's CPU. A host must be a controller-target and
must support the SMBus host notify protocol. Only one host is allowed in a system.
Similarities between SMBus and I2C
• 2-wire bus protocol (1 clk, 1 data) + SMBus Alert line optional
• Controller-target communication, controller provides clock
• Multi controller capability
• SMBus data format similar to I2C 7-bit addressing format ([Figure 238](../figures/figure_238.md)).
30 < FPCLK1 ≤ 40 15 13
40 < FPCLK1 ≤ 50 15 15
[Table 122](../tables/table_122.md). Maximum DNF[3:0] value to be compliant with Thd:dat(max) (continued)
PCLK1 frequency
Maximum DNF value
Sm mode Fm mode

RM0090 Rev 22 849/1741
RM0090 Inter-integrated circuit (I2C) interface
867
Differences between SMBus and I2C
The following table describes the differences between SMBus and I2C.
SMBus application usage
With System Management Bus, a device can provide manufacturer information, tell the
system what its model/part number is, save its state for a suspend event, report different
types of errors, accept control parameters, and return its status. SMBus provides a control
bus for system and power management related tasks.
Device identification
Any device that exists on the System Management Bus as a target has a unique address
called the target address. For the list of reserved target addresses, refer to the SMBus
specification version. 2.0 (http://smbus.org/).
Bus protocols
The SMBus specification supports up to 9 bus protocols. For more details of these protocols
and SMBus address types, refer to SMBus specification version. 2.0. These protocols
should be implemented by the user software.
Address resolution protocol (ARP)
SMBus target address conflicts can be resolved by dynamically assigning a new unique
address to each target device. The Address Resolution Protocol (ARP) has the following
attributes:
• Address assignment uses the standard SMBus physical layer arbitration mechanism
• Assigned addresses remain constant while device power is applied; address retention
through device power loss is also allowed
• No additional SMBus packet overhead is incurred after address assignment. (i.e.
subsequent accesses to assigned target addresses have the same overhead as
accesses to fixed address devices.)
• Any SMBus controller can enumerate the bus
Unique device identifier (UDID)
In order to provide a mechanism to isolate each device for the purpose of address
assignment, each device must implement a unique device identifier (UDID).
[Table 123](../tables/table_123.md). SMBus vs. I2C
SMBus I 2C
Max. speed 100 kHz Max. speed 400 kHz
Min. clock speed 10 kHz No minimum clock speed
35 ms clock low timeout No timeout
Logic levels are fixed Logic levels are V DD dependent
Different address types (reserved, dynamic, ...) 7-bi t, 10-bit and general call target address types
Different bus protocols (quick command, process
call, ...) No bus protocols

Inter-integrated circuit (I2C) interface RM0090
850/1741 RM0090 Rev 22
For the details on 128-bit UDID and more information on ARP, refer to SMBus specification
version 2.0.
SMBus alert mode
SMBus Alert is an optional signal with an interrupt line for devices that want to trade their
ability to controller for a pin. SMBA is a wired-AND signal just as the SCL and SDA signals
are. SMBA is used in conjunction with the SMBus General Call Address. Messages invoked
with the SMBus are two bytes long.
A target-only device can signal the host through SMBA that it wants to talk by setting ALERT
bit in I2C_CR1 register. The host processes the interrupt and simultaneously accesses all
SMBA devices through the Alert Response Address (known as ARA having a value 0001
100X). Only the device(s) which pulled SMBA low acknowledges the alert Response
Address. This status is identified using SMBALERT Status flag in I2C_SR1 register. The
host performs a modified Receive Byte operation. The 7 bit device address provided by the
target transmit device is placed in the seven most significant bits of the byte. The eighth bit
can be a zero or one.
If more than one device pulls SMBA low, the highest priority (lowest address) device wins
communication rights via standard arbitration during the target address transfer. After
acknowledging the target address the device must disengage its SMBA pull-down. If the
host still sees SMBA low when the message transfer is complete, it knows to read the ARA
again.
A host that does not implement the SMBA signal may periodically access the ARA.
For more details on SMBus Alert mode, refer to SMBus specification version 2.0
(https://smbus.org/).
Timeout error
There are differences in the timing specifications between I2C and SMBus.
SMBus defines a clock low timeout, TIMEOUT of 35 ms. Also SMBus specifies TLOW:
SEXT as the cumulative clock low extend time for a target device. SMBus specifies TLOW:
MEXT as the cumulative clock low extend time for a controller device. For more details on
these timeouts, refer to SMBus specification version 2.0.
The status flag Timeout or Tlow Error in I2C_SR1 shows the status of this feature.
How to use the interface in SMBus mode
To switch from I2C mode to SMBus mode, the following sequence should be performed.
• Set the SMBus bit in the I2C_CR1 register
• Configure the SMBTYPE and ENARP bits in the I2C_CR1 register as required for the
application
To configure the device as a controller, follow the Start condition generation procedure in
Section 27.3.3. Otherwise, follow the sequence in Section 27.3.2.
The application must control the various SMBus protocols by software.
• SMB Device Default Address acknowledged if ENARP=1 and SMBTYPE=0
• SMB Host Header acknowledged if ENARP=1 and SMBTYPE=1
• SMB Alert Response Address acknowledged if SMBALERT=1

RM0090 Rev 22 851/1741
RM0090 Inter-integrated circuit (I2C) interface
867
27.3.8 DMA requests
DMA requests (when enabled) are generated only for data transfer. DMA requests are
generated by Data register becoming empty in transmission and Data register becoming full
in reception. The DMA must be initialized and enabled before the I2C data transfer. The
DMAEN bit must be set in the I2C_CR2 register before the ADDR event. In controller mode
or in target mode when clock stretching is enabled, the DMAEN bit can also be set during
the ADDR event, before clearing the ADDR flag. The DMA request must be served before
the end of the current byte transfer. When the number of data transfers which has been
programmed for the corresponding DMA stream is reached, the DMA controller sends an
End of Transfer EOT signal to the I2C interface and generates a Transfer Complete interrupt
if enabled:
• Controller transmitter: In the interrupt routine after the EOT interrupt, disable DMA
requests then wait for a BTF event before programming the Stop condition.
• Controller receiver
– When the number of bytes to be received is equal to or greater than two, the DMA
controller sends a hardware signal, EOT_1, corresponding to the last but one data
byte (number_of_bytes – 1). If, in the I2C_CR2 register, the LAST bit is set, I2C
automatically sends a NACK after the next byte following EOT_1. The user can
generate a Stop condition in the DMA Transfer Complete interrupt routine if
enabled.
– When a single byte must be received: the NACK must be programmed during EV6
event, i.e. program ACK=0 when ADDR=1, before clearing ADDR flag. Then the
user can program the STOP condition either after clearing ADDR flag, or in the
DMA Transfer Complete interrupt routine.
Transmission using DMA
DMA mode can be enabled for transmission by setting the DMAEN bit in the I2C_CR2
register. Data are loaded from a Memory area configured using the DMA peripheral (refer to
the DMA specification) to the I2C_DR register whenever the TxE bit is set. To map a DMA
stream x for I2C transmission (where x is the stream number), perform the following
sequence:
1. Set the I2C_DR register address in the DMA_SxPAR  register. The data are moved to
this address from the memory after each TxE event.
2. Set the memory address in the DMA_SxMA0R  register (and in DMA_SxMA1R register
in the case of a double buffer mode). The data are loaded into I2C_DR from this
memory after each TxE event.
3. Configure the total number of bytes to be transferred in the DMA_SxNDTR  register.
After each TxE event, this value is decremented.
4. Configure the DMA stream priority using the PL[0:1] bits in the DMA_SxCR register
5. Set the DIR bit in the DMA_SxCR  register and configure interrupts after half transfer or
full transfer depending on application requirements.
6. Activate the stream by sett ing the EN bit in the DMA_SxCR register.
When the number of data transfers which has been programmed in the DMA controller
registers is reached, the DMA controller sends an End of Transfer EOT/ EOT_1 signal to the
I2C interface and the DMA generates an interrupt, if enabled, on the DMA stream interrupt
vector.
Note: Do not enable the ITBUFEN bit in the I2C_ CR2 register if DMA is used for transmission.

Inter-integrated circuit (I2C) interface RM0090
852/1741 RM0090 Rev 22
Reception using DMA
DMA mode can be enabled for reception by setting the DMAEN bit in the I2C_CR2 register.
Data are loaded from the I2C_DR register to a Memory area configured using the DMA
peripheral (refer to the DMA specification) whenever a data byte is received. To map a DMA
stream x for I2C reception (where x is the stream number), perform the following sequence:
1. Set the I2C_DR register address in DMA_SxPAR  register. The data are moved from
this address to the memory after each RxNE event.
2. Set the memory address in the DMA_SxMA0R  register (and in DMA_SxMA1R register
in the case of a double buffer mode). The data are loaded from the I2C_DR register to
this memory area after each RxNE event.
3. Configure the total number of bytes to be transferred in the DMA_SxNDTR register.
After each RxNE event, this value is decremented.
4. Configure the stream priority using the PL[0:1] bits in the DMA_SxCR register
5. Reset the DIR bit and configure interrupts in the DMA_SxCR register after half transfer
or full transfer depending on application requirements.
6. Activate the stream by setting th e EN bit in the DMA_SxCR register.
When the number of data transfers programmed in the DMA controller registers is reached,
the DMA controller sends an End of Transfer EOT/ EOT_1 signal to the I2C interface and
DMA generates an interrupt, if enabled, on the DMA stream interrupt vector.
Note: Do not enable the ITBUFEN bit in the I2 C_CR2 register if DMA is used for reception.
27.3.9 Packet error checking
A PEC calculator has been implemented to improve the reliability of communication. The
PEC is calculated by using the C(x) = x8 + x2 + x + 1 CRC-8 polynomial serially on each bit.
• PEC calculation is enabled by setting the ENPEC bit in the I2C_CR1 register. PEC is a
CRC-8 calculated on all message bytes including addresses and R/W bits.
– In transmission: set the PEC transfer bit in the I2C_CR1 register after the TxE
event corresponding to the last byte. The PEC is transferred after the last
transmitted byte.
– In reception: set the PEC bit in the I2C_CR1 register after the RxNE event
corresponding to the last byte so that the receiver sends a NACK if the next
received byte is not equal to the internally calculated PEC. In case of controller-
Receiver, a NACK must follow the PEC whatever the check result. The PEC must
be set before the ACK of the CRC reception in target mode. It must be set when
the ACK is set low in controller mode.
• A PECERR error flag/interrupt is also available in the I2C_SR1 register.
• If DMA and PEC calculation are both enabled:
– In transmission: when the I 2C interface receives an EOT signal from the DMA
controller, it automatically sends a PEC after the last byte.
– In reception: when the I 2C interface receives an EOT_1 signal from the DMA
controller, it automatically considers the next byte as a PEC and checks it. A DMA
request is generated after PEC reception.
• To allow intermediate PEC transfers, a control bit (LAST) is available in the I2C_CR2
register to determine if it is really the last DMA transfer or not. If it is the last DMA

RM0090 Rev 22 853/1741
RM0090 Inter-integrated circuit (I2C) interface
867
request for a controller receiver, a NACK is automatically sent after the last received
byte.
• PEC calculation is corrupted by an arbitration loss.
27.4 I 2C interrupts
The table below gives the list of I2C interrupt requests.
Note: SB, ADDR, ADD10, STOPF, BTF, RxNE and TxE are logically OR-ed on the same interrupt
channel.
BERR, ARLO, AF, OVR, PECERR, TIMEOUT and SMBALERT are logically OR-ed on the
same interrupt channel.
[Table 124](../tables/table_124.md). I2C Interrupt requests
Interrupt event Event flag Enable control bit
Start bit sent (controller) SB
ITEVTEN
Address sent (controller) or Address matched
(target) ADDR
10-bit header sent (controller) ADD10
Stop received (target) STOPF
Data byte transfer finished BTF
Receive buffer not empty RxNE
ITEVTEN and ITBUFEN
Transmit buffer empty TxE
Bus error BERR
ITERREN
Arbitration loss (controller) ARLO
Acknowledge failure AF
Overrun/Underrun OVR
PEC error PECERR
Timeout/Tlow error TIMEOUT
SMBus Alert SMBALERT

Inter-integrated circuit (I2C) interface RM0090
854/1741 RM0090 Rev 22
[Figure 245](../figures/figure_245.md). I2C interrupt mapping diagram
ADDR
SB
ADD10
RxNE
TxE
BTF
it_event
ARLO
BERR
AF
OVR
PECERR
TIMEOUT
SMBALERT
ITERREN
it_error
ITEVTEN
ITBUFEN
STOPF
MS42082V1

RM0090 Rev 22 855/1741
RM0090 Inter-integrated circuit (I2C) interface
867
27.5 I 2C debug mode
When the microcontroller enters the debug mode (Cortex®-M4 with FPU core halted), the
SMBUS timeout either continues to work normally or stops, depending on the
DBG_I2Cx_SMBUS_TIMEOUT configuration bits in the DBG module. For more details,
refer to Section 38.16.2: Debug support for timers, watchdog, bxCAN and I2C.
27.6 I 2C registers
Refer to Section 1.1 for a list of abbreviations used in register descriptions.
The peripheral registers have to be accessed by half-words (16 bits) or words (32 bits).
27.6.1 I 2C Control register 1 (I2C_CR1)
Address offset: 0x00
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9 8 7 6543210
SWRST
Res.
ALERT PEC POS ACK STOP START NO
STRETCH ENGC ENPEC ENARP SMB
TYPE Res.
SMBU
S PE
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 15 SWRST: Software reset
When set, the I2C is under reset state. Before resetting this bit, make sure the I2C lines are
released and the bus is free.
0: I2C Peripheral not under reset
1: I2C Peripheral under reset state
Note: This bit can be used to reinitialize the peri pheral after an error or a locked state. As an
example, if the BUSY bit is set and remains locked due to a glitch on the bus, the
SWRST bit can be used to exit from this state.
Bit 14 Reserved, must be  kept at reset value
Bit 13 ALERT: SMBus alert
This bit is set and cleared by software, and cleared by hardware when PE=0.
0: Releases SMBA pin high. Alert Response Address Header followed by NACK.
1: Drives SMBA pin low. Alert Response Address Header followed by ACK.
Bit 12 PEC: Packet error checking
This bit is set and cleared by software, and cleared by hardware when PEC is transferred or
by a START or Stop condition or when PE=0.
0: No PEC transfer
1: PEC transfer (in Tx or Rx mode)
Note: PEC calculation is corrupted by an arbitration loss.
Bit 11 POS: Acknowledge/PEC Position (for data reception)
This bit is set and cleared by software and cleared by hardware when PE=0.
0: ACK bit controls the (N)ACK of the current byte being received in the shift register. The
PEC bit indicates that current byte in shift register is a PEC.
1: ACK bit controls the (N)ACK of the next byte which is received in the shift register. The
PEC bit indicates that the next byte in the shift register is a PEC
Note: The POS bit must be used only in 2-byte reception configuration in controller mode. It
must be configured before data reception starts, as described in the 2-byte reception
procedure recommended in Section : Controller receiver.

Inter-integrated circuit (I2C) interface RM0090
856/1741 RM0090 Rev 22
Bit 10 ACK: Acknowledge enable
This bit is set and cleared by software and cleared by hardware when PE=0.
0: No acknowledge returned
1: Acknowledge returned after a byte is received (matched address or data)
Bit 9 STOP: Stop generation
The bit is set and cleared by software, cleared by hardware when a Stop condition is
detected, set by hardware when a timeout error is detected.
In Controller mode:
0: No Stop generation.
1: Stop generation after the current byte transfer or after the current Start condition is sent.
In Target mode:
0: No Stop generation.
1: Release the SCL and SDA lines after the current byte transfer.
Bit 8 START: Start generation
This bit is set and cleared by software and cleared by hardware when start is sent or PE=0.
In Controller mode:
0: No Start generation
1: Repeated start generation
In Target mode:
0: No Start generation
1: Start generation when the bus is free
Bit 7 NOSTRETCH: Clock stretching disable (Target mode)
This bit is used to disable clock stretching in target mode when ADDR or BTF flag is set,
until it is reset by software.
0: Clock stretching enabled
1: Clock stretching disabled
Bit 6 ENGC: General call enable
0: General call disabled. Address 00h is NACKed.
1: General call enabled. Address 00h is ACKed.
Bit 5 ENPEC: PEC enable
0: PEC calculation disabled
1: PEC calculation enabled
Bit 4 ENARP: ARP enable
0: ARP disable
1: ARP enable
SMBus Device default address recognized if SMBTYPE=0
SMBus Host address recognized if SMBTYPE=1
Bit 3 SMBTYPE: SMBus type
0: SMBus Device
1: SMBus Host

RM0090 Rev 22 857/1741
RM0090 Inter-integrated circuit (I2C) interface
867
Note: When the STOP , START or PEC bit is set, th e software must not perform any write access
to I2C_CR1 before this bit is cleared by hardware. Otherwise there is a risk of setting a
second STOP , START or PEC request.
27.6.2 I 2C Control register 2 (I2C_CR2)
Address offset: 0x04
Reset value: 0x0000
Bit 2 Reserved, must be kept at reset value
Bit 1 SMBUS: SMBus mode
0: I2C mode
1: SMBus mode
Bit 0 PE: Peripheral enable
0: Peripheral disable
1: Peripheral enable
Note: If this bit is reset while a communication is on going, the peripheral is disabled at the
end of the current communication, when back to IDLE state.
All bit resets due to PE=0 occur at the end of the communication.
In controller mode, this bit must not be reset before the end of the communication.
1 5 1 4 1 3 1 21 1 1 0 9 8 76543210
Reserved
LAST DMAEN ITBUFEN ITEVTEN ITERREN
Reserved
FREQ[5:0]
rw rw rw rw rw rw rw rw rw rw rw
Bits 15:13 Reserved, must be kept at reset value
Bit 12 LAST: DMA last transfer
0: Next DMA EOT is not the last transfer
1: Next DMA EOT is the last transfer
Note: This bit is used in controller receiver mode  to permit the generation of a NACK on the
last received data.
Bit 11 DMAEN: DMA requests enable
0: DMA requests disabled
1: DMA request enabled when TxE=1 or RxNE =1
Bit 10 ITBUFEN: Buffer interrupt enable
0: TxE = 1 or RxNE = 1 does not generate any interrupt.
1: TxE = 1 or RxNE = 1 generates Event Interrupt (whatever the state of DMAEN)

Inter-integrated circuit (I2C) interface RM0090
858/1741 RM0090 Rev 22
Bit 9 ITEVTEN: Event interrupt enable
0: Event interrupt disabled
1: Event interrupt enabled
This interrupt is generated when:
– SB = 1 (Controller)
– ADDR = 1 (Controller/Target)
– ADD10= 1 (Controller)
– STOPF = 1 (Target)
– BTF = 1 with no TxE or RxNE event
– TxE event to 1 if ITBUFEN = 1
– RxNE event to 1if ITBUFEN = 1
Bit 8 ITERREN: Error interrupt enable
0: Error interrupt disabled
1: Error interrupt enabled
This interrupt is generated when:
–B E R R  =  1
–A R L O  =  1
–A F  =  1
–O V R  =  1
– PECERR = 1
– TIMEOUT = 1
– SMBALERT = 1
Bits 7:6 Reserved, must be kept at reset value
Bits 5:0 FREQ[5:0]: Peripheral clock frequency
The FREQ bits must be configured with the APB clock frequency value (I2C peripheral
connected to APB). The FREQ field is used by the peripheral to generate data setup and
hold times compliant with the I2C specifications. The minimum allowed frequency is 2 MHz,
the maximum frequency is limited by the maximum APB frequency and cannot exceed
50 MHz (peripheral intrinsic maximum limit).
0b000000: Not allowed
0b000001: Not allowed
0b000010: 2 MHz
...
0b110010: 50 MHz
Higher than 0b101010: Not allowed

RM0090 Rev 22 859/1741
RM0090 Inter-integrated circuit (I2C) interface
867
27.6.3 I 2C Own address register 1 (I2C_OAR1)
Address offset: 0x08
Reset value: 0x0000
27.6.4 I 2C Own address register 2 (I2C_OAR2)
Address offset: 0x0C
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9 8 7 654321 0
ADD
MODE Reserved
ADD[9:8] ADD[7:1] ADD0
rw rw rw rw rw rw rw rw rw rw rw
Bit 15 ADDMODE Addressing mode (target mode)
0: 7-bit target address (10-bit address not acknowledged)
1: 10-bit target address (7-bit address not acknowledged)
Bit 14 Should always be kept at 1 by software.
Bits 13:10 Reserved, must be kept at reset value
Bits 9:8 ADD[9:8]: Interface address
7-bit addressing mode: don’t care
10-bit addressing mode: bits9:8 of address
Bits 7:1 ADD[7:1]: Interface address
bits 7:1 of address
Bit 0 ADD0: Interface address
7-bit addressing mode: don’t care
10-bit addressing mode: bit 0 of address
1 5 1 4 1 3 1 2 1 1 1 0 9 87 654321 0
Reserved
ADD2[7:1] ENDUAL
rw rw rw rw rw rw rw rw
Bits 15:8 Reserved, must be kept at reset value
Bits 7:1 ADD2[7:1]: Interface address
bits 7:1 of address in dual addressing mode
Bit 0 ENDUAL: Dual addressing mode enable
0: Only OAR1 is recognized in 7-bit addressing mode
1: Both OAR1 and OAR2 are recognized in 7-bit addressing mode

Inter-integrated circuit (I2C) interface RM0090
860/1741 RM0090 Rev 22
27.6.5 I 2C Data register (I2C_DR)
Address offset: 0x10
Reset value: 0x0000
27.6.6 I 2C Status register 1 (I2C_SR1)
Address offset: 0x14
Reset value: 0x0000
1 5 1 4 1 3 1 2 1 1 1 0 9 87 654321 0
Reserved
DR[7:0]
rw rw rw rw rw rw rw rw
Bits 15:8 Reserved, must be kept at reset value
Bits 7:0 DR[7:0] 8-bit data register
Byte received or to be transmitted to the bus.
– Transmitter mode: Byte transmission starts automatically when a byte is written in the DR
register. A continuous transmit stream can be maintained if the next data to be transmitted is
put in DR once the transmission is started (TxE=1)
– Receiver mode: Received byte is copied into DR (RxNE=1). A continuous transmit stream
can be maintained if DR is read before the next data byte is received (RxNE=1).
Note: In target mode, the address is not copied into DR.
Write collision is not managed (DR can be written if TxE=0).
If an ARLO event occurs on ACK pulse, the received byte is not copied into DR and so
cannot be read.
1 5 1 4 1 3 1 2 1 1 1 0 9 87 654321 0
SMB
ALERT
TIME
OUT Res.
PEC
ERR OVR AF ARLO BERR TxE RxNE
Res.
STOPF ADD10 BTF ADDR SB
r c _ w 0 r c _ w 0 r c _ w 0 r c _ w 0 r c _ w 0 r c _ w 0 r c _ w 0 r r rrrr r
Bit 15 SMBALERT: SMBus alert
In SMBus host mode:
0: no SMBALERT
1: SMBALERT event occurred on pin
In SMBus target mode:
0: no SMBALERT response address header
1: SMBALERT response address header to SMBALERT LOW received
– Cleared by software writing 0, or by hardware when PE=0.

RM0090 Rev 22 861/1741
RM0090 Inter-integrated circuit (I2C) interface
867
Bit 14 TIMEOUT: Timeout or Tlow error
0: No timeout error
1: SCL remained LOW for 25 ms (Timeout)
or
Controller cumulative clock low extend time more than 10 ms (Tlow:mext)
or
Target cumulative clock low extend time more than 25 ms (Tlow:sext)
– When set in target mode: target resets the communication and lines are released by
hardware
– When set in controller mode: Stop condition sent by hardware
– Cleared by software writing 0, or by hardware when PE=0.
Note: This functionality is available only in SMBus mode.
Bit 13 Reserved, must be kept at reset value
Bit 12 PECERR: PEC Error in reception
0: no PEC error: receiver returns ACK after PEC reception (if ACK=1)
1: PEC error: receiver returns NACK after PEC reception (whatever ACK)
– Cleared by software writing 0, or by hardware when PE=0.
Note: When the received CRC is wrong, PECERR is not set in target mode if the PEC control
bit is not set before the end of the CRC reception. Nevertheless, reading the PEC value
determines whether the received CRC is right or wrong.
Bit 11 OVR: Overrun/Underrun
0: No overrun/underrun
1: Overrun or underrun
– Set by hardware in target mode when NOSTRETCH=1 and:
– In reception when a new byte is received (including ACK pulse) and the DR register has not
been read yet. New received byte is lost.
– In transmission when a new byte should be sent and the DR register has not been written
yet. The same byte is sent twice.
– Cleared by software writing 0, or by hardware when PE=0.
Note: If the DR write occurs very close to SCL rising edge, the sent data is unspecified and a
hold timing error occurs
Bit 10 AF: Acknowledge failure
0: No acknowledge failure
1: Acknowledge failure
– Set by hardware when no acknowledge is returned.
– Cleared by software writing 0, or by hardware when PE=0.
Bit 9 ARLO: Arbitration lost (controller mode)
0: No Arbitration Lost detected
1: Arbitration Lost detected
Set by hardware when the interface loses the arbitration of the bus to another controller
– Cleared by software writing 0, or by hardware when PE=0.
After an ARLO event the interface switches back automatically to Target mode (MSL=0).
Note: In SMBUS, the arbitration on the data in target mode occurs only during the data phase,
or the acknowledge transmission (not on the address acknowledge).

Inter-integrated circuit (I2C) interface RM0090
862/1741 RM0090 Rev 22
Bit 8 BERR: Bus error
0: No misplaced Start or Stop condition
1: Misplaced Start or Stop condition
– Set by hardware when the interface detects an SDA rising or falling edge while SCL is high,
occurring in a non-valid position during a byte transfer.
– Cleared by software writing 0, or by hardware when PE=0.
Bit 7 TxE: Data register empty (transmitters)
0: Data register not empty
1: Data register empty
– Set when DR is empty in transmission. TxE is not set during address phase.
– Cleared by software writing to the DR register or by hardware after a start or a stop condition
or when PE=0.
TxE is not set if either a NACK is received, or if next byte to be transmitted is PEC (PEC=1)
Note: TxE is not cleared by writing the first data being transmitted, or by writing data when
BTF is set, as in both cases the data register is still empty.
Bit 6 RxNE: Data register not empty (receivers)
0: Data register empty
1: Data register not empty
– Set when data register is not empty in receiver mode. RxNE is not set during address phase.
– Cleared by software reading or writing the DR register or by hardware when PE=0.
RxNE is not set in case of ARLO event.
Note: RxNE is not cleared by reading data when BTF is set, as the data register is still full.
Bit 5 Reserved, must be kept at reset value
Bit 4 STOPF: Stop detection (target mode)
0: No Stop condition detected
1: Stop condition detected
– Set by hardware when a Stop condition is detected on the bus by the target after an
acknowledge (if ACK=1).
– Cleared by software reading the SR1 register followed by a write in the CR1 register, or by
hardware when PE=0
Note: The STOPF bit is not set after a NACK reception.
It is recommended to perform the complete clearing sequence (READ SR1 then
WRITE CR1) after the STOPF is set. Refer to [Figure 242](../figures/figure_242.md).
Bit 3 ADD10: 10-bit header sent (Controller mode)
0: No ADD10 event occurred.
1: Controller has sent first address byte (header).
– Set by hardware when the controller has sent the first byte in 10-bit address mode.
– Cleared by software reading the SR1 register followed by a write in the DR register of the
second address byte, or by hardware when PE=0.
Note: ADD10 bit is not set after a NACK reception

RM0090 Rev 22 863/1741
RM0090 Inter-integrated circuit (I2C) interface
867
27.6.7 I 2C Status register 2 (I2C_SR2)
Address offset: 0x18
Reset value: 0x0000
Note: Reading I2C_SR2 after readi ng I2C_SR1 clears the ADDR flag, even if the ADDR flag was
set after reading I2C_SR1. Consequently, I2C_SR2 must be read only when ADDR is found
set in I2C_SR1 or when the STOPF bit is cleared.
Bit 2 BTF: Byte transfer finished
0: Data byte transfer not done
1: Data byte transfer succeeded
– Set by hardware when NOSTRETCH=0 and:
– In reception when a new byte is received (including ACK pulse) and DR has not been read
yet (RxNE=1).
– In transmission when a new byte should be sent and DR has not been written yet (TxE=1).
– Cleared by software by either a read or write in the DR register or by hardware after a start or
a stop condition in transmission or when PE=0.
Note: The BTF bit is not set after a NACK reception
The BTF bit is not set if next byte to be transmitted is the PEC (TRA=1 in I2C_SR2
register and PEC=1 in I2C_CR1 register)
Bit 1 ADDR: Address sent (controller mode)/matched (target mode)
This bit is cleared by software reading SR1 register followed reading SR2, or by hardware
when PE=0.
Address matched (Target)
0: Address mismatched or not received.
1: Received address matched.
– Set by hardware as soon as the received target address matched with the OAR registers
content or a general call or a SMBus Device Default Address or SMBus Host or SMBus Alert
is recognized. (when enabled depending on configuration).
Note: In target mode, it is recommended to pe rform the complete clearing sequence (READ
SR1 then READ SR2) after ADDR is set. Refer to [Figure 242](../figures/figure_242.md).
Address sent (Controller)
0: No end of address transmission
1: End of address transmission
– For 10-bit addressing, the bit is set after the ACK of the 2nd byte.
– For 7-bit addressing, the bit is set after the ACK of the byte.
Note: ADDR is not set after a NACK reception
Bit 0 SB: Start bit (Controller mode)
0: No Start condition
1: Start condition generated.
– Set when a Start condition generated.
– Cleared by software by reading the SR1 register followed by writing the DR register, or by
hardware when PE=0
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
PEC[7:0] DUALF SMB
HOST
SMBDE
FAULT
GEN
CALL Res.
TRA BUSY MSL
rrr rrrrr r r r r r r r

Inter-integrated circuit (I2C) interface RM0090
864/1741 RM0090 Rev 22
Note: Reading I2C_SR2 after readi ng I2C_SR1 clears the ADDR flag, even if the ADDR flag was
set after reading I2C_SR1. Consequently, I2C_SR2 must be read only when ADDR is found
set in I2C_SR1 or when the STOPF bit is cleared.
Bits 15:8 PEC[7:0] Packet error checking register
This register contains the internal PEC when ENPEC=1.
Bit 7 DUALF: Dual flag (Target mode)
0: Received address matched with OAR1
1: Received address matched with OAR2
– Cleared by hardware after a Stop condition or repeated Start condition, or when PE=0.
Bit 6 SMBHOST: SMBus host header (Target mode)
0: No SMBus Host address
1: SMBus Host address received when SMBTYPE=1 and ENARP=1.
– Cleared by hardware after a Stop condition or repeated Start condition, or when PE=0.
Bit 5 SMBDEFAULT: SMBus device default address (Target mode)
0: No SMBus Device Default address
1: SMBus Device Default address received when ENARP=1
– Cleared by hardware after a Stop condition or repeated Start condition, or when PE=0.
Bit 4 GENCALL: General call address (Target mode)
0: No General Call
1: General Call Address received when ENGC=1
– Cleared by hardware after a Stop condition or repeated Start condition, or when PE=0.
Bit 3 Reserved, must be kept at reset value
Bit 2 TRA: Transmitter/receiver
0: Data bytes received
1: Data bytes transmitted
This bit is set depending on the R/W bit of the address byte, at the end of total address
phase.
It is also cleared by hardware after detection of Stop condition (STOPF=1), repeated Start
condition, loss of bus arbitration (ARLO=1), or when PE=0.
Bit 1 BUSY: Bus busy
0: No communication on the bus
1: Communication ongoing on the bus
– Set by hardware on detection of SDA or SCL low
– cleared by hardware on detection of a Stop condition.
It indicates a communication in progress on the bus. This information is still updated when
the interface is disabled (PE=0).
Bit 0 MSL: Controller/target
0: Target mode
1: Controller mode
– Set by hardware as soon as the interface is in Controller mode (SB=1).
– Cleared by hardware after detecting a Stop condition on the bus or a loss of arbitration
(ARLO=1), or by hardware when PE=0.

RM0090 Rev 22 865/1741
RM0090 Inter-integrated circuit (I2C) interface
867
27.6.8 I 2C Clock control register (I2C_CCR)
Address offset: 0x1C
Reset value: 0x0000
Note: f PCLK1 must be at least 2 MHz to achieve Sm mode I²C frequencies. It must be at least 4
MHz to achieve Fm mode I²C frequencies. It must be a multiple of 10MHz to reach the
400 kHz maximum I²C Fm mode clock.
The CCR register must be configured only when the I2C is disabled (PE = 0).
1 5 1 4 1 3 1 2 1 1 1 0 9 87 654321 0
F/S DUTY
Reserved
CCR[11:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bit 15 F/S: I2C controller mode selection
0: Sm mode I2C
1: Fm mode I2C
Bit 14 DUTY: Fm mode duty cycle
0: Fm mode tlow/thigh = 2
1: Fm mode tlow/thigh = 16/9 (see CCR)
Bits 13:12 Reserved, must be kept at reset value
Bits 11:0 CCR[11:0]: Clock control register in Fm/Sm mode (Controller mode)
Controls the SCL clock in controller mode.
Sm mode or SMBus:
Thigh = CCR * TPCLK1
Tlow = CCR * TPCLK1
Fm mode:
If DUTY = 0:
Thigh = CCR * TPCLK1
Tlow = 2 * CCR * TPCLK1
If DUTY = 1:
Thigh = 9 * CCR * TPCLK1
Tlow = 16 * CCR * TPCLK1
For instance: in Sm mode, to generate a 100 kHz SCL frequency:
If FREQ = 08, TPCLK1 = 125 ns so CCR must be programmed with 0x28
(0x28 <=> 40d x 125 ns = 5000 ns.)
Note: The minimum allowed value is 0x04, except in FAST DUTY mode where the minimum
allowed value is 0x01
thigh = tr(SCL) + tw(SCLH).
tlow = tf(SCL) + tw(SCLL).
Where the I2C parameters below are part of the I2C standard specification.
- tr(SCL) = SCL clock rise time from 30% to 70%.
- tf(SCL) = SCL clock fall time from 70% to 30%.
- tw(SCLH) = SCL clock high time measure at 70%.
- tw(SCLL) = SCL clock low time measure at 30%.
I2C communication speed, fSCL ~ 1/(thigh + tlow). The real frequency may differ due to
the analog noise filter input delay.
The CCR register must be configured only when the I2C is disabled (PE = 0).

Inter-integrated circuit (I2C) interface RM0090
866/1741 RM0090 Rev 22
27.6.9 I 2C TRISE register (I2C_TRISE)
Address offset: 0x20
Reset value: 0x0002
27.6.10 I 2C FLTR register (I2C_FLTR)
Address offset: 0x24
Reset value: 0x0000
The I2C_FLTR is available on STM32F42xxx and STM32F43xxx only.
1 5 1 4 1 3 1 2 1 1 1 0 9 87 654321 0
Reserved
TRISE[5:0]
rw rw rw rw rw rw
Bits 15:6 Reserved, must be kept at reset value
Bits 5:0 TRISE[5:0]: Maximum rise time in Fm/Sm mode (Controller mode)
These bits should provide the maximum duration of the SCL feedback loop in controller
mode. The purpose is to keep a stable SCL frequency whatever the SCL rising edge
duration.
These bits must be programmed with the maximum SCL rise time given in the I2C bus
specification, incremented by 1.
For instance: in Sm mode, the maximum allowed SCL rise time is 1000 ns.
If, in the I2C_CR2 register, the value of FREQ[5:0] bits is equal to 0x08 and TPCLK1 = 125 ns
therefore the TRISE[5:0] bits must be programmed with 09h.
(1000 ns / 125 ns = 8 + 1)
The filter value can also be added to TRISE[5:0].
If the result is not an integer, TRISE[5:0] must be programmed with the integer part, in order
to respect the tHIGH parameter.
Note: TRISE[5:0] must be configured only when the I2C is disabled (PE = 0).
1 5 1 4 1 3 1 2 1 1 1 0 9 87 654321 0
Reserved
ANOFF DNF[3:0]
rw rw rw rw rw
Bits 15:5 Reserved, must be kept at reset value
Bit 4 ANOFF: Analog noise filter OFF
0: Analog noise filter enable
1: Analog noise filter disable
Note: ANOFF must be configured only when the I2C is disabled (PE = 0).
Bits 3:0 DNF[3:0]: Digital noise filter
These bits are used to configure the digital noise filter on SDA and SCL inputs. The digital filter
suppresses the spikes with a length of up to DNF[3:0] * TPCLK1.
0000: Digital noise filter disable
0001: Digital noise filter enabled and filtering capability up to 1* TPCLK1.
...
1111: Digital noise filter enabled and filtering capability up to 15* TPCLK1.
Note: DNF[3:0] must be configured only when the I2 C is disabled (PE = 0). If the analog filter
is also enabled, the digital filter is added to the analog filter.

RM0090 Rev 22 867/1741
RM0090 Inter-integrated circuit (I2C) interface
867
27.6.11 I 2C register map
The table below provides the I2C register map and reset values.
Refer to Section 2.3: Memory map for the register boundary addresses table.
[Table 125](../tables/table_125.md). I2C register map and reset values
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
0x00
I2C_CR1
Reserved
SWRST
Reserved
ALERT
PEC
POS
ACK
STOP
START
NOSTRETCH
ENGC
ENPEC
ENARP
SMBTYPE
Reserved
SMBUS
PE
R e s e t  v a l u e 0 0000 0 0 00000 00
0x04
I2C_CR2
Reserved
LAST
DMAEN
ITBUFEN
ITEVTEN
ITERREN
Reserved
FREQ[5:0]
R e s e t  v a l u e 000 0 0 000000
0x08
I2C_OAR1
Reserved
ADDMODE
Reserved
ADD[9:8] ADD[7:1]
ADD0
R e s e t  v a l u e 0 0 0 00000000
0x0C
I2C_OAR2
Reserved
ADD2[7:1]
ENDUAL
Reset value 00000000
0x10
I2C_DR
Reserved
DR[7:0]
Reset value 00000000
0x14
I2C_SR1
Reserved
SMBALERT
TIMEOUT
Reserved
PECERR
OVR
AF
ARLO
BERR
TxE
RxNE
Reserved
STOPF
ADD10
BTF
ADDR
SB
R e s e t  v a l u e 00 000 0 0 00 00000
0x18
I2C_SR2
Reserved
PEC[7:0]
DUALF
SMBHOST
SMBDEFAUL
GENCALL
Reserved
TRA
BUSY
MSL
R e s e t  v a l u e 000000 0 0 0000 000
0x1C
I2C_CCR
Reserved
F/S
DUTY
Reserved
CCR[11:0]
R e s e t  v a l u e 00 00 0 0 00000000
0x20
I2C_TRISE
Reserved
TRISE[5:0]
Reset value 000010
0x24
I2C_FLTR
Reserved
ANOFF
DNF[3:0]
Reset value 00000
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 238: Architectural Diagram](../figures/figure_238.md)
* [Figure 239: Architectural Diagram](../figures/figure_239.md)
* [Figure 240: Architectural Diagram](../figures/figure_240.md)
* [Figure 241: Architectural Diagram](../figures/figure_241.md)
* [Figure 242: Architectural Diagram](../figures/figure_242.md)
* [Figure 243: Architectural Diagram](../figures/figure_243.md)
* [Figure 244: Architectural Diagram](../figures/figure_244.md)
* [Figure 245: Architectural Diagram](../figures/figure_245.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 122: Configuration Matrix](../tables/table_122.md)
* [Table 123: Configuration Matrix](../tables/table_123.md)
* [Table 124: Configuration Matrix](../tables/table_124.md)
* [Table 125: Configuration Matrix](../tables/table_125.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)