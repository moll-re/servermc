#!/bin/bash
#launched through crontab every 8 mins (*/8 * * * *)

cd /home/mc/servermc/server

if mcwrapper status
then
    mcwrapper cmd say "Please remember to run /stop before leaving the server"
else
    shutdown now
fi
