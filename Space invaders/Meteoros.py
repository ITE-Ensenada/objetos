import pygame
from pygame.locals import*
import random 
from Balas import*

#Clase de los meteoros
class Meteoro1(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load("Meteoro.png"), (70,90))
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]

	def update(self):
		if pygame.sprite.spritecollide(self, Balas_group, False):
			self.kill()

#Herencias de clase de meteoros
class Meteoro2(Meteoro1):
	pass
class Meteoro2(Meteoro1):
	pass
class Meteoro3(Meteoro1):
	pass
class Meteoro4(Meteoro1):
	pass
class Meteoro5(Meteoro1):
	pass
class Meteoro6(Meteoro1):
	pass
class Meteoro7(Meteoro1):
	pass
class Meteoro8(Meteoro1):
	pass
class Meteoro9(Meteoro1):
	pass
class Meteoro10(Meteoro1):
	pass

