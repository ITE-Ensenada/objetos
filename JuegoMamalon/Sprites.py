'''Descripcion: Este archivo contiene las clases de los sprites del juego'''

import pygame

class Tile(pygame.sprite.Sprite):
    '''Clase para crear los tiles del nivel'''

    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift):
        '''Metodo para actualizar el tile'''

        self.rect.x += x_shift

        #Gif que usaré para proximo sprite de personaje https://cdn.lospec.com/gallery/grape-slime-397989.gif