from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import Avatar
from mensajes.models import Mensaje


class MensajeForm(forms.ModelForm):

    emisor = forms.CharField(label="emisor del mensaje")
    mensaje = forms.CharField(label="escriba su mensaje")

    class Meta:
        model = Mensaje
        fields = ["emisor", "mensaje"]  