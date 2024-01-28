"""Configuración de URLs para ebarber

La lista `urlpatterns` direcciona las URLs a las vistas. Para más información, por favor consulta:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Ejemplos:
Vistas basadas en funciones
    1. Agrega una importación: from my_app import views
    2. Agrega una URL a urlpatterns: path('', views.home, name='home')
Vistas basadas en clases
    1. Agrega una importación: from other_app.views import Home
    2. Agrega una URL a urlpatterns: path('', Home.as_view(), name='home')
Incluyendo otra configuración de URL
    1. Importa la función include(): from django.urls import include, path
    2. Agrega una URL a urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el sitio administrativo.
    path('', include('barbershop.urls'))  # Incluye las URLs de la aplicación barbershop-toto.
]

