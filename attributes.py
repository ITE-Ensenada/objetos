import pygame
import os 
from pygame.locals import *
from sprite import *
from attributes import *
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#clase del jugador
class Jugador(pygame.sprite.Sprite):

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = ('anim/stand/sd.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        
class Crow(pygame.sprite.Sprite):

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = ('anim/crow.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        
class Porky(pygame.sprite.Sprite):

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = ('anim/porky.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        
        
        