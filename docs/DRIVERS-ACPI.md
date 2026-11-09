# UEFI drivers, tools and ACPI

## Boot files and drivers

| File | Purpose | Upstream reference |
|---|---|---|
| BOOTx64.efi | UEFI fallback bootstrap | [OpenCorePkg 1.0.8](https://github.com/acidanthera/OpenCorePkg/releases/tag/1.0.8) |
| OpenCore.efi | OpenCore boot manager | [OpenCorePkg](https://github.com/acidanthera/OpenCorePkg) |
| OpenRuntime.efi | UEFI runtime support | [OpenCorePkg 1.0.8](https://github.com/acidanthera/OpenCorePkg/tree/1.0.8) |
| ResetNvramEntry.efi | Reset NVRAM tool entry | [OpenCorePkg](https://github.com/acidanthera/OpenCorePkg) |
| HfsPlus.efi | HFS+ filesystem support | [OcBinaryData](https://github.com/acidanthera/OcBinaryData) |
| OpenShell.efi | Diagnostic UEFI shell, not a runtime driver | [OpenCorePkg](https://github.com/acidanthera/OpenCorePkg) |

All three entries in UEFI/Drivers are enabled. Individual driver versions are not inferred from filenames; the manifest identifies the included binaries by SHA-256. ResetNvramEntry is part of the frozen configuration, not an instruction to reset NVRAM during installation.

## ACPI tables

| Table | Enabled | Intended role |
|---|---|---|
| SSDT-PLUG.aml | Yes | CPU plugin-type property |
| SSDT-USBX.aml | Yes | USB power properties |
| SSDT-PNLF.aml | Yes | Internal display backlight device |
| SSDT-RTCAWAC.aml | Yes | RTC/AWAC compatibility |

The supplied AML files are retained byte-for-byte. Their original DSL and compiler provenance have not been independently established; the role descriptions are not a fresh decompilation audit. The config also retains two ACPI patch entries. [Dortania's ACPI guide](https://dortania.github.io/Getting-Started-With-ACPI/) explains the concepts but is not asserted to be the source of these exact binaries.

UTBMap is a hardware-specific USB map, not a UEFI driver. It contains 10 mapped XHC ports; adapting to a different board requires checking the physical ports.
