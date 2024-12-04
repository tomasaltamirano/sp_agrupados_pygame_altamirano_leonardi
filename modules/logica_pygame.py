import pygame

def dibujar_imagen(pantalla, path: str, resolucion: tuple, posicion: tuple) -> None:
    imagen = pygame.image.load(path)
    imagen_escala = pygame.transform.scale(imagen, resolucion)
    pantalla.blit(imagen_escala, posicion)


def ejecutar_eventos( x: int, y: int,fondo_pantalla,color,lista_banderas) -> None:

    
    if x >= 499 and x <= 596 and y >= 201 and y <= 298 :
        
        #pygame.draw.rect(fondo_pantalla, color, (495, 195, 110, 110))
        
        contador += 1
        
        marcar_desmarcar_imagen(lista_banderas[0],fondo_pantalla,color,contador,495,195,110,110)
        #lista_banderas[0] = True
        print("corazon")
        
    elif  x >= 631 and x <= 727 and y >= 201 and y <= 298 :
        pygame.draw.rect(fondo_pantalla, color, (626, 195, 110, 110))
        lista_banderas[1] = True
        print("trebol")
    elif x >= 762 and x <= 858 and y >= 201 and y <= 298 :
        pygame.draw.rect(fondo_pantalla, color, (756, 195, 110, 110))
        lista_banderas[2] = True
        print("picas")
    elif x >= 893 and x <= 989 and y >= 201 and y <= 298 :
        pygame.draw.rect(fondo_pantalla, color, (885, 195, 110, 110))
        lista_banderas[3] = True
        print("diamante")
    elif x >= 499 and x <= 596 and y >= 350 and y <= 446 :
        pygame.draw.rect(fondo_pantalla, color, (495,345, 110, 110))
        lista_banderas[4] = True
        print("pollo")
    elif x >= 631 and x <= 727 and y >= 350 and y <= 446 :
        pygame.draw.rect(fondo_pantalla, color, (626,345, 110, 110))
        lista_banderas[5] = True
        print("cerdo")
    elif x >= 762 and x <= 858 and y >= 350 and y <= 446 :
        pygame.draw.rect(fondo_pantalla, color, (755,345, 110, 110))
        lista_banderas[6] = True
        print("oveja")
    elif x >= 893 and x <= 989 and y >= 350 and y <= 446 :
        pygame.draw.rect(fondo_pantalla, color, (885,345, 110, 110))
        lista_banderas[7] = True
        print("vaca")
    elif x >= 499  and x <= 596 and y >= 500 and y <= 596 :
        pygame.draw.rect(fondo_pantalla, color, (495,493, 110, 110))
        lista_banderas[8] = True
        print("bombero")
    elif x >= 631  and x <= 727 and y >= 500 and y <= 596 :
        pygame.draw.rect(fondo_pantalla, color, (626,493, 110, 110))
        lista_banderas[9] = True
        print("medico")
    elif x >= 762  and x <= 858 and y >= 500 and y <= 596 :
        pygame.draw.rect(fondo_pantalla, color, (756,493, 110, 110))
        lista_banderas[10] = True
        print("chef")
    elif x >= 893  and x <= 989 and y >= 500 and y <= 596 :
        pygame.draw.rect(fondo_pantalla, color, (885,493, 110, 110))
        lista_banderas[11] = True
        print("policia")
    elif x >= 499  and x <= 596 and y >= 650 and y <= 746 :
        pygame.draw.rect(fondo_pantalla, color, (495,645, 110, 110))
        lista_banderas[12] = True
        print("batidora")
    elif x >= 631  and x <= 727 and y >= 650 and y <= 746 :
        pygame.draw.rect(fondo_pantalla, color, (626,645, 110, 110))
        lista_banderas[13] = True
        print("licuadora")
    elif x >= 762  and x <= 858 and y >= 650 and y <= 746 :
        pygame.draw.rect(fondo_pantalla, color, (756,645, 110, 110))
        lista_banderas[14] = True
        print("tostadora")
    elif x >= 893  and x <= 989 and y >= 650 and y <= 746 :
        pygame.draw.rect(fondo_pantalla, color, (885,645, 110, 110))
        lista_banderas[15] = True
        print("cafetera")
    return contador

def marcar_desmarcar_imagen(bandera,fondo_pantalla,color,contador,x,y,ancho,largo):
    if bandera == False and contador == 1:
        pygame.draw.rect(fondo_pantalla, color, (x,y,ancho,largo))
        
