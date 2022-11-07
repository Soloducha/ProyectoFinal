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
    procesar_articulo,
    procesar_seccion,
   # procesar_pagina,
    buscar_pagina,
    buscar_articulo,
    buscar_autor,
    buscar_seccion,
    AutorList,
    AutorUpdateView,
   # AutorCreacion,
    AutorDelete,
    AutorDetalle,
    ArticuloList,
    ArticuloDetalle,
    ArticuloDelete,
    SeccionList,
    SeccionDetalle,
    SeccionDelete,
    PaginasList,
    PaginaDetalle,
    PaginaDelete,
    ArticuloUpdateView,
    PaginaCreacion,
    PaginaUpdateView
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

    path("formulario-articulo/", procesar_articulo, name="ArticuloNew"),
    path("articulo/list/", ArticuloList.as_view(), name="ArticuloList"),
    path("buscar-articulo/", buscar_articulo, name="ArticuloSearch"),
    path("articulo/detalle/<pk>", ArticuloDetalle.as_view(), name="ArticuloDetail"),
    path("articulo/borrar/<pk>", ArticuloDelete.as_view(), name="ArticuloDelete"),
    path("articulo/editar/<pk>", ArticuloUpdateView.as_view(), name="ArticuloUpdate"),

    path("formulario-autor/", procesar_autor, name="AutorNew"),
    path("autor/list/", AutorList.as_view(), name="AutorList"),
    path("buscar-autor/", buscar_autor, name="AutorSearch"),
    path("autor/detalle/<pk>", AutorDetalle.as_view(), name="AutorDetail"),
    path("autor/borrar/<pk>", AutorDelete.as_view(), name="AutorDelete"),
    path("autor/editar/<pk>", AutorUpdateView.as_view(), name="AutorUpdate"),

    path("formulario-seccion/", procesar_seccion, name="SeccionNew"),
    path("buscar-seccion/", buscar_seccion, name="SeccionSearch"),
    path("seccion/list/", SeccionList.as_view(), name="SeccionList"),
    path("seccion/detalle/<pk>", SeccionDetalle.as_view(), name="SeccionDetail"),
    path("seccion/borrar/<pk>", SeccionDelete.as_view(), name="SeccionDelete"),

    path("pagina-nuevo/", PaginaCreacion.as_view(), name="PaginaNew"),
    path("buscar-pagina/", buscar_pagina, name="PaginaSearch"),
    path("pagina/list/", PaginasList.as_view(), name="PaginaList"),
    path("pagina/detalle/<pk>", PaginaDetalle.as_view(), name="PaginaDetail"),
    path("pagina/borrar/<pk>", PaginaDelete.as_view(), name="PaginaDelete"),
    path("pagina/editar/<pk>", PaginaUpdateView.as_view(), name="PaginaUpdate"),




]

