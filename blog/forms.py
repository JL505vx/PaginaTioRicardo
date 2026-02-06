from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Formulario para crear/editar posts desde el panel del doctor.
    """

    class Meta:
        model = Post
        fields = ['titulo', 'resumen', 'contenido', 'publicado']
        labels = {
            'titulo': 'Titulo',
            'resumen': 'Resumen corto',
            'contenido': 'Contenido completo',
            'publicado': 'Publicar ahora',
        }
