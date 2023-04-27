'''Descripción: Este archivo contiene la clase Level'''

import pygame
from sprites import Tile
from confi import TILE_SIZE, ANCHO_PANTALLA
from jugador import Player

class Level:
    '''Clase para crear el nivel'''

    def __init__(self,level_data,surface):

        #level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self,layout):
        '''Metodo para crear el nivel'''

        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                pos_x = col_index * TILE_SIZE
                pos_y = row_index * TILE_SIZE

                if cell == 'X':
                    tile = Tile((pos_x,pos_y),TILE_SIZE)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((pos_x,pos_y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        '''Metodo para mover el nivel horizontalmente'''

        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < ANCHO_PANTALLA/4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > ANCHO_PANTALLA -(ANCHO_PANTALLA/4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        '''Metodo para detectar colisiones horizontales'''

        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        '''Metodo para detectar colisiones verticales'''

        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        '''Metodo para correr el nivel'''

        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        #player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        