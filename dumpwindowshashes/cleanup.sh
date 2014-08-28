#!/bin/sh
wipe -f ~/bootkey
umount /dev/sda1
rm -rf /mnt/sda1 
wipe -f ~/samdump