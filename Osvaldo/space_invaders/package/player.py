'''Descripcion: Este archivo contiene la clase Game, la cual se encarga de manejar el juego'''

import pygame as pg
from package.settings import PLAYER_SPEED, PLAYER_LIFE, X, Y, ANCHO, ALTO

class Player(pg.sprite.Sprite):
    '''Clase que representa al jugador'''

    def __init__(self, game):

        super().__init__() # Inicializar clase padre

        self.game = game # Instancia de la clase Game

        self.pos_x, self.pos_y = X, Y # Posicion del jugador

        self.sprite0, self.sprite1 = self.create_sprites() # Sprites del jugador

        self.current_sprite = self.sprite0 # Sprite actual

        self.rect = self.collition_rect() # Rectangulo para deteccion de colisiones

        self.life = PLAYER_LIFE # Vidas del jugador

    def collition_rect(self):
        '''Metodo que se encarga de crear el rectangulo de colisiones'''

        rect = self.current_sprite.get_rect() # Rectangulo para deteccion de colisiones

        rect.x = self.pos_x # Actualizar la posicion en x del rectangulo de colisiones
        rect.y = self.pos_y # Actualizar la posicion en y del rectangulo de colisiones

        return rect

    def lost_life(self):
        '''Metodo que se encarga de restar una vida al jugador'''

        self.life -= 1 # Restar una vida al jugador

        if self.life == 0:

            self.game.close_game() # Cerrar el juego


    def create_sprites(self):
        '''Metodo que se encarga de crear los sprites del jugador'''

        # Sprite0 del jugador
        sprite0 = pg.image.load('Assets/Player/Nave0.png').convert_alpha()
        sprite0 = pg.transform.scale(sprite0, (48, 48)) # Scale del sprite

        # Sprite1 del jugador
        sprite1 = pg.image.load('Assets/Player/Nave1.png').convert_alpha()
        sprite1 = pg.transform.scale(sprite1, (48, 48)) # Scale del sprite

        return sprite0, sprite1 # Retornar sprites

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

        new_x = self.pos_x + increment_x # Nueva posicion en x

        new_y = self.pos_y + increment_y # Nueva posicion en y

        if -5 < new_x < ANCHO - 40:

            self.rect.x = new_x # Actualizar posicion en x del rectangulo de colisiones

            self.pos_x = new_x # Actualizar posicion en x

        if 0 < new_y < ALTO - 40:

            self.rect.y = new_y # Actualizar posicion en y del rectangulo de colisiones

            self.pos_y = new_y # Actualizar posicion en y


    def update(self):
        '''Metodo que se encarga de actualizar al jugador'''

        self.draw_player() # Dibujar jugador

        self.movement() # Mover jugador


    def draw_player(self):
        ''' Metodo que se encarga de dibujar al jugador'''

        self.game.screen.blit(self.current_sprite, (self.pos_x, self.pos_y)) # Dibujar jugador

        self.rect = self.collition_rect() # Actualizar rectangulo de colisiones

        pg.draw.rect(self.game.screen, 'red', self.rect, 2) # Dibujar rectangulo de colisiones

    def change_sprite(self):
        '''Metodo que se encarga de cambiar el sprite del jugador'''

        if self.current_sprite == self.sprite0:
            self.current_sprite = self.sprite1


    def reset_sprite(self):
        '''Metodo que se encarga de resetear el sprite del jugador'''

        self.current_sprite = self.sprite0


    @property
    def get_pos(self):
        '''Metodo que se encarga de obtener la posicion del jugador'''

        return self.pos_x, self.pos_y
