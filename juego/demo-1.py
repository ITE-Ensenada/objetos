import pygame, sys
from pygame.locals import *
import juegogranja
pygame.init()


FPS = 10 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((740, 467), 0, 32)

pygame.display.set_caption('Animation')

WHITE = (179, 113, 209)

personajeImg = pygame.image.load('harrystyles.png')
personajeImg = pygame.transform.scale(personajeImg, (300, 190))
pygame.display.set_caption("harry valley")
personajeX = 10
personajeY = 10

direction = 'right'
fondo = pygame.image.load("granja.png")
while True: # the main game loop

	SCREEN.blit(fondo, [0,0])
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		personajeX -= 5
	if keys[pygame.K_RIGHT]:
		personajeX += 5
	if keys[pygame.K_UP]:
		personajeY -= 5
	if keys[pygame.K_DOWN]:
		personajeY += 5
	

    
	SCREEN.blit(personajeImg, (personajeX, personajeY))
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)