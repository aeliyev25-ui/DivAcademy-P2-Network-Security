# P2 Evidence checklist

## Verified lab tests (screenshots must be captured or copied from OWN VM session, sanitized)

- [x] LAN↔DMZ ping denied / nftables logging
- [x] Suricata IDS lab ICMP alerts
- [x] Inline IPS ICMP test 4/4 dropped with nft counter and Suricata `[Drop]`
- [x] dnsmasq normal resolution + sinkhole 0.0.0.0
- [x] PostgreSQL 3 classified data rows
- [x] Restic encrypted snapshot + repository check success
- [x] Restore snapshot from Backup VM into separate PostgreSQL DB (3 rows)
- [x] `chattr +i` test: Operation not permitted
- [x] Daily backup timer active (waiting) + manual backup success log
- [x] USBGuard daemon active, implicit policy block
- [x] DLP regex preflight HIGH/BLOCK JSON, ticket UUID
- [x] Cowrie decoy SSH shell reached from Client
- [x] Canary file access CRITICAL JSON event

## Not yet verified / pending

- [ ] Inline IPS rule survives reboot and full traffic inspected
- [ ] DNS bypass, DoH/DoT and tunnel detection
- [ ] Real USB/email/cloud content DLP enforcement and ticket integration
- [ ] Wazuh agent alerts on Azure / SIEM dashboards
- [ ] Honeypot log into SIEM; WAF blocklist automatic update; AD and DNS traps
- [ ] Genuine WORM/remote 3-2-1 backup and automatic remote sync
- [ ] Two-SIEM / cloud-wide requirements confirmed by the entire team
- [ ] Redacted screenshots committed to repo
