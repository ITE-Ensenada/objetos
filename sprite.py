import pygame
import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))


#Personaje
Wr = [pygame.image.load('anim/walkr/wr1.png'),
    pygame.image.load('anim/walkr/wr2.png')]

Wl = [pygame.image.load('anim/walkl/wl1.png'),
    pygame.image.load('anim/walkl/wl2.png')]

Wu = [pygame.image.load('anim/walku/wu1.png'),
    pygame.image.load('anim/walku/wu2.png')]

Wd = [pygame.image.load('anim/walkd/wd1.png'),
    pygame.image.load('anim/walkd/wd2.png')]
