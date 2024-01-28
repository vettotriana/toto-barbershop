"""
Configuración WSGI para el proyecto ebarber.

Expone el llamable WSGI como una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Establece el módulo de configuración por defecto de Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebarber.settings')

# Obtiene la aplicación WSGI para el proyecto.
application = get_wsgi_application()
