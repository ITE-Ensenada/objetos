#"Juego de la serpiente"
import pygame
import turtle
import time
import random

class Snake:
    def __init__(self):
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "stop"
    
    def create_snake(self):
        for i in range(3):
            segment = turtle.Turtle()
            segment.speed(0)
            segment.shape("square")
            segment.color("black")
            segment.penup()
            segment.goto(-i*20,0)
            self.segments.append(segment)
    
    def movimiento(self):
        for i in range(len(self.segments) -1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()

        up = move_up
        down = move_down
        right = move_right
        left = move_left

        # Ajustes de la ventana
        tamanio = (826, 427)
        screen = pygame.display.set_mode(tamanio)
        
        




        if self.move_up == "up":
            self.head.sety(self.head.ycor() + 20)

        elif self.move_down == "down":
            self.head.sety(self.head.ycor() - 20)

        elif self.move_left == "left":
            self.head.setx(self.head.xcor() - 20)

        elif self.move_right == "right":
            self.head.setx(self.head.xcor() + 20)
            #"Movimiento"
    def move_up():
        if self.direction != "down":
            self.direction = "up"

    def move_down(self):
        if self.direction != "up":
            self.direction = "down"

    def move_left(self):
        if self.direction != "right":
            self.direction = "left"

    def move_right(self):
        if self.direction != "left":
            self.direction = "right"



    def add_segment(self):
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("grey")
        segment.penup()
        self.segments.append(segment)

class Manzanita:
    def __init__(self):
        self.Manzanita = turtle.Turtle()
        self.Manzanita.speed(0)
        self.Manzanita.shape("circle")
        self.Manzanita.color("red")
        self.Manzanita.penup()
        self.Manzanita.goto(0, 100)

    def randomize_position(self):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.food.goto(x, y)

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.puntos = 0
        self.mejor_puntuacion = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.actualizar_puntuacion()

    def actualizar_puntuacion(self):
        self.clear()
        self.write(f"Puntos: {self.puntos}  Mejor puntuacion: {self.mejor_puntuacion}", align="center",
                   font=("Courier", 24, "normal"))

    def aumentar_puntos(self, puntos):
        self.puntos += puntos
        if self.puntos > self.mejor_puntuacion:
            self.mejor_puntuacion = self.puntos
        self.actualizar_puntuacion()

    def reset(self):
        self.puntos = 0
        self.actualizar_puntuacion()

    # Ajustes de la ventana


        

            
      

