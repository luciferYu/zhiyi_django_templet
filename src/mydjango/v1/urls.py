#!/data/exec/python/bin/python3
# -*- coding:utf-8 -*-
#auth Yuzhiyi

from django.conf.urls import url
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    url(r'^status$', status,name='status'),
]

router = DefaultRouter()  # 可以处理视图的路由器
router.register(r'TestChild',TestChildViewSet) # 向路由器中注册视图集

urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中



if __name__ == '__main__':
    pass