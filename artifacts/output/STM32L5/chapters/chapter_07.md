# Chapter 7: Instruction cache (ICACHE)

## 1. Chapter Overview & Technical Scope
Official STMicroelectronics STM32L5 Reference Manual RM0438 - Chapter 7: Instruction cache (ICACHE).
* **Document Source**: RM0438 Reference Manual
* **PDF Reference Location**: Pages 242 - 258
* **Taxonomy Section**: CHAPTERS


## 2. Official Reference Manual Text Content (RM0438 Ingestion)
```text
Instruction cache (ICACHE) RM0438
242/2187 RM0438 Rev 8
7 Instruction cache (ICACHE)
7.1 ICACHE introduction
The instruction cache (ICACHE) is introduced on the C-AHB code bus of the Cortex®-M33
processor, to improve performance when fetching instructions and data from internal and
external memories.
Some specific features, like dual master ports, hit-under-miss, and critical-word-first refill
policy, result in close to zero-wait-state performance in most use cases.
7.2 ICACHE main features
The main features of ICACHE are listed below:
• Bus interface
– One 32-bit AHB slave port, the execution port (input from Cortex ®-M33 C-AHB
code interface)
– Two AHB master ports: master1 and master 2 ports, with outputs to Fast and Slow
buses of main AHB bus matrix, respectively
– One 32-bit AHB slave port for control (input from AHB peripherals interconnect, for
ICACHE registers access)
• Cache access
– 0 wait-state on hits
– Hit-under-miss capability: ab ility to serve processor requests (access to cached
data) during an ongoing line refill due to a previous cache miss
– Dual master access: feature used to decouple the traffic according to targeted
memory. For example, the ICACHE assigns fast traffic (addressing flash
memories and SRAMs) to the AHB master1 port, and slow traffic (addressing
external memories) to the AHB master2 port, thus preventing processor stalls on
line refills from external memories. This allows ISR (interrupt service routine)
fetching on internal flash memory to take place in parallel with a cache line refill
from external memories.
– Minimal impact on interrupt la tency, thanks to dual master
– Optimal cache line refill thanks to WRAPw bursts of the size of the cache line
(32-bit word size, w, aligned on cache line size)
– n-way set-associative defaul t configuration with possibility to configure as 1-way,
means direct mapped cache, for applications needing very-low-power
consumption profile
• Memory address remap
– Possibility to remap input add ress falling into up to four memory regions (used to
remap aliased code in external memories to the code region, for execution from
the C-AHB code interface)
• Replacement and refill
– pLRU-t (pseudo-least-recent ly-used, based on binary tree) replacement policy,
algorithm with best complexity/performance balance
– Critical-word-first refill policy, minimizing processor stalls

RM0438 Rev 8 243/2187
RM0438 Instruction cache (ICACHE)
258
– Possibility to configure burst type of  AHB memory transaction for remapped
regions: INCRw or WRAPw (size w aligned on cache line size)
• Performance counters
The ICACHE implements two performance counters:
– Hit monitor counter (32-bit)
– Miss monitor counter (16-bit)
• Error management
– Possibility to detect an unex pected cacheable write access, to flag an error, and
optionally, to raise an interrupt
• TrustZone® security support
• Maintenance operation
– Cache invalidate: full cache invalidation, fast command, noninterruptible
7.3 ICACHE implementation
7.4 ICACHE functional description
The purpose of this block is to cache instruction fetches or instruction memories loads,
coming from the processor. As such, the ICACHE manages only cacheable read
transactions, and does not manage cacheable write transactions.
The noncacheable transactions (both read and write) bypass the ICACHE.
For the error management purpose, if a write cacheable transaction is presented (this
happens only in case of bad software programming), the ICACHE sets an error flag and, if
enabled, raises an interrupt to the processor.
[Table 54](../tables/table_54.md). ICACHE features
Feature ICACHE
Number of ways 2
Cache size 8K b y t e s
Cache line width 16 bytes
Range granularity of memory regions to be remapped 2 Mbytes
Number of regions to remap 4
Data size of AHB slave interface 32 bits
Data size of AHB fast master1 interface 32 bits
Data size of AHB slow master2 interface 32 bits

Instruction cache (ICACHE) RM0438
244/2187 RM0438 Rev 8
7.4.1 ICACHE block diagram
[Figure 18](../figures/figure_18.md). ICACHE block diagram
7.4.2 ICACHE reset and clocks
The ICACHE is clocked on the Cortex®-M33 C-AHB bus clock.
When the ICACHE reset signal is released, a cache invalidate procedure is automatically
launched, making the ICACHE busy (ICACHE_SR = 0x0000 0001).
When this procedure is finished:
• the ICACHE is invalidated: “cold cache”, with all cache line valid bits = 0 (ICACHE must
be filled up)
• ICACHE_SR = 0x0000 0002 (reflecting the cache is no longer busy)
• the ICACHE is disabled: the EN bit in ICACHE_CR holds its reset state (= 0).
Note: When disabled, the ICACHE is bypassed, except the remapping mechanism that is still
functional: slave input requests (remapped or not) are forwarded to the master port(s).
MSv48191V3
AHB
AHB
AHB
AHB
Region 0 cfg
Region 1 cfg
Region 2 cfg
Region 3 cfg
Hit monitor
Miss monitor
Control
Status
Configuration interface
Execution
port
Cortex-M33C-AHB
Main AHB
Execution port interface
Configuration
slave port
Master1
port
Master2
port
Master port interfacepLRU-t REMAP
Cache control logic
Cache memory port
Cache
TAG
memories
Cache
data
memories
Cache
FSM
n ways n waysICACHE
icache_it

RM0438 Rev 8 245/2187
RM0438 Instruction cache (ICACHE)
258
7.4.3 ICACHE TAG memory
The ICACHE TAG memory contains:
• address tags indicating which data are contained in the cache data memories
• validity bits
There is one valid bit per cache line (per way).
The valid bit is set when a cache line is refilled (after a miss).
Valid bits are reset in any of the below cases:
• after the ICACHE reset is released
• when the cache is disabled, by setting EN = 0 in ICACHE_CR (by software)
• when executing an ICACHE invalidate command, by setting CACHEINV = 1
in ICACHE_CR (by software)
When a cacheable transaction is received at the execution input port, its AHB address
(HADDR_in) is split into the following fields (see [Table 55](../tables/table_55.md) for B and W definitions):
• HADDR_in[B-1:0]: address byte offset, indicates which byte to select inside
a cache line.
• HADDR_in[B+W-1:B]: address way index, indicates which cache line to select
inside each way.
• HADDR_in[31:B+W]: tag address, to be compared to the TAG memory address
to check if the requested data is already available (meaning valid) inside the ICACHE.
The following table gives a summary of the ICACHE main parameters for TAG memory
dimensioning. [Figure 19](../figures/figure_19.md) shows the functional view of TAG and data memories, for an n-way
set associative ICACHE.
[Table 55](../tables/table_55.md). TAG memory dimensioning parameters
for n-way set associative operating mode (default)
Parameter Value Example
Cache size S Kbytes = s bytes (s = 1024 x S) 8 Kbytes = 8192 bytes
Cache number of ways n 2
Cache line size L-byte = l-bit (l = 8 x L) 16-byte = 128-bit
Number of cache lines LpW = s / (n x L) lines / way 256 lines / way
Address byte offset size B = log 2(L) bit 4-bit
Address way index size W = log 2(LpW) bit 8-bit
TAG address size T = (32 - W - B) bit 20-bit

Instruction cache (ICACHE) RM0438
246/2187 RM0438 Rev 8
[Figure 19](../figures/figure_19.md). ICACHE TAG and data memories functional view
7.4.4 Direct-mapped ICACHE (1-way cache)
The default configuration (at reset) is an n-way set associative cache (WAYSEL = 1 in
ICACHE_CR), but the user can configure the ICACHE as direct mapped by writing
WAYSEL = 0 (only possible when the cache is disabled, EN = 0 in ICACHE_CR).
The following table gives a summary of ICACHE main parameters for TAG memory when
the direct-mapped cache operating mode is selected.
MSv48192V2
==
LpW lines / way
OffsetIndexTAG
pLRU-t
l-bit
T-bit W-bit B-bit
T-bit
Data_Way0
Data_Way(n-1)
Data memory
==
AHB_address
(HADDR_in)
LpW lines / way
n ways
TAG_Way(n-1)Vn-1
V0 TAG_Way0
TAG memory
n ways
way selection
(for replacement)
Cache hit/miss, in Way(n-1)
Cache hit/miss, in Way0
[Table 56](../tables/table_56.md). TAG memory dimensioning parameters for direct-mapped cache mode
Parameter Value Example
Cache size S Kbytes = s bytes (s = 1024 x S) 8 Kbytes = 8192 bytes
Cache number of ways 1 1
Cache line size L-byte = l-bit (l = 8 x L) 16-byte = 128-bit
Number of cache lines LpW = s / L lines 512 lines
Address byte offset size B = log 2(L) bit 4-bit
Address way index size W = log 2(LpW) bit 9-bit
TAG address size T = (32 - W - B) bit 19-bit

RM0438 Rev 8 247/2187
RM0438 Instruction cache (ICACHE)
258
All cache operations (such as read, refill, remapping, invalidation) remain the same in the
direct-mapped configuration. The only difference is the absence of a replacement algorithm
in case of line eviction (as explained in Section 7.4.8): only one way (the unique one) is
possible for any data refill.
7.4.5 ICACHE enable
To activate the ICACHE, the EN bit in ICACHE_CR must be set to 1.
When the ICACHE is disabled, it is bypassed and all transactions are copied from the slave
to the master ports in the same clock cycle.
It is recommended to initialize or modify the main memory content (region to be later
cached) with the ICACHE disabled, and to enable the ICACHE only when this region
remains unchanged (an enabled ICACHE detects cacheable write transactions as errors).
To ensure performance determinism, it is recommended to wait for the end of a potential
cache invalidate procedure before enabling the ICACHE. This procedure occurs when the
hardware reset signal is released, when CACHEINV is set, or when EN is cleared in
ICACHE_CR. During the procedure, BUSYF is set in ICACHE_SR, and once finished,
BUSYF is cleared and BSYENDF is set in the same register (raising the ICACHE interrupt if
enabled on such a busy end condition).
The software must test BUSYF and/or BSYENDF values before enabling the ICACHE.
Else, if the ICACHE is enabled before the end of an invalidate procedure, any cache access
(while BUSYF = 1) is treated as noncacheable, and its performance depends on the main
memory access time.
The address remapping is performed, whether the ICACHE is enabled or not, if the input
transaction address falls into the memory regions defined and enabled in ICACHE_CRRx
(see [Figure 20](../figures/figure_20.md)).
The ICACHE is, by default, disabled at boot.
7.4.6 Cacheable and noncacheable traffic
The ICACHE is developed for the Cortex®-M33 core. It is placed on the C-AHB bus, and
thus caches the code memory region, ranging from address 0x0000 0000 to 0x1FFF FFFF
of the memory map.
To make other memory regions cacheable, the ICACHE supports a memory region
remapping feature, used to define up to four external memory regions, whose addresses
have an alias in the code region. Addressing these memory regions through their code alias
address allows the memory request to be routed to the C-AHB bus, and to be managed by
the ICACHE.
Any external memory space physically mapped at an address in the range
[0x6000 0000:0xAFFF FFFF] can be aliased with an address in the range
[0x0000 0000:0x07FF FFFF] or [0x1000 0000:0x1FFF FFFF].
For a given memory request in the code region, the ICACHE implements the address
remapping functionality first. If aliased, it is the remapped address, which is then cached,
and, if needed, provided to the master port to address the main AHB bus matrix.
The destination physical address does not need further manipulation on the AHB bus.
The remapping functionality is available also for noncacheable traffic, and when the cache
is disabled.

Instruction cache (ICACHE) RM0438
248/2187 RM0438 Rev 8
Additional details on address remapping are provided in Section 7.4.7.
An incoming memory request to the ICACHE is defined as cacheable according to its AHB
transaction memory lookup attribute, as shown in [Table 57](../tables/table_57.md). This AHB attribute depends on
the MPU (memory protection unit) programming for the addressed region.
In the case of a noncacheable access (read or write), the ICACHE is bypassed. The AHB
transaction is propagated unchanged to the master output port, except the transaction
address, which may be modified due to the address remapping feature (see Section 7.4.7).
The bypass, and eventual remap logic, does not increase the latency of the access to the
targeted memory.
In the case of a cacheable access, the ICACHE behaves as explained in Section 7.4.8.
Cacheable memory regions are defined and programmed by the user in the MPU
responsible for the generation of the AHB attribute signals for any transaction addressing a
given region.
[Table 58](../tables/table_58.md) summarizes programmable configurations of various memories.
7.4.7 Address remapping
The ICACHE allows an alias address to be defined in the code region for up to four  external
memory regions.
The address remapping is applied on the code alias address, transforming it into the
destination external physical address.
The remapping operation is fully software configurable by programming ICACHE_CRRx
(x = 0 to 3, number of remapped regions). This programming can be done only when the
ICACHE is disabled.
Each region x can be individually enabled with REN in ICACHE_CRRx. Once enabled, the
remap operation occurs even if the ICACHE is disabled, or if the transaction is
noncacheable.
[Table 57](../tables/table_57.md). ICACHE cacheability for AHB transaction
AHB lookup attribute Cacheability
1 Cacheable
0 Noncacheable
[Table 58](../tables/table_58.md). Memory configurations
Memory Cacheable
(MPU programming)
Remapped in the ICACHE
(ICACHE_CRRx programming)
Flash Yes or no Not required
SRAM Not recommended Not required
External
memories
Yes Required
No Required if the user wants code in external memories fetched
on C-AHB bus (else on S-AHB bus)

RM0438 Rev 8 249/2187
RM0438 Instruction cache (ICACHE)
258
Remap regions can have different size: each can be programmed in RSIZE of its
ICACHE_CRRx. The size of each region is a power of two multiple of range granularity
(2 Mbytes), with a minimum of 2 Mbytes, and a maximum of 128 Mbytes.
The address remapping mechanism is based on the matching of an incoming AHB address
(HADDR_in) with a given code subregion base-address, and the modification of this
address into its (remapped) physical address, as follows:
• HADDR_in belongs to region x if HADDR_in[31:RI] = 000:BASEADDR[28:RI], where:
– 000:BASEADDR is the code subregion base-address programmed in BASEADDR
of ICACHE_CRRx.
– RI defines the number of significant bits to consider. RI = log 2 (region size)
with a minimum value of 21 (for a 2-Mbyte region) and a maximum value of 27
(for a 128-Mbyte region).
• If the region x is enabled, the master port output AHB address (HADDR_out) is
composed by concatenating the two below parts:
– REMAPADDR[31:RI] field of ICACHE_CRRx as MSBs
– HADDR_in[RI-1:0] as LSBs
[Figure 20](../figures/figure_20.md) describes the matching and the output address generation.
[Figure 20](../figures/figure_20.md). ICACHE remapping address mechanism
[Table 59](../tables/table_59.md) summarizes all possible configurations of BASEADDR and REMAPADDR sizes
(number of significant MSBs) in ICACHE_CRRx, depending upon RSIZE.
[Table 59](../tables/table_59.md). ICACHE remap region size, base address, and remap address
Region size (Mbytes) Base address size (MSBs) Remap address (MSBs)
28 1 1
47 1 0
86 9
16 5 8
32 4 7
64 3 6
128 2 5
MSv48194V2
HADDR_in[RI-1:0]
31                                                                    RI RI-1                                 0
31                                                                    RI RI-1                                 0
000:
HADDR_in
HADDR_out
= =BASEADDR[28:RI]
Address in region x 0        1
REMAPADDR[31:RI]

Instruction cache (ICACHE) RM0438
250/2187 RM0438 Rev 8
Care must be taken while programming BASEADDR and REMAPADDR in ICACHE_CRRx:
if the programmed value is bigger than expected (number of MSBs, see [Table 59](../tables/table_59.md)),
the unneeded extra LSBs are ignored.
Typical remapping example: a 128-Mbyte external RAM region physically located in the
external address range [0x9000 0000:0x97FF FFFF], remapped in the code section range
[0x1800 0000:0x1FFF FFFF]:
• REMAPADDR[31:21] = 0x480
• BASEADDR[28:21] = 0xC0
• HADDR_in[31:27] is compared to 000:BASEADDR[28:27], while HADDR_in and
BASEADDR[26:21] are ignored.
If the comparison matches:
• HADDR_out[31:27] gets REMAPADDR[31:27] (in place of HADDR_in[31:27])
• HADDR_out[26:0] gets HADDR_in[26:0]
The software can program the kind of AHB burst generated by the ICACHE master ports on
the bus matrix (for cache line refill), by setting HBURST in ICACHE_CRRx with:
• WRAP for remapped external memories accessed through interfaces that can support
WRAP burst mode, providing the benefit of the critical-word-first feature performance:
– WRAP burst size = cache line size
– WRAP burst start address = word address of the first data requested by the core
• INCR: INCR burst mode for external memories accessed through the interfaces that do
not support WRAP burst mode (losing the benefit of critical-word-first feature):
– INCR burst size = cache line size
– INCR burst start address =  address aligned on the boundary of the cache line
containing the requested word.
Note: Coherency is needed when programming the SAU (secure attribution unit) and the MPU
(memory protection unit) attributes for both the external regions and their aliased code
subregions.
7.4.8 Cacheable accesses
When the ICACHE receives a cacheable transaction from the Cortex®-M33, it checks if the
address requested is present in its TAG memory, and if the corresponding cache line is
valid.
There are then three alternatives:
• The address is present inside the TAG memory, the cache line is valid: cache hit, the
data is read from the cache and provided to the processor in the same cycle.
• The address is not present in the TAG memory: cache miss, the data is read from
the main memory and provided to the processor, and a cache line refill is performed.
The critical-word-first policy ensures minimum wait cycles for the processor, since read
data can be provided while the cache still performs a cache line refill (associated
latency is the latency of fetching one word from the main memory).
The burst generated on the ICACHE master bus is WRAPw (w being the cache line
width, in words) if no address remap occurs. If an address remap occurs, the kind of
burst depends upon the HBURST programmed in corresponding ICACHE_CRRx.
The AHB transaction attributes are also propagated to the main AHB bus matrix on the
master port selected for the line refill.

RM0438 Rev 8 251/2187
RM0438 Instruction cache (ICACHE)
258
• The address is not present in TAG memory, but belongs to the refill burst from the main
memory currently ongoing: cache hit (hit-under-miss feature).
This happens during cache-line refill. The ICACHE can provide the requested data as
soon as data are available at its master interface, thus avoiding a miss (fetching data
from the main memory).
In the case of cache refill (due to cache miss), the ICACHE selects which cache line is
written with the refill data:
• In direct map (1-way) mode, only one line can be used to store the refill data: the line
pointed by the index of the input address.
• In n-way set associative mode, one line among n can be used (the line pointed by the
address index, in each of the n ways). The way selection is based on a pLRU-t
replacement algorithm that points, for each index, on the way candidate for the next
refill.
If the cache line where the refill data must be written is already valid, the targeted cache line
must be invalidated first. This is true whatever the direct map or n-way set associative cache
mode.
7.4.9 Dual-master cache
The ICACHE implements a dual-port AHB master on the main AHB bus matrix: master1 and
master2 ports. This is used to split the traffic going to different destination memories.
The nonremapped traffic goes systematically to master1 port. The remapped traffic can be
routed on the master2 port by programming MSTSEL in ICACHE_CRRx (on a region basis).
The code can typically be fetched as follows:
• internal flash memory and internal SRAM on master1 port (Fast bus)
• external flash memory/RAM on master2 port (Slow bus)
For systems not implementing external memories, the traffic to the internal flash memory
can be decoupled from the traffic to the internal SRAM (when remapped by the ICACHE).
This feature is used to prevent further processor stalls on misses.
Alongside with hit-under-miss, this dual-master feature allows the processor to have an
alternative path in case of fetching from different memories.
7.4.10 ICACHE security
The ICACHE implements an Armv8-M TrustZone.
ICACHE configuration registers are protected at system level.
7.4.11 ICACHE maintenance
The software can invalidate the whole content of the ICACHE by programming CACHEINV
in the ICACHE_CR register.
When CACHEINV = 1, the ICACHE control logic sets the BUSYF flag in ICACHE_SR and
launches the invalidate cache operation, resetting each TAG valid bit to 0 (one valid bit per
cache line). CACHEINV is automatically cleared.
Once the invalidate operation is finished (all valid bits reset to 0), the ICACHE automatically
clears BUSYF, and sets BSYENDF in the ICACHE_SR register.

Instruction cache (ICACHE) RM0438
252/2187 RM0438 Rev 8
If enabled on this flag condition (BSYENDIE = 1 in ICACHE_IER), the ICACHE interrupt
is raised. Then, the (empty) cache is available again.
7.4.12 ICACHE performance monitoring
The ICACHE provides the following monitors for performance analysis:
• The 32-bit hit monitor counts the cacheable AHB-transactions on the slave cache port
that hits the ICACHE content.
It also takes into account all accesses whose address is present in the TAG memory or
in the refill buffer (due to a previous miss, and whose data is coming, or is soon to
come, from the cache master port) (see Section 7.4.8).
• The 16-bit miss monitor counts the cacheable AHB-transactions on the slave cache
port that misses the ICACHE content.
It also takes into account all accesses whose address is not present neither in
the TAG memory nor in the refill buffer.
Upon reaching their maximum values, these monitors do not wrap over.
Hit and miss monitors can be enabled and reset by software allowing the analysis of specific
pieces of code.
The software can perform the following tasks:
• Enable/stop the hit monitor through HITMEN in ICACHE_CR.
• Reset the hit monitor by setting HITMRST in ICACHE_CR.
• Enable/stop the miss monitor through MISSMEN in ICACHE_CR.
• Reset the miss monitor by setting MISSMRST in ICACHE_CR.
To reduce power consumption, these monitors are disabled (stopped) by default.
7.4.13 ICACHE boot
The ICACHE is disabled (EN = 0 in ICACHE_CR) at boot.
The code remapping at boot is not needed for a Cortex®-M33 as it implements the VTOR
(vector tables) that allows a boot start address definition different than 0x0.
Once the boot is finished, the ICACHE can be enabled (software setting EN = 1
in CACHE_CR).
7.5 ICACHE low-power modes
At device level, using the ICACHE reduces the power consumption by fetching instructions
from the internal ICACHE most of the time, rather than from the bigger and then more power
consuming main memories. This reduction is even higher if the cached main memories are
external.
Applications with lower performance profile (in terms of hit ratio) and stringent power
consumption constraints may benefit from the lower power consumption of an ICACHE
configured as direct mapped. This single-way cache configuration is obtained by
programming WAYSEL = 0 in ICACHE_CR (see [Figure 19](../figures/figure_19.md)). The power consumption is
reduced by accessing, for each request, only the necessary cut of TAG and data memories.
The cache effect still improves fetch performance, even if for most code execution, it is less
efficient than with an n-way set associative cache mode.

RM0438 Rev 8 253/2187
RM0438 Instruction cache (ICACHE)
258
7.6 ICACHE error management and interrupts
If an unsupported cacheable write request is detected (functional error), the ICACHE
generates an error by setting the ERRF flag in ICACHE_SR. An interrupt is generated if the
corresponding interrupt enable bit is set (ERRIE = 1 in ICACHE_IER).
The other possible interrupt generation is at the end of a cache invalidation operation.
When the cache-busy state is finished, the ICACHE sets the BSYENDF flag in
ICACHE_SR. An interrupt is generated if the corresponding interrupt enable bit is set
(BSYENDIE = 1 in ICACHE_IER).
All ICACHE interrupt sources raise the same and unique interrupt signal, icache_it, and then
use the same interrupt vector.
The ICACHE also propagates all AHB bus errors (such as security issues, address
decoding issues) from the master1 or master2 port back to the execution port.
7.7 ICACHE registers
7.7.1 ICACHE control register (ICACHE_CR)
Address offset: 0x000
Reset value: 0x0000 0004
[Table 60](../tables/table_60.md). ICACHE interrupts
Interrupt vector Interrupt event Event flag En able control bit Interrupt clear method
ICACHE
Functional error ERRF
in ICACHE_SR
ERRIE
in ICACHE_IER
Set CERRF to 1
in ICACHE_FCR
End of busy state
(invalidate finished)
BSYENDF
in ICACHE_SR
BSYENDIE
in ICACHE_IER
Set CBSYENDF to 1
in ICACHE_FCR
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. MISS
MRST
HITM
RST
MISS
MEN
HITM
EN
rw rw rw rw
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. WAY
SEL
CACHE
INV EN
r wwr w
Bits 31:20 Reserved, must  be kept at reset value.
Bit 19 MISSMRST: miss monitor reset
0: release the cache miss monitor reset (needed to enable the counting)
1: reset cache miss monitor
Bit 18 HITMRST: hit monitor reset
0: release the cache miss monitor reset (needed to enable the counting)
1: reset cache hit monitor

Instruction cache (ICACHE) RM0438
254/2187 RM0438 Rev 8
7.7.2 ICACHE status register (ICACHE_SR)
Address offset: 0x004
Reset value: 0x0000 0001
Bit 17 MISSMEN: miss monitor enable
0: cache miss monitor switched off. Stopping the monitor does not reset it.
1: cache miss monitor enabled
Bit 16 HITMEN: hit monitor enable
0: cache hit monitor switched off. Stopping the monitor does not reset it.
1: cache hit monitor enabled
Bits 15:3 Reserved, must be kept at reset value.
Bit 2 WAYSEL: cache associativity mode selection
This bit allows user to choose ICACHE set-associativity. It can be written by software only
when cache is disabled (EN = 0).
0: direct mapped cache (1-way cache)
1: n-way set associative cache (reset value)
Bit 1 CACHEINV: cache invalidation
Set by software and cleared by hardware when the BUSYF flag is set (during cache
maintenance operation). Writing 0 has no effect.
0: no effect
1: invalidate entire cache (all cache lines valid bit = 0)
Bit 0 EN: enable
0: cache disabled
1: cache enabled
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. ERRF BSYEN
DF BUSYF
rrr
Bits 31:3 Reserved, must be kept at reset value.
Bit 2 ERRF: cache error flag
0: no error
1: an error occurred during the operation (cacheable write)
Bit 1 BSYENDF: busy end flag
0: cache busy
1: full invalidate CACHEINV operation finished
Bit 0 BUSYF: busy flag
0: cache not busy on a CACHEINV operation
1: cache executing a full invalidate CACHEINV operation

RM0438 Rev 8 255/2187
RM0438 Instruction cache (ICACHE)
258
7.7.3 ICACHE interrupt enab le register (ICACHE_IER)
Address offset: 0x008
Reset value: 0x0000 0000
7.7.4 ICACHE flag clea r register (ICACHE_FCR)
Address offset: 0x00C
Reset value: 0x0000 0000
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. ERRIE BSYEN
DIE Res.
rw rw
Bits 31:3 Reserved, must be kept at reset value.
Bit 2 ERRIE: interrupt enable on cache error
Set by software to enable an interrupt generation in case of cache functional error (cacheable
write access)
0: interrupt disabled on error
1: interrupt enabled on error
Bit 1 BSYENDIE: interrupt enable on busy end
Set by software to enable an interrupt generation at the end of a cache invalidate operation.
0: interrupt disabled on busy end
1: interrupt enabled on busy end
Bit 0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
Res. Res. Res. Res. Res. Res. Re s. Res. Res. Res. Res. Res. Res. CERRF CBSY
ENDF Res.
ww
Bits 31:3 Reserved, must be kept at reset value.
Bit 2 CERRF: clear cache error flag
Set by software.
0: no effect
1: clears ERRF flag in ICACHE_SR
Bit 1 CBSYENDF: clear busy end flag
Set by software.
0: no effect
1: clears BSYENDF flag in ICACHE_SR.

Instruction cache (ICACHE) RM0438
256/2187 RM0438 Rev 8
7.7.5 ICACHE hit monitor register (ICACHE_HMONR)
Address offset: 0x010
Reset value: 0x0000 0000
7.7.6 ICACHE miss monitor register (ICACHE_MMONR)
Address offset: 0x014
Reset value: 0x0000 0000
7.7.7 ICACHE region x configurat ion register (ICACHE_CRRx)
Address offset: 0x020 + 0x4 * x, (x = 0 to 3)
Reset value: 0x0000 0200
Define an alias address in the code region for other regions, making them cacheable.
BASEDADDR and REMAPADDR fields are write locked (read only) when EN = 1 in
ICACHE_CR.
Bit 0 Reserved, must be kept at reset value.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
HITMON[31:16]
rrrrrrrrrrrrrrrr
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
HITMON[15:0]
rrrrrrrrrrrrrrrr
Bits 31:0 HITMON[31:0]: cache hit monitor counter
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res. Res.
1 5 1 4 1 3 1 2 1 1 1 0 9876543210
MISSMON[15:0]
rrrrrrrrrrrrrrrr
Bits 31:16 Reserved, must  be kept at reset value.
Bits 15:0 MISSMON[15:0]: cache miss monitor counter
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
HBURST Res. Res. MSTSEL Res. REMAPADDR[31:21]
rw rw rw rw rw rw rw rw rw rw rw rw rw
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
REN Res. Res. Res. RSIZE[2:0] Res. BASEADDR[28:21]
rw rw rw rw rw rw rw rw rw rw rw rw

RM0438 Rev 8 257/2187
RM0438 Instruction cache (ICACHE)
258
Bit 31 HBURST: output burst type for region x
0: WRAP
1: INCR
Bits 30:29 Reserved, must  be kept at reset value.
Bit 28 MSTSEL: AHB cache master selection for region x
0: no action (master1 selected by default)
1: master2 selected
Bit 27 Reserved, must be kept at reset value.
Bits 26:16 REMAPADDR[31:21]: remapped address for region x
This field replaces the alias address defined by BASEADDR field.
The only useful bits are [31:RI], where 21 ≤ RI ≤ 27 is the number of bits of RSIZE
(see Section 7.4.7). If the programmed value has more LSBs, the useless bits are ignored.
Bit 15 REN: enable for region x
0: disabled
1: enabled
Bits 14:12 Reserved, must  be kept at reset value.
Bits 11:9 RSIZE[2:0]: size for region x
000: reserved
001: 2 Mbytes
010: 4 Mbytes
011: 8 Mbytes
100: 16 Mbytes
101: 32 Mbytes
110: 64 Mbytes
111: 128 Mbytes
Bit 8 Reserved, must be kept at reset value.
Bits 7:0 BASEADDR[28:21]: base address for region x
This alias address is replaced by REMAPADDR field.
The only useful bits are [28:RI], where 21 ≤ RI ≤ 27 is the number of bits of RSIZE
(see Section 7.4.7). If the programmed value has more LSBs, the useless bits are ignored.

Instruction cache (ICACHE) RM0438
258/2187 RM0438 Rev 8
7.7.8 ICACHE register map
Refer to Section 2.3: Memory organization for the register boundary addresses.
[Table 61](../tables/table_61.md). ICACHE register map and reset values
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
0x000 ICACHE_CR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
MISSMRST
HITMRST
MISSMEN
HITMEN
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
WAYSEL
CACHEINV
EN
R e s e t  v a l u e 0000 100
0x004 ICACHE_SR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ERRF
BSYENDF
BUSYF
Reset value 001
0x008 ICACHE_IER
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
ERRIE
BSYENDIE
Res.
Reset value 00
0x00C ICACHE_FCR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
CERRF
CBSYENDF
Res.
Reset value 00
0x010 ICACHE_HMONR HITMON[31:0]
R e s e t  v a l u e 00000000000000000000000000000000
0x014 ICACHE_MMONR
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res.
Res. MISSMON[15:0]
R e s e t  v a l u e 0000000000000000
0x018-
0x01C Reserved Reserved
0x020 ICACHE_CRR0
HBURST
Res.
Res.
MSTSEL
Res.
Res. REMAPADDR[31:21]
REN
Res.
Res.
Res.
RSIZE
[2:0]
Res.
Res.BASEADDR[28:21]
R e s e t  v a l u e 0 0 00000000000 001 0000000
0x024 ICACHE_CRR1
HBURST
Res.
Res.
MSTSEL
Res.
Res. REMAPADDR[31:21]
REN
Res.
Res.
Res.
RSIZE
[2:0]
Res.
Res.BASEADDR[28:21]
R e s e t  v a l u e 0 0 00000000000 001 0000000
0x028 ICACHE_CRR2
HBURST
Res.
Res.
MSTSEL
Res.
Res. REMAPADDR[31:21]
REN
Res.
Res.
Res.
RSIZE
[2:0]
Res.
Res.BASEADDR[28:21]
R e s e t  v a l u e 0 0 00000000000 001 0000000
0x02C ICACHE_CRR3
HBURST
Res.
Res.
MSTSEL
Res.
Res. REMAPADDR[31:21]
REN
Res.
Res.
Res.
RSIZE
[2:0]
Res.
Res.BASEADDR[28:21]
R e s e t  v a l u e 0 0 00000000000 001 0000000
```

## 3. Referenced Figures & Diagrams in this Chapter
* [Figure 18: Architectural Diagram](../figures/figure_18.md)
* [Figure 19: Architectural Diagram](../figures/figure_19.md)
* [Figure 20: Architectural Diagram](../figures/figure_20.md)

## 4. Referenced Configuration Tables in this Chapter
* [Table 54: Configuration Matrix](../tables/table_54.md)
* [Table 55: Configuration Matrix](../tables/table_55.md)
* [Table 56: Configuration Matrix](../tables/table_56.md)
* [Table 57: Configuration Matrix](../tables/table_57.md)
* [Table 58: Configuration Matrix](../tables/table_58.md)
* [Table 59: Configuration Matrix](../tables/table_59.md)
* [Table 60: Configuration Matrix](../tables/table_60.md)
* [Table 61: Configuration Matrix](../tables/table_61.md)

## 5. Master Index & System Links
* **Master System Memory Map**: [Master System Memory Map](../memory/memory_map.md)
* **Master Map of Content**: [Wiki Root Index](../index.md)