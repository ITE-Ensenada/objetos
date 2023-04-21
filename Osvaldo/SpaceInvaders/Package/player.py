import pygame as pg
from Package.settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.pos = self.x, self.y = X, Y
        
        # SPRITES DEL JUGADOR
        self.sprite0 = pg.image.load('Assets/Player/Nave0.png').convert_alpha()
        self.sprite0 = pg.transform.scale(self.sprite0, (48, 48))
        self.sprite1 = pg.image.load('Assets/Player/Nave1.png').convert_alpha()
        self.sprite1 = pg.transform.scale(self.sprite1, (48, 48)) 
        self.current_sprite = self.sprite0 # SPRITE ACTUAL
        self.rect = self.current_sprite.get_rect() # RECTANGULO PARA DETECCION DE COLISIONES
        
    def movement(self):
        dx, dy = 0, 0
        keys = pg.key.get_pressed()
        
        if keys[pg.K_a]:
            self.change_sprite()
            dx -= PLAYER_SPEED * self.game.delta_time
        if keys[pg.K_d]:
            self.change_sprite()
            dx += PLAYER_SPEED * self.game.delta_time
        if keys[pg.K_w]:
            self.change_sprite()
            dy -= PLAYER_SPEED * self.game.delta_time
        if keys[pg.K_s]:
            self.change_sprite()
            dy += PLAYER_SPEED * self.game.delta_time
        
        self.check_walls(dx, dy)
    
    def check_walls(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if (new_x > -5) and new_x < (ANCHO - 40):
            self.x = new_x
        if new_y < ( ALTO  - 40 ) and new_y > 0:
            self.y = new_y
    
    def update(self):
        self.movement()
        self.draw_player()
    
    def draw_player(self):
        # DIBUJA LA NAVE
        self.game.screen.blit(self.current_sprite, (self.x, self.y))
        # ACTULIZAR EL RECTANGULO DE COLISION DE LA NAVE
        self.rect = self.current_sprite.get_rect()
        
    def change_sprite(self):
        # CAMBIA EL SPRITE DE LA NAVE
        if self.current_sprite == self.sprite0:
            self.current_sprite = self.sprite1
            
    def reset_sprite(self):
        # REINICIA EL SPRITE AL DEFAUTL
        self.current_sprite = self.sprite0
        
    @property
    def get_pos(self):
        return self.pos