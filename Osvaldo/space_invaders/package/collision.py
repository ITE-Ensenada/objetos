'''Descripcion: Este archivo contiene la clase Collision, 
                la cual se encarga de manejar las colisiones'''

import pygame as pg

class Collision:
    '''Clase que se encarga de manejar las colisiones'''

    def __init__(self, game):
        self.game = game


    def bullet_collision(self):
        '''Metodo que se encarga de manejar la colision entre las balas'''

        group_bullets = self.game.player.bullets # Lista de balas
        group_asteroid = self.game.asteroid_generator.asteroid_list # Lista de asteroides

        if pg.sprite.spritecollide(group_bullets, group_asteroid, True):

            self.game.asteroid_generator.asteroid_list.lost_life() # Perder vida

    def asteroid_player_collision(self):
        '''Metodo que se encarga de manejar la colision entre el jugador y los asteroides'''

        groups = self.game.asteroid_generator.asteroid_list # Lista de asteroides

        # Si el jugador colisiona con un asteroide
        if pg.sprite.spritecollide(self.game.player, groups, True):

            self.game.player.lost_life() # Perder vida


    def bullet_asteroid_collision(self):
        '''Metodo que se encarga de manejar la colision entre las balas y los asteroides'''

        print('Esto no hace nada... Aun...')


    def update(self):
        '''Metodo que se encarga de actualizar las colisiones'''

        self.asteroid_player_collision()