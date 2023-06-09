from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    APTO_CHOICES = [(False, 'No'), (True, 'Sí')]
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    organizacion_id = models.ForeignKey("organizacion.Organizacion", on_delete=models.SET_NULL, null=True, verbose_name="Organización")
    sexo_id = models.ForeignKey(Sexo, on_delete=models.SET_NULL, null=True)
    tipo_animal_id = models.ForeignKey(TipoAnimal, on_delete=models.SET_NULL, null=True, verbose_name="Tipo de animal")
    observaciones = models.CharField(max_length=1000)
    foto1 = models.ImageField(upload_to='Animales_Fotos', null=True, blank = True)
    foto2 = models.ImageField(upload_to='Animales_Fotos', null=True, blank = True)
    foto3 = models.ImageField(upload_to='Animales_Fotos', null=True, blank = True)
    apto_perros = models.BooleanField(default=False, verbose_name="Apto para hogar con perros", choices=APTO_CHOICES)
    apto_gatos = models.BooleanField(default=False, verbose_name="Apto para hogar con gatos", choices=APTO_CHOICES)
    apto_infantes = models.BooleanField(default=False, verbose_name="Apto para hogar con niños", choices=APTO_CHOICES)
    castradx = models.BooleanField(default=False, verbose_name="Castradx", choices=APTO_CHOICES)
    vacunadx = models.BooleanField(default=False, verbose_name="Vacunadx", choices=APTO_CHOICES)
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de actualización")

    class  Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    def __str__(self) -> str:
        return self.nombre
    


class hogarTransito(models.Model):
    """
    Modelo para la creación del formulario de postulación de Hogar de Tránsito.
    """
    animal_id = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True, verbose_name="Animal")
    direccion = models.CharField(max_length=200, verbose_name="Localidad/Barrio")
    edad = models.IntegerField(verbose_name="Edad del interesadx")
    profesion = models.CharField(max_length=1000, verbose_name="Profesión (solo para conocerte más a vos y tus horarios) ")
    convivencia = models.CharField(max_length=1000, verbose_name="¿Vivís con alguien? Si es así, cuántas personas y edades.")
    vivienda  = models.CharField(max_length=1000, verbose_name="Tipo de vivienda: Casa/Departamento/PH/Otro...")
    espacio_libre  = models.CharField(max_length=1000, verbose_name="¿Tenés algún espacio libre?")
    animales_casa  = models.CharField(max_length=1000, verbose_name="¿Tenés animales en casa? Si es así, decinos cuántos, qué animales y edades...")
    class  Meta:
        verbose_name = 'hogar de tránsito'
        verbose_name_plural = 'hogares de tránsito'

    def __str__(self) -> str:
        return f"{self.animal_id}"