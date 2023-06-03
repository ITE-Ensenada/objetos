""""Este codigo ejecuta un programa similar a paint, el cual funciona con una lista de comandos predeterminada"""
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#Colores para seleccionar en la lista de comandos

class Paint:
    """Clase de la ventana del Paint"""
    def __init__(self):
        """Caracteristicas de la ventana"""
        self.width = 800
        self.height = 600
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.default_bg_color = GREEN
        self.pixel_size = 1
        self.line_color = BLUE
        self.undo_stack = []

        pygame.init()
        pygame.display.set_caption("Paint con txt")
        self.surface.fill(self.default_bg_color)
        pygame.display.flip()

    def draw_pixel(self, x, y):
        """Dibujar pixel"""
        pygame.draw.rect(self.surface, self.line_color, (x, y, self.pixel_size, self.pixel_size))
        pygame.display.flip()

    def change_pixel_size(self, size):
        """Cambiar tamaño de pixel"""
        self.pixel_size = size

    def change_bg_color(self, color):
        """Cambiar color de fondo"""
        self.default_bg_color = color
        self.surface.fill(self.default_bg_color)
        pygame.display.flip()

    def linea_h(self):
        """Dibujar linea"""
        for i in range(0, 100):
            self.draw_pixel(100 + i, 200)
        pygame.display.flip()

    def linea_v(self):
        """Dibujar linea"""
        for i in range(0, 100):
            self.draw_pixel(100, 200 + i)
        pygame.display.flip()

    def draw_circle(self, center_x, center_y, radius):
        """Dibujar un circulo"""
        x = 0
        y = radius
        d = 3 - 2 * radius

        while x <= y:
            self.draw_pixel(center_x + x, center_y + y)
            self.draw_pixel(center_x + x, center_y - y)
            self.draw_pixel(center_x - x, center_y + y)
            self.draw_pixel(center_x - x, center_y - y)
            self.draw_pixel(center_x + y, center_y + x)
            self.draw_pixel(center_x + y, center_y - x)
            self.draw_pixel(center_x - y, center_y + x)
            self.draw_pixel(center_x - y, center_y - x)

            x += 1
            if d < 0:
                d += 4 * x + 6
            else:
                d += 4 * (x - y) + 10
                y -= 1

    def draw_line(self, x1, y1, x2, y2):
        """Dibujar linea"""
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = -1 if x1 > x2 else 1
        sy = -1 if y1 > y2 else 1
        err = dx - dy

        while x1 != x2 or y1 != y2:
            self.draw_pixel(x1, y1)
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def draw_triangle(self, x1, y1, x2, y2, x3, y3):
        """Dibujar triangulo"""
        self.draw_line(x1, y1, x2, y2)
        self.draw_line(x2, y2, x3, y3)
        self.draw_line(x3, y3, x1, y1)

    def draw_rectangle(self, x, y, width, height):
        """Dibujar rectangulo"""
        for i in range(height):
            for j in range(width):
                self.draw_pixel(x + j, y + i)
        pygame.display.flip()


linea1 = Paint()

myfile = open("comandos.cmd.txt", "r")
for cmd in myfile:
    cmd = cmd.strip()
    if cmd == "linea -h":
        linea1.linea_h()
    elif cmd == "linea -v":
        linea1.linea_v()
    elif cmd.startswith("circle"):
        _, center_x, center_y, radius = cmd.split()
        linea1.draw_circle(int(center_x), int(center_y), int(radius))
    elif cmd.startswith("triangle"):
        _, x1, y1, x2, y2, x3, y3 = cmd.split()
        linea1.draw_triangle(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3))
    elif cmd.startswith("line"):
        _, x1, y1, x2, y2 = cmd.split()
        linea1.draw_line(int(x1), int(y1), int(x2), int(y2))
    elif cmd.startswith("rectangle"):
        _, x, y, width, height = cmd.split()
        linea1.draw_rectangle(int(x), int(y), int(width), int(height))
    elif cmd == "undo":
        linea1.undo()
    elif cmd.startswith("bg_color"):
        _, r, g, b = cmd.split()
        color = (int(r), int(g), int(b))
        linea1.change_bg_color(color)
    elif cmd.startswith("pixel_size"):
        _, size = cmd.split()
        linea1.change_pixel_size(int(size))
    print(f"-{cmd}-")

myfile.close()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()