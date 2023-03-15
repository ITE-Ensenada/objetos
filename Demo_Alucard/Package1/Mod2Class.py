import pygame

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
    personajeImg = pygame.image.load('Assets/alucard.png')						#Imagen del personaje
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
