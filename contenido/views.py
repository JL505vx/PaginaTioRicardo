"""
Vistas publicas y privadas del contenido.
"""
from django.shortcuts import render, redirect, get_object_or_404
from accounts.decorators import require_role
from accounts.models import CustomUser
from .models import Seccion, Recurso
from .forms import SeccionForm, RecursoForm
from blog.models import Post


def _contenido_para_blog(recurso: Recurso) -> tuple[str, str]:
    """
    Genera resumen y contenido para un post del blog basado en el recurso.
    """
    resumen = recurso.descripcion or 'Recurso informativo publicado por el doctor.'
    contenido = ''

    if recurso.tipo == Recurso.TIPO_VIDEO and recurso.url_video:
        contenido = f'Video recomendado: {recurso.url_video}'
    elif recurso.archivo:
        contenido = f'Recurso descargable disponible: {recurso.archivo.url}'
    elif recurso.tipo == Recurso.TIPO_TEXTO and recurso.texto:
        contenido = recurso.texto
    else:
        contenido = recurso.descripcion or 'Contenido informativo.'

    return resumen, contenido


def lista_publica(request):
    """
    Biblioteca publica para pacientes/visitantes.
    """
    secciones = Seccion.objects.prefetch_related('recursos').all()
    recursos = Recurso.objects.filter(publicado=True)
    return render(
        request,
        'contenido/recursos_list.html',
        {'secciones': secciones, 'recursos': recursos},
    )


@require_role(CustomUser.ROLE_DOCTOR)
def lista_contenido_doctor(request):
    """
    Panel del doctor para administrar contenido.
    """
    secciones = Seccion.objects.prefetch_related('recursos').all()
    recursos = Recurso.objects.all()
    return render(
        request,
        'panel_doctor/contenido_list.html',
        {'secciones': secciones, 'recursos': recursos},
    )


@require_role(CustomUser.ROLE_DOCTOR)
def crear_recurso_doctor(request):
    """
    Crear un recurso nuevo.
    """
    if request.method == 'POST':
        form = RecursoForm(request.POST, request.FILES)
        if form.is_valid():
            recurso = form.save(commit=False)
            recurso.creado_por = request.user
            recurso.save()

            # Publicar automaticamente en el blog solo si el doctor lo decide
            if recurso.publicar_en_blog:
                resumen, contenido = _contenido_para_blog(recurso)
                if recurso.blog_post:
                    recurso.blog_post.titulo = recurso.titulo
                    recurso.blog_post.resumen = resumen
                    recurso.blog_post.contenido = contenido
                    recurso.blog_post.publicado = True
                    recurso.blog_post.save()
                else:
                    post = Post.objects.create(
                        titulo=recurso.titulo,
                        resumen=resumen,
                        contenido=contenido,
                        autor=request.user,
                        publicado=True,
                    )
                    recurso.blog_post = post
                    recurso.save(update_fields=['blog_post'])
            else:
                if recurso.blog_post:
                    recurso.blog_post.publicado = False
                    recurso.blog_post.save()

            return redirect('panel_doctor:contenido')
    else:
        form = RecursoForm()

    return render(request, 'panel_doctor/contenido_form.html', {'form': form})


@require_role(CustomUser.ROLE_DOCTOR)
def crear_seccion_doctor(request):
    """
    Crear una seccion nueva.
    """
    if request.method == 'POST':
        form = SeccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('panel_doctor:contenido')
    else:
        form = SeccionForm()

    return render(request, 'panel_doctor/contenido_seccion_form.html', {'form': form})


@require_role(CustomUser.ROLE_DOCTOR)
def editar_recurso_doctor(request, recurso_id):
    """
    Editar un recurso existente.
    """
    recurso = get_object_or_404(Recurso, id=recurso_id)

    if request.method == 'POST':
        form = RecursoForm(request.POST, request.FILES, instance=recurso)
        if form.is_valid():
            recurso = form.save(commit=False)
            recurso.creado_por = recurso.creado_por or request.user
            recurso.save()

            if recurso.publicar_en_blog:
                resumen, contenido = _contenido_para_blog(recurso)
                if recurso.blog_post:
                    recurso.blog_post.titulo = recurso.titulo
                    recurso.blog_post.resumen = resumen
                    recurso.blog_post.contenido = contenido
                    recurso.blog_post.publicado = True
                    recurso.blog_post.save()
                else:
                    post = Post.objects.create(
                        titulo=recurso.titulo,
                        resumen=resumen,
                        contenido=contenido,
                        autor=request.user,
                        publicado=True,
                    )
                    recurso.blog_post = post
                    recurso.save(update_fields=['blog_post'])
            else:
                if recurso.blog_post:
                    recurso.blog_post.publicado = False
                    recurso.blog_post.save()

            return redirect('panel_doctor:contenido')
    else:
        form = RecursoForm(instance=recurso)

    return render(
        request,
        'panel_doctor/contenido_form.html',
        {'form': form, 'recurso': recurso},
    )


@require_role(CustomUser.ROLE_DOCTOR)
def eliminar_recurso_doctor(request, recurso_id):
    """
    Eliminar un recurso.
    """
    recurso = get_object_or_404(Recurso, id=recurso_id)

    if request.method == 'POST':
        if recurso.blog_post:
            recurso.blog_post.delete()
        recurso.delete()
        return redirect('panel_doctor:contenido')

    return render(
        request,
        'panel_doctor/contenido_confirm_delete.html',
        {'recurso': recurso},
    )


@require_role(CustomUser.ROLE_DOCTOR)
def editar_seccion_doctor(request, seccion_id):
    """
    Editar una seccion existente.
    """
    seccion = get_object_or_404(Seccion, id=seccion_id)

    if request.method == 'POST':
        form = SeccionForm(request.POST, instance=seccion)
        if form.is_valid():
            form.save()
            return redirect('panel_doctor:contenido')
    else:
        form = SeccionForm(instance=seccion)

    return render(
        request,
        'panel_doctor/contenido_seccion_form.html',
        {'form': form, 'seccion': seccion},
    )


@require_role(CustomUser.ROLE_DOCTOR)
def eliminar_seccion_doctor(request, seccion_id):
    """
    Eliminar una seccion.
    """
    seccion = get_object_or_404(Seccion, id=seccion_id)

    if request.method == 'POST':
        seccion.delete()
        return redirect('panel_doctor:contenido')

    return render(
        request,
        'panel_doctor/contenido_seccion_confirm_delete.html',
        {'seccion': seccion},
    )
