import pygame
from Package import *

pygame.init()   #Inicio de pygame


window          #Creacion de una ventana

while True:

    registrarEventos()      #Se manda llamar la funcion registrar eventos del Package, events.py
    
    pygame.display.update() #Se actualiza la pantalla