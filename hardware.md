```
System:
  Host: ryan Kernel: 6.8.0 arch: x86_64 bits: 64 compiler: gcc v: 14.2.1 clocksource: tsc
    avail: hpet,acpi_pm
    parameters: initrd=\EFI\nixos\1acir5q09ndn9imay82sjfz05jlbns0a-initrd-linux-6.8-vcreflection-initrd.efi
    init=/nix/store/jncx9a6wzz5848x916r9pjgbj5k8i63k-nixos-system-ryan-25.05.20250722.2a10236/init
    amd_iommu=on console=ttyS0,115200 console=tty0 kvm_amd.sev=1 kvm_amd.sev_es=1
    kvm_amd.sev_snp=1 sp5100_tco.blacklist=yes hugepagesz=1GB hugepages=0 hugepagesz=2MB
    hugepages=1000 nohibernate loglevel=4 lsm=landlock,yama,bpf
  Console: pty pts/15 DM: LightDM v: 1.32.0 Distro: NixOS 25.05 (Warbler)
Machine:
  Type: Server System: Dell product: PowerEdge R7515 v: N/A serial: 9P0PSH3 Chassis: type: 23
    serial: 9P0PSH3
  Mobo: Dell model: 07PXPY v: A04 serial: .9P0PSH3.CNCMS0016O01PE.
    part-nu: SKU=08FD;ModelName=PowerEdge R7515 uuid: 4c4c4544-0050-3010-8050-b9c04f534833
    UEFI: Dell v: 2.9.3 date: 08/05/2022
Memory:
  System RAM: total: 1024 GiB available: 991.23 GiB used: 127.21 GiB (12.8%)
  Array-1: capacity: 2 TiB slots: 16 modules: 16 EC: Multi-bit ECC max-module-size: 128 GiB
    note: est.
  Device-1: A1 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD869D80AD part-no: HMAA8GR7AJR4N-XN serial: 24178C4F
  Device-2: A2 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD869D80AD part-no: HMAA8GR7AJR4N-XN serial: 241789BA
  Device-3: A3 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD869D80AD part-no: HMAA8GR7AJR4N-XN serial: 2414B4EC
  Device-4: A4 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD869D80AD part-no: HMAA8GR7AJR4N-XN serial: 2414B4D8
  Device-5: A5 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD869D80AD part-no: HMAA8GR7AJR4N-XN serial: 2414B4E0
  Device-6: A6 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD869D80AD part-no: HMAA8GR7AJR4N-XN serial: 2414B528
  Device-7: A7 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD869D80AD part-no: HMAA8GR7AJR4N-XN serial: 2414B4E6
  Device-8: A8 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD869D80AD part-no: HMAA8GR7AJR4N-XN serial: 2414B4EF
  Device-9: A9 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD863280AD part-no: HMAA8GR7CJR4N-XN serial: 87D2AA74
  Device-10: A10 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD863280AD part-no: HMAA8GR7CJR4N-XN serial: 87D2AA73
  Device-11: A11 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD863280AD part-no: HMAA8GR7CJR4N-XN serial: 87D2AA46
  Device-12: A12 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD863280AD part-no: HMAA8GR7CJR4N-XN serial: 87D2A9CC
  Device-13: A13 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD863280AD part-no: HMAA8GR7CJR4N-XN serial: 87D2AA91
  Device-14: A14 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD863280AD part-no: HMAA8GR7CJR4N-XN serial: 87D2AA8B
  Device-15: A15 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD863280AD part-no: HMAA8GR7CJR4N-XN serial: 87D2AA41
  Device-16: A16 type: DDR4 detail: synchronous registered (buffered) size: 64 GiB speed:
    spec: 3200 MT/s actual: 2933 MT/s volts: curr: 1.2 min: 1.2 max: 1.2 width (bits): data: 64
    total: 72 manufacturer: 80AD863280AD part-no: HMAA8GR7CJR4N-XN serial: 87D2AA8C
PCI Slots:
  Slot: 3 type: PCIe gen: 4 status: in use length: long volts: 3.3 bus-ID: c4:00.0
  Slot: 2 type: PCIe gen: 3 status: in use length: long volts: 3.3 bus-ID: 81:00.0
  Slot: 5 type: PCIe gen: 3 status: in use length: long volts: 3.3 bus-ID: 03:00.0
  Slot: 4 type: PCIe gen: 4 status: in use length: long volts: 3.3 bus-ID: 41:00.0
  Slot: 1 type: PCIe gen: 3 status: in use length: long volts: 3.3 bus-ID: 02:00.0
CPU:
  Info: model: AMD EPYC 7713P socket: SP3 bits: 64 type: MCP arch: Zen 3 gen: 3 level: v3
    note: check built: 2021-22 process: TSMC n7 (7nm) family: 0x19 (25) model-id: 1 stepping: 1
    microcode: 0xA001173
  Topology: cpus: 1x dies: 1 clusters: 1 cores: 64 smt: <unsupported> cache: L1: 4 MiB
    desc: d-64x32 KiB; i-64x32 KiB L2: 32 MiB desc: 64x512 KiB L3: 256 MiB desc: 8x32 MiB
  Speed (MHz): avg: 2000 min/max: 1500/3721 boost: disabled base/boost: 2000/3900 scaling:
    driver: acpi-cpufreq governor: schedutil volts: 1.8 V ext-clock: 2000 MHz cores: 1: 2000 2: 2000
    3: 2000 4: 2000 5: 2000 6: 2000 7: 2000 8: 2000 9: 2000 10: 2000 11: 2000 12: 2000 13: 2000
    14: 2000 15: 2000 16: 2000 17: 2000 18: 2000 19: 2000 20: 2000 21: 2000 22: 2000 23: 2000
    24: 2000 25: 2000 26: 2000 27: 2000 28: 2000 29: 2000 30: 2000 31: 2000 32: 2000 33: 2000
    34: 2000 35: 2000 36: 2000 37: 2000 38: 2000 39: 2000 40: 2000 41: 2000 42: 2000 43: 2000
    44: 2000 45: 2000 46: 2000 47: 2000 48: 2000 49: 2000 50: 2000 51: 2000 52: 2000 53: 2000
    54: 2000 55: 2000 56: 2000 57: 2000 58: 2000 59: 2000 60: 2000 61: 2000 62: 2000 63: 2000
    64: 2000 bogomips: 255536
  Flags: avx avx2 ht lm nx pae sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3 svm
  Vulnerabilities:
  Type: gather_data_sampling status: Not affected
  Type: itlb_multihit status: Not affected
  Type: l1tf status: Not affected
  Type: mds status: Not affected
  Type: meltdown status: Not affected
  Type: mmio_stale_data status: Not affected
  Type: retbleed status: Not affected
  Type: spec_rstack_overflow status: Vulnerable: Safe RET, no microcode
  Type: spec_store_bypass mitigation: Speculative Store Bypass disabled via prctl
  Type: spectre_v1 mitigation: usercopy/swapgs barriers and __user pointer sanitization
  Type: spectre_v2 mitigation: Retpolines, IBPB: conditional, IBRS_FW, STIBP: disabled, RSB
    filling, PBRSB-eIBRS: Not affected
  Type: srbds status: Not affected
  Type: tsx_async_abort status: Not affected
Graphics:
  Device-1: Matrox Systems Integrated G200eW3 Graphics driver: mgag200 v: kernel ports:
    active: VGA-1 empty: none bus-ID: c3:00.0 chip-ID: 102b:0536 class-ID: 0300
  Display: unspecified server: X.org v: 1.21.1.18 driver: gpu: mgag200 tty: 128x91
  Monitor-1: VGA-1 size-res: N/A in console modes: max: 1024x768 min: 640x480
  API: EGL v: 1.5 platforms: device: 0 drv: swrast surfaceless: drv: swrast
    inactive: gbm,wayland,x11
  API: OpenGL v: 4.5 vendor: mesa v: 25.0.7 note: console (EGL sourced) renderer: llvmpipe
    (LLVM 19.1.7 256 bits)
  Info: Tools: api: eglinfo,glxinfo de: xfce4-display-settings x11: xdpyinfo, xprop, xrandr
Audio:
  Message: No device data found.
  Server-1: PipeWire v: 1.4.5 status: off with: 1: pipewire-pulse status: off 2: wireplumber
    status: off 3: pipewire-alsa type: plugin tools: pw-cat,pw-cli,wpctl
Network:
  Device-1: Broadcom BCM57416 NetXtreme-E Dual-Media 10G RDMA Ethernet vendor: Dell
    driver: bnxt_en v: kernel pcie: gen: 3 speed: 8 GT/s lanes: 8 port: N/A bus-ID: 02:00.0
    chip-ID: 14e4:16d8 class-ID: 0200 temp: 51.0 C
  IF: ens1f0np0 state: up speed: 10000 Mbps duplex: full mac: 2c:ea:7f:af:56:78
  IP v4: 131.159.102.8/24 type: dynamic scope: global
  IP v6: 2a09:80c0:102::8/128 type: dynamic noprefixroute scope: global
  IP v6: fe80::2eea:7fff:feaf:5678/64 virtual: proto kernel_ll scope: link
  Device-2: Broadcom BCM57416 NetXtreme-E Dual-Media 10G RDMA Ethernet vendor: Dell
    driver: bnxt_en v: kernel pcie: gen: 3 speed: 8 GT/s lanes: 8 port: N/A bus-ID: 02:00.1
    chip-ID: 14e4:16d8 class-ID: 0200
  IF: ens1f1np1 state: down mac: 2c:ea:7f:af:56:79
  Device-3: Broadcom NetXtreme BCM5720 Gigabit Ethernet PCIe vendor: Dell PowerEdge R6515/R7515
    LOM driver: tg3 v: kernel pcie: gen: 2 speed: 5 GT/s lanes: 1 link-max: lanes: 2 port: N/A
    bus-ID: c1:00.0 chip-ID: 14e4:165f class-ID: 0200
  IF: eno8303 state: down mac: d0:8e:79:ba:1a:28
  Device-4: Broadcom NetXtreme BCM5720 Gigabit Ethernet PCIe vendor: Dell PowerEdge R6515/R7515
    LOM driver: tg3 v: kernel pcie: gen: 2 speed: 5 GT/s lanes: 1 link-max: lanes: 2 port: N/A
    bus-ID: c1:00.1 chip-ID: 14e4:165f class-ID: 0200
  IF: eno8403 state: down mac: d0:8e:79:ba:1a:29
  IF-ID-1: docker0 state: down mac: 02:42:4e:40:38:54
  IP v4: 172.17.0.1/16 scope: global broadcast: 172.17.255.255
  IP v6: fe80::42:4eff:fe40:3854/64 virtual: proto kernel_ll scope: link
  IF-ID-2: tap0_patrick state: up speed: 10000 Mbps duplex: full mac: 72:66:d4:ad:aa:55
  IP v4: 192.168.27.1/24 scope: global
  IP v6: fe80::7066:d4ff:fead:aa55/64 virtual: proto kernel_ll scope: link
  IF-ID-3: tinc.retiolum state: unknown speed: 10000 Mbps duplex: full mac: N/A
  IP v6: 42:0:3c46:53a7:e0e3:a2b6:471d:44a/16 scope: global
  Info: services: sshd, systemd-networkd, systemd-timesyncd
  WAN IP: 131.159.102.8
RAID:
  Hardware-1: Broadcom / LSI MegaRAID SAS-3 3008 [Fury] driver: megaraid_sas v: 07.727.03.00-rc1
    port: 1000 bus-ID: 01:00.0 chip-ID: 1000:005f rev: N/A class-ID: 0104
  Device-1: zroot type: zfs status: ONLINE level: linear raw: size: 1.45 TiB free: 259 GiB
    allocated: 1.2 TiB zfs-fs: size: 1.41 TiB free: 213.15 GiB
  Components: Online:
  1: nvme1n1p2 maj-min: 259:8 size: 1.45 TiB
Drives:
  Local Storage: total: raw: 5.3 TiB usable: 5.26 TiB used: 1.05 TiB (20.0%)
  ID-1: /dev/nvme0n1 maj-min: 259:5 vendor: Dell model: Ent NVMe AGN MU AIC 1.6TB size: 1.46 TiB
    block-size: physical: 512 B logical: 512 B tech: SSD serial: S61ANA0T700017 fw-rev: 2.0.2
    temp: 18 ° (291 K) C
  SMART: yes health: PASSED on: 1y 335d 4h cycles: 21 read-units: 24,190,396 [12.3 TB]
    written-units: 16,330,485 [8.36 TB]
  ID-2: /dev/nvme1n1 maj-min: 259:6 vendor: Dell model: Ent NVMe AGN MU AIC 1.6TB size: 1.46 TiB
    block-size: physical: 4096 B logical: 4096 B tech: SSD serial: S61ANA0T700063 fw-rev: 2.0.2
    temp: 18 ° (291 K) C scheme: GPT
  SMART: yes health: PASSED on: 1y 335d 4h cycles: 21 read-units: 32,709,087 [16.7 TB]
    written-units: 47,532,851 [24.3 TB]
  ID-3: /dev/nvme2n1 maj-min: 259:9 vendor: Samsung model: SSD 970 EVO Plus 1TB size: 931.51 GiB
    block-size: physical: 512 B logical: 512 B speed: 31.6 Gb/s lanes: 4 tech: SSD
    serial: S4EWNX0R513894H fw-rev: 2B2QEXM7 temp: 28.9 C
  SMART: yes health: PASSED on: 152d 2h cycles: 29 read-units: 144,370,200 [73.9 TB]
    written-units: 48,371,835 [24.7 TB]
  ID-4: /dev/nvme3n1 maj-min: 259:0 vendor: SK Hynix model: PC801 NVMe 1TB size: 953.87 GiB
    block-size: physical: 512 B logical: 512 B speed: 63.2 Gb/s lanes: 4 tech: SSD
    serial: SNB5N744011305V1P fw-rev: 51002141 temp: 32.9 C scheme: GPT
  SMART: yes health: PASSED on: 2y 41d 10h cycles: 133 read-units: 2,385,499 [1.22 TB]
    written-units: 5,705,019 [2.92 TB]
  ID-5: /dev/sda maj-min: 8:0 vendor: Ardor Gaming model: AL15SEB060NY size: 558.91 GiB
    block-size: physical: 512 B logical: 512 B speed: <unknown> tech: HDD rpm: 10000 serial: N/A
    fw-rev: EF06 temp: 21 C
  SMART: yes state: enabled
Partition:
  ID-1: / raw-size: N/A size: 1.26 TiB used: 1.05 TiB (83.5%) fs: zfs logical: zroot/root/nixos
  ID-2: /boot raw-size: 1024 MiB size: 1021.9 MiB (99.79%) used: 29.6 MiB (2.9%) fs: vfat
    block-size: 4096 B dev: /dev/nvme1n1p1 maj-min: 259:7
  ID-3: /home raw-size: N/A size: 3.4 TiB used: 1.24 TiB (36.3%) fs: nfs4
    remote: nfs:/export/home
  ID-4: /tmp raw-size: N/A size: 213.18 GiB used: 33.4 MiB (0.0%) fs: zfs
    logical: zroot/root/tmp
Swap:
  Alert: No swap data was found.
Sensors:
  Src: ipmi System Temperatures: cpu: N/A mobo: N/A
  Fan Speeds (rpm): cpu: 9840 mobo: 9960 fan-3: 9960 fan-4: 9960 fan-5: 10080 fan-6: 9840
  Power: 12v: N/A 5v: N/A 3.3v: N/A vbat: N/A dimm-p1: N/A dimm-p2: N/A
  Src: lm-sensors System Temperatures: cpu: 41.0 C mobo: N/A
  Fan Speeds (rpm): N/A
Info:
  Processes: 969 Power: uptime: 4d 8h 57m states: freeze,mem suspend: s2idle wakeups: 0
    hibernate: disabled image: 396.48 GiB Init: systemd v: 257 default: graphical tool: systemctl
  Packages: pm: nix-default pkgs: 0 pm: nix-sys pkgs: 987 libs: 234 pm: nix-usr pkgs: 0
    Compilers: gcc: 14.2.1 Shell: Sudo (sudo) v: 1.9.17p1 default: Bash v: 5.2.37
    running-in: pty pts/15 inxi: 3.3.38
```