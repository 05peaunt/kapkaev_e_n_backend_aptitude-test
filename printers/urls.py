from django.urls import path
from .views import *
app_name = "printers"
urlpatterns = [

    path('printers/', PrinterView.as_view()),
    path('printers/<int:pk>', SinglePrinterView.as_view()),
]
