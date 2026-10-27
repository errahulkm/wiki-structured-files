# Chapter 3: Boot configuration

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 3: Boot configuration.
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 97 - 99
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 97/2187
RM0438 Boot configuration
99
3 Boot configuration
At startup, a BOOT0 pin, nBOOT0 and NSBOOTADDx[24:0] / SECBOOTADD0[24:0] option
bytes are used to select the boot memory address which includes:
• Boot from any address in user flash
• Boot from system memory bootloader
• Boot from any address in embedded SRAM
• Boot from Root Security service (RSS)
The BOOT0 value may come from the PH3-BOOT0 pin or from an option bit depending on
the value of a user option bit to free the GPIO pad if needed.
Refer to [Table 6](../tables/table_6.md) and [Table 7](../tables/table_7.md) for boot modes when TrustZone is disabled and enabled
respectively.
When TrustZone is enabled by setting the TZEN option bit, the boot space must be in
secure area. The SECBOOTADD0[24:0] option bytes are used to select the boot secure
memory address.
A unique boot entry option can be selected by setting the BOOT_LOCK option bit. All other
boot options are ignored.
[Table 6](../tables/table_6.md). Boot modes when TrustZone is disabled (TZEN=0)
nBOOT0
FLASH_
OPTR[27]
BOOT0
pin PH3
nSWBOOT0
FLASH_
OPTR[26]
Boot address option-
bytes selection Boot area ST programmed
default value
- 0 1 NSBOOTADD0[24:0]
Boot address defined by
user option bytes
NSBOOTADD0[24:0]
Flash: 0x0800 0000
- 1 1 NSBOOTADD1[24:0]
Boot address defined by
user option bytes
NSBOOTADD1[24:0]
System bootloader:
0x0BF9 0000
1 - 0 NSBOOTADD0[24:0]
Boot address defined by
user option bytes
NSBOOTADD0[24:0]
Flash: 0x0800 0000
0 - 0 NSBOOTADD1[24:0]
Boot address defined by
user option bytes
NSBOOTADD1[24:0]
System bootloader:
0x0BF9 0000

Boot configuration RM0438
98/2187 RM0438 Rev 8
The boot address option bytes enables the possibility to program any boot memory address.
However, the allowed address space depends on flash read protection RDP level.
If the programmed boot memory address is out of the allowed memory mapped area when
RDP level is 0.5 or more, the default boot fetch address is forced to:
• 0x0800 0000 (when TZEN = 0)
• RSS (when TZEN = 1)
Refer to the [Table 8](../tables/table_8.md).
[Table 7](../tables/table_7.md). Boot modes when TrustZone is enabled (TZEN=1)
BOOT_
LOCK
nBOOT0
FLASH_
OPTR[27]
BOOT0
pin
PH3
nSWBOOT0
FLASH_
OPTR[26]
RSS
command
Boot address
option-bytes
selection
Boot area
ST
programme
d default
value
0
-0 1 0 SECBOOTADD0
[24:0]
Secure boot address
defined by user option
bytes
SECBOOTADD0
[24:0]
Flash:
0x0C00 0000
- 1 1 0 N/A RSS: 0x0FF8 0000 RSS:
0x0FF8 0000
1- 0 0 SECBOOTADD0
[24:0]
Secure boot address
defined by user option
bytes
SECBOOTADD0
[24:0]
Flash:
0x0C00 0000
0- 0 0 N / A RSS: RSS:
0x0FF8 0000
RSS:
0x0FF8 0000
-- - ≠ 0N / A RSS: RSS:
0x0FF8 0000
RSS:
0x0FF8 0000
1- - - - SECBOOTADD0
[24:0]
Secure boot address
defined by user option
bytes
SECBOOTADD0
[24:0]
Flash:
0x0C00 0000
[Table 8](../tables/table_8.md). Boot space versus RDP protection
RDP TZEN = 1 TZEN = 0
0 Any boot address Any boot address
0.5
Boot address only in:
RSS: 0x0FF80000
or secure flash: 0x0C000000 -
0x0C07 FFFF
Otherwise the boot address is forced to RSS
N/A
1 Any boot address
2
Boot address only in flash 0x0800 0000 -
0x0807 FFFF
Otherwise the forced boot address is:
0x0800 0000(1)

RM0438 Rev 8 99/2187
RM0438 Boot configuration
99
The BOOT0 value (either coming from the pin or the option bit) is latched upon reset
release. It is up to the user to set nBOOT0 or BOOT0 values to select the required boot
mode.
The BOOT0 pin or user option bit (depending on the nSWBOOT0 bit value in the
FLASH_OPTR register) is also re-sampled when exiting from Standby mode. Consequently,
they must be kept in the required Boot mode configuration in Standby mode.After startup
delay, the selection of the boot area is done before releasing the processor reset.
PH3/BOOT0 GPIO is configured in:
• Input mode during the complete reset phase if the option bit nSWBOOT0 is set into the
FLASH_OPTR register and then switches automatically in analog mode after reset is
released (BOOT0 pin).
• Input mode from the reset phase to the completion of the option byte loading if the bit
nSWBOOT0 is cleared into the FLASH_OPTR register (BOOT0 value coming from the
option bit). It switches then automatically to the analog mode even if the reset phase is
not complete.
Embedded bootloader and RSS
The bootloader is located in the system memory. It is used to reprogram the flash memory
by using USART, I2C, SPI, FDCAN or USB FS in device mode through the DFU (device
firmware upgrade). It is programmed by ST during production. Refer to AN2606, STM32
microcontroller system memory boot mode.
The root secure services (RSS) are embedded in a flash memory area named secure
information block, programmed during ST production.
The RSS enables for example the secure firmware installation (SFI) thanks to the RSS
extension firmware (RSSe SFI).
This feature allows the customers to protect the confidentiality of the firmware to be
provisioned into the STM32 device when the production is subcontracted to a third party.
The RSS is available on all devices, after enabling the TrustZone through the TZEN option
bit.
1. In RDP level 2, the boot is done from the addr ess programmed in NSBOOTADD0 or NSBOOTADD1
depending on the boot configuration before setting the RDP level 2 and if the programmed address is
within the user flash memory.
If the programmed NSBOOTADD0 or NSBOOTADD1 is not a valid address, the boot if forced at 0x800
0000.
```

## 3. Referenced Figures & Diagrams in this Chapter
* *No dedicated figure diagrams referenced in this chapter text.*

## 4. Referenced Configuration Tables in this Chapter
* [Table 6: Configuration Matrix](../tables/table_6.md)
* [Table 7: Configuration Matrix](../tables/table_7.md)
* [Table 8: Configuration Matrix](../tables/table_8.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)