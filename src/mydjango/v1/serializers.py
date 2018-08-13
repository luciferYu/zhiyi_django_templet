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


# class BlogSerializer(serializers.Serializer):
#     name = serializers.CharField(label='名称')
#     tagline = serializers.CharField(label='标签')

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    #entry = EntrySerializer(many=True)
    class Meta:
        model = Blog
        fields = '__all__'


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(label='姓名', max_length=20)
    email = serializers.EmailField()





if __name__ == '__main__':
    pass