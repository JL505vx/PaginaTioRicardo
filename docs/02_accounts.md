# 02. Accounts (Autenticacion y Roles)

## Archivos

1. `accounts/models.py`
2. `accounts/forms.py`
3. `accounts/views.py`
4. `accounts/urls.py`
5. `accounts/decorators.py`
6. `accounts/admin.py`
7. `templates/accounts/*.html`

## models.py

1. `CustomUser`:
   - Extiende `AbstractUser`.
   - Campo `rol`: `doctor` o `paciente`.
2. `ConversacionPrivada`:
   - Chat 1 a 1 entre doctor y paciente.
3. `MensajePrivado`:
   - Mensajes dentro del chat privado.

## forms.py

1. `RegistroPacienteForm`:
   - Crea usuarios con rol `paciente`.
2. `RegistroDoctorForm`:
   - Crea usuarios con rol `doctor`.
3. `LoginForm`:
   - Login comun.
4. `MensajePrivadoForm`:
   - Envio de mensajes privados.

## views.py

1. `registro_paciente`:
   - Registro publico paciente.
2. `registro_doctor`:
   - Registro doctor (en entorno real se protegeria).
3. `login_paciente`:
   - Login dedicado paciente.
4. `login_doctor`:
   - Login dedicado doctor.
5. `panel_paciente`:
   - Lista chats privados del paciente.
6. `chat_paciente`:
   - Chat privado con doctor.
7. `logout_view`:
   - Cierra sesion y redirige al inicio.

## urls.py

1. `/cuentas/registro/paciente/`
2. `/cuentas/registro/doctor/`
3. `/cuentas/ingresar/paciente/`
4. `/cuentas/ingresar/doctor/`
5. `/cuentas/panel/paciente/`
6. `/cuentas/chat/<doctor_id>/`
7. `/cuentas/salir/`

## decorators.py

1. `require_role(role)`:
   - Bloquea vista si usuario no tiene el rol.
   - Redirige a `blog:home` si no tiene permiso.

## admin.py

1. Registra `CustomUser`.
2. Registra chats privados y mensajes.

## templates/accounts

1. `login_paciente.html`:
   - Login paciente.
2. `login_doctor.html`:
   - Login doctor con estilo distinto.
3. `registro_paciente.html`:
   - Registro paciente.
4. `registro_doctor.html`:
   - Registro doctor.
5. `panel_paciente.html`:
   - Panel del paciente y chats.
6. `chat_paciente.html`:
   - Chat privado paciente-doctor.
