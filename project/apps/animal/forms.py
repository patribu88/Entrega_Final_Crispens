from django import forms

from .models import Animal, hogarTransito


class AnimalForm(forms.ModelForm):

    """Formulario para cargar un animal para transitar."""
    class Meta:
        model = Animal
        fields = "__all__"

        widgets = {
            "apto_perros": forms.Select(attrs={"class": "form-control"}),
        }

class hogarTransitoForm(forms.ModelForm):
    """Formulario para postularse para transitar un animal."""
    class Meta:
        model = hogarTransito
        fields = "__all__"