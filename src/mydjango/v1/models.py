from django.db import models
from db.AbstractModel import *


# Create your models here.


class TestChild(AbstractModel):
    child_name = models.CharField(max_length=20, default="")
    child_counter = models.IntegerField(default=0)
    parent_childs = models.ForeignKey('TestParent', default="")

    def __str__(self):
        return self.child_name


class TestParent(AbstractModel):
    '''测试父类'''
    parent_name = models.CharField(max_length=20, default="")
    parent_sex = models.BooleanField(default=True)
    parent_desc = models.TextField()

    def __str__(self):
        return self.parent_name


class BookInfo(models.Model):
    '''定义一个图书类'''
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期', null=True)
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')

    def __str__(self):
        return self.btitle