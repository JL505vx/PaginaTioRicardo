"""Registro en admin para manejar usuarios con rol."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ConversacionPrivada, MensajePrivado


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Rol', {'fields': ('rol',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rol', {'fields': ('rol',)}),
    )
    list_display = ['username', 'email', 'rol', 'is_staff']
    list_filter = ['rol', 'is_staff']


@admin.register(ConversacionPrivada)
class ConversacionPrivadaAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'paciente', 'tema', 'creado']
    search_fields = ['doctor__username', 'paciente__username']


@admin.register(MensajePrivado)
class MensajePrivadoAdmin(admin.ModelAdmin):
    list_display = ['conversacion', 'autor', 'creado']
    search_fields = ['cuerpo']
