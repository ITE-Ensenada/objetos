import pygame,sys
from pygame.locals import*
pygame.init()
FPS = 10 
fpsClock = pygame.time.Clock()

BASE = 444
ALTURA = 240

SCREEN = pygame.display.set_mode((BASE,ALTURA))
pygame.display.set_caption('Super Mario')

X=10
Y=190
FONDO = pygame.image.load('fondo.png')
PARADO = pygame.image.load('mario/0.png')
while True:
    SCREEN.blit(FONDO, [0,0])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        X -= 10
    if keys[pygame.K_RIGHT]:
        X += 10
    if keys[pygame.K_UP]:
        Y -= 10

    SCREEN.blit(PARADO,(X,Y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
