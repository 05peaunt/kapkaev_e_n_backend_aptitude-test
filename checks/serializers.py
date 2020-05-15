from rest_framework import serializers
from .models import *

#чек
class CheckSerializer(serializers.ModelSerializer):
    pdf_file  = serializers.SerializerMethodField()
    class Meta:
        model = Check
        fields = ( 'id', 'printer_id', 'type', 'status', 'pdf_file', 'order')
    #абсолютный путь к pdf_file    
    def pdf_file(self, check):
        request = self.context.get('request')
        pdf_file_url = check.pdf_file.url
        return request.build_absolute_uri(ad_picture_1_url)
