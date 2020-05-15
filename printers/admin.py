from django.contrib import admin
from .models import *


class PrinterAdmin(admin.ModelAdmin):
    model = Printer
    list_display = ['name', 'api_key', 'check_type', 'point_id']
admin.site.register(Printer, PrinterAdmin)
