from sys import exit
import pygame

def event_loop(event):
    if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()


def draw_map2D(event, screen,screen_alto, screen_ancho, mapa):
    square = ( (screen_ancho) * (1/2) )/ 8
    start_X =(screen_ancho / 4)
    
    for col in range( len( mapa ) ):
        for row in range( len( mapa ) ):
            if mapa[col][row] != 0:
                pygame.draw.rect(screen, (255, 255, 255), ( start_X + (square * (row)) , (square * (col)), square, square))