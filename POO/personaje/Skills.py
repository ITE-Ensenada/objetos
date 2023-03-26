import pygame, sys
from pygame.locals import *
from personaje.rect import *
class Kameha (pygame.sprite.Sprite):	
	def __init__ (self):
		super().__init__()
		self.image=pygame.image.load('imagenes/Kamehameha+.png').convert_alpha()
		self.tamano=pygame.transform.scale(self.image, (10, 40))
		self.dano=32
		self.color='blue'
		self.rapidez=26
		self.rect=self.tamano.get_rect()
		self.rect.x=muve_goku.rect.x+70
		self.rect.y=muve_goku.rect.y

	def update(self):
		self.rect.x+=self.rapidez

class Destello (pygame.sprite.Sprite):	
	def __init__ (self):
		super().__init__()
		self.image=pygame.image.load('imagenes/destello.png')
		self.tamano=pygame.transform.scale(self.image, (30, 40))
		self.dano=35
		self.color='Yellow'
		self.rapidez=38
		self.rect=self.tamano.get_rect()
		self.rect.x=muve_vegeta.rect.x-85
		self.rect.y=muve_vegeta.rect.y
	def update(self):
		self.rect.x-=self.rapidez


def tamano(im):
	tam=pygame.transform.scale(im, (100, 1000))
	return tam
