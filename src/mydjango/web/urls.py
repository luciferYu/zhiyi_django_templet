#!/data/exec/python/bin/python3
# -*- coding:utf-8 -*-
#auth Yuzhiyi

from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^status$', status,name='status'),
    url(r'^test_image',test_image,name='test_image'),
    url(r'^test_shell',test_shell,name='test_shell'),
]


if __name__ == '__main__':
    pass