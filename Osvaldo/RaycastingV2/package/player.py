import pygame as pg
from package.settings import *
from math import pi,cos,sin

class Player:   
    def __init__(self, game):
        self.game = game
        self.x, self. y = PlayerPos
        self.angle = PlayerAngle
        self.speed = PlayerSpeed
        self.speedRotation = PlayerSpeedRotation
        
    def draw2Dmap(self):
        pg.draw.circle(self.game.screen, 'red', (self.x * tile_square_size, 
                                                 self.y * tile_square_size), 10)
        
        pg.draw.line(self.game.screen, 'green', (self.x * tile_square_size, self.y * tile_square_size),
                                                (self.x * tile_square_size + cos(self.angle) * 100, 
                                                (self.y * tile_square_size + sin(self.angle) * 100)), 2)
        
    def movement(self):
        keys = pg.key.get_pressed()
        # DELTA X, Y, SON EL INCREMENTO DESDE LA POSICION INICIAL DEL JUGADOR
        dx, dy = 0, 0
        speed = PlayerSpeed * self.game.delta_time
        speed_cos = speed * cos(self.angle)
        speed_sin = speed * sin(self.angle)
        
        self.mouse_controll()
        
        # MOVEMENT
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
        
        # ROTACION CON TECLAS
        if keys[pg.K_LEFT]:
            self.angle += -(PlayerSpeedRotation * self.game.delta_time)
        if keys[pg.K_RIGHT]:
            self.angle += (PlayerSpeedRotation * self.game.delta_time)

        self.x += dx
        self.y += dy
        
    def mouse_controll(self):
        mx, my = pg.mouse.get_pos()
        if mx < LEFT_MOUSE_LIMIT or mx > RIGHT_MOUSE_LIMIT:
            pg.mouse.set_pos( ((ancho / 2), (alto / 2)) )
        self.mx_rel = pg.mouse.get_rel()
        print(self.mx_rel)
        
        
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def pos_map(self):
        return int(self.x), int(self.y)