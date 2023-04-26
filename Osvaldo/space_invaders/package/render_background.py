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

        # Sprite de la vida del jugador
        self.player_life = self.create_sprites_player_life()


    def create_sprites_player_life(self):
        '''Metodo que se encarga de crear los sprites de la vida del jugador'''

        sprites = [
            (pygame.image.load('Assets/Life0.png').convert_alpha()),
            (pygame.image.load('Assets/Life1.png').convert_alpha()),
            (pygame.image.load('Assets/Life2.png').convert_alpha()),
            (pygame.image.load('Assets/Life3.png').convert_alpha())
        ]

        for index, sprite in enumerate(sprites):
            sprites[index] = pygame.transform.scale(sprite, (104, 27.2))

        return sprites

    def draw_life_player(self):
        '''Dibujar vidas del jugador'''

        # Dibuja la vida del jugador
        self.game.screen.blit(self.player_life[self.game.player.life - 1], (0, 0))

    def draw_background(self):
        '''Dibujar fondo'''''

        self.game.screen.blit(self.background, (0, 0))


    def update(self):
        '''Actualizar renderizador de fondo'''

        self.draw_background()
        self.draw_life_player()
