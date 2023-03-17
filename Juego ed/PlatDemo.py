import pygame, sys
from pygame.locals import *
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
import propiedades

FPS = 60 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1024, 576), 0, 0,0)

pygame.display.set_caption('Animation')


WHITE = (0,191,255)

personajeImg = pygame.image.load('spr_gbstand.png')
personajeImg = pygame.transform.scale(personajeImg, (100,100))
width,height = 1024,576
window = pygame.display.set_mode((1024,576))
bg_img = pygame.image.load('spr_bg.png')
bg_img = pygame.transform.scale(bg_img,(1024,576))
window.blit(bg_img,(0,0))
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
	 
	 

	