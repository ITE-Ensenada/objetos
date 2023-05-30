'''Descripcion: '''

import pygame
from game_data.general_settings.settings import (
    NPC_LIFE,
    NPC_SPEED,
    NPC_WIDTH,
    NPC_HEIGHT
)
from package_controladores.subpackage_objetos.estructuras_basicas.esqueleto import Esqueleto
from package_controladores.subpackage_objetos.bullet import Bullet
from package_controladores.subpackage_objetos.player import Player

class Npc(Esqueleto):
    '''Clase'''

    def __init__(self, game, pos_x, pos_y):

        super().__init__(
            game,
            pos_x,
            pos_y,
            NPC_LIFE)
        self.sprites = self.create_sprites()
        self.rect = self.collide_rect()


    def create_sprites(self):
        '''Metodo que se encarga de crear los sprites del npc'''

        sprites = pygame.image.load('Assets/Npc/Alien0.png')
        sprites = pygame.transform.scale(sprites, (NPC_WIDTH, NPC_HEIGHT) )

        return sprites

    def collide_rect(self):
        '''Metodo que se encarga de crear el rectangulo de colisiones'''

        rect = self.sprites.get_rect()
        rect.x = self.pos[0]
        rect.y = self.pos[1]

        return rect


    def shot(self):
        '''Metodo que se encarga de disparar'''

        bullet = Bullet(self.game) # Crear una bala

        self.bullet_list.add(bullet) # Agregar una bala al grupo de balas

    def draw(self):
        '''Metodo que se encarga de dibujar'''

        self.game.screen.blit(self.sprites, self.pos)

        pygame.draw.rect(self.game.screen, 'red', self.collide_rect(), 2)

    def update(self):
        '''Metodo que se encarga de actualizar'''

        self._pos_y += NPC_SPEED * self.game.delta_time

        self.current_sprite = self.sprites

        self.draw()