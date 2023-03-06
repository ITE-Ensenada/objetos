import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)

    rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size())//2]*2))
    
    for x in range(rect.width):
        u = x / (rect.width - 1)
        color = (round(u*255), 0, round((1-u)*255))
        for y in range(rect.height):
            window.set_at((rect.left + x, rect.top + y), color) 
    
    pygame.display.flip()

pygame.quit()
exit()
