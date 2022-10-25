from django.db import models
from django.contrib.auth.models import User
from blog.models import Avatar


class Mensaje(models.Model):
    class Meta:
        verbose_name_plural = "Mensajes"
    
    emisor = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = Avatar(User)
    mensaje = models.CharField(max_length=200)

    def __str__(self): 
        return self.mensaje

