#!/bin/bash
# Documentation ONLY. Do not execute a second time if p2-cowrie already exists.
# Image tag and storage path match the successful Docker lab invocation.
docker run -d \
  --name p2-cowrie \
  --restart unless-stopped \
  --memory 512m \
  --pids-limit 128 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  -p 192.168.60.10:2222:2222 \
  -v p2-cowrie-var:/cowrie/cowrie-git/var \
  cowrie/cowrie:latest
