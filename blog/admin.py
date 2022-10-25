from django.contrib import admin
from django.contrib import admin
from blog.models import Autor, Avatar, Pagina
from mensajes.models import Mensaje

admin.site.register(Autor)
admin.site.register(Pagina)
admin.site.register(Avatar)
admin.site.register(Mensaje)