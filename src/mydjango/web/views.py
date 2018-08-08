# import the logging library
import logging

from django.shortcuts import render
from django.http import HttpResponse
from utils.common import time_counter,get
from utils.pmk import LinuxShell



# Get an instance of a logger
logger = logging.getLogger(__name__)
access_logger = logging.getLogger('access_log')


# Create your views here.

def status(request):
    return HttpResponse('ok')

@time_counter
def test_image(request):
    return render(request, 'web/test_image.html', locals())

def test_shell(request):
    title = 'test_shell'
    access_logger.debug(request.path)
    command = get(request,'command')
    if command == '':
        command = 'date'
    kshell = LinuxShell('127.0.0.1')
    kshell.conn()
    result = kshell.run_cmd(command)
    return render(request, 'web/test_shell.html', locals())
