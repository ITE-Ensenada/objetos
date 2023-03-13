import pygame, sys
from pygame.locals import *

class Set_display():
    SCREEN = pygame.display.set_mode((1200, 800))    #El tamaño de la ventana
    window_name = pygame.display.set_caption('Animation')   #Da el nombre de la ventana
    WHITE = (255, 255, 255)                                 #Define el color para el fondo de la pantalla en una variable
    FPS = 10                                                #Frames per second setting

    def backgroungColor(self):                                  #Pinta el fondo de pantalla
        self.SCREEN.fill(self.WHITE)

    def drawImagen(self, personajeImg, positionX, positionY):   #Pinta la imagen del personaje
        self.SCREEN.blit(personajeImg, (positionX, positionY))

class Alicard():
    personajeImg = pygame.image.load('alucard.png')						#Imagen del personaje
    personajeImg = pygame.transform.scale(personajeImg, (384, 216))	    #Tamaño de la imagen del personaje
    personajeX = 10														#Movimiento eje X del personaje
    personajeY = 10														#Movimiento eje Y del personaje
    direction = 'right'													#Direccion inicial del personaje

    #Metodos que mueven los atributos de posicion
    def move_right(self):
        self.personajeX += 20
    def move_left(self):
        self.personajeX -= 20
    def move_up(self):
        self.personajeY -= 20
    def move_down(self):
        self.personajeY += 20    



pygame.init()

#Declaracion de objetos
player = Alicard()                     #Objeto que controla al personaje
screen = Set_display()                 #Objeto que controla la pantalla
fpsClock = pygame.time.Clock()         #Objeto que ayuda a rastrear el tiempo

while True: #Ciclo del juego
    
    screen.backgroungColor()   #Pinta el fondo de pantalla

    #Evalua la direccion del objeto player y ocasiona cambie de direccion
    if player.direction == 'right':
        player.move_right()
        if player.personajeX >= 796:
            player.direction = 'down'
    elif player.direction == 'down':
        player.move_down()
        if player.personajeY >= 564:
            player.direction = 'left'
    elif player.direction == 'left':
        player.move_left()
        if player.personajeX <= 20:
            player.direction = 'up'
    elif player.direction == 'up':
        player.move_up()
        if player.personajeY <= 20:
            player.direction = 'right'
    
    #screen.SCREEN.blit(player.personajeImg, (player.personajeX, player.personajeY))    #En caso de no usarse la linea de codigo 65 se puede usar esta
    screen.drawImagen(player.personajeImg, player.personajeX, player.personajeY)        #Dibuja una imagen sobre otra (Dibuja la imagen del personaje sobre el display)

    for event in pygame.event.get():
        print(event)

        #Detecta un evento donde se oprima una tecla para realizar una accion especifica
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:  #Si se oprime la flecha abajo, el personaje cambia su direccion
                player.direction = 'down'
            
            if event.key == pygame.K_UP:    #Si se oprime la flecha arriba, el personaje cambia su direccion
                player.direction = 'up'
            
            if event.key == pygame.K_LEFT:  #Si se oprime la flecha izquierda, el personaje cambia su direccion
                player.direction = 'left'
            
            if event.key == pygame.K_RIGHT: #Si se oprime la flecha derecha, el personaje cambia su direccion
                player.direction = 'right'

            #Con la letra ESCAPE se sale del juego (SE AGREGO PARA FACILIDAD DE TESTEO)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit() 

        if event.type == QUIT:              #Si se detecta que se cierra la ventana se cierra el juego 
            pygame.quit()
            sys.exit()
    
    pygame.display.update()                 #Actualiza el display
    fpsClock.tick(screen.FPS)