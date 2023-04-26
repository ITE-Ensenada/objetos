'''Descripcion: Este archivo contiene la clase Collision, 
                la cual se encarga de manejar las colisiones'''

import pygame as pg

class Collision:
    '''Clase que se encarga de manejar las colisiones'''

    def __init__(self, game):
        self.game = game
    
    def asteroid_player_collision(self):
        '''Metodo que se encarga de manejar la colision entre el jugador y los asteroides'''

        groups = self.game.asteroid_generator.asteroid_list # Lista de asteroides

        # Si el jugador colisiona con un asteroide
        if pg.sprite.spritecollide(self.game.player, groups, True):

            self.game.player.lost_life() # Perder vida


    def bullet_asteroid_collision(self):
        pass


    def update(self):
        '''Metodo que se encarga de actualizar las colisiones'''

        self.asteroid_player_collision()
