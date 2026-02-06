# TioRicardoPaginaBlog

Documentacion extensa del proyecto (Django).

## Contenido

1. Resumen
2. Como correr el proyecto
3. Rutas principales
4. Arquitectura por apps
5. Documentacion por archivos (HTML/CSS/Views/URLs/Models/Forms)
6. Base de datos y modelos
7. Flujo de roles (Doctor/Paciente)
8. Biblioteca y Blog (publicacion)

## 1. Resumen

Proyecto web para el Dr. Ricardo Bernae Luna Cruz (anestesiologo) con:

1. Blog informativo.
2. Foro de dudas.
3. Panel privado del doctor.
4. Panel privado de paciente.
5. Biblioteca de recursos (documentos, videos, imagenes, texto).
6. Chat privado doctor-paciente.

## 2. Como correr el proyecto

1. Migraciones:
   `python manage.py makemigrations`
   `python manage.py migrate`
2. Ejecutar servidor:
   `python manage.py runserver 8002`

## 2.1 Deploy Demo en Render (opcional)

Este proyecto incluye `render.yaml` para despliegue rapido en Render.

Pasos:
1. Crear Web Service desde el repo de GitHub.
2. Render lee `render.yaml` automaticamente.
3. Esperar build y deploy.

Nota: en modo demo con SQLite, los datos pueden perderse si Render reinicia.

## 3. Rutas principales

1. Inicio: `http://127.0.0.1:8002/`
2. Blog: `http://127.0.0.1:8002/blog/`
3. Foro: `http://127.0.0.1:8002/foro/`
4. Recursos: `http://127.0.0.1:8002/recursos/`
5. Login paciente: `http://127.0.0.1:8002/cuentas/ingresar/paciente/`
6. Login doctor: `http://127.0.0.1:8002/cuentas/ingresar/doctor/`
7. Panel doctor: `http://127.0.0.1:8002/doctor/`
8. Panel paciente: `http://127.0.0.1:8002/cuentas/panel/paciente/`

## 4. Arquitectura por apps

1. `accounts`: autenticacion, roles, panel paciente y chat.
2. `blog`: posts informativos.
3. `foro`: temas y mensajes publicos.
4. `panel_doctor`: dashboard del doctor y chat privado.
5. `contenido`: biblioteca de recursos (publico y panel doctor).

## 5. Documentacion por archivos

Esta documentacion extensa esta en `docs/`:

1. docs/01_config_y_settings.md
2. docs/02_accounts.md
3. docs/03_blog.md
4. docs/04_foro.md
5. docs/05_panel_doctor.md
6. docs/06_contenido_biblioteca.md
7. docs/07_templates_base_y_partials.md
8. docs/08_css.md
9. docs/09_flujos.md
10. docs/10_templates_detalle.md
11. docs/11_css_detalle.md
12. docs/12_views_urls_detalle.md
13. docs/13_manual_usuario.md

## 6. Base de datos y modelos

Resumen en `docs/09_flujos.md` y detalles por app en `docs/02_accounts.md`, `docs/03_blog.md`, `docs/04_foro.md` y `docs/06_contenido_biblioteca.md`.

## 7. Flujo de roles

1. Paciente:
   - Registro y login.
   - Panel propio.
   - Foro y chat privado (si el doctor responde).
2. Doctor:
   - Panel privado.
   - Responde foro.
   - Gestiona recursos.
   - Chat privado con pacientes.

## 8. Biblioteca y Blog

1. Un recurso puede publicarse en Recursos y opcionalmente en Blog.
2. La decision es del doctor con dos checkboxes claros.
3. Recomendaciones automaticas segun el tipo de recurso.
