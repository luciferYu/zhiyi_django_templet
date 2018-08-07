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
