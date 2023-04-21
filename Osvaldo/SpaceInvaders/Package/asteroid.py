import random
import pygame as pg
from Package.settings import *

class Asteroid(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        
        self.game = game
        self.x = random.randint(0, ANCHO - 90)
        self.y = -138
        self.sprite0 = pg.image.load('Assets/Asteroid/Asteroid0.png').convert_alpha()
        self.sprite0 = pg.transform.scale(self.sprite0, (90, 138))
        self.sprite1 = pg.image.load('Assets/Asteroid/Asteroid1.png').convert_alpha()
        self.sprite1 = pg.transform.scale(self.sprite1, (90, 138))
        self.current_sprite = self.sprite0 # SPRITE ACTUAL
        self.rect = self.current_sprite.get_rect() # RECTANGULO PARA DETECCION DE COLISIONES
        
    def movement(self):
        self.y += ASTEROID_SPEED * self.game.delta_time
        
    def draw(self):
        self.game.screen.blit(self.sprite0, (self.x, self.y))
        pg.draw.rect(self.game.screen, (255, 0, 0), self.rect, 2)

        
    def update(self):
        self.movement()
        self.draw()