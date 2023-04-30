import pygame, sys, time, random
from pygame.locals import *

#COSO PARA DELIMITAR LAS DIMENSIONES DE LA PANTALLA
pygame.init()
width = 500
height = 700
play_surface = pygame.display.set_mode((width, height))
fps = pygame.time.Clock()

#FUNCION PARA GENERAR DE MANERA ALEATORIA LOS TUBOS
def pipe_random_height():
    pipe_h = [random.randint(200, (height/2)-20), random.randint((height/2)+20, height-200)]
    return pipe_h

#AQUI SE VAN A DEFINIR TODAS LA VARIABLES PARA PODER JUGAR, GRAVEDAD, VELOCIDAD, ETC.
def main():
    score = 0
    player_pos = [100, 350]
    gravity = 1
    speed = 0
    jump = -30

    pipe_pos = 700
    pipe_widht = 50
    pipe_height = pipe_random_height()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    speed += jump


        speed += gravity
        speed *= 0.95
        player_pos[1] += speed
        
        #GENERACION DE TUBOS CUANDO PASAS UNO
        if pipe_pos >= -20:
            pipe_pos -= 10
        else:
            pipe_pos = 700
            pipe_height = pipe_random_height()
            score += 1

        #PANTALLA
        play_surface.fill((0,0,0))

        #AQUI SE VA ESTAR DIBUJANDO EL JUGADOR (DEBERIA SER UN PAJARO PERO LUEGO LO CAMBIO XD)
        pygame.draw.circle(play_surface, (255, 160, 60), (int(player_pos[0]), int(player_pos[1])), 20)

        #ESTA COSA ES PARA DIBUJAR LOS "TUBOS "XD
        pygame.draw.rect(play_surface, (200,200,200), [pipe_pos, 0, pipe_widht, pipe_height[0]], 0)
        pygame.draw.rect(play_surface, (200,200,200), [pipe_pos, pipe_height[1], pipe_widht, 500], 0)

        #COSO PARA LAS COLISIONES
        if player_pos[1] <= pipe_height[0] or player_pos[1] >= pipe_height[1]:
            if player_pos[0] in list(range(pipe_pos, pipe_pos+pipe_widht)):
                print(f"Game Over. Score {score})")

        if player_pos[1] >= height:
            player_pos[1] = height
            speed = 0
        elif player_pos[1] <= 0:
            player_pos[1] = 0
            speed = 0

        pygame.display.flip()
        fps.tick(30)


main()
pygame.quit()