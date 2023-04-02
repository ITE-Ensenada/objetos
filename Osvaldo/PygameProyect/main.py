import pygame
from Package import *
from math import sin,cos,pi,radians

# OBJETOS
jugador = Player( (screen_Ancho / 4) + ( square * (3/2) ) , square * (3/2) , pi , pi/3 )
clock = pygame.time.Clock()

# INICIO DE LA PANTALLA
screen = pygame.display.set_mode((screen_Ancho, screen_Alto))
pygame.display.set_caption("Intento raycasting")

while True:
    


    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        
        # ---
        draw_map2D(screen, jugador)

        # APLICAR RAY CASTING
        ray_cast(screen, jugador)


        #Detecta teclas
        if keys[pygame.K_LEFT]:
            jugador.angle = -0.1
        if keys[pygame.K_RIGHT]:
            jugador.angle = 0.1
        if keys[pygame.K_UP]:
            jugador.posX = -math.sin(jugador.angle) * 5
            jugador.posY = math.cos(jugador.angle) * 5
        if keys[pygame.K_DOWN]:
            jugador.posX = math.sin(jugador.angle) * 5
            jugador.posY = -math.cos(jugador.angle) * 5
        
        # if keys[pygame.K_m]:
        #     draw_map2D(screen, jugador)


        # FIN DEL JUEGO
        if keys[pygame.QUIT] or keys[pygame.K_ESCAPE]: end_game()

        


    # ACTUALIZA LA PANTALLA
    pygame.display.flip()

    # CONTOLA LOS FPS
    clock.tick(30)
