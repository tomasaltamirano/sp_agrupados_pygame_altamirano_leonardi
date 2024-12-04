import pygame
from modules.paths_imagenes import *
from modules.logica_pygame import *

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

 




def dibujar_imagen(pantalla, path: str, resolucion: tuple, posicion: tuple) -> None:
    imagen = pygame.image.load(path)
    imagen_escala = pygame.transform.scale(imagen, resolucion)
    pantalla.blit(imagen_escala, posicion)





#imagen.topleft = (200, 200)


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
            ejecutar_eventos(x, y, fondo_pantalla,VERDE)

        #if imagen.collidepoint():  # Ver si el clic fue sobre la imagen
        #        print("¡Botón presionado!")
    
    

    pygame.display.update()


pygame.quit()