from django.shortcuts import render
from . import models, forms
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 


# Create your views here.


def index(request: HttpResponse): 
    return render(request, "animal/index.html")


class AnimalList(ListView):
    model = models.Animal
    context_object_name = "animales"

class AnimalCreate(CreateView):
    model = models.Animal
    form_class = forms.AnimalForm
    success_url = reverse_lazy("animal:index")


class OrganizacionDelete(DeleteView):
    model = models.Animal
    success_url = reverse_lazy("animal:index")


class OrganizacionUpdate(UpdateView):
    model = models.Animal
    success_url = reverse_lazy("animal:animal_list")
    form_class = forms.AnimalForm

