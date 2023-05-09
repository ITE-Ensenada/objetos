'''Descripcion: Archivo principal del juego'''

import sys # Importar librería para salir del programa
import pygame # Importar librería pygame
from pygame.locals import ( # Importar constantes de pygame
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    KEYUP,
    K_a,
    K_d,
    K_w,
    K_s,
    QUIT)
from package.settings import FPS # Importar variables de configuración
from package import ( # Importar clases del juego
    Player,
    AsteroidGenerator,
    RenderLife,
    Collision,
    Screen)

class Game(Screen):
    '''Clase principal del juego'''
    def __init__(self):
        pygame.init() # Inicializar pygame

        super().__init__() # Inicializar clase padre

        self.event = None # Variable para controlar eventos

        self.player = Player(self) # Crear jugador

        self.asteroid_generator = AsteroidGenerator(self) # Crear generador de asteroides

        self.render_life = RenderLife(self) # Crear renderizador de fondo

        self.collision = Collision(self) # Crear colisiones


    def update(self):
        '''Actualizar juego'''

        # self.screen.fill('black') # Limpiar pantalla

        self.draw_background() # Dibujar fondo

        self.render_life.update() # Actualizar fondo

        self.player.update() # Actualizar jugador

        self.asteroid_generator.update() # Actualizar generador de asteroides

        self.collision.update() # Actualizar colisiones

        pygame.display.update() # Actualizar pantalla

        self.delta_time = self.clock.tick(FPS) # Actualizar tiempo

    def run(self):
        '''Bucle principal delA juego'''

        while True: # Bucle principal
            self.events() # Actualizar eventos
            self.update() # Actualizar juego

    def events(self):
        '''Actualizar eventos'''

        for self.event in pygame.event.get(): # Recorrer todos los eventos
            self.game_over() # Actualizar eventos de salida
            self.reset_player_sprite() # Resetear sprite del jugador
            self.player_shot() # Actualizar eventos de disparo


    def close_game(self):
        '''Cerrar juego'''

        pygame.quit()
        sys.exit()


    def game_over(self):
        '''Actualizar eventos de salida'''
        if self.player.life <= 0: # Si el jugador se queda sin vida
            self.close_game() # Cerrar juego

        if (self.event.type == QUIT
            or (self.event.type == KEYDOWN
                and self.event.key == K_ESCAPE)): # Salir del juego

            self.close_game() # Cerrar juego

    def reset_player_sprite(self):
        '''Resetear sprite del jugador'''

        if (self.event.type == KEYUP
            and (self.event.key in (K_a, K_d, K_w, K_s))): # Resetear sprite del jugador

            self.player.reset_sprite() # Resetear sprite del jugador


    def player_shot(self):
        '''Actualizar eventos de disparo'''

        if (self.event.type == KEYDOWN
            and self.event.key == K_SPACE):

            self.player.shot() # Disparar


if __name__ == '__main__':
    game = Game() # Crear juego
    game.run() # Correr juego
