from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import TestChildSerializer
from .models import *



# Create your views here.

def status(request):
    return HttpResponse('ok')

class TestChildViewSet(ModelViewSet):
    queryset = TestChild.objects.all()
    serializer_class = TestChildSerializer