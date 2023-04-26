# pylint: disable=C0103
# pylint: disable=W0105
"""juego del ajedrez"""
import sys
import pygame
from pygame.locals import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

pygame.init()

pantallax = 640
pantallay = 640
SCREEN = pygame.display.set_mode((pantallax, pantallay), 0, 32)
pygame.display.set_caption('Ajedrez')

fondo = pygame.image.load('tablero1.png')
fondo = pygame.transform.scale(fondo, (640, 640))

Pieza_1 = pygame.image.load('torre.png')
Pieza_1 = pygame.transform.scale(Pieza_1, (80, 80))

Pieza_X1 = 0
Pieza_Y1 = 0

while True:  # the main game loop
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(fondo, (0, 0))
    SCREEN.blit(Pieza_1, (Pieza_X1, Pieza_Y1))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # TorreIzq
            if event.key == K_DOWN:
                Pieza_Y1 = Pieza_Y1 + 80
            if event.key == K_UP:
                Pieza_Y1 = Pieza_Y1 - 80
            if event.key == K_RIGHT:
                Pieza_X1 = Pieza_X1 + 80
            if event.key == K_LEFT:
                Pieza_X1 = Pieza_X1 - 80

    pygame.display.update()
