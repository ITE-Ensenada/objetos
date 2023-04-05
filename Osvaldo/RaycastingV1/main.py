import pygame
from Package import *
from math import sin,cos,pi,radians

# OBJETOS
jugador = Player( (screen_Ancho / 4) + ( square * (3/2) ) , square * (3/2) , pi , pi/3 )
clock = pygame.time.Clock()

# INICIO DE LA PANTALLA
screen = pygame.display.set_mode((screen_Ancho, screen_Alto), )
pygame.display.set_caption("Intento raycasting")

while True:
    # VARIABLE DE TECLAS
    keys = pygame.key.get_pressed()

    # BACKGROUND UPDATE
    pygame.draw.rect(screen, ( 50, 50, 50 ), ( 0, 0, screen_Ancho, screen_Alto))

    # DIBUJO DEL MAPA 2D
    # draw_map2D(screen, jugador)
    
    # ALGORITMO RAYCASTING
    ray_cast(screen, jugador)

    # EVENTOS DEL TECLADO
    if keys[pygame.K_LEFT]:
        jugador.angle = -0.025
    if keys[pygame.K_RIGHT]:
        jugador.angle = 0.025
    if keys[pygame.K_UP]:
        jugador.posX = -math.sin(jugador.angle) * 1.5
        jugador.posY = math.cos(jugador.angle) * 1.5
    if keys[pygame.K_DOWN]:
        jugador.posX = math.sin(jugador.angle) * 1.5
        jugador.posY = -math.cos(jugador.angle) * 1.5
    if keys[pygame.K_ESCAPE]: end_game()
    
    # EVENTOS EN CICLO FOR
    for event in pygame.event.get():
        # FIN DEL JUEGO
        if event.type == pygame.QUIT: end_game()
    
    # ACTUALIZA LA PANTALLA
    pygame.display.flip()

    # CONTOLA LOS FPS
    clock.tick(120)
