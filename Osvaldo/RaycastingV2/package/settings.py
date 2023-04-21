from math import pi
from pygame import display

# VARIABLES JUEGO
RESOLUCION = ANCHO, ALTO = [1920, 1080]
FPS = 60

# VARIABLES DIBUJO 2D
tile_square_size = 100

# VARIABLES PLAYER
PLAYER_POSITION = x, y = 1.5, 1.5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.00175
PLAYER_SPEED_RUNNING = PLAYER_SPEED + 0.00225
PLAYER_SPEED_ROTATION = 0.0035

# VARIABLES CONTROL MOUSE
MOUSE_SENSIBILITY = 0.0004
LEFT_MOUSE_LIMIT = 10
RIGHT_MOUSE_LIMIT = ANCHO - LEFT_MOUSE_LIMIT
MOUSE_REL_LIMIT = 40

# VARIABLES CAMARA
FOV = pi/3
HALF_FOV = FOV / 2

# VARIABLES RAYCASTING
NUM_RAYS = ANCHO 
MAX_DEPTH = tile_square_size * 8
DELTA_ANGLE = FOV / NUM_RAYS