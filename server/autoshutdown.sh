#!/bin/bash

# launch as crontab:
# */5 * * * * ~/servermc/server/autoshutdown.sh

stat = $(spigot status)

if [$stat == "Not running"]
then
    sudo shutdown now
else
    echo "Still running"
fi