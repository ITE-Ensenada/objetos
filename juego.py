import pygame
import sys
import movimientos
from pygame.locals import *
pygame.init()
FPS = 10 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((800, 800), 0, 32)

pygame.display.set_caption('Animation')

WHITE = (0, 78, 75)

personajeImg = movimientos.Quieto
personajeImg = pygame.transform.scale(personajeImg, (57, 90))

personajeX = 10
personajeY = 10
Vel_x = 0
Vel_y = 0

salto = False
cami_Iz = False
cami_Der = False
quieto = True

juego = True
while juego: # the main game loop

		SCREEN.fill(WHITE)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()  
				# checking if keydown event happened or not
			if event.type == pygame.KEYDOWN:
				# verificar cual fue el evento
				if event.key == pygame.K_ESCAPE:
					juego = False
				if event.key == pygame.K_UP:
					salto = True
					cami_Der = False
					cami_Iz = False
					Vel_y = -5
				if event.key == pygame.K_DOWN:
					salto = True
					cami_Der = False
					cami_Iz = False
					Vel_y = 5
				if event.key == pygame.K_LEFT:
					cami_Iz = True
					salto = False
					cami_Der = False
					Vel_x = -5
				if event.key == pygame.K_RIGHT:
					cami_Der = True
					salto = False
					cami_Iz = False
					Vel_x = 5

				if salto == True:
					personajeImg = movimientos.Salto				
				if cami_Iz == True:
					personajeImg = movimientos.Izquierda					
				if cami_Der == True:					
					personajeImg = movimientos.Derecha

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					Vel_x = 0
				if event.key == pygame.K_LEFT:
					Vel_x = 0
				if event.key == pygame.K_DOWN:
					Vel_y = 0
				if event.key == pygame.K_UP:
					Vel_y = 0    

			
		personajeX += Vel_x
		personajeY += Vel_y

				
		SCREEN.blit(personajeImg, (personajeX, personajeY))

		pygame.display.update()
		fpsClock.tick(FPS)