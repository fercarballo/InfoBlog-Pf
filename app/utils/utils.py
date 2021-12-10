import logging

def paginar(obj: list, paginas_a_mostrar = 3, debug=False):
    
    '''Determinar la lista de páginas a mostrar según la cantidad de posts.
       Toma: Obj; Una lista que contiene todos los posts.
       Devuelve: Tupla; El primer elemento es la lista de los números entre 1 y la longitud de OBJ,
       el segundo elemento es una lista abreviada que contiene los 3 primeros números, y el número final.
       
       Keyword Arguments:
       paginas_a_mostrar: Defalut 3. Determina la cantidad de páginas a mostrar antes de colapsar la lista y agregar "...".
       debug: Default False. Loggea información el la consola con el nivel de prioridad INFO'''

    
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
    if not debug:
        logging.disable()

    logging.info("\nLlamada función paginar.")
    logging.info(f"Lista recibida: {obj}")
    logging.info(f"Páginas a mostrar: {paginas_a_mostrar}")        

        
    paginas = [x+1 for x in range(len(obj)//2)]\
              if len(obj) % 2 == 0\
              else [x+1 for x in range((len(obj)//2)+1)]
    
    logging.info(f"Var 'paginas': {paginas}")

    if len(paginas) > paginas_a_mostrar and paginas[-1] - paginas[paginas_a_mostrar-1] >1:
        paginas_ab = [*paginas[:paginas_a_mostrar-1],
                      "...",
                      paginas[-1]]   

    else:
        paginas_ab = paginas

    logging.info(f"Var 'paginas_ab': {paginas_ab}\n")    

    return (paginas, paginas_ab)