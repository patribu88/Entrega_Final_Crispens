from django.shortcuts import render
from . import models, forms
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 


# Lleva a la vista principal de la App de Animales.
def index(request: HttpResponse): 
    return render(request, "animal/index.html")

#Permite ver el listado de todos los animales disponibles y buscar por nombre de animal
class AnimalList(ListView):
    model = models.Animal
    template_name = "animal/list.html"
    context_object_name = "animales"

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Animal.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Animal.objects.all()
        return object_list   


#Vista que permite ver con mayor detalle las características del animal.

class AnimalDetail(DetailView):
    model = models.Animal

#Vista que permite crear un nuevo registro para la base de datos de animales. Solo los administradores pueden acceder.
class AnimalCreate(CreateView):
    model = models.Animal
    form_class = forms.AnimalForm
    success_url = reverse_lazy("animal:index")

#Vista que permite eliminar un registro en la base de datos de animales. Solo los administradores pueden acceder.

class AnimalDelete(DeleteView):
    model = models.Animal
    success_url = reverse_lazy("animal:index")

#Vista que permite actualizar un registro en la base de datos de animales. Solo los administradores pueden acceder.

class AnimalUpdate(UpdateView):
    model = models.Animal

    success_url = reverse_lazy("animal:animal_list")
    form_class = forms.AnimalForm

    
#formulario para que usuarios puedan postularse a transitar un animal en particular.

class hogarTransitoCreate(CreateView):
    model = models.hogarTransito
    form_class = forms.hogarTransitoForm
    success_url = reverse_lazy("animal:index")