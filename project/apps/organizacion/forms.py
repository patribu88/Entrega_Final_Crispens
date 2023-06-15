from django import forms

from .models import Organizacion, Region


class OrganizacionForm(forms.ModelForm):
    """Form para crer una nueva organización o actualizarla."""
    class Meta:
        model = Organizacion
        fields = "__all__"
