#!/bin/bash

# launch as crontab
# */5 * * * * ~/servermc/server/autoshutdown.sh

cd ~/servermc/server/
sudo python3 shutdown.py
