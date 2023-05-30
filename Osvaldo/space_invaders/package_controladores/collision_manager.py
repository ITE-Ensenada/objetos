'''Descripcion: Este archivo contiene la clase Collision, 
                la cual se encarga de manejar las colisiones'''

import pygame as pg

class CollisionManager:
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

        groups = self.game.hostile_manager.asteroid_generator.asteroid_list # Lista de asteroides

        # Si el jugador colisiona con un asteroide
        if pg.sprite.spritecollide(self.game.player, groups, True):

            self.game.player.lost_life() # Perder vida


    def npc_player_collision(self):
        '''Metodo que se encarga de manejar la colision entre el jugador y los npc'''
        groups = self.game.hostile_manager.npc_generator.npc_list # Lista de npc
        
        #Si el jugador colisiona con un asteroide
        if pg.sprite.spritecollide(self.game.player, groups, True):

            self.game.player.lost_life()

        
    def bullet_npc_collision(self):
        '''Metodo que se encarga de manejar la colision entre las balas y los npc'''
        
        colisiones = pg.sprite.groupcollide(
            self.game.hostile_manager.npc_generator.npc_list,
            self.game.player.bullet_list,
            False,
            True
        )
        
        for npc, bullet in colisiones.items():
            if npc.rect.top > 0:
                npc.lost_life()


    def bullet_asteroid_collision(self):
        '''Metodo que se encarga de manejar la colision entre las balas y los asteroides'''

        colisiones = pg.sprite.groupcollide(
            self.game.hostile_manager.asteroid_generator.asteroid_list,
            self.game.player.bullet_list,
            False,
            True)

        for asteroid, bullet in colisiones.items():
            asteroid.lost_life()

    def update(self):
        '''Metodo que se encarga de actualizar las colisiones'''

        self.asteroid_player_collision()
        
        self.npc_player_collision()

        self.bullet_asteroid_collision()
        
        self.bullet_npc_collision()
