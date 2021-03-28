#!/bin/bash

# launch as crontab
# */5 * * * * sh ~/servermc/server/autoshutdown.sh
# run as user, NO SUDO

cd ~/servermc/server/ # important for imports
python3 shutdown_auto.py
