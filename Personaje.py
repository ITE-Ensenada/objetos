# pylint: disable=C0103

''' Modulo personaje:

	Clase personaje(Character)
	Contiene atributos del personaje y un metodo para verificar la salud del mismo

	Clase jugador(Player)
	Esta clase es directamente para el jugador:
	Solo tiene 2 atributos, el segundo que es la edad nos ayudara para:

	- Verificar si es mayor de edad
	- Si es mayor de edad, que pueda jugar al videojuego
	- Y si no, negarle el acceso
'''

class Character:
    '''
    Esta es la clase mas importante:
    contiene todos los atributos del personaje
    un total de 10 atributos, (por el momento solo 
    un atributo tiene un valor por defecto)
    '''
    def __init__(self, name, age, speed, dodge, damage, stamina, strength, height, skin_color):
        self.name = name
        self.age = age
        self.speed = speed
        self.dodge = dodge
        self.damage = damage
        self.health = 20
        self.stamina = stamina
        self.strength = strength
        self.height = height
        self.skin_color = skin_color

    # Metodo para presentar al personaje

    def show(self):
        '''
            Un metodo sencillo, simplemente para presentar los
            atributos de nuestro personaje
        '''
        print("Presentando a: \n" "Nombre: " +
              self.name, "\nEdad: " + self.age, "\n")
        print("Caracteristicas: \n" "Velocidad: " + self.speed,
              "\nSalud: ", self.health, "\nAltura: " + self.height,
              "\nColor de piel: " + self.skin_color)
        print("Habilidades: \n" "Esquiva: " + self.dodge, "\nDaño: " + self.damage,
              "\nEstamina: " + self.stamina, "\nFuerza: " + self.strength)

    def checkHealth(self):

        '''
            El siguiente metodo sirve para cuando
            el personaje sea atacado o caiga en una
            trampa, o reciba algun tipo de herida, el
            jugador reciba una notificacion mediante
            el siguiente algoritmo: 
        '''

        if (self.health < 15) and (self.health > 10):
            print("Salud baja")
        elif self.health <= 7:
            print("Vida:")
            print(self.health)
            print("Curate!")

class Player:
    '''
        Haciendo uso de los atributos name & age:
        Le pedimos ambos (linea 29 y 30) datos al usuario y los leemos para
        crear un decorador (en el modulo main) que nos sirva como validacion
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        