
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login', do_login, name="do_login"),
    path('internet_nauta', get_internet_info, name="get_internet_info"),
    path('qr', get_qr_info, name="get_qr_info"),
    path('internet_nauta/connect', internet_nauta_connect, name="internet_nauta_connect"),
]
