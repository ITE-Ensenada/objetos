"""Este clase es la que se encarga de que la torreta pueda disparar. """
import random
import pygame

a= random.randint(1, 10)
# Constantes del juego
ANCHO = 1280
ALTO = 720
# Constantes del juego
NEGRO = (0, 0, 0)

class Bala(pygame.sprite.Sprite):
    """Esta es una clase de ejemplo que realiza una tarea específica."""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocidad = -10

    def update(self):
        """Es la actualizacion de la posion de la bala"""
        # Actualización de la posición de la bala
        self.rect.y += self.velocidad
        if self.rect.bottom < 0:
            self.kill()