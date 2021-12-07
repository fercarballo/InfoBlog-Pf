from django.shortcuts import get_object_or_404, render
from .models import Post


def inicio_view(request):
    '''Encargada de resolver la Request y decidir qué mostrar en base a la acción que toma el usuario.
       Si el usuario está buscando algo, se muestra "busqueda.html", de lo contrario, se muestra "index.html".
       
       Si "request" posee una clave no vacía "search", se procede a filtrar los posts basados en el valor de la misma
       y se establece la url a "post/busqueda.html".
       De lo contrario, se procede a buscar todos los posts y la url queda con su valor por defecto de "base/index.html".
       
       Esta implementación no es del todo correcta, está ligada fuertemente a la implementación de la barra de búsqueda 
       en el archivo "index.html", esta solución funciona solo si la barra se encuentra en ese archivo, 
       de lo contrario, habrá que crear una vista propia para la búsqueda.'''

    termino_busqueda = ""
    url = "base/index.html"

    if 'busqueda' in request.GET and request.GET['busqueda'] != "":
        termino_busqueda = request.GET['busqueda']
        url = "post/busqueda.html"
        
        posts = Post.objects.all().filter(titulo__icontains=termino_busqueda, estado=True)            
    
    else:        
        posts = Post.objects.filter(estado = True)

    return render(request, url, {'posts':posts, 'query':termino_busqueda})



def vista_post(request, post: str):
    '''Recibir la URL del post de la función obtener_url_absoluta y mostrarla.
       Toma: Una request y un String que represente la url del post.
       Devuelve: Render.
       Utiliza la función get_object_or_404 para buscar en Post, todos los resultados donde la slug
       sea igual a la que le pasamos y el estado sea Publicado. Si no se encuentra, levanta error 404.'''
    
    objeto_post = get_object_or_404(Post, slug=post)    
    
    return render(request, 'post/post_simple.html', {"post": objeto_post})
