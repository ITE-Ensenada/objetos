""""Este codigo ejecuta un juego de Hasbulla recogiendo dinero"""
import random
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Bomba(pygame.sprite.Sprite):
    """"boom"""
    def __init__(self):
        """"imagen"""
        super().__init__()
        self.image = pygame.image.load("Bomba.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
    def update(self):
        """"rango"""
        self.rect.y += 1

        if self.rect.y > 600:
            self.rect.y = -10
            self.rect.x = random.randrange(900)

    def detenido(self):
        """"explosion"""
        print(f"{self.hasbulla} has sido detenido.")

class Money(pygame.sprite.Sprite):
    """"dinero"""
    def __init__(self):
        """"imagen"""
        super().__init__()
        self.image = pygame.image.load("MONEY.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        """"rango"""
        self.rect.y += 1

        if self.rect.y > 600:
            self.rect.y = -10
            self.rect.x = random.randrange(900)

    def billetes(self):
        """obtuviste billetes"""
        print(f"{self.hasbulla} has obtenido billetes.")


class Coin(Money):
    """"dinero"""
    def __init__(self):
        """"imagen"""
        super().__init__()
        self.image = pygame.image.load("COIN.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        """"rango"""
        self.rect.y += 1

        if self.rect.y > 600:
            self.rect.y = -10
            self.rect.x = random.randrange(900)

    def moneda(self):
        """moneda obtenida"""
        print(f"{self.hasbulla} has obtenido moneda.")


class Treasure(Money):
    """"dinero"""
    def __init__(self):
        """"imagen"""
        super().__init__()
        self.image = pygame.image.load("TREASURE.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        """"rango"""
        self.rect.y += 1

        if self.rect.y > 600:
            self.rect.y = -10
            self.rect.x = random.randrange(900)

    def tesoro(self):
        """"tesoro obtenido"""
        print(f"{self.hasbulla} has obtenido tesoro.")


class Hasbulla(pygame.sprite.Sprite):
    """"Enanito Feliz"""
    def __init__(self):
        """"imagen"""
        super().__init__()
        self.image = pygame.image.load("hasbulla1.gif").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        """rango"""
        mouse_pos = pygame.mouse.get_pos()
        Hasbulla.rect.x = mouse_pos[0]
        Hasbulla.rect.y = mouse_pos[1]

    def feliz(self):
        """"Hasbulla es feliz"""
        print(f"{self.hasbulla} Esta contento.")


pygame.init()

screen = pygame.display.set_mode([900, 600])
clock = pygame.time.Clock()
done = False
score = 0

money_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    money = Money()
    money.rect.x = random.randrange(900)
    money.rect.y = random.randrange(600)

    money_list.add(money)
    all_sprite_list.add(money)

hasbulla = Hasbulla()
all_sprite_list.add(hasbulla)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprite_list.update()

    money_hit_list = pygame.sprite.spritecollide(hasbulla, money_list, True)

    for money in money_hit_list:
        score += 1
        print(score)
    screen.fill(WHITE)

    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
