import pygame, sys
from pygame.locals import *
from Personaje import *

# ***************************************

			# Objects

p1 = Character("John Wick", "50", "1", "5", "2", "20", "10", "7", "1.80", "Blanco")
p1.showCharacter()			


# ***************************************

pygame.init()

FPS = 60 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1366, 800), 0, 32)

pygame.display.set_caption('Animation')

WHITE = (0, 113, 209)

personajeImg = pygame.image.load('JohnWick.png')
personajeImg = pygame.transform.scale(personajeImg, (300, 300))

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

	pygame.display.update()
	fpsClock.tick(FPS)

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

	pygame.display.update()
	fpsClock.tick(FPS)