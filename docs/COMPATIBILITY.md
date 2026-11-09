# Compatibility

## Scope

The supported reference hardware is the E14 Gen 1 Intel configuration listed in the README. No support claim is made for Gen 5 AMD, other processors, alternate wireless cards, or untested macOS releases. Component presence in a config is not proof that every related hardware feature has been tested.

## Wi-Fi

The [README at commit 7204c69](https://github.com/laobamac/itlwm/blob/7204c69/README.md) documents Tahoe support and these limitations: HE/802.11ax disabled by default, no WPA3-only, mandatory PMF, AWDL/AirDrop or MLO. The configuration does not opt in to HE with `itlwm_he=1`.

The tested native Wi-Fi connection and enterprise profile work reliably. This does not establish every enterprise authentication method, roaming scenario, Continuity feature, or Wi-Fi mode. See the [upstream FAQ](https://openintelwireless.github.io/itlwm/FAQ) for background; fork behavior must be evaluated separately.

## Bluetooth and input

Basic Bluetooth connectivity works, but historical bluetoothd crash reports exist. They do not establish a specific faulty kext or prove that a crash is currently recurring. Caps Lock input works immediately; its indicator LED has shown a short delay. No speculative keyboard patch is included.

## Apple-specific features

Goodix capture experiments are not native Touch ID integration and are not included. Apple Intelligence, Secure Enclave-backed features and Apple-silicon-only applications cannot be assumed available from SMBIOS spoofing. FileVault, DRM streaming, iServices and other Apple ecosystem features have not been validated as part of this distribution.

## Power and peripherals

HDMI sleep/wake has been tested. Hibernation, overnight battery drain, all microphone/jack combinations, every physical USB port, camera behavior and complete gesture coverage are not documented as passing. Avoid inferring these results from driver names or a device appearing in System Information.

## Maintenance

The configuration is frozen. New macOS, OpenCore or kext versions require their own validation and rollback plan; this repository makes no promise that the latest upstream version will retain compatibility. No scheduled updates or automatic fixes are provided.
