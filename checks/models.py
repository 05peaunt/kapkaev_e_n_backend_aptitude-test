

from django.contrib.postgres.fields import JSONField
from time import gmtime, strftime

import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
#from django_currentuser.middleware import (get_current_authenticated_user)
from django.conf import settings

from rest_framework.fields import ListField
import uuid
#чек
class Check(models.Model):

    KITCHEN = 'kitchen'
    CLIENT = 'client'
    CHECK_TYPE = [
                        (KITCHEN, ('Кухня')),
                        (CLIENT, ('Клиент')),
    ]

    NEW = 'new'
    RENDERED = 'rendered'
    PRINTED = 'printed'
    STATUS = [
                        (NEW, ('Новый')),
                        (RENDERED, ('Готов')),
                        (PRINTED, ('Распечатан')),
    ]
    printer_id = models.ForeignKey('printers.Printer', related_name='printer_r', on_delete=models.SET_NULL, null=True, blank = True)
    type = models.CharField("Тип Чека", max_length = 50, choices = CHECK_TYPE, default=CLIENT)
    status = models.CharField("Статус", max_length = 50, choices = STATUS, default=NEW)
    pdf_file = models.FileField(null=True, blank = True)
    order = JSONField()
    def __str__(self):
        return str(self.id)
