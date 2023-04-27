'''Descripcion: Este archivo contiene las variables globales del juego'''

MAPA = [
'                                              XXXXX',
'                                              X X X',
'                                            X XXXXX',
' XX    XXX         XX         XXXX        XXX X   X',
' XX                                       XXX X   X',
' XXXX         XX      XX                     XXX XX',
' XXXX       XX               XX               XXXXX',
' XX    X XXXX   XX XX                         XXXXX',
'       X XXXX   XX XXX    XX     XXXX         XXXXX',
' P  XXXX XXXXXX XX XXXX   XX                  XXXXX',
'XXXXXXXX XXXXXX XX XXXXX  XXXXXX          XXXXXXXXX']

#P para colocar jugador
#X sirve para colocar los obstaculos

TILE_SIZE = 64
ANCHO_PANTALLA = 1200
ALTO_PANTALLA= len(MAPA) * TILE_SIZE
