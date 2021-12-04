from django.shortcuts import render
from .models import Post

# Create your views here.

def inicio_view(request):
    posts = Post.objects.filter(estado = True) #se filtra solo los post activos.
    return render(request, 'base/index.html', {'posts':posts})