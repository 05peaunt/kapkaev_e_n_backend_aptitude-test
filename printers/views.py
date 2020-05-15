from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import *
from users.models import CustomUser
from django.conf import settings
from django.contrib.auth.models import Group
from .serializers import *
from time import gmtime, strftime
from datetime import datetime
from rest_framework.response import Response
import json
from rest_framework.permissions import *
#посмотреть все возможные поездки
class PrinterView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PrinterSerializer
    queryset = Printer.objects.all()

class SinglePrinterView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = PrinterSerializer
    queryset = Printer.objects.all()
