"""
Este es un juego de batalla aerea que se trata de disparale a los aviones para derrivarlos.
Autor: Sebastián Carrillo
Fecha: 26/04/2023
"""

import sys
import random
import pygame
from claseavion import Avion
from clasebala import Bala
from clasetorreta import Torreta


x = random.randint(1, 10)
# Inicialización de Pygame
pygame.init()


# Establecer la ventana y el título
WIDTH = 1280
HEIGHT =720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Batalla aérea")
# Constantes del juego
ANCHO = 1280
ALTO = 720
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
FPS = 60
clock = pygame.time.Clock()

# Fondo de juego
fondo = pygame.image.load("fondo.png").convert()
# Definición de la clase Torreta

# Definición de la clase Bala

# Definición de la clase Avion


# Creación de objetos del juego
todos_los_sprites = pygame.sprite.Group()
balas = pygame.sprite.Group()
aviones = pygame.sprite.Group()

torreta = Torreta()
todos_los_sprites.add(torreta)

for i in range(8):
    avion = Avion()
    todos_los_sprites.add(avion)
    aviones.add(avion)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de la torreta
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        torreta.move_left()
    elif keys[pygame.K_RIGHT]:
        torreta.move_right()

    # Actualización de objetos
    todos_los_sprites.update()

    # Detección de colisiones
    for bala in balas:
        colisiones = pygame.sprite.spritecollide(bala, aviones, True)
        for avion in colisiones:
            avion = Avion()
            todos_los_sprites.add(avion)
            aviones.add(avion)

    # Eliminar aviones al llegar al final de la pantalla
    for avion in aviones:
        if avion.rect.bottom > HEIGHT:
            aviones.remove(avion)
            todos_los_sprites.remove(avion)

    # Dibujado de objetos
    screen.blit(fondo, (0, 0))
    
    #todos_los_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
