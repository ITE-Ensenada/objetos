'''Descripcion: Este archivo contiene la clase Bullet
                La cual se encarga de representar una bala'''

import pygame
from package.settings import BULLET_DAMAGE, BULLET_SPEED
from package.subpackage.esqueleto import Esqueleto

class Bullet( Esqueleto ):
    '''Clase que representa una bala'''

    def __init__(self, game):

        super().__init__(
            game,
            None,
            None,
            None)

        self._pos_x = self.game.player.pos[0] # Actualizar posicion en x de la bala

        self._pos_y = self.game.player.pos[1] # Actualizar posicion en y de la bala

        self.sprite = self.create_sprite() # Sprite de la bala

        self.rect = self.collition_rect # Rectanguo de colisiones

        self.damage = BULLET_DAMAGE # Daño de la bala

    def create_sprite(self):
        '''Metodo que se encarga de crear el sprite de la bala'''

        sprite = pygame.image.load('Assets/Player/Bullet.png').convert_alpha()

        sprite = pygame.transform.scale(sprite, (10, 10))

        return sprite


    def collition_rect(self):
        '''Metodo que se encarga de crear el rectangulo de colisiones'''

        rect = self.sprite.get_rect()

        rect.x = self.pos[0]

        rect.y = self.pos[1]

        return rect


    def movement(self):
        '''Metodo que se encarga de mover la bala'''

        self._pos_y -= BULLET_SPEED * self.game.delta_time # Velocidad de la bala

        self.rect = self.collition_rect() # Actualizar el rectangulo de colisione


    def draw(self):
        '''Dibujar la bala'''

        self.game.screen.blit(self.sprite, (self.pos[0], self.pos[1])) # Dibujar la bala

        pygame.draw.rect(self.game.screen, 'red', self.rect, 2) # Dibujar el rectangulo de colisiones


    def update(self):
        '''Actualizar la bala'''

        self.movement()

        self.draw()
