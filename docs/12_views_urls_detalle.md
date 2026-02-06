# 12. Views y URLs en Detalle

Este documento explica cada vista y su ruta.

## Blog

1. `blog.views.home` -> `/`
   - Landing con resumen de posts.
2. `blog.views.post_list` -> `/blog/`
   - Lista completa de posts.
3. `blog.views.post_detail` -> `/blog/<slug>/`
   - Detalle del post.

## Foro

1. `foro.views.lista_temas` -> `/foro/`
   - Lista publica de temas.
2. `foro.views.nuevo_tema` -> `/foro/nuevo/`
   - Crear tema (requiere login).
3. `foro.views.detalle_tema` -> `/foro/<id>/`
   - Tema, respuestas y chat privado habilitado si doctor responde.

## Accounts

1. `accounts.views.registro_paciente` -> `/cuentas/registro/paciente/`
2. `accounts.views.registro_doctor` -> `/cuentas/registro/doctor/`
3. `accounts.views.login_paciente` -> `/cuentas/ingresar/paciente/`
4. `accounts.views.login_doctor` -> `/cuentas/ingresar/doctor/`
5. `accounts.views.panel_paciente` -> `/cuentas/panel/paciente/`
6. `accounts.views.chat_paciente` -> `/cuentas/chat/<doctor_id>/`
7. `accounts.views.logout_view` -> `/cuentas/salir/`

## Panel Doctor

1. `panel_doctor.views.dashboard` -> `/doctor/`
2. `panel_doctor.views.chat_doctor` -> `/doctor/chat/<id>/`
3. `contenido.views.lista_contenido_doctor` -> `/doctor/contenido/`
4. `contenido.views.crear_recurso_doctor` -> `/doctor/contenido/nuevo/`
5. `contenido.views.crear_seccion_doctor` -> `/doctor/contenido/seccion/`
6. `contenido.views.editar_recurso_doctor` -> `/doctor/contenido/<id>/editar/`
7. `contenido.views.eliminar_recurso_doctor` -> `/doctor/contenido/<id>/eliminar/`
8. `contenido.views.editar_seccion_doctor` -> `/doctor/contenido/seccion/<id>/editar/`
9. `contenido.views.eliminar_seccion_doctor` -> `/doctor/contenido/seccion/<id>/eliminar/`
10. `blog.views.doctor_post_list` -> `/doctor/blog/`
11. `blog.views.doctor_post_create` -> `/doctor/blog/nuevo/`
12. `blog.views.doctor_post_edit` -> `/doctor/blog/<id>/editar/`
13. `blog.views.doctor_post_delete` -> `/doctor/blog/<id>/eliminar/`

## Contenido Publico

1. `contenido.views.lista_publica` -> `/recursos/`
