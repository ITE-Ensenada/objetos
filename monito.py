"""Este modulo es para dar a concer nuestro personaje"""
#pylint: disable=too-few-public-methods
class Personaje:
    """Clase que define las estadisticas de tu personaje"""
    personaje1 = "principal"

    def __init__(self, name, lvl, atack, speed, hp):
        self.nombre = name
        self.nivel = lvl
        self.ataque = atack
        self.velocidad = speed
        self.vida = hp

    def presentacion(self):
        """Presenta nuestro personaje con sus estadisticas"""
        print(f"Nombre = {self.nombre}")
        print(f"\nNivel = {self.nivel}")
        print(f"\nAtaque =  {self.ataque}")
        print(f"\nVelocidad = {self.velocidad}")
        print(f"\nVida = {self.vida}")
