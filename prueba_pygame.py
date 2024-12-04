import pygame
from modules.visuales import *

TAMAÑO_VENTANA = (800, 500)
COLOR_PANTALLA = (49, 100, 247)
TAMAÑO_BOTON = (100, 100)
ESPACIO_ENTRE_BOTONES = 10
FILAS = 4
COLUMNAS = 4
IMAGENES = [
    "imagenes/batidora.jpg","imagenes/bombero.jpg","imagenes/cafetera.jpg","imagenes/cerdo.jpg",
    "imagenes/chef.jpg","imagenes/corazon.jpg","imagenes/diamante.jpg","imagenes/doctor.jpg",
    "imagenes/gallina.jpg","imagenes/licuadora.jpg","imagenes/oveja.jpg","imagenes/picas.jpg",
    "imagenes/policia.jpg","imagenes/tostadora.jpg","imagenes/trebol.jpg","imagenes/vaca.jpg"
]



pygame.init()

ventana_principal = pygame.display.set_mode(TAMAÑO_VENTANA)
pygame.display.set_caption("Agrupados")

ancho_cuadricula = COLUMNAS * TAMAÑO_BOTON[0] + (COLUMNAS - 1) * ESPACIO_ENTRE_BOTONES
alto_cuadricula = FILAS * TAMAÑO_BOTON[1] + (FILAS - 1) * ESPACIO_ENTRE_BOTONES

margen_izquierdo = (TAMAÑO_VENTANA[0] - ancho_cuadricula) // 2
margen_superior = (TAMAÑO_VENTANA[1] - alto_cuadricula) // 2


botones = []
for fila in range(FILAS):
    for columna in range(COLUMNAS):
        x = margen_izquierdo + columna * (TAMAÑO_BOTON[0] + ESPACIO_ENTRE_BOTONES)
        y = margen_superior + fila * (TAMAÑO_BOTON[1] + ESPACIO_ENTRE_BOTONES)
        
        indice_imagen = fila * COLUMNAS + columna
        boton = crear_boton(
            pantalla = ventana_principal,
            posicion = (x, y),
            dimension = TAMAÑO_BOTON,
            path_imagen=IMAGENES[indice_imagen]
        )
        botones.append(boton)


bandera_juego = True 


while bandera_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera_juego = False
        # elif evento.type == pygame.MOUSEBUTTONDOWN:
        #     if boton["rectangulo"].collidepoint(evento.pos):
        #         print("clickea2")
    
    ventana_principal.fill(COLOR_PANTALLA)
    
    for boton in botones:
        dibujar(boton)
    
    pygame.display.update()
    
    
pygame.quit()
