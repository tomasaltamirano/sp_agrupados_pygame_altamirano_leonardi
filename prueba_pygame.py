import pygame
import random
from modules.visuales import *
from modules.datos import *
from logica import *

pygame.init()


VERDE = (0,255,0)
AMARILLO = (255,255,0)
BLANCO = (255,255,255)
TAMAÑO_VENTANA = (800, 500)
COLOR_PANTALLA = (49, 100, 247)
TAMAÑO_BOTON = (100, 100)
ESPACIO_ENTRE_BOTONES = 10
FILAS = 4
COLUMNAS = 4


ventana_principal = pygame.display.set_mode(TAMAÑO_VENTANA)
pygame.display.set_caption("Agrupados")
fuente = pygame.font.Font(None, 40)


lista_categorias = obtener_categorias()
lista_limpia = limpiar_datos(lista_categorias)
diccionario_categorias = transformar_lista_a_diccionario(lista_limpia)


nivel = 1
puntuacion = 0
vidas = 3
bandera_nombre = False
filas_completadas = 0
lista_categorias = []
bandera_juego = True 
bandera_primera_categoria = True
guardar_boton = []
lista_usados = []
contador = [0]
lista_intocables = []
lista_amarillos = []
guardar_boton = []


imagenes = obtener_imagenes(diccionario_categorias, nivel)
botones = crear_botones_imagenes(ventana_principal, imagenes, FILAS, COLUMNAS, TAMAÑO_BOTON, ESPACIO_ENTRE_BOTONES, TAMAÑO_VENTANA)
# categorias_nivel = diccionario_categorias[nivel_actual]


ventana_principal.fill(COLOR_PANTALLA)
bandera_primera_categoria = True


while bandera_juego:
    if not bandera_nombre:
        
        mostrar_mensaje(ventana_principal, TAMAÑO_VENTANA, fuente, "ingrese su nombre")
        # pygame.display.update()
        nombre_jugador = pedir_nombre(ventana_principal, TAMAÑO_VENTANA, fuente)
        if not nombre_jugador:
            mostrar_mensaje(ventana_principal, TAMAÑO_VENTANA, fuente, "ingresa tu nombre...")

            pygame.display.update()
            
        else:
            bandera_nombre = True 
            ventana_principal.fill(COLOR_PANTALLA)
            
            # for boton in botones:
            #     dibujar(boton)
        
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera_juego = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            
            # Lógica de selección de imágenes.
            bandera_primera_categoria, contador, categoria = seleccionar_imagenes(
                AMARILLO, lista_amarillos, contador, lista_usados, guardar_boton,
                botones, x, y, VERDE, COLOR_PANTALLA, ventana_principal, 
                bandera_primera_categoria, lista_categorias
            )
            print(f"contando:{contador}")
            if contador[0] == 4:
                puntuacion += 1
                filas_completadas += 1
                print(f"Filas completadas: {filas_completadas}")
                #! aca podriamos tener una funcion que muestre un mensaje o un sonido en pantalla indicando que completo una fila con exito.
                if filas_completadas == 4:
                    filas_completadas = 0  # Reinicia el contador.
                    nivel, botones = cambiar_nivel(
                        nivel, 
                        diccionario_categorias, 
                        ventana_principal, 
                        FILAS, 
                        COLUMNAS, 
                        TAMAÑO_BOTON, 
                        ESPACIO_ENTRE_BOTONES, 
                        TAMAÑO_VENTANA, 
                        COLOR_PANTALLA, 
                        lista_amarillos, 
                        lista_usados, 
                    )
                    contador[0] = 0  # Reinicia el contador de imágenes seleccionadas.
            else:
                # Descontar una vida si no completa la fila
                vidas -= 1
            if vidas <= 0:
                mostrar_mensaje(ventana_principal, TAMAÑO_VENTANA, fuente, "Game Over!")
                bandera_juego = False

        verificar_contador(contador, lista_usados, AMARILLO, lista_amarillos,lista_categorias, VERDE, COLOR_PANTALLA, ventana_principal)
        mostrar_puntos_y_vidas(ventana_principal, fuente, puntuacion, vidas)

    for boton in botones:
        dibujar(boton)

    pygame.display.update()




