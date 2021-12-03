from django.db import models
from django import forms

# Create your models here.
class Usuarios(forms.models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=100, null=False, blank=False)
    apellido = models.CharField('Apellido', max_length=100, null=False, blank=False)
    correo = models.EmailField('Correo electrónico', null=False, blank=False)
    contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
            model = Usuarios
            widgets = {
            'password': forms.PasswordInput(),
        }
            ordering = ('id__date_joined', )