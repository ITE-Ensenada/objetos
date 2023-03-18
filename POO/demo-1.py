import pygame, sys
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

RED = (255,0,0)

while True: # the main game loop

	SCREEN.fill(RED)
	SCREEN.blit(goku.img, (muve_goku.rect))
	SCREEN.blit(vegeta.img, (muve_vegeta.rect))
	#SCREEN.blit(destello.img, (destelloF.rect))

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
			'''if event.key==K_r:
				SCREEN.blit(kame.img, (kameha.rect))
				goku.img=pygame.image.load('imagenes/goku ataque.png')
				goku.img=tamano(goku.img)
				while True:
					kameha.rect.x+=kame.rapidez
					SCREEN.blit(kame.img, (kameha.rect))'''


			if event.key==K_UP:
				muve_vegeta.rect.y-=vegeta.velocidad
			if event.key==K_DOWN:
				muve_vegeta.rect.y+=vegeta.velocidad
			if event.key==K_RIGHT:
				muve_vegeta.rect.x+=vegeta.velocidad
			if event.key==K_LEFT:
				muve_vegeta.rect.x-=vegeta.velocidad


	
	
	pygame.display.update()
	fpsClock.tick(FPS)