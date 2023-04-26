#import libraries
import pygame 
import random
import time
import sys

#pygame start
pygame.init()
pygame.display.set_caption('gaynor')

#define colors
blue    = (0, 0, 255)
green   = (0, 255, 0)
red     = (255, 0, 0)
white   = (255, 255, 255)
black   = (0, 0, 0)

window_x = 720
window_y = 520
CELL_SIZE = 20

font = pygame.font.SysFont('Georgia', 22)

snake_speed = CELL_SIZE

#snake_speed = 15
screen = pygame.display.set_mode([window_x, window_y])
clock = pygame.time.Clock()

class Snake: 
    def __init__(self):
        self.positions = [(window_x / 2, window_y / 2)]
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
    def move(self):
        x, y = self.positions[0]
        if self.direction == 'UP':
            y -= snake_speed
        elif self.direction == 'DOWN':
            y += snake_speed
        elif self.direction == 'LEFT':
            x -= snake_speed 
        elif self.direction == 'RIGHT':
            x += snake_speed
        
        self.positions.insert(0, (x,y))
        self.positions.pop()
    def change_direction(self, direction):
        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
    def add_segment(self):
        self.positions.append(self.positions[-1])
    def draw(self, surface):
        for position in self.positions:
            pygame.draw.rect(surface, green, (position[0], position[1], CELL_SIZE, CELL_SIZE))
            
class Apple:
        def __init__(self):
            self.position = (0, 0)
            self.randomize_position()
        def randomize_position(self):
            x = random.randint(0, window_x / CELL_SIZE -1) * CELL_SIZE
            y = random.randint(0, window_y / CELL_SIZE -1) * CELL_SIZE
            self.position = (x, y)
        def draw(self, surface):
            pygame.draw.rect(surface, red, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

def draw_text(text, font, surface, x, y):
    text_object = font.render(text, True, white)  #render
    text_rect = text_object.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_object, text_rect)

snake = Snake()
apple = Apple() 
score = 0
game_over = False
        
#run = True
while True: #run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('UP')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('DOWN')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('LEFT')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('RIGHT')
            elif event.key == pygame.K_c and game_over == True:
                #para reiniciar juego
                snake = Snake()
                apple = Apple()
                score = 0
                game_over = False
            

    if game_over == False:
        snake.move()

        if snake.positions[0][0] < 0 or snake.positions [0][0] > window_x - CELL_SIZE or snake.positions[0][1] < 0 or snake.positions [0][1] > window_y - CELL_SIZE:
                game_over = True
        for position in snake.positions[1:]:
                if snake.positions[0] == position:
                    game_over = True

#comprobar si la serpiente puede comer la manzana
    if snake.positions[0] == apple.position:
        apple.randomize_position()
        snake.add_segment()
        score += 10

#pantalla
    screen.fill(black) #1
    draw_text('score: {}'.format(score), font, screen, window_x / 2, 10)
    snake.draw(screen) 
    apple.draw(screen)

    if game_over == True:
        draw_text('GAME OVER', font, screen, window_x / 2, window_y / 2)
        draw_text('presiona C para volver a jugar :)', font, screen, window_x / 2, window_y / 2 + 30)


#actualiza pantalla ELIMINAR
    pygame.display.update()
    clock.tick(8)
pygame.quit()