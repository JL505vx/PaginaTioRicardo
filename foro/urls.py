"""
Rutas del foro.
"""
from django.urls import path
from . import views

app_name = 'foro'

urlpatterns = [
    path('', views.lista_temas, name='lista_temas'),
    path('nuevo/', views.nuevo_tema, name='nuevo_tema'),
    path('<int:tema_id>/', views.detalle_tema, name='detalle_tema'),
]
