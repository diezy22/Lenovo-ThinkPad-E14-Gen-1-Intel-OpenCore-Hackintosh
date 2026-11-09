# Configuration notes

## Baseline

- OpenCore 1.0.8; tested OS: macOS Tahoe 26.7.2 (25G332).
- SMBIOS: MacBookPro16,1; unique identifiers are sanitized.
- Builtin picker, ShowPicker enabled, 10-second timeout.
- LauncherOption: Disabled. Firmware boot entries are not exported or created by this package.
- Boot arguments: `-v keepsyms=1 debug=0x100 agdpmod=vit9696 alcid=21`.
- SecureBootModel: Disabled; Vault: Optional; ScanPolicy: 0.
- csr-active-config: Data `00000000`; XhciPortLimit: false; DisableIoMapper: true.

These are the frozen configuration values, not a universal security or compatibility recommendation. SIP configuration is separate from OpenCore SecureBootModel and hardware-backed Apple Secure Boot.

## Battery

ECEnabler RELEASE 1.0.6 with VirtualSMC / SMCBatteryManager RELEASE 1.3.8 is the tested combination for battery reporting and battery-only boot. No new EC patch or firmware changes are introduced by this package.

## Graphics and HDMI

Properties are applied to `PciRoot(0x0)/Pci(0x2,0x0)`. Values below are the stored Data bytes in hexadecimal.

| Property | Data |
|---|---|
| AAPL,ig-platform-id | 00009b3e |
| device-id | 9b3e0000 |
| framebuffer-con2-enable | 01000000 |
| framebuffer-con2-type | 00080000 |
| framebuffer-con2-busid | 02000000 |
| force-online | 01000000 |
| force-online-framebuffers | 02ffffffffffffff |

Other existing framebuffer properties remain in config.plist. HDMI extended display, restart with HDMI attached, and sleep/wake recovery were tested on this hardware. These values are not portable to every Intel laptop. Reference: [WhateverGreen Intel FAQ](https://github.com/acidanthera/WhateverGreen/blob/master/Manual/FAQ.IntelHD.en.md).

## Wi-Fi and Bluetooth

AirportItlwm 2.4.0 is enabled for Darwin 25.0.0–25.99.99. Build provenance records the laobamac fork at [commit 7204c69](https://github.com/laobamac/itlwm/commit/7204c69). The legacy itlwm 2.3.0 bundle is retained but disabled. Do not enable both Wi-Fi drivers simultaneously.

IntelBluetoothFirmware 2.5.3, IntelBTPatcher 2.5.3 and BlueToolFixup 2.7.2 are enabled. Host-specific Bluetooth NVRAM values are omitted from the public template. Basic Bluetooth connectivity has been tested, but this repository does not claim crash-free long-duration operation.

## Audio

AppleALC 1.9.8, SimpleHDA 1.0.1 and `alcid=21` form the audio baseline. SimpleHDA is restricted to Darwin 25.x. [SimpleHDA's documentation](https://github.com/laobamac/SimpleHDA/blob/main/README.en.md) explains its use alongside AppleALC; the two are not treated as a duplicate-driver conflict.

## USB and ACPI

UTBMap defines 10 ports on XHC. HS05, HS06 and HS07 use connector type 255. Physical port behavior must be verified when adapting the EFI. Four SSDT tables and two ACPI patch entries are preserved. See [Drivers and ACPI](DRIVERS-ACPI.md).

## Sleep

Ordinary sleep/wake and hibernation are separate. OpenCore HibernateMode is None. OS-level power settings are not distributed by an EFI folder; this repository does not apply pmset settings or claim hibernation support.
