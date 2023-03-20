import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
)
def handle_keys(keys_pressed):
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                personajeY -= 50
            if event.key == pygame.K_DOWN:
                personajeY += 50
            if event.key == pygame.K_LEFT:
                personajeX -= 50
            if event.key == pygame.K_RIGHT:
                personajeX += 50
