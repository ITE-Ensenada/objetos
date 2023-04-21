import pygame as pg
from sys import exit
from Package import *

class Game:
    def __init__(self):
        # INICIAR PYGAME
        pg.init()
        
        # ATRIBUTO VENTANA    
        self.screen = pg.display.set_mode(RESOLUTION, FLAGS)
        
        # ATRIBUTO CLOCK
        self.clock = pg.time.Clock()
        
        # DELTA TIME
        self.delta_time = 1
        
        # --
        self.player = Player(self)
        
        # --
        self.asteroid_generator = AsteroidGenerator(self)
        #self.asteroid = Asteroid(self)
        
        # --
        self.render_background = RenderBackground(self)
        

    def update(self):
        self.screen.fill('black')
        
        self.render_background.update()
        
        self.player.update()
        
        self.asteroid_generator.update()
        #self.asteroid.update()
                
        pg.display.update()
        
        self.delta_time = self.clock.tick(FPS)

        # --
        # print(self.delta_time)
    
    
    def run(self):
        while(True):
            self.events()
            self.update()
            
    def events(self):
        for self.event in pg.event.get():
            self.game_over()
            
    def game_over(self):
        if self.event.type == pg.QUIT or (self.event.type == pg.KEYDOWN and self.event.key == pg.K_ESCAPE):
            pg.quit()
            exit()
        if self.event.type == pg.KEYUP and (self.event.key == pg.K_a or self.event.key == pg.K_d or self.event.key == pg.K_w or self.event.key == pg.K_s):
            self.player.reset_sprite()
    

game = Game()
game.run()