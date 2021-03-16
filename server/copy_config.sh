#!/bin/bash

cp -R ./plugins/. /srv/craftbukkit/plugins
chown -hR craftbukkit /srv/craftbukkit/

cp conf.d /etc/conf.d/spigot


