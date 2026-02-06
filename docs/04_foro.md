# 04. Foro

## Archivos

1. `foro/models.py`
2. `foro/forms.py`
3. `foro/views.py`
4. `foro/urls.py`
5. `foro/admin.py`
6. `templates/foro/*.html`

## models.py

1. `Tema`:
   - Duda principal del paciente.
2. `Mensaje`:
   - Respuestas dentro del tema.

## forms.py

1. `TemaForm`:
   - Crear tema.
2. `MensajeForm`:
   - Responder tema.

## views.py

1. `lista_temas`:
   - Lista publica de temas.
2. `nuevo_tema`:
   - Crear tema (requiere login).
3. `detalle_tema`:
   - Muestra mensajes y permite responder.
   - Detecta si un doctor respondio para habilitar chat privado.

## urls.py

1. `/foro/` -> lista.
2. `/foro/nuevo/` -> nuevo tema.
3. `/foro/<id>/` -> detalle.

## templates/foro

1. `lista_temas.html`.
2. `nuevo_tema.html`.
3. `detalle_tema.html`.
