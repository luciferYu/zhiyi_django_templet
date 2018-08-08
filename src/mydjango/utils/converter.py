#!/data/exec/python/bin/python3
# -*- coding:utf-8 -*-
# auth Yuzhiyi
import datetime, time


def string_2_timestamp(time_string):
    time_stamp = time.mktime(time.strptime(time_string, '%Y-%m-%d %H:%M:%S'))
    return time_stamp

def timestamp_2_string(time_stamp):
    time_struct = time.localtime(time_stamp)
    time_string = time.strftime('%Y-%m-%d %H:%M:%S',time_struct)
    return time_string


if __name__ == '__main__':
    mytime = '2018-08-08 09:53:53'
    print(string_2_timestamp(mytime))

    my_timestamp = 1533693233.0
    print(timestamp_2_string(my_timestamp))

