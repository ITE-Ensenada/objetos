import pygame, sys, time
from pygame.locals import *
from personaje.Personaje import *
from personaje.Skills import *
from personaje.rect import *

pygame.init()

FPS = 30 # frames per second setting

fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
if __name__ == '__main__': 
	print ('Jugadores disponibles: Goku		vegeta \n El jugador 1 sera Goku y el jugador 2 sera Vegeta') 


# set up the window
SCREEN = pygame.display.set_mode((WINDOW_WIDTH ,WINDOW_HEIGHT))

pygame.display.set_caption('Animation')

fondo = pygame.image.load('imagenes/fondo.jpg')
fondo = pygame.transform.scale(fondo, (1200, 800))
kamelista = pygame.sprite.Group()
deslista = pygame.sprite.Group()
ponch = False

while True: # the main game loop

	SCREEN.blit(fondo, (0,0))
	SCREEN.blit(goku.img, (muve_goku.rect))
	SCREEN.blit(vegeta.img, (muve_vegeta.rect))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key==K_w:
				muve_goku.rect.y-=goku.velocidad
			if event.key==K_s:
				muve_goku.rect.y+=goku.velocidad
			if event.key==K_d:
				muve_goku.rect.x+=goku.velocidad
			if event.key==K_a:
				muve_goku.rect.x-=goku.velocidad
			if event.key==K_r:
				goku.img = pygame.image.load('imagenes/goku ataque.png')
				goku.img=size(goku.img)
				kameha=Kameha()
				kameha.image=size(kameha.image)
				kamelista.add(kameha)
				ponch = True

			if event.key==K_UP:
				muve_vegeta.rect.y-=vegeta.velocidad
			if event.key==K_DOWN:
				muve_vegeta.rect.y+=vegeta.velocidad
			if event.key==K_RIGHT:
				muve_vegeta.rect.x+=vegeta.velocidad
			if event.key==K_LEFT:
				muve_vegeta.rect.x-=vegeta.velocidad
			if event.key==K_l:
				vegeta.img=pygame.image.load('imagenes/Vegeta ataque.png')
				vegeta.img=size(vegeta.img)
				destello=Destello()
				destello.image=size(destello.image)
				deslista.add(destello)
				ponch = True


	kamelista.update()
	deslista.update()
	kamelista.draw(SCREEN)
	deslista.draw(SCREEN)
	if ponch:
		for f in kamelista:
			if f.rect.colliderect(muve_vegeta.rect):
				vegeta.vida-=kameha.dano
				print (f"vegeta{vegeta.vida}")
				goku.img = pygame.image.load('imagenes/goku.png')
				goku.img = size(goku.img)
				vegeta.img = pygame.image.load('imagenes/vegueta lastimado.png')
				vegeta.img = size(vegeta.img)
				ponch = False

		for r in deslista:
			if r.rect.colliderect(muve_goku.rect):
				goku.vida-=destello.dano
				print (goku.vida)
				vegeta.img=pygame.image.load('imagenes/Vegeta.png')
				vegeta.img=size(vegeta.img)
				goku.img = pygame.image.load('imagenes/goku lastimado.png')
				goku.img=size(goku.img)
				ponch = False
				
	pygame.display.update()
	fpsClock.tick(FPS)