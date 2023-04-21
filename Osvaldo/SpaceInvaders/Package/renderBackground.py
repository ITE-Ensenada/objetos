import pygame as pg
from Package.settings import *

class RenderBackground():
    def __init__(self, game):
        self.game = game
        self.background = pg.image.load('Assets/Stars_background.jpg').convert_alpha()
        # self.background = pg.transform.rotate(self.background, 90)
        self.background = pg.transform.scale(self.background, (ANCHO, ALTO))
        
    def draw_background(self):
        self.game.screen.blit(self.background, (0, 0))
        
    def update(self):
        self.draw_background()