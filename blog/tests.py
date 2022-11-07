from django.test import TestCase
from blog.models import Autor

class ViewTestCase(TestCase):
    def test_autores(self):
        Autor.objects.create(nombre="Juan", apellido="Lopez")
        Autor.objects.create(nombre="Gonzalo", apellido="Gonzalez")
        todos_los_autores = Autor.objects.all()

        assert len(todos_los_autores) == 2
        assert todos_los_autores[0].nombre == "Juan"
        assert todos_los_autores[0].apellido == "Lopez"
        assert todos_los_autores[1].nombre == "Gonzalo"
        assert todos_los_autores[1].apellido == "Gonzalez"

class ViewTestCase(TestCase):
    def test_Articulos(self):
        pass

class ViewTestCase(TestCase):
    def test_Secciones(self):
        pass