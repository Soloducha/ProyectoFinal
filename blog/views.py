from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, "inicio.html")

def about(request):
    return render(request, "about.html")

def blogs(request):
    return render(request, "blogs.html") #busca todos los blogs y muestra en un a lista