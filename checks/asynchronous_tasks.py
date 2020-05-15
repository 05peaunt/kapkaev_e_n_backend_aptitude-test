# -*- coding: utf-8 -*-
from django_rq import job


import json
import requests
from django.template import Context, Template, RequestContext
from .models import *

from django.shortcuts import render,  redirect

from django.shortcuts import render
from django.template.loader import render_to_string

from django.conf import settings
import os

import base64
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''генерация html и pdf с информацией о заказе'''
@job
def make_html_and_pdf(request, current_order_id, address, client_name, phone, goods, total, printer_check_type, check_id):
    context = {"current_order_id" : current_order_id, "address" : address, "client_name" : client_name, "phone" : phone, "goods" : goods, "total" : total}
    data = render_to_string(str(printer_check_type) +'_check.html', context)
    if not os.path.exists(BASE_DIR + '/media/html/' + str(current_order_id) + '_' + str(printer_check_type) + '.html'):
        with open((BASE_DIR + '/media/html/' + str(current_order_id) + '_' + str(printer_check_type) + '.html'), 'w') as f:
            f.write(data)


    url = 'http://localhost:32769/'
    contents =  open((BASE_DIR + '/media/html/' + str(current_order_id) + '_' + str(printer_check_type) + '.html'), 'rt').read()
    data = {'contents': contents}
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, data=json.dumps(data).encode('ascii'), headers=headers)
    with open(BASE_DIR + '/media/pdf/' + str(current_order_id) + '_' + str(printer_check_type) + '.pdf', 'wb') as f:
        f.write(response.content)
        f.close()
    check = Check.objects.get(id = check_id)
    check.status = 'rendered'
    check.pdf_file.name = str(current_order_id) + '_' + str(printer_check_type) + '.pdf'
    check.save()
