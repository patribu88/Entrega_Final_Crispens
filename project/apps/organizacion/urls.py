from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("organizacion/list/", views.OrganizacionList.as_view(), name="organizacion_list"),
    path("organizacion/create/", staff_member_required(views.OrganizacionCreate.as_view()), name="organizacion_create"),
    path("organizacion/delete/<int:pk>", staff_member_required(views.OrganizacionDelete.as_view()), name="organizacion_delete"),
    path("organizacion/update/<int:pk>", staff_member_required(views.OrganizacionUpdate.as_view()), name="organizacion_update"),
]