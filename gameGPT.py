import pygame
import random

# Inicializar Pygame
pygame.init()

# Configurar la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego Simple")

# Configurar los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clase para representar el personaje
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def update(self):
        # Mover el personaje con las teclas de flecha
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Clase para representar enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        # Mover el enemigo hacia abajo y regresar al inicio si sale de la pantalla
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Crear todos los sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
enemies = pygame.sprite.Group()
for i in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Configurar el reloj
clock = pygame.time.Clock()

# Loop principal del juego
running = True
while running:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar los sprites
    all_sprites.update()

    # Detectar colisiones entre el personaje y los enemigos
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    # Dibujar todo
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Esperar para mantener una velocidad constante
    clock.tick(60)

# Salir del juego
pygame.quit()

