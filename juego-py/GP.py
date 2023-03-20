import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1200, 800), 0, 32)

pygame.display.set_caption('Animation')

WHITE = (91, 44, 111)

personajeImg = pygame.image.load('meap.png')
personajeImg = pygame.transform.scale(personajeImg, (100, 200))

personajeX = 10

personajeY = 10

direction = 'right'
print ('\n^pa rriba\n vpa bajo\n <pa la izquierda\n >pa la derecha')
while True: # the main game loop

                                SCREEN.fill(WHITE)
	
                                for event in pygame.event.get():
                                                if event.type == QUIT:
                                                                pygame.quit()
                                                                sys.exit()
			
                                                if event.type == pygame.KEYDOWN:
                                                                if event.key == pygame.K_UP:
                                                                                personajeY -= 50
                                                                if event.key == pygame.K_DOWN:
                                                                                personajeY += 50
                                                                if event.key == pygame.K_LEFT:
                                                                                personajeX -= 50
                                                                if event.key == pygame.K_RIGHT:
                                                                                personajeX += 50
                                SCREEN.blit(personajeImg, (personajeX, personajeY))
	
	

                                pygame.display.update()
                                fpsClock.tick(FPS)
