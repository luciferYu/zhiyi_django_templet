#!/data/exec/python/bin/python3
# -*- coding:utf-8 -*-
#auth Yuzhiyi

from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^status$', status,name='status'),
]


if __name__ == '__main__':
    pass