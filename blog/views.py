"""
Vistas del sitio publico.
"""
from django.shortcuts import render, get_object_or_404, redirect
from accounts.decorators import require_role
from accounts.models import CustomUser
from .forms import PostForm
from .models import Post


def home(request):
    """
    Home/landing con informacion del doctor y resumen del blog.
    """
    posts = Post.objects.filter(publicado=True).order_by('-creado')[:3]
    return render(request, 'blog/home.html', {'posts': posts})


def post_list(request):
    """
    Lista de entradas del blog.
    """
    posts = Post.objects.filter(publicado=True).order_by('-creado')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, slug):
    """
    Detalle de una entrada.
    """
    post = get_object_or_404(Post, slug=slug, publicado=True)
    return render(request, 'blog/post_detail.html', {'post': post})


@require_role(CustomUser.ROLE_DOCTOR)
def doctor_post_list(request):
    """
    Lista de posts para el panel del doctor.
    """
    posts = Post.objects.order_by('-creado')
    return render(request, 'panel_doctor/blog_list.html', {'posts': posts})


@require_role(CustomUser.ROLE_DOCTOR)
def doctor_post_create(request):
    """
    Crear post desde el panel del doctor.
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('panel_doctor:blog')
    else:
        form = PostForm()

    return render(request, 'panel_doctor/blog_form.html', {'form': form})


@require_role(CustomUser.ROLE_DOCTOR)
def doctor_post_edit(request, post_id):
    """
    Editar post desde el panel del doctor.
    """
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('panel_doctor:blog')
    else:
        form = PostForm(instance=post)

    return render(request, 'panel_doctor/blog_form.html', {'form': form, 'post': post})


@require_role(CustomUser.ROLE_DOCTOR)
def doctor_post_delete(request, post_id):
    """
    Eliminar post desde el panel del doctor.
    """
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('panel_doctor:blog')

    return render(request, 'panel_doctor/blog_confirm_delete.html', {'post': post})
