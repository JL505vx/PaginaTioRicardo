"""
Modelos del foro de discusion.
"""
from django.db import models
from django.conf import settings


class Tema(models.Model):
    """
    Tema principal del foro (la duda inicial del paciente).
    """

    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='temas',
    )
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titulo


class Mensaje(models.Model):
    """
    Mensajes dentro de un tema (respuestas del doctor o pacientes).
    """

    tema = models.ForeignKey(
        Tema,
        on_delete=models.CASCADE,
        related_name='mensajes',
    )
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mensajes_foro',
    )
    cuerpo = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Mensaje de {self.autor} en {self.tema}'
