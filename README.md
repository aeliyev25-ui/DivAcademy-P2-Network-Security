# P2 — Network & Infrastructure Security Lab

**DivAcademy Final Project — P2 workstream**  
**Environment:** VMware Workstation, 6 Ubuntu Server VMs  
**Repo:** curated configuration examples, scripts, verified test summaries and evidence checklist. 

> **Important:** Files in this repository are sanitized, reconstructed from our executed lab steps, and should be compared with the final configurations on the VMs before deployment. Never blindly run the whole repository. The `planned/` directory contains not-yet-deployed integration examples. This repository does NOT claim full completion of every project requirement.

## Architecture

| VM | Network | IP | Function |
|---|---|---|---|
| Firewall | VMnet8 WAN + VMnet1–6 | WAN 192.168.232.18 (DHCP), LAN 192.168.10.1 | nftables, NAT, Suricata, dnsmasq |
| Client Test | VMnet1 | 192.168.10.10 | USBGuard, Python DLP, tests |
| DMZ | VMnet2 | 192.168.20.10 | Segmentation test |
| Database | VMnet3 | 192.168.30.10 | PostgreSQL, Restic, backup timer |
| Backup | VMnet4 | 192.168.40.10 | Encrypted backup copy, ext4 immutable-bit lab |
| Honeypot | VMnet6 | 192.168.60.10 | Docker Cowrie, canary file monitor |

Gateways: VMnet1 `.10.1`, VMnet2 `.20.1`, VMnet3 `.30.1`, VMnet4 `.40.1`, VMnet5 `.50.1`, VMnet6 `.60.1` (all `192.168.X.1`). Management VMnet5 is configured on Firewall without a dedicated test VM.

## Directory map

- `firewall/` — nftables rules and forwarded IPS *pending* snippet
- `suricata/` — IDS/IPS rule files and NFQUEUE service override
- `dns/` — DNS sinkhole configuration
- `network/` — subnet documentation
- `database/` — test data, Restic backup script and systemd timer
- `dlp/` — Python regex preflight checker; USBGuard note
- `honeypot/` — Cowrie startup command and Python canary monitor
- `planned/` — Wazuh agent integration examples not yet applied
- `docs/` — actual test evidence, outstanding work, report material

## Verified lab demonstrations

1. LAN ↔ DMZ isolation (nftables deny and DROP log counters).
2. Suricata IDS ICMP alert; inline NFQUEUE test: 4 ICMP requests from `192.168.10.10` to `1.1.1.1` were dropped with 4 `[Drop]` Suricata alerts.
3. DNS sinkhole: `blocked.example.test A` → `0.0.0.0`; normal `google.com` resolves.
4. `p2lab` PostgreSQL data classified PUBLIC / INTERNAL / CONFIDENTIAL.
5. Restic encrypted snapshot copied to separate Backup VM; `restic check --read-data` found no errors; PostgreSQL remote restore showed all three test rows.
6. `chattr +i` laboratory immutable attribute: test file creation returned `Operation not permitted`.
7. USBGuard is active with implicit policy `block`; Python DLP detected fake FIN/card and logged `HIGH` / `BLOCK` with a ticket UUID.
8. Cowrie Docker honeypot accepted a **decoy** SSH login on TCP 2222.
9. File canary monitor logged `CRITICAL` `canary_file_access` when a decoy file was opened.
10. Daily `p2-db-backup.timer` was seen `active (waiting)`.

These are observations, **not** claims of full real USB/email/cloud DLP enforcement, durable IPS for all flows, true WORM/offsite backup, or Wazuh delivery.

## Remaining integration / gaps

- Azure Wazuh SIEM integration via Tailscale/VPN (not yet done); automatic HIGH / CRITICAL alerts and ticketing need demonstration.
- Suricata NFQUEUE test rule persistence in `/etc/nftables.conf` and post-reboot verification; broader inline policy pending.
- DNS bypass / DoH / DoT, DNS tunnelling detection and CTI feed pending.
- True content-aware endpoint DLP blocking for USB/email/cloud pending.
- Actual 3-2-1 offsite, privileged-user-proof immutable backup, encrypted storage and remote backup automation pending.
- Honeypot/WAF automatic IP blocklist, AD/DNS honeytokens and multi-source correlation pending.
- Project-wide requirements (cloud infrastructure, 10+ servers, two SIEMs) are shared across the team and are not fulfilled by this VMware-only workstream by itself.

## Security and setup

Do not commit secrets, `.env`, Restic password file, SSH keys, real customer data, dumps, production IP/public tokens, credentials, Wazuh enrollment secrets, or VM disks. `.gitignore` excludes common sensitive artifacts. Check every file and screenshot before making the repo public. For a course submission, prefer **Private** visibility until reviewed.

## Evidence

Add **redacted** local screenshots to `evidence/` and update `docs/evidence-checklist.md` to point to each one. We don't manufacture or alter evidence.

## Team and next steps

P2 owns network, firewall, IDS/IPS, DNS, database, DLP/backup and honeypot. P4 owns SIEM; P1 contributes AD and identity; P3 contributes application/WAF. We will integrate using approved private VPN connectivity.
