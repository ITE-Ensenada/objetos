import pygame as pg
from package.settings import *
from math import pi,cos,sin

class Player:   
    def __init__(self, game):
        self.game = game
        self.x, self. y = PlayerPos
        self.angle = PlayerAngle
        self.speed = PlayerSpeed
        self.speedRotation = PlayerSpeedRotation
        
    def draw2Dmap(self):
        self.movement
        
        pg.draw.circle(self.game.screen, 'red', (self.pos[0] * tile_square_size, 
                                                 self.pos[1] * tile_square_size), 10)
        
        pg.draw.line(self.game.screen, 'green', (self.pos[0] * tile_square_size, self.pos[1] * tile_square_size),
                                                ((self.pos[0] * tile_square_size) - sin(self.angle) * 50, 
                                                 (self.pos[1] * tile_square_size) + cos(self.angle) * 50))
        
    def movement(self):
        keys = pg.key.get_pressed()
        sin_theta = sin(self.angle)
        cos_theta = cos(self.angle)
        dx, dy = 0, 0
        speed_sin = self.speed * sin_theta
        speed_cos = self.speed * cos_theta
        
        if keys == [pg.K_w]:
            dx += speed_sin
            dy += speed_cos
        if keys == [pg.K_d]:
            dx += -speed_sin
            dy += -speed_cos
        if keys == [pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys == [pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
        
        
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def pos_map(self):
        return int(self.x), int(self.y)