from modules.mostrar_y_recorrer import *
from modules.logica_juego import *
from modules.datos import *
from modules.guardar_archivo import *
from datetime import datetime


continuar = "si"
bandera_pedir_nombre = True
while continuar == "si":

        inicio = datetime.now()

        lista_repetidos = []
        categoria_actual = None
        palabras_categoria = None
        bandera_categoria = None
        bandera_comodin_palabra_categoria = False
        bandera_comodin_personalizado = False
        bandera_emparejar_palabras = False

        categoria = None
        vidas = 3
        puntos = 0
        errores = 0
        contador_filas = 0
        nivel_actual = 1

        if bandera_pedir_nombre == True:
            print("")
            nombre_jugador = pedir_nombre_jugador()
            print("")




        def jugar_juego(matriz_principal: list, diccionario: dict,diccionario_general,vidas,puntos,nivel_actual,lista_palabras,errores,bandera_comodin_personalizado,bandera_comodin_palabra_categoria,bandera_emparejar_palabras,nombre_jugador) -> int:
            """
            Ejecuta el flujo principal del juego, gestionando rondas, categorías, niveles y puntos.


            Args:
                matriz_principal (list): Matriz principal del nivel actual con palabras a emparejar.
                diccionario (dict): Diccionario con las categorías y palabras del nivel actual.
                diccionario_general (dict): Diccionario completo con todos los niveles y categorías.
                vidas (int): Cantidad inicial de vidas del jugador.
                puntos (int): Puntos acumulados por el jugador.
                nivel_actual (int): Nivel en el que se encuentra el jugador.
                lista_palabras (list): Lista de palabras disponibles en el nivel actual.
                errores (int): Cantidad de errores cometidos por el jugador.
                bandera_comodin_personalizado (bool): Indica si se utilizó el comodín personalizado.
                bandera_comodin_palabra_categoria (bool): Indica si se utilizó el comodín de palabra por categoría.
                bandera_emparejar_palabras (bool): Indica si se activó el emparejamiento de palabras.
                nombre_jugador (str): Nombre del jugador.

            Returns:
                int: Retorna los puntos totales obtenidos por el jugador al finalizar la partida
            """

            #inicio = datetime.now()

            lista_repetidos = []
            categoria_actual = None
            palabras_categoria = None
            bandera_categoria = None
            bandera_gano = False

            categoria = None
            contador_filas = 0


            print("")
            pregunta = input("esta es la vista por fila, quiere cambiarlo a vista por columnas? ")
            print("")


            if pregunta == "si":

                print("")
                matriz_principal = reorganizar_matriz (matriz_principal)
                mostrar_matriz(matriz_principal)
                print("")

            ordenar_alfabeticamente = input("desea ordenar el cuadro alfabeticamnete? ")
            print("")
            if ordenar_alfabeticamente == "si":
                matriz_principal = bubble_sort_matriz_algoritmica(matriz_principal)
                mostrar_matriz(matriz_principal)


            for ronda in range(4):

                bandera_primero = True
                intentos = 3
                print(f"\033[1;36mRonda: {ronda + 1}\033[0m")
                #mostrar_matriz(matriz_principal)
                contador = 0

                if categoria_actual is None:

                    devuelve = revisar_palabra(lista_repetidos,diccionario,bandera_primero,bandera_categoria,categoria,contador,intentos,vidas,puntos,errores,lista_palabras,bandera_comodin_personalizado,bandera_comodin_palabra_categoria,bandera_emparejar_palabras,categoria_primera=None)
                    eleccion_usuario = devuelve[0]
                    categoria = devuelve[1]
                    bandera_categoria = devuelve[2]
                    vidas = devuelve[3]
                    contador = devuelve[5]
                    categoria_primera = devuelve[6]
                    puntos = devuelve [7]
                    bandera_comodin_personalizado = devuelve[9]
                    bandera_comodin_palabra_categoria = devuelve[10]
                    bandera_emparejar_palabras = devuelve [11]



                    mostrar_puntos (intentos,contador,bandera_primero,vidas,bandera_categoria,puntos)
                    bandera_primero = False


                while contador != 4 and intentos != 0:
                    devuelve = revisar_palabra(lista_repetidos,diccionario,bandera_primero,bandera_categoria,categoria,contador,intentos,vidas,puntos,errores,lista_palabras,bandera_comodin_personalizado,bandera_comodin_palabra_categoria,bandera_emparejar_palabras,categoria_primera)

                    eleccion_usuario = devuelve[0]
                    categoria = devuelve[1]
                    bandera_categoria = devuelve[2]
                    vidas = devuelve[3]
                    bandera_existencia = devuelve[4]
                    contador = devuelve[5]
                    categoria_primera = devuelve[6]
                    puntos = devuelve[7]
                    errores = devuelve[8]
                    bandera_comodin_personalizado = devuelve[9]
                    bandera_comodin_palabra_categoria = devuelve[10]
                    bandera_emparejar_palabras = devuelve[11]


                    if bandera_primero == True:
                        resultado = sumar_restar_puntos_y_vidas(bandera_categoria,contador,intentos,vidas,bandera_existencia,puntos)
                        bandera_primero = False

                        contador = resultado[0]
                        intentos = resultado[1]
                        puntos = resultado[3]
                        errores = resultado[4]



                    mostrar_puntos (intentos,contador,bandera_primero,vidas,bandera_categoria,puntos)


                    if vidas == 0:
                        # pasarlo a una nueva funcion
                        print("No lograste completar una fila, perdiste!!! ")
                        mostrar_datos_final_juego(puntos,errores,nombre_jugador)
                        fin = datetime.now()
                        duracion = (fin - inicio).total_seconds()
                        duracion = (int(duracion))
                        print(f"tiempo de juego: {duracion} segundos")
                        print("-"*10)
                        break

                if vidas == 0:
                    bandera_perdio = True
                    break


                if contador == 4 and vidas != 0:

                    print("")
                    print(f"\033[1;32m¡Completaste una fila en la categoría: {categoria}!\033[0m")
                    mostrar_matriz(matriz_principal)

                    if contador != 4:
                        mostrar_matriz(matriz_principal)
                    contador_filas += 1 

                    if contador_filas == 4:
                        print("pasaste de nivel!!!")
                        print("")
                        nivel_actual += 1 

                        if nivel_actual == 6: 
                            #pasarlo a nueva funcion
                            print("ganaste")
                            mostrar_datos_final_juego(puntos,errores,nombre_jugador)
                            fin = datetime.now()
                            duracion = (fin - inicio).total_seconds()
                            duracion = (int(duracion))
                            print(f"tiempo de juego: {duracion} segundos")
                            print("-"*10)

                            bandera_gano = True
                            break

                        diccionario_categorias_nivel = cargar_niveles(diccionario_general, nivel_actual)

                        lista_palabras = diccionario_a_lista(diccionario_categorias_nivel)

                        matriz_principal = cargar_matriz_principal(lista_palabras)

                        if bandera_gano == False:
                            mostrar_matriz(matriz_principal)
                            jugar_juego (matriz_principal,diccionario_categorias_nivel,diccionario,vidas,puntos,nivel_actual,lista_palabras,errores,bandera_comodin_personalizado,bandera_comodin_palabra_categoria,bandera_emparejar_palabras,nombre_jugador)


            return puntos



        diccionario_categorias_nivel = cargar_niveles(diccionario, nivel_actual)

        if diccionario_categorias_nivel:
            lista_palabras = diccionario_a_lista(diccionario_categorias_nivel)
            matriz_principal = cargar_matriz_principal(lista_palabras)


            mostrar_matriz(matriz_principal)

        else:
            print("No hay palabras para el nivel actual.")


        #matriz_principal = acomodar_matriz_por_abc(matriz_principal,lista_palabras)
        #bubble_sort_matriz_algoritmica(matriz_principal)

        mostrar_matriz(matriz_principal)

        puntos = jugar_juego (matriz_principal,diccionario_categorias_nivel,diccionario,vidas,puntos,nivel_actual,lista_palabras,errores,bandera_comodin_personalizado,bandera_comodin_palabra_categoria,bandera_emparejar_palabras,nombre_jugador)



        continuar = input ("desea juga de nuevo? ")

        if continuar == "no":
            path = "datos\\puntaje.json"

            guardar_puntaje_ordenado(path,nombre_jugador, puntos)



