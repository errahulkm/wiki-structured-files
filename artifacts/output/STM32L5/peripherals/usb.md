# Universal Serial Bus (USB)

## 1. Overview & Key Features
The Universal Serial Bus (USB) block provides complete operational functionality for the STM32L5 microcontroller.
Documented in [Chapter 50](../chapters/chapter_50.md), [Chapter 51](../chapters/chapter_51.md) (Pages 1935 - 1967).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 50](../chapters/chapter_50.md), [Chapter 51](../chapters/chapter_51.md)
* **Bus Architecture**: Internal AHB / APB Interconnect

## 4. Functional Description & Operational Sequences
Detailed functional specifications, initialization state machines, DMA request mappings, and operating modes.

## 5. Architectural Figures & Diagrams
* [Figure: Universal Serial Bus (USB) Architectural Block Diagram](../figures/usb_block_diagram.md)

## 6. Reference Tables & Configuration Matrices
* [Table: Universal Serial Bus (USB) Configuration & Parameter Matrix](../tables/usb_configuration_table.md)

## 7. Hardware Register Map Summary & Schemas
| Register Name | Offset | Description | JSON Schema Link |
| :--- | :--- | :--- | :--- |
| `USB` | `0x1967` | DP USB PHY Register mapper APB interface PCLK APB bus IRQs to NVIC Arbiter Packet buffer memory Register mapper Control registers and logic Interrupt registers and logic Endpoint registers Endpoint registers Endpoint selection Clock recoveryRX-TXSuspend timer Packet buffer interface Analog transceiver DM Interrupt mapper APB wrapper BCDEmbedded pull-up NOE PCLK RM0438 Rev 8 1937/2187 RM0438 Universal serial bus full-speed device interface (USB) | [USB.json](../registers_json/USB.json) |
| `USB_BCDR` | `0x58` | Universal Serial Bus (USB) USB_BCDR Register | [USB_BCDR.json](../registers_json/USB_BCDR.json) |
| `USB_BTABLE` | `0x50` | Universal Serial Bus (USB) USB_BTABLE Register | [USB_BTABLE.json](../registers_json/USB_BTABLE.json) |
| `USB_CNTR` | `0x40` | USB control register (USB_CNTR) | [USB_CNTR.json](../registers_json/USB_CNTR.json) |
| `USB_DADDR` | `0x4C` | Universal Serial Bus (USB) USB_DADDR Register | [USB_DADDR.json](../registers_json/USB_DADDR.json) |
| `USB_EP0R` | `0x00` | Universal Serial Bus (USB) USB_EP0R Register | [USB_EP0R.json](../registers_json/USB_EP0R.json) |
| `USB_EP1R` | `0x04` | Universal Serial Bus (USB) USB_EP1R Register | [USB_EP1R.json](../registers_json/USB_EP1R.json) |
| `USB_EP2R` | `0x08` | Universal Serial Bus (USB) USB_EP2R Register | [USB_EP2R.json](../registers_json/USB_EP2R.json) |
| `USB_EP3R` | `0x0C` | Universal Serial Bus (USB) USB_EP3R Register | [USB_EP3R.json](../registers_json/USB_EP3R.json) |
| `USB_EP4R` | `0x10` | Universal Serial Bus (USB) USB_EP4R Register | [USB_EP4R.json](../registers_json/USB_EP4R.json) |
| `USB_EP5R` | `0x14` | Universal Serial Bus (USB) USB_EP5R Register | [USB_EP5R.json](../registers_json/USB_EP5R.json) |
| `USB_EP6R` | `0x18` | Universal Serial Bus (USB) USB_EP6R Register | [USB_EP6R.json](../registers_json/USB_EP6R.json) |
| `USB_EP7R` | `0x1C` | Universal Serial Bus (USB) USB_EP7R Register | [USB_EP7R.json](../registers_json/USB_EP7R.json) |
| `USB_FNR` | `0x48` | USB frame number register (USB_FNR) | [USB_FNR.json](../registers_json/USB_FNR.json) |
| `USB_ISTR` | `0x44` | 1952/2187 RM0438 Rev 8 USB interrupt status register (USB_ISTR) | [USB_ISTR.json](../registers_json/USB_ISTR.json) |
| `USB_LPMCSR` | `0x54` | LPM control and status register (USB_LPMCSR) | [USB_LPMCSR.json](../registers_json/USB_LPMCSR.json) |