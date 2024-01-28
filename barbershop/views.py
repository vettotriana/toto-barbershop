from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import *
from .models import *
from .forms import CreateUserForm, BarbershopForm, BookForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group, User

# Vista para la página de inicio. Muestra todas las barberías registradas.
def home(request):
    barbershops = Barbershop.objects.all()
    return render(request, 'barbershop/home.html', {'barbershops':barbershops})

# Vista para la página "Acerca de". Muestra información general.
def about(request):
    return render(request, 'barbershop/about.html', {'title': 'About'})

# Vista para la página de registro. Permite a los usuarios registrarse.
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(user=user)
            messages.success(request, 'Cuenta creada para ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'barbershop/register.html', context)

# Vista para crear una nueva barbería. Solo accesible para usuarios autenticados con roles permitidos.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer'])
def createBarbershop(request):
    form = BarbershopForm()
    if request.method == 'POST':
        form = BarbershopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('barbershop-home')
    context = {'form':form}
    return render(request, 'barbershop/create_barber.html', context)

# Vista para crear una nueva reserva. Solo accesible para usuarios autenticados con roles permitidos.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer'])
def createBook(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('barbershop-home')
    context = {'form':form}
    return render(request, 'barbershop/book_form.html', context)

# Vista para la página de inicio de sesión. Permite a los usuarios iniciar sesión.
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('barbershop-home')
    context = {}
    return render(request, 'barbershop/login.html', context)

# Vista para mostrar las reservaciones del usuario. Solo accesible para usuarios autenticados con roles permitidos.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer'])
def Bookings(request):
    bookings = Book.objects.last()
    context = {'bookings': bookings}
    return render(request, 'barbershop/bookings.html', context)

# Vista para cerrar sesión. Redirecciona a la página de inicio de sesión tras cerrar sesión.
def logoutUser(request):
    logout(request)
    return redirect('login')
