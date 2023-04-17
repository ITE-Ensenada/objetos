import pygame as pg
from package.level import *
from package.settings import *

class Map:
    def __init__(self, game):
        # OBTIENE LOS ATRIBUTOS Y METODOS DEL OBJETO 'game'
        self.game = game
        
        # SE CREA EL ATRIBUTO MAPA
        self.map = level0
    
    def draw2Dmap(self):
        for row in range(len(self.map)):
            for col in range(len(self.map)):
                if self.map[row][col] == 1:
                    pg.draw.rect( self.game.screen, 'white', 
                                ( tile_square_size * col , 
                                  tile_square_size * row, 
                                  tile_square_size, 
                                  tile_square_size))
                
    
        
