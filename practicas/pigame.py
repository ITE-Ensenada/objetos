import sys, pygame, random
from pygame.locals import *
from modulos.Clases import *

pygame.init()

FPS = 10 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1200, 600), 0, 32)

pygame.display.set_caption('PUCHAMOOOOOOON')

fondo = pygame.image.load('recursos/fondo.jpg')

personajeImg = pygame.image.load('recursos/prota.png')
personajeImg = pygame.transform.scale(personajeImg, (50, 50))

personajeX = 10

personajeY = 10

while True: # the main game loop

    SCREEN.blit(fondo, [0,0])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_w:
                if personajeY > 0:
                    personajeY -= 5
            if event.key ==pygame.K_s:
                if personajeY < 350:
                    personajeY += 5
            if event.key ==pygame.K_d:
                if personajeX < 550:
                    personajeX += 5
            if event.key ==pygame.K_a:
                if personajeX > 0:
                    personajeX -= 5
					
    SCREEN.blit(personajeImg, (personajeX, personajeY))

    pygame.display.update()
    fpsClock.tick(FPS)