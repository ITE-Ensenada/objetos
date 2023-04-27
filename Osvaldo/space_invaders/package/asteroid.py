'''Descripcion: Este archivo contiene la clase Asteroid.
                La cual se encarga de representar un asteroide'''

import random
import pygame as pg
from package.settings import ANCHO, ASTEROID_SPEED, ASTEROID_LIFE
from package.subpackage.clase_base import Esqueleto

class Asteroid(Esqueleto):
    ''' Clase que representa un asteroide'''

    def __init__(self, game):

        super().__init__( # Inicializar clase padre
            game,
            random.randint(0, ANCHO - 90),
            -138,
            self.create_sprites(),
            ASTEROID_LIFE)

        self.rect = self.collition_rect() # Rectangulo para deteccion de colisiones


    def collition_rect(self):
        '''Metodo que se encarga de crear el rectangulo de colisiones'''

        rect = self.sprites.get_rect() # Rectangulo para deteccion de colisiones

        rect.x = self.pos[0] # Actualizar la posicion en x del rectangulo de colisiones
        rect.y = self.pos[1] # Actualizar la posicion en y del rectangulo de colisiones

        return rect


    def create_sprites(self):
        '''Metodo que se encarga de crear los sprites del asteroide'''

        sprite = pg.image.load('Assets/Asteroid/Asteroid0.png').convert_alpha()
        sprite = pg.transform.scale(sprite, (90, 138)) # Scale del sprite

        return sprite # Retornar sprites


    def movement(self):
        ''' Metodo que se encarga de mover el asteroide'''

        self._pos_y += ASTEROID_SPEED * self.game.delta_time # Mover el asteroide en y

        self.rect = self.collition_rect() # Actualizar el rectangulo de colisiones


    def draw(self):
        '''Dibujar el asteroide'''

        self.game.screen.blit(self.sprites, (self.pos[0], self.pos[1])) # Dibujar el asteroide

        pg.draw.rect(self.game.screen, 'red', self.rect, 2) # Dibujar el rectangulo de colisiones

    def update(self):
        '''Actualizar asteroide'''

        self.movement() # Mover el asteroide

        self.draw() # Dibujar el asteroide
