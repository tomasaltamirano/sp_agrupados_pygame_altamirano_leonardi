import random
from modules.datos import *

def obtener_imagenes(diccionario_categorias: dict, nivel:int) -> list:
    categorias_nivel = diccionario_categorias[nivel]
    imagenes = []
    
    for categoria, rutas in categorias_nivel.items():
        for ruta in rutas:
            imagenes.append((ruta, categoria))

    random.shuffle(imagenes)     
    return imagenes

