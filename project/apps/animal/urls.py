from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("animal/list/", views.AnimalList.as_view(), name="animal_list"),
    path("animal/create/", staff_member_required(views.AnimalCreate.as_view()), name="animal_create"),
]