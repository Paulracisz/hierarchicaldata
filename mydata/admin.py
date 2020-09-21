from django.contrib import admin
from mydata.models import File
from mptt.admin import MPTTModelAdmin

# Register your models here.
admin.site.register(File, MPTTModelAdmin)