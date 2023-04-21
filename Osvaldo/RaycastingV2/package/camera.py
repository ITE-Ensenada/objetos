import pygame as pg
from package.settings import *
from math import sin, cos

class Camera:
    def __init__(self, game):
        self.game = game
    
    def raycasting(self):
        start_angle = self.game.player.angle - HALF_FOV
        
        for ray in range(NUM_RAYS):
            
            for depth in range(MAX_DEPTH):
                target_x = self.game.player.pos[0] + cos(start_angle) * depth
                target_y = self.game.player.pos[1] + sin(start_angle) * depth
                
                row = int(target_y)
                col = int(target_x)
                
                if self.game.mapa.map[row][col] == 1:
                    pg.draw.line(self.game.screen, 'yellow', 
                                 (self.game.player.pos[0] * tile_square_size, 
                                  self.game.player.pos[1] * tile_square_size),
                                 ((tile_square_size * ( self.game.player.pos[0] + cos(start_angle) * depth ) - tile_square_size),
                                  (tile_square_size * ( self.game.player.pos[1] + sin(start_angle) * depth ) - tile_square_size)))
                    break
                
                    #target_x = jugador.posX - math.sin( start_angle ) * profundidad
                    #target_y = jugador.posY + math.cos( start_angle ) * profundidad
                print(row, col)
            
            start_angle += DELTA_ANGLE
         
            
    def update(self):
        self.raycasting()
    