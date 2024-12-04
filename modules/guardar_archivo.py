import json
import os

def crear_archivo_json(path):
    """
    Crea un archivo JSON vacío si no existe.

    Args:
        path (_type_): Ruta donde se va ubicar el archivo
    """
    if not os.path.exists(path):
        with open(path, "w", encoding="utf8") as archivo:
            json.dump([], archivo, indent=4, ensure_ascii=False)

def cargar_puntajes(path):
    """
    Carga los puntajes desde un archivo JSON. Si no existe, lo crea y devuelve una lista vacía.

    Args:
        path (_type_): Ruta donde se va ubicar el archivo

    Returns:
        retorna una lista de puntajes cargados desde el archivo JSON. Si el archivo está vacío o no existe, devuelve una lista vacía.
    """
    crear_archivo_json(path)
    with open(path, "r", encoding="utf8") as archivo:
        return json.load(archivo)

def guardar_puntajes(path, datos):
    """
    Guarda la lista de puntajes en un archivo JSON.
    
    Args:
        path (str): Ruta donde se ubicará el archivo JSON.
        datos (list): Lista de puntajes a guardar en el archivo.
    """
    with open(path, "w", encoding="utf8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def ordenar_puntajes(datos):
    """
    Ordena la lista de puntajes de mayor a menor usando Bubble Sort.

    Args:
        datos (_type_): lista de datos con los puntajes a ordenar

    Returns:
        retorna la lista de puntajes ordenados
    """
    n = len(datos)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if datos[j]["puntaje"] < datos[j + 1]["puntaje"]:
                auxiliar = datos[j]
                datos[j] = datos[j+1]
                datos[j+1] = auxiliar
    return datos

def guardar_puntaje_ordenado(path, nombre, puntaje):
    """
    Crea el archivo si no existe, agrega un puntaje, ordena y guarda los datos.

    Args:
        path (_type_): Ruta donde se va ubicar el archivo
        nombre (_type_): Nombre del jugador que se guarda en el archivo
        puntaje (_type_): Puntaje del jugador que se guarda en el archivo
    """
    datos = cargar_puntajes(path)
    datos.append({"nombre": nombre, "puntaje": puntaje})
    datos = ordenar_puntajes(datos)
    guardar_puntajes(path, datos)

