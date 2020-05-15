from rest_framework import serializers
from .models import *

#принтер
class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = ( 'name', 'api_key', 'check_type', 'point_id')
