from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
        'Título', max_length=100, null=False, blank=False)
    fecha_creacion = models.DateField(
        'Fecha de creación', auto_now=False, auto_now_add=True)
    descripcion = models.CharField(
        'Descripción', max_length=255, null=False, blank=False)
    slug = models.CharField('Slug', max_length=100, null=False, blank=False)
    cuerpo = models.TextField('Cuerpo', max_length=255)
    img = models.URLField(max_length=255, null=False, blank=False)
    estado = models.BooleanField('Publicado/No publicado', default=True)
    categoria = models.ForeignKey(Categoria, on_delete=SET(self.estado=False))

    class Meta:
        ordering = ('id__date_joined', )