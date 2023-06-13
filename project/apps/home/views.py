from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .import views
from .import forms
from .import models


#Para el login:

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    return render(request, 'home/index.html')


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


#Editar perfil

@login_required
def editarPerfil(request):

    #Instancia del login
    usuario = request.user

    if request.method == 'POST':
        miFormulario = forms.UserEditForm(request.POST)
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            
            usuario.save()
            
            return render(request,"home/index.html" , {"mensaje":"Usuario Modificado :)"})
    else:
        miFormulario = forms.UserEditForm(initial={'email': usuario.email})

    return render(request, "home/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
    