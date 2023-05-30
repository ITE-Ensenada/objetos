'''Descripcion: Este archivo contiene la clase AsteroidGenerator, 
                la cual se encarga de generar asteroides'''

import pygame as pg
from game_data.general_settings.settings import ALTO, ASTEROID_INTERVAL
from package_controladores.subpackage_objetos.asteroid import Asteroid

class AsteroidGenerator:
    '''Clase que se encarga de generar asteroides'''

    def __init__(self, game):

        self.game = game # Instancia de la clase Game

        self.asteroid_list = pg.sprite.Group() # Lista de asteroides

        self.last_asteroid = 0 # Tiempo del último asteroide generado


    def generate_asteroid(self, current_time):
        '''Generar asteroides.
        Si el tiempo actual es mayor al tiempo del último asteroide generado'''

        if current_time - self.last_asteroid > ASTEROID_INTERVAL:

            asteroid = Asteroid(self.game) # Instancia de la clase Asteroid

            self.asteroid_list.add(asteroid) # Agregamos el asteroide a la lista de asteroides

            self.last_asteroid = current_time  # Actualizamos el tiempo del último asteroide


    def eliminate_asteroid(self):
        '''Metodo para eliminar los asteroides'''
        for asteroid in self.asteroid_list:
            if asteroid.life <= 0:
                self.game.score_manager.add_points_asteroid()

            if (asteroid.life <= 0 
                or asteroid.rect.top >= ALTO):
                asteroid.kill()


    def update(self):

        '''Actualizar generador de asteroides'''

        current_time = pg.time.get_ticks() # Tiempo actual

        self.generate_asteroid(current_time) # Generar asteroides

        self.eliminate_asteroid()

        self.asteroid_list.update() # Actualizar asteroides
