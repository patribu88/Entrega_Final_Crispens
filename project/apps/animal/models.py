from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# Create your models here.

class TipoAnimal(models.Model):
    """
    Tipo de animal disponible para transitar.
    """
    TipoAnimal = models.CharField(max_length=30)

    class  Meta:
        verbose_name = 'Tipo de Animal'
        verbose_name_plural = 'Tipos de animales'

    def __str__(self) -> str:
        return self.TipoAnimal

  
class Sexo(models.Model):
    """
    Sexo de los animales disponibles para transitar.
    """
    sexo = models.CharField(max_length=30)

    class  Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'

    def __str__(self) -> str:
        return self.sexo
    
class Animal(models.Model):
    """
    Animal disponible para transitar hasta su adopción definitiva.
    """
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    organizacion_id = models.ForeignKey("organizacion.Organizacion", on_delete=models.SET_NULL, null=True)
    sexo_id = models.ForeignKey(Sexo, on_delete=models.SET_NULL, null=True)
    tipo_animal_id = models.ForeignKey(TipoAnimal, on_delete=models.SET_NULL, null=True)
    personalidad = models.CharField(max_length=300)
    foto = models.ImageField(upload_to='Animales_Fotos', null=True, blank = True)

    class  Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}"