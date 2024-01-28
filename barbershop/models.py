from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Obtener el modelo de usuario actualmente activo.
User = get_user_model()

# Modelo para representar a los clientes de la barbería/peluquería.
class Customer(models.Model):
    # Relación uno a uno con el modelo de usuario para extender sus propiedades.
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)  # Nombre del cliente.
    phone = models.CharField(max_length=100, null=True)  # Teléfono del cliente.
    profile_pic = models.ImageField(null=True, blank=True)  # Imagen de perfil del cliente, opcional.
    email = models.CharField(max_length=100, null=True)  # Email del cliente.

    def __str__(self):
        return self.name  # Devuelve el nombre del cliente como representación en cadena.


# Modelo para representar las barberías/peluquerías.
class Barbershop(models.Model):
    # Categorías de servicios ofrecidos.
    CATEGORY = (
    ('Solo Cortes', 'Solo Cortes'),
    ('Servicios Completos', 'Servicios Completos'),
    ('Corte y Barba', 'Corte y Barba'),
    ('Tratamientos Capilares', 'Tratamientos Capilares'),
    ('Coloración', 'Coloración'),
    ('Estilismo', 'Estilismo'),
    ('Paquetes VIP', 'Paquetes VIP'),
    ('Servicios para Niños', 'Servicios para Niños'),
)

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  # Vinculación con el usuario.
    Barbershopname = models.CharField(max_length=100, null=True)  # Nombre de la barbería/peluquería.
    phone = models.CharField(max_length=100, null=True)  # Teléfono de contacto.
    email = models.CharField(max_length=100, null=True)  # Email de contacto.
    area = models.CharField(max_length=100, null=True)  # Área o ubicación.
    service = models.CharField(max_length=100, null=True, choices=CATEGORY)  # Servicio ofrecido, seleccionado de las categorías.

    def __str__(self):
        return self.Barbershopname  # Devuelve el nombre de la barbería/peluquería como representación en cadena.


# Modelo para representar las reservaciones de servicios.
class Book(models.Model):
    # Estados de la reservación, reflejando distintos servicios y sus costos.
    STATUS = (
    ('Corte de Cabello y Afeitado 10$', 'Corte de Cabello y Afeitado 10$'),
    ('Corte de Cabello y Recorte 8$', 'Corte de Cabello y Recorte 8$'),
    ('Corte de Cabello 7$', 'Corte de Cabello 7$'),
    ('Coloración de Cabello 20$', 'Coloración de Cabello 20$'),
    ('Tratamiento Capilar 15$', 'Tratamiento Capilar 15$'),
    ('Lavado y Peinado 12$', 'Lavado y Peinado 12$'),
    ('Barba Detallada 9$', 'Barba Detallada 9$'),
)

    # Horarios disponibles para reservación.
    TIME = (
    ('Mañana Temprano (6:00 - 8:00)', 'Mañana Temprano (6:00 - 8:00)'),
    ('Mañana (8:00 - 12:00)', 'Mañana (8:00 - 12:00)'),
    ('Mediodía (12:00 - 14:00)', 'Mediodía (12:00 - 14:00)'),
    ('Tarde (14:00 - 18:00)', 'Tarde (14:00 - 18:00)'),
    ('Tarde Noche (18:00 - 21:00)', 'Tarde Noche (18:00 - 21:00)'),
    ('Noche (21:00 - 23:00)', 'Noche (21:00 - 23:00)'),
    ('Horario Extendido/Nocturno (23:00 - 02:00)', 'Horario Extendido/Nocturno (23:00 - 02:00)'),
)

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)  # Cliente que realiza la reservación.
    barbershop = models.ForeignKey(Barbershop, null=True, on_delete=models.SET_NULL)  # Barbería/peluquería reservada.
    date_created = models.DateTimeField(auto_now_add=True, null=True)  # Fecha de creación de la reservación.
    time = models.CharField(max_length=200, null=True, choices=TIME)  # Horario seleccionado para la reservación.
    status = models.CharField(max_length=200, null=True, choices=STATUS)  # Estado de la reservación, indicando el servicio seleccionado.
