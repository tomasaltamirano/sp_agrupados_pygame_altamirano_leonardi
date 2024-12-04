import pygame
"""
funciones que se encargan de cargar los elementos visuales en la pantalla
"""
def crear_boton(pantalla, posicion, dimension, texto=None, fuente=None, path_imagen = None):
    boton = {}
    boton["pantalla"] = pantalla
    boton["posicion"] = posicion #tupla
    boton["dimension"] = dimension #tupla
    boton["superficie"] = pygame.Surface(dimension)
    
    if path_imagen != None:
        
        imagen = pygame.image.load(path_imagen)
        #! error aca!!
        print(f"probando si cargan las imagenes...: {path_imagen}")
        
        boton["superficie"] = pygame.transform.scale(imagen, boton["dimension"])
        
    boton["rectangulo"] = boton["superficie"].get_rect(topleft=boton["posicion"])
    return boton

def dibujar(boton):
    boton["pantalla"].blit(boton["superficie"], boton["posicion"])
    
    
#==========================================================
def crear_botones_imagenes(ventana_principal:tuple, imagenes:list, FILAS:int, COLUMNAS:int, TAMAÑO_BOTON, ESPACIO_ENTRE_BOTONES, TAMAÑO_VENTANA) -> list:
    ancho_cuadricula = COLUMNAS * TAMAÑO_BOTON[0] + (COLUMNAS - 1) * ESPACIO_ENTRE_BOTONES
    alto_cuadricula = FILAS * TAMAÑO_BOTON[1] + (FILAS - 1) * ESPACIO_ENTRE_BOTONES

    margen_izquierdo = (TAMAÑO_VENTANA[0] - ancho_cuadricula) // 2 #podes usar un numero fijo y tambien anda
    margen_superior = (TAMAÑO_VENTANA[1] - alto_cuadricula) // 2


    botones = []
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            x = margen_izquierdo + columna * (TAMAÑO_BOTON[0] + ESPACIO_ENTRE_BOTONES)
            y = margen_superior + fila * (TAMAÑO_BOTON[1] + ESPACIO_ENTRE_BOTONES)
            
            ruta_imagen, categoria = imagenes.pop()
            boton = crear_boton(
                pantalla = ventana_principal,
                posicion = (x, y),
                dimension = TAMAÑO_BOTON,
                path_imagen=ruta_imagen
            )
            boton["categoria"] = categoria
            botones.append(boton)
            
    return botones