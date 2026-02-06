"""
Rutas de autenticacion.
Separadas por rol para diseno y flujos distintos.
"""
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('registro/paciente/', views.registro_paciente, name='registro_paciente'),
    path('registro/doctor/', views.registro_doctor, name='registro_doctor'),
    path('ingresar/paciente/', views.login_paciente, name='login_paciente'),
    path('ingresar/doctor/', views.login_doctor, name='login_doctor'),
    path('panel/paciente/', views.panel_paciente, name='panel_paciente'),
    path('chat/<int:doctor_id>/', views.chat_paciente, name='chat_paciente'),
    path('vista/alternar/', views.alternar_vista_publica, name='alternar_vista_publica'),
    path('salir/', views.logout_view, name='logout'),
]
