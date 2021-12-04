from django import forms
from app.usuarios.models import Usuarios

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        widgets = {
        'contrasena': forms.PasswordInput(),
    }