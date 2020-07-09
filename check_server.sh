#!/bin/bash
# should run in a minutely cron

nc -zw10 192.168.2.182 22 > /dev/null

cd ~/servermc/

if [ $? -eq 0 ]
then
        echo "ACTIVE" > server_status.txt
else
        echo "INACTIVE" > server_status.txt
fi
