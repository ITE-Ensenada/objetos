'''Descripcion: 
    Este archivo contienen una clase base para una variedad de clases'''

import pygame as pg

class Esqueleto(pg.sprite.Sprite):
    '''Clase base para la clase player, asteroid y npc'''

    def __init__(self, game, pos_x, pos_y, life):

        super().__init__() # Inicializar clase padre
        self.game = game # Instancia de la clase Game
        self._pos_x, self._pos_y = pos_x, pos_y # Posicion en x, y
        self._life = life # Vidas del esqueleto


    def lost_life(self):
        '''Metodo que se encarga de restar una vida'''

        self._life -= 1 # Restar una vida


    @property
    def life(self):
        '''Metodo que se encarga de retornar las vidas del esqueleto'''

        return self._life


    @property
    def pos(self):
        '''Metodo que se encarga de retornar la posicion del esqueleto'''

        return self._pos_x, self._pos_y
