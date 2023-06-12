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
    template_name = "organizacion/organizacion_list.html"
    context_object_name = "organizaciones"

class OrganizacionCreate(CreateView):
    model = models.Organizacion
    template_name = "organizacion/organizacion_form.html"
    form_class = forms.OrganizacionForm
    success_url = reverse_lazy("organizacion:index")