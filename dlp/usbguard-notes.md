# USBGuard

Client VM: USBGuard installed, `systemctl is-active usbguard` returned `active`; `usbguard get-parameter ImplicitPolicyTarget` returned `block`. Existing virtual USB devices were allowed under policy generated using `usbguard generate-policy`.

This demonstrates an enforcement policy for **unapproved USB devices**, not file-content-based DLP for a previously authorized USB device. Actual USB transfer blocking and alert forwarding were NOT verified.
