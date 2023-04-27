# Pokemon

## Este juego es una batalla pokemon, en el, el jugador selecciona un movimiento y empieza la pelea. 
## Se gana cuando la vida del enemigo sea 0 o menos y se pierde cuando la vida de tu pokemon sea 0 o menos 

## alcance 
una pelea pokemon, actualmente cuenta con 4 programados Snorlax, Swampert, Blaziken y Decidueye

# como ejecutarlo
Este juego se ejecuta en python3.10 utilizando las librerias: pygame, math, random, time, sys
Ademas este programa usa la fuente Comic Sans MS, leyendola desde el sistema desde la computadora
en caso de no tener la fuente abrir el codigo en un block de notas y cambiar "Comic Sans MS" en las lineas 196 y 197
casi al final del codigo, por una fuente que tenga en su sistema o instalar la fuente en su sistema

para instalar pygame es necesario un venv 
```bash

python3.10 -m venv venv
source venv/bin/activate
pip install pygame
python pigame.py
```
Tambien puede descargar el programa Sublime Text3, el cual se puede descargar desde el siguiente link
(https://www.sublimetext.com/3)
Abrir el codigo en dicho programa y presionar Ctrl + B, respetando la ubicacion de las carpetas y archivos
En caso de querer usar algun pokemon en especifico ir a la linea 173 y cambiar el nombre el pokemon actual por el que se desea usar
Ejemplo pokejugador.Snorlax(), pasaria a ser pokejugador.Swampert()
Aplica igual si quiere que su rival sea diferente, solo que el cambio se hace en la linea 174

# controles para jugar
teclas 1-4: usar movimientos pokemon
tecla 9: ver estadisticas del pokemon del jugador
tecla 0: ver estadisticas del pokemon oponente
