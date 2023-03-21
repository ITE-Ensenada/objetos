import pygame
from Package import *
from math import sin,cos,pi

# CLASES
class Player:
    def __init__(self, posX, posY, angle):
       self._posX = posX
       self._posY = posY
       self._angle = angle

    def draw_player( self, screen ):
        pygame.draw.circle(screen, (255, 0, 0), (self.posX, self.posY), 10) #Por arreglar

    @property
    def angle(self):
        return self._angle
    
    @property
    def posX(self):
        return self._posX
    
    @posX.setter
    def posX(self, value):
        self._posX = value
    
    @property
    def posY(self):
        return self._posY
    
    @posX.setter
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

# OBJETOS
jugardor = Player(1,1,pi)
clock = pygame.time.Clock()


# CONSTANTES
screen_Alto = 480
screen_Ancho = screen_Alto * 2
fov = pi / 3 
half_fov = fov / 2

# INICIO DE LA PANTALLA
screen = pygame.display.set_mode((screen_Ancho, screen_Alto))
pygame.display.set_caption("Intento raycasting")

while True:



    for event in pygame.event.get():

        # ---
        draw_map2D(event, screen, screen_Alto, screen_Ancho, mapa)
        jugardor.draw_player( screen ) #Por arreglar

        # FIN DEL JUEGO
        event_loop(event)


    # ACTUALIZA LA PANTALLA
    pygame.display.flip()

    # CONTOLA LOS FPS
    clock.tick(30)
