from django import forms

from .models import Animal, hogarTransito


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = "__all__"

        widgets = {
            "apto_perros": forms.Select(attrs={"class": "form-control"}),
        }

class hogarTransitoForm(forms.ModelForm):
    class Meta:
        model = hogarTransito
        fields = "__all__"