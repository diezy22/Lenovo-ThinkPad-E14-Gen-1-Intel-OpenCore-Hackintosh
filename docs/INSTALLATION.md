# Installation

## Prerequisites

Use this configuration only as a reference for matching Gen 1 Intel hardware. Keep a working EFI backup and a bootable recovery USB available before changing a boot partition. Hardware variants may require a different USB map, ACPI tables, or framebuffer.

This repository does not establish a complete BIOS baseline. Do not copy AMD UMA settings, CPU core-count patches or NootedRed instructions from another E14 generation. No TPM reset, BIOS update, global Gatekeeper disable, or Reset NVRAM operation is part of these instructions.

## Prepare the configuration

1. Extract or clone the repository.
2. Generate identifiers for the selected SMBIOS with [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS). The tested model is MacBookPro16,1.
3. Fill `PlatformInfo/Generic/SystemSerialNumber`, `MLB`, `SystemUUID`, and `ROM` in a private copy of `EFI/OC/config.plist`. Use identifiers belonging to your installation, not another user's values.
4. Check your USB mapping and hardware-specific properties. The bundled UTBMap is not a universal port map.
5. Run `ocvalidate` from the [OpenCore 1.0.8 release](https://github.com/acidanthera/OpenCorePkg/releases/tag/1.0.8). Schema validation does not guarantee a successful boot.

Do not publish your populated config. Keep the sanitized template in public Git history. If you accidentally commit identifiers, deleting them in a later commit does not remove them from earlier history.

## Test before internal installation

Copy `EFI/` to the root of the correctly identified EFI partition on your recovery/test media. The expected paths are `EFI/BOOT/BOOTx64.efi` and `EFI/OC/config.plist`, not `EFI/EFI/...`.

For macOS installation media, follow [Dortania's installer guide](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/). This repository does not contain macOS installation files and should not be flashed as an ISO.

Verify boot, battery-only boot, Wi-Fi, sound, HDMI and sleep/wake before adopting the configuration. Do not replace a working internal EFI simply to match this repository. If adapting to an internal disk, identify it by device and partition identity and preserve separate Windows EFI files.

## Recovery

Use your previously working USB EFI if a new configuration fails. Restore your own private EFI backup to the same verified macOS EFI target. Do not overwrite the Windows disk, reset NVRAM, or remove Windows Boot Manager as a generic recovery step.

A sanitized public config is not a complete substitute for a private, ready-to-boot backup. The repository contains no automated partition mounting, formatting, NVRAM-writing, or installer scripts.
