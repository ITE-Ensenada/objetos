import pygame
import sys
import movimiento
from pygame.locals import *
pygame.init()
FPS = 10 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1200, 800), 0, 32)

pygame.display.set_caption('Animation')

WHITE = (0, 78, 75)

personajeImg = pygame.image.load('dragon.png')
personajeImg = pygame.transform.scale(personajeImg, (100, 100))

personajeX = 10

personajeY = 10

while True: # the main game loop

		SCREEN.fill(WHITE)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()  
				# checking if keydown event happened or not
			if event.type == pygame.KEYDOWN:
				# verificar cual fue el evento
				if event.key == pygame.K_UP:
					personajeY -= 5
				if event.key == pygame.K_DOWN:
					personajeY += 5
				if event.key == pygame.K_LEFT:
					personajeX -= 5
				if event.key == pygame.K_RIGHT:
					personajeX += 5

		SCREEN.blit(personajeImg, (personajeX, personajeY))

		pygame.display.update()
		fpsClock.tick(FPS)