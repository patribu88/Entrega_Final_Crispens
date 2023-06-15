from django.shortcuts import render
from . import models, forms
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 


# Create your views here.

# Vista para ir a página principal de la app de organizaciones.
def index(request: HttpResponse): 
    return render(request, "organizacion/index.html")


# Vista para ir a al listado de organizaciones disponibles.
class OrganizacionList(ListView):
    model = models.Organizacion
    context_object_name = "organizaciones"

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Organizacion.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Organizacion.objects.all()
        return object_list

# Vista para crear una nueva organización, solo disponible para administrador.

class OrganizacionCreate(CreateView):
    model = models.Organizacion
    form_class = forms.OrganizacionForm
    success_url = reverse_lazy("organizacion:index")

# Vista para eliminar una organización, solo disponible para administrador.
class OrganizacionDelete(DeleteView):
    model = models.Organizacion
    success_url = reverse_lazy("organizacion:index")

# Vista para actualizar una organización, solo disponible para administrador.
class OrganizacionUpdate(UpdateView):
    model = models.Organizacion
    success_url = reverse_lazy("organizacion:organizacion_list")
    form_class = forms.OrganizacionForm


