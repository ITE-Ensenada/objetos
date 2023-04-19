import pygame, sys
from pygame.locals import *

pygame.init()

textoBaseDePreguntas = '''
Capital de colombia\tBogota\tCartagena\tCali\tBarranquilla
\n
Capital de venezuela\tCaracas\tMaracaibo\tBarquisimeto\tBolivar
\n
A que simbolo pertenece el hierro\tFe\tHe\tNa\tK
'''
base_de_preguntas = []
renglones = textoBaseDePreguntas.split("\n")
cantidadDePreguntas = len(renglones)

for i in range(cantidadDePreguntas):
    if(renglones[i]==""):
        continue
    base_de_preguntas.append(renglones[i].split("\t"))

print(base_de_preguntas)  

FPS = 10 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1200, 800), 0, 32)

pygame.display.set_caption('Animation')

WHITE = (179, 113, 209)

personajeImg = pygame.image.load('')
personajeImg = pygame.transform.scale(personajeImg, (100, 200))

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