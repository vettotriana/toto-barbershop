from django.http import HttpResponse
from django.shortcuts import redirect

# Decorador para restringir el acceso a usuarios no autenticados a ciertas vistas.
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('barbershop-home')  # Redirecciona a usuarios autenticados al inicio.
        else:
            return view_func(request, *args, **kwargs)  # Permite el acceso a usuarios no autenticados.
    return wrapper_func

# Decorador para permitir el acceso solo a usuarios con roles específicos.
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():  # Comprueba si el usuario pertenece a algún grupo.
                group = request.user.groups.all()[0].name
            if group == 'full' or group == 'clientes':
                return view_func(request, *args, **kwargs)  # Permite acceso si el usuario tiene el rol permitido.
            else:
                return HttpResponse('No estas autorizado a ver esta pagina contacta al servicio barberia de toto')  # Mensaje de no autorizado.
        return wrapper_func
    return decorator

