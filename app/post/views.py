from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.

def inicio_view(request):
    posts = Post.objects.filter(estado = True) #se filtra solo los post activos.
    return render(request, 'base/index.html', {'posts':posts})


def vista_post(request, post: str):
    '''Recibir la URL del post de la función obtener_url_absoluta y mostrarla.
       Toma: Una request y un String que represente la url del post.
       Devuelve: Render.
       Utiliza la función get_object_or_404 para buscar en Post, todos los resultados donde la slug
       sea igual a la que le pasamos y el estado sea Publicado. Si no se encuentra, levanta error 404.'''
    
    objeto_post = get_object_or_404(Post, slug=post)    
    
    return render(request, 'post/post_simple.html', {"post": objeto_post})
