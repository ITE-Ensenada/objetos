'''Descripcion: Archivo principal del juego'''

import sys # Importar librería para salir del programa
import pygame # Importar librería pygame
from pygame.locals import ( # Importar constantes de pygame
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    K_a,
    K_d,
    K_w,
    K_s,
    QUIT)
from package.settings import RESOLUTION, FLAGS, FPS # Importar variables de configuración
from package.asteroid_generator import AsteroidGenerator # Importar generador de asteroides
from package.render_background import RenderBackground # Importar renderizador de fondo
from package.player import Player # Importar jugador
from package.collision import Collision # Importar colisiones

class Game:
    '''Clase principal del juego'''
    def __init__(self):
        pygame.init() # Inicializar pygame

        self.event = None # Variable para controlar eventos

        self.screen = pygame.display.set_mode(RESOLUTION, FLAGS) # Crear ventana

        self.clock = pygame.time.Clock() # Crear reloj

        self.delta_time = 1 # Variable para controlar el tiempo

        self.player = Player(self) # Crear jugador

        self.asteroid_generator = AsteroidGenerator(self) # Crear generador de asteroides

        self.render_background = RenderBackground(self) # Crear renderizador de fondo

        self.collision = Collision(self)


    def update(self):
        '''Actualizar juego'''

        self.screen.fill('black') # Limpiar pantalla

        self.render_background.update() # Actualizar fondo

        self.player.update() # Actualizar jugador

        self.asteroid_generator.update() # Actualizar generador de asteroides

        self.collision.update() # Actualizar colisiones

        pygame.display.update() # Actualizar pantalla

        self.delta_time = self.clock.tick(FPS) # Actualizar tiempo

    def run(self):
        '''Bucle principal del juego'''

        while True: # Bucle principal
            self.events() # Actualizar eventos
            self.update() # Actualizar juego

    def events(self):
        '''Actualizar eventos'''

        for self.event in pygame.event.get(): # Recorrer todos los eventos
            self.game_over() # Actualizar eventos de salida
            self.reset_player_sprite() # Resetear sprite del jugador

    def close_game(self):
        '''Cerrar juego'''

        pygame.quit()
        sys.exit()
    

    def game_over(self):
        '''Actualizar eventos de salida'''

        if (self.event.type == QUIT
            or (self.event.type == KEYDOWN
                and self.event.key == K_ESCAPE)): # Salir del juego

            self.close_game() # Cerrar juego

    def reset_player_sprite(self):
        '''Resetear sprite del jugador'''

        if (self.event.type == KEYUP
            and (self.event.key in (K_a, K_d, K_w, K_s))): # Resetear sprite del jugador

            self.player.reset_sprite() # Resetear sprite del jugador




if __name__ == '__main__':
    game = Game() # Crear juego
    game.run() # Correr juego
    