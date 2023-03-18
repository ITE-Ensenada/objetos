import pygame, sys, clasespersonajes

from pygame.locals import *


pygame.init()

FPS = 10 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1200, 800), 0, 32)

pygame.display.set_caption('Animation')

WHITE = (179, 113, 209)

personajeImg = pygame.image.load('zero.png')
personajeImg = pygame.transform.scale(personajeImg, (100, 200))

personajeX = 5

personajeY = 5

while True: # the main game loop

	
    SCREEN.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                personajeY -= 10
            if event.key == pygame.K_DOWN:
                personajeY += 10
            if event.key == pygame.K_LEFT:
                personajeX -= 10
            if event.key == pygame.K_RIGHT:
                personajeX += 10
	
	
    SCREEN.blit(personajeImg, (personajeX, personajeY))
                
    pygame.display.update()
    fpsClock.tick(FPS)