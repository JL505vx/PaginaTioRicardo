"""Registro del contenido en admin."""
from django.contrib import admin
from .models import Seccion, Recurso


@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden', 'creado']
    search_fields = ['nombre']


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'seccion', 'publicado', 'publicar_en_blog', 'creado', 'creado_por']
    list_filter = ['tipo', 'publicado', 'publicar_en_blog']
    search_fields = ['titulo', 'descripcion']
