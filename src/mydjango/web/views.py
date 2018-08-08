from django.shortcuts import render
from django.http import HttpResponse
from utils.common import time_counter,get
from utils.pmk import LinuxShell


# Create your views here.

def status(request):
    return HttpResponse('ok')

@time_counter
def test_image(request):
    return render(request, 'web/test_image.html', locals())

def test_shell(request):
    command = get(request,'command')
    if command == '':
        command = 'date'
    kshell = LinuxShell('127.0.0.1')
    kshell.conn()
    result = kshell.run_cmd(command)
    return render(request, 'web/test_shell.html', locals())
