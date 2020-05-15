
from django.contrib.postgres.fields import ArrayField
from time import gmtime, strftime

import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
#from django_currentuser.middleware import (get_current_authenticated_user)
from django.conf import settings

from rest_framework.fields import ListField
import uuid
#принтер
class Printer(models.Model):

    KITCHEN = 'kitchen'
    CLIENT = 'client'
    CHECK_TYPE = [
                        (KITCHEN, ('Кухня')),
                        (CLIENT, ('Клиент')),
    ]

    name = models.CharField("Название", max_length = 50, blank = True, null=True)
    api_key = models.CharField("API_KEY", primary_key=True, max_length=100, blank=True, unique=True, default=uuid.uuid4)
    check_type = models.CharField("Тип Чека", max_length = 50, choices = CHECK_TYPE, default=CLIENT)
    point_id = models.IntegerField("Точка привязки", blank = True, null = True)

    def __str__(self):
        return str(self.api_key)
