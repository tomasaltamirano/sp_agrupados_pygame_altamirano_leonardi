from modules.mostrar_y_recorrer import *
from modules.logica_juego import *
from modules.datos import *
from modules.guardar_archivo import *
from datetime import datetime
from modules.paths_imagenes import *
from modules.logica_pygame import *
import pygame


#pygame.init()
#
#flag = True
#NEGRO = (0,0,0)
#
#ventana = pygame.display.set_mode((500,500))
#pygame.display.set_caption("agrupados")
#
#
#while flag == True:
#
#    ventana.fill(NEGRO)
#
#    lista_eventos = pygame.event.get()
#    for evento in lista_eventos:
#        if evento.type == pygame.QUIT:
#            flag = False








pygame.init()

flag = True
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)

#1930,1010 para ventana completa
ventana = pygame.display.set_mode((1400,800))
pygame.display.set_caption("agrupados")
ventana.fill(NEGRO)

posicion_x, posicion_y = 100, 100  
ancho, alto = 50, 50

icono = pygame.image.load("imagenes\\icono_utn.jpg")
pygame.display.set_icon(icono)

fuente = pygame.font.SysFont("Arial",60)
texto = fuente.render("bienvenido",False,VERDE,BLANCO)

fondo_pantalla = pygame.image.load("imagenes\\fondo de pantalla.jpg")
fondo_pantalla = pygame.transform.scale(fondo_pantalla, (1930, 1010)) 





bandera_1 = False
bandera_2 = False
bandera_3 = False
bandera_4 = False
bandera_5 = False
bandera_6 = False
bandera_7 = False
bandera_8 = False
bandera_9 = False
bandera_10 = False
bandera_11 = False
bandera_12 = False
bandera_13 = False
bandera_14 = False
bandera_15 = False
bandera_16 = False

lista_banderas = [bandera_1,bandera_2,bandera_3,bandera_4,bandera_5,bandera_6,bandera_7,bandera_8,bandera_9,bandera_10,bandera_11,bandera_12,bandera_13,bandera_14,bandera_15,bandera_16]

while flag == True:

    
    #pygame.draw.rect(fondo_pantalla, VERDE, posicion_x, posicion_y, ancho, alto)
    ventana.blit(fondo_pantalla,(0,0))

    dibujar_imagen(fondo_pantalla, imagen_corazon, (100,100),(500,200))
    dibujar_imagen(fondo_pantalla, imagen_trebol, (100,100),(630,200))
    dibujar_imagen(fondo_pantalla, imagen_picas, (100,100),(760,200))
    dibujar_imagen(fondo_pantalla, imagen_diamante, (100,100),(890,200))
    dibujar_imagen(fondo_pantalla, imagen_gallina, (100,100),(500,350))
    dibujar_imagen(fondo_pantalla, imagen_cerdo, (100,100),(630,350))
    dibujar_imagen(fondo_pantalla, imagen_oveja, (100,100),(760,350))
    dibujar_imagen(fondo_pantalla, imagen_vaca, (100,100),(890,350))
    dibujar_imagen(fondo_pantalla, imagen_bombero, (100,100),(500,500))
    dibujar_imagen(fondo_pantalla, imagen_doctor, (100,100),(630,500))
    dibujar_imagen(fondo_pantalla, imagen_chef, (100,100),(760,500))
    dibujar_imagen(fondo_pantalla, imagen_policia, (100,100),(890,500))
    dibujar_imagen(fondo_pantalla, imagen_batidora, (100,100),(500,650))
    dibujar_imagen(fondo_pantalla, imagen_licuadora, (100,100),(630,650))
    dibujar_imagen(fondo_pantalla, imagen_tostada, (100,100),(760,650))
    dibujar_imagen(fondo_pantalla, imagen_cafetera, (100,100),(890,650))

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        
        if evento.type == pygame.QUIT:
            flag = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            #print(evento.pos)
            x,y = evento.pos
            #print(x,y)
            ejecutar_eventos(x, y, fondo_pantalla,VERDE,lista_banderas)

        
    
    

    pygame.display.update()








#continuar = "si"
#bandera_pedir_nombre = True
#while continuar == "si":






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

#if bandera_pedir_nombre == True:
#    print("")
"$$$"
#nombre_jugador = pedir_nombre_jugador()
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


    lista_repetidos = []
    categoria_actual = None
    palabras_categoria = None
    bandera_categoria = None
    bandera_gano = False

    categoria = None
    contador_filas = 0


    print("")
    "$$$"
    #pregunta = input("esta es la vista por fila, quiere cambiarlo a vista por columnas? ")
    pregunta = "si"
    print("")


    if pregunta == "si":

        print("")
        matriz_principal = reorganizar_matriz (matriz_principal)
        mostrar_matriz(matriz_principal)
        print("")

    "$$$"
    #ordenar_alfabeticamente = input("desea ordenar el cuadro alfabeticamnete? ")
    #print("")
    #if ordenar_alfabeticamente == "si":
    #    matriz_principal = bubble_sort_matriz_algoritmica(matriz_principal)
    #    mostrar_matriz(matriz_principal)


    for ronda in range(4):

        bandera_primero = True
        intentos = 3
        print(f"\033[1;36mRonda: {ronda + 1}\033[0m")
        
        contador = 0

        if categoria_actual is None:

            "$$$"
            #devuelve = revisar_palabra(lista_repetidos,diccionario,bandera_primero,bandera_categoria,categoria,contador,intentos,vidas,puntos,errores,lista_palabras,bandera_comodin_personalizado,bandera_comodin_palabra_categoria,bandera_emparejar_palabras,categoria_primera=None)
            #eleccion_usuario = devuelve[0]
            #categoria = devuelve[1]
            #bandera_categoria = devuelve[2]
            #vidas = devuelve[3]
            #contador = devuelve[5]
            #categoria_primera = devuelve[6]
            #puntos = devuelve [7]
            #bandera_comodin_personalizado = devuelve[9]
            #bandera_comodin_palabra_categoria = devuelve[10]
            #bandera_emparejar_palabras = devuelve [11]



            mostrar_puntos (intentos,contador,bandera_primero,vidas,bandera_categoria,puntos)
            bandera_primero = False


        while contador != 4 and intentos != 0:
            "$$$"
            #devuelve = revisar_palabra(lista_repetidos,diccionario,bandera_primero,bandera_categoria,categoria,contador,intentos,vidas,puntos,errores,lista_palabras,bandera_comodin_personalizado,bandera_comodin_palabra_categoria,bandera_emparejar_palabras,categoria_primera)

            #eleccion_usuario = devuelve[0]
            #categoria = devuelve[1]
            #bandera_categoria = devuelve[2]
            #vidas = devuelve[3]
            #bandera_existencia = devuelve[4]
            #contador = devuelve[5]
            #categoria_primera = devuelve[6]
            #puntos = devuelve[7]
            #errores = devuelve[8]
            #bandera_comodin_personalizado = devuelve[9]
            #bandera_comodin_palabra_categoria = devuelve[10]
            #bandera_emparejar_palabras = devuelve[11]


            #if bandera_primero == True:
            #    resultado = sumar_restar_puntos_y_vidas(bandera_categoria,contador,intentos,vidas,bandera_existencia,puntos)
            #    bandera_primero = False

            #    contador = resultado[0]
            #    intentos = resultado[1]
            #    puntos = resultado[3]
            #    errores = resultado[4]



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



#diccionario_categorias_nivel = cargar_niveles(diccionario, nivel_actual)

#if diccionario_categorias_nivel:
#    lista_palabras = diccionario_a_lista(diccionario_categorias_nivel)
#    matriz_principal = cargar_matriz_principal(lista_palabras)


#    mostrar_matriz(matriz_principal)

#else:
#    print("No hay palabras para el nivel actual.")



#mostrar_matriz(matriz_principal)
"$$$$"
#puntos = jugar_juego (matriz_principal,diccionario_categorias_nivel,diccionario,vidas,puntos,nivel_actual,lista_palabras,errores,bandera_comodin_personalizado,bandera_comodin_palabra_categoria,bandera_emparejar_palabras,nombre_jugador)



#continuar = input ("desea juga de nuevo? ")

#if continuar == "no":
#    path = "datos\\puntaje.json"
#
#    "$$$$"
#    #guardar_puntaje_ordenado(path,nombre_jugador, puntos)

pygame.quit()


