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

        self.sprite = self.create_sprites() # Sprite del asteroide

        self.rect = self.collition_rect() # Rectangulo para deteccion de colisiones


    def collition_rect(self):
        '''Metodo que se encarga de crear el rectangulo de colisiones'''

        rect = self.sprite.get_rect() # Rectangulo para deteccion de colisiones

        rect.x = self.pos_x # Actualizar la posicion en x del rectangulo de colisiones
        rect.y = self.pos_y # Actualizar la posicion en y del rectangulo de colisiones

        return rect


    def create_sprites(self):
        '''Metodo que se encarga de crear los sprites del asteroide'''

        sprite = pg.image.load('Assets/Asteroid/Asteroid0.png').convert_alpha()
        sprite = pg.transform.scale(sprite, (90, 138)) # Scale del sprite

        return sprite # Retornar sprites


    def movement(self):
        ''' Metodo que se encarga de mover el asteroide'''

        self.pos_y += ASTEROID_SPEED * self.game.delta_time # Mover el asteroide en y

        self.rect = self.collition_rect() # Actualizar el rectangulo de colisiones


    def draw(self):
        '''Dibujar el asteroide'''

        self.game.screen.blit(self.sprite, (self.pos_x, self.pos_y)) # Dibujar el asteroide

        pg.draw.rect(self.game.screen, 'red', self.rect, 2) # Dibujar el rectangulo de colisiones

    def update(self):
        '''Actualizar asteroide'''

        self.movement() # Mover el asteroide

        self.draw() # Dibujar el asteroide
