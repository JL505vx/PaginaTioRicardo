# 07. Templates Base y Partials

## Archivos

1. `templates/base.html`
2. `templates/partials/topbar.html`
3. `templates/partials/navbar.html`
4. `templates/partials/footer.html`

## base.html

1. Define estructura general.
2. Carga CSS y tipografias.
3. Incluye topbar, navbar y footer.
4. Define bloque `{% block content %}`.

## topbar.html

1. Muestra contacto y nombre del doctor.

## navbar.html

1. Navegacion principal.
2. Muestra botones segun rol:
   - Doctor: Panel Doctor.
   - Paciente: Mi Panel.

## footer.html

1. Pie de pagina con info general.
2. Link discreto a Acceso profesional y Biblioteca.
