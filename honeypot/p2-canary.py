#!/usr/bin/env python3
"""Lab file-canary monitor for HOST OS path, not Cowrie's decoy filesystem."""
import os
import ctypes
import struct
import json
from datetime import datetime, timezone
DIRECTORY = "/srv/p2-canary"
FILENAME = "Customer_DB_Passwords.txt"
LOG = "/var/log/p2-canary/alerts.jsonl"
IN_OPEN = 0x20
os.makedirs(DIRECTORY, exist_ok=True)
os.makedirs("/var/log/p2-canary", exist_ok=True)
libc = ctypes.CDLL("libc.so.6", use_errno=True)
libc.inotify_init1.argtypes = [ctypes.c_int]
libc.inotify_init1.restype = ctypes.c_int
libc.inotify_add_watch.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_uint32]
libc.inotify_add_watch.restype = ctypes.c_int
fd = libc.inotify_init1(os.O_CLOEXEC)
if fd < 0:
    raise OSError(ctypes.get_errno(), "inotify init failed")
wd = libc.inotify_add_watch(fd, DIRECTORY.encode(), IN_OPEN)
if wd < 0:
    raise OSError(ctypes.get_errno(), "inotify watch failed")
print("P2 Canary monitoring started", flush=True)
while True:
    data = os.read(fd, 4096)
    offset = 0
    while offset + 16 <= len(data):
        watch, mask, cookie, length = struct.unpack_from("iIII", data, offset)
        name = data[offset + 16:offset + 16 + length]
        name = name.split(b"\x00", 1)[0].decode()
        offset += 16 + length
        if watch == wd and mask & IN_OPEN and name == FILENAME:
            event = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "severity": "CRITICAL",
                "event_type": "canary_file_access",
                "action": "ALERT",
                "resource": DIRECTORY + "/" + FILENAME,
            }
            with open(LOG, "a") as f:
                f.write(json.dumps(event) + "\n")
            print(json.dumps(event), flush=True)
