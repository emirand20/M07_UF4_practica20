from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=32)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre