import pygame

# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie
width = 800 
height = 600
surface = pygame.display.set_mode((width, height))
background_color = (255,23,100)
surface.fill(background_color)
# Establecer el color de un píxel en la posición (100, 200) a rojo (255, 0, 0)
color = (255,120, 10)
def linea_h():
    for i in range(0,100):
        surface.set_at((100 + i, 200), color)
    ## Mostrar la superficie en la pantalla
    pygame.display.flip()

def linea_v():
    for i in range(0,100):
        surface.set_at((100, 200 + i), color)
    pygame.display.flip()

# Esperar a que el usuario cierre la ventana
while True:
    cmd = input("cmd> ")
    if cmd == "exit":
        pygame.quit()
    if cmd == "linea -h":
        linea_h()
    if cmd == "linea -v":
        linea_v()
