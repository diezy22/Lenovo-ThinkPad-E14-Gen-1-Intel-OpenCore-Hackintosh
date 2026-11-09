# Lenovo ThinkPad E14 Gen 1 — Intel OpenCore

[![OpenCore](https://img.shields.io/badge/OpenCore-1.0.8-blue)](https://github.com/acidanthera/OpenCorePkg/releases/tag/1.0.8)
[![macOS](https://img.shields.io/badge/macOS-Tahoe%2026.7.2-lightgrey)](https://www.apple.com/macos/)
[![Platform](https://img.shields.io/badge/Platform-Intel%20Comet%20Lake-informational)](https://dortania.github.io/OpenCore-Install-Guide/config-laptop.plist/comet-lake.html)

## About

OpenCore EFI configuration for the **Lenovo ThinkPad E14 Gen 1 with an Intel Core i5-10210U**, tested with macOS Tahoe 26.7.2 (25G332).

This repository documents a frozen configuration with native Intel Wi-Fi, battery reporting, and HDMI output including sleep/wake recovery. It is intended as a hardware-specific reference, not a universal E14 installer.

> [!IMPORTANT]
> The public configuration has blank or zeroed SMBIOS identifiers. Generate your own identifiers before use. This EFI targets **Gen 1 Intel**, not Gen 5 AMD or other E14 generations.

## Hardware

| Component | Tested configuration |
|---|---|
| Model | Lenovo ThinkPad E14 Gen 1, type 20RA / variant 20RAS12700 |
| Processor | Intel Core i5-10210U, 4 cores / 8 threads, 1.6 GHz base / up to 4.2 GHz |
| Graphics | Integrated Intel UHD Graphics; Coffee Lake-compatible framebuffer, device ID 0x3E9B |
| Memory | 8 GB RAM |
| Internal display | 14-inch; exact panel model and resolution not independently documented |
| macOS storage | WD PC SN530 512 GB NVMe |
| Additional storage | KLEVV NEO N400 240 GB SATA; separate Windows installation |
| Wireless | Intel Wi-Fi 6 AX201 |
| Bluetooth | Intel Bluetooth, USB ID 8087:0026 |
| Audio | AppleALC + SimpleHDA, layout ID 21; physical codec not independently documented |
| Ethernet | RealtekRTL8111 driver included; exact controller revision not independently documented |
| Input | VoodooPS2 keyboard, mouse and trackpad stack |
| Fingerprint | Goodix 27C6:55A4; native Touch ID unavailable |
| SMBIOS | MacBookPro16,1 |

The [Lenovo platform specification](https://psrefstuff.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E14/ThinkPad_E14_Spec.pdf) covers multiple hardware options. Verify your particular unit before reusing this configuration.

## Working

- Internal OpenCore boot without a USB drive.
- Boot on AC power and battery power.
- Battery detection and charge reporting.
- Stable native Wi-Fi through AirportItlwm Tahoe, including the tested enterprise Wi-Fi profile.
- Internal speaker output.
- HDMI extended display, boot with HDMI attached, and HDMI recovery after sleep/wake.
- Keyboard input; the known LED timing limitation is listed below.

These are results from the tested configuration, not guarantees for every device with the same model name.

## Known limitations

| Area | Status |
|---|---|
| Bluetooth | Basic connectivity tested; historical bluetoothd crashes were observed. Long-duration stability is not established. |
| Caps Lock LED | Input changes immediately; the LED has shown a 3–5 second delay. |
| AirDrop / AWDL | Not supported by the included Wi-Fi fork. |
| WPA3-only / mandatory PMF / MLO | Not supported by the documented Wi-Fi build. |
| Wi-Fi 6 / HE | Disabled by default in the Wi-Fi fork; not enabled in this configuration. |
| Touch ID | Goodix is not integrated with native macOS Touch ID. |
| Hibernation | Not validated; OpenCore HibernateMode is None. Ordinary sleep is a separate feature. |
| Other hardware | Full microphone/jack, camera, Ethernet, USB-port and gesture coverage has not been documented. |
| FileVault and Apple ecosystem features | Not validated by this repository. |

See [Compatibility](docs/COMPATIBILITY.md) for the scope of these statements. No performance scores or percentage-based compatibility rating is claimed.

## Repository layout

```text
EFI/
├── BOOT/BOOTx64.efi
└── OC/
    ├── OpenCore.efi
    ├── config.plist
    ├── ACPI/
    ├── Drivers/
    ├── Kexts/
    └── Tools/
docs/
├── INSTALLATION.md
├── CONFIGURATION.md
├── KEXTS.md
├── DRIVERS-ACPI.md
├── COMPATIBILITY.md
└── VALIDATION.md
scripts/verify.py
SECURITY.md
THIRD-PARTY-NOTICES.md
SHA256SUMS.txt
```

## Getting started

1. Compare your hardware with the table above and back up your existing EFI.
2. Read [Installation](docs/INSTALLATION.md), including SMBIOS preparation and recovery requirements.
3. Review the [configuration notes](docs/CONFIGURATION.md), [kext inventory](docs/KEXTS.md), and [UEFI drivers / ACPI tables](docs/DRIVERS-ACPI.md).
4. Validate your edited config with **ocvalidate 1.0.8** before testing from recovery media.

This is an EFI-folder package, not a macOS installer, ISO, or full-disk image. Existing Windows boot files are not included or managed.

## Verify the downloaded files

Run from the repository root with Python 3:

```sh
python3 scripts/verify.py
```

The verifier only reads files and compares SHA-256 checksums. Editing `config.plist` intentionally changes its checksum. Validation details are in [docs/VALIDATION.md](docs/VALIDATION.md).

## References and credits

- [OpenCorePkg](https://github.com/acidanthera/OpenCorePkg) and [OpenCore 1.0.8 documentation](https://github.com/acidanthera/OpenCorePkg/blob/1.0.8/Docs/Configuration.tex).
- [Dortania Comet Lake laptop guide](https://dortania.github.io/OpenCore-Install-Guide/config-laptop.plist/comet-lake.html).
- [Dortania post-install guide](https://dortania.github.io/OpenCore-Post-Install/).
- [WhateverGreen Intel graphics documentation](https://github.com/acidanthera/WhateverGreen/blob/master/Manual/FAQ.IntelHD.en.md).
- [AirportItlwm Tahoe source, commit 7204c69](https://github.com/laobamac/itlwm/tree/7204c69).
- [SimpleHDA](https://github.com/laobamac/SimpleHDA).
- [USBToolBox](https://github.com/USBToolBox).
- [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS).

All component sources are linked in the inventory. See [third-party notices](THIRD-PARTY-NOTICES.md) for attribution and component licensing. Documentation organization was informed by [5T33Z0's E14 Gen 5 AMD repository](https://github.com/5T33Z0/Lenovo-ThinkPad-E14-Gen-5-AMD-OpenCore); its AMD configuration, patches, BIOS settings and benchmark results are not used here.
