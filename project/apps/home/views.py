from django.shortcuts import render
from .import views

#Para el login:

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "home/index.html", {"mensaje":f"Bienvenido {usuario}"})
    else:
        form = AuthenticationForm()
    return render(request, "home/login.html", {"form": form})