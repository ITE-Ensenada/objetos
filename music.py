import pygame
import os 
from pygame.locals import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#Música de fondo
pygame.mixer.music.load('sonido/onett.wav')
pygame.mixer.music.play(-1)