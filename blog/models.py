from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return self.apellido + " " + self.nombre


class Pagina(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)