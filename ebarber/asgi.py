"""
Configuración ASGI para el proyecto ebarber-toto.

Expone el llamable ASGI como una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo, consulta
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Establece el módulo de configuración predeterminado de Django para el proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebarber.settings')

# Obtiene la aplicación ASGI para el proyecto.
application = get_asgi_application()
