'''Descripcion: Este archivo es utilizado crear la ventana del juego y el reloj del juego'''

import pygame
from game_data.general_settings.settings import RESOLUTION, FLAGS, FPS # Importar variables de configuración

class Screen:
    '''Clase que representa la pantalla del juego, 
        y se encarga de crear la ventana y el reloj del juego'''

    def __init__(self):

        self.screen = pygame.display.set_mode(RESOLUTION, FLAGS) # Crear ventana

        self.clock = pygame.time.Clock() # Crear reloj

        self.delta_time = 1 # Variable para el delta time

        self.running = False # Variable para controlar el bucle principal

        self.background = self.create_background_game() # Crear fondo


    def create_background_game(self):
        '''Metodo que se encarga de crear el fondo del juego'''

        background = pygame.image.load('Assets/Stars_background.jpg').convert_alpha()
        background = pygame.transform.scale(background, RESOLUTION)

        return background


    def draw_background(self):
            '''Dibujar fondo'''''
    
            self.screen.blit(self.background, (0, 0))
    
    def draw_menu(self):
        font = pygame.font.Font(None, 36)
        title_text = font.render("Juego Espacial", True, (255, 255, 255))
        start_text = font.render("Presiona ESPACIO para comenzar", True, (255, 255, 255))

        self.screen.blit(title_text, (300, 200))
        self.screen.blit(start_text, (250, 300))
        