# P2 technical report (concise)

## 3 — Network architecture, firewall, IDS/IPS and DNS

Six Ubuntu Server virtual machines were configured on VMware Workstation. A Linux firewall routes six zones (LAN, DMZ, Server, Security, Management and Quarantine). nftables default-deny forward policy provides explicit interzone access and log prefixes for blocked traffic. Suricata 8.0.8 was deployed for IDS and tested in inline NFQUEUE IPS mode; four ICMP requests from 192.168.10.10 to 1.1.1.1 were dropped and observed in Suricata logs. DNS security was demonstrated through dnsmasq: a normal domain resolved while `blocked.example.test` returned the sinkhole address `0.0.0.0`.

## 13 — Data classification, DLP and backup

PostgreSQL `p2lab` stores synthetic PUBLIC, INTERNAL and CONFIDENTIAL records. A Python regex checker detected fake FIN and credit card patterns and generated HIGH/BLOCK audit events with unique ticket IDs; USBGuard is active with an implicit deny policy for unapproved devices. Restic encrypted a PostgreSQL backup which was copied over SSH to a separate backup VM; integrity checking and a full restore into `p2lab_remote_restore` succeeded. A test copy was protected with the Linux immutable attribute; a daily local backup timer was enabled. This is **not yet** complete DLP enforcement, 3-2-1 offsite backup or WORM storage.

## 14 — Honeypot and decoy files

Cowrie was deployed to a dedicated Quarantine-zone VM using Docker on TCP 2222; Client successfully reached its decoy SSH shell. A Python inotify monitor observed opening a synthetic `Customer_DB_Passwords.txt` and wrote a CRITICAL JSON alert. Actual integration with P4 Wazuh on Azure and SOC delivery timing are outstanding.

## Deployment and proof status

See `README.md` and `docs/evidence-checklist.md`. Do not claim screenshots or automatic SIEM events until they have been collected and verified. All data used is synthetic.
