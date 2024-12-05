import pygame
from logica import *
"""
funciones que se encargan de cargar los elementos visuales en la pantalla
"""

def mostrar_mensaje(ventana_principal, tamaño_ventana, fuente, mensaje):
    """Muestra un mensaje en un cuadro más pequeño en la pantalla."""
    # Dimensiones del cuadro (ajusta según lo necesites)
    ancho_cuadro = 400
    alto_cuadro = 70
    x_cuadro = (tamaño_ventana[0] - ancho_cuadro) // 2
    y_cuadro = 60
    # x_cuadro = 130
    # y_cuadro = 50

    # Dibuja un cuadro para el mensaje
    color_cuadro = (38, 76, 153)  
    color_borde = (249, 125, 27)  
    pygame.draw.rect(ventana_principal, color_cuadro, (x_cuadro, y_cuadro, ancho_cuadro, alto_cuadro))
    pygame.draw.rect(ventana_principal, color_borde, (x_cuadro, y_cuadro, ancho_cuadro, alto_cuadro), 3)  # Borde

    # Renderiza el mensaje
    texto = fuente.render(mensaje, True, (255, 255, 255))  # Texto en blanco
    texto_rect = texto.get_rect(center=(x_cuadro + ancho_cuadro // 2, y_cuadro + alto_cuadro // 2))

    ventana_principal.blit(texto, texto_rect)  # Dibuja el texto dentro del cuadro

    # Actualiza la pantalla y espera
    pygame.display.flip()
    pygame.time.delay(2000)
    
    
def mostrar_puntos_y_vidas(ventana_principal, fuente, puntuacion, vidas):
    texto_puntos = fuente.render(f"Puntos: {puntuacion}", True, (255, 255, 255))
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, (255, 255, 255))
    
    ventana_principal.blit(texto_puntos, (20, 20))  # Posición para los puntos
    ventana_principal.blit(texto_vidas, (20, 60))


def crear_boton(pantalla, posicion, dimension, texto=None, fuente=None, path_imagen = None):
    boton = {}
    boton["estado"] = False
    boton["pantalla"] = pantalla
    boton["posicion"] = posicion #tupla
    boton["dimension"] = dimension #tupla
    boton["superficie"] = pygame.Surface(dimension)
    
    if path_imagen != None:
        
        imagen = pygame.image.load(path_imagen)
        #! error aca!!
        # print(f"probando si cargan las imagenes...: {path_imagen}")
        
        boton["superficie"] = pygame.transform.scale(imagen, boton["dimension"])
        
    boton["rectangulo"] = boton["superficie"].get_rect(topleft=boton["posicion"])
    return boton

def dibujar(boton):
    boton["pantalla"].blit(boton["superficie"], boton["posicion"])
    
    
#==========================================================
def crear_botones_imagenes(ventana_principal:tuple, imagenes:list, FILAS:int, COLUMNAS:int, TAMAÑO_BOTON, ESPACIO_ENTRE_BOTONES, TAMAÑO_VENTANA) -> list:
    ancho_cuadricula = COLUMNAS * TAMAÑO_BOTON[0] + (COLUMNAS - 1) * ESPACIO_ENTRE_BOTONES
    alto_cuadricula = FILAS * TAMAÑO_BOTON[1] + (FILAS - 1) * ESPACIO_ENTRE_BOTONES

    margen_izquierdo = (TAMAÑO_VENTANA[0] - ancho_cuadricula) // 2 #podes usar un numero fijo y tambien anda
    margen_superior = (TAMAÑO_VENTANA[1] - alto_cuadricula) // 2


    botones = []
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            x = margen_izquierdo + columna * (TAMAÑO_BOTON[0] + ESPACIO_ENTRE_BOTONES)
            y = margen_superior + fila * (TAMAÑO_BOTON[1] + ESPACIO_ENTRE_BOTONES)
            
            ruta_imagen, categoria = imagenes.pop()
            boton = crear_boton(

                
                pantalla = ventana_principal,
                posicion = (x, y),
                dimension = TAMAÑO_BOTON,
                path_imagen=ruta_imagen
            )
            boton["categoria"] = categoria
            botones.append(boton)
            
    return botones


def seleccionar_imagenes(amarillo,lista_amarillos,contador,lista_usados,guardar_boton,botones,x,y,verde,COLOR_PANTALLA,ventana_principal,bandera_primera_categoria,lista_categorias):
    for boton in botones:
        if boton["rectangulo"].collidepoint(x,y) and boton["estado"] == True:
            contador[0] -=1
            # print(contador)
        if boton["rectangulo"].collidepoint(x,y) and boton["estado"] == False:
            contador[0] += 1
            # print(contador)
        if boton["rectangulo"].collidepoint(x,y): 
            
                contador[0] -= 1

                categoria = boton["categoria"]
                x,y =boton["posicion"]
                # print(boton["estado"])

                if boton not in lista_amarillos:
                    print(categoria)
                    # print(boton["estado"])
                    bandera_primera_categoria, contador,lista_usados = encontrar_categoria(lista_amarillos,amarillo,contador,lista_usados,guardar_boton,boton,categoria,bandera_primera_categoria,lista_categorias,x,y,verde,COLOR_PANTALLA,ventana_principal)
                    enmarcar_imagen(contador,amarillo,lista_amarillos,lista_usados,boton,x,y,verde,COLOR_PANTALLA,ventana_principal)

    return bandera_primera_categoria,contador, categoria


def enmarcar_imagen(contador,amarillo,lista_amarillos,lista_usados,boton,x,y,color,COLOR_PANTALLA,ventana_principal):

    if boton["estado"] == True and boton not in lista_amarillos:
        
        
        
        # print("desactiva")

        pygame.draw.rect(ventana_principal, COLOR_PANTALLA, (x-5,y-5,110,110))
        boton["estado"] = False

    elif boton["estado"] == False and boton not in lista_amarillos:
        #print(lista_amarillos)
        pygame.draw.rect(ventana_principal, color, (x-5,y-5,110,110))
        
        
        
        
        # print("activa")
        
        boton["estado"] = True
    
    elif boton["estado"] == None:
        pygame.draw.rect(ventana_principal, amarillo, (x-5,y-5,110,110))
        
        boton["estado"] = None

def encontrar_categoria (lista_amarillos,AMARILLO,contador,lista_usados,guardar_boton,boton,categoria,bandera_primera_categoria,lista_categorias,x,y,verde,COLOR_PANTALLA,ventana_principal):
    # print(bandera_primera_categoria,"dsadasdasdasdasdas")
    if bandera_primera_categoria == True and boton["estado"] == False:
        
        numero = contador[0]
        numero += 1
        contador[0] = numero
        # print(contador)

        guardar_boton.append(boton)
        lista_usados.append(boton)
        lista_categorias.append(categoria)
        boton["estado"] = True
        enmarcar_imagen(contador,AMARILLO,lista_amarillos,lista_usados,boton,x,y,verde,COLOR_PANTALLA,ventana_principal)
        
        # print("lista_usados:", lista_usados)
        # print("primero")

        bandera_primera_categoria = False

    elif bandera_primera_categoria == False:
        
        if boton["estado"] == False and boton != guardar_boton[0]:
            # print("holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            if len(lista_categorias) > 0 and lista_categorias[-1] == categoria:  
                
                

                numero = contador[0]
                numero += 1
                contador[0] = numero
                # print(contador)
                # print("entro en categoria ==")
                
                lista_usados.append(boton)
                # print("Las categorías son iguales.")

        
            elif lista_categorias[-1] != categoria:

                
                # print("entro en categoria !=")
                
                lista_usados.append(boton)
                for boton in lista_usados:

                    x,y = boton["posicion"]
                    boton ["estado"] = True
                    # print("borra la lista usados")
                    bandera_primera_categoria 

                    enmarcar_imagen(contador,AMARILLO,lista_amarillos,lista_usados,boton,x,y,verde,COLOR_PANTALLA,ventana_principal)

                # lista_categorias.clear()
                # lista_usados.clear()
                # lista_amarillos.clear()

                
                contador[0] = 0
                
                # print("cambia la bandera a true")
                bandera_primera_categoria = True
                
                encontrar_categoria(lista_amarillos,AMARILLO,contador,lista_usados,guardar_boton,boton,categoria,bandera_primera_categoria,lista_categorias,x,y,verde,COLOR_PANTALLA,ventana_principal)
            

    return bandera_primera_categoria ,contador, lista_usados

def verificar_contador(contador,lista_usados,amarillo,lista_amarillos,lista_categorias, verde,COLOR_PANTALLA,ventana_principal):
    if contador[0] == 4:
        for boton in lista_usados:
            lista_amarillos.append(boton)
        
        for boton in lista_amarillos:
            x,y = boton["posicion"]
            boton ["estado"] = None

            enmarcar_imagen(contador,amarillo,lista_amarillos,lista_usados,boton,x,y,verde,COLOR_PANTALLA,ventana_principal)
            
            numero = contador[0]
            numero = 0
            contador[0] = numero
            # print(contador)
    if contador[0] <= -1:
        contador[0] = 0
    
def cambiar_nivel(nivel_actual, diccionario_categorias, ventana_principal, FILAS, COLUMNAS, TAMAÑO_BOTON, ESPACIO_ENTRE_BOTONES, TAMAÑO_VENTANA, COLOR_PANTALLA, lista_usados, lista_amarillos):
    """
    Cambia al siguiente nivel del juego.
    - Actualiza el nivel.
    - Regenera los botones con las imágenes del nuevo nivel.
    """
    nivel_actual += 1  # Aumenta el nivel.
    lista_usados.clear()  # Limpia las listas.
    lista_amarillos.clear()
    
    print(f"PASASTE AL NIVEL: {nivel_actual}!")

    # Obtiene las imágenes del nuevo nivel.
    imagenes = obtener_imagenes(diccionario_categorias, nivel_actual)
    
    # Crea los botones para el nuevo nivel.
    botones = crear_botones_imagenes(ventana_principal, imagenes, FILAS, COLUMNAS, TAMAÑO_BOTON, ESPACIO_ENTRE_BOTONES, TAMAÑO_VENTANA)

    # Limpia la pantalla.
    ventana_principal.fill((49, 100, 247))

    return nivel_actual, botones

# Permite al usuario ingresar su nombre
def pedir_nombre(ventana_principal, TAMAÑO_VENTANA, fuente):
    # mostrar_mensaje(ventana_principal, TAMAÑO_VENTANA, fuente, "ingresa tu nombre")
    
    reloj = pygame.time.Clock()
    nombre = ""
    ingresar = True
    input_rect = pygame.Rect((TAMAÑO_VENTANA[0] // 2 - 150, TAMAÑO_VENTANA[1] // 2 - 25), (300, 50))

    while ingresar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ingresar = False
                return None  # Salir del programa
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Finaliza ingreso con Enter
                    ingresar = False
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]  # Borra último caracter
                else:
                    nombre += evento.unicode

        ventana_principal.fill((49, 100, 247))  # Fondo azul
        pygame.draw.rect(ventana_principal, (255, 255, 255), input_rect)  # Cuadro de texto
        texto = fuente.render(nombre, True, (0, 0, 0))
        ventana_principal.blit(texto, (input_rect.x + 10, input_rect.y + 10))
        pygame.display.flip()
        reloj.tick(30)

    return nombre

    