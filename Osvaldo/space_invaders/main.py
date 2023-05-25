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
from game_data.general_settings.settings import FPS # Importar variables de configuración
from game_data.save_data.scores import ScoresManager
from package_controladores import ( # Importar clases del juego
    Player,
    Npc,
    AsteroidGenerator,
    RenderItemsManager,
    CollisionManager,
    Screen)


class Game(Screen):
    '''Clase principal del juego'''

    def __init__(self):
        pygame.init() # Inicializar pygame

        super().__init__() # Inicializar clase padre

        self.event = None # Variable para controlar eventos

        self.player = Player(self) # Crear jugador

        self.asteroid_generator = AsteroidGenerator(self) # Crear generador de asteroides

        self.score_manager = ScoresManager(self)

        self.collision_manager = CollisionManager(self) # Crear colisiones

        self.render_items_manager = RenderItemsManager(self) # Crear renderizador de fondo


    def update_menu_game(self):
        '''Actualizar menú'''

        self.draw_menu() # Dibujar menú

        pygame.display.update() # Actualizar pantalla


    def update_running_game(self):
        '''Actualizar juego'''

        self.draw_background() # Dibujar fondo

        self.player.update() # Actualizar jugador

        self.asteroid_generator.update_asteroids() # Actualizar generador de asteroides

        self.collision_manager.update() # Actualizar colisiones

        self.render_items_manager.update() # Actualizar fondo

        pygame.display.update() # Actualizar pantalla

    def update_game_over_menu(self):
        '''Actualizar pantalla de game over'''

        self.draw_game_over()

        pygame.display.update() # Actualizar pantalla


    def run(self):
        '''Bucle principal del juego'''

        while True: # Bucle principal
            self.events() # Actualizar eventos
            if not self.running and self.player.life > 0:
                self.update_menu_game() # Actualizar menú
            elif self.running and self.player.life > 0:
                self.update_running_game() # Actualizar juego
            elif not self.running and self.player.life <= 0:
                self.update_game_over_menu() # Actualizar pantalla de game over

            self.delta_time = self.clock.tick(FPS) # Actualizar tiempo


    def events(self):
        '''Actualizar eventos'''
        if self.player.life <= 0: # Si el jugador se queda sin vida
            self.running = False # Dejar de correr el juego

        for self.event in pygame.event.get(): # Recorrer todos los eventos
            self.start_game()
            self.game_over() # Actualizar eventos de salida
            self.reset_player_sprite() # Resetear sprite del jugador
            self.player_shot() # Actualizar eventos de disparo


    def start_game(self):
        '''Método para iniciar el juego'''

        if (not self.running
            and self.event.type == KEYDOWN
            and self.event.key == K_SPACE
            and self.player.life > 0):

            self.running = True


    def close_game(self):
        '''Cerrar juego'''

        self.score_manager.save_high_scores()
        pygame.quit()
        sys.exit()


    def game_over(self):
        '''Metodo para salir del juego'''
        if (self.event.type == QUIT
            or (self.event.type == KEYDOWN
                and self.event.key == K_ESCAPE)): # Salir del juego

            self.close_game() # Cerrar juego

        if (not self.running
            and self.event.type == KEYDOWN
            and self.event.key == K_SPACE
            and self.player.life <= 0):

            self.close_game()

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
