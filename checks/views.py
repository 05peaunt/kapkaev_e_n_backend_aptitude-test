from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import *
from django.conf import settings
from .serializers import *
from rest_framework.response import Response
import json
from printers.models import *
from .extract_json import extract_element_from_json
from rest_framework.permissions import *
from django.shortcuts import render,  redirect

from .asynchronous_tasks import *

from django.contrib import messages

class CheckView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CheckSerializer
    queryset = Check.objects.all()
    # Создаем чеки
    '''запрос на добавление чеков'''
    def post(self, request):
        '''точка с которой создают заказ'''
        point_id = extract_element_from_json(request.data, ["point_id"])[0]
        '''проверяем созданы ли уже чеки для этого заказа'''
        current_order_id = extract_element_from_json(request.data, ["id"])[0]#id создаваемого заказа
        existing_orders = Check.objects.all().values_list('order', flat=True)#существующие заказы
        for existing_order in existing_orders:
            existing_order_id = extract_element_from_json(existing_order, ["id"])[0]#id существующего заказа
            if current_order_id == existing_order_id:
                return Response({"message": "для этого заказа уже созданы чеки"}, status=400)
            else:
                pass
        '''принтеры, привязанные к нашей точке'''
        current_point_printers = Printer.objects.filter(point_id = point_id)
        if not current_point_printers:
            return Response({"message": "для этой точки не настроено ни одного принтера"}, status=400)
        else:
            pass
        '''получаем адрес из заказа'''
        address = extract_element_from_json(request.data, ["address"])[0]#адрес
        '''получаем имя клиента из заказа'''
        client_name = extract_element_from_json(request.data, ["client", "name"])[0]#имя
        '''получаем телефон клиента из заказа'''
        phone = extract_element_from_json(request.data, ["client", "phone"])[0]#телефон
        '''получаем список позиций в заказе'''
        goods = extract_element_from_json(request.data, ["items"])[0]#заказы
        '''получаем итоговую стоимость заказа'''
        total = 0
        for good in goods:
            dish_cost = good["quantity"] * good["unit_price"]
            total += dish_cost
        '''приступаем к созданию чеков'''
        for printer in current_point_printers:
            serializer = CheckSerializer(data={'printer_id': printer.api_key, 'type': printer.check_type, 'order': request.data, 'pdf_file': None, 'status': 'new'})
            if serializer.is_valid(raise_exception=True):
                saved_check = serializer.save()
                '''отправляем задание на генерацию pdf в очередь'''
                make_html_and_pdf(request, current_order_id, address, client_name, phone, goods, total, printer.check_type, saved_check.id)
                messages.info(self.request, 'Задача в очереди')
        return Response({"message": "чеки успешно созданы"}, status=200)
    '''запрос на получение чеков'''
    def get(self, request):
        api_key = self.request.query_params.get('api_key', None)
        try:
            printer = Printer.objects.get(api_key = api_key)
        except Printer.DoesNotExist:
            return Response({"message": "не существует принтера с таким api_key"}, status=401)
        printer_api_key = printer.api_key
        checks = Check.objects.filter(printer_id = printer_api_key, status = 'rendered')
        serializer = (self.serializer_class(checks, many=True, context={'request': request}))
        return Response(serializer.data)


class SingleCheckView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CheckSerializer
    queryset = Check.objects.all()
    '''запрос на получение конкретного чека'''
    def get(self, request):
        check_id = self.request.query_params.get('check_id', None)
        api_key = self.request.query_params.get('api_key', None)
        try:
            printer = Printer.objects.get(api_key = api_key)
        except Printer.DoesNotExist:
            return Response({"message": "не существует принтера с таким api_key"}, status=401)
        printer_api_key = printer.api_key
        try:
            check = Check.objects.get(id = check_id, printer_id = printer_api_key)
        except Check.DoesNotExist:
            return Response({"message": "Данного чека не существует"}, status=400)
        if check.status == 'new':
            return Response({"message": "Для данного чека не сгенерирован PDF-файл"}, status=400)
        serializer = (self.serializer_class(check, context={'request': request}))
        return Response(serializer.data)
