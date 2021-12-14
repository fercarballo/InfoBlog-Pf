from django.conf.urls import url
from django.shortcuts import get_object_or_404, render, redirect
from app.usuarios.models import Usuarios
from .models import Post
from django.core.paginator import Paginator
from app.utils.utils import paginar
from django.http.response import HttpResponseRedirect
from app.comentarios.forms import FormComentario
#-----------------------------------------
from .forms import CrearUsuarioForm
from django.contrib.auth import authenticate, login
#-----------------------------------------


def inicio_view(request):
    '''Encargada de resolver la Request y decidir qué mostrar en base a la acción que toma el usuario.
       Si el usuario está buscando algo, se muestra "busqueda.html", de lo contrario, se muestra "index.html".
       
       Si "request" posee una clave no vacía "search", se procede a filtrar los posts basados en el valor de la misma
       y se establece la url a "post/busqueda.html".
       De lo contrario, se procede a buscar todos los posts y la url queda con su valor por defecto de "base/index.html".
       
    '''

    posts = Post.objects.filter(estado = True, destacado=False)

    if 'busqueda' in request.GET and request.GET['busqueda'] != "":
        return HttpResponseRedirect(f"/search/{request.GET['busqueda']}")    
    p = Paginator(posts, 2)
    posts_paginados = [p.page(x+1).object_list for x in range(p.num_pages)]

    contexto = {
        "posts": posts,                      
        "paginas": posts_paginados,
        "numero_paginas": paginar(len(posts))[1]        
        }

    return render(request, "base/index.html" , contexto)


def vista_post(request, post: str):
    '''Recibir la URL del post de la función obtener_url_absoluta y mostrarla.
       Toma: Una request y un String que represente la url del post.
       Devuelve: Render.
       Utiliza la función get_object_or_404 para buscar en Post, todos los resultados donde la slug
       sea igual a la que le pasamos y el estado sea Publicado. Si no se encuentra, levanta error 404.'''
    
    objeto_post = get_object_or_404(Post, slug=post)
    comentarios = objeto_post.comentarios.filter(estado= True)   
    # Lógica comentarios, checkea si se hace una request POST, y de ahí, si el comentario es válido se lo guarda
    # Si no, simplemente se envía una instancia de FormComentario vacía para poder mostrarla en el template.
    comentario_nuevo = None
    if request.method == "POST":
        form_comentario= FormComentario(request.POST)
        if form_comentario.is_valid():
            comentario_nuevo = form_comentario.save(commit=False)
            comentario_nuevo.post_id = objeto_post
            comentario_nuevo.autor = Usuarios.objects.filter(nombre="admin")[0] # Usuario por defecto: admin. Esto cambiará a request.user.username cuando funcione el login
            comentario_nuevo.save()
            return HttpResponseRedirect("/"+objeto_post.slug)
    else:
        form_comentario = FormComentario()

    contexto={
        "post": objeto_post, 
        "comentarios": comentarios, 
        "comentario": comentario_nuevo,
        "forma_comentario": form_comentario
    }
    
    return render(request, 'post/post_simple.html', context=contexto)


def vista_paginada(request, *args, posts_in = None, **kwargs):
    '''
    Se encarga de mostrar los posts que deberían estar en cada número de página
    '''
    
    if 'busqueda' in request.GET and request.GET['busqueda'] != "":
        return HttpResponseRedirect(f"/search/{request.GET['busqueda']}")    
    
    if posts_in:
        if posts_in[0] == None:
            posts = []
        else:
            posts = posts_in
            
    else:
        if 'query' in kwargs:            
            posts = Post.objects.filter(estado=True, destacado=False, titulo__icontains=kwargs['query'])                  
        else:
            posts = Post.objects.filter(estado=True, destacado=False)

    posts_a_mostrar = posts[(kwargs["num"]-1)*4:]
    cantidad_posts = len(posts)    
    
    p = Paginator(posts_a_mostrar, 2)    
    posts_paginados = [p.page(x+1).object_list for x in range(p.num_pages)]
    
    contexto = {
        "pagina_solicitada": kwargs["num"],
        "paginas": posts_paginados,
        "numero_paginas": paginar(cantidad_posts, cuenta_posts=cantidad_posts, pagina_elegida= kwargs["num"])[1]
    }

    if 'query' in kwargs:
        contexto['query'] = kwargs['query']

    return render(request, "post/paginacion.html", context=contexto)


def vista_busqueda(request, **kwargs):
    
    posts_filtrados = Post.objects.all().filter(titulo__icontains=kwargs['query'])    
    
    if len(posts_filtrados) == 0:
        posts_filtrados = [None]

    if 'num' in kwargs:
        kwargs['num']
    else:
        kwargs["num"] = 1

    return vista_paginada(request, posts_in=posts_filtrados, num=kwargs['num'], query=kwargs['query'])


def registro(request):
    form = CrearUsuarioForm()
    if request.method == 'POST':
        formulario = CrearUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save() #guarda usuario 
            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request,user) #loguea al usuario recien creado
            return redirect('inicio') #redirige al index.html

    context = {'form':form}
    return render(request,'registration/register.html',context)
