"""
Modelo de usuario personalizado.
Se usa para separar el tipo de cuenta: doctor o paciente.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    """
    Extiende el usuario estándar de Django con un campo de rol.
    Esto permite separar el acceso y el diseño entre doctor y paciente.
    """

    ROLE_DOCTOR = 'doctor'
    ROLE_PACIENTE = 'paciente'

    ROLE_CHOICES = [
        (ROLE_DOCTOR, 'Doctor'),
        (ROLE_PACIENTE, 'Paciente'),
    ]

    rol = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_PACIENTE,
        help_text='Define si el usuario es doctor o paciente.',
    )

    @property
    def es_doctor(self) -> bool:
        return self.rol == self.ROLE_DOCTOR

    @property
    def es_paciente(self) -> bool:
        return self.rol == self.ROLE_PACIENTE

    def __str__(self) -> str:
        return f'{self.username} ({self.get_rol_display()})'


class ConversacionPrivada(models.Model):
    """
    Conversacion privada entre un doctor y un paciente.
    Se crea cuando el paciente decide escribirle al doctor.
    """

    doctor = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='conversaciones_doctor',
    )
    paciente = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='conversaciones_paciente',
    )
    tema = models.ForeignKey(
        'foro.Tema',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='conversaciones',
        help_text='Tema de foro que inicio la conversacion (opcional).',
    )
    creado = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('doctor', 'paciente')

    def __str__(self) -> str:
        return f'Chat {self.doctor} / {self.paciente}'


class MensajePrivado(models.Model):
    """
    Mensajes dentro de una conversacion privada.
    """

    conversacion = models.ForeignKey(
        ConversacionPrivada,
        on_delete=models.CASCADE,
        related_name='mensajes',
    )
    autor = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='mensajes_privados',
    )
    cuerpo = models.TextField()
    creado = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'Mensaje privado de {self.autor}'
