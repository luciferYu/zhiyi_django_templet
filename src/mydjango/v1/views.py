import urllib
import logging
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from utils.common import *

logger = logging.getLogger("django")

# Create your views here.

def status(request):
    return HttpResponse('ok')


def book(request):
    if request.method == 'GET':
        btitle = get(request,'btitle')
        btitle = urllib.parse.unquote(btitle)  # 将浏览器中的中文 转换为 string
        book = BookInfo.objects.get(btitle=btitle)
        serializer = BookInfoSerializer(book)
        return JsonResponse(serializer.data)

def blog(request,bid):
    if request.method == 'GET':
        try:
            blog = Blog.objects.using('read').get(pk=bid)  # 使用只读库读取数据
            blogserializer = BlogSerializer(blog)
        except:
            logger.error('访问blog参数错误')
            return HttpResponse('404 没有找到')
        else:
            return JsonResponse(blogserializer.data)
            #return render(request,'web/blog.html',locals())

class TestChildViewSet(ModelViewSet):
    queryset = TestChild.objects.all().order_by('child_name')
    serializer_class = TestChildSerializer

class TestParentViewSet(ModelViewSet):
    queryset = TestParent.objects.all()
    serializer_class = TestParentSerializer



