import pygame, sys
from pygame.locals import *
from personaje.Personaje import *
from personaje.Skills import *
class Rect:
	def __init__(self, rect, x, y):
		self.rect=rect
		self.rect.x=x
		self.rect.y=y		

muve_goku=Rect(goku.img.get_rect(), 10, 10)
kameha=	Rect(kame.img.get_rect(), muve_goku.rect.x+85, muve_goku.rect.y)
muve_vegeta=Rect(vegeta.img.get_rect(), 1000, 600)
destelloF=Rect(destello.img.get_rect(), muve_vegeta.rect.x-85, muve_vegeta.rect.y)