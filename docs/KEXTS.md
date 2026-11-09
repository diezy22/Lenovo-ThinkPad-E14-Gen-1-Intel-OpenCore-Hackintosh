# Kext inventory

Versions are read from the bundled Info.plist files. Enabled describes Kernel/Add in the public config, not a fresh runtime loading test. Nested VoodooPS2 plugins are listed separately.

| Component | Version | Enabled | Purpose / upstream |
|---|---|---|---|
| `AirportItlwm` | 2.4.0 | Yes | [Native Tahoe Wi-Fi, laobamac fork](https://github.com/laobamac/itlwm/tree/7204c69) |
| `AppleALC` | 1.9.8 | Yes | [AppleHDA codec patches](https://github.com/acidanthera/AppleALC) |
| `BlueToolFixup` | 2.7.2 | Yes | [BlueTool compatibility](https://github.com/acidanthera/BrcmPatchRAM) |
| `BrightnessKeys` | 1.0.3 | Yes | [Brightness key handling](https://github.com/acidanthera/BrightnessKeys) |
| `ECEnabler` | 1.0.6 | Yes | [Embedded Controller access compatibility](https://github.com/averycblack/ECEnabler) |
| `IntelBTPatcher` | 2.5.3 | Yes | [Intel Bluetooth compatibility](https://github.com/OpenIntelWireless/IntelBluetoothFirmware) |
| `IntelBluetoothFirmware` | 2.5.3 | Yes | [Intel Bluetooth firmware loader](https://github.com/OpenIntelWireless/IntelBluetoothFirmware) |
| `Lilu` | 1.7.2 | Yes | [Kernel patching framework](https://github.com/acidanthera/Lilu) |
| `NVMeFix` | 1.1.3 | Yes | [NVMe compatibility and power management](https://github.com/acidanthera/NVMeFix) |
| `RealtekRTL8111` | 2.5.0 | Yes | [Realtek Ethernet driver](https://github.com/Mieze/RTL8111_driver_for_OS_X) |
| `SMCBatteryManager` | 1.3.8 | Yes | [Battery reporting plugin](https://github.com/acidanthera/VirtualSMC) |
| `SMCProcessor` | 1.3.8 | Yes | [CPU sensor plugin](https://github.com/acidanthera/VirtualSMC) |
| `SimpleHDA` | 1.0.1 | Yes | [Tahoe AppleHDA stack support](https://github.com/laobamac/SimpleHDA) |
| `USBToolBox` | 1.2.0 | Yes | [USB mapping support](https://github.com/USBToolBox/kext) |
| `UTBMap` | 1.1 | Yes | [Hardware-specific USB port map](https://github.com/USBToolBox/tool) |
| `VirtualSMC` | 1.3.8 | Yes | [SMC emulation](https://github.com/acidanthera/VirtualSMC) |
| `VoodooPS2Controller` | 2.3.7 | Yes | [PS/2 input controller](https://github.com/acidanthera/VoodooPS2) |
| `VoodooInput` | 1.1.6 | Yes | [Multitouch input plugin](https://github.com/acidanthera/VoodooInput) |
| `VoodooPS2Keyboard` | 2.3.7 | Yes | [PS/2 keyboard plugin](https://github.com/acidanthera/VoodooPS2) |
| `VoodooPS2Mouse` | 2.3.7 | Yes | [PS/2 mouse plugin](https://github.com/acidanthera/VoodooPS2) |
| `VoodooPS2Trackpad` | 2.3.7 | Yes | [PS/2 trackpad plugin](https://github.com/acidanthera/VoodooPS2) |
| `WhateverGreen` | 1.7.1 | Yes | [Graphics and framebuffer patches](https://github.com/acidanthera/WhateverGreen) |
| `itlwm` | 2.3.0 | No | [Legacy Wi-Fi bundle, disabled](https://github.com/OpenIntelWireless/itlwm) |

The directory contains 19 top-level kext bundles and four nested plugins. AirportItlwm and SimpleHDA are restricted to Darwin 25.x. The disabled itlwm bundle is retained to preserve the frozen file set. No new binaries were downloaded or substituted during documentation cleanup.
