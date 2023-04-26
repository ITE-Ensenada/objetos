import os
import pygame
from sprite import *
from attributes import *
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Inicialización
pygame.init()

#Pantalla
W, H = 640, 360
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Mama2')
ICONO=pygame.image.load('icon.png')
pygame.display.set_icon(ICONO)

#Fondo del juego
FONDO = pygame.image.load('imagenes/bg/onett.png')

#Música de fondo
pygame.mixer.music.load('sonido/onett.wav')
pygame.mixer.music.play(-1)

QUIETO = pygame.image.load('anim/stand/sd.png')

X=0
PX = 200
PY = 200
ANCHO = 40
VELOCIDAD = 5

#Control de FPS
RELOJ = pygame.time.Clock()

#Variables dirección
IZQUIERDA = False
DERECHA = False
ARRIBA = False
ABAJO = False

#Pasos
CUENTAPASOS = 0

#Movimiento
def recarga_pantalla():
    #Variables globales
    global CUENTAPASOS
    global X
    PANTALLA.blit(FONDO,[0,0])
    #Contador de pasos
    if CUENTAPASOS + 1 >= 3:
        CUENTAPASOS = 0
    #Movimiento a la izquierda
    if IZQUIERDA:
        PANTALLA.blit(Wl[CUENTAPASOS // 1], (int(PX), int(PY)))
        CUENTAPASOS += 1
        # Movimiento a la derecha
    elif DERECHA:
        PANTALLA.blit(Wr[CUENTAPASOS // 1], (int(PX), int(PY)))
        CUENTAPASOS += 1
    elif ABAJO:
        PANTALLA.blit(Wd[CUENTAPASOS // 1], (int(PX), int(PY)))
        CUENTAPASOS += 1
    elif ARRIBA:
        PANTALLA.blit(Wu[CUENTAPASOS // 1], (int(PX), int(PY)))
        CUENTAPASOS += 1

    else:
        PANTALLA.blit(QUIETO,(int(PX), int(PY)))

EJECUTA = True

#Bucle de acciones y controles
while EJECUTA:
    #FPS
    RELOJ.tick(15)

    #Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EJECUTA = False

    #Opción tecla pulsada
    Keys = pygame.key.get_pressed()

    #Tecla A - Moviemiento a la izquierda
    if Keys[pygame.K_a] and PX > -900:
        PX -= VELOCIDAD
        IZQUIERDA = True
        #Tecla D - Moviemiento a la derecha
    elif Keys[pygame.K_d] and PX < 900 - VELOCIDAD - ANCHO:
        PX += VELOCIDAD
        IZQUIERDA = False
        DERECHA = True

    #Personaje quieto
    else:
        IZQUIERDA = False
        DERECHA = False
        CUENTAPASOS = 0

    #Tecla W - Moviemiento hacia arriba
    if Keys[pygame.K_w] and PY > 100:
        PY -= VELOCIDAD
        ARRIBA=True
        ABAJO=False
    #Tecla S - Moviemiento hacia abajo
    if Keys[pygame.K_s] and PY < 300:
        PY += VELOCIDAD
        ABAJO=True
        ARRIBA=False
    
     # Actualización de la ventana
    pygame.display.update()
    #Llamada a la función de actualización de la ventana
    recarga_pantalla()
    #Salir del juego
pygame.quit()
