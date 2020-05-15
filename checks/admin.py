from django.contrib import admin
from .models import *


class CheckAdmin(admin.ModelAdmin):



    model = Check
    list_filter = ('type','printer_id')
    list_display = ['id', 'printer_id', 'type', 'status', 'pdf_file', 'order']
admin.site.register(Check, CheckAdmin)
