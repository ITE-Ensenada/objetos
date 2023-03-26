import pygame, sys
from pygame.locals import *
from personaje.Personaje import *
class Rect:
	def __init__(self, rect, x, y):
		self.rect=rect
		self.rect.x=x
		self.rect.y=y		
	def update(self, vel):
		self.rect.x-= vel
		return rect
muve_goku=Rect(goku.img.get_rect(), 10, 10)
muve_vegeta=Rect(vegeta.img.get_rect(), 1000, 600)
