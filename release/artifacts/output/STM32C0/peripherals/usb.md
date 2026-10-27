# Universal Serial Bus (USB)

## 1. Overview & Key Features
The Universal Serial Bus (USB) block provides complete operational functionality for the STM32C0 microcontroller.
Documented in [Chapter 29](../chapters/chapter_29.md) (Pages 954 - 1000).

## 2. Dependencies & Interconnects
* **Clocking & Prescalers**: Controlled via [Reset and Clock Control (RCC)](../system/rcc.md).
* **Power Scaling**: Depends on power domain scaling settings in [Power Control (PWR)](../system/pwr.md).
* **Memory Map**: Mapped in [Master System Memory Map](../memory/memory_map.md).

## 3. Memory Map & Base Address
* **Parent Category**: PERIPHERALS
* **Reference Chapter**: [Chapter 29](../chapters/chapter_29.md)
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
| `USB_BCDR` | `0x58` | Universal Serial Bus (USB) USB_BCDR Register | [USB_BCDR.json](../registers_json/USB_BCDR.json) |
| `USB_CHEP0R` | `0x00` | Universal Serial Bus (USB) USB_CHEP0R Register | [USB_CHEP0R.json](../registers_json/USB_CHEP0R.json) |
| `USB_CHEP1R` | `0x04` | Universal Serial Bus (USB) USB_CHEP1R Register | [USB_CHEP1R.json](../registers_json/USB_CHEP1R.json) |
| `USB_CHEP2R` | `0x08` | Universal Serial Bus (USB) USB_CHEP2R Register | [USB_CHEP2R.json](../registers_json/USB_CHEP2R.json) |
| `USB_CHEP3R` | `0x0C` | Universal Serial Bus (USB) USB_CHEP3R Register | [USB_CHEP3R.json](../registers_json/USB_CHEP3R.json) |
| `USB_CHEP4R` | `0x10` | Universal Serial Bus (USB) USB_CHEP4R Register | [USB_CHEP4R.json](../registers_json/USB_CHEP4R.json) |
| `USB_CHEP5R` | `0x14` | Universal Serial Bus (USB) USB_CHEP5R Register | [USB_CHEP5R.json](../registers_json/USB_CHEP5R.json) |
| `USB_CHEP6R` | `0x18` | Universal Serial Bus (USB) USB_CHEP6R Register | [USB_CHEP6R.json](../registers_json/USB_CHEP6R.json) |
| `USB_CHEP7R` | `0x1C` | Universal Serial Bus (USB) USB_CHEP7R Register | [USB_CHEP7R.json](../registers_json/USB_CHEP7R.json) |
| `USB_CHEPNR` | `0x00` | USB endpoint/channel n register (USB_CHEPNR) | [USB_CHEPNR.json](../registers_json/USB_CHEPNR.json) |
| `USB_CHEP_RXTXBD_0` | `0x08` | Universal Serial Bus (USB) USB_CHEP_RXTXBD_0 Register | [USB_CHEP_RXTXBD_0.json](../registers_json/USB_CHEP_RXTXBD_0.json) |
| `USB_CHEP_RXTXBD_1` | `0x10` | Universal Serial Bus (USB) USB_CHEP_RXTXBD_1 Register | [USB_CHEP_RXTXBD_1.json](../registers_json/USB_CHEP_RXTXBD_1.json) |
| `USB_CHEP_RXTXBD_2` | `0x18` | Universal Serial Bus (USB) USB_CHEP_RXTXBD_2 Register | [USB_CHEP_RXTXBD_2.json](../registers_json/USB_CHEP_RXTXBD_2.json) |
| `USB_CHEP_TXRXBD_0` | `0x04` | Universal Serial Bus (USB) USB_CHEP_TXRXBD_0 Register | [USB_CHEP_TXRXBD_0.json](../registers_json/USB_CHEP_TXRXBD_0.json) |
| `USB_CHEP_TXRXBD_1` | `0x0C` | Universal Serial Bus (USB) USB_CHEP_TXRXBD_1 Register | [USB_CHEP_TXRXBD_1.json](../registers_json/USB_CHEP_TXRXBD_1.json) |
| `USB_CHEP_TXRXBD_2` | `0x14` | Universal Serial Bus (USB) USB_CHEP_TXRXBD_2 Register | [USB_CHEP_TXRXBD_2.json](../registers_json/USB_CHEP_TXRXBD_2.json) |
| `USB_CNTR` | `0x40` | USB control register (USB_CNTR) | [USB_CNTR.json](../registers_json/USB_CNTR.json) |
| `USB_DADDR` | `0x4C` | Universal Serial Bus (USB) USB_DADDR Register | [USB_DADDR.json](../registers_json/USB_DADDR.json) |
| `USB_FNR` | `0x48` | USB frame number register (USB_FNR) | [USB_FNR.json](../registers_json/USB_FNR.json) |
| `USB_ISTR` | `0x44` | USB interrupt stat us register (USB_ISTR) | [USB_ISTR.json](../registers_json/USB_ISTR.json) |
| `USB_LPMCSR` | `0x54` | USB LPM control and st atus register (USB_LPMCSR) | [USB_LPMCSR.json](../registers_json/USB_LPMCSR.json) |