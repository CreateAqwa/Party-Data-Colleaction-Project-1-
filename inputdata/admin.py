from django.contrib import admin
from inputdata.models import data

class Admininput(admin.ModelAdmin):
    list_display=("name","mobno","city")

admin.site.register(data,Admininput)
# Register your models here.


