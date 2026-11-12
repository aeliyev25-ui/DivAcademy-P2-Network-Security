#!/bin/bash
# Tested locally; does not automatically mirror to remote backup VM.
set -Eeuo pipefail
umask 077
DUMP="/var/lib/postgresql/p2-staging/p2lab-auto.dump"
REPO="/var/backups/p2-restic"
PASS="/root/p2-restic-password" # FILE PATH ONLY; NOT A PASSWORD
cleanup() {
    code=$?
    rm -f "$DUMP"
    if [ "$code" -ne 0 ]; then
        logger -p user.err -t P2-BACKUP "HIGH: Database backup FAILED"
    fi
}
trap cleanup EXIT
sudo -u postgres pg_dump -Fc -f "$DUMP" p2lab
restic -r "$REPO" --password-file "$PASS" backup "$DUMP"
logger -p user.info -t P2-BACKUP "SUCCESS: Encrypted database backup completed"
