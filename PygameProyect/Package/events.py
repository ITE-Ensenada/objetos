import pygame, sys

def registrarEventos():

    for event in pygame.event.get():
        #Registro de eventos con el teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        #Registro de QUIT
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
