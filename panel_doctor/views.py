"""
Panel privado para el doctor.
Muestra todos los mensajes y temas recibidos.
"""
from django.shortcuts import render, redirect, get_object_or_404
from accounts.decorators import require_role
from accounts.models import CustomUser, ConversacionPrivada, MensajePrivado
from accounts.forms import MensajePrivadoForm
from foro.models import Tema, Mensaje


@require_role(CustomUser.ROLE_DOCTOR)
def dashboard(request):
    """
    Panel del doctor con resumen de actividad.
    """
    temas = Tema.objects.order_by('-creado')[:20]
    mensajes = Mensaje.objects.order_by('-creado')[:30]

    conversaciones = (
        ConversacionPrivada.objects.filter(doctor=request.user)
        .select_related('paciente', 'tema')
        .order_by('-creado')
    )

    return render(
        request,
        'panel_doctor/dashboard.html',
        {
            'temas': temas,
            'mensajes': mensajes,
            'conversaciones': conversaciones,
        },
    )


@require_role(CustomUser.ROLE_DOCTOR)
def chat_doctor(request, conversacion_id):
    """
    Chat privado visto por el doctor.
    """
    conversacion = get_object_or_404(
        ConversacionPrivada,
        id=conversacion_id,
        doctor=request.user,
    )

    if request.method == 'POST':
        form = MensajePrivadoForm(request.POST)
        if form.is_valid():
            MensajePrivado.objects.create(
                conversacion=conversacion,
                autor=request.user,
                cuerpo=form.cleaned_data['cuerpo'],
            )
            return redirect('panel_doctor:chat_doctor', conversacion_id=conversacion.id)
    else:
        form = MensajePrivadoForm()

    mensajes = conversacion.mensajes.select_related('autor').order_by('creado')

    return render(
        request,
        'panel_doctor/chat_doctor.html',
        {
            'conversacion': conversacion,
            'mensajes': mensajes,
            'form': form,
        },
    )
