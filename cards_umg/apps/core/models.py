from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    icono = models.ImageField(upload_to='categorias/', height_field=None, width_field=None, max_length=None)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre