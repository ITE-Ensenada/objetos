import pygame as pg
from Package.settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.pos = self.x, self.y = X, Y
        self.life = LIFE
        
        
    def movement(self):
        dx, dy = 0, 0
        keys = pg.key.get_pressed()
        
        if keys[pg.K_a]:
            dx -= PLAYER_SPEED * self.game.delta_time
        if keys[pg.K_d]:
            dx += PLAYER_SPEED * self.game.delta_time
        if keys[pg.K_w]:
            dy -= PLAYER_SPEED * self.game.delta_time
        if keys[pg.K_s]:
            dy += PLAYER_SPEED * self.game.delta_time
        
        self.check_walls(dx, dy)
    
    def check_walls(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if (new_x > 5) and new_x < (ANCHO - 5):
            self.x = new_x
        if new_y < (ALTO - 10) and new_y > 10:
            self.y = new_y
    
    def update(self):
        self.movement()
        self.draw_player()
    
    def draw_player(self):
        pg.draw.circle(self.game.screen, 'white', (self.x, self.y), 10)