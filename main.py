'''
    El modulo main:

    Aqui se importan los demas modulos
    Se crean los objetos
    Valida el funcionamiento del juego
    Valida al usuario
'''

# pylint: disable=C0103
# pylint: disable = E1101
#pylint: disable=W0401
#pylint: disable=W0631
#pylint: disable=W0614

# Librerias-Modulos:

import sys
import functools
from time import sleep
import pygame
from pygame.locals import *
from Personaje import *
from Weapon import Pistol
from Suit import*

name = input("Favor de escribir tu nombre: ")
age = input("Favor de escribir tu edad: ")
intAge = int(age)

def decorador_player(f):
    '''
    El siguiente decorador nos ayudara
    a tomar en cuenta los datos proporcionados
    anteriormente: nombre y edad
    '''
    @functools.wraps(f)
    def function_f(args, kwargs):
        print("\nHola, estamos validando la informacion proporcionada: ")
        sleep(3)
        f(args, kwargs)
    return function_f

@decorador_player
def func_validacion(name, intAge):

    '''
    Ya que el usuario/jugador haya ingresado sus datos
    los validamos por medio del siguiente algoritmo:
    '''
    print("\nNombre: ", name, "\nEdad: ", intAge)
    if intAge < 18:
        print("\nNo puedes jugar")
        sys.exit()
    else:
        print("\nBienvenido, disfruta del juego")

func_validacion(name, intAge)

pygame.init()

# Objetos creados:

# Jugador(s)

player1 = Player(" ", " ")
# el objeto player toma la informacion ingresada en la linea 23
player1.name = name
print("Jugador uno: ", player1.name)

# Personaje(s)

p1 = Character("John Wick", "50", "1", "5", "2", "10", "7", "1.80", "Blanco")
p1.show()

# Arma(s)
glock34 = Pistol("\nPistola", "27", "Unico", "120m", "Fibra de carbono")


# Traje(s)
suit1 = Suit("Rojo", "Kevlar", "Corte Ingles", True, 2, "Negra")
suit2 = Suit("Gris", "Kevlar", "Corte Frances", True, 2, "Negra")
suit1.show_suit()
# True = 1, False = 0 (Estos valores se imprimen)

fps = 60  # frames per second setting

fps_clock = pygame.time.Clock()

# Ajustes de la ventana

size = (1023, 616)
screen = pygame.display.set_mode(size)

pygame.mouse.set_visible(0)
pygame.display.set_caption("Juego")

fondo = pygame.image.load("City.png").convert()

personaje_img = pygame.image.load("JohnR.png")
personaje_img = pygame.transform.scale(personaje_img, (200, 150))

white = (255, 255, 255)

personaje_x = 1
personaje_y = 400
speed = 0

# Codigo para las direcciones

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

     # Evento teclado
    if personaje_x <= 858 and personaje_y == 400:
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
    if personaje_y <= 0:
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

    screen.blit(fondo, [0, 0])
    screen.blit(personaje_img, (personaje_x, personaje_y))
    personaje_x += speed

    pygame.draw.rect(screen, white, (personaje_y, personaje_y, 0, 0))
    pygame.display.flip()
    fps_clock.tick(60)
