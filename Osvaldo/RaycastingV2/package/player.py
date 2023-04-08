import pygame as pg
from package.settings import *
from math import pi,cos,sin

class Player:   
    def __init__(self, game):
        self.game = game
        self.x, self. y = PLAYER_POSITION
        self.angle = PLAYER_ANGLE
        
    def draw2Dmap(self):
        pg.draw.circle(self.game.screen, 'red', (self.x * tile_square_size, 
                                                 self.y * tile_square_size), 10)
        
        pg.draw.line(self.game.screen, 'green', (self.x * tile_square_size, self.y * tile_square_size),
                                                (self.x * tile_square_size + cos(self.angle) * 100, 
                                                (self.y * tile_square_size + sin(self.angle) * 100)), 2)
        
    def movement(self):
        # DELTA X, Y, SON EL INCREMENTO DESDE LA POSICION INICIAL DEL JUGADOR
        dx, dy = 0, 0
        self.speed = PLAYER_SPEED * self.game.delta_time
        speed_cos = self.speed * cos(self.angle)
        speed_sin = self.speed * sin(self.angle)
        
        keys = pg.key.get_pressed()
        
        # MOVEMENT
        # if self.game.mapa.map[int(self.y)][int(self.x)] == 0:
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
                
        
        # ACTUALIZACION DEL MOVIMIENTO
        # self.x += dx
        # self.y += dy
        
        self.check_collision(dx, dy)

    def check_collision(self, dx, dy):
        if self.game.mapa.map[int(self.y + dy)][int(self.x)] != 1:
            self.y += dy
        if self.game.mapa.map[int(self.y)][int(self.x + dx)] != 1:
            self.x += dx
    
    def mouse_control(self):
        pg.mouse.set_visible(False)
        mx, my = pg.mouse.get_pos()
        if mx < LEFT_MOUSE_LIMIT or mx > RIGHT_MOUSE_LIMIT:
            pg.mouse.set_pos( ((ANCHO / 2), (ALTO / 2)) )
        self.mx_rel = pg.mouse.get_rel()[0]
        self.mx_rel = max(-MOUSE_REL_LIMIT, min(MOUSE_REL_LIMIT, self.mx_rel))
        self.angle += self.mx_rel * MOUSE_SENSIBILITY * self.game.delta_time
    
    def update(self):
        self.movement()
        self.mouse_control()
    
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def pos_map(self):
        return int(self.x), int(self.y)