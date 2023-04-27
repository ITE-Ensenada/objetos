# pylint: disable=C0103
# pylint: disable=E1101
"""Juego Conecta 4  en Python."""
import sys
import math
import numpy as np
import pygame

N_FILAS = 6
N_COLUMNAS = 7
BLUE, BLACK, YELLOW, GREEN= (0,0,255), (0,0,0), (255,255,0), (0,255,0)

def crear_tablero():
    """aqui creamos el tablero con ayuda de libreria numpy"""
    tablero = np.zeros((N_FILAS, N_COLUMNAS))
    return tablero
def espacio_valido (tablero, col):
    """va checando el espacio valido"""
    return tablero[N_FILAS-1][col] == 0
def sig_f_vacia(tablero, col):
    """siguiente fila vacia"""
    for filas in range(N_FILAS):
        if tablero [filas][col] == 0:
            return filas
def soltar_pieza(tablero, fila, col, pieza):
    """soltar pieza tal cual que se vea reflejada"""
    tablero[fila][col] = pieza
def imprimir_tablero(tablero):
    """esta funcion imprime el tablero."""
    print(np.flipud(tablero))
def movida_ganadora(tablero, pieza):
    """va checando cada movimiento en columnas y filas"""
    #checar posiciones en horizontal\
    for columna in range(N_COLUMNAS-3):
        for filas in range(N_FILAS):
            if (tablero[filas][columna] == pieza
                and tablero[filas][columna+1] == pieza
                and tablero[filas][columna+2] == pieza
                and tablero[filas][columna+3] == pieza):
                return True
    #checar posiciones en vertical
    for columna in range(N_COLUMNAS):
        for filas in range(N_FILAS-3):
            if (tablero[filas][columna] == pieza
                and tablero[filas+1][columna] == pieza
                and tablero[filas+2][columna] == pieza
                and tablero[filas+3][columna] == pieza):
                return True
    #checar posiciones en diagonal con pendiente positiva
    for columna in range(N_COLUMNAS-3):
        for filas in range(N_FILAS -3):
            if (tablero[filas][columna] == pieza
                and tablero[filas+1][columna+1] == pieza
                and tablero[filas+2][columna+2] == pieza
                and tablero[filas+3][columna+3] == pieza):
                return True
    #checar posiciones en horizontal
    for columna in range(N_COLUMNAS-3):
        for filas in range(3, N_FILAS):
            if (tablero[filas][columna] == pieza
                and tablero[filas-1][columna+1] == pieza
                and tablero[filas-2][columna+2] == pieza
                and tablero[filas-3][columna+3] == pieza):
                return True
            
def dibujar_tablero(tablerito):
    """dibuja el tablero""" 
    for columna  in range(N_COLUMNAS):
        for filas in range(N_FILAS):
            pygame.draw.rect(screen, BLUE, (columna*squaresize, filas*squaresize+squaresize,
            squaresize, squaresize))
            pygame.draw.circle(screen, BLACK, (int(columna*squaresize+(squaresize/2)),
            int(filas*squaresize+squaresize+(squaresize/2))), RADIO)
            pygame.display.update()
    for columna  in range(N_COLUMNAS):
        for filas in range(N_FILAS):
            if tablerito [filas][columna] == 1:
                pygame.draw.circle(screen, YELLOW, (int(columna*squaresize+(squaresize/2)),
                int(alto-(filas*squaresize+(squaresize/2)))), RADIO)
            elif tablerito [filas][columna] == 2:
                pygame.draw.circle(screen, GREEN, (int(columna*squaresize+(squaresize/2)),
                int(alto-(filas*squaresize+(squaresize/2)))), RADIO)
    
    pygame.display.update()


tablerito = crear_tablero()
imprimir_tablero(tablerito)
JUEGOTERMINADO, turn = False, 0

pygame.init()

squaresize = 90
RADIO = int((squaresize/2) - 5)
ancho = N_COLUMNAS * squaresize
alto = (1+ N_FILAS) * squaresize
size = (ancho, alto)
screen = pygame.display.set_mode(size)
pygame.display.update()
dibujar_tablero(tablerito)
while not JUEGOTERMINADO:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x = event.pos[0]
            # # solicitar el movimiento del jugador 1
            if turn == 0:
                pos_x = event.pos[0]
                colu = math.floor(int(pos_x/squaresize))
                if espacio_valido(tablerito, colu):
                    fila = sig_f_vacia(tablerito, colu)
                    soltar_pieza(tablerito, fila, colu, 1)
                    if movida_ganadora(tablerito, 1):
                        print ("Ganador jugador 1 felicidades!!")
                        JUEGOTERMINADO = True
            else:
                pos_x = event.pos[0]
                colu = math.floor(int(pos_x/squaresize))
                if espacio_valido(tablerito, colu):
                    fila = sig_f_vacia(tablerito, colu)
                    soltar_pieza(tablerito, fila, colu, 2)
                    if movida_ganadora(tablerito, 2):
                        print ("Ganador jugador 2 felicidades!!")
                        JUEGOTERMINADO = True

            imprimir_tablero(tablerito)
            dibujar_tablero(tablerito)
            turn += 1
            turn = turn % 2
