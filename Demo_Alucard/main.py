import pygame, sys
from Package1 import *

pygame.init()

#Declaracion de objetos
player = Alicard()              #Objeto que controla al personaje
screen = Set_display()          #Objeto que controla la pantalla
fpsClock = pygame.time.Clock()  #Objeto que ayuda a rastrear el tiempo

while True:     #Ciclo del juego
    
    screen.backgroungColor()    #Pinta el fondo de pantalla

    do_action(player)           #Evalua la direccion del objeto player y ocasiona cambie de direccion
    
    screen.drawImagen(player.personajeImg, player.personajeX, player.personajeY)    #Dibuja una imagen sobre otra (Dibuja la imagen del personaje sobre el display)
    
    registroEventos(player)     #Registra los eventos que suceden

    pygame.display.update()     #Actualiza el display
    fpsClock.tick(screen.FPS)