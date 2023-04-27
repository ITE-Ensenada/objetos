"""Codigo principal de mi juego"""
import sys
import pygame

from Confi import *
from Nivel import Level

pygame.init()
screen = pygame.display.set_mode((Ancho_Pantalla,Alto_Pantalla))
clock = pygame.time.Clock()
level = Level(Mapa,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)
