import pygame, sys
from pygame.locals import*

pygame.init()

fps = 10
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((1000,600))

pygame.display.set_caption('Test')

#colors
c1  = (000,000,000) #black
c2  = (255,255,255) #white
c3  = (000,255,255) #cyan
c4  = (255,000,000) #red
c5  = (000,128,000) #green

#main cycle
while True:

    screen.fill(c5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(fps)