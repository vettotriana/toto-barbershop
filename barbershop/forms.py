from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Barbershop, Book

# Formulario para crear o editar reservaciones, basado en el modelo Book.
class BookForm(ModelForm):
    class Meta:
        model = Book  # Especifica el modelo sobre el cual el formulario se basa.
        fields = ['barbershop', 'time', 'status']  # Campos del modelo a incluir en el formulario.

# Formulario para crear o editar información de una barbería, basado en el modelo Barbershop.
class BarbershopForm(ModelForm):
    class Meta:
        model = Barbershop  # Modelo base del formulario.
        fields = ['Barbershopname', 'phone', 'email', 'area', 'service']  # Campos a incluir.

# Formulario personalizado para crear usuarios, extendiendo UserCreationForm para incluir campos adicionales.
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User  # Modelo base del formulario, en este caso el modelo de usuario de Django.
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']  # Campos del formulario.

