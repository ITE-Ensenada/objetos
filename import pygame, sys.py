import pygame, sys
from pygame.locals import *
from personajes import *
from validacion import edad
 
miPersonaje= Personaje("Juan","18", "masculino", "200", "60", "caballero", "humano", "178", "delgado", "negro")
print(miPersonaje)

miArma = Armas("90", "80", "Madera y Hierro", "5kg")
print(miArma)

pygame.init()

FPS = 24 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1366, 768), 0, 32)

pygame.display.set_caption('Animation')
fondo = pygame.image.load("imagenes/santuario_enlace.jpg").convert()

WHITE = (179, 113, 209)

personajeImg = pygame.image.load('imagenes/artorias.png')
personajeImg = pygame.transform.scale(personajeImg, (156, 160))

personajeX = 10

personajeY = 10

x_speed = 0

y_speed = 0

direction = 'right'

#Coordenadas del personaje


while True: # the main game loop	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			print("presionaste una tecla")
			if event.key == pygame.K_a:
				x_speed = -3
			if event.key == pygame.K_d:
				x_speed = 3
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				x_speed = 0
			if event.key == pygame.K_d:
				x_speed = 0
		
	SCREEN.fill(WHITE)
	SCREEN.blit(fondo,SCREEN.blit(fondo, [0, 0]))

	SCREEN.blit(personajeImg, (personajeX, personajeY))
	personajeX += x_speed

	pygame.draw.rect(SCREEN,WHITE, (personajeX, personajeY, 0, 0))


	pygame.display.update()
	fpsClock.tick(FPS)

