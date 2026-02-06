# 03. Blog

## Archivos

1. `blog/models.py`
2. `blog/views.py`
3. `blog/urls.py`
4. `blog/admin.py`
5. `templates/blog/*.html`

## models.py

1. `Post`:
   - `titulo`, `slug`, `resumen`, `contenido`, `autor`, `publicado`.
   - `slug` se genera automaticamente si esta vacio.

## views.py

1. `home`:
   - Home publica con resumen de posts.
2. `post_list`:
   - Lista completa de posts.
3. `post_detail`:
   - Detalle de post por slug.

## urls.py

1. `/` -> `home`
2. `/blog/` -> `post_list`
3. `/blog/<slug>/` -> `post_detail`

## admin.py

1. Registro de `Post` con prepopulated slug.

## templates/blog

1. `home.html`:
   - Hero y secciones informativas.
2. `post_list.html`:
   - Lista de posts.
3. `post_detail.html`:
   - Detalle del post.

## Panel del Doctor (CRUD)

1. `/doctor/blog/`:
   - Lista de posts para crear, editar o eliminar.
2. `/doctor/blog/nuevo/`:
   - Crear post.
3. `/doctor/blog/<id>/editar/`:
   - Editar post.
4. `/doctor/blog/<id>/eliminar/`:
   - Eliminar post.
