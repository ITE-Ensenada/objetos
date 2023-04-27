'''Descripcion: Este archivo contiene la clase Game, la cual se encarga de manejar el juego'''

import pygame as pg
from package.settings import PLAYER_SPEED, PLAYER_LIFE, X, Y, ANCHO, ALTO
from package.subpackage.esqueleto import Esqueleto

class Player(Esqueleto):
    '''Clase que representa al jugador'''

    def __init__(self, game):

        super().__init__(
            game,
            X,
            Y,
            self.create_sprites(),
            PLAYER_LIFE)

        self.current_sprite = self.sprites[0] # Sprite actual

        self.rect = self.collition_rect() # Rectangulo para deteccion de colisiones

    def collition_rect(self):
        '''Metodo que se encarga de crear el rectangulo de colisiones'''

        rect = self.current_sprite.get_rect() # Rectangulo para deteccion de colisiones

        rect.x = self.pos[0] # Actualizar la posicion en x del rectangulo de colisiones
        rect.y = self.pos[1] # Actualizar la posicion en y del rectangulo de colisiones

        return rect


    def create_sprites(self):
        '''Metodo que se encarga de crear los sprites del jugador'''

        sprites = [
            pg.image.load('Assets/Player/Nave0.png').convert_alpha(),
            pg.image.load('Assets/Player/Nave1.png').convert_alpha()
        ]

        for index,sprite in enumerate(sprites):
            sprites[index] = pg.transform.scale(sprite, (48, 48)) # Scale del sprite

        return sprites # Retornar sprites


    def movement(self):
        '''Metodo que se encarga de mover al jugador'''

        increment_x, increment_y = 0, 0 # Incremento de la posicion del jugador

        keys = pg.key.get_pressed() # Obtener teclas presionadas

        if keys[pg.K_a]:

            self.change_sprite() # Cambiar sprite

            increment_x -= PLAYER_SPEED * self.game.delta_time # Incremento en x

        if keys[pg.K_d]:

            self.change_sprite() # Cambiar sprite

            increment_x += PLAYER_SPEED * self.game.delta_time # Incremento en x

        if keys[pg.K_w]:

            self.change_sprite() # Cambiar sprite

            increment_y -= PLAYER_SPEED * self.game.delta_time # Incremento en y

        if keys[pg.K_s]:

            self.change_sprite() # Cambiar sprite

            increment_y += PLAYER_SPEED * self.game.delta_time # Incremento en x

        self.check_walls(increment_x, increment_y) # Verificar colisiones con las paredes


    def check_walls(self, increment_x, increment_y):
        '''Metodo que se encarga de verificar colisiones con las paredes'''

        new_position = [ # Nueva posicion del jugador
            self.pos[0] + increment_x,
            self.pos[1] + increment_y
            ]

        if 0 <= new_position[0] <= ANCHO - 48:

            self.rect.x = new_position[0] # Actualizar posicion en x del rectangulo de colisiones

            self._pos_x = new_position[0] # Actualizar posicion en x

        if 0 <= new_position[1] <= ALTO - 48:

            self.rect.y = new_position[1] # Actualizar posicion en y del rectangulo de colisiones

            self._pos_y = new_position[1] # Actualizar posicion en y


    def update(self):
        '''Metodo que se encarga de actualizar al jugador'''

        self.draw_player() # Dibujar jugador

        self.movement() # Mover jugador


    def draw_player(self):
        ''' Metodo que se encarga de dibujar al jugador'''

        self.game.screen.blit(self.current_sprite, (self.pos)) # Dibujar jugador

        self.rect = self.collition_rect() # Actualizar rectangulo de colisiones

        pg.draw.rect(self.game.screen, 'red', self.rect, 2) # Dibujar rectangulo de colisiones


    def change_sprite(self):
        '''Metodo que se encarga de cambiar el sprite del jugador'''

        if self.current_sprite == self.sprites[0]:
            self.current_sprite = self.sprites[1]


    def reset_sprite(self):
        '''Metodo que se encarga de resetear el sprite del jugador'''

        self.current_sprite = self.sprites[0]
