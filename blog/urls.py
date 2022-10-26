from multiprocessing import context
from re import template
from django.urls import path
from blog.views import inicio, about, MyLogin, register, editar_perfil, agregar_avatar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="inicio"),
    path("inicio/", inicio, name="inicio"),
    path("about/", about, name="about"),
    path("login/", MyLogin.as_view(), name="Login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="logout.html"),
        name="Logout",
    ),
    path("register/", register, name="Register"),
    path("editar-perfil/", editar_perfil, name="EditarPerfil"),
    path("agregar-avatar/", agregar_avatar, name="AgregarAvatar")
]
