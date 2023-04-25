"""juego del ajedrez"""
import pygame
import sys
from pygame.locals import *
pygame.init()

SCREEN = pygame.display.set_mode((720, 720), 20, 32)
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
while True: # the main game loop
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(fondo, (0, 0))
    SCREEN.blit(Pieza_1, (Pieza_X1, Pieza_Y1))
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

