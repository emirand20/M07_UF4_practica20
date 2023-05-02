from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length = 100)
    precio = models.DecimalField('Precio',max_digits=10, decimal_places=2)

    def __str__(self):
        return  '{0},{1}'.format(self.nombre, self.precio)