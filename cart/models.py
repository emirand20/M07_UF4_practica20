from django.db import models
from catalog.models import Producto
# Create your models here.

class Carrito(models.Model):
    productos = models.ManyToManyField(Producto)

    def total(self):
        return sum(producto.precio for producto in self.productos.all())
    
    '''def __str__(self):
        return f'{self.nombre} -> {self.precio}'''