import pygame
from logica import *
"""
funciones que se encargan de cargar los elementos visuales en la pantalla
"""
def crear_boton(pantalla, posicion, dimension, texto=None, fuente=None, path_imagen = None):
    boton = {}
    boton["estado"] = False
    boton["pantalla"] = pantalla
    boton["posicion"] = posicion #tupla
    boton["dimension"] = dimension #tupla
    boton["superficie"] = pygame.Surface(dimension)
    
    if path_imagen != None:
        imagen = pygame.image.load(path_imagen)
        print(f"probando si cargan las imagenes...: {path_imagen}")
        
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

        if boton["rectangulo"].collidepoint(x,y) :
            categoria = boton["categoria"]
            x,y =boton["posicion"]
            print(boton["estado"])

            
                
            
            bandera_primera_categoria, contador = encontrar_categoria(lista_amarillos,amarillo,contador,lista_usados,guardar_boton,boton,categoria,bandera_primera_categoria,lista_categorias,x,y,verde,COLOR_PANTALLA,ventana_principal)
            enmarcar_imagen(contador,amarillo,lista_amarillos,lista_usados,boton,x,y,verde,COLOR_PANTALLA,ventana_principal)
            verificar_contador(contador,lista_usados,amarillo,lista_amarillos,verde,COLOR_PANTALLA,ventana_principal)

            #        x,y = boton["posicion"]
            #        boton ["estado"] = False
            #        print(boton)
            #        
            #        enmarcar_imagen(contador,amarillo,lista_amarillos,lista_usados,boton,x,y,verde,COLOR_PANTALLA,ventana_principal)
                    
            
            
                
    return bandera_primera_categoria,contador


def enmarcar_imagen(contador,amarillo,lista_amarillos,lista_usados,boton,x,y,color,COLOR_PANTALLA,ventana_principal):

    if boton["estado"] == True and boton not in lista_amarillos:
        
        
        
        print("desactiva")

        pygame.draw.rect(ventana_principal, COLOR_PANTALLA, (x-5,y-5,110,110))
        boton["estado"] = False

    elif boton["estado"] == False and boton not in lista_amarillos:
        #print(lista_amarillos)
        pygame.draw.rect(ventana_principal, color, (x-5,y-5,110,110))
        
        
        
        
        print("activa")
        
        boton["estado"] = True
    
    elif boton["estado"] == None:
        pygame.draw.rect(ventana_principal, amarillo, (x-5,y-5,110,110))
        
        boton["estado"] = None
    


def encontrar_categoria (lista_amarillos,amarillo,contador,lista_usados,guardar_boton,boton,categoria,bandera_primera_categoria,lista_categorias,x,y,verde,COLOR_PANTALLA,ventana_principal):

    if bandera_primera_categoria == True and boton["estado"] != None:
        print("primero")
        numero = contador[0]
        numero += 1
        contador[0] = numero
        print(contador)

        guardar_boton.append(boton)
        lista_usados.append(boton)
        lista_categorias.append(categoria)
        bandera_primera_categoria = False

    elif bandera_primera_categoria == False and boton["estado"] != None:
        
        if boton["estado"] == False: #and boton != guardar_boton[0]:
            
            if len(lista_categorias) > 0 and lista_categorias[-1] == categoria:  
                
                numero = contador[0]
                numero += 1
                contador[0] = numero
                print(contador)
                print("entro en categoria ==")
                
                lista_usados.append(boton)
                print("Las categorías son iguales.")

                # if contador[0] == 4:

                #     for boton in lista_usados:

                #         x,y = boton["posicion"]
                #         boton ["estado"] = False

                #         numero = contador[0]
                #         numero = 0
                #         contador[0] = numero
                #         print(contador)

                        # enmarcar_imagen(contador,amarillo,lista_amarillos,lista_usados,boton,x,y,verde,COLOR_PANTALLA,ventana_principal)

            elif lista_categorias[-1] != categoria:

                lista_usados.append(boton)
                for boton in lista_usados:

                    x,y = boton["posicion"]
                    boton ["estado"] = True

                    enmarcar_imagen(contador,amarillo,lista_amarillos,lista_usados,boton,x,y,verde,COLOR_PANTALLA,ventana_principal)

                    print("entro en categoria !=")
                    contador[0] = 1
                    lista_categorias = []
                    
                    bandera_primera_categoria = True
                
                
            
                # for boton in lista_usados:

                #     x,y = boton["posicion"]
                #     boton ["estado"] = True
                #     numero = contador[0]
                #     numero = 0
                #     contador[0] = numero
                    
                #     enmarcar_imagen(contador,amarillo,lista_amarillos,lista_usados,boton,x,y,verde,COLOR_PANTALLA,ventana_principal)
                    
    # if contador[0] == 4:

    #     for boton in lista_usados:

    #         x,y = boton["posicion"]
    #         boton ["estado"] = False
    #         enmarcar_imagen(contador,amarillo,lista_amarillos,lista_usados,boton,x,y,verde,COLOR_PANTALLA,ventana_principal)

    #         numero = contador[0]
    #         numero = 0
    #         contador[0] = numero
    #         print(contador)

    return bandera_primera_categoria ,contador
    


def verificar_contador(contador,lista_usados,amarillo,lista_amarillos,verde,COLOR_PANTALLA,ventana_principal):
    if contador[0] == 4:

        for boton in lista_usados:
            
            x,y = boton["posicion"]
            boton ["estado"] = False

            enmarcar_imagen(contador,amarillo,lista_amarillos,lista_usados,boton,x,y,verde,COLOR_PANTALLA,ventana_principal)
            
            numero = contador[0]
            numero = 0
            contador[0] = numero
            print(contador)
    

