"""Este clase es la que se encarga de que la torreta pueda funcione corretamente con todas sus funciones. """
import random
import pygame
from clasebala import Bala

x= random.randint(1, 10)
# Constantes del juego
ANCHO = 1280
ALTO = 720

# Cargar imágenes
#IMAGEN_TORRETA = pygame.image.load("torreta.png")

class Torreta(pygame.sprite.Sprite):
    """Clase que representa la torreta en el juego.

    La torreta se mueve de izquierda a derecha y tambien puede disparar.
    """
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("torreta.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 10
        self.velocidad = 0

    def update(self):
        """Es se encarga de la actualizacion de la posicion de la torreta."""
        # Actualización de la posición de la torreta
        self.rect.x += self.velocidad
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.left < 0:
            self.rect.left = 0

    def disparar(self):
        """Esta se encarga de la creacion de la bala para que la torreta pueda disparar de donde sea."""
        # Creación de una bala en la posición de la torreta
        bala = Bala(self.rect.centerx, self.rect.top)
        balas.add(bala)
        todos_los_sprites.add(bala)
        # Para mover la torreta de izquierda a derecha
    def move_left(self):
        """Esta se encarga mover la torreta de izquierda a derecha con las teclas."""
        self.rect.x -= 5
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        """Esta se encarga mover la torreta de izquierda a derecha con las teclas."""
        self.rect.x += 5