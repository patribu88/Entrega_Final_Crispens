from django import forms

from .models import Organizacion, Region


class OrganizacionForm(forms.ModelForm):
    class Meta:
        model = Organizacion
        fields = "__all__"
