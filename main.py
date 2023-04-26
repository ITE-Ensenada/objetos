import pygame
import sys
import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#Iniciación de Pygame
pygame.init()

#Pantalla - ventana
W, H = 640, 360
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Mama2')
icono=pygame.image.load('icon.png')
pygame.display.set_icon(icono)

#Fondo del juego
fondo = pygame.image.load('imagenes/bg/onett.png')

#Música de fondo
pygame.mixer.music.load('sonido/onett.wav')
pygame.mixer.music.play(-1)


#Personaje
quieto = pygame.image.load('anim/stand/sd.png')

wr = [pygame.image.load('anim/walkr/wr1.png'),
    pygame.image.load('anim/walkr/wr2.png')]

wl = [pygame.image.load('anim/walkl/wl1.png'),
    pygame.image.load('anim/walkl/wl2.png')]

wu = [pygame.image.load('anim/walku/wu1.png'),
    pygame.image.load('anim/walku/wu2.png')]

wd = [pygame.image.load('anim/walkd/wd1.png'),
    pygame.image.load('anim/walkd/wd2.png')]


x=0
px = 200
py = 200
ancho = 40
velocidad = 5

#Control de FPS
reloj = pygame.time.Clock()



#Variables dirección
izquierda = False
derecha = False
arriba = False
abajo = False

#Pasos
cuentaPasos = 0

#Movimiento
def recargaPantalla():
    #Variables globales
    global cuentaPasos
    global x
    PANTALLA.blit(fondo,[0,0])
    #Contador de pasos
    if cuentaPasos + 1 >= 3:
        cuentaPasos = 0
    #Movimiento a la izquierda
    
    if izquierda:
        PANTALLA.blit(wl[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
        # Movimiento a la derecha
    elif derecha:
        PANTALLA.blit(wr[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
    elif abajo:
        PANTALLA.blit(wd[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
    elif arriba:
        PANTALLA.blit(wu[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    else:
        PANTALLA.blit(quieto,(int(px), int(py)))

ejecuta = True

#Bucle de acciones y controles
while ejecuta:
    #FPS
    reloj.tick(15)

    #Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    #Opción tecla pulsada
    keys = pygame.key.get_pressed()

    #Tecla A - Moviemiento a la izquierda
    if keys[pygame.K_a] and px > -900:
        px -= velocidad
        izquierda = True
        

    #Tecla D - Moviemiento a la derecha
    elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True

    #Personaje quieto
    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0

    #Tecla W - Moviemiento hacia arriba
    if keys[pygame.K_w] and py > 100:
        py -= velocidad
        arriba=True
        abajo=False
    #Tecla S - Moviemiento hacia abajo
    if keys[pygame.K_s] and py < 300:
        py += velocidad
        abajo=True
        arriba=False
    

    # Actualización de la ventana
    pygame.display.update()
    #Llamada a la función de actualización de la ventana
    recargaPantalla()

#Salida del juego
pygame.quit()