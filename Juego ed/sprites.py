import pygame
from config import *
import math
import random
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

SCREEN = pygame.display.set_mode((640,360), 0, 32)
class Player(pygame.sprite.Sprite):
    def __init__ (self,game,x,y):
        
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        personajeImg = pygame.image.load('sd.png')
        personajeImg = pygame.transform.scale(personajeImg, (128, 128))
        SCREEN.blit(personajeImg, (x, y))
        self.x=x * TILESIZE
        self.y=y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.image = pygame.Surface([self.width,self.height])
        self.image = personajeImg
        
        self.facing = 'down'

        
    
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
            pass
      
            self.movement()

            self.rect.x += self.x_change
            self.rect.y += self.y_change

            self.x_change = 0
            self.y_change = 0


    def movement(self):
          
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.x_change -= PLAYER_SPEED
                self.facing= 'left'
                keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.x_change += PLAYER_SPEED
                self.facing= 'right'
            if keys[pygame.K_UP]:
                self.y_change -= PLAYER_SPEED
                self.facing= 'up'
            if keys[pygame.K_DOWN]:
                self.y_change += PLAYER_SPEED
                self.facing= 'down'   
