#!/bin/bash
#launched through crontab every 10 mins

cd /home/mc/tekxit3


if pgrep -x "java" > /dev/null
then
    mcwrapper cmd say "§l Please remember to run /stop before leaving the server"
else
    shutdown now
fi
