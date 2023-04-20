import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir pantalla
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Memorizar números")

# Definir fuentes de texto
font_small = pygame.font.Font(None, 24)
font_large = pygame.font.Font(None, 72)

# Definir variables de juego
number_sequence = [3, 7, 1, 9, 4, 8, 2, 5, 6]
memorized = False
correct = False
feedback_message = ""

# Función para mostrar la secuencia de números
def show_number_sequence():
    global memorized
    text = font_large.render(" ".join(map(str, number_sequence)), True, BLACK)
    screen.blit(text, [50, 100])
    pygame.display.flip()
    pygame.time.wait(3000)
    memorized = True

# Función para mostrar el mensaje de retroalimentación
def show_feedback():
    global feedback_message
    text = font_small.render(feedback_message, True, BLACK)
    screen.blit(text, [150, 200])
    text = font_small.render("Presiona Enter para jugar de nuevo", True, BLACK)
    screen.blit(text, [80, 230])
    pygame.display.flip()

# Ciclo principal del juego
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if correct:
                    # Reiniciar el juego
                    number_sequence = [random.randint(0, 9) for _ in range(10)]
                    memorized = False
                    correct = False
                else:
                    # Evaluar la respuesta del usuario
                    answer = input_box.text
                    answer_array = list(map(int, answer.split()))
                    correct = answer_array == number_sequence
                    feedback_message = "¡Correcto!" if correct else "Incorrecto"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not memorized:
                # Mostrar la secuencia de números
                show_number_sequence()

    # Dibujar la pantalla
    screen.fill(WHITE)
    if memorized and not correct:
        # Mostrar el cuadro de texto para la respuesta del usuario
        input_box = pygame.draw.rect(screen, BLACK, [120, 120, 160, 32], 2)
        text = font_small.render("Escribe los números aquí:", True, BLACK)
        screen.blit(text, [120, 90])
    if correct:
        # Mostrar el mensaje de retroalimentación
        show_feedback()
    pygame.display.flip()

    # Limitar a 60 FPS
    clock.tick(60)

# Cerrar Pygame
pygame.quit()

