'''Descripcion: Este archivo contiene la clase Asteroid.
                La cual se encarga de representar un asteroide'''

import random
import pygame as pg
from package.settings import ANCHO, ASTEROID_SPEED

class Asteroid(pg.sprite.Sprite):
    ''' Clase que representa un asteroide'''

    def __init__(self, game):

        super().__init__() #

        self.game = game # Instancia de la clase Game

        self.pos_x = random.randint(0, ANCHO - 90) # Posicion en x

        self.pos_y = -138 # Posicion en y

        # Sprite 1 del asteroide
        self.sprite0 = pg.image.load('Assets/Asteroid/Asteroid0.png').convert_alpha()
        self.sprite0 = pg.transform.scale(self.sprite0, (90, 138)) # Scale del sprite

        # Sprite 2 del asteroide
        self.sprite1 = pg.image.load('Assets/Asteroid/Asteroid1.png').convert_alpha()
        self.sprite1 = pg.transform.scale(self.sprite1, (90, 138)) # Scale del sprite

        self.current_sprite = self.sprite0 # Sprite actual

        self.rect = self.current_sprite.get_rect() # Rectangulo para deteccion de colisiones

    def movement(self):
        ''' Metodo que se encarga de mover el asteroide'''

        self.pos_y += ASTEROID_SPEED * self.game.delta_time # Mover el asteroide en y

        self.change_sprite() # Cambiar el sprite del asteroide

        self.rect = self.current_sprite.get_rect() # Actualizar el rectangulo de colisiones

        self.rect.x = self.pos_x # Actualizar la posicion en x del rectangulo de colisiones

        self.rect.y = self.pos_y # Actualizar la posicion en y del rectangulo de colisiones


    def change_sprite(self):
        '''Cambiar el sprite del asteroide'''

        if self.current_sprite == self.sprite0:
            self.current_sprite = self.sprite1

    def draw(self):
        '''Dibujar el asteroide'''

        self.game.screen.blit(self.sprite0, (self.pos_x, self.pos_y)) # Dibujar el asteroide

    def update(self):
        '''Actualizar asteroide'''

        self.movement() # Mover el asteroide

        self.draw() # Dibujar el asteroide
