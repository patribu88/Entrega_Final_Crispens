from django.shortcuts import render
from . import models, forms
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 


# Create your views here.


def index(request: HttpResponse): 
    return render(request, "animal/index.html")


class AnimalList(ListView):
    model = models.Animal
    template_name = "animal/list.html"
    context_object_name = "animales"

class AnimalDetail(DetailView):
    model = models.Animal

class AnimalCreate(CreateView):
    model = models.Animal
    form_class = forms.AnimalForm
    success_url = reverse_lazy("animal:index")


class AnimalDelete(DeleteView):
    model = models.Animal
    success_url = reverse_lazy("animal:index")


class AnimalUpdate(UpdateView):
    model = models.Animal
    success_url = reverse_lazy("animal:animal_list")
    form_class = forms.AnimalForm

