import pygame, sys
from pygame.locals import *

def registroEventos(player): #Evalua y registra un evento
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

def do_action(player): #Realiza una evaluacion para determinar que hara el objeto dado
    
    if player.direction == 'right':
        player.move_right()
        if player.personajeX >= 796:
            player.direction = 'down'
    elif player.direction == 'down':
        player.move_down()
        if player.personajeY >= 564:
            player.direction = 'left'
    elif player.direction == 'left':
        player.move_left()
        if player.personajeX <= 20:
            player.direction = 'up'
    elif player.direction == 'up':
        player.move_up()
        if player.personajeY <= 20:
            player.direction = 'right'