import pygame
import random

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Definir dimensiones de pantalla
ancho_pantalla = 800
alto_pantalla = 600

# Definir tamaño del bloque
tamaño_bloque = 10

# Inicializar Pygame
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode([ancho_pantalla, alto_pantalla])

# Establecer título de la pantalla
pygame.display.set_caption("Juego de la serpiente")

# Definir función para dibujar serpiente
def dibujar_serpiente(lista_bloques):
    for bloque in lista_bloques:
        pygame.draw.rect(pantalla, VERDE, [bloque[0], bloque[1], tamaño_bloque, tamaño_bloque])

# Definir función para generar comida aleatoria
def generar_comida():
    x_comida = round(random.randrange(0, ancho_pantalla - tamaño_bloque) / 10.0) * 10.0
    y_comida = round(random.randrange(0, alto_pantalla - tamaño_bloque) / 10.0) * 10.0
    return x_comida, y_comida

# Definir función principal del juego
def juego():
    # Inicializar variables del juego
    juego_terminado = False
    juego_en_pausa = False
    direccion_x = 0
    direccion_y = 0
    cabeza_x = ancho_pantalla / 2
    cabeza_y = alto_pantalla / 2
    lista_bloques = []
    largo_serpiente = 1
    x_comida, y_comida = generar_comida()
    reloj = pygame.time.Clock()

    # Bucle principal del juego
    while not juego_terminado:
        # Bucle de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_terminado = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    juego_en_pausa = not juego_en_pausa
                elif evento.key == pygame.K_LEFT:
                    direccion_x = -tamaño_bloque
                    direccion_y = 0
                elif evento.key == pygame.K_RIGHT:
                    direccion_x = tamaño_bloque
                    direccion_y = 0
                elif evento.key == pygame.K_UP:
                    direccion_x = 0
                    direccion_y = -tamaño_bloque
                elif evento.key == pygame.K_DOWN:
                    direccion_x = 0
                    direccion_y = tamaño_bloque

        # Mover cabeza de la serpiente
        cabeza_x += direccion_x
        cabeza_y += direccion_y

        # Si la cabeza de la serpiente choca con el borde de la pantalla, se acaba el juego
        if cabeza_x < 0 or cabeza_x >= ancho_pantalla or cabeza_y < 0 or cabeza_y >= alto_pantalla:
            juego_terminado = True

        # Si la cabeza de la serpiente choca con un bloque de su propio cuerpo, se acaba

        pygame.display.flip()
