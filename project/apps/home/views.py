from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .import views
from .import forms


#Para el login:

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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


# Vista de registro
def register(request):
    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                return render(request,"home/index.html" ,  {"mensaje":"Usuario Creado :)"})

    else:
        form = forms.CustomUserCreationForm()      
    return render(request,"home/registro.html" ,  {"form":form})

    