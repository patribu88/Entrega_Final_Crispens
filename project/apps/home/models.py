from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    class  Meta:
        verbose_name = 'avatar'
        verbose_name_plural = 'avatares'
    def __str__(self):
        return f"{self.user} - {self.imagen}"
