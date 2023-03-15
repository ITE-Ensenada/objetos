import pygame, sys
from pygame.locals import *

def registroEventos(player):
    for event in pygame.event.get():
        print(event)

        #Detecta un evento donde se oprima una tecla para realizar una accion especifica
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:  #Si se oprime la flecha abajo, el personaje cambia su direccion
                player.direction = 'down'
            
            if event.key == pygame.K_UP:    #Si se oprime la flecha arriba, el personaje cambia su direccion
                player.direction = 'up'
            
            if event.key == pygame.K_LEFT:  #Si se oprime la flecha izquierda, el personaje cambia su direccion
                player.direction = 'left'
            
            if event.key == pygame.K_RIGHT: #Si se oprime la flecha derecha, el personaje cambia su direccion
                player.direction = 'right'

            #Con la letra ESCAPE se sale del juego (SE AGREGO PARA FACILIDAD DE TESTEO)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit() 

        if event.type == QUIT:              #Si se detecta que se cierra la ventana se cierra el juego 
            pygame.quit()
            sys.exit()

