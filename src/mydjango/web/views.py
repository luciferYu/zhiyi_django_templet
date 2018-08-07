from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def status(request):
    return HttpResponse('ok')


def test_image(request):
    return render(request, 'web/test_image.html', locals())
