#!/bin/bash
# Backup OmniRoute data before updates
BACKUP_DIR="/mnt/tb/1Apps/omniroute/backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
cp /mnt/tb/1Apps/omniroute/data/server.env "$BACKUP_DIR/"
cp /mnt/tb/1Apps/omniroute/data/storage.sqlite "$BACKUP_DIR/"
echo "Backup saved to: $BACKUP_DIR"
