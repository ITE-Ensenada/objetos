import pygame as pg
from Package.settings import *
from Package.asteroid import *

class AsteroidGenerator():
    def __init__(self, game):
        self.game = game
        self.asteroid_list = pg.sprite.Group()
        self.last_asteroid = 0
        
    def generateAsteroid(self, current_time):
        if current_time - self.last_asteroid > ASTEROID_INTERVAL:
            asteroid = Asteroid(self.game)
            self.asteroid_list.add(asteroid)
            self.last_asteroid = current_time  # Actualizamos el tiempo del último asteroide generado
        
    def update(self):
        current_time = pg.time.get_ticks()
        self.generateAsteroid(current_time)
        
        # Eliminar asteroides que hayan salido completamente por la parte de abajo de la pantalla
        for asteroid in self.asteroid_list:
            if asteroid.rect.bottom > ALTO/2:
                asteroid.kill()
                
        # Actualizar todos los asteroides que aún están en la pantalla
        self.asteroid_list.update()