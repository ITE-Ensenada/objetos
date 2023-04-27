import pygame
from pygame.locals import*

Balas_group = pygame.sprite.Group()
class Balas(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load("Bala.png"), (50,20))
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]

	def update(self):
		self.rect.x += 5
		if self.rect.bottom < 0:
			self.kill()
		if pygame.sprite.spritecollide(self, Naves_group2, False):
			self.kill()
			Nave2.vida_restante -= 1

class Balas2(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load("Bala2.png"), (50,20))
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]

	def update(self):
		self.rect.x -= 5
		if self.rect.bottom < 0:
			self.kill()
		if pygame.sprite.spritecollide(self, Naves_group, False):
			self.kill()
			Nave.vida_restante -= 1
		if pygame.sprite.spritecollide(self, Meteoro_group, True):
			self.kill()