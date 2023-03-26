import pygame, sys
from pygame.locals import *

class Personaje:
	especie="Sayayin"
	def __init__(self, img, name, age, altura, vida, inteligencia, carisma, velocidad, rango, fuerza):
		self.img = img
		self.nombre=name
		self.edad=age
		self.piel='blanca'
		self.altura=altura
		self.vida=vida
		self.inteligencia=inteligencia
		self.carisma=carisma
		self.velocidad=velocidad
		self.rango=rango
		self.fuerza=fuerza

goku = Personaje(pygame.image.load('imagenes/goku.png'), 'Kakaroto', 35, 176, 687, 89, 'Mucha', 24, 90, 280)
vegeta = Personaje(pygame.image.load('imagenes/Vegeta.png'), 'Vegeta', 33, 173, 580, 120, 'Poca', 28, 70, 300)

def size(im):
	tam=pygame.transform.scale(im, (100, 200))
	return tam

goku.img=size(goku.img)
vegeta.img=size(vegeta.img)

