#!/bin/bash
#cron every five minutes

OUT = $(mark2 send list)
if [[$OUT == ""]] then
  for i in {1..20}
  do
    OUT = $(mark2 send list)
    if [[$OUT != ""]] then
      exit 1
    else
      sleep 30
  done
fi
mark2 stop
