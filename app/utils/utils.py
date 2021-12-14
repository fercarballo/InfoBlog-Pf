import logging

def paginar(obj: list, paginas_a_mostrar = 3, cuenta_posts = 0, pagina_elegida = 1, debug=False):
    
    '''Determinar la lista de páginas a mostrar según la cantidad de posts.
       Toma: Obj; Una lista que contiene todos los posts.
       Devuelve: Tupla; El primer elemento es la lista de los números entre 1 y la longitud de OBJ,
       el segundo elemento es una lista abreviada que contiene los 3 primeros números, y el número final.
       
       Keyword Arguments:
       paginas_a_mostrar: Default 3. Determina la cantidad de páginas a mostrar antes de colapsar la lista y agregar "...".
       cuenta_posts: Default 0. Indica la cantidad de posts totales, será útil para arreglar los numeros de paginación
       pagina_elegida: Default 1. Indica la página que solicitamos (page/n), será útil para arreglar los números de paginación.  
       debug: Default False. Loggea información el la consola con el nivel de prioridad INFO'''

    # TODO Agregar captura de search=?
    # TODO Changelog
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
    if not debug:
        logging.disable()

    logging.info("\nLlamada función paginar.")
    logging.info(f"Lista recibida: {obj}")
    logging.info(f"kwarg Páginas a mostrar: {paginas_a_mostrar}") 
    logging.info(f"kwarg Posts totales: {cuenta_posts}")       

        
    paginas = [x+1 for x in range(obj//4)]\
              if obj % 2 == 0\
              else [x+1 for x in range((obj//4)+1)]

    logging.info(f"Var 'paginas': {paginas}")

    if len(paginas) > paginas_a_mostrar and paginas[-1] - paginas[paginas_a_mostrar-1] >1:
        paginas_ab = [*paginas[:paginas_a_mostrar-1],
                      "...",
                      paginas[-1]]   

    else:
        paginas_ab = paginas

    logging.info(f"Var 'paginas_ab': {paginas_ab}\n")    

    return (paginas, paginas_ab)


def resolver_paginacion(*args):
    print(args)