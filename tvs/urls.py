from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:room_id>', serve_room, name="serve_room"),
]
