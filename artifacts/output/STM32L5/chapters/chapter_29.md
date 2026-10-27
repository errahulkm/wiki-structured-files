# Chapter 29: AES hardware accelerator (AES)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 29: AES hardware accelerator (AES).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 953 - 1000
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 953/2187
RM0438 AES hardware  accelerator (AES)
1000
29 AES hardware accelerator (AES)
29.1 Introduction
The AES hardware accelerator (AES) encrypts or decrypts data, using an algorithm and
implementation fully compliant with the advanced encryption standard (AES) defined in
Federal information processing standards (FIPS) publication 197.
The peripheral supports CTR, GCM, GMAC, CCM, ECB, and CBC chaining modes for key
sizes of 128 or 256 bits.
AES is an AMBA AHB slave peripheral accessible through 32-bit single accesses only.
Other access types generate an AHB error, and other than 32-bit writes may corrupt the
register content.
The peripheral supports DMA single transfers for incoming and outgoing data (two DMA
channels required).
29.2 AES main features
• Compliance with NIST “Advanced encryption standard (AES), FIPS publication 197”
from November 2001
• 128-bit data block processing
• Support for cipher key lengths of 128-bit and 256-bit
• Encryption and decryption with multiple chaining modes:
– Electronic codebook (ECB) mode
– Cipher block chaining (CBC) mode
– Counter (CTR) mode
– Galois counter mode (GCM)
– Galois message authentication code (GMAC) mode
– Counter with CBC-MAC (CCM) mode
• 51 or 75 clock cycle latency in ECB mode for processing one 128-bit block of data with,
respectively, 128-bit or 256-bit key
• Integrated round key scheduler to compute the last round key for ECB/CBC decryption
• AMBA AHB slave peripheral, accessible through 32-bit word single accesses only
• 256-bit write-only register for storing the cryptographic key (eight 32-bit registers)
• 128-bit register for storing initialization vector (four 32-bit registers)
• 32-bit buffer for data input and output
• Automatic data flow control with support of single-transfer direct memory access (DMA)
using two channels (one for incoming data, one for processed data)
• Data-swapping logic to support 1-, 8-, 16- or 32-bit data
• Possibility for software to suspend a message if AES needs to process another
message with a higher priority, then resume the original message
29.3 AES implementation
The devices have one AES peripheral.

AES hardware accelerator (AES) RM0438
954/2187 RM0438 Rev 8
29.4 AES functi onal description
29.4.1 AES block diagram
[Figure 196](../figures/figure_196.md) shows the block diagram of AES.
[Figure 196](../figures/figure_196.md). AES block diagram
29.4.2 AES internal signals
[Table 226](../tables/table_226.md) describes the user relevant internal signals interfacing the AES peripheral.
29.4.3 AES cryptographic core
Overview
The AES cryptographic core consists of the following components:
• AES core algorithm (AEA)
• multiplier over a binary Galois field (GF2mul)
• key input
• initialization vector (IV) input
• chaining algorithm logic (XOR, feedback/counter, mask)
MSv42154V1
aes_hclk
Banked registers
DOUT
KEY
IVI
DIN
AES
key
control
status
IV, counter
data in
data out
aes_it
32-bit
AHB bus
aes_in_dma
AES_CR
AES_KEYRx
AES_SR
AES_IVRx
AES_DINR
AES_DOUTR
AES
Core
(AEA)
swap
AHB
interface
IRQ
interface
Control Logic
DMA
interfaceaes_out_dma
32-bit
access
Save / RestoreAES_SUSPRx
[Table 226](../tables/table_226.md). AES internal input/output signals
Signal name Signal type Description
aes_hclk Input AHB bus clock
aes_it Output AES interrupt request
aes_in_dma Input/Output Input DMA single request/acknowledge
aes_out_dma Input/Output Output DMA single request/acknowledge

RM0438 Rev 8 955/2187
RM0438 AES hardware  accelerator (AES)
1000
The AES core works on 128-bit data blocks (four words) with 128-bit or 256-bit key length.
Depending on the chaining mode, the AES requires zero or one 128-bit initialization vector
IV.
The AES features the following modes of operation:
• Mode 1:
Plaintext encryption using a key stored in the AES_KEYRx registers
• Mode 2:
ECB or CBC decryption key preparation. It must be used prior to selecting Mode 3 with
ECB or CBC chaining modes. The key prepared for decryption is stored automatically
in the AES_KEYRx registers. Now the AES peripheral is ready to switch to Mode 3 for
executing data decryption.
• Mode 3:
Ciphertext decryption using a key stored in the AES_KEYRx registers. When ECB and
CBC chaining modes are selected, the key must be prepared beforehand, through
Mode 2.
Note: Mode 2 is only used when performing ECB and CBC decryption.
The operating mode is selected by programming the MODE[1:0] bitfield of the AES_CR
register. It may be done only when the AES peripheral is disabled.
Typical data processing
Typical usage of the AES is described in Section 29.4.4: AES procedure to perform a cipher
operation.
Note: The outputs of the intermediate AEA stages  are never revealed outside the cryptographic
boundary, with the exclusion of the IVI bitfield.
Chaining modes
The following chaining modes are supported by AES, selected through the CHMOD[2:0]
bitfield of the AES_CR register:
• Electronic code book (ECB)
• Cipher block chaining (CBC)
• Counter (CTR)
• Galois counter mode (GCM)
• Galois message authentication code (GMAC)
• Counter with CBC-MAC (CCM)
Note: The chaining mode may be  changed only when AES is disabled (bit EN of the AES_CR
register cleared).
Principle of each AES chaining mode is provided in the following subsections.
Detailed information is in dedicated sections, starting from Section 29.4.8: AES basic
chaining modes (ECB, CBC).

AES hardware accelerator (AES) RM0438
956/2187 RM0438 Rev 8
Electronic codebook (ECB) mode
[Figure 197](../figures/figure_197.md). ECB encryption and decryption principle
ECB is the simplest mode of operation. There are no chaining operations, and no special
initialization stage. The message is divided into blocks and each block is encrypted or
decrypted separately.
Note: For decryption, a special key scheduling is required before processing the first block.
MSv42140V1
Encryption
Plaintext block 1 Plaintext block 2 Plaintext block 3
Ciphertext block 1 Ciphertext block 2 Ciphertext block 3
Encrypt Encrypt Encrypt
Decryption
key key key
Plaintext block 1 Plaintext block 2 Plaintext block 3
Ciphertext block 1 Ciphertext block 2 Ciphertext block 3
Decrypt Decrypt Decryptkey key key
input
output
key
scheduling
Legend

RM0438 Rev 8 957/2187
RM0438 AES hardware  accelerator (AES)
1000
Cipher block chaining (CBC) mode
[Figure 198](../figures/figure_198.md). CBC encryption and decryption principle
In CBC mode the output of each block chains with the input of the following block. To make
each message unique, an initialization vector is used during the first block processing.
Note: For decryption, a special key scheduling is required before processing the first block.
MSv42141V1
Encryption
Plaintext block 1 Plaintext block 2 Plaintext block 3
Ciphertext block 1 Ciphertext block 2 Ciphertext block 3
Encrypt Encrypt Encrypt
Decryption
key key key
Plaintext block 1 Plaintext block 2 Plaintext block 3
Ciphertext block 1 Ciphertext block 2 Ciphertext block 3
Decrypt Decrypt Decryptkey key key
input
output
key
scheduling
Legend
initialization
vector
initialization
vector

AES hardware accelerator (AES) RM0438
958/2187 RM0438 Rev 8
Counter (CTR) mode
[Figure 199](../figures/figure_199.md). CTR encryption and decryption principle
The CTR mode uses the AES core to generate a key stream. The keys are then XOR-ed
with the plaintext to obtain the ciphertext as specified in NIST Special Publication 800-38A,
Recommendation for Block Cipher Modes of Operation.
Note: Unlike with ECB and CBC modes, no key scheduling is required for the CTR decryption,
since in this chaining scheme the AES core is always used in encryption mode for producing
the key stream, or counter blocks.
MSv42142V1
Encryption
Plaintext block 1
Ciphertext block 1 Ciphertext block 2 Ciphertext block 3
Encrypt Encrypt Encrypt
Decryption
Ciphertext block 1 Ciphertext block 2 Ciphertext block 3
Decrypt Decrypt Decrypt
input
output
Legend
key key key
key key key
Plaintext block 2 Plaintext block 3
Counter Counter Counter+1 +1
Plaintext block 1 Plaintext block 2 Plaintext block 3
Counter Counter Counter+1 +1
XOR
value value + 1 value + 2
value value + 1 value + 2

RM0438 Rev 8 959/2187
RM0438 AES hardware  accelerator (AES)
1000
Galois/counter mode (GCM)
[Figure 200](../figures/figure_200.md). GCM encryption and authentication principle
In Galois/counter mode (GCM), the plaintext message is encrypted while a message
authentication code (MAC) is computed in parallel, thus generating the corresponding
ciphertext and its MAC (also known as authentication tag). It is defined in NIST Special
Publication 800-38D, Recommendation for Block Cipher Modes of Operation -
Galois/Counter Mode (GCM) and GMAC.
GCM mode is based on AES in counter mode for confidentiality. It uses a multiplier over a
fixed finite field for computing the message authentication code. It requires an initial value
and a particular 128-bit block at the end of the message.
Galois message authentication code (GMAC) principle
[Figure 201](../figures/figure_201.md). GMAC authentication principle
Galois message authentication code (GMAC) allows authenticating a message and
generating the corresponding message authentication code (MAC). It is defined in NIST
Special Publication 800-38D, Recommendation for Block Cipher Modes of Operation -
Galois/Counter Mode (GCM) and GMAC.
MSv42143V1
Plaintext block 1
Ciphertext block 1 Ciphertext block 2 Ciphertext block 3
Encrypt Encrypt Encryptkey key key
Plaintext block 2 Plaintext block 3
Counter Counter Counter+1 +1
GF2mul GF2mul GF2mul
Final TAG
Init
(Encrypt)
key
Initialization
vector
H
input
output
Legend
XOR
value value + 1 value + 2
MSv42144V1
Plaintext block 1 Plaintext block 2 Plaintext block 3
GF2mul GF2mul GF2mul
Final TAG
Init
(Encrypt)
key
Initialization
vector
H
input
output
Legend
XOR

AES hardware accelerator (AES) RM0438
960/2187 RM0438 Rev 8
GMAC is similar to GCM, except that it is applied on a message composed only by plaintext
authenticated data (that is, only header, no payload).
Counter with CBC-MAC (CCM) principle
[Figure 202](../figures/figure_202.md). CCM encryption and authentication principle
In Counter with cipher block chaining-message authentication code (CCM) mode, the
plaintext message is encrypted while a message authentication code (MAC) is computed in
parallel, thus generating the corresponding ciphertext and the corresponding MAC (also
known as tag). It is described by NIST in Special Publication 800-38C, Recommendation for
Block Cipher Modes of Operation - The CCM Mode for Authentication and Confidentiality.
CCM mode is based on AES in counter mode for confidentiality and it uses CBC for
computing the message authentication code. It requires an initial value.
Like GCM, the CCM chaining mode can be applied on a message composed only by
plaintext authenticated data (that is, only header, no payload). Note that this way of using
CCM is not called CMAC (it is not similar to GCM/GMAC), and its use is not recommended
by NIST.
29.4.4 AES procedure to perform a cipher operation
Introduction
A typical cipher operation is explained below. Detailed information is provided in sections
starting from Section 29.4.8: AES basic chaining modes (ECB, CBC).
MSv42145V1
Plaintext block 1
Ciphertext block 1 Ciphertext block 2 Ciphertext block 3
Encrypt Encrypt Encryptkey key key
Plaintext block 2 Plaintext block 3
Count 1 Count 2 Count 3+1 +1
Encrypt Encrypt Encrypt
Final TAG
Init
(Encrypt)
key
Initialization
vector
input
output
Legend
XOR
B0
key

RM0438 Rev 8 961/2187
RM0438 AES hardware  accelerator (AES)
1000
Initialization of AES
To initialize AES, first disable it by clearing the EN bit of the AES_CR register. Then perform
the following steps in any order:
• Configure the AES mode, by programming the MODE[1:0] bitfield of the AES_CR
register.
– For encryption, select Mode 1 (MODE[1:0] = 00).
– For decryption, select Mode 3 (MODE[1:0] = 10), unless ECB or CBC chaining
modes are used. In this latter case, perform an initial key derivation of the
encryption key, as described in Section 29.4.5: AES decryption round key
preparation.
• Select the chaining mode, by programming the CHMOD[2:0] bitfield of the AES_CR
register.
• Configure the data type (1-, 8-, 16- or 32-bit), with the DATATYPE[1:0] bitfield in the
AES_CR register.
• When it is required (for example in CBC or CTR chaining modes), write the initialization
vector into the AES_IVRx registers.
• Configure the key size (128-bit or 256-bit), with the KEYSIZE bitfield of the AES_CR
register.
• Write a symmetric key into the AES_KEYRx registers (4 or 8 registers depending on
the key size).
Data append
This section describes different ways of appending data for processing, where the size of
data to process is not a multiple of 128 bits.
For ECB or CBC mode, refer to Section 29.4.6: AES ciphertext stealing and data padding.
The last block management in these cases is more complex than in the sequence described
in this section.
Data append through polling
This method uses flag polling to control the data append through the following sequence:
1. Enable the AES peripheral by setting  the EN bit of the AES_CR register.
2. Repeat the following sub-sequence un til the payload is entirely processed:
a) Write four input data words into the AES_DINR register.
b) Wait until the status flag CCF is set in  the AES_SR, then read the four data words
from the AES_DOUTR register.
c) Clear the CCF flag, by setting the CCFC bit of the AES_CR register.
d) If the data block just processed is th e second-last block of the message and the
significant data in the last block to process is inferior to 128 bits, pad the
remainder of the last block with zeros and, in case of GCM payload encryption or
CCM payload decryption, specify the number of non-valid bytes, using the NPBLB
bitfield of the AES_CR register, for AES to compute a correct tag;.
3. As it is the last block, discard the data th at is not part of the data, then disable the AES
peripheral by clearing the EN bit of the AES_CR register.
Note: Up to three wait cycles are automatically inserted between two consecutive writes to the
AES_DINR register, to allow sending the key to the AES processor.
NPBLB bits are not used in header phase of GCM, GMAC and CCM chaining modes.

AES hardware accelerator (AES) RM0438
962/2187 RM0438 Rev 8
Data append using interrupt
The method uses interrupt from the AES peripheral to control the data append, through the
following sequence:
1. Enable interrupts from AES by setting the CCFIE bit of the AES_CR register.
2. Enable the AES peripheral by setti ng the EN bit of the AES_CR register.
3. Write first four input data words into the AES_DINR register.
4. Handle the data in the AES interrupt service routine, upon interrupt:
a) Read four output data words from the AES_DOUTR register.
b) Clear the CCF flag and thus the pending interrupt, by setting the CCFC bit of the
AES_CR register.
c) If the data block just processed is th e second-last block of an message and the
significant data in the last block to process is inferior to 128 bits, pad the
remainder of the last block with zeros and, in case of GCM payload encryption or
CCM payload decryption, specify the number of non-valid bytes, using the NPBLB
bitfield of the AES_CR register, for AES to compute a correct tag;. Then proceed
with point 4e).
d) If the data block just pr ocessed is the last block of the message, discard the data
that is not part of the data, then disable the AES peripheral by clearing the EN bit
of the AES_CR register and quit the interrupt service routine.
e) Write next four input data words into  the AES_DINR register and quit the interrupt
service routine.
Note: AES is tolerant of delays between consecutive read or write operations, which allows, for
example, an interrupt from another peripheral to be served between two AES computations.
NPBLB bits are not used in header phase of GCM, GMAC and CCM chaining modes.
Data append using DMA
With this method, all the transfers and processing are managed by DMA and AES. To use
the method, proceed as follows:
1. Prepare the last four-w ord data block (if the data to process does not fill it completely),
by padding the remainder of the block with zeros.
2. Configure the DMA controller so as to transfer the data to process from the memory to
the AES peripheral input and the processed data from the AES peripheral output to the
memory, as described in Section 29.4.16: AES DMA interface. Configure the DMA
controller so as to generate an interrupt on transfer completion. In case of GCM
payload encryption or CCM payload decryption, DMA transfer must not include the
last four-word block if padded with zeros. The sequence described in Data append
through polling must be used instead for this last block, because NPBLB bits must be
setup before processing the block, for AES to compute a correct tag.
3. Enable the AES peripheral by setti ng the EN bit of the AES_CR register
4. Enable DMA requests by setting the DM AINEN and DMAOUTEN bits of the AES_CR
register.
5. Upon DMA interrupt indicating the transfer completion, get the AES-processed data
from the memory.
Note: The CCF flag has no use with this met hod, because the reading of the AES_DOUTR
register is managed by DMA automatically, without any software action, at the end of the
computation phase.
NPBLB bits are not used in header phase of GCM, GMAC, and CCM chaining modes.

RM0438 Rev 8 963/2187
RM0438 AES hardware  accelerator (AES)
1000
29.4.5 AES decryption round key preparation
Internal key schedule is used to generate AES round keys. In AES encryption, the round 0
key is the one stored in the key registers. AES decryption must start using the last round
key. As the encryption key is stored in memory, a special key scheduling must be performed
to obtain the decryption key. This key scheduling is only required for AES decryption in ECB
and CBC modes.
Recommended method is to select the Mode 2 by setting to 01 the MODE[1:0] bitfield of the
AES_CR (key process only), then proceed with the decryption by setting MODE[1:0] to 10
(Mode 3, decryption only). Mode 2 usage is described below:
1. Disable the AES peripheral by clearing the EN bit of the AES_CR register.
2. Select Mode 2 by setting to 01 th e MODE[1:0] bitfield of the AES_CR. The
CHMOD[2:0] bitfield is not significant in this case because this key derivation mode is
independent of the chaining algorithm selected.
3. Set key length to 128 or 256 bits , via KEYSIZE bit of AES_CR register.
4. Write the AES_KEYRx re gisters (128 or 256 bits) with encryption key. Writes to the
AES_IVRx registers have no effect.
5. Enable the AES peripheral, by setting the EN bit of the AES_CR register.
6. Wait until the CCF flag is set in the AES_SR register.
7. Clear the CCF flag. Derived key is available in AES core, ready to use for decryption.
Note: The AES is disabled by hardware wh en the derivation key is available.
To restart a derivation key computation, repeat steps 4, 5, 6, and 7.
Note: The operation of the key preparation lasts 59 or 82 clock cycles, depending on the key size
(128- or 256-bit).
29.4.6 AES ciphertext stealing and data padding
When using AES in ECB or CBC modes to manage messages the size of which is not a
multiple of the block size (128 bits), ciphertext stealing techniques are used, such as those
described in NIST Special Publication 800-38A, Recommendation for Block Cipher Modes
of Operation: Three Variants of Ciphertext Stealing for CBC Mode. Since the AES peripheral
does not support such techniques, the application must complete the last block of input data
using data from the second last block.
Note: Ciphertext stealing techniques are not documented in this reference manual.
Similarly, when AES is used in other modes than ECB or CBC, an incomplete input data
block (that is, block with input data shorter than 128 bits) must be padded with zeros prior to
encryption (that is, extra bits must be appended to the trailing end of the data string). After
decryption, the extra bits must be discarded. As AES does not implement automatic data
padding operation to the last block, the application must follow the recommendation given
in Section 29.4.4: AES procedure to perform a cipher operation to manage messages the
size of which is not a multiple of 128 bits.
Note: Padding data are swapped in a similar way as normal data, according to the
DATATYPE[1:0] field of the AES_CR register (see Section 29.4.13: AES data registers and
data swapping for details).

AES hardware accelerator (AES) RM0438
964/2187 RM0438 Rev 8
29.4.7 AES task suspend and resume
A message can be suspended if another message with a higher priority must be processed.
When this highest priority message is sent, the suspended message can resume in both
encryption or decryption mode.
Suspend/resume operations do not break the chaining operation and the message
processing can resume as soon as AES is enabled again to receive the next data block.
[Figure 203](../figures/figure_203.md) gives an example of suspend/resume operation: Message 1 is suspended in
order to send a shorter and higher-priority Message 2.
[Figure 203](../figures/figure_203.md). Example of suspend mode management
A detailed description of suspend/resume operations is in the sections dedicated to each
AES mode.
29.4.8 AES basic chai ning modes (ECB, CBC)
Overview
This section gives a brief explanation of the four basic operation modes provided by the
AES core: ECB encryption, ECB decryption, CBC encryption and CBC decryption. For
detailed information, refer to the FIPS publication 197 from November 26, 2001.
MSv42148V1
128-bit block 1
Message 1
128-bit block 2
128-bit block 4
128-bit block 5
128-bit block 6
...
AES suspend
sequence
AES resume
sequence
128-bit block 1
128-bit block 2
Message 2
128-bit block 3
New higher-priority
message 2 to be
processed

RM0438 Rev 8 965/2187
RM0438 AES hardware  accelerator (AES)
1000
[Figure 204](../figures/figure_204.md) illustrates the electronic codebook (ECB) encryption.
[Figure 204](../figures/figure_204.md). ECB encryption
In ECB encrypt mode, the 128-bit plaintext input data block Px in the AES_DINR register
first goes through bit/byte/half-word swapping. The swap result Ix is processed with the AES
core set in encrypt mode, using a 128- or 256-bit key. The encryption result Ox goes through
bit/byte/half-word swapping, then is stored in the AES_DOUTR register as 128-bit ciphertext
output data block Cx. The ECB encryption continues in this way until the last complete
plaintext block is encrypted.
[Figure 205](../figures/figure_205.md) illustrates the electronic codebook (ECB) decryption.
[Figure 205](../figures/figure_205.md). ECB decryption
To perform an AES decryption in the ECB mode, the secret key has to be prepared by
collecting the last-round encryption key (which requires to first execute the complete key
schedule for encryption), and using it as the first-round key for the decryption of the
ciphertext. This preparation is supported by the AES core.
In ECB decrypt mode, the 128-bit ciphertext input data block C1 in the AES_DINR register
first goes through bit/byte/half-word swapping. The keying sequence is reversed compared
to that of the ECB encryption. The swap result I1 is processed with the AES core set in
decrypt mode, using the formerly prepared decryption key. The decryption result goes
through bit/byte/half-word swapping, then is stored in the AES_DOUTR register as 128-bit
plaintext output data block P1. The ECB decryption continues in this way until the last
complete ciphertext block is decrypted.
MSv19105V2
Encrypt
AES_KEYRx (KEY)
AES_DINR (plaintext P1)
AES_DOUTR (ciphertext C1)
Swap
managementDATATYPE[1:0]
DATATYPE[1:0] Swap
management
Encrypt
AES_KEYRx (KEY)
AES_DINR (plaintext P2)
AES_DOUTR (ciphertext C2)
Swap
managementDATATYPE[1:0]
DATATYPE[1:0] Swap
management
input
output
Legend
I1 I2
O1 O2
Block 1 Block 2
AES core
MSv19106V2
Decrypt
AES_KEYRx (KEY)
AES_DINR (ciphertext C1)
AES_DOUTR (plaintext P1)
Swap
managementDATATYPE[1:0]
DATATYPE[1:0] Swap
management
Decrypt
AES_KEYRx (KEY)
AES_DINR (ciphertext C2)
AES_DOUTR (plaintext P2)
Swap
managementDATATYPE[1:0]
DATATYPE[1:0] Swap
management
input
output
Legend
I1 I2
O1 O2
Block 1 Block 2

AES hardware accelerator (AES) RM0438
966/2187 RM0438 Rev 8
[Figure 206](../figures/figure_206.md) illustrates the cipher block chaining (CBC) encryption.
[Figure 206](../figures/figure_206.md). CBC encryption
In CBC encrypt mode, the first plaintext input block, after bit/byte/half-word swapping (P1’),
is XOR-ed with a 128-bit IVI bitfield (initialization vector and counter), producing the I1 input
data for encrypt with the AES core, using a 128- or 256-bit key. The resulting 128-bit output
block O1, after swapping operation, is used as ciphertext C1. The O1 data is then XOR-ed
with the second-block plaintext data P2’ to produce the I2 input data for the AES core to
produce the second block of ciphertext data. The chaining of data blocks continues in this
way until the last plaintext block in the message is encrypted.
If the message size is not a multiple of 128 bits, the final partial data block is encrypted in
the way explained in Section 29.4.6: AES ciphertext stealing and data padding.
[Figure 207](../figures/figure_207.md) illustrates the cipher block chaining (CBC) decryption.
[Figure 207](../figures/figure_207.md). CBC decryption
In CBC decrypt mode, like in ECB decrypt mode, the secret key must be prepared to
perform an AES decryption.
After the key preparation process, the decryption goes as follows: the first 128-bit ciphertext
block (after the swap operation) is used directly as the AES core input block I1 for decrypt
operation, using the 128-bit or 256-bit key. Its output O1 is XOR-ed with the 128-bit IVI field
(that must be identical to that used during encryption) to produce the first plaintext block P1.
MSv19107V2
Block cipher
encryption
AES_KEYRx (KEY)
AES_DINR (plaintext P1)
AES_DOUTR (ciphertext C1)
Swap
managementDATATYPE[1:0]
DATATYPE[1:0] Swap
management
Block cipher
encryption
AES_KEYRx (KEY)
AES_DINR (plaintext P2)
AES_DOUTR (ciphertext C2)
Swap
managementDATATYPE[1:0]
DATATYPE[1:0] Swap
management
AES_IVRx (init. vector)
input
output
Legend
XOR
I1 I2
O1 O2
Block 1 Block 2
IVI P1' P2'
MSv19104V2
Decrypt
AES_KEYRx (KEY)
AES_DINR (ciphertext C1)
AES_DOUTR (plaintext P1)
Swap
managementDATATYPE[1:0]
DATATYPE[1:0] Swap
management
Decrypt
AES_KEYRx (KEY)
AES_DINR (ciphertext C2)
AES_DOUTR (plaintext P2)
Swap
managementDATATYPE[1:0]
DATATYPE[1:0] Swap
management
AES_IVRx (IV)
input
output
Legend
XOR
I1 I2
O1 O2
Block 1 Block 2
IVI
P1' P2'

RM0438 Rev 8 967/2187
RM0438 AES hardware  accelerator (AES)
1000
The second ciphertext block is processed in the same way as the first block, except that the
I1 data from the first block is used in place of the initialization vector.
The decryption continues in this way until the last complete ciphertext block is decrypted.
If the message size is not a multiple of 128 bits, the final partial data block is decrypted in
the way explained in Section 29.4.6: AES ciphertext stealing and data padding.
For more information on data swapping, refer to Section 29.4.13: AES data registers and
data swapping.
ECB/CBC encryption sequence
The sequence of events to perform an ECB/CBC encryption (more detail in Section 29.4.4):
1. Disable the AES peripheral by clearing the EN bit of the AES_CR register.
2. Select the Mode 1 by setting to 00 the MODE[1:0] bitfield of the AES_CR register and
select ECB or CBC chaining mode by setting the CHMOD[2:0] bitfield of the AES_CR
register to 000 or 001, respectively. Data type can also be defined, using
DATATYPE[1:0] bitfield.
3. Select 128- or 256-bit ke y length through the KEYSIZE bit of the AES_CR register.
4. Write the AES_KEYRx regist ers (128 or 256 bits) with encryption key. Fill the
AES_IVRx registers with the initialization vector data if CBC mode has been selected.
5. Enable the AES peripheral by setti ng the EN bit of the AES_CR register.
6. Write the AES_DINR register four times to input the plaintext (MSB first), as shown in
[Figure 208](../figures/figure_208.md).
7. Wait until the CCF flag is set in the AES_SR register.
8. Read the AES_DOUTR register four times to get the ciphertext (MSB first) as shown in
[Figure 208](../figures/figure_208.md). Then clear the CCF flag by setting the CCFC bit of the AES_CR register.
9. Repeat steps 6-7-8 to process all the blocks with the same encryption key.
[Figure 208](../figures/figure_208.md). ECB/CBC encryption (Mode 1)
ECB/CBC decryption sequence
The sequence of events to perform an AES ECB/CBC decryption is as follows (More detail
in Section 29.4.4).
1. Follow the steps described in Section 29.4.5: AES decryption round key preparation, in
order to prepare the decryption key in AES core.
2. Select the Mode 3 by setting to 10 the MODE[1:0] bitfield of the AES_CR register and
select ECB or CBC chaining mode by setting the CHMOD[2:0] bitfield of the AES_CR
MS18936V3
WR
PT3
WR
PT2
WR
PT1
WR
PT0 Wait until flag CCF = 1 RD
CT3
RD
CT2
RD
CT1
RD
CT0
Input phase
4 write operations into
AES_DINR[31:0]
Computation phase Output phase
4 read operations of
AES_DOUTR[31:0]
PT = plaintext = 4 words (PT3, … , PT0)
CT = ciphertext = 4 words (CT3, … , CT0)
MSB LSB MSB LSB

AES hardware accelerator (AES) RM0438
968/2187 RM0438 Rev 8
register to 000 or 001, respectively. Data type can also be defined, using
DATATYPE[1:0] bitfield. KEYSIZE bitfield must be kept as-is.
3. Write the AES_IVRx registers with the initialization vector (required in CBC mode only).
4. Enable AES by setting the EN bit of the AES_CR register.
5. Write the AES_DINR register four times to in put the cipher text (MSB first), as shown in
[Figure 209](../figures/figure_209.md).
6. Wait until the CCF flag is set in the AES_SR register.
7. Read the AES_DOUTR re gister four times to get the plain text (MSB first), as shown in
[Figure 209](../figures/figure_209.md). Then clear the CCF flag by setting the CCFC bit of the AES_CR register.
8. Repeat steps 5-6-7 to process all the blocks encrypted with the same key.
[Figure 209](../figures/figure_209.md). ECB/CBC decryption (Mode 3)
Suspend/resume operations in ECB/CBC modes
To suspend the processing of a message, proceed as follows:
1. If DMA is used, stop the AES DMA transfers to the IN FIFO by clearing the DMAINEN
bit of the AES_CR register.
2. If DMA is not us ed, read four times the AES_DOUTR register to save the last
processed block. If DMA is used, wait until the CCF flag is set in the AES_SR register
then stop the DMA transfers from the OUT FIFO by clearing the DMAOUTEN bit of the
AES_CR register.
3. If DMA is not used, poll the CCF flag of  the AES_SR register until it becomes 1
(computation completed).
4. Clear the CCF flag by setting t he CCFC bit of the AES_CR register.
5. Save initialization vector registers (only required in CBC mode as AES_IVRx registers
are altered during the data processing).
6. Disable the AES per ipheral by clearing the bit EN of the AES_CR register.
7. Save the AES_CR register and clear the key registers if they are not needed, to
process the higher priority message.
8. If DMA is used, save the DMA controller stat us (pointers for IN and OUT data transfers,
number of remaining bytes, and so on).
MS18938V3
WR
CT3
WR
CT2
WR
CT1
WR
CT0 Wait until flag CCF = 1 RD
PT3
RD
PT2
RD
PT1
RD
PT0
Input phase
4 write operations into
AES_DINR[31:0]
Computation phase Output phase
4 read operations from
AES_DOUTR[31:0]
PT = plaintext = 4 words (PT3, … , PT0)
CT = ciphertext = 4 words (CT3, … , CT0)
MSB LSB MSB LSB

RM0438 Rev 8 969/2187
RM0438 AES hardware  accelerator (AES)
1000
To resume the processing of a message, proceed as follows:
1. If DMA is used, configure the DMA controller so  as to complete the rest of the FIFO IN
and FIFO OUT transfers.
2. Disable the AES per ipheral by clearing the EN bit of the AES_CR register.
3. Restore AES_CR regi ster (with correct KEYSIZE) then restore AES_KEYRx registers.
4. Prepare the decryption key as described in Section 29.4.5: AES decryption round key
preparation (only required for ECB or CBC decryption).
5. Restore AES_IVRx register s using the saved configuration (only required in CBC
mode).
6. Enable the AES peripheral by setti ng the EN bit of the AES_CR register.
7. If DMA is used, enable AES DMA transfers by setting the DMAINEN and DMAOUTEN
bits of the AES_CR register.
29.4.9 AES counter (CTR) mode
Overview
The counter mode (CTR) uses AES as a key-stream generator. The generated keys are
then XOR-ed with the plaintext to obtain the ciphertext.
CTR chaining is defined in NIST Special Publication 800-38A, Recommendation for Block
Cipher Modes of Operation. A typical message construction in CTR mode is given in
[Figure 210](../figures/figure_210.md).
[Figure 210](../figures/figure_210.md). Message construction in CTR mode
The structure of this message is:
• A 16-byte initial counter block (ICB), composed of two distinct fields:
– Initialization vector (IV): a 96-bit value that must be unique for each encryption
cycle with a given key.
– Counter: a 32-bit big-endian integer that is incremented each time a block
processing is completed. The initial value of the counter must be set to 1.
• The plaintext P is encrypted as ciphertext C, with a known length. This length can be
non-multiple of 16 bytes, in which case a plaintext padding is required.
MSv42156V1
16-byte boundaries
ICB Ciphertext (C) 0
4-byte boundaries
CounterInitialization vector (IV)
decrypt
Plaintext (P)
Zero
padding

AES hardware accelerator (AES) RM0438
970/2187 RM0438 Rev 8
CTR encryption and decryption
[Figure 211](../figures/figure_211.md) and [Figure 212](../figures/figure_212.md) describe the CTR encryption and decryption process,
respectively, as implemented in the AES peripheral. The CTR mode is selected by writing
010 to the CHMOD[2:0] bitfield of AES_CR register.
[Figure 211](../figures/figure_211.md). CTR encryption
[Figure 212](../figures/figure_212.md). CTR decryption
In CTR mode, the cryptographic core output (also called keystream) Ox is XOR-ed with
relevant input block (Px' for encryption, Cx' for decryption), to produce the correct output
block (Cx' for encryption, Px' for decryption). Initialization vectors in AES must be initialized
as shown in [Table 227](../tables/table_227.md).
[Table 227](../tables/table_227.md). CTR mode initialization vector definition
AES_IVR3[31:0] AES_IVR2[31:0] AES_IVR1[31:0] AES_IVR0[31:0]
IVI[127:96] IVI[ 95:64] IVI[63:32] IVI[31:0}
32-bit counter = 0x0001
MSv19102V3
Encrypt
AES_KEYRx (KEY)
AES_DINR (plaintext P1)
AES_DOUTR (ciphertext C1)
DATATYPE[1:0] Swap
managementinput
output
Legend
XOR
Swap
management
DATATYPE[1:0]
Encrypt
AES_KEYRx (KEY)
AES_DOUTR (ciphertext C2)
DATATYPE[1:0] Swap
management
Swap
management
DATATYPE[1:0]
Counter
increment (+1)
AES_DINR (plaintext P2)
I1 I2
O1 O2
Block 1 Block 2
P1' P2'
C1' C2'
AES_IVRx
Nonce + 32-bit counter (+1)
AES_IVRx
Nonce + 32-bit counter
MSv18942V2
Encrypt
AES_KEYRx (KEY)
AES_DINR (ciphertext C1)
AES_DOUTR (plaintext P1)
DATATYPE[1:0] Swap
management
AES_IVRx
Nonce + 32-bit counter
input
output
Legend
XOR
Swap
management
DATATYPE[1:0]
Encrypt
AES_KEYRx (KEY)
AES_DOUTR (plaintext P2)
DATATYPE[1:0] Swap
management
AES_IVRx
Nonce + 32-bit counter (+1)
Swap
management
DATATYPE[1:0]
Counter
increment (+1)
AES_DINR (ciphertext C2)
I1 I2
O1 O2
Block 1 Block 2
C1' C2'
P1' P2'

RM0438 Rev 8 971/2187
RM0438 AES hardware  accelerator (AES)
1000
Unlike in CBC mode that uses the AES_IVRx registers only once when processing the first
data block, in CTR mode AES_IVRx registers are used for processing each data block, and
the AES peripheral increments the counter bits of the initialization vector (leaving the nonce
bits unchanged).
CTR decryption does not differ from CTR encryption, since the core always encrypts the
current counter block to produce the key stream that is then XOR-ed with the plaintext (CTR
encryption) or ciphertext (CTR decryption) input. In CTR mode, the MODE[1:0] bitfield
setting 01 (key derivation) is forbidden and all the other settings default to encryption mode.
The sequence of events to perform an encryption or a decryption in CTR chaining mode:
2. Select CTR chaini ng mode by setting to 010 the CHMOD[2:0] bitfield of the AES_CR
register. Set MODE[1:0] bitfield to any value other than 01.
3. Initialize the AES_KEYRx regi sters, and load the AES_IVRx registers as described in
[Table 227](../tables/table_227.md).
4. Set the EN bit of the AES_CR register, to  start encrypting the current counter (EN is
automatically reset when the calculation finishes).
5. If it is the last block, pad the data wit h zeros to have a complete block, if needed.
6. Append data in AES, and read the result. The three possible scenarios are described in
Section 29.4.4: AES procedure to perform a cipher operation.
7. Repeat the previous step till the second-last block is processed. For the last block,
apply the two previous steps and discard the bits that are not part of the payload (if the
size of the significant data in the last input block is less than 16 bytes).
Suspend/resume operations in CTR mode
Like for the CBC mode, it is possible to interrupt a message to send a higher priority
message, and resume the message that was interrupted. Detailed CBC suspend/resume
sequence is described in Section 29.4.8: AES basic chaining modes (ECB, CBC).
Note: Like for CBC mode, the AES_IVRx registers must be reloaded during the resume operation.
29.4.10 AES Galois/c ounter mode (GCM)
Overview
The AES Galois/counter mode (GCM) allows encrypting and authenticating a plaintext
message into the corresponding ciphertext and tag (also known as message authentication
code). To ensure confidentiality, GCM algorithm is based on AES counter mode. It uses a
multiplier over a fixed finite field to generate the tag.
GCM chaining is defined in NIST Special Publication 800-38D, Recommendation for Block
Cipher Modes of Operation - Galois/Counter Mode (GCM) and GMAC. A typical message
construction in GCM mode is given in [Figure 213](../figures/figure_213.md).
1. Disable the AES peripheral by clearing the EN bit of the AES_CR register.

AES hardware accelerator (AES) RM0438
972/2187 RM0438 Rev 8
[Figure 213](../figures/figure_213.md). Message construction in GCM
The message has the following structure:
• 16-byte initial counter block (ICB), composed of two distinct fields:
– Initialization vector (IV): a 96-bit value that must be unique for each encryption
cycle with a given key. Note that the GCM standard supports IVs with less than 96
bits, but in this case strict rules apply.
– Counter: a 32-bit big-endian integer that is incremented each time a block
processing is completed. According to NIST specification, the counter value is 0x2
when processing the first block of payload.
• Authenticated header AAD (also knows as additional authentication data) has a
known length Len(A) that may be a non-multiple of 16 bytes, and must not exceed
264 – 1 bits. This part of the message is only authenticated, not encrypted.
• Plaintext message P is both authenticated and encrypted as ciphertext C, with a
known length Len(P) that may be non-multiple of 16 bytes, and cannot exceed 232 - 2
128-bit blocks.
• Last block contains the AAD header length (bits [32:63]) and the payload length (bits
[96:127]) information, as shown in [Table 228](../tables/table_228.md).
The GCM standard specifies that ciphertext C has the same bit length as the plaintext P.
When a part of the message (AAD or P) has a length that is a non-multiple of 16-bytes a
special padding scheme is required.
MSv42157V1
Plaintext (P)
16-byte
boundaries
Additional authenticated data
(AAD)
Authenticated & encrypted ciphertext (C)
0
Len(A) Len(P) = Len(C)
0
[Len(A)]64
Last
block
[Len(C)]64
Authentication tag (T)
ICB
4-byte boundaries
CounterInitialization vector (IV)
authenticate
0
encrypt
Zero padding / zeroed bits
authenticate
auth.
[Table 228](../tables/table_228.md). GCM last block definition
Endianness Bit[0] ---------- Bit[31] Bit[32]---------- Bit[6 3] Bit[64] -------- Bit[95] Bit[96] --------- Bit[127]
Input data 0x0 AAD length[31:0] 0x0 Payload length[31:0]

RM0438 Rev 8 973/2187
RM0438 AES hardware  accelerator (AES)
1000
GCM processing
[Figure 214](../figures/figure_214.md) describes the GCM implementation in the AES peripheral. The GCM is selected
by writing 011 to the CHMOD[2:0] bitfield of the AES_CR register.
[Figure 214](../figures/figure_214.md). GCM authenticated encryption
The mechanism for the confidentiality of the plaintext in GCM mode is similar to that in the
Counter mode, with a particular increment function (denoted 32-bit increment) that
generates the sequence of input counter blocks.
AES_IVRx registers keeping the counter block of data are used for processing each data
block. The AES peripheral automatically increments the Counter[31:0] bitfield. The first
counter block (CB1) is derived from the initial counter block ICB by the application software
(see [Table 229](../tables/table_229.md)).
(4) Final
(1) Init
(2) Header
AES_KEYRx (KEY)
AES_DINR (plaintext P1)
AES_DOUTR
(ciphertext C1)
DATATYPE
[1:0] Swap
management
AES_IVRx
ICB + (32-bit counter = 0x02)
input
output
Legend
XOR
Swap
management
DATATYPE
[1:0]
AES_KEYRx (KEY)
DATATYPE[1:0] Swap
management
AES_IVRx
Swap
management
DATATYPE
[1:0]
Counter
increment (+1)
AES_DINR (plaintext Pn)
H
AES_DOUTR
(ciphertext Cn)
H
Encrypt
[0]128
H
AES_DINR (AAD 0)
Swap
management
Swap
management
AES_DINR (AAD i)
GF2mul
DATATYPE
[1:0]
GF2mulH H
AES_KEYRx (KEY)
GF2mul GF2mul
GF2mulH
AES_DINR
Len(A)64 || Len(C)64
Encrypt
AES_KEYRx (key)
AES_IVRx
(IV + 32-bit counter (= 0x1))
AES_DOUTR
(Authentication TAG T)
S
Encrypt Encrypt
Block 1 Block n
CBn
CB1 CBn
(3) Payload
[Table 229](../tables/table_229.md). Initialization of AES_IVRx registers in GCM mode
AES_IVR3[31:0] AES_IVR2[31:0] AES_IVR1[31:0] AES_IVR0[31:0]
ICB[127:96] ICB[ 95:64] ICB[63:32] ICB[31:0]
32-bit counter = 0x0002
Note: In this mode, the setting 01 of the MODE [1:0] bitfield (key derivation) is forbidden.

AES hardware accelerator (AES) RM0438
974/2187 RM0438 Rev 8
The authentication mechanism in GCM mode is based on a hash function called GF2mul
that performs multiplication by a fixed parameter, called hash subkey (H), within a binary
Galois field.
A GCM message is processed through the following phases, further described in next
subsections:
• Init phase: AES prepares the GCM hash subkey (H).
• Header phase: AES processes the additional authenticated data (AAD), with hash
computation only.
• Payload phase: AES processes the plaintext (P) with hash computation, counter block
encryption and data XOR-ing. It operates in a similar way for ciphertext (C).
• Final phase: AES generates the authenticated tag (T) using the last block of the
message.
GCM init phase
During this first step, the GCM hash subkey (H) is calculated and saved internally, to be
used for processing all the blocks. The recommended sequence is:
2. Select GCM chaining mode, by setting to  011 the CHMOD[2:0] bitfield of the AES_CR
register, and optionally, set the DATATYPE[1:0] bitfield.
3. Indicate the Init phase, by setting to  00 the GCMPH[1:0] bitfield of the AES_CR
register.
4. Set the MODE[1:0] bitfield of the AES_CR regi ster to 00 or 10. Although the bitfield is
only used in payload phase, it is recommended to set it in the Init phase and keep it
unchanged in all subsequent phases.
5. Initialize the AES_KEYRx re gisters with a key, and initialize AES_IVRx registers with
the information as defined in [Table 229](../tables/table_229.md).
6. Start the calculation of the hash key, by setting to 1 the EN bit of the AES_CR register
(EN is automatically reset when the calculation finishes).
7. Wait until the end of comp utation, indicated by the CCF flag of the AES_SR transiting
to 1. Alternatively, use the corresponding interrupt.
8. Clear the CCF flag of the AES_SR regist er, by setting the CCFC bit of the AES_CR
register.
GCM header phase
This phase coming after the GCM Init phase must be completed before the payload phase.
The sequence to execute, identical for encryption and decryption, is:
1. Indicate the header phase,  by setting to 01 the GCMPH[1:0] bitfield of the AES_CR
register. Do not modify the MODE[1:0] bitfield as set in the Init phase.
2. Enable the AES peripheral by setti ng the EN bit of the AES_CR register.
3. If it is the last block and the AAD size in the block is inferior to 128 bits, pad the
remainder of the block with zeros. Then append the data block into AES in one of ways
described in Section 29.4.4: AES procedure to perform a cipher operation. No data is
read during this phase.
4. Repeat the step 3 until the last additional authenticated data block is processed.
Note: The header phase can be skipped if  there is no AAD, that is, Len(A) = 0.
1. Disable the AES peripheral by clearing the EN bit of the AES_CR register.

RM0438 Rev 8 975/2187
RM0438 AES hardware  accelerator (AES)
1000
GCM payload phase
This phase, identical for encryption and decryption, is executed after the GCM header
phase. During this phase, the encrypted/decrypted payload is stored in the AES_DOUTR
register. The sequence to execute is:
1. Indicate the payload phase, by setting to 10 the GCMPH[1:0] bitfield of the AES_CR
register. Do not modify the MODE[1:0] bitfield as set in the Init phase.
2. If the header phase was skipped, enable the AES peripheral by setting the EN bit of the
AES_CR register.
3. If it is the last block and the plaintext (enc ryption) or ciphertext (decryption) size in the
block is inferior to 128 bits, pad the remainder of the block with zeros.
4. Append the data block into AES in one of ways described in Section 29.4.4: AES
procedure to perform a cipher operation, and read the result.
5. Repeat the previous step t ill the second-last plaintext block is encrypted or till the last
block of ciphertext is decrypted. For the last block of plaintext (encryption only),
execute the two previous steps. For the last block, discard the bits that are not part of
the payload when the last block size is less than 16 bytes.
Note: The payload phase can be skipped if there is no payload data, that is, Len(C)  = 0 (see
GMAC mode).
GCM final phase
In this last phase, the AES peripheral generates the GCM authentication tag and stores it in
the AES_DOUTR register. The sequence to execute is:
Note: In the final phase, data is written to AES_DINR normally (no swapping), while swapping is
applied to tag data read from AES_DOUTR.
When transiting from the header or the payload phase to the final phase, the AES peripheral
must not be disabled, otherwise the result is wrong.
1. Indicate the final phase, by setting to 11 the GCMPH[1:0] bitfield of the AES_CR
register.
2. Compose the data of the block, by conc atenating the AAD bit length and the payload
bit length, as shown in [Table 228](../tables/table_228.md). Write the block into the AES_DINR register.
3. Wait until the end of comp utation, indicated by the CCF flag of the AES_SR transiting
to 1.
4. Get the GCM authentication tag, by reading the AES_DOUTR register four times.
5. Clear the CCF flag of the AES_SR regist er, by setting the CCFC bit of the AES_CR
register.
6. Disable the AES periphe ral, by clearing the bit EN of the AES_CR register. If it is an
authenticated decryption, compare the generated tag with the expected tag passed
with the message.

AES hardware accelerator (AES) RM0438
976/2187 RM0438 Rev 8
Suspend/resume operations in GCM mode
29.4.11 AES Galois message authentication code (GMAC)
Overview
The Galois message authentication code (GMAC) allows the authentication of a plaintext,
generating the corresponding tag information (also known as message authentication
code). It is based on GCM algorithm, as defined in NIST Special Publication 800-38D,
Recommendation for Block Cipher Modes of Operation - Galois/Counter Mode (GCM) and
GMAC.
To suspend the processing of a message, proceed as follows:
1. If DMA is used, stop the AES DMA transfers to the IN FIFO by clearing the DMAINEN
bit of the AES_CR register. If DMA is not used, make sure that the current computation
is completed, which is indicated by the CCF flag of the AES_SR register set to 1.
2. In the payload phase, if DMA is not used , read four times the AES_DOUTR register to
save the last-processed block. If DMA is used, wait until the CCF flag is set in the
AES_SR register then stop the DMA transfers from the OUT FIFO by clearing the
DMAOUTEN bit of the AES_CR register.
3. Clear the CCF flag of the AES_SR regist er, by setting the CCFC bit of the AES_CR
register.
4. Save the AES_SUSPxR registers in the memory, where x is from 0 to 7.
5. In the payload phas e, save the AES_IVRx registers as, during the data processing,
they changed from their initial values. In the header phase, this step is not required.
6. Disable the AES per ipheral, by clearing the EN bit of the AES_CR register.
7. Save the current AES config uration in the memory, excluding the initialization vector
registers AES_IVRx. Key registers do not need to be saved as the original key value is
known by the application.
8. If DMA is used, save the DMA controller status (pointers for IN data transfers, number
of remaining bytes, and so on). In the payload phase, pointers for OUT data transfers
must also be saved.
To resume the processing of a message, proceed as follows:
1. If DMA is used, configure the DMA controller in order to complete the rest of the FIFO
IN transfers. In the payload phase, the rest of the FIFO OUT transfers must also be
configured in the DMA controller.
2. Disable the AES per ipheral by clearing the EN bit of the AES_CR register.
3. Write the suspend register values, previo usly saved in the memory, back into their
corresponding AES_SUSPxR registers, where x is from 0 to 7.
4. In the payload phase, write the initializatio n vector register values, previously saved in
the memory, back into their corresponding AES_IVRx registers. In the header phase,
write initial setting values back into the AES_IVRx registers.
5. Restore the initial setting values in the AES_CR and AES_KEYRx registers.
6. Enable the AES peripheral by setti ng the EN bit of the AES_CR register.
If DMA is used, enable AES DMA requests by setting the DMAINEN bit (and DMAOUTEN
bit if in payload phase) of the AES_CR register.

RM0438 Rev 8 977/2187
RM0438 AES hardware  accelerator (AES)
1000
A typical message construction for GMAC is given in [Figure 215](../figures/figure_215.md).
[Figure 215](../figures/figure_215.md). Message construction in GMAC mode
AES GMAC processing
[Figure 216](../figures/figure_216.md) describes the GMAC mode implementation in the AES peripheral. This mode is
selected by writing 011 to the CHMOD[2:0] bitfield of the AES_CR register.
[Figure 216](../figures/figure_216.md). GMAC authentication mode
The GMAC algorithm corresponds to the GCM algorithm applied on a message only
containing a header. As a consequence, all steps and settings are the same as with the
GCM, except that the payload phase is omitted.
MSv42158V2
Authenticated data
16-byte
boundaries
0
Len(A)
[Len(A)]64
Last
block
[0]64
Authentication tag (T)
ICB
4-byte boundaries
CounterInitialization vector (IV)
Zero padding
auth.
MSv42150V2
(4) Final(1) Init
(2) Header
AES_KEYRx (KEY)
input
output
Legend
XOR
AES_KEYRx (KEY)
AES_IVRx
IV + 32-bit counter (= 0x0)
Encrypt
[0]128
H
AES_DINR
(message block 1)
Swap
management
Swap
management
AES_DINR
(message block n)
GF2mul
DATATYPE
[1:0]
GF2mulH H
GF2mulH
AES_DINR
len(A)64 || [0]64
AES_DOUTR
(authentication tag T)
S
Encrypt

AES hardware accelerator (AES) RM0438
978/2187 RM0438 Rev 8
Suspend/resume operations in GMAC
29.4.12 AES counter with CBC-MAC (CCM)
Overview
The AES counter with cipher block chaining-message authentication code (CCM)
algorithm allows encryption and authentication of plaintext, generating the corresponding
ciphertext and tag (also known as message authentication code). To ensure confidentiality,
the CCM algorithm is based on AES in counter mode. It uses cipher block chaining
technique to generate the message authentication code. This is commonly called CBC-
MAC.
Note: NIST does not approve this CBC-MAC as an au thentication mode outside the context of the
CCM specification.
CCM chaining is specified in NIST Special Publication 800-38C, Recommendation for Block
Cipher Modes of Operation - The CCM Mode for Authentication and Confidentiality. A typical
message construction for CCM is given in [Figure 217](../figures/figure_217.md).
[Figure 217](../figures/figure_217.md). Message construction in CCM mode
The structure of the message is:
• 16-byte first authentication block (B0), composed of three distinct fields:
– Q: a bit string representation of the octet length of P (Len(P))
– Nonce (N): a single-use value (that is, a new nonce must be assigned to each
new communication) of Len(N) size. The sum Len(N) + Len(P) must be equal to
15 bytes.
– Flags: most significant octet containing four flags for control information, as
specified by the standard. It contains two 3-bit strings to encode the values t (MAC
length expressed in bytes) and Q (plaintext length such that Len(P) < 28q bytes).
The counter blocks range associated to Q is equal to 28Q-4, that is, if the maximum
value of Q is 8, the counter blocks used in cipher must be on 60 bits.
• 16-byte blocks (B) associated to the Associated Data (A).
This part of the message is only authenticated, not encrypted. This section has a
In GMAC mode, the sequence described for the GCM applies except that only the header
phase can be interrupted.
MSv42159V2
Plaintext (P)
16-byte
boundaries
Associated data (A)
Authenticated & encrypted ciphertext (C)
0
Len(A) Len(P)
0 Enc
(T)
MAC (T)
B0
4-byte boundaries
QNonce (N)
authenticate
encrypt
Zero padding
Len(C)
[a]32
[a]16
Len(T)
flags
Len(N) Decrypt and compare

RM0438 Rev 8 979/2187
RM0438 AES hardware  accelerator (AES)
1000
known length Len(A) that can be a non-multiple of 16 bytes (see [Figure 217](../figures/figure_217.md)). The
standard also states that, on MSB bits of the first message block (B1), the associated
data length expressed in bytes (a) must be encoded as follows:
– If 0 < a < 2 16 - 28, then it is encoded as [a]16, that is, on two bytes.
–I f  2 16 - 28 < a < 232, then it is encoded as 0xff || 0xfe || [a]32, that is, on six bytes.
–I f  2 32 < a < 264, then it is encoded as 0xff || 0xff || [a]64, that is, on ten bytes.
• 16-byte blocks (B) associated to the plaintext message P, which is both authenticated
and encrypted as ciphertext C, with a known length Len(P). This length can be a non-
multiple of 16 bytes (see [Figure 217](../figures/figure_217.md)).
• Encrypted MAC (T) of length Len(T) appended to the ciphertext C of overall length
Len(C).
When a part of the message (A or P) has a length that is a non-multiple of 16-bytes, a
special padding scheme is required.
Note: CCM chaining mode can also be used with a ssociated data only (that is, no payload).
As an example, the C.1 section in NIST Special Publication 800-38C gives the following
values (hexadecimal numbers):
N: 10111213 141516 (Len(N) = 56 bits or 7 bytes)
A: 00010203 04050607 (Len(A) = 64 bits or 8 bytes)
P: 20212223 (Len(P) = 32 bits or 4 bytes)
T: 6084341B (Len(T) = 32 bits or t = 4)
B0: 4F101112 13141516 00000000 00000004
B1: 00080001 02030405 06070000 00000000
B2: 20212223 00000000 00000000 00000000
CTR0: 0710111213 141516 00000000 00000000
CTR1: 0710111213 141516 00000000 00000001
Generation of formatted input data blocks Bx (especially B0 and B1) must be managed by
the application.

AES hardware accelerator (AES) RM0438
980/2187 RM0438 Rev 8
CCM processing
[Figure 218](../figures/figure_218.md) describes the CCM implementation within the AES peripheral (encryption
example). This mode is selected by writing 100 into the CHMOD[2:0] bitfield of the AES_CR
register.
[Figure 218](../figures/figure_218.md). CCM mode authenticated encryption
The data input to the generation-encryption process are a valid nonce, a valid payload
string, and a valid associated data string, all properly formatted. The CBC chaining
mechanism is applied to the formatted plaintext data to generate a MAC, with a known
length. Counter mode encryption that requires a sufficiently long sequence of counter blocks
as input, is applied to the payload string and separately to the MAC. The resulting ciphertext
C is the output of the generation-encryption process on plaintext P.
AES_IVRx registers are used for processing each data block, AES automatically
incrementing the CTR counter with a bit length defined by the first block B0. [Table 230](../tables/table_230.md)
shows how the application must load the B0 data.
Note: The AES peripheral in CCM mo de supports counters up to 64 bits, as specified by NIST.
MSv42152V2
(2) Header
(1) Init
(4) Final
AES_DINR (plaintext P1)
AES_DOUTR (ciphertext C1)
DATATYPE
[1:0]Swap
management
AES_IVRx (CTR1)
input
output
Legend
XOR
Swap
management
DATATYPE
[1:0]
AES_KEYRx (KEY)
AES_IVRx (CTRm)
Swap
management
DATATYPE
[1:0]
Counter
increment (+1)
AES_DINR (plaintext
last block Pm )
AES_DOUTR
(ciphertext last block Cm)
Encrypt
AES_IVRx (CTR0)
AES_DINR (associated
data block B1)
Swap
management
Swap
management
AES_DINR (associated
data last block Bu)
AES_KEYRx (KEY)
AES_DINR (CTR0)
Encrypt
AES_KEYRx (KEY)
AES_DOUTR
(EncTAG)
MAC (T)
Encrypt Encrypt
S0
BrBu+1
Encrypt
AES_KEYRx (KEY)
Encrypt
AES_KEYRx (KEY)
Encrypt
AES_KEYRx (KEY)
Encrypt
AES_KEYRx (KEY)
AES_KEYRx (KEY)
DATATYPE
[1:0] Swap
management
DATATYPE[1:0]DATATYPE[1:0]
SmS1
Counter
increment (+1)
AES_IVRx (First block B0)
mask
Block 1 Block m (3) Payload
[Table 230](../tables/table_230.md). Initialization of AES_IVRx registers in CCM mode
AES_IVR3[31:0] AES_IVR2[31:0] AES_IVR1[31:0] AES_IVR0[31:0]
B0[127:96] B0[95:64 ] B0[63:32] B0[31:0]

RM0438 Rev 8 981/2187
RM0438 AES hardware  accelerator (AES)
1000
A CCM message is processed through the following phases, further described in next
subsections:
• Init phase: AES processes the first block and prepares the first counter block.
• Header phase: AES processes associated data (A), with tag computation only.
• Payload phase: IP processes plaintext (P), with tag computation, counter block
encryption, and data XOR-ing. It works in a similar way for ciphertext (C).
• Final phase: AES generates the message authentication code (MAC).
CCM Init phase
In this phase, the first block B0 of the CCM message is written into the AES_IVRx register.
The AES_DOUTR register does not contain any output data. The recommended sequence
is:
2. Select CCM chaining mode, by setting to  100 the CHMOD[2:0] bitfield of the AES_CR
register, and optionally, set the DATATYPE[1:0] bitfield.
3. Indicate the Init phase, by setting to  00 the GCMPH[1:0] bitfield of the AES_CR
register.
4. Set the MODE[1:0] bitfield of the AES_CR regi ster to 00 or 10. Although the bitfield is
only used in payload phase, it is recommended to set it in the Init phase and keep it
unchanged in all subsequent phases.
5. Initialize the AES_KEYRx re gisters with a key, and initialize AES_IVRx registers with
B0 data as described in [Table 230](../tables/table_230.md).
6. Start the calculation of the counter, by se tting to 1 the EN bit of the AES_CR register
(EN is automatically reset when the calculation finishes).
7. Wait until the end of comp utation, indicated by the CCF flag of the AES_SR transiting
to 1. Alternatively, use the corresponding interrupt.
8. Clear the CCF flag in the AES_SR register, by setting to 1 the CCFC bit of the AES_CR
register.
CCM header phase
This phase coming after the GCM Init phase must be completed before the payload phase.
During this phase, the AES_DOUTR register does not contain any output data.
The sequence to execute, identical for encryption and decryption, is:
1. Indicate the header phase,  by setting to 01 the GCMPH[1:0] bitfield of the AES_CR
register. Do not modify the MODE[1:0] bitfield as set in the Init phase.
2. Enable the AES peripheral by setti ng the EN bit of the AES_CR register.
3. If it is the last block and the AAD size in the block is inferior to 128 bits, pad the
remainder of the block with zeros. Then append the data block into AES in one of ways
described in Section 29.4.4: AES procedure to perform a cipher operation. No data is
read during this phase.
4. Repeat the step 3 until the last additional authenticated data block is processed.
Note: The header phase can be skipped if th ere is no associated data, that is, Len(A) = 0.
The first block of the associated data (B1) must be formatted by software, with the
associated data length.
Note: In this mode, the setting 01 of the MODE [1:0] bitfield (key derivation) is forbidden.
1. Disable the AES peripheral by clearing the EN bit of the AES_CR register.

AES hardware accelerator (AES) RM0438
982/2187 RM0438 Rev 8
CCM payload phase (encryption or decryption)
This phase, identical for encryption and decryption, is executed after the CCM header
phase. During this phase, the encrypted/decrypted payload is stored in the AES_DOUTR
register. The sequence to execute is:
1. Indicate the payload phase, by setting to 10 the GCMPH[1:0] bitfield of the AES_CR
register. Do not modify the MODE[1:0] bitfield as set in the Init phase.
2. If the header phase was skipped, enable the AES peripheral by setting the EN bit of the
AES_CR register.
3. If it is the last data block to encrypt and t he plaintext size in the block is inferior to 128
bits, pad the remainder of the block with zeros.
4. Append the data block into AES in one of ways described in Section 29.4.4: AES
procedure to perform a cipher operation, and read the result.
5. Repeat the previous step t ill the second-last plaintext block is encrypted or till the last
block of ciphertext is decrypted. For the last block of plaintext (encryption only), apply
the two previous steps. For the last block, discard the data that is not part of the
payload when the last block size is less than 16 bytes.
Note: The payload phase can be skipped if there is no payload data, that is, Len(P)  = 0 or
Len(C) = Len(T).
Remove LSBLen(T)(C) encrypted tag information when decrypting ciphertext C.
CCM final phase
In this last phase, the AES peripheral generates the GCM authentication tag and stores it in
the AES_DOUTR register. The sequence to execute is:
1. Indicate the final phase, by setting to 11 the GCMPH[1:0] bitfield of the AES_CR
register.
2. Wait until the en d-of-computation flag CCF of the AES_SR register is set.
3. Read four times the AES_DOUTR regi ster: the output corresponds to the CCM
authentication tag.
4. Clear the CCF flag of the AES_SR regist er by setting the CCFC bit of the AES_CR
register.
5. Disable the AES per ipheral, by clearing the EN bit of the AES_CR register.
6. For authenticated decryption, compare the generated encrypted tag with the encrypted
tag padded in the ciphertext.
When transiting from the header phase to the final phase, the AES peripheral must not be
disabled, otherwise the result is wrong.
Application must mask the authentication tag output with tag length to obtain a valid tag.
Suspend/resume operations in CCM mode
To suspend the processing of a message in header or payload phase, proceed as
follows:
1. If DMA is used, stop the AES DMA transfers to the IN FIFO by clearing the DMAINEN
bit of the AES_CR register. If DMA is not used, make sure that the current computation
is completed, which is indicated by the CCF flag of the AES_SR register set to 1.
2. In the payload phase, if DMA is not used , read four times the AES_DOUTR register to
save the last-processed block. If DMA is used, wait until the CCF flag is set in the
Note: In this final phase, swapp ing is applied to tag data read from AES_DOUTR register.

RM0438 Rev 8 983/2187
RM0438 AES hardware  accelerator (AES)
1000
AES_SR register then stop the DMA transfers from the OUT FIFO by clearing the
DMAOUTEN bit of the AES_CR register.
3. Clear the CCF flag of the AES_SR regist er, by setting to 1 the CCFC bit of the AES_CR
register.
4. Save the AES_SUSPxR registers (where  x is from 0 to 7) in the memory.
5. Save the AES_IVRx registers as, during the data processing, they changed from their
initial values.
6. Disable the AES per ipheral, by clearing the EN bit of the AES_CR register.
7. Save the current AES config uration in the memory, excluding the initialization vector
registers AES_IVRx. Key registers do not need to be saved as the original key value is
known by the application.
8. If DMA is used, save the DMA controller status (pointers for IN data transfers, number
of remaining bytes, and so on). In the payload phase, pointers for OUT data transfers
must also be saved.
To resume the processing of a message, proceed as follows:
1. If DMA is used, configure the DMA controller in order to complete the rest of the FIFO
IN transfers. In the payload phase, the rest of the FIFO OUT transfers must also be
configured in the DMA controller.
2. Disable the AES per ipheral by clearing the EN bit of the AES_CR register.
3. Write the suspend register values, previo usly saved in the memory, back into their
corresponding AES_SUSPxR registers (where x is from 0 to 7).
4. Write the initialization vector  register values, previously saved in the memory, back into
their corresponding AES_IVRx registers.
5. Restore the initial setting values in the AES_CR and AES_KEYRx registers.
6. Enable the AES peripheral by setti ng the EN bit of the AES_CR register.
7. If DMA is used, enable AES DMA reques ts by setting to 1 the DMAINEN bit (and
DMAOUTEN bit if in payload phase) of the AES_CR register.
29.4.13 AES data regist ers and data swapping
Data input and output
A 128-bit data block is entered into the AES peripheral with four successive 32-bit word
writes into the AES_DINR register (bitfield DIN[31:0]), the most significant word (bits
[127:96]) first, the least significant word (bits [31:0]) last.
A 128-bit data block is retrieved from the AES peripheral with four successive 32-bit word
reads from the AES_DOUTR register (bitfield DOUT[31:0]), the most significant word (bits
[127:96]) first, the least significant word (bits [31:0]) last.
The 32-bit data word for AES_DINR register or from AES_DOUTR register is organized in
big endian order, that is:
• the most significant byte of a word to write into AES_DINR must be put on the lowest
address out of the four adjacent memory locations keeping the word to write, or
• the most significant byte of a word read from AES_DOUTR goes to the lowest address
out of the four adjacent memory locations receiving the word
For using DMA for input data block write into AES, the four words of the input block must be
stored in the memory consecutively and in big-endian order, that is, the most significant
word on the lowest address. See Section 29.4.16: AES DMA interface.

AES hardware accelerator (AES) RM0438
984/2187 RM0438 Rev 8
Data swapping
The AES peripheral can be configured to perform a bit-, a byte-, a half-word-, or no
swapping on the input data word in the AES_DINR register, before loading it to the AES
processing core, and on the data output from the AES processing core, before sending it to
the AES_DOUTR register. The choice depends on the type of data. For example, a byte
swapping is used for an ASCII text stream.
The data swap type is selected through the DATATYPE[1:0] bitfield of the AES_CR register.
The selection applies both to the input and the output of the AES core.
For different data swap types, [Figure 219](../figures/figure_219.md) shows the construction of AES processing core
input buffer data P127 to P0, from the input data entered through the AES_DINR register, or
the construction of the output data available through the AES_DOUTR register, from the
AES processing core output buffer data P127 to P0.
[Figure 219](../figures/figure_219.md). 128-bit block construction with respect to data swap
MSv42153V2
DATATYPE[1:0] = 00: no swapping
Word 2Word 3
D127 D96 P95
LSBMSB
DATATYPE[1:0] = 01: 16-bit (half-word) swapping
Word 3
DATATYPE[1:0] = 10: 8-bit (byte) swapping
Word 2Word 3
DATATYPE[1:0] = 11: bit swapping
Word 3
LSBMSB
LSBMSB
LSBMSB
LSBMSB
MSB
MSB
MSB LSB
LSB
Word 0Word 1
LSB
Word 0
Word 0Word 1
D63 D32 D31 D0D64
Word 2
Zero padding (example)
Legend:
Data swap
Word 2
D95
Word 1
Word 0Word 1
AES input/output data block in memory
AES core input/output buffer data
1
1
1
1
2
2
2
2
3
3
3
3
4
4
4
4
Order of write to AES_DINR / read from AES_DOUTR
MSB
LSB
increasing memory address
D127 D96 D63 D32 D31 D0D64D95
D127 D96 D95D112 D111 D80 D31 D0 D15D16D64D79 D32 D63 D48 D47
D127..120 D103..96D119..112 D111.104 D71...64 D95..88 D87..80 D79..72 D63...56 D55...48 D47...40 D39...32 D31...24 D23...16 D15...8 D7...0
D127 D126 D125 D98 D97 D96 D95 D94 D93 D31 D30 D29 D0 D1D2D66 D65 D64 D63 D62 D61 D34 D33 D32
byte 3 byte 2 byte 1 byte 0
D63 D55 D47 D39D56 D48 D40 D32
most significant bit (127) of memory data block / AEC core buffer
least significant bit (0) of memory data block / AEC core buffer
Dx input/output data bit ‘x’
D96D111 D127 D112 D64 D79 D95 D80 D32 D47 D63 D48 D0 D15 D31 D16
D103..96 D111.104 D119..112 D127..120 D71...64 D79..72 D87..80 D95..88 D39...32 D47...40 D55...48 D63...56 D7...0 D15...8 D23...16 D31...24
D96 D127D97 D126D98 D125 D95D64 D94D65 D93D66 D63 D32 D62D33 D61D34 D31 D0 D30D1 D29D2
1 4

RM0438 Rev 8 985/2187
RM0438 AES hardware  accelerator (AES)
1000
Note: The data in AES key regi sters (AES_KEYRx) and initialization registers (AES_IVRx) are not
sensitive to the swap mode selection.
Data padding
[Figure 219](../figures/figure_219.md) also gives an example of memory data block padding with zeros such that the
zeroed bits after the data swap form a contiguous zone at the MSB end of the AES core
input buffer. The example shows the padding of an input data block containing:
• 48 message bits, with DATATYPE[1:0] = 01
• 56 message bits, with DATATYPE[1:0] = 10
• 34 message bits, with DATATYPE[1:0] = 11
29.4.14 AES key registers
The AES_KEYRx write-only registers store the encryption or decryption key bitfield
KEY[127:0] or KEY[255:0]. The data to write to each register is organized in the memory in
little-endian order, that is, with most significant byte on the highest address (reads are not
allowed for security reason).
The key is spread over eight registers as shown in [Table 231](../tables/table_231.md).
The key for encryption or decryption may be written into these registers when the AES
peripheral is disabled, by clearing the EN bit of the AES_CR register.
The key registers are not affected by the data swapping controlled by DATATYPE[1:0]
bitfield of the AES_CR register.
29.4.15 AES initialization vector registers
The four AES_IVRx registers keep the initialization vector input bitfield IVI[127:0]. The data
to write to or to read from each register is organized in the memory in little-endian order, that
is, with most significant byte on the highest address. The registers are also ordered from
lowest address (AES_IVR0) to highest address (AES_IVR3).
The signification of data in the bitfield depends on the chaining mode selected. When used,
the bitfield is updated upon each computation cycle of the AES core.
Write operations to the AES_IVRx registers when the AES peripheral is enabled have no
effect to the register contents. For modifying the contents of the AES_IVRx registers, the EN
bit of the AES_CR register must first be cleared.
Reading the AES_IVRx registers returns the latest counter value (useful for managing
suspend mode).
The AES_IVRx registers are not affected by the data swapping feature controlled by the
DATATYPE[1:0] bitfield of the AES_CR register.
[Table 231](../tables/table_231.md). Key endianness in AES_KEYRx registers (128- or 256-bit key length)
AES_KEYR7
[31:0]
AES_KEYR6
[31:0]
AES_KEYR5
[31:0]
AES_KEYR4
[31:0]
AES_KEYR3
[31:0]
AES_KEYR2
[31:0]
AES_KEYR1
[31:0]
AES_KEYR0
[31:0]
- - - - KEY[127:96] KEY[95:64] KEY[63:32] KEY[31:0]
KEY[255:224] KEY[223:192] KEY[191:160] KEY[159:128] KEY[127:96] KEY[95:64] KEY[63:32] KEY[31:0]

AES hardware accelerator (AES) RM0438
986/2187 RM0438 Rev 8
29.4.16 AES DMA interface
The AES peripheral provides an interface to connect to the DMA (direct memory access)
controller. The DMA operation is controlled through the AES_CR register.
Data input using DMA
Setting the DMAINEN bit of the AES_CR register enables DMA writing into AES. The AES
peripheral then initiates a DMA request during the input phase each time it requires to write
a 128-bit block (quadruple word) to the AES_DINR register, as shown in [Figure 220](../figures/figure_220.md).
Note: According to the algorithm and the mode selected, special padding / ciphertext stealing
might be required. For example, in case of AES GCM encryption or AES CCM decryption, a
DMA transfer must not include the last block. For details, refer to Section 29.4.4: AES
procedure to perform a cipher operation.
[Figure 220](../figures/figure_220.md). DMA transfer of a 128-bit data block during input phase
Data output using DMA
Setting the DMAOUTEN bit of the AES_CR register enables DMA reading from AES. The
AES peripheral then initiates a DMA request during the Output phase each time it requires
to read a 128-bit block (quadruple word) to the AES_DINR register, as shown in [Figure 221](../figures/figure_221.md).
Note: According to the message size, extra bytes migh t need to be discarded by application in the
last block.
MSv42160V1
AES core input buffer
AES_DINR
LSBMSB
(No swapping)
Memory accessed through DMA
Word2Word3 Word0Word1
DMA
single writeDMA req N DMA req N+1 DMA req N+2 DMA req N+3
I127 I96 I63 I32 I31 I0I64I95
D127 D96 D63 D32 D31 D0D64D95DIN[127:96] DIN[95:64] DIN[63:32] DIN[31:0]
DMA
single write
DMA
single write
DMA
single write
Chronological order
Increasing address
LSBMSB
AES
peripheral System
1 2 3 4
1 Order of write to AES_DINR
1 2 3 4
4

RM0438 Rev 8 987/2187
RM0438 AES hardware  accelerator (AES)
1000
[Figure 221](../figures/figure_221.md). DMA transfer of a 128-bit data block during output phase
DMA operation in different operating modes
DMA operations are usable when Mode 1 (encryption) or Mode 3 (decryption) are selected
via the MODE[1:0] bitfield of the register AES_CR. As in Mode 2 (key derivation) the
AES_KEYRx registers must be written by software, enabling the DMA transfer through the
DMAINEN and DMAOUTEN bits of the AES_CR register have no effect in that mode.
DMA single requests are generated by AES until it is disabled. So, after the data output
phase at the end of processing of a 128-bit data block, AES switches automatically to a new
data input phase for the next data block, if any.
When the data transferring between AES and memory is managed by DMA, the CCF flag
has no use because the reading of the AES_DOUTR register is managed by DMA
automatically at the end of the computation phase. The CCF flag must only be cleared when
transiting back to data transferring managed by software. See Section 29.4.4: AES
procedure to perform a cipher operation, subsection Data append, for details.
29.4.17 AES error management
AES configuration can be changed at any moment by clearing the EN bit of the AES_CR
register.
Read error flag (RDERR)
Unexpected read attempt of the AES_DOUTR register sets the RDERR flag of the AES_SR
register, and returns zero.
RDERR is triggered during the computation phase or during the input phase.
Note: AES is not disabled upon a RDERR error detection and continues processing.
An interrupt is generated if the ERRIE bit of the AES_CR register is set. For more details,
refer to Section 29.5: AES interrupts.
The RDERR flag is cleared by setting the ERRIE bit of the AES_CR register.
Write error flag (WDERR)
Unexpected write attempt of the AES_DINR register sets the WRERR flag of the AES_SR
register, and has no effect on the AES_DINR register. The WRERR is triggered during the
computation phase or during the output phase.
MSv42161V1
AES core output buffer
LSBMSB
(No swapping)
Memory accessed through DMA
Word2Word3 Word0Word1
DMA
single readDMA req N DMA req N+1 DMA req N+2 DMA req N+3
O127 O96 O63 O32 O31 O0O64O95
D127 D96 D63 D32 D31 D0D64D95DOUT[127:96] DOUT[95:64] DOUT[63:32] DOUT[31:0]
DMA
single read
DMA
single read
DMA
single read
Chronological order
Increasing address
LSBMSB
SystemAES
peripheral
1 2 3 4
1 2 3 4
1 Order of read from AES_DOUTR4
AES_DOUTR

AES hardware accelerator (AES) RM0438
988/2187 RM0438 Rev 8
Note: AES is not disabled after a WRERR error detection and continues processing.
An interrupt is generated if the ERRIE bit of the AES_CR register is set. For more details,
refer to Section 29.5: AES interrupts.
The WRERR flag is cleared by setting the ERRC bit of the AES_CR register.
29.5 AES interrupts
Individual maskable interrupt sources generated by the AES peripheral signal the following
events:
• computation completed
• read error
• write error
These sources are combined into a common interrupt signal from the AES peripheral that
connects to the Arm® Cortex® interrupt controller. Each can individually be
enabled/disabled, by setting/clearing the corresponding enable bit of the AES_CR register,
and cleared by setting the corresponding bit of the AES_CR register.
The status of each can be read from the AES_SR register.
[Table 232](../tables/table_232.md) gives a summary of the interrupt sources, their event flags and enable bits.
29.6 AES processing latency
The tables below summarize the latency to process a 128-bit block for each mode of
operation.
[Table 232](../tables/table_232.md). AES interrupt requests
Interrupt
acronym AES interrupt event Event flag Enable bit Interrupt clear
method
AES
computation completed flag CCF CCFIE set CCFC (1)
read error flag RDERR
ERRIE set ERRC (1)
write error flag WRERR
1. Bit of the AES_CR register.
[Table 233](../tables/table_233.md). Processing latency for ECB, CBC and CTR
Key size Mode of operation Algorithm Clock
cycles
128-bit
Mode 1: Encryption ECB, CBC, CTR 51
Mode 2: Key derivation - 59
Mode 3: Decryption ECB, CBC, CTR 51
256-bit
Mode 1: Encryption ECB, CBC, CTR 75
Mode 2: Key derivation - 82
Mode 3: Decryption ECB, CBC, CTR 75

RM0438 Rev 8 989/2187
RM0438 AES hardware  accelerator (AES)
1000
29.7 AES registers
29.7.1 AES control register (AES_CR)
Address offset: 0x00
Reset value: 0x0000 0000
[Table 234](../tables/table_234.md). Processing latency for GCM and CCM (in clock cycles)
Key size Mode of operation Algorithm Init Phase Header
phase(1)
Payload
phase(1) Tag phase(1)
128-bit Mode 1: Encryption/
Mode 3: Decryption
G C M 6 43 55 15 9
CCM 63 55 114 58
256-bit Mode 1: Encryption/
Mode 3: Decryption
G C M 8 83 57 57 5
CCM 87 79 162 82
1. Data insertion can include wait states forced by AES  on the AHB bus (maximum 3 cycles, typical 1 cycle).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. NPBLB[3:0] Res.
KEYSIZE
Res.
CHMOD[2]
rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. GCMPH[1:0]
DMAOUTEN
DMAINEN
ERRIE CCFIE ERRC CCFC CHMOD[1:0] MODE[1:0] DATATYPE[1:0] EN
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:24 Reserved, must be kept at reset value.
Bits 23:20 NPBLB[3:0]: Number of padding bytes in last block
The bitfield sets the number of padding bytes in last block of payload:
0000: All bytes are valid (no padding)
0001: Padding for one least-significant byte of last block
...
1111: Padding for 15 least-significant bytes of last block
Bit 19 Reserved, must be kept at reset value.
Bit 18 KEYSIZE: Key size selection
This bitfield defines the length of the key used in the AES cryptographic core, in bits:
0: 128
1: 256
Attempts to write the bit are ignored when the EN bit of the AES_CR register is set before the write
access and it is not cleared by that write access.
Bit 17 Reserved, must be kept at reset value.
Bit 15 Reserved, must be kept at reset value.

AES hardware accelerator (AES) RM0438
990/2187 RM0438 Rev 8
Bits 14:13 GCMPH[1:0]: GCM or CCM phase selection
This bitfield selects the phase of GCM, GMAC or CCM algorithm:
00: Init phase
01: Header phase
10: Payload phase
11: Final phase
The bitfield has no effect if other than GCM, GMAC or CCM algorithms are selected (through the
ALGOMODE bitfield).
Bit 12 DMAOUTEN: DMA output enable
This bit enables/disables data transferring with DMA, in the output phase:
0: Disable
1: Enable
When the bit is set, DMA requests are automatically generated by AES during the output data
phase. This feature is only effective when Mode 1 or Mode 3 is selected through the MODE[1:0]
bitfield. It is not effective for Mode 2 (key derivation).
Bit 11 DMAINEN: DMA input enable
This bit enables/disables data transferring with DMA, in the input phase:
0: Disable
1: Enable
When the bit is set, DMA requests are automatically generated by AES during the input data phase.
This feature is only effective when Mode 1 or Mode 3 is selected through the MODE[1:0] bitfield. It is
not effective for Mode 2 (key derivation).
Bit 10 ERRIE: Error interrupt enable
This bit enables or disables (masks) the AES interrupt generation when RDERR and/or WRERR is
set:
0: Disable (mask)
1: Enable
Bit 9 CCFIE: CCF interrupt enable
This bit enables or disables (masks) the AES interrupt generation when CCF (computation complete
flag) is set:
0: Disable (mask)
1: Enable
Bit 8 ERRC: Error flag clear
Upon written to 1, this bit clears the RDERR and WRERR error flags in the AES_SR register:
0: No effect
1: Clear RDERR and WRERR flags
Reading the flag always returns zero.
Bit 7 CCFC: Computation complete flag clear
Upon written to 1, this bit clears the computation complete flag (CCF) in the AES_SR register:
0: No effect
1: Clear CCF
Reading the flag always returns zero.

RM0438 Rev 8 991/2187
RM0438 AES hardware  accelerator (AES)
1000
29.7.2 AES status register (AES_SR)
Address offset: 0x04
Reset value: 0x0000 0000
Bits 16, 6:5 CHMOD[2:0]: Chaining mode selection
This bitfield selects the AES chaining mode:
000: Electronic codebook (ECB)
001: Cipher-block chaining (CBC)
010: Counter mode (CTR)
011: Galois counter mode (GCM) and Galois message authentication code (GMAC)
100: Counter with CBC-MAC (CCM)
others: Reserved
Attempts to write the bitfield are ignored when the EN bit of the AES_CR register is set before the
write access and it is not cleared by that write access.
Bits 4:3 MODE[1:0]: AES operating mode
This bitfield selects the AES operating mode:
00: Mode 1: encryption
01: Mode 2: key derivation (or key preparation for ECB/CBC decryption)
10: Mode 3: decryption
11: Reserved
Attempts to write the bitfield are ignored when the EN bit of the AES_CR register is set before the
write access and it is not cleared by that write access.
Bits 2:1 DATATYPE[1:0]: Data type selection
This bitfield defines the format of data written in the AES_DINR register or read from the
AES_DOUTR register, through selecting the mode of data swapping:
00: None
01: Half-word (16-bit)
10: Byte (8-bit)
11: Bit
For more details, refer to Section 29.4.13: AES data registers and data swapping.
Attempts to write the bitfield are ignored when the EN bit of the AES_CR register is set before the
write access and it is not cleared by that write access.
Bit 0 EN: AES enable
This bit enables/disables the AES peripheral:
0: Disable
1: Enable
At any moment, clearing then setting the bit re-initializes the AES peripheral.
This bit is automatically cleared by hardware upon the completion of the key preparation (Mode 2)
and upon the completion of GCM/GMAC/CCM initial phase.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. BUSY WRERR RDERR CCF
rrr r
Bits 31:4 Reserved, must be kept at reset value.

AES hardware accelerator (AES) RM0438
992/2187 RM0438 Rev 8
Bit 3 BUSY: Busy
This flag indicates whether AES is idle or busy during GCM payload encryption phase:
0: Idle
1: Busy
When the flag indicates “idle”, the current GCM encryption processing may be suspended to
process a higher-priority message. In other chaining modes, or in GCM phases other than payload
encryption, the flag must be ignored for the suspend process.
Bit 2 WRERR: Write error
This flag indicates the detection of an unexpected write operation to the AES_DINR register (during
computation or data output phase):
0: Not detected
1: Detected
The flag is set by hardware. It is cleared by software upon setting the ERRC bit of the AES_CR
register.
Upon the flag setting, an interrupt is generated if enabled through the ERRIE bit of the AES_CR
register.
The flag setting has no impact on the AES operation. Unexpected write is ignored.
Bit 1 RDERR: Read error flag
This flag indicates the detection of an unexpected read operation from the AES_DOUTR register
(during computation or data input phase):
0: Not detected
1: Detected
The flag is set by hardware. It is cleared by software upon setting the ERRC bit of the AES_CR
register.
Upon the flag setting, an interrupt is generated if enabled through the ERRIE bit of the AES_CR
register.
The flag setting has no impact on the AES operation. Unexpected read returns zero.
Bit 0 CCF: Computation completed flag
This flag indicates whether the computation is completed:
0: Not completed
1: Completed
The flag is set by hardware upon the completion of the computation. It is cleared by software, upon
setting the CCFC bit of the AES_CR register.
Upon the flag setting, an interrupt is generated if enabled through the CCFIE bit of the AES_CR
register.
The flag is significant only when the DMAOUTEN bit is 0. It may stay high when DMA_EN is 1.

RM0438 Rev 8 993/2187
RM0438 AES hardware  accelerator (AES)
1000
29.7.3 AES data input register (AES_DINR)
Address offset: 0x08
Reset value: 0x0000 0000
Only 32-bit access type is supported.
29.7.4 AES data output register (AES_DOUTR)
Address offset: 0x0C
Reset value: 0x0000 0000
Only 32-bit read access type is supported.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
DIN[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
DIN[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 DIN[31:0]: Input data word
A four-fold sequential write to this bitfield during the input phase results in writing a complete 128-bit
block of input data to the AES peripheral. From the first to the fourth write, the corresponding data
weights are [127:96], [95:64], [63:32], and [31:0]. Upon each write, the data from the 32-bit input
buffer are handled by the data swap block according to the DATATYPE[1:0] bitfield, then written into
the AES core 128-bit input buffer.
The data signification of the input data block depends on the AES operating mode:
- Mode 1 (encryption): plaintext
- Mode 2 (key derivation): the bitfield is not used (AES_KEYRx registers used for input)
- Mode 3 (decryption): ciphertext
The data swap operation is described in Section 29.4.13: AES data registers and data swapping on
page 983.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
DOUT[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
DOUT[15:0]
rrrrrrrrrrrrrrrr

AES hardware accelerator (AES) RM0438
994/2187 RM0438 Rev 8
29.7.5 AES key regi ster 0 (AES_KEYR0)
Address offset: 0x10
Reset value: 0x0000 0000
29.7.6 AES key regi ster 1 (AES_KEYR1)
Address offset: 0x14
Reset value: 0x0000 0000
Bits 31:0 DOUT[31:0]: Output data word
This read-only bitfield fetches a 32-bit output buffer. A four-fold sequential read of this bitfield, upon
the computation completion (CCF set), virtually reads a complete 128-bit block of output data from
the AES peripheral. Before reaching the output buffer, the data produced by the AES core are
handled by the data swap block according to the DATATYPE[1:0] bitfield.
Data weights from the first to the fourth read operation are: [127:96], [95:64], [63:32], and [31:0].
The data signification of the output data block depends on the AES operating mode:
- Mode 1 (encryption): ciphertext
- Mode 2 (key derivation): the bitfield is not used
- Mode 3 (decryption): plaintext
The data swap operation is described in Section 29.4.13: AES data registers and data swapping on
page 983.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
KEY[31:16]
wwwwwwwwwwwwwwww
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
KEY[15:0]
wwwwwwwwwwwwwwww
Bits 31:0 KEY[31:0]: Cryptographic key, bits [31:0]
This write-only bitfield contains the bits [31:0] of the AES encryption or decryption key, depending on
the operating mode:
- In Mode 1 (encryption), Mode 2 (key derivation): the value to write into the bitfield is the encryption
key.
- In Mode 3 (decryption): the value to write into the bitfield is the encryption key to be derived before
being used for decryption.
The AES_KEYRx registers may be written only when KEYSIZE value is correct and when the AES
peripheral is disabled (EN bit of the AES_CR register cleared).  Note that, if, the key is directly
loaded to AES_KEYRx registers (hence writes to key register is ignored and KEIF is set).
Refer to Section 29.4.14: AES key registers on page 985 for more details.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
KEY[63:48]
wwwwwwwwwwwwwwww
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
KEY[47:32]
wwwwwwwwwwwwwwww

RM0438 Rev 8 995/2187
RM0438 AES hardware  accelerator (AES)
1000
29.7.7 AES key regi ster 2 (AES_KEYR2)
Address offset: 0x18
Reset value: 0x0000 0000
29.7.8 AES key regi ster 3 (AES_KEYR3)
Address offset: 0x1C
Reset value: 0x0000 0000
29.7.9 AES initialization vec tor register 0 (AES_IVR0)
Address offset: 0x20
Reset value: 0x0000 0000
Bits 31:0 KEY[63:32]: Cryptographic key, bits [63:32]
Refer to the AES_KEYR0 register for description of the KEY[255:0] bitfield.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
KEY[95:80]
wwwwwwwwwwwwwwww
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
KEY[79:64]
wwwwwwwwwwwwwwww
Bits 31:0 KEY[95:64]: Cryptographic key, bits [95:64]
Refer to the AES_KEYR0 register for description of the KEY[255:0] bitfield.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
KEY[127:112]
w w w w w w ww w w ww www w
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
KEY[111:96]
w w w w w w ww w w ww www w
Bits 31:0 KEY[127:96]: Cryptographic key, bits [127:96]
Refer to the AES_KEYR0 register for description of the KEY[255:0] bitfield.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
IVI[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
IVI[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

AES hardware accelerator (AES) RM0438
996/2187 RM0438 Rev 8
29.7.10 AES initialization vector register 1 (AES_IVR1)
Address offset: 0x24
Reset value: 0x0000 0000
29.7.11 AES initialization vector register 2 (AES_IVR2)
Address offset: 0x28
Reset value: 0x0000 0000
29.7.12 AES initialization vector register 3 (AES_IVR3)
Address offset: 0x2C
Reset value: 0x0000 0000
Bits 31:0 IVI[31:0]: Initialization vector input, bits [31:0]
Refer to Section 29.4.15: AES initialization vector registers on page 985 for description of the
IVI[127:0] bitfield.
The initialization vector is only used in chaining modes other than ECB.
The AES_IVRx registers may be written only when the AES peripheral is disabled
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
IVI[63:48]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
IVI[47:32]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 IVI[63:32]: Initialization vector input, bits [63:32]
Refer to the AES_IVR0 register for description of the IVI[128:0] bitfield.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
IVI[95:80]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
IVI[79:64]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 IVI[95:64]: Initialization vector input, bits [95:64]
Refer to the AES_IVR0 register for description of the IVI[128:0] bitfield.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
IVI[127:112]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
IVI[111:96]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 997/2187
RM0438 AES hardware  accelerator (AES)
1000
29.7.13 AES key regi ster 4 (AES_KEYR4)
Address offset: 0x30
Reset value: 0x0000 0000
29.7.14 AES key regi ster 5 (AES_KEYR5)
Address offset: 0x34
Reset value: 0x0000 0000
29.7.15 AES key regi ster 6 (AES_KEYR6)
Address offset: 0x38
Reset value: 0x0000 0000
Bits 31:0 IVI[127:96]: Initialization vector input, bits [127:96]
Refer to the AES_IVR0 register for description of the IVI[128:0] bitfield.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
KEY[159:144]
wwwwwwwwwwwwwwww
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
KEY[143:128]
wwwwwwwwwwwwwwww
Bits 31:0 KEY[159:128]: Cryptographic key, bits [159:128]
Refer to the AES_KEYR0 register for description of the KEY[255:0] bitfield.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
KEY[191:176]
wwwwwwwwwwwwwwww
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
KEY[175:160]
wwwwwwwwwwwwwwww
Bits 31:0 KEY[191:160]: Cryptographic key, bits [191:160]
Refer to the AES_KEYR0 register for description of the KEY[255:0] bitfield.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
KEY[223:208]
wwwwwwwwwwwwwwww
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
KEY[207:192]
wwwwwwwwwwwwwwww
Bits 31:0 KEY[223:192]: Cryptographic key, bits [223:192]
Refer to the AES_KEYR0 register for description of the KEY[255:0] bitfield.

AES hardware accelerator (AES) RM0438
998/2187 RM0438 Rev 8
29.7.16 AES key regi ster 7 (AES_KEYR7)
Address offset: 0x3C
Reset value: 0x0000 0000
Note: The key registers from 4 to 7 are used only when the key length of 256 bits is selected. They
have no effect when the key length of 128 bits is selected (only key registers 0 to 3 are used
in that case).
29.7.17 AES suspend re gisters (AES_SUSPxR)
Address offset: 0x040 + 0x4 * x, (x = 0 to 7)
Reset value: 0x0000 0000
These registers contain the complete internal register states of the AES processor when the
AES processing of the current task is suspended to process a higher-priority task.
Upon suspend, the software reads and saves the AES_SUSPxR register contents (where x
is from 0 to 7) into memory, before using the AES processor for the higher-priority task.
Upon completion, the software restores the saved contents back into the corresponding
suspend registers, before resuming the original task.
These registers can be read only when AES is enabled. Reading these registers while AES
is disabled returns 0x0000 0000.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
KEY[255:240]
wwwwwwwwwwwwwwww
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
KEY[239:224]
wwwwwwwwwwwwwwww
Bits 31:0 KEY[255:224]: Cryptographic key, bits [255:224]
Refer to the AES_KEYR0 register for description of the KEY[255:0] bitfield.
Note: These registers are used only when GCM, GMAC, or CCM chaining mode is selected.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
SUSP[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
SUSP[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 SUSP[31:0]: AES suspend
Upon suspend operation, this bitfield of the corresponding AES_SUSPxR register takes the value of
one of internal AES registers.

RM0438 Rev 8 999/2187
RM0438 AES hardware  accelerator (AES)
1000
29.7.18 AES register map
[Table 235](../tables/table_235.md). AES register map and reset values
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
0x000
AES_CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
NPBLB[3:0]
Res.
KEYSIZE
Res.
CHMOD[2]
Res.
GCMPH[1:0]
DMAOUTEN
DMAINEN
ERRIE
CCFIE
ERRC
CCFC
CHMOD[1:0]
MODE[1:0]
DATATYPE[1:0]
EN
R e s e t  v a l u e 0000 0 0 000000000000000
0x004
AES_SR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
BUSY
WRERR
RDERR
CCF
Reset value 0000
0x008
AES_DINR DIN[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x00C
AES_DOUTR DOUT[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x010
AES_KEYR0 KEY[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x014
AES_KEYR1 KEY[63:32]
R e s e t  v a l u e 00000000000000000000000000000000
0x018
AES_KEYR2 KEY[95:64]
R e s e t  v a l u e 00000000000000000000000000000000
0x01C
AES_KEYR3 KEY[127:96]
R e s e t  v a l u e 00000000000000000000000000000000
0x020
AES_IVR0 IVI[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x024
AES_IVR1 IVI[63:32]
R e s e t  v a l u e 00000000000000000000000000000000
0x028
AES_IVR2 IVI[95:64]
R e s e t  v a l u e 00000000000000000000000000000000
0x02C
AES_IVR3 IVI[127:96]
R e s e t  v a l u e 00000000000000000000000000000000
0x030
AES_KEYR4 KEY[159:128]
R e s e t  v a l u e 00000000000000000000000000000000
0x034
AES_KEYR5 KEY[191:160]
R e s e t  v a l u e 00000000000000000000000000000000
0x038
AES_KEYR6 KEY[223:192]
R e s e t  v a l u e 00000000000000000000000000000000
0x03C
AES_KEYR7 KEY[255:224]
R e s e t  v a l u e 00000000000000000000000000000000
0x040
AES_SUSP0R SUSP[31:0]
R e s e t  v a l u e 00000000000000000000000000000000

AES hardware accelerator (AES) RM0438
1000/2187 RM0438 Rev 8
Refer to Section 2.3 on page 86 for the register boundary addresses.
0x044
AES_SUSP1R SUSP[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x048
AES_SUSP2R SUSP[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x04C
AES_SUSP3R SUSP[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x050
AES_SUSP4R SUSP[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x054
AES_SUSP5R SUSP[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x058
AES_SUSP6R SUSP[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x05C
AES_SUSP7R SUSP[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x060-
0x3FF Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
[Table 235](../tables/table_235.md). AES register map and reset values (continued)
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
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 196: Architectural Diagram](../figures/figure_196.md)
* [Figure 197: Architectural Diagram](../figures/figure_197.md)
* [Figure 198: Architectural Diagram](../figures/figure_198.md)
* [Figure 199: Architectural Diagram](../figures/figure_199.md)
* [Figure 200: Architectural Diagram](../figures/figure_200.md)
* [Figure 201: Architectural Diagram](../figures/figure_201.md)
* [Figure 202: Architectural Diagram](../figures/figure_202.md)
* [Figure 203: Architectural Diagram](../figures/figure_203.md)
* [Figure 204: Architectural Diagram](../figures/figure_204.md)
* [Figure 205: Architectural Diagram](../figures/figure_205.md)
* [Figure 206: Architectural Diagram](../figures/figure_206.md)
* [Figure 207: Architectural Diagram](../figures/figure_207.md)
* [Figure 208: Architectural Diagram](../figures/figure_208.md)
* [Figure 209: Architectural Diagram](../figures/figure_209.md)
* [Figure 210: Architectural Diagram](../figures/figure_210.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 226: Configuration Matrix](../tables/table_226.md)
* [Table 227: Configuration Matrix](../tables/table_227.md)
* [Table 228: Configuration Matrix](../tables/table_228.md)
* [Table 229: Configuration Matrix](../tables/table_229.md)
* [Table 230: Configuration Matrix](../tables/table_230.md)
* [Table 231: Configuration Matrix](../tables/table_231.md)
* [Table 232: Configuration Matrix](../tables/table_232.md)
* [Table 233: Configuration Matrix](../tables/table_233.md)
* [Table 234: Configuration Matrix](../tables/table_234.md)
* [Table 235: Configuration Matrix](../tables/table_235.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)