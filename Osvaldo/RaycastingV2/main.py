from package import *
import pygame, sys

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(resolucion)
        self.clock = pygame.time.Clock()
        self.newGame()
    
    def newGame(self):
        self.map = Mapa(self)
        
    def updateScreen(self):
        pygame.display.update()
        self.clock.tick(FPS)
    
    def drawScreen(self):
        self.screen.fill('black')
        self.map.draw()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE ):
                pygame.quit()
                sys.exit()
        
    def run(self):
        while True:
            self.check_events()
            self.drawScreen()
            self.updateScreen()
    
    
if __name__ == '__main__':
    game = Game()
    game.run()