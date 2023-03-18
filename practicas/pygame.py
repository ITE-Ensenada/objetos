import pygame, sys
from pygame.locals import *
from modulos.Clases import *

if __name__ == '__main__':
	nombre = input('ingresa tu nombre: ')
	edad = input('ingresa tu edad: ')
	prota = Personaje(nombre,edad)
	print(prota)
	print("controles:\nw = moverse hacia arriba \ns = moverse hacia abajo \na = moverse hacia la izquierda \nd = moverse hacia la derecha")
	
pygame.init()

FPS = 10 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((600, 400), 0, 32)

pygame.display.set_caption('Juego obviamente entretenido')

fondo = pygame.image.load('recursos/fondo.PNG')

personajeImg = pygame.image.load('recursos/prota.png')
personajeImg = pygame.transform.scale(personajeImg, (prota.width, prota.height))

personajeX = prota.posicionX

personajeY = prota.posicionY

while True: # the main game loop

	SCREEN.blit(fondo, [0,0])

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
		
			if event.key ==pygame.K_w:
				if personajeY > 0:
					personajeY -= prota.velocidad
			if event.key ==pygame.K_s:
				if personajeY < 350:
					personajeY += prota.velocidad
			if event.key ==pygame.K_d:
				if personajeX < 550:
					personajeX += prota.velocidad
			if event.key ==pygame.K_a:
				if personajeX > 0:
					personajeX -= prota.velocidad
					
	SCREEN.blit(personajeImg, (personajeX, personajeY))

	pygame.display.update()
	fpsClock.tick(FPS)