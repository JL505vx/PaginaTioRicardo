"""Registro de modelos del blog en el admin."""
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'publicado', 'creado']
    list_filter = ['publicado', 'creado']
    search_fields = ['titulo', 'resumen']
    prepopulated_fields = {'slug': ('titulo',)}
