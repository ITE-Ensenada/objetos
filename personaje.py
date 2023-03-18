import pygame, sys
from pygame.locals import *
from Juego import *

myCharacter = ('Emely','18','rojo','10','ball','10','0','3')

pygame.init()

FPS = 10 # frames per second setting

fpsClock = pygame.time.Clock()

# Ajustes de ventana

tamanio = (1000, 600)
SCREEN = pygame.display.set_mode(tamanio)

pygame.display.set_caption('Animation')

RED = (255, 0, 0)
personajeImg = pygame.image.load("puca.png")
personajeImg = pygame.transform.scale(personajeImg, (170, 200))

personajeX = 10

personajeY = 10

direction = 'right'

while True: # the main game loop

	SCREEN.fill(RED)

	if direction == 'right':
		personajeX += 5
		if personajeX == 800:
			direction = 'down'
	elif direction == 'down':
		personajeY += 5
		if personajeY == 800:
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