from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    class Meta: 
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return self.apellido + " " + self.nombre


class Articulo(models.Model):
    class Meta: 
        verbose_name_plural = "Articulos"

    titulo = models.CharField(max_length=30)
    resumen = models.CharField(max_length=30, null=True)
    texto = models.CharField(max_length=1000)
    fecha = models.DateField(null = True) 

    def __str__(self):
        return self.titulo


class Pagina(models.Model):
    class Meta: 
        verbose_name_plural = "Paginas"
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    resumen = models.CharField(max_length=30, null=True)
    texto = models.CharField(max_length=1000)
    fecha = models.DateField(null = True) 

    def __str__(self):
        return self.titulo


class Seccion(models.Model):
    class Meta: 
        verbose_name_plural = "Secciones"

    nombre_seccion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_seccion


class Imagenes(models.Model):
    class Meta: 
        verbose_name_plural = "Imagenes"
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)