import pygame, sys
from pygame.locals import *
pygame.init()

SCREEN = pygame.display.set_mode((500, 500), 0, 32)

pygame.display.set_caption('Ajedrez')

WHITE = (236, 65, 29)

personaje1= pygame.image.load('peon.png')
personaje1 = pygame.transform.scale(personaje1, (100, 100))
personaje2 = pygame.image.load('rey.png')
personaje2 = pygame.transform.scale(personaje2, (100, 100))

personajeX = 10
personajeY = 10

z = 200
w = 200

while True: # the main game loop

	SCREEN.fill(WHITE)
	SCREEN.blit(personaje1, (personajeX, personajeY))
	SCREEN.blit(personaje2, (z, w))
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN: 
			if event.key==K_w:
				personajeY = personajeY-20
			if event.key==K_s:
				personajeY = personajeY+20
			if event.key==K_d:
				personajeX = personajeX+20
			if event.key==K_a:
				personajeX = personajeX-20 
			if event.key==K_i:
				w = w-20
			if event.key==K_k:
				w = w+20
			if event.key==K_l:
				z = z+20
			if event.key==K_j:
				z = z-20
		
	pygame.display.update()