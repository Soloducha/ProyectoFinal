from multiprocessing import context
from re import template
from django.urls import path

from blog.views import (
    inicio
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="inicio"),
]