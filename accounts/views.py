"""
Vistas de autenticacion con diseno separado para doctor y paciente.
"""
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import RegistroPacienteForm, RegistroDoctorForm, LoginForm, MensajePrivadoForm
from .models import CustomUser, ConversacionPrivada, MensajePrivado
from .decorators import require_role


def registro_paciente(request):
    """
    Registro publico para pacientes.
    Crea un usuario con rol 'paciente'.
    """
    if request.method == 'POST':
        form = RegistroPacienteForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:panel_paciente')
    else:
        form = RegistroPacienteForm()

    return render(request, 'accounts/registro_paciente.html', {'form': form})


def registro_doctor(request):
    """
    Registro del doctor.
    En un entorno real deberia estar protegido o por invitacion.
    """
    if request.method == 'POST':
        form = RegistroDoctorForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('panel_doctor:dashboard')
    else:
        form = RegistroDoctorForm()

    return render(request, 'accounts/registro_doctor.html', {'form': form})


def login_paciente(request):
    """
    Login con plantilla dedicada para pacientes.
    """
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.rol != CustomUser.ROLE_PACIENTE:
                messages.error(request, 'Esta cuenta no es de paciente.')
            else:
                login(request, user)
                return redirect('accounts:panel_paciente')
    else:
        form = LoginForm()

    return render(request, 'accounts/login_paciente.html', {'form': form})


def login_doctor(request):
    """
    Login con plantilla dedicada para doctor.
    """
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.rol != CustomUser.ROLE_DOCTOR:
                messages.error(request, 'Esta cuenta no es de doctor.')
            else:
                login(request, user)
                return redirect('panel_doctor:dashboard')
    else:
        form = LoginForm()

    return render(request, 'accounts/login_doctor.html', {'form': form})


def logout_view(request):
    """
    Cierre de sesion simple para ambos roles.
    """
    logout(request)
    return redirect('blog:home')


@require_role(CustomUser.ROLE_PACIENTE)
def panel_paciente(request):
    """
    Panel privado del paciente.
    Aqui se mostraran sus temas y mensajes personales.
    """
    conversaciones = (
        ConversacionPrivada.objects.filter(paciente=request.user)
        .select_related('doctor', 'tema')
        .order_by('-creado')
    )

    return render(
        request,
        'accounts/panel_paciente.html',
        {'conversaciones': conversaciones},
    )


@require_role(CustomUser.ROLE_DOCTOR)
def alternar_vista_publica(request):
    """
    Permite al doctor ver el sitio como lo veria un visitante/paciente.
    Solo cambia la apariencia, no los permisos.
    """
    actual = request.session.get('vista_publica', False)
    request.session['vista_publica'] = not actual
    next_url = request.GET.get('next') or '/'
    return redirect(next_url)


@require_role(CustomUser.ROLE_PACIENTE)
def chat_paciente(request, doctor_id):
    """
    Chat privado del paciente con un doctor.
    """
    doctor = CustomUser.objects.get(id=doctor_id, rol=CustomUser.ROLE_DOCTOR)
    conversacion, _ = ConversacionPrivada.objects.get_or_create(
        doctor=doctor,
        paciente=request.user,
    )

    if request.method == 'POST':
        form = MensajePrivadoForm(request.POST)
        if form.is_valid():
            MensajePrivado.objects.create(
                conversacion=conversacion,
                autor=request.user,
                cuerpo=form.cleaned_data['cuerpo'],
            )
            return redirect('accounts:chat_paciente', doctor_id=doctor.id)
    else:
        form = MensajePrivadoForm()

    mensajes = conversacion.mensajes.select_related('autor').order_by('creado')

    return render(
        request,
        'accounts/chat_paciente.html',
        {
            'conversacion': conversacion,
            'mensajes': mensajes,
            'form': form,
            'doctor': doctor,
        },
    )
