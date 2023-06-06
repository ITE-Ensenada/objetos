import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Paint:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.default_bg_color = BLUE
        self.pixel_size = 1
        self.line_color = BLUE
        self.undo_stack = []

        pygame.init()
        pygame.display.set_caption("Paint con txt")
        self.surface.fill(self.default_bg_color)
        pygame.display.flip()

    def draw_pixel(self, x, y):
        pygame.draw.rect(self.surface, self.line_color, (x, y, self.pixel_size, self.pixel_size))
        pygame.display.flip()

    def change_pixel_size(self, size):
        self.pixel_size = size

    def change_bg_color(self, color):
        self.default_bg_color = color
        self.surface.fill(self.default_bg_color)
        pygame.display.flip()

    def linea_h(self):
        for i in range(0, 100):
            self.draw_pixel(100 + i, 200)
        pygame.display.flip()

    def linea_v(self):
        for i in range(0, 100):
            self.draw_pixel(100, 200 + i)
        pygame.display.flip()

    def draw_circle(self, center_x, center_y, radius):
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
        self.draw_line(x1, y1, x2, y2)
        self.draw_line(x2, y2, x3, y3)
        self.draw_line(x3, y3, x1, y1)

    def draw_rectangle(self, x, y, width, height):
        for i in range(height):
            for j in range(width):
                self.draw_pixel(x + j, y + i)
        pygame.display.flip()

    def undo(self):
        if len(self.undo_stack) > 0:
            last_action = self.undo_stack.pop()
            self.surface.fill(self.default_bg_color)
            for action in self.undo_stack:
                action()
            pygame.display.flip()

def execute_commands():
    linea1 = Paint()

    with open("comandos.cmd.txt", "r") as myfile:
        for cmd in myfile:
            cmd = cmd.strip()
            if cmd == "linea -h":
                linea1.linea_h()
                linea1.undo_stack.append(linea1.linea_h)
            elif cmd == "linea -v":
                linea1.linea_v()
                linea1.undo_stack.append(linea1.linea_v)
            elif cmd.startswith("circle"):
                _, center_x, center_y, radius = cmd.split()
                linea1.draw_circle(int(center_x), int(center_y), int(radius))
                linea1.undo_stack.append(lambda: linea1.draw_circle(int(center_x), int(center_y), int(radius)))
            elif cmd.startswith("triangle"):
                _, x1, y1, x2, y2, x3, y3 = cmd.split()
                linea1.draw_triangle(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3))
                linea1.undo_stack.append(lambda: linea1.draw_triangle(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3)))
            elif cmd.startswith("line"):
                _, x1, y1, x2, y2 = cmd.split()
                linea1.draw_line(int(x1), int(y1), int(x2), int(y2))
                linea1.undo_stack.append(lambda: linea1.draw_line(int(x1), int(y1), int(x2), int(y2)))
            elif cmd.startswith("rectangle"):
                _, x, y, width, height = cmd.split()
                linea1.draw_rectangle(int(x), int(y), int(width), int(height))
                linea1.undo_stack.append(lambda: linea1.draw_rectangle(int(x), int(y), int(width), int(height)))
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

def main():
    pygame.init()
    execute_commands()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
