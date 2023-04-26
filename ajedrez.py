# pylint: disable=C0103
# pylint: disable=W0105
"""juego del ajedrez"""
import sys
import pygame
from pygame.locals import __all__
"""juego del ajedrez"""
import pygame
import sys
from pygame.locals import *
pygame.init()
pantallax = 720
pantallay = 720
SCREEN = pygame.display.set_mode((pantallax,pantallay))
pygame.display.set_caption('Ajedrez')
fondo = pygame.image.load('tablero1.png')
fondo = pygame.transform.scale(fondo, (720, 720))


Pieza_1 = pygame.image.load('torre.png')
Pieza_1 = pygame.transform.scale(Pieza_1, (90, 90))
Pieza_2 = pygame.image.load('caballo.png')
Pieza_2 = pygame.transform.scale(Pieza_2, (90, 90))
Pieza_3 = pygame.image.load('alfil.png')
Pieza_3 = pygame.transform.scale(Pieza_3, (90, 90))
Pieza_4 = pygame.image.load('rey.png')
Pieza_4 = pygame.transform.scale(Pieza_4, (90, 90))
Pieza_5 = pygame.image.load('reyna.png')
Pieza_5 = pygame.transform.scale(Pieza_5, (90, 90))
Pieza_6 = pygame.image.load('alfil.png')
Pieza_6 = pygame.transform.scale(Pieza_6, (90, 90))
Pieza_7 = pygame.image.load('caballo.png')
Pieza_7 = pygame.transform.scale(Pieza_7, (90, 90))
Pieza_8 = pygame.image.load('torre.png')
Pieza_8 = pygame.transform.scale(Pieza_8, (90, 90))

Pieza_X1 = 0
Pieza_Y1 = 0
Pieza_X2 = 90
Pieza_Y2 = 0
Pieza_X3 = 180
Pieza_Y3 = 0
Pieza_X4 = 270
Pieza_Y4 = 0
Pieza_X5 = 360
Pieza_Y5 = 0
Pieza_X6 = 450
Pieza_Y6 = 0
Pieza_X7 = 540
Pieza_Y7 = 0
Pieza_X8 = 630
Pieza_Y8 = 0



Pieza__X1 = 0
Pieza_Y1 = 0
Pieza_X2 = 90
Pieza_Y2 = 0
Pieza_X3 = 180
Pieza_Y3 = 0
Pieza_X4 = 270
Pieza_Y4 = 0
Pieza_X5 = 360
Pieza_Y5 = 0
Pieza_X6 = 450
Pieza_Y6 = 0
Pieza_X7 = 540
Pieza_Y7 = 0
Pieza_X8 = 630
Pieza_Y8 = 0
>>>>>>> 82c43fb918533e9ef88ff0dc7bcf5a73a7fb78bf
while True: # the main game loop
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(fondo, (0, 0))
    SCREEN.blit(Pieza_1, (Pieza_X1, Pieza_Y1))
<<<<<<< HEAD

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
=======
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  

            #TorreIzq
            if event.key == K_DOWN:
                Pieza_Y1 = Pieza_Y1+90
            if event.key == K_UP:
                Pieza_Y1 = Pieza_Y1-90
            if event.key == K_RIGHT:
                Pieza_X1 = Pieza_X1+90
            if event.key == K_LEFT:
                Pieza_X1 = Pieza_X1-90
pygame.display.update()


'''Caballo izq
if event.key==K_0:
personajeY2 = personajeY2+180
personajeX2 = personajeX2+90
if event.key==K_7:
personajeY2 = personajeY2+180
personajeX2 = personajeX2-90
if event.key==K_8:
personajeY2 = personajeY2-180
personajeX2 = personajeX2+90
if event.key==K_9:
personajeY2 = personajeY2-180
personajeX2 = personajeX2-
if event.key==K_w:
personajeY3 = personajeY3-90
if event.key==K_s:
personajeY3 = personajeY3+90
if event.key==K_d:
personajeX3 = personajeX3+90
if event.key==K_a:
personajeX3 = personajeX3-90
if event.key==K_w:
personajeY4 = personajeY4-90
if event.key==K_s:
personajeY4 = personajeY4+90
if event.key==K_d:
personajeX4 = personajeX4+90
if event.key==K_a:
personajeX4 = personajeX4-90
if event.key==K_w:
personajeY5 = personajeY5-90
if event.key==K_s:
personajeY5 = personajeY5+90
if event.key==K_d:
personajeX5 = personajeX5+90
if event.key==K_a:
personajeX5 = personajeX5-90
if event.key==K_w:
personajeY6 = personajeY6-90
if event.key==K_s:
personajeY6 = personajeY6+90
if event.key==K_d:
personajeX6 = personajeX6+90
if event.key==K_a:
personajeX6 = personajeX6-90
Caballo Der
if event.key==K_4:
personajeY7 = personajeY7+180
personajeX7 = personajeX7+90
if event.key==K_1:
personajeY7 = personajeY7+180
personajeX7 = personajeX7-90
if event.key==K_2:
personajeY7 = personajeY7-180
personajeX7 = personajeX7+90
if event.key==K_3:
personajeY7 = personajeY7-180
personajeX7 = personajeX7-90
if event.key==K_w:
personajeY8 = personajeY8-90
if event.key==K_s:
personajeY8 = personajeY8+90
if event.key==K_d:
personajeX8 = personajeX8+90
if event.key==K_a:
personajeX8 = personajeX8-90'''
