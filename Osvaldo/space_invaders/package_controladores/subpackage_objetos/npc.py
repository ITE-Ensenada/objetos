import pygame
from game_data.general_settings.settings import (
    NPC_LIFE,
    NPC_SPEED
)
from package_controladores.subpackage_objetos.estructuras_basicas.esqueleto import Esqueleto


class Npc(Esqueleto):
    def __init__(self, game, pos_x, pos_y, life):

        super().__init__(game, pos_x, pos_y, life)
        self.current_sprite = self.create_sprites()
        self.rect = self.collide_rect()


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