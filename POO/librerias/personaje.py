'''Modulo de los personajes'''
import pygame

class Personaje:
    def __init__(self, img, name, vida):
        self.img=img
        self.nombre=name
        self.vida=vida

    def size(self):
        self.img=pygame.transform.scale(self.img, (100, 200))

class Saya(Personaje):
    '''Para los sayayines'''
    def __init__(self, img, name, vida, velocidad, rango, fuerza):
        super().__init__(img, name, vida)
        self.velocidad=velocidad
        self.rango=rango
        self.fuerza=fuerza

goku=Saya(pygame.image.load('imagenes/goku.png'), 'Goku', 687, 24, 90, 280)
vegeta = Saya(pygame.image.load('imagenes/Vegeta.png'), 'Vegeta', 580, 28, 70, 300)
