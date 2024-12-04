import random
from modules.datos import *

lista_categorias = obtener_categorias()
lista_limpia = limpiar_datos(lista_categorias)
diccionario_categorias = transformar_lista_a_diccionario(lista_limpia)
nivel = 1

def obtener_imagenes(diccionario_categorias: dict, nivel:int) -> list:
    categorias_nivel = diccionario_categorias[nivel]
    imagenes = []
    
    for categoria, rutas in categorias_nivel.items():
        for ruta in rutas:
            imagenes.append((ruta, categoria))
       
    random.shuffle(imagenes)     
    return imagenes

#debugueo: las rutas de las imagenes llegan bien a esta funcion
# imagenes = obtener_imagenes(diccionario_categorias, nivel)
# print("Imágenes obtenidas:", imagenes)

