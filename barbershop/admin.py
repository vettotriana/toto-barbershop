from django.contrib import admin
# Importa todos los modelos definidos en models.py del mismo directorio.
from .models import *

# Registra el modelo Customer en el sitio de administración de Django,
# permitiendo que los objetos Customer sean gestionados a través de la interfaz administrativa.
admin.site.register(Customer)

# Registra el modelo Barbershop en el sitio de administración de Django,
# habilitando la gestión de objetos Barbershop desde el panel administrativo.
admin.site.register(Barbershop)

# Registra el modelo Book en el sitio de administración de Django,
# posibilitando la administración de reservaciones (objetos Book) desde la interfaz de administración.
admin.site.register(Book)
