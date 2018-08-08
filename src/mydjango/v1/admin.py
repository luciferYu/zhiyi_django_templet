from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TestChild)
admin.site.register(TestParent)
admin.site.register(BookInfo)