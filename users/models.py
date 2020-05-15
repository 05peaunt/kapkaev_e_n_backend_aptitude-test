# users/models.py
from __future__ import unicode_literals
from django.utils import timezone


from django.contrib.auth.models import (AbstractUser)
from django.db import models


class CustomUser(AbstractUser):
    pass
    def __str__(self):
        return self.username
