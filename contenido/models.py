"""
Modelos para la biblioteca de contenido del doctor.
Incluye documentos, videos, imagenes y notas informativas.
"""
from django.db import models
from django.conf import settings


class Seccion(models.Model):
    """
    Seccion principal para agrupar recursos (ej. Preparacion, Recuperacion).
    """

    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden', 'nombre']

    def __str__(self) -> str:
        return self.nombre


class Recurso(models.Model):
    """
    Recurso publicado por el doctor.
    Puede ser documento, video, imagen o texto.
    """

    TIPO_DOCUMENTO = 'documento'
    TIPO_VIDEO = 'video'
    TIPO_IMAGEN = 'imagen'
    TIPO_TEXTO = 'texto'

    TIPO_CHOICES = [
        (TIPO_DOCUMENTO, 'Documento'),
        (TIPO_VIDEO, 'Video'),
        (TIPO_IMAGEN, 'Imagen'),
        (TIPO_TEXTO, 'Texto'),
    ]

    seccion = models.ForeignKey(
        Seccion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='recursos',
    )
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='recursos_creados',
        help_text='Usuario doctor que creo el recurso.',
    )
    blog_post = models.OneToOneField(
        'blog.Post',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='recurso_relacionado',
        help_text='Post generado automaticamente en el blog.',
    )
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.TextField(blank=True)
    archivo = models.FileField(upload_to='recursos/', blank=True)
    url_video = models.URLField(blank=True)
    texto = models.TextField(blank=True)
    publicado = models.BooleanField(
        default=True,
        help_text='Si esta activo, el recurso se muestra en /recursos/.',
    )
    publicar_en_blog = models.BooleanField(
        default=False,
        help_text='Si esta activo, tambien se crea un post en el blog.',
    )
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self) -> str:
        return self.titulo
