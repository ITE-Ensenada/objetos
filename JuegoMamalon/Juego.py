'''Codigo principal de mi juego'''

import sys
import pygame

from confi import ALTO_PANTALLA, ANCHO_PANTALLA, MAPA
from nivel import Level

pygame.init()
screen = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
clock = pygame.time.Clock()
level = Level(MAPA,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)
