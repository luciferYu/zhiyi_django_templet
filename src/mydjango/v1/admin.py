from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TestChild)
admin.site.register(TestParent)
admin.site.register(BookInfo)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)