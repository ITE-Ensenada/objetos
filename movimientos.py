import pygame
from pygame.locals import *
pygame.init()
caminaDerecha = [pygame.image.load('imagenes/run01.png'),
    pygame.image.load('imagenes/run02.png'),
        pygame.image.load('imagenes/run03.png')]
        
caminaIzquierda = [pygame.image.load('imagenes/run01_izq.png'),
        pygame.image.load('imagenes/run02_izq.png'),
        pygame.image.load('imagenes/run03_izq.png')]  

Quieto = pygame.image.load('imagenes/estatico.png')  

Salto = pygame.image.load('imagenes/salto.png')