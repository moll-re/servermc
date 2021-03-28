#!/bin/bash
# symlink to a desktop, so that POWEROFF only powers off when nothing else is running

# run as user, NO SUDO
cd ~/servermc/server/ # important for imports
python3 shutdown_manual.py