import pygame, sys
from pygame.locals import *
from characterPygame import *

myCharacter = Personaje("Jason el gato", "6", "Naranja", "80cm", "Curacion")

print("Presentando a: \n" "Nombre: " + myCharacter.nombre, "\nEdad: " + myCharacter.edad, "\nColor de piel: " + myCharacter.color,
	"\nEstatura: " + myCharacter.height, "\nHabilidad predeterminada: " + myCharacter.curacion)

weaponSword = Weapons("90x110 cm", "7")
print("\nArmas disponibles: ", "\nEspada: ", "\nDimensiones: " + weaponSword.dimensiones, "\nDamage: " + weaponSword.damage)

weaponAxe = Weapons("70cm","5")
print("\nHacha: ", "\nDimensiones: " + weaponAxe.dimensiones, "\nDamage: " + weaponAxe.damage)

pygame.init()

FPS = 60 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1200, 800), 0, 32)

pygame.display.set_caption('Animation')

WHITE = (0, 113, 209)

personajeImg = pygame.image.load('cat.png')
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
