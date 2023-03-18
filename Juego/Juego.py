import pygame, sys

from pygame.locals import *

pygame.init()

FPS = 30

fpsClock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((1022,479), 0, 32)

pygame.display.set_caption('Animation')

#Carga de imagenes
sanicImg = pygame.image.load('sanic.png')
sanicImg = pygame.transform.scale(sanicImg, (100, 200))
Nivel = pygame.image.load("nivel.jpg").convert()

#Clase de personaje y ataques
class sanic:
	def especificaciones(self,hp,atbasico,velocidad):
		self.hp=hp
		self.atbasico=atbasico
		self.velocidad=velocidad

class golpe:
	def __init__(self,elemento,mejora,ataque):
		self.elemento=elemento
		self.mejora=mejora
		self.ataque=ataque

class patada:
	def __init__(self,elemento,ataque,mejora):
		self.elemento=elemento
		self.mejora=mejora
		self.ataque=ataque

class girar:
	def __init__(self,velocidad,salto):
		self.velocidad=velocidad
		self.salto=salto
     
#Cordenadas de personaje 
sanicX= 150
sanicY= 200
MovEnX=0

#Movimiento de personaje
while True: 

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				MovEnX= -5
			if event.key == pygame.K_d:
				MovEnX = 10

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				MovEnX = 0
			if event.key == pygame.K_d:
				MovEnX = 0
	
	sanicX += MovEnX	
	SCREEN.blit(Nivel,SCREEN.blit(Nivel, [0, 0]))
	SCREEN.blit(sanicImg, (sanicX, sanicY))

	pygame.display.update()
	fpsClock.tick(FPS)