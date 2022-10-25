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
 
class MyLogin(LoginView):
    template_name= "login.html"

def inicio(request):
    return render(request, "inicio.html")

def about(request):
    return render(request, "about.html")

def blogs(request):
    return render(request, "blogs.html") #busca todos los blogs y muestra en un a lista




def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "AppCoder24/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "registro.html", {"form": form})