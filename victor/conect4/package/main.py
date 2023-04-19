import numpy as np

N_FILAS = 6
N_COLUMNAS = 7

def crear_tablero():
    tablero = np.zeros((N_FILAS, N_COLUMNAS))
    return tablero

def espacio_valido (tablero, col):
    return tablero[N_FILAS-1][col] == 0
 
def sig_f_vacia(tablero, col):
    for f in range(N_FILAS):
        if tablero [f][col] == 0:
            return f
        
def soltar_pieza(tablero, fila, col, pieza):
    tablero[fila][col] = pieza

def imprimir_tablero(tablero):
    print(np.flipud(tablero))
    
tablero = crear_tablero()
imprimir_tablero(tablero)

game_over, turn = False, 0

while not game_over:

    # solicitar el movimiento del jugador 1\
    if turn == 0:
       col = int(input("jugador 1 haz tu movida (0-6):"))
       if espacio_valido(tablero, col):
           fila = sig_f_vacia(tablero, col)
           soltar_pieza(tablero, fila, col, 1)
           imprimir_tablero(tablero)

    else:
        col = int(input("jugador 2 haz tu movida (0-6):"))
        if espacio_valido(tablero, col):
            fila = sig_f_vacia(tablero, col)
            soltar_pieza(tablero, fila, col, 2)
            imprimir_tablero(tablero)

    turn += 1
    turn = turn % 2