from django.db import models


# Create your models here.
class Categoria(models.Model):    
    nombre = models.CharField('Nombre de la Categoría',
                              max_length=80, 
                              null=False, 
                              blank=False)
                              
    estado = models.BooleanField('Categoría Activada/Categoría Desactivada',
                                 default=True)

    def __str__(self) -> str:
        return self.nombre
