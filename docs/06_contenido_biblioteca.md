# 06. Contenido y Biblioteca

## Archivos

1. `contenido/models.py`
2. `contenido/forms.py`
3. `contenido/views.py`
4. `contenido/urls.py`
5. `contenido/admin.py`
6. `templates/contenido/recursos_list.html`
7. `templates/panel_doctor/contenido_list.html`
8. `templates/panel_doctor/contenido_form.html`
9. `templates/panel_doctor/contenido_seccion_form.html`

## models.py

1. `Seccion`:
   - Agrupa recursos por tema.
   - Campo `orden` define el orden.
2. `Recurso`:
   - Tipos: documento, video, imagen, texto.
   - `publicado`: visible en /recursos/.
   - `publicar_en_blog`: crea post en /blog/ (decidido por el doctor).
   - `blog_post`: relacion al post generado.

## forms.py

1. `RecursoForm`:
   - Campos para recursos.
   - Etiquetas claras para publicar.

## views.py

1. `lista_publica`:
   - Muestra recursos publicados.
2. `lista_contenido_doctor`:
   - Panel de administracion.
3. `crear_recurso_doctor`:
   - Guarda recursos.
   - Si `publicar_en_blog` esta activo crea/actualiza Post.
4. `crear_seccion_doctor`:
   - Crea secciones.

## urls.py

1. `/recursos/` -> lista publica.

## admin.py

1. Registro de Seccion y Recurso.

## templates

1. `recursos_list.html`:
   - Lista publica.
2. `contenido_list.html`:
   - Panel del doctor con explicacion.
3. `contenido_form.html`:
   - Formulario de recurso y recomendaciones.
4. `contenido_seccion_form.html`:
   - Formulario de secciones.
