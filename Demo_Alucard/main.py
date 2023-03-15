import pygame, sys
from pygame.locals import *
from Package1 import *



pygame.init()

#Declaracion de objetos
player = Alicard()                     #Objeto que controla al personaje
screen = Set_display()                 #Objeto que controla la pantalla
fpsClock = pygame.time.Clock()         #Objeto que ayuda a rastrear el tiempo

while True: #Ciclo del juego
    
    screen.backgroungColor()   #Pinta el fondo de pantalla

    #Evalua la direccion del objeto player y ocasiona cambie de direccion
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
    
    #screen.SCREEN.blit(player.personajeImg, (player.personajeX, player.personajeY))    #En caso de no usarse la linea de codigo 65 se puede usar esta
    screen.drawImagen(player.personajeImg, player.personajeX, player.personajeY)        #Dibuja una imagen sobre otra (Dibuja la imagen del personaje sobre el display)

    registroEventos(player) #Registra los eventos que suceden

    pygame.display.update()                 #Actualiza el display
    fpsClock.tick(screen.FPS)