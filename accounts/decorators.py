"""
Decoradores de acceso basados en rol.
"""
from django.contrib import messages
from django.shortcuts import redirect


def require_role(role):
    """
    Bloquea la vista si el usuario no tiene el rol indicado.
    """

    def decorator(view_func):
        def _wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('accounts:login_paciente')

            if getattr(request.user, 'rol', None) != role:
                messages.error(request, 'No tienes permisos para ver esta pagina.')
                # Redirige al inicio publico del blog (ruta con nombre correcto)
                return redirect('blog:home')

            return view_func(request, *args, **kwargs)

        return _wrapped

    return decorator
