"""Este programa es un juego centrado en batallas pokemon autor: Juan Roman"""
#pylint: disable=C0103
#pylint: disable=E1101
import sys
import random
import time
import pygame
from pygame.locals import *
from modulos.Clases import *

blanco = (255,255,255)
negro = (0,0,0)

def movertexto(texto, coordenadas):
    """esta funcion escribe dandole el texto y donde se quiere dibujar"""
    narrador = fuentemovimientos.render(texto,True,blanco)
    SCREEN.blit(narrador, coordenadas)
    pygame.display.update()

def presentador(funcion):
    """aqui esta el decorador"""
    def decorador(movimientojugador,pokejugador,pokerival):
        """el cual identifica si se acabo el juego"""
        condicion = funcion(movimientojugador,pokejugador,pokerival)
        return condicion
    return decorador

def batalla(pokejugador,pokerival):
    """funcion principal, donde corre el juego"""
    #elementos para desplegar movimientos
    movimiento1txt = "1)"+movimientosarre[pokejugador.movimientos[0]][0]
    movimiento2txt = "2)"+movimientosarre[pokejugador.movimientos[1]][0]
    movimiento3txt = "3)"+movimientosarre[pokejugador.movimientos[2]][0]
    movimiento4txt = "4)"+movimientosarre[pokejugador.movimientos[3]][0]
    movimiento1 = fuentemovimientos.render(movimiento1txt,True,blanco)
    movimiento2 = fuentemovimientos.render(movimiento2txt,True,blanco)
    movimiento3 = fuentemovimientos.render(movimiento3txt,True,blanco)
    movimiento4 = fuentemovimientos.render(movimiento4txt,True,blanco)
    tipomovimiento1txt = "Tipo: "+tipos[movimientosarre[pokejugador.movimientos[0]][1]]
    tipomovimiento2txt = "Tipo: "+tipos[movimientosarre[pokejugador.movimientos[1]][1]]
    tipomovimiento3txt = "Tipo: "+tipos[movimientosarre[pokejugador.movimientos[2]][1]]
    tipomovimiento4txt = "Tipo: "+tipos[movimientosarre[pokejugador.movimientos[3]][1]]
    tipomovimiento1 = fuentemovimientos.render(tipomovimiento1txt,True,blanco)
    tipomovimiento2 = fuentemovimientos.render(tipomovimiento2txt,True,blanco)
    tipomovimiento3 = fuentemovimientos.render(tipomovimiento3txt,True,blanco)
    tipomovimiento4 = fuentemovimientos.render(tipomovimiento4txt,True,blanco)
    #elementos para desplegar la vida de ambos
    nombrejugadortxt = pokejugador.nombre+"   lv "+str(pokejugador.nivel)
    nombrerivaltxt = pokerival.nombre+"   lv "+str(pokerival.nivel)
    estadisticasjugadortxt = "9) Ver estadisticas"
    estadisticasrivaltxt = "0) Ver estadisticas"
    nombrejugador = fuentetexto.render(nombrejugadortxt,True,negro)
    nombrerival = fuentetexto.render(nombrerivaltxt,True,negro)
    estadisticasjugador = fuentetexto.render(estadisticasjugadortxt,True,negro)
    estadisticasrival = fuentetexto.render(estadisticasrivaltxt,True,negro)
    #para cerrar el juego si alguien gana o pierde
    condicion = 0
    while True: # the main game loop
        vidajugadortxt = "HP: "+str(pokejugador.vida_actual)+"/"+str(pokejugador.vida)
        vidarivaltxt = "HP: "+str(pokerival.vida_actual)+"/"+str(pokerival.vida)
        vidajugador = fuentemovimientos.render(vidajugadortxt,True,negro)
        vidarival = fuentemovimientos.render(vidarivaltxt,True,negro)

        SCREEN.blit(fondo, [0,0])
        SCREEN.blit(imagenrival, (763, 33))
        SCREEN.blit(imagenjugador, (178, 180))

        SCREEN.blit(imagenvida, (700, 310))
        SCREEN.blit(nombrejugador, (715,320))
        SCREEN.blit(estadisticasjugador, (715,360))
        SCREEN.blit(vidajugador, (950,340))

        SCREEN.blit(imagenvida, (70, 100))
        SCREEN.blit(nombrerival, (85, 110))
        SCREEN.blit(estadisticasrival, (85, 150))
        SCREEN.blit(vidarival, (290, 130))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    condicion = turno(0,pokejugador,pokerival)
                if event.key == pygame.K_2:
                    condicion = turno(1,pokejugador,pokerival)
                if event.key == pygame.K_3:
                    condicion = turno(2,pokejugador,pokerival)
                if event.key == pygame.K_4:
                    condicion = turno(3,pokejugador,pokerival)
                if event.key == pygame.K_9:
                    estadisticas(pokejugador)
                if event.key == pygame.K_0:
                    estadisticas(pokerival)

        #texto de los movimientos
        SCREEN.blit(movimiento1, (50, 440))
        SCREEN.blit(tipomovimiento1, (50, 470))
        SCREEN.blit(movimiento2, (310, 440))
        SCREEN.blit(tipomovimiento2, (310, 470))
        SCREEN.blit(movimiento3, (50, 505))
        SCREEN.blit(tipomovimiento3, (50, 535))
        SCREEN.blit(movimiento4, (310, 505))
        SCREEN.blit(tipomovimiento4, (310, 535))
                    
        pygame.display.update()
        fpsClock.tick(FPS)
        if condicion != 0:
            break
@presentador
def turno(movimientojugador,pokejugador,pokerival):
    """esta funcion es para calcular el resultado en cada turno"""
    if pokejugador.velocidad >= pokerival.velocidad:
        textoinicial = pokejugador.nombre+" a usado "+movimientosarre[pokejugador.movimientos[movimientojugador]][0]
        movertexto(textoinicial,(40, 440))
        texto = pokejugador.pelea(pokejugador.movimientos[movimientojugador],pokejugador,pokerival)
        movertexto(texto[0],(40, 470))
        movertexto(texto[1],(40, 500))
        pygame.display.update()
        time.sleep(2)
        if pokerival.vida_actual <= 0:
            movertexto("Has ganado",(900,470))
            time.sleep(2)
            return 1
        movimientorival = random.randrange(0,3)
        textoinicial = pokerival.nombre+" rival a usado "+movimientosarre[pokerival.movimientos[movimientorival]][0]
        movertexto(textoinicial,(500, 440))
        texto = pokerival.pelea(pokerival.movimientos[movimientorival],pokerival,pokejugador)
        movertexto(texto[0],(500, 470))
        movertexto(texto[1],(500, 500))
        time.sleep(2)
        if pokejugador.vida_actual <= 0:
            movertexto("Has perdido",(900,470))
            time.sleep(2)
            return 1
    else:
        movimientorival = random.randrange(0,3)
        texto = pokerival.nombre+" rival a usado "+movimientosarre[pokerival.movimientos[movimientorival]][0]
        movertexto(texto,(40, 440))
        texto = pokerival.pelea(pokerival.movimientos[movimientorival],pokerival,pokejugador)
        movertexto(texto[0],(40, 470))
        movertexto(texto[1],(40, 500))
        time.sleep(2)
        if pokejugador.vida_actual <= 0:
            movertexto("Has perdido",(900,470))
            time.sleep(2)
            return 1
        texto = pokejugador.nombre+" a usado "+movimientosarre[pokejugador.movimientos[movimientojugador]][0]
        movertexto(texto,(500, 440))
        texto = pokejugador.pelea(pokejugador.movimientos[movimientojugador],pokejugador,pokerival)
        movertexto(texto[0],(500, 470))
        movertexto(texto[1],(500, 500))
        time.sleep(2)
        if pokerival.vida_actual <= 0:
            movertexto("Has ganado",(900,470))
            time.sleep(2)
            return 1
    return 0
def estadisticas(pokemon):
    """esta funcion manda a llamar las estadisticas del pokemon"""
    movertexto("Estadisticas de "+pokemon.nombre,(50, 440))
    texto = pokemon.stats()
    movertexto(texto[0],(50, 470))
    movertexto(texto[1],(450, 460))
    movertexto(texto[2],(450, 490))
    movertexto(texto[3],(700, 460))
    movertexto(texto[4],(700, 490))
    movertexto(texto[5],(450, 520))
    time.sleep(6)
    

pokejugador = Swampert()
pokerival = Blaziken()

pygame.init()
FPS = 10 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window

SCREEN = pygame.display.set_mode((1200, 600), 0, 32)
pygame.display.set_caption('Pokemon')

fondo = pygame.image.load('recursos/fondo.png')
fondo = pygame.transform.scale(fondo, (1200, 600))

imagenjugador = pygame.image.load('recursos/'+pokejugador.nombre+'E.png')
imagenjugador = pygame.transform.scale(imagenjugador, (240, 240))
imagenrival = pygame.image.load('recursos/'+pokerival.nombre+'F.png')
imagenrival = pygame.transform.scale(imagenrival, (240, 240))
imagenvida = pygame.image.load('recursos/vida.png')
imagenvida = pygame.transform.scale(imagenvida, (430, 100))


fuentemovimientos = pygame.font.SysFont('Comic Sans MS', 25)
fuentetexto = pygame.font.SysFont('Comic Sans MS', 20)

batalla(pokejugador,pokerival)