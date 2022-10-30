from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import Avatar
from django.contrib.auth import authenticate
from mensajes.models import Mensaje
from django.db import models

class Chat(models.Model):
    emisor = models.IntegerField()
    mensaje = models.CharField(max_length=200)
    avatar = models.ImageField()
    alineamiento = models.CharField(max_length=1)

@login_required
def mensajeria(request):
    if request.method == "GET":
        mensajes_guardados=Mensaje.objects.filter()
        chats=[]
        i=0
        for item in mensajes_guardados:
            emisor=item.emisor_id,
            mensaje = item.mensaje,
            avatar = Avatar.objects.filter(user=emisor).first()
            if i %2 == 0:
                alineamiento = "I"
            else:
                alineamiento = "R"
            i=i+1
         
            chat=Chat(emisor=emisor[0],mensaje=mensaje[0],avatar=avatar, alineamiento=alineamiento)
            chats.append(chat)

        

        avatar = Avatar.objects.filter(user=request.user).first()
   
        if avatar is not None:
            contexto = {"mensajes": chats,"avatar": avatar.imagen.url}
        else:
            contexto = {"mensajes": chats}

        return render(request, "mensajeria.html", contexto)

    if request.method == "POST":
        
        formulario = request.POST
        if formulario["mensaje"] is not None:
            mensaje_recibido = formulario["mensaje"]
            emisor = request.user

            nuevo_mensaje = Mensaje(
                emisor=emisor,
                mensaje=mensaje_recibido
            )
            nuevo_mensaje.save()
            
            mensajes_guardados=Mensaje.objects.filter()
            chats=[]
            i=0
            for item in mensajes_guardados:
                emisor=item.emisor_id,
                mensaje = item.mensaje,
                avatar = Avatar.objects.filter(user=emisor).first()
                if i %2 == 0:
                    alineamiento = "I"
                else:
                    alineamiento = "R"
                i=i+1
            
                chat=Chat(emisor=emisor[0],mensaje=mensaje[0],avatar=avatar, alineamiento=alineamiento)
                chats.append(chat)

            avatar = Avatar.objects.filter(user=request.user).first()
            if avatar is not None:
                contexto = {"mensajes": chats,"avatar": avatar.imagen.url}
            else:
               contexto = {"mensajes": chats}

            return render(request, "mensajeria.html", contexto)
        else:
            mensajes_guardados=Mensaje.objects.filter()
            chats=[]
            i=0
            for item in mensajes_guardados:
                emisor=item.emisor_id,
                mensaje = item.mensaje,
                avatar = Avatar.objects.filter(user=emisor).first()
                if i %2 == 0:
                    alineamiento = "I"
                else:
                    alineamiento = "R"
                i=i+1
            
                chat=Chat(emisor=emisor[0],mensaje=mensaje[0],avatar=avatar, alineamiento=alineamiento)
                chats.append(chat)

            avatar = Avatar.objects.filter(user=request.user).first()
            if avatar is not None:
                contexto = {"mensajes": chats,"avatar": avatar.imagen.url}
            else:
               contexto = {"mensajes": chats}
            
            return render(request, "mensajeria.html", contexto)