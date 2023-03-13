import pygame, sys
from pygame.locals import *

class Display():
    legth = 384
    width = 720
    FLAGS = pygame.SCALED
    
    '''
    def __init__(self, width, legth):
        self.width = width
        self.legth = legth
    '''    
    def display_init(self):
        pygame.display.set_mode((self.legth, self.width), self.FLAGS, 32)


def main():
    pygame.init()

    while True:
        #pygame.display.set_mode((1200,800))
        for event in pygame.event():
            #Logica del juego


            #Registro de eventos
            if event.type == KEYDOWN:   #Evento, oprimir teclas
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit() 

            if event.type == QUIT:      #Evento, pantalla quit
                pygame.quit()
                sys.exit()
        pygame.display.update()

pygame.display.set_mode((384, 720))


#main()