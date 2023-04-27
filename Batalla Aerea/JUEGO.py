import pygame
import random

# Inicializar Pygame
pygame.init()

# Establecer la ventana y el título
WIDTH = 600
HEIGHT =800

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Derrivar aviones")

# Cargar las imágenes
avion_img = pygame.image.load("avion.png")
torreta_img = pygame.image.load("torreta.png")
bala_img = pygame.image.load("bala.png")

# Definir la clase Avion
class Avion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = avion_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 5
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = 0

# Definir la clase Torreta
class Torreta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = torreta_img
        #self.rect = self.image.get_rect()
        #self.rect.x = WIDTH / 2 - self.rect.width / 2
        #self.rect.y = HEIGHT - self.rect.height
        imagen_chica = pygame.transform.scale(torreta_img, (50, 50))

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5
        elif teclas[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += 5

# Definir la clase Bala
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bala_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 10

# Establecer la posición inicial del avión
avion_x = random.randint(0, WIDTH - avion_img.get_width())
avion_y = 0

# Establecer la posición inicial de la torreta
torreta_x = WIDTH / 2 - torreta_img.get_width() / 2
torreta_y = HEIGHT - torreta_img.get_height()

# Inicializar la lista de balas
balas = []

# Establecer la velocidad del juego
velocidad_juego = 30

# Inicializar la puntuación
puntuacion = 0

# Establecer el reloj del juego
reloj = pygame.time.Clock()

# Bucle principal del juego
while True:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Disparar una bala al presionar la tecla Espacio
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bala_x = torreta_x + torreta_img.get_width() / 2 - bala_img.get_width() / 2
                bala_y = torreta_y - bala_img.get_height()
                balas.append(Bala(bala_x, bala_y))
    # Manejar la entrada del teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and torreta_x > 0:
        torreta_x -= 5
    elif teclas[pygame.K_RIGHT] and torreta_x < WIDTH - torreta_img.get_width():
        torreta_x += 5

    # Mover el avión hacia abajo
    avion_y += 5

    # Si el avión se sale de la pantalla, establecer una nueva posición aleatoria
    if avion_y > HEIGHT:
        avion_x = random.randint(0, WIDTH - avion_img.get_width())
        avion_y = 0

    # Mover las balas hacia arriba y eliminarlas si salen de la pantalla
    for bala in balas:
        bala[1] -= 10
        if bala[1] < 0:
            balas.remove(bala)

    # Dibujar los elementos del juego
    window.fill((255, 255, 255))
    window.blit(avion_img, (avion_x, avion_y))
    window.blit(torreta_img, (torreta_x, torreta_y))
    for bala in balas:
        window.blit(bala_img, (bala[0], bala[1]))

    # Detectar colisiones entre las balas y el avión
    for bala in balas:
        bala_rect = pygame.Rect(bala[0], bala[1], bala_img.get_width(), bala_img.get_height())
        avion_rect = pygame.Rect(avion_x, avion_y, avion_img.get_width(), avion_img.get_height())
        if bala_rect.colliderect(avion_rect):
            # Si hay colisión, eliminar la bala y establecer una nueva posición para el avión
            balas.remove(bala)
            avion_x = random.randint(0, WIDTH - avion_img.get_width())
            avion_y = 0
            # Incrementar la puntuación
            puntuacion += 1

    # Mostrar la puntuación en la pantalla
    font = pygame.font.Font(None, 36)
    texto_puntuacion = font.render(f"Puntuación: {puntuacion}", True, (0, 0, 0))
    window.blit(texto_puntuacion, (10, 10))

    # Actualizar la pantalla
    pygame.display.update()

    # Establecer la velocidad del juego
    reloj.tick(velocidad_juego)
