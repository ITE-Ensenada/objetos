import pygame, sys
from pygame.locals import *

class alucard():
	def __init__(self):
		personajeImg = pygame.image.load('alucard.png')						#Imagen del personaje
		personajeImg = pygame.transform.scale(personajeImg, (2*192, 2*108))	#Tamaño de la imagen del personaje
		personajeX = 10														#Movimiento eje X del personaje
		personajeY = 10														#Movimiento eje Y del personaje
		direction = 'right'													#Direccion inicial del personaje


def set_screen():
	pass

pygame.init()

FPS = 30 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window
SCREEN = pygame.display.set_mode((1200, 800), 0, 32) #El tamaño de la ventana
pygame.display.set_caption('Animation') #Da el nombre de la ventana
WHITE = (255, 255, 255) #Define el color para el fondo de la pantalla en una variable

#Variables del personaje
personajeImg = pygame.image.load('alucard.png')						#Imagen del personaje
personajeImg = pygame.transform.scale(personajeImg, (2*192, 2*108))	#Tamaño de la imagen del personaje
personajeX = 10														#Movimiento eje X del personaje
personajeY = 10														#Movimiento eje Y del personaje
direction = 'right'													#Direccion inicial del personaje

while True: # the main game loop

	SCREEN.fill(WHITE)	#Define el color del background

	if direction == 'right':
		personajeX += 10
		if personajeX == 800:
			direction = 'down'
	elif direction == 'down':
		personajeY += 10
		if personajeY == 500:
			direction = 'left'
	elif direction == 'left':
		personajeX -= 10
		if personajeX == 10:
			direction = 'up'
	elif direction == 'up':
		personajeY -= 10
		if personajeY == 10:
			direction = 'right'
	SCREEN.blit(personajeImg, (personajeX, personajeY))
	
	#Ciclo que rastrea los eventos del juego
	for event in pygame.event.get(): 
		print(event)
		
		#Detecta un evento donde se oprima una tecla para realizar una accion especifica
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				direction = 'down'
			if event.key == pygame.K_UP:
				direction = 'up'
			if event.key == pygame.K_LEFT:
				direction = 'left'
			if event.key == pygame.K_RIGHT:
				direction = 'right'

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update() 
	fpsClock.tick(FPS)