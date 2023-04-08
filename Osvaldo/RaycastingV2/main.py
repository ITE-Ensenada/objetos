import pygame as pg
from sys import exit
from package import *

class Game:
    def __init__(self):
        # INICIAR PYGAME
        pg.init()
        
        # CREAR UN ATRIBUTO PANTALLA
        self.screen = pg.display.set_mode(RESOLUCION)
        
        # ATRIBUTO, OBJETO CLOCK PARA EL MANEJO DE LOS FPS
        self.clock = pg.time.Clock()
        
        # DELTA TIME
        self.delta_time = 1
        
        # --
        self.mapa = Map(self)
        
        # --
        self.player = Player(self)
        
    def run(self):
        while True:
            # FINALIZA EL PROGRAMA
            self.end_program()
            
            # DIBUJA EL MAPA EN 2D
            self.draw()
            
            # ACTUALIZA LA PANTALLA
            self.update()
    
    def update(self):
        # ACTUALIZA AL JUGADOR 
        self.player.update()
        
        # ACTUALIZA LA PANTALLA
        pg.display.update()
        
        # RESTRINGUE LA VELOCIDAD A LOS FPS DADOS
        self.delta_time = self.clock.tick(FPS)
        
        # OBSERVA FPS
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
    
    def end_program(self):
        # FINALIZA EL PROGRAMA
        for event in pg.event.get():
            # print(event)
            if event.type == pg.QUIT or ( event.type == pg.KEYDOWN  and event.key == pg.K_ESCAPE ):
                pg.quit()
                exit()

    def draw(self):
        self.screen.fill('black')
        self.player.draw2Dmap()
        self.mapa.draw2Dmap()
        
        
# MAIN
if __name__ == '__main__':
    game = Game()
    game.run()
    