import pygame

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Moving Image')

image = pygame.image.load('HASBY.png')
image_width = image.get_width()
image_height = image.get_height()

x = (screen_width - image_width) / 2
y = (screen_height - image_height) / 2

speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= speed
            elif event.key == pygame.K_DOWN:
                y += speed
            elif event.key == pygame.K_LEFT:
                x -= speed
            elif event.key == pygame.K_RIGHT:
                x += speed
    
    screen.fill((255, 255, 255))
    screen.blit(image, (x, y))
    pygame.display.flip()

pygame.quit()
