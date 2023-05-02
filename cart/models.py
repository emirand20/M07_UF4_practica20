from django.db import models
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'