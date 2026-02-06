"""
Rutas del panel del doctor.
"""
from django.urls import path
from . import views
from contenido import views as contenido_views
from blog import views as blog_views

app_name = 'panel_doctor'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('chat/<int:conversacion_id>/', views.chat_doctor, name='chat_doctor'),
    path('contenido/', contenido_views.lista_contenido_doctor, name='contenido'),
    path('contenido/nuevo/', contenido_views.crear_recurso_doctor, name='contenido_nuevo'),
    path('contenido/seccion/', contenido_views.crear_seccion_doctor, name='contenido_seccion'),
    path('contenido/<int:recurso_id>/editar/', contenido_views.editar_recurso_doctor, name='contenido_editar'),
    path('contenido/<int:recurso_id>/eliminar/', contenido_views.eliminar_recurso_doctor, name='contenido_eliminar'),
    path('contenido/seccion/<int:seccion_id>/editar/', contenido_views.editar_seccion_doctor, name='seccion_editar'),
    path('contenido/seccion/<int:seccion_id>/eliminar/', contenido_views.eliminar_seccion_doctor, name='seccion_eliminar'),
    path('blog/', blog_views.doctor_post_list, name='blog'),
    path('blog/nuevo/', blog_views.doctor_post_create, name='blog_nuevo'),
    path('blog/<int:post_id>/editar/', blog_views.doctor_post_edit, name='blog_editar'),
    path('blog/<int:post_id>/eliminar/', blog_views.doctor_post_delete, name='blog_eliminar'),
]
