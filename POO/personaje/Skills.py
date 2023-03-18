import pygame, sys
from pygame.locals import *

class Skills:
	def __init__(self, img, nome, dano, color, rapidez):
		self.img = img
		self.skill=nome
		self.dano=dano
		self.color=color
		self.rapidez=rapidez

kame = Skills(pygame.image.load('imagenes/Kamehameha+.png'), 'Kamehameha', 130, 'blue', 1)
destello = Skills(pygame.image.load('imagenes/destello.png'),'Destello final', 140, 'Yellow', 52)

def tamano(im):
	tam=pygame.transform.scale(im, (100, 200))
	return tam

kame.img=tamano(kame.img)
destello.img=tamano(destello.img)
