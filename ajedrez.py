import pygame, sys
from pygame.locals import *
pygame.init()

SCREEN = pygame.display.set_mode((720, 720), 20, 32)
pygame.display.set_caption('Ajedrez')
fondo = pygame.image.load('tablero1.png')
fondo = pygame.transform.scale(fondo, (720, 720))


personaje1 = pygame.image.load('torre.png')
personaje1 = pygame.transform.scale(personaje1, (90, 90))
personaje2 = pygame.image.load('caballo.png')
personaje2 = pygame.transform.scale(personaje2, (90, 90))
personaje3 = pygame.image.load('alfil.png')
personaje3 = pygame.transform.scale(personaje3, (90, 90))
personaje4 = pygame.image.load('rey.png')
personaje4 = pygame.transform.scale(personaje4, (90, 90))
personaje5 = pygame.image.load('reyna.png')
personaje5 = pygame.transform.scale(personaje5, (90, 90))
personaje6 = pygame.image.load('alfil.png')
personaje6 = pygame.transform.scale(personaje6, (90, 90))
personaje7 = pygame.image.load('caballo.png')
personaje7 = pygame.transform.scale(personaje7, (90, 90))
personaje8 = pygame.image.load('torre.png')
personaje8 = pygame.transform.scale(personaje8, (90, 90))

personajeX1 = 0
personajeY1 = 0
personajeX2 = 90
personajeY2 = 0
personajeX3 = 180
personajeY3 = 0
personajeX4 = 270
personajeY4 = 0
personajeX5 = 360
personajeY5 = 0
personajeX6 = 450
personajeY6 = 0
personajeX7 = 540
personajeY7 = 0
personajeX8 = 630
personajeY8 = 0
while True: # the main game loop
	SCREEN.fill((255, 255, 255))
	SCREEN.blit(fondo, (0, 0))
	SCREEN.blit(personaje1, (personajeX1, personajeY1))
	"""
	SCREEN.blit(personaje2, (personajeX2, personajeY2))
	SCREEN.blit(personaje3, (personajeX3, personajeY3))
	SCREEN.blit(personaje4, (personajeX4, personajeY4))
	SCREEN.blit(personaje5, (personajeX5, personajeY5))
	SCREEN.blit(personaje6, (personajeX6, personajeY6))
	SCREEN.blit(personaje7, (personajeX7, personajeY7))
	SCREEN.blit(personaje8, (personajeX8, personajeY8))
	"""
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:  
    #TorreIzq
   		if event.key == K_DOWN:
			personajeY1 = personajeY1+90
		if event.key == K_UP:
			personajeY1 = personajeY1-90
		if event.key == K_RIGHT:
			personajeX1 = personajeX1+90
		if event.key == K_LEFT:
			personajeX1 = personajeX1-90
pygame.display.update()
"""

#Caballo izq
if event.key==K_0:
personajeY2 = personajeY2+180
personajeX2 = personajeX2+90
if event.key==K_7:
personajeY2 = personajeY2+180
personajeX2 = personajeX2-90
if event.key==K_8:
personajeY2 = personajeY2-180
personajeX2 = personajeX2+90
if event.key==K_9:
personajeY2 = personajeY2-180
personajeX2 = personajeX2-
if event.key==K_w:
personajeY3 = personajeY3-90
if event.key==K_s:
personajeY3 = personajeY3+90
if event.key==K_d:
personajeX3 = personajeX3+90
if event.key==K_a:
personajeX3 = personajeX3-90
if event.key==K_w:
personajeY4 = personajeY4-90
if event.key==K_s:
personajeY4 = personajeY4+90
if event.key==K_d:
personajeX4 = personajeX4+90
if event.key==K_a:
personajeX4 = personajeX4-90
if event.key==K_w:
personajeY5 = personajeY5-90
if event.key==K_s:
personajeY5 = personajeY5+90
if event.key==K_d:
personajeX5 = personajeX5+90
if event.key==K_a:
personajeX5 = personajeX5-90
if event.key==K_w:
personajeY6 = personajeY6-90
if event.key==K_s:
personajeY6 = personajeY6+90
if event.key==K_d:
personajeX6 = personajeX6+90
if event.key==K_a:
personajeX6 = personajeX6-90
#Caballo Der
if event.key==K_4:
personajeY7 = personajeY7+180
personajeX7 = personajeX7+90
if event.key==K_1:
personajeY7 = personajeY7+180
personajeX7 = personajeX7-90
if event.key==K_2:
personajeY7 = personajeY7-180
personajeX7 = personajeX7+90
if event.key==K_3:
personajeY7 = personajeY7-180
personajeX7 = personajeX7-90
if event.key==K_w:
personajeY8 = personajeY8-90
if event.key==K_s:
personajeY8 = personajeY8+90
if event.key==K_d:
personajeX8 = personajeX8+90
if event.key==K_a:
personajeX8 = personajeX8-90
"""
