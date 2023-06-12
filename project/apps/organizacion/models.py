from django.db import models

# Create your models here.

class Region(models.Model):
    """
    Área de la cobertura de la organización protectora de animales.
    """
    nombre = models.CharField(max_length=30)

    class  Meta:
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'

    def __str__(self) -> str:
        return self.nombre
    

class Organizacion(models.Model):
    """
    Organizaciones protectoras de animales que poseen la responsabilidad del animal en tránsito encargadas de gestionar la adopción.
    """
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.BigIntegerField()
    direccion = models.CharField(max_length=50)
    region_id = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    class  Meta:
        verbose_name = 'organización'
        verbose_name_plural = 'organizaciones'

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Zona de cobertura: {self.region_id} "