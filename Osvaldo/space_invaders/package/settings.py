''' Descripcion: Este archivo contiene las variables globales del juego '''

from pygame import FULLSCREEN, SCALED

# SCREEN SETTINGS
RESOLUTION = ANCHO, ALTO = 1920 / 2 , 1080 / 2 # 960 x 540
FLAGS = FULLSCREEN | SCALED
FPS = 60

# PLAYER SETTING
X = ANCHO / 2 - 50 # 430
Y = ALTO - 96 # 444
PLAYER_SPEED = 0.25
PLAYER_LIFE = 3

# ASTEROID SETTING
ASTEROID_SPEED = 0.5
INTERVAL_ASTEOID = 2000
ASTEROID_INTERVAL = 500

# BACKGROUND SETTING
BACKGROUND_SPEED = 0.05
