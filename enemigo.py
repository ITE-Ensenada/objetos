"""Este modulo determina las estadisticas de los enemigos"""
#pylint: disable=too-few-public-methods
class Enemigo:
    """Estadisticas del enemigo"""
    enemigo1 = "debil"
    def __init__(self, atack, speed):
        self.ataque = atack
        self.velocidad = speed
        self.vida = 50

    def contra(self):
        """Muestra las estadisticas del enemigo"""
        print(f"Tu enemigo tiene {self.vida}, su ataque es de: {self.ataque}")
        print(f"y su velocidad de: {self.velocidad}")

class Jefe(Enemigo):
    """Clase hija la cual determina el poder de un jefe"""
    def __init__(self, atack, speed):
        super().__init__(atack, speed)
        self.super = 300
        self.minions = 3
