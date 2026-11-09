# Package validation

- All 59 EFI file contents, including the sanitized config, match the preceding public package byte-for-byte.
- The fallback path is normalized to `EFI/BOOT/BOOTx64.efi`; no boot code is changed.
- ocvalidate 1.0.8 returns exit code 0. See [the output](ocvalidate.txt).
- SMBIOS identifiers remain empty or zeroed; host-specific Bluetooth variables remain omitted.
- Documentation links, checksums and ZIP integrity are checked during packaging.
- No runtime boot, hardware regression test or live EFI rewrite is performed as part of documentation packaging.

Versions and enabled states are derived from the frozen config and Info.plist files. Previous successful hardware tests establish the documented baseline; checksums alone do not prove hardware compatibility. The public template must be populated with private identifiers before use.

Use `python3 scripts/verify.py` to verify unchanged distributed files. Intentional edits, including filling in identifiers, change the relevant checksum.
