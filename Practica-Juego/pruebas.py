import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 20 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1200, 800), 0, 32)

pygame.display.set_caption('Animation')

WHITE = (110, 51, 255)

personajeImg = pygame.image.load('polnareff.png')
personajeImg = pygame.transform.scale(personajeImg, (100, 200))

personajeX = 10

personajeY = 10

direction = 'right'
print('\n\n CONTROLERS:    \nFLECHA ^ =Arriba\n FLECHA v =Abajo\n FLECHA < =Izquierda\n FLECHA > =Derecha')

while True: # the main game loop
                                        
                SCREEN.fill(WHITE)
                
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                                #cheking if keydown event happened or not
                        if event.type == pygame.KEYDOWN:
                                #verificar cual fue el evento
                                if event.key == pygame.K_UP:
                                        personajeY -= 15
                                if event.key == pygame.K_DOWN:
                                        personajeY += 15
                                if event.key == pygame.K_LEFT:
                                        personajeX -= 15
                                if event.key == pygame.K_RIGHT:
                                        personajeX += 15
                
                SCREEN.blit(personajeImg, (personajeX, personajeY))
	

 
                pygame.display.update()
                fpsClock.tick(FPS)
