from sys import exit
import pygame
import math

# FIN DEL JUEGO
def end_game(event):

    pygame.quit()
    exit()



# DIBUJO DEL MAPA EN 2D
def draw_map2D(event, screen, square, screen_ancho, mapa, jugador):
    
    # INICIO DE DIBUJO EN EL EJE X
    start_X = (screen_ancho / 4)
    
    # ACTUALIZACION DEL BACKGROUND
    pygame.draw.rect( screen, ( 0, 0, 0 ), ( 0, 0, screen_ancho, screen_ancho / 2 ) )
    
    # DIBUJA EL MAPA 2D
    for col in range( len( mapa ) ):
        for row in range( len( mapa ) ):
            
            pygame.draw.rect( screen, ( 255, 255, 255 ) if mapa[col][row] == 1 else ( 100, 100 , 100 ),
                            ( start_X + ( square * row ), ( square * col + 1 ), square - 1, square - 1))
            
    # DIBUJA EL JUGADOR
    pygame.draw.circle(screen, ( 255, 0, 0 ), ( int( jugador.posX ), int( jugador.posY ) ), 8)

    # DIBUJA LA DIRECCION DEL JUGADOR
    pygame.draw.line(screen, ( 0, 255, 0 ), ( jugador.posX, jugador.posY ), ( jugador.posX - math.sin( jugador.angle ) * 30, 
                                                                              jugador.posY + math.cos( jugador.angle ) * 30 ) , 3 )
    
    # DIBUJAR EL FOV
    pygame.draw.line(screen, ( 0, 255, 0 ), (jugador.posX , jugador.posY ), ( jugador.posX - math.sin( jugador.angle - jugador.halfFOV) * 30, 
                                                                              jugador.posY + math.cos( jugador.angle - jugador.halfFOV ) * 30 ) , 3 ) 
    
    pygame.draw.line(screen, ( 0, 255, 0 ), (jugador.posX , jugador.posY ), ( jugador.posX - math.sin( jugador.angle + jugador.halfFOV) * 30, 
                                                                              jugador.posY + math.cos( jugador.angle + jugador.halfFOV ) * 30 ) , 3 ) 

# ALGORITMO DE RAY CASTING 
def ray_cast():
    pass