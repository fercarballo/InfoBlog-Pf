from django.db import models
from django.db.models.deletion import CASCADE
from app.post.models import Post
from app.usuarios.models import Usuarios
# Create your models here.


class Comentarios(models.Model):   
    post_id = models.ForeignKey(Post, on_delete=CASCADE)
    autor   = models.ForeignKey(Usuarios, on_delete=CASCADE)
    fecha   = models.DateField('Fecha de Creación',
                             auto_now=False,
                             auto_now_add=True)
    cuerpo  = models.TextField('Cuerpo', max_length=255)
    estado  = models.BooleanField(default=False)

    class Meta:
        ordering = ('fecha', )
