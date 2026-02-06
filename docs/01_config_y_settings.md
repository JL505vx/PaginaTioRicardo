# 01. Configuracion y Settings

Este documento describe configuraciones globales del proyecto.

## Archivos clave

1. `config/settings.py`
2. `config/urls.py`

## config/settings.py

1. `INSTALLED_APPS` incluye:
   - `accounts`, `blog`, `foro`, `panel_doctor`, `contenido`.
2. `TEMPLATES` usa `BASE_DIR / 'templates'` para plantillas globales.
3. `DATABASES`:
   - SQLite por defecto.
   - PostgreSQL via variables de entorno (Docker).
4. `AUTH_USER_MODEL`:
   - `accounts.CustomUser` (usuario con rol).
5. `STATIC_URL`, `STATICFILES_DIRS`:
   - CSS e imagenes desde `static/`.
6. `MEDIA_URL`, `MEDIA_ROOT`:
   - Archivos subidos (recursos en biblioteca).
7. `LANGUAGE_CODE` y `TIME_ZONE`:
   - Espanol Mexico y zona local.

## config/urls.py

1. Rutas publicas:
   - `/` (blog.home)
   - `/blog/`
   - `/foro/`
   - `/recursos/`
2. Rutas de cuentas:
   - `/cuentas/`
3. Panel doctor:
   - `/doctor/`
4. Alias legacy:
   - `/panel-doctor/`
5. Static/media en DEBUG.
