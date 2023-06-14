from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("animal/list/", views.AnimalList.as_view(), name="animal_list"),
    path("animal/detail/<int:pk>", views.AnimalDetail.as_view(), name="animal_detail"),
    path("animal/create/", staff_member_required(views.AnimalCreate.as_view()), name="animal_create"),
    path("animal/delete/<int:pk>", staff_member_required(views.AnimalDelete.as_view()), name="animal_delete"),
    path("animal/update/<int:pk>", staff_member_required(views.AnimalUpdate.as_view()), name="animal_update"),
]