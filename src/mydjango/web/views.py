from django.shortcuts import render
from django.http import HttpResponse
from utils.common import time_counter
from utils.pmk import LinuxShell


# Create your views here.

def status(request):
    return HttpResponse('ok')

@time_counter
def test_image(request):
    return render(request, 'web/test_image.html', locals())

def test_shell(request):
    kshell = LinuxShell('127.0.0.1')
    kshell.conn()
    result = kshell.run_cmd('df -h')
    return render(request, 'web/test_shell.html', locals())
