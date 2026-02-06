# 10. Templates en Detalle

Este documento describe cada template HTML y su proposito.

## templates/base.html

1. Layout principal del sitio.
2. Carga CSS y tipografias.
3. Incluye topbar, navbar y footer.

## templates/partials/topbar.html

1. Barra superior con contacto y nombre del doctor.

## templates/partials/navbar.html

1. Navegacion principal.
2. Acciones por rol (doctor/paciente).

## templates/partials/footer.html

1. Pie de pagina con informacion general.

## templates/blog/home.html

1. Hero principal.
2. Seccion de beneficios.
3. Vista previa de posts.

## templates/blog/post_list.html

1. Lista de publicaciones del blog.

## templates/blog/post_detail.html

1. Detalle del post.

## templates/foro/lista_temas.html

1. Lista de temas del foro.

## templates/foro/nuevo_tema.html

1. Formulario para crear tema.

## templates/foro/detalle_tema.html

1. Tema y respuestas.
2. Boton para abrir chat privado si doctor respondio.

## templates/accounts/login_paciente.html

1. Login paciente.

## templates/accounts/login_doctor.html

1. Login doctor (tema diferente).

## templates/accounts/registro_paciente.html

1. Registro paciente.

## templates/accounts/registro_doctor.html

1. Registro doctor.

## templates/accounts/panel_paciente.html

1. Panel del paciente.
2. Lista de chats privados.

## templates/accounts/chat_paciente.html

1. Chat privado paciente-doctor.

## templates/panel_doctor/dashboard.html

1. Panel del doctor.
2. Resumen de foro, chats y accesos.
3. Explicacion de funciones.

## templates/panel_doctor/chat_doctor.html

1. Chat privado del doctor.

## templates/panel_doctor/contenido_list.html

1. Biblioteca del doctor.
2. Explica secciones, recursos y publicaciones.

## templates/panel_doctor/contenido_form.html

1. Formulario crear recurso.
2. Recomendaciones segun tipo.

## templates/panel_doctor/contenido_seccion_form.html

1. Formulario crear seccion.

## templates/panel_doctor/contenido_confirm_delete.html

1. Confirmacion de eliminar recurso.

## templates/panel_doctor/contenido_seccion_confirm_delete.html

1. Confirmacion de eliminar seccion.

## templates/panel_doctor/blog_list.html

1. Lista de posts del doctor.

## templates/panel_doctor/blog_form.html

1. Crear/editar post.

## templates/panel_doctor/blog_confirm_delete.html

1. Confirmacion de eliminar post.

## templates/contenido/recursos_list.html

1. Biblioteca publica para pacientes.
