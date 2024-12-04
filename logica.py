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

#debugueo: las rutas de las imagenes llegan bien a esta funcion
# imagenes = obtener_imagenes(diccionario_categorias, nivel)
# print("Imágenes obtenidas:", imagenes)

def encontrar_categoria (lista_amarillos,color,contador,lista_usados,guardar_boton,boton,categoria,bandera_primera_categoria,lista_categorias,x,y,verde,COLOR_PANTALLA,ventana_principal):
    if bandera_primera_categoria == True and boton["estado"] != None:
        print("entra en encontrar categoria")
        guardar_boton.append(boton)
        lista_usados.append(boton)
        lista_categorias.append(categoria)
        bandera_primera_categoria = False

    elif bandera_primera_categoria == False and boton["estado"] != None:
        print("entra en encontrar resto categorias")
        if boton["estado"] == True and boton != guardar_boton[0]:
            if len(lista_categorias) > 0 and lista_categorias[-1] == categoria:  

                contador += 1
                lista_usados.append(boton)
                print("Las categorías son iguales.")
            else:
                #lista_usados.append(boton)
                for boton in lista_usados:
                    print("dasdas")
                    x,y = boton["posicion"]
                    boton ["estado"] = None
                    enmarcar_imagen(lista_amarillos,lista_usados,boton,x,y,color,COLOR_PANTALLA,ventana_principal)

    return bandera_primera_categoria ,contador

