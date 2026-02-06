"""
Rutas publicas de la biblioteca.
"""
from django.urls import path
from . import views

app_name = 'contenido'

urlpatterns = [
    path('', views.lista_publica, name='lista_publica'),
]
