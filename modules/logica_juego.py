from modules.mostrar_y_recorrer import * 
from modules.datos import *



def pedir_nombre_jugador() -> str:
    """Pide el nombre de usuario al iniciar el juego

    Returns:
        retorna el nombre del usuario en formato str
    """
    
    while True:
        nombre = input("Ingrese su nombre: ").strip().capitalize()
        if nombre == "":
            print("el nombre no puede estar vacio, reingrese.")
        if nombre != "":
            print(f"Bienvenido: {nombre}!")
            break
        
    return nombre

def revisar_palabra (lista_repetidos:list, diccionario:dict, bandera_primero:bool, bandera_categoria:bool, categoria:str,contador:int, intentos:int, vidas:int, puntos:int, errores:int, lista_palabras:list, bandera_comodin_personalizado:bool,bandera_comodin_palabra_categoria: bool,bandera_emparejar_palabras:bool, categoria_primera: str):
    
    """
    Gestiona el ingreso de palabras del jugador, validando existencia, categoría, y si ya fue usada. 
    También administra los comodines y actualiza las variables del juego.

    Args:
        lista_repetidos (list): Lista de palabras ya ingresadas.
        diccionario (dict): Diccionario con categorías y palabras disponibles.
        bandera_primero (bool): Indica si es la primera palabra ingresada.
        bandera_categoria (bool): Indica si la categoría de la palabra es válida.
        categoria (str): Categoría de la palabra actual.
        contador (int): Cantidad de palabras acertadas.
        intentos (int): Número de intentos restantes.
        vidas (int): Número de vidas disponibles.
        puntos (int): Puntuación actual.
        errores (int): Número de errores cometidos.
        lista_palabras (list): Lista de palabras del nivel actual.
        bandera_comodin_personalizado (bool): Indica si se usó el comodín personalizado.
        bandera_comodin_palabra_categoria (bool): Indica si se usó el comodín de categoría.
        bandera_emparejar_palabras (bool): Indica si se usó el comodín de emparejar palabras.
        categoria_primera (str): Categoría de la primera palabra ingresada.

    Returns:
        una lista con los valores actualizados de las variables principales del juego.
    """
    while True:
        
        print("")
        eleccion_usuario = input("ingrese una palabra: ").strip().lower()

        if eleccion_usuario == "1" or eleccion_usuario == "2" or eleccion_usuario == "3":
            lista = usar_comodines(eleccion_usuario,lista_palabras,lista_repetidos,bandera_comodin_personalizado,bandera_comodin_palabra_categoria,bandera_emparejar_palabras,puntos)
            bandera_comodin_personalizado = lista[0]
            bandera_comodin_palabra_categoria = lista[1]
            bandera_emparejar_palabras = lista[2]
            puntos = lista[3]
            continue

        
        resultado = validar_existencia_de_palabra(diccionario,lista_repetidos,eleccion_usuario)

        eleccion_usuario = resultado[0]
        bandera_existencia = resultado [1]
        categoria = resultado[2]

        devuelve = evitar_repeticion_palabras(diccionario, lista_repetidos, eleccion_usuario )

        eleccion_usuario = devuelve[0]
        bandera_repetida = devuelve[1]

        if bandera_existencia == False or bandera_repetida == False:
            mostrar_mensaje(bandera_existencia, bandera_repetida)
            continue

        if bandera_primero == True:

            resultado = definir_categoria(diccionario,eleccion_usuario)
            categoria_primera = resultado["categoria"]
            

            resultado = sumar_restar_puntos_y_vidas(bandera_categoria,bandera_existencia,contador,intentos,vidas,bandera_existencia,puntos,errores)
            contador = resultado[0]
            vidas = resultado[2]
            puntos = resultado [3]
            errores = resultado[4]
            

            lista_repetidos.append(eleccion_usuario)

        else:
            bandera_categoria = validar_misma_categoria(diccionario,eleccion_usuario,categoria_primera,bandera_existencia)
        
            resultado = sumar_restar_puntos_y_vidas(bandera_categoria,bandera_existencia,contador,intentos,vidas,bandera_existencia,puntos,errores)
            contador = resultado[0]
            vidas = resultado[2]
            puntos = resultado [3]
            errores = resultado [4]
            

        
            if bandera_categoria == True:
                lista_repetidos.append(eleccion_usuario)
        

        #if bandera_existencia == True and bandera_repetida == True:
        break

        #mostrar_mensaje(bandera_existencia, bandera_repetida)


    devuelve = [eleccion_usuario,categoria,bandera_categoria,vidas,bandera_existencia,contador,categoria_primera,puntos,errores,bandera_comodin_personalizado,bandera_comodin_palabra_categoria,bandera_emparejar_palabras]

    return devuelve

def evitar_repeticion_palabras(diccionario: dict, lista_repetidos: list, eleccion_usuario: str, bandera_2 = False ) -> str:
    """
    valida si una palabra ya fue ingresada

    Args:
        diccionario (dict): diccionario con las categorias y las palabras
        lista_repetidos (list): lista con las palabras repeditas.
        eleccion_usuario (str): palabra ingresada por el usuario
        

    Returns:
        retorna una lista en la cual bandera_repetida indica si la palabra es repetida 
    """
    bandera_repetida = True
    for palabra in lista_repetidos:

        if palabra == eleccion_usuario:

            bandera_repetida = False
            break

    resultado = [eleccion_usuario,bandera_repetida]

    return resultado

def validar_existencia_de_palabra(diccionario:dict, lista_repetidos:list, eleccion_usuario,) -> str:
    """
    verifica si la palabra ingresada pertenece a una categoria

    Args:
        diccionario (dict): Diccionario de categorias y palabras.
        lista_repetidos (list): Lista con las palabras repetidas.
        eleccion_usuario (_type_): Palabra elegida por el usuario

    Returns:
        str: Retorna una lista en la que bandera_existencia indica si la palabra existe y categoria es la categoria a la que pertenece
    """

    bandera_existencia = False
    for categoria, palabras in diccionario.items():
        if eleccion_usuario in palabras:

            bandera_existencia = True
            break
    
    resultado = [eleccion_usuario,bandera_existencia,categoria]
    return  resultado

def sumar_restar_puntos_y_vidas (bandera_categoria:bool, bandera_existencia:bool, contador:int, intentos:int, vidas:int, bandera_existecia: bool, puntos:int, errores:int) -> list:
    
    """
    Actualiza la puntuación, vidas e intentos del jugador según la validez de la palabra ingresada.

    Args:
        bandera_categoria (bool): Indica si la categoría de la palabra es correcta.
        bandera_existencia (bool): Indica si la palabra existe.
        contador (int): Contador de palabras acertadas.
        intentos (int): Número de intentos restantes.
        vidas (int): Número de vidas disponibles.
        puntos (int): Puntuación actual.
        errores (int): Cantidad de errores cometidos.

    Returns:
        retorna una lista con los valores actualizados de [contador, intentos, vidas, puntos, errores].
    """
    
    if (bandera_categoria == True or bandera_categoria == None) and bandera_existencia == True:
        contador += 1
        puntos += 1

    elif bandera_categoria == False and bandera_existecia == True:
        puntos -= 1
        vidas -= 1
        errores += 1

    resultado = [contador,intentos,vidas,puntos,errores]
    return resultado

def validar_misma_categoria(diccionario:dict, eleccion_usuario:str, categoria:str, bandera_existencia:bool) -> bool:
    
    """
    Comprueba si una palabra pertenece a la misma categoría de las previamente ingresadas.

    Args:
        diccionario (dict): Diccionario con categorías y palabras.
        eleccion_usuario (str): Palabra ingresada por el usuario.
        categoria (str): Categoría base para validar.
        bandera_existencia (bool): Indica si la palabra existe en el diccionario.

    Returns:
        retorna un bool `True` si pertenece a la misma categoría, `False` en caso contrario.
    """
    bandera_categoria = False
    bandera_vidas = False
    for palabras in diccionario[categoria]:
    
        if palabras == eleccion_usuario:
            bandera_categoria = True
            bandera_vidas = True
            break
    if bandera_vidas == False and bandera_existencia == True:
        print("perdio una vida ")

    return bandera_categoria

def definir_categoria(diccionario:dict, palabra:str) -> dict:
    """
    Obtiene la categoría de una palabra específica.

    Args:
        diccionario (dict): Diccionario de palabras categorizadas.
        palabra (str): Palabra para la cual se desea obtener la categoría.

    Returns:
        retorna un diccionario con la categoría y las palabras asociadas, junto con la palabra ingresada.
    """


    resultado = {"categoria": None, "palabras": None, "palabra": palabra}
    
    for categoria, palabras in diccionario.items():
        if palabra in palabras:
            resultado["categoria"] = categoria
            resultado["palabras"] = palabras
            break
    
    
    return resultado 

def comodin_personalizado(lista_palabras:list) -> None:
    """
    Crea una matriz 4x4 con palabras seleccionadas de la lista_palabras y la muestra al usuario, es un comodin que sugiere palabras al usuario segun las palabras disponibles

    Args:
        lista_palabras (list): Lista de palabras disponibles para llenar la matriz
    """
    matriz_nueva = [["","","",""],
                    ["","","",""],
                    ["","","",""],
                    ["","","",""]]
    
    
    i = 0
    contador = 0
    for j in range (contador,len(lista_palabras),4):
            

            matriz_nueva[i][i] = lista_palabras[j]
            contador += 4
            i += 1
            if contador == 16:
                break
    print("")
    print("perdio un punto")
    
    print("matriz recomendada: ")
    print("")
    mostrar_matriz (matriz_nueva)
    print("")
    

def comodin_mostrar_palabra_categoria(lista_repetidos: list, diccionario:dict, lista_palabras:list) -> None:
    """
    Encuentra y muestra una palabra de una categoria que no se haya usado previamente.

    Args:
        lista_repetidos (list): Lista de palabras que ya se usaron
        diccionario (dict): Diccionario que contiene las palabras y las categorias
        lista_palabras (list): Lista de palabras que todavia se pueden usar
    """
    bandera_repetida = False
    for palabra in (lista_palabras):

        if palabra not in lista_repetidos:

            for nivel in diccionario:

                for categoria in diccionario[nivel]:
            
                    for buscar in diccionario[nivel][categoria]:
                
                        if buscar == palabra:

                            print (f"categoria: {categoria} ---> palabra: {palabra} ")
                            return
                        

def comodin_emparejar_palabras (lista_repetidos:list, diccionario:dict, lista_palabras:list) -> None:
    """
    Muestra dos palabras que no se hayan usado y las empareja

    Args:
        lista_repetidos (list): Lista de palabras repetidas
        diccionario (dict): Diccionario que contiene las categorias y palabras
        lista_palabras (list): Lista de palabras que todavia estan disponibles
    """
    contador = 0
    
    for palabra in (lista_palabras):
        
        if palabra not in lista_repetidos:
            print("palabras emparejadas: ")
            for nivel in diccionario:
                
                for categoria in diccionario[nivel]:
                    
                    for palabra_buscar in diccionario[nivel][categoria]:
                    
                        print(palabra_buscar)

                        contador += 1
                        if contador == 2:
                            return
                    

def usar_comodines(eleccion_usuario:str, lista_palabras:list, lista_repetidos: list, bandera_comodin_personalizado:bool, bandera_comodin_palabra_categoria:bool, bandera_emparejar_palabras:bool, puntos:int) -> list:
    """
    gestiona la ejecucion del comodin elegido y actualiza las banderas

    Args:
        eleccion_usuario (str): Opción elegida por el usuario para activar un comodín
        lista_palabras (list): Lista de palabras disponibles
        lista_repetidos (list): Lista de palabras repetidas
        bandera_comodin_personalizado (bool): indica si el comodin personalizado ya fue usado
        bandera_comodin_palabra_categoria (bool): indica si el comodin de la categoria ya fue usado
        bandera_emparejar_palabras (bool): Indica si el comodín de emparejar palabras ya fue usado
        puntos (int): puntuacion actual del usuario

    Returns:
        retorna una lista actualizada de las banderas y los comodines usados
    """

    if eleccion_usuario == "1" and bandera_comodin_personalizado == False:
        comodin_personalizado(lista_palabras)
        puntos -= 1
        bandera_comodin_personalizado = True
        print(f"su puntuacion actual es: {puntos}")

    elif eleccion_usuario == "1" and bandera_comodin_personalizado == True:
        print("ya uso este comodin")

    if eleccion_usuario == "2" and bandera_comodin_palabra_categoria == False:
        print("")
        comodin_mostrar_palabra_categoria(lista_repetidos,diccionario,lista_palabras)
        bandera_comodin_palabra_categoria = True
        print("")


    elif eleccion_usuario == "2" and bandera_comodin_palabra_categoria == True:
        print("ya uso este comodin")

    if eleccion_usuario == "3" and bandera_emparejar_palabras == False:
        comodin_emparejar_palabras (lista_repetidos,diccionario,lista_palabras)
        bandera_emparejar_palabras = True
        print("")


    elif eleccion_usuario == "3" and bandera_emparejar_palabras == True:
        print("ya uso este comodin")

    lista = [bandera_comodin_personalizado,bandera_comodin_palabra_categoria,bandera_emparejar_palabras,puntos]
    return lista


def bubble_sort_matriz_algoritmica(matriz_principal:list)-> list:
    """recibe matriz principal y prdena todos sus elementos alfabeticamente

    Args:
        matriz_principal (list): mstriz principal con sus palabras

    Returns:
        list: matriz principal ordenada
    """
    filas = len(matriz_principal)
    columnas = len(matriz_principal[0])
    
    
    for _ in range(16):
        for i in range(filas):
            for j in range(columnas - 1):  
                if matriz_principal[i][j] > matriz_principal[i][j + 1]:
                    matriz_principal[i][j], matriz_principal[i][j + 1] = matriz_principal[i][j + 1], matriz_principal[i][j]
                    #print(matriz_principal)
            if i < filas - 1 and matriz_principal[i][columnas - 1] > matriz_principal[i + 1][0]:
                matriz_principal[i][columnas - 1], matriz_principal[i + 1][0] = matriz_principal[i + 1][0], matriz_principal[i][columnas - 1]
                #print(matriz_principal)
    return matriz_principal


