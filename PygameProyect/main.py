import pygame
from Package import *
from math import sin,cos,pi,radians

# CLASES
class Player:
    def __init__(self, posX, posY, angle, fov):
        self._posX = posX
        self._posY = posY
        self._angle = angle
        self._fov = fov
        self._halfFOV = fov / 2

    @property
    def fov(self):
        return self._fov

    @property
    def halfFOV(self):
        return self._halfFOV

    @property
    def fov(self):
        return self._fov
    
    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self, value):
        self._angle += value
    
    @property
    def posX(self):
        return self._posX
    
    @posX.setter
    def posX(self, value):
        self._posX = value
    
    @property
    def posY(self):
        return self._posY
    
    @posY.setter
    def posY(self, value):
        self._posY = value

# MAPA DEL JUEGO EN BINARIO
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


# CONSTANTES 
screen_Alto = 480
screen_Ancho = screen_Alto * 2
square = (screen_Ancho / 16 ) 


# OBJETOS
jugador = Player( (screen_Ancho / 4) + ( square * (3/2) ) , square * (3/2) , pi , pi/3 )
clock = pygame.time.Clock()

# INICIO DE LA PANTALLA
screen = pygame.display.set_mode((screen_Ancho, screen_Alto))
pygame.display.set_caption("Intento raycasting")

while True:
    


    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        # FIN DEL JUEGO
        end_game(event)
        
        # ---
        draw_map2D(event, screen, square, screen_Ancho, mapa, jugador)
        
        if keys[pygame.K_LEFT]:
            jugador.angle = -0.1
        if keys[pygame.K_RIGHT]:
            jugador.angle = 0.1
        


    # ACTUALIZA LA PANTALLA
    pygame.display.flip()

    # CONTOLA LOS FPS
    clock.tick(30)
