from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Comentarios(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=CASCADE)
    autor = models.ForeignKey(Usuario, on_delete=CASCADE)
    fecha = models.DateField(
        'Fecha de Creación', auto_now=False, auto_now_add=True)
    cuerpo = models.TextField('Cuerpo', max_length=255)
    estado = models.BooleanField(default=False)

    class Meta:
        ordering = ('id__date_joined', )

