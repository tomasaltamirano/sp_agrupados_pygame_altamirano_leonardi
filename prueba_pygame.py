import pygame
import random
from modules.visuales import *
from modules.datos import *
from logica import *

pygame.init()


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
filas_completadas = 0
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
contador = [0]
# lista_categorias = []

lista_intocables = []

lista_amarillos = []

guardar_boton = []


ventana_principal.fill(COLOR_PANTALLA)
bandera_primera_categoria = True


while bandera_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera_juego = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            print("desde los botones")
            # Lógica de selección de imágenes.
            bandera_primera_categoria, contador = seleccionar_imagenes(
                AMARILLO, lista_amarillos, contador, lista_usados, guardar_boton,
                botones, x, y, VERDE, COLOR_PANTALLA, ventana_principal, 
                bandera_primera_categoria, lista_categorias
            )
            print(f"contando:{contador}")
            if contador[0] == 4:
                print(f"Filas completadas: {filas_completadas}")
                filas_completadas += 1
                
                if filas_completadas == 4:
                    filas_completadas = 0  # Reinicia el contador.
                    nivel, botones = cambiar_nivel(
                        nivel, diccionario_categorias, ventana_principal, 
                        FILAS, COLUMNAS, TAMAÑO_BOTON, ESPACIO_ENTRE_BOTONES, 
                        TAMAÑO_VENTANA, COLOR_PANTALLA
                    )
                    contador[0] = 0  # Reinicia el contador de imágenes seleccionadas.
                    # lista_categorias.clear()
        verificar_contador(contador, lista_usados, AMARILLO, lista_amarillos,lista_categorias, VERDE, COLOR_PANTALLA, ventana_principal)

                    # lista_usados.clear()  # Limpia las listas.
                    # lista_amarillos.clear()
                    # lista_categorias.clear()

                    
                
    # Redibuja los botones.
    for boton in botones:
        dibujar(boton)

    pygame.display.update()


# while bandera_juego:
    
    
#     #ventana_principal.fill(COLOR_PANTALLA)
#     #for boton in botones:
#     #    dibujar(boton)

#     #if contador[0] == 4:
#     #    
#     #    print("ganaste")
#     #    for i in range (len(lista_usados)):
#     #        
#     #        lista_usados[i]["estado"]= None
#     #        x,y = lista_usados[i]["posicion"]
#     #        lista_amarillos.append(lista_usados[i])
            

#             #enmarcar_imagen(contador,AMARILLO,lista_amarillos,lista_usados,lista_usados[i],x,y,VERDE,COLOR_PANTALLA,ventana_principal)

    
    
#     #contador = [0]
    
    


#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             bandera_juego = False
#         elif evento.type == pygame.MOUSEBUTTONDOWN:
#             x,y = evento.pos
            
#             #seleccion de imagenes
#             bandera_primera_categoria,contador = seleccionar_imagenes(AMARILLO,lista_amarillos,contador,lista_usados,guardar_boton,botones,x,y,VERDE,COLOR_PANTALLA,ventana_principal,bandera_primera_categoria,lista_categorias)
#             #print(contador,"dsadas")
#             #print(type(contador))
#             verificar_contador(contador,lista_usados,AMARILLO,lista_amarillos,VERDE,COLOR_PANTALLA,ventana_principal)
            
#             if contador[0] == 4:
#                 contador_filas_completadas += 1
#                 print(f"filas completadas: {contador_filas_completadas}/4")
#                 if contador_filas_completadas == 4:
#                     contador_filas_completadas = 0 #para resetear el contador de filas
#                     nivel, botones = cambiar_nivel(nivel, diccionario_categorias, ventana_principal, imagenes, FILAS, COLUMNAS, TAMAÑO_BOTON, ESPACIO_ENTRE_BOTONES, TAMAÑO_VENTANA)
#                     contador[0] = 0  # Reinicia el contador de imágenes seleccionadas.
#                     lista_usados.clear()  # Limpia las listas.
#                     lista_amarillos.clear()
#                     lista_categorias.clear()
                
#     #ventana_principal.fill(COLOR_PANTALLA)
    
#     for boton in botones:
#         dibujar(boton)
    
#     pygame.display.update()
    
    
# pygame.quit()

