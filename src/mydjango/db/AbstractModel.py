#!/data/exec/python/bin/python3
# -*- coding:utf-8 -*-
# auth Yuzhiyi
from django.db import models


class AbstractModel(models.Model):
    # 数据创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 数据修改时间
    update_time = models.DateTimeField(auto_now=True)
    # 数据是否删除
    real_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True


if __name__ == '__main__':
    pass
