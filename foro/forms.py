from django import forms
from .models import Tema, Mensaje


class TemaForm(forms.ModelForm):
    """
    Formulario para crear un tema nuevo en el foro.
    """

    class Meta:
        model = Tema
        fields = ['titulo', 'cuerpo']
        labels = {'titulo': 'Titulo', 'cuerpo': 'Mensaje'}


class MensajeForm(forms.ModelForm):
    """
    Formulario para responder dentro de un tema.
    """

    class Meta:
        model = Mensaje
        fields = ['cuerpo']
        labels = {'cuerpo': 'Respuesta'}
