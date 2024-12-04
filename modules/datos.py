def obtener_categorias():
    """lee un archivo csv y devuelve las categorias

    Returns:
        retorna una lista de listas, cada sublista representa una linea del archivo csv, cada elemento esta normalizado (separado por comas)
    """
    lista_categorias = []
    with open("datos\\categorias.csv", "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            linea_normalizada = linea.lower()
            elementos = linea_normalizada.split(",") 

            lista_categorias.append(elementos)
    return lista_categorias

def limpiar_fila(fila:list):
    """
    Limpia los espacios innecesarios de cada elemento en una lista

    Args:
        fila(list): lista de elementos a limpiar

    Returns:
        retorna la lista limpia sin espacios al inicio o al final
    """
    fila_limpia = []
    for elemento in fila:
        elemento_limpio = elemento.strip()  
        if elemento_limpio:  
            fila_limpia.append(elemento_limpio)
    return fila_limpia

def limpiar_datos(lista:list) -> list:
    """
    Limpia los datos de una lista procesando cada sublista con la función `limpiar_fila`

    Args:
        lista (list): lista de listas a limpiar

    Returns:
        retorna la lista limpia que fue normalizada
    """
    lista_limpia = []
    for fila in lista:
        fila_limpia = limpiar_fila(fila)  
        lista_limpia.append(fila_limpia)  
    return lista_limpia

def transformar_lista_a_diccionario(lista_limpia:list) -> dict:
    """
    Transforma una lista limpia en un diccionario estructurado por niveles y categorías.

    Args:
        lista_limpia (list): Lista procesada donde cada sublista contiene un nivel, una categoría y una lista de palabras.

    Returns:
        retorna un diccionario donde las claves son los niveles (int) y los valores son diccionarios con categorías como claves y palabras como valores.
    """
    diccionario = {}
    for fila in lista_limpia:
        nivel = int(fila[0])
        categoria = fila[1]  
        palabras = fila[2:]  
        if nivel not in diccionario:
            diccionario[nivel] = {}
        diccionario[nivel][categoria] = palabras
        
    return diccionario

