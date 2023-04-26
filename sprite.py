import pygame
import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))


#Personaje
wr = [pygame.image.load('anim/walkr/wr1.png'),
    pygame.image.load('anim/walkr/wr2.png')]

wl = [pygame.image.load('anim/walkl/wl1.png'),
    pygame.image.load('anim/walkl/wl2.png')]

wu = [pygame.image.load('anim/walku/wu1.png'),
    pygame.image.load('anim/walku/wu2.png')]

wd = [pygame.image.load('anim/walkd/wd1.png'),
    pygame.image.load('anim/walkd/wd2.png')]
