from django.shortcuts import render
from .models import Post

# Create your views here.

def inicio_view(request):
    posts = Post.objects.all()
    return render(request, 'base/index.html', context={"posts":posts})