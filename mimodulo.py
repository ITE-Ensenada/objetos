import pygame, random

class Personaje:
	especie = "Puca"
	def __init__(self,name,age,vida,nivel,caminar):
		self.nombre = name
		self.edad = age
		self.vida = 10
		self.nivel = 0
		self.caminar = 3

class Personaje:
	especie = "Puca"
	def __init__(vida,fuerza,nivel,caminar):
		self.vida = 10
		self.nivel = 0
		self.caminar = 3

class Puca(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('IMAGENES/puca.png').convert_alpha()
		pygame.display.set_icon(self.image)
		self.rect = self.image.get_rect()
		self.rect.centerx = width//2
		self.rect.centery = height-50
		self.velocidad_x = 0
		self.vida = 100