from django.apps import AppConfig

# Configuración de la aplicación 'barbershop' para toto dentro del proyecto Django.
# Esta clase hereda de AppConfig, que es utilizada por Django para almacenar
# la configuración de una aplicación específica. Al definir la propiedad 'name',
# se establece el nombre de la aplicación que Django reconocerá para configuraciones
# futuras, como la inclusión en la lista de INSTALLED_APPS del archivo settings.py.

class BarbershopConfig(AppConfig):
    name = 'barbershop'
