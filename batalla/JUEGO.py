import pygame
import random

# Configuración de la pantalla
WIDTH = 800
HEIGHT = 600
FPS = 30

# Inicialización de Pygame y creación de la pantalla
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Batalla Aerea")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clases
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
            pass

class Plane(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Grupos de sprites
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Creación de los barcos y adición al grupo de sprites
ship = Ship(WIDTH / 2, HEIGHT - 50)
all_sprites.add(ship)

# Bucle principal del juego
running = True
while running:
    
# Mantenimiento de la velocidad de fotogramas
    clock.tick(FPS)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(ship.rect.centerx, ship.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # Actualización de los sprites
    all_sprites.update()

    # Dibujado de la pantalla
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Actualización de la pantalla
    pygame.display.flip()

# Salida del juego
pygame.quit()