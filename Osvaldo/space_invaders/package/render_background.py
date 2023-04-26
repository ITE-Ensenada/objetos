'''Descripcion: Este archivo contiene la clase RenderBackground. 
                La cual se encarga de renderizar el fondo del juego'''

import pygame
from package.settings import ALTO, ANCHO

class RenderBackground():
    '''Clase que se encarga de renderizar el fondo del juego'''

    def __init__(self, game):

        self.game = game # Instancia de la clase Game

        # Fondo
        self.background = pygame.image.load('Assets/Stars_background.jpg').convert_alpha()

        # Scale del fondo
        self.background = pygame.transform.scale(self.background, (ANCHO, ALTO))
    
    def draw_background(self):
        '''Dibujar fondo'''''

        self.game.screen.blit(self.background, (0, 0))

    def update(self):
        '''Actualizar renderizador de fondo'''

        self.draw_background()
