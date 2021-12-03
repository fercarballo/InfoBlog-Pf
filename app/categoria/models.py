from functools import _Descriptor
from django.db import models
from django.db.models.fields.json import DataContains

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoría',
                              max_length=80, null=False, blank=False)
    estado = models.BooleanField(
        'Categoría Activada/Categoría Desactivada', default=True)


