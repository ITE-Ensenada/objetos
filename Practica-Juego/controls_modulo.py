import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)
                    
def handle_keys(event_key):
    if event.type == pygame.KEYDOWN:
            #verificar cual fue el evento
            if event.key == pygame.K_UP:
                personajeY -= 10
            if event.key == pygame.K_DOWN:
                personajeY += 10
            if event.key == pygame.K_LEFT:
                personajeX -= 10
            if event.key == pygame.K_RIGHT:
                personajeX += 10

        
