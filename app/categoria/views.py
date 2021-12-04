from django.shortcuts import render
from .models import Categoria

def inicio_view(request):
    posts = Categoria.objects.filter(estado = True) #se filtra solo los post activos.
    return render(request, 'xxxxxx', {'xxxxxx': xxxxx})