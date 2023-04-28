"""Modulo principal el cual muestra y ejecuta el juegos"""
#pylint: disable = C0103
#pylint: disable = E1101

import sys
import pygame
import pygame.locals
from monito import Personaje
from disparo import Arma

# datos jugador
def pregunta(func):
    """Pregunta nombre y edad del jugador"""
    def nom_edad():
        nombre = input("Ingresa tu nombre: ")
        edad = int(input("Ingresa tu edad: "))
        func(nombre, edad)

    return nom_edad

@pregunta
def verificador(nombre, edad):
    """Verifica si se es mayor de edad"""  
    if edad >= 18:
        print(f"Puedes jugar {nombre}!, eres mayor")
    else:
        print(f"No puedes jugar {nombre}!, ya que tu edad es: {edad}")
        exit()

verificador()

# Importa las clases
Jugador = Personaje("Salvador", "1", "10", "5", "100")
Personaje.presentacion(Jugador)

disparo = Arma("10", "5")
Arma.accion(disparo)

pygame.init()

#Cuadros por segundo
FPS = 60

fpsClock = pygame.time.Clock()

# Ajustes de la ventana

tamanio = (1024, 1024)
SCREEN = pygame.display.set_mode(tamanio)

pygame.mouse.set_visible(0)
pygame.display.set_caption("Juego")

WHITE = (179, 113, 209)
fondo = pygame.image.load("fondo.png").convert()
personajeImg = pygame.image.load("nave.png")
personajeImg = pygame.transform.scale(personajeImg, (100, 100))

personajeX = 5

personajeY = 10

velocidad = 0

# Aqui es para direccionar
event = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Evento teclado
    if personajeY <= 858:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                velocidad = 5
            if event.key == pygame.K_UP:
                velocidad = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                velocidad = 0
            if event.key == pygame.K_DOWN:
                velocidad = 0

    else:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                velocidad = 0
            if event.key == pygame.K_UP:
                velocidad = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                velocidad = 0
            if event.key == pygame.K_DOWN:
                velocidad = 0
    if personajeY <= 0:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                velocidad = 5
            if event.key == pygame.K_UP:
                velocidad = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                velocidad = 0
            if event.key == pygame.K_DOWN:
                velocidad = 0

    SCREEN.blit(fondo, [0, 0])
    SCREEN.blit(personajeImg, (personajeX, personajeY))
    personajeY += velocidad
    pygame.draw.rect(SCREEN, WHITE, (personajeY, personajeY, 0, 0))
    pygame.display.flip()
    fpsClock.tick(60)
    
