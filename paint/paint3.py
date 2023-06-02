"Este es un programa para dibujar llamado paint fue Programado por: CARRILLO07 "
import sys
import pygame

class Paint:
    "Esta es una clase llamada paint y es donde se encuentran los comandos que se utilizan en este codigo"
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.commands = {
            'about': self.about,
            'help': self.help,
            'rectangulo': self.create_rectangle,
            'circulo': self.create_circle,
            'horizontal': self.create_horizontal_line,
            'vertical': self.create_vertical_line
        }
        self.description = "Este es un programa de paint por línea de comandos."
        self.programmer = "Programador: [CARRILLO07]"
        self.supported_commands = "Comandos soportados: about, help, rectangle, circle, horizontal, vertical""[Lista de colores soportados- white, red, green, blue, yellow, cyan, magenta, gray, purple]"
        self.colors = {
            'black': (0, 0, 0),
            'white': (255, 255, 255),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'yellow': (255, 255, 0),
            'cyan': (0, 255, 255),
            'magenta': (255, 0, 255),
            'gray': (128, 128, 128),
            'purple': (128, 0, 128)
        }
    def about(self):
        "Esta es una funcion que se encarga de mostrar la descripcion de lo que hace el programa"
        self.screen.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 24)
        text = font.render(self.description + "\n" + self.programmer, True, (0, 0, 0))
        self.screen.blit(text, (50, 50))
        pygame.display.flip()
    def help(self):
        "Esta es una funcion que se esncarga de darle al usuario ayuda sobre los comandos que soporta el programa"
        self.screen.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 24)
        text = font.render(self.supported_commands, True, (0, 0, 0))
        self.screen.blit(text, (50, 50))
        pygame.display.flip()
    def create_rectangle(self):
        "Esta es la funcion que se encarga de crear un  rectangulo de cualquier dimension quee desee el usuario"
        self.screen.fill((255, 255, 255))
        if len(sys.argv) < 4:
            print("Por favor, ingrese el ancho y la altura del rectángulo.")
            return
        width = int(sys.argv[2])
        height = int(sys.argv[3])
        pygame.draw.rect(self.screen, self.get_color(), pygame.Rect(250 - width // 2, 250 - height // 2, width, height))
        pygame.display.flip()
    def create_circle(self):
        "Esta funcion se encarga de crear un circulo del radio que desee el usuario"
        self.screen.fill((255, 255, 255))
        if len(sys.argv) < 3:
            print("Por favor, ingrese el radio del círculo.")
            return
        radius = int(sys.argv[2])
        pygame.draw.circle(self.screen, self.get_color(), (250, 250), radius)
        pygame.display.flip()
    def create_horizontal_line(self):
        "Esta funcion se encarga de crear una linea horizontal de la longitud que desee el usuario"
        self.screen.fill((255, 255, 255))
        if len(sys.argv) < 3:
            print("Por favor, ingrese la longitud de la línea horizontal.")
            return
        length = int(sys.argv[2])
        pygame.draw.line(self.screen, self.get_color(), (250 - length // 2, 250), (250 + length // 2, 250), 3)
        pygame.display.flip()
    def create_vertical_line(self):
        "Esta funcion se encarga de crear una linea vertical de la longitud que desee el usuario "
        self.screen.fill((255, 255, 255))
        if len(sys.argv) < 3:
            print("Por favor, ingrese la longitud de la línea vertical.")
            return
        length = int(sys.argv[2])
        pygame.draw.line(self.screen, self.get_color(), (250, 250 - length // 2), (250, 250 + length // 2), 3)
        pygame.display.flip()
    def get_color(self):
        "Esta es la funcion que hace que se pueda elegir el color deseado para la figura"
        if len(sys.argv) < 4 or sys.argv[3] not in self.colors:
            return (0, 0, 0)  # Default color: black
        return self.colors[sys.argv[3]]
    def run_command(self, command):
        "Esta funcion es la que se encarga de correr el comando help"
        if command in self.commands:
            self.commands[command]()
        else:
            self.help()

def main():
    "Esta funcion se encarga de dar al inicio un mensaje diciendo que ingrese un comando deseado"
    paint = Paint()
    if len(sys.argv) < 2:
        print("Por favor, ingrese un comando.")
        return
    command = sys.argv[1].lower()
    paint.run_command(command)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()             