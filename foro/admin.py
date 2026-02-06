"""Registro de modelos del foro en el admin."""
from django.contrib import admin
from .models import Tema, Mensaje


@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'creado']
    search_fields = ['titulo', 'cuerpo']


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ['tema', 'autor', 'creado']
    search_fields = ['cuerpo']
