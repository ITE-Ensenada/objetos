import pygame, random

ANCHO = 650
ALTO = 649

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)


pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("GATITEEEEEEE")
clock = pygame.time.Clock()

class Gatito(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("gatite.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = ANCHO // 2
		self.rect.bottom = ALTO - 10
		self.speed_x = 0
		self.vida = 100

	def update(self):
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			print ("te has movido a la izquierda")
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			print ("te has movido a la izquierda")
			self.speed_x = 5
		self.rect.x += self.speed_x
		if self.rect.right > ANCHO:
			self.rect.right = ANCHO
		if self.rect.left < 0:
			self.rect.left = 0

	def disparo(self):
		bala = Bala(self.rect.centerx, self.rect.top)
		all_sprites.add(bala)
		bullets.add(bala)


class Meteoro(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(meteoro_imagenes)
		self.image.set_colorkey(NEGRO)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(ANCHO - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > ALTO + 10 or self.rect.left < -25 or self.rect.right > ANCHO + 22 :
			self.rect.x = random.randrange(ANCHO - self.rect.width)

			self.rect.y = random.randrange(-150, -100)
			self.speedy = random.randrange(1, 8)

class Bala(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("laser.png")
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_kbum[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_kbum):
				self.kill() 
			else:
				center = self.rect.center
				self.image = explosion_kbum[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

def Texto_mostrado(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, (255, 255, 255))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def Barra_vida(surface, x, y, percentage):
	BAR_ANCHO = 100
	BAR_ALTO = 10
	fill = (percentage / 100) * BAR_ANCHO
	border = pygame.Rect(x, y, BAR_ANCHO, BAR_ALTO)
	fill = pygame.Rect(x, y, fill, BAR_ALTO)
	pygame.draw.rect(surface, VERDE, fill)
	pygame.draw.rect(surface, BLANCO, border, 2)

def texto_pantalla():
	pantalla.blit(background, [0, 0])
	Texto_mostrado(pantalla, "GATITE", 65, ANCHO // 2, ALTO / 4)
	Texto_mostrado(pantalla, "PRESIONA UNA TECLA PA COMENZAR", 17, ANCHO // 2, ALTO * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYUP:
				waiting = False

meteoro_imagenes = []
Meteoro_lista = ["meteoros/meteoro_grande1.png", "meteoros/meteoro_grande2.png", "meteoros/meteoro_medio1.png", "meteoros/meteoro_medio2.png"]
for img in Meteoro_lista:
	meteoro_imagenes.append(pygame.image.load(img).convert())

 
explosion_kbum = []
for i in range(8):
	file = "explosiones/pum0{}.png".format(i)
	img = pygame.image.load(file)
	img_scale = pygame.transform.scale(img, (50, 50))
	explosion_kbum.append(img_scale)


background = pygame.image.load("fondite.png").convert()

pierde = True
run = True
while run:
	if pierde:
		texto_pantalla()
		pierde = False
		all_sprites = pygame.sprite.Group()
		Meteoro_lista = pygame.sprite.Group()
		bullets = pygame.sprite.Group()

		jugador = Gatito()
		all_sprites.add(jugador)

		for i in range(6):
			meteoro = Meteoro()
			all_sprites.add(meteoro)
			Meteoro_lista.add(meteoro)

		puntaje = 0

	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				print("has disparado")
				jugador.disparo()
		

	all_sprites.update()


	hits = pygame.sprite.groupcollide(Meteoro_lista, bullets, True, True)
	for hit in hits:
		puntaje += 1
		explosion = Explosion(hit.rect.center)
		all_sprites.add(explosion)

		meteoro = Meteoro()
		all_sprites.add(meteoro)
		Meteoro_lista.add(meteoro)

	pantalla.blit(background, [0, 0])
	all_sprites.draw(pantalla)

	Texto_mostrado(pantalla, str(puntaje), 35, ANCHO // 2, 10)


	Barra_vida(pantalla, 8, 5, jugador.vida)


	pygame.display.flip()

pygame.quit()