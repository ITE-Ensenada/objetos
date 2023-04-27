"""Este clase tiene un generador random para que aparescan aviones aleatoriamente. """
import random
import pygame


# Constantes del juego
ANCHO = 1280
ALTO = 720
# Cargar imágenes
IMAGEN_AVION = pygame.image.load("avion.png")
# Definición de la clase Avion
class Avion(pygame.sprite.Sprite):
    """Clase que representa un avion en el juego.

    El avion cae desde arriba y aparece de forma random.
    """

    def __init__(self):
        super().__init__()
        self.imagen_original = IMAGEN_AVION
        self.imagen = pygame.image.load('avion.png').convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen_original, (80, 60))
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.velocidad = random.randrange(1, 8)

    def update(self):
        """Actualizacion de la posicion del avion en el juego.
        
        Es para regresar la posicion de la torreta a su lugar
        """
        # Actualización de la posición del avión
        self.rect.y += self.velocidad
        if self.rect.top > ALTO:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.velocidad = random.randrange(1, 8)


