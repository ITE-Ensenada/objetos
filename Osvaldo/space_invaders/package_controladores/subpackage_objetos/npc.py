'''Descripcion: '''

import pygame
from game_data.general_settings.settings import (
    NPC_LIFE,
    NPC_SPEED

)
from package_controladores.subpackage_objetos.estructuras_basicas.esqueleto import Esqueleto
from package_controladores.subpackage_objetos.bullet import Bullet
from package_controladores.subpackage_objetos.player import Player

class Npc(Player):
    '''Clase'''

    def __init__(self, game, pos_x, pos_y):

        super().__init__(
            game,
            pos_x,
            pos_y,
            NPC_LIFE)


    def create_sprites(self):
        '''Metodo que se encarga de crear los sprites del npc'''

        sprites = pygame.image.load('Assets/Npc/Alien0.png')
        sprites = pygame.transform.scale(sprites, (48, 48) )

        return sprites

    def collide_rect(self):
        '''Metodo que se encarga de crear el rectangulo de colisiones'''

        rect = self.current_sprite.get_rect()
        rect.x = self.pos[0]
        rect.y = self.pos[1]

        return rect


    def shot(self):
        '''Metodo que se encarga de disparar'''

        bullet = Bullet(self.game) # Crear una bala

        self.bullet_list.add(bullet) # Agregar una bala al grupo de balas
