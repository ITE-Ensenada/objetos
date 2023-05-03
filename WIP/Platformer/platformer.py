import pygame, sys, time
from pygame.locals import*
import player, platforms

pygame.init()

font1 = pygame.font.SysFont('Times New Roman', 30)
font2 = pygame.font.SysFont('Times New Roman', 20)
fps = 10
fpsClock = pygame.time.Clock()

w_width    = 900    # X mark
w_height   = 600    # Y mark

screen = pygame.display.set_mode((w_width,w_height), 0, 32)
pygame.display.set_caption('Test')

floorDeco   = pygame.image.load('WIP/Platformer/Assets/Platforms/floorOver.png')
floorDecoX  = 0
floorDecoY  = 0

mc  = pygame.image.load('WIP/Platformer/Assets/Player/Idle/Idle 07.png')
mcX = 50
mcY = 514

bg  = pygame.image.load('WIP/Platformer/Assets/Background/BG1.png')
bgX = 0
bgY = 0

#colors
black   = (000,000,000) #black
white   = (255,255,255) #white
cyan    = (000,255,255) #cyan
red     = (255,000,000) #red
green   = (000,128,000) #green

def msg(text, font, surface, x, y):
    text_object = font.render(text, True, black)
    text_rect   = text_object.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_object, text_rect)

overLimits = False

#main cycle
while True:

    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if overLimits == False:
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    mcY -= 10
                    if mcY <= 0:
                        print("No puedes salir del límite.")
                        mcY += 10
                        overLimits = True
                elif event.key == pygame.K_DOWN:
                    mcY += 10
                    if mcY >= 524:
                        print("No puedes salir del límite.")
                        mcY -= 10
                        overLimits = True
                elif event.key == pygame.K_RIGHT:
                    mcX += 10
                    if mcX >= 900:
                        print("No puedes salir del límite.")
                        mcX -= 10
                        overLimits = True
                elif event.key == pygame.K_LEFT:
                    mcX -= 10
                    if mcX <= 0:
                        print("No puedes salir del límite.")
                        mcX += 10
                        overLimits = True
    
    screen.blit(bg,(bgX,bgY))
    screen.blit(mc,(mcX,mcY))
    screen.blit(floorDeco,(floorDecoX,floorDecoY))
    
    if overLimits == True:
        msg('You cant go over limits.', font1, screen, w_width/2, w_height/2)
        msg('Press spacebar to continue...', font2, screen, w_width/2, w_height/2 + 40)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    overLimits = False

    pygame.display.update()
    fpsClock.tick(fps)