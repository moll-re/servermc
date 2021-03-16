#!/bin/bash

# launch as crontab:
# @reboot sh ~/servermc/website/launch.sh
# 0,30 * * * * sh ~/servermc/website/launch.sh

cd ~/servermc/website

if pgrep -x "python" > /dev/null
then
    echo "Already running"
else
    sudo python3 index.py
fi