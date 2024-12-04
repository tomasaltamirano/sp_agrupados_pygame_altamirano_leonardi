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
        boton["superficie"] = pygame.transform.scale(imagen, boton["dimension"])
        
    boton["rectangulo"] = boton["superficie"].get_rect(topleft=boton["posicion"])
    return boton

def dibujar(boton):
    boton["pantalla"].blit(boton["superficie"], boton["posicion"])
