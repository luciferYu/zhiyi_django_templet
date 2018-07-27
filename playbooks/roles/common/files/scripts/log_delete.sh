#!/bin/bash

days=`date -d "-93 day" +%Y-%m-%d`

[ -d "/data/log/nginx/" ] && rm -rf /data/log/nginx/$days
