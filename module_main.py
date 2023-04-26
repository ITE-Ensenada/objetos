# pylint: disable=C0103
import sys
import pygame
from pygame.locals import *
from personajes import *

pygame.init()

FPS = 60  # frames per second setting
fps_clock = pygame.time.Clock()

# Set up the window
SCREEN = pygame.display.set_mode((1200, 675), 0, 32)
pygame.display.set_caption('Animation')

fondo = pygame.image.load("imagenes/fuente.png").convert()
fondo = pygame.transform.scale(fondo, (1200, 675))

WHITE = (255, 255, 255)

personaje_img = pygame.image.load('imagenes/link.png')
personaje_img = pygame.transform.scale(personaje_img, (125, 90))

#spawn del personaje
personaje_x = 0
personaje_y = 540

x_speed = 0
y_speed = 0

direction = 'right'

#caracteristicas del personaje jugable
player1 = Jugador("Masculino", "250", "Link", "100", "Hyliano", "60 kg", "1.4 m", "Rubio")
Jugador.mostrar_caracteristicas(player1)

#caracteristicas del enemigo (WIP)
enemigo1 = Enemigo("Masculino", "5000", "Artorias", "Espadon", "Guerrero", "Ataques a largas distancias", "Alma de Artorias")
Enemigo.mostrar_caracteristicas(enemigo1)

# Coordenadas del personaje
while True:  # el ciclo del juego
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
                print('Izquierda')
            if event.key == pygame.K_RIGHT:
                x_speed = 3
                print('Derecha')
            if event.key == pygame.K_a:
                print('salto')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_a:
                print('dejo de saltar')
                
    SCREEN.fill(WHITE)
    SCREEN.blit(fondo, (0, 0))
    SCREEN.blit(personaje_img, (personaje_x, personaje_y))
    personaje_x += x_speed
    pygame.draw.rect(SCREEN, WHITE, (personaje_x, personaje_y, 0, 0))
    pygame.display.update()
    fps_clock.tick(FPS)