from sys import exit
import pygame
import math
from Package.setting import *

# FIN DEL JUEGO
def end_game():
    pygame.quit()
    exit()



# DIBUJO DEL MAPA EN 2D
def draw_map2D(screen, jugador):
    
    # INICIO DE DIBUJO EN EL EJE X
    start_X = (screen_Ancho / 4)
    
    # ACTUALIZACION DEL BACKGROUND
    pygame.draw.rect( screen, ( 0, 0, 0 ), ( 0, 0, screen_Ancho, screen_Ancho / 2 ) )
    
    # DIBUJA EL MAPA 2D
    for col in range( len( mapa ) ):
        for row in range( len( mapa ) ):
            
            pygame.draw.rect( screen, ( 255, 255, 255 ) if mapa[col][row] == 1 else ( 100, 100 , 100 ),
                            ( start_X + ( square * row ), ( square * col + 1 ), square - 1, square - 1))
            
    # DIBUJA EL JUGADOR
    pygame.draw.circle(screen, ( 255, 0, 0 ), ( int( jugador.posX ), int( jugador.posY ) ), 8)

    # DIBUJA LA DIRECCION DEL JUGADOR
    # pygame.draw.line(screen, ( 0, 255, 0 ), ( jugador.posX, jugador.posY ), ( jugador.posX - math.sin( jugador.angle ) * 30, 
    #                                                                           jugador.posY + math.cos( jugador.angle ) * 30 ) , 3 )
    
    # DIBUJAR EL FOV
    # pygame.draw.line(screen, ( 0, 255, 0 ), (jugador.posX , jugador.posY ), ( jugador.posX - math.sin( jugador.angle - jugador.halfFOV) * 30, 
    #                                                                           jugador.posY + math.cos( jugador.angle - jugador.halfFOV ) * 30 ) , 3 ) 
    # 
    # pygame.draw.line(screen, ( 0, 255, 0 ), (jugador.posX , jugador.posY ), ( jugador.posX - math.sin( jugador.angle + jugador.halfFOV) * 30, 
    #                                                                           jugador.posY + math.cos( jugador.angle + jugador.halfFOV ) * 30 ) , 3 ) 


# ALGORITMO DE RAY CASTING 
def ray_cast2D(screen, jugador):
    # DEFINIR EL AVANCE DE CADA RAYO
    step_angle = jugador.fov / casted_rays

    # DEFINIR EL ANGULO MAS A LA IZQUIERDA DEL FOV
    start_angle = jugador.angle -  jugador.halfFOV

    # INICIO DE DIBUJO EN EL EJE X
    start_X = (screen_Ancho / 4)

    # Increment angl(e by a single step
    for ray in range(casted_rays):
        
        for profundidad in range(max_Profundidad):
            # OBTENER COORDENADAS DEL OBJETIVO
            target_x = jugador.posX - math.sin( start_angle ) * profundidad
            target_y = jugador.posY + math.cos( start_angle ) * profundidad

            row = int( target_y / square )
            col = int( ( target_x - start_X ) / square )

            if mapa[row][col] == 1:
                # DIBUJA LA PARED QUE SE TOCA
                # pygame.draw.rect(screen, ( 0, 255, 0 ), (start_X + col * square,
                #                                          row * square + 1,
                #                                          square - 1,
                #                                          square - 1) )
                
                # DIBUJA EL RAYCASTING
                # pygame.draw.line(screen, ( 255, 255, 0 ), (jugador.posX , jugador.posY ), ( target_x, target_y ) )
                
                # CALCULA EL ALTO DE LA PARED 3D
                wall_alto = 21000 / (profundidad + 0.0001)
                
                # DIBUJAR PROYECCION 3D
                pygame.draw.rect(screen, WHITE, (ray * scale,
                                                (screen_Alto / 2) - (wall_alto / 2),
                                                 scale , wall_alto) )
                break

        start_angle += step_angle