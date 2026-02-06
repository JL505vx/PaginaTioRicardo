"""
Modelos del blog informativo del doctor.
"""
from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Post(models.Model):
    """
    Entrada del blog creada por el doctor.
    """

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    resumen = models.TextField()
    contenido = models.TextField()
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    publicado = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.titulo
