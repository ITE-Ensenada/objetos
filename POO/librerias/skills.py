'''Las habilidades'''
import pygame
from pygame.locals import __all__
from librerias.rect import muve_goku, muve_vegeta
class Kameha (pygame.sprite.Sprite):
    '''Goku'''
    def __init__ (self):
        super().__init__()
        self.image=pygame.image.load('imagenes/Kamehameha+.png').convert_alpha()
        self.size=pygame.transform.scale(self.image, (10, 40))
        self.dano=32
        self.color='blue'
        self.rapidez=26
        self.rect=self.size.get_rect()
        self.rect.x=muve_goku.rect.x+70
        self.rect.y=muve_goku.rect.y

    def update(self):
        '''se mueve'''
        self.rect.x+=self.rapidez

class Destello (pygame.sprite.Sprite):
    '''Destellos'''
    def __init__ (self):
        super().__init__()
        self.image=pygame.image.load('imagenes/destello.png')
        self.size=pygame.transform.scale(self.image, (30, 40))
        self.dano=35
        self.color='Yellow'
        self.rapidez=38
        self.rect=self.size.get_rect()
        self.rect.x=muve_vegeta.rect.x-85
        self.rect.y=muve_vegeta.rect.y

    def update(self):
        '''se mueve x2'''
        self.rect.x-=self.rapidez

def size(imag):
    '''ajusta tamaño'''
    tam=pygame.transform.scale(imag, (100, 1000))
    return tam
