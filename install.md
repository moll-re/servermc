# How-to:

## RPI:
Add crontab:
````@reboot sudo python3 servermc/website/index.py````

## Server (manjaro):
Run copy_config.sh with sudo


## Do once:
* disable discrete GPU on server:
Add `install nouveau /bin/true` to `/etc/modprobe.d/blacklist.conf`. To reuse: remove line and reboot.

