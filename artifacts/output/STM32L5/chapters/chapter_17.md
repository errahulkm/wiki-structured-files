# Chapter 17: Extended interrupts and event controller (EXTI)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 17: Extended interrupts and event controller (EXTI).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 533 - 562
* **Taxonomy Section**: CORE
* **Parent IP Module**: [Interrupts and Events (NVIC/EXTI)](../core/interrupts.md)

## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
RM0438 Rev 8 533/2187
RM0438 Extended interrupts and event controller (EXTI)
562
17 Extended interrupts and event controller (EXTI)
The extended interrupts and event controller (EXTI) manages the individual CPU and
system wakeup through configurable and direct event inputs. It provides wakeup requests to
the power control, and generates an interrupt request to the CPU NVIC and events to the
CPU event input. For the CPU an additional event generation block (EVG) is needed to
generate the CPU event signal.
The EXTI wakeup requests allow the system to be woken up from Stop modes.
The interrupt request and event request generation can be used also in Run modes.
The EXTI also includes the EXTI mux IOport selection.
17.1 EXTI main features
The EXTI main features are the following:
• 43 input events supported.
• All event inputs allow the possibility to wake up the system.
• Events which do not have an associated wakeup flag in the peripheral, have a flag in
the EXTI and generate an interrupt to the CPU from the EXTI.
• Events can be used to generate a CPU wakeup event.
The asynchronous event inputs are classified in two groups:
• Configurable events (signals from I/Os or peripherals able to generate a pulse).
The configurable events have the following features:
– Selectable active trigger edge
– Interrupt pending st atus register bits independent for the rising and falling edge
– Individual interrupt and event generation mask, used for conditioning the CPU
wakeup, interrupt and event generation
– SW trigger possibility
• Direct events (interrupt and wakeup sources from peripherals having an associated
flag which requires to be cleared in the peripheral).
The direct events have the following features:
– Fixed rising edge active trigger
– No interrupt pending status register bit in the EXTI. (The interrupt pending status
flag is provided by the peripheral generating the event.)
– Individual interrupt and event generation mask, used for conditioning the CPU
wakeup and event generation
– No SW trigger possibility
• Secure events
– The access to control and configuration bits of secure input events can be made
secure and or privilege.
• EXTI IO port selection.

Extended interrupts and event controller (EXTI) RM0438
534/2187 RM0438 Rev 8
17.2 EXTI block diagram
The EXTI consists of a register block accessed via an AHB interface, the event input trigger
block, the masking block, and EXTI mux as shown in [Figure 47](../figures/figure_47.md).
The register block contains all the EXTI registers.
The event input trigger block provides event input edge trigger logic.
The masking block provides the event input distribution to the different wakeup, interrupt
and event outputs, and their masking.
The EXTI mux provides the IO port selection on to the EXTI event signal.
[Figure 47](../figures/figure_47.md). EXTI block diagram
EVG
Pulse
EXTI
Event
Trigger
Direct event(x)
orconfigurable event(y)
it_exti_per(y)*
c_eventMaskingevents
AHB interface
PWR
CPU
rxev
nvic(x)
Peripherals
sys_wakeup
nvic(y)
Wakeup
Interrupt Direct event(x)
c_evt_exti
c_evt_rst
hclk
c_fclk
c_wakeup
GPIO
Configurable event(15:0)
EXTImux
IOPort
exti[15:0] To interconnect
* it_exti_per(y) are only available for configurable events (y)
MSv49347V1
Registers exti_ilac
[Table 110](../tables/table_110.md). EXTI pin overview
Pin name I/O Description
AHB interface I/O EXTI register bus interface. When one event is configured to enable
security, the AHB interface supports secure accesses
hclk I AHB bus clock and EXTI system clock
Configurable
event(y) I Asynchronous wakeup events from peripherals which do not have an
associated interrupt and flag in the peripheral
exti_ilac O Illegal access event
Direct event(x) I Synchronous and asynchronous wakeup events from peripherals which
have an associated interrupt and flag in the peripheral
IOPort(n) I GPIOs block IO ports[15:0]
exti[15:0] O EXTI GPIO output port to trigger other IPs
it_exti_per (y) O Interrupts to the CPU associated with Configurable event (y)
c_evt_exti O High level sensitive even t output for CPU synchronous to hclk

RM0438 Rev 8 535/2187
RM0438 Extended interrupts and event controller (EXTI)
562
17.2.1 EXTI connections betw een peripherals and CPU
The peripherals able to generate wakeup or interrupt events when the system is in Stop
mode are connected to the EXTI.
• Peripheral wakeup signals which generate a pulse or which do not have an interrupt
status bits in the peripheral, are connected to an EXTI configurable event input. For
these events the EXTI provides a status pending bit which requires to be cleared. It is
the EXTI interrupt associated with the status bit that will interrupt the CPU.
• Peripheral interrupt and wakeup signals that have a status bit in the peripheral which
requires to be cleared in the peripheral, are connected to an EXTI direct event input.
There is no status pending bit within the EXTI. The interrupt or wakeup is cleared by
the CPU in the peripheral. It is the peripheral interrupt that interrupts the CPU directly.
• All GPIO ports input to the EXTI multiplexer, allowing the selection of a port pin to wake
up the system via a configurable event.
The EXTI configurable event interrupts are connected to the NVIC of the CPU.
The dedicated EXTI/EVG CPU event is connected to the CPU rxev input.
The EXTI CPU wakeup signals are connected to the PWR block, and are used to wake up
the system and CPU sub-system bus clocks.
17.2.2 EXTI interrupt/event mapping
The EXTI lines are connected as shown in [Table 112](../tables/table_112.md): EXTI line connections.
c_evt_rst I Asynchronous reset input to clear c_evt_exti
sys_wakeup O Asynchronous system wakeup request to PWR for ck_sys and hclk
c_wakeup O Wakeup request to PWR for CPU, synchronous to hclk
[Table 111](../tables/table_111.md). EVG pin overview
Pin name I/O Description
c_fclk I CPU free Running clock
c_evt_in I High level sensitive events input from EXTI, asynchronous to CPU clock
c_event O Event pulse, synchronous to CPU clock
c_evt_rst O Event reset signal , synchronous to CPU clock
[Table 110](../tables/table_110.md). EXTI pin overview (continued)
Pin name I/O Description
[Table 112](../tables/table_112.md). EXTI line connections
EXTI line Line source Line type
0-15 GPIO Configurable
16 PVD output Configurable
17 RTC Direct
18 RTC secure Direct
19 TAMP Direct

Extended interrupts and event controller (EXTI) RM0438
536/2187 RM0438 Rev 8
20 TAMP secure Direct
21 COMP1 output Configurable
22 COMP2 output Configurable
23 I2C1 wakeup Direct
24 I2C2 wakeup Direct
25 I2C3 wakeup Direct
26 USART1 wakeup Direct
27 USART2 wakeup Direct
28 USART3 wakeup Direct
29 USART4 wakeup Direct
30 USART5 wakeup Direct
31 LPUART1 wakeup Direct
32 LPTIM1 Direct
33 LPTIM2 Direct
34 USB FS wakeup Direct
35 PVM1 wakeup Configurable
36 PVM2 wakeup Configurable
37 PVM3 wakeup Configurable
38 PVM4 wakeup Configurable
39 reserved Direct
40 I2C4 wakeup Direct
41 UCPD1 wakeup Direct
42 LPTIM3 wakeup Direct
[Table 112](../tables/table_112.md). EXTI line connections (continued)
EXTI line Line source Line type

RM0438 Rev 8 537/2187
RM0438 Extended interrupts and event controller (EXTI)
562
17.3 EXTI functional description
Depending on the EXTI event input type and wakeup target(s), different logic
implementations are used. The applicable features are controlled from register bits:
• Active trigger edge enable, by rising edge selection
EXTI rising trigger selection register (EXTI_RTSR1),
EXTI rising trigger selection register (EXTI_RTSR2),
and falling edge selection
EXTI falling trigger selection register (EXTI_FTSR1),
EXTI falling trigger selection register (EXTI_FTSR2).
• Software trigger, by
EXTI software interrupt event register (EXTI_SWIER1),
EXTI software interrupt event register (EXTI_SWIER2).
• Interrupt pending flag, by
EXTI rising edge pending register (EXTI_RPR1),
EXTI falling edge pending register (EXTI_FPR1),
EXTI rising edge pending register (EXTI_RPR2),
EXTI falling edge pending register (EXTI_FPR2).
• CPU wakeup and interrupt enable, by
EXTI CPU wakeup with interrupt mask register (EXTI_IMR1),
EXTI CPU wakeup with interrupt mask register (EXTI_IMR2).
• CPU wakeup and event enable, by
EXTI CPU wakeup with interrupt mask register (EXTI_IMR1),
EXTI CPU wakeup with event mask register (EXTI_EMR2).
17.3.1 EXTI configurable event input wakeup
[Figure 48](../figures/figure_48.md) is a detailed representation of the logic associated with configurable event inputs
which wakeup the CPU sub-system bus clocks and generated an EXTI pending flag and
interrupt to the CPU and or a CPU wakeup event.
[Table 113](../tables/table_113.md). EXTI event input configurations and register control
Event input
type Logic implementation
EXTI_RTSR
EXTI_FTSR
EXTI_SWIER
EXTI_R/FPR
EXTI_IMR
EXTI_EMR(1)
1. Only for input events with confi guration “rxev generation” enabled.
Configurable Configurable event input wakeup logic x x x x x x
Direct Direct event input wakeup logic - - - - x x

Extended interrupts and event controller (EXTI) RM0438
538/2187 RM0438 Rev 8
[Figure 48](../figures/figure_48.md). Configurable event trigger logic CPU wakeup
1. Only for the input events that support CPU rxev generation c_event.
The software interrupt event register allows to trigger configurable events by software,
writing the corresponding register bit, irrespective of the edge selection setting.
The rising edge and falling edge selection registers allow the enabling and selection of the
configurable event active trigger edge or both edges.
The CPU has its dedicated wakeup (interrupt) mask register and a dedicated event mask
registers. The enabled event make it possible to generate an event on the CPU. All events
for a CPU are ordered together into a single CPU event signal. The event pending registers
(EXTI_RPR and EXTI_FPR) is not set for an unmasked CPU event.
The configurable events have unique interrupt pending request registers, shared by the
CPU. The pending register is only set for an unmasked interrupt. Each configurable event
provides a common interrupt to the CPU. The configurable event interrupts need to be
acknowledged by software in the EXTI_RPR and/or EXTI_FPR registers.
When a CPU wakeup (interrupt) or CPU event is enabled the asynchronous edge detection
circuit is reset by the clocked delay and rising edge detect pulse generator. This guarantees
that the EXTI hclk clock is woken up before the asynchronous edge detection circuit is reset.
Note: A detected configurable event interrupt pe nding request, may be cleared by any CPU with
the correct access permission. The system is not able to enter into low-power modes as
long as an interrupt pending request is active.
EVG
EXTI
Peripheral interface
Falling
trigger
selection
register
Rising
trigger
selection
register
Pending
request
register
Asynchronous Edge
detection circuitConfigurable
Event input(y)
it_exti_per(y)
CPU Event(y)(1)
c_wakeup
Rising Edge
detect Pulse
generator
rst
Delay
hclk
hclk
CPU
Interrupt
mask
register
CPU
Event
mask
register
Other CPU Wakeups
sys_wakeupOther Wakeups
Wakeup(y)
Other CPU Events(x,y)
c_event
CPU Wakeup(y)
Synch
hclk
Software
interrupt
event
register
AHB
interface
CPU
Rising Edge
detect Pulse
generator
ck_fclk_c
Rising
Edge
detect
hclk
rst c_evt_exti
c_evt_rst
Same circuit for Configurable
and Direct events
MS46537V1

RM0438 Rev 8 539/2187
RM0438 Extended interrupts and event controller (EXTI)
562
17.3.2 EXTI direct event input wakeup
[Figure 49](../figures/figure_49.md) is a detailed representation of the logic associated with direct event inputs waking
up the system.
The direct events do not have an associated EXTI interrupt. The EXTI only wakes up the
system and CPU sub-system clocks and may generate a CPU wakeup event. The
peripheral synchronous interrupt, associated with the direct wakeup event wakes up the
CPU.
The EXTI direct event is able to generate a CPU event. This CPU event wakes up the CPU.
The CPU event may occur before the associated peripheral interrupt flag is set.
[Figure 49](../figures/figure_49.md). Direct event trigger logic CPU wakeup
1. Only for the input events that support CPU rxev generation c_event.
17.3.3 EXTI mux selection
The EXTI mux allow the selection of GPIOs as interrupts and wakeup. The GPIOs are
connected via 16 EXTI mux lines to the first 16 EXTI events as configurable event. The
selection of GPIO port as EXTI mux output, is controlled by registers: EXTI external interrupt
selection register (EXTI_EXTICRn).
EVG
EXTI
Direct
Event
input(x) Asynchronous
Rising Edge
detect circuit
Falling Edge
detect
Pulse
generator
rst
Delay
hclk
CPU
Rising Edge
detect Pulse
generator
hclk
ck_fclk_c
Peripheral interface
CPU
Event
mask
register
c_event
c_wakeup
sys_wakeup
Other CPU Wakeups
Other Wakeups
CPU Event(x)(1)
CPU Wakeup(x)
Wakeup(x)
Synch
hclk
AHB interface
CPU
Interrupt
mask
register
c_evt_exti
hclk
Other CPU Events(x,y)
hclk
rst
c_evt_rst
Same circuit for Configurable
and Direct events
MS46536V1
Rising
Edge
detect

Extended interrupts and event controller (EXTI) RM0438
540/2187 RM0438 Rev 8
[Figure 50](../figures/figure_50.md). EXTI mux GPIO selection
The EXTIs mux outputs are available as output signals from the EXTI to trigger other IPs.
The EXTI mux outputs are available independent from any masking in EXTI_IMRx and
EXTI_EMRx.
17.4 EXTI functional behavior
The direct event inputs are enabled in the respective peripheral generating the wakeup
event. The configurable events are enabled by enabling at least one of the trigger edges.
Once an event input is enabled, the generation of a CPU wakeup is conditioned by the CPU
interrupt mask and CPU event mask.
For configurable event inputs, when the enabled edge(s) occur on the event input, an event
request is generated. When the associated CPU interrupt is unmasked the corresponding
pending bit EXTI_RPR.RPIFn and/or EXTI_FPR.FPIFn is/are set and the CPU sub-system
is woken up and CPU interrupt signal is activated. The EXTI_RPR.RPIFn and/or
EXTI_FPR.FPIFn pending bit shall be cleared by software writing it to ‘1’. This action clears
the CPU interrupt.
For direct event inputs, when enabled in the associated peripheral, an event request is
generated on the rising edge only. There is no corresponding CPU pending bit in the EXTI.
MS44726V1
PA0
PB0
PC0
Px0
………....
EXTI0
_
PA1
PB1
PC1
Px1
………....
EXTI1
_
PA15
PB15
PC15
Px15
………....
EXTI15
_
………....
[Table 114](../tables/table_114.md). Masking functionality
CPU interrupt
enable
EXTI_IMR.IMn
CPU event enable
EXTI_EMR.EMn
Configurable
event inputs
EXTI_RPR.RPIFn
EXTI_FPR.FPIFn
exti(n)
interrupt(1)
CPU
event CPU wakeup
0
0 no masked masked masked
1 no masked yes yes
1
0 status latched yes masked yes (2)
1 status latched yes yes yes
1. The single exti(n) interrupt will go to the CPU. If no interrupt  is required for CPU, the exti(n) interrupt shall be masked in the
CPU NVIC.
2. Only if CPU interrupt is enabled in EXTI_IMR.IMn.

RM0438 Rev 8 541/2187
RM0438 Extended interrupts and event controller (EXTI)
562
When the associated CPU interrupt is unmasked, the corresponding CPU sub-system is
woken up. The CPU is woken up (interrupted) by the peripheral synchronous interrupt.
The CPU event has to be unmasked to generate an event. When the enabled edge(s) occur
on the event input a CPU event pulse is generated. There is no event pending bit.
For the configurable event inputs an event request can be generated by software when
writing a ‘1’ in the software interrupt/event register EXTI_SWIER, allowing the generation of
a rising edge on the event. The rising edge event pending bit is set in EXTI_RPR,
irrespective of the setting in EXTI_RTSR.
17.5 EXTI event protection
The EXTI is able to protect event register bits from being modified by non-secure and
unprivileged accesses. The protection can individually be activated per input event via the
register bits in EXTI_SECCFGR and EXTI_PRIVCFGR. At EXTI level the protection
consists in preventing unauthorized write access to:
• Change the settings of the secure and/or privileged configurable events.
• Change the masking of the secure and/or privileged input events.
• Clear pending status of the secure and/or privileged input events.
17.5.1 EXTI security protection
When security is enabled for an input event, the associated input event configuration and
control bits can only be modified and read by a secure access, a non-secure write access is
discarded and a read returns 0.
[Table 115](../tables/table_115.md). Register protection overview
Register name Access type Protection (1)(2)
1. Security is enabled with the indivi dual Input event. EXTI_SECCFG registers.
2. Privilege is enabled with the individual  Input event EXTI_PRIVCFGRn registers.
EXTI_RTSR RW
Security and privilege can be bit wise enabled in
EXTI_SECCFGR and EXTI_PRIVCFGR
EXTI_FTSR RW
EXTI_SWIER RW
EXTI_RPR RW
EXTI_FPR RW
EXTI_SECCFGR RW Always secure, and privilege can be bit wise enabled in
EXTI_PRIVCFGR
EXTI_PRIVCFGR RW Always privilege, and security can be bit wise enabled in
EXTI_SECCFGR
EXTI_EXTICRn RW Security and privilege can be bit wise enabled in
EXTI_SECCFGR and EXTI_PRIVCFGR
EXTI_LOCKR RW Always secure.
EXTI_IM RW Security and privilege can be bit wise enabled in
EXTI_SECCFGR and EXTI_PRIVCFGREXTI_EMR RW

Extended interrupts and event controller (EXTI) RM0438
542/2187 RM0438 Rev 8
When input events are non-secure, the security is disabled. The associated input event
configuration and control bits can be modified and read by a secure access and non-secure
access.
The security configuration in registers EXTI_SECCFGR can be globally locked after reset
by EXTI_LOCKR.LOCK.
17.5.2 EXTI privilege protection
When privilege is enabled for an input event, the associated input event configuration and
control bits can only be modified and read by a privilege access, an unprivileged write
access is discarded and a read returns 0.
When input events are unprivileged, the privilege is disabled. The associated input event
configuration and control bits can be modified and read by a privilege access and
unprivileged access.
The privilege configuration in registers EXTI_PRIVCFGRn can be globally locked after reset
by EXTI_LOCKR.LOCK.

RM0438 Rev 8 543/2187
RM0438 Extended interrupts and event controller (EXTI)
562
17.6 EXTI registers
The EXTI register map is divided in the following sections:
All the registers can be accessed with word (32-bit), half-word (16-bit) and byte (8-bit)
access.
17.6.1 EXTI rising trigger sel ection register (EXTI_RTSR1)
Address offset: 0x000
Reset value: 0x0000 0000
Contains only register bits for configurable events.
[Table 116](../tables/table_116.md). EXTI register map sections
Address offset Description
0x000 - 0x01C General configurab le event [31:0] configuration
0x020 - 0x03C General configurab le event [63:32] configuration
0x060 - 0x06C EXTI IOport mux selection
0x070 EXTI protection lock configuration
0x080 - 0x0BC CPU input event configuration
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Re s. Res. Res. Res. Res. RT22 RT21 Res. Res. Res. Res. RT16
rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
RT15 RT14 RT13 RT12 RT11 RT10 RT9 RT8 RT7 RT6 RT5 RT4 RT3 RT2 RT1 RT0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:23 Reserved, must be kept at reset value.

Extended interrupts and event controller (EXTI) RM0438
544/2187 RM0438 Rev 8
17.6.2 EXTI falling trigger selec tion register (EXTI_FTSR1)
Address offset: 0x004
Reset value: 0x0000 0000
Contains only register bits for configurable events.
Bits 22:21 RT[22:21]: Rising trigger event configuration bit of configurable event input x(1) (where x = 18
to 22)
When SECx is disabled, RTx can be accessed with non-secure and secure access.
When SECx is enabled, RTx can only be accessed with secure access. Non-secure write to
this bit x is discarded, non-secure read returns 0.
When EXTI_PRIVCFGRn.PRIVx is disabled, RTx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGRn.PRIVx is enabled, RTx can only be accessed with privilege access.
Unprivileged write to this bit x is discarded, unprivileged read returns 0.
0: Rising trigger disabled (for event and Interrupt) for input line
1: Rising trigger enabled (for event and Interrupt) for input line
Bits 20:17 Reserved, must be kept at reset value.
Bits 16:0 RT[16:0]: Rising trigger event configuration bit of configurable event input x(1) (where x = 0 to
16)
When EXTI_SECCFGR SECx is disabled, RTx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR SECx is enabled, RTx can only be accessed with secure access. Non-
secure write to this bit x is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR PRIVx is disabled, RTx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR PRIVx is enabled, RTx can only be accessed with privilege access.
Unprivileged write to this bit x is discarded, unprivileged read returns 0.
0: Rising trigger disabled (for event and Interrupt) for input line
1: Rising trigger enabled (for event and Interrupt) for input line
1. The configurable event inputs are edge trigger ed, no glitch must be generated on these inputs.
If a rising edge on the configurable event input occurs during writing of the register, the associated pending bit is not set.
Rising and falling edge triggers can be set for the same configurable event input. In this case, both edges generate a
trigger.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Re s. Res. Res. Res. Res. FT22 FT21 Res. Res. Res. Res. FT16
rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
FT15 FT14 FT13 FT12 FT11 FT10 FT9 FT8 FT7 FT6 FT5 FT4 FT3 FT2 FT1 FT0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 545/2187
RM0438 Extended interrupts and event controller (EXTI)
562
17.6.3 EXTI software interrupt event register (EXTI_SWIER1)
Address offset: 0x008
Reset value: 0x0000 0000
Contains only register bits for configurable events.
Bits 31:23 Reserved, must be kept at reset value.
Bits 22:21 FT[22:21]: Falling trigger event configuration bit of configurable event input x (1) (where x = 18
to 22).
When EXTI_SECCFGR.SECx is disabled, FTx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, FTx can only be accessed with secure access. Non-
secure write to this FTx is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, FTx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, FTx can only be accessed with privilege access.
Unprivileged write to this FTx is discarded, unprivileged read returns 0.
0: Falling trigger disabled (for event and Interrupt) for input line
1: Falling trigger enabled (for event and Interrupt) for input line.
Bit 20:17 Reserved, must be kept at reset value.
Bits 16:0 FT[16:0]: Falling trigger event configuration bit of configurable event input x (1) (where x = 0 to
16).
When EXTI_SECCFGR.SECx is disabled, FTx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, FTx can only be accessed with secure access. Non-
secure write to this FTx is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, FTx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, FTx can only be accessed with privilege access.
Unprivileged write to this FTx is discarded, unprivileged read returns 0.
0: Falling trigger disabled (for event and Interrupt) for input line
1: Falling trigger enabled (for event and Interrupt) for input line.
1. The configurable event inputs are edge trigger ed, no glitch must be generated on these inputs.
If a falling edge on the configurable event input occurs during writing of the register, the associated pending bit is not set.
Rising and falling edge triggers can be set for the same configurable event input. In this case, both edges generate a
trigger.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Re s. Res. Res. Res. Res. SWI22 SWI21 Res. Res. Res. Res. SWI16
rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
SWI15 SWI14 SWI13 SWI12 SWI11 SWI10 SWI9 SWI8 SWI7 SWI6 SWI5 SWI4 SWI3 SWI2 SWI1 SWI0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

Extended interrupts and event controller (EXTI) RM0438
546/2187 RM0438 Rev 8
17.6.4 EXTI rising edge pendi ng register (EXTI_RPR1)
Address offset: 0x00C
Reset value: 0x0000 0000
Contains only register bits for configurable events.
Bits 31:23 Reserved, must be kept at reset value.
Bits 22:21 SWI[22:21]: Software interrupt on event x (where x = 18 to 22)
When EXTI_SECFGR.SECx is disabled, SWIx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, SWIx can only be accessed with secure access.
Non-secure write to this SWI x is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, SWIx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, SWIx can only be accessed with privilege access.
Unprivileged write to this SWIx is discarded, unprivileged read returns 0.
A software interrupt is generated independent from the setting in EXTI_RTSR and
EXTI_FTSR. It always returns 0 when read.
0: Writing 0 has no effect.
1: Writing a 1 to this bit triggers a rising edge event on event x. This bit is auto cleared by
HW.
Bit 20:17 Reserved, must be kept at reset value.
Bits 16:0 SWI[16:0]: Software interrupt on event x (where x = 18 to 22)
When EXTI_SECFGR.SECx is disabled, SWIx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, SWIx can only be accessed with secure access.
Non-secure write to this SWI x is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, SWIx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, SWIx can only be accessed with privilege access.
Unprivileged write to this SWIx is discarded, unprivileged read returns 0.
A software interrupt is generated independent from the setting in EXTI_RTSR and
EXTI_FTSR. It always returns 0 when read.
0: Writing 0 has no effect.
1: Writing a 1 to this bit triggers a rising edge event on event x. This bit is auto cleared by
HW.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. RPIF22 RPIF21 Res. Res. Res. Res. RPIF16
rc_w1 rc_w1 rc_w1
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
RPIF15 RPIF14 RPIF13 RPIF12 RPIF11 RPIF10 RPIF9 RPI F8 RPIF7 RPIF6 RPIF5 RPIF4 RPIF3 RPIF2 RPIF1 RPIF0
rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1

RM0438 Rev 8 547/2187
RM0438 Extended interrupts and event controller (EXTI)
562
17.6.5 EXTI falling edge pend ing register (EXTI_FPR1)
Address offset: 0x010
Reset value: 0x0000 0000
Contains only register bits for configurable events.
Bits 31:23 Reserved, must be kept at reset value.
Bits 22:21 RPIF[22:21]: configurable event inputs x rising edge pending bit (where x = 18 to 22).
When EXTI_SECCFGR.SECx is disabled, RPIFx can be accessed with non-secure and
secure access.
When EXTI_SECCFGR.SECx is enabled, RPIFx can only be accessed with secure access.
Non-secure write to this RPIFx is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, RPIFx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, RPIFx can only be accessed with privilege access.
Unprivileged write to this RPIFx is discarded, unprivileged read returns 0.
0: No rising edge trigger request occurred
1: Rising edge trigger request occurred
This bit is set when the rising edge event or an EXTI_SWIER software trigger arrives on the
configurable event line. This bit is cleared by writing a 1 into the bit.
Bit 20:17 Reserved, must be kept at reset value.
Bits 16:0 RPIF[16:0]: configurable event inputs x rising edge pending bit (where x = 0 to 16).
When EXTI_SECCFGR.SECx is disabled, RPIFx can be accessed with non-secure and
secure access.
When EXTI_SECCFGR.SECx is enabled, RPIFx can only be accessed with secure access.
Non-secure write to this RPIFx is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, RPIFx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, RPIFx can only be accessed with privilege access.
Unprivileged write to this RPIFx is discarded, unprivileged read returns 0.
0: No rising edge trigger request occurred
1: Rising edge trigger request occurred
This bit is set when the rising edge event or an EXTI_SWIER software trigger arrives on the
configurable event line. This bit is cleared by writing a 1 into the bit.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. FPIF22 FPIF21 Res. Res. Res. Res. FPIF16
rc_w1 rc_w1 rc_w1
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
FPIF15 FPIF14 FPIF13 FPIF12 FPIF11 FPIF10 FPIF9 FPI F8 FPIF7 FPIF6 FPIF5 FPIF4 FPIF3 FPIF2 FPIF1 FPIF0
rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1 rc_w1

Extended interrupts and event controller (EXTI) RM0438
548/2187 RM0438 Rev 8
17.6.6 EXTI security configurati on register (EXTI_SECCFGR1)
Address offset: 0x014
Reset value: 0x0000 0000
This register provides write access security, a non-secure write access is ignored and
causes the generation of an illegal access event. A non-secure read returns the register
data.
Contains only register bits for security capable input events.
Bits 31:23 Reserved, must be kept at reset value.
Bits 22:21 FPIF[22:21]: configurable event inputs x falling edge pending bit (where x = 22 to 18)
When EXTI_SECCFGR.SECx is disabled, FPIFx can be accessed with non-secure and
secure access.
When EXTI_SECCFGR.SECx is enabled, FPIFx can only be accessed with secure access.
Non-secure write to this FPIFx is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, FPIFx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, FPIFx can only be accessed with privilege access.
Unprivileged write to this FPIFx is discarded, unprivileged read returns 0.
0: No falling edge trigger request occurred
1: Rising edge trigger request occurred
This bit is set when the falling edge event arrives on the configurable event line. This bit is
cleared by writing a 1 into the bit.
Bit 20:17 Reserved, must be kept at reset value.
Bits 16:0 FPIF[16:0]: configurable event inputs x falling edge pending bit (where x = 0 to 16)
When EXTI_SECCFGR.SECx is disabled, FPIFx can be accessed with non-secure and
secure access.
When EXTI_SECCFGR.SECx is enabled, FPIFx can only be accessed with secure access.
Non-secure write to this FPIFx is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, FPIFx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, FPIFx can only be accessed with privilege access.
Unprivileged write to this FPIFx is discarded, unprivileged read returns 0.
0: No falling edge trigger request occurred
1: Rising edge trigger request occurred
This bit is set when the falling edge event arrives on the configurable event line. This bit is
cleared by writing a 1 into the bit.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
SEC31 SEC30 SEC29 SEC28 SEC27 SEC26 SEC25 SEC24 SEC23 SEC22 SEC21 SEC20 SEC19 SEC18 SEC17 SEC16
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
SEC15 SEC14 SEC13 SEC12 SEC11 SEC10 SEC9 SEC 8 SEC7 SEC6 SEC5 SEC4 SEC3 SEC2 SEC1 SEC0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 549/2187
RM0438 Extended interrupts and event controller (EXTI)
562
17.6.7 EXTI privilege configurat ion register (EXTI_PRIVCFGR1)
Address offset: 0x018
Reset value: 0x0000 0000
This register provides privileged write access protection. An unprivileged read returns the
register data.
Contains only register bits for security capable input events.
17.6.8 EXTI rising trigger sel ection register (EXTI_RTSR2)
Address offset: 0x020
Reset value: 0x0000 0000
Contains only register bits for configurable events.
Bits 31:0 SEC[31:0]: Security enable on event input x (where x = 0 to 31)
When EXTI_PRIVCFGRn.PRIVx is disabled, SECx can be accessed with privilege and
unprivileged access.
When EXTI_PRIVCFGRn.PRIVx is enabled, SECx can only be written with privilege access.
Unprivileged write to this SECx is discarded.
0: Event security disabled (non-secure)
1: Event security enabled (secure)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
PRIV31 PRIV30 PRIV29 PRIV28 PRIV27 PRIV26 PRIV25 PRIV24 PRIV23 PRIV22 PRIV21 PRIV20 PRIV19 PRIV18 PRIV17 PRIV16
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
PRIV15 PRIV14 PRIV13 PRIV12 PRIV11 PRIV10 PRIV9 PRIV8 PRIV7 PRIV6 PRIV5 PRIV4 PRIV3 PRIV2 PRIV1 PRIV0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 PRIV[31:0]: Security enable on event input x (where x = 0 to 31)
When EXTI_SECCFGR.SECx is disabled, PRIVx can be accessed with secure and non-
secure access.
When EXTI_SECCFGR.SECx is enabled, PRIVx can only be written with secure access.
Non-secure write to this PRIVx is discarded.
0: Event privilege disabled (unprivileged)
1: Event privilege enabled (privileged)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
Res. Res. Res. Res. Re s. Res. Res. Res. Res. RT38 RT37 RT36 RT35 Res. Res. Res.
rw rw rw rw

Extended interrupts and event controller (EXTI) RM0438
550/2187 RM0438 Rev 8
17.6.9 EXTI falling trigger selec tion register (EXTI_FTSR2)
Address offset: 0x024
Reset value: 0x0000 0000
Contains only register bits for configurable events.
Bits 31:7 Reserved, must be kept at reset value.
Bits 6:3 RT[38:35]: Rising trigger event configuration bit of configurable event input x(1) (where x = 35
to 38).
When EXTI_SECCFGR.SECx is disabled, RTx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, RTx can only be accessed with secure access.
Non-secure write to this RTx is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, RTx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, RTx can only be accessed with privilege access.
Unprivileged write to this RTx is discarded, unprivileged read returns 0.
0: Rising trigger disabled (for event and interrupt) for input line
1: Rising trigger enabled (for event and interrupt) for input line
Bits 2:0 Reserved, must be kept at reset value.
1. The configurable event inputs are edge triggered, no glitch  must be generated on these inputs. If a falling edge on the
configurable event input occurs during writing of the register, the associated pending bit is not set.
Rising and falling edge triggers can be set for the same configurable event input. In this case, both edges generate a
trigger.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
Res. Res. Res. Res. Re s. Res. Res. Res. Res. FT38 FT37 FT36 FT35 Res. Res. Res.
rw rw rw rw
Bits 31:7 Reserved, must be kept at reset value.
Bits 6:3 FT[38:35]: Falling trigger event configuration bit of configurable event input x(1) (where x = 35
to 38)
When EXTI_SECCFGR.SECx is disabled, FTx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, FTx can only be accessed with secure access. Non-
secure write to this FTx is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, FTx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, FTx can only be accessed with privilege access.
Unprivileged write to this FTx is discarded, unprivileged read returns 0.
0: Falling trigger disabled (for event and interrupt) for input line
1: Falling trigger enabled (for event and interrupt) for input line
Bits 2:0 Reserved, must be kept at reset value.

RM0438 Rev 8 551/2187
RM0438 Extended interrupts and event controller (EXTI)
562
17.6.10 EXTI software interrupt  event register (EXTI_SWIER2)
Address offset: 0x028
Reset value: 0x0000 0000
Contains only register bits for configurable events.
17.6.11 EXTI rising edge pe nding register (EXTI_RPR2)
Address offset: 0x02C
Reset value: 0x0000 0000
Contains only register bits for configurable events.
1. The configurable event inputs are edge trigger ed, no glitch must be generated on these inputs.
If a falling edge on the configurable event input occurs during writing of the register, the associated pending bit is not set.
Rising and falling edge triggers can be set for the same configurable event input. In this case, both edges generate a
trigger.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
Res. Res. Res. Res. Re s. Res. Res. Res. Res. S W I 3 8S W I 3 7S W I 3 6S W I 3 5 Res. Res. Res.
rw rw rw rw
Bits 31:7 Reserved, must be kept at reset value.
Bits 6:3 SWI[38:35]: Software interrupt on event x (where x = 35 to 38)
When EXTI_SECCFGR.SECx is disabled, SWIx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, SWIx can only be accessed with secure access.
Non-secure write to this SWIx is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, SWIx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, SWIx can only be accessed with privilege access.
Unprivileged write to this SWIx is discarded, unprivileged read returns 0.
A software interrupt is generated independent from the setting in EXTI_RTSR and
EXTI_FTSR. It always return 0 when read.
0: Writing 0 has no effect.
1: Writing a 1 to this bit triggers a rising edge event on event x+32. This bit is auto cleared by
HW.
Bits 2:0 Reserved, must be kept at reset value.

Extended interrupts and event controller (EXTI) RM0438
552/2187 RM0438 Rev 8
17.6.12 EXTI falling edge pend ing register (EXTI_FPR2)
Address offset: 0x030
Reset value: 0x0000 0000
Contains only register bits for configurable events.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
Res. Res. Res. Res. Res. Res. Res. Res. Res. RPIF38 RPIF37 RPIF36 RPIF35 Res. Res. Res.
rc_w1 rc_w1 rc_w1 rc_w1
Bits 31:7 Reserved, must be kept at reset value.
Bits 6:3 RPIF[38:35]: configurable event inputs x rising edge pending bit (where x = 35 to 38).
When EXTI_SECCFGR.SECx is disabled, RPIFx can be accessed with non-secure and
secure access.
When EXTI_SECCFGR.SECx is enabled, RPIFx can only be accessed with secure access.
Non-secure write to this RPIFx is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, RPIF can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, RPIFx can only be accessed with privilege access.
Unprivileged write to this RPIFx is discarded, unprivileged read returns 0.
0: No rising edge trigger request occurred
1: Rising edge trigger request occurred
This bit is set when the rising edge event or an EXTI_SWIER software trigger arrives on the
configurable event line. This bit is cleared by writing a 1 into the bit.
Bits 2:0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
Res. Res. Res. Res. Res. Res. Res. Res. Res. FPIF38 FPIF37 FPIF36 FPIF35 Res. Res. Res.
rc_w1 rc_w1 rc_w1 rc_w1

RM0438 Rev 8 553/2187
RM0438 Extended interrupts and event controller (EXTI)
562
17.6.13 EXTI security enable  register (EXTI_SECCFGR2)
Address offset: 0x034
Reset value: 0x0000 0000
This register provides write access security, a non-secure write access is ignored and
causes the generation of an illegal access event. A non-secure read returns the register
data.
Contains only register bits for security capable Input events.
17.6.14 EXTI privilege enable  register (EXTI_PRIVCFGR2)
Address offset: 0x038
Reset value: 0x0000 0000
Bits 31:7 Reserved, must be kept at reset value.
Bits 6:3 FPIF[38:35]: configurable event inputs x pending bit (where x = 35 to 38).
When EXTI_SECCFGR.SECx is disabled, FPIFx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, FPIFx can only be accessed with secure access.
Non-secure write to this FPIFx is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, FPIFx can be accessed with unprivileged and
privilege access.
When EXTI_PRIVCFGR.PRIVx is enabled, FPIFx can only be accessed with privilege access.
Unprivileged write to this FPIFx is discarded, unprivileged read returns 0.
0: No fallling edge trigger request occurred
1: Rising edge trigger request occurred
This bit is set when the falling edge event arrives on the configurable event line. This bit is
cleared by writing a 1 into the bit.
Bits 2:0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. SEC42 SEC41 SEC40 SEC39 SEC38 SEC37 SEC36 SEC35 SEC34 SEC33 SEC32
rw rw rw rw rw rw rw rw rw rw rw
Bits 31:11 Reserved, must be kept at reset value.
Bits 10:0 SEC[42:32]: Security enable on event input x (where x = 32 to 42)
When EXTI_PRIVCFGRn.PRIVx is disabled, SECx can be accessed with privilege and
unprivileged access.
When EXTI_PRIVCFGRn.PRIVx is enabled, SECx can only be written with privilege access.
Unprivileged write to this SECx is discarded
0: Event security disabled (non-secure)
1: Event security enabled (secure)

Extended interrupts and event controller (EXTI) RM0438
554/2187 RM0438 Rev 8
This register provides privileged write access protection, an unprivileged write access is
discarded and causes the generation of an illegal access event. An unprivileged read
returns the register data.
Contains only register bits for security capable Input events.
17.6.15 EXTI external interrupt se lection register (EXTI_EXTICRn)
Address offset: 0x060 (EXTI_EXTICR1) EXTI mux 0, 1, 2, 3 (m =0)
Address offset: 0x064 (EXTI_EXTICR2) EXTI mux 4, 5, 6, 7 (m = 4)
Address offset: 0x068 (EXTI_EXTICR3) EXTI mux 8, 9, 10, 11 (m = 8)
Address offset: 0x06C (EXTI_EXTICR4) EXTI mux 12, 13, 14, 15 (m = 12)
Reset value: 0x0000 0000
EXTIm fields contain only the number of bits in line with the nb_ioport configuration.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. PRIV42 PRIV41 PRIV40 PRIV39 PRIV38 PRIV37 PRIV36 PRIV35 PRIV34 PRIV33 PRIV32
rw rw rw rw rw rw rw rw rw rw rw
Bits 31:11 Reserved, must be kept at reset value.
Bits 10:0 PRIV[42:32]: Privilege enable on event input x (where x = 32 to 42)
When EXTI_SECCFGR.SECx is disabled, PRIVx can be accessed with secure and non-
secure access.
When EXTI_SECCFGR.SECx is enabled, PRIVx can only be accessed with secure access.
Non-secure write to this PRIVx is discarded.
0: Event privilege disabled (unprivileged)
1: Event security enabled (privileged)
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
EXTIm+3[7:0] EXTIm+2[7:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
EXTIm+1[7:0] EXTIm[7:0]
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 555/2187
RM0438 Extended interrupts and event controller (EXTI)
562
Bits 31:24 EXTIm+3[7:0]: EXTIm+3 GPIO port selection (where m = 0, 4, 8, or 12 for respectively
EXTI_EXTICR[1:4]).
These bits are written by software to select the source input for EXTIm+3 external interrupt.
When EXTI_SECCFGR.SEC(m+3) is disabled, EXTI(m+3) can be accessed with non-secure
and secure access.
When EXTI_SECCFGR.SEC(m+3) is enabled, EXTI(m+3) can only be accessed with secure
access. Non-secure write is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIV(m+3) is disabled, EXTI(m+3) can be accessed with privilege
and unprivileged access.
When EXTI_PRIVCFGR.PRIV(m+3) is enabled, EXTI(m+3) can only be accessed with
privilege access. Unprivileged write to this bit is discarded.
0x00: PA[m+3] pin
0x01: PB[m+3] pin
0x02: PC[m+3] pin
0x03: PD[m+3] pin
0x04: PE[m+3] pin
0x05: PF[m+3] pin
0x06: PG[m+3] pin
0x07: PH[m+3] pin
Others reserved

Extended interrupts and event controller (EXTI) RM0438
556/2187 RM0438 Rev 8
Bits 23:1 EXTIm+2[7:0]: EXTIm+2 GPIO port selection (where m = 0, 4, 8, or 12 for respectively
EXTI_EXTICR[1:4])(where m = 0, 4, 8, or 12 for respectively EXTI_EXTICR[1:4]).
These bits are written by software to select the source input for EXTIm+2 external interrupt.
When EXTI_SECCFGR.SEC(m+2) is disabled, EXTI(m+2) can be accessed with non-secure
and secure access.
When EXTI_SECCFGR.SEC(m+2) is enabled, EXTI(m+2) can only be accessed with secure
access. Non-secure write is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIV(m+2) is disabled, EXTI(m+2) can be accessed with privilege
and unprivileged access.
When EXTI_PRIVCFGR.PRIV(m+2) is enabled, EXTI(m+2) can only be accessed with
privilege access. Unprivileged write to this bit is discarded.
0x00: PA[m+2] pin
0x01: PB[m+2] pin
0x02: PC[m+2] pin
0x03: PD[m+2] pin
0x04: PE[m+2] pin
0x05: PF[m+2] pin
0x06: PG[m+2] pin
0x07: PH[m+2] pin
Others reserved
Bits 15:8 EXTIm+1[7:0]: EXTIm+1 GPIO port selection (where m = 0, 4, 8, or 12 for respectively
EXTI_EXTICR[1:4]).
These bits are written by software to select the source input for EXTIm+1 external interrupt.
When EXTI_SECCFGR.SEC(m+1) is disabled, EXTI(m+1) can be accessed with non-secure
and secure access.
When EXTI_SECCFGR.SEC(m+1) is enabled, EXTI(m+1) can only be accessed with secure
access. Non-secure write is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVm+1 is disabled, EXTI(m+1) can be accessed with privilege and
unprivileged access.
When EXTI_PRIVCFGR.PRIVm+1 is enabled, EXTI(m+1) can only be accessed with privilege
access. Unprivileged write to this bit is discarded.
0x00: PA[m+1] pin
0x01: PB[m+1] pin
0x02: PC[m+1] pin
0x03: PD[m+1] pin
0x04: PE[m+1] pin
0x05: PF[m+1] pin
0x06: PG[m+1] pin
0x07: PH[m+1] pin
Others reserved

RM0438 Rev 8 557/2187
RM0438 Extended interrupts and event controller (EXTI)
562
17.6.16 EXTI lock re gister (EXTI_LOCKR)
Address offset: 0x070
Reset value: 0x0000 0000
This register provides both write access security, a non-secure write access is ignored and a
read access returns zero data, and generate an illegal access event.
17.6.17 EXTI CPU wakeup with inte rrupt mask register (EXTI_IMR1)
Address offset: 0x080
Reset value: 0xFF9E 0000
Bits 7:0 EXTIm[7:0]: EXTIm GPIO port selection (where m = 0, 4, 8, or 12 for respectively
EXTI_EXTICR[1:4]).
These bits are written by software to select the source input for EXTIm external interrupt.
When EXTI_SECCFGR.SEC(m) is disabled, EXTI(m) can be accessed with non-secure and
secure access.
When EXTI_SECCFGR.SEC(m) is enabled, EXTI(m) can only be accessed with secure
access. Non-secure write is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIV(m) is disabled, EXTI(m) can be accessed with privilege and
unprivileged access.
When EXTI_PRIVCFGR.PRIV(m) is enabled, EXTI(m) can only be accessed with privilege
access. Unprivileged write to this bit is discarded
0x00: PA[m] pin
0x01: PB[m] pin
0x02: PC[m] pin
0x03: PD[m] pin
0x04: PE[m] pin
0x05: PF[m] pin
0x06: PG[m] pin
0x07: PH[m] pin
Others reserved
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
Res. Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. Res. LOCK
rs
Bits 31:1 Reserved, must be kept at reset value.
Bit 0 LOCK: Global security and privilege configuration registers EXTI_SECCFGR and
EXTI_PRIVCFGR lock.
This register bit is write once after reset.
0: Security and privilege configuration open, can be modified.
1: Security and privilege configuration locked, can no longer be modified.

Extended interrupts and event controller (EXTI) RM0438
558/2187 RM0438 Rev 8
Contains register bits for configurable events and direct events.
17.6.18 EXTI CPU wakeup with e vent mask register (EXTI_EMR1)
Address offset: 0x084
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
IM31 IM30 IM29 IM28 IM27 IM26 IM25 IM24 IM23 IM22 IM21 IM20 IM19 IM18 IM17 IM16
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
IM15 IM14 IM13 IM12 IM11 IM10 IM9 IM8 IM7 IM6 IM5 IM4 IM3 IM2 IM1 IM0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 IM[31:0]: CPU wakeup with interrupt mask on event input x (1) (where x = 0 to 31).
When EXTI_SECCFGR.SECx is disabled, IMx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, IMx can only be accessed with secure access. Non-
secure write to this bit is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, IMx can be accessed with privilege and
unprivileged access.
When EXTI_PRIVCFGR.PRIVx is enabled, IMx can only be accessed with privilege access.
Unprivileged write to this bit is discarded.
0: Wakeup with interrupt request from input event x is masked
1: Wakeup with interrupt request from input event x is unmasked
1. The reset value for configurable event inputs is set to ‘0’ in order to disable the interrupt by default.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
EM31 EM30 EM29 EM28 EM27 EM26 EM25 EM24 EM23 EM22 EM21 EM20 EM19 EM18 EM17 EM16
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
EM15 EM14 EM13 EM12 EM11 EM10 EM9 EM8 EM7 EM6 EM5 EM4 EM3 EM2 EM1 EM0
rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw rw
Bits 31:0 EM[31:0]: CPU wakeup with event generation mask on event input x (where x = 0 to 31).
When EXTI_SECCFGR.SECENx is disabled, EMx can be accessed with non-secure and
secure access.
When EXTI_SECCFGR.SECENx is enabled, EMx can only be accessed with secure access.
Non-secure write to this bit x is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, EMx can be accessed with privilege and
unprivileged access.
When EXTI_PRIVCFGR.PRIVx is enabled, EMx can only be accessed with privilege access.
Unprivileged write to this bit is discarded.
0: Wakeup with event generation from Line x is masked
1: Wakeup with event generation from Line x is unmasked

RM0438 Rev 8 559/2187
RM0438 Extended interrupts and event controller (EXTI)
562
17.6.19 EXTI CPU wakeup with inte rrupt mask register (EXTI_IMR2)
Address offset: 0x090
Reset value: 0x0000 0787
Contains register bits for configurable events and direct events.
17.6.20 EXTI CPU wakeup with e vent mask register (EXTI_EMR2)
Address offset: 0x094
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9 87654321 0
Res. Res. Res. Res. Res. IM42 IM41 IM40 Res. IM38 IM37 IM36 IM35 IM34 IM33 IM32
rw rw rw rw rw rw rw rw rw rw
Bits 31:11 Reserved, must be kept at reset value.
Bits 10:0 IM[42:40]: CPU wakeup with interrupt mask on event input x (1) (where x = 40 to 42).
When EXTI_SECCFGR.SECx is disabled, IMx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, IMx can only be accessed with secure access. Non-
secure write to this bit is discarded, non-secure read returns 0..
When EXTI_PRIVCFGR.PRIVx is disabled, IMx can be accessed with privilege and
unprivileged access.
When EXTI_PRIVCFGR.PRIVx is enabled, IMx can only be accessed with privilege access.
Unprivileged write to this bit is discarded.
0: Wakeup with interrupt request from input event x is masked
1: Wakeup with interrupt request from input event x is unmasked
Bit 7 Reserved, must be kept at reset value.
Bits 6:0 IM[38:32]: CPU wakeup with interrupt mask on event input x(1) (where x = 32 to 38).
When EXTI_SECCFGR.SECx is disabled, IMx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, IMx can only be accessed with secure access. Non-
secure write to this bit is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, IMx can be accessed with privilege and
unprivileged access.
When EXTI_PRIVCFGR.PRIVx is enabled, IMx can only be accessed with privilege access.
Unprivileged write to this bit is discarded.
0: Wakeup with interrupt request from input event x is masked
1: Wakeup with interrupt request from input event x is unmasked
1. The reset value for configurable event inputs is set to ‘0’ in order to disable the interrupt by default.

Extended interrupts and event controller (EXTI) RM0438
560/2187 RM0438 Rev 8
17.6.21 EXTI register map
The following table gives the EXTI register map and the reset values.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Res. Res. Res. Res. Res. EM42 EM41 EM40 Res. EM38 EM37 EM36 EM35 EM34 EM33 EM32
rw rw rw rw rw rw rw rw rw rw
Bits 31:11 Reserved, must be kept at reset value.
Bits 10:0 EM[42:40]: CPU wakeup with event generation mask on event input(1) (where x = 40 to 42).
When EXTI_SECCFGR.SECx is disabled, EMx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, EMx can only be accessed with secure access.
Non-secure write to this bit x is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, EMx can be accessed with privilege and
unprivileged access.
When EXTI_PRIVCFGR.PRIVx is enabled, EMx can only be accessed with privilege access.
Unprivileged write to this bit is discarded.
0: Wakeup with event generation from line x is masked
1: Wakeup with event generation from line x is unmasked
Bit 7 Reserved, must be kept at reset value.
Bits 6:0 EM[38:32]: CPU wakeup with event generation mask on event input x(1) (where x = 32 to 38).
When EXTI_SECCFGR.SECx is disabled, EMx can be accessed with non-secure and secure
access.
When EXTI_SECCFGR.SECx is enabled, EMx can only be accessed with secure access.
Non-secure write to this bit x is discarded, non-secure read returns 0.
When EXTI_PRIVCFGR.PRIVx is disabled, EMx can be accessed with privilege and
unprivileged access.
When EXTI_PRIVCFGR.PRIVx is enabled, EMx can only be accessed with privilege access.
Unprivileged write to this bit is discarded.
0: Wakeup with event generation from line x is masked
1: Wakeup with event generation from line x is unmasked
1. The reset value for configurable event inputs is set to ‘0’ in order to disable the interrupt by default.
[Table 117](../tables/table_117.md). Extended interrupt/event controller register map and reset values
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
0x000 EXTI_RTSR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
RT[22:21]
Res.
Res.
Res.
Res.
RT[16:0]
R e s e t  v a l u e 00 00000000000000000

RM0438 Rev 8 561/2187
RM0438 Extended interrupts and event controller (EXTI)
562
0x004 EXTI_FTSR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
FT[22:21]
Res.
Res.
Res.
Res.
FT[16:0]
R e s e t  v a l u e 00 00000000000000000
0x008 EXTI_SWIER1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SWI[22:21]
Res.
Res.
Res.
Res.
SWi[16:0]
R e s e t  v a l u e 00 00000000000000000
0x00C EXTI_RPR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
RPIF[22:21]
Res.
Res.
Res.
Res.
RPIF[16:0]
R e s e t  v a l u e 00 00000000000000000
0x010 EXTI_FPR1
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
FPIF[22:21]
Res.
Res.
Res.
Res.
FPIF[16:0]
R e s e t  v a l u e 00 00000000000000000
0x014
EXTI_SECCFGR
1 SEC[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x018 EXTI_PRIVCFG1 PRIV[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x020 EXTI_RTSR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
RT
[38:35]
Res.
Res.
Res.
Reset value 0000
0x024 EXTI_FTSR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
FT
[38:35]
Res.
Res.
Res.
Reset value 0000
0x028 EXTI_SWIER2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SWI
[38:35]
Res.
Res.
Res.
Reset value 0000
0x02C EXTI_RPR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
RPIF
[38:35]
Res.
Res.
Res.
Reset value 0000
0x030 EXTI_FPR2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
FPIF
[38:35]
Res.
Res.
Res.
Reset value 0000
0x034 EXTI_SECCFG2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
SEC[42:32]
Reset value 00000000000
0x038 EXTI_PRIVCFG2
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
PRIV[42:32]
Reset value 00000000000
[Table 117](../tables/table_117.md). Extended interrupt/event controller register map and reset values (continued)
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

Extended interrupts and event controller (EXTI) RM0438
562/2187 RM0438 Rev 8
Refer to Section 2.3 on page 86 for the register boundary addresses.
0x060 EXTI_EXTICR1 EXTI3[7:0] EXTI2[7:0] EXTI1[7:0] EXTI0[7:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x064 EXTI_EXTICR2 EXTI7[7:0] EXTI6[7:0] EXTI5[7:0] EXTI4[7:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x068 EXTI_EXTICR3 EXTI11[7:0] EXTI10[7:0] EXTI9[7:0] EXTI8[7:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x06C EXTI_EXTICR4 EXTI15[7:0] EXTI14[7:0] EXTI13[7:0] EXTI2[7:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x070 EXTI_LOCKR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
LOCK
Reset value 0
0x080 EXTI_IMR1 IM[31:0]
R e s e t  v a l u e 11111111100111100000000000000000
0x084 EXTI_EMR1 EM[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x088-
0x08C Reserved
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
0x090 EXTI_IMR2 IM[42:32]
Reset value 11110000111
0x094 EXTI_EMR2 EM[42:32]
Reset value 00000000000
[Table 117](../tables/table_117.md). Extended interrupt/event controller register map and reset values (continued)
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
* [Figure 47: Architectural Diagram](../figures/figure_47.md)
* [Figure 48: Architectural Diagram](../figures/figure_48.md)
* [Figure 49: Architectural Diagram](../figures/figure_49.md)
* [Figure 50: Architectural Diagram](../figures/figure_50.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 110: Configuration Matrix](../tables/table_110.md)
* [Table 111: Configuration Matrix](../tables/table_111.md)
* [Table 112: Configuration Matrix](../tables/table_112.md)
* [Table 113: Configuration Matrix](../tables/table_113.md)
* [Table 114: Configuration Matrix](../tables/table_114.md)
* [Table 115: Configuration Matrix](../tables/table_115.md)
* [Table 116: Configuration Matrix](../tables/table_116.md)
* [Table 117: Configuration Matrix](../tables/table_117.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)