from django.urls import path
from . import views

urlpatterns = [
    # Ruta para crear una nueva reserva.
    path('create_book/', views.createBook, name='create_book'),
    # Ruta para crear una nueva barbería.
    path('create_barber/', views.createBarbershop, name='create_barber'),
    # Ruta para la página de registro de usuarios.
    path('register/', views.registerPage, name='register'),
    # Ruta para la página de inicio de sesión.
    path('login/', views.loginPage, name='login'),
    # Ruta para cerrar sesión.
    path('logout/', views.logoutUser, name='logout'),
    # Ruta para visualizar las reservaciones.
    path('bookings/', views.Bookings, name='bookings'),
    # Ruta para la página principal de la barbería.
    path('', views.home, name='barbershop-home'),
    # Ruta para la página "Acerca de".
    path('about/', views.about, name='barbershop-about'),
    # Rutas comentadas que pueden ser habilitadas para funcionalidades adicionales.
    #path('customer/<str:ok>/', views.customer, name='customer'),
    #path('barbershop/<str:pk>/', views.searchbarber, name='barbershop-searchbarber'),
]

