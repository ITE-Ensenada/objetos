'''Descripcion: Este archivo contiene la clase del jugador'''

import pygame

class Player(pygame.sprite.Sprite):
    '''Clase para crear al jugador'''

    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        #player movement
        self.speed = 8
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = 0.8
        self.jump_speed = -16

    def get_input(self):
        '''Metodo para obtener la entrada del usuario'''

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_w]:
            self.jump()

    def apply_gravity(self):
        '''Metodo para aplicar gravedad al jugador'''

        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        '''Metodo para hacer saltar al jugador'''

        self.direction.y = self.jump_speed

    def update(self):
        '''Metodo para actualizar al jugador'''

        self.get_input()
