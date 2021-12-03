from django.db import models
from app.categoria.models import Categoria

# Create your models here.
class Post(models.Model):    
    titulo = models.CharField('Título', 
                              max_length=100, 
                              null=False, 
                              blank=False)

    fecha_creacion = models.DateField('Fecha de creación', 
                                      auto_now=False, 
                                      auto_now_add=True)

    descripcion = models.CharField('Descripción', 
                                    max_length=255, 
                                    null=False, 
                                    blank=False)

    slug = models.SlugField('Slug', 
                            max_length=100, 
                            null=False, 
                            blank=False)

    cuerpo = models.TextField('Cuerpo', max_length=255)

    img = models.URLField(max_length=255, blank=True)

    estado = models.BooleanField('Publicado/No publicado', default=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.SET(0))
    # la forma mas facil de ocultar un post es poniéndole una categoría que no se muestre
    # Si no, la lógica para eliminar o cambiar un atributo se vuelve complicada, ya que
    # los atributos de los modelos no son atributos como tal, si no que son agregados por metaclasses
    # a una lista _meta.fields

    class Meta:
        ordering = ('fecha_creacion', )