import pygame, sys
from pygame.locals import*
pygame.init()
win=pygame.display.set_mode((740,945))
img=pygame.image.load("gatite.png")
fondo=(255,255,255)
pygame.init()
FPS= 10 


class gato:
    especie= "cafe con leche"
    def __init__ (Self,nombre,vida):
        Self.nombre=nombre
        Self.vida=250
        Self.fuerza=10
        Self.caminar=15
       
x=10
y=98

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_a: 
                print ("Has presionado la letra A")
                x=x-25
            if event.key == pygame.K_w:
                print ("La letra w se ha presionado")
                y=y-25
            if event.key == pygame.K_d: 
                print ("La letra d se ha presionado")
                x=x+25
            if event.key == pygame.K_s: 
                print ("La letra s se ha presionado")
                y=y+25
            
    
    win.fill(fondo)
    win.blit(img,(x,y))
    pygame.display.update()         