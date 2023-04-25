"""Juego Conecta 4  en Python."""
import numpy as np
N_FILAS = 6
N_COLUMNAS = 7
def crear_tablero():
    '''aqui creamos el tablero con ayuda de libreria numpy'''
    tablero = np.zeros((N_FILAS, N_COLUMNAS))
    return tablero
def espacio_valido (tablero, col):
    '''va checando el espacio valido'''
    return tablero[N_FILAS-1][col] == 0
def sig_f_vacia(tablero, col):
    '''siguiente fila vacia'''
    for filas in range(N_FILAS):
        if tablero [filas][col] == 0:
            return filas
def soltar_pieza(tablero, fila, col, pieza):
    '''soltar pieza tal cual que se vea reflejada'''
    tablero[fila][col] = pieza
def imprimir_tablero(tablero):
    '''esta funcion imprime el tablero.'''
    print(np.flipud(tablero))
def movida_ganadora(tablero, pieza):
    '''va checando cada movimiento en columnas y filas'''
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
tablero = crear_tablero()
imprimir_tablero(tablero)
JUEGOTERMINADO, turn = False, 0
while not JUEGOTERMINADO:
    # solicitar el movimiento del jugador 1
    if turn == 0:
        col = int(input("jugador 1 haz tu movida (0-6):"))
        if espacio_valido(tablero, col):
            fila = sig_f_vacia(tablero, col)
            soltar_pieza(tablero, fila, col, 1)
            imprimir_tablero(tablero)
            if movida_ganadora(tablero, 1):
                print ("Ganador jugador 1 felicidades!!")
                imprimir_tablero(tablero)
                JUEGOTERMINADO = True
                break
    else:
        col = int(input("jugador 2 haz tu movida (0-6):"))
        if espacio_valido(tablero, col):
            fila = sig_f_vacia(tablero, col)
            soltar_pieza(tablero, fila, col, 2)
            imprimir_tablero(tablero)
            if movida_ganadora(tablero, 2):
                print ("Ganador jugador 2 felicidades!!")
                imprimir_tablero(tablero)
                JUEGOTERMINADO = True
                break
    turn += 1
    turn = turn % 2