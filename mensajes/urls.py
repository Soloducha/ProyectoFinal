from multiprocessing import context
from re import template
from django.urls import path

from mensajes.views import (
    mensajeria
)  

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", mensajeria, name="mensajes"),
]