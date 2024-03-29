#!/data/exec/python/bin/python3
# -*- coding:utf-8 -*-
# auth Yuzhiyi
import datetime, time


def string_2_timestamp(time_string):
    '''
    字符串转时间戳
    :param time_string: 字符串  2018-08-08 09:53:53
    :return: int类型 1533693233.0
    '''
    time_stamp = time.mktime(time.strptime(time_string, '%Y-%m-%d %H:%M:%S'))
    return time_stamp

def timestamp_2_string(time_stamp):
    '''
    时间戳转字符串
    :param time_stamp: 时间戳  int类型 1533693233.0
    :return:  字符串  2018-08-08 09:53:53
    '''
    time_struct = time.localtime(time_stamp)
    time_string = time.strftime('%Y-%m-%d %H:%M:%S',time_struct)
    return time_string


if __name__ == '__main__':
    mytime = '2018-08-08 09:53:53'
    print(string_2_timestamp(mytime))

    my_timestamp = 1533693233.0
    print(timestamp_2_string(my_timestamp))

