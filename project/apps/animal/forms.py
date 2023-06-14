from django import forms

from .models import Animal, TipoAnimal, Sexo


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = "__all__"

