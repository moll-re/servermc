#!/bin/bash
#launched through crontab every 10 mins

if pgrep -x "java" > /dev/null
then
    echo "Still running"
else
    shutdown now
fi
