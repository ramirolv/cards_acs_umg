from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    icono = models.ImageField(upload_to='categorias/', height_field=None, width_field=None, max_length=None)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# Definir una función para eliminar la imagen asociada a la categoría antes de que se elimine la categoría
@receiver(pre_delete, sender=Categoria)
def eliminar_imagen_categoria(sender, instance, **kwargs):
    # Asegúrate de que haya una imagen asociada antes de intentar eliminarla
    if instance.icono:
        instance.icono.delete()

# Definir una función para eliminar la imagen anterior si se cambia por otra
@receiver(pre_save, sender=Categoria)
def eliminar_imagen_anterior(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        # Recupera la categoría existente
        categoria_existente = Categoria.objects.get(pk=instance.pk)
        # Comprueba si la imagen se ha cambiado
        if categoria_existente.icono and categoria_existente.icono != instance.icono:
            # Elimina la imagen anterior
            categoria_existente.icono.delete()
    except Categoria.DoesNotExist:
        return False