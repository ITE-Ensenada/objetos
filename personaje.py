import pygame, sys
from pygame.locals import *
from juego import *

myCharacter = ('Emely','18','10','10','0','3')

pygame.init()

FPS = 10 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

tamanio = (826, 427)
SCREEN = pygame.display.set_mode(tamanio)

pygame.display.set_caption('Animation')

fondo = pygame.image.load("fondo.png").convert()

personajeImg = pygame.image.load("puca.png")
personajeImg = pygame.transform.scale(personajeImg, (235, 200))

personajeX = 20

personajeY = 200

direction = 'right'

while True: # the main game loop

	if direction == 'right':
		personajeX += 7
		if personajeX ==600:
			direction = 'stop'
	elif direction == 'down':
		personajeY += 7
		if personajeY == 600:
			direction = 'down'
	elif direction == 'right':
		personajeX -= 6
		if personajeX == 6:
			direction = 'down'
	elif direction == 'right':
		personajeY -= 6
		if personajeY == 6:
			direction = 'down'

	SCREEN.blit(fondo, [0,0])
	SCREEN.blit(personajeImg, (personajeX, personajeY))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	pygame.display.update()
	fpsClock.tick(FPS)