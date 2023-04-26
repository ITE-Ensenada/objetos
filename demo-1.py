import pygame, sys
from pygame.locals import *

pygame.init()
 

FPS = 10 # frames per second setting

fpsClock = pygame.time.Clock()

#set up the window
SCREEN = pygame.display.set_mode((1200, 800), 0, 32)
pygame.display.set_caption('Animation')
WHITE = (179, 113, 209)

personajeImg = pygame.image.load('alucard.png')
personajeImg = pygame.transform.scale(personajeImg, (100, 200))
personajeX = 10
personajeY = 10
direction = 'right'

while True: # the main game loop

	SCREEN.fill(WHITE)

	if direction == 'right':
		personajeX += 5
		if personajeX == 800:
			direction = 'down'
	elif direction == 'down':
		personajeY += 5
		if personajeY == 500:
			direction = 'left'
	elif direction == 'left':
		personajeX -= 5
		if personajeX == 10:
			direction = 'up'
	elif direction == 'up':
		personajeY -= 5
		if personajeY == 10:
			direction = 'right'
	SCREEN.blit(personajeImg, (personajeX, personajeY))
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			print("Presionastes una tecla")
			if event.key == pygame.K_PLUS:
				FPS =  FPS + 10
			if event.key == pygame.K_MINUS:
				FPS = FPS - 5


	pygame.display.update()
	fpsClock.tick(FPS)
