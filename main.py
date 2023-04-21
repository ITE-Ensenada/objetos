import pygame, sys
from pygame.locals import *
from Personaje import *
from Weapon import *

# ***************************************

			# Objects

p1 = Character("John Wick", "50", "1", "5", "2", "20", "10", "7", "1.80", "Blanco")
p1.showCharacter()
glock34 = Pistol("\nPistola", "27", "Unico", "120m", "Fibra de carbono")
glock34.ShowWeapon()

# ***************************************

pygame.init()

FPS = 60  # frames per second setting

fpsClock = pygame.time.Clock()

# Ajustes de la ventana

size = (1023, 616)
SCREEN = pygame.display.set_mode(size)

pygame.mouse.set_visible(0)
pygame.display.set_caption("Juego")

WHITE = (179, 113, 209)
fondo = pygame.image.load("City.png").convert()

# ****** Personaje *******

personajeImg = pygame.image.load("John.png")
personajeImg = pygame.transform.scale(personajeImg, (200, 150))

personajeX = 1

personajeY = 400

# ***********************

# Obstaculo

speed = 0

# Codigo para las direcciones
while True: 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

     #Evento teclado
    if personajeX <= 858 and personajeY == 400:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed = 5
            if event.key == pygame.K_LEFT:
                speed = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed = 0
            if event.key == pygame.K_RIGHT:
                speed = 0


    else:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed = 0
            if event.key == pygame.K_LEFT:
                speed = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed = 0
            if event.key == pygame.K_RIGHT:
                speed = 0
    if personajeY <= 0:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed = 5
            if event.key == pygame.K_LEFT:
                speed = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed = 0
            if event.key == pygame.K_RIGHT:
                speed = 0

    SCREEN.blit(fondo, [0, 0])
    SCREEN.blit(personajeImg, (personajeX, personajeY))
    personajeX += speed

    pygame.draw.rect(SCREEN, WHITE, (personajeY, personajeY, 0, 0))
    pygame.display.flip()
    fpsClock.tick(60)