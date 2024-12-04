elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton["rectangulo"].collidepoint(evento.pos):
                print("clickea2")