
from DistribuidoraCarne import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.cache import cache
from django.http import HttpResponse

class LoginAttemptsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica si el usuario está intentando iniciar sesión
        if request.method == 'POST' and 'login' in request.path:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

            # Comprueba si el usuario existe y si ha excedido el límite de intentos
            if User.objects.filter(username=username).exists():
                cache_key = f'login_attempts_{username}'
                login_attempts = cache.get(cache_key, 0)
                if login_attempts >= settings.MAX_LOGIN_ATTEMPTS:
                    return HttpResponse("Acceso bloqueado. Has excedido el límite de intentos.")
                if not login(username=username, password=password):
                    login_attempts += 1
                    cache.set(cache_key, login_attempts, settings.LOGIN_TIMEOUT)

        response = self.get_response(request)
        return response
