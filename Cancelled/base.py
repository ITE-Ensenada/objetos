import pygame, sys
from pygame.locals import *
import movement, character, weapon, skill

pygame.init()

FPS = 10 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1200, 800), 0, 32)

pygame.display.set_caption('Animation')

WHITE = (179, 113, 209)

personajeImg = pygame.image.load('Assets\Siete.png')
personajeImg = pygame.transform.scale(personajeImg, (192, 160))

personajeX = 10

personajeY = 10

while True: # the main game loop

	SCREEN.fill(WHITE)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
			elif event.key == pygame.K_UP:
				personajeY -= 10
				if personajeY <= 0:
					print("No puedes salir del límite.")
					personajeY += 10
			elif event.key == pygame.K_DOWN:
				personajeY += 10
				if personajeY >= 640:
					print("No puedes salir del límite.")
					personajeY -= 10
			elif event.key == pygame.K_RIGHT:
				personajeX += 10
				if personajeX >= 1008:
					print("No puedes salir del límite.")
					personajeX -= 10
			elif event.key == pygame.K_LEFT:
				personajeX -= 10
				if personajeX <= 0:
					print("No puedes salir del límite.")
					personajeX += 10


	SCREEN.blit(personajeImg, (personajeX, personajeY))
	
	pygame.display.update()
	fpsClock.tick(FPS)