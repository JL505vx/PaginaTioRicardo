from django import forms
from .models import Seccion, Recurso


class SeccionForm(forms.ModelForm):
    """
    Formulario para crear secciones de la biblioteca.
    """

    class Meta:
        model = Seccion
        fields = ['nombre', 'descripcion', 'orden']
        labels = {
            'nombre': 'Nombre de la seccion',
            'descripcion': 'Descripcion',
            'orden': 'Orden',
        }


class RecursoForm(forms.ModelForm):
    """
    Formulario para crear recursos.
    """

    class Meta:
        model = Recurso
        fields = [
            'seccion',
            'titulo',
            'tipo',
            'descripcion',
            'archivo',
            'url_video',
            'texto',
            'publicado',
            'publicar_en_blog',
        ]
        labels = {
            'seccion': 'Seccion',
            'titulo': 'Titulo',
            'tipo': 'Tipo de recurso',
            'descripcion': 'Descripcion',
            'archivo': 'Archivo (documento o imagen)',
            'url_video': 'URL del video',
            'texto': 'Texto',
            'publicado': 'Publicar en Recursos (visible a pacientes)',
            'publicar_en_blog': 'Publicar tambien en Blog',
        }
        help_texts = {
            'publicado': 'Activa esto si quieres que aparezca en /recursos/.',
            'publicar_en_blog': 'Activa esto si quieres un post automatico en /blog/.',
        }

    def clean(self):
        cleaned = super().clean()
        tipo = cleaned.get('tipo')
        archivo = cleaned.get('archivo')
        url_video = cleaned.get('url_video')
        texto = cleaned.get('texto')

        if tipo == Recurso.TIPO_VIDEO and not url_video:
            self.add_error('url_video', 'Este tipo requiere una URL de video.')
        if tipo in (Recurso.TIPO_DOCUMENTO, Recurso.TIPO_IMAGEN) and not archivo:
            self.add_error('archivo', 'Este tipo requiere un archivo.')
        if tipo == Recurso.TIPO_TEXTO and not texto:
            self.add_error('texto', 'Este tipo requiere contenido de texto.')

        return cleaned
