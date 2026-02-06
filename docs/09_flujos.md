# 09. Flujos y Casos de Uso

## Flujo paciente

1. Entra a `/cuentas/ingresar/paciente/`.
2. Publica tema en `/foro/`.
3. Recibe respuesta del doctor.
4. Si el doctor responde, puede abrir chat privado.

## Flujo doctor

1. Entra a `/cuentas/ingresar/doctor/`.
2. Revisa panel en `/doctor/`.
3. Responde en foro.
4. Administra biblioteca en `/doctor/contenido/`.
5. Decide si publica en Recursos y/o Blog.

## Publicacion Recursos y Blog

1. Recurso con `publicado`:
   - Visible en `/recursos/`.
2. Recurso con `publicar_en_blog`:
   - Crea o actualiza Post en `/blog/`.
3. Si desmarca `publicar_en_blog`, el post se oculta.

## Chats privados

1. Se crean cuando el paciente abre chat.
2. Solo doctor y paciente pueden verlos.
