import logging
from functools import wraps
import time

def temporizar(func):
    """Print the runtime of the decorated function"""
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        tiempo_comienzo = time.perf_counter()
        valor = func(*args, **kwargs)
        tiempo_final = time.perf_counter()      
        tiempo_total = tiempo_final - tiempo_comienzo    
        logging.info(f"Función {func.__name__!r} corrió en {tiempo_total:.4f} segundos.")
        return valor
    return wrapper_timer

@temporizar
def paginar(obj: list, paginas_a_mostrar = 3, cuenta_posts = 0, pagina_elegida = 1, debug=False):
    
    '''Determinar la lista de páginas a mostrar según la cantidad de posts.
       Toma: Obj; Una lista que contiene todos los posts.
       Devuelve: Tupla; El primer elemento es la lista de los números entre 1 y la longitud de OBJ,
       el segundo elemento es una lista abreviada que contiene los 3 primeros números, y el número final.
       
       Keyword Arguments:
       paginas_a_mostrar: Default 3. Determina la cantidad de páginas a mostrar antes de colapsar la lista y agregar "...".
       cuenta_posts: Default 0. Indica la cantidad de posts totales. Solamente útil a modo de información
       pagina_elegida: Default 1. Indica la página que solicitamos (page/n).  
       debug: Default False. Loggea información el la consola con el nivel de prioridad INFO'''

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

    if pagina_elegida > 1:
        paginas_ab = [*paginas[pagina_elegida-2:pagina_elegida+1]]
    else:
        paginas_ab = [*paginas[:pagina_elegida+2]]

    if paginas_ab[0] - 1 > 1:
        paginas_ab = [1,
                      "...",
                      *paginas_ab]

    elif paginas_ab[0] - 1 == 1:
        paginas_ab = [1, *paginas_ab]

    if paginas[-1] - paginas_ab[-1] > 1:
        paginas_ab = [*paginas_ab,
                      "...",
                      paginas[-1]]
    elif paginas[-1] - paginas_ab[-1] == 1:
        paginas_ab = [1, *paginas_ab[1:], paginas[-1]]

    logging.info(f"Var 'paginas_ab': {paginas_ab}\n")    

    return (paginas, paginas_ab)


# def test_paginar(cantidad_posts, pagina_elegida):

#     paginas = [x+1 for x in range(cantidad_posts//4)]\
#               if cantidad_posts % 2 == 0\
#               else [x+1 for x in range((cantidad_posts//4)+1)]    

#     if pagina_elegida > 1:
#         paginas_ab = [*paginas[pagina_elegida-2:pagina_elegida+1]]
#     else:
#         paginas_ab = [*paginas[:pagina_elegida+2]]

#     if paginas_ab[0] - 1 > 1:
#         paginas_ab = [1,
#                       "...",
#                       *paginas_ab]

#     elif paginas_ab[0] - 1 == 1:
#         paginas_ab = [1, *paginas_ab]

#     if paginas[-1] - paginas_ab[-1] > 1:
#         paginas_ab = [*paginas_ab,
#                       "...",
#                       paginas[-1]]
#     elif paginas[-1] - paginas_ab[-1] == 1:
#         paginas_ab = [1, *paginas_ab[1:], paginas[-1]]
    
    

#     print(f"""\n\tVariable cantidad_posts: {cantidad_posts}.
#         Variable pagina_elegida: {pagina_elegida}
#         Paginas abreviadas: {paginas_ab}.
#         Paginas totales: {paginas}\n""")
#     return paginas_ab, paginas


# if __name__ == "__main__":
    
#     for i in range(1, 6):
#         test_paginar(20, i)