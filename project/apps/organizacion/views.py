from django.shortcuts import render
from . import models, forms
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 


# Create your views here.


def index(request: HttpResponse): 
    return render(request, "organizacion/index.html")



class OrganizacionList(ListView):
    model = models.Organizacion
    context_object_name = "organizaciones"

class OrganizacionCreate(CreateView):
    model = models.Organizacion
    form_class = forms.OrganizacionForm
    success_url = reverse_lazy("organizacion:index")


class OrganizacionDelete(DeleteView):
    model = models.Organizacion
    success_url = reverse_lazy("organizacion:index")


class OrganizacionUpdate(UpdateView):
    model = models.Organizacion
    success_url = reverse_lazy("organizacion:organizacion_list")
    form_class = forms.OrganizacionForm


