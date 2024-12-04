import random
import re
from modules.datos import *


lista_categorias = obtener_categorias()
diccionario = transformar_lista_a_diccionario(lista_categorias)

def cargar_niveles(diccionario, nivel_actual):
    """
    Filtra y devuelve las categorías correspondientes al nivel actual.

    Args:
        diccionario (dict): Diccionario que contiene niveles como claves y categorías como valores.
        nivel_actual (int): Nivel actual del juego.

    Returns:
        dict: Diccionario con las categorías del nivel actual.
    """
    categorias = {}
    if nivel_actual in diccionario:
        categorias = diccionario[nivel_actual]
        

    return categorias

def diccionario_a_lista(diccionario_categorias_nivel):
    """
    Convierte un diccionario de categorías a una lista de palabras.

    Args:
        diccionario_categorias_nivel (dict): Diccionario con categorías y listas de palabras.

    Returns:
        list: Lista con todas las palabras de las categorías.
    """
    lista_palabras = []
    for palabras in diccionario_categorias_nivel.values():
        lista_palabras.extend(palabras)
        
    return lista_palabras

def borrar_elemento_de_lista (lista_palabras:list, numero: int) -> list:
    """
    Elimina un elemento de una lista según su índice y devuelve la lista actualizada.

    Args:
        lista_palabras (list): Lista original de palabras.
        numero (int): Índice del elemento a eliminar.

    Returns:
        list: Lista actualizada sin el elemento especificado.
    """
    lista_nueva = []

    for i in range(len(lista_palabras)):

        if i != numero:
            lista_nueva += [lista_palabras[i]]

    return lista_nueva

def cargar_matriz_principal(lista_palabras:list) -> list:
    """
    Crea y devuelve una matriz de 4x4 llenada con palabras aleatorias de una lista.

    Args:
        lista_palabras (list): Lista de palabras disponibles.

    Returns:
        list: Matriz 4x4 con palabras distribuidas aleatoriamente.
    """
    matriz_principal = []
    for _ in range(4):  # 4 filas
        fila = []
        for _ in range(4):  # 4 columnas
            if lista_palabras:  # Verifica que queden elementos en la lista
                numero = random.randint(0, len(lista_palabras) - 1)
                palabra = lista_palabras[numero]
                fila.append(palabra)
                lista_palabras = borrar_elemento_de_lista(lista_palabras, numero)  # Actualiza la lista
        matriz_principal.append(fila)
    return matriz_principal
    
def mostrar_matriz(matriz_principal:list) -> None:
    """
    Muestra la matriz principal en un formato tabular y presenta las opciones de comodines.

    Args:
        matriz_principal (list): Matriz de palabras a mostrar.

    Returns:
        None
    """
    for i in range (len(matriz_principal)):
        
        for j in range(len(matriz_principal)):

            print(f"{matriz_principal[i][j]:10}",end=" | ")
        print("")
        print("-" * (len(matriz_principal[0]) * 13))
    print("")
    print("1-para usar el comodin personalizado")
    print("2-para usar el comodin mostrar palabra y su categoria")
    print("3-para usar el comodin mostrar dos palabras de una misma categoria")
        
def mostrar_mensaje(bandera_existencia:bool, bandera_repetida:bool) -> None:
    """
    Muestra un mensaje según las banderas de existencia y repetición de una palabra.

    Args:
        bandera_existencia (bool): Indica si la palabra existe en la categoría.
        bandera_repetida (bool): Indica si la palabra ya fue ingresada.

    Returns:
        None
    """
    
    if bandera_existencia == True and bandera_repetida == False:
        mensaje = "la plabra ya fue ingresada: "
    elif bandera_existencia == False and bandera_repetida == True:
        mensaje ="la palabra no existe: "
    print(mensaje)

def mostrar_puntos (intentos:int, contador:int, bandera_primero:bool, vidas:int, bandera_categoria:bool, puntos:int) -> None:
    """
    Muestra el progreso del jugador en la ronda actual.

    Args:
        intentos (int): Intentos restantes del jugador.
        contador (int): Palabras acertadas en la ronda actual.
        bandera_primero (bool): Indica si es el primer intento.
        vidas (int): Vidas restantes del jugador.
        bandera_categoria (bool): Indica si el jugador seleccionó una categoría.
        puntos (int): Puntos acumulados del jugador.

    Returns:
        None
    """

    print(f"Intentos restantes: {vidas}")
    print(f"Progreso: {contador}/4 palabras")
    if puntos < 0:
        puntos = 0
    print(f"puntos: {puntos}")

def reorganizar_matriz (matriz:list) -> list:
    """
    cambia la visualización de filas a columnas.

    Args:
        matriz (list): Matriz original a transponer.

    Returns:
        list: Matriz transpuesta.
    """
    matriz_principal = [[0,0,0,0],
                        [0,0,0,0],
                        [0,0,0,0],
                        [0,0,0,0]]
    for i in range(len(matriz)):  # 4 filas
        
        for j in range(len(matriz[0])):  # 4 columnas

            matriz_principal[j][i] = matriz [i][j]

    return matriz_principal

def mostrar_datos_final_juego(puntos:int, errores:int, nombre_jugador:str):
    """
    Muestra los datos finales de la partida al jugador.

    Args:
        puntos (int): Puntos obtenidos por el jugador.
        errores (int): Número de errores cometidos por el jugador.
        nombre_jugador (str): Nombre del jugador.

    Returns:
        bool: Bandera para indicar que se mostraron los datos finales.
    """
    
    print("")
    print("-"*10)
    print("datos de partida:")
    print("")
    print(f"nombre: {nombre_jugador}")
    print(f"puntos: {puntos}")
    print(f"errores {errores}")
    #print("-"*10)
    bandera_mostrar = True
    return bandera_mostrar


# lista_categorias = obtener_categorias()
# diccionario = transformar_lista_a_diccionario(lista_categorias)

# def cargar_niveles(diccionario, nivel_actual):
#     categorias = {}
#     if nivel_actual in diccionario:
#         categorias = diccionario[nivel_actual]
        

#     return categorias

# def diccionario_a_lista(diccionario_categorias_nivel):
#     lista_palabras = []
#     for palabras in diccionario_categorias_nivel.values():
#         lista_palabras.extend(palabras)
        
#     return lista_palabras

# def borrar_elemento_de_lista (lista_palabras:list, numero: int) -> list:
#     lista_nueva = []

#     for i in range(len(lista_palabras)):

#         if i != numero:
#             lista_nueva += [lista_palabras[i]]

#     return lista_nueva

# def cargar_matriz_principal(lista_palabras):
#     matriz_principal = []
#     for _ in range(4):  # 4 filas
#         fila = []
#         for _ in range(4):  # 4 columnas
#             if lista_palabras:  # Verifica que queden elementos en la lista
#                 numero = random.randint(0, len(lista_palabras) - 1)
#                 palabra = lista_palabras[numero]
#                 fila.append(palabra)
#                 lista_palabras = borrar_elemento_de_lista(lista_palabras, numero)  # Actualiza la lista
#         matriz_principal.append(fila)
#     return matriz_principal
    

# def mostrar_matriz(matriz_principal):

#     for i in range (len(matriz_principal)):
        
#         for j in range(len(matriz_principal)):

#             print(f"{matriz_principal[i][j]:10}",end=" | ")
#         print("")
#         print("-" * (len(matriz_principal[0]) * 13))
#     print("")
#     print("1-para usar el comodin personalizado")
#     print("2-para usar el comodin mostrar palabra y su categoria")
#     print("3-para usar el comodin mostrar dos palabras de una misma categoria")
        

# def mostrar_mensaje(bandera_existencia, bandera_repetida):
#     if bandera_existencia == True and bandera_repetida == False:
#         mensaje = "la plabra ya fue ingresada: "
#     elif bandera_existencia == False and bandera_repetida == True:
#         mensaje ="la palabra no existe: "
#     print(mensaje)

# def mostrar_puntos (intentos,contador,bandera_primero,vidas,bandera_categoria,puntos):

#     print(f"Intentos restantes: {vidas}")
#     print(f"Progreso: {contador}/4 palabras")
#     if puntos < 0:
#         puntos = 0
#     print(f"puntos: {puntos}")

# def reorganizar_matriz (matriz):
#     matriz_principal = [[0,0,0,0],
#                         [0,0,0,0],
#                         [0,0,0,0],
#                         [0,0,0,0]]
#     for i in range(len(matriz)):  # 4 filas
        
#         for j in range(len(matriz[0])):  # 4 columnas

#             matriz_principal[j][i] = matriz [i][j]

                
                
#     return matriz_principal

# def mostrar_datos_final_juego(puntos,errores,nombre_jugador):
#     print("")
#     print("-"*10)
#     print("datos de partida:")
#     print("")
#     print(f"nombre: {nombre_jugador}")
#     print(f"puntos: {puntos}")
#     print(f"errores {errores}")
#     print("-"*10)
#     bandera_mostrar = True
#     return bandera_mostrar




