Este es mi juego 2D de plataformas sin terminar.
Lo dividi en 5 archivos distintos para tener un codigo modular

1. Tener python y pygame instalado
2. Descargar los 5 archivos .py 
3. Correr el archivo principal el cual es "Juego.py".
4. A disfrutar mi pequeña demo funcional sin imagenes y animaciones :D

--Juego.py--

    Este archivo solamente importa los demas archivos y da la funcion de correr el juego

--Confi.py--

    Aqui define el tamaño de la ventana, el tamaño de los recuadros grises y ademas podemos modificar el mapa con "X" y espacios para 
    expandirlo a lo largo (A lo alto no esta programado xdd)

--Jugador.py--

    Contiene la clase del jugador la cual tiene los atributos como su forma, el movimiento del jugador como su velocidad, gravedad y salto. 
    Las teclas para poder moverlo A y D para moverse a los lados y W para saltar.

--Nivel--

    Este es la cabeza del juego.
    Donde se termina de formar el mapa, se aplican las colisiones del entorno con el jugador y el movimiento de la camara dependiendo de la cercania delo jugador con los bordes.
