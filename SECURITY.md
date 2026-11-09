# Public configuration and private identifiers

The public config intentionally has empty SystemSerialNumber and MLB, an all-zero SystemUUID, and a six-byte zero ROM. Generate your own identifiers before use. Keep populated configs private and out of Git history.

Host-specific Bluetooth NVRAM data, device serials, private partition identifiers, Wi-Fi profiles, certificates, diagnostic reports and biometric experiment data are not part of this distribution. Do not add those items to bug reports or pull requests.

Changing the SMBIOS model does not reproduce Apple's Secure Enclave or T2/Apple Silicon boot security. The included SecureBootModel setting is Disabled. FileVault has not been validated by this project. Installation does not require globally disabling Gatekeeper or SIP.

Third-party binary rights and notices remain separate from the documentation; see THIRD-PARTY-NOTICES.md. This project does not provide a blanket license or security guarantee for every included vendor payload.
