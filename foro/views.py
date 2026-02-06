"""
Vistas del foro de discusion.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Tema
from accounts.models import CustomUser
from .forms import TemaForm, MensajeForm


def lista_temas(request):
    """
    Lista publica de temas del foro.
    """
    temas = Tema.objects.order_by('-creado')
    return render(request, 'foro/lista_temas.html', {'temas': temas})


@login_required
def nuevo_tema(request):
    """
    Crear un tema nuevo. Requiere usuario autenticado.
    """
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            tema = form.save(commit=False)
            tema.autor = request.user
            tema.save()
            return redirect('foro:detalle_tema', tema_id=tema.id)
    else:
        form = TemaForm()

    return render(request, 'foro/nuevo_tema.html', {'form': form})


def detalle_tema(request, tema_id):
    """
    Vista de un tema y sus mensajes.
    Permite responder si el usuario esta autenticado.
    """
    tema = get_object_or_404(Tema, id=tema_id)
    mensajes = tema.mensajes.select_related('autor').order_by('creado')
    doctor_respondio = mensajes.filter(autor__rol=CustomUser.ROLE_DOCTOR).exists()
    doctor_responder = (
        mensajes.filter(autor__rol=CustomUser.ROLE_DOCTOR).first().autor
        if doctor_respondio
        else None
    )

    if request.method == 'POST' and request.user.is_authenticated:
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.tema = tema
            mensaje.autor = request.user
            mensaje.save()
            return redirect('foro:detalle_tema', tema_id=tema.id)
    else:
        form = MensajeForm()

    return render(
        request,
        'foro/detalle_tema.html',
        {
            'tema': tema,
            'mensajes': mensajes,
            'form': form,
            'doctor_respondio': doctor_respondio,
            'doctor_responder': doctor_responder,
        },
    )
