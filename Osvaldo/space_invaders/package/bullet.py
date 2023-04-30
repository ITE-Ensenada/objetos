'''Descripcion: Este archivo contiene la clase Bullet
                La cual se encarga de representar una bala'''

import pygame
from package.settings import BULLET_DAMAGE, BULLET_SPEED

class Bullet:
    '''Clase que representa una bala'''

    def __init__(self, game):

        self.game = game # Instancia de la clase Game

        self.pos = self.game.player.pos # Posicion de la bala

        self.sprite = self.create_sprite() # Sprite de la bala

        self.rect = self.collition_rect # Rectanguo de colisiones

        self.damage = BULLET_DAMAGE # Daño de la bala

    def create_sprite(self):
        '''Metodo que se encarga de crear el sprite de la bala'''

        sprite = pygame.image.load('Assets/Player/Bullet.png').convert_alpha()

        sprite = pygame.transform.scale(sprite, (2, 2))

        return sprite


    def collition_rect(self):
        '''Metodo que se encarga de crear el rectangulo de colisiones'''

        rect = self.sprite.get_rect()

        rect.x = self.pos[0]

        rect.y = self.pos[1]

        return rect


    def movement(self):
        '''Metodo que se encarga de mover la bala'''

        speed = BULLET_SPEED * self.game.delta_time # Velocidad de la bala

        self.pos[1] -= speed


    def draw(self):
        '''Dibujar la bala'''

        self.game.screen.blit(self.sprite, (self.pos[0], self.pos[1]))


    def update(self):
        '''Actualizar la bala'''

        self.movement()

        self.draw()
