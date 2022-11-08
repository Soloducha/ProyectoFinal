from django.http import HttpResponse
from django.shortcuts import render
from blog.forms import AutorForm, PaginaForm, AvatarForm, UserEditionForm, ImagenForm
from blog.models import Autor, Pagina, Avatar, Imagenes

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse


@login_required
def inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}

    return render(request, "inicio.html", contexto)


@login_required
def about(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}
    return render(request, "about.html", contexto)


def blogs(request):
    return render(
        request, "blogs.html"
    )  # busca todos los blogs y muestra en un a lista


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )
    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form": form})


class MyLogin(LoginView):
    template_name = "login.html"


class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "logout.html"


@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()

    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "inicio.html", {"avatar": avatar.imagen.url})

    if avatar is not None:
        contexto = {"user": user, "form": form, "avatar": avatar.imagen.url}
    else:
        contexto = {}
    return render(request, "editarPerfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "inicio.html")

    contexto = {"form": form}
    return render(request, "cambiarAvatar.html", contexto)

@login_required
def agregar_imagen(request):
    if request.method != "POST":
        form = ImagenForm()
    else:
        form = ImagenForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            #Imagenes.objects.filter(pagina=request.id).delete()
            form.save()
            return render(request, "inicio.html")

    contexto = {"form": form}
    return render(request, "cambiarImagen.html", contexto)


def procesar_autor(request):
    avatar = Avatar.objects.filter(user=request.user).first()

    if request.method == "GET":
        mi_formulario = AutorForm()
        if avatar is not None:
            contexto = {"avatar": avatar.imagen.url, "formulario": mi_formulario}
        else:
            contexto = {"formulario": mi_formulario}
        
        return render(request, "formulario-autor.html", contexto)

    if request.method == "POST":
        if avatar is not None:
            contexto = {"avatar": avatar.imagen.url}
        else:
            contexto = {}

        mi_formulario = AutorForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Autor(
                nombre=datos_ingresados_por_usuario["nombre"],
                apellido=datos_ingresados_por_usuario["apellido"],
            )
            nuevo_modelo.save()

            return render(request, "exito.html",contexto)


@login_required
def buscar_autor(request):
    avatar = Avatar.objects.filter(user=request.user).first()

    if request.method == "GET":
        if avatar is not None:
            contexto = {"avatar": avatar.imagen.url}
        else:
            contexto = {}
        return render(request, "busqueda-autor.html", contexto)

    if request.method == "POST":
        nombre_a_buscar = request.POST["nombre"]
        resultados_de_busqueda = Autor.objects.filter(nombre=nombre_a_buscar)
        if avatar is not None:
            contexto = {"avatar": avatar.imagen.url, "resultados": resultados_de_busqueda}
        else:
            contexto = {"resultados": resultados_de_busqueda}
        return render(request, "resultado-de-busqueda.html", contexto)


@login_required
def buscar_pagina(request):
    avatar = Avatar.objects.filter(user=request.user).first()

    if request.method == "GET":
        if avatar is not None:
            contexto = {"avatar": avatar.imagen.url}
        else:
            contexto = {}
        return render(request, "busqueda-pagina.html", contexto)

    if request.method == "POST":
        pagina_a_buscar = request.POST["nombre"]
        resultados_de_busqueda = Pagina.objects.filter(titulo=pagina_a_buscar)
        if avatar is not None:
            contexto = {"avatar": avatar.imagen.url, "resultados": resultados_de_busqueda}
        else:
            contexto = {"resultados": resultados_de_busqueda}
        return render(request, "resultado-de-busqueda.html", contexto)


class AutorCreacion(LoginRequiredMixin, CreateView):
    model = Autor
    fields = ["nombre", "apellido"]
    success_url = "/autor/list"


class AutorList(LoginRequiredMixin, ListView):
    model = Autor
    template_name = "autor_list.html"


class AutorDetalle(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = "autor_detalle.html"
 
 
class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    success_url = "/autor/list/"
    fields = ["nombre", "apellido"]


class AutorDelete(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = "/autor/list/"


class PaginaCreacion(LoginRequiredMixin, CreateView):
    model = Pagina
    fields = ["autor", "titulo", "resumen", "texto", "fecha"]
    success_url = "/pagina/list/"
    

class PaginasList(LoginRequiredMixin, ListView):
    model = Pagina

    template_name = "pagina_list.html"

class PaginaDetalle(LoginRequiredMixin, DetailView):
    model = Pagina
    template_name = "pagina_detalle.html"
     
    def get_context_data(self,*args,**kwargs):  
        idpath=self.request.path[-1]
        imagen = Imagenes.objects.filter(pagina=idpath).first()
        kwargs.update({"imagen": imagen })
        context= super().get_context_data(**kwargs)
        return context

class PaginaUpdateView(LoginRequiredMixin, UpdateView):
    model = Pagina
    success_url = "/pagina/list/"
    fields = ["autor", "titulo", "resumen", "texto", "fecha"]


class PaginaDelete(LoginRequiredMixin, DeleteView):
    model = Pagina
    success_url = "/pagina/list/"