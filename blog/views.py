from django.http import HttpResponse
from django.shortcuts import render

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

from blog.models import Avatar
from blog.forms import AvatarForm, UserEditionForm

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
        contexto = {
        "user": user, 
        "form": form,
        "avatar": avatar.imagen.url
        }
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
