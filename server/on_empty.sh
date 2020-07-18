#!/bin/bash
#cron every five minutes

OUT=$(mark2 send list)
if [[ $OUT == "" ]]
then
  for i in {1..20}
  do
    OUT=$(mark2 send list)
    if [[ $OUT == "" ]]
    then
      sleep 30
    else
      exit 1
    fi
  done
fi
mark2 stop
