#!/data/exec/python/bin/python3
# -*- coding:utf-8 -*-
#auth Yuzhiyi
from .models import *
from rest_framework import serializers

class TestChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestChild
        fields = '__all__'


class TestParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestParent
        fields = '__all__'

class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)




if __name__ == '__main__':
    pass