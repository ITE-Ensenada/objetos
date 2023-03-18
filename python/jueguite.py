import pygame, sys, time
from pygame.locals import*
pygame.init()
win=pygame.display.set_mode((740,945))
img=pygame.image.load("gatite.png")
fondo=(255,255,255)
pygame.init()
FPS= 10 
x=10
y=98

class gato:
    especie= "cafe con leche"   
    def especificaciones (Self,nombre,vida,fuerza,caminar):
        Self.nombre=nombre
        Self.vida=vida
        Self.fuerza=fuerza
        Self.caminar=caminar

class arma_principal:
	Espada = "1"
	def __init__(self,material,daño,resistencia):
		self.material=material
		self.daño=daño
		self.resistencias=resistencia 

class arma_secundaria: 		
	Espada = "2"
	def __init__(self,material,daño,resistencia):
		self.material=material
		self.daño=daño
		self.resistencias=resistencia 

class arma_terciaria: 
	Espada = "3"
	def __init__(self,material,daño,resistencia):
		self.material=material	
		self.daño=daño
		self.resistencia=resistencia

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
