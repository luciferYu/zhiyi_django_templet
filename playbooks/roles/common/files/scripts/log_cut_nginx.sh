#!/bin/bash

ngx_log_dir="/data/log/nginx"

now_time=$(date +%m-%d-%H)
this_day=$(date +%F)

cd $ngx_log_dir
[ -d "$this_day" ] || mkdir $this_day

for logfile in `ls *.log`
do
	mv $logfile $logfile-$now_time
	tar zcvf $logfile-$now_time.tgz $logfile-$now_time
	mv $logfile-$now_time.tgz $this_day
	rm -f $logfile-$now_time
done

kill -USR1 `cat /data/exec/nginx/logs/nginx.pid`