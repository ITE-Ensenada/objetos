import random
import pygame
from pygame.locals import*
from Meteoros import*
#Fps
reloj=pygame.time.Clock()
FPS=60
#Pantalla
SCREEN_AL=1100
SCREEN_AN=600
SCREEN=pygame.display.set_mode((SCREEN_AL,SCREEN_AN))
#Nombre y icono del juegoA
pygame.display.set_caption('Space Fighters')
icono=pygame.image.load("Nave1.png")
pygame.display.set_icon(icono)
#Rgb de Colores
AzulCielo=(63,255,238)
Blanco=(255, 255, 255)
Negro=(0, 0, 0)
Rojo=(255, 0, 0)
Verde=(0, 255, 0)
Azul=(0, 0, 255)
#Carga de fondo
fondo=pygame.image.load("Fondo.png")
def dibujar_fondo():
    """Carga fondo"""
    SCREEN.blit(fondo,(0,0))
#Clase para Nave 1
class Nave(pygame.sprite.Sprite):
    """Clase para nave1"""
    def __init__(self,p_x,p_y,vida):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("Nave1.png"), (120, 80))
        self.rect = self.image.get_rect()
        self.rect.center = [p_x,p_y]
        self.vida_inicio = vida
        self.vida_restante = vida
        self.ultima_bala = pygame.time.get_ticks()

    def update(self):
        """Actualizador"""
        velo_nave = 8

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= velo_nave
        if key[pygame.K_RIGHT] and self.rect.right < SCREEN_AL and self.rect.right < 500 :
            self.rect.x += velo_nave
        if key[pygame.K_UP] and self.rect.y > 10 :
            self.rect.y -= velo_nave
        if key[pygame.K_DOWN] and self.rect.y < 480 :
            self.rect.y += velo_nave
        pygame.draw.rect(SCREEN,Rojo,(self.rect.x,(self.rect.bottom + 10),self.rect.width,15))
        if self.vida_restante > 0:
            pygame.draw.rect(SCREEN,Verde,(self.rect.x,(self.rect.bottom + 10),int(self.rect.width *
            (self.vida_restante / self.vida_inicio)),15))
        if self.vida_restante == 0:
            self.kill()

        enfriamiento = 500
        tiempo = pygame.time.get_ticks()
        if key[pygame.K_m] and tiempo - self.ultima_bala > enfriamiento:
            bala = Balas (self.rect.centerx + 80, self.rect.centery)
            Balas_group.add(bala)
            self.ultima_bala = tiempo

        ya_1=250
        limite_1 = 10000
        limite_2 = 8000
        tiempo = pygame.time.get_ticks()
        if tiempo < limite_1:
            if tiempo > limite_2/2:
                pygame.draw.rect(SCREEN,AzulCielo,(10,10,40,40))
                if tiempo > limite_2:
                    pygame.draw.rect(SCREEN,Rojo,(20,20,20,20))
                    if key[pygame.K_n] and tiempo - self.ultima_bala > ya_1:
                        ultis = Ulti(self.rect.centerx + 80, self.rect.centery)
                        Balas_group.add(ultis)
                        self.ultima_bala = tiempo
                if tiempo > limite_2:
                    pygame.draw.rect(SCREEN,Rojo,(10,10,40,40))
#Creacion para agrupar las naves
Naves_group = pygame.sprite.Group()
Nave = Nave(int(70), 310, 5)
Naves_group.add(Nave)
#Clase para Nave 2
class Nave2(pygame.sprite.Sprite):
    """Clase para nave2"""
    def __init__(self,p_x,p_y, vida):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("Nave2.png"),(120, 80))
        self.rect = self.image.get_rect()
        self.rect.center = [p_x,p_y]
        self.vida_inicio = vida
        self.vida_restante = vida
        self.ultima_bala = pygame.time.get_ticks()

    def update(self):
        """Actualizador"""
        velo_nave=8

        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.rect.left > 0 and self.rect.left > 580:
            self.rect.x -= velo_nave
        if key[pygame.K_d] and self.rect.right < SCREEN_AL:
            self.rect.x+=velo_nave
        if key[pygame.K_w] and self.rect.y > 10 :
            self.rect.y -= velo_nave
        if key[pygame.K_s] and self.rect.y < 480 :
            self.rect.y += velo_nave
        pygame.draw.rect(SCREEN,Rojo,(self.rect.x,(self.rect.bottom + 10),self.rect.width,15))
        if self.vida_restante >= 1:
            pygame.draw.rect(SCREEN,Verde,(self.rect.x,(self.rect.bottom + 10),int(self.rect.width *
            (self.vida_restante / self.vida_inicio)),15))
        if self.vida_restante == 0:
            self.kill()

        enfriamiento = 500
        tiempo = pygame.time.get_ticks()
        if key[pygame.K_f] and tiempo - self.ultima_bala > enfriamiento:
            bala = Balas2 (self.rect.x - 40, self.rect.centery)
            Balas_group.add(bala)
            self.ultima_bala=tiempo

        ya_1=250
        limite_1 = 10000
        limite_2 = 8000
        tiempo = pygame.time.get_ticks()
        if tiempo < limite_1:
            if tiempo > limite_2/2:
                pygame.draw.rect(SCREEN,AzulCielo,(1050,10,40,40))
                if tiempo > limite_2:
                    pygame.draw.rect(SCREEN,Rojo,(1050,20,20,20))
                    if key[pygame.K_e] and tiempo - self.ultima_bala > ya_1:
                        ultis = Ulti2(self.rect.centerx - 60, self.rect.centery)
                        Balas_group.add(ultis)
                        self.ultima_bala = tiempo
                    if tiempo > limite_2:
                        pygame.draw.rect(SCREEN,Rojo,(1050,10,40,40))
#Creacion de segundo grupo para agrupar naves
Naves_group2 = pygame.sprite.Group()
Nave2 = Nave2(int(1030), 310, 5)
Naves_group2.add(Nave2)
#Clase para balas
class Balas(pygame.sprite.Sprite):
    """Clase para balas"""
    def __init__(self,b_x,b_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("Bala.png"), (50,20))
        self.rect = self.image.get_rect()
        self.rect.center = [b_x,b_y]

    def update(self):
        """Actualizador"""
        self.rect.x += 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, Naves_group2, False):
            self.kill()
            Nave2.vida_restante -= 1
        if pygame.sprite.spritecollide(self, Meteoro_group, True):
            self.kill()
class Balas2(pygame.sprite.Sprite):
    """Clase para balas2"""
    def __init__(self,b_x,b_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("Bala2.png"), (50,20))
        self.rect = self.image.get_rect()
        self.rect.center = [b_x,b_y]

    def update(self):
        """Actualizador"""
        self.rect.x -= 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, Naves_group, False):
            self.kill()
            Nave.vida_restante -= 1
        if pygame.sprite.spritecollide(self, Meteoro_group, True):
            self.kill()
#Creacion para agrupar las balas
Balas_group = pygame.sprite.Group()
#Creacion de clase para la ulti
class Ulti(pygame.sprite.Sprite):
    """Clase para Ulti1"""
    def __init__(self,b_x,b_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("Bala.png"), (50,20))
        self.rect = self.image.get_rect()
        self.rect.center = [b_x,b_y]

    def update(self):
        """Actualizador"""
        self.rect.x += 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, Naves_group2, False):
            self.kill()
            Nave2.vida_restante -= 1
        if pygame.sprite.spritecollide(self, Meteoro_group, True):
            self.kill()
class Ulti2(pygame.sprite.Sprite):
    """Clase para Ulti2"""
    def __init__(self,b_x,b_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("Bala2.png"), (50,20))
        self.rect = self.image.get_rect()
        self.rect.center = [b_x,b_y]

    def update(self):
        """Actualizador"""
        self.rect.x -= 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, Naves_group, False):
            self.kill()
            Nave.vida_restante -= 1
        if pygame.sprite.spritecollide(self, Meteoro_group, True):
            self.kill()
#Creacion de agrupacion de las ulti
Ultis_group = pygame.sprite.Group()
#Codigo para hacer que cada meteoro aparezca en pantalla
Meteoro_group = pygame.sprite.Group()
Meteoro1 = Meteoro1(int(random.randint(500,600)),random.randint(0,590))
Meteoro2 = Meteoro2(int(random.randint(500,600)),random.randint(0,590))
Meteoro3 = Meteoro3(int(random.randint(500,600)),random.randint(0,590))
Meteoro4 = Meteoro4(int(random.randint(500,600)),random.randint(0,590))
Meteoro5 = Meteoro5(int(random.randint(500,600)),random.randint(0,590))
Meteoro6 = Meteoro6(int(random.randint(500,600)),random.randint(0,590))
Meteoro7 = Meteoro7(int(random.randint(500,600)),random.randint(0,590))
Meteoro8 = Meteoro8(int(random.randint(500,600)),random.randint(0,590))
Meteoro9 = Meteoro9(int(random.randint(500,600)),random.randint(0,590))
Meteoro10 = Meteoro10(int(random.randint(500,600)),random.randint(0,590))
Meteoro_group.add(Meteoro1)
Meteoro_group.add(Meteoro2)
Meteoro_group.add(Meteoro3)
Meteoro_group.add(Meteoro4)
Meteoro_group.add(Meteoro5)
Meteoro_group.add(Meteoro6)
Meteoro_group.add(Meteoro7)
Meteoro_group.add(Meteoro8)
Meteoro_group.add(Meteoro9)
Meteoro_group.add(Meteoro10)
#While del juego

while True:

    reloj.tick(FPS)
    dibujar_fondo()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Actualizacion en pantalla de todo
    Meteoro1.update()
    Meteoro2.update()
    Meteoro3.update()
    Meteoro4.update()
    Meteoro5.update()
    Meteoro6.update()
    Meteoro7.update()
    Meteoro8.update()
    Meteoro9.update()
    Meteoro10.update()
    Balas_group.update()
    Nave.update()
    Nave2.update()
    Meteoro_group.draw(SCREEN)
    Balas_group.draw(SCREEN)
    Naves_group.draw(SCREEN)
    Naves_group2.draw(SCREEN)
    pygame.display.update()
