'''Descripcion: Este archivo contiene la clase RenderBackground. 
                La cual se encarga de renderizar el fondo del juego'''

import pygame
from package.settings import ALTO, ANCHO

class RenderItems():
    '''Clase que se encarga de renderizar el fondo del juego'''

    def __init__(self, game):

        self.game = game # Instancia de la clase Game

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

    def score_record(self):
        
        high_score = self.game.score_manager.load_high_score
        actual_score = self.game.score_manager.temp_score
        
        font = pygame.font.Font(None, 36)
        text = font.render(("Puntaje: "
                            + str(actual_score))
                            + '        Puntaje maximo: '
                            + str(high_score)
                           , True, (255, 255, 255))

        text_rect = text.get_rect()
        text_rect.topleft = (ALTO - 75, 10)
        self.game.screen.blit(text, text_rect)



    def update(self):
        '''Metodo que se encarga de actualizar el fondo del juego'''
        
        self.score_record()
        self.draw_life_player()
