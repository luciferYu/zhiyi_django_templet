#!/data/exec/python/bin/python3
# -*- coding:utf-8 -*-
#auth Yuzhiyi
from .models import *
from rest_framework import serializers

class TestChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestChild
        fields = '__all__'




if __name__ == '__main__':
    pass