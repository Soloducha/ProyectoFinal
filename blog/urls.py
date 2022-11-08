from multiprocessing import context
from re import template
from django.urls import path
from blog.views import (
    inicio,
    about,
    MyLogin,
    register,
    editar_perfil,
    agregar_avatar,
    procesar_autor,
   # procesar_pagina,
    buscar_pagina,
    buscar_autor,
    AutorList,
    AutorUpdateView,
   # AutorCreacion,
    AutorDelete,
    AutorDetalle,
    PaginasList,
    PaginaDetalle,
    PaginaDelete,
    PaginaCreacion,
    PaginaUpdateView,
    agregar_imagen
)
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
    path("agregar-avatar/", agregar_avatar, name="AgregarAvatar"),

    path("formulario-autor/", procesar_autor, name="AutorNew"),
    path("autor/list/", AutorList.as_view(), name="AutorList"),
    path("buscar-autor/", buscar_autor, name="AutorSearch"),
    path("autor/detalle/<pk>", AutorDetalle.as_view(), name="AutorDetail"),
    path("autor/borrar/<pk>", AutorDelete.as_view(), name="AutorDelete"),
    path("autor/editar/<pk>", AutorUpdateView.as_view(), name="AutorUpdate"),

    path("pagina-nuevo/", PaginaCreacion.as_view(), name="PaginaNew"),
    path("buscar-pagina/", buscar_pagina, name="PaginaSearch"),
    path("pagina/list/", PaginasList.as_view(), name="PaginaList"),
    path("pagina/detalle/<int:pk>", PaginaDetalle.as_view(), name="PaginaDetail"),
    #path(r'^pagina/detalle/(?P<pk>\d+)', PaginaDetalle.as_view(), name="PaginaDetail"),
    path("pagina/borrar/<pk>", PaginaDelete.as_view(), name="PaginaDelete"),
    path("pagina/editar/<pk>", PaginaUpdateView.as_view(), name="PaginaUpdate"),

    path("agregar-imagen/", agregar_imagen, name="AgregarImagen"),


]

