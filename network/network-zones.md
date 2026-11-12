# P2 network segmentation

| VMnet | Subnet | Gateway | Description |
|---|---|---|---|
| VMnet8 | 192.168.232.0/24 | DHCP gateway, e.g. .2 | WAN / VMware NAT |
| VMnet1 | 192.168.10.0/24 | 192.168.10.1 (ens34) | LAN Client |
| VMnet2 | 192.168.20.0/24 | 192.168.20.1 (ens38) | DMZ |
| VMnet3 | 192.168.30.0/24 | 192.168.30.1 (ens39) | Database / Server |
| VMnet4 | 192.168.40.0/24 | 192.168.40.1 (ens40) | Backup / Security |
| VMnet5 | 192.168.50.0/24 | 192.168.50.1 (ens41) | Management |
| VMnet6 | 192.168.60.0/24 | 192.168.60.1 (ens42) | Honeypot Quarantine |

`ens33` WAN; test client=192.168.10.10, DMZ=192.168.20.10, DB=192.168.30.10, backup=192.168.40.10, honeypot=192.168.60.10. Linux forwarding enabled on firewall. LAN↔DMZ denies tested; other zone-specific access follows explicit ports only. Firewall INPUT and IPv6 controls need separate hardening.
