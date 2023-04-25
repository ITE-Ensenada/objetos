import sys, random, pygame
from pygame.locals import *
from modulos.Clases import *
#pokemon espalda x178 y183
#pokemon frente x763 y33
def presentador(funcion):
    def decorador(pokejugador,pokerival):
        print("Te has topado con un",pokerival.nombre,"salvaje")
        print("Ve",pokejugador.nombre)
        a = funcion(pokejugador,pokerival)
        print("Finalizo el combate")
        return a
    return decorador
@presentador
def batalla(pokejugador,pokerival):
    while(0==0):

        movimientojugador = random.randrange(0,3)
        if pokejugador.velocidad >= pokerival.velocidad:
            pokejugador.pelea(pokejugador.movimientos[movimientojugador],pokejugador,pokerival)
            if pokerival.vida <= 0:
                print("Has vencido")
                break
            pokerival.pelea(pokerival.movimientos[random.randrange(0,3)],pokerival,pokejugador)
            if pokejugador <= 0:
                print("Fuiste derrotado")
                break
        else:
            pokerival.pelea(pokerival.movimientos[random.randrange(0,3)],pokerival,pokejugador)
            if pokejugador.vida <= 0:
                print("Fuiste derrotado")
                break
            pokejugador.pelea(pokejugador.movimientos[movimientojugador],pokejugador,pokerival)
            if pokerival.vida <= 0:
                print("Has vencido")
                break

pokejugador = Snorlax()
pokerival = Decidueye()
batalla(pokejugador,pokerival)

FPS = 10 # frames per second setting

fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1200, 600), 0, 32)

pygame.display.set_caption('Pokemon')

fondo = pygame.image.load('recursos/fondo.jpg')

imagenjugador = pygame.image.load('recursos/'+pokejugador.nombre+'E.png')
imagenjugador = pygame.transform.scale(imagenjugador, (240, 240))
imagenrival = pygame.image.load('recursos/'+pokerival.nombre+'F.png')
imagenrival = pygame.transform.scale(imagenrival, (240, 240))

personajeX = 650
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
                    personajeY -= 1
                    print(personajeX,personajeY)
            if event.key ==pygame.K_s:
                if personajeY < 600:
                    personajeY += 1
                    print(personajeX,personajeY)
            if event.key ==pygame.K_d:
                if personajeX < 1200:
                    personajeX += 1
                    print(personajeX,personajeY)
            if event.key ==pygame.K_a:
                if personajeX > 0:
                    personajeX -= 1
                    print(personajeX,personajeY)
					
    SCREEN.blit(imagenjugador, (178, 183))
    SCREEN.blit(imagenrival, (763, 33))

    pygame.display.update()
    fpsClock.tick(FPS)