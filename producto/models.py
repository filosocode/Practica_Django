from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
