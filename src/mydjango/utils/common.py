#!/data/exec/python/bin/python3
# -*- coding:utf-8 -*-
# auth Yuzhiyi
import time

def post(request, key):
    return request.POST.get(key, '').strip()


def post_list(request, key):
    return request.POST.getlist(key)


# get方法去掉空格
def get(request, key):
    return request.GET.get(key, '').strip()


def set_cookie(response, key, value):
    '''
    设置cookie函数
    :param response:将要返回的响应
    :param key: cookie的键
    :param value: cookie的值
    :return:
    '''
    response.set_cookie(key, value, max_age=86400)


def get_cookie(request, key):
    '''
    获得cookie
    :param request:客户端请求
    :param key: 要获得的cookie的键
    :return: 查询的cookie的值
    '''
    return request.COOKIES.get(key, '')


def del_cookie(response, key):
    '''
    删除cookie
    :param response:将要返回的响应
    :param key: 要删除的cokkie值
    :return:
    '''
    response.delete_cookie(key)


def set_session(request, key, value):
    '''
    设置session
    :param request: 用户的请求
    :param key: 要设置session的键
    :param value: 要设置session的值
    :return:
    '''
    request.session[key] = value


def get_session(request, key):
    '''
    获取session
    :param request: 用户的请求
    :param key: 要获取session的键
    :return:
    '''
    return request.session.get(key, '')


def flush_session(request):
    '''
    设置session
    :param request: 用户的请求
    :return:
    '''
    request.session.flush()

def time_counter(func):
    def inner(*args,**kwargs):
        pc_start = time.perf_counter()
        ret = func(*args,**kwargs)
        pc_end = time.perf_counter()
        print('use time {:.16f}'.format(float(pc_end - pc_start)))
        return ret
    return inner




if __name__ == '__main__':
    pass
