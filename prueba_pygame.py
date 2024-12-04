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
VERDE = (0,255,0)
AMARILLO = (255,255,0)

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

lista_categorias = []
bandera_juego = True 
bandera_primera_categoria = True
guardar_boton = []
lista_usados = []
contador = 0
lista_amarillos = []

ventana_principal.fill(COLOR_PANTALLA)

while bandera_juego:
    
    #ventana_principal.fill(COLOR_PANTALLA)
    #for boton in botones:
    #    dibujar(boton)

    if contador == 3:
        print(lista_usados)
        print("ganaste")
        for i in range (len(lista_usados)):
            lista_usados[i]["estado"]= None
            x,y = lista_usados[i]["posicion"]
            lista_amarillos.append(lista_usados[i])

            enmarcar_imagen(AMARILLO,lista_amarillos,lista_usados,lista_usados[i],x,y,AMARILLO,COLOR_PANTALLA,ventana_principal)

        guardar_boton = []
        lista_categorias = []
        contador = 0
        bandera_primera_categoria = True
        


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera_juego = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x,y = evento.pos
            
            bandera_primera_categoria,contador = seleccionar_imagenes(AMARILLO,lista_amarillos,contador,lista_usados,guardar_boton,botones,x,y,VERDE,COLOR_PANTALLA,ventana_principal,bandera_primera_categoria,lista_categorias)
    
    #ventana_principal.fill(COLOR_PANTALLA)
    
    for boton in botones:
        dibujar(boton)
    
    pygame.display.update()
    
    
pygame.quit()

