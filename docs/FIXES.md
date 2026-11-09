# Fixes and provenance

This document explains the fixes shipped in the frozen E14 Gen 1 Intel EFI. It separates upstream software, hardware-specific settings, and changes outside the EFI. Successful results refer to tests on the documented machine; they are not a universal compatibility guarantee.

## What this repository changes

The functional work consists primarily of selecting compatible driver builds, enabling or disabling the correct components, and configuring OpenCore properties. It does not establish a newly authored custom kernel driver or a source-level modification to every included kext.

The Wi-Fi and Tahoe audio components come from separately maintained forks/projects. Version labels identify the supplied bundles; SHA-256 identifies their actual files. Apart from the recorded Wi-Fi commit, a complete source-commit and reproducible-build chain has not been established for every binary.

## Included fixes

| Area | Configuration or files | Validated outcome and limits | Primary references |
|---|---|---|---|
| Internal boot | `EFI/BOOT/BOOTx64.efi`, `EFI/OC/OpenCore.efi` | Internal boot without USB tested. Firmware boot entries themselves are not exported. | [OpenCore 1.0.8](https://github.com/acidanthera/OpenCorePkg/releases/tag/1.0.8) |
| Battery | `ECEnabler.kext` 1.0.6 and `SMCBatteryManager.kext` 1.3.8; RELEASE baseline, enabled in `Kernel/Add` | Battery reporting and battery-only boot tested. Runtime longevity and hibernation are separate. | [ECEnabler](https://github.com/averycblack/ECEnabler), [VirtualSMC](https://github.com/acidanthera/VirtualSMC) |
| Native Wi-Fi | `AirportItlwm.kext` 2.4.0 enabled for Darwin 25.x; `itlwm.kext` 2.3.0 disabled | Native Wi-Fi and the tested enterprise profile confirmed stable. Profiles and certificates are not distributed. | [laobamac source at 7204c69](https://github.com/laobamac/itlwm/tree/7204c69), [upstream FAQ](https://openintelwireless.github.io/itlwm/FAQ) |
| Audio | `AppleALC.kext` 1.9.8, `SimpleHDA.kext` 1.0.1; `alcid=21` | Speaker output tested. Complete microphone/jack and HDMI-audio coverage is not established. | [AppleALC](https://github.com/acidanthera/AppleALC), [SimpleHDA](https://github.com/laobamac/SimpleHDA) |
| Bluetooth | `IntelBluetoothFirmware.kext` 2.5.3, `IntelBTPatcher.kext` 2.5.3, `BlueToolFixup.kext` 2.7.2 | Basic activation/connectivity improved. Historical bluetoothd crashes prevent claiming full long-duration stability. | [IntelBluetoothFirmware](https://github.com/OpenIntelWireless/IntelBluetoothFirmware), [BrcmPatchRAM](https://github.com/acidanthera/BrcmPatchRAM) |
| HDMI detection | `DeviceProperties/Add/PciRoot(0x0)/Pci(0x2,0x0)` connector con2 enable/type/bus ID | Extended display and boot with HDMI attached tested. | [WhateverGreen Intel FAQ](https://github.com/acidanthera/WhateverGreen/blob/master/Manual/FAQ.IntelHD.en.md) |
| HDMI wake | Same device path; `force-online` and `force-online-framebuffers` | External display recovery after ordinary sleep/wake tested. Does not establish hibernation support. | [WhateverGreen](https://github.com/acidanthera/WhateverGreen) |

### HDMI values

Data values below are the exact stored bytes, not decimal integers. They are specific to the tested framebuffer topology.

| Property | Data hex |
|---|---|
| framebuffer-con2-enable | `01000000` |
| framebuffer-con2-type | `00080000` |
| framebuffer-con2-busid | `02000000` |
| force-online | `01000000` |
| force-online-framebuffers | `02ffffffffffffff` |

The framebuffer device and remaining properties are listed in [Configuration](CONFIGURATION.md).

## Existing patches and supporting components

The following are present in the baseline. Their presence does not mean a new fix was developed or every related function was retested during repository preparation.

- **Brightness ACPI:** DSDT-scoped `PNLF` to `XNLF` rename, paired with the included SSDT-PNLF; and the one-occurrence `NBCF` byte patch documented in [Drivers and ACPI](DRIVERS-ACPI.md).
- **USB:** USBToolBox 1.2.0 with hardware-specific UTBMap 1.1, 10 mapped XHC ports. XhciPortLimit is disabled.
- **CPU / SMC:** SSDT-PLUG, VirtualSMC and SMCProcessor remain in the supplied configuration.
- **Backlight / RTC:** SSDT-PNLF, BrightnessKeys and SSDT-RTCAWAC remain enabled.
- **Input / storage / Ethernet:** VoodooPS2Controller, NVMeFix and RealtekRTL8111 are included. Driver inclusion alone is not proof of exhaustive hardware testing.

## What is not included

An EFI folder does not preserve UEFI BootOrder/Boot#### entries, BIOS options, Windows Boot Manager, macOS power preferences, installed login items, Wi-Fi enterprise profiles, Keychain certificates or SSH keys. The package does not apply those changes automatically.

The earlier internal-disk boot repair also depended on the target disk's existing layout and firmware behavior. Copying these files is not equivalent to reproducing that disk repair, and no generic Windows bootloader deletion is instructed.

Goodix sensor experiments and fingerprint acquisition utilities are not shipped. No native Touch ID driver or Caps Lock LED fix is claimed. AirDrop/AWDL and hibernation limitations remain as documented in [Compatibility](COMPATIBILITY.md).

## Public template versus private boot backup

The public config intentionally omits unique SMBIOS identities and host-specific Bluetooth NVRAM values. That sanitization changes the public config compared with a private ready-to-boot backup; it does not remove the final HDMI, battery or Wi-Fi settings. Populate your own identifiers before testing.

This documentation update does not rewrite the active EFI, replace bundled drivers or apply new patches. Refer to [Validation](VALIDATION.md) and the checksum manifest for the packaged file set.
