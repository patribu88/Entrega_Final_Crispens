from django.shortcuts import render
from . import models, forms
from django.http import HttpRequest, HttpResponse
# Create your views here.


def index(request: HttpResponse): 
    return render(request, "organizacion/index.html")


from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 

class OrganizacionList(ListView):
    model = models.Organizacion
    template_name = "organizacion/organizacion_list.html"
    context_object_name = "organizaciones"

