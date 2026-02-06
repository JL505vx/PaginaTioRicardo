# 05. Panel Doctor

## Archivos

1. `panel_doctor/views.py`
2. `panel_doctor/urls.py`
3. `templates/panel_doctor/*.html`

## views.py

1. `dashboard`:
   - Resumen de temas, mensajes y chats.
2. `chat_doctor`:
   - Chat privado por conversacion.

## urls.py

1. `/doctor/` -> dashboard.
2. `/doctor/chat/<id>/` -> chat privado.
3. `/doctor/contenido/` -> biblioteca del doctor.
4. `/doctor/contenido/nuevo/` -> crear recurso.
5. `/doctor/contenido/seccion/` -> crear seccion.
6. `/doctor/blog/` -> administrar blog.
7. `/doctor/blog/nuevo/` -> nuevo post.
8. `/doctor/blog/<id>/editar/` -> editar post.
9. `/doctor/blog/<id>/eliminar/` -> eliminar post.

## templates/panel_doctor

1. `dashboard.html`:
   - Panel con resumen y bloque explicativo.
2. `chat_doctor.html`:
   - Chat privado del doctor.
3. `contenido_list.html`:
   - Biblioteca del doctor con ayuda.
4. `contenido_form.html`:
   - Formulario para crear recurso.
5. `contenido_seccion_form.html`:
   - Formulario para crear seccion.
6. `blog_list.html`:
   - Lista de posts del doctor.
7. `blog_form.html`:
   - Crear/editar post.
8. `blog_confirm_delete.html`:
   - Confirmacion de eliminar post.
