from django.db import models
from ..core.models import *


class Collection(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    miniatura = models.ImageField(
        upload_to='collection_thumbnails/', null=True, blank=True, default="card.png")

    def __str__(self):
        return self.nombre


class Card(models.Model):
    enunciado = models.TextField()
    respuesta = models.TextField()
    coleccion = models.ForeignKey(Collection, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
