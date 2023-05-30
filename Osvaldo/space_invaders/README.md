# Space Invaders

## Descripcion del proyecto
Este es un juego arcade desarrollado en Python utilizando la biblioteca Pygame. El objetivo del juego es destruir a todos los enemigos y objetos que se mueven en la pantalla con una nave espacial controlada por el jugador. El jugador tiene una cantidad limitada de vidas y pierde una vida si es golpeado por un enemigo o objeto. El juego termina si el jugador pierde todas sus vidas (Se tiene un total de 4 vidas).

El proyecto cuenta con distintas funcionalidades, como la capacidad de guardar y cargar puntajes maximos a la hora de abandonar el juego, o perder por un game over.

## Requisitos

Este juego fue programado utilizando Python 3.10.6 y Pygame 2.3.0.

Verifique que cuente con estas versiones instaladas en su sistema antes de ejecutar el juego.

## Instalación en sistema operativo Linux, utilizando terminal
    1) Abrir una terminal (Ctrl + Alt + T)
    2) Tener instalado pygame 2.3.0 y Python 3.10.6 y Git para descargar el repositorio, en caso contrario instalar:
        - Python 3.10.6: sudo apt-get install python3.10.6
        - Pygame 2.3.0: pip3 install pygame==2.3.0
        - git: sudo apt-get install git
    3) Clonar el repositorio en algun directorio local. Ejemplo para clonarlo en el escritorio:
        - cd ~/Desktop
        - git clone https://github.com/Grum5/PyGame.git
    4) Entrar al directorio del repositorio clonado e ir a la direccion del archivo main.py del juego:
        - cd PyGame/Osvaldo/space_invaders
    5) Ejecutar el juego desde la terminal con el comando:
        - python3 main.py

## Instalacion en sistema operativo Windows
    1) Tener instalado Git y Python, en caso contrario instalarlos desde las paginas correspondientes:
        - Python: https://www.python.org/downloads/
        - Git: https://git-scm.com/downloads
    2) Abrir el cmd de windows (tecla windows + r, escribir cmd y dar enter)
    3) Instalar pygame 2.3.0 con el comando:
        - pip install pygame==2.3.0
    4) Clonar el repositorio en algun directorio local. Ejemplo para clonarlo en el escritorio:
        - cd Desktop
        - git clone https://github.com/Grum5/PyGame.git
    5) Entrar al directorio del repositorio clonado e ir a la direccion del archivo main.py del juego:
        - cd PyGame/Osvaldo/space_invaders
    6) Ejecutar el juego desde la terminal con el comando:
        - python main.py

## Controles del juego
El jugador puede controlar la nave espacial utilizando las siguientes teclas del teclado:

    W: mover la nave hacia arriba
    A: mover la nave hacia la izquierda
    S: mover la nave hacia abajo
    D: mover la nave hacia la derecha
    Barra espaciadora: disparar un proyectil
