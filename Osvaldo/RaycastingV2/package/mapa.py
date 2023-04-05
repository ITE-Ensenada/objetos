from package.level import * 
from pygame import draw


class Mapa:
    def __init__(self, game):
        self.game = game
        self.level = level0
        self.world_map = {}
        self.get_map2D()
        
    def get_map2D(self):
        for j, row in enumerate(self.level):
            for i, value in enumerate(row):
                # DE SER UNA TUPLA EL MAPA SE TRANSFORMA EN UN DICCIONARIO
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        for pos in self.world_map:
            draw.rect(self.game.screen, 'white', (pos[0] * 100, pos[1] * 100, 100, 100 ), 2) 