import pygame
import random

# Define el tamaño de la pantalla y el tamaño de cada celda
ANCHO = 500
ALTO = 500
TAM_CELDA = 50

# Define los colores que se utilizarán para pintar las celdas
COLORES = [(0,0,255)]

class Barco:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def mover_izquierda(self):
        if self.columna > 0:
            self.columna -= 1

    def mover_derecha(self):
        if self.columna < 9:
            self.columna += 1
            
# Inicializa Pygame
pygame.init()

# Crea la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Crea una matriz de 10x10 para almacenar los colores de cada celda
colores_celdas = [[random.choice(COLORES) for _ in range(10)] for _ in range(10)]

# Bucle principal
while True:
    # Captura los eventos de Pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            SystemExit.exit()

    # Dibuja las celdas en la pantalla
    for fila in range(10):
        for columna in range(10):
            # Calcula las coordenadas de la celda en la pantalla
            x = columna * TAM_CELDA
            y = fila * TAM_CELDA

            # Obtiene el color de la celda y pinta el rectángulo en la pantalla
            color_celda = colores_celdas[fila][columna]
            rectangulo = pygame.Rect(x, y, TAM_CELDA, TAM_CELDA)
            pygame.draw.rect(pantalla, color_celda, rectangulo)

    # Actualiza la pantalla
    pygame.display.update()
