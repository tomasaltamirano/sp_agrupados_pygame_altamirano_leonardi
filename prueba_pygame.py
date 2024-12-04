import pygame
import random
from modules.visuales import *
from modules.datos import *
from logica import *

pygame.init()

"""
NOTA:
HABRIA QUE HACER QUE CUANDO SE HAGA CLICK EN UN BOTON SE MARQUEN DE COLOR PARA IDENTIFICARLOS, Y HACER QUE CADA VEZ QUE CLICKEAMOS EN UN BOTON PASE ALGO,
"""


TAMAÑO_VENTANA = (800, 500)
COLOR_PANTALLA = (49, 100, 247)
TAMAÑO_BOTON = (100, 100)
ESPACIO_ENTRE_BOTONES = 10
FILAS = 4
COLUMNAS = 4

ventana_principal = pygame.display.set_mode(TAMAÑO_VENTANA)

lista_categorias = obtener_categorias()
lista_limpia = limpiar_datos(lista_categorias)
diccionario_categorias = transformar_lista_a_diccionario(lista_limpia)

nivel = 1
imagenes = obtener_imagenes(diccionario_categorias, nivel)

#aca parece que no se esta enviando correctamente la ruta "imagenes" a la funcion que crea los botones
botones = crear_botones_imagenes(ventana_principal, imagenes, FILAS, COLUMNAS, TAMAÑO_BOTON, ESPACIO_ENTRE_BOTONES, TAMAÑO_VENTANA)
# categorias_nivel = diccionario_categorias[nivel_actual]


pygame.display.set_caption("Agrupados")


bandera_juego = True 


while bandera_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera_juego = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton["rectangulo"].collidepoint(evento.pos):
                print("clickea2")
    
    ventana_principal.fill(COLOR_PANTALLA)
    
    for boton in botones:
        dibujar(boton)
    
    pygame.display.update()
    
    
pygame.quit()

