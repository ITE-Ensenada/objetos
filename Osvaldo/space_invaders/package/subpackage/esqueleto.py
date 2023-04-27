'''Descripcion: Este archivo contienen una clase base para la clase player del juego, asteroid y npc'''

import pygame as pg

class Esqueleto(pg.sprite.Sprite):
    def __init__(self, game, X, Y, sprites, life):

        super().__init__() # Inicializar clase padre

        self.game = game # Instancia de la clase Game

        self._pos_x, self._pos_y = X, Y # Posicion en x, y

        self.sprites = sprites # Sprites del jugador

        self._life = life # Vidas del esqueleto

    def lost_life(self):
        '''Metodo que se encarga de restar una vida'''

        self._life -= 1 # Restar una vida
        
    @property
    def life(self):
        return self._life

    @property
    def pos(self):
        return self._pos_x, self._pos_y