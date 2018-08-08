import urllib
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from utils.common import *



# Create your views here.

def status(request):
    return HttpResponse('ok')


def book(request):
    if request.method == 'GET':
        btitle = get(request,'btitle')
        btitle = urllib.parse.unquote(btitle)
        book = BookInfo.objects.get(btitle=btitle)
        serializer = BookInfoSerializer(book)
        return JsonResponse(serializer.data)



class TestChildViewSet(ModelViewSet):
    queryset = TestChild.objects.all().order_by('child_name')
    serializer_class = TestChildSerializer

class TestParentViewSet(ModelViewSet):
    queryset = TestParent.objects.all()
    serializer_class = TestParentSerializer

