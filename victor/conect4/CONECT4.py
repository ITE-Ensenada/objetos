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
    
def movida_ganadora(tablero, pieza):
    #checar posiciones en horizontal\
    for c in range(N_COLUMNAS-3):
        for f in range(N_FILAS):
            if tablero[f][c] == pieza and tablero[f][c+1] == pieza and tablero[f][c+2] == pieza and tablero [f][c+3] == pieza:
              return True 
    #checar posiciones en vertical
    for c in range(N_COLUMNAS):
        for f in range(N_FILAS-3):
            if tablero[f][c] == pieza and tablero[f+1][c] == pieza and tablero[f+2][c] == pieza and tablero [f+3][c] == pieza:
              return True 
    #checar posiciones en diagonal con pendiente positiva
    for c in range(N_COLUMNAS-3):
        for f in range(N_FILAS -3):
            if tablero[f][c] == pieza and tablero[f+1][c+1] == pieza and tablero[f+2][c+2] == pieza and tablero [f+3][c+3] == pieza:
              return True 
    #checar posiciones en horizontal
    for c in range(N_COLUMNAS-3):
        for f in range(3, N_FILAS):
            if tablero[f][c] == pieza and tablero[f-1][c+1] == pieza and tablero[f-2][c+2] == pieza and tablero [f-3][c+3] == pieza:
              return True 
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

           if movida_ganadora(tablero, 1):
                print ("Ganador jugador 1 felicidades!!")
                imprimir_tablero(tablero)
                game_over = True
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
                game_over = True
                break
            

    turn += 1
    turn = turn % 2