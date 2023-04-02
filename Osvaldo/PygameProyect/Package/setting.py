# MAPA BINARIO
mapa = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,1],
    [1,0,0,0,1,0,0,1],
    [1,0,1,0,1,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]
]

# CONSTANTES DE LA PANTALLA
screen_Alto = 480
screen_Ancho = screen_Alto * 2 #960

# CONSTANTES DEL MAPA 2D
square = (screen_Ancho / 16 )  # TILE_SIZE
 
# CONSTATNTES PARA EL ALGORITMO RAY CASTING
casted_rays = 120
max_Profundidad = screen_Alto