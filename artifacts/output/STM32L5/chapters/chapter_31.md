# Chapter 31: On-the-fly decryption engine (OTFDEC)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 31: On-the-fly decryption engine (OTFDEC).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 1023 - 1045
* **Taxonomy Section**: SECURITY
* **Parent IP Module**: [Cryptographic Processor (CRYP)](../security/cryp.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 1023/2187
RM0438 On-the-fly decryption engine (OTFDEC)
1045
31 On-the-fly decryption engine (OTFDEC)
31.1 OTFDEC introduction
OTFDEC allows on-the-fly decryption of the AHB traffic based on the read request address
information. Four independent and non-overlapping encrypted regions can be defined in
OTFDEC.
OTFDEC uses AES-128 in counter mode to achieve the lowest possible latency. As a
consequence, each time the content of one encrypted region is changed, the entire region
must be re-encrypted with a different cryptographic context (key or initialization vector). This
constraint makes OTFDEC suitable to decrypt read-only data or code, stored in external
NOR flash.
Note: When OTFDEC is used in conjunction with OCTOSPI, it is mandatory to access the flash
memory using the memory-mapped mode of the flash memory controller.
When security is enabled in the product, OTFDEC can be programmed only by a secure
host.
31.2 OTFDEC main features
• On-the-fly 128-bit decryption during the OCTOSPI Memory-mapped read operations
(single or multiple).
– Use of AES in counter (CTR) mode, with two 128-bit keystream buffers
– Support for any read size
– Physical address of the reads used for the encryption/decryption
• Up to four independent encrypted regions
– Granularity of the region definition: 4096 bytes
– Region configuration wr ite-locking mechanism
– Each region has its own 128-bit key, two bytes firmware version, and eight bytes
application-defined nonce. At least one of those must be changed each time an
encryption is performed by the application.
• Encryption keys confidentiality and integrity protection
– Write-only registers, with software locking mechanism
– Availability of 8-bit CRC as public key information
• Support for OCTOSPI pre-fetching mechanism
• Possibility to select an enhanced encryption mode to add a proprietary layer of
protection on top of AES stream cipher (execute only)
• Privileged-aware AMBA AHB slave peripheral, accessible through 32-bit word single
accesses only (otherwise an AHB bus error is generated, and write accesses are
ignored)
• Secure only programming if TrustZone security is enabled in the product
• Encryption mode

On-the-fly decryption engine (OTFDEC) RM0438
1024/2187 RM0438 Rev 8
31.3 OTFDEC functional description
31.3.1 OTFDEC block diagram
[Figure 225](../figures/figure_225.md). OTFDEC block diagram
1. otfdec_tzen
31.3.2 OTFDEC internal signals
[Table 241](../tables/table_241.md) describes a list of useful to know internal signals available at OTFDEC level, not
at the product level (on pads).
OCTOSPI (Slave)
AHB clock domain
Banked registers
(x = 1 to 4)
RxKEYR
RxADDR
RxCFGR Control
Logic
AES-CTR
AHB lite
slave
interface
Key
IVsRxNONCE
...
Keystream[1]
Keystream[0]
AHB memory
interface
OTFDEC
32-bit AHB bus
To / from
control logic
Other AHB signals
32-bit AHB bus
AHB memory
interface Other AHB signals
otfdec_it IRQ
interface
Proprietary
XOR
hrdata_o[31:0] hrdata_in[31:0]
See (1)
otfdec_hclk
hreadyout_i
haddr[31:0]haddr[31:0]
hreadyout_o
XOR
[Table 241](../tables/table_241.md). OTFDEC internal input/output signals
Signal name Signal type Description
otfdec_hclk Digital input AHB bus clock
otfdec_it Digital output OTFDEC global interrupt request
otfdec_tzen Digital input OTFDEC TrustZone enable, controlling TrustZone features of the
peripheral (TZEN)

RM0438 Rev 8 1025/2187
RM0438 On-the-fly decryption engine (OTFDEC)
1045
The TZEN option bit in FLASH is used to activate TrustZone in the device.
• TZEN = 1: TrustZone security is enabled in the product.
• TZEN = 0: TrustZone security is disabled in the product.
31.3.3 OTFDEC on-the-fly decryption
Introduction
Typical usage for OTFDEC is shown on [Figure 226](../figures/figure_226.md).
[Figure 226](../figures/figure_226.md). Typical OTFDEC use in a SoC
Original purpose of OTFDEC is to protect the confidentiality of read-only firmware libraries
stored in external SPI NOR flash devices.
A special locking scheme is available in OTFDEC in order to protect the integrity of the
decryption keys and also to protect the other configurations against software denial of
services attacks. OTFDEC access to most registers can be made privileged-only by setting
PRIV bit in OTFDEC_PRIVCFGR register. OTFDEC is only writeable by TrustZone CPU,
when TrustZone security is activated.
When OTFDEC is used in conjunction with OCTOSPI, it is mandatory to read the flash
memory using the Memory-mapped mode of the flash controller.
On top of decrypting on-the-fly, OTFDEC can also encrypt 32-bit word at a time (see
Section 31.5.3: Encrypting for OTFDEC for more details).
OTFDEC architecture
OTFDEC analyzes all AHB read transfers on the associated AHB bus. If the read request is
within one of the four regions programmed in OTFDEC, the control logic triggers a
keystream computation based on AES algorithm in counter mode. This keystream is then
used to decrypt on-the-fly the data present in the read transfer from the OCTOSPI AHB
master, tying low the HREADYOUT signal of this master while the keystream information is
being computed (this takes up to 11 cycles). Any accesses outside the enabled OTFDEC
regions belong to a non-encrypted region.
Each OTFDEC region is programmed through OTFDEC_RxCFGR,
OTFDEC_RxSTARTADDR, OTFDEC_RxENDADDR, OTFDEC_RxNONCER and
MS48973V1
Instruction
cache
data/system
cache
SPI NOR
Flash
OCTOSPI
SPI bus
SoC boundary
OTFDEC

On-the-fly decryption engine (OTFDEC) RM0438
1026/2187 RM0438 Rev 8
OTFDEC_RxKEYR registers, where x = 1 to 4. In OTFDEC_RxCFGR, the MODE bits
define the OTFDEC operating mode (standard or enhanced encryption).
Granularity for the region determination is 4096 bytes.
Note: Although OTFDEC does not prevent region overlapping, it is not a valid programming and it
must be avoided by application software.
OTFDEC can decrypt incremental or wrap bursts only if they do not cross the 4096-byte
aligned address boundaries.
31.3.4 OTFDEC usage of AES in counter mode decryption
[Figure 227](../figures/figure_227.md) shows how OTFDEC uses industry standard Advanced Encryption Standard
(AES) algorithm in counter chaining mode. This mode is specified by NIST in Special
Publication 800-38A, Recommendation for Block Cipher Modes of Operation.
[Figure 227](../figures/figure_227.md). AES CTR decryption flow
Every 128-bit data block, a special keystream information is computed using AES block
cipher, as defined below:
• initialization vector AES_IV[127:0] = RxNONCER1[31:0] || RxNONCER0[31:0] ||
0b0000 0000 0000 0000 || RxCFGR[31:16] || 0b00 || (x-1) || ReadAddress[31:4]
• key material AES_KEY[127:0] = RxKEYR3[31:0] || RxKEYR2[31:0] || RxKEYR1[31:0] ||
RxKEYR0[31:0]
Note: Above x is the RegionID of the se lected encrypted region (x=1 to 4).
ReadAddress is the AHB address of the encrypted data block, modulo 128-bit.
Resulting 128-bit keystream is XORed with 128-bit cipher text data to produce the 128-bit
clear text data.
• AES_DIN and AES_DOUT data blocks are constructed following the rule below (“|”
represents a binary concatenation):
AES_Dx[127:0]= AHB_word(@ | 0xC)[31:0] | AHB_word(@ | 0x8)[31:0] | AHB_word(@
| 0x4)[31:0] || AHB_word(@ | 0x0)[31:0], where @ is the hexadecimal address used to
compute the keystream (ReadAddress[31:4] above).
MS48969V1
AES Block cipher
encryption
AES_IV
Nonce   Version  Id  Address_0
AES_KEY
AES_DIN (cipher text 0)
AES_DOUT (plain text 0)
AES Block cipher
encryption
AES_IV
AES_DIN (cipher text 1)
AES_DOUT (plain text 1)
AES_KEY
Keystream_0 Keystream_1
Nonce   Version  Id  Address_1
128-bit
128-bit
128-bit
128-bit 128-bit
128-bit

RM0438 Rev 8 1027/2187
RM0438 On-the-fly decryption engine (OTFDEC)
1045
When the read request is not within an encrypted region, or the decryption is not enabled in
this region, the AHB data is not changed.
Note: When the application sets th e MODE bitfield to 11 in OTFDEC_RxCFGR, an additional layer
of protection is added on top of the AES stream cipher. This enhanced encryption mode can
only be used with instructions (execute-only region).
31.3.5 Flow control management
[Figure 228](../figures/figure_228.md) shows how OTFDEC manages one INCR4 AHB burst that corresponds to one
128-bit AES data block.
[Figure 228](../figures/figure_228.md). OTFDEC flow control overview (dual burst read request)
with the following notes:
1. OTFDEC enforces HREADY signal from the AHB master low as it is not ready to
decrypt data (keystream computation).
2. Thanks to the keystream buffer, OTFDEC can be ready to process a new batch of data
within 12 cycles in this configuration (120 MHz AHB clock, 104 MHz SPI bus delivering
2 bytes per SPI clock).
31.3.6 OTFDEC error management
OTFDEC automatically manages errors defined as below:
• Illegal read to OTFDEC_RxKEYR registers
• Illegal write to OTFDEC_RxKEYR registers while CONFIGLOCK or KEYLOCK = 1 in
OTFDEC_RxCFGR, while the access is secure. If the security is disabled in the
product, the same error occurs when the access is nonsecure.
• Illegal write to OTFDEC_RxCFGR, OTFDEC_RxSTARTADDR,
OTFDEC_RxENDADDR or OTFDEC_RxNONCER registers while CONFIGLOCK = 1
in OTFDEC_RxCFGR (x = 1 to 4), while the access is secure. If the security is disabled
in the product the same error occurs when the access is nonsecure.
• Illegal read to an execute-only region (MODE[1:0] = 11). Such illegal request returns
0x0, without bus error.
• Execution request to a region while encryption is enabled (ENC = 1). The request
returns 0x0, without bus error.
• Key error: read request to an encrypted region while its key registers are null or not
properly initialized (KEYCRC = 0x0). Source of the error can be an incorrect key
loading sequence (see KEYCRC in OTFDEC_RxCFGR) or it can be an abort event
AHB Clock
HADDR Add(A)
HREADY
Add(B) Add(C)
HRDATA Data(A) Data(B) Data(C) Data(D)
OTFDEC (AES) Keystream[0]
OTFDEC (XOR)
120MHz
Keystream[1]
XOR(A) XOR(B) XOR(C) XOR(D)
>12 cycles
1
2
MS48974V1

On-the-fly decryption engine (OTFDEC) RM0438
1028/2187 RM0438 Rev 8
(tamper detection, unauthorized debug connection, untrusted boot, RDP level
regression). Such read request returns 0x0, without bus error.
• Write to any registers while the access is nonsecure, if TrustZone security is enabled in
the product.
This last error is managed and cleared through TrustZone interrupt controller, as
described in the GTZC section of the product reference manual.
For these errors (except the last one), an interrupt can be generated if the SEIE, XONEIE or
KEIE bit is set in OTFDEC_IER register (see Section 31.4).
Note: After a key error, OTFDEC keys must be pr operly initialized again, and a reset of OTFDEC
may be needed if registers are locked.
31.4 OTFDEC interrupts
There are three independent maskable interrupt sources generated by the OTFDEC,
signaling following security events:
• Illegal read or write access to keys (SEIF flag), see Section 31.3.6
• Illegal write to a region configuration while CONFIGLOCK = 1 (SEIF flag), see
Section 31.3.6
• Read access to an execute-only region (MODE[1:0] = 11), triggering the XONEIF flag
• Executing while encryption is enabled (XONEIF flag)
• Key error (encrypted regions read as zero) triggering the KEIF flag, see Section 31.3.6.
Interrupt sources are connected to the same global interrupt request signal.
OTFDEC interrupt sources can be enabled/disabled by setting the corresponding SEIE,
XONEIE or KEIE bit in OTFDEC_IER, as described in [Table 242](../tables/table_242.md). Status of the interrupt
event is found in OTFDEC_ISR, and this event can be cleared using OTFDEC_ICR.
31.5 OTFDEC application information
31.5.1 OTFDEC initialization process
Introduction
One key aspect of OTFDEC is the trusted initialization of its registers, as it involves secret
keys. Two trusted initialization schemes are recommended here below.
[Table 242](../tables/table_242.md). OTFDEC interrupt requests
Interrupt
acronym Interrupt event Event flag (1)
1. The event flags are found in the OTFDEC_ISR register.
Enable
control bit Interrupt clear method
OTFDEC
Security error SEIF SEIE S et SEIF in OTFDEC_ICR
Execute-only
Execute while
encryption
XONEIF XONEIE Set XONEIF in OTFDEC_ICR
Key error KEIF KEIE Set KEIF in OTFDEC_ICR

RM0438 Rev 8 1029/2187
RM0438 On-the-fly decryption engine (OTFDEC)
1045
Note: Those sequences are for production code, as  during firmware development, it is not always
recommended to lock the key or the region configuration.
Writes to configuration registers are effective when the configuration locks allow it, even if
the region is enabled.
Initialization scheme 1: one key for all regions
In this scheme, one entity owns the secret key used to decrypt the four protected regions.
The recommended OTFDEC configuration sequence is described below:
1. For x = 1 to 4, write the correct MODE[1:0] value in OTFDEC_RxCFGR.
2. For x = 1 to 4, program OTFDEC_RxKEYR registers using the sequence described in
KEYCRC (to have a valid CRC). Warning as key registers are write only.
3. For x = 1 to 4, check the key CRC. If OK, set KEYLOCK bit in OTFDEC_RxCFGR. This
bit cannot be cleared (key registers in this region x are no more writable).
4. To do to decrypt a region x (task that does not necessarily have to be performed by the
entity that owns the decryption keys):
a) Verify if the key CRC corresponds to th e encrypted binary stored in the region.
b) Fill the detailed informatio n corresponding to this binary (nonce, start address, end
address, version number).
c) Enable decryption of this region using REG_EN.
d) Set CONFIGLOCK bit in OTFDEC_R xCFGR. This bit cannot be cleared (the
region configuration is no more writable).
Caution: For a given region, when MODE bits are changed, the key registers and associated CRC
are cleared by hardware. As a consequence, step 1 above must be done before step 2, and
MODE bits must not be modified after step 2.
Initialization scheme 2: one key per region
In this scheme, one entity can own the secret used to decrypt one (or more) protected
region. The recommended OTFDEC configuration sequence is described below:
1. To do to decrypt a region x (this task must be performed by the entity that owns the
corresponding key):
a) Write the correct MODE[1:0] value in OTFDEC_R xCFGR.
b) Program OTFDEC_RxKEYR  registers using the sequence described in KEYCRC
(to have a valid CRC). Warning as key registers are write only.
c) Check the key CRC. If OK, set KEYLOCK bit in OTFDEC_R xCFGR. This bit
cannot be cleared (key registers are no more writable).
d) Fill the detailed informatio n corresponding to the protected firmware (nonce, start
address, end address, version number).
e) Enable decryption of this region using REG_EN.
f) Set CONFIGLOCK bit in OTFDEC_R xCFGR. This bit cannot be cleared (the
region configuration is no more writable).
Caution: For a given region, when MODE bits are changed, the key registers and associated CRC
are cleared by hardware. As a consequence step a) above must be done before step b),
and MODE bits must not be modified after step b).

On-the-fly decryption engine (OTFDEC) RM0438
1030/2187 RM0438 Rev 8
31.5.2 OTFDEC and power management
Each time OTFDEC is reset, the correct key loading sequence described in Section 31.5.1
must be performed (in this case KEYCRC = 0 in OTFDEC_RxCFGR).
It is recommended for application software to verify this point each time OTFDEC is reset by
hardware.
31.5.3 Encrypting for OTFDEC
Code and data standard encryption
OTFDEC uses standard AES in counter mode when processing a binary stored in a
protected region with MODE[1:0] = 10. When this mode is selected, any AES compatible
hardware accelerator or library can be used to encrypt those protected libraries. OTFDEC
can be used as well, as described in enhanced encryption section below (with
MODE[1:0] = 10).
Definition and endianness of the AES inputs and outputs are defined in Section 31.3.4:
OTFDEC usage of AES in counter mode decryption.
Enhanced encryption with OTFDEC
OTFDEC uses a proprietary layer of protection on top of the standard AES in counter mode
when processing a code stored in a protected region with MODE[1:0] = 11.
Enhanced encryption mode can be used to increase the robustness against tampering.
Recommended sequence to encrypt using OTFDEC is described below:
1. The application in charge of the encrypti on sets the ENC bit in OTFDEC_CR. This
application must run in TrustZone secure mode when TrustZone security is enabled in
the product. If PRIV bit is set in OTFDEC_PRIVCFGR, this application must be
privileged.
2. Encryption application initia lizes OTFDEC as described in Section 31.5.1: OTFDEC
initialization process. OCTOSPI must also be properly clocked, so that OTFDEC is fully
functional in encryption mode. This step can also be done before step 1.
3. Encryption application writes 32-bit of clear-text data at the expected protected
address, then reads it back encrypted at the same address to store it in RAM. Note that
this data stays inside the device, as it is intercepted by OTFDEC in encryption mode.
4. Encryption application goes back to prev ious step (changing the address) until the
whole binary is processed.
5. Encryption application clears the ENC bi t in OTFDEC_CR. Another application can
then take the encrypted binary and flash it to the correct address in external flash.
There are few important notes about this procedure:
• Encryption granularity is 32-bit (single 32-bit access is mandatory).
• While ENC bit is set, reads to non-encrypted regions return normal data (such as no
encryption nor decryption). While in encryption mode, no access to OCTOSPI
(including registers) must be done. This is because the OTFDEC cuts the
communication with OCTOPSI while ENC bit is set.
• OTFDEC does not support execution while ENC = 1 (only encrypted data reads). Upon
illegal execution detection a XONEIF flag is raised and zero is returned.

RM0438 Rev 8 1031/2187
RM0438 On-the-fly decryption engine (OTFDEC)
1045
31.5.4 OTFDEC key CRC source code
Below is the CRC source code that can be used to compare with the result of the
computation provided by OTFDEC in KEYCRC bitfield after loading the keys in
OTFDEC_RxKEYR registers.
uint8_t getCRC(uint32_t * keyin)
{
const uint8_t CRC7_POLY = 0x7;
const uint32_t key_strobe[4] = {0xAA55AA55, 0x3, 0x18, 0xC0};
uint8_t  i, j, k, crc = 0x0;
uint32_t  keyval;
for (j = 0; j < 4; j++)
{
keyval = *(keyin+j);
if (j == 0)
{
keyval ^= key_strobe[0];
}
else
{
keyval ^= (key_strobe[j] << 24) | (crc << 16) | (key_strobe[j] << 8)
| crc;
}
for (i = 0, crc = 0; i < 32; i++)
{
k = (((crc >> 7) ^ (keyval >> (31-i))&0xF)) & 1;
crc <<= 1;
if (k)
{
crc ^= CRC7_POLY;
}
}
crc^=0x55;
}
return crc;
}

On-the-fly decryption engine (OTFDEC) RM0438
1032/2187 RM0438 Rev 8
31.6 OTFDEC registers
31.6.1 OTFDEC control register (OTFDEC_CR)
Address offset: 0x0
Reset value: 0x0000 0000
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
Unprivileged reads return zero and unprivileged writes are ignored if PRIV bit is set in
OTFDEC_PRIVCFGR.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. ENC
rw
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 ENC: Encryption mode bit
When this bit is set, OTFDEC is used in encryption mode, during which application can write
clear text data then read back encrypted data. When this bit is cleared (default), OTFDEC is
used in decryption mode, during which application only read back decrypted data. For both
modes, cryptographic context (keys, nonces, firmware versions) must be properly initialized.
When this bit is set, only data accesses are allowed (zeros are returned otherwise, and
XONEIF is set). When MODE = 11, enhanced encryption mode is automatically selected.
0: OTFDEC working in decryption mode
1: OTFDEC working in encryption mode
Note: When ENC bit is set, no access to  OCTOSPI must be done (registers and
Memory-mapped region).

RM0438 Rev 8 1033/2187
RM0438 On-the-fly decryption engine (OTFDEC)
1045
31.6.2 OTFDEC privileged access control configuration register
(OTFDEC_PRIVCFGR)
Address offset: 0x10
Reset value: 0x0000 0000
31.6.3 OTFDEC region x configur ation register (OTFDEC_RxCFGR)
Address offset: 0x20 + 0x30 * (x - 1), (x = 1 to 4)
Reset value: 0x0000 0000
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
Unprivileged reads return zero and unprivileged writes are ignored if PRIV bit is set in
OTFDEC_PRIVCFGR.
Writes are ignored if CONFIGLOCK bit is set to 1.
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. PRIV
rw
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 PRIV: Privileged access protection.
0: No additional protection is added on OTFDEC register accesses.
1: An additional protection is added when accessing all registers except
OTFDEC_PRIVCFGR:
– Unprivileged read accesses to registers return zeros
– Unprivileged write accesses to registers are ignored.
Note: This bit can only be written in privile ged mode. There is no limitations on reads.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REG_VERSION[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
KEYCRC[7:0] Res. Res. MODE[1:0] Res. KEYLOCK CONFI
GLOCK
REG_
EN
r rrrr r r r r wr w r s r sr w

On-the-fly decryption engine (OTFDEC) RM0438
1034/2187 RM0438 Rev 8
Bits 31:16 REG_VERSION[15:0]: region firmware version
This 16-bit bitfield must be correctly initialized before the region corresponding REG_EN bit is
set in OTFDEC_RxCFGR.
Bits 15:8 KEYCRC[7:0]: region key 8-bit CRC
When KEYLOCK = 0, KEYCRC bitfield is automatically computed by hardware while loading
the key of this region in this exact sequence: KEYR0 then KEYR1 then KEYR2 then finally
KEYR3 (all written once). A new computation starts as soon as a new valid sequence is
initiated, and KEYCRC is read as zero until a valid sequence is completed.
When KEYLOCK = 1, KEYCRC remains unchanged until the next reset.
CRC computation is an 8-bit checksum using the standard CRC-8-CCITT algorithm
X8 + X2 + X + 1 (according the convention). Source code is available in Section 31.5.4.
This field is read only.
Note: CRC information is updated only after the last bit of the key has been written.
Bits 7:6 Reserved, must be kept at reset value.
Bits 5:4 MODE[1:0]: operating mode
This bitfield selects the OTFDEC operating mode for this region:
10: All read accesses are decrypted (instruction or data).
11: Enhanced encryption mode is activated, and only instruction accesses are decrypted
Others: Reserved
When MODE ≠ 11, the standard AES encryption mode is activated.
When either of the MODE bits are changed, the region key and associated CRC are zeroed.
Bit 3 Reserved, must be kept at reset value.
Bit 2 KEYLOCK: region key lock
0: Writes to this region KEYRx registers are allowed.
1: Writes to this region KEYRx registers are ignored until next OTFDEC reset. KEYCRC
bitfield is locked.
Note: This bit is set once: if this bit is set, it  can only be reset to 0 if the OTFDEC is reset.
Bit 1 CONFIGLOCK: region config lock
0: Writes to this region OTFDEC_RxCFGR, OTFDEC_RxSTARTADDR,
OTFDEC_RxENDADDR and OTFDEC_RxNONCERy registers are allowed.
1: Writes to this region OTFDEC_RxCFGR, OTFDEC_RxSTARTADDR,
OTFDEC_RxENDADDR and OTFDEC_RxNONCERy registers are ignored until next
OTFDEC reset.
Note: This bit is set once. If this bit is set, it can only be reset to 0 if OTFDEC is reset. Setting
this bit forces KEYLOCK bit to 1.
Bit 0 REG_EN: region on-the-fly decryption enable
0: On-the-fly decryption is disabled for this region.
1: On-the-fly decryption is enabled for this region. Data are XORed with the corresponding
keystream.
Note: Garbage is decrypted if region context (version, key, nonce) is not valid when this
bit is set.

RM0438 Rev 8 1035/2187
RM0438 On-the-fly decryption engine (OTFDEC)
1045
31.6.4 OTFDEC region x start address register
(OTFDEC_RxSTARTADDR)
Address offset: 0x24 + 0x30 * (x - 1), (x = 1 to 4)
Reset value: 0x0000 0000
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
Unprivileged reads return zero and unprivileged writes are ignored if PRIV bit is set in
OTFDEC_PRIVCFGR.
31.6.5 OTFDEC region x end addre ss register (OTFDEC_RxENDADDR)
Address offset: 0x28 + 0x30 * (x - 1), (x = 1 to 4)
Reset value: 0x0000 0FFF
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
Unprivileged reads return zero and unprivileged writes are ignored if PRIV bit is set in
OTFDEC_PRIVCFGR.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REG_START_ADDR[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
REG_START_ADDR[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 REG_START_ADDR[31:0]: Region AHB start address
This register must be written before the region corresponding REG_EN bit in the
OTFDEC_RxCFGR register is set.
Writing to this register is discarded if performed while the region CONFIGLOCK bit in the
OTFDEC_RxCFGR register is set.
Note: When determining the region the first 12 bits  (LSB) and the last 4 bits (MSB) are ignored.
When this register is accessed in read the 4 MSB bits and the 12 LSB bits return zeros .
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REG_END_ADDR[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
REG_END_ADDR[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

On-the-fly decryption engine (OTFDEC) RM0438
1036/2187 RM0438 Rev 8
31.6.6 OTFDEC region x nonce re gister 0 (OTFDEC_RxNONCER0)
Address offset: 0x2C + 0x30 * (x - 1), (x = 1 to 4)
Reset value: 0x0000 0000
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
Unprivileged reads return zero and unprivileged writes are ignored if PRIV bit is set in
OTFDEC_PRIVCFGR.
Bits 31:0 REG_END_ADDR[31:0]: Region AHB end address
This register must be written before the region corresponding REG_EN bit in the
OTFDEC_RxCFGR register is set, and OTFDEC_RxENDADDR must be strictly greater than
OTFDEC_RxSTARTADDR to be valid.
Writing to this register is discarded if performed while the region CONFIGLOCK bit in
OTFDEC_RxCFGR is set.
Note: When determining the region the first 12 bits  (LSB) and the last 4 bits (MSB) are ignored.
When this register is accessed in read the 4 MSB bits return zeros and the 12 LSB bits return ones.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REG_NONCE[31:16]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
REG_NONCE[15:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 REG_NONCE[31:0]: Region nonce, bits [31:0]
This register must be written before the region corresponding REG_EN bit in OTFDEC_RxCFGR is
set.
Writing is discarded in this register if performed while the region CONFIGLOCK bit in the
OTFDEC_RxCFGR is set.

RM0438 Rev 8 1037/2187
RM0438 On-the-fly decryption engine (OTFDEC)
1045
31.6.7 OTFDEC region x nonce re gister 1 (OTFDEC_RxNONCER1)
Address offset: 0x30 + 0x30 * (x - 1), (x = 1 to 4)
Reset value: 0x0000 0000
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
Unprivileged reads return zero and unprivileged writes are ignored if PRIV bit is set in
OTFDEC_PRIVCFGR.
31.6.8 OTFDEC region x key re gister 0 (OTFDEC_RxKEYR0)
Address offset: 0x34 + 0x30 * (x - 1), (x = 1 to 4)
Reset value: 0x0000 0000
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
Unprivileged writes are ignored if PRIV bit is set in OTFDEC_PRIVCFGR.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REG_NONCE[63:48]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
REG_NONCE[47:32]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 REG_NONCE[63:32]: Region nonce, bits [63:32]
Refer to the OTFDEC_RxNONCER0 register for description of the NONCE[63:0] bitfield.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REG_KEY[31:16]
w w w w w w ww w w ww www w
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
REG_KEY[15:0]
w w w w w w ww w w ww www w
Bits 31:0 REG_KEY[31:0]: Region key, bits [31:0]
This register must be written before the region corresponding REG_EN bit in
OTFDEC_RxCFGR is set.
Reading this register returns a zero value. Writing to this register is discarded if performed while the
region CONFIGLOCK or KEYLOCK bit is set in the OTFDEC_RxCFGR.
Note: When application successfully changes MODE bits in OTFDEC_RxCFGR and
OTFDEC_RxKEYR, and associated KEYCRC are erased.

On-the-fly decryption engine (OTFDEC) RM0438
1038/2187 RM0438 Rev 8
31.6.9 OTFDEC region x key re gister 1 (OTFDEC_RxKEYR1)
Address offset: 0x38 + 0x30 * (x - 1), (x = 1 to 4)
Reset value: 0x0000 0000
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
Unprivileged writes are ignored if PRIV bit is set in OTFDEC_PRIVCFGR.
31.6.10 OTFDEC region x key register 2 (OTFDEC_RxKEYR2)
Address offset: 0x3C + 0x30 * (x - 1), (x = 1 to 4)
Reset value: 0x0000 0000
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
Unprivileged writes are ignored if PRIV bit is set in OTFDEC_PRIVCFGR.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REG_KEY[63:48]
w w w w w w ww w w ww www w
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
REG_KEY[47:32]
w w w w w w ww w w ww www w
Bits 31:0 REG_KEY[63:32]: Region key, bits [63:32]
Refer to the OTFDEC_RxKEYR0 register for description of the KEY[127:0] bitfield.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REG_KEY[95:80]
w w w w w w ww w w ww www w
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
REG_KEY[79:64]
w w w w w w ww w w ww www w
Bits 31:0 REG_KEY[95:64]: Region key, bits [95:64]
Refer to the OTFDEC_RxKEYR0 register for description of the KEY[127:0] bitfield.

RM0438 Rev 8 1039/2187
RM0438 On-the-fly decryption engine (OTFDEC)
1045
31.6.11 OTFDEC region x key register 3 (OTFDEC_RxKEYR3)
Address offset: 0x40 + 0x30 * (x - 1), (x = 1 to 4)
Reset value: 0x0000 0000
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
Unprivileged writes are ignored if PRIV bit is set in OTFDEC_PRIVCFGR.
31.6.12 OTFDEC interrupt st atus register (OTFDEC_ISR)
Address offset: 0x300
Reset value: 0x0000 0000
Unprivileged reads return zero if PRIV bit is set in OTFDEC_PRIVCFGR.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
REG_KEY[127:112]
w w w w w w ww w w ww www w
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
REG_KEY[111:96]
w w w w w w ww w w ww www w
Bits 31:0 REG_KEY[127:96]: Region key, bits [127:96]
Refer to the OTFDEC_RxKEYR0 register for description of the KEY[127:0] bitfield.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
KEIF
XONEIF
SEIF
rrr
Bits 31:3 Reserved, must be kept at reset value.
Bit 2 KEIF: Key error interrupt flag status
This bit is set by hardware and read only by application. The bit is set when a read access
occurs on an encrypted region, while its key registers is null or not properly initialized
(KEYCRC = 0x0).
This bit is cleared when the application sets in OTFDEC_ICR the corresponding bit to 1.
0: OTFDEC operates properly.
1: Read access detected on an enabled encrypted region with its key registers null or not
properly initialized (KEYCRC = 0x0). OTFDEC returns a zeroed value for the read, and an
optional interrupt is generated if bit KEIE is set to 1 in OTFDEC_IER.
After KEIF is set any subsequent read to the region with bad key registers returns a zeroed
value. This state remains until those key registers are properly initialized (KEYCRC not
zero).

On-the-fly decryption engine (OTFDEC) RM0438
1040/2187 RM0438 Rev 8
31.6.13 OTFDEC interrupt clear register (OTFDEC_ICR)
Address offset: 0x304
Reset value: 0x0000 0000
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
Unprivileged writes are ignored if PRIV bit is set in OTFDEC_PRIVCFGR.
Bit 1 XONEIF: Execute-only execute-never error interrupt flag status
This bit is set by hardware and read only by application. This bit is set when a read access
and not an instruction fetch is detected on any encrypted region with MODE bits set to 11.
Lastly, XONEIF is also set when an execute access is detected while encryption mode is
enabled.
This bit is cleared when application sets in OTFDEC_ICR the corresponding bit to 1.
0: No execute-only error status. No interrupt pending.
1: Read access detected on one region with MODE bits set to 11 or execute access detected
while ENC = 1. OTFDEC returns a zeroed value for the illegal access, and an optional
interrupt is generated if bit XONEIE is set to 1 in OTFDEC_IER.
Bit 0 SEIF: Security error interrupt flag status
This bit is set by hardware and read only by application. This bit is set when at least one
security error has been detected.
This bit is cleared when application sets in OTFDEC_ICR the corresponding bit to 1.
0: No security error status. No interrupt pending.
1: Security error flag status, with interrupt pending. Actual interrupt generation is dependent
on OTFDEC_IER corresponding bit SEIE.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
KEIF
XONEIF
SEIF
www
Bits 31:3 Reserved, must be kept at reset value.

RM0438 Rev 8 1041/2187
RM0438 On-the-fly decryption engine (OTFDEC)
1045
31.6.14 OTFDEC interrupt en able register (OTFDEC_IER)
Address offset: 0x308
Reset value: 0x0000 0000
Nonsecure AHB write access (HNONSEC = 1) is discarded if the TrustZone security is
enabled in the product.
Unprivileged reads return zero and unprivileged writes are ignored if PRIV bit is set in
OTFDEC_PRIVCFGR.
Bit 2 KEIF: Key error interrupt flag clear
This bit is written by application, and always read as 0.
0: KEIF flag status is not affected.
1: KEIF flag status is cleared in OTFDEC_ISR.
Note: Clearing KEIF does not solve the source of  the problem (bad key registers). To be able
to access again any encrypted region, OTFDEC key registers must be properly
initialized again.
Bit 1 XONEIF: Execute-only execute-never error interrupt flag clear
This bit is written by application, and always read as 0.
0: XONEIF flag status is not affected.
1: XONEIF flag status is cleared in OTFDEC_ISR.
Bit 0 SEIF: Security error interrupt flag clear
This bit is written by application, and always read as 0.
0: SEIF flag status is not affected.
1: SEIF flag status is cleared in OTFDEC_ISR.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
KEIE
XONEIE
SEIE
rw rw rw
Bits 31:3 Reserved, must be kept at reset value.

On-the-fly decryption engine (OTFDEC) RM0438
1042/2187 RM0438 Rev 8
31.6.15 OTFDEC register map
Bit 2 KEIE: Key error interrupt enable
This bit is read and written by application. It controls the OTFDEC interrupt generation when
KEIF flag status is set.
0: Interrupt generation on key error flag KEIF is disabled (masked).
1: Interrupt generation on key error flag KEIF is enabled (not masked).
Bit 1 XONEIE: Execute-only execute-never error interrupt enable
This bit is read and written by application. It controls the OTFDEC interrupt generation when
XONEIF flag status is set.
0: Interrupt generation on execute-only error XONEIF is disabled (masked).
1: Interrupt generation on execute-only error XONEIF is enabled (not masked).
Bit 0 SEIE: Security error interrupt enable
This bit is read and written by application. It controls the OTFDEC interrupt generation when
SEIF flag status is set.
0: Interrupt generation on security error SEIF is disabled (masked).
1: Interrupt generation on security error SEIF is enabled (not masked).
[Table 243](../tables/table_243.md). OTFDEC register map and reset values
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
OTFDEC_CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ENC
Reset value 0
0x04-
0x0C Reserved Reserved
0x10
OTFDEC_
PRIVCFGR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PRIV
Reset value 0
0x14-
0x1C Reserved Reserved
0x20
OTFDEC_
R1CFGR1 REG1_VERSION[15:0] KEYCRC[7:0]
Res.
Res.
MODE[1:0]
KEYLOCK
CONFIGLOCK
REG_EN
R e s e t  v a l u e 0000000000000000000000000 00000
0x24
OTFDEC_
R1STARTADDR REG1_START_ADDR[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x28
OTFDEC_
R1ENDADDR REG1_END_ADDR[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x2C
OTFDEC_
R1NONCER0 REG1_NONCE[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x30
OTFDEC_
R1NONCER1 REG1_NONCE[63:32]
R e s e t  v a l u e 00000000000000000000000000000000
0x34
OTFDEC_
R1KEYR0 REG1_KEY[31:0]
R e s e t  v a l u e 00000000000000000000000000000000

RM0438 Rev 8 1043/2187
RM0438 On-the-fly decryption engine (OTFDEC)
1045
0x38
OTFDEC_
R1KEYR1 REG1_KEY[63:32]
R e s e t  v a l u e 00000000000000000000000000000000
0x3C
OTFDEC_
R1KEYR2 REG1_KEY[95:64]
R e s e t  v a l u e 00000000000000000000000000000000
0x40
OTFDEC_
R1KEYR3 REG1_KEY[127:96]
R e s e t  v a l u e 00000000000000000000000000000000
0x44 -
0x4C Reserved Reserved
0x50
OTFDEC_
R2CFGR REG2_VERSION[15:0] KEYCRC[7:0]
Res.
Res.
MODE[1:0]
KEYLOCK
CONFIGLOCK
REG_EN
R e s e t  v a l u e 0000000000000000000000000 00000
0x54
OTFDEC_
R2STARTADDR REG2_START_ADDR[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x58
OTFDEC_
R2ENDADDR REG2_END_ADDR[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x5C
OTFDEC_
R2NONCER0 REG2_NONCE[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x60
OTFDEC_
R2NONCER1 REG2_NONCE[63:32]
R e s e t  v a l u e 00000000000000000000000000000000
0x64
OTFDEC_
R2KEYR0 REG2_KEY[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x68
OTFDEC_
R2KEYR1 REG2_KEY[63:32]
R e s e t  v a l u e 00000000000000000000000000000000
0x6C
OTFDEC_
R2KEYR2 REG2_KEY[95:64]
R e s e t  v a l u e 00000000000000000000000000000000
0x70
OTFDEC_
R2KEYR3 REG2_KEY[127:96]
R e s e t  v a l u e 00000000000000000000000000000000
0x74 -
0x7C Reserved Reserved
0x80
OTFDEC_
R3CFGR REG3_VERSION[15:0] KEYCRC[7:0]
Res.
Res.
MODE[1:0]
KEYLOCK
CONFIGLOCK
REG_EN
R e s e t  v a l u e 0000000000000000000000000 00000
0x84
OTFDEC_
R3STARTADDR REG3_START_ADDR[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x88
OTFDEC_
R3ENDADDR REG3_END_ADDR[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
[Table 243](../tables/table_243.md). OTFDEC register map and reset values (continued)
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

On-the-fly decryption engine (OTFDEC) RM0438
1044/2187 RM0438 Rev 8
0x8C
OTFDEC_
R3NONCER0 REG3_NONCE[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x90
OTFDEC_
R3NONCER1 REG3_NONCE[63:32]
R e s e t  v a l u e 00000000000000000000000000000000
0x94
OTFDEC_
R3KEYR0 REG3_KEY[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x98
OTFDEC_
R3KEYR1 REG3_KEY[63:32]
R e s e t  v a l u e 00000000000000000000000000000000
0x9C
OTFDEC_
R3KEYR2 REG3_KEY[95:64]
R e s e t  v a l u e 00000000000000000000000000000000
0xA0
OTFDEC_
R3KEYR3 REG3_KEY[127:96]
R e s e t  v a l u e 00000000000000000000000000000000
0xA4 -
0xAC Reserved Reserved
0xB0
OTFDEC_
R4CFGR REG4_VERSION[15:0] KEYCRC[7:0]
Res.
Res.
MODE[1:0]
KEYLOCK
CONFIGLOCK
REG_EN
R e s e t  v a l u e 0000000000000000000000000 00000
0xB4
OTFDEC_
R4STARTADDR REG4_START_ADDR[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0xB8
OTFDEC_
R4ENDADDR REG4_END_ADDR[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0xBC
OTFDEC_
R4NONCER0 REG4_NONCE[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0xC0
OTFDEC_
R4NONCER1 REG4_NONCE[63:32]
R e s e t  v a l u e 00000000000000000000000000000000
0xC4
OTFDEC_
R4KEYR0 REG4_KEY[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0xC8
OTFDEC_
R4KEYR1 REG4_KEY[63:32]
R e s e t  v a l u e 00000000000000000000000000000000
0xCC
OTFDEC_
R4KEYR2 REG4_KEY[95:64]
R e s e t  v a l u e 00000000000000000000000000000000
0xD0
OTFDEC_
R4KEYR3 REG4_KEY[127:96]
R e s e t  v a l u e 00000000000000000000000000000000
0x0D4-
0x2FC Reserved Reserved
[Table 243](../tables/table_243.md). OTFDEC register map and reset values (continued)
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

RM0438 Rev 8 1045/2187
RM0438 On-the-fly decryption engine (OTFDEC)
1045
Refer to Section 2.3: Memory organization for the register boundary addresses.
0x300
OTFDEC_ISR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
KEIF
XONEIF
SEIF
Reset value 000
0x304
OTFDEC_ICR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
KEIF
XONEIF
SEIF
Reset value 000
0x308
OTFDEC_IER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
KEIE
XONEIE
SEIE
Reset value 000
[Table 243](../tables/table_243.md). OTFDEC register map and reset values (continued)
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
* [Figure 225: Architectural Diagram](../figures/figure_225.md)
* [Figure 226: Architectural Diagram](../figures/figure_226.md)
* [Figure 227: Architectural Diagram](../figures/figure_227.md)
* [Figure 228: Architectural Diagram](../figures/figure_228.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 241: Configuration Matrix](../tables/table_241.md)
* [Table 242: Configuration Matrix](../tables/table_242.md)
* [Table 243: Configuration Matrix](../tables/table_243.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)