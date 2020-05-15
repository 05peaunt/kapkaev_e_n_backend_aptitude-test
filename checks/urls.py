from django.urls import path
from .views import *

from . import views

app_name = "checks"
urlpatterns = [

    path('create_checks/', CheckView.as_view()), #создать чек
    path('new_checks/', CheckView.as_view()),    #посмотреть новые чеки
    path(r'check/', SingleCheckView.as_view()),  #посмотреть конкретный чек


]
