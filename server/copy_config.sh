#!/bin/bash

cp -rf ./plugins/. /srv/craftbukkit/plugins
# every file in the local folder will overwrite the config in /srv/crafbukkit/plugins.
# Remember there might be more files already
chown -hR craftbukkit /srv/craftbukkit/


cp conf.d /etc/conf.d/spigot


